---
title: ! 'Internet Explorer: Global Variables, and Stack Overflows'
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 560
wordpress_url: http://cappuccino.org/discuss/?p=560
date: '2010-03-01'
categories:
- Code
tags: []
---

Every once in a while, you stumble upon a particularly strange bug. A bug that seems to defy the rules of space-time. A bug that makes you pull your hair out for days. A bug that almost certainly includes Internet Explorer. This was one of those bugs for me, and since I haven't found a lot of information out there even now that I know what the problem was, I wanted to write it up for posterity.

It starts with what looks like a relatively benign function, that we'll call recurse:

	:::javascript
	window.recurse = function(times)
	{
	    if (times !== 0)
	        recurse(times - 1);
	}

	recurse(13);

If you pass in the magic number 13 (or anything higher), this recursion is going to fail with our stack overflow pop up. No problem, you say? You've fought Internet Explorer before, and you know how to get down to business. Fire up the trusty IE 8 debugger and get to work! Unfortunately for you, the debugger won't be triggered. Just a pop up for you. If you're feeling extra ambitious, maybe you'll try installing Visual Studio and hooking up the advanced debugger directly to IE; I did. No such luck.

I should mention that the code above wasn't what forced me to investigate this bug. I'm not usually in the habit of writing recursive functions that don't actually do anything. And when your code base is tens of thousands of lines long, and your coworker has pushed a
couple thousand new lines of code (which radically alter the load process), tracking down any problem without a debugger starts to get hairy. At one point in the process, I actually stepped line by line through every single new line of code, certain I'd track down the bug. I didn't, because not only does IE not trigger the normal exception mechanism, it doesn't even report the error until after any waiting script executions are finished. Fun.

Thankfully, [my neighbor](http://joel.franusic.com) works at Microsoft, so I was able to get an inside look into the issue. That's where our test function comes in (thanks Microsoft). Let's get back to it:

	:::javascript
	var recurse = function(times)
	{
	    if (times !== 0)
	        recurse(times - 1);
	}

	recurse(13);
	recurse(10000);

Our new version works. Can you spot the difference? We're using a "local" (but really global considering our current scope) variable here, instead of assigning the function to a property on the window object. This tells us that it has something to do with the window "host" object, but it isn't the whole piece of the puzzle just yet.

	:::javascript
	(function(){
	    var recurse = function(times)
	    {
	        if (times !== 0)
	            recurse(times - 1);
	    }

	    //we won't have access outside to recurse, so add a global ref
	    window.recurse = recurse;
	})();

	recurse(13);

This test also works, and is pretty much the last piece of the puzzle. From this we can see that simply assigning a variable through the window object isn't the problem, the problem is actually recursing through that variable.

In the block above, the recursion is happening through the local var, not the global reference, and so it isn't triggering the bug. To prove that this is the case, let's try the opposite test:

	(function(){
	    var r = function(times)
	    {
	        if (times !== 0)
	            recurse(times - 1);
	    }

	    //we won't have access outside to recurse, so add a global ref
	    window.recurse = r;
	})();

	recurse(13);

Here, we're doing the recursion through the global reference, and as we expected it fails. So, the lesson to learn here is that any recursion that happens through the window object is limited to a stack depth of 12. If there was a tl;dr; to this post, it would be that.

To dig just a little bit deeper into some of the oddities of what's going on here (and how it impacted Cappuccino), you'll want to see this unbelievably strange (but not technically incorrect) behavior:

	window === window;           //true
	window.window === window;    //false

	function global(){
	    return (function(){return this;})();
	}

	global() === window;         //true
	global().window === window;  //false

Technically, the behavior of the window object isn't defined by ECMAScript or any browser standard; it's a native object provided by the browser to the runtime environment. As a result, even though IE's behavior here is strange, and the opposite of all other major browsers, it isn't technically wrong. It's absolutely terrible, though.

Why did we have this problem in the first place? To answer that, you need to know a bit about CommonJS modules. In the CommonJS "spec" modules have their own scope, and don't export their vars as globals to the outside world. Instead, the module loader passes in an "exports" object, and the module author assigns properties to that object. Another way to put it would be to say that the public API of any module has to be explicitly created by assigning methods to the exports object.

In addition to Cappuccino, we're also the authors of Narwhal, the most popular implementation of the CommonJS spec. We've already migrated most of our tools to run on top of Narwhal, and we're continuing to improve the integration between Objective-J and Narwhal. Part of that means changing some of our code to use the exports technique, and using that same code in the browser.

What we ended up with was something like this:

	:::javascript
	var exports = {};
	(function(global, exports){

	    //lots of methods...

	    function objj_msgSend(){
	        //do some stuff;
	    }

	    //lots of exports...
	    exports.objj_msgSend = objj_msgSend;

	    // make exports global
	    for (var export in exports)
	        if (exports.hasOwnProperty(export))
	            global[export] = exports[export];

	})(window, exports)

The final loop assigns the exports to the global scope, since that's how Objective-J code is expected to run. This last step was the cause of all of our problems, because as you can see, we're creating all global methods on the window object, which means all calls to them are going to go through the host object, and be subject to our exceptionally low recursion limit.

Our first fix looked like this:

	:::javascript
    for (var export in exports)
        if (exports.hasOwnProperty(export))
            eval(export +" = global[""+export+""];");

The eval creates a global implicitly, rather than explicitly, which doesn't trigger the trip through the host object. We explored a few different ways to get around the bug, including working with Microsoft, but found no other viable solution.

Rather than ship this code in Cappuccino 0.8, though, we decided to take a step back and re-examine our initial requirements. The desire to strictly adhere to the CommonJS proposal was requiring that our code become more complex and harder to maintain, so we dropped that requirement.

The final version of the code is almost exactly the same, except rather than doing things like `global.foo = function(){}`, we're simply using implicit global creation directly. This is more in line with the way all existing JavaScript runtimes actually work. It's also the way Narwhal works, and probably the way CommonJS _should_ work.

I want to give another thank you to all the folks at Microsoft who helped us track down the problem and provided us with a simple test case that reproduced the problem. They were quite helpful, and we (along with all of our users) appreciate it. Now hopefully we'll see this issue addressed in IE9, along with a faster JavaScript engine :).

**Update:** Re-reading this post a year later, I realize I never made it clear that the issue isn't just recursion. IE won't support _any_ execution stack longer than 12 frames.

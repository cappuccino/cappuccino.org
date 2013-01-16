---
title: On Leaky Abstractions and Objective-J
author: Francisco Tolmasky
author_email: francisco@280north.com
wordpress_id: 159
wordpress_url: http://cappuccino.org/discuss/?p=159
date: '2008-12-08'
tags:
- cappuccino
- objective-j
---

In a [recent post](http://ejohn.org/blog/javascript-language-abstractions/) by John Resig, and in many of the comments, there seems to be the mistaken belief that Objective-J was designed to allow existing Objective-C programmers to write code that runs on the web. It's been compared to GWT, where developers program almost exclusively in Java and are allowed to "circumvent" JavaScript. This however is not the case with Objective-J at all. For starters, Objective-J is simply a language addition to JavaScript, and exists separately from the actual Cappuccino framework (which I'll discuss a little later). It does not directly have anything to do with the DOM or AJAX, etc. The purpose behind Objective-J was to facilitate the development of Cappuccino, and when we originally set out to do that we simply wanted to add a few key missing features to the existing JavaScript "standard". In other words, Objective-J is our take on JavaScript 2.0.

Now, this is usually the point at which someone chimes in that JavaScript is **perfect**, and that I just don't understand it (you know, despite the fact that I've been using it for upwards of 10 years and have worked on its implementation in a major shipping browser). However, I think most people in the community can agree that there are some pretty big holes remaining in JavaScript. JavaScript is being used in increasingly larger projects, and in these projects some of its weaknesses are beginning to show. This is precisely why we have things like the (now dead) ECMAScript 4 proposal, Harmony, and Adobe's ActionScript. And the truth is, had JavaScript 2.0 come around and been widely implemented and supported, we would have built Cappuccino without Objective-J. But the problem is that JavaScript 2.0 didn't come around. I started working on what would eventually become Objective-J and Cappuccino **three years ago**, and in that time there have been no significant improvements or changes to the JavaScript language. Yes, certain browsers have taken it upon themselves to add a few nice features here and there, but for people writing real applications that need to run on most browsers, its simply not practical to rely on them. For the most part, we're writing the same JavaScript today (language-wise at least) that we were 5 years ago. And that doesn't seem like its going to change anytime soon.

### Everybody is writing "abstractions" around JavaScript

And I don't just mean projects like Pyjamas and GWT. I mean **EVERYBODY**, including Prototype, Dojo, and jQuery. Yes, you read correctly, all the major JavaScript frameworks are essentially doing the same thing we are to some degree or another -- we're really not that original. The sole difference between their approach and ours is that when they add new language features to JavaScript, they're not taking the extra step of introducing _new syntax_. Don't believe me? Take a quick look at an example right out of the Prototype tutorials:

	:::javascript
	// when subclassing, specify the class you want to inherit from
	var Pirate = Class.create(Person,
	{
	     // redefine the speak method
	    say: function($super, message)
	    {
	          return $super(message) + ', yarr!';
	    }
	});

What we're seeing here is the introduction of classical inheritance to the JavaScript language. This has always traditionally been a language feature, but due to its absence in JavaScript, the folks at Prototype have chosen to make it a library feature. The important thing to realize here is that it requires as much work to learn about the Class function as it would to learn about a new class keyword. And the same is true of Dojo:

	:::javascript
	dojo.declare("Employee", Person,
	{
	    constructor: function(name, age, currentResidence, position)
	    {
	          // remember, Person constructor is called automatically
	          this.password="";
	          this.position=position;
	    },
	    login: function()
	    {
	          if (this.password)
	               alert('you have successfully logged in');
	          else
	               alert('please ask the administrator for your password');
	    }
	});

Once again, `dojo.declare` might as well be a new keyword since its shoehorning classical inheritance right into JavaScript. The jQuery UI widgets do something very similar to this with the "widget" factory method:

	:::javascript
	$.widget("ui.sortable", $.extend({}, $.ui.mouse,
	{
	    _init: function()
	    {
	           var o = this.options;
	           this.containerCache = {};
	           this.element.addClass("ui-sortable");
	//...

At the end of the day, it doesn't really matter if you're a JavaScript expert, all these libraries have quite the learning curve and if its your first time with any of them, you're going to have be referring to documentation a lot. And that's **not a bad thing**. My point is simply that in JavaScript, more so than anywhere else, libraries need to first define what is essentially a new mini-language before they can begin to do anything useful. This is a bit unfortunate, because it ends up tying language additions to library features, despite there being no necessary connection between the two. This makes it particularly hard to use the different libraries together in an efficient way. Sure, you can use all three in the same project, but there are some clear walls between them since each one decides to do classes a little bit differently. Not to mention the fact that you now have pretty redundant code your site. This is what happens when a language is clearly missing features. Individual frameworks in the .NET, Objective-C, Java, and so forth world don't suffer from core incompatibility in the way they choose to do something as fundamental as defining class hierarchies. This is part of the reason we built Objective-J as its own standalone entity.  If all you want is some of the cool language features that Objective-J adds (without any of the design patterns in Cappuccino) then you can _just_ use Objective-J, there is no "all or nothing" contract.

### OK, so how is Objective-J different?

As we've now seen, there is a general tendency to add language features to JavaScript. Now, in _my personal opinion_, I prefer language features as fundamental as these to be part of the syntax, not part of a library. Let's look at what Objective-J inheritance looks like:

	:::objj
	@import "Animal.j"

	@implementation Snake : Animal
	{
	    Number miceEaten;
	}

	- (String)speak
	{
	    return "hisss!";
	}

	@end


To me this code reads a little more naturally, and at the very least it's no harder to pick up than the numerous library functions required in the other libraries. This approach also has the added benefit of making it absolutely trivial to write new syntax modules so that my text editor of choice can actually know what is going on in my code. You'll also notice that creating a new syntax gives us great flexibility and allows us to add a few nifty features that wouldn't otherwise be possible, such as optional static typing and code importing. But again, this isn't as "out there" as some people would have you believe. It has even more benefits as we'll soon find out, but before we do, let me answer the question that I'm sure many of you are asking right now:

### Why Objective-C style syntax?

 Again, we didn't start off saying "let's port Objective-C"!  In fact, our first versions of Objective-J looked very similar to Java or C++:

	class Snake extends Animal
	{
	    Instance.speak = function()
	    {
	          return "hisss!";
	    }
	}

However, this approach had some serious issues. To better understand them, we have to take a look at what the principal design goals of Objective-J actually were:

1. First off, it **had** to be a strict superset of JavaScript - meaning all existing JavaScript had to work. Believe it or not, we _do like_ JavaScript, and we didn't want to break it or create a trade-off of features.  Not to mention we wanted the existing plethora of libraries to still work.
2. Secondly of course, we wanted to add a number of "key" features.  Some things as crucial as being able to **import code** and built in support for classical inheritance.  We also wanted some features inspired by languages like Ruby, such as method_missing.
3. And lastly, we wanted to keep the ease of use of JavaScript, which meant not adding an extra "compilation" step, but instead allowing developers to still pound out some code and hit refresh and see it run.

The problem with adding language features in a way that would be more "familiar" to most developers, like the Java approach above, is that it would break backwards compatibility with existing JavaScript. This is because a lot of the keywords we wanted to use are actually reserved words in JavaScript, despite not being currently used. There is good reason for this though, because at some point they may actually _mean_ something, and we wanted to make sure Objective-J kept working when JavaScript (finally) got a real update. Of course, we could have just chosen different keywords, like "Class" instead of "class" for instance. This however also breaks backwards compatibility because someone may have used the Class identifier in their code already.

The other problem with this approach is that it made it next to impossible to add harder features like optional static typing or dynamic dispatch of methods (thus allowing for method_missing) without having a full blown compiler. There's no way to "intercept" a method call in JavaScript.  So once again, we were stuck.

Luckily for us however, a group of people ran into these same issues about 25 years ago when trying to improve the C language. These were the folks at Stepstone who developed Objective-C. Just like in our case, Objective-C had to be a strict superset of C (unlike C++ which does NOT always play nice with C). Also lucky for us is that JavaScript syntax is very close to C syntax, so their language additions translated very naturally to JavaScript. And perhaps now it is obvious why our keywords start with the `@` symbol, because in this manner there is no possibility of ever clashing with future JavaScript keywords or predefined user variables and functions. In other words, we can now add to the language as much as we want without the fear of breaking compatibility with existing JavaScript.

Similarly, the new method passing syntax allows us to have firmer control of how messages are sent:

	:::objj
	object.jsMethod();
	[object objjMessage];

This is the famous bracket syntax. What you may not realize is that this makes it perfectly clear when you are using Objective-J style message dispath, allowing us to "hook in" and add things like `method_missing`, etc. There are a whole bunch of other cool things that this enables which are outside the scope of this post, but I encourage you to check out the other [tutorials](http://www.cappuccino-project.org/learn/) on our site to learn about them. All this, **without** breaking any existing libraries and without requiring the user to compile before every run. Pretty impressive for a langauge that is supposedly "completely different" from JavaScript.

### The Part About Leaky Abstractions

On top of Objective-J, we've built the Cappuccino framework, which is designed to help developers write desktop class applications on the web. One of the many things Cappuccino does is "abstract away" the DOM, and I'll get into why we do this in a moment.  But before I do, I think I should take a second to address this whole "leaky abstractions" business, because there seems to be a fair bit of confusion regarding this as well. If you haven't already read it, or even if you have, I recommend you take a look at [Joel Spolsky's original article on the subject](http://www.joelonsoftware.com/articles/LeakyAbstractions.html).

When people refer to this article, it is usually to criticize some "abstraction" because it will "inevitably" be leaky, and then oh boy you better watch out! But this was not Spolsky's thesis. He didn't end the article with "and thus avoid abstractions at all costs". He was not somehow suggesting that we stop abstracting altogether. Quite the contrary, its clear that although these "leaks" are an unfortunate and unavoidable consequence, abstractions are still incredibly worthwhile: hence the conundrum. In every single example given in the article, it was never implied that the abstraction was somehow bad or invalid because of its leak: just because certain SQL queries are slow doesn't mean you should manually read in tab delimmeted files and scan them yourself. Just because TCP can fail if you unplug your computer doesn't mean you should do IP transfers yourself. It just turns out that, big surprise, nothing is perfect. Joel put it best himself:

> Indeed, the abstractions we've created over the years **do** allow us to deal with new orders of complexity in software development that we didn't have to deal with ten or fifteen years ago, like GUI programming and network programming.

And the truth of the matter is that the problem of leaks is overstated. I find it particularly hilarious when JavaScript programmers bring this up, since JavaScript, being a garbage collected _dynamic_ _**interpreted**_ language, is quite possibly one of the biggest abstractions of all. And yet, most of us can see that the benefits of JavaScript far outweigh the "leaks". I think few JavaScript programmers have had to learn "the whole stack" once they've encountered one of JavaScript's many leaks, whether it be performance issues (from being interpreted) or perhaps large memory consumption (from being improperly garbage collected in some browsers). No one has had to go and open up WebKit's source code to figure out these problems. Most of the time you simply Google your concern and learn the workaround. Not that big a deal.

Leaks are just something we all have to learn to deal with in every facet of programming, because programming **is** abstraction. Abstraction is basically all programmers ever do, from pushing electrons across a wire, to turning C into assembly, to interpreting JavaScript in your browser, every step in computer science has been an exercise in abstraction. There is nothing inherently wrong with abstraction. I can understand if someone disagrees with a particular abstraction for well defined reasons, but simply waving your hands and referring me to the law of leaky abstractions is not a valid argument.

To suggest that we shouldn't abstract because of Joel Spolsky's Law that all abstractions are inherently leaky is to suggest that we shouldn't debug because of Murphy's Law that all code will remain inhrerently buggy.

### Back to Cappuccino and the DOM

Cappuccino doesn't just abstract away the DOM, it abstracts away HTML, CSS, VML, the JavaScript DOM API, etc. Why? Because as you can see there are just too many technologies with overlapping responsibilities. It's never really clear whether you should create a button in HTML or in JavaScript code, and whether you should style it in a CSS files or apply styles manually in JavaScript, or whether you should just use Canvas to draw everything. Not to mention that on top of having to sort through all these technologies, you have the additional challenge of having to accomodate for every slightly different flavor that exists in every browser. Sometimes its relatively simple, but othertimes it can be quite complex, as is the case with Canvas and VML. The other problem is that these technologies were simply not originally designed to handle the tasks they are now performing.  HTML was designed for laying out documents, not creating applications.

We look at these technologies completely differently. To us, HTML, CSS, Canvas, the DOM, etc all represent the "rendering engine" of the web, in the same way that graphics cards are the rendering engines for your computer. It's too difficult to learn the intricacies of every graphics card on the market, so developers instead use technologies that hide these details like OpenGL. In the same way, Cappuccino defines a common way to "draw" for the web. Internally, it figures out whether its more efficient to make a div, or draw to a canvas, or use VML. This is a fantastic time saver today, because it allows Cappuccino to worry about things like performance and allows you to just get a button on the screen. But its going to be even better as time goes on. This is not only because the underlying code will get better, but because web applications today look like this:

> ![](/img/cpo-uploads/2008/12/webapps1.png)

But tomorrow, when enough browsers finally support SVG, they may look like this:

> ![](/img/cpo-uploads/2008/12/webapps2.png)

Or, for all we know, like this:

> ![](/img/cpo-uploads/2008/12/webapps4.png)

The important thing is that when this happens, and it _will_ eventually happen, people who invested heavily in todays technologies will have to spend a great deal of effort updating, but we will just swap out the guts of Cappuccino and your code will inherit the benefits of SVG or whatever new technology is out there.

### Conclusion

To me what we've done with Objective-J and Cappuccino seems inevitable. Even the most conservative major JavaScript libraries can't get away without adding features to the language, and we've simply taken the next logical step with Objective-J. Similarly, Cappuccino is a tool that allows you to stop thinking about web pages and browser incompatibilities, and instead focus on the complex problems presented by the challenge of creating full-on applications on the web. As we've said [countless](http://www.cappuccino-project.org/discuss/2008/10/21/web-pages/) [times](http://www.cappuccino-project.org/learn/), Cappuccino isn't for everything. All of this abstraction isn't necessary if you're simply trying to add dynamic elements to a site like bankofamerica or digg. Cappuccino is for building rich applications in the browser, a small minority in the web world today. We believe that this is where things are headed, and we designed Cappuccino specifically to get _us_ there.

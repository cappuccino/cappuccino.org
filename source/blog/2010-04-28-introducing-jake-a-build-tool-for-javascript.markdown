---
title: ! 'Introducing Jake: A Build Tool for JavaScript'
author: Francisco Tolmasky
author_email: francisco@280north.com
wordpress_id: 660
wordpress_url: http://cappuccino.org/discuss/?p=660
date: '2010-04-28'
tags:
- tools
- jake
- rake
---

Now that we've [shipped Cappuccino 0.8](http://www.cappuccino-project.org/discuss/2010/04/07/cappuccino-0-8/), I wanted to take some time to describe in more detail what might be one of the most exciting new features our users may not even notice: [Jake](http://github.com/280north/jake). Jake is a new build tool built entirely in JavaScript that runs on top of the CommonJS standard. As its name suggests, it is based on the existing and already popular Rake tool and benefits from the same simplicity.

### Since when does JavaScript need to be built?

Well, JavaScript doesn't _need_ to be built, but if you look at almost every major library, you'll notice all of them ship in some sort of built or "compiled" state. That's because despite being an interpreted language, there is still plenty JavaScript can gain in the form of optimizations from a build phase. You can concatenate all your code into one file, minimize it, remove dead code, sprite the images associated with the code, and do all sorts of other interesting things that at the end of the day result in a faster web site for your users.

So the concept of building JavaScript is not new in any way. Jake is just a new tool that can help you do all this in a language that's probably already familiar to you. But before I get into how to use Jake, I'd like to explain the need for such a tool when clearly people are already doing this with non-JavaScript alternatives.

### A brief history of build tools used by Cappuccino

Jake is actually the third build tool we've used for Cappuccino since we started the project. Like many current JavaScript projects, Cappuccino used to use tools borrowed from other environments.

When we originally shipped Cappuccino, we used a combination of [Apache Ant](http://ant.apache.org/) and some custom built JavaScript tools. Our goal has always been to minimize the friction a user experienced when trying to build Cappuccino from scratch, and thus at the time Ant seemed like a good solution since it is cross platform and many people already have it installed with their Java distributions. Ant also let us call into JavaScript with a little bit of legwork. However, the problems with using Ant soon outweighed the benefits. Ant may be a great fit for Java projects since it was designed for that purpose and many of the build commands are tailored specifically for Java, but using it to build non-Java projects can sometimes be an incredibly frustrating ordeal. For starters, Ant uses XML configuration files, which means that performing simple logic can sometimes be quite a daunting task. Java programmers probably don't notice this because Ant is smart enough to "understand" Java dependencies out of the box, but it had no idea how to deal with our JS files in anything but the most rudimentary way. The solutions usually involved using custom-built extensions which somewhat defeated the purpose of using Ant for its existing install base and portability.

As we tried to do increasingly complex operations during our build process, it became evident that Ant was no longer going to cut it, and so I set out to search for a new tool to replace it. I looked at a number of different options (even briefly trying make -- bad idea), but one tool really stood out for me: Rake.

I think [Rake](http://rake.rubyforge.org/) is quite possibly the first build tool that I haven't ended up hating. In fact, I really like Rake. One of the best parts about Rake is its simplicity: it chose to use Ruby itself instead of defining a configuration file format. That means that there's really no "build" mindset you have to get into, and at the end of the day you're just writing a really simple program. If at any point you need to do something out of the ordinary in your build process, you can always just code it. There's no need to invent a new configuration property or hassle with trying to find some obscure "right" way to do things: you can just code it. Strangely enough, Rake also has the most intuitive built-in commands I have ever used. Creating dependencies is a breeze, and it is smart enough to handle things like cleaning a project very elegantly for you. If you've never tried Rake, you really should.

### So why not stick with Rake?

Moving to Rake was a really great decision at the time, but Rake unfortunately had one problem that eventually got to us: it had to be written in Ruby. This is not a problem per se of course, and the truth is that Ruby is one of the reasons Rake shines. The DSL Ruby allows in Rake makes it truly a joy to use, but the unfortunate fact is that many our users simply don't know Ruby, so interacting with the build system could prove difficult to them. This resulted in a number of problems:

1. Users didn't like having to install Ruby gems to build Cappuccino from scratch.
2. On top of the occasional Rhino bug, we now had to deal with Ruby incompatibilities across distributions and versions which were very difficult for us to deal with effectively as this was not our native environment.
3. Users were afraid to submit patches to the build scripts because they weren't as knowledgable in Ruby.
4. Users were afraid to innovate in the build space for the same reason.
5. Users were less likely to use our optimization tools, because again, it required using the Ruby build process, installing gems, etc.
6. Since our product and our build tools were written in different languages, we were incapable of easily sharing code between the two. We had to jump through a lot of hoops to call JavaScript from Ruby (usually through Rhino), which resulted in pretty slow builds.

So all in all, while Rake provided a pretty good "out of the box" experience for our users and contributors, it meant they were really stuck when something went wrong, and that they were not as capable of fixing or improving it. This is a pretty general problem in the JavaScript space I feel. You'll notice that a lot of the work of "optimizing" and deploying JavaScript usually takes place in a different language. For example, most JavaScript compressors are written in Java. This is really unfortunate, because it creates an artificial rift between JavaScript programmers and the people trying to make their JavaScript really fast. One of our goals for Cappuccino 0.8 was to remedy this because we felt that there was still a tremendous amount left to be done in the JavaScript and web application optimizations, and we wanted all the help we could get.

### Jake

Luckily for us, things had really changed since we originally shipped Cappuccino. Most importantly, there is now a real standard for running JavaScript on the command line: CommonJS. Recall for a moment that when we originally shipped Cappuccino, doing something a simple as reading a file in JavaScript was still an open question! At the time the best solution was to use Rhino and drop down to Java APIs. Not only was this slow, it was completely unportable to the other JavaScript engines that would come along like JavaScriptCore and V8. But with CommonJS around, it was now finally viable to write command line scripts in JavaScript.

So with these tools in hand we set out to write [Jake](http://github.com/280north/jake): a JavaScript port of Rake. Again, we really liked Rake, so the goal was simply to expose the functionality of this tool to JavaScript. This ended up turning out quite well for us, because we didn't have to worry about inventing a new build tool. The result is that most Rakefiles can be trivially "ported" to Jake, so a lot of the existing JavaScript projects that currently use Rake can quickly transition over.

Let's quickly take a look at how to create build tasks with Jake:

	:::javascript
	var task = require("jake").task;

	task ("log", function()
	{
	    print("hey there!");
	});

That's all there is to it. You simply call the task function, give it a name, and a closure that contains task's instructions. If you want to set up a dependency, say on two other tasks, you can do so as well:

	:::javascript
	task ("log", ["task-one", "task-two"], function()
	{
	    print("hey there!");
	});

Now, log will first make sure to execute task-one and task-two before executing. If you've used Rake, this should look really familiar. Here is the same task in Rake for comparison:

	:::javascript
	task :log => [:task-one, :task-two] do
	    echo "hey there!"
	end

Jake also includes a host of tools to make dealing with files super easy. This is how you would make sure to generate a new concatenated and compressed file every time you edit one of your original source files:

	:::javascript
	var shrinksafe = require("minify/shrinksafe"),
	    read = require("file").read,
	    write = require("file").write,
	    filedir = require("jake").filedir,
	    FileList = require("jake").FileList;

	filedir ("build/compressed.js", new FileList("*.js"), function()
	{
	    var result = "";

	    (new FileList("*.js")).forEach(function(filename)
	    {
	        result += shrinksafe.compress(read(filename));
	    });

	    write("build/compressed.js", result);
	});

So what we're doing here is creating a task for our "build/compressed.js" file. The filedir task is nice enough to create the intermediate "build" directory for us (if you don't want this behavior, you can use the file task instead). This task will only run any time one of the files in our project with the ".js" extension changes. So, if you don't change any code, this task is skipped. The FileList object takes globs and is iterable, so when this task is called, it simply iterates over each of these files, reads them, compresses them, and writes out the concatenated result. Pretty easy. The best part is that since CommonJS supports a bunch of compressors, its really easy to write a task that uses whichever one generates the smallest file size:

	:::javascript
	filedir ("build/compressed.js", new FileList("*.js"), function()
	{
	    var smallest = null,
	        compressors = ["minify/shrinksafe", "minify/closure-compiler"];

	    compressors.forEach(function(compressor)
	    {
	        var result = "";

	        (new FileList("*.js")).forEach(function(filename)
	        {
	            result += require(compressor).compress(read(filename));
	        });

	        if (!smallest || result.length < smallest.length)
	            smallest = result;
	    });

	    write("build/compressed.js", smallest);
	});

### Already in use

This isn't a toy, we are actively using this as our only build system in Cappuccino. That means you can check out some pretty sophisticated examples by taking a look at the [Cappuccino source code](http://github.com/280north/cappuccino/), or by talking to anyone who has shipped a Cappuccino project. Just ask to see their Jakefiles. If you already have a CommonJS platform installed, you can get jake by just using the tusk package manager:

	tusk install jake

If not, you can head on over to [narwhaljs.org](http://narwhaljs.org) and download narwhal to get started writing JavaScript on the server and command line. Alternatively, you can download the Cappuccino source code and run our bootstrap script, which not only installs narwhal for you, but also custom tailors your installation to use the fastest JavaScript engine available for your machine that narwhal supports (this means that if you're on a Mac you'll get the super fast JavaScriptCore engine instead of the quite slow default Rhino one):

	$ git clone git://github.com/280north/cappuccino.git cappuccino
	$ cd cappuccino
	$ ./bootstrap.sh

If you do this you'll also be able to checkout out some of the cool extensions to Jake specifically for Cappuccino projects. We've created the bundle, framework, and app tasks that completely put together your project for you (similar to the gem tasks in Rake). These tasks implement some pretty cool optimizations, like our [automagic image spriting](http://www.cappuccino-project.org/discuss/2009/11/11/just-one-file-with-cappuccino-0-8/). If you're having any trouble, feel free to jump in our [IRC room](irc://irc.freenode.net#cappuccino) so we can answer your questions or comments on how to get set up building your projects with jake.

You can of course also [get the source code](http://github.com/280north/jake) as well and submit patches or [file bugs](http://github.com/280north/jake/issues):

	$ git clone git://github.com/280north/jake.git

Perhaps one of the coolest results of this is that Cappuccino is really now self-hosting: **the entire stack is finally JavaScript** and easily accessible for hacking.

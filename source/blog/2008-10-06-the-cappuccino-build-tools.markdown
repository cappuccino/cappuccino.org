---
title: The Cappuccino and Objective-J Build Tools
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 41
wordpress_url: http://cappuccino.org/discuss/?p=41
date: '2008-10-06'
categories:
- Cappuccino
- Tutorials
- Tools
tags:
- Cappuccino
- build tool
- Objective-J
---


_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

This article is a high level overview of the current Cappuccino and Objective-J build tools. Subsequent posts will cover each tool in more detail.

One of our primary design goals with Cappuccino and Objective-J was to keep the simple development cycle web developers are used to: edit your code, save, refresh the browser. At the same time we wanted to add powerful language features to JavaScript without requiring the user install a plugin like Flash or Silverlight. At first glance it seemed like only two of these three requirements could be satisfied simultaneously, until we had the key realization that we could simply write our compiler in JavaScript itself, and perform the compilation at runtime on the client.

In reality the Objective-J "compiler" is more like a preprocessor, performing a relatively simple transformation from Objective-J code to JavaScript code, which is then interpretted by the browser's native JavaScript engine. We don't do full parsing and compiling, nor do we have a separate interpreter on top of JavaScript. The result is that the compiler and resulting code run very fast.

This turned out to work great. Simply [download the starter package](http://www.cappuccino-project.org/starter), load index.html in your browser, and start editing away! If you're just getting started with Objective-J and Cappuccino you don't even need to worry about the build tools, they're entirely optional.

When it comes time to deploy your application you may want to optimize it. There's no reason for your customers to wait any longer than necessary, even if the overhead is minimal. That's where the build tools come in. Each tool has a specific purpose, and they all work together to produce an optimized Cappuccino application:

* **objjc** - the Objective-J compiler
* **steam** - a general tool for managing the build process, creating new Cappuccino applications, etc.
* **press** - code stripping and other optimizations
* **bake** - deployment tool

### objjc

 At the lowest level is "objjc", the Objective-J compiler. It's equivalent to gcc or javac, except it converts Objective-J code to JavaScript. Because we can run the same JavaScript code in the browser and [Rhino](http://www.mozilla.org/rhino/) the core of objjc is identical to the in-browser compiler.

[](/img/cpo-uploads/2008/10/objjc.png)[![](/img/cpo-uploads/2008/10/objjc1.png)](/img/cpo-uploads/2008/10/objjc1.png)

Currently objjc's implementation is closer to a simple preprocessor than a compiler, much like the original Objective-C compiler was implemented as a preprocessor on top of C. The preprocessor simply looks for the few Objective-J syntax additions and replaces it with the raw JavaScript equivalent. A big reason this is possible is that Objective-J is a strict superset of JavaScript, thus all JavaScript code is valid Objective-J code.

Typically you don't call objjc directly, but rather let steam manage the build process.

### steam

 Next up is steam, which is the main Objective-J and Cappuccino build tool. Currently it serves two purposes: "steam build" (similar to Xcode's "xcodebuild") and "steam create" (similar to Ruby on Rail's "rails" command).

"steam build" runs the compilation process on an entire application or framework and outputs a single ".sj" file, vastly decreasing the number of HTTP requests required to load an application. These ".sj" files are archives of the compiled input ".j" files, along with information detailing each file's required imports. This allows the Objective-J loading system to efficiently and asynchronously load a large application.

[](/img/cpo-uploads/2008/10/steam.png)[![](/img/cpo-uploads/2008/10/steam1.png)](/img/cpo-uploads/2008/10/steam1.png)

"steam create" copies all the files required for a new project to the directory specified.

### press

 The "press" tool takes in a full application and attempts to determine which code files are unecessary. It then strips those files and writes the results to another directory. This could be thought of as a "linker" though it works very differently than a traditional linker. On a simple project it will reduce the AppKit and Foundation frameworks size by approximately 30%, and we expect further improvements.

[](/img/cpo-uploads/2008/10/press.png)[![](/img/cpo-uploads/2008/10/press1.png)](/img/cpo-uploads/2008/10/press1.png)

Optionally, it can run the [pngcrush](http://pmt.sourceforge.net/pngcrush/) utility on all your png graphics, attempting to reduce their size. Eventually press will also automatically sprite images, further reducing the number of HTTP requests required to load your images.

### bake

 Finally, we have "bake", the Cappuccino deployment tool (like ["Capistrano"](http://www.capify.org/) but specialized for Cappuccino applications). Bake orchestrates all the above tools to produce, and optionally deploy, a highly optimized Cappuccino application. First it can pull both Cappuccino and your application code from git, svn, or a local or remote directory via rsync.

[![](/img/cpo-uploads/2008/10/bake1.png)](/img/cpo-uploads/2008/10/bake1.png)It then copies pieces of the various "checkouts" to the "products" directory, first running a build process like "steam" or ant, if specified. For example, it can run steam on your application code, and copy the results to the product directory, then do the same for AppKit and Foundation, copying the results to the Frameworks/AppKit and Frameworks/Foundation directories to build the complete application.

Once an application is assembled, bake can run "press", optimizing the application's size.

Then bake sets up a directory structure and index.html file which allows for several important tricks: aggressive caching, keeping the client application in sync with the server backend, and atomic deployments, all while preserving a single user-facing URL for the application.

Finally, the application is archived and gzipped, scp'd to one or more servers, and atomically deployed to the specified path(s).

### Conclusion

Cappuccino's build tools are great at optimizing your deployed application, but there are further web server specific optimizations possible as well, including enabling [gzipping](http://httpd.apache.org/docs/2.0/mod/mod_deflate.html) and caching. These will be discussed in subsequent articles.




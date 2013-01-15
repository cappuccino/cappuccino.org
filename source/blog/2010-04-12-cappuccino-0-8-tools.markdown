---
title: Cappuccino 0.8 Tools
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 601
wordpress_url: http://cappuccino.org/discuss/?p=601
date: '2010-04-12'
tags:
- cappuccino
- tool
---

Cappuccino comes with a comprehensive set of tools for developing, debugging, optimizing, and deploying your Cappuccino applications. Those who have been following Cappuccino since the 0.7 release will notice some changes in the tools. The most important being that Cappuccino's tools are now written entirely in JavaScript and Objective-J.

The 0.7 release used [Rake](http://rake.rubyforge.org/), a Ruby build tool similar to "make", to manage the build process of Cappuccino applications, as well as Cappuccino and Objective-J itself. In an effort to speed up the tools, reduce the number of dependencies, and allow us to focus on a single language family, we have replaced the Rake dependency with a simple port of Rake for JavaScript, aptly named [Jake](http://github.com/280north/jake). Since Jake is written in JavaScript, other JavaScript and Objective-J build tools like the Objective-J compiler can run within the same process, speeding up the build time significantly.

Additionally, we have expanded the command-line/server-side JavaScript environment used for Cappuccino's tools, now available as a separate project called [Narwhal](http://narwhaljs.org/). Narwhal aims to support the emerging [CommonJS](http://commonjs.org/) module and standard library specifications on multiple JavaScript engines.

We started working with the [Rhino](http://www.mozilla.org/rhino/) engine, since the existing build tools were built on Rhino, and have recently added support for the JavaScriptCore / SquirrelFish engine. The performance of Narwhal on JavaScriptCore is an order of magnitude faster than Rhino, vastly improving build times. Currently "narwhal-jsc" supports Mac OS X, but other platform support is in progress.

Another major change was the refactoring of the ["press"](https://github.com/cappuccino/cappuccino/wiki/press) tool, which attempts to strip unnecessary files from your application bundle. As part of that refactoring we moved the "--flatten" feature, which inlines all code and files into one or more JavaScript files, into a separate tool, unsurprisingly called ["flatten"](https://github.com/cappuccino/cappuccino/wiki/flatten). Flatten now supports splitting your application into multiple files which will be downloaded by the browser in parallel, via the "--split N" option.

For more information on all of these tools, check out the [Tools](https://github.com/cappuccino/cappuccino/wiki/tools) wiki page.

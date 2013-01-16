---
title: ! 'GitHub Issues Cappuccino App: Desktop and Web'
author: Francisco Tolmasky
author_email: francisco@280north.com
wordpress_id: 803
wordpress_url: http://cappuccino.org/discuss/?p=803
date: '2010-05-13'
categories:
- Uncategorized
tags: []
---


To showcase our new [NativeHost](http://www.cappuccino-project.org/discuss/2010/05/13/nativehost-run-your-cappuccino-applications-on-the-desktop) technology, we're proud to announce the brand new GitHub Issues App, written entirely in Cappuccino and available for both desktop and web:

[![](/img/cpo-uploads/2010/05/tryitonline.png)](http://githubissues.heroku.com/)

[![](/img/cpo-uploads/2010/05/downloadit.png)](http://download.cappuccino.org/Issues-1.0.zip)

The online version is running on Heroku's Node.js beta at [http://githubissues.heroku.com](http://githubissues.heroku.com). If you're already using GitHub's Issue tracking feature, then this app will work for you right out of the box. Simply type in your repo's identifier (username/reponame), and we'll fetch all the issues for you. You can also log in with your GitHub account to access private repositories.

### Open Source

 The GitHub Issues app was put together by some truly excellent members of the Cappuccino community, and we're open sourcing it so that it can serve as an example of how to build and architect a full blown application with Cappuccino and [Atlas](http://280atlas.com).

[![](/img/cpo-uploads/2010/05/atlas-cat.png)](/img/cpo-uploads/2010/05/atlas-cat.png) If you don't have Atlas you can still build the app using the [Jakefile](http://www.cappuccino-project.org/discuss/2010/04/28/introducing-jake-a-build-tool-for-javascript/) in the repo, but you will need Atlas to edit the visual interface files. You can find the source code at [http://github.com/280north/issues](http://github.com/280north/issues). So don't just use it, clone it, patch it, and of course, [file bugs](http://githubissues.heroku.com/#280north/issues)!

### Cappuccino, NativeHost, Heroku, Node, Oh My!

 This app uses and integrates a tremendous amount of new and exciting technology. If you take a look at the source you should find examples on how to do everything from setting up a server to talk to Cappuccino, to optionally deploying your app to the desktop, to talking to other JavaScript libraries:

* We use our brand new [NativeHost](http://www.cappuccino-project.org/discuss/2010/05/13/nativehost-run-your-cappuccino-applications-on-the-desktop) technology which allows the app to run both on web and desktop.
* We make extensive use of the new tableview component, added in version 0.8
* We integrate with [markdown](http://github.github.com/github-flavored-markdown/scripts/showdown.js) and [mustache.js](http://github.com/boucher/mustache.js) and show you how to intermingle Cappuccino chrome with HTML pages.
* In web mode we use [node.js](http://nodejs.org/) running on [Heroku's new Node Beta](http://blog.heroku.com/archives/2010/4/28/node_js_support_experimental/).
* We of course use the awesome [JSON GitHub Issues API](http://develop.github.com/p/issues.html).
* We lay out almost all our UI code visually in [Atlas](http://280atlas.com).

 If you'd like to help improve the app, or just have questions about the code, make sure to get in touch with us and the rest of the Cappuccino community [in the IRC channel](http://www.cappuccino-project.org/discuss/list.php) or [on the mailing list](http://www.cappuccino-project.org/discuss/list.php)

### Thanks!

 I wanted to thank everyone who helped bring this app together, including the fantastic guys at the [GitHub](http://github.com) and [Heroku](http://heroku.com/), and of course [Randy Luecke](http://github.com/me1000/) and [Ludwig Pettersson](http://github.com/luddep) who actually did the hard work of putting this thing together.


---
title: ! 'NativeHost: Run your Cappuccino applications on the desktop'
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 759
wordpress_url: http://cappuccino.org/discuss/?p=759
date: '2010-05-13'
tags:
- tools
---


Today we're adding an exciting [new open source component](http://github.com/280north/cappuccino/tree/master/Tools/NativeHost) to the repertoire of Cappuccino tools. If you've checked out out any of the [Atlas](http://280atlas.com/) betas, you're probably aware that they're distributed as a desktop application. What you may not know is that despite this, Atlas is still itself a full fledged Cappuccino application (written in Atlas no less). Atlas has had the ability to create both web and desktop applications from the start, requiring nothing but the click of a button:

[![](/img/cpo-uploads/2010/05/atlas-desktop-native.png)](/img/cpo-uploads/2010/05/atlas-desktop-native.png) The way we've accomplished this is with a technology we call [NativeHost](http://github.com/280north/cappuccino/tree/master/Tools/NativeHost). NativeHost allows you to take existing Cappuccino applications and with no additional work target them for the desktop. It accomplishes this with an incredibly small and lightweight wrapper around the WebKit browser engine. In this respect, it is similar to a number of existing technologies, including [Adobe AIR](http://www.adobe.com/products/air/) and [Titanium](http://www.appcelerator.com/), but that's where the similarities end.

### Why deploy to the desktop?

 We believe that applications are moving to the web, but as things stand today, there are still some valid use cases for choosing to distribute a downloadable executable. By allowing you to seamlessly deploy to both desktop and web, we hope to remove one of the blockers keeping people from choosing HTML5 as their next target environment. There are a number of scenarios in which you might decide that the desktop currently fits your needs better:

* When your application needs access to the local filesystem or other native APIs not available to web applications running in browsers.
* When you need enhanced offline access.
* When your target users work in an environment that does not trust the cloud yet (providing a downloadable and not using any web buzz words goes a long way here).
* When you need integration with OS features like the taskbar, dock, application switcher, etc.

 This is actually precisely why we created this technology. We were originally planning on releasing Atlas as a cloud-based IDE, but soon discovered our users were much more comfortable currently running it as a desktop app. With NativeHost, we can fulfill these needs today, but switch to the web in the future. Whatever your reasons are, NativeHost aims to provide the best solution for Cappuccino applications.

### Why NativeHost?

 Before creating NativeHost, we evaluated a number of existing solutions but found that they all suffer from either or both of two major drawbacks:

* Many tools require modification to the existing web app to work on the desktop, or worse, require you to target this environment from the beginning. They aren't really about making web apps works well on the desktop, but rather for creating desktop apps using web technologies. We see this as the worst of both worlds: creating an application that can't currently take advantage of all the native platform's advantages, which simultaneously will require a lot of extra work to deploy on the web.
* The flip side to this is tools that provide only a very thin layer around your web app and thus hardly feel native at all.

Again, we feel that the ultimate distribution platform is the web, and that the desktop is almost a transitional necessity today. So with that in mind, we certainly didn't want to create a tool that required adding a bunch of new API that won't work online. However, we also wanted an experience that truly felt good on the desktop. NativeHost is able to accomplish this because it is so tightly integrated with Cappuccino. It provides a seamless experience to both the application developer and end user. The goal is to have any existing Cappuccino app _just work_ on the desktop without requiring any new code. This is manifested in an increasing number of integration points:

* The Cappuccino "main menu" automatically populates the native Mac OS X menu bar. On other platforms it will do what is expected by users on that platform. For example, in a Windows version of NativeHost the menu would be attached the top of individual windows.
* Cappuccino windows (CPWindow) automatically become "native" windows. In the browser Cappuccino windows are typically drawn inside the main browser window. In native host they become real operating system level windows that can be minimized, etc.
* Secure access to the native file system without new API: use existing methods like XMLHttpRequest.
* Cappuccino's document architecture is integrated with the operating system.
* Operating system open/save panels are used.
* Just like any native application your application can register itself to open specific file types. When the operating system requests that your application open a document that information is passed on to Cappuccino for your application to handle.

### Getting up and running with NativeHost

 The easiest way to try out NativeHost is with&nbsp;[Atlas](http://280atlas.com/). Open or create an application, select "Native Desktop" from the "Platform" menu, then press the "Build and Run" button. This will build and launch the current application using NativeHost.

We've also recently added support for NativeHost to the Cappuccino build tools. If your "Jakefile" does not contain tasks for "desktop" or "run-desktop" you can copy them out of a freshly generated project's Jakefile (changing the application name where necessary).

Once you have an application with an updated Jakefile simply execute "jake run-desktop" within the project's directory to build and launch the application using NativeHost.

NativeHost has some additional features, like the ability to start a webserver in the background to handle tasks using APIs not exposed to WebKit. We'll talk more about these features in a future post.

Currently NativeHost supports Mac OS X, but we're working on other platforms.&nbsp;If you're experienced with developing native applications on other platforms and interested in helping out, feel free to get in touch.

If you have any problems using NativeHost, the Cappuccino community will happily help you out. Join us [in the IRC channel](http://www.cappuccino-project.org/discuss/list.php),&nbsp;[on the mailing list](http://www.cappuccino-project.org/discuss/list.php), or [file a bug](http://github.com/280north/cappuccino/issues).




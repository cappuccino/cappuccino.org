---
title: Cappuccino 0.7 Now Available
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 314
wordpress_url: http://cappuccino.org/discuss/?p=314
date: '2009-05-20'
categories:
- Cappuccino
- Releases
tags:
- Cappuccino
- Objective-J
- Rake
- nib2cib
- Aristo
- Sofa
- open source
- Narwhal
---


We're pleased to announce the immediate release of [Cappuccino 0.7](/download/), the latest update to the Cappuccino web framework. This release has been five months in the making, and it marks a significant step forward for the project.

### 0.7 By The Numbers

As of version 0.6, Cappuccino had 9 total contributors. Version 0.7 more than triples that number with 29 total contributors. And thanks to the inspiration and hard work of [Xavier Noria and Jos&eacute; Espinal](http://weblog.rubyonrails.org/2009/5/18/new-code-contributor-index), we've got a slick new website that keeps up to date tallies on all of the [contributors](http://contributors.cappuccino.org/contributors) to the project. Check it out [here](http://contributors.cappuccino.org/contributors). If you find a mistake, be sure to let us know in the comments.

![contributors](/img/cpo-uploads/2009/05/contributors.jpg)

This release includes over 100 bug fixes, thanks in part to all the new contributors, and to the hard work of users taking the time to file quality bug reports. If you hadn't noticed already, we've moved to github's new [issue tracking](http://github.com/280north/cappuccino/issues) for bug reports, so check out the new system, and vote on issues that are important to you.

### New Look

[![aristo](/img/cpo-uploads/2009/05/aristo.png)](/images/Aristo.jpg)

The biggest new feature of Cappuccino is our new new theme: Aristo. Aristo is the new look and feel for Cappuccino applications. Created by the talented designers at [Sofa](http://madebysofa.com), Aristo is designed specifically to look good in the browser, and in any browser, whether it's Firefox, Safari, or even Internet Explorer, Mac and Windows. We've also [open-sourced](http://github.com/280north/aristo/tree/master) the PSD file used to create Aristo. All the controls have been updated to use the new style, and we've added a few new controls as well, like checkboxes, radio buttons, and segmented controls.

### Theming

We didn't just build one new look for Cappuccino, though. Instead, we built an entirely new theme engine which will let anyone create a theme for Cappuccino. All the properties of the standard controls are fully themeable in all the different "theme states" (like "pushed", "disabled", "normal", etc.). In the coming months, we'll be sharing new themes with the community, and building a site for users to post their own themes for others to download and use.

### Interface Builder

Those of you who come from a Cocoa background are used to using Apple's [Interface Builder](http://developer.apple.com/tools/interfacebuilder.html) tool to layout your Cocoa applications. Thanks to a technology in 0.7 called [nib2cib](http://wiki.github.com/280north/cappuccino/nib2cib), you can use Interface Builder to layout Cappuccino applications too. All of the classes supported in Cappuccino 0.7 that have Cocoa analogues are included. So, you can drag checkboxes, sliders, text fields, buttons, and lots more. You can even instantiate custom top level objects, or custom view subclasses, which will be converted to the right class in Cappuccino by the nib2cib tool. Once you're done laying out the UI of your application with Interace Builder, you can use it's target-action and outlet technology to build up its logic as well.

![making a cappuccino application using interface builder](/img/cpo-uploads/2009/05/temp-image_1_72.png)

[nib2cib](http://wiki.github.com/280north/cappuccino/nib2cib) is a powerful tool that drastically reduces the amount of code you need to write to build an interface with Cappuccino. The starter package now includes both a nib/xib based application template, and a standard, code based template, so you can choose which is best for you. From the command line you can use the new [capp](http://wiki.github.com/280north/cappuccino/capp) tool to generate a nib/xib project by typing "capp gen -t NibApplication MyApp".

### The Rest

As if that wasn't enough, there are a lot more changes. First off, improved support for debugging in Cappuccino and Objective-J, thanks to some contributions to WebKit. For more details, see [Francisco's post](http://www.alertdebugging.com/2009/04/29/building-a-better-javascript-profiler-with-webkit/) on the topic.

We now build on top of Rake instead of ant, which has helped us create a much better build system that can improve quickly. Objective-J has improved support for deploying code to multiple platforms, like server (e.g. rhino) and browser. And we're including the new [Narwhal JavaScript standard library](http://github.com/tlrobinson/narwhal/tree/master) in Cappuccino as an external dependency.

Narwhal is still in the early stages, but eventually it will be a set of standard JavaScript APIs that work consistently across many different JavaScript implementations, making it easy to work on any JavaScript interpreter you have available. We'll write more about all these new features as time goes on, especially all the new tools and APIs in 0.7, so stay tuned. In the mean time, you can check out information we've posted to the [wiki](http://wiki.github.com/280north/cappuccino/).

Thanks again to everyone who's contributed to Cappuccino for the 0.7 release, and to everyone using Cappuccino!

- Ross




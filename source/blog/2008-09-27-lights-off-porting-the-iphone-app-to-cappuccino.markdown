---
title: Lights Off - Porting the iPhone app to Cappuccino
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 27
wordpress_url: http://cappuccino.org/discuss/?p=27
date: '2008-09-27'
categories:
- Cappuccino
tags:
- Cocoa
- iPhone
- Porting
---


A couple days ago, [Steven&nbsp;Troughton-Smith](http://steventroughtonsmith.blogspot.com/) decided to try his luck at Cappuccino. With a background in Cocoa programming, and recent work on rewriting Lights Off&nbsp;for the iPhone&nbsp;(the game originally released by Lucas Newman for jailbroken phones), he thought it would be interesting to port Lights Off to Cappuccino. &nbsp;In only an hour or two, he had the complete app running in a web browser on top of Cappuccino.

[	[](http://vimeo.com/moogaloop.swf?clip_id=1820770&server=vimeo.com&show_title=1&show_byline=1&show_portrait=0&color=&fullscreen=1)]()
[Lights Off Final Demo (Cappuccino)](http://vimeo.com/1820770?pg=embed&sec=1820770) from [Steven Troughton-Smith](http://vimeo.com/user784130?pg=embed&sec=1820770) on [Vimeo](http://vimeo.com?pg=embed&sec=1820770).
Steven had to say this about Cappuccino:

>  Wow, just wow. I've spent five mins with Cappuccino and Obj-J, and it feels like home. Because it matches AppKit, I dont have to check docs. I can easily code an Obj-J web app just from what I already know about AppKit, and all the structures and methods are basically the same.
>

This is a testament to the power of Cappuccino, and the ease with which existing Cocoa programmers can pick it up. Without needing to know any CSS or HTML, Steven was able to get Lights Off running, complete with animations backed by our implementation of Core Animation. He was kind enough to e-mail me his code, which [you can download](http://cappuccino.org/files/LightsOff.zip) and play around with.

Right now we're working on tools to boost performance and usability on the iPhone, and once they're ready we'll get Lights Off running on the iPhone to show it off. I think everyone will be impressed with how well it works. In the meantime, I hope this inspires you existing Cocoa developers to try out Cappuccino and see what it can do!

* [Lights Off Cappuccino Google Code project](http://code.google.com/p/lightsoffcappuccino/)




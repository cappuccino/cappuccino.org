---
title: Solving the JavaScript Memory Management Problem
author: Ross Boucher
author_email: ross@280north.com
wordpress_id: 606
wordpress_url: http://cappuccino.org/discuss/?p=606
date: '2010-04-01'
tags:
- cappuccino
- objective-j
- code
---


JavaScript has some real problems. Anyone who has programmed for the web can attest to that. And anyone familiar with what we're doing with Cappuccino will recognize that we're not afraid to tackle those problems head on. When we created Objective-J we set out to create a set of true enhancements to the JavaScript language that would add powerful new dynamic features to the language, like advanced automatic dependency resolution, truly dynamic message passing, and familiar classical inheritance. By all accounts it has been a tremendous success.

Lately, though, we're beginning to realize that we didn't quite go far enough. Memory issues have long plagued JavaScript developers. Because the garbage collector is opaque to the developer, and nothing like "finalize" is provided by the language, programmers often find themselves in situations where they are forced to hold on to an object reference for too long (or forever) creating a memory leak.

Just as we've done before, when we tackled this problem we decided to look at what has worked in the past. Finding inspiration in the elegant simplicity of C, we knew we'd found the right solution. And so, we're pleased to announce the immediate availability of a manual memory management system in Cappuccino.

A lot of Cocoa developers disparaged garbage collection when it came to Objective-C, and we've come to realize they were absolutely right! Why rely on machines to solve problems for us when we can do it by hand. So, we've taken the Cocoa reference counting system and implemented it in JavaScript. We've replaced the existing no-op -retain, -release, and -autorelease methods with fully working implementations. When an object's release count reaches 0, the object's dealloc method will be called, and the memory will be able to be reclaimed. Now you have a clear way to clean up unwanted references when an object is no longer being used. Just make sure you do your reference counting correctly!

To do this right, we've created a global object table. These objects aren't going anywhere on their own! If you don't release an object, it will stick around forever, ensuring you'll always have it when you need it. This global table acts as a lookup table for any object, allowing us to finally implement pointers in JavaScript. Since $ has become the coolest way to do completely non-standard lookups in an almost indecipherable way, we thought we'd jump on the bandwagon. Pass any pointer to $ and you'll get the associated object! How do you get a pointer you ask? $$ of course! For example:

    :::objj
    var o = [CPobject new]; // +new returns with a retain count of 1!
    var p = $$(o); // returns a pointer to o

    o === $(p); // we dereference the pointer and get the right object!


Zombies come standard, too! Just set OBJJ_ZOMBIE_DETECTION to true and objj_msgSend will throw an exception if you ever message an object that's been dealloc'd.

We've even take the time to properly -autorelease all objects returned from class methods in Foundation, but we've made absolutely no effort to properly retain those objects in Cappuccino code that uses them yet. So we need your help. Every line must be scrutinized (but we shouldn't to automate this process, as it would surely be too error prone). Rather than focus on developing new features or fixing bugs in the issue tracker, we hope that all Cappuccino contributors will spend their time writing memory management code so that we can fully realize this web development revolution!

We'll be including these exciting new features in a future release, so you should get started adding manual memory management code to every single line of Cappuccino you've ever written! In the meantime, check out the [working code on Github](http://github.com/280north/cappuccino/commit/6678bba94f7778b245d8219292b3a6ac85d31678).

_Please note this is an April Fools joke!_




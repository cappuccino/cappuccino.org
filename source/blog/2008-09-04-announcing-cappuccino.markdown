---
title: Announcing Cappuccino
author: admin
author_email: ross@280north.com
wordpress_id: 16
wordpress_url: http://cappuccino.org/discuss/?p=16
date: '2008-09-04'
categories:
- Cappuccino
tags: []
---


It is our great pleasure to finally release Objective-J and Cappuccino to the open source community today. We've been working hard on this, and we're incredibly excited to get it into people's hands and start seeing what they can do with it.

### Objective-J and Cappuccino offer a different take on web development.

 Imagine that if every time developers wanted to add a new feature to Python, or even just fix a simple long standing bug, they first had to get permission from Intel and AMD. They'd start by drafting up a proposal of the desired changes, then approach the large chip makers, try to build a consensus, and finally wait patiently while these chip makers actually did the implementing of the proposed features. Sounds a bit silly doesn't it? Well, this is exactly the way web development works today. It's as if at some point we all decided that the future of the core technologies of the web would be in the hands of a very select minority, while the rest of us would have to look on from the sidelines and hope for the best.

Pretty much everyone agrees that JavaScript, and application development on the web in general, are in serious need of an update. But then why has JavaScript stagnated for so long? The reason is pretty simple: the motivations of the people designing it are fundamentally split from those of the people that actually use it. &nbsp;You don't have to search very far to notice this, just look at the now defunct ECMA Script 4 proposal. &nbsp;Most JavaScript programmers today could list a number of features and bug fixes they'd like in JavaScript, such as classical inheritance, better media support, and access to the webcam. &nbsp;However, instead of tackling these very tangible concerns, ECMA Script 4 instead chose to focus on obscure problems like let-versus-var scoping rules. The result was an overly bloated and complex proposal that was destined to be scrapped, and more importantly, would have not pushed the next generation of web applications even had it succeeded. Ironically enough, in the last couple of years the most important developments have been proprietary additions like Microsoft's XMLHTTPRequest and Apple's canvas tag. Even vendors, though, aren't in a position to move the web forward at a great pace. Browser vendors decisions are rooted in internal politics, and complicated by the fact that the major players don't play well together.

And that's why Objective-J is different. Objective-J is not simply a new JavaScript library, but an attempt to restore control of the language and basic building blocks of web development to the developers. &nbsp;We believe in the importance of getting the entire community involved, so that we can experiment and move forward at our own pace. So while it's true that Objective-J is great because it adds features like Ruby's methodMissing and classical inheritance, the real beauty of Objective-J is that it already works in every major browser and it is completely extendable at our&nbsp;discretion. New language features can be added as necessary, and since every individual developer ships the entire runtime without a plugin, no one company can control the destiny of any other, unlike Silverlight or Flash. Perhaps most importantly, you're not bound to our development schedule.

### It's the Frameworks, stupid.

 In reality, Objective-J was built to support the real star of the show: Cappuccino. Cappuccino is essentially a port of the GNUStep frameworks (or Cocoa as more people are familiar with them), and it aims to fundamentally change the way applications are written on the web. Unlike many other libraries out there today, Cappuccino is designed with the express purpose of building desktop caliber applications that run in the browser. That's why we chose to base this framework on proven technologies that have had thousands of successful applications written on them already, and have been proven to be one of the best development environments there is.

To be clear, Cappuccino is about building applications, not web pages. When you think about applications, think 280 Slides, or GMail, or Meebo. &nbsp;jQuery, Prototype, and others do a great job of making static web pages a little more interactive, but they weren't designed for building full fledged applications. &nbsp;Similarly, Cappuccino is not for building web pages; it's optimized for a completely different set of tasks.

[280 Slides](http://280slides.com) is the first app built on Cappuccino, and it's a great showcase of what's possible. &nbsp;Cappuccino builds in many of the features you see, like the Document architecture, object copy/paste, global undo and redo, drag and drop, and great graphics support.

We're open sourcing this technology because we sincerely want to be part of a world where there are more high quality web applications like 280 Slides. We'll be putting a lot of resources into Cappuccino in the future, and we plan to build a strong open source community around the development platform. We can't wait to see where you take this with us.

-- Francisco




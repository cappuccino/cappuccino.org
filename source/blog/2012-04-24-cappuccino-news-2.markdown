---
title: Cappuccino News
author: aparajita
author_email: aparajita@aparajitaworld.com
wordpress_id: 1284
wordpress_url: http://cappuccino.org/discuss/?p=1284
date: '2012-04-24'
categories:
- Cappuccino
- Update
tags: []
---


### New features

 &ndash; Basic support has been added for NSDateFormatter in nib2cib. &nbsp;(Alexander Ljungberg)

&ndash; Lazy support for bytes() and base64() added to CFData, +dataWithBytes and +dataWithBase64 methods added to CPData. &nbsp;(cacaodev)

&ndash; capp_lint has been added to the Tools directory. capp_lint is a command-line tool to check code conformance with the Cappuccino style conventions. Anyone submitting pull requests should use capp_lint. Note that if you use the SublimeLinter plugin with Sublime Text 2, capp_lint is built in. &nbsp;(Aparajita Fishman)

&ndash; Added missing CPSplitView -adjustSubviews method. &nbsp;(Aparajita Fishman)

&ndash; Added a&nbsp;rhino-narwhal patch that can be applied to add JAVA_OPTS support when running Cappuccino utilities through rhino. &nbsp;(Alexander Ljungberg)

&nbsp;   

### Changes/Fixes

 &ndash; CPURLRequest -init correctly initializes the object. &nbsp;(Alexander Ljungberg)

&ndash;&nbsp;Fixed a crash when removing objects from an array controller which has its arrangedObjects.@count observed. &nbsp;(Alexander Ljungberg)

&ndash;&nbsp;Fixed: a collection view wouldn't become the first responder when its items were clicked. &nbsp;(Alexander Ljungberg)

&ndash; Fixed CPScrollView trying to access subviews in -initWithCoder. &nbsp;(Aparajita Fishman)

&ndash;&nbsp;Added an `xcode-select` warning to bootstrap.sh. &nbsp;(Alexander Ljungberg)

&ndash; CPKeyedUnarchiver -decodeIntForKey, -decodeFloatForKey, and -decodeDoubleForKey now return 0 instead of nil, per Cocoa. (Aparajita Fishman)

&nbsp;   

### Issues/Pull Requests

 261 open issues

~180 left to triage

~20 closed in the last 8 days.

22 open pull requests

1 pull request closed in the last 8 days.




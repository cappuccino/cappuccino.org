---
title: Cup - The File Upload Framework
date: '2013-05-25'
author: Aparajita Fishman
tags:
- cappuccino
- frameworks
---

A common need for Cappuccino apps is the ability to upload files. Until now, the only native Cappuccino upload solution was [DeepDropUpload](https://github.com/davidcann/deepDropUpload) by David Cann. While DeepDropUpload works, it hasn't been updated in two years, and it doesn't integrate directly with Interface Builder.

### Cup

Cup \(**C**appuccino **Up**loader\) is a Cappuccino framework that provides a Cappuccino interface to the fantastic [jQuery File Upload](http://blueimp.github.io/jQuery-File-Upload/) library. Among the many features of Cup:

* Multiple, simultaneous uploads.
* Overall and per-file progress.
* Complete upload queue management.
* Extensive control via delegates.
* Complete integration with Interface Builder.
* Name filtering via regex.

When used with Interface Builder \(Xcode\), sophisticated uploaders can be designed, configured and implemented with **zero** lines of code. It's a testament to the beauty and power of Cappuccino. If you don't believe it, watch the [Cup screencast](https://vimeo.com/66123997).

You can find the source for Cup [on github](https://github.com/aparajita/Cup/wiki), along with complete documentation and a [demo app](https://github.com/aparajita/Cup-demo). I hope you find it useful!

  _Aparajita_

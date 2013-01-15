---
title: Just One File with Cappuccino 0.8
author: Francisco Tolmasky
author_email: francisco@280north.com
wordpress_id: 498
wordpress_url: http://cappuccino.org/discuss/?p=498
date: '2009-11-11'
categories:
- Cappuccino
- Tools
tags: []
---


The entire 280 crew just got back from an awesome time at [JSConf EU](http://jsconf.eu/2009/) in Berlin, where we got to show off some of the cool new developments coming with Cappuccino 0.8. I wanted to take the time to share one in particular in more depth here: **image spriting**.

### The Problem with Spriting

Image spriting is the act of taking all the images in your app (or framework, or library, or whatever) and combining them down to one single image. This has the advantages of being smaller (since each individual image has overhead associated with the format), as well as allowing you to grab it from your server with one request:

![Traditional Spriting](/img/cpo-uploads/2009/11/Screen-shot-2009-11-11-at-1.55.50-AM.png)

This is faster in an absolute sense, but even more so psychologically since it allows you to show the contents of your app faster without having all the images "flash in" later. Cappuccino currently uses a similar technique with the source code in your application: concatenating it all together and minifying it, but up until now we've had no automatic, or built-in, support for spriting, you've instead had to do it entirely yourself. And truthfully, no framework has really good support for this.

This is because the fundamental problem with spriting today is that the process isn't really automated and the results are thus subpar. Sure, there are scripts which will put images together for you, but they all require you to configure them first and to update them as your use of the images in question changes. This is because traditional spriting is dependent on **how** you use your images. Whether you choose to repeat, stretch, scale, or even draw to a canvas affects which images can be sprited together, and even which can't be sprited at all. This has a number of unfortunate side effects:

* **Rarely do you actually end up with just one image:** Instead, you can end up with 2, 3, or even more. This is because images have to be "grouped" by their use. For example, vertically repeating images can be sprited together, but not with horizontally repeating images.
* **You may have to actually change your code:** Since images are being mutated, the code you write needs to take into account these new images. If you are lucky you have a system that is relatively good at doing this for you. However, if you decide to use an image in a new way (such as drawing it to a canvas), you either have to update your configuration files or choose to code it differently. This is easy to forget.
* **Your images are still shipped separately from your code:** Even in the best case where you are lucky enough to successfully sprite all your images together, you still have to wait for them separately from when your code is ready, potentially leading to noticeable delays from latency, or a "flash in" effect.
* **Inflexible due to loss of data:** There exist cases where your code is meant to be used by others, such as with libraries and frameworks. In this case, images can't be used in any way other than how you intended them to if they are sprited, because the original images are gone or would require a redundant second download.

So unfortunately there is currently no good one-size-fits-all solution for image spriting the way there is with "code spriting". All of them require the user to actually become involved in the optimization process, and even still can produce less than stellar results. This is clearly not a solution that can scale, and most everyone agrees to this.

But we're hoping to change this with the release of Cappuccino 0.8, as we're introducing a whole new, completely cross-platform, way to sprite: base64 images. By encoding images as base64, we create a lossless text representation of images, allowing us not only to use them in whatever way we please, but to actually ship them **with** the code:

There are many advantages to this:

* **One file, guaranteed:** All images can always be sprited together regardless of how you plan to use them, and can be included with the actual source code. This has the added benefit that gzip can work its magic on the entirety of your web app as one, producing better results.
* **No need to ever modify code or configuration files:** Since we've eliminated the ambiguous part of spriting images, the Cappuccino build tools are able to perform this optimization on your code automatically without tedious configuration files or having to "learn" how to sprite.

### Yes, This Works in IE 6 and 7.

 I'm sure most people are wondering how we are pulling this off in versions of IE before 8, since they do not support data URLs. Notice that earlier I didn't specifically mention data URLs though, I instead only referred to the more broad technology of base64 images. As it turns out, IE has had support for base64 images since version 6 (!) with a little-known technology called MHTML. MHTML allows you place all your resources in one "resources" file, which incidentally can be any file in your website... including the same file that contains all your code.

Cappuccino is already smart enough to be able to automatically download and use different code depending on what browser is being used (and with **no** server configuration), so we now simply ship data URL versions of this technique to modern browsers, and MHTML versions to older copies of IE:

![Cappuccino Spriting](/img/cpo-uploads/2009/11/Screen-shot-2009-11-11-at-1.57.08-AM.png)

This is a very exciting feature for us. This has been a weak point in Cappuccino and its nice to finally have a solution that not only works, but is drop dead simple to use. Our tests have been proven incredibly promising, giving us the fastest load times we've ever seen with Cappuccino, and absolutely fantastic perceived speed as well. Our tools have all been honed to use this at every level: Apps, frameworks, and themes will automatically sprite your images for you.

This is just one of the many enhancements coming with Cappuccino 0.8, and the best part is as usual you won't have to change a single line of code to get all the benefits.




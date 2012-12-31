---
topic_index: 0
---

Before reading any further, please note that Cappuccino is not like
jQuery or Mootools. Cappuccino is **not** good at making websites. It’s
good for making web applications.

Cappuccino **rocks** at:

* Creating a backend for an advanced corporate website.
* Creating a real time application with a lot of user interaction.
* Creating a mockup application.
* Creating a smooth Twitter client.
* Creating a nice email client.
* Making an online RSS reader.
* So much more.

Cappuccino is **not** meant:

* To make your company corporate website.
* For a blog.
* As a widget in your existing website.

The best way to know if Cappuccino is what you want and what you need is
to ask yourself:

> “Does it make sense to make a native desktop application of my
> project?”

If the answer is “yes”, then you should definitly give Cappuccino a try.
It will greatly improve your developement time thanks to a powerful
foundation, great controls and cool toolchain.

## Ok, I want Cappuccino. What is it really?

Cappuccino is GNUStep or Cocoa for the web. Cocoa is the set of
libraries and frameworks used to create both Mac OS and iOS
applications.

-   Cocoa relies on Objective-C, a superset of C which adds **real**
    object-oriented programming.
-   Cappuccino relies on Objective-J, a superset of JavaScript which
    adds **real** object-oriented programming.

With Cocoa, you can build amazing apps for iOS or Mac OS X devices. With
Cappuccino you can build awesome apps for anybody with a web browser.
Cappuccino abstracts away the underlying JavaScript and DOM management.
The code you’ll write will work **as is** in Firefox, Chrome, Safari and
Internet Explorer.

To use Cappuccino, some knowledge of Cocoa is recommended, in particular
its key concepts. As you can see from the following examples, code in
Cocoa and Cappuccino looks very similar:

#### Cocoa sample code

    :::objc
    NSString *myString = @"hello world";
    NSArray *myArray = [NSArray array];
    [myArray addObject:myString];

#### Cappuccino sample code

    :::objj
    var myString = @"hello world",
        myArray = [CPArray array];
    [myArray addObject:myString];

## How do I work with Cappuccino?

To start working with Cappuccino you don’t need a lot of stuff. Here are
the basics

### Code editor

The following table shows the state of Cappuccino support in some major editors, in no particular order.


<table class="table span9">
<tbody><tr>
<th>Editor</th>
<th>Platform</th>
<th>Syntax coloring</th>
<th>Linting</th>
</tr>
<tr>
<td>Emacs</td>
<td>All</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>SubEthaEdit</td>
<td>Mac OS X</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>SublimeText</td>
<td>All</td>
<td>Yes</td>
<td>Yes (live)</td>
</tr>
<tr>
<td>TextMate</td>
<td>Mac OS X</td>
<td>Yes</td>
<td>Yes (not live)</td>
</tr>
<tr>
<td>vi</td>
<td>All</td>
<td>Yes</td>
<td>No</td>
</tr>
</tbody></table>

## The Cappuccino toolchain

Everything you need is shipped with Cappuccino. We’ll see soon how to
install and use them, but here's an overview:

* **Cappuccino framework**: Make your applications.
* **Jake**: Build your applications.
* **OJUnit**: Test your applications.
* **Press/Flatten tools**: Deploy your applications.

## The Xcode case

Xcode is the Apple’s IDE to build Cocoa application. Thanks to Cappuccino's affinity with Cocoa, you can build your user interfaces in Xcode and convert the output files to Cappuccino ready UI archives. For that you'll require these tools:

* **XcodeCapp**: The corner stone of the toolchain if you use Xcode which enables Cappuccino projects to be viewed in Xcode.
* **nib2cib**: Command line utility to convert `XIB` (native Cocoa UI file) to `CIB` (native Cappuccino UI file)

Xcode is **not** required to build great Cappuccino apps. It is however a very valuable tool that could save you hundreds of hours of work and drastically reduce the total amount of code for you to write, debug and manage.

Cappuccino is an open source application framework for developing
applications that look and feel like the desktop software users are
familiar with.

Cappuccino is built on top of standard web technologies like JavaScript,
and it implements most of the familiar APIs from GNUstep and Apple's
Cocoa frameworks. When you program in Cappuccino, you don't need to
concern yourself with the complexities of traditional web technologies
like HTML, CSS, or even the DOM. The unpleasantries of building complex
cross browser applications are abstracted away for you.

Cappuccino was implemented using a new programming language called
Objective-J, which is modelled after Objective-C and built entirely on
top of JavaScript. Programs written in Objective-J are interpreted in
the client, so no compilation or plugins are required. Objective-J is
released alongside Cappuccino in this project and under the
[LGPL](/learn/lgpl.txt).

## Designed for Applications

Nobody will deny that there is a distinct difference between a web site
and a desktop application. Similarly, we believe there is a big
difference between a static web page and a full fledged web application.
Cappuccino is designed for applications, not web pages.

Instead of doing all or most of the work on the server, Cappuccino
applications do as much as possible in the client. A typical application
would never reload, but rather send and recieve data using traditional
AJAX techniques and then present that data in the client code.

Instead of worrying about how to implement drag and drop, copy and paste
(of text *and objects*), undo and redo, document saving, rich
cross-browser drawing and graphics, and a slew of other features,
developers are free to focus on specific problems like PowerPoint
support, or Twitter integration, or whatever else makes their
application unique and compelling.

## How does Cappuccino Compare to Other Frameworks?

Cappuccino is *not* designed for building web sites, or making existing
sites more "dynamic". We think these goals are too far removed from
those of application development to be served well by a single
framework. Projects like Prototype and jQuery are excellent at those
tasks, but they are forced by their nature to make compromises which
render them ineffective at application development.

On the other end of the existing frameworks are technologies like
SproutCore. While SproutCore set out with similar goals to Cappuccino,
it takes a distincly different approach. It still relies on HTML, CSS,
JavaScript, Prototype, and an entirely new and unique set of APIs. It
also requires special development software and a cumbersome compilation
step. We think this is the wrong approach.

With Cappuccino, you don't need to know HTML. You'll never write a line
of CSS. You don't ever have to interact with DOM. We only ask developers to
learn one technology, Objective-J, and one set of APIs. Plus, these
technologies are implementations of well known and well understood
existing ones. Developers can leverage decades of collective experience
to really accelerate the pace of building rich web applications.

If you want to build a rich web application, you need to learn
*something* new. Many people think this will be JavaScript 2, or HTML 5,
or some new standard. The problem is, as we've come to realize,
standards bodies work too slowly. Cappuccino works right now, not in the
theoretical future. Objective-J is essentially JavaScript 2, but
available today in every major browser. Because we rely on only the most
essential web technologies, improvements are not limited by the pace of
browser vendors and standards bodies.

## Browsers

Cappuccino and Objective-J run in any modern web browser, including:

-   Internet Explorer 7+
-   Firefox 2+
-   Safari 3+
-   Google Chrome
-   Opera 9+

## Thank You

Obviously, like everyone else in the open source world, we owe a great
deal of thanks to others, including several existing projects. Among
them are:

-   [GNU Step](http://www.gnustep.org/)
-   [Cocotron](http://www.cocotron.org/)

## When should I use Cappuccino?

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

## Tools of the Trade

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

### The Cappuccino toolchain

Everything you need is shipped with Cappuccino. We’ll see soon how to
install and use them, but here's an overview:

* **Cappuccino framework**: Make your applications.
* **Jake**: Build your applications.
* **OJUnit**: Test your applications.
* **Press/Flatten tools**: Deploy your applications.

### Xcode

Xcode is the Apple’s IDE to build Cocoa application. Thanks to Cappuccino's affinity with Cocoa, you can build your user interfaces in Xcode and convert the output files to Cappuccino ready UI archives. For that you'll require these tools:

* **XcodeCapp**: The corner stone of the toolchain if you use Xcode which enables Cappuccino projects to be viewed in Xcode.
* **nib2cib**: Command line utility to convert `XIB` (native Cocoa UI file) to `CIB` (native Cappuccino UI file)

Xcode is **not** required to build great Cappuccino apps. It is however a very valuable tool that could save you hundreds of hours of work and drastically reduce the total amount of code for you to write, debug and manage.

## More Information

You can learn more about using Cappuccino and Objective-J in this tutorial or by browsing
[documentation](/learn/documentation/).


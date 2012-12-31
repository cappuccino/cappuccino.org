---
topic_index: 1
---

In this tutorial we list what you need in order to install Cappuccino.

## Supported platforms

Cappuccino is supported on the following platforms:

<table class="table span9">
<tbody><tr>
<th>Platform</th>
<th>Supported features</th>
</tr>
<tr>
<td>Mac OS X</td>
<td>Toolchain, Interface Builder</td>
</tr>
<tr>
<td>Linux</td>
<td>Toolchain</td>
</tr>
<tr>
<td>Windows</td>
<td>Toolchain with installation of <a href="http://cygwin.org">Cygwin</a></td>
</tr>
</tbody></table>

This tutorial will be written based on Mac OS X, with notes on any differences with other platforms included.

## Get Developers Tools (Mac OS X only)

In order to use Xcode's Interface Builder, and to compile Cappuccino itself, you need the Mac developer tools installed. You can get the latest version from the [AppStore for
free](http://itunes.apple.com/en/app/xcode/id448457090). Xcode 4 is the current version, but Xcode 3 is (probably) still usable.

## Install Git

If you wish to install the Cappuccino sources you'll need the source control management software Git.

Git is included with Xcode 4. You can check you have it by entering the following command in your Terminal:

    :::bash
    # git --version
    git version 1.7.4.4

On other platforms you can grab the latest version of Git at the following URL:
[http://git-scm.com/download](http://git-scm.com/download).

## Java

For the most part you don't need Java to use Cappuccino. In particular you don't need to know Java, and your users do not require it. But certain tools in the Cappuccino toolset depend on Java being installed.

On Mac OS X Java is installed automatically when you need it. On other platforms, please install Oracle’s JDK.

<span class="label label-info">Info</span>  Java is needed to run the Rhino Engine, which is sometimes used to execute JavaScript outside of the browser.

Your browser
============

You probably already have a browser, but make sure you get a good one. Normally you'd want a WebKit based browser:

* [Chrome](http://google.com/chrome),
* [Chromium](http://www.chromium.org/),
* [Safari](http://www.apple.com/safari/)

These browsers are fast and have a powerful JavaScript engine, plus a great set of native tools to
debug and profile your Javascript (and so Cappuccino) applications.

Cappuccino also works with [Firefox](http://www.mozilla.org/firefox/) and [Internet Explorer
8+](http://windows.microsoft.com/en-US/internet-explorer/products/ie/home).

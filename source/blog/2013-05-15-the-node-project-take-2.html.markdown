---
title: The Node Project - Take 2
date: '2013-05-15'
author: Aparajita Fishman
tags:
- cappuccino
- projects
---

The time has come to move Cappuccino to [Node.js](nodejs.org). Why move to Node? There are three main reasons:

### 1. Cross-platform parity

Cappuccino's build system is built on top of narwhal + rhino (jsc on Mac OS X). Rhino/jsc is the Javascript engine, narwhal is a set of libraries that interface with the host system. Rhino requires Java and is very slow. Narwhal has been abandoned. In addition to these dependencies, our current build system relies on Posix binaries to overcome limitations in narwhal.

Narwhal runs fully only on Mac OS X (using jsc), runs with difficulty on Linux, and doesn't run at all on Windows.

Node runs equally well on all three platforms, is very fast, and replaces narwhal, rhino, and jsc, with no other dependencies. By converting our Javascript code and Posix binary calls to Node, we can have parity on all platforms and a much simpler install.

### 2. Ease of installation and upgrading

The single biggest point of friction for beginning users is the obscure incantations necessary to get Cappuccino installed and running. Updating is more difficult than it should be, with a frequent need to rebuild from scratch.

Using the magic of `npm`, the Node Package Manager, our goal is to have the Cappuccino install be like this:

    npm install cappuccino --dev

No bootstrap, no compiling. One line and you're done. Cappuccino will run fully from source, with no compiling necessary (other than themes). This will make updates much easier. Of course when it comes time to deploy, you will be able to create a compressed version.

### 3. More modularity, better ecosystem

Currently Cappuccino is a very large, monolithic beast. Frequently when we change one small part of it, users have to clobber and rebuild the whole thing. Why should this be so?

We envision Cappuccino being split into modular packages that form a stack: Objective-J, Foundation, AppKit, Tools. Installing packages higher in the stack automatically installs the dependencies lower in the stack.

Node (and thus Javascript) is very popular as a server-side scripting language. But wouldn't you rather use Objective-J + Foundation? In the future, you will be able to do that easily:

    npm install Cappuccino-Foundation

More importantly, the modularity and ability to make easily installable packages will encourage Cappuccino developers to publish their extensions to Cappuccino. And we don't have to spend any time creating the infrastructure for finding and installing Cappuccino packages, npmjs.org already serves as a central repository and search engine for Node packages. There is a huge and growing Node ecosystem, and Cappuccino can be part of that.


### Moving Forward

**Bringing parity to all platforms and making it easier to install and use is the single most important thing we can do to ensure wider adoption.**

More users means more support from the community, more funds for development, and thus an even better Cappuccino.

This is a big project -- we will be rebuilding Cappuccino from the ground up and rewriting many of the tools.

<hr>
**Our fundraising goal: $5000**
<hr>

A few months ago, we received almost half of that, and had to abandon the project at that time. But now we are ready to try again. Let's make it happen this time!

If you donated before, thank you! Please donate again. If you didn't donate the first time, now is your chance to contribute to a brighter future for Cappuccino. Any amount, great or small, is more than welcome and greatly appreciated.

You can donate here:

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="C2EG6R4LHBHT2">
<input type="image" src="http://www.aparajitaworld.com/cappuccino/Donate-button.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

Thank you for using Cappuccino, and thank you for your support!

_The Cappuccino Core Team_

---
title: The Node.js Project
date: 2013-02-17 07:27 +00:00
author: Aparajita Fishman
tags:
- cappuccino
- projects
---

Cappuccino was released to the Open Source community on September 4, 2008. After four years and over 6,800 commits, Cappuccino continues to grow and improve. But to make Cappuccino ready for the next four years and expand our user base, we need to update the build system.

The original build system used **ant**, which was then followed by **rake**, which ran on Ruby. In 2010 the build system was ported to JavaScript and **jake** (a port of rake), which ran on top of narwhal (a CommonJS runtime) and the package manager **tusk**. This is the system we are still using today.

A **lot** has happened since 2010 in the JavaScript world. [**Node.js**](http://nodejs.org) is now the king of CommonJS and runs on Mac OS X, Linux, and Windows. [**npm**](http://npmjs.org), the node package manager, is a world class tool that boasts over 23,000 packages available. On the other hand, narwhal and tusk do not run on Windows and are no longer being maintained.

The time has come to take Cappuccino’s build system to the next level, to create a **cross-platform** infrastructure for Cappuccino — where Windows is a first class citizen — that will keep it on the cutting edge for the next four years. To do this we must move to node.

The goal here is not just to port the existing build system from narwhal to node. The goal is to create a brand-new build system — reimagined from the ground up — that leverages all of the power of node, npm and their thriving ecosystems. The goal is to create a build system that is better, faster, and more extensible. A build system that dramatically improves the process of building, debugging, testing, packaging, and deploying Cappuccino.

#### We need your help

To do all of this will require quite a bit of time — more time then we can spend in our spare time to get this finished in any reasonable timeframe. That’s why we are asking for your help! We know many of you would like to help with Cappuccino, but you neither have the time nor the experience to help us with the coding. Now, you can help by donating to this project. Your donations will allow us to spend the time necessary to finish the project (in this life!) and do it right.

<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="5TFJAUEBDET98">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="Donate">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

Any amount, great or small, is more than welcome and greatly appreciated. Your donations are an investment in a brighter future for Cappuccino. Thank you for using Cappuccino, and thank you for your support!

_- The Cappuccino Core Developer Team_

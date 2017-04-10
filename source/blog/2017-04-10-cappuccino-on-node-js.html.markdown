---
title: Cappuccino on Node.js
author: Martin Carlberg
author_email: martin@carlberg.org
date: '2017-04-10'
tags:
- Cappuccino
- objj
- update
- Node.js
- Node
---

### Background
Up until now Cappuccino has only been able to build on two different Javascript engines, [Rhino](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino) (Linux and Mac) and [JavaScriptCore](https://developer.apple.com/reference/javascriptcore) (Mac). Rhino is very old, slow and is based on Java. JavaScriptCore is very fast and modern but runs only on Mac OS X. Almost everyone else in the Javascript world is using [Node.js](https://nodejs.org).

### Announcement
Today we are proud to announce Cappuccino support for Node.js. This is made possible by great work by [Frank Rehwinkel](https://github.com/FrankReh).

### How is it done
There has been multiple attempts to support this over the last couple of years and I think the reason for the success by Frank is that he started this in very small steps. Cappuccino is using the Javascript Narwhal library to run its build scripts. Narwhal can be run on multiple Javascript engines and we have supported Rhino and JavaScriptCore for many years. It is fairly easy to support additional Javascript engines by implementing a specified api. This will glue Narwhal together with the Javascript engine and this is what Frank has done for Node.js.

### How to use it
Everything will work as before except we can now choose Node.js as Javascript engine instead of Rhino or JavaScriptCore. First make sure [Node.js](https://nodejs.org) is installed. Then the new [Cappuccino-Base](https://github.com/cappuccino/cappuccino-base) is next. It is included in the latest version of Cappuccino. Easiest installed by following the instructions [here](http://www.cappuccino-project.org/#download). Some Node.js modules are needed to be downloaded. Run the ```bash``` script at ```<Your Narwhal Folder>/packages/narwhal-node/bin/npm-install```. There are also some small changes to the Cappuccino framework to support Node.js. They are not included in the latest version so download the lastest master version from [Github](https://github.com/cappuccino/cappuccino). When it is downloaded you need to set the environment variable ```NARWHAL_ENGINE``` to ```node```. In ```bash```you can type ```export NARWHAL_ENGINE=node```. Now everything works as normal and you can build it with ```jake install```.

### Performance
Node.js is much faster than Rhino and almost up to par with JavaScriptCore. Here are some build tests done with the different engines using the command ```jake install``` on a MacBook Pro:
1. Node: 2 minute 2 seconds
2. JavascriptCore: 1 minute 49 seconds
3. Rhino: 5 minutes 31 seconds

### The next step
The build process is still dependent on a couple of non Javascript tools like [gcc](https://gcc.gnu.org)  and [ShrinkSafe](http://shrinksafe.dojotoolkit.org) etc. When we have removed all dependencies it will be much easier to build Cappuccino on all platforms including Windows. Also in the long run it should be nice to remove Narwhal and maybe replace Jake with something more modern. Work is being done to remove gcc and if you want to get involved in working with removing any of these dependancies please get in contact with us on the [mailing list](https://groups.google.com/forum/#!forum/objectivej) or on [Gitter](https://gitter.im/cappuccino/cappuccino).

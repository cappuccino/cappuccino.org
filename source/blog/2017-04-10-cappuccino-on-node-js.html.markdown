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
There has been multiple attempts to support this over the last couple of years and I think the reason for Frank’s success is that he did focus on the main issue and asked the right question. Why can't you run it on Node.js if you can run it on JavaScriptCore?. Cappuccino is using the Javascript Narwhal library to run its build scripts. Narwhal can be run on multiple Javascript engines and we have supported Rhino and JavaScriptCore for many years. It is possible to support additional Javascript engines by implementing a specified api. This will glue Narwhal together with the Javascript engine and this is what Frank has done for Node.js.

### How to use it
Everything will work as before except we can now choose Node.js as Javascript engine instead of Rhino or JavaScriptCore. In the next release it will be included and ready to use out of the box. But if you want to try it now please follow the install instructions below:

1. Make sure [Node.js](https://nodejs.org) is installed.
2. The new [Cappuccino-Base](https://github.com/cappuccino/cappuccino-base) is needed. It is included in the latest version of Cappuccino. Easiest installed by following the instructions [here](http://www.cappuccino-project.org/#download).
3. Some Node.js modules are needed to be downloaded. Run the ```bash``` script at ```<Your Narwhal Folder>/packages/narwhal-node/bin/npm-install```.
4. There are also some small changes to the Cappuccino framework to support Node.js. They are not included in the latest version so download the lastest master version from [Github](https://github.com/cappuccino/cappuccino).
5. Set the environment variable ```NARWHAL_ENGINE``` to ```node```. In ```bash```you can type ```export NARWHAL_ENGINE=node```.

Now everything works as normal and you can build Cappuccino with ```jake install```.

### Performance
Node.js is much faster than Rhino and is up to par with JavaScriptCore. Here are some build tests done with the different engines using the command ```jake install``` on a MacBook Pro:

1. Node: 2 minutes
2. JavascriptCore: 2 minutes
3. Rhino: 5 minutes 30 seconds

### The next step
As soon as possible we will drop support for Rhino as it is old and is not maintained. It will allow us to be more up to date and for example support the ES6 release of Javascript. The build process is still dependent on a couple of non Javascript tools like [gcc](https://gcc.gnu.org) and [ShrinkSafe](http://shrinksafe.dojotoolkit.org) etc. When we have removed all dependencies it will be much easier to build Cappuccino on all platforms including Windows. Also in the long run it should be nice to remove Narwhal and maybe replace Jake (our build system) with something more modern. Work is being done to remove gcc and if you want to get involved in working with removing any of these dependancies please get in contact with us on the [mailing list](https://groups.google.com/forum/#!forum/objectivej) or on [Gitter](https://gitter.im/cappuccino/cappuccino).

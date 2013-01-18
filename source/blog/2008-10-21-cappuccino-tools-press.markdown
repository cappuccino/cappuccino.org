---
title: ! 'Cappuccino Tools: &ldquo;press&rdquo;'
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 104
wordpress_url: http://cappuccino.org/discuss/?p=104
date: '2008-10-21'
tags:
- cappuccino
- tutorials
- tools
- build tool
---

_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

In the third installment of the build tools series we tackle one of the most advanced build tools: `press`. Recall from the [overview](/blog/2008/10/the-cappuccino-build-tools.html) that "press" is a tool for stripping code and other optimizations. Additionally, it can convert an entire Objective-J application into a single pure JavaScript file, which we'll see can be useful.

### press

The primary goal of press is to strip unused code from your application and frameworks and perform other optimizations. It needs to know about the entire application, including your application code and the Cappuccino frameworks, in order to determine the dependencies and remove unused files. It is called with two parameters, the path to your application, and the output directory:

    press root_directory output_directory

This will run press on your application located at `root_directory`, and output a similar but smaller version (with unused files stripped) at `output_directory`.

Additionally, there are several useful options:

* _‐‐main path_: The relative path (from root_directory) to the main file (default: `main.j`)
* _‐‐frameworks path_: The relative path (from root_directory) to the frameworks directory (default: `Frameworks`)
* _‐‐png_: Run `pngcrush` on all PNGs (`pngcrush` must be installed!)
* _‐‐flatten_: Flatten all code into a single Application.js file and attempt to add script tag to `index.html` (useful for Adobe AIR and CDN deployment)
* _‐‐nostrip_: Don't strip any files. Mostly useful for debugging.

### ‐‐flatten

The most interesting of these options is `‐‐flatten`, which converts your application into a single pure JavaScript file that can be imported with a standard "script" tag. While the Objective-J load system is great in most scenarios, there are currently a few limitations that a pure JavaScript file helps overcome. Namely that the load system doesn't work in Adobe AIR due to strict security restrictions, and the load system doesn't work across domains, such as with a CDN, also due to browser security restrictions. By flattening all Objective-J code into a JavaScript file, we can use a standard script tag to load our application, which works cross-domain and in Adobe AIR.

### Internals

If you're interested in how press works, read on. It starts by loading your application while noting which global variables are defined in each file. It then "walks" along the dependency "graph", including every imported file, with one important exception: framework imports like `import <AppKit/AppKit.j>` and `import <Foundation/Foundation.j>` are ignored since these types of imports would result in the entire framework (including unused files) being imported. Instead, press looks at the global dependencies, and only keeps the files that are referenced by any other file that has been imported.

### Conclusion

press is a already a great tool, but there is much room for improvement. In the future we would like to add finer-granularity code stripping, such as method-level rather than file-level. Additionally, we're working on an automatic [image spriting](http://www.alistapart.com/articles/sprites) and optimization feature which determines exactly which images are required for your application and includes them in a single image, vastly reducing the number of HTTP requests to load your application.

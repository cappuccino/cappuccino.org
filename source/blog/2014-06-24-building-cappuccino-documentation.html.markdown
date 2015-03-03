---
title: Building Cappuccino Documentation
date: '2014-06-24'
author: Andrew Hankinson
tags:
 - documentation
 - doxygen
 - docsets
---

In this post I will explain how you can use the `jake` command to build the Cappuccino documentation straight from the source. I will cover building both the HTML version of the source, as well as a DocSet version suitable for use in [Dash](http://kapeli.com/dash) or XCode.

## Getting Started

You will need the following tools to build the Cappuccino documentation from source. (These are all available from your preferred package manager).

 * `doxygen`: An open-source documentation generator. I used v.1.8.7.
 * `markdown`: The Markdown compiler.
 * `graphviz`: Optional, but recommended. Uses the `dot` utility to generate inheritance graphs

## Building HTML Documentation

Once you have the prerequisites installed (and assuming you've built and installed Cappuccino), the easiest way to generate the documentation is using the `jake` command in your Cappuccino source directory.

`$> jake docs`

This command will apply some source formatting and then run Doxygen to generate the documentation. Once it has finished, your documentation can be found in your Cappuccino Build directory (On my system, this is `Build/Documentation/html` inside my Cappuccino source directory). Open up `index.html` in your favourite web browser.

## Building DocSets

DocSets are a documentation bundle, and can be used in several documentation viewers including Dash and XCode. Doxygen can be configured to build a docset.

*Note: Some of these build notes come from Bogdan Popescu, maker of the Dash documentation viewer.*

### Configure Doxygen

The Cappuccino Doxygen file is in `Tools/Documentation/Cappuccino.doxygen`. Generating a docset requires some modifications to this file.

```
GENERATE_DOCSET = YES
DOCSET_BUNDLE_ID = org.cappuccino-project.cappuccino
DOCSET_PUBLISHER_ID = org.cappuccino-project
DOCSET_PUBLISHER_NAME = Cappuccino Project
PROJECT_NAME = Cappuccino
SEARCHENGINE = NO
DISABLE_INDEX = YES
GENERATE_TREEVIEW = NO
```

### Build the Documentation

Once you have configured doxygen, you can build the documentation using `jake`, similar to the process used for the HTML documentation. For best results, you should disable the Doxygen frame:

`$> jake docs-no-frame`

### Build the Docset

In the `Build/Documentation/html` directory there should now be a Makefile. This will be used to build the docset.

#### Optional: Disable Text Indexes

You can disable the full-text search function, which makes the build process much faster. Edit the make file, and find the line:

`$(XCODE_INSTALL)/usr/bin/docsetutil index $(DOCSET_NAME)`

You should replace it with:

`$(XCODE_INSTALL)/usr/bin/docsetutil index -skip-text $(DOCSET_NAME)`

#### Run Make

To build the docset, ensure you are in the `Build/Documentation/html` directory and run:

`$> make`

By default, this will generate the file `org.cappuccino-project.cappuccino.docset` in the `Build/Documentation/html` directory. You should rename this:

`$> mv org.cappuccino-project.cappuccino.docset Cappuccino.docset`

#### Optional: Look-and-Feel

There are a couple post-configuration tasks that will make your docset look a bit nicer. The first is to apply a few custom CSS tools to the docset. In `Build/Documentation/html` run the following command:

```
cd Cappuccino.docset && echo -e "open(FILE, \">>\$ARGV[0]\");\nprint FILE \"\\\n#top {display:none}\\\n#side-nav {display:none}\\\n\";\nprint \"Appended CSS to \$ARGV[0]\\\n\";\nclose(FILE);" > css.pl && find . -type f -name "*.css" -exec perl css.pl {} \; && rm -rf css.pl && cd ../
```

#### Optional: Dash Icon and Keyword

If you are using Dash, you can also replace the default Info.plist with [one supplied by Bogdan Popescu](/downloads/documentation/Info.plist), which will cause Dash to display the Cappuccino logo and provide the `cappuccino:` keyword. (You may need to right-click and "Save As..." the .plist file).

`$> cp ~/Downloads/Info.plist Cappuccino.docset/Contents`

#### Using the DocSets

Double-clicking the docset should open it up in your favourite documentation viewer. Here's a screenshot of it in Dash:

[![](/img/cpo-uploads/2014/06/cappuccino-docs-in-dash.png)](/img/cpo-uploads/2014/06/cappuccino-docs-in-dash.png)

You can also open the docsets in XCode by placing the .docset file in `~/Library/Developer/Shared/Documentation/DocSets/`. You will need to restart XCode if it's already running.

### Wrapping up

The Cappuccino documentation still has a long way to go (and we're always looking for volunteers to help!) but hopefully this post has provided some help for building the latest version of the documentation straight from the source.

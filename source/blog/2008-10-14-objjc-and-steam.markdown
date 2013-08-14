---
title: ! 'Cappuccino Tools: "objjc" and "steam"'
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 93
wordpress_url: http://cappuccino.org/discuss/?p=93
date: '2008-10-14'
categories:
- Cappuccino
- Tutorials
- Tools
tags:
- Cappuccino
- build tool
- Objective-J
---


_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

In our previous post on the [Cappuccino build tools](http://www.cappuccino-project.org/discuss/2008/10/06/the-cappuccino-build-tools/) we summarized the purpose of four of the tools. In this article we'll dive deeper into two of them, objjc and steam.

To review, the purpose of these tools is to prepare your application for deployment by pre-compiling all application Objective-J code into JavaScript, thereby reducing the load time for clients. Additionally, since most developers won't need to modify Cappuccino itself, we always compile Cappuccino's AppKit and Foundation frameworks to further reduce load time.

The only time you'll need to run steam (which handles running objjc for you) is when you're deploying your application, or if you're making changes to the Cappuccino frameworks themselves. In the latter case, the easiest way to recompile the frameworks is to run the default ant task in the Cappuccino source tree:

	cd /path/to/cappuccino
	ant

To use the freshly built frameworks simply replace the "Frameworks" directory in your application with a symbolic link to the Release directory in the directory pointed to by your $STEAM_BUILD environment variable:

	cd /path/to/your_application
	mv Frameworks Frameworks-Original
	ln -s $STEAM_BUILD/Release Frameworks

(if you're loading your project through a webserver like Apache make sure to [enable the FollowSymLinks option](http://tlrobinson.net/blog/?p=40))

### objjc

 objjc, the Objective-J compiler, is the most important of the build tools, but you'll likely never invoke it directly. objj can take any number of parameters as input filenames and output filenames (preceded by the "-o" flag). For example:
``objj Class1.j -o Class1.o Class2.j -o Class2.o``

![](/img/cpo-uploads/2008/10/objjc1.png)

This will invoke the Objective-J compiler (which is identical to the one used by Objective-J in the browser) on each input file, outputting JavaScript plus some metadata to each specified output file. Next we need to combine all of these individual output files into a single ".sj" archive that contains the JavaScript and import dependency metadata for the entire framework. It would be possible to do this by hand, but steam takes care of it for you.

### steam

steam is the general Cappuccino build tool that manages the creation and compilation of your Cappuccino applications.

To create a basic Cappuccino application, simply run steam with the "create" command:

``steam create ApplicationName``

This will create a new Cappuccino application in the directory "ApplicationName". This application can be modified and run (by opening index.html in the browser) without any further usage of the build tools.

When you're ready to compile the application code for deployment, add a .steam file to your application, like the following:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Name</key>
        <string>YourApplication</string>
        <key>Targets</key>
        <array>
            <dict>
                <key>Name</key>
                <string>YourApplication</string>
            </dict>
        </array>
        <key>Configurations</key>
        <array>
            <dict>
                <key>Name</key>
                <string>Debug</string>
                <key>Settings</key>
                <dict>
                    <key>PREPROCESS</key>
                    <true/>
                    <key>FLAGS</key>
                    <string>-DDEBUG</string>
                </dict>
            </dict>
            <dict>
                <key>Name</key>
                <string>Release</string>
                <key>Settings</key>
                <dict>
                    <key>PREPROCESS</key>
                    <true/>
                    <key>PREINTERPRET</key>
                    <true/>
                </dict>
            </dict>
        </array>
    </dict>
    </plist>

This file defines the targets and configurations for your project. This one defines a single target, YourApplication, and two configurations, Release and Debug. To compile your application, simply execute steam with the build command, the .steam filename, and the configuration name:

``steam build -f MyApp.steam -c Release``

If a .steam filename is not provided it will look for a file with the extension ".steam". Likewise, if a configuration name is not provided, it will use the first one defined in the file. The following will run the "Debug" configuration in your .steam file:

``steam build``

steam gathers all ".j" files in your application, compiles them, and combines them into a single ".sj" file ("static Objective-J"), along with a new "Info.plist" which tell Objective-J which files are contained in the ".sj".

![](/img/cpo-uploads/2008/10/steam1.png)

The results are placed in a subdirectory of $STEAM_BUILD named the same as the configuration, i.e. Debug or Release. Alternatively, pass the "-b" flag and a build directory to specify where it should be built.

The compiled application or framework can then be used in place of the original uncompiled collection of .j files. If it was an application, copy or symlink your Frameworks directory to it's directory. If it was a framework, copy it to your application's Frameworks directory.

### Conclusion

This article covered the core Cappuccino build tools, objjc and steam. Remember that you will probably never want to call objjc directly, but rather rely on the "steam build" command to manage the build process for you. Additionally, remember the build process is entirely optional (except if you're editing the Cappuccino frameworks themselves), and is only necessary as a deploy-time optimization.

In subsequent articles we'll cover the remaining more advanced build tools, press and bake, as well as further deployment optimizations.




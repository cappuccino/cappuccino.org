---
title: ! 'Cappuccino Tools: "bake"'
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 135
wordpress_url: http://cappuccino.org/discuss/?p=135
date: '2008-10-29'
tags:
- cappuccino
- tutorials
- tools
---

_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

In the final installment of the Cappuccino Tool article series (for now), we cover "bake", an automatic deployment tool. Writing a Cappuccino application does not require using "bake", but can help with more advanced deployments.

### Introduction

"bake" is somewhat analogous to [Capistrano](http://www.capify.org/), a deployment tool often used for deploying Ruby on Rails and other applications, but "bake" has several features specifically for deploying Cappuccino applications.

The basic idea behind "bake" is to assemble a complete deployable copy of your application by pulling the pieces from various places (Git, Subversion, and local or remote directories via rsync), building it, packing it up, and deploying it to your server(s).

One key feature of bake is the management of multiple deployments over time, which allows three things: [atomic](http://en.wikipedia.org/wiki/Atomic_operation) deployments, keeping your client side code (the Cappuccino application) synchronized with your server side code, and enabling aggressive caching on all your static resources (code, images, etc). We'll see later this is done by putting all the new resources in place, then "swinging" a single file, the index.html with a `<base>` tag.

"Atomic deployments" means that the deployment is updated to the new version in a single operation, which is either successful or not, nothing in between. Every client loading your application receives either the previous deployment, or the new deployment, but never a mixture of the two.

Keeping client code synchronized with server code is (sometimes) important for making sure users who have already loaded the application can continue using it even after you deploy a new version of the server side code that is incompatible with older versions of the client side code.

Aggressive caching of static resources reduces the load time of Cappuccino applications for repeat useres. This is possible because every resources URL is unique in each deployment, so we can set the "Expires" header far in the future (e.x. 'Expires "Thu, 15 Apr 2010 20:00:00 GMT"'). While the actual file name is not unique (for example `Objective-J/Objective-J.js`), in the deployed application the _path_ will be unique, `www.yourserver.com/YourApp/1225273279/Objective-J/Objective-J.js`, where the version number changes for each deployment)

### Summary

The configuration for a bake deployment is specified in a "bakefile", which is in the JSON format with a structure like the following:

	:::json
	{
		"sources" : [
		    {
		        "type"    : "git",
		        "path"    : "git://github.com/280north/cappuccino.git",
		        "parts"   : [
	    	        {
	    	            "src"       :   "Objective-J",
	    	            "dst"       :   "Frameworks/Objective-J",
	    	            "build"     :   "ant -DBuild=BUILD_PATH",
	    	            "copyFrom"  :   "Release/Objective-J"
	    	        },
		            {
	    	            "src"       :   "Foundation",
	    	            "dst"       :   "Frameworks/Foundation",
	    	            "build"     :   "steam build -c Release -b BUILD_PATH",
	    	            "copyFrom"  :   "Release/Foundation"
		            },
	        	    {
	    	            "src"       :   "AppKit",
	    	            "dst"       :   "Frameworks/AppKit",
	    	            "build"     :   "steam build -c Release -b BUILD_PATH",
	    	            "copyFrom"  :   "Release/AppKit"
	        	    }
		        ]
		    },
		    {
		        "type"    : "rsync",
		        "path"    : "/Users/username/projects/NewApplication",
		        "parts"   : [
		            {
	    	            "src"       :   "",
	    	            "dst"       :   "Blah"
		            }
		        ]
		    },
		    {
		        "type"    : "svn",
		        "path"    : "https://svn.youserver.com/Project/trunk",
		        "parts"   : [
		            {
	    	            "src"       :   "subdirectory",
	    	            "dst"       :   "Something"
		            }
		        ]
		    }
		],
		"deployments" : [
		    { "host" : "deploy@myserver.com", "path" : "/var/www/mysite/public" }
		],
		"templateVars" : {
	        "APPLICATION_NAME" : "My Application",
	        "BACKGROUND_COLOR" : "black",
	        "TEXT_COLOR" : "black"
		}
	}


This bakefile contains three "sources": a git repository, a local directory, and a svn repository. The git repository is the main [Cappuccino git repository](http://github.com/cappuccino/cappuccino/), hosted on GitHub. You could replace this with a different branch if you needed a specific version, or even your own if you have one. This source contains three "parts", Objective-J, AppKit, and Foundation. The "src" specifies where in the checkout the part is located, while "dst" specified where in the final built application it should be placed. You can optionally specify a "build" command, which is run from the specified "src" directory. This command should include the placeholder "BUILD_PATH", which will be filled in by "bake" with the temporary directory where the build results are placed (equivalent to $STEAM_BUILD for any "steam" commands). Additionally, if you specify a "build" command you also need to specify a "copyFrom" parameter, which tells build the subdirectory of the build directory it should copy the built part from.

Once each piece of the application has been built it is copied to the appropriate subdirectory of a uniquely named (using the current Unix timestamp) "versioned" directory. Rather than deploying this versioned directory directly, it is placed within another directory which contains a special index.html file. This file includes a `<base>` tag that points to the versioned directory, which causes the browser to treat it as the base for all relative URLs, thus loading the correct version of all resources without requiring the application be located at a unique URL. "bake" will fill in "$VERSION" template variable in the base tag of the template with the correct

Additionally, "bake" will calculate the size of all code which needs to be loaded, in order to provide an accurate loading progress bar. The calculated size is inserted into the template variable "$FILES_TOTAL". You can also specify other template variables such as "$APPLICATION_NAME", "$BACKGROUND_COLOR", and "$TEXT_COLOR" in the bakefile.

If you use your own template, the only required variable is the "$VERSION" one, but you can specify as many custom variables as you wish.

Finally, once the application has been built and assembled, it is optionally run through ["press"](http://www.cappuccino-project.org/blog/2008/10/cappuccino-tools-press.html), then gzipped. If the "--deploy" command line parameter was given then the gzipped application is transmitted to the deployment servers, un-gzipped, and copied to the deployment path using a specific sequence of command to ensure the deployment is atomic:

	:::sh
	tar xzf 1225273279.tar.gz
	mkdir -p /path/to/deployment
	mv 1225273279/1225273279/ /path/to/deployment/1225273279
	mv 1225273279/index.html path/to/deployment/index.html
	rm 1225273279.tar.gz
	rmdir 1225273279
	cd /path/to/deployment
	ln -nsf 1225273279 Current

(version "1225273279", deplyoment directory `/path/to/deployment`)

One important thing to note about "bake" is that since the old deployment remains live (but hidden) if you deploy a fix for a security vulnerability you should manually purge all the old deployments from your server. If the change doesn't introduce any incompatibilities between the server and client, you could set up a [rewrite rule](http://en.wikipedia.org/wiki/Rewrite_engine) to direct all requests to the purged deployments to the latest, which is always symlinked to "Current".

### Conclusion

Once again I should stress that this tool is by no means required for writing a Cappuccino application. It was written to help deploy our production application, [280 Slides](http://280slides.com), but we have made it available for anyone who has similar deployment requirements. If it doesn't quite fit your requirements, please feel free to suggest improvements, or even better, make improvements yourself and contribute them back!

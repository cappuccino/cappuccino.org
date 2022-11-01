---
title: Full support for ECMAScript 2022 in Objective-J. The release of Cappuccino 1.3!
author: Martin Carlberg
date: '2022-11-14'
tags:
- cappuccino
- release
- update
categories:
- Uncategorized
---


#### Details

We are excited to announce the release of version 1.3 of the Cappuccino frameworks with full support for ECMAScript 2022 in Objective-J.

This includes support for Promises including async and await. You can now write code like this:

    :::objj
	- (async @action)doAction:(id)sender {
	    const { response, data, error } = await [CPURLConnection sendAsynchronousRequest:[CPURLRequest requestWithURL:@"http://cappuccino.dev"]];
 	    if (error == nil) {
 		//do the stuff...
 	    } else {
 		// Handle errors
 	    }
 	}


_- Martin Carlberg_


---
title: The release of Cappuccino 1.3 --- Full support for ECMAScript 2022 in Objective-J!
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

Here is another hany use case of async / await:

    :::objj
    - (async CPView)getMyView {
        var aView = await [self loadTopView];

        if (aView) {
            [self addViewAsTop:aView];
        } else {
            aView = [[CPView alloc] initWithFrame:CGRectMake(0, 0, 200, 200)];
        }

        return aView;
    }

The new language features are very convenient to use Object Destructuring when working with CPPoint, CPRect and CPSize.

This will assign x and y with 12 and 13

    :::objj
      let { x, y } = CPPointMake(12, 13)

The variables can have their own names too. This will assign myX and myY with 12 and 13:

    :::objj
      let { x: myX, y: myY } = CPPointMake(12, 13)

This also works with more complex things like a CPRect.

    :::objj
      let { origin: { x: myX, y: myY }, size: { width: myWidth, height: myHeight } } = CPRectMake(20, 10, 100, 200)

The new Arrow Functions also make the code look a little bit cleaner.

    :::objj
    let array = [1,2,3,4,5,6,7,8,9]
    let result = 0
    [array enumerateObjectsUsingBlock:e => result += e]

This will add all numbers in the array and assign it to the variable result. The old code looked like this:

    :::objj
    let array = [1,2,3,4,5,6,7,8,9]
    let result = 0
    [array enumerateObjectsUsingBlock:function(e) { result += e }]

Another nice new feature is "for of". It works the way it should work and not like the old "for in"

    :::objj
    let array = [1,2,3,4,5,6,7,8,9]
    for (const element of array) {
      console.log(element) // prints the element
    }
    
_- Martin Carlberg_


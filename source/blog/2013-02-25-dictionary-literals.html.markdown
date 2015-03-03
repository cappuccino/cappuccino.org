---
title: Dictionary Literals
date: '2013-02-25'
author: Alexander Ljungberg
tags:
- update
- objective-j
---

Support for dictionary literals has today been added to Objective-J 2.0 in [Cappuccino master](https://github.com/cappuccino/cappuccino/commit/5200f945fe905d5f00addaa00bb78ae09a3cedaf). A dictionary literal allows you to allocate a `CPDictionary` with specific contents in a concise and readable manner.

The syntax is `@{ key: value, key2: value2, ... }`, which is equivalent to the [same feature in Objective-C](http://clang.llvm.org/docs/ObjectiveCLiterals.html). Here's an example from `CPBox`:

##### Before

    :::objj
    return [CPDictionary dictionaryWithObjects:[[CPNull null], [CPNull null], 1.0, 3.0, CGSizeMakeZero(), 6.0, [CPNull null], CGSizeMakeZero()]
                                       forKeys:[   @"background-color",
                                                   @"border-color",
                                                   @"border-width",
                                                   @"corner-radius",
                                                   @"inner-shadow-offset",
                                                   @"inner-shadow-size",
                                                   @"inner-shadow-color",
                                                   @"content-margin"]];

##### After

    :::objj
    return @{
            @"background-color": [CPNull null],
            @"border-color": [CPNull null],
            @"border-width": 1.0,
            @"corner-radius": 3.0,
            @"inner-shadow-offset": CGSizeMakeZero(),
            @"inner-shadow-size": 6.0,
            @"inner-shadow-color": [CPNull null],
            @"content-margin": CGSizeMakeZero(),
        };

The new syntax is much easier to read, and the relationship between each key and value pair is clear. The format should be familiar from languages such as Python and, of course, JavaScript itself.

Regular JavaScript dictionaries will continue to work as normal.

    :::objj
    // Objective-J Dictionary Literal
    var a = @{ @"count": 2 };

    // JavaScript Object
    var a = { @"count": 2 };

For the sake of completeness, Objective-J 2.0 also implements array literals: `@[1, 2, 3]`. Since Objective-J already bridges `CPArray` and JavaScript arrays, this is equivalent to just `[1, 2, 3]`. This is similar to how `@"string" == "string"` in Objective-J today.

The dictionary literals feature is available today if you [build from source](/learn/build-source.html).

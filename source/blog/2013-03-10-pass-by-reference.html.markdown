---
title: Pass by Reference
date: '2013-03-10'
author: Alexander Ljungberg
tags:
- update
- objective-j
---

Objective-J 2.0 now supports pass by reference using the new `@ref` and `@deref` syntax. Pass by reference allows you to store a reference to a variable in a different variable and then to pass it around. Among other things this makes it possible to send a message which returns multiple values (one as the return value, and an arbitrary number as output variables).

A common use case is with `CPNumberFormatter`.

`- (BOOL)getObjectValue:forString:errorDescription:` returns `YES` when it's successful and `NO` when it's not. So if the return value is a boolean, where can you find the actual object value after successful conversion?

All you have to do is to provide somewhere for it to be written to.

    :::objj
    var nf = [CPNumberFormatter new],
        valueOut = nil,
        errorOut = @"";

    if ([nf getObjectValue:@ref(valueOut) forString:@"10" errorDescription:@ref(errorOut)])
        CPLog.info(valueOut); // now valueOut == 10.

    [nf setMinimum:100];
    if (![nf getObjectValue:@ref(valueOut) forString:@"10" errorDescription:@ref(errorOut)])
        CPLog.info(errorOut); // now valueOut is unchanged, but errorOut == @"Value is less than the minimum allowed value".

The number formatter is returning values by writing them into the storage you provided for it: `valueOut` and `errorOut` in your local scope.

If you have programmed Objective-C, C or C++ you might think of an `@ref` reference as a JavaScript analog to a pointer. In C you might write:

    :::c
    int a;
    int *aPtr = &a;
    *aPtr = 5;
    printf("%d", *aPtr); // prints 5

Whereas in Objective-J you would write:

    :::objj
    var a,
        aRef = @ref(a);

    @deref(aRef) = 5;
    console.log(@deref(aRef)); // logs 5

Once you have a reference you can pass it around, save it, and dereference it as needed. It's not an actual pointer though so pointer arithmetic is not possible.

The `@ref` feature is available today in [Cappuccino master](https://github.com/cappuccino/cappuccino/commits/master) if you [build from source](/learn/build-source.html).

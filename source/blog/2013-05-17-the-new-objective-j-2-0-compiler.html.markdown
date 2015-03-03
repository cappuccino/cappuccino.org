---
title: The New Objective-J 2.0 Compiler
date: '2013-05-17'
author: Martin Carlberg
tags:
- cappuccino
- compiler
---

The new Objective-J 2.0 compiler has three components: tokenizer, parser and code generator. The merging of [this pull request](https://github.com/cappuccino/cappuccino/pull/1929) brought major improvements to the tokenizer and code generator.

### Tokenizer improvements: macros and preprocessor directives

The tokenizer now supports GCC-like macros (`#define`) and preprocessor directives (`#if`, `#else`, `#endif`) with an all new recursive token transformer. The Cappuccino framework today uses a lot of macros and directives and preprocesses all files with GCC. This improvement to the tokenizer is a major step towards removing the dependency on GCC. The GCC dependency today prevents Cappuccino itself from being compiled on Windows (although you can perfectly well run Cappuccino apps in Windows using a precompiled Cappuccino build).

One benefit for all of us is that we can start using macros and preprocessor directives in our own code, as they now work even when running from source in the browser!

#### When to use macros or preprocessor directives

Does this mean we should all start using `#define` and `#if`? The vast majority of the time, the answer is "no":

* `#define` can usually be implemented with regular variables or functions.

* `#if/#else/#endif` can be implemented with regular JavaScript `if/else`.

Macro and preprocessor directive support was added primarily to support our existing code base without needing GCC. However, in some cases macros and preprocessor directives are more convenient.

* You may decide that stylistically, using `#define` for constants is clearer than using JavaScript variables. Using a `#define` has the added advantage that it can't possibly be changed by accident as a variable can. However, be aware that you **don’t** want to use a `#define` (as opposed to a variable) for a long string, because that will end up increasing the size of your code.

* Using a macro instead of a JavaScript function has the advantage of being generated inline, thus you have access to the complete set of variables within the current scope, including `self`, whereas using a function would require passing those variables. Again, be aware that using macros could increase the size of your code and actually be slower than a JavaScript function.

* If you have a large chunk of code that is completely unused based on a `#define` constant, you can eliminate the code altogether by using `#if/#else/#endif`.

#### Examples: using #define for constants

Good use of `#define`:

    :::objj
    #define BUFFER_SIZE 1024

    for (var i = 0; i < BUFFER_SIZE; i++)
    {
        // <do buffer stuff>
    }

compiles to:

    :::js
    for (var i = 0; i < 1024; i++)
    {
        // <do buffer stuff>
    }

Bad use of `#define`:

    :::objj
    #define ERROR_MSG_FORMAT "An error occurred: %@. Would you like to continue?"

    [CPException raise:CPGenericException format:ERROR_MSG_FORMAT, someError];

    // more code

    [CPException raise:CPGenericException format:ERROR_MSG_FORMAT, anotherError];

compiles to:

    :::objj
    [CPException raise:CPGenericException format:"An error occurred: %@. Would you like to continue?", someError];

    // more code

    [CPException raise:CPGenericException format:"An error occurred: %@. Would you like to continue?", anotherError];

Notice that ERROR\_MSG\_FORMAT was replaced with the longish string every time it was referenced, which increased the size of your code. A better way:

    :::objj
    var ERROR_MSG_FORMAT = "An error occurred: %@. Would you like to continue?";

    [CPException raise:CPGenericException format:ERROR_MSG_FORMAT, someError];

    // more code

    [CPException raise:CPGenericException format:ERROR_MSG_FORMAT, anotherError];

#### Examples: using #define for macros

A reasonable use of macros:

    :::objj
    #define CreateMyJSObject(aName, anAddress) {name: aName, address: anAddress}

    var a = CreateMyJSObject("Martin", "Mainstreet");

This compiles to:

    :::objj
    var a = {name: "Martin", address: "Mainstreet"};

These macros seem quite beneficial on the surface, because they reduce function calls:

    :::objj
    #define CGRectMake(_x, _y, _width, _height)  {origin:{x:_x, y:_y}, size:{width:_width, height:_height}}

    #define CGRectMakeCopy(r)  CGRectMake(r.origin.x, r.origin.y, r.size.width, r.size.height)

    var rect = CGRectMake(10, 20, 300, 400),
        copy = CGRectMakeCopy(rect);

This compiles to:

    :::objj
    var rect = {origin:{x:10, y:20}, size:{width:300, height:400}},
        copy = {origin:{x:rect.origin.x, y:rect.origin.y}, size:{width:rect.size.width, height:rect.size.height}};

Because everything is generated inline, you end up with much larger source code. Depending on how often you use these macros, that might not be so bad. But there is a hidden performance penalty if you aren't careful. Consider this example:

    :::objj
    var rect = CGRectMake(10, 20, 300, 400),
        copy = CGRectMakeCopy([self bounds]);

which compiles to:

    :::objj
    var rect = {origin:{x:10, y:20}, size:{width:300, height:400}},
        copy = {origin:{x:[self bounds].origin.x, y:[self bounds].origin.y}, size:{width:[self bounds].size.width, height:[self bounds].size.height}};

Notice that `CGRectMakeCopy` has not only generated **way** more code than a function call, it also generates four relatively expensive method calls. Ouch!

For this reason, we actually ended replacing macros like this in Cappuccino with JavaScript functions:

    :::objj
    function CGRectMake(x, y, width, height)
    {
        return {origin:{x:x, y:y}, size:{width:width, height:height}};
    }

    function CGRectMakeCopy(rect)
    {
        return {origin:{x:rect.origin.x, y:rect.origin.y}, size:{width:rect.size.width, height:rect.size.height}};
    }

    var rect = CGRectMake(10, 20, 300, 400),
        copy = CGRectMakeCopy([self bounds]);

The compiled code is exactly the same as the written code, which is much smaller than with macros, and in this case `[self bounds]` is evaluated only once before being passed to `CGRectMakeCopy`, which is much faster.

So think twice (or thrice) before using macros!

#### Example: preprocessor directives

This code:

    :::objj
    #define BUFFER_SIZE 1024

    #if BUFFER_SIZE > 500
        // <Do large buffer size implementation>
    #else
        // <Do small buffer size implementation>
    #endif

compiles to:

    :::objj
    // <Do large buffer size implementation>

For a pre-compiled application, this can obviously reduce the size of the payload. Eventually we will add the ability to `#define` constants at compile time on the command line, which will allow you to have dynamic `#define`s without editing your source code.

#### Macro limitations

For more information about what macros can do, please read the [GCC docs](http://GCC.gnu.org/onlinedocs/cpp/Macros.html). Please note the following limitations compared to GCC macros:

* Stringification and Variadic Macros are not supported.

* Macros are only valid within the file in which they are defined.

### Code generator improvements

Previously the code generator copied the code from the source file and replaced parts of it to generate pure Javascript. Now it generates all of the code from the AST that the parser creates.

Here are some things you might notice if you look at your compiled code:

* All comments, extra whitespaces and blank lines are gone when compiling in the browser. When building from the command line GCC has always removed comments and blank lines. In the future the compiler will completely replace GCC.

* The code is generated with a fixed Cappuccino-like code style with no blank lines and uses an indent of 4 spaces.

* All redundant parentheses are removed since the code generator knows the Javascript operator precedence rules. For example, `1 + (2 * 3)` compiles to `1 + 2 * 3`.

* All modern browsers accept trailing commas in objects without choking (e.g. `[1, 2, 3,]`). But trailing commas will cause an error in IE8. The compiler now strips trailing commas from generated code so it will work correctly in IE8.

Happy coding!

\- Martin

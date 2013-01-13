
More often than not, software doesn't work on the first try. This tutorial will explain the basics of Cappuccino
debugging.

### The debugger

As mentioned in chapter on [development environment](environment.html), modern browsers provide tools to debug JavaScript. There is [Firebug](http://getfirebug.com/) for Firefox, [Debug
Bar](http://www.debugbar.com/) for Internet Explorer and the embeded
Developer tools in all WebKit browsers (Safari, Chrome, Chromium etc).
In this tutorial, we are going to use the WebKit debugger, which is one
of the most powerful tool for web application development.

### Access the debugger

Open `index.html` of the starter app in the browser. You will see the “Hello world”
label displayed.

Open the debugger. In Safari, it’s located under Development > Display Error Console. In Chrome
it's found under Presentation > Developers Options > JavaScript console.

This is what the inspector looks like in Safari:

![Main Window](tuto-debugger-0.png)

As you can see it’s empty. You have several tools you access from the
toolbar:

-   **Elements** allows you to get informations about any DOM element on
    the page, access and edit CSS rules etc. It’s very useful in
    general, but most of the time you don’t need it in Cappuccino.
-   **Resources** displays information about the webpage
    resources: images, scripts, frames and so on that
    are loaded as part of the page or available to the page.
-   **Network** allows you to monitor network access. It can be very useful
    to optimise your application. It also displays all the XHR requests.
-   **Script** is the JavaScript debugger. We’ll talk about it later
    in this tutorial
-   **Timeline** displays live information about the rendering of your page memory usage over the time.
-   **Profile** allows you to take memory heap snapshots, compare
    several snapshot, and list all the objects used in the page.
-   **Audit** mostly never works with Cappuccino apps.
-   **Console** displays log messages from your Cappuccino
    application.

We are going to mainly use Script and Console in this tutorial.

### Make your application verbose

The most basic tool in the developer's toolbox is logging.

Open the `AppController.j` of the starter app, and add the following code:

    :::objj
    // [...]
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        // [...]
        [contentView addSubview:label];
        [theWindow orderFront:self];
     
        // log the content of the label
        CPLog.info("The content of the label is: " + [label stringValue]);
    }

Reload the app, open the Debugger and select the `Console` tool. You
will see nothing!

his is normal, because you have opened `index.html` which logs nothing by default. Now open
`index-debug.html`, and select the `Console` tool:

![Console](tuto-debugger-2.png)

<span class="label label-info">Info</span>  You can enable logging in `index.html` as well by registering a logger using `CPLogRegister`.

There are 6 logging levels: `fatal`, `error`, `warn`, `info`, `debug` and `trace`. You use them with `CPLog.fatal()`, `CPLog.warn()`, `CPLog.info()` etc.

It is generally a good idea to log verbosely when you develop and then to eliminate logging statements, or to switch them to a lower level so as to suppress them when the app becomes more mature.

### The JavaScript debugger

Sometimes a problem is too complex to be cracked by logging alone, and a more powerful tool is called for: the Debugger.

Let’s add bad code in our `AppController.j`:

    :::objj
    // [...]
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        // [...]
        [contentView addSubview:label];
        [theWindow orderFront:self];

        // log the content of the label
        CPLog.info("The content of the label is: " + [label stringValue]);

        // I'm gonna crash!
        [notDefinedVariable doSomethingNotDefined:withAnotherNotDefinedVariable];
    }

Reload `index-debug.html` and look at the Console:

![Oops, an error](tuto-debugger-3.png)

The Console shows an error: `ReferenceError: Can't find variable: notDefinedVariable`. In this example the cause is obvious, but sometimes it’s not. Let’s imagine you can’t find the cause.

When an unmatched exception is logged, it’s too late to go back and
see the cause. The debugger has to be enabled **before** the error.

Go to the Script tab (Safari) or the Sources (Chrome), and click on the “Enable Debugging”
button:

![Console](tuto-debugger-4.png)

The Debugger will become activated. Make sure the icon with a stop sign and two parallel lines is blue or purple. This activates the "Pause on [uncaught] exceptions" feature.

![Console](tuto-debugger-5.png)

Reload the application. When the error occurs, the debugger will stop JavaScript execution when it encounters an exception:

![Console](tuto-debugger-6.png)

On the left side you can see the line of code in the code that caused the exception. On the right side you have the execution stack.

Note that the code has been compiled from Objective-J to JavaScript by Cappuccino at this point, so the code does not look exactly like your original code. For example:

    :::objj
    [myObject saySomething:@"hello"];

Is compiled into:

    :::objj
    objj_msgSend(myObject, "saySomething:", "hello");

If you want to delve into the depths of the Objective-J runtime, take a look at the equivalent documentation for Objective-C: [Apple’s developer documentation](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html). For the most part you don't need to understand it perfectly to find out what's wrong with your original code though.

The Call Stack shown on the right hand side of the Debugger allows you to click on earlier calls in the execution stack to inspect what was going on at that point. You can also display the content of your objects by
putting the mouse over a declaration:

![Console](tuto-debugger-7.png)

### Setting breakpoints

Breakpoints allow you to specify points where code execution should automatically pause. You can place breakpoints by clicking line numbers of code in the Scripts (Safari) or Source (Chrome) tab. Sometimes these don't stick around when you reload the app though so an easier way is to use the `debugger` statement in code.


    :::objj 
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc] initWithContentRect:CGRectMakeZero() styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView],
            label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];
     
        [label setStringValue:@"Hello World!"];
        [label setFont:[CPFont boldSystemFontOfSize:24.0]];
     
        debugger; // the breakpoint!
     
        [label sizeToFit];
     
        [label setAutoresizingMask:CPViewMinXMargin | CPViewMaxXMargin | CPViewMinYMargin | CPViewMaxYMargin];
        [label setCenter:[contentView center]];
        [contentView addSubview:label];
        [theWindow orderFront:self];
    }

If the JavaScript debugger is active when you reload the app you will see it stop execution when the `debugger` statement is executed;

![Console](tuto-debugger-8.png)

From here you can inspect the code, or single step forward using the debugger buttons.

### Wrapping Up

The WebKit’s developer tools (and JS debuggers in general) have became
extremely powerful tools. This tutorial only covers the basics. There is additional documentation available for Safari from Apple: [Apple’s
documentation](http://developer.apple.com/library/safari/#documentation/AppleApplications/Conceptual/Safari_Developer_Guide/1Introduction/Introduction.html).

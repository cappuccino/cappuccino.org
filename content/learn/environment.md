### Supported platforms

Cappuccino is supported on the following platforms:[span_68](start_span)[span_68](end_span)

| Platform | Supported features |
| :--- | :--- |
| Mac OS X | Toolchain, Interface Builder |
| Linux | Toolchain |
| Windows | Toolchain with installation of [Cygwin](http://cygwin.org) |[span_69](start_span)[span_69](end_span)

This tutorial will be written based on Mac OS X, with notes on any differences with other platforms included[span_70](start_span)[span_70](end_span).

### Downloading & Running the Sample Application

If you haven't already, download the [Cappuccino Starter package](/downloads.html)[span_71](start_span)[span_71](end_span). This zip file includes a sample application (`NewApplication`), licensing info, a script you can run later to download
all the Cappuccino tools, and a README[span_72](start_span)[span_72](end_span).

![open new application](/img/new-application.png)[span_73](start_span)[span_73](end_span)

### Running NewApplication

Once you've downloaded and unzipped the Cappuccino Starter package, open
up the `NewApplication` folder, and locate the `index.html` file[span_74](start_span)[span_74](end_span). Now,
simply open that file in your favorite web browser by double-clicking
it, or just by dragging it on top of your browser application[span_75](start_span)[span_75](end_span). You
should end up with something that looks like this (in Safari):[span_76](start_span)[span_76](end_span)

![New Application running in Safari](/img/new-app-running-safari.png)[span_77](start_span)[span_77](end_span)

> **Info:** This will only work in some browsers[span_78](start_span)[span_78](end_span). Normally you'll need to start a web server too[span_79](start_span)[span_79](end_span).
> One easy way to start a web server is to use Python: just run `python -m SimpleHTTPServer` from the folder in which your project is located[span_80](start_span)[span_80](end_span).

### The Code

The source behind this sample application is startingly simple[span_81](start_span)[span_81](end_span).
Although there are a few files, the only one we're interested in right
now is `AppController.j`[span_82](start_span)[span_82](end_span). The others are necessary, but you don't need
to modify them to work on your application[span_83](start_span)[span_83](end_span).

![AppController.j](/img/new-app-appcontroller.png)[span_84](start_span)[span_84](end_span)

You can see in the image above that we have syntax highlighting in
TextMate[span_85](start_span)[span_85](end_span). You can get this by installing the appropriate mode, found on
our [getting set up tutorial](/learn/environment.html)[span_86](start_span)[span_86](end_span).

### Making a Simple Change

Now let's see what it takes to make a simple addition to NewApplication[span_87](start_span)[span_87](end_span).
We'll add a button that toggles the text on the screen between "Hello
World!" and "Goodbye[span_88](start_span)!"[span_88](end_span). After the line that contains `[contentView
addSubview:label]` (line 31), add the following code snippet:[span_89](start_span)[span_89](end_span)

    :::objj
    var button = [[CPButton alloc] initWithFrame: CGRectMake(
                    CGRectGetWidth([contentView bounds])/2.0 - 40,
                    CGRectGetMaxY([label frame]) + 10,
                    80, 24
                 )];

    [button setAutoresizingMask:CPViewMinXMargin |
                                CPViewMaxXMargin |
                                CPViewMinYMargin |
                                CPViewMaxYMargin];

    [button setTitle:"swap"];

    [button setTarget:self];
    [button setAction:@selector(swap:)];

    [contentView addSubview:button];

Now, refresh your browser, and you should see a button right below
"Hello World[span_90](start_span)!"[span_90](end_span). It won't work just yet, because we haven't told it what
to do when the button is pressed[span_91](start_span)[span_91](end_span). Before we do that, let's quickly go
over what each of the previous lines does:[span_92](start_span)[span_92](end_span)

    :::objj
    var button = [[CPButton alloc] initWithFrame: CGRectMake(
                    CGRectGetWidth([contentView bounds])/2.0 - 40,
                    CGRectGetMaxY([label frame]) + 10,
                    80, 24
                 )];

This line instantiates a new `CPButton` object, and places it 40 pixels to
the left of the center of its parent view, and 10 pixels below the
bottom of the label above it[span_93](start_span)[span_93](end_span). It's 80 pixels wide, and 24 pixels tall[span_94](start_span)[span_94](end_span).
`CGRectMake` is the main way to create a `CGRect`, which is the object
that describes the size and positioning of every view in Cappuccino[span_95](start_span)[span_95](end_span).
`[contentView bounds]` returns the `CGRect`of `view`, but without its
positioning information[span_96](start_span)[span_96](end_span). `[label frame]` return the `CGRect` of the label,
including its position information[span_97](start_span)[span_97](end_span).

    :::objj
    [button setAutoresizingMask:CPViewMinXMargin |
                                CPViewMaxXMargin |
                                CPViewMinYMargin |
                                CPViewMaxYMargin];

Auto-resize flags define how a view resizes when its parent resizes
(all the way up to the window)[span_98](start_span)[span_98](end_span). In this case, it's saying that it would
like to have flexible space above, below, to the right, and to the left[span_99](start_span)[span_99](end_span).
In other words, stay in the center, and don't change size[span_100](start_span)[span_100](end_span).

    :::objj
    [button setTitle:"swap"];

Set the title of the button to "swap[span_101](start_span)"[span_101](end_span).

    :::objj
    [button setTarget:self];
    [button setAction:@selector(swap:)];

In Cappuccino, as in OpenStep and Cocoa, controls like buttons use the
target/action mechanism for defining their behavior[span_102](start_span)[span_102](end_span). Think of this as
the equivalent to DOM elements' onclick, but much more powerful[span_103](start_span)[span_103](end_span). In the
code above, we're setting `self` (the `AppController` instance) to be
our target, and `swap:` to be our action[span_104](start_span)[span_104](end_span). This means that when the
button is pressed, we'll send the `swap:` message to `self`, which
would be equivalent to writing `[self swap:button]`[span_105](start_span)[span_105](end_span). You'll notice
`swap:` takes one parameter[span_106](start_span)[span_106](end_span). By default, actions usually have one
parameter, called `sender`, so that you can know who is requesting
this action take place (in this case it is the button)[span_107](start_span)[span_107](end_span). This can provide
useful context when multiple buttons or views have the same target and
action[span_108](start_span)[span_108](end_span).

    :::objj
    [contentView addSubview:button];

Finally, in this last line, we add our button as a subview of the
window's content view[span_109](start_span)[span_109](end_span). The content view is the root view of a window,
and so the first place you'd put any additional views[span_110](start_span)[span_110](end_span).

As it currently stands, `label` is scoped to just exist within
`applicationDidFinishLaunching:`, which means it won't be accessible in
`swap:` or any other methods[span_111](start_span)[span_111](end_span). So instead of making it a local variable,
lets make it an **instance variable** of `AppController`[span_112](start_span)[span_112](end_span). To do this we
simply need to add it to our class declaration by replacing:[span_113](start_span)[span_113](end_span)

    :::objj
    @implementation AppController : CPObject
    {
    }

with:[span_114](start_span)[span_114](end_span)

    :::objj
    @implementation AppController : CPObject
    {
        CPTextField label;
    }

Now, let's take out the var keyword in the original declaration of
`label`[span_115](start_span)[span_115](end_span).

    var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

becomes:[span_116](start_span)[span_116](end_span)

    label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

Now we need to actually add the swap method[span_117](start_span)[span_117](end_span). Add the following code
after the closing bracket of the `applicationDidFinishLaunching:`
method:[span_118](start_span)[span_118](end_span)

    - (void)swap:(id)sender
    {
        if ([label stringValue] == "Hello World!")
            [label setStringValue:"Goodbye!"];
        else
            [label setStringValue:"Hello World!"];
    }

This code checks what the current value of `label` is and uses that to
decide what to set the new value to[span_119](start_span)[span_119](end_span).

Now you should be able to run this new code by saving `AppController.j`
and hitting refresh in your browser[span_120](start_span)[span_120](end_span). Click the button, and you should
see the string change back and forth between "Hello World!" and
"Goodbye[span_121](start_span)!"[span_121](end_span).

For a finishing touch, add this line after you create the label in
`applicationDidFinishLaunching:`[span_122](start_span)[span_122](end_span)

    [label setAlignment:CPCenterTextAlignment];

Now the text will be centered as it toggles back and forth[span_123](start_span)[span_123](end_span). For the
complete changes, you can download this copy of
[AppController.j](/learn/files/AppController.j)[span_124](start_span)[span_124](end_span).

![finished version](/img/new-app-completed.png)[span_125](start_span)[span_125](end_span)

### Wrapping Up

This concludes our quick introduction to the Cappuccino Starter package,
and to modifying your first application[span_126](start_span)[span_126](end_span). Now that you've got your feet
wet, you can move on to a more advanced tutorial[span_127](start_span)[span_127](end_span).

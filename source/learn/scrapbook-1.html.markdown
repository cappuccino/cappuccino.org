### An introduction to Cappuccino Graphics

This tutorial is the first in a multi-part series in which we will be
building a full featured Scrapbooking application, complete with backend
storage. The goal of these tutorials is to start off simple and
incrementally add features, mimicking the development of a real world
application and allowing us to focus on different aspects of Cappuccino
along the way. For this first installment, we will be getting familiar
with Cappuccino's view hierarchy and graphics subsystem.

### The Idea

Before we jump into any serious programming, let's begin by getting a
good idea of what we're building. The goal of the scrapbook application
is to provide users with a place to arrange their photos into albums.
These albums will have different themes and allow users to insert,
scale, rotate, and crop their images. When done, they will be able to
save and share their albums.

As I mentioned earlier, we will be focusing on some of the core
graphical aspects of this application right now, and saving most of the
overall design decisions of this application for later. So the very
first thing we're going to tackle is building a solid UI for scaling and
cropping images. The plan is to present the user with a few controls in
a heads up display which will allow them to manipulate selected images,
and then go away when the user is done editing. You can see a working
example of this [here](/learn/demos/Scrapbook/Part%201/index-debug.html). You should
take a few minutes to play around with it and get an idea of what we
will be building. You can also view or download the entire source of the
application [here](https://github.com/cappuccino/cappuccino-demos/tree/master/Scrapbook/Part%201) if you
prefer to follow along with the code.

![Completed App](scrapbook-1-completed.png)

### Setting Up the Project

Since we're not doing anything too complex yet, we're going to build off
of the [Starter Template](/downloads.html). Open up `AppController.j` and
delete all the code relating to the HelloWorld textfield, such that all
that is left in `applicationDidFinishLaunching:` is the following:

    :::objj
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc]
                            initWithContentRect:CGRectMakeZero()
                            styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView];

        [theWindow orderFront:self];
    }

If you now rerun this application by hitting refresh, you will see that
nothing shows up on the screen. So let's take a moment to understand
what is going on in these very few lines of code.

In Cappuccino, all view hierarchies start from within a `CPWindow`. So
to get anything to display on the screen, we first require the creation
of a window. `CPWindow`s should not be confused with the browser window
however. `CPWindow`s exist within the main browser window, and there can
be multiple of them. The relationship between `CPWindow` and the browser
window is similar to that between Desktop windows and the screen. In
Cappuccino, we often refer to the browser window as the `bridge`,
since the browser window bridges the web to the desktop.

When you create a `CPWindow`, you generally specify the content
rectangle and style mask. The content rectangle describes the position
and size of the inner content ignoring the chrome around it. The style
mask describes the chrome, or look, of the window. In this case, we are
creating a window with the "borderless bridge" look. The borderless
bridge style describes a `CPWindow` with no chrome at all, and that
takes up the entire size of the browser window, which is why we don't
bother sending a meaningful value in for the content rectangle -- it
gets set automatically for us. The `CPBorderlessWindowMask` is similar
to this, but does not follow the size of the browser window.

Now, the `contentView` of a `CPWindow` is the root view class of a
window. This is where you will be putting all of your custom UI, such as
buttons, text fields, etc. Let's go ahead and set the color of our
content view to be black by adding this code right after the
declaration:

    :::objj
    [contentView setBackgroundColor:[CPColor blackColor]];

If you refresh now, you'll see that the entire browser window has turned
black. This is because, as we described earlier, borderless bridge
windows "fit" their parent browser windows.

### Photo Inspector

Since we're on the topic of windows, let's go ahead and make our
heads-up-display (HUD) controller that we mentioned earlier. First,
let's just make a HUD panel. A panel is a type of window that floats on
top of other windows. Create a panel in the `applicationDidFinishLaunching:` method:

    :::objj
    var HUDPanel = [[CPPanel alloc]
        initWithContentRect:CGRectMake(0, 0, 225, 125)
        styleMask:CPHUDBackgroundWindowMask | CPClosableWindowMask];

    [HUDPanel setFloatingPanel:YES];

    [HUDPanel orderFront:self];

Now if you refresh, you'll see a little HUD panel show up at the top
left corner of your screen. You can drag on it to move it around, and
click on the close box to close it. As you can see, in this case we
specified an actual content rectangle since we aren't relying on the
panel simply stretching to the entire size of the bridge. We chose two
style masks in this case: `CPHUDBackgroundWindowMask` and
`CPClosableWindowMask`. `CPHUDBackgroundWindowMask` notifies our
panel that we want the HUD look, and `CPClosableWindowMask` lets the
panel know that it should display its close box. If you remove the
`CPClosableWindowMask` mask, you will no longer be able to close the
panel.

![](scrapbook-1-just-inspector.png)

Let's start giving the panel some contents. The easiest thing to add is
a title:

    :::objj
    [HUDPanel setTitle:"Inspector"];

We will now add our two sliders to control the scale and rotation of our
photos. To do this we will use the `CPSlider` class. Just as we did with
the main window, we will grab the contentView of the HUD panel to place
these sliders in:

    :::objj
    var panelContentView = [HUDPanel contentView],
        centerX = (CGRectGetWidth([panelContentView bounds]) - 135.0) / 2.0;

    var scaleSlider = [[CPSlider alloc] initWithFrame:CGRectMake(centerX, 13.0, 135.0, 24.0)];

    [scaleSlider setMinValue:50];
    [scaleSlider setMaxValue:150];
    [scaleSlider setValue:100];

    [panelContentView addSubview:scaleSlider];

    var scaleStartLabel = [self labelWithTitle:"50%"],
        scaleEndLabel = [self labelWithTitle:"150%"];

    [scaleStartLabel setFrameOrigin:CGPointMake(
        centerX - CGRectGetWidth([scaleStartLabel frame]), 10)];
    [scaleEndLabel setFrameOrigin:
        CGPointMake(CGRectGetMaxX([scaleSlider frame]), 10)];

    [panelContentView addSubview:scaleStartLabel];
    [panelContentView addSubview:scaleEndLabel];

    rotationSlider = [[CPSlider alloc] initWithFrame:
        CGRectMake(centerX, 43, 135, 24)];

    [rotationSlider setMinValue:0];
    [rotationSlider setMaxValue:360];
    [rotationSlider setValue:0];

    [panelContentView addSubview:rotationSlider];

    var rotationStartLabel = [self labelWithTitle:"0\u00B0"],
        rotationEndLabel = [self labelWithTitle:"360\u00B0"];

    [rotationStartLabel setFrameOrigin:CGPointMake(centerX - CGRectGetWidth([rotationStartLabel frame]), 40)];
    [rotationEndLabel setFrameOrigin:CGPointMake(CGRectGetMaxX([rotationSlider frame]), 40)];

    [panelContentView addSubview:rotationStartLabel];
    [panelContentView addSubview:rotationEndLabel];

You'll notice this makes use of the `labelWithTitle:` method that we
have not yet defined. Go ahead and define it in AppController like so:

    :::objj
    - (CPTextField)labelWithTitle:(CPString)aTitle
    {
        var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

        [label setStringValue:aTitle];
        [label setTextColor:[CPColor whiteColor]];

        [label sizeToFit];

        return label;
    }

This may seem daunting, but it’s really not that complex. Let's start by
analyzing the `labelWithTitle:` method. It should look familiar, since
it’s almost identical to the code that was in the original
implementation of `applicationDidFinishLaunching:`. All we are doing is
creating a text field, setting its text contents to be `aTitle`,
setting its text color to white, and finally sizing it appropriately and
returning it.

In the slider creation code we are creating two sliders: one to modify
scale and another for rotation, so we only really need to go over half
the code. We are making our sliders **135 pixels** wide, so begin by
calculating the center position in our panel's content view. After we
have this, We create a new slider at this position. We then set three
important values for sliders: the minimum value, the maximum value, and
the current value. The minimum value is what the left hand side of the
slider represents, the maximum is what the right hand side represents,
and the current value is simply where the knob of the slider currently
resides. In this case of the `scaleSlider`, we want to be able to
scale our photos from 50% to 150%, and obviously we want them to begin
at 100%. With the rotationSlider, we want to go from 0 degrees to 360
degrees, and start at 0 degrees. To highlight these values, we create 2
labels for each slider to sit to the left and to the right of the
sliders. So, your code should now look like this:

    :::objj
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc]
                            initWithContentRect:CGRectMakeZero()
                            styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView];

        [theWindow orderFront:self];

        var HUDPanel = [[CPPanel alloc]
            initWithContentRect:CGRectMake(0, 0, 225, 125)
            styleMask:CPHUDBackgroundWindowMask | CPClosableWindowMask];

        [HUDPanel setFloatingPanel:YES];

        [HUDPanel orderFront:self];

        [HUDPanel setTitle:"Inspector"];

        var panelContentView = [HUDPanel contentView],
            centerX = (CGRectGetWidth([panelContentView bounds])
            - 135) / 2;

        var scaleSlider = [[CPSlider alloc]
            initWithFrame:CGRectMake(centerX, 13, 135, 24)];

        [scaleSlider setMinValue:50];
        [scaleSlider setMaxValue:150];
        [scaleSlider setValue:100];

        [panelContentView addSubview:scaleSlider];

        var scaleStartLabel = [self labelWithTitle:"50%"],
            scaleEndLabel = [self labelWithTitle:"150%"];

        [scaleStartLabel setFrameOrigin:CGPointMake(centerX -
            CGRectGetWidth([scaleStartLabel frame]), 10)];
        [scaleEndLabel setFrameOrigin:
            CGPointMake(CGRectGetMaxX([scaleSlider frame]), 10)];

        [panelContentView addSubview:scaleStartLabel];
        [panelContentView addSubview:scaleEndLabel];

        rotationSlider = [[CPSlider alloc]
            initWithFrame:CGRectMake(centerX, 43, 135, 24)];

        [rotationSlider setMinValue:0];
        [rotationSlider setMaxValue:360];
        [rotationSlider setValue:0];

        [panelContentView addSubview:rotationSlider];

        var rotationStartLabel = [self labelWithTitle:"0\u00B0"],
            rotationEndLabel = [self labelWithTitle:"360\u00B0"];

        [rotationStartLabel setFrameOrigin:CGPointMake(centerX -
            CGRectGetWidth([rotationStartLabel frame]), 40)];
        [rotationEndLabel setFrameOrigin:
            CGPointMake(CGRectGetMaxX([rotationSlider frame]), 40)];

        [panelContentView addSubview:rotationStartLabel];
        [panelContentView addSubview:rotationEndLabel];
    }

    - (CPTextField)labelWithTitle:(CPString)aTitle
    {
        var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

        [label setStringValue:aTitle];
        [label setTextColor:[CPColor whiteColor]];

        [label sizeToFit];

        return label;
    }

    @end

We now have a functioning panel, but it's not much good to us here
within the `applicationDidFinishLaunching:` method. So let's create a
new file called `PhotoInspector.j` to contain it.

In `PhotoInspector.j`, we will be creating a subclass of
`CPWindowController` to manage this panel. `CPWindowController`s are
designed to manage `CPWindow`s and their interactions with other
objects. Once we've create this class, we'll move all the relevant code
to it, namely the `labelWithTitle` method and view creation code:

    :::objj
    @import <AppKit/CPPanel.j>
    @import <AppKit/CPWindowController.j>

    @implementation PhotoInspector : CPWindowController
    {
    }

    - (id)init
    {
        var theWindow = [[CPPanel alloc]
            initWithContentRect:CGRectMake(0, 0, 225, 125)
            styleMask:CPHUDBackgroundWindowMask | CPClosableWindowMask];

        self = [super initWithWindow:theWindow];

        if (self)
        {
            [theWindow setTitle:@"Inspector"];
            [theWindow setFloatingPanel:YES];

            var contentView = [theWindow contentView],
                centerX = (CGRectGetWidth([contentView bounds]) - 135) / 2;

            scaleSlider = [[CPSlider alloc]
                initWithFrame:CGRectMake(centerX, 13, 135, 24)];

            [scaleSlider setMinValue:50];
            [scaleSlider setMaxValue:150];
            [scaleSlider setValue:100];

            [contentView addSubview:scaleSlider];

            var scaleStartLabel = [self labelWithTitle:"50%"],
                scaleEndLabel = [self labelWithTitle:"150%"];

            [scaleStartLabel setFrameOrigin:CGPointMake(centerX -
                CGRectGetWidth([scaleStartLabel frame]), 10)];
            [scaleEndLabel setFrameOrigin:
                CGPointMake(CGRectGetMaxX([scaleSlider frame]), 10)];

            [contentView addSubview:scaleStartLabel];
            [contentView addSubview:scaleEndLabel];

            rotationSlider = [[CPSlider alloc]
                initWithFrame:CGRectMake(centerX, 43, 135, 24)];

            [rotationSlider setMinValue:0];
            [rotationSlider setMaxValue:360];
            [rotationSlider setValue:0];

            [contentView addSubview:rotationSlider];

            var rotationStartLabel = [self labelWithTitle:"0\u00B0"],
                rotationEndLabel = [self labelWithTitle:"360\u00B0"];

            [rotationStartLabel setFrameOrigin:CGPointMake(centerX -
                CGRectGetWidth([rotationStartLabel frame]), 40)];
            [rotationEndLabel setFrameOrigin:
                CGPointMake(CGRectGetMaxX([rotationSlider frame]), 40)];

            [contentView addSubview:rotationStartLabel];
            [contentView addSubview:rotationEndLabel];
        }

        return self;
    }

    - (CPTextField)labelWithTitle:(CPString)aTitle
    {
        var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

        [label setStringValue:aTitle];
        [label setTextColor:[CPColor whiteColor]];

        [label sizeToFit];

        return label;
    }

    @end

As you can see very little of the code has changed. The only real
addition is calling `initWithWindow:` in the new `init` method. This is
the standard way to create window controllers. We can now modify our
AppController code to the following:

    :::objj
    @import <Foundation/CPObject.j>
    @import "PhotoInspector.j"

    @implementation AppController : CPObject
    {
    }

    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc]
                            initWithContentRect:CGRectMakeZero()
                            styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView];

        [contentView setBackgroundColor:[CPColor blackColor]];

        [theWindow orderFront:self];

        var theInspector = [[PhotoInspector alloc] init];

        [theInspector showWindow:self];
    }

    @end

This successfully encapsulates the inspector panel away. To bring it up
all we need to do now is call `showWindow:` on our `PhotoInspector`
class, which we inherit for free from `CPWindowController`. You'll
notice we also had to include the `PhotoInspector` class' file
`PhotoInspector.j`. We use quotes to include this file because it is
local, as opposed to the AppKit files which are in our default search
paths.

### Building the Beginnings of our PageView

Now that we have a photo inspector, we need some photos to inspect. In
our product, Scrapbook will be represented as a series of pages. Each
page will contain a number of panes that each contain an image. These
pages will be represented by `PageView`s, so let's start fleshing out
our `PageView` class in a file called `PageView.j`.

    :::objj
    @import <AppKit/CPView.j>

    @implementation PageView : CPView
    {
    }

    @end

As you can see, `PageView` is a subclass of `CPView`, the core UI class
in Cappuccino. However, we will actually be doing the brunt of our
graphics work not in a view, but in a `layer`. In Cappuccino,
`CALayer`s are designed and optimized for drawing and performing complex
graphics routines, whereas `CPView`s are better at handling UI widgets.
We can add layers to views by making them **layer-backed**:

    :::objj
    @implementation PageView : CPView
    {
        CALayer _rootLayer;
    }

    - (id)initWithFrame:(CGRect)aFrame
    {
        self = [super initWithFrame:aFrame];

        if (self)
        {
            _rootLayer = [CALayer layer];

            [self setWantsLayer:YES];
            [self setLayer:_rootLayer];

            [_rootLayer setBackgroundColor:[CPColor whiteColor]];

            [_rootLayer setNeedsDisplay];
        }

        return self;
    }

    @end

Here we create the view as usual, but let the view know that it will be
hosting a layer with the `setWantsLayer:` method, and adding the actual
layer with `setLayer:`. We give the layer a background color, but need
to call `setNeedsDisplay` for the layer to actually show itself. In
Cappuccino, you never explicitly tell views or layers to draw, instead
you inform them that they need to do so. This is because Cappuccino
coalesces and optimizes drawing.

As we said earlier, we now need a pane in this page. Pane's hold images
as well as storing the scale and rotation properties of the image it
displays. We will be implementing panes as layers:

    :::objj
    @implementation PaneLayer : CALayer
    {
        float       _rotationRadians;
        float       _scale;

        CPImage     _image;
        CALayer     _imageLayer;

        PageView    _pageView;
    }

    - (id)initWithPageView:(PageView)aPageView
    {
        self = [super init];

        if (self)
        {
            _pageView = aPageView;

            _rotationRadians = 0.0;
            _scale = 1.0;

            _imageLayer = [CALayer layer];
            [_imageLayer setDelegate:self];

            [self addSublayer:_imageLayer];
        }

        return self;
    }

    - (PageView)pageView
    {
        return _pageView;
    }

    - (void)setBounds:(CGRect)aRect
    {
        [super setBounds:aRect];

        [_imageLayer setPosition:
            CGPointMake(CGRectGetMidX(aRect),
            CGRectGetMidY(aRect))];
    }

    - (void)setImage:(CPImage)anImage
    {
        if (_image == anImage)
            return;

        _image = anImage;

        if (_image)
            [_imageLayer setBounds:CGRectMake(0.0, 0.0,
                [_image size].width, [_image size].height)];

        [_imageLayer setNeedsDisplay];
    }

    - (void)setRotationRadians:(float)radians
    {
        if (_rotationRadians == radians)
            return;

        _rotationRadians = radians;

        [_imageLayer setAffineTransform:CGAffineTransformScale(
            CGAffineTransformMakeRotation(_rotationRadians),
            _scale, _scale)];
    }

    - (void)setScale:(float)aScale
    {
        if (_scale == aScale)
            return;

        _scale = aScale;

        [_imageLayer setAffineTransform:CGAffineTransformScale(
            CGAffineTransformMakeRotation(_rotationRadians),
            _scale, _scale)];
    }

    - (void)drawInContext:(CGContext)aContext
    {
        CGContextSetFillColor(aContext, [CPColor grayColor]);
        CGContextFillRect(aContext, [self bounds]);
    }

    - (void)imageDidLoad:(CPImage)anImage
    {
        [_imageLayer setNeedsDisplay];
    }

    - (void)drawLayer:(CALayer)aLayer inContext:(CGContext)aContext
    {
        var bounds = [aLayer bounds];

        if ([_image loadStatus] !=
            CPImageLoadStatusCompleted)
            [_image setDelegate:self];
        else
            CGContextDrawImage(aContext, bounds, _image);
    }

    @end

That's the entire `PaneLayer` class and it's pretty straight forward. I
just put it in `PageView.j` for now right before the implementation of
`PageView`. You can choose put it in a separate file, but don't forget
to import it in `PageView.j` if you do.

Let's start by looking at the insance variables. As I said, the pane
layer keeps an image, rotation, and scale, represented here by
`_image`, `_rotationRadians`, and `_scale`. We have two
additional members though: `_imageLayer`, which we will use to draw
the image, and `_pageView`, which just gives us a reference to our
owning page.

In `initWithPageView:` we set up our default values. Clearly we'd like
the image to start off unrotated and unscaled. We also create our
internal `_imageLayer` and set ourselves to be the `delegate` with
`setDelegate:`. Delegates are an important concept in Cappuccino,
because they allow you to modify the behavior of classes without having
to subclass them. Many classes in Cappuccino allow you to supply a
delegate, and then call several methods on that delegate. In this case,
we set ourselves as the delegate of the image layer class because we
want to implement `drawLayer:inContext:`

    :::objj
    - (void)drawLayer:(CALayer)aLayer inContext:(CGContext)aContext
    {
        var bounds = [aLayer bounds];

        if ([_image loadStatus] != CPImageLoadStatusCompleted)
            [_image setDelegate:self];
        else
            CGContextDrawImage(aContext, bounds, _image);
    }

This **delegate method** allows another class to draw within the
`_imageLayer`. In this case all we're doing is drawing our image into
the layer. `aContext` is the drawing context of the layer in question,
and we use `CGContextDrawImage` to render `_image` to the rectangle
`bounds`. This just means that we always want the image to fit the
entire width and height of the layer. Notice that we use delegates once
more though: If the image hasn't completed loading, we set ourselves as
the delegate of the image. Once the image has completed loading, it will
send its delegate the `imageDidLoad:` message:

    :::objj
    - (void)imageDidLoad:(CPImage)anImage
    {
        [_imageLayer setNeedsDisplay];
    }

So once the image has completed loading, we just tell our
`_imageLayer` that it needs to redisplay itself because it has new
information to show. The other drawing function we have is the layer's
own `drawInContext:`, where all we do is draw gray since this will be
the background color of our pane.

The rest of the methods are now prety straight forward since they are
just **setters** and **getters** for our existing properties. We supply
the `pageView` method to allow one to get the owning page view. We
override `setBounds:` to keep the internal `_imageLayer` centered,
and we use `setImage:` to set the image of the layer:

    :::objj
    - (void)setImage:(CPImage)anImage
    {
        if (_image == anImage)
            return;

        _image = anImage;

        if (_image)
            [_imageLayer setBounds:CGRectMake(0.0, 0.0,
                [_image size].width, [_image size].height)];

        [_imageLayer setNeedsDisplay];
    }

We use the information from the image to set the size of the
`_imageLayer`, since we want them to match. We also once again inform
our `_imageLayer` that it needs to redraw because it now has a new
image.

The last two methods are the most interesting and where the magic
happens. Both `setScale:` and `setRotationRadians:` use the built in
transformation methods to adjust the `_imageLayer`. In both cases we
simply take our two values and create a `transform` with them. This is
all that is necessary in Cappuccino to rotate and scale layers.

    :::objj
    - (void)setRotationRadians:(float)radians
    {
        if (_rotationRadians == radians)
            return;

        _rotationRadians = radians;

        [_imageLayer setAffineTransform:CGAffineTransformScale(
            CGAffineTransformMakeRotation(_rotationRadians),
            _scale, _scale)];
    }

    - (void)setScale:(float)aScale
    {
        if (_scale == aScale)
            return;

        _scale = aScale;

        [_imageLayer setAffineTransform:CGAffineTransformScale(
            CGAffineTransformMakeRotation(_rotationRadians),
            _scale, _scale)];
    }

Let's now go ahead and create a simple pane within our page view:

    :::objj
    @implementation PageView : CPView
    {
        CALayer     _rootLayer;

        PaneLayer   _paneLayer;
    }

    - (id)initWithFrame:(CGRect)aFrame
    {
        self = [super initWithFrame:aFrame];

        if (self)
        {
            _rootLayer = [CALayer layer];

            [self setWantsLayer:YES];
            [self setLayer:_rootLayer];

            [_rootLayer setBackgroundColor:
                [CPColor whiteColor]];

            _paneLayer = [[PaneLayer alloc]
                initWithPageView:self];

            [_paneLayer setBounds:CGRectMake(0, 0,
                400 - 2 * 40, 400. - 2 * 40)];
            [_paneLayer setAnchorPoint:CGPointMakeZero()];
            [_paneLayer setPosition:CGPointMake(40, 40)];

            [_paneLayer setImage:[[CPImage alloc]
                initWithContentsOfFile:
                @"Resources/sample.jpg"
                size:CGSizeMake(500, 430)]];

            [_rootLayer addSublayer:_paneLayer];

            [_paneLayer setNeedsDisplay];

            [_rootLayer setNeedsDisplay];
        }

        return self;
    }

    @end

For now we are just going to use a default image for our pane, which you
can download [here](https://raw.github.com/cappuccino/cappuccino-demos/master/Scrapbook/Part%201/Resources/sample.jpg) and put into a
folder called "Resources". We set the size of the `_paneLayer` with
`setBounds:`, and the position of the layer with a combination of
`setAnchorPoint:` and `setPosition:`. This is because unlike `CPView`s,
by default the `position` of a `CALayer` refers to the position of its
center point. To make the `position` refer to the top left corner, we
have to specify an achor point of **(0.0, 0.0)**.

### Wrapping Up

We are now almost done with our application. All that is left is to
bring together the photo inspector and the page view. The photo
inspector will essentially "edit" the page views, so let's add the
following code after `[_rootLayer addSublayer:_paneLayer]` in
`initWithFrame:`

    :::objj
    _borderLayer = [CALayer layer];

    [_borderLayer setAnchorPoint:CGPointMakeZero()];
    [_borderLayer setBounds:[self bounds]];
    [_borderLayer setDelegate:self];

    [_rootLayer addSublayer:_borderLayer];

Also add `_borderLayer` to PageView's declaration:

    :::objj
    @implementation PageView : CPView
    {
        CALayer     _borderLayer;
        CALayer     _rootLayer;

        PaneLayer   _paneLayer;
    }

The border layer is meant to draw the borders of the panes. Once again
we are making ourselves the delegate of `_borderLayer`, so add
`drawLayer:inContext:` to `PageView`

    :::objj
    - (void)drawLayer:(CALayer)aLayer inContext:(CGContext)aContext
    {
        CGContextSetFillColor(aContext, [CPColor whiteColor]);

        var bounds = [aLayer bounds],
            width = CGRectGetWidth(bounds),
            height = CGRectGetHeight(bounds);

        CGContextFillRect(aContext, CGRectMake(0, 0, width, 40));
        CGContextFillRect(aContext, CGRectMake(0, 40,
            40, height - 2 * 40));
        CGContextFillRect(aContext, CGRectMake(width - 40, 40,
            40, height - 2 * 40));
        CGContextFillRect(aContext, CGRectMake(0, height - 40,
            width, 40));
    }

Here we are just drawing a few white-filled rectangles to be the borders
of our internal pane. We can now add a new method called `setEditing:`
to our page view:

    :::objj
    - (void)setEditing:(BOOL)isEditing
    {
        [_borderLayer setOpacity:isEditing ? 0.5 : 1.0];
    }

What this method does is make the border of our pane semi-transparent
when we are editing. That way as you scale and rotate you can still see
much of the full image despite it being "inside" the pane.

We will now return to our `PhotoInspector` class to make it aware of
these two new classes we've created. Start by adding a `PaneLayer` to
the `PhotoInspector` declaration:

    :::objj
    @import <AppKit/CPWindowController.j>
    @import "PageView.j"

    @implementation PhotoInspector : CPWindowController
    {
        CPSlider    _scaleSlider;
        CPSlider    _rotationSlider;

        PaneLayer   _paneLayer;
    }

Now let's add a few methods to make the PhotoInspector a `singleton`,
since there's only ever one used in the application:

    :::objj
    var PhotoInspectorSharedInstance    = nil;

    @implementation PhotoInspector : CPWindowController
    {
        CPSlider    _scaleSlider;
        CPSlider    _rotationSlider;

        PaneLayer   _paneLayer;
    }

    + (PhotoInspector)sharedPhotoInspector
    {
        if (!PhotoInspectorSharedInstance)
            PhotoInspectorSharedInstance = [[PhotoInspector alloc] init];

        return PhotoInspectorSharedInstance;
    }

You can now get at the shared `PhotoInspector` instance by calling
`[PhotoInspector sharedPhotoInspector]`. Notice that this method begins
with a plus instead of a minus. That's because this is a **class
method**. Also, we declared a **file local** variable to store the
shared instance at the top with this line:

    :::objj
    var PhotoInspectorSharedInstance    = nil;

Unlike JavaScript, varing variables in a file does trap them in that
file's scope, so this variable will only be accessible through the
`sharedPhotoInspector` method.

We will now add the setter for the `_paneLayer` member, which
represents the pane and image that the photo inspector is currently
inspecting:

    :::objj
    - (void)setPaneLayer:(PaneLayer)anPaneLayer
    {
        if (_paneLayer == anPaneLayer)
            return;

        [[_paneLayer pageView] setEditing:NO];

        _paneLayer = anPaneLayer;

        var page = [_paneLayer pageView];

        [page setEditing:YES];

        if (_paneLayer)
        {
            var frame = [page convertRect:[page bounds] toView:nil],
                windowSize = [[self window] frame].size;

            [[self window] setFrameOrigin:
                CGPointMake(CGRectGetMidX(frame) -
                windowSize.width / 2.0, CGRectGetMidY(frame))];
        }
    }

As you can see, when we pass in a new pane layer, we first do a little
bit of cleanup on our old pane layer if we have one. We tell its
corresponding page view that we are no longer editing, and then tell the
new pane layer's page view that we are editing (thus dimming the border
described above). We then position our window at the center of the pane.

Let's actually make our two sliders useful now by giving them
`targets` and `actions` in our `init` method after they are created:

    :::objj
    [rotationSlider setTarget:self];
    [rotationSlider setAction:@selector(rotate:)];

>

    :::objj
    [scaleSlider setTarget:self];
    [scaleSlider setAction:@selector(scale:)];

Targets and actions are kind of like callbacks, but object-oriented and
much more powerful. Instead of supplying a callback `function`, you
supply both a callback object, or target, and a callback method to call
on that object. In this case, when we move the `rotationSlider`, we
will have `rotate:` called on `self` (the `PhotoInspector` instance),
and when we move the `scaleSlider`, `scale:` will be called.

We of course must implement `scale:` and `rotate:` in `PhotoInspector`
for this to be useful at all:

    :::objj
    - (void)scale:(id)aSender
    {
        [_paneLayer setScale:[aSender value] / 100.0];
    }

    - (void)rotate:(id)aSender
    {
        [_paneLayer setRotationRadians:PI / 180 * [aSender value]];
    }

All we do in these two methods is make use of the setters we implemented
in the `PaneLayer` class. You might have noticed that our code is
curiously devoid of the null-checks you so often find in JavaScript,
Java, C++, etc. That's because Objective-J just ignores messages sent to
nil, so instead of having to do:

    :::objj
    if (myObject)
        [myObject method];

You can safely do:

    :::objj
    [myObject method];

We are going to add two more methods to PhotoInspector to complete it:

    :::objj
    + (void)inspectPaneLayer:(PaneLayer)anPaneLayer
    {
        var inspector = [self sharedPhotoInspector];

        [inspector setPaneLayer:anPaneLayer];

        [inspector showWindow:self];
    }

    - (void)windowWillClose:(id)aSender
    {
        [self setPaneLayer:nil];
    }

The first just provides a shorthand for bringing up the inspector and
telling it to inspect a certain `PaneLayer`. The second handles the case
when the inspector window is closed: we certainly don't want to leave
the currently editing pane in editing mode, so we set our editing pane
to be `nil`. However, to receive the `windowDidCLose:` method, we must
make ourselves the delegate of our window, which we can do in the init
method:

    :::objj
    //...
    if (self)
    {
        [theWindow setTitle:@"Inspector"];
        [theWindow setFloatingPanel:YES];

        [theWindow setDelegate:self];
    //...

Our `PhotoInspector` is now complete, we just need to bring it up when
we double click on our page view. To do this, let's return to the
PageView class and add a `mouseDown:` method:

    :::objj
    - (void)mouseDown:(CPEvent)anEvent
    {
        if ([anEvent clickCount] == 2)
            [PhotoInspector inspectPaneLayer:_paneLayer];
    }

There is no need to register for events in Cappuccino as you might do in
JavaScript, simply implement on of the event handling methods such as
`mouseDown:` and you will receive the event. Here, we simply check the
click count of the mouse down event and inspect our single pange if it
is a double click.

To finish this application, put the following in your
`applicationDidFinishLaunching:` to make a sample `PageView`:

    :::objj
    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc]
                initWithContentRect:CGRectMakeZero()
                styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView];

        [contentView setBackgroundColor:[CPColor blackColor]];

        [theWindow orderFront:self];

        var bounds = [contentView bounds],
            pageView = [[PageView alloc] initWithFrame:
                CGRectMake(CGRectGetWidth(bounds) / 2
                - 200, CGRectGetHeight(bounds) / 2 - 200,
                400, 400)];

        [pageView setAutoresizingMask:  CPViewMinXMargin |
                                        CPViewMaxXMargin |
                                        CPViewMinYMargin |
                                        CPViewMaxYMargin];

        [contentView addSubview:pageView];

        var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

        [label setTextColor:[CPColor whiteColor]];
        [label setStringValue:@"Double Click to Edit Photo"];

        [label sizeToFit];
        [label setFrameOrigin:CGPointMake(CGRectGetWidth(bounds) / 2 -
            CGRectGetWidth([label frame]) / 2,
            CGRectGetMinY([pageView frame]) -
            CGRectGetHeight([label frame]))];
        [label setAutoresizingMask: CPViewMinXMargin |
                                    CPViewMaxXMargin |
                                    CPViewMinYMargin |
                                    CPViewMaxYMargin];

        [contentView addSubview:label];
    }

Your `AppController.j` should now look something like this:

    :::objj
    @import <Foundation/CPObject.j>

    @import "PageView.j"
    @import "PhotoInspector.j"


    @implementation AppController : CPObject
    {
    }

    - (void)applicationDidFinishLaunching:(CPNotification)aNotification
    {
        var theWindow = [[CPWindow alloc]
                initWithContentRect:CGRectMakeZero()
                styleMask:CPBorderlessBridgeWindowMask],
            contentView = [theWindow contentView];

        [contentView setBackgroundColor:[CPColor blackColor]];

        [theWindow orderFront:self];

        var bounds = [contentView bounds],
            pageView = [[PageView alloc] initWithFrame:
                CGRectMake(CGRectGetWidth(bounds) / 2
                - 200, CGRectGetHeight(bounds) / 2 - 200,
                400, 400)];

        [pageView setAutoresizingMask:  CPViewMinXMargin |
                                        CPViewMaxXMargin |
                                        CPViewMinYMargin |
                                        CPViewMaxYMargin];

        [contentView addSubview:pageView];

        var label = [[CPTextField alloc] initWithFrame:CGRectMakeZero()];

        [label setTextColor:[CPColor whiteColor]];
        [label setStringValue:@"Double Click to Edit Photo"];

        [label sizeToFit];
        [label setFrameOrigin:CGPointMake(CGRectGetWidth(bounds) / 2 -
            CGRectGetWidth([label frame]) / 2,
            CGRectGetMinY([pageView frame]) -
            CGRectGetHeight([label frame]))];
        [label setAutoresizingMask: CPViewMinXMargin |
                                    CPViewMaxXMargin |
                                    CPViewMinYMargin |
                                    CPViewMaxYMargin];

        [contentView addSubview:label];
    }

    @end

### Conclusion

This concludes our first tutorial. We've gotten familiar with some of
the drawing and event constructs of Cappuccino and have put together a
pretty simple prototype of our Scrapbook application. Next time, we'll
be going deeper into events and drag and drop to start making our
application more useful.

Something you may have noticed is that we never once spoke about browser
inconsistencies, nor do we have any conditional code based on what
browser the user is on. Since all the constructs we use are from
Cappuccino, we shift all the heavy lifting of these sorts of tasks to
the framework, and can instead focus on the key features of our
application.

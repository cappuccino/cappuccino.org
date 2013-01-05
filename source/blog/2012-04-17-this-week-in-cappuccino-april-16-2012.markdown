---
title: Cappuccino News
author: Aparajita Fishman
author_email: aparajita@aparajitaworld.com
wordpress_id: 1265
wordpress_url: http://cappuccino.org/discuss/?p=1265
date: '2012-04-17'
tags:
- Cappuccino
- Update
---


If you have news about new projects in which Cappuccino is being used &mdash; internal or external &mdash; be sure to let everyone know!

Please pay special attention to the **Fixes & Changes** section, there may be changes that will affect your code.

#### New Features

- Two new methods have been added to CPView: `registerThemeValues:` and `registerThemeValues:inherit:`. These methods allow you to quickly configure the appearance of widgets using the same compact data format used in `ThemeDescriptors.j`, but at runtime. This is great when you need to customize your widgets but don't want to go through the hassle of creating a new theme. For example:

	    :::objj
		ToolbarButtonHeight = 30.0;
		ToolbarButtonThemeValues = [];

		@implementation ToolbarButton : CPButton

		+ (void)initialize
		{
		    var bezelColor = CPColorWithImages(
		    [
		        ["button-bezel-left.png", 2.0, ToolbarButtonHeight],
		        ["button-bezel-center.png", 1.0, ToolbarButtonHeight],
		        ["button-bezel-right.png", 2.0, ToolbarButtonHeight]
		    ],
		    CPColorPatternIsHorizontal),

		    highlightedBezelColor = CPColorWithImages(
		    [
		        ["button-bezel-highlighted-left.png", 2.0, ToolbarButtonHeight],
		        ["button-bezel-highlighted-center.png", 1.0, ToolbarButtonHeight],
		        ["button-bezel-highlighted-right.png", 2.0, ToolbarButtonHeight]
		    ],
		    CPColorPatternIsHorizontal);

		    ToolbarButtonThemeValues = [
		        [@"font",               [CPFont systemFontOfSize:17.0], CPThemeStateBordered],
		        [@"text-color",         [CPColor colorWithHexString:@"c7c8ca"]],
		        [@"text-shadow-color",  [CPColor clearColor], CPThemeStateBordered],
		        [@"text-shadow-color",  [CPColor clearColor], CPThemeStateBordered | CPThemeStateDisabled],
		        [@"bezel-color",        bezelColor, CPThemeStateBordered],
		        [@"bezel-color",        highlightedBezelColor, CPThemeStateBordered | CPThemeStateHighlighted],
		        [@"min-size",           CGSizeMake(0.0, ToolbarButtonHeight)],
		        [@"max-size",           CGSizeMake(-1.0, ToolbarButtonHeight)],
		    ];
		}

		- (id)initWithFrame:(CGRect)aFrame
		{
		    self = [super initWithFrame:aFrame];

		    if (self)
		        [self registerThemeValues:ToolbarButtonThemeValues];

		    return self;
		}

		@end

- The new Cocoa image scaling constant names have been added to `CPControl.j`:

		New name                            Old name
		CPImageScaleProportionallyDown      CPScaleProportionally
		CPImageScaleAxesIndependently       CPScaleToFit;
		CPImageScaleNone                    CPScaleNone;
		CPImageScaleProportionallyUpOrDown  <not implemented>

	The old names are supported but deprecated, so you should use the new names. Support for `CPImageScaleProportionallyUpOrDown` has been added as well (thanks Blair Duncan). There is a demo of image alignment and scaling in `Tests/Manual/CPImageViewAlignmentScaling`.

- `valuePath` and `valueURL` bindings have been added for `CPImageView`. See `Tests/Manual/CPImageViewbindingsTest` for an example. (Thanks cocoadev)

- Added `CPURL -URLByDeletingLastPathComponent` and `CFURL.createDeletingLastPathComponent`.

- We implemented a documented issue life cycle and have started the long overdue process of triaging the hundreds of open tickets. We encourage everyone to take a look here before posting issues:

	[Posting issues](/contribute.html#bug-reports)

- Support for symlinks in a project has been added to XcodeCapp. (Thanks Richard van Zon)

#### Fixes & Changes

- `CPEvent -timestamp` now returns the fractional number of seconds since startup, as documented in Cocoa. (Thanks cocoadev)

- XcodeCapp ignores userland NS files (NS_*.j).

- When committing changes to an edited table cell, there was an infinite loop. This has been fixed.

- jake will not stop if you don't enter valid credentials when trying to install man pages for tools.

- Previously, when a control set its value and there were bindings to the control, the value would eventually echo back. In the case of a text field, this would result in the selection changing. This has been fixed. (Thanks cocoadev)

- A bunch of unnecessary and unintended global variables have been removed. (Thanks Blair Duncan)

- Improvements/fixes have been made to the formatting of the log level and title in CPLog. The level will default if none is passed. If nil is passed, it is suppressed.

- When a text field became first responder, it would be focused and then selected in two separate Javascript timeouts. This caused a small flash in some browsers. The second timeout has been eliminated to eliminate the flash.

- CPTabView will not allow a tab to be selected if the delegate disallows it. (Thanks cocoadev)

- The binding collection operators `@min`, `@max`, `@sum` and `@avg` were rewritten, refactored and fixed to eliminate an infinite loop with empty collections. They now support full property key paths.

- When a text field resigns, it always sends `CPControlTextDidEndEditingNotification`, whether or not editing had begun. This is consistent with Cocoa.


#### **Ticket/Pull Request Count**

* 276 open issues.
* ~225 left to triage.
* ~36 closed in the last 10 days.
* 18 open pull requests.
* 27 pull requests merged or closed in the past 10 days.

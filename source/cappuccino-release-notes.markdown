---
title: Cappuccino Release Notes
layout: markdown
---

## What's New in Cappuccino 0.9.6

*Release date: 2013-01-20*

Everything that was new in RC1 and RC2 and the following:

### Foundation and Core

* (4684856) New: improve `describe` format of `CPDictionary` and `CPArray` to be more like literals.  E.g. a dictionary is expressed as @{key1: value1}, an array like @[value2, value2], a string like @"<value>".
* (eb2bb24) New: added support for `CPNumberFormatterPercentStyle` in `CPNumberFormatter`.
* (797bfee) New: implement `CPPointInRect`.  This improves source code compatibility with Cocoa when replacing NS with CP.
* (7485c4e) New: -`CPHTTPURLResponse allHeaderFields`.  When a `CPURLConnection` response is of the `CPHTTPURLResponse` type, the raw HTTP headers can now be retrieved through the allHeaderFields message.
* (821961f) New: argument check `CPIndexSet indexSetWithIndex:`.  Without this check, an index set could be initialised with NaN which would later lead to an infinite loop when enumerating the index set.  This error makes the error early and explicit.

*Bug Fixes:*

* (77955f4) Fixed: `setTimeout(f)` did not work for some JS libraries such as `PDF.j`s when running in a Cappuccino context.
* (8e16e62) Fixed: fix a bug where `CPURL` was not encoding self._baseURL and self._string.

### AppKit

* (f535a6a) New: minor `CPTabView` optimisation.
* (b577644) New: significantly optimise `CPToolbar` validation.
* (7264692) New: optimise `CPSegmentedButton setEnabled:forSegment:`.
* (632fba9) New: null check when laying out columns in `CPTableView`.
* (a337bc2) New: reduce number of divs used by typical apps by something like 2.7%.
* (3fd8d3e) New: `- CPTableView clickedColumn`.
* (a70bc7d) New: "Creates Sort Descriptors" `CPTableColumn` value binding option. With this option an array controller driven table view can be sorted by clicking the table column headers without manually setting up sort descriptor prototypes.
* (adb6404) New: support Cib/Interface Builder window positioning masks. This adds support for all "initial position" window masks in Interface Builder except "centre". Position can be specified in current screen space coordinates and then adjusted proportionally to the browser size, or adjusted while preserving a left or right margin and a top or bottom margin.
* (7c56ea4) New: skeleton `CPColor colorUsingColorSpaceName:`.
* (e530831) New: `+ CPFont systemFontSizeForControlSize:`.
* (fd138cf) New: `- CPBox setTitleFont:` support.
* (ca4e034) New: `- CPBezierPath appendBezierPathWithArcFromPoint:toPoint:radius:` and `CGPathAddArcToPoint`.
* (9c2cb39) New: `CGContextIsPathEmpty` for non-canvas based platforms.
* (eba3e95) New: `- CPBezierPath controlPointBounds` and `CGPathGetBoundingBox`.
* (23adbd4) New: improve tooltips API and avoid some sticky tooltips.
* (391701f) New: `- CPBezierPath addClip` and `setClip`. This enables e.g. a `CPGradient` to be drawn clipped by an arbitrary bezier path.
* (4bedd52) New: `CPGraphicsContext saveGraphicsState` and `restoreGraphicsState`.
* (fb155de) New: allow non-string tooltips. Technically the tooltip should be a `CPString` but if a date or a number is passed this will now work without a crash.
* (c3c61e1) New: `- CPBox titleView`.
* (a1751cc) New: improve popover's content view resizing.
* (ba33803) New: improve CPPopover's `popoverDidShow:` timing.
* (9ebc787) New: improve `CPTokenField` token spacing.
* (b97a076) New: `CPStepper` bindings support for `CPValueBinding`, `CPMinValueBinding`, `CPMaxValueBinding`. Placehoders defaults are minValue, minValue, maxValue.
* New: popover animation support in Firefox, Opera and IE10.
* (c2bf47e) New: support `CPThemeStateEditable` for text fields.
* (bd1f64b) New: only show token delete button on hover, and only when token field is editable. Before this change the close button showed at all times, even for token fields which weren't even editable.  This change brings us closer to Cocoa in that there's no token delete button most of the time, and just like in Cocoa there are more controls available on hover. (Although in Cocoa there's a disclosure arrow and we have a close button instead.).
* (deb6224) New: support for resizing windows on all sides.
* (76a4ded) New: `CPBrowserStyleProperty` for getting browser specific CSS and JS names.
* (b59f96d) New: key view loop enhancements:
    * Nested views are now handled recursively as they are in Cocoa.
    * If there is no first responder and no initial first responder when a window first becomes key, use the first valid key view, not the first geometric key view.
    * Cocoa calculates the key view loop for nibs that do not have one, but does not call recalculateKeyViewLoop.

*Bug Fixes:*

* (ff93262) Fixed: work around rendering bugs in WebKit when moving canvas backed views. This bug would cause errors such as the subviews of a `CPBox` not drawing properly as the box moved.
* (b33763c) Fixed: popovers could only properly open relative to views in the main window.
* (0e68729) Fixed: dragged table view columns ignored custom column header views.
* (2355b7a) Fixes #1666: since 5763ebd extremely slow double clicks would be accepted.
* (31d5ddb) Fixed: improve `CPStepper` graphics.
    * Disabled `CPStepper` looked larger than the regular stepper due to the outline becoming white.
    * Wrong pixels at bottom corners.
* (ee1c547) Fixed: frame of `CPScrollView` was calculated incorrectly.
* (04f650d) Fixed: windows selection compatibility. Fix for issue 1390.
* (0a18990) Fixed: notify `CPOutlineView` delegate that item did collapse after reloading them.
* (905d23d) Fixed: small graphical fix in `CPPredicateEditor`.
* (c37783c) Fixed: fixed table column header styling.
* (da91ab9) Fixed: implicitly set `selectionIndexes`. `CPTableView`'s `selectionIndexes` binding shouldn't be set automatically unless the content binding was also set automatically (through a table column binding). Assume that manual content binding implies a desire to manually bind selection indexes (and sort descriptors) as well.
* (0f5d459) Fixed: collection view crash on unepexted drag events.
* (90d2713) Fixed: relative URLs were deemed to fail the SOP test by web views.
* (0d9973a) Fixed: out of place table headers and other text positioning errors.
* (0fa499b) Place `CPAlert`s above popovers.
* (f1c6a8b) Fixed: `Error: Permission denied to access property '_childAppIsStarting'` in Firefox. This error would occur when running an app in an iframe which could not access its parent frame.
* (7fab752) Fixed: text field responder error when using a formatter. If the formatter rejected a change and prevented the first responder status from being surrendered, the text field would still stop listening to key window changes and break first responder behaviour when switching between windows.
* (074e9f7) Fixed: incorrect `- CPWindow contentRectForFrameRect:` and `frameRectForContentRect:` for borderless windows with toolbars.
* (2758454) Fixed: tab views added in IB didn't resize properly. IB sets `autoresizesSubviews` to NO for tab views by default. In Cocoa this doesn't make any difference because `NSTabView` ignores this setting.  This fix makes it so that Cappuccino's tab view also works with `autoresizesSubviews` off.
* (fd3ad76) Fixed: after tabbing to a token field it'd immediately lose first responder status.
* (256d363) Fixed: token fields lost first responder status when switching between windows.
* (e2f8d77) Fixed: white line when scrolling between tokens.
* (4ef5dc8) Fixed: token field autocomplete menu placed incorrectly.
* (ce9534c) Fixed: `canBecomeKeyWindow` response for auxiliary windows. Without this fix Cappuccino always returned YES for `canBecomeKeyWindow` for every window. But in Cocoa, only "standard" windows with a title bar and/or resizing return YES.  With this fix Cappuccino better matches Cocoa's behaviour.
* (9035439) Fixed: token field first responder flicker when clicking tokens.
* (d27e333) Fixed: tokens could be deleted in an non editable token field.
* (095858d) Fixed: token field autocomplete scrollbars unresponsive to mouse.
* (0781a41) Fixed: `popoverDidShow` in Firefox.
* (eed37a0) Fixed: if any token field was being edited, the object value of all other token fields contained the partial value.
* (252b8f5) Fixed: `[CPApp windows]` contained nil.
* (cea1209) Fixed: `CPAlert` sheet crash.
* (3775c3f) Fixed: `CPAlert` was a `CPView`.
* (deacdde) Fixed: `CPSegmentedControl` not reducing its size when removing segments.
* (782f47a) Fixed: key view loop fixes/improvements
    * `- CPWindow setInitialFirstResponder` now works reliably and follows Cocoa behavior in that if -makeFirstResponder is called with something other than the window before the window is first shown, it will override the initial first responder.
    * Like Cocoa, until the first responder is set during window load, the first responder is the window by default, not the content view.
    * Optimized search for any view that has a previous/next key view set.
    * `- CPWindow autorecalculatesKeyViewLoop` now behaves per Cocoa, it only has an effect when views are added or removed.
    * If the first responder does not have a valid previous/next key view, it does not resign to nil, per Cocoa behavior.
* (cdc88db) `CPTextField` will no longer lose focus unnecessarily.
* (8d68e80) Fix `- CPWindow canBecomeKeyWindow` and `-canBecomeMainWindow` to match Cocoa behavior (and misleading documentation).

### nib2cib

* (7dd034e) New: nib2cib will now adjust to the correct themed height for subclasses of `CPButton`. For examples `CPPopUpButton` can get another height then `CPButton`.

*Bug Fixes:*

* (4e6b997) Fixed: adjust size in `NSStepper` to `CPStepper`.
* (3dacb4a) Fixed: fix nib2cib alignment of`CPColorWell`, `CPComboBox`, `CPPopUpButton` and `CPSegmentedControl`.
* (8ff2a32) Fixed: fix tag reading from IB Both controls and cells can have tags in IB, but Cappuccino has no cells. If the control has a tag, that takes precedence. Tag reading was moved to NSControl from NSView, since NSView does not have a tag in Cocoa.
* (8819fd5) Fixed: improve `nib2cib` support for `NSMatrix` based radio groups.  Without this fix, a matrix with a target-action pair would crash when the cib was loaded due to the matrix having been replaced with a `CPView` (which cannot take a target-action pair).  Now if the matrix is for radio buttons, the action connection for the matrix is made to the `CPRadioGroup` instead and works as expected when radio selections are made.

### Misc

* (3ccaa4d) New: button types can be set in IB, no need for code.
* (7bf46cb) New: add support for disabling sudo action in jake with `CAPP_NOSUDO=1`.
* (a24f33a) New: add .travis.yml for Travis-CI support.
* (7070fe9) New: `--quiet` and `--verbose` bootstrap.sh options.

*Bug Fixes:*

* (b28673d) Fixed: eliminate some debug output from `jake test` runs.
* (c30a6fb) Improve XcodeCapp support for custom class inheritance.
* (4acda0c) Fixed: fix and update css for documentation when using doxygen 1.8.
* (0f9a2dc) XcodeCapp support for zsh.

### Other Changes


d1c9786, acd98b5, d0fa16b, 63bad1d, bf3a152, 48e797a, e4a6d85, 2f428fa, 2e7afc3, df28a46, ad5b9b6, a7b40a5, d4b0e2a, 117d946, c8a37b4, 02a885e, 59ad849, 8a59235, 90d52a8, 95246d7, d718c29, ce167cf, 1edcc51, e46cd14, c2da96e, b629b88, 084e0a3, a973be2, 6c265fe, c896101, 8a39561, 6bc8ad0, 632e226, 2236e7d, 9d4e816, da01d3a, 282e966, 2611e86, f5bb8ab, 947b116, 8ec1325, e2f19c3, 7b2464a, 1ebdd8e, d82da5d, a202cfb, 2a11bdb, 9705f1f, 787dd10, dcdcd8e, 0d31f79, d072f17, 3e65178, f1a171a, 002c49b, 964f3fe, 45ad537, a9be167, c81b8fb, 32eafb7, 50031db, 19f668f, 6284f29, 40ab25d, 29fe631, 295eedc, 110bd20, 1f8306d, 6e3f822, 18f8294, 71f502a, 23817a0, 95511b5, 7fdc3ab, 0e82504, 4021eae, 7de4fe7, c9434ec, 2b1b1ea, 848c893, af2e034

## What's New in Cappuccino 0.9.6 (RC2)


*Release date: 2012-08-22*

### Foundation and Core

* New: `CFURL.createCopyDeletingLastPathComponent`.
* New: `CPURL URLByDeletingLastPathComponent`.
* New: `CFData.bytes()` and `CFData.base64()`.
* New: `CPData +dataWithBytes` and `CPData +dataWithBase64:`.
* New: `CPString pathWithComponents:`, `stringByAppendingPathComponent:`, and `stringByAppendingPathExtension:`.
* New: `CPArray` and `CPDictionary` descriptions now attempt to describe JavaScript member objects in more detail than just `[Object object]`.
* `CPMutableArray sortUsingDescriptors:` optimised.
* Improved documentation for `CPArray`, `CPString`.
* New: `CPArray indexesOfObjectPassingTest:`.
* New: `CPIndexSet indexPassingTest:`, `indexesPassingTest:`, `indexWithOptions:passingTest:`, `indexesWithOptions:passingTest:`, `indexInRange:options:passingTest:` and `indexesInRange:options:passingTest:`.
* Reimplement `CPGeometry` using `CGGeometry` since they are equivalent in Objective-J.
* New: `CPDictionary keysOfEntriesPassingTest:`, `keysOfEntriesWithOptions:passingTest:` and `keysSortedByValueUsingComparator:`.
* New: `CPDictionary enumerateKeysAndObjectsUsingBlock:`.
* New: `CGInsetMakeInvertedCopy`.
* New: `CPUndoManager` posts `CPUndoManagerDidCloseUndoGroupNotification`.
* `CFData` base64 encoding optimised.
* New: `CPNumberFormatter setMinimumFractionDigits:` support.
* New: very basic `CPNumberFormatter` currency style.
* New: `CPNumberFormatter generatesDecimalNumbers` support, enabled by default.

*Bug Fixes:*

* Fixed: a `CPURLRequest` created without using the designated initialiser wouldn't work.
* Fixed #1512: patch for rhino-narwhal to add `JAVA_OPTS` support when running Cappuccino utilities through rhino. This generally improves configurability for special cases, and specifically enables a work around for the `failed to map segment from shared object` error on some platforms.
* Fixed #1529: incorrect `CPDecimalNumber` result for 220000/220. In general divisions where the quotient had fewer digits than the dividend when disregarding exponent would fail.
* Fixed: `LOG` global function.
* Fixed: `CPString` path methods should collect `//` into `/`.
* Fixed: main bundle URL missing final `/` when running in CommonJS.
* Fixed: `CPDateReferenceDate` should be 'Jan 1 2001' instead of 'Feb 1 2001'
* Match `CPDate distantPast` and `distantFuture` with Cocoa.
* Fixed: removed redundant `CPCopyRange` function.
* Fixed: incorrect change information sent to observers when the top level object of an observed key path changes.
* Fixed: crash if an observer was set between `willChange…` / `didChange…`.
* Fixed #1624: `CPNumberFormatter` grouping was wrong.
* Fixed: `CPNumberFormatter` grouping separator support. `perMillSymbol` was incorrectly used as the grouping separator.
* Fixed: `CPSet` used identity checks, not Objective-J equality checks.
* Fixed: `CPArray` should throw an exception when observer is added/removed.
* Fixed: `CPSet removeObject:` for an object not a member is not an error.
* Properly allow `CPNumberFormatter` to operate on most `CPNumber` types. This only worked by accident before.
* Correct `CPNumberFormatter maximumFractionalDigits` default.
* Fix `CPNumberFormatter` maximum fraction digits property name.
* Extend `CPNumberFormatter` CPCoding support and fix rounding default.
* Fixed: `CPDecimal` would not accept strings such as '.003' or '-.003' (no integer component).

### AppKit

* Much improved support for sheets in general and modal sheets in particular (doc-modal).
* Better animation of sheet shadow when the sheet animates in our out.
* `CPPredicateEditor` improvements. Bindings compatibility.
* Raise an exception if a view is added to itself as a subview.
* New: `+ (BOOL)automaticallyNotifiesObserversOf<Key>` support.
* If `showRelativeToRect:` is called while a popover is closing, it is ignored.
* If `showRelativeToRect:` is called when the popover is already open the existing popover is repositioned.
* Close all popovers when a window is closed.
* New: `CGInsetUnion` and `CGInsetDifference`.
* New: small progress indicator spinners.
* New: `CPImageView CPValueURLBinding` and `CPValuePathBinding` read-only support.
* New: hold down the option key while expanding an outline view item to expand all children as well.
* New: `CPImageView CPImageScaleProportionallyUpOrDown`.
* New: `CPSplitView adjustSubviews`.
* Archive `CPView` tooltips.
* The parent window of a sheet can be moved.
* New: `CPWindow` sheet delegate messages.
* New: `CPImage -initWithData:`.
* New: `CPImageView` support for `CPDataBinding`.
* New: `CPTableView` themed attribute for round rect selection of rows. Selections in the tableview can now have round corners. The default is a regular rect.
* New: `CPTableView` content binding (especially useful for Lion style view-based tables.)
* New: `CPImage data`. If the image was not initialised using data but the browser supports canvas, data is generated.
* Improve toolbar item layout. The height of all items is determined by the tallest item. If a toolbar item has a small view or a small icon, it is now centred within the available space above the label. For example, for a tiny icon in one item next to a normal size icon the tiny icon would be centre aligned with the larger icon.
* New: toolbar `CPToolbarDisplayModeIconOnly` support.
* New: toolbar support for tall custom widgets. You can now finally have that `CPTableView` you always wanted in your toolbar.
* New: toolbar "labels only" mode.
* Use any size toolbar icons such as 48x48 and the toolbar adapts automatically (unlike Cocoa).
* Improved artwork for button bars (switch odd blue colour for a more standard white).
* New: `CPTokenField` delegate method `tokenField:representedObjectForEditingString:`. This improves support for represented objects and is used both when an autocompletion suggestion is used or when the name of a token is typed in by hand.
* Place token autocomplete underneath what's being completed.
* Autosize token field autocomplete menu. The new menu is much more efficient for the user:
    * Less tall items makes it much easier to select among many completions.
    * Exactly wide enough for widest item.
    * Tall enough to show all items (instead of just 3 as before).
    * Uses a maximum width and height defined by the screen edges and some Cocoa-like constants.
* Improve token field subclassing support. Token field now triggers autocompletion from `textDidChange:` which better meets the expectations of Cappuccino programmers. Eliminated custom non-Cappuccino key press handler.
* New: `CPTokenField keyUp:` support.
* New: key bindings support for token field. Also improve compatibility with `CPTextField` superclass and subclassing support by properly using `interpretKeyEvents:` like `CPTextField`.
* Allow token field subclasses to override `defaultCompletionDelay`.
* Allow token field `insertText:` to be somewhat overridden. If `insertText:` is overridden to do nothing, nothing in inserted.
* Overwrite selected tokens by typing.
* New: `CPArrayController removeObjectAtArrangedObjectIndex:`.
* New: select all support for `CPTokenField`.
* Improve token field keyboard navigation when tokens are selected.
* New: many more `CPButton` types, `highlightsBy` and `showsStateBy` support, including for subclasses (`CPCheckBox` and `CPRadio`) when appropriate. All button types now supported:
    * `CPPushOnPushOffButton`
    * `CPToggleButton`
    * `CPMomentaryChangeButton`
    * `CPOnOffButton`
    * `CPMomentaryPushInButton`
    * `CPMomentaryPushButton`
    * `CPMomentaryLight`
* New: full `CPPopUpButton` bindings support.
* New: `CPToolbar` autovalidate support.
* New: `CPSplitViewWillResizeSubviewsNotification` notification `userInfo` now contains the divider index.
* New: `CPComboBox`.
* Better focus ring for `CPTextField` and all subclasses, and improved drawing of disabled contents.
* New: themable `CPColorWell` with Aristo look. Highlighted and disabled visuals.
* Standardise `CPColorWell`'s mouse handling and highlighting. Switch to `setNeedsLayout` based drawing.
* New: `CGRectInsetByInset`.
* New: the system font can now be changed at runtime, even for archived UI (e.g. through `nib2cib`.) There is no need to recompile if the system font is changed in Info.plist.
* New: `CPControl` now archives its formatter. This allows you to use a formatter with a table column's data view.
* New: a font of size 0 now uses the current system font size.
* New: `CPFontManager setSelectedFont:isMultiple:` and other basic properties.
* New: `CPFontManager convertFont:`, `convertFont:toHaveTrait:` and `addFontTrait:`.
* New: `CPFontManager weightOfFont:` and `traitsOfFont:`.
* New: `CPFontManager convertFont:toFace:`.
* New: notify when a `CPTableView` column moves through `CPTableViewColumnDidMoveNotification` and the delegate.
* New: `+CPEvent modifierFlags`.
* New: `CPEvent description`.
* New: `CPViewController isViewLoaded`.
* New: inactive windows (windows which are not the key window) now have a greyed out window title.
* Improve `CPTokenField`, `CPView`, `CPTableColumn` and `CPWindow` documentation.

*Bug Fixes:*

* Fixed: attempt to close a sheet while it is animating is now handled.
* Fixed: in Safari 5.1 sheets would sometimes not correctly order out.
* Fixed #1279: `CPRuleEditor` was not compatible with Internet Explorer 7, 8 or 9.
* Fixed: `CPRuleEditor` would not scroll properly in a scroll view as more rules were added.
* Fixed: `CPTabView` item selection could not be fully disabled through the delegate.
* Fixed #1457: clicking `CPPopUpButton` then dragging to an item and releasing the mouse button did not select the item.
* Fixed cases where a `CPMenu` would not close after certain mouse interactions.
* Fixed: check box binding value transformers were ignored.
* Fixed: reverse value transformations were not applied for table view bindings.
* Fixed: `CPPopover close` consulted the delegate's `popoverShouldClose`.
* Fixed: infinite loop with empty collection in `@min`, `@max` and `@sum` operators.
* Fixed: return `valueForUndefinedKey:` value properly for KVC.
* Fixed: `CPSet valueForKeyPath:` returned incorrect results in some cases.
* Fixed: `CPTextField` did not send `CPControlTextDidEndEditingNotification` if editing had not started, contrary to Cocoa.
* Fixed #1433: more initial key view loop calculations.
* Fixed: flashing `CPTextField` insertion point when text field becomes the first responder.
* Fixed: when bindings were applied in reverse, the source of the binding would cause the destination to needlessly update again, causing e.g. the `CPTextField` cursor to jump to the end after every character typed when `continuouslyUpdatesValue` was on.
* Fixed: table view highlighting drawing bug.
* Fixed: table view infinite loop when finishing cell editing.
* Fixed: `CPEvent timeStamp` did not return seconds since startup.
* Fixed: don't crash when removing objects from an array controller which has its arrangedObjects.@count observed.
* Fixed: a collection view wouldn't become the first responder when its items were clicked.
* Fixed #1485: `CPScroller` decoding bugs which would lead to errors such as `CPInvalidArgumentException: CPScroller does not contain theme attribute 'scroller-width'`.
* Fixed: timestamp for `CPEvent`s from periodic events.
* Fixed: menu item highlighting error.
* Fixed #1491: `CPInvalidArgumentException: - [_CPMenuBarWindow scrollByDelta:] unrecognized selector sent to instance` when attempting to scroll in a menu.
* Fixed: collection views cleared their selection whenever the content was changed.
* Fixed: `CPPredicateEditor` `Display value must be…` exception in recent revisions.
* Fixed: `CPOutlineView setMenu:` was not effective.
* Raise an error on attempt to add a new sheet to a window which already has one, or to a window which is a sheet.
* Fixed: sheets would order out without an explicit `orderOut:` message, unlike Cocoa.
* Fixed: `CPProgressIndicator` encoder wasted space and caused errors. The errors would cause exceptions such as `Not allowed to load local resource: file:///<some local path from the machine that ran nib2cib>` when loading cib driven app through a web server.
* Fixed: `CPPopover` typo (`setBehaviour:` -> `setBehavior:`).
* Fixed: `CPTextField` delegate method `control:didFailToFormatString:errorDescription:` did not actually send a string.
* Fixed: `CPTableView` bug where dragged rows didn't have their bindings applied.
* Fixed: when a `CPPopover` closes implicitly, `popoverShouldClose` delegate method should be checked.
* Added a very hacky workaround for the jittery [resize bug in WebKit](https://github.com/cappuccino/cappuccino/issues/1325).
* Fixed: `CGSizeFromString` and `CGPointFromString` would try to parse only integer values.
* Fixed: shared `CPDocumentController` instantiation.
* Fixed: `window.status` access when not running in the browser by `CPApplication`.
* Fixed: `CPOutlineView` disclosure control width was hardcoded.
* Fixed: `CPMenu` highlights wouldn't always disappear.
* Fixed: `CPTableView selectedColumn`.
* Fixed: `CPButton`'s "dim image when disabled" should be on by default.
* Fixed: token field auto completions. Auto completions are strings, not represented objects.
* Improve `CPTokenField` autocomplete scrolling.
* Fixed: `CPTokenField` autocomplete menu could show up underneath other windows.
* Fixed: make sure autocomplete menu fits within browser.
* Fixed: `CPTokenField keyDown:` handling. Previous nonstand implementation interacted poorly with Cappuccino's event handling and subclasses.
* Fixed: `CPTokenField` object value for half finished tokens. Try to convert to a `representedObject` before responding to `objectValue`.
* Fixed: `CPTokenField` nil `representedObjectForEditingString:` handling. If `tokenField: representedObjectForEditingString:` returns nil, act the same as if the delegate method didn't exist.
* Fixed: `CPTokenField` token layout when tokens are selected.
* Fixed: browser shortcuts wouldn't work when a `CPTokenField` was active.
* Fixed: evaluation of whether a document based application needs an untitled document on startup.
* Fixed: `CPToolbar` delegate method `toolbarDefaultItemIdentifiers:` is optional. This fix makes it possible for a cib-defined toolbar to have a delegate set without defining `toolbarDefaultItemIdentifiers:`. You might be implementing other delegate methods.
* Fixed: `CPPredicateEditor CPTextField` action bug.
* Fixed: non-bordered buttons should retain their size, not shrink to fit.
* Fixed #1559: many edge cases of split view autosaving and restoration, including deeply nested split views. This fix also makes it easier to override autosave restores in a subclass or a controller's `viewDidLoad`.
* Implement `CPWindowController setViewControllerContainerView:` and fix `CPWindowController setViewControllerView:`.
* Use theme system for `CPColorWell` bordered state. This is more consistent with the rest of Cappuccino and prepares for theming support.
* Fix `CPColorPanel` errors.
* Fix clipping of text due to fractional pixels.
* `CPGeometry` moved to `Foundation`.
* `CPRuleEditor` fixes regarding format strings and regexes.
* Fixed: browser propagation control when not in browser. This would lead to a `[CPPlatformWindow _willPropagateCurrentDOMEvent] unrecognized selector sent to instance` error if an event was sent in a non DOM environment.
* Fixed #1593: editing of custom data views in `CPTableView`.
* Fixed: a `CPArrayController` driven table could show an empty selection after `removeObject:`.
* Fixed: removing selected `CPPopUpButton` item. When the selected item of a `CPPopUpButton` is removed the first item should become selected.
* Fixed: popovers in modal windows couldn't be interacted with. This prevented e.g. date picker popovers in sheet dialogs.
* Fixed: `CPCib instantiateCibWithOwner:topLevelObjects:` did not allow a nil owner.
* Fixed: jumping text when editing a `CPTextField` in some browsers, especially Firefox and newer versions of Chrome.
* Fixed: Internet Explorer drew toolbars of borderless windows wrong.
* `CPCib initWithContentsOfURL:` returns nil if the requested data is nil.
* Fixed: `CPTokenField`s would sometimes unexpectedly steal first responder status. If an autocomplete choice was made followed by immediately focusing on another control, the token field would reclaim first responder status a moment later.
* Fixed: `CPTokenField` scrolling away from selected token. Sometimes clicking a token would cause the token field to scroll to some other spot.
* Fixed: `CPEvent data1` and `data2` weren't stored right. They were stored in globals instead of ivars, allowing only one `data1` or `data2` in the whole app.
* Fixed: in `CPArrayController` wrong indexes would become selected when removing arranged objects.
* Fixed: `CPWindowController setViewController:` was incorrectly causing view loading.
* Fixed: wrong text sizing across the board for custom fonts. If a custom font was used with the CSS `@font-face` syntax, Cappuccino would calculate the wrong sizes for strings throughout.
* Allow `CPControl` formatter to format nil.
* Fixed: many sheet related first responder and mouse interaction bugs.
* Fixed: non-key window text fields tried to receive input, looked active.
* Fixed: text field font size while editing was wrong in Internet Explorer.
* Fixed: text field cut/paste by context menu would not trigger a change notification. Also just regular copy and paste could fail to trigger notifications.

### Nib2Cib

* New: XcodeCapp support for Xcode 4.4 with much improved code generation. The Xcode 4.4 support enables connection of new outlets and actions without restarting Xcode. At the same time Xcode should now be better at recognising the super classes of Cappuccino classes.
* New: support for User Defined Runtime Attributes in IB.
* New: support for defining userland NS classes for conversion from IB.
* New: support for nib2cib configuration files.
* New: support `CPDateFormatter` (although actual formatting not yet implemented in Cappuccino.)
* New: support for tooltips.
* Faster image utility.
* New: support for `CPProgressIndicator` size.
* nib2cib will now log the path and size of custom image resources in super verbose mode.
* New: support alternative image and title for buttons.
* New: support "thick divider" split view style.
* New: support for tags on `NSCell`, useful for radio groups.

*Bug Fixes:*

* `NSButton` now allows buttons that are not fixed height, if the theme allows it.
* Fixed: a regular size spinner in IB became twice as large in Cappuccino.
* Fixed: button `imageDimsWhenDisabled` default.
* Make the default grid color in IB show correctly in `CPTableView`.
* Make `NSClipView` obey the Draw Background checkbox in IB

### Misc

* Improved `capp ThemeDescriptor` template with better tasks, documentation and structure.
* Stop generating useless XML from doxygen.
* New `dump_theme` tool to inspect themes.
* New: `capp_lint` added to Tools.
* Fixed: don't mention `narwhaljs.org` in bootstrap.sh - it doesn't exist anymore.
* Warn about the need to `xcode-select` in bootstrap.sh.
* New: `capp_lint` check for space inside parens and dependent statement on same line

*Bug Fixes:*

* Fixed: `objcc --includeTypeSignatures` typo.

## What's New in Cappuccino 0.9.6 (RC1)


*Release date: 2012-04-26*

### Foundation and Core

* Faster `CPNotificationCenter removeObserver:`.
* Complete `isEqual:` support for `CPExpression` and `CPPredicate` subclasses.
* New: `CPObject performSelector:withObject:`.
* Improved docuemntation for `CPSet` and `CPMutableSet`.
* New: `objcc -T` (or `--includeTypeSignatures`) option which activates the `IncludeTypeSignatures` option.
* New: `CFPropertyList` support for date decoding.
* New: `CPIndexSet enumerateIndexesUsingBlock:`, `enumerateIndexesWithOptions:usingBlock:` and `enumerateIndexesInRange:options:usingBlock:`.
* `CPIndexSet` optimisations.
* New: `CPArray enumerateObjectsWithOptions:usingBlock:`.

*Bug Fixes:*

* Fixed #1405: `TypeError: framework is not a function, it is undefined` when compiling Objective-J on Linux.
* Fixed #1405: `Error: Could not load file at Foundation/Foundation.j` when compiling Aristo on Linux.
* Fixed: `CPNotificatioNCenter` notifications were sent to removed observers. If one observer of a notification centre notification removed another observer, that other observer would still be notified even that it was no longer observing.
* Fixed #1424: incorrect PNG paths for `pngcrush`.
* Fixed: `CFPropertyList.propertyListFromXML` did not properly decode base64 encoded data values.
* Fixed: `CPKeyedUnarchiver decodeBytesForKey:`.

### AppKit

* Archive default theme attribute values.
* New: tooltips are now themable.
* New: some bindings support for `CPPopUpButton`.
* New: title support for `CPBox`.
* New: support for split view `shouldAdjustSizeOfSubview:` delegate method.
* Improved: rewritten `CPSplitView` resizing which plays well with a mix of fixed size and non-fixed size panes.
* Throw an exception when trying to set a scroller's knob proportion to NaN or Inifinity.
* Minor `CPCollectionView` optimisations.
* Throw an exception when trying to set a null minimum item size for a `CPCollectionView`.
* New: `CPWorkspace openFile:` and `openURL:`.
* Support for "small" size toolbars (`CPToolbar sizeMode`).
* Improved documentation for `CPSplitView` and `CPScrollView`.
* New: checkbox placeholder bindings options.
* Calculate a default key view loop for windows loading from cibs if necessary even if `autorecalculatesKeyViewLoop` is NO.
* Constrain `CPColor` components to [0.0, 1.0].
* New: `CPColor colorWithSRGBRed:green:blue:alpha:`.
* New: `CPColorSpace` (basic).
* New: `CPGradient` with `drawInRect:angle:`.
* Stub out `CPView inLiveResize`.
* New: `CPGraphicsContext isFlipped`.
* Tile narrow vertical three part images horizontally, and short horizontal three part images vertically. For example you can use a 1px wide vertical three part image to stretch to any width.
* New: `CPColorWell` bindings support.
* New: `CPOutlineView` delegate method `outlineView:shouldShowOutlineDisclosureControlForItem:` (corresponding to `shouldShowOutlineCellForItem:` in Cocoa).
* New: `appkit_tag_dom_elements` debug option adds a `data-cappuccino-view` attribute to most Cappuccino controls, making it easier to troubleshoot in a browser based document inspector.
* Minor scroll view optimisations.
* Don't draw a table corner view if there is no vertical scrollbar.
* New: `CPSet sortedArrayUsingDescriptors:`.
* New: `CPView registerThemeValues:` to change view theme attributes at runtime in a manner similar to `ThemeDescriptors.j`.
* `CPPopover` animation tweaks and improvements.
* New: select `CPOutlineView` item parent with left arrow key.
* New: `CPOutlineView selectionShouldChangeInOutlineView:` delegate method.

*Bug Fixes:*

* Fixed #1296: `CPBrowser` did not notify its delegate of new selections if the selection was made using the keyboard.
* Fixed #1413: Internet Explorer `colorWithCSSString:` crash. Syntax such as `[[CPColor colorWithCSSString:@"rgba(0,0,0,0.5)"] cssString]` lead to a CSS string incompatible with browsers without the CSS rgba feature.
* Fixed #1412: Internet Explorer rendered clearColor shadows in black.
* Fixed #1411: in Internet Explorer, no table/outline view selection highlights would render for certain cibs.
* Fixed: `CPArray filteredArrayUsingPredicate:` and `CPArray filterUsingPredicate:` did not work for certain types of arrays, and could potentially cause erroneous results for `CPArrayController`s with filter predicates.
* Fixed #1436: calling `CPShadowView shadowViewEnclosingView:` on a subclass of `CPShadowView` would return an instance of the superclass.
* Fixed: `CPTabView selectedTabViewItem` would raise an exception when there were no tab items instead of nil.
* Fixed: `CPTabView` would not properly reflect changed views if the view changed while the tab was not selected.
* Fixed: `CPSplitView` tried to auto save even without an auto save name.
* Fixed: `+ CPFont boldFontWithName:size:italic:` sometimes returned a non-bold, non-italic font.
* Fixed #1444: `CPCompoundPredicate` of `CPNotPredicateType` error.
* Fixed: `+ CPFont fontWithName:size:italic:` sometimes returned a non-italic font even for `italic:YES`.
* Fixed: `CPTableColumn` decoded and set its header view twice.
* Fixed: `CPArrayController avoidsEmptySelection` incorrectly was applied when setting an empty selection through code.
* Fixed #1450: a scroll view with non hiding legacy scrollbars would crash if the document view had a size of 0 pixels in either dimension.
* Fixed: `CPCollectionView setSelectionIndexes:nil` would freeze the app.
* Fixed: don't crash when loading a `CPCollectionView` with no item prototype view from a cib.
* Fixed: sending `CPWindow setAutorecalculatesKeyViewLoop:NO` caused the window to recalculate the key view loop.
* Fixed: `[CPString count] unrecognized selector` error when binding an array controller's content array to a key of another AC's selection.
* `CPWindow autorecalculatesKeyViewLoop` now defaults to NO rather than null.
* Fixed: small size toolbars in bridge windows didn't show the bottom shadow line.
* Fixed: blurry `CPOutlineView` disclosure triangle.
* Fixed: scroll views with a bezel border had two strange dots in the upper corners instead of a Lion-like bezel.
* Fixed: table column divider lines were drawn on top of the header bottom line.
* `CPViewController` view loading behaviour tweaks.
* Fixed: `CPViewController initWithCibNamed:bundle:` ignored the `bundle` argument.
* Fixed: `CPPopover` created a new window every time it opened, leaking memory in the process.
* Fixed: `CPPopover` delegate method `popoverDidClose` could be called before animation finished.
* Fixed: `CPPopUpButton` exposed an unintended `selectedTag` method.

### Nib2Cib

* Make bold text labels a little taller when converted to avoid cropping the bottom.
* New: `CPStepper` support.
* New: `CPTableView` background colour support.

*Bug Fixes:*

* Fixed: empty `CPTabView`s could not be converted.
* Fixed: toolbars with standard items such as `NSToolbarShowColorsItem` didn't convert right.
* Fixed: `CPBox` title position 'none' was converted to 'on top'.
* Support for `CPWindow autorecalculatesKeyViewLoop`.
* Fixed: base64 data could not be decoded from nib files.
* Fixed: search fields had the bottom pixel cut off.
* Fixed: toolbar search fields were cut in half height-wise due to a too small max size.
* Fixed: spinner style progress indicators were nib2cibbed to progress bars.
* Fixed: spinner progress indicators took on the wrong size in Cappuccino.

### Misc

* Fixed #1401: Cappuccino docs wouldn't display properly in Windows.

## What's New in Cappuccino 0.9.5


*Release date: 2011-11-16*

The final release of Cappuccino 0.9.5 is identical to RC5.

## What's New in Cappuccino 0.9.5 (RC5)


*Release date: 2011-11-16*

### Misc

 * Fixed version number in documentation.

## What's New in Cappuccino 0.9.5 (RC4)


*Release date: 2011-11-16*

### AppKit

 * Fixed with `CPTokenField`: quickly entered tokens would be ignored.
 * Fixed with `CPTokenField`: crash if added to a window in a unit test.
 * Fixed #1398: in a `CPTokenField`, deleting tokens in front of selected tokens would shift the selection to the right.
 * Fixed #1397: make sure `CPTokenField` selection is initialised when loading from cib.

## What's New in Cappuccino 0.9.5 (RC3)


*Release date: 2011-11-11*

### Foundation and Core

 * Local param shadowing now emits a warning instead of an error. This is temporary awaiting a proper fix of param shadowing in the preprocessor.
 * `CPScanner` fixes.
 * Don't log backtraces repeatedly when using `objj_backtrace_decorator`.
 * `CPString -substringWithRange:` and `-rangeOfString:options:range` now throws `CPRangeException` for out of bounds ranges.
 * Add `-forwardingTargetForSelector:` support.
 * Crude but functional infinite recursion checker, optional at compile time.
 * New: `CPNumberFormatter` with `CPNumberFormatterDecimalStyle` support.
 * New: support null values in `CPDictionary's +dictionaryWithJSObject:recursively:` (issue #1299).
 * New: objjc --help.
 * New: objjc option to compile to stdout, with or without `@STATIC` tags, suitable for JavaScript linters.
 * Improved performance of `[CPString copy]`.

*Bug Fixes:*

 * Fixed: `CPURL -isEqual:` for URLs with redundant slashes.
 * Fixed: `CPDate` timezone calculation in `initWithString:`.
 * Fixed #1065: `CPString -rangeOfString:` backwards search did not work.
 * Fixed: `CPString -rangeOfString:` anchored backwards search did not work.
 * Fixed: searching a string for @"" with `CPString -rangeOfString:` returned results other than `CPNotFound`.
 * Fixed: `CPString -rangeOfString:options:range` returned locations relative to the passed-in range instead of the full string.
 * Fixed: `CPMutableSet -addObject:` should raise with nil or undefined.
 * Fixed: very large numbers written to 280north1 plist files would be read back as very small numbers. This would among other things break nib2cib where certain controls would take on infinitesimal sizes.
 * Fixed #1289: infinite recursion when coercing an object without a `-description` method into a string.
 * Fixed #469: infinite recursion when an unimplemented message was sent to an object with no superclass.
 * Fixed with `CPDecimal`: decimal numbers below 1.0 would compare incorrectly with 0.0.
 * Fixed #1380, #1383: avoid "popen error (pipe): Too many open files" error when building Cappuccino.
 * Fixed #1384: avoid user defaults QUOTA_EXCEEDED_ERR crash.

### AppKit

 * New: `CPButton` continuous mode.
 * Improved: `CPSound` error handling and better Cocoa compliance.
 * Improved: table view keyboard row selection.
 * New: `CPProgressIndicator` is now coding compliant.
 * New: keyboard navigation in menus.
 * New: mouse wheel support in menus.
 * New: automatic or explicit scroll mode selection for web views.
 * New: support for pattern fills in `CGContext` (`CGContextSetFillColor` with a pattern color).
 * Clean up JavaScript (missing semicolons, don't use commas as statement separators.)
 * `CPWebView -isLoading` method.
 * Support for web views with transparent or coloured backgrounds.
 * `CPObjectController automaticallyPreparesContent` support.
 * Added support for the `CPNullPlaceholderBindingOption` for bound text fields.
 * New: text field support for `CPContinuouslyUpdatesValueBindingOption`.
 * New: bindings support for inline table view cell editing.
 * Support for `CPOutlineView outlineViewDeleteKeyPressed:` delegate method.
 * `CPEvents` sent during `mouseDragged:` now have `deltaX` and `deltaY` appropriately set (issues #1210, #1211).
 * New: coding support for `CPIndexPath`.
 * `CPMenu` item validation.
 * New: `collectionView:menuForItemAtIndex:` delegate method support.
 * New: `CPDictionary -keysSortedByValueUsingSelector:` which, just as it sounds, returns the keys of the dictionary sorted using a given selector.
 * Key equivalent display in menus for special characters such as escape, tab, arrow keys and many others.
 * New: tooltip support for any view with the standard yellow box look (issue #1264).
 * Remove table view corner view if there is no header view.
 * Added `CPMenu -removeAll` method (issue #1260).
 * New: `CPPredicateEditor` allows a search or filter predicate to be constructed visually by the user.
 * Optimise array controller `addObject:` by eliminating entirely pointless rearrange when added objects did not pass the filter. Also avoid double rearrange if `clearsFilterPredicateOnInsertion`.
 * Draw table view gridlines precisely inside the right side of cells so that grid line positioning and spacing matches Cocoa.
 * New: `CPUserDefaultsController` which can be used to easily bind controls to user default keys, in Interface Builder or elsewhere.
 * Optimise `CPArrayController insertObject:atArrangedObjectIndex:`.
 * Minor array controller optimisation: don't send a `filterPredicate` change notification if `clearsFilterPredicateOnInsertion` is YES but `filterPredicate` is already nil when `insertObject:atArrangedObjectIndex:` is called.
 * `CPArrayController handlesContentAsCompoundValue` support for `contentArray` binding.
 * Left and right arrow keys can now be used to expand and collapse items in `CPOutlineView`.
 * New: `CPLevelIndicator` shows a meter with discrete levels from empty to full.
 * `CPFormatter` support for `CPControl`.
 * New scroll view `scrollViewWillScroll:` and `scrollViewDidScroll:` delegate methods, inspired by `UIScrollViewDelegate` (issue #1177).
 * Multiple improvements to `CPMenu` opening, closing and handling of submenus.
 * Coding support for `CPCharacterSet` when the set is of the `characterSetWithCharactersInString` kind.
 * `CPCharacterSet -isEqual:` support when the set is of the `characterSetWithCharactersInString` kind.
 * Inverted `CPCharacterSet +characterSetWithCharactersInString` now archive properly.
 * New: coding support for `CPTokenField`.
 * `CPArray` range checking (issue #1334).
 * `CPBoxes` created with `+boxEnclosingView:` now take on the autoresizing mask of the passed view (issue #1335).
 * Improved table view redrawing performance when `usesAlternatingBackgroundColors` is YES (issue #1341).
 * Allow `CPAlert` subclasses to use `+alertWithMessageText:...` et al (issue #1333).
 * Improved performance of `valueForKeyPath:` (issue #1344).
 * `[CPSound play]` now plays the sound once it has been loaded if it hasn't yet (issue #1345).
 * Raise `CPRangeException` if `CPString substringToIndex:` is out of bounds.
 * New: support nested `willChange<Key>` and `didChange<Key>` calls. When multiple calls are nested, only the first `willChange...` and the last `didChange...` will notify observers, avoiding duplicate notifications for the same change. This can massively improve performance since observations sometimes lead to cascading updates (issue #1343).
 * Send `didChange` in reverse order of `willChange` in `CPObjectController setContent:`.
 * Implemented support for the `CPTokenField tokenField:shouldAddObjects:atIndex:` delegate method (issue #1360).
 * `CPStepper` button sizes can now be themed.
 * New: `CPColorWithImages()` convenience function to quickly create a `CPColor` from single, 3-part or 9-part images (issue #1274).
 * Enhanced `-description` method of `CPImage` and `CPColor` to show the exact content, especially for pattern colors (issue #1274).
 * New: allow binding a table column value to an array controller reached through a key path.
 * Improved split view performance: eliminate excessive `splitViewDidResizeSubviews:` messages.
 * New: support for collapsing views towards the right in split views.
 * New: split view auto save support.
 * New: 'overlay' style scrollbars which fade out when not in use. Old style scrollbars are also supported and automatically enabled if the browser does not use overlay style scrollbars (e.g. OS X Lion with a touch enabled input device uses overlay style scrollbars, but a Windows XP machine with a mousewheel would not.)
 * New: `CPWindow setMovable:` support which specifies whether a window can be dragged (issue #1358).
 * New: `CPPopover` control to create small "pop up" widgets attached to other controls, similar to the Downloads pop-over in Safari 5 (issue #1316).
 * Allow almost anything as a key equivalent unless a text field is the first responder. E.g. pressing "a" with no modifiers can now trigger a button.

*Bug Fixes:*

 * Fixed with `CPViewAnimation:` all animation curves behaved like a linear curve (issue #1313).
 * Fixed: issue with `CPSound` in Firefox.
 * Fixed #1033: `CPFlashView` setParameters: bugs.
 * Fixed: uniform table view column resizing.
 * Fixed: `CPSearchField` layout glitch.
 * Fixed #1122: `CPSplitView setIsPaneSplitter:` had the opposite effect of what it should have been.
 * Fixed with `CPTextField`: cut and paste using the mouse did not set stringValue properly.
 * Fixed with `CPTextField`: `CPControlTextDidBeginEditingNotification` and `CPControlTextDidChangeNotification` were not sent after cut and paste.
 * Fixed: bugs with `CPTableView` column resizing.
 * Fixed: `CPOutLineView outlineView:sortDescriptorsDidChange:` delegate message was not sent.
 * Fixed with KVO: method replacement happened for every call to `addObserver:` when one replacement would do.
 * Fixed: spacing in `CPBrowser`.
 * Fixed: color panel layout issues.
 * Fixed: scroll view corner and headerview decoding.
 * Fixed: unarchiving table views with no header view.
 * Fixed #1136: for the most part, web views' `setScrollMode:` message did nothing.
 * Fixed: web view AppKit scrollbars often did not reflect the true content size of the view.
 * Fixed: several Internet Explorer compatibility bugs.
 * Fixed: `[CPArrayController arrangedObjects]` could be nil.
 * Fixed #1160: `CPSearchField` delegate method `controlTextDidChange:` didn't always get fired.
 * Fixed: memory leak in `CPSearchField`.
 * Fixed: scroller error when horizontal scroller was too small.
 * Fixed: split view did not reposition subviews or remove divider when a subview was removed.
 * Fixed: root layer transform inadvertantly changed when redisplayed.
 * Fixed: if `unarchiver:didDecodeObject:` returned nil, the original object was still replaced (with nil) instead of being kept.
 * Fixed #864: corner view did not always draw the line above the left edge of the scroll view.
 * Fixed: loading an empty string into a web view would make it entirely white regardless of the background colour specified.
 * Fixed: in Firefox, certain web views would not send the first `webView:didFinishLoadForFrame:` delegate message.
 * Fixed: `CPSlider isContinuous` disagreed with `setContinuous:`.
 * Fixed: `CPSliders` always became continuous when archived/unarchived.
 * Fixed: more graceful handling when `nextKeyView` is self.
 * Fixed: when a column was selected the column selection colour would not cover the whole column.
 * Fixed: table views' `rectOfColumn:` method returned a rect reduced by the intercell spacing. It should return the rect of the entire column.
 * Fixed: when table view grid lines were active they did not draw on top of selection highlights like in Cocoa.
 * Fixed: an array controller with a bound `contentArray` would sometimes fail when `add:`, `remove:` and similar methods were called.
 * Fixed #687: `CPColor colorWithCSSString:` did not properly handle the alpha component of the CSS rbga() syntax.
 * Fixed: `CPInvalidArgumentException: Unsupported method on CPArray` when attempting to bind to a `CPArrayController's arrangedObjects` before calling `setContent:`.
 * Fixed #1174: `CPArrayController _arrangedObjects` initialisation error.
 * Fixed: `CPOutlineView` provided dragged items in reverse order.
 * Fixed: once a table view drag and drop was retargeted, the new target would 'stick' as the drag continued.
 * Fixed: the content view of a decoded `CPBox` would have the wrong autoresizing mask.
 * Fixed: unhandled keyboard events of a window did not travel past the window.
 * Fixed: JS objects 'randomly' failed to unarchive due to a caching problem. One visible symptom was that `CPTextField's` custom inset would decode fine, but a subclass of a `CPTextField` would fail to decode the inset.
 * Fixed: table headers didn't scroll with the rest of the table during drag and drop.
 * Fixed: `CGGradientCreateWithColorComponents` assumed there'd only be two colors in each gradient.
 * Fixed #1242: color space was missing for colors created by `CGColorCreateGenericGray`, `CGColorCreateGenericRGB` and `CGColorCreateGenericCMYK`.
 * Fixed #1242: `CGColorCreateCopyWithAlpha` could create colors with an alpha value incorrectly linked to other cached colors.
 * Fixed: crash when the same observer was removed twice. Warn instead.
 * Fixed: out of bounds error in `CPPopUpButton itemWithTitle:`.
 * Fixed: setting a new platform window on a visisble window caused a DOM exception.
 * Fixed: `[CPIndexSet indexPathByRemovingLastIndex]` didn't remove the last index.
 * Fixed: `[CPIndexSet indexes]` did not return a copy of the indexes.
 * Fixed #1249: multiple `_CPImageAndTextViews` sharing the same `CPImage` failed to properly observe its loading.
 * Fixed #684: sizing problem when revealing hidden `CPWebView`.
 * Fixed #664: web view sizing bug when loading contents prior to adding the view to the display tree.
 * Fixed #682: `CPColor isEqual:` sometimes failed to recognise equal instances specified with `colorWithCSSString:`.
 * Fixed: `CPColor isEqual:` for pattern images.
 * Fixed: on WebKit for the Mac, the right command key was not recognised as a modifier.
 * Fixed: duplicate observer notification for array controller `addObject:` (on arrangedObjects).
 * Fixed: `CPTableColumn width`, `minWidth` and `maxWidth` encoding.
 * Fixed: don't return nil from `CPController initWithCoder:`.
 * Fixed: during `CPUserDefault` change notifications, `objectForKey:` could return the value from prior to the change.
 * Fixed: array controller `remove:` would not only remove selected rows, but also any other rows `isEqual:` to the selected rows.
 * Fixed with table view: don't start dragging if there are no rows.
 * Fixed: under some circumstances a `CPMenu` could return a separator as the highligted item.
 * Fixed: pressing the up arrow key in a table view would cause a crash if the previous selection was non continuous.
 * Fixed #1320: if a `CPTextField's` target action changed the first responder then the target action was called twice if the textfield edit was completed by hitting the enter/return key.
 * Fixed #1285: `CPPredicate` would crash if a beginsWith or endsWith comparison was made where the right hand string was longer than the left hand string.
 * Fixed #1305: max toolbar item width was constrained to the width of the label.
 * Fixed with menus: don't disallow `setEnabled:` for auto enabled items.
 * Fixed with token fields: `tokenField:tokenField completionsForSubstring:indexOfToken:indexOfSelectedItem:` ignored its `indexOfToken:` parameter.
 * Fixed: in recent versions of WebKit window.open("") does not work, which broke new platform windows (issue #1352).
 * Fixed: `CPArrayController setSelectionIndexes:` sometimes modified its input.
 * Fixed: several `CPArrayController` methods returned `undefined` instead of booleans.
 * Fixed: `CPWindow` did not return NO to `acceptsFirstResponder` messages.
 * Fixed: multiple errors with key view loops (window's content view not included at the start of the loop, `selectNextKeyView:`, `selectPreviousKeyView:`, `selectKeyViewFollowingView:` and `selectKeyViewPrecedingView:` not acting like in Cocoa).
 * Fixed: `mutableArrayValueForKey:` KVO proxy objects did not use plural selectors (e.g. `remove<Key>AtIndexes:`, `replace<Key>AtIndexes:`) when implemented by the proxied object.
 * Fixed: platform window titles could not be changed once the window had been opened.
 * Fixed with `CPStepper setFrame:` method modified its input.
 * Fixed: `CPRadio` sent its action after a programmatic `setState:` change.
 * Fixed: disappearing or fuzzy table header dividing lines at certain table sizes.
 * Fixed #1376: zombie table group rows.
 * Fixed with `CPTextField`: if a field lost focus while a key was depressed the string value would not update with the last pressed key.
 * Fixed: `CPMenu -removeAllItems` was not KVO compliant.
 * Fixed #1319: `CPPopupButton -selectedIndex` could become wrong when menu items were removed.
 * Fixed #1019: in Internet Explorer, many key equivalents such as left arrow, page up and delete did not work.

### Nib2Cib

 * New: `CPProgressIndicator` support.
 * New: Support for image views in table views.
 * New: Support 'enabled' state for controls.
 * Much improved font support (issue #1197 among others.)
 * Support for `sendsActionOnEndEditing` flag.
 * Improved support for radio buttons (issue #1197).
 * nib2cib support for bold and italic (issue #1266).
 * Much improved button positioning for various button styles (issue #1268).
 * nib2cib support for `NSButtonCell` (e.g. checkboxes) in table columns.
 * Partial button image support in nib2cib covering `NSAddTemplate` and `NSRemoveTemplate` (standard plus and minus buttons).
 * nib2cib support for formatters such as the new number formatter.
 * nib2cib support for token fields.
 * New: XcodeCapp, a graphical utility which automates the nib2cib process and makes it easy to use Xcode 4's Interface Builder to visually create and edit the user interface of a Cappuccino application. XcodeCapp replaces the older command line based xcodecapp utility.

*Bug Fixes:*

 * Fixed: sometimes nib2cibbed check boxes would appear out of place.
 * Fixed #1190: potential `Result of expression '_subviews[index]' [null] is not an object` error for nib2cibbed radio groups.
 * Fixed: could not load theme errors.
 * Fixed #1265: enabled state for `NSColorWell` was not read properly.

### Misc

 * Fixed Objective-J Preprocessor tests: scoping bug that caused only the last file in FILENAMES to be tested.
 * Improved: Xcode 4.0 support for building NativeHost.
 * Documentation updates: new front page, tweaked design and many more documented classes and methods.
 * More complete `capp --help`.
 * man page for `capp`.
 * Fixed #1259: issues finding Mac OS X 10.5 SDK on certain machines when building NativeHost.
 * New: "framework" template for capp which generates a skeleton Cappuccino Framework (issue #1321).
 * Cappuccino moved to a new GitHub location: `https://github.com/cappuccino/cappuccino`.
 * Simplified bootstrap which better hides complexity.
 * When bootstrapping, don't suggest changing `NARWHAL_ENGINE` to `jsc` if it's already `jsc`.

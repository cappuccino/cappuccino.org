---
title: Cappuccino Release Notes
layout: markdown
---

## What's New in Cappuccino 0.9.8

*Release date : 2015-03-29*

Cappuccino 0.9.8 introduces multiline support for CPTextField, Cucapp, XcodeCapp 3.2 and over 300 other changes and improvements.

Highlights in this release:

* New: `@typdef` support.
* New: multi-line support for `CPTextField`.
* New: `CFError`, `CPURLErrors` and `CFError`.
* New: `CPControl -setControlSize:`.
* Redesigned 'CPPredicateEditor' and 'CPRuleEditor'.
* New: all `@protocols` in Foundation and AppKit.
* New: support for `capp_lint` and `objj` to XcodeCapp (now version 3.2).
* Added Cucapp as part of the Cappuccino Project (https://github.com/cappuccino/cucapp)
* New: support for more than 32 theme states in the theming system.
* Fixed: many memory leaks in Foundation and AppKit.
* Optimization of the runtime function `objj_msgSend`.


Foundation and Core
-------------------

* (a1ea371) New: `CPCoding` for `CPAttributedString`.
* (7c6ef51) New: `CPDate +dateByAddingTimeInterval:`.
* (e7ae969) New: `CPNotificationCenter -addObserverName:object:queue:usingBlock:`.
* (fa5fd1e) New: `CPDiacriticInsensitiveSearch` support in `CPString` for the method `-(CPRange)rangeOfString:options:range:`. Added support for strip variants of 'E' 'I' 'O' 'U'.

*Bug Fixes:*

* (1dc84f9) Fixed: issue with `CPDateFormatter -_dateWithTimeZone:` when timeZone is null.
* (acd5442) Fixed: `CPDateFormatter`'s `relativeDateFormating` didn't work in January and was inaccurate for some time intervals around daylight saving time changes.
* (d176dd0) Fixed: `CPNumber +numberWithBool:` broke `CPComparisonPredicate`.
* (a31ad2c) Fixed: `CPAttributedString -isEqual:` true despite attribute differences.
* (9119e08) Fixed: `CPDateFormatter` didn't work for non-"en" locales.
* (06240d1) Fixed: `CPUserDefault -setFloat:forKey:` used `@selector(aValue)` instead of `@selector(floatValue)`.
* (d3490f6) The method `encodeValueOfObjCType` has been renamed to `encodeValueOfObjJType` in `CPCoder`.
* (eb883bc) Refactoring of the classes `CPURLRequest` and `CPURLConnection`:
     * The property `withCredentials` has been moved from `CPURLConnection` to `CPURLRequest`.
     * The accessors `originalRequest` and `currentRequest` have been added to `CPURLConnection`.
     * Added the possibility to make a deep copy of the `CPURLRequest`.
* (b1382e8) Fixed: a `CPOperation` marked as cancelled could not be restarted.
* (fa7b71c) Fixed: constructors of `CPDate` did not raise warnings when the arguments were not `floats` or `ints`.

AppKit
------

* (7b86465) New: protocols `CPTableViewDelegate` and `CPTableViewDataSource`.
* (09eca10) New: protocol `CPAlertDelegate`.
* (4d266f4) New: protocol `CPCollectionViewDelegate`.
* (5b2bfce) New: protocol `CPApplicationDelegate`.
* (db113da) New: protocols `CPOutlineViewDelegate` and `CPOutlineViewDataSource`.
* (7d14676) New: protocol `CPTabViewDelegate`.
* (5dd4266) New: protocol `CPToolbarDelegate`.
* (cc9d896) New: protocol `CPPopoverDelegate`.
* (f8ae610) New: protocol `CPSplitViewDelegate`.
* (7ccdc50) New: protocol `CPAnimationDelegate`.
* (d5af980) New: protocol `CPSoundDelegate`.
* (0a85b4b) New: protocol `CPImageDelegate`.
* (1825887) New: protocol `CPMenuDelegate`.
* (59b80ab) New: protocol `CPComboDelegate`.
* (9b39724) New: protocol `CPRuleEditorDelegate`.
* (1171c9a) New: protocol `CPTokenFieldDelegate`.
* (9d2fba3) New: protocol `CPWindowDelegate`.
* (26118ee) New: protocols `CPControlTextEditingDelegate` and `CPTextFieldDelegate`.
* (2513cf0) New: protocol `CPBrowserDelegate`.
* (25bb51f) New: protocol `CPComboBoxDataSource`.
* (6cae917) New: bidirectional `CPLevelIndicator` behavior.
* (7d304fb) New: support for unlimited number of `CPTheme` state definitions.
* (970b176) New: graphical `CPDatePicker` now reacts correctly to clicks on the arrow buttons with Cmd / ctrl / alt depressed.
* (c1fb54e) New: delegate method `CPTableView -tableView:willRemoveView:forTableColumn:row`.
* (904454d) New: delegate method `CPOutlineView -outlineView:willRemoveView:forTableColumn:item:`.
* (1b351ad) New: `CPColor +checkerBoardColor` for debug use.
* (050fcf2) New: `CPThemeStateFirstResponder` for `CPView`.
* (025a43e) New: `CPThemeStateKeyWindow` for `CPView`.
* (a544854) New: feature to select a set of dates with a shift click in a `CPDatePicker`.
* (0f2ec90) New: support for `documentVisibleRect` in `CPClipView` and `CPScrollView`.
* (7470f4f) New: `CPEvent` `scrollingDeltaX`, `scrollingDeltaY` and `hasPreciseScrollingDeltas`.
* (07c0de7) New: support line-by-line scrolling with old scroll wheel devices in Firefox.
* (12c427a) New: added the method `CPControl -setControlSize:`.
* (3dc581e) New: added the theme attribute `nib2cib-adjustment-frame`.
* (a3796fe) New: the method `-(void)bind:toObject:withKeyPath:options:` now checks if another exclusive binding exists.
* (a3796fe) New: added the private method `+(void)_reverseSetValueFromExclusiveBinderForObject:` in `CPBinder` to send the value back to the bound object when you don't know the original binding name.
* (9c6cca7) New: multi-line support for `CPTextField`.
* (e1d92bd) New: `CPDatePicker` now has a focus ring when editing.
* (fa3f18c) Optimizaton: `CPWindow -setContentView:` now checks that the new view is not the same as the existing content view.


*Bug Fixes:*

* (8b975f5, 8147f64) Fixed: `CPDatePicker` textual issues.
* (21aac76) Fixed: crash in `CPDateFormatter -getObjectValue:forString:errorDescription:` with nil errorDescription.
* (2fc501f) Fixed: `CPDateFormatter -stringFromDate:` did not return a default date.
* (ebccbf2) Fixed: issues with timeZone and the `CPDatePicker`.
* (93b48ba) Fixed: support for dates (`CPDatePicker`) in `CPPredicateEditor`.
* (1814f6b) Fixed: crash when clicking on an empty `CPTableView` with variable row height.
* (821f8fe) Fixed: error when several objects were bound to the same `objectController.selection.keyPath` and the objectController selection changed.
* (d7b5382) Fixed: `CPTabView` did not update its tab's labels when laid out.
* (974942a) Fixed: OS X two finger scrolling issue.
* (86f0724) Fixed: `CPRoundRectBezelStyle` gave a `CPNull` ThemeState.
* (5b4e7df) Fixed: placeholder string shown while editing empty `CPTextField`.
* (be3c4ab) Fixed: `CPPopover` not closing in some browsers.
* (15e16d8) Fixed: editing text fields on different windows could clobber each other's contents.
* (8bdaeab) Fixed: selection behavior when implementing `CPTableView -selectionIndexesForProposedSelection:`
* (1557c56) Fixed: crash due to wrong delegate bitmask in `CPOutlineView`.
* (af83065) Fixed: warning due to use of `aDOMEvent.returnValue`.
* (3e187df) Fixed: `CPPopover transitionend` not correctly called in random cases.
* (07f7ad0) Fixed: crash on Cmd + Z keypress within a control in a `CPPopover`.
* (de4bc67) Fixed: `CPToolTip` added to `CPWindow` wrong.
* (af37616) Fixed: `CPToolTip` still shown when closing a window asynchronously.
* (4dadf0c) Fixed: `CPPopover` did not update its frame after `setContentSize:`.
* (3c0f6d3) Fixed: `CPMenu` enabled state was not visually updated upon change of a bound value.
* (951e811) Fixed: `CPPopover -popverWillShow:` was called too early.
* (584955c) Fixed: `CPPopover -updateFrameWithSize:` always assumed the popover was open.
* (59a9727) Fixed: crash due to `CPTooltip` remaining attached to a closed `CPWindow`.
* (26d6450) Fixed: variable scope in `CPSegmentedControl`.
* (7fc014f) Fixed: `contentInset` theme value read two times in `CPToolBar`.
* (d46b9b5) Fixed: textual `CPDatePicker` stepper incorrectly enabled after decode.
* (61f6ef4) Fixed: crash in `CALayer` when running non-DOM platform.
* (ba27a4c) Fixed: new first responder and key window theme states not always applied.
* (a4702d4) Fixed: illegible white on grey text in `CPTableView`.
* (f953b4d) Fixed: warning when closing a `CPPopover` for the first time.
* (741ac31) Fixed: issue when making the first paste with a right click.
* (089d564) Fixed: `CPDatePicker` firstResponder issue.
* (ac53b30) Fixed: `CPComboBox` doesn't work in modal.
* (1e12973) Fixed: wrong text colour in a `CPTableView` cell when editing another cell.
* (a129f2c) Fixed: `CPTextField` didn't update its style while editing.
* (3364e6c) Fixed: unsigned delegate methods of `CPTokenField` erased by `CPTextField`.
* (cd6ffba) Fixed: `CPPanel` and `CPPopover` didn't close when hitting escape.
* (972c142) Fixed: `CPDatePicker` value became wrong after a stepper was clicked.
* (148f317) Fixed: when closing a `CPPanel` with escape, the delegates were not called.
* (3b9a012) Fixed: `CPTextField -setTextColor:` did not change the color of the placeholder.
* (43ed8be) Fixed: delegate method `popoverWillShow:` called when the popover was already open.
* (7bd27eb) Fixed: crash of press tool when missing theme attribute(s).
* (34072f3) Fixed: `stringValue` was used instead of `intValue` in `CPDatePicker`.
* (f8457bd) Fixed: `CPPopover _closeOnBlur` had accessors.
* (c274f27) Fixed: escape on a `CPanel` or a `CPPopover` broke the key chain event.
* (88954b9) Fixed: `CPCollectionView` height was too low.
* (7de3022) Fixed: animation of a `CPPopover` didn't work as in Cocoa.
* (c642d76) Fixed: `CPPopover` didn't handle semi-transient behavior.
* (3652931) Fixed: `CPTextField -setTextFieldBackgroundColor:` had not effect.
* (4a3f51e) Fixed: `CPDatePicker` did not use days, months, year when used within a `CPPredicateEditor`.
* (293114f) Fixed: delete methods erased entire field in `CPTextField`.
* (01b631a) Fixed: `CPPopover` not showing in correct platform window.
* (d686a0d) Fixed: `CPTextField` bindings delete data in case of multiple selection after tabbing out with no editing.
* (7890085) Fixed: `CPPopover` animation issues.
* (26e29df) Fixed: `CPRuleEditor/CPPredicateEditor` alignments.
* (3e4c038) Fixed: memory leaks in `CPOutlineView` and corrupted itemInfos dictionary.
* (55861a8) Fixed: transient popovers were not closed by a right click.
* (b3f7f44) New: set user event flag based on presence of DOMEvent in `CPTextField`.
* (a04f104) Fixed: checking if a `CPTextField` is usable in a `CPPlatformWindow`.
* (48b3eb2) Fixed: delegate method `popoverDidShow:` not called with a none animated `CPPopover`.
* (b1981bb) Fixed: `activateIgnoringOtherApps:shouldIgnoreOtherApps` did not call `_didBecomeActive` in `CPApplication`.
* (4cebfbc) Removed outdated `collectionViewDidChangeSelection:` delegate method.
* (b2f1477) Fixed: wrong condition in `CPApplication` in `_didBecomeActive`.
* (9ed30f5) Fixed: methods `viewDidMoveToSuperview`, `viewDidMoveToWindow`, `viewWillMoveToSuperview` and `viewWillMoveToWindow` not called as in Cocoa.
* (abdf115) Fixed: memory leaks with `CPNotification`.
* (92a5fa1) Fixed: crash of the `CPOutlineView` when reloading and asssigning an item to another parent.
* (f1cfa14) Fixed: buttons in `CPButtonBar` were never removed from the `CPButtonBar`
* (3f4ba87) Fixed: `CPTooltip` content alignement was mistakenly set to be justified.
* (b922144) Fixed: some tooltips were truncated.
* (fe6a576) Fixed: Aristo 1 close button of inactive windows looked like the same in active windows.
* (f007ecf) Fixed: wrong text-color for `CPDatePicker`.
* (ae5b3c4) Fixed: `CPDatePicker` didn't work in a `CPTableView`.
* (ab4f0f8) Fixed: display-issue in Google Chrome caused by a negative z-index.
* (48276f9) Fixed: `CPPlatformString +sizeWithFont:inWidth` sometimes calculated a width 1 px too narrow.
* (8d036ab) Fixed: backspace in a non-editable or disabled `CPTextField` triggered the browser's page back button.
* (b9b396a) Fixed: `CPButton -setHidden:` in a button bar was not working.
* (1e39281) Fixed: the method `-(void)unbindAllForObject:` of the class `CPBinder` did not work.
* (7db488c) Fixed: memory leaks in `CPImageView` due to the `CPImageDidLoadNotification`.
* (a3796fe) Fixed: memory leaks for the classes `CPPopUpButton`, `CPRadio` and `CPSegmentedControl` when using bindings.
* (83ec89f) Fixed: `CPDatePicker` incorrectly sent an action to its target when using the method `-(void)setObjectValue:` or `-(void)setDateValue:`.
* (c1e89bd) Fixed: `CPDatePicker` did not behave a a `CPTextField` in a `CPTableView` with regards to row selection.
* (b617d60) Fixed: when encoding and decoding a `CPTableView`, several `_CPTableDrawView`s were added to the view.
* (921fcbd) Fixed: the first responder would sometimes stop being the first responder when moved between two views in the same window.
* (5979baa) Fixed: `CPPopover`'s `-popoverShouldClose:` delegate method was not called in transient or semi-transient mode.
* (608480c) `CPPopover` windows now trap the next mouse event automatically if the popover is still visible after a `performClose:`.
* (09e3c5e) Fixed: ability to select part of a textual `CPDatePicker` when dragging.
* (f295667) Fixed: `Key Value Observing` generated new and old values in the change dictionary regardless of the options provided when adding the observer. Now it respects the options passed in the method `addObserver:forKeyPath:options:context:`. This can result in speed improvements of up to 200%.
* (8e346f1) Fixed: when a `CPTableView` had its selection style set to `CPTableViewSelectionHighlightStyleNone`, two clicks were required to select a control in a row.
* (328172c) Fixed: `CPTableView` enabled the bezeled state of a non-selectable `CPTextField` when right clicked.
* (a75e5d9) Fixed: a selectable text mouse cursor style was not shown when the mouse hovered above an enabled and editable or selectable `CPTextField`.
* (2e3c658) Fixed: when closing and reopening a `CPWindow` the first responder would not reset.
* (459374d) Fixed: the menu of `CPComboBox` would not move in tandem with its control's window.
* (f486c02) Fixed: some `CPComboBox` APIs. You can now set the `font`, `alignment`, `intercellSpacing` and `itemHeight` of the `CPComboBox` without `listDelegate`.
* (2dff805) The `content-inset` of a `CPComboBox` has been changed for better alignment.
* (5cad5b0) Fixed: the text cursor of a `CPTextField` didn't take the `content-inset` into account.
* (d8718cc) Fixed: when switching between two `CPPlatformWindow`s, the new targeted window didn't get the first `CPEvent` which instead went to the previous window.
* (d8718cc) Fixed: a `CPPanel` could not be opened in a `CPPlatformWindow` other than the main one.
* (afe326c) New: you can now set a specific height for a `CPTextField` even if a control size is set.
* (5a99e18) Fixed: chaining sheet dialogs in a `CPWindow` wouldn't work.
* (d5b4d66) Fixed: opening a `CPMenu` with items and then opening a `CPMenu` without any items would cause a crash.
* (05d602c) `CPDatePicker` no longer holds the character `CPCarriageReturnCharacter`.
* (c4fbef2) Fixed: crash when dragging the first filter of a `CPRuleEditor` above the first line of the rule editor.
* (f17898d, 0fb7399) Fixed: `CPPopover` would no longer move together with the control it was attached to.
* (3aa8eb9) Fixed: blank screen in some browser. The `z-index` of the main `div` of the Cappuccino is now set to 0 instead of -1000.
* (82dc126) Fixed: memory leaks in the classes `CPTableView`, `CPScrollView`, `CPClipeView`, `CPComboBox`, `CPTextField` and `CPView`.
* (82dc126) Fixed: a null `intercellSpacing` would crash `CPComboBox`. The delegate method `comboBoxWillDismiss:` did not work.
* (f4c2a0a) Fixed: the add and remove button of a `CPPredicateEditor` were blurred.
* (0265fc3) Fixed: the size of a `CPCheckBox` was incorrectly calculated when using the constructor `checkBoxWithTitle:`.
* (02f301d) Fixed: `CPStepper` class method returned `id` instead of `CPStepper` type.
* (f2528b5) Fixed: inconsistent naming of `CPDOMDisplayServerSetStyleBackgroundSize`
* (a2c0b47) Fixed: `CPDatePicker` did not gray out dates outside of minDate and maxDate.

Objective-J
-----------

* (5ab346e) New: the keyword `@typedef` has been added to Objective-J. This keyword allows you to define new types for your application.
* (d3490f6) New: `CFError` has been added to the framework. `CPError` is now toll-free bridged with `CFError`. This mirrors the implementation in Cocoa.
* (d3490f6) New: `CPURLErrors` and `CFNetworkErrors` have been added to the framework. They respect the same error codes as in Cocoa.
* (2411edd) New: faster `objj_msgSend`.
* (3331778) New: `CFHTTPRequest` now accepts the withCredentials property.
* (ffcef90) New: `CPURLRequest` now accepts withCredentials.

*Bug Fixes:*

* (ee668df) Fixed: ivars with accessors in a Category caused a duplicate ivar error.
* (8c43f4f) Fixed: potential error while skipping whitespace in XML plists.
* (1dbd41a) Fixed: error in Internet Explorer if Info.plist was served with the wrong content type.
* (d629a13) Fixed: issue with InvalidStateError when using `CPURLConnection` in IE11.
* (2f7681f) Fixed: the compiler did not show erorrs on the first line of a file.
* (13fe318) Fixed: `Objective-J` now gives an understandable error when the compiler cannot find a protocol in a class declaration.
* (6f90e76) Fixed: the keyword `@ref` did not work correctly if the variable was an ivar.

XcodeCapp
---------

* (973940f) New: integration of `capp_lint` in XcodeCapp.
* (f14add2) New: added option in XcodeCapp for displaying errors in notifications.
* (4806c52) New: update Cappuccino from XcodeCapp.
* (b028e62) New: support of objj in XcodeCapp.
* (148960e) New: XcodeCapp now has an option to select if it becomes active or not when opening the errors & warnings panel.

*Bug Fixes:*

* (8f5aa0e) Fixed: XcodeCapp documentation was outdated.

Nib2cib
-------

* (0cc1679) New: `nib2cib` support for the standard color panel toolbar item.

*Bug Fixes:*

* (4a31467) Fixed: `CPSegementedControl` causes an error in `nib2cib`.
* (e7a0e9a) Fixed: "the built in image NSRadioButton is not supported" error.
* (b28e0d1) Fixed: `nib2cib` of `CPDatePicker` would not convert enabled state.
* (c28da78) Fixed: `nib2cib` of segmented control would not convert enabled state.

Misc
----

* (fadffee) New: `bootstrap.sh` now uses SSL.
* (febce68) New: don't run Travis setup quietly to make it easier to track setup errors.
* (2e015c9) New: `Doxygen` theme refresh.
* (6334458) New: `CFPropertyList` unit tests have been added.
* (79c2576) New: manual `AppKit` tests have been added.
* (9e918cc) New: ability to perform offline bootstraping.
* (cd19fc7) New: `capp_lint` is installed with `jake install`.
* (02f36a1) New: theme kitchen sink manual test to exercise many themable controls in many states at once.
* (b028e62) New: options `-m`, `-I`, `-h` added to `objj` to compile several files.
* (64a15db) New: when building your application you can now disable the `CommonJS` build phase by setting the system environement variable `IGNORE_ENV_COMMONJS`.
* (ef4cd6a) New: `--theme` option for capp tool.
* (06d0357) The Objective-J VIM highlighting has been updated and is similar to the official `Objective-C` VIM highlighting and the official `JavaScript` VIM highlighting.
* (fdc5ed9) New: the configuration files of `doxygen` have been redesigned. The command `jake docset` has been added.

*Bug Fixes:*

* (fa66c26) Fixed: broken documentation.
* (23ff035) Fixed: wrong link to install `homebrew`.
* (d51f179) Fixed: error when running some XML tests with rhino.
* (c21d0c6) Fixed: dependency on tusk in `jakefile`.
* (372372a) Fixed: `capp_lint` didn't handle protocol.
* (8d7c47a) Remove explicit use of Mac OS X 10.5 SDK, replace with latest OS X in `fontinfo`.
* (7958775, 75a4d8a) Fixed: `bootstrap.sh` didn't handle specific OpenJDK Runtime Environment version. `bootstrap.sh` could not filter the OpenJDK version key out correctly.
* (a822ec7) Fixed: `jake` did not work in the Cappuccino directory for non-Mac OS X systems.
* (e155cca) Old CI scripts have been removed from the Tools directory.
* (c484e4a) NativeHost is no longer built by default.
* (c3fc6a0) Fixed: the URL of the current release version of Cappuccino was wrong in the documentation.
* (e40612a) Fixed: in the `Jakefile` template, the configuration build environment parameter could have multiple values. Now this variable is correctly set by detecting the build environment.
* (de3eb86) Fixed: some warnings when compiling Cappuccino with `rhino`.
* (ee688d9) Fixed: showcase of themes was broken.

OJTest
------
* (1ab1ac2) New: ability to launch a set of tests from a test file.
* (9bb55a2) New: `+setUp` and `+tearDown` methods.
* (410d9ce) New: print the number of tests launched by `OJTest`.
* (080b5b7) New: warnings raised when tests are declared several times.

*Bug Fixes:*

* (1f6cc19) Fixed: coverage options for `OJTest`.

Other Changes
-------------

The changes above summarise a few hundred of the most important changes in Cappuccino 0.9.8. You can review the other 700 or so changes in the [0.9.7...0.9.8 compare view](https://github.com/cappuccino/cappuccino/compare/0.9.7...0.9.8).


## What's New in Cappuccino 0.9.7

*Release date: 2013-11-28*

Cappuccino 0.9.7 introduces Aristo 2, Objective-J 2.0 and over 500 other changes and improvements.

Highlights in this release:

 * Objective-J 2.0: dictionary literals, array literals, pass by reference and protocols.
 * Compiler rewritten from ground up to generate faster than ever Cappuccino application code.
 * Aristo 2 - a new, lighter Cappuccino theme made by Sofa.
 * Native browser copy and paste support.
 * Scalable `CPView` ('zoom in' or out within a view and all its subviews).
 * Multiple-value bindings support.
 * Lion style "view based" `CPTableView`. While Cappuccino already supported view based table views, this new API matches Cocoa's and allows more convenient table customisation in Interface Builder and easier use of bindings (such as when binding a custom table cell view to a key of the row data).
 * XcodeCapp 3 featuring a much smoother experience with project history, speed and robustness improvements and throughout better UI.
 * `CPDatePicker`.
 * `CPLocale`.
 * `- CPObject performSelector:withObject:afterDelay:`.
 * `CPError`.
 * `CPByteCountFormatter`.


Foundation and Core
-------------------
* (176440e) New: `- CPURLConnection sendSynchronousRequest:` return nil if `CPHTTPRequest` failed.
* (76e9725) New: error on adding `CPNotFound` to an index set.
* (75d73d3) New: format object descriptions like object literals.
* (55ec70c) New: `CPError` class.
* (04026c0) New: faster `- CPArray objectsAtIndexes:` when the array is a native array (up to 6X).
* (0268f98) New: faster `- CPMutableArray removeObjectIdenticalTo:` when the array is a native array (up to 10X).
* (5200f94) New: dictionary literals in Objective-J 2.0.
* (472848d) New: array literals in Objective-J 2.0.
* (f4b08a9) New: `- CPObject performSelector:withObject:afterDelay:` and related methods.
* (34faf36) New: @ref and @deref in Objective-J 2.0.
* (c550cd7) New: optimise `- CPArray enumerateObjectsWithOptions:usingBlock:`.
* (ecc1e77) New: added macro/identifier concatenation with the '##' operator.
* (a373081) New: `CFBundle.identifier`, `CFBundle.bundleWithIdentifier`, `- CPBundle -bundleWithIdentifier`.
* (fe26e6c) New: `+ CPException raise:format:`.
* (1f280b3) New: `- CPNumberFormatter localizedStringFromNumber:numberStyle:`.
* (bf94dd3) New: KVC `setValue:forKey:` now automatically unwraps `CPValue`.
* (d3a44cb) New: `objj_getClassList()`.
* (4221acf) New: more fine-grained `OBJJ_PROGRESS_CALLBACK` calls, allowing smoother progress bars.
* (42ad40d) New: sort the keys in `- CPDictionary description`.  This makes it easier to find an item in a large dictionary.
* (d38125d) New: Objective-J protocols supports.
* (d3ab2a0) New: "//example.com/x" style URL support in `CPURL` and `CFURL`.

*Bug Fixes:*

* (13fbfb6) Fix to enable the startup loader to continue if dynamically loaded.
* (23401d3) Fixed: error in function `CPDescriptionOfObject` when a JSON object property has a null value.
* (24d6e58) Fixed: `CPPredicate TRUEPREDICATE` didn't work.
* (1f0ab2a) Fixed: bad formatting of negative numbers by `CPNumberFormatter`.
* (2371438) Fixed: KVC array `removeObjectsInArray:`.
* (b34e24d) Fixed: `mutableArrayValueForKey: … removeObjectsInArray` should remove all instances of the found objects.
* (e17253d) Fixed: `CPDecimalCompare` problems when comparing to zero.
* (181c4ad) Fixed: support IBOutlet as a synonym to @outlet.
* (63ae584) Fixed: `CPDecimalRound` should return a result in all cases.
* (fc403d6) Fixed: `CPString compare:` method against nil and `CPNull`.
* (f52f118) Fixed: array sort using descriptors involving nil and `CPNull`.
* (c437024) Fixed: subclasses of `CPMutableArray` had broken `removeObject:`.
* (6d1c4a9) Fixed: `- CPMutableArray removeObjectIdenticalTo:` did not remove all instances, was documented incorrectly.
* (ae2ed8b) Fixed: `CPAttributedString` problems with empty strings and out of range indexes.
* (6ee3a39) `- CPDictionary setObject:forKey:` will log deprecated warning when passing nil object or key.
* (5312524) Fixed: define navigator.userAgent as another ugly Rhino fix.
* (7bef84e) Fixed: allow `CPDecimal` to handle decimal numbers with leading zeros.
* (7d51a34) Fixed: `- CPUndoManager isUndoRegistrationEnabled`.
* (39b49d4) Fixed: `CPNumberFormatter` formatted @"" wrong.
* (bd6d2e7) Fixed: `CPString stringByTrimmingCharactersInSet`.
* (05fa505) Fixed: `CPArray` did not allow binding to @count.
* (cc2503a) Fixed: `CFBundle.prototype.bundleURL()` did not return an absolute URL.
* (d64ea28) Fixed: `- CPBundle bundleWithIdentifier` did not create `CPBundle` when necessary.
* (ffdee8c) Fixed: `[CPExpression isEqual:nil]` and `[CPPredicate isEqual:nil]`.
* (fe79628) Fixed: `CGRectFromString` made bad `CGSizeFromString` call.
* (2290574) Fixed: crash on `CPArray/CPDictionary description` if a value was the window object.
* (e59389b) Fixed: crash in `CPArray/CPDictionary description` containing self referential JS object.
* (0f53ced) Fixed: comparing a `CPNumber` vs nil or `CPNull` didn't throw an exception.
* (3419f6f) `CPTimer` number of seconds interval set to 0.1 if equal to 0.0, like in Cocoa.
* (f75955b) Fixed: `CPNumberFormatter` minimum and maximum wrong encoding when set to nil.
* (df2be92) Fixed: `CPNumber numberWithBool:` not returning a number.

AppKit
------
* (bafd62d) New: `- CPCollectionView draggingViewForItemsAtIndexes:withEvent:offset:`.
* (27cda34) New: improve performance of row and column drag and drop for `CPTableView`.
* (67f7649) New: `CPTableView` with Lion's view-based API.
* (4369f4b) New: set `CPThemeStateEditable` in `CPTextField setEditable:`.
* (f4904b8) New: `- CPCib initWithContentsOfURL:` return nil if the returned data is nil.
* (7bf5f6f) New: added `scrollRectToVisible` when `CPTokenField` becomes first responder.
* (8b5c0fb) New: CPCollectionView - allow the prototype view to be loaded from a cib.
* (6561e4f) New: Aristo 2 theme.
* (4757648) New: CPAlert can be moved now.
* (edc6244) New: make `CPBox` themable.
* (b82225e) New: make `CPLevelIndicator` themable.
* (347de2c) New: make `CPSplitView` themable.
* (2da0142) New: make find/search/cancel buttons themable.
* (ce33737) New: make `CPBrowser` themable.
* (844ed59) New: `CPCursor` will now look in the theme to get system cursors.
* (cebf8d3) New: make standard template images plus, minus and action themable.
* (f30e846) New: added theme value to set the position of the buttons relative to the type of window.
* (3b72626) New: added inactive state to window title bar (for windows which are neither key nor main).
* (348d689) New: close popovers attached to controls in windows which close.
* (25633f0) New: child window support.
* (b3bf190) New: reduce the menu sticky interval to 0.4s which improves UX and is more like Cocoa behavior.
* (8cbfc79) New: makes popover's background and stroke color (both minimal and HUD style) themable.
* (18d77ca) New: `CPTokenField` menu per token support (`tokenField:menuForRepresentedObject:`).
* (4680f0f) New: `CPGradient initWithStartingColor:endingColor:`.
* (d1ebf8d) New: make `CPShadow` mutable (e.g. `setShadowColor:`).
* (08ad614) New: `- CPGradient drawInBezierPath:angle:`.
* (e376f97) New: `- CPShadow set`.
* (8b17b52) New: `value` and `isIndeterminate` binding support for `CPProgressIndicator`.
* (4791973) New: don't limit max number of rows for collection views if max number of rows is set to 0.
* (055d43e) New: custom system cursors to use sprited PNG's for non IE browsers.
* (1c6d2f7) New: don't change the platform window's title unless the Cappuccino window is full platform.
* (e03622b) New: `+ CPBezierPath bezierPathWithRoundedRect:xRadius:yRadius:`.
* (02b7198) New: action bindings for `CPMenuItem`.
* (cd54687) New: when a column header is pressed and is the _editingColumn, make the table view first responder.
* (92c2ed9) New: table view `selectAll:` and `deselectAll:`.
* (3591ba0) New: CPImageView bindings improvements.
* (a9952a2) New: CPRadioGroup bindings - `selectedValue`, `selectedTag`, `selectedIndex`, `enabled` and `hidden`.
* (77d2ebb) New: `shouldReorderColumn` delegate method for `CPTableView`.
* (262bd5b) New: use dedicated class, `_CPStateMarker`, instead of `CPString` for selection markers.
* (72c277d) New: `CPSegmentedControl` segment selection bindings support.
* (7fab8d9) New: don't allow views from another window to be next/previouskeyViews.
* (ab692bb) New: `CGContextSetLineDash`.
* (ffbd981) New: `- CPBezierPath setLineDash:` and `getLineDash:`.
* (5868a4c) New: `- CPDocumentController documentForWindow` and `hasEditedDocuments`.
* (1649ea6) New: `CPDatePicker`.
* (1649ea6) New: `CPLocale`.
* (6ef5b46) New: `CPTokenField` sends focus and blur notifications.
* (100f1b0) New: about panel is now constructed in code, rather than in a CIB.
* (95d4bef) New: `- CPColor hueComponent`, `saturationComponent` and `brightnessComponent`.
* (7b59ec9) New: allow sheets to have toolbars.
* (44a8726) New: type check - `CPPasteBoard setString:forType:` to catch strange bugs earlier.
* (ad33411) New: `CGContextDrawRadialGradient` support.
* (25f54c8) New: `CGPathContainsPoint`.
* (a9a0b1c) New: JavaScript clipboard API support for pasting.
* (93c2762) New: improve `CPPopover` theamability.
* (b258b1a) New: appkit_tag_dom_elements now tags with UIDs too. Tagging with UIDs can make it much easier to debug encoding/decoding related bugs where it's not clear that the right view ended up in the right spot.
* (5a7c2e5) New: added themable attribute for grid line thickness in table view.
* (7f08997) New: added themable attribute for divider thickness in table header view.
* (2183c6d) New: added methods to globally turn off window constraining when resizing the platform window.
* (fc93190) New: notify when the platform window resizes.
* (377618d) New: non-editable but selectable text fields can become the first responder.
* (03acecd) New: selectable text field Select All (Cmd-A, Ctrl-A) support.
* (638d8de) New: triple-click selectable text field to select all.
* (648dc6e) New: Edit > Delete menu item support for text fields.
* (5958220) New: `- CPTextField deleteForward:`.
* (08eff6e) New: grey out Edit menu non applicable items for text fields.
* (8503081) New: `shouldExpand/Collapse` delegate for `CPOutlineView`.
* (ef5f26f) New: added support for scaling in `CPView` (`scaleUnitSquareToSize` and `setScaleSize`).
* (cf19aef) New: added method `selectionIndexesForProposedSelection` in `CPOutlineView`.
* (ebc1025) New: fill in `userInfo` for `CPTextDidEndEditingNotification`.
* (1cec1b0) New: `CPTableView` drop view themable.
* (6a7e0ff) Reworked PatternColor to be a lot smarter, support much more concise expression of images.
* (abaa1e8) New: support for multiple-value bindings.
* (a011596) New: `CGContext`: render any arbitrary drawing to a pattern context and use that as a fill or stroke pattern.
* (2b23374) New: `CPAlert` custom didEnd selector or block.

*Bug Fixes:*

* (57c8d22) Fixed: `CPCollectionView` dragging: bug where the dragging view was created from content instead of selection.
* (5384a9e) Fixed: `CPTableView` auto-save columns.
* (9ef9bf9) Fixed: `CPFlashView` minor bugs.
* (0582033) Fixed: `CPArrayController` selection binding failure in retrieving initial selection values.
* (ada73a1) Fixed: left/right cursors in `CPBrowser`.
* (1d1f2d7) Fixed: `scrollRectToVisible` in `CPView`.
* (0892ca1) Fixed: popovers could overlap the menu bar.
* (21b5ead) Fixed: drag and drop error with `CPCollectionView` when the collection view is a drop destination but not a source.
* (f403699) Fixed: bug with content-inset in text field.
* (f8e7250) Fixed: bug with closable button in `CPWindow`.
* (7e502ff) Fixed: sizing bug with `CPStepper`.
* (9f85d2b) Fixed: scroll-wheel in FF 3+.
* (765b106) Fixed: mouse location in key events and copy event.
* (c5fbeff) Fixed: position of buttons in an alert.
* (fdbef47) Fixed: popover positioning errors, especially when closing the window from which the popover came.
* (57b2d73) Fixed: undefined location of key events.
* (bfb85cc) Fixed: minor visual errors with `CPMenu`.
* (49c52a0) Fixed: disappearing token delete button.
* (0f64616) Fixed: crash in token field autocomplete.
* (3d9b69a) Fixed: broken corners on primary `CPBox` in Chrome.
* (6b0565e) Fixed: `CPBox` with `CPBezelBorder` had unexpected inner shadow.
* (4991913) Fixed: blurry popovers in Chrome.
* (baa69ff) Fixed: "cannot read property '_tokenScrollView' of null."
* (535b8e5) Fixed: orphan token field autocomplete menus.
* (933a1be) Fixed: `- CPWindow setRepresentedFilename:` set as a string, not a `CPURL`.
* (ab49c63) Fixed: `CPArrayController add:` adding wrong object, `insert:` not inserting in right position when there's a selection.
* (1f19e02) Fixed: `CPWebView` scroll-wheel.
* (5427e9a) Fixed: column drag and drop in the table view.
* (4ec3b5e) Fixed: add missing `isClockwise` property to `CGPath`.
* (7ab84ca) Fixed: bugs in `CGContextCanvas` and `CGPath`.
* (09b5eef) Fixed: [CPBox setContentView:nil] crash.  This is allowed in Cocoa so should not crash Cappuccino either.
* (a19ec35) Fixed: broken tab view decoded from xib in certain situation.
* (7c677de) Fixed: bugs in `CPColorWithImages` and `CPImageInBundle`.
* (a011596) Fixed: `CGContext` fixes/enhancements.
* (e40138c) Fixed: `CPToolbar` calls incorrect notification method.
* (ce7e512) Fixed: `CPView removeFromSuperview` performance.
* (84f42bd) Fixed: decoding a `CPClipView` could result in duplicate subviews.
* (a736bb4) Fixed: empty content view allowed when resizing a window.
* (471641c) Fixed: subviews in cib did not receive `view(Will/Did)MoveToSuperview:`.
* (2cb3450) Fixed: `CGPathEqualToPath` did not compare all subpath types.
* (a6fafcd) Fixed: inadvertent grid lines in token field menu.
* (ee20038) Fixed: `CPWebScriptObject callWebScriptMethod:withArguments:`.
* (b7ff643) Fixed: when clicking and dragging inside a menu, `mouseEntered` and `mouseExited` was mixed up for custom views.
* (62ced17) Fixed: if a menu item had no item, no target, and no action binding, it could still be left enabled after validation.
* (4605130) Fixed: `resizeWithOldSuperviewSize` not working like in Cocoa.
* (11c6b66) Fixed: wrong placeholder string in `CPTextField` when using bindings.
* (152fd66) Fixed: reordering table view column with a restriction on a targeted column.
* (2bf2442) Fixed: using keyboard navigation in empty `CPCollectionView` threw exception.
* (ff15f11) Fixed: transient popover windows would close on mouse interaction with certain controls.
* (6327d8c) Fixed: transient popovers broke modal windows.
* (59b766e) Fixed: token field autocomplete menu not receiving mouse events in presence of modal window.
* (5f086b1) Fixed: a platform window could be resized by clicking just under the menu bar and dragging downwards, even that platform windows are supposed to be the size of the browser window by definition.
* (2dca00c) Fixed: sheets could be resized from the top.
* (f208ff5) Fixed: attached sheet shadow had extra width, was too dark.
* (17f9304) Fixed: sheet animation was resizing the sheet to zero, causing problems.
* (3af2314) Fixed: sheets resizing incorrectly.
* (6c80d1f) Fixed: `resizeWithOldSuperviewSize` did not maintain size ratio.
* (4450455) Fixed: frame/bounds change notification sent needlessly.
* (bbfaac5) Fixed: windows were allowed to extend beyond the usable screen content.
* (481f7c6) Fixed: browser would scroll text fields into view when they focused.
* (50ca0d4) Fixed: menubar title was set to document title.
* (677124d) Fixed: another tab view decoding error.
* (8d54c01) Fixed: menus not closing on left click.
* (843e501) Fixed: modal sheet would appear briefly before animation.
* (92fb9ea) Fixed: if a sheet's parent window frame was changed, the sheet did not reposition.
* (2dd7ba6) Fixed: sheet top shadow would not adjust when parent window was resized.
* (25d5441) Fixed: sheet opening animation was not cleaned up when sheet immediately closed.
* (3301754) Fixed: a sheet's parent window did not become main.
* (7df34cc) Fixed: windows with sheets were filtering mouse move events.
* (1e98c66) Fixed: under some circumstances, blur function could be called with no `CPTextFieldInputOwner` set.
* (facd97c) Fixed: if `orderOut:` was not called for a popover, it would not detach from its parent.
* (dc96b38) Fixed: popovers were not constrained to the usable content frame.
* (03b6634) Fixed: couldn't set the first responder of a sheet.
* (35dd35d) Fixed: array controller failed to recognize row 0 as the insert location.
* (6dc9aa8) Fixed: eliminated duplicate `CPThemeStateSelectedTableDataView`.
* (7225e7e) Fixed: deprecate `-tableView:dataViewForTableColumn:row:` and `-outlineView:dataViewForTableColumn:item:`
* (33858cf) Fixed: incorrect table column highlighting and row selection after column sort.
* (720b61f) Fixed: close pull down menu on second click on its button.
* (fd20a80) Fixed: table view selection color did not change when losing focus.
* (b36f8d7) Fixed: unfocused selection highlight in table upside down.
* (efdf0a6) Fixed: when editing a table cell, the row lost focus.
* (afc2c17) Fixed: highlighted table cells with `CPTableViewSelectionHighlightStyleNone` had white text.
* (3178f0b) Fixed: `CPDocumentController` missing method `currentDocument`.
* (3ef5cfe) Fixed: infinite loop when a first responder has a nil superview.
* (6d0caac) Fixed: `setAnimates:` on a popover would only be applied after closing/reopening the popover.
* (aa0602d) Fixed: fix a memory leak in `_CPImageAndTextView.j`.
* (c6a59d7) Fixed: `CPMenuBar` theming.
* (59d1da7) Fixed: setting `CPNullPlaceholderBindingOption` in binding was setting the actual value of a text field instead of just its placeholder.
* (71cc825) Fixed: `CPMenu` ghosts after many right clicks.
* (cc9ff15) Fixed: if a menu was dismissed with and item highlighted, and then the item was used in another menu (e.g., re-added to a context menu for a table row) it would appear highlighted, even though the menu highlight index was not set.
* (6e2dcd5) Fixed: delegate method fires twice when using keyboard to select rows in table view.
* (40579b5) Fixed: parameter range of `CPColor colorWithHue:saturation:brightness:` were in degrees and percent rather than factors.
* (4e1a141) Fixed: `- CPColor hsbComponents` range.
* (d00846a) Fixed: `CPColor colorWithHue:saturation:brightness:` parameters not clamped.
* (70b5105) Fixed: `CPColor colorWithHue:saturation:brightness:` returning undefined.
* (056a00e) Fixed: `CPComboBox` popupList should close if mouse is clicked outside of the control.
* (81a61c1) Fixed: trying to open a `CPPopover` in a secondary platform window opened in the main window.
* (6bd9a08) Fixed: `CPAlert` always shows on main platform window.
* (a38d6c1) Fixed: tooltips always showing in primary platform window.
* (3e268a8) Fixed: outline view disclosure button not always becoming selected when its row was.
* (2e93e4a) Fixed: sheets not appearing underneath toolbar if one was present.
* (eacc527) Fixed: tooltips not always showing.
* (9ffa184) Fixed: IE8/9 drawing errors for negative size views.
* (6701117) Fixed: `[pasteboard declareTypes:...owner:nil]` would emit a warning.
* (5e0793c) Fixed: fixed small init bug in `CPBezierPath`.
* (de4e28b) Fixed: fixed bug with linear gradient when drawing it without `CPGradient`.
* (b5df5f7) Fixed: `CGPath` wrong when creating an arc.
* (8d7e2f9) Fixed: `CPCollectionView` range bounds exception if shift key was held for first selection.
* (3b48aaf) Fixed: table view `removeTableColumn:` did not remove column from tableColumns array.
* (8bf2118) Fixed: selection possible in a tableView without any columns.
* (2cbc4d9) Fixed: `CPWindows` contentView "Autoresizes Subviews" set in Cib not honoured.
* (22dcacd) Fixed: remove non-standard `CPDocument` API "firstEligibleExistingWindowController".
* (198857e) Fixed: copying from a `CPTextField` would not actually put the string value in the Cappuccino pasteboard.
* (f318759) Fixed: menu items becoming permanently disabled, breaking e.g. Select All.
* (6ef776e) Fixed: `- CPView nextValidKeyView` infinite loop.
* (e7ecd92) Fixed: custom `CPWindow` subclasses breaking flatten.
* (d61d4eb) Fixed: `-CPImage initWithContentsOfFile:nil` created broken image.
* (54d13c8) Fixed: `CPImageView`'s _DOMImageElement was not created during initWithCoder.
* (64f962e) Fixed: `viewDidHide` and `viewDidUnhide` were not called when a view was being added to/removed from hidden ancestor.
* (7788435) Fixed: `CPTextField` would not become/resign key responder when first responder and unhidden/hidden.
* (650bc77) Fixed: number formatter was called twice for every `setObjectValue`.
* (27165db) Fixed: menu items would not obey enabled bindings for auto-enabling menus.
* (5b62773) Fixed: off-by-one in row calculation caused drawing problems with variable-height rows in `CPTableView`.
* (d8281a6) Simplified the overlay scroller test.
* (b49a872) Fixed: IE could scroll entire app to the left.
* (e61b678) Fixed: crash when the autocomplete menu of a token field is visible while one of the superviews is removed.
* (3c2a2f3) Fixed: resizing a window did not attempt to maintain a minimum margin on screen.
* (6bec406) Fixed: window width was not constrained when platform window was resized.
* (d751fea) Fixed: constraining window's to the screen did not respect a window's minSize.
* (8d47b3f) Fixed: `CGContextAddArc` would fail if the path was empty.
* (4b4ac5d) Fixed: certain actions could edit a non-editable text field.
* (a90180a) Fixed: `- CPTextField copy:` only worked for editable text fields.
* (0e7b592) Fixed: certain editing actions were allowed for disabled text fields.
* (2065c7f) Fixed: `CPTextField deleteBackward:` left 1 character.
* (ec4b348) Fixed: a disabled `CPMenuItem` could still have a selected background.
* (58d5d7d) Fixed: selectable text deselected when a menu was clicked.
* (376b3a4) Fixed: copy and paste by Cappuccino Edit menu not working.
* (9d43a55) Fixed: `- CPTextField deleteBackward:` required a selection.
* (0b5a98d) Fixed: `lineBreakMode` set to `CPLineBreakByTruncating*` was trimming consecutive white spaces.
* (016c267) Fixed: order of deletegate messages from `CPTableView`.
* (2df13b7) Fixed: `CPComboBox` not reacting correctly when its menu scroll bar was clicked.
* (0afc903) Fixed: delegate method `shouldSelectItem` in `CPOutlineView`.
* (c22f489) Fixed: `shouldSelectTableColumn` not called by `CPTableView` and `CPOutlineView`.
* (d1406e1) Fixed: editing text fields could clobber the changes made in one window with those made in another.
* (ff06737) Fixed: fix first responder assignment when pressing a table view header column.
* (e058d2e) Fixed: double clicking something to open/close a sheet.
* (aeb42ea) New: `CPByteCountFormatter`, a complete implementation of `NSByteCountFormatter`.

nib2cib
-------
* (5a99011) New: support for `CPView` identifier property.
* (c2cad3c) New: NSNib support. NSNib are represented as data inside nib files.
* (2bd5696) New: info message when converting `NSTableCellView` nib to plist.
* (744f3d7) New: allow `CPCheckBox` and `CPRadio` to have themed height and adjusts it correctly.
* (7ff8bda) New: CPDictionaryController initial commit.
* (4188b27) New: move special per class nib2cib processing to the classes themselves in `awakeFromNib`.  Having class specific code in the class makes more sense, and this will make it easier to add more class specific transformations.
* (d9117bd) New: enable use of image resources from frameworks, not just main bundle resources folder.
* (0bbaec0) New: `CPDateFormatter` and `CPTimeZone` support.
* (9cb2c75) New: --no-colors option for nib2cib.
* (0b7e92a) New: better logging of image bundle info in nib2cib.
* (a63bb15) New: nib2cib gives a more helpful message when unsupported classes are encountered.
* (72169e5) New: nib2cib support for runtime attributes of point, size, rect and range types.

*Bug Fixes:*

* (a5e62ed) Fixed: `NSMenu autoEnablesItems` was not supported.
* (fa70827) Fixed: normal, small and mini label placement.
* (da47161) Fixed: nib2cib error on case sensitive filesystems.
* (3239337) Fixed: `CPScroller` orientation import.
* (1cb8844) Fixed: custom NSBoxes placed in Xcode became smaller in Cappuccino.
* (f805b6b) Fixed: `CPTabView` decoding causing tab selection errors.
* (5fac631) Fixed: minimum/maximum support for `CPNumberFormatter`.
* (8055808) Fixed: table view cells with custom font/color did not change properly when selected.
* (2f71b8d) Fixed: handling of custom styled table text cells.
* (d654562) Fixed: import of `CPComboBox` enabled state.
* (7154252) Fixed: import of `CPTextField` enabled state.
* (9d69ec7) Fixed: size of table view corner view.
* (083310c) Fixed: nib2cib did not allow xibs or images to be in subdirectories of Resources.

Misc
----
* (606205b) New: XcodeCapp 3, retina ready, notification center support, new icons, speed improvements throughout and many new features.
* (628a4db) New: improved error reporting from XcodeCapp.
* (5a558a9) New: eliminated the "SomethingElse" framework that no one actually removes.
* (238b6c8) New: modernize index[-debug].html, IE 9+ now run in edge mode.
* (9e7346f) New: new index.html with loading progress by default.

*Bug Fixes:*

* (229e43f) Fixed: fix build path when $CAPP_BUILD not defined.
* (450081e) Fixed: 'cannot run program "ulimit"' error.
* (9c0c87d) Remove some of the more nonsensical main menu items in the NibApplication template.
* (e10ce7a) Improve bootstrap.sh compatibility with ZSH.
* (054421c) Fixed: crash with Rhino in fontinfo due to missing import.


Other Changes
-------------

The changes above summarise a few hundred of the most important changes in Cappuccino 0.9.7. You can review the other 1000 or so changes in the [0.9.6...0.9.7 compare view](https://github.com/cappuccino/cappuccino/compare/0.9.6...0.9.7).

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

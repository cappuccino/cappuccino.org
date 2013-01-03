---
title: Cappuccino News
author: Aparajita Fishman
author_email: aparajita@aparajitaworld.com
wordpress_id: 1270
wordpress_url: http://cappuccino.org/discuss/?p=1270
date: '2012-04-10'
tags:
- Cappuccino
- Update
---


What's new in Cappuccino in the past two weeks:

- Some major new features have been added to `nib2cib`:

    * `nib2cib` now supports User Defined Runtime Attributes in Interface Builder.
    * `nib2cib` now supports userland NS classes. This is a huge new feature that allows you to add `nib2cib` support for your own classes without modifying `nib2cib`. Along with User Defined Runtime Attributes, you can now place and configure your own view classes in `nib2cib`!
    * `nib2cib` now supports file-based configuration options, which is important when you are using XcodeCapp.

    See the `nib2cib` man page for more information on the new `nib2cib` features.

- If you ever looked at the DOM elements to figure out why your views are not laid out the way you want, this feature is for you. Put the following line in your index-debug.html `<script>` section where Objective-J is configured:

        appkit_tag_dom_elements = true;

    This will add an attribute called "data-cappuccino-view" to all DOM elements that are created by CPView (and subclasses). The value of the attribute is the class name. Great for debugging the view hierarchy!

- The functions `CGInsetUnion` and `CGInsetDifference` have been added.

- We now have small and mini progress indicator images for use with `CPProgressIndicator`. (Thanks daboe01)

- Popovers have cool new animation and are a lot more robust.

- The capp ThemeDescriptor template has been enhanced to automatically symlink BlendKit so that you can run the theme showcase without any extra work.

- A new command line tool, `dump_theme`, has been added. You can use this to view a formatted dump of any theme. Use 'man dump_theme' for more info.

- Option/Alt-clicking on a disclosure toggle of a `CPOutlineView` will recursively expand the item and all of its children. (Thanks Blair Duncan)

- Added `CPURL -URLByDeletingLastPathComponent`.

- Windows now automatically set up the key loop and if no view has been set as the initial first responder, sets the first key view as the initial first responder.

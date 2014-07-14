---
title: Cappuccino News 2014 July 14th
author: Alexandre Wilhelm
author_email: alexandre.wilhelmfr@gmail.com
date: '2014-07-14'
tags:
- Cappuccino
- update
---

Here's a quick update on what's new with Cappuccino for the last two weeks.

#### Community

- Developers of `Cappuccino` are now on http://gitter.im/cappuccino/cappuccino. Don't hesitate to come and ask whatever you want!

#### New features

- `Cucapp` is now available in a sub-repository of `Cappuccino` (https://github.com/cappuccino/cucapp). Thanks Daniel Parnell!

- Some new major features have been added to `Cucapp`:
    * `Cucapp` provides several environment variables to configure your tests.
    * `Cucapp` supports file names such as `CPTextField+IP.j`.
    * Internal categories were added to help you manage specific actions.
    * `cucappIdentifier`, added by one of the above categories, allows you to easily access a `CPResponder` in your tests.
    * A set of new APIs were added. Yyou can now simulate mouse/keyboard events in your tests.

- The `CPPopover` works with the behavior `CPPopoverBehaviorSemitransient`.

- `CPURLConnection` now accepts `withCredentials`. This option has the same behavior as the option `withCredentials` for an `XMLHttpRequest`.

- The methods `+(void)setUp` and `+(void)tearDown` are now called when launching a test with `OJUnit`.

- `OJUnit` provides an option to run only one test now.

#### Changes/Fixes

- The escape key works as in Cocoa when a `CPPopover` or `CPPanel` is open.

- Animation of a `CPopover` works as in Cocoa when disappearing.

- `CPAttributedString` coalesces attributes correctly.

#### Commits/Issues/Pull Requests

* 3 commits to master
* 63 commits to all branches
* 255 additions
* 85 deletions
* 4 merged pull requests
* 1 closed issue

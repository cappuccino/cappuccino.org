---
title: Cappuccino News
author: Alexandre Wilhelm
author_email: alexandre.wilhelmfr@gmail.com
date: '2014-07-14'
tags:
- Cappuccino
- update
---

Here's a quick update on what's new with Cappuccino this last two weeks.

#### Community

- Developers of `Cappuccino` are now on http://gitter.im/cappuccino/cappuccino. Don't hesitate to come and ask whatever you want !

#### New features

- `Cucapp` is now available in a sub-repository of `Cappuccino` (https://github.com/cappuccino/cucapp). Thanks Daniel Parnell !

- Some new major features have been added to `Cucapp`:
    * `Cucapp` provides several environment variables to configure your tests.
    * `Cucapp` supports name file as CPTextField+IP.j.
    * Internal categories were added to help you to manage specific actions.
    * One of this category proposes the variable `cucappIdentifier` to allow you to access easily to a `CPResponder` in your tests.
    * A set of new API were added. In overall you can now simulate mouse/keyboard events in your tests.


- The `CPPopover` works with the behavior `CPPopoverBehaviorSemitransient`.

- `CPURLConnection` proposes a new option `withCredentials`. This option has the same behavior as the option `withCredentials` for a `XMLHttpRequest`.

- The methods `+(void)setUp` and `+(void)tearDown` are now called when launching a test with `OJUnit`.

- `OJUnit` provides an option to launch only one test now.

#### Changes/Fixes

- The hit of the key escape works as in `cocoa` when a `CPPopover` or `CPPanel` is opened.

- Animation of a `CPopover` works as in `cocoa` when disappearing.

- `CPAttributedString` coalesces his attributes as `cocoa` does.

#### Commits/Issues/Pull Requests

* 3 commits to master
* 63 commits to all branches
* 255 additions
* 85 deletions
* 4 merged pull requests
* 1 closed issue

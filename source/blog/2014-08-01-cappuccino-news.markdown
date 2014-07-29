---
title: Cappuccino News 2014 August 1st
author: Alexandre Wilhelm
author_email: alexandre.wilhelmfr@gmail.com
date: '2014-08-11'
tags:
- Cappuccino
- update
---

Here's a quick update on what's new with Cappuccino for the last two weeks.

#### Community

- [Cappuccino in action](http://www.cappuccino-project.org/blog/2014/07/cappuccino-in-action-nuage-networks.html) by Antoine Mercadal has been added to the blog.

#### New features

- `Cucapp` allows you to specify URL parameters between each test (accessible via the global variable `$url_params`).

#### Changes/Fixes

- An `objectController` can now handle several objects bound to itself.

- Delegate methods in a `CPTokenField` rework.

- `CPDateFormatter` now returns by default english format unless other symbols have been explicitly provided or set.

- Scrolling in Firefox is now way faster.

- `CPMenu` updates its view when a binded `CPMenuItem` is notified.

- `CPDatePicker` has now the format Year/Month/Day in a `CPPredicateEditor` by default.

- The edition of a selected text in a `CPTextField` through `Cucapp` works now.

- The XML dump created for `Cucapp` does not include hidden views or unvisible windows anymore.
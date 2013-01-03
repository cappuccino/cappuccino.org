---
title: We're now cappuccino/cappuccino on GitHub
author: Alexander Ljungberg
author_email: aljungberg@slevenbits.com
wordpress_id: 1178
wordpress_url: http://cappuccino.org/discuss/?p=1178
date: '2011-09-01'
tags:
- cappuccino
- 280 north
- github
---


The main Cappuccino repository has been renamed. What used to be: `280north/cappuccino`
is now `cappuccino/cappuccino`. `280north/cappuccino` is a fork of the new main repository, which means old links will continue to work.

You can find the new repository [here](https://github.com/cappuccino/cappuccino).

For most people this will not make much of a difference but if you are building from source, you might want to pull from the new repository instead. The Git URL is then:

    git://github.com/cappuccino/cappuccino.git

If you are running a UNIX like system, you can update your Git clone using a command like this one:

    find . -path "*.git/config" -type f -exec sed -i '' 's/github.com\/280north/github.com\/cappuccino/g' '{}' \;

If you find an old issue link, from a mailing list for instance, you will have to modify it by hand to find its new home. For example:

    https://github.com/280north/cappuccino/issues/10

becomes:

    https://github.com/cappuccino/cappuccino/issues/10

Feel free to help out and update links in the [wiki](https://github.com/cappuccino/cappuccino/wiki).




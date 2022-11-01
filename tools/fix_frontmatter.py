#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import difflib
import sys


def fixup(content):
    """Interpret the blog post markdown given as a string. Fix the frontmatter
    such that:

    - all tags are lowercase
    - if a category is all lowercase, title cap it
    - if the categories field is empty, put in the single category Uncategorized

    Return the new frontmatter with the old remainder of the markdown."""

    frontmatter, remainder = content.split('---', 2)[1:]
    frontmatter = yaml.load(frontmatter, Loader=yaml.Loader)
    frontmatter['tags'] = [tag.lower() for tag in frontmatter['tags']]
    if 'categories' not in frontmatter:
        frontmatter['categories'] = ['Uncategorized']
    else:
        frontmatter['categories'] = [category.title() if category.islower() else category for category in frontmatter['categories']]
    return f"""---
{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---{remainder}"""

EXAMPLE_1 = """---
title: The Cappuccino and Objective-J Build Tools
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 41
wordpress_url: http://cappuccino.org/discuss/?p=41
date: '2008-10-06'
categories:
- Cappuccino
- tutorials
- Tools
- CPCoder Night
tags:
- Cappuccino
- build tool
- Objective-J
---


_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

This article is a high level overview of the current Cappuccino and Objective-J build tools. Subsequent posts will cover each tool in more detail.
"""

EXPECTED_1 = """---
title: The Cappuccino and Objective-J Build Tools
author: Tom Robinson
author_email: tom@280north.com
wordpress_id: 41
wordpress_url: http://cappuccino.org/discuss/?p=41
date: '2008-10-06'
categories:
- Cappuccino
- Tutorials
- Tools
- CPCoder Night
tags:
- cappuccino
- build tool
- objective-j
---


_Note: please check the [tools page](https://github.com/cappuccino/cappuccino/wiki/tools) on the wiki for the latest information on Cappuccino's tools._

This article is a high level overview of the current Cappuccino and Objective-J build tools. Subsequent posts will cover each tool in more detail.
"""


def test_fixup_1():
    fixed_up = fixup(EXAMPLE_1)
    if fixed_up != EXPECTED_1:
        with open('/tmp/a', 'w') as f:
            f.write(EXPECTED_1)
        with open('/tmp/b', 'w') as f:
            f.write(fixed_up)
        print(''.join(difflib.unified_diff(fixed_up.splitlines(), EXPECTED_1.splitlines())))
        raise AssertionError


# test_fixup_1()

if __name__ == '__main__':
    print(fixup(sys.stdin.read()))

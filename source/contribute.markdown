---
title: Contribute
layout: markdown
---

As an open source project, your contributions are important to the
future of Cappuccino. Whether you're looking to write code, add new
documentation, or just report a bug, you'll be helping everyone who uses
Cappuccino in the future.

### Reporting Bugs or Missing Features <a name="bug-reports">&nbsp;</a>

We use the [GitHub issue tracker](http://github.com/cappuccino/cappuccino/issues) to report and
follow bugs in Cappuccino. If you think you've found a problem in
Cappuccino, you can always ask about it on the mailing list or in the
IRC chat room, or you can search GitHub. If you've discovered a new bug,
report it!

These things are likely bugs:

- Code that doesn’t run at all due to JavaScript errors.
- Code that doesn’t behave according to the documentation (Cappuccino docs or Cocoa docs).
- Methods or features that behave differently in Cocoa than in Cappuccino.

#### Before You Report It

If you are sure the problem comes from Cappuccino and not from your
code, we want to know about it. Before writing up a new ticket
in the issue tracker, please consider these guidelines:

-   **Do** [search the issue
    tracker](https://github.com/cappuccino/cappuccino/issues) to see if
    your issue has already been filed. If it has and you have some more
    details to add, add a comment to the existing issue.
-   **Don’t** reopen issues that have been tagged “\#wont-fix”. This
    means that the decision has been made that we can’t or won’t fix
    this particular issue. If you’re not sure why, please ask on the
    [Cappuccino users group](http://groups.google.com/group/objectivej).
-   **Do** search the [Cappuccino users group](http://groups.google.com/group/objectivej) and [Cappuccino developers group](http://groups.google.com/group/objectivej-dev) to
    see if your issue has already been discussed. If it has not and you
    are not sure if what you are seeing is a bug, ask the users group.
-   **Don’t** use the ticket system to ask support questions. Use the
    [Cappuccino users group](http://groups.google.com/group/objectivej),
    or the \#cappuccino IRC channel for that.
-   **Don’t** use the ticket system to make large-scale feature
    requests. Please discuss them on the [Cappuccino developers group](http://groups.google.com/group/objectivej-dev) first.

#### Reporting Guidelines

Once you are ready to file a bug report or feature request, here are some tips:

-   **Don’t** just say “X doesn’t work” or “When I do X, it doesn’t
    work.” Please write a clear, concise description of the problem, and
    a clear set of instructions for replicating the problem. If there
    are error messages involved, please include them exactly as they
    appear.
-   **Do** include your operating system version, Cappuccino version,
    and browser version.
-   **Do** include a link to the source of a minimal example app that
    illustrates the bug.
-   **Don’t** post to one of the groups to announce that you have filed
    a bug report. We are notified as soon as they are filed.

When you have everything ready, go ahead and [open a new ticket](https://github.com/cappuccino/cappuccino/issues/new).

### The Issue Lifecycle

Once the ticket is created, there is a [well-defined lifecycle](/contribute/issue-lifecycle.html) it goes through. We track its progress
through the lifecycle with tags so you know what its status is.

### Getting the Code <a name="get-code">&nbsp;</a>

Cappuccino is hosted on
[GitHub](http://github.com/cappuccino/cappuccino) using the
[Git](http://git-scm.com/) version control system. You can get the code
with the following command:

    git clone git://github.com/cappuccino/cappuccino.git

If you don't have Git installed, don't worry, it's simple. Check out the
[official download page](http://git-scm.com/download), or view the
installation guide on the [Git Wiki](http://git.or.cz/gitwiki/Installation).

You can also download the latest source code as a [zip
file](http://github.com/cappuccino/cappuccino/zipball/master) or
[tarball](http://github.com/cappuccino/cappuccino/tarball/master). These
links go to the top of the tree, but using GitHub, you can find any
specific revision on any branch and download either file.

For help getting set up with the build tools and checking out the source
code, follow [this guide](http://wiki.github.com/cappuccino/cappuccino/getting-and-building-the-source).

### What to Work On

From time to time we might update the [Projects to Work On](https://github.com/cappuccino/cappuccino/wiki/projects-to-work-on) list. If there's nothing you want to work on there, there might be an open [issue](https://github.com/cappuccino/cappuccino/issues) or two.

### Contributing Code

Bug fixes, new features and other patches you write should be submitted as pull requests. Patches should conform to the project's [contribution guidelines](https://github.com/cappuccino/cappuccino/blob/master/CONTRIBUTING.md) as closely as possible.

### Documentation, Wiki & Tutorials

Cappuccino documentation is integrated inline with Cappuccino code. We
use a documentation generating tool to create the [docs on this site](/learn/documentation/). You can run it yourself by running `jake docs` in the Cappuccino project. If you'd like to improve the documentation for a given section of the code, you can get the code as described above and make your changes. When you're ready, go through the normal commit process to have your changes integrated with the project.

Github has an [integrated wiki](http://github.com/cappuccino/cappuccino/wikis) which this project
uses for collaboration. We keep a list of projects we think need the most attention and are worth working on, along with lots of other useful information for developers. This site also has a [tutorial section](/learn/) where we collect and link to tutorials. If you've written a tutorial, you can submit a pull request [this site](https://github.com/cappuccino/cappuccino.org) for potential inclusion.

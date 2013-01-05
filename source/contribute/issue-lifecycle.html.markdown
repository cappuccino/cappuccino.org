---
title: Issue Lifecycle
layout: markdown
---

## The Exciting Life of an Issue

Issues are at the heart of the Cappuccino project. They tell us where we
are in terms of what needs to be fixed, and where we want to go in terms
of new features to be added. From the point when an issue is created to
the point where it is closed, there is a well-defined path it follows.

A picture is worth a thousand words, so here is a graphical
representation of the issue lifecycle:

[![Issue Lifecycle](/img/issue-lifecycle.png "issue-lifecycle")](/img/issue-lifecycle.png)

## Issue States, Phases, Tags and Categories

At the highest level, an issue is either **Open** or **Closed**. At the
beginning of an issue’s lifecycle, a newly created issue is Open, and it
remains Open until it enters one of the “Closed” states pictured above,
which is the end of its lifecycle.

Within the high level Open and Closed states, an issue is either in the
**Review** phase or in the **Resolution** phase. Within a phase, an
issue may have one or more tags that identify where it is within the
lifecycle and what actions are necessary to advance to the next step.
Issue lifecycle tags begin with “\#”, such as “\#new” and “\#accepted”.
Issues may also have labels that do not begin with “\#”, which are
**category** labels, such as “bug” and “feature”.

## The Lifecycle in Detail

Since a picture is worth a thousand words, here is the thousand-word
description of the issue lifecycle.

### New issue

When you create a new issue, its state is Open and it is in the Review
phase. An automated script gives it the **\#new** tag, adds it to the
“Someday” milestone, adds the **\#needs-patch** tag if it is not a pull
request, and the core team is notified.

### Initial triage

A designated Reviewer or core team member reviews the issue and the
following actions are taken:

-   Determine if the issue is a bug report or feature request. A label
    is added to the issue (**bug** or **feature**) to indicate which.
-   The component of Cappuccino affected by the issue is marked with the
    label **AppKit**, **Foundation**, **Objective-J**, **documentation**
    or **tools**. If bindings are involved, the **bindings** label is
    added.
-   If the issue affects certain browsers, the relevant labels
    (**WebKit**, **IE**, etc.) are added to the issue.
-   If the description of the problem/feature is not clear, the issue is
    tagged **\#needs-info** and the necessary information is solicited
    through the issue comments.
-   If the issue is a bug report and there is no sample app or code that
    reduces the bug to a minimal set of circumstances, it is labeled
    **\#needs-reduction**.
-   If the issue is a bug report and it is unclear if the bug still
    exists, it is labeled **\#needs-confirmation**.

At this point, there are a couple of paths the issue might take.

-   If the issue is clearly not something that will ever be fixed or
    implemented, the issue is labeled **\#wont-fix** and is closed.
-   If a bug report cannot be reproduced, it is labeled
    **\#works-for-me** and is closed.
-   If an issue is a duplicate of another issue, a link to the duplicate
    issue is put in the comments, it is labeled **\#duplicate**, and is
    closed.
-   If the issue is a very low priority and might be dealt with in the
    distant future, it is added to the “Someday” milestone and is left
    open.
-   If none of the above apply and the issue is obviously something that
    needs fixing or implementing, it is labeled **\#accepted** and
    enters the Resolution phase.
-   If it is not clear whether or how an issue might be resolved, the
    reviewer submits the issue to peer review by labeling it
    **\#needs-review**.

### Peer review

Sometimes accepting a bug report or feature request requires an
architectural or implementation design decision. For architectural
decisions, the question is whether the issue fits in with the overall
design of the Cappuccino frameworks. For implementation decisions, the
question is whether it is technically feasible to implement the fix, and
if so how to do so.

To make these decisions, we bring the design decisions up for a vote,
perhaps with some preliminary discussion. For more information on the
voting process, see [How We Make Decisions](#how-we-make-decisions).

If the vote indicates an issue will be accepted, it is labeled
**\#accepted** and enters the Resolution phase. Otherwise it is labeled
**\#wont-fix** and closed, or it is added to the “Someday” milestone and
left open.

### Resolution phase

Once an issue has been accepted, now it has to be resolved by fixing the
bug or implementing the feature. This is where we really rely on the
community to help with the coding!

Once a patch is submitted, either as a gist or as a pull request, then
the code has to be reviewed by a designated Reviewer or core team
member.

-   If the code needs better documentation, it is labeled
    **\#needs-docs**.
-   If the code needs a unit test or test app, it is labeled
    **\#needs-test**.
-   If the code has problems with formatting or fails a capp\_lint
    check, has bugs, or has non-optimal logic or algorithms, it is
    labeled **\#needs-improvement**.

Once the code is free of any **\#needs-** tags, it is labeled
**\#ready-to-commit**. As the final step, a core team member commits the
code to the master branch, labels the issue **\#fixed**, and closes the
issue. Thus ends the lifecycle of an issue.

### “Bumping” An Issue

If you see an issue that you especially want to have fixed or
implemented, you can vote “bump” it by adding a comment that consists of
nothing more than “+1”. This will get picked up automatically and the
title of the issue will be updated to show the latest bump count. In
addition, the core team will be notified so we have an idea which issues
are a priority for the community.

## How We Make Decisions <a name="#how-we-make-decisions">&nbsp;</a>

We strive to be as transparent and democratic as possible, so when a new
feature or design decision will have a significant impact on the
community, we may ask for an informal vote on the objectivej or
objectivej-dev mailing list. The subject of the vote will be prefixed by
“[VOTE] ”.

In these votes we follow the voting style commonly used by open source
projects, where votes are given as +1, +0, -0, or -1. Roughly
translated, these votes mean:

-   **+1**: I love the idea and I’m strongly committed to it.
-   **+0**: Sounds OK to me.
-   **-0**: I’m not thrilled, but I won’t stand in the way.
-   **-1**: I strongly disagree and would be very unhappy to see the
    idea turn into reality.

Although these votes are informal, they will be taken very seriously.
After a suitable voting period (usually a week or two), if an obvious
consensus emerges we will follow the votes.

However, consensus is not always possible. If consensus cannot be
reached, or if the discussion fizzles out without arriving at a concrete
decision, we use a more formal process.

Any core developer may call for a formal vote using the same voting
mechanism outlined above. The subject of these formal votes will be
prefixed with “[CORE-VOTE] ”. These formal votes differ from informal
votes in that although they are conducted in public, only votes by the
core team count. A proposition will be considered carried by the core
team if:

-   There are two +1 votes from members of the core team.
-   There are no -1 votes from members of the core team.

When calling for a vote, the caller should specify a deadline by which
votes must be received, with one week being the minimum amount of time.

Since this process allows any core developer to veto a proposal, any -1
votes must be accompanied by a thorough explanation of what it would
take to convert the -1 into at least a +0.

Whenever possible, these formal votes will be announced and held in
public on the objectivej or objectivej-dev mailing list. However, very
sensitive or contentious issues — including votes on new core developers
— may be held in private, using the same rules.

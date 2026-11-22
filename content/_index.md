---
title: "Cappuccino, for serious Web Apps"
description: "The application architecture the web was built on, complete in the browser: document models, undo, drag-and-drop, command dispatch, all in the box."
---

> The technology used to create the WWW,\
> brought home to applications running on it.

Serious web application development demands Cappuccino: a complete, open-source port of AppKit and Foundation — the architecture under which the World Wide Web itself was first built — delivering the application fundamentals the platform still ships without, ready for everyone from a lone developer to the largest team.

The web development ecosystem is a wilderness of shifting sands: tooling that requires manual assembly, interoperates poorly, and loses support as quickly as it appears. The most successful commercial enterprises in human history require industrial-scale resources to bring real application functionality to the web, and even they ship without the fundamentals. Gmail has no application-wide undo, to this day. In Cappuccino, an undo stack is not a research program; it is table stakes.

In late 1990, Tim Berners-Lee built WorldWideWeb — the first web browser and editor, together with the first web server — alone, in a handful of months, on a NeXT workstation. He chose NeXTSTEP and Objective-C because they alone gave a lone developer the leverage to build a graphical hypertext client, a WYSIWYG editor, and a companion server, sui generis. Nearly four decades later, that foundation is now Apple's Cocoa: AppKit and UIKit, running on 2.5 billion active devices. It is the most proven application architecture in existence, and it remains state of the art.

Cappuccino faithfully ports that architecture to the browser through Objective-J — a transliteration of Objective-C onto JavaScript — carried as far as the browser platform allows. It provides the complete foundation the platform lacks: infrastructure-grade tooling, active styling bundles, document models, undo/redo stacks, responder chains, drag-and-drop protocols, window management, and unified event routing — all in a single cohesive model. The architecture was mature before the first line of Objective-J was written in late 2007; three developers proved it pre-release with 280 Slides, a desktop-class presentation application. Nearly two decades on, AppKit API coverage has grown almost complete.

The first web client and server were born inside this model. Cappuccino brings web application development full circle — home to the nursery — and leaves the ecosystem's headaches behind. It was state of the art at inception, nearly four decades ago. It remains so today.

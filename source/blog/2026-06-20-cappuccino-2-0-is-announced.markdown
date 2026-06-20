---
title: Path to Cappuccino 2.0.0: Native Toolchain and Framework Milestones
author: David and Daniel
date: '2024-06-14'
tags:
cappuccino
- release
- update
- compiler
- toolchain
- framework
categories:
- Uncategorized
---

#### Details

Hello everyone,

We have significant news regarding the progress toward Cappuccino 2.0. This update represents a broader shift in the project than we have announced in some time, driven by parallel, complementary efforts over the past several months. 

We have focused our work on two distinct fronts: Daniel has driven updates to the core framework, while David has focused on rebuilding the infrastructure-grade toolchain and compiler.

### The Framework & Component Highlights

Daniel has completed a resolution-independent Aristo3 theme, alongside hundreds of improvements to the core codebase. This is sustained, high-quality work that has substantially advanced the framework. 

Rather than just incremental fixes, this iteration introduces major new architectural components and optimizations since the 1.0 baseline:

*   **New Layout & Controller Architecture**: 
    *   `CPStackView` has been introduced to make fluid, linear interface layouts straightforward to manage.
    *   `CPSplitViewController` and `CPSplitViewItem` bring modern split-pane layouts in line with macOS.
    *   `CPTreeController` and `CPMapTable` have been implemented to simplify tree-structured data binding and key-value management.
*   **Rich Text Evolution in `CPTextView`**: 
    *   Native table rendering with round-trip RTF and Markdown (`CPMarkdownParser`) parser support.
    *   Support for baseline offsets, superscript, and subscript text formatting.
    *   Addition of native context menus and reliable clipboard copy/paste mechanisms.
    *   We resolved a critical $O(N^2)$ layout bottleneck in `CPLayoutManager` when rendering large text documents. Text-heavy applications should now load and scroll noticeably faster.
*   **Modern Core Animation (CA) Support**: 
    *   `CAAnimationGroup` and timer-based animations have been integrated directly into `CALayer`.
    *   Visual components like `CPOutlineView` now utilize these animations for smooth disclosure triangle transitions and row expansion.
*   **Ecosystem and Theme Refinements**:
    *   **SVG-Native UI**: Legacy bitmap-based icons inside the Aristo3 theme have been replaced with scalable vector graphics (SVG) for crisp rendering at any zoom level.
    *   **Dark Mode Foundations**: Systematic cleanup of background and control colors has been conducted to allow better styling under system Dark Mode settings.
    *   **Mobile & Touch Optimization**: Native momentum-scrolling support has been added to touch gestures alongside dedicated iPad soft-keyboard and double-tap emulation refinements.

### An Infrastructure-Grade Toolchain

In parallel, David has built a native compiler and toolchain from the ground up. By moving away from dependencies on the Node, npm, or React ecosystems for the build pipeline, we aim to provide a more stable and self-contained environment. 

The `NibApplication` template now builds and runs under this new pipeline. This native compiler is designed for high performance, with the goal of enabling incremental builds fast enough to trigger on every keystroke, independent of development hardware.

#### Correctness Over Tolerance

The legacy toolchain inherited JavaScript's permissive, lazy-loading behaviors, which could occasionally mask underlying architectural issues. The new compiler enforces strict build-time determinism. As a result, it will surface import cycles that the older toolchain silently tolerated. 

These cycles represent real architectural issues in projects. The compiler is designed to flag these clearly and provide guidance on resolving them, typically through the use of forward declarations. 

#### Single Binary Distribution

To simplify development setup, the toolchain is distributed as a single binary. There is no longer a dependency on Node, npm, or external package managers to compile your application. You can simply download the binary for your platform, place it in your system's PATH, and begin building.

### Ongoing Work: nib2cib

Deep work on the `nib2cib` tool has surfaced legacy environmental assumptions carried over from early NeXT and Apple implementations. Rather than applying hasty patches, we are addressing these assumptions deliberately to ensure long-term stability. A technical discussion on this topic will be opened in the repositories shortly to gather community input.

### Next Steps and Availability

The main repositories are now public, and we encourage you to explore the new toolchain repository here:

[Cappuccino Toolchain on GitHub](https://github.com/enquora-net/cappuccino-toolchain)

The toolchain serves as the foundation that makes the updated framework features accessible and deployable. Consolidation, testing, and hardening of these tools will continue through July. 

Please watch the repositories and enable notifications to stay updated on progress. We will be monitoring the channels and are available to field questions and discuss these updates over the coming week.

Thank you for your continued support as we work toward the 2.0 release.

— The Cappuccino Project,  
David and Daniel

***

[Explore the Toolchain Repository](https://github.com/enquora-net/cappuccino-toolchain) | [Join the Discussion on Gitter](https://gitter.im/cappuccino/cappuccino)
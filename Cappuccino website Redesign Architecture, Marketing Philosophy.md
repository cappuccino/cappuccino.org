# Cappuccino.org Redesign: Architecture, Strategy, and Context

## 1. Strategic Posture & Rhetorical Thesis
* **Objective:** Modernize `cappuccino.org` into a narrative-forward, long-form essay that positions **Cappuccino 2** as the unbroken inheritance of Turing Award–class systems architecture (Smalltalk $\rightarrow$ NeXTSTEP $\rightarrow$ OpenStep $\rightarrow$ Cappuccino $\rightarrow$ Cappuccino 2).
* **Target Audience:** High-intent, senior technical readers willing to engage with architectural trade-offs. Casual scanners self-select out by design.
* **Commanding the High Ground (Implicit Critique):**
  * Never mention, name, or explicitly critique competing frameworks. Doing so accepts their premises and puts the narrative on the defensive.
  * Attack **churn** and **fragility**—the primary structural weaknesses of popular web stacks—indirectly by presenting multi-decade API longevity, deterministic single-binary builds, zero-dependency toolchains, and formal object models as quiet, unremarkable engineering baselines.
* **Launch Vehicle:** The site redesign serves directly as the release announcement for **Cappuccino 2**, framing its modern infrastructure-grade toolchain, hardened frameworks, and resolution-independent theming as the culmination of a four-decade lineage.

---

## 2. Information Architecture (Progressive Disclosure)
* **Landing Page (Pure Narrative):** A single, uninterrupted architectural argument. Legacy feature lists (groundbreaking 15–20 years ago, irrelevant today) are completely removed from the home page.
* **Off-Page Deep Dives:** Every milestone node along the narrative links to a dedicated sub-page for extensive technical exposition. Concrete specifications, architecture notes, and feature breakdowns live on their own URLs, keeping the landing page essay unencumbered.

---

## 3. Visual & Typographic Baseline
* **Layout Philosophy:** Borderless, whitespace-driven layout. No cards, no boxes, and no continuous left borders (which look crude and compete with the ragged-left vertical rhythm of text).
* **Alignment & Measure:** Left-aligned prose (`65ch` maximum measure) to prevent typographic "rivers" and maximize readability.
* **Typography (`Nunito` Variable):**
  * **Base Font Size:** `1.125rem` (`18px`)
  * **Line Height:** `1.78`
  * **Letter Spacing:** `0.005em`
  * **Word Spacing:** `0.04em`
  * **Variable Weight (`wght` axis):** Pinned to `425` (within the `200`–`900` range) for optimal body density.

---

## 4. The Vertical Timeline Rail (HTML/CSS Architecture)
* **Concept:** Structurally an editorial bulleted list where bullets are expanded into milestone nodes, connected by a continuous vertical thread, and paired with full narrative paragraphs.
* **Dual Purpose of Nodes:**
  1. **Visual Pacing & Anchoring:** Provides non-competing margin anchors that visually prove four decades of uninterrupted architectural continuity without boxing the prose.
  2. **Interactive Tap Targets:** Large circular or lozenge-shaped callouts (`>= 44px` / `2.75rem`) act as smooth-scroll anchor links (`href="#milestone-id"`) matching the automated scrolling behavior of the legacy site.
* **Terminal Node:** Concludes with **Cappuccino 2** (*modern infrastructure-grade toolchain, hardened and expanded frameworks implementation, and resolution-independent theming*).
* **Pure HTML & CSS Implementation (No JS or SVG required):**
  * **Semantic Markup:** An ordered list (`<ol>`) inside a two-column CSS Grid (fixed-width rail track alongside the `65ch` prose column).
  * **Continuous Track:** Rendered via `::before` pseudo-elements connecting the milestone markers cleanly down the rail axis.
  * **Smooth Scrolling:** Native `scroll-behavior: smooth` on `html`, paired with `scroll-margin-top` on target sections so headings clear the fixed masthead.
  * **Progressive Scroll Fill:** Modern CSS scroll-driven animations (`animation-timeline: scroll()`) animate a secondary fill layer along the rail in sync with reading progress, degrading automatically to a static graphic when `prefers-reduced-motion: reduce` is active.

---


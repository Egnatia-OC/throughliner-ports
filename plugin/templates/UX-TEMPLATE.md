# UX.md — [Project Name] User Experience

This document describes every functionality and UI element as the user experiences it, and why the user needs it. Every entry must correspond to something that actually exists in the current build. If an entry cannot be traced to an existing feature, it is not a current user experience — it is a plan, and it belongs in `BACKLOG.md`.

`UX.md` only describes what has been decided. Open questions and undecided details do NOT live here as placeholders, and do NOT live here as sentences that gesture at the doc's own undecidedness (e.g. "currently undecided", "pending decision"). Open questions live in `BACKLOG.md` as planning batches.

## Project context

[One paragraph: what the app is, what it does, and what makes it distinct from existing apps in the space. Filled in once the project's basic identity is settled. Delete this instruction when filled in.]

## UX principles for [Project Name]

These inform every design decision. Entries below should serve one or more of these principles. If a proposed change conflicts with a principle, flag the conflict before building.

1. **[Principle name].** [One-line claim. Then a few sentences explaining why this principle matters for this project's users — the user context, the constraint, or the failure mode it protects against.]

2. **[Principle name].** [As above.]

3. **[Principle name].** [As above.]

[Add 3–6 principles total. Delete this instruction when filled in.]

## Functionalities

### [Feature name]

[One paragraph describing how the user experiences this feature: what they see, what they tap, what happens.]

The user needs this because [rationale — tie back to a UX principle or to the user context].

### [Feature name]

[As above.]

<!--
Optional patterns for entries (full spec in DOC-STRUCTURE.md → UX.md structure):

- **Risk accepted:** line at the end of an entry — for known downsides the user
  has explicitly weighed and chosen. Keeps the trade-off visible.

- *(see Other Entry)* italics — cross-references where features compose. Do
  not duplicate content across entries.

- **Parent → Sub-area** entry names — for sub-functionalities with distinct
  user-facing rationale. Use sparingly; if a sub-control's "user needs this
  because..." line is the same as the parent's, fold it in instead.
-->

## Fold-ins pending

Proposed entries or updates that Claude has queued for this doc. Each block describes the proposed change, its origin, and whether it replaces an existing section or adds a new one. Fold these into the main body during your next planning session, then delete the block. Section starts empty for new projects.

For the canonical block format, see `DOC-STRUCTURE.md` → *Fold-ins pending sections*.

---
*No-code method — Version 45.*

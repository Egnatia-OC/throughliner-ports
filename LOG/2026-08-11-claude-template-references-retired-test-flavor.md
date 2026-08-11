# [HASH] — The shipped CLAUDE.md template stops inviting users to prepare for a retired feature [claude-template-references-retired-test-flavor]

Audit finding, approved by the user. `CLAUDE-TEMPLATE.md` invited the user to add test procedures that "Claude will follow during test entries and /done verification". The test flavor is retired; the method now routes a check Claude can run into building, and a check only the user can run into a `[user]` item.

**Why staleness in a template is worse than staleness in a doc.** This text is copied into every new project at /setup, so the wrong claim is *reproduced* rather than merely sitting somewhere. The gate's staleness test applies directly: a confidently wrong rule is worse than a missing one, and this one invited the user to prepare for a mechanism that no longer exists.

The replacement describes the live routing in the template's own register — plain words, no method vocabulary, since this is text a brand-new non-coder reads before they know any of it.

**Files touched:** `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`
**Routed to Captures:** none from this item

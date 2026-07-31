# 3565ea1 — Restored red flags as tagged work lines: plugin-behaviour.md rules + four-state model, plan.md risk routing, FAQ entry

The queue redesign had stripped the structured red-flags mechanism — the dedicated `## Red flags` section and the open/resolved/accepted states — leaving only the plain-English screening in SPEC. This batch restores the structure, recast for the two-section work-line model: a red flag is now an ordinary work line carrying a `Red flag · State: <open|resolved|accepted>` marker, not a pinned section. The rationale, carried from the 2026-07-04 /plan session and folded inline: a dedicated section would read as a claim to manage every risk that exists — comprehensive data/security management the tool can't back up — when it only ever holds the risks Claude identified; a tagged work line surfaces and addresses a genuine risk without that over-claim. SPEC's risk principle (line 46) survived intact and stays honest, so SPEC needed no edit — the spec-sync gate confirmed no drift.

Four changes across three files. plugin-behaviour.md gained two sections after Captures: "Work-line states — the canonical four" (Unprocessed / Processed-above-the-cleared-line / Processed-below-the-line / Deleted, with the cleared-to-run line named as the replacement for parking and order as the replacement for dependencies — added to stop sessions mischaracterising the model), and "Red flags" + "Flag states" (the marker format, the three states, and that the future unattended mode's gate reads them). plan.md restored risk routing: a bullet in Capture and processing discipline, and a "keep a surfaced risk as a red-flag work line" route in Step 2's execute step, with the open→resolved / open→accepted transitions and consent recorded in the LOG. faq-template.md plus its index gained a plain-English "what's a red flag" entry covering the three states and why it's a tag, not a section.

This is the rulebook layer; [hooks-work-line-recut] (session-start scan of the marker) and [done-work-line-recut] (consent recording) implement it, and both depend on this batch's red-flag line format — defined here once, no double-build.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added Work-line states + Red flags/Flag states sections
- plugin/si-plugin/docs/plan.md: added risk-routing bullet + Step 2 red-flag keep route
- plugin/si-plugin/templates/faq-template.md: added "what's a red flag" entry
- plugin/si-plugin/templates/faq-index-template.md: added its index line

**Routed to Captures:** none

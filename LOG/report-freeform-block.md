# 053c608 — plugin-behaviour.md: plugin-feedback report now drafted as one free-form scrubbed block, not labelled fields

The consumer feedback channel had Claude draft the scrubbed report broken into labelled fields (method+version, skill/step, question or gap, context, steps to reproduce). Those fields don't correspond to whatever input the flintcraft.tech/report page presents, so a user pasting the draft had to reconcile Claude's structure against a different on-page form.

Decision (2026-07-27): drop the labelled-field structure — Claude drafts ONE free-form scrubbed block that drops cleanly into a single submission box, whatever the page provides. This dissolves the mismatch (nothing to reconcile) and pairs with [report-url-404], whose page requirement collapses to a single text box. The block still carries what a useful report needs — what the plugin did vs expected, which skill and step, the method version, generic repro steps — as prose in one block. Scrubbing is unchanged and non-negotiable: no app names, file contents, secrets, or QUEUE/SPEC content; the user reviews and pastes it themselves; Claude never auto-submits.

SPEC.md and the FAQ needed no change — neither described the report's field structure (both already describe it as prose), so there was nothing to sync.

**Files touched:**
- plugin-behaviour.md (Consumer feedback channel — "One free-form block, not labelled fields")

**Routed to Captures:** none

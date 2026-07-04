# [HASH] — Recut the /done family to the two-section work-line model

The /done family still spoke the old model — routing by Build/Test/Audit/Freeform subheadings, writing can't-run checks to a `## Deferred tests` section, cross-checking shipped slugs against `## Batches`, and naming LOG files after a "batch slug." This recut moves it onto the two-section work-line model that plan.md, plugin-behaviour.md, and the /next family already use.

done.md now routes by the run's work-line flavor, not subheadings, and drops the test route entirely — the test flavor is retired. A check Claude can run is part of building; a check only the user can run is a `[user]` line /next hands over, so nothing deferred-test-shaped reaches /done. The `## Deferred tests` section is replaced by a short note: a can't-run-now check becomes a `[user]` work line appended to Unprocessed. LOG files are named after the work-line slug. The shipped-slug cross-check reads Processed. The Accepted red flags section is reconciled — an accepted flag is a red-flag work line at `State: accepted`, its consent still recorded in the LOG. done-build/audit/freeform.md were recut to work-line vocabulary and self-scoping, writing one LOG entry per built line. done-test.md was deleted.

Two fixes went beyond the headline scope, both to avoid shipping a doc that points at already-removed machinery. The staleness sweeps in done-build/audit/freeform referenced plugin-behaviour.md's Staleness watch, Unpark watch, and parked items — all gone — so they were reframed to a light check of remaining Unprocessed/Processed lines with a fate-vs-mechanical split. And done-plan.md was missing the Accepted-red-flags pointer a /plan needs when it accepts a planning-stage risk, and referenced an overlap scan the /next recut removed; both fixed.

A third FAQ entry made stale by this work — "how do I check an update works" — was left alone and filed as [faq-update-check-test-concept], because how the work-line model handles a post-reinstall check is an open question tied to [test-concept-redesign], not a quick swap.

**Files touched:**
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/done-build.md
- plugin/si-plugin/docs/done-audit.md
- plugin/si-plugin/docs/done-freeform.md
- plugin/si-plugin/docs/done-test.md (deleted)
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md
- QUEUE.md (capture + deferred-test line + batch removal)

**Routed to Captures:** [faq-update-check-test-concept]

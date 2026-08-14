# 78fa417 — Two rationale passages cut from done-build.md

"Why the sync gate left this close" explained the removal of the build close's SPEC sync — that a close-time sync on a document the build never read can only record what the build did, so it became a place to justify whatever the run had done. The instruction it sits under already states plainly that the build close checks its work against SPEC and does not sync SPEC to match, with a table covering agreement, contradiction and new product truth.

The second was the sentence refusing a single combined LOG entry per run on retrievability grounds. The rule above it — one entry per built item, unconditional, because a work item's queue text is consumed when it builds and the entry becomes the only surviving record — is complete without the refusal of the alternative.

The refused alternative is kept here so it is not re-proposed blind: a combined entry per run is cheaper, and it was rejected because the retrieve path is "search the index, then open the matched entry", so combining trades away exactly the per-slug retrievability the entries exist for.

**Files touched:** `plugin/throughliner/docs-b/done-build.md` (−12 lines).
**Routed to Captures:** none

# 455082b — Made /plan verify an item's load-bearing factual claims at the moment it's processed

A capture is written when its claims are true and then sits while the project moves under it. The below-line revisit re-checks lift-conditions every session, but only for items already in Processed — a claim stated as prose inside an Unprocessed capture is re-read by nothing.

The check is not "verify the blocker." That was the original framing and it was too narrow: of the three catches behind this item, only one was a stated blocker. The other two were plain factual premises — what the docs say, and what a number is — and both reversed their item's shape when checked. So the rule is **verify the item's load-bearing factual claims before discussing it on its own terms**, with a stated blocker being one kind of such claim rather than the category.

Load-bearing is defined by a test, so the check can't sprawl into a fact-audit of every sentence: would the item change shape, priority, or readiness if the claim were false? Background colour fails that test; an assertion about what ships, what a measurement is, or what has landed passes it.

It stays at the moment of processing, where all three catches actually happened. One item, one check, only when the item makes such a claim — so cost scales with work being done rather than with queue size. A staleness sweep across all of Unprocessed at the close was rejected and recorded as rejected: with around thirty items it is the diff-everything-every-session cost the method fights, it would near-always find nothing, and a check that near-always no-ops is one that gets skipped.

The reason it needed writing down at all is that every catch so far happened because Claude happened to look, not because any step asked — which is precisely what stops happening in the fresh short session the method designs for.

This run supplied a fourth instance immediately, which is the strongest argument the rule could have had. [spec-diverges-from-shipped-docsets], built in this same session, asserted three SPEC divergences; two were false, both were load-bearing on the item's shape, and both were caught only because the build checked before editing.

**Files touched:** `docs-b/plan.md`
**Routed to Captures:** none from this item

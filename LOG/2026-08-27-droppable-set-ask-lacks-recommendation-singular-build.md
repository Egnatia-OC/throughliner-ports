# 32675a3 — The droppable-set ask states its recommendation at any batch size

The plural specimen carried its recommendation implicitly — "Drop both, or name
any to keep?" reads as a recommendation because of the shape of the question. At a
batch of one that shape collapses, and the natural phrasing becomes "drop this, or
keep it?", which hands the user a balanced choice where the pass has in fact
reached a view.

So the step now requires the recommendation stated explicitly, with keeping
offered as the exception, whatever the batch size — and a singular specimen sits
beside the plural one showing it: *"One looks droppable — **[old-slug]**: its
premise is gone. My recommendation is to drop it — keep it instead?"*

The plural specimen stays, and the step's mechanics are unchanged. The pass still
only ever deletes, and only fires when something is obviously droppable.

**Widening the one-at-a-time delete branch's rule to cover this was refused on the
item**: the fix belongs at the step whose specimen breaks, not at a second site
that would then need keeping in step with it.

**Files touched:** `plugin/throughliner/docs/plan.md` — beat 1 of the session
opening.

**Routed to Captures:** none.

Rule gate: run — amendment to the droppable-set step in plan.md, parent named; no freestanding rule, nothing evicted beyond the specimen wording it rewords.

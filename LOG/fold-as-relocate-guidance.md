# 53e3a8e — plan.md: relocate-before-removing clause added to /plan's delete sub-step

Resolves Half B of the two-section reconciliation. The decision was **not** to add a named third disposition to /plan's keep/delete routing — folding stays a judgment call, not a new state. A "fold" route had been drafted once before and reverted, and the anti-proliferation origin intent argues against new routing machinery. But the behaviour still needed naming so it can't be lost: routing a fold through a plain "delete" risks dropping content the user wanted kept, because delete's meaning is "not worth doing." So a short clause was added under plan.md's Step 2 delete sub-step — when a capture's content belongs in SPEC, LOG, or another work item, /plan relocates that content first (editing the target with the user's approval) and only then removes the standalone item. Framed explicitly as a judgment call, not a new disposition: the item is still deleted, just after its worth-keeping content has been carried where it belongs. Scope: plan.md only.

**Files touched:**
- plugin/si-plugin/docs/plan.md

**Routed to Captures:** none

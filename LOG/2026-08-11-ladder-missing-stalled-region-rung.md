# 7c9922a — The processing ladder gains a rung for work that would unstick a stalled cleared region [ladder-missing-stalled-region-rung]

Mixed authorship: the widening is the user's — their words were that the ladder should be widened to include these factors — and so is the placement decision. The narrowing to one factor, the argument for it, and the concern recorded against the placement are Claude's.

**Why it is not ordinary unblock-potential**, which is the whole reason it sits above that rung rather than inside it. Unblock-potential ranks items by how much other work they release. A stalled cleared region is a different quantity: until it is settled *no* build happens, so the cost of leaving it is a stop to everything rather than a delay to something. That is rung 1's argument for an uncleared red flag — a non-throughput concern outranking throughput.

**The precedent that admits it, and the alternative it defeats.** The cheaper answer is that surfacing the stall at session start is enough and no rung is needed. That fails on the ladder's own contents: a red flag is *also* surfaced at session start by the hook, and it still has rung 1. The method already does both for one condition, so a stall having only the surfacing half would be the inconsistency, not the saving.

**Placement was the user's call against Claude's recommendation, and the risk they accepted has now lapsed.** Claude recommended holding this below the line blocked by [nothing-audits-the-cleared-region], on the ground that a rung keyed to a condition nothing detects would ship inert. The user chose to ship it alongside the detector instead, and the stated condition for that being safe was build order — the detector first, in the same run. Both shipped in this run, in that order, so the risk of an inert rung did not materialise.

**Claude's disagreement on the second factor, recorded because it is why this covers one and not two.** The other factor raised was end-preferred placement of `[user]` and `[audit]` lines. It does not belong in a processing-order ladder: it is a placement rule already living in `done-plan.md`, and restating it here would put one rule in two documents that drift apart. What was actually wrong with it was that nothing re-applied it between closes, which is [lift-step-has-no-placement-rule] — also built this run.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none from this item

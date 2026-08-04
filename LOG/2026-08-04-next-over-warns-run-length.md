# [HASH] — Stated the no-unprompted-context-sizing rule at /next's run presentation, where the impulse fires

The capture reported that /next always warns there are too many items, the user tells it to run half, checks context and finds it around 10%, shows that, and /next finishes the rest — having never once run out of context on a run. The cost was never the warning; it was the negotiation, a round spent every run re-litigating how much fits against a risk that has not materialised.

The capture assumed a rule telling /next to warn. There isn't one, and the shipped rules say the opposite — `docs-b/next-build.md` ("you only learn a session is wearing thin when the user says so"), `docs-b/plugin-behaviour.md` ("the trigger is always the user's report"), and `docs/plugin-behaviour.md` harder still ("never Claude noticing on its own"). `docs-b/next.md` Step 1.3 carried no size language at all. So this was Claude violating an existing rule, not following a bad one, which changed the fix from softening the warning to getting the existing rule in front of the session at the moment it's needed.

Two causes compounded. Delivery: the strongest statement lives in `plugin-behaviour.md`, which the payload fix in this same run establishes was truncated out of every session — so under the pre-rezip host it certainly never arrived. Placement: both statements sit in context-management sections framed around what to do *when the user reports a squeeze*, handling the response rather than the impulse, so a session at the run presentation had a general disposition toward caution with nothing nearby contradicting it.

The clause points at the canonical rule rather than restating its reasoning, and it names the cost to the user plainly, because a rule that only forbids reads as arbitrary.

It also covers the second observed form deliberately: caution expressed as *process* — proposing pause points or staged markers for a long run — which is the same warning wearing different clothes and would slip past a narrowly-read version.

Evidence provenance is worth keeping: every observed instance predates the 2026-08-04 rezip, so there is currently no evidence about the current host. A recurrence after this ships is new evidence rather than confirmation, and would mean the diagnosis is wrong and the item reopens on different ground.

**Files touched:** `docs-b/next.md`
**Routed to Captures:** none from this item

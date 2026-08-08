# [HASH] — resources/compression-pass-plan.md written: the first standing procedure in this project whose output is shorter documents rather than findings

The capture that produced this came from a confusion that was itself the evidence.
Asked what the differential audit had yielded, the user described what they had
originally wanted — *"something that would audit the whole docset and help us find
all the bloat and shrink it"* — and diagnosed the condition underneath: *"the docs
just keep growing because instead of actually editing the method, Claude is just
adding and adding and adding."*

**The confusion is caused by the artifacts, not by misremembering.** Two different
jobs share the word "audit" and neither one shrinks anything. The consistency-audit
plan carries both its modes, and both ask *do the documents agree with each other
and with the code*. Neither asks *is this document longer than it needs to be*. The
full run of 2026-08-07 is even filed as a pre-compression audit, and the plan's own
text names its full mode as reserved for "before a compression pass" — so the audit
that existed was the safety check you run *before* compressing, and the compression
it was named for had no plan, no queue item, and no phase in the cycle.

**The plan opens by naming that distinction**, because it is the thing most likely
to be lost: a compression pass that files findings has not compressed anything.
Findings are the audit's output; shorter documents are this one's.

**Four things it states, settled at processing so the build was authoring rather
than design.**

1. **What counts as bloat, in concrete forms** rather than as a judgment about length: one rule restated at three sites where one is canonical and the others are drift; an incident recounted at length whose lesson has since become a one-line rule; a rule superseded but never deleted; duplicate worked examples making one point. And explicitly what is **not** bloat — the why-clause that makes a rule followed. That is the corpus's core design decision, and a pass that treats it as fat produces rules that stop being followed.
2. **How a cut is verified safe:** the full-corpus consistency audit as a stated precondition, then a per-cut grep of the rule's other statement sites before removing anything — the ripple discipline CLAUDE.md already requires at authoring time, applied in reverse. A third step was added at authoring: name what survives and where, since a cut with no named survivor is a deletion, which is a different decision.
3. **It edits; it does not report.**
4. **Where it fires:** its own phase, after a full-corpus audit, never on the same branch as the audit preceding it — otherwise the pass is editing text the audit's repairs are also editing.

**The growth is structural rather than a lapse of discipline, which is why a rule
would not have fixed it.** Every rule in this corpus carries its evidence, its
rejected alternatives and its originating incident, deliberately. But nothing
anywhere asks whether a rule's paragraph still needs to be that long *now*, after
the incident has receded and three later rules have restated half of it. So when
something goes wrong the only sanctioned move is to add another paragraph. Measured
rather than asserted: `docs-b/plugin-behaviour.md` is roughly twice the next largest
procedure doc and is loaded in every session whatever the session is doing.

**The one precedent argues the pass is achievable rather than aspirational.**
Docset B was authored by subtraction from docset A, and the subtraction was measured
at the time. A one-off authoring event driven by a model change, not a repeatable
pass — but it establishes that this corpus survives being cut substantially.

**The honest limit is stated in the plan, not implied.** The adherence-measurement
harness was consciously waived, so nothing will measure whether a cut helped or
hurt. The pre-check and the per-cut grep establish that a cut broke no *reference* —
never that the shortened rule still steers as well as the long one did. The plan
says so and tells the reader not to describe the cuts as validated.

This item was split three ways at processing. The phase table folded into
[merge-cycle-as-queue-machinery]; the genuinely open half — which audits should
exist at all — became [audit-set-design-for-the-cycle], left in Unprocessed rather
than riding into a cleared item on a sibling's coat-tails.

**Files touched:**
- `resources/compression-pass-plan.md` — new, a sibling to the two existing standing plans.

**Routed to Captures:** none from this item.

**FAQ:** not needed because consumers maintain no docset and never run a compression pass.

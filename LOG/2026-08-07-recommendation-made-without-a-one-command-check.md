# 5993a10 — The load-bearing-claims check widened to cover Claude's own assertions, not only the item's

`docs-b/plan.md`'s keep-step already required verifying an item's load-bearing factual claims before discussing it on its own terms. Its subject is now any load-bearing claim in play — **what Claude is about to assert, as much as what the item asserts.** Same test ("would this change if the claim were false?"), same cheapness, one more subject.

Deliberately a scope widening rather than a new rule: a second rule would need its own trigger, and the existing one already fires at the right moment.

The hole it closes is real. A recommendation rests on premises exactly as a work item does, and Claude's premises were checked by nothing, because every verification rule points at text somebody else wrote. The failure that earned it: asked a direct question about making project docs private, Claude recommended making the whole repository private — which would have ended every install and update, because the plugin is distributed from inside that same repository via `./plugin/si-plugin`. One grep of README.md would have caught it, and the fact it establishes was already written in this project's own CLAUDE.md. It was found a turn later, when writing the item forced the install path to be read.

**Recorded with its honest limit rather than oversold:** a recommendation is made at exactly the moment a confident answer is most welcome and least examined, which is the pressure that defeats rules. What makes this more than another wording is that the remedy is an action taken *before* speaking rather than a restraint applied while speaking.

It paid twice more in this session. It caught a message from a companion project asserting that a hook "needs building" when the hook was built and released — overturned by one grep of the hook source. And the check's discipline is what produced the audit findings in this run rather than accepting the queue's own confident claims.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none

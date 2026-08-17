# [HASH] — the /plan carve-out gains the ordering it was missing

No rule was adjudicated. The disposition is a correction to two existing statements: the /plan carve-out in the mid-skill capture rule gains **before any write**, and the mid-run discovery block gains a pointer to it. `plan.md` is unchanged.

The item was filed as a contradiction — two always-loaded statements saying capture-first against one in `plan.md` saying ask-first, with the always-loaded pair winning because it is read by every session. Reading the mechanism narrowed the diagnosis.

**The carve-out already existed and was never lost.** The always-loaded capture rule ends by saying that inside /plan both branches get an offer, and that a Claude-raised one asks once whether to file it or work it now. It landed in the same build as the `plan.md` rule.

Two defects in it, both small. It omitted *before any write*, which is the entire point of the `plan.md` version — and it was attached to a sentence about confirming and resuming "naming what you filed", which presumes the write already happened. So it read as guidance on what to *say after* capturing rather than on asking before. Separately, the mid-run discovery rule still said "capture and continue — the common case" with nothing pointing at the /plan exception.

That explains the observed consistency better than a contradiction would: the right rule was not outvoted, it was written where it reads as being about wording rather than about sequence.

The cost of getting it wrong is a write thrown away, since a capture answered "work it now" is immediately rewritten as a work item — the user's point, and the reason the ordering is now explicit.

Failure evidence is the behaviour being consistent enough across sessions that the user took it for the design.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none

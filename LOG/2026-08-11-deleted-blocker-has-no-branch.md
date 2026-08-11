# [HASH] — A deleted blocker gets its own branch, and the two texts that contradicted each other now agree [deleted-blocker-has-no-branch]

Captured by the user, who asked what happens to items whose blockers have gone stale or been deleted. The verification and diagnosis are Claude's, from reading both texts at processing time.

**The situation.** A blocker that is deleted leaves the held item naming a slug not in the queue. So does a blocker that shipped. From the queue alone the two are identical: both are simply absent.

**The two authorities disagreed, and this was read rather than recalled.** `plan.md`'s revisit said a missing blocker is *a fault; surface it and fix it this session*. `post_tool_use.py` said the opposite — three causes and only one is a fault. One treated absence as broken, the other as usually fine. **And neither listed deletion at all.** It is a fourth cause, and the only one where the correct response is neither lifting the item nor repairing the reference.

**Why deletion needs its own branch rather than folding in.** A blocker is deleted because someone judged it not worth doing, and that judgment frequently undermines the held item's own premise — the held item was designed assuming its blocker would happen. Lifting it clears work whose reason for existing may have died with its blocker. So the response is to re-examine the held item, which is a fate decision and therefore the user's at /plan. That makes it the one branch in the revisit that is a question for the user, and the doc now says so.

**Why it failed silently, which is why it was worth building.** LOG *can* distinguish the two — a shipped item has a build entry, a deleted one is recorded in a /plan close's queue changes — but nothing instructed the session to look. A session finding no ship record had no branch to take, and the cheapest available readings were both wrong.

**Part 3 was reworded after testing, and the correction is the interesting half.** `reorder_queue.py --delete` now reports held items naming the deleted slug. The first version asserted "deleted as not worth doing" — but the same `--delete` removes a *built* item during a /next run, which is the common case, so that reading would have fired wrongly on nearly every use. That is precisely the cry-wolf failure this family of items keeps warning about. The script cannot tell the two apart, so it states both readings and lets the reader pick.

**Why part 3 does not make parts 1 and 2 unnecessary**, the obvious objection: a deletion can happen by hand edit, bypassing the mover entirely, and the two contradicting texts were wrong regardless of how the deletion happened.

A third site turned up that the item did not name: `session_start.py`'s dead-blocker emitter, written earlier in this same run, carried the same three-cause wording. Caught by grepping the literal phrase rather than by memory of having written it.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/hooks/post_tool_use.py`, `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/scripts/reorder_queue.py`
**Routed to Captures:** none from this item

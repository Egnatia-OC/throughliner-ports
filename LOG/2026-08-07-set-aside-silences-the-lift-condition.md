# 5993a10 — A set-aside marker suppresses asking but never a silent mechanical check, and a user-only silence is now disclosed when it is created

The user asked what would actually prompt them with "are you back at the desktop yet?", and whether a lift-condition that is neither a capture nor an advisory is blessed by the method at all. **The answer to the question as asked is yes** — /plan's below-line revisit gathers user-only conditions into one consolidated question per planning session. But it stops being true the moment the same item also carries a `Set aside ·` marker, whose entire purpose is to take an item **out** of that question. An item carrying both has a condition that will never be asked about: the silent shelf the method spent months eliminating, arrived at by following two correct rules at once.

It was nearly created live — Claude was about to move a walk-through below the line with a lift-condition *and* record the user's words as a set-aside, treating both as obviously right. The user's question caught it. Neither rule is wrong and each is well-reasoned alone, so nothing about applying both felt like an error.

**The finding is worse than the capture stated, and this is what the fix had to answer.** The marker is only safe because of the "nothing is quiet forever" guarantee: when the queue has nothing else to offer, set-aside items are raised again. That needs queue exhaustion — no cleared work and nothing unprocessed but set-aside items. This queue holds dozens of items and will not meet that condition in any foreseeable session. So the backstop does not reach, and on a working queue a set-aside is effectively permanent silence unless the user happens to remember. The capture framed this as two rules cancelling out; the sharper finding is that the backstop was designed for a small queue and this is not one.

**The resolution reuses reasoning the method already had rather than inventing a mechanism.** The marker's own guards say it suppresses *recommendations and offers*, and that it changes when an item is **raised**, never whether it is **processed**. Nothing there suppresses a **silent mechanical check** — and a cheap mechanical check is the session seeing, not asking, exactly as the `[user]` lifecycle's check-the-world rule establishes. They govern different things, and saying so resolves the conflict without restoring any nagging.

Three clauses: `plugin-behaviour.md`'s Set aside section gains the suppresses-asking-not-seeing rule and states plainly that queue exhaustion is a weak backstop on a large queue, so nobody later cites it as a guarantee; `plan.md`'s revisit table splits its `set aside` row into checkable (route to the silent check, propose lifting if cleared — a proposal on a condition that really cleared is news, not a re-offer) and user-only (skip); and `done-plan.md` now **discloses the silence in one line at the moment a marker is recorded on a user-only condition**, plus prefers a checkable condition over a user-only one where the same waiting state can be expressed either way.

That disclosure is the half the user actually ran into: the behaviour was correct and completely undiscoverable, and they found out only by asking.

**Rejected, recorded so it is not re-proposed as an oversight:** making the marker and the lift-condition mutually exclusive. Forcing a choice loses either the recorded progress or the condition, and both are information the next run needs.

The live instance, [merged-plugin-live-verification], is **not** un-silenced by this — its retry clause is user-only.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/done-plan.md`
**Routed to Captures:** none

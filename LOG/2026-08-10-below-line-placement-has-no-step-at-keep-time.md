# [HASH] — plan.md's Keep sub-step gained the below-the-line placement procedure it never had

The problem is the user's, in their own words: they always have to explain how
holding things below the line works, and watch like a hawk for Claude failing to
ensure the held item is blocked by something in Unprocessed — and if not, that the
something gets written into Unprocessed so it is. The two-section queue is over a
month old and they are still explaining it.

**The diagnosis: the rule was stated where it is read and the procedure was absent
where it is used.** The always-loaded rules state it, and `plan.md`'s Step 1
revisit knows how to *read* a `Blocked by:` line. But the **Keep** sub-step — the
moment a session decides an item goes below the line — carried no placement
procedure at all. The only procedure for holding an item was in `done-plan.md`,
which loads at the close, after the item has already been written. A session
making the decision had a rule and no step, and met the step at the end of the
session.

Now, in Keep: if the item goes below the line, name its blocker; if that blocker is
not already a queue item, write it into Unprocessed **first**, then write the held
item. Destination-first, for the same reason the existing add-then-remove ordering
gives — a reference resolves the moment its target exists. And if nothing in the
queue blocks it, it belongs above the line.

The live instance that raised it: three items were written below the line naming
[exception-handling-in-rule-authoring] as their blocker before that item existed.
The queue lint caught it after the write; no followed step did.

**Not an enforcement problem.** The lint already backstops this and fired
correctly — it fired again repeatedly during this session's own run, each time
correctly, on items whose blockers had just shipped. This is about getting it right
at the moment of writing rather than being corrected afterwards.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**FAQ: not needed because** the existing entry on what below-the-line means already
describes the rule accurately from the user's side; this adds a step Claude
follows, not a behaviour they see.

**Routed to Captures:** none from this item.

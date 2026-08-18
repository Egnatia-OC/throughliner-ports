# 7e3c1c8 — a Files line names only the files that change, and exclusions move off it

`plan.md`'s two-limb keep check gains a clause: the Files line names only files that change, and a file the item has decided *not* to touch is a different statement belonging in its own sentence outside the line.

The digest extracts every backticked path from that line and keeps anything looking like a file. It has no notion of scope, so an excluded path is indistinguishable from an included one — which is why [law-prose-restyle]'s "`CLAUDE.md` and `SPEC.md` are both out of scope" produced two false merge candidates in the block whose whole purpose is surfacing work that could be settled together. The digest was not guessing wrongly; it was being told wrongly.

The fix is at the authoring end rather than in the detector, matching what [rule-counter-blind-to-bold-prose-rules] settled the day before: a pattern cannot tell an excluded path from an included one any more than it can tell prose from a rule, and teaching it to recognise exclusion phrases would fire on honest text.

[law-prose-restyle]'s own entry was reworded to match, its exclusion sentence moved beneath the Files line. Re-running the digest confirmed both false candidates gone.

Rule gate: run — a subordinate clause on the existing two-limb keep check, which already governs what a Files line must state; no slot spent, nothing evicted.

**Files touched:** `plugin/throughliner/docs-b/plan.md`, `QUEUE.md`
**Routed to Captures:** none

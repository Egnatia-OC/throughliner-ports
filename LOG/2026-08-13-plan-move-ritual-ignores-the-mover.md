# [HASH] — plan.md moves queue items with the mover instead of retyping them

`plan.md` was the only document still prescribing the three-edit mark/add/delete
ritual by hand, in detail, while `next.md` and `done-plan.md` already called
`reorder_queue.py`. The keep-move now calls `--move-section` with `--marker-after`
in the same command, and the below-the-line lift calls `--move`. The digest re-run
afterwards stays — it caught all three of the corruptions the hand ritual was
written to prevent, and costs one command. The hand ritual survives, compressed,
as a named fallback for when the script fails or refuses on a malformed file; its
three recorded failures are real and a fresh session with a broken script still
needs a route.

The marking edit falls away entirely outside that fallback: renaming the heading
to a placeholder existed only to tell two near-identical copies apart, and under
the script there are never two copies.

Skip-to-defer needed no change, correcting the item's own guess — it moves
nothing at all, deliberately, so there was no hand instruction there to replace.

The measurement that made the case: lifting one item and filing one capture by
hand cost 6,253 output tokens across four edits, 66% of that turn, against 8% for
the narration the user actually read.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none

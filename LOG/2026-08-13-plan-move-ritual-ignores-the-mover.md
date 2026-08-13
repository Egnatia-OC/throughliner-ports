# 340e7ef — plan.md moves queue items with the mover instead of retyping them

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

---

## After the close — independently confirmed by another project, within the hour

Written after `340e7ef` was committed and pushed.

Understudy hit this exact defect in a live /plan session on their own project and
reported it before knowing it had been fixed. Their account adds the detail this
entry's rationale lacked: following the three-edit recipe, **the delete could not
be done in one edit at all**, because every paragraph of the original also exists
in the new copy, so nothing short of the entire block is a unique match — and the
block is long. Their session then tried a Python one-liner, which the write-guard
correctly blocked, and only then found `reorder_queue.py`. They noted it is named
in the write-guard's error message but not at the step where a move is authored,
which is the same diagnosis reached here independently.

They then confirmed the fix live: their installed plugin picked up `1.20.0-test9`,
and the same session used the fixed path for its next two keeps, both clean, one
call each.

**One measurement of theirs qualifies a claim made in the reply to them**, so it
is recorded here rather than left in correspondence. The harness echo that
re-prints the top of QUEUE.md fires on the script's writes too, not only on
`Edit` and `Write` — each `--move-section` call produced one. So this change takes
a keep-move from three echoes to one, a two-thirds cut, rather than removing the
cost. Carried as [queue-edit-echo-costs-context], where ownership of the echo is
still unresolved.

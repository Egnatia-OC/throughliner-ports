# 6088ec7 — the reorder script's error paths now name the argument shape, not just the vocabulary

Moving a work item into Processed at a chosen position had cost three attempts in
a real close, and the error messages were why. `--position 4` was told the valid
words were TOP, BOTTOM, BEFORE and AFTER — true, and silent on the thing that
actually mattered, which is that two of those four take a following bare word.
The natural next guess is a named flag, so `--position AFTER --anchor <slug>` came
next, and that produced the general usage line, two turns away from the real
problem.

Replaying it showed the second failure had a cause the work item described only by
its symptom. `--anchor` was not rejected: it was swallowed *as* the anchor slug,
which left two stray arguments and tripped the argument-count check, whose message
is the generic usage. So the script accepted an obviously-wrong anchor and then
complained about something else entirely.

Three changes, all confined to error paths. Both direction-word errors — the
`--position` form and the `--move` form, which had the same shape — now state
that TOP and BOTTOM take nothing after them, that BEFORE and AFTER each take an
anchor slug as the next bare word, and that there is no numeric position. A
missing anchor says so with the shape spelled out rather than falling through to
the general usage. And an anchor that is plainly a flag is rejected by name, so
the `--anchor` guess fails on its own terms instead of two steps later.

The usage string and the module contract were also split: `--position` had been
written as one form with a bracketed optional inside a bracketed optional, which
reads as though the anchor is optional in all four cases when it is required for
two and meaningless for the other two. It is now two lines, matching how the
`--move` forms were already written. The `--move-section` contract note gained one
more sentence while it was open — that the default BOTTOM, in Processed, means
*below* the readiness marker, so an item moved there because it was cleared needs
a `--position` or a follow-up `--marker-after` or the file reads as though nothing
was cleared.

Verified against the actual failures rather than by inspection: the existing test
suite passes, and all three invocations from the reported incident were replayed
against a scratch copy of the queue — each now names the shape, and the working
form still works. The new error text was kept ASCII-only after the console
mangled an em dash in a first draft.

The item's own open question was whether a working script is worth touching for
an ergonomics issue only Claude ever meets. Judged a strawman rather than a live
fork: the change alters no behaviour, has no user-facing surface, and is covered
by the existing tests, while the cost it removes is established rather than
speculative — two turns, recurring at every close that moves an item.

Run under the overnight blitz's sanctioned departures (`resources/overnight-blitz-plan.md`):
approvals deferred, committed to branch `overnight-blitz-2026-08-06`, no push and
no release. Processed out of Unprocessed by this run under the blitz's softened
bar; the reasoning above is recorded in the work item too, so a disagreement has
something to argue with.

FAQ: not needed because the script is invoked by Claude and never by the user —
nothing a non-coder meets has changed.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py` (argument-parser
error paths, the usage string, and the module contract block).
**Routed to Captures:** a third-instance note appended to
[claude-reached-for-shell-write-against-rule] — this run reached for a heredoc
Python splice to remove a work item from QUEUE.md, the same shape that capture
already records twice, this time with the capture itself in the file being
edited.

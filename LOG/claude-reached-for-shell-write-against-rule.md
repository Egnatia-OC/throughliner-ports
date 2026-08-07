# 96166c6 — Gave the queue mover a `--delete` operation, so removing a work item stops being the moment a shell write looks cheaper

Three recorded slips all took one shape: a work item was being removed from a long QUEUE.md, `Edit` demanded reproducing a large block exactly, and a heredoc'd Python splice looked cheaper. The third happened inside an unattended `/next` run with no user present and no harness classifier in the way, while the session was editing the very file holding the capture warning about it.

Sharper prose was ruled out on evidence rather than preference. The rule against it is IMPORTANT-flagged in the user's global instructions, unambiguous, names this exact operation, and was loaded every time. The wording was never the problem — the missing tool was. `reorder_queue.py` could move blocks byte-for-byte but could not delete one, so every removal of a shipped or dropped item fell back to hand-editing a large block, which is exactly when the shortcut looks attractive.

So the fix removes the pressure rather than adding enforcement: give the mover a delete and the safe path becomes the cheap path. This is the method's own recorded pattern — a prohibition with no sanctioned alternative reliably produces an invented one, and the invented move is worse because nothing recognises or records it.

The operation refuses rather than guesses when a slug resolves to nothing or to more than one block, and prints the heading line it removed so the deletion is visible in the transcript. One case needed care and got its own test: deleting the item the readiness marker sits after would silently lose the marker, and a queue with no marker reads as *nothing cleared* — so the marker is re-anchored to whatever now precedes it.

Adding was deliberately left out, and the asymmetry is the reasoning: a capture is an append of fresh text with no existing block to reproduce, so `Edit` handles it cleanly and there is no shortcut to be tempted by. The danger is specific to removal.

**Built out of its queue order**, ahead of five other items, because every removal in the same run otherwise meant hand-editing a long block — the exact cost this item exists to remove. It added no files, so the reorder widened nothing.

/plan turned out to be the primary customer, which the original framing missed: it is the only skill permitted to delete an item at all, and its delete step named no tool.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py`, `resources/testing/test_reorder_queue.py`, `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/plan.md`

**Routed to Captures:** [next-build-removal-step-not-pointed-at-delete] — `next-build.md`'s own per-item removal step was outside this item's Files list and still names no tool, which is where two of the three recorded slips actually happened

# b4de5bf — The mover reports line crossings on both paths, and refuses to clear items nobody named

The crossing report existed only on the within-section reorder path. `--move-section`, which moves an item between sections and may carry `--marker-after`, never ran it — and that is the path where the largest crossings happen. Observed rather than reasoned: a `--move-section … --position BOTTOM --marker-after` swept four held items into the cleared region and reported only that the moved item was now cleared, while the corrective `--move` in the same session printed four crossing warnings. Same hazard, same script, opposite verbosity, and the silent path is the one where a whole held region can move at once.

The report was written because crossings must be visible — its own comment says so — and it was absent from the path where it matters most. The queue lint caught the corruption afterwards, which is a real backstop but a later one.

The user chose refusal over the cheaper report-everywhere-only option, on a distinction that does not overturn the existing reasoning. That reasoning, written into the code, argues for reporting rather than refusing because moving an item across the line is a legitimate way to clear or shelve work and refusing would force a two-step dance for an ordinary operation. It is correct about a deliberate move of a *named* item and keeps that case unchanged. What it never addressed is unnamed items crossing as a side effect of where the marker landed.

**The refusal is asymmetric, and that narrowing was forced by the existing test suite rather than chosen freely.** The specified symmetric form — refuse on any unnamed crossing — was built first, and `test_reorder_queue.py` failed: anchoring the marker to a newly-kept item necessarily shelves whatever sat below it, and that is the commonest planning operation there is. A symmetric refusal would have made the sanctioned route refuse the ordinary case, which is the cry-wolf shape this project keeps repealing. So only an unnamed crossing *into* the cleared region refuses. That is where the harm is: an unattended /next run may build anything above the line, so widening it by accident hands unvetted work to a run with nobody watching. An unnamed crossing *out* is reported and allowed — it narrows what a run may build, the work stays in the queue, and the next planning session sees it.

Both paths now compute crossings before writing, so a refusal leaves the file untouched rather than reporting after the fact. The original report-don't-refuse argument is preserved in the factored helper's docstring, for the case it was written about.

Two cases added: an unnamed sweep refused with the file byte-for-byte unchanged, and a named crossing still reporting and still succeeding — the second pinning the behaviour the refusal must not take.

The item carried its gate disposition twice, the second a truncated copy of the first. The fuller one was transcribed; the duplication is filed as `[duplicate-gate-line-on-a-processed-item]`.

Rule gate: not needed — this extends an existing report to a second code path and adds a refusal branch. No rule in the method's own text is authored or amended.

FAQ: not needed because the mover is Claude's tool; what changes for the user is that a queue edit which would silently clear work they held now stops instead.

**Files touched:** `plugin/throughliner/scripts/reorder_queue.py`, `plugin/throughliner/scripts/test_reorder_queue.py`.

**Routed to Captures:** `[duplicate-gate-line-on-a-processed-item]`.

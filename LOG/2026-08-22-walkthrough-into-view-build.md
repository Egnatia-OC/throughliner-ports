# c904687 — generate_build_view.py and next.md — [user] items' Walkthrough blocks travel into the view verbatim; a missing block prints a halt line

Finding from the previous run ([user-walkthrough-missing-from-view]): the view printed "no build block" for a [user] item, the run may not read QUEUE.md, yet next.md's walk-through branch said to drive the steps the item records — which lived only in queue prose. The alternative, letting the walk-through branch read the queue, was refused: it breaches the run-never-reads-the-queue design for one flavor, and the reasons that design exists (transcription into shipped docs, whole-queue reads) apply to [user] items too. The mechanism mirrors the disposition carry: the view copies the block led by the item's Walkthrough label (bold or plain, `.` or `:`) byte-for-byte, from the label to the end of the entry; where none exists it prints that no walkthrough travelled and the run halts on the item. next.md's walk-through branch now names the view as where the steps come from.

Tick: done, confirmed (24 view suite cases pass via `py`; regenerating this queue shows [discord-post-context-adjacency] carrying its steps). One acceptance expectation did not hold and the cause is in the queue, not the generator: [competition-comparison-article] carries no Walkthrough block at all, so the view correctly prints the halt line for it — a keep-step gap on that item, routed to Captures below.

Rule gate: not needed — script and procedure-doc plumbing for an already-decided lifecycle; no method rule authored.
FAQ: not needed because the walk-through experience is unchanged for the user; only where Claude reads the steps from moved.

**Files touched:** plugin/throughliner/scripts/generate_build_view.py, plugin/throughliner/docs/next.md, resources/testing/test_build_view.py
**Routed to Captures:** [article-walkthrough-missing], filed at the close with the user's go

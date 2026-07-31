# 3ca0e2e — plan.md keep-step made delete-source-first, next.md removal annotated destination-first: closed the both-sections window in QUEUE section-moves [queue-move-viewer-lag]

The reported "item visible in both sections" was diagnosed (2026-07-30) as a procedural both-sections window during a move — add-then-delete across two writes — not a viewer bug. Traced all four named move sites; only plan.md's keep-step actually creates the window (both endpoints are co-visible QUEUE sections). Fixed it to delete-from-source-first: remove from Unprocessed, then add the drafted item to Processed, both writes in one turn, so the item is never in both sections. Alternative weighed and rejected: reusing reorder_queue.py for a byte-for-byte atomic move — ruled out because the keep-step re-authors the item (new rationale prose), so a byte-move would carry stale text, and a single atomic Edit can't span the two non-contiguous sections. Delete-first's loss-risk is mitigated: the drafted item is approved and on-screen before either write, and the existing write-then-verify re-read confirms it landed. Annotated next.md's removal as deliberately destination-first (items in _build.md before QUEUE removal) — correct there because the destination is the working file, not the other QUEUE section. done-plan.md, done-build.md, reorder_queue.py left unchanged (no both-sections move in them). Not user-visible, so no SPEC/FAQ change.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/next.md

**Routed to Captures:** none

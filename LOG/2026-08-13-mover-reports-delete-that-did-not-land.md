# 340e7ef — The queue mover verifies its own write before reporting success

`reorder_queue.py` gained `write_verified()`, which every write path now goes
through: flush and fsync the handle, re-read the file from disk, and confirm the
affected slug resolves where it should — absent from the source section for a
delete, present in the destination for a move, all present for a reorder. A
failure exits non-zero with a plain message naming the slug and what was found,
so a caller cannot read it as success.

The defect being fixed is the false report, not the failed write. A delete that
fails loudly costs a retry. A delete that reports success and does nothing breaks
the guarantee the whole copy-per-item design rests on — that an item still in
QUEUE.md means exactly one thing, not built yet.

The fsync is not decoration and the code says so. This project sits under a file
sync layer, and a plain read-back could be served the same in-flight content and
pass for exactly the reason the check exists. The honest limit is recorded in the
docstring too: this catches a write that never reached the file, not a sync layer
reverting it after the process has exited.

Two tests added: that an ordinary delete really leaves the file, and that
`write_verified` exits non-zero when the re-read disagrees. Verified live — every
queue removal in this run went through the new path.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py`,
`plugin/si-plugin/scripts/test_reorder_queue.py`
**Routed to Captures:** none

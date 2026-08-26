# [HASH] — Log-index read window corrected in the two shipped docs and the post source material

The orientation read's window was changed at [plan-log-index-read-underdesigned] from a bare five lines to a derived one — the index lines newer than the most recent planning session's record — and `plan.md` was updated then. Three other places still described the repealed rule, and two of them ship: the always-loaded rules every session reads, and `done.md`'s month-rollover step. Until this build they gave a session two different accounts of the same step, and they were about to ship with today's release. The third, `ANNOUNCEMENT-IDEAS.md`, is post source material, so the wrong description could have travelled into a public post.

All three now describe the derived window. `SPEC.md`'s sentence was already correct — planning wrote it at the keep-step, since product truth is planning's to write.

The item's own record of how this got through is worth keeping: the repeal-trace rule requires an item repealing a specific sentence to grep its distinctive words across the project before its file list is written, and that grep was not run when the original item was kept. The build stayed inside its named file, correctly — widening scope mid-run is what that rule exists to prevent — so the miss sat at the keep-step. This was logged at the keep as a second recorded instance of the repeal-trace rule not firing, which is the evidence its own admission test asks for. It is noted here rather than acted on.

The acceptance grep was re-run after the edits with both original terms. The only surviving matches are unrelated ordinary uses of "a handful of" in two scripts and one SPEC sentence about queue reading; no live rule text describes the repealed read. Dated history — log entries and queue records quoting the old rule — was left untouched, as the item's refusal line required.

Depth: short.

Rule gate: run — no new rule; the build transcribed the wording already decided and gate-run at [plan-log-index-read-underdesigned], into the docs that missed it.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (index-read sentence, line 1018), `plugin/throughliner/docs/done.md` (month-rollover step, line 287), `ANNOUNCEMENT-IDEAS.md` (line 26).
**Routed to Captures:** none.
**Advisory:** not needed — the close's recommendation is the queue-state ladder's plain statement of what is ready, not a concrete pick.

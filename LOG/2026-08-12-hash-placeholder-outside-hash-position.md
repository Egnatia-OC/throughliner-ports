# e5d169b — A hash placeholder outside hash position is now detectable, and the one stuck entry is repaired

`LOG/2026-08-10-queue-machinery-repair-freeform.md` was written with a non-template header block — `**Slug:** / **Commit:** / **Session type:**` — so its placeholder sat in a `**Commit:**` field rather than at the start of a heading. The backfill matches only hash position, so the entry was never scanned, never filled, and never reported.

The entry is corrected to the template heading shape. Rather than leaving a token for the backfill, the real hash was recovered from the entry's own index line (`f8b03ea`) and written in directly — the item said to check before assuming the backfill could do it, and this entry's title had drifted from anything `git log -S` would match, so it could not have.

`session_start.py` gains `_hash_is_misplaced` and a distinct anomaly message: a `[HASH]` token in a *committed* entry, outside hash position, is reported as a **malformed entry** rather than as the backfill possibly failing. Those are different faults and now read differently.

The detector is deliberately narrow, matching two unambiguous shapes — a field whose value is the token, and the token alone on its line. Any backticked occurrence is excluded before those are tried, because prose discussing the token is correct writing and several entries do it, including the entry about hash placeholders. Firing on those would have built the cry-wolf failure this item was mistakenly filed about. Verified against eight cases including all three prose forms, zero failures, and a scan of the whole real LOG now returns nothing.

**Worth recording: the item's premise was two-thirds wrong, and the /plan that processed it had already corrected it by checking the files rather than re-reading the capture.** The item claimed the hook nags about this at every session start. It does the opposite — the defect is silence, a committed artifact carrying a token no mechanism will ever fill and no check can see. The remedy the item proposed was aimed at a message that does not fire and would not have found this.

**Files touched:** `LOG/2026-08-10-queue-machinery-repair-freeform.md`, `plugin/si-plugin/hooks/session_start.py`
**Routed to Captures:** none from this item
Rule gate: not needed — a hook check and a data repair; no rule in the method's text.

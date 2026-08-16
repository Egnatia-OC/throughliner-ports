# 0e62afe — A new item goes to Unprocessed first and is moved, never hand-placed into Processed

`reorder_queue.py` moves existing items, so authoring a new one directly into Processed has no command and gets done by hand — which is the operation `plan.md` already warns about, where an exact-string edit can corrupt an item with no error. It is not rare: /plan's work-it-now branch places a kept item straight into Processed, and a decision the user gives as an instruction arrives with no Unprocessed entry to move.

Two instances in consecutive sessions. One landed below the readiness marker and was caught by the lint on the next edit. The other landed correctly only because the file's structure was read first — which is the hazard rather than the mitigation.

The answer is procedural, on the user's decision: append to the bottom of Unprocessed like any capture, then move with `--move-section` exactly as a processed capture is. No code changes, no new mover mode, no new tests. The reasoning that decided it: the procedural route costs one extra command, while the code route buys that command back in exchange for a new way for the mover to fail — and the mover is what every queue operation depends on, so its failure surface is the last one worth enlarging to save a keystroke.

**Files touched:** `plugin/throughliner/docs-b/plan.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the keep-step's existing mover instruction, which already tells a session to move rather than hand-edit; this names the one case that instruction did not cover. Subordinate to it, no slot spent. Failure evidence is two instances in two consecutive sessions. **Nothing is evicted** — one paragraph is added, and the rejected alternative was never shipped.

FAQ: not needed because this governs how Claude edits the queue file — nothing a user does changes.

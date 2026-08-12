# e5d169b — --move-section accepts --marker-after, so keeping and clearing an item is one command

Moving an item from Unprocessed into Processed *and* clearing it is the ordinary shape of keeping work at /plan — the commonest planning operation, not an edge case. It took two commands.

**The item's diagnosis was wrong, and the real behaviour is worse.** It reported the call exiting non-zero with `no order supplied: pass a full slug list or use --move`. Reproduced on a scratch fixture rather than taken on trust, as the item instructed: the reported command exits **0**, the move lands correctly, and `--marker-after` is **silently ignored**. It is stripped from argv before the `--move-section` branch is reached, so it never collides with the general path — it simply never reaches `move_section()`. A silent half-execution is worse than a loud failure, and it strengthens the case for the accept-the-combination route the item chose over the better-error one.

`move_section()` now takes `marker_pref` and applies it to the destination section. Every check runs before anything is written, so the call does both halves or neither: no marker in the destination, or a slug that is not there after the move, refuses the whole call. That matters because the readiness marker decides how much work an unattended /next run may build with nobody present, so a move that lands while its marker placement fails is the dangerous outcome, not the tidy one.

Two test cases added: the combined call lands the item above the marker and moves the marker to the named slug, and a bad marker slug refuses with the file byte-for-byte unchanged. The suite runs 13 checks, all passing.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py`, `scripts/test_reorder_queue.py`
**Routed to Captures:** none from this item
**Rule gate:** not needed — a script capability and its tests.

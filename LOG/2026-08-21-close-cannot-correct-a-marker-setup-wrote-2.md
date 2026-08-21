# 15e10c9 — The epoch marker is written only when its conversion ran, so a skip can no longer stamp a shape the project doesn't have

Build entry; the planning record is `2026-08-21-close-cannot-correct-a-marker-setup-wrote.md`. Root cause fixed at the write rather than the lock: /setup once stamped epoch 4 after a skipped conversion, asserting a shape the project didn't have, and no session could correct the marker afterwards. setup.md's step 3a is now conditional — write the new epoch only when the conversion ran to completion; on a skip, leave the old value and say plainly the halt will recur because the conversion is still owed. Accepting the scope-lock for an already-wrong marker stands as the settled answer; widening the lock for approved corrections stays refused. A doc-pinning test covers the skip path.

**Files touched:** `plugin/throughliner/docs/setup.md`, `resources/testing/test_setup_epoch_marker_skip.py` (new, 3 assertions).
**Routed to Captures:** none from this item.
Tick: done, confirmed — the test passes.
FAQ: not needed because the user's action on a skip is unchanged; the halt simply keeps telling the truth.
Rule gate: run — an amendment to setup.md's migration step (the epoch write gains its condition). No freestanding rule; the accept-the-lock half authors nothing.

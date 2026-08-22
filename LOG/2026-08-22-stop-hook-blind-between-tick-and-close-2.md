# [HASH] — The filing-claim hook no longer false-fires on work ticked earlier in the same run

Between an item's tick (which removes it from the queue) and the close (which writes its LOG entry), a slug is in neither file, so the stop hook's filing-claim check read a citation of the run's own finished work as a report of a write that never happened — a false block at the moment of highest confidence, which is how a guard teaches sessions to distrust it. The keep dissolved the item's open question from the record: pre_tool_use.py already reads this session's build working file, so the stop hook reading the same per-session file is precedented and correctly scoped, and the window closes itself when the close deletes the file.

Built: `_slugs_ticked_in_working_file()` — any bracketed slug in this session's `_build-<session-id>.md` is treated as this run's own work, deliberately broad because over-suppression only quiets the guard about slugs the session's own working file names; a missing or unparseable file changes nothing. The once-per-claim downgrade is untouched. SPEC's stop-hook sentence already covers both suppressions — amended at the keep, confirmed against the built behaviour.

Tick: done, confirmed — all nine suite assertions pass, including the three new ones: ticked-slug citation passes, an absent unticked slug still blocks, no working file behaves as before.

**Files touched:** plugin/throughliner/hooks/stop.py, resources/testing/test_stop_hook.py
**Routed to Captures:** none
Rule gate: not needed — a hook fix plus its tests; no method rule changes.
FAQ: not needed because this is hook behaviour a user never steers.

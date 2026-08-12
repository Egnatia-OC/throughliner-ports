# [HASH] — The two standing PreToolUse schema failures were stale fixtures, now fixed

Two assertions had been failing since before this session: *PreToolUse (out of scope): decision is deny* returned `ask`, and *PreToolUse (in scope): emits nothing* emitted the planning-quiet-list advisory.

The /plan diagnosis was confirmed against the code before anything changed. `working_file()` resolves the build working file as `_build-<safe session id>.md`, and `safe_session_id("")` falls back to `unknown`. The fixture wrote a plain `_build.md` and sent no `session_id`, so the hook looked for `_build-unknown.md`, found nothing, and **correctly** concluded no build was running — which produces `ask` where the test expects `deny`, and the no-build advisory where it expects silence. Two failures, one cause.

`_scoped_project` now writes the session-scoped name from a fixed `TEST_SESSION_ID`, and both payloads carry that `session_id`. Both assertions pass.

The comment the item asked for sits on the constant, recording *why* the name is session-scoped — because the legacy name read as correct for weeks, and it read as correct precisely because every document still calls the file `_build.md` in prose. That is the thing that hid this.

`pre_tool_use.py` was **not** changed, per the item's caution: making the hook accept the legacy plain name would reintroduce the cross-session leak the rename removed, where a planning session in one chat finds another chat's working file and applies its file list.

The how-far-back question needed no bisect — it dates to [session-scope-the-working-file] shipping.

**Since this run edited three hooks, all five suites were run.** `hook_schema_check.py`, `test_reorder_queue.py`, `test_pre_tool_use_shell_writes.py` and `test_editing_state_marker.py` all pass. `test_plan_quiet_list.py` fails two assertions from the identical stale-fixture cause — pre-existing, reproduced against a detached checkout of `b51d205`, and in a different file from the one this item scoped, so it was captured rather than folded in.

**Files touched:** `resources/testing/hook_schema_check.py`
**Routed to Captures:** [plan-quiet-list-fixture-also-stale]. It matters beyond bookkeeping: [nothing-runs-the-hook-tests-at-a-close] was held below the line naming *this* item as its blocker, on the ground that a hard close-time gate cannot ship while the suites carry standing failures. They still do. That item's `Blocked by:` was re-pointed at the new capture, with the reasoning written in — not lifted, since lifting is /plan's call at the below-the-line revisit.
**Rule gate:** not needed — stale test fixtures corrected.

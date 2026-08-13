# 16ed591 — The last two standing test failures were stale fixtures, and all five suites now pass

`test_plan_quiet_list.py` asserted that the planning quiet list covers `_plan.md` and `_build.md`. It does not, deliberately: working files were renamed to `_plan-<session id>.md` and `_build-<session id>.md`, and a bare name was visible to every session on the project, which is exactly what session-scoping removed. The fixtures had never been updated, so two assertions had been failing since that rename shipped.

The two cases now assert the session-scoped shape, and a third was added pinning the retired bare name as **not** quiet-listed — so the suite records the current contract in both directions rather than just ceasing to fail.

One thing the item asked for turned out not to be needed, and reading the mechanism is what settled it. The item said to send a matching `session_id` in the payload each case builds, transferring the shape of the earlier schema-check fix. `_is_plan_quiet_path` takes only `(filepath, cwd)` and matches working files by **shape**, not by this session's id — deliberately, since writing to another session's working file is still a planning-note write and the quiet list is about noise rather than ownership. So no payload change was involved. This is the keep-step's sharpened second limb applied to itself: the item asserted how a mechanism behaves, and looking at the mechanism changed the build.

All five suites under `resources/testing/` now pass, including after this run's change to `pre_tool_use.py`. That is the condition [nothing-runs-the-hook-tests-at-a-close] waits on; lifting it is /plan's call at the below-the-line revisit, not a run's.

**Files touched:** `resources/testing/test_plan_quiet_list.py`

**Routed to Captures:** none

Rule gate: not needed — a test-fixture correction, authoring no rule.

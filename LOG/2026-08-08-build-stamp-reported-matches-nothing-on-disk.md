# [HASH] — The host-liveness build stamp stops counting a CLI bookkeeping file, and a test pins it

The session-start hook reports a build stamp — a content hash of the installed plugin's files — so a session can tell whether host-side changes are actually live by comparing it against the target's stamp. It was lying, and it lied in the direction that causes real damage.

**The cause, measured rather than theorised.** The plugin CLI writes a bookkeeping file named `.in_use` into whichever installed build is active, and removes it again as the active build changes. `content_stamp()` hashed it along with everything else — its exclusions covered only `__pycache__` and `.pyc`. Three measurements established this in one session: the installed `1.19.0-test3` and the target `plugin/si-plugin` were byte-identical except for that file; recomputing the installed build's stamp with it excluded produced exactly the target's stamp; and the reported stamp matched the installed directory as it stood with the file present. A live corroboration arrived the same day — the hook reported one stamp at a session start and a different one after a mid-conversation restart, with no reinstall between and the reported version unchanged.

**The original finding was wrong in the dangerous direction, and that is why this earned a test rather than a one-line fix.** The capture that started it concluded "the branch's plugin changes are not live in the host, so the soak has been exercising something else." The host was in fact byte-identical to the target. The comparison lied *toward deferring* — confidently, and it was acted on, feeding a decision about whether to merge. A verification tool that fails toward caution still fails: it spends real time and produces real wrong decisions, and it does so while looking like diligence.

So the build carries an assertion in `hook_schema_check.py`, which the Rezip and Release rituals run before every restart. It asserts the *shape* of the fix rather than the one filename — a stamp unmoved by adding and removing the marker, and still moved by a genuine package file — so the next CLI artifact of this kind is caught by a check that already runs, rather than by another multi-day investigation.

**Files touched:** `plugin/si-plugin/hooks/session_start.py` (`.in_use` added to `content_stamp()`'s exclusions, with the docstring recording why), `resources/testing/hook_schema_check.py` (new `test_content_stamp_ignores_the_cli_in_use_marker`, wired into the suite). Full suite run green.

Host-side: goes live at the next rezip.

**FAQ:** not needed because the build stamp is developer-facing machinery for this self-hosting project — a consumer sees the line but never compares it against a target, and the FAQ has no entry describing it.

**Routed to Captures:** none from this item.

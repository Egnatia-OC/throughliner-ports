# [HASH] — statusline-restart-test: the desktop app never ran the probe, so the mechanism is dead here

**[user] walk-through of the status-line restart test.** Second attempt; the first ran 2026-08-10 and did not discriminate.

**Claude's step 1, re-verified at the start of this walk-through rather than taken on trust:**
- `.claude/settings.local.json` still carries the `statusLine` entry, pointing at `resources/testing/statusline_probe.py` by absolute path.
- `resources/testing/statusline-marker.log` is 504 bytes and holds **only** its header block. Nothing below it, so the app has written nothing since the marker was cleared on 2026-08-10.

**Why this attempt discriminates where the first did not.** On 2026-08-10 the setting was added while the app was already running, so the app that quit had never seen it and the app that relaunched was the first launch with it on disk. That timing explanation is now spent: the setting has been on disk through at least one full launch. A silent marker after this restart means the third outcome — the desktop app does not run status-line commands in this environment.

**Capability check run before handing over**, per the over-tag guard: no tool available quits and relaunches the desktop app, and none can observe what a session on the far side of a restart receives. The tag stands.

**Observable check at close:** the contents of `resources/testing/statusline-marker.log`, read by Claude rather than taken on report.

## Walk-through progress

- Step 1 — probe wiring and marker state confirmed. Done.
- Step 2 — user fully killed the app (process confirmed gone) and relaunched. Done.
- Step 3 — session opened on the far side of the restart. Done.
- Step 4 — Claude read the marker. Done.

## Result: the third outcome. The mechanism is dead in this environment.

`resources/testing/statusline-marker.log` is **504 bytes — its header block and nothing else**, byte-identical to its state before the restart. The app wrote no line.

**Why this run discriminates where 2026-08-10's did not.** That attempt was set aside because `.claude/settings.local.json` had been edited while the app was already running: the app that quit had never seen the `statusLine` entry, and the app that relaunched was the first launch with it on disk. The setting has now been on disk through that full launch *and* this one, so the timing explanation is spent. The remaining alternative — the script being broken — was excluded before the marker was ever cleared, by a hand smoke test that fed the probe a payload on stdin and confirmed it wrote its line correctly.

So of the three outcomes the item names — real percentages, `null` values, or the file never written — this is the third: **the desktop app does not support status-line commands here.**

**What follows, recorded but not acted on.** [statusline-context-reader] is held below the line with `Blocked by: [statusline-restart-test]`, and its own text says that if the file is never written, the mechanism is dead in this environment and the item is deleted. That deletion is a fate decision and therefore the user's, made at /plan — this session records the finding and leaves the item where it is.

Worth noting alongside it: the consumer that item was originally built for was already deleted on 2026-08-11 ([session-sizing-and-break-lines]), so nothing is waiting on the context-% number even if the mechanism had worked.

**This `[user]` item is complete** — walked to its end, with the observable check run by Claude rather than taken on report.

Rule gate: not needed — a walk-through authored no rules and edited no method text.
FAQ: not needed because the mechanism under test never shipped; a consumer has never seen it.

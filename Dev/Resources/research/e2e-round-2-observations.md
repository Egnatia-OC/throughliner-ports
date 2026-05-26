# E2E round 2 observations — 2026-05-24

Taskflow build cycle test with plugin version 0.60.0. Batch 0001 (Project skeleton and Room data model).

## Findings

### 1. After-build must not touch source code (CRITICAL)

After-build detected a build failure (duplicate `kotlin.android` plugin with AGP 9.2.1) and attempted to fix it. This triggered a cascading failure:

- Removed Kotlin plugin → broke `kotlinOptions` DSL → re-added plugin → removed again with different fix → dead template files now cause compile errors (dependencies removed) → deleted dead files (overriding user's explicit refusal) → theme references broken → new file created → cache locked → Gradle daemon kill → force-remove attempt → more template leftovers → stuck on file locks asking user for help.

Total: 6+ minutes of cascading repairs ending in a stuck state.

**Root cause:** After-build's scope includes no mandate to fix code. Its job is recap, MANIFEST update, TEST-LOG rows, and prompting the user. A build failure should be surfaced as "build doesn't compile — fix needed before testing" and left for the next session or a new batch.

**Fix:** Hard boundary in `after-build.md` — after-build must never edit source files, gradle files, or any non-method file. Build failures go in the recap and TEST-LOG notes.

### 2. Stop hook auto-chains before-build → build (BUG)

Before-build completed and said "Next step: run `/build` when you're ready to start." The Stop hook then fired, found unticked files in the batch, and auto-redirected to the batch-executor — no user input.

**Root cause:** Stop hook at `stop.py:322-324` redirects whenever it finds an unticked batch. It doesn't distinguish "just locked by before-build" from "mid-build, continue."

**Fix:** Check whether any files are already ticked. Zero ticked = just locked (exit silent). Some ticked = mid-build (redirect). Clean signal, no new state needed.

### 3. Planning subagent quality good, cost too high

31.6k tokens / 1m 58s for a feature-request routing that resulted in "this is already planned." Push-back on a nonsensical feature request also worked correctly. Quality is not the problem — cost is.

Baseline from 0060 was ~75k, so 0063's efficiency pass roughly halved it, but 31.6k is still too much for a lookup-and-respond operation. Most cost is likely the five drift checks running against empty state (no previous builds, empty TEST-LOG).

**Scoped as 0071.**

### 4. After-build overrode explicit user refusal

User declined dead file deletion ("Why should they be deleted?"). After-build backed off correctly at first. Later, after its own fix cascade broke dependencies, it deleted the same files without re-asking — the compile errors from its own changes made deletion "necessary."

**This is a consent violation.** The user said no. The system should not create conditions that make the refusal untenable, then override it.

### 5. No session-open status summary for users

When a session opens, the user gets no visible summary of project state — how many batches exist, which is next, what it involves. SessionStart injects context for Claude but nothing user-facing.

**User expectation:** "Whenever a session is started it should always give a rundown of how many batches there are, what the next one is and what it involves, and ask if the user would like to do it."

### 6. Before-build worked correctly

19 files locked, 11 tests (all Claude-verified), noted template-file deletions as side effects. Clean output, correct structure. 10.6k tokens — reasonable.

### 7. Prerequisite carve-out worked

Batch executor caught the `TaskflowApplication` manifest gap, halted, surfaced with justification, got approval, respawned with the fix included. The `[Prerequisite, not in plan]` pattern worked as designed.

### 8. User hasn't experienced batch creation through the plugin

Taskflow's 22 batches were written in a pre-plugin session. The user has never gone through the planning subagent's batch-creation flow from scratch. This is the most important untested path — "I have an idea for an app" → planning subagent creates batches. Deferred to Polite Fart Announcer burner app test.

### 9. "Run it yourself" — system commands

Claude asked the user to run a PowerShell command to set JAVA_HOME instead of doing it itself. User told it to do it itself; it complied. The plugin's "plain English over jargon" rule should extend to "run system commands yourself rather than asking the user."

### 10. Desktop app plugin install via zip works

Plugin successfully packaged as zip (`Compress-Archive -Path plugin\* -DestinationPath sovereign-implementer-plugin.zip`) and uploaded via desktop app (Customise → plugin icon → + → Create plugin → Upload plugin). Version 0.60.0 confirmed. See `research/desktop-app-plugin-upload.md`.

### 11. Skills migration eliminates legacy warning

Migrating `commands/before-build.md` and `commands/build.md` to `skills/*/SKILL.md` format resolved the "legacy commands/format" warning on install.

## Token costs observed

| Phase | Tokens | Time | Notes |
|---|---|---|---|
| Planning (feature routing) | 31.6k | 1m 58s | "Already planned" response |
| Planning (push-back) | ~same session | — | Correct refusal |
| Before-build | 10.6k | 11s+ | 19 files locked |
| Build (batch executor) | ~165k | 12m+ | 20 files written, prerequisite carve-out |
| After-build + fix cascade | 3.3k+ | 6m+ | Ended stuck on file locks |

## Priority actions

1. **Hard boundary: after-build cannot edit source code** — scope file needed
2. **Stop hook: don't auto-chain from before-build** — fix in stop.py
3. **Session-open status summary** — scope file needed
4. **Subagent cost optimization** — scoped as 0071
5. **"Run commands yourself" prose rule** — add to universal-behaviour.md

# 0060 — Taskflow E2E prep and testing

## Goal

Prepare Taskflow's docs for a plugin-driven build cycle (structural migration from V34 to current), then run the plugin against Taskflow in a parallel session to gather E2E test notes. This is the first real-project test since V35, covering the six versions of deferred smoke tests (V43–V50).

## Inputs

- Taskflowapp folder at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` (write access required — read-only restriction lifted for this session)
- Taskflowapp's current spine docs in `no-code-method/` subfolder (BACKLOG.md, MANIFEST.md, UX.md, BUILD-LOG.md, TEST-LOG.md)
- Taskflowapp's CLAUDE.md (written by `/setup` at V34)
- Deferred smoke-test list from dev-project CLAUDE.md → *What's next*: V43 mode-aware messaging, V45 fold-in section carve-out, V46 automated test pass, V48 BACKLOG folder-split, V49 batch structure, V49 research folder, V50 build-log folder

## Outputs

- Taskflowapp docs migrated to V50 structure (BACKLOG folder, build-log folder, fold-ins resolved, orphaned files removed)
- E2E test notes from a planning-and-build cycle run with the plugin active in a parallel Taskflow session
- Test notes formatted as input for the next dev-side planning round (before 0054)

## Success criteria

- Taskflowapp's docs pass `/setup` case 4 structural migration cleanly
- At least one planning-and-build cycle completes in the parallel plugin session
- Test notes captured for every deferred smoke-test item
- No regressions in Taskflowapp's existing planning docs (content preserved, structure updated)

## Prep work (done from this dev-side session)

1. Lift read-only restriction on Taskflowapp in this project's CLAUDE.md (session-scoped or permanent — decide at session start)
2. Delete orphaned files: root-level `SYSTEM-PROMPT.md` (duplicate of the one declared in the path block), `CLAUDE.md.foreign-backup-2026-05-21`
3. Resolve the two pending fold-ins (UX.md and SYSTEM-PROMPT.md version footers)
4. Structural migration: BACKLOG single-file → folder format, BUILD-LOG single-file → folder format

## E2E test (user-driven in parallel session)

5. User toggles SI plugin on in a separate Taskflow Claude Code session
6. Run a planning-and-build cycle with the plugin driving
7. Observe plugin behaviour against every deferred smoke-test item
8. Bring observations back to this session as test notes

## Open questions — resolved

- **Read-only restriction:** Lifted permanently. Taskflowapp write access from this project is now allowed for E2E testing and structural migration. CLAUDE.md updated.
- **Subfolder convention:** Works fine. The CLAUDE.md path block maps logical names to physical paths in `no-code-method/`. `/setup` case 4 honours the paths — no move to project root.
- **Cycle count:** Two cycles across two sessions. This session (v61) handles prep + first cycle; a follow-up session handles the second cycle with test notes feeding back.

## Session format — resolved

Alex wants to be coached live through the E2E test step by step in this session (not running it solo in a parallel session). When context runs low, carry over to a new session.

## Prep work completed (v61, sessions 1–2)

1. ✅ Lifted read-only restriction on Taskflowapp permanently in this project's CLAUDE.md
2. ✅ Deleted orphans: `CLAUDE.md.foreign-backup-2026-05-21`, `no-code-method/no-code-method.md.md`, `no-code-method/SYSTEM-PROMPT.md` (duplicate)
3. ✅ Resolved fold-ins: added V34 footers to `UX.md` and `SYSTEM-PROMPT.md`, removed `## Fold-ins pending` section from BACKLOG.md
4. ✅ Fixed Taskflowapp path references (old `C:\Users\Alex\Desktop\Taskflowapp` → new location under `Planning in here\`)
5. ✅ Plugin installed at v0.55.0 via local marketplace in desktop app
6. ✅ Added subagent-warning rule to global `~/.claude/CLAUDE.md`

## `/setup` case 4 results (v61, session 2)

**Detection:** Correct. Identified case 4 (adopted at V34, plugin at V55), offered refresh or cancel.

**Migrations executed:**
- ✅ CLAUDE.md rewritten to V55 template format with JSON path block
- ✅ TEST-LOG.md migrated from 8-column to 10-column format (Type and Verifier columns added)
- ✅ BACKLOG split from single file into `BACKLOG/` folder: INDEX.md + 22 per-batch files (0001–0022), CLAUDE.md path block updated
- ✅ Footer bumps V34 → V55 on all seven docs
- ❌ **BUILD-LOG folder migration missed** — still single-file `BUILD-LOG.md`, path block still points to flat file

**Token cost (three subagent invocations):**
- Case detection: 37.9k tokens (excessive — should be a quick classify, not full doc reads)
- Migration plan: 36.2k tokens (heavy but less offensive — had to read existing docs)
- Migration execution: 88.8k tokens, 10 minutes runtime
- **Total: ~163k tokens for `/setup` case 4.** This is a serious cost finding for Pro users.

## E2E test findings

### From sessions 1–2 (prep and /setup)

1. **Setup subagent token cost is too high.** 37.9k just to detect case 4 and present two options. The subagent is likely front-loading doc reads (DOC-STRUCTURE, VOCABULARY, etc.) before classifying. Should classify first, then load only what the matched case needs.
2. **BUILD-LOG folder migration missed.** Case 4 refresh didn't convert BUILD-LOG.md to the `build-log/` folder format introduced in V50. Fixed manually in session 3. The setup subagent's case 4 migration path needs to include BUILD-LOG → build-log/ folder conversion.
3. **No project-boundary enforcement.** A Taskflow session with the plugin installed can write to any path on the filesystem, including the plugin's own source code. Need a PreToolUse hook that blocks writes outside the project root.
4. **Desktop app plugin management friction.** `/plugin` command doesn't work in desktop app (opens a modal instead). Plugin was stuck at stale v0.37.0 after prior `--plugin-dir` usage. Uninstall caused the plugin card to vanish from Directory. Required manual `enabledPlugins` edit in `settings.json` + Task Manager kill to get a true restart. Full install/reinstall procedure needs documenting.
5. **BACKLOG batch-structure stubs are placeholder.** All 22 per-batch files got V47 format stubs (Goal/Outputs/Success criteria sections + Changes: delimiter) but content is placeholder — needs filling in during the next planning session. This blocked the before-build subagent from locking batch 0001 (see finding #9).

### From session 3 (planning, before-build)

6. **Too many permission prompts in Accept edits mode.** Subagents fire a flood of permission requests even in Accept edits mode. Likely caused by Bash calls, Task/Agent invocations, and possibly Glob/Grep calls that Accept edits doesn't auto-allow. The volume makes the experience feel broken — the user can't step away or focus on anything else.
7. **Planning subagent explores codebase before checking docs.** On a feature request, the planning subagent spawned a Haiku code-exploration agent ("Find category screen code") before checking UX.md and BACKLOG. The answer was entirely in the docs — the code search was wasted tokens and time (~75k tokens, 5+ minutes). The subagent body doesn't enforce doc-first ordering strongly enough.
8. **Token cost not observable.** The token count disappears from the desktop app UI as soon as the next message arrives. No way to track cumulative cost without watching the exact moment each agent finishes. Desktop app limitation, not fixable from the plugin — but makes cost monitoring during E2E testing impractical.
9. **Before-build correctly gates on placeholder content.** Before-build refused to lock batch 0001 because its scope-context sections (Goal, Outputs, Success criteria) still contained `[To be filled in during the next planning session.]` placeholder text, change-list items lacked `[Requested]`/`[Suggested]` provenance labels, and the `Serves UX.md:` line was misplaced. This is correct behaviour — the subagent caught the problem and halted rather than proceeding with garbage. But it means a full build cycle can't be tested until at least one batch has real planning content.

### What these findings reveal about downstream subagents

The findings from setup, planning, and before-build expose patterns likely to repeat in the batch-executor and after-build subagents:

**Token cost compounds through the pipeline.** Setup cost ~163k tokens. Planning cost ~75k+ for a single scope-existence check. A full build cycle (planning → before-build → build → after-build) could easily burn 300k–500k tokens — a significant fraction of a Pro user's daily allowance on a single batch. The root cause is consistent: subagents front-load doc reads and spawn inner agents for work that could be direct reads. Every subagent in the chain likely has this problem; fixing it in one doesn't fix the others.

**Permission prompt flood will be worse during builds.** Planning and before-build are mostly reads with a few writes. The batch-executor writes to every file in the batch's file list, plus ticks each one in BACKLOG. The after-build subagent writes to MANIFEST.md, TEST-LOG.md, and build-log/. Each write triggers a permission prompt in Accept edits mode. Bash calls for Claude-automatable tests (after-build) definitely trigger prompts. A build batch touching 8–10 files could generate 30+ permission prompts across executor and after-build combined.

**Codebase exploration tendency will be expensive during builds.** The planning subagent explored code before checking docs. The batch-executor *legitimately* needs to read code, but if it also spawns exploration agents to "understand the codebase" before starting file-by-file work, the overhead multiplies. The executor's instructions should be explicit: read the files in the batch's `Files:` list and the resources in `Inputs:`, nothing else.

**Placeholder stubs block the entire pipeline.** `/setup` case 4 created 22 batch files with placeholder content. Before-build correctly refuses to lock any of them. This means a full E2E build cycle requires filling in at least one batch's scope-context sections through a proper planning session first — and the planning session itself was expensive and wandered into code exploration. The prep cost to reach a testable build state is high.

### Preemptive changes for more fruitful future E2E testing

These changes address root causes, not symptoms. Each would make the next E2E round cheaper and faster to reach a testable build cycle.

1. **Enforce doc-first ordering in the planning subagent body.** Add an explicit instruction: "Check UX.md and BACKLOG for scope existence before any codebase exploration. Only explore code if the docs don't answer the question." This eliminates the wasted code-search pattern (finding #7) and should cut planning token cost significantly.

2. **Defer doc reads in all subagent bodies until after classification.** The setup subagent reads DOC-STRUCTURE and VOCABULARY before it even knows which case it's in. Planning may do the same. Each subagent should classify/triage first (a cheap operation — read CLAUDE.md path block, check a few markers), then load only the docs the matched path needs.

3. **Add BUILD-LOG folder migration to /setup case 4.** One-line gap (finding #2) — case 4 handles BACKLOG folder split and TEST-LOG column migration but misses BUILD-LOG. Adding it means future E2E setups complete without manual fixup.

4. **Fill one Taskflow batch with real planning content before the next E2E round.** The placeholder stubs (finding #5) block the entire build pipeline. Rather than testing planning-to-fill-a-batch and building in the same E2E session (expensive), fill batch 0001's scope-context sections in a dedicated Taskflow planning session beforehand. Then the next E2E test can start directly at `/before-build` → `/build` → after-build — testing the build pipeline without burning tokens on planning first.

5. **Audit subagent bodies for inner agent spawns.** Each subagent may spawn Explore, Plan, or general-purpose agents internally for work that could be a direct Read or Grep. An audit of all five subagent bodies (planning, before-build, batch-executor, after-build, setup) looking for agent-spawning patterns would identify where tokens are being burned on intermediaries.

## Status

E2E testing paused after before-build gate. Three subagents tested (setup, planning, before-build); two untested (batch-executor, after-build). Nine findings logged. Next E2E round should address preemptive changes 1–4 before attempting a full build cycle.

## Risks / dependencies

- Plugin version confirmed at 0.55.0 — correct for current method version V55.
- Taskflow session must be told "do not modify files outside this project folder" until project-boundary hook is built.
- Context carryover: sessions 1–2 burned significant context on prep work and plugin install troubleshooting. Session 3 completed E2E testing through before-build.
- Crash course updated with "sessions are stateless; docs are the memory" paragraph (session 3).

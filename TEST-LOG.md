# TEST-LOG.md — Smoke test record (this project)

One row per check per session. Newest at bottom. Status (`Pass`/`Fail`/`Skipped`) is never edited — regressions append new rows. `Superseded` only when a component changes enough to invalidate the original test. Entry-shape spec in `BUILD-METHOD.md` → *TEST-LOG entry shape*.

---

## V18–V22 — backfilled from BUILD-LOG (2026-05-16)

Reconstructed from BUILD-LOG.md. Pre-dates live discipline (V24).

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 001 | 2026-05-12 | V18 | Plugin loads via `claude --plugin-dir <path>` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`) | Pass | First-ever plugin smoke test. |
| 002 | 2026-05-12 | V18 | `/hooks` shows `SessionStart` registered after plugin load | `hooks/hooks.json` + `hooks/session_start.py` | Pass | |
| 003 | 2026-05-12 | V18 | Claude recites the eight universal-behaviour rules verbatim when asked at session start | `hooks/universal-behaviour.md` (via `SessionStart` additionalContext) | Pass | Confirms hook stdout reaches conversation context. |
| 004 | 2026-05-13 | V19 | Plugin loads in scratch directory | plugin scaffold | Pass | |
| 005 | 2026-05-13 | V19 | Both `SessionStart` and `PreToolUse` hooks registered after load | `hooks/hooks.json` | Pass | |
| 006 | 2026-05-13 | V19 | `/init-project` scaffolds the four templates cleanly into an empty directory | `plugin/skills/init-project/` + `plugin/templates/` | Pass | |
| 007 | 2026-05-13 | V19 | `/init-project` refuses on a non-empty target directory with a clear error | `plugin/skills/init-project/scripts/scaffold.py` (recursive scan) | Pass | Sandbox `/tmp/scaffold_test2/docs/UX.md`; refused with exit code 2. |
| 008 | 2026-05-13 | V19 | `PreToolUse` hook blocks `Edit(UX.md)` with deny message visible to Claude | `hooks/pre_tool_use.py` | Pass | Stress-tested with explicit "attempt the edit anyway"; deny worked. |
| 009 | 2026-05-13 | V19 | Claude pivots to add `[FOLD-IN PENDING]` block to `BACKLOG.md` after `UX.md` edit denial | `hooks/pre_tool_use.py` (deny-message redirect text) | Pass | Worked as designed. |
| 010 | 2026-05-13 | V19 | `BACKLOG.md` edit proceeds unblocked (post-pivot, since `BACKLOG.md` isn't locked) | `hooks/pre_tool_use.py` (matcher scope check) | Pass | |
| 011 | 2026-05-13 | V19 | `${CLAUDE_PLUGIN_ROOT}` expands correctly inside a skill body on Windows | `plugin/skills/init-project/SKILL.md` | Pass | Resolved V19 plan uncertainty in one try; expanded to full Windows path. |
| 012 | 2026-05-13 | V19 | Skill frontmatter shape produces a working slash command at `/no-code-method:init-project` | `plugin/skills/init-project/SKILL.md` (`disable-model-invocation: true`, `user-invocable: true`) | Pass | |
| 013 | 2026-05-13 | V19 | V18 universal-behaviour rules self-police a placeholder edit *before* `PreToolUse` fires | `hooks/universal-behaviour.md` | Pass | Claude refused citing UX.md "no placeholders" rule before the hook ran. Rules do soft work beyond hook backstop. |
| 014 | 2026-05-13 | V19 | Windows subfolder-conflict in `/init-project` recursive scan | `plugin/skills/init-project/scripts/scaffold.py` | Skipped | Validated equivalent in Linux sandbox (`pathlib.rglob` name matching is platform-agnostic). Conscious skip per V19 BUILD-LOG. |
| 015 | 2026-05-14 | V21 | Plugin loads via `claude --plugin-dir <path>` in `~\v21-scratch` | plugin (V21 state) | Pass | |
| 016 | 2026-05-14 | V21 | `/hooks` confirms `SessionStart` + `PreToolUse` both registered | `hooks/hooks.json` | Pass | |
| 017 | 2026-05-14 | V21 | Empty-folder session emits tier 1 (silent — no `additionalContext`) | `hooks/session_start.py` (tier detection) | Pass | Behaviour change from V18; verified V21's narrower scope. |
| 018 | 2026-05-14 | V21 | `/init-project` scaffolds four templates cleanly (V21 templates, post-footer bump) | `plugin/skills/init-project/` | Pass | |
| 019 | 2026-05-14 | V21 | Fresh Claude Code session against scaffolded folder fires tier 3 | `hooks/session_start.py` (tier detection + foundational reads) | Pass | |
| 020 | 2026-05-14 | V21 | Tier-3 emit: path block resolves 3 of 3 declared SoT doc paths | `hooks/session_start.py` (path block parser) | Pass | |
| 021 | 2026-05-14 | V21 | Tier-3 emit: template state detected in all four spine docs | `hooks/session_start.py` (template-state detector) | Pass | All four spine docs had `[Project Name]` placeholder intact. |
| 022 | 2026-05-14 | V21 | Tier-3 emit: routing reminder present in additionalContext | `hooks/session_start.py` | Pass | |
| 023 | 2026-05-14 | V21 | Version-footer mismatch tripwire detects out-of-sync footer | `hooks/session_start.py` (footer comparison vs. `PLUGIN_METHOD_VERSION`) | Pass | Surfaced real bug — `plugin/templates/*.md` footers missed during V20→V21 bump. Tripwire paid for itself. |
| 024 | 2026-05-14 | V21 | Tier-2 detection on a method-shaped folder with partial structure | `hooks/session_start.py` (tier-2 detector + 4 sub-cases) | Skipped | Mid-smoke-test tripwire catch already exercised structural-mismatch path end-to-end. Per V21 BUILD-LOG: revisit only if real-world tier-2 misfires surface. |
| 025 | 2026-05-14 | V22 | Planning subagent invoked in Taskflow via auto-delegation | `plugin/agents/planning.md` (subagent body + auto-delegation description) | Pass | Subagent fired + produced recap; surfaced INVENTORY ghost-command issue (#026). |
| 026 | 2026-05-14 | V22 | INVENTORY shipped/unshipped annotations correct | `planning/INVENTORY.md` (slash-commands list) | Fail | INVENTORY listed future commands (`/migrate`, etc.) as if shipped; subagent recommended `/migrate` (not shipping until V27). Fixed same V22 commit: annotated every entry "Shipped Vxx" / "Pending Vxx" + top-of-section preface. See #027. |
| 027 | 2026-05-14 | V22 | INVENTORY shipped/unshipped annotations correct (post-fix retest) | `planning/INVENTORY.md` | Pass | After in-session annotations fix. |
| 028 | 2026-05-14 | V22 | V21 SessionStart hook tier-2 detection on Taskflow | `hooks/session_start.py` (tier detection) | Pass | Per V22 BUILD-LOG: tier-2 classification correct; main Claude read gap flag and declined auto-route to planning. |
| 029 | 2026-05-14 | V22 | Serves-line PreToolUse deny on broken entry name | `hooks/pre_tool_use.py` (V22 Serves-line check) | Skipped | Taskflow is tier 2; full auto-route + Serves-line flow requires tier 3. Pivot to v22-scratch hit side-quests (mistaken `/init-project` from Taskflow's session; loop-detection menu on third invocation). Resolved by closing Taskflow session and starting fresh, but explicit deny test not completed. |
| 030 | 2026-05-14 | V22 | Serves-line PreToolUse accept on case-insensitive match | `hooks/pre_tool_use.py` (V22 Serves-line check) | Skipped | Same as #029. |

---

## V23 — no testable code (2026-05-17)

Cowork-mentions-strip across method docs + plugin components. No behavioural change; no rows.

---

## V24 — TEST-LOG creation + BUILD-METHOD doc

Creates TEST-LOG.md itself; adds BUILD-METHOD.md as peer to BUILD-LOG.md. Dev-internal-only; no rows.

---

## V25 — Build orchestration core (2026-05-16)

CLI pre-validation via outputs/ workaround. Windows integration deferred to post-commit PowerShell session.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 031 | 2026-05-16 | V25 | `parse_backlog.py` CLI: 15-scenario suite covering top-batch detection, change_list parsing, Files: tick-state, Serves line extraction, prerequisite labels, malformed-input lenience | `plugin/scripts/parse_backlog.py` | Pass | 15/15. Pre-validation tier (CLI). outputs/ workaround. Windows retest owed. |
| 032 | 2026-05-16 | V25 | Stop hook end-to-end CLI: 8-scenario suite covering empty backlog, single-batch redirect, post-completion next-batch redirect, `stop_hook_active` loop prevention, parser-error lenience | `plugin/hooks/stop.py` (+ `parse_backlog.py`) | Pass | 8/8. Pre-validation. Loop-exit (Opus risk #2) verified. outputs/ workaround. Windows retest owed. |
| 033 | 2026-05-16 | V25 | PreToolUse boundary check (V25 (c)) + V19 (a)/(b) read-only and V22 (e) Serves-line regression: 9-scenario suite | `plugin/hooks/pre_tool_use.py` | Pass | 9/9. Pre-validation. New (c) blocks edits outside Files: and allows prerequisite-labeled files; V19/V22 checks still pass. outputs/ workaround. Windows retest owed. |

---

## V25 — Windows integration smoke test (2026-05-17)

PowerShell, `claude --plugin-dir`, pre-populated `v25-scratch`. Three Fail rows = real V25 bugs → OPEN-QUESTIONS entries for V26.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 034 | 2026-05-17 | V25 | Plugin loads via `claude --plugin-dir` from `v25-scratch` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`, `commands/`, `agents/`) | Pass | Windows integration tier; deferred from session resume. |
| 035 | 2026-05-17 | V25 | `/hooks` shows 3 hooks configured: PreToolUse (1), SessionStart (1), Stop (1) | `plugin/hooks/hooks.json` + the three hook scripts | Pass | Header confirms exact V25 expectation; other hook types show no count. |
| 036 | 2026-05-17 | V25 | `/agents` Library shows 3 plugin subagents (planning, before-build, batch-executor) | `plugin/agents/*.md` | Pass | Listed as `no-code-method:batch-executor`, `before-build`, `planning` — all "inherit" model. Library tab = canonical registry; Agents tab = current-conversation invocations only. |
| 037 | 2026-05-17 | V25 | Both V25 slash commands registered, accessible via `/no-code-method:before-build` and `/no-code-method:build` | `plugin/commands/*.md` | Pass | Bare names don't auto-resolve — `/no-code-method:` prefix required for commands-directory pattern. `/init-project` (skill-with-flags) auto-shortens; new commands don't. Worth noting; not blocking. |
| 038 | 2026-05-17 | V25 | SessionStart tier-1 silent in empty `v25-scratch` (initial launch, before pre-population) | `plugin/hooks/session_start.py` (tier detection) | Pass | Empty folder → tier 1, no `additionalContext`. V21 regression coverage. |
| 039 | 2026-05-17 | V25 | SessionStart tier-3 emit in configured `v25-scratch` (pre-populated CLAUDE.md + spine docs with V25 footers) | `plugin/hooks/session_start.py` (tier detection + foundational reads) | Pass | Verified indirectly: `/no-code-method:before-build` had context it needed (CLAUDE.md path block, BACKLOG.md state, UX.md entries). No project-confusion from main Claude. |
| 040 | 2026-05-17 | V25 | V19 PreToolUse hook still blocks UX.md writes with deny-and-redirect message | `plugin/hooks/pre_tool_use.py` (V19 (a) + (b)) | Pass | Regression check. During pre-restart `/init-project`: Write(UX.md) → PreToolUse deny with canonical "UX.md is locked" + FOLD-IN PENDING redirect → Claude wrote real fold-in block to BACKLOG.md. |
| 041 | 2026-05-17 | V25 | Stop hook misfires on template-placeholder BACKLOG.md (fires immediately after `/init-project` scaffolds, redirects with literal placeholder payload as if a real batch) | `plugin/hooks/stop.py` (+ `plugin/scripts/parse_backlog.py` placeholder detection gap) | **Fail** | Parser treats template example batch as real unticked batch. Main Claude refused (soft discipline saved it). V26 fix: parser detects bracketed-placeholder → returns `{}`. |
| 042 | 2026-05-17 | V25 | BACKLOG-TEMPLATE.md's instructional canonical-format example block uses the literal `[FOLD-IN PENDING]` marker | `templates/BACKLOG-TEMPLATE.md` + `plugin/templates/BACKLOG-TEMPLATE.md` | **Fail** | Template uses real marker, making real fold-ins indistinguishable from example. V26 fix: code-fence example + relocate canonical-format docs to DOC-STRUCTURE.md. |
| 043 | 2026-05-17 | V25 | `/no-code-method:before-build` invokes before-build subagent end-to-end (validate → enumerate → recap) | `plugin/commands/before-build.md` + `plugin/agents/before-build.md` | Pass | After self-recovery from #044, before-build read state, validated batch, produced recap. Subagent flow shape works as designed. |
| 044 | 2026-05-17 | V25 | before-build subagent body specifies parser invocation as `python plugin/scripts/parse_backlog.py` (project-relative path, no BACKLOG.md argument) | `plugin/agents/before-build.md` (validate-pass step 1) | **Fail** | Real V25 bug. Parser lives at `${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py`, requires BACKLOG.md path as `argv[1]`. Subagent recovered via Glob + retry but spec is wrong. V26 fix: rewrite step 1 to use `${CLAUDE_PLUGIN_ROOT}` + pass absolute BACKLOG.md path. See `planning/OPEN-QUESTIONS.md`. |
| 045 | 2026-05-17 | V25 | `/no-code-method:build` (or chained from before-build's completion) spawns batch-executor with the batch payload | `plugin/commands/build.md` + `plugin/agents/batch-executor.md` | Pass | Unclear from chat whether `/build` was invoked or main Claude chained directly into batch-executor after before-build's recap. Either way, batch-executor spawned correctly. |
| 046 | 2026-05-17 | V25 | batch-executor reads UX.md + MANIFEST.md before file edit | `plugin/agents/batch-executor.md` | Pass | Read(UX.md) + Read(MANIFEST.md) as first two tool uses in subagent context. Matches "First action — load project state" step. |
| 047 | 2026-05-17 | V25 | batch-executor writes the file declared in `Files:` list, ticks BACKLOG.md per-file, updates MANIFEST.md | `plugin/agents/batch-executor.md` (per-file work loop + completion path) | Pass | Sequence: Write(index.html) → Edit(BACKLOG.md) flipping `- [ ]`→`- [x]` → Edit(MANIFEST.md) adding entry. Per-file ticking + post-build MANIFEST update both correct. |
| 048 | 2026-05-17 | V25 | batch-executor produces build recap with correct shape per *After every build* | `plugin/agents/batch-executor.md` (recap shape) | Pass | All spec sections present: "UX.md changes implied" (None), "Red flags" (None), "Next steps" (refresh + open + /clear), "Files touched" (3 listed). |
| 049 | 2026-05-17 | V25 | Rendered output matches UX.md "Hello screen" entry (index.html renders "hello" centered in browser) | end-to-end across V25 + generated `index.html` | Pass | Tab titled "hello", body "hello" centered both axes via inline flex. Artefact matches UX entry's stated behaviour. |
| 050 | 2026-05-17 | V25 | Stop hook does NOT misfire when current batch is fully complete (all `- [x]`) | `plugin/hooks/stop.py` (parser skip-completed logic) | Pass | After batch-executor finished + ticked, chat returned to idle — no redirect, no loop, no inappropriate next-batch. Parser skip-completed worked as designed. |

---

## V27 — Test-confirmation gate + after-build + planning extension (2026-05-17)

8/13 ran (6 Pass, 1 Fail, 1 partial Pass w/ caveat); 5 Skipped pending AB2 lock-bug fix. Tiers: G1–G3 direct hook-script; G4/G5/P1/AB2 `claude --plugin-dir` against fixtures; D1 direct Read. Three V27 bugs → OPEN-QUESTIONS.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 051 | 2026-05-17 | V27 | D1 — `DOC-STRUCTURE.md` carries the *Change list — `[Requested]`/`[Suggested]` labels* sub-section under *Build batches* | `DOC-STRUCTURE.md` | Pass | Read of line 119 — bolded paragraph with labels-on-changes-not-files rule, planning/before-build/after-build chain, carve-out-labels note. Matches V27 BUILD-LOG Decision 1 (Q3 placement). |
| 052 | 2026-05-17 | V27 | G4 — PreToolUse check (f) permits Task → batch-executor when TEST-LOG has no unconfirmed previous-session rows | `plugin/hooks/pre_tool_use.py` (V27 check (f)) | Pass | Fixture had all rows `Confirmed Explicitly: Yes`. `/no-code-method:build` → Task → batch-executor; gate allowed silently; subagent proceeded into per-file work. |
| 053 | 2026-05-17 | V27 | G1 — Gate denies Task → batch-executor when TEST-LOG has unconfirmed rows and BUILD-LOG is parseable (narrowed mode) | `plugin/hooks/pre_tool_use.py` (V27 check (f), BUILD-LOG-narrowed path) | Pass | Direct hook invocation. Deny JSON identified session `v26`, named both unconfirmed rows + components. Caveat: parallel `claude --plugin-dir` attempt showed batch-executor running via Stop-hook redirect — script-level gate works; wiring layer uncertain. |
| 054 | 2026-05-17 | V27 | G2 — Gate denies in strict fallback when `BUILD-LOG.md` is missing | `plugin/hooks/pre_tool_use.py` (V27 check (f), strict-fallback path) | Pass | After `Remove-Item BUILD-LOG.md`. Deny JSON: "BUILD-LOG.md not found — strict fallback mode: any `Confirmed Explicitly: No` blocks", fix advice (path block / root), both rows enumerated. Distinguishable from G1 wording. |
| 055 | 2026-05-17 | V27 | G3 — Gate denies in strict fallback when `BUILD-LOG.md` present but unparseable | `plugin/hooks/pre_tool_use.py` (V27 check (f), strict-fallback path, unparseable variant) | Pass | Fixture: BUILD-LOG.md with only `#`/`###` headings (no `## <token>`). Deny JSON: "present but unparseable — no `## <session-tag>` heading at top", strict-fallback mode, fix advice (`expected ## <tag> ... newest first`). Distinguishable from G2 wording. |
| 056 | 2026-05-17 | V27 | G5 — SessionStart tripwire fires when previous-batch TEST-LOG rows are unconfirmed; routes main Claude to planning subagent regardless of opener | `plugin/hooks/session_start.py` (V27 TEST-LOG tripwire) | Pass | Verified during G1 attempt. Main Claude opened: "I can't run /build right now — SessionStart hook flagged previous batch's test session (v26) open with two unconfirmed rows" and routed to planning subagent instead of /build's flow. Tripwire surfaced + was acted on. Part (b) — tripwire absent when all confirmed — implicitly verified by G4. |
| 057 | 2026-05-17 | V27 | P1 — Planning subagent leads with first pending row (per-row read-back) as first sub-step of *During planning* | `plugin/agents/planning.md` (V27 extension — Rule 2) | Pass | Verified during G1 attempt. Planning subagent invoked via tripwire-routing override; asked "Row #001 — Pending row one... — Pass, Fail, or Skipped?" by name. Specific-row read-back shape confirmed. Caveat: "advances to next row" half not exercised — turn ended on question, Stop-hook bug derailed next turn before answer. |
| 058 | 2026-05-17 | V27 | AB2 — after-build subagent appends blank-Status rows to `TEST-LOG.md` when opening a test session | `plugin/agents/after-build.md` (test-session-open step) + `plugin/hooks/pre_tool_use.py` (V19 check (a)) | Fail | **Critical V27 bug.** Write(TEST-LOG.md) denied — TEST-LOG.md in path block but not in `WRITABLE_LOGICAL_NAMES`. One-line fix: add `"TEST-LOG.md"` to writable set. Without it, V27 gate is structurally inert. |
| 059 | 2026-05-17 | V27 | AB1 — after-build subagent silently updates `MANIFEST.md` for created/renamed/deleted elements | `plugin/agents/after-build.md` (MANIFEST silent update step) | Skipped | Blocked by AB2 (#058). After-build halted; diagnostic reported "decided no MANIFEST.md entry warranted (trivial placeholder)" but couldn't progress past TEST-LOG write to verify silent-update in non-trivial case. Retest after fix. |
| 060 | 2026-05-17 | V27 | AB3 — after-build recap labels `[Requested]` / `[Suggested]` from BACKLOG.md change-list bullets | `plugin/agents/after-build.md` (recap shape, label-read pass) | Skipped | Blocked by AB2 (#058). After-build halted before recap. Retest after fix. |
| 061 | 2026-05-17 | V27 | P2 — Planning subagent pushes back on bulk confirmations during read-back | `plugin/agents/planning.md` (V27 extension — per-row enforcement, "Never infer completion") | Skipped | Depends on after-build successfully opening test session via TEST-LOG writes. AB2 (#058) blocks natural setup. Retest after fix; alternatively testable with hand-crafted fixture rows (G1 style). |
| 062 | 2026-05-17 | V27 | L1 — Planning subagent writes `[Requested]` / `[Suggested]` labels inline on BACKLOG.md change-list bullets | `plugin/agents/planning.md` (V27 extension — inline label-writing) | Skipped | Deferred to post-fix retest. Claude Code wiring issues this session (Stop-hook-vs-tripwire conflict, gate visibility on redirect) make subagent runs fragile. |
| 063 | 2026-05-17 | V27 | L2 — before-build subagent preserves `[Requested]` / `[Suggested]` labels across halt-C re-batching splits | `plugin/agents/before-build.md` (label-preservation rule) | Skipped | Deferred to post-fix retest. Needs fixture engineered for halt-C verification-burden split; fragile against this session's wiring issues. |

---

## V28 — V27 fix sweep + helpers extraction (2026-05-18)

Live `claude --plugin-dir` against rebuilt g4 fixture. Two-session run: (1) Stop hook → after-build → MANIFEST + recap + TEST-LOG row; (2) restart → tripwire → planning read-back → Pass recorded. All rows Pass; one caveat on #069.

Three V27 Skipped rows unblocked: AB1 (#059), AB3 (#060) retested via after-build; P1 (#057) regression-checked. P2 #061, L1 #062, L2 #063 remain Skipped (need narrower fixtures).

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 064 | 2026-05-18 | V28 | AB2 retest — after-build writes blank-Status rows to `TEST-LOG.md` when opening a test session (the V19-check-(a) fix) | `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES += "TEST-LOG.md"`) + `plugin/agents/after-build.md` | Pass | Write(TEST-LOG.md) succeeded; row #001 landed with blank Status. Flips V27 #058 Fail. |
| 065 | 2026-05-18 | V28 | AB1 retest — after-build silently updates `MANIFEST.md` for created elements | `plugin/agents/after-build.md` (MANIFEST silent update step) | Pass | MANIFEST entry added (alphabetical, single-line). Flips V27 #059 Skipped. |
| 066 | 2026-05-18 | V28 | AB3 retest — after-build recap labels `[Requested]` / `[Suggested]` from BACKLOG.md change-list bullets | `plugin/agents/after-build.md` (recap shape, label-read pass) | Pass | Recap "What shipped" carried `[Requested]` label from BACKLOG. Flips V27 #060 Skipped. |
| 067 | 2026-05-18 | V28 | SessionStart tripwire fires post-refactor (V27 #056 regression check after V28 helpers extraction) | `plugin/hooks/session_start.py` (TEST-LOG tripwire) + `plugin/scripts/project_state.py` (extracted helpers) | Pass | Run 2 (restart with unconfirmed row from run 1). Main Claude invoked planning subagent to close test session. Confirms `project_state.py` extraction faithful to V27 behaviour. |
| 068 | 2026-05-18 | V28 | Planning subagent per-row read-back post-refactor (V27 #057 regression check) | `plugin/agents/planning.md` (V27 extension — Rule 2) | Pass | Specific-row read-back shape preserved post-refactor. Full advance-after-answer path also verified (see #070). |
| 069 | 2026-05-18 | V28 | Stop hook exits silent when previous-batch test session is open (V28 stop.py fix) | `plugin/hooks/stop.py` (V28 `is_test_session_open` check before `run_parser`) + `plugin/scripts/project_state.py` | Pass (caveat) | Stop hook exited silent as expected. **Caveat:** fixture's batch was fully ticked, so `run_parser` would return empty even without V28's check — uniquely-V28-distinguishing scenario (unticked batch + unconfirmed rows) not replicated. Mechanical inspection supports Pass. |
| 070 | 2026-05-18 | V28 | Planning subagent records Pass + closes test session via Edit on `TEST-LOG.md` | `plugin/agents/planning.md` (read-back close-out) + `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES` applies to Edit too) | Pass | Edit flipped row #001 Status to Pass, Confirmed Explicitly to Yes. Drift checks clean. Demonstrates Edit (not just Write) uses the V28 fix path. |

---

## V29 — Safety net + unified `/adopt` skill-command (2026-05-19)

Live tests across 5 fixture folders, one per `/adopt` case. Plugin v0.29.0. Three findings fixed in-commit. Row #083 Fail and #089 Skipped — fixes applied, retest owed.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 071 | 2026-05-19 | V29 | Case 1 (empty folder): SessionStart silent — no advisory fires | `plugin/hooks/session_start.py` (V29 unadopted-folder detection) | Pass | Fixture `case1-empty/` (single `.placeholder` file, under Q2 threshold). Claude Code banner shows standard greeting, no `[no-code-method]` advisory line. |
| 072 | 2026-05-19 | V29 | Case 1: `/adopt` detects empty case, walks 4 new-project prompts, scaffolds 5 spine docs at V29 | `plugin/agents/adopt.md` (case 1) + `plugin/skills/adopt/scripts/scaffold.py` | Pass | Subagent ran `detect-case`, opened with case-1 text verbatim, walked Q1–Q4 one at a time, scaffolded CLAUDE.md / UX.md / BACKLOG.md / MANIFEST.md / TEST-LOG.md with current-version footers. |
| 073 | 2026-05-19 | V29 | Case 1: subagent pushes back on thin Q3 answer, then gracefully accepts `[FOLD-IN PENDING]` fallback | `plugin/agents/adopt.md` (case 1 Q3) + universal-behaviour rules | Pass | Thin answer ("task entry, lists, sync") → push-back about missing UX paragraphs → offered fold-in fallback → user chose scaffold-only → subagent accepted, queued 4 fold-in blocks. |
| 074 | 2026-05-19 | V29 | Case 2 (existing code, no docs): SessionStart advisory fires | `plugin/hooks/session_start.py` (V29 advisory) | Pass | Fixture had `package.json` + `src/index.js` (triggers Q2 build-manifest + recognized-source-dir). Advisory: `[no-code-method] Folder has work but isn't adopted — run /adopt to start...` |
| 075 | 2026-05-19 | V29 | Case 2: PreToolUse blocks Edit on unadopted folder with detailed deny reason | `plugin/hooks/pre_tool_use.py` (V29 unadopted-folder check) | Pass | "Try the edit anyway" stress test. Hook denied Update(src\index.js): "BLOCKED: this folder is unadopted... Run /adopt first. The five-case dialogue routes you to the right setup..." File unchanged. |
| 076 | 2026-05-19 | V29 | Case 2: gate self-clears once `.no-code-method-skip` marker present | `plugin/hooks/pre_tool_use.py` (V29 marker check) | Pass | After marker was created, retry of Edit on `src/index.js` passed through hook — Claude Code asked user-level approval (not hook deny). Verifies the marker-suppresses-gate path. |
| 077 | 2026-05-19 | V29 | PreToolUse does NOT gate Bash file writes — design observation, not bug | `plugin/hooks/pre_tool_use.py` (scope) | Pass | Claude bypassed via PowerShell `New-Item`. Threat model is accidental edits (Edit/Write tools); creative circumvention out of scope. Advisory wording narrowed in-commit. |
| 078 | 2026-05-19 | V29 | Case 3 (existing code, foreign CLAUDE.md): SessionStart advisory fires | `plugin/hooks/session_start.py` (V29 advisory) | Pass | Same generic advisory as case 2; the case-2-vs-case-3 differentiation happens inside `/adopt`'s detect-case, not in the SessionStart message. Reasonable design (keep advisory simple). |
| 079 | 2026-05-19 | V29 | Case 3 overwrite: foreign `CLAUDE.md` backed up with date suffix; fresh template scaffolded; pre-existing code untouched | `plugin/agents/adopt.md` (case 3 option 2) + `scaffold.py` | Pass | Subagent ran `cp CLAUDE.md CLAUDE.md.foreign-backup-2026-05-19` (today's date), removed original, ran write, scaffolded new CLAUDE.md / UX.md / BACKLOG.md / MANIFEST.md / TEST-LOG.md at V29. `package.json` and `src/index.js` unchanged. |
| 080 | 2026-05-19 | V29 | Case 3: subagent honors "skip questions" gracefully — no push-back, docs left at template shape | `plugin/agents/adopt.md` (case 3 four-prompt walk) | Pass | "Skip questions" mid-flow → no push-back, scaffold complete, no pre-fill. Note: skip path bypasses fold-in queueing entirely (no breadcrumb), unlike case 1. |
| 081 | 2026-05-19 | V29 | Case 4 (already method-managed, version mismatch): detect-template-state reads `user_v` from CLAUDE.md and `plugin_v` from session_start.py at runtime | `plugin/agents/adopt.md` (case 4 first-action) | Pass | Fixture had V25 footers on CLAUDE.md + 4 spine docs; plugin is V29. Subagent ran `detect-case`, then explicitly grepped `PLUGIN_METHOD_VERSION` in `${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py`, then `ls`-ed the fixture folder to enumerate spine docs. Exactly what new V29 first-action prescribes. |
| 082 | 2026-05-19 | V29 | Case 4: version-mismatch dialogue opens with new V29 text | `plugin/agents/adopt.md` (case 4 opener — V29 mismatch branch) | Pass | Mismatch dialogue opened correctly. Subagent adaptively softened "SessionStart already flagged" to "may have flagged" — good context-sensitive behaviour. |
| 083 | 2026-05-19 | V29 | Case 4 refresh: subagent over-locks `BACKLOG.md`, `MANIFEST.md`, `TEST-LOG.md` — should treat as writable per spec | `plugin/agents/adopt.md` (case 4 option 1 — refresh) | Fail | Subagent treated all spine docs as locked, routing BACKLOG/MANIFEST/TEST-LOG through fold-in. Spec says only UX.md + additional SoT docs are locked. **Fix applied in-commit:** explicit writable-vs-locked callout added to case 4. Retest owed. |
| 084 | 2026-05-19 | V29 | Case 4: main Claude correctly bumps writable footers after subagent's incomplete refresh | main Claude + `plugin/hooks/pre_tool_use.py` (V19 lock) | Pass | UX.md blocked by hook; BACKLOG/MANIFEST/TEST-LOG passed through, footers bumped. Definitively localized #083 to subagent classification, not hook. |
| 085 | 2026-05-19 | V29 | Case 4: PreToolUse V19 lock correctly scoped — only UX.md denied, other spine docs pass through | `plugin/hooks/pre_tool_use.py` (V19 check (a)) | Pass | Verified during #084. Update(UX.md) deny reason: "BLOCKED: UX.md is a locked source-of-truth doc. It is read-only to Claude (the agent); only the user can edit it, by hand during a planning session." All other path-block-declared docs (BACKLOG, MANIFEST, TEST-LOG) edited successfully. Confirms the V19 lock is scoped to UX + additional SoT docs, not all path-block entries. |
| 086 | 2026-05-19 | V29 | Case 5 (opted out): SessionStart silent when `.no-code-method-skip` marker present | `plugin/hooks/session_start.py` (V29 marker check before advisory) | Pass | Fixture had `package.json` (would trigger advisory) plus `.no-code-method-skip`. Marker correctly suppressed advisory. Standard Claude Code greeting only. |
| 087 | 2026-05-19 | V29 | Case 5: `/adopt` detects opt-out state and offers clear-marker / cancel | `plugin/agents/adopt.md` (case 5) | Pass | Dialogue matches adopt.md case 5 text verbatim. Neutral tone — opting out framed as a legitimate state, not stuck. |
| 088 | 2026-05-19 | V29 | Case 5 cancel: clean exit, no changes | `plugin/agents/adopt.md` (case 5 option 2) | Pass | Recap: "Cancelled (case 5 — folder stays opted out). No changes made." 0 tool uses. |
| 089 | 2026-05-19 | V29 | Case 4 walkthrough text visibility before any Edit | `plugin/agents/adopt.md` (case 4 option 1 — pre-edit walkthrough) | Skipped | Couldn't verify whether subagent surfaced the writable/locked walkthrough before editing — Edit diff appeared with no walkthrough visible. Investigate via transcript expansion or fresh run. |

---

## V32 — NO-CODE-METHOD.md retired from plugin runtime; subagent inlining (2026-05-20)

`claude --plugin-dir` against `v32-scratch` (Hello-screen batch). V32 claim: subagents no longer read `NO-CODE-METHOD.md` — procedures inlined, cross-cutting rules in `universal-behaviour.md`, terms in `VOCABULARY.md`.

Rows tagged `Pass (caveat)` where the NO-CODE-METHOD.md absence is inferred from behaviour (file mods, recap content) rather than directly observed — subagent tool traces aren't visible in interactive mode.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 090 | 2026-05-20 | V32 | Plugin loads via `claude --plugin-dir` from `v32-scratch` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`, `commands/`, `agents/`, `docs/`) | Pass | First V32 smoke test. `v32-scratch` scaffolded inside workspace folder by Cowork (CLAUDE.md, UX.md w/ Hello screen entry, BACKLOG.md w/ one unticked Hello batch, empty MANIFEST.md + TEST-LOG.md); ran via PowerShell. |
| 091 | 2026-05-20 | V32 | `/hooks` shows 3 hooks configured: PreToolUse (1), SessionStart (1), Stop (1) | `plugin/hooks/hooks.json` + the three hook scripts | Pass | Regression check; matches V25 #035 and V28 baseline. |
| 092 | 2026-05-20 | V32 | Planning subagent (run 1 — "Plan goodbye screen addition") does not Read `NO-CODE-METHOD.md` at session start; operates from inlined `*Procedure order*` + reads V32 split locations | `plugin/agents/planning.md` (V32 inlining) | Pass (caveat) | 4 tool uses. Behavioural evidence: posed clarifying question (consistent with inlined procedure). NO-CODE-METHOD.md absence inferred, not directly observed. |
| 093 | 2026-05-20 | V32 | Batch-executor (Hello build) does not Read `NO-CODE-METHOD.md`; reads MANIFEST + UX first, then writes `hello.html`, ticks BACKLOG, updates MANIFEST | `plugin/agents/batch-executor.md` | Pass (caveat) | 5 tool uses. File mods confirmed: hello.html written, BACKLOG ticked, MANIFEST entry added. NO-CODE-METHOD.md inference same as #092. |
| 094 | 2026-05-20 | V32 | After-build subagent (Hello build, via Stop-hook redirect) does not Read `NO-CODE-METHOD.md`; produces recap, updates MANIFEST, opens TEST-LOG row | `plugin/agents/after-build.md` (V32 inlining) | Pass (caveat) | 7 tool uses. Recap correct: `[Requested]` label preserved, test row referenced by ID, flags clean. MANIFEST + TEST-LOG row written. Inference same as #092. |
| 095 | 2026-05-20 | V32 | Planning subagent (run 2 — "Resume goodbye planning") closes test session via per-row read-back on TEST-LOG row #001; strips completed Hello batch from BACKLOG | `plugin/agents/planning.md` (V32 inlining; V27 per-row read-back) | Pass | 8 tool uses. TEST-LOG row flipped to Pass/Confirmed. Hello batch removed from BACKLOG. Loose phrasing accepted (only one pending row). |
| 096 | 2026-05-20 | V32 | Four drift checks run during planning session 2 — all clean against `v32-scratch` state | `plugin/agents/planning.md` (drift-check procedure, V22 + V27) | Pass | "Four drift passes ran clean." Regression check post-V32 inlining. |
| 097 | 2026-05-20 | V32 | Universal-behaviour push-back rule fires on principle-conflict — planning surfaces goodbye-vs-principle-1 conflict in chat | `plugin/hooks/universal-behaviour.md` (push-back rule absorbed via SessionStart additionalContext) + `plugin/agents/planning.md` | Pass | Planning surfaced "violates principle 1" reasoning rather than silently routing to batch. User dropped feature; no BACKLOG churn. Minor: spec says create batch AND surface in chat — skipping batch on immediate drop is defensible. |
| 098 | 2026-05-20 | V32 | Main Claude refuses to silently route around mid-turn dual-thread mismatch (active planning question + Stop-hook batch-executor redirect) | `plugin/hooks/universal-behaviour.md` (push-back rule) | Pass | Dual-thread collision (pending planning question + Stop-hook redirect). Main Claude surfaced three options rather than picking silently. User chose "build first." |
| 099 | 2026-05-20 | V32 | Before-build subagent V32 inlining check | `plugin/agents/before-build.md` (V32 inlining) | Skipped | No second unticked batch available. Parity reasoning from planning (#092, #095) and after-build (#094) carries — same inlining pattern. Strict trace via headless automation owed. |

---

## V34 — Git safety-guard hook (2026-05-21)

Direct Python invocation — deterministic, zero API cost.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 100 | 2026-05-21 | V34 | Hook denies `git reset --hard` — standalone and chained (`cd foo && git reset --hard`) | `plugin/hooks/pre_tool_use_git_guard.py` (RESET_HARD regex) | Pass | Both variants emit deny JSON with `permissionDecision: "deny"` and clear reason text naming the blocked command + safer alternatives. Regex bug caught pre-ship: `\b` before `--hard` silently passed because both preceding space and leading `-` are non-word characters; fixed by removing the leading `\b`. |
| 101 | 2026-05-21 | V34 | Hook denies `git push --force` and `git push -f` — standalone and chained | `plugin/hooks/pre_tool_use_git_guard.py` (PUSH_FORCE regex) | Pass | Three variants tested: `git push --force origin main`, `git push -f origin main`, chained `git commit -m msg && git push --force origin main`. All denied with correct reason text pointing at `--force-with-lease` as safer alternative. |
| 102 | 2026-05-21 | V34 | Hook allows safe git operations — `git commit`, `git tag`, `git push` (no force), `git push --force-with-lease`, `git reset --soft`, `git push origin v34` | `plugin/hooks/pre_tool_use_git_guard.py` | Pass | Six variants tested. All exit 0 with no stdout (implicit allow). Critical check: `--force-with-lease` is NOT blocked by the `--force` regex — negative lookahead `(?!-with-lease)` works correctly. |
| 103 | 2026-05-21 | V34 | Hook allows non-Bash tool calls and handles edge cases (Edit tool, empty command, malformed JSON) | `plugin/hooks/pre_tool_use_git_guard.py` (early-exit paths) | Pass | Three edge cases tested. All exit 0 with no stdout. Confirms lenient-by-default behaviour: hook only inspects Bash tool calls with non-empty command strings; everything else passes through. |

---

## V35 — E2E Taskflow test — first non-synthetic-fixture run (2026-05-21)

First plugin run against real Taskflow. Two sessions: case 1 (cold-start adoption), case 4 (refresh after real docs replaced templates). Planning subagent reached Q1 of 5 before halting — questions collided with decisions settled in Alex's separate planning project. Build/before-build/after-build not exercised.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 104 | 2026-05-21 | V35 | SessionStart safety net advisory fires on unadopted real Taskflow folder | `plugin/hooks/session_start.py` (V29 unadopted-folder detection) | Pass | `Taskflowapp/` had foreign CLAUDE.md + recognized source dirs; advisory fired correctly. First non-synthetic-fixture validation of the V29 detection. |
| 105 | 2026-05-21 | V35 | `/adopt` case 1 detection + migrate on real Taskflow with foreign CLAUDE.md | `plugin/agents/adopt.md` (case 1) + `plugin/skills/adopt/scripts/scaffold.py` | Pass | Previous-session run. Detected case 1, migrated foreign CLAUDE.md to V34 spec with fenced JSON path block, backed up original as `.foreign-backup-2026-05-21`, scaffolded BUILD-LOG.md + TEST-LOG.md under `no-code-method/`. |
| 106 | 2026-05-21 | V35 | `/adopt` sanity check refuses Windows home directory as adoption target | `plugin/agents/adopt.md` (sanity check on cwd) | Pass | Launched from `C:\Users\Alex` → subagent caught it, presented Cancel. Prevents scattering spine docs into home directory. |
| 107 | 2026-05-21 | V35 | `/adopt` case 4 refresh on real Taskflow — footer-bump on writable docs, fold-in routing on locked docs | `plugin/agents/adopt.md` (case 4 option 1 — refresh) | Pass | Bumped writable footers directly (BACKLOG, MANIFEST), routed locked docs (UX, SYSTEM-PROMPT) through fold-in. Validates V29 #083 fix on real input. |
| 108 | 2026-05-21 | V35 | Planning subagent first [SEQUENCE] question against real Taskflow planning batch | `plugin/agents/planning.md` (V22 + V27 + V32 inlining) | Skipped | Subagent opened [SEQUENCE] correctly (5 questions, Q1 presented). Halted — questions clashed with decisions already settled in Alex's separate planning project. Not a plugin bug. |

---

## V37 — Marketplace.json + local install + smoke test (2026-05-21)

First globally-installed test (`/plugin marketplace add` + `/plugin install`). Empty `~\v37-scratch`. All 7 Pass.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 109 | 2026-05-21 | V37 | `claude plugin validate .` passes clean on `.claude-plugin/marketplace.json` | `.claude-plugin/marketplace.json` | Pass | Initial run surfaced "no marketplace description" warning; description field added; second run clean. |
| 110 | 2026-05-21 | V37 | `claude plugin marketplace add ./` adds marketplace to user settings | `.claude-plugin/marketplace.json` | Pass | Output: "Successfully added marketplace: sovereign-implementer (declared in user settings)". |
| 111 | 2026-05-21 | V37 | `claude plugin install no-code-method@sovereign-implementer` installs plugin globally (scope: user) | `plugin/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` | Pass | Output: "Successfully installed plugin: no-code-method@sovereign-implementer (scope: user)". No `--plugin-dir` needed going forward. |
| 112 | 2026-05-21 | V37 | Empty-folder session (no `--plugin-dir`) opens silently — SessionStart tier 1 | `plugin/hooks/session_start.py` (tier detection) | Pass | `~\v37-scratch` is empty; tier 1 = plugin invisible. Standard Claude Code greeting only. First globally-installed SessionStart validation. |
| 113 | 2026-05-21 | V37 | `/hooks` shows 2 `[Plugin]` PreToolUse hooks: `Bash` (git guard) and `Edit\|Write\|MultiEdit\|Task` (locked-doc + boundary enforcement) | `plugin/hooks/hooks.json` + `pre_tool_use.py` + `pre_tool_use_git_guard.py` | Pass | 4 total hooks (2 plugin + 2 user settings). SessionStart/Stop don't appear in `/hooks` UI — differs from `--plugin-dir` (#035, #091). |
| 114 | 2026-05-21 | V37 | `/adopt` fires case 1 on empty folder — scaffold detection + first prompt delivered | `plugin/agents/adopt.md` (case 1) + `plugin/skills/adopt/scripts/scaffold.py` | Pass | Subagent ran `detect-case`, correctly identified empty folder, opened with "I'll ask you four quick questions" and presented Q1 (project context). First globally-installed subagent invocation. |
| 115 | 2026-05-21 | V37 | `/reload-plugins` loads full plugin surface without restart | plugin (all components) | Pass | Output: "Reloaded: 1 plugin · 2 skills · 11 agents · 4 hooks · 0 plugin MCP servers · 0 plugin LSP servers". Confirms filesystem-based reload mechanism works for globally-installed plugin. |

---

## V39 — MANIFEST paths field + read-before-edit gate (2026-05-21)

Direct hook-script invocation against Python-built fixture. Validates read-before-edit gate: paths-field parsing (three shapes), MANIFEST → target matching, deny, transcript-scan retry, spine-doc exemption. All 7 Pass.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 116 | 2026-05-21 | V39 | Edit on a file matching a MANIFEST entry's single-file `(path)` field is denied with V39 marker | `pre_tool_use.py` → `check_read_before_edit` + `parse_manifest_entries` | Pass | Fixture `MANIFEST.md` had `- **TaskCard** (\`app/TaskCard.kt\`) — ...`; Edit on `app/TaskCard.kt` denied with `BLOCKED [V39 read-before-edit]` marker present in stdout. |
| 117 | 2026-05-21 | V39 | Edit on a file matching a MANIFEST entry's multi-file list `(path1, path2)` shape is denied | `pre_tool_use.py` → `parse_manifest_entries` + `_path_matches_entry_path` | Pass | Fixture entry `(\`app/notifications/Service.kt\`, \`app/notifications/Channels.kt\`)` — Edit on `Service.kt` matched and denied. |
| 118 | 2026-05-21 | V39 | Edit on a file under a MANIFEST entry's directory-prefix `(dir/)` is denied | `pre_tool_use.py` → `_path_matches_entry_path` (trailing-slash branch) | Pass | Fixture entry `(\`app/settings/\`)` — Edit on `app/settings/AccountScreen.kt` matched via directory-prefix rule and denied. |
| 119 | 2026-05-21 | V39 | Edit on a file not named in any MANIFEST entry is allowed (no false denial) | `pre_tool_use.py` → `check_read_before_edit` (no-match branch) | Pass | Edit on `somewhere_not_listed.kt` — gate returned None, hook emitted nothing, exit 0. Confirms the gate only fires on covered files. |
| 120 | 2026-05-21 | V39 | MANIFEST entry without a `(path)` field is silently skipped by the gate (legacy / incremental migration) | `pre_tool_use.py` → `manifest_entry_covers_file` (empty paths) | Pass | Fixture had `- **LegacyComponent** — Old component, no path field yet.`; Edit on an unrelated file allowed. Confirms `entry.paths == []` → skipped. |
| 121 | 2026-05-21 | V39 | Spine-doc target (MANIFEST.md itself) is exempt from the V39 gate even if accidentally listed | `pre_tool_use.py` → `check_read_before_edit` (`V39_EXEMPT_LOGICAL_NAMES` check) | Pass | Edit on `MANIFEST.md` allowed regardless of whether MANIFEST coincidentally had a matching entry. Defensive guard against build-cycle deadlock. |
| 122 | 2026-05-21 | V39 | Retry after first deny succeeds via transcript scan (block-once semantics, no state file) | `pre_tool_use.py` → `transcript_shows_prior_v39_deny` | Pass | Wrote a fake transcript file containing `BLOCKED [V39 read-before-edit]: <abs path>`; subsequent Edit on the same file allowed. Confirms the marker line is what the retry check matches on. |

---

## V42 — Drift check 1 (direct-edit detection) smoke test (2026-05-21)

`claude --plugin-dir` against `~\v42-scratch`. Full adopt → plan → before-build → build → tag → manual-edit → reopen-planning loop. Plugin v0.40.0.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 123 | 2026-05-21 | V42 | Drift check 1 detects uncommitted manual edit to `index.html` (hello → goodbye) after `git tag v1`, surfaces per-file confirmation walk | `plugin/agents/planning.md` (drift check 1 — direct-edit detection) | Pass | Full loop: adopt → plan → build → tag → manual Notepad edit outside Claude → new session → planning. Subagent diffed against tag, found change, asked per-file confirmation. Shape matches spec. |

---

## 0068 — E2E round 2: Taskflow build cycle (2026-05-24)

Full build cycle against real Taskflow (batch 0001 — Project skeleton and Room data model). Plugin v0.60.0 installed via desktop app zip upload. 22 build batches pre-planned in BACKLOG.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 124 | 2026-05-24 | 0068 | Desktop app zip install: plugin packaged as zip, uploaded via Customise → + → Upload, version 0.60.0 confirmed | plugin scaffold (`.claude-plugin/plugin.json`) | Pass | First zip-upload install. `Compress-Archive -Path plugin\* -DestinationPath sovereign-implementer-plugin.zip`. "Legacy commands/format" warning resolved by migrating commands/ to skills/*/SKILL.md. |
| 125 | 2026-05-24 | 0068 | Skills migration: before-build and build moved from commands/ to skills/*/SKILL.md format | `plugin/skills/before-build/SKILL.md`, `plugin/skills/build/SKILL.md` | Pass | Legacy warning eliminated. No references to commands/ found in plugin. |
| 126 | 2026-05-24 | 0068 | Planning subagent correctly identifies already-planned feature (drag-target delete zone) and declines to create duplicate batch | `plugin/agents/planning.md` | Pass | Matched to UX.md "Drag-target icons" and batch 0010. 31.6k tokens / 1m 58s — quality good, cost too high. |
| 127 | 2026-05-24 | 0068 | Planning subagent pushes back on nonsensical feature request (upside-down phone button) with technical explanation | `plugin/agents/planning.md` + `universal-behaviour.md` (push-back rule) | Pass | "That doesn't make sense as a feature. Phone OSes handle screen rotation." Asked if user was testing push-back. |
| 128 | 2026-05-24 | 0068 | Before-build locks batch 0001: 19 files, 11 tests, all Claude-verified, notes template-file side effects | `plugin/agents/before-build.md` + `plugin/skills/before-build/SKILL.md` | Pass | 10.6k tokens. Clean output, correct structure. |
| 129 | 2026-05-24 | 0068 | Stop hook auto-chains before-build → build without waiting for user to invoke `/build` | `plugin/hooks/stop.py` (batch-executor redirect) | **Fail** | Before-build said "Next step: run /build when you're ready." Stop hook fired, found unticked files, redirected to batch-executor. User never invoked /build. Fix: check whether any files are ticked — zero ticked = just locked (exit silent). |
| 130 | 2026-05-24 | 0068 | Prerequisite carve-out: batch executor halts on missing TaskflowApplication manifest registration | `plugin/agents/batch-executor.md` (prerequisite carve-out) | Pass | Halted, surfaced justification, got approval, respawned with fix. Pattern worked as designed. |
| 131 | 2026-05-24 | 0068 | Build completes: 20 files written and ticked (19 planned + 1 prerequisite) | `plugin/agents/batch-executor.md` | Pass | ~165k tokens / 12m+. Build itself succeeded. |
| 132 | 2026-05-24 | 0068 | After-build edits source code to fix build failure (duplicate kotlin.android plugin) — out of scope for after-build | `plugin/agents/after-build.md` | **Fail** | After-build's job is recap + MANIFEST + TEST-LOG. It diagnosed a Kotlin plugin conflict and edited gradle files, triggering a cascading failure. Must not touch source code. |
| 133 | 2026-05-24 | 0068 | After-build cascading fix: gradle fix → new error → undo → redo → dead file deletion → theme fix → cache locks → stuck | `plugin/agents/after-build.md` | **Fail** | 6+ minutes of cascading repairs. Each fix created the next problem. Ended stuck on Android Studio file locks asking user for help. |
| 134 | 2026-05-24 | 0068 | After-build overrides explicit user refusal to delete dead template files | `plugin/agents/after-build.md` + `universal-behaviour.md` | **Fail** | User declined deletion ("Why should they be deleted?"). After-build backed off. Later, its own fix cascade broke dependencies, making files cause compile errors — deleted them without re-asking. Consent violation. |
| 135 | 2026-05-24 | 0068 | No session-open status summary visible to user (batch count, next batch, what it involves) | `plugin/hooks/session_start.py` | **Fail** | SessionStart injects context for Claude but nothing user-facing. User expectation: rundown of state + "would you like to build it?" on every session open. |
| 136 | 2026-05-24 | 0068 | Claude asks user to run PowerShell command (set JAVA_HOME) instead of running it itself | `universal-behaviour.md` (plain English rule) | **Fail** | User told it to do it itself; it complied. Rule gap: no guidance on running vs. asking for system commands. |

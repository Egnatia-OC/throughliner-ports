# TEST-LOG.md — Smoke test record (this project)

Record of every smoke-test check run against the plugin. One row per check per session. Newest at bottom — ID order matters more than recency.

*Status*: `Pass`, `Fail`, or `Skipped` (reason in *Notes*). Status is never edited — regressions append new rows; the historical record stays intact.

`Superseded` only when a component changes enough that the original test no longer makes sense. Old row flips to `Superseded` with a note naming the session that changed it; new rows record the retest.

Full entry-shape spec in `BUILD-METHOD.md` → *TEST-LOG entry shape*.

---

## V18–V22 — backfilled from BUILD-LOG (2026-05-16)

Reconstructed from BUILD-LOG.md "What shipped" + pivot/surprise sections. Pre-dates live discipline (V24).

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

CLI smoke tests via outputs/ workaround (Cowork bash-mount staleness). Pre-validation tier; Windows integration in `claude --plugin-dir` still owed (deferred to Alex's PowerShell session, post-V25 commit).

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 031 | 2026-05-16 | V25 | `parse_backlog.py` CLI: 15-scenario suite covering top-batch detection, change_list parsing, Files: tick-state, Serves line extraction, prerequisite labels, malformed-input lenience | `plugin/scripts/parse_backlog.py` | Pass | 15/15. Pre-validation tier (CLI). outputs/ workaround. Windows retest owed. |
| 032 | 2026-05-16 | V25 | Stop hook end-to-end CLI: 8-scenario suite covering empty backlog, single-batch redirect, post-completion next-batch redirect, `stop_hook_active` loop prevention, parser-error lenience | `plugin/hooks/stop.py` (+ `parse_backlog.py`) | Pass | 8/8. Pre-validation. Loop-exit (Opus risk #2) verified. outputs/ workaround. Windows retest owed. |
| 033 | 2026-05-16 | V25 | PreToolUse boundary check (V25 (c)) + V19 (a)/(b) read-only and V22 (e) Serves-line regression: 9-scenario suite | `plugin/hooks/pre_tool_use.py` | Pass | 9/9. Pre-validation. New (c) blocks edits outside Files: and allows prerequisite-labeled files; V19/V22 checks still pass. outputs/ workaround. Windows retest owed. |

---

## V25 — Windows integration smoke test (2026-05-17)

Run from fresh PowerShell on Alex's Windows machine via `claude --plugin-dir <path-to-sovereign-implementer/plugin>`. Pre-populated `v25-scratch` inside Cowork-accessible parent (earlier `~\v25-scratch` abandoned — outside Cowork access). Three Fail rows = real V25 bugs; fix-shape OPEN-QUESTIONS entries logged for V26.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 034 | 2026-05-17 | V25 | Plugin loads via `claude --plugin-dir` from `v25-scratch` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`, `commands/`, `agents/`) | Pass | Windows integration tier; deferred from session resume. |
| 035 | 2026-05-17 | V25 | `/hooks` shows 3 hooks configured: PreToolUse (1), SessionStart (1), Stop (1) | `plugin/hooks/hooks.json` + the three hook scripts | Pass | Header confirms exact V25 expectation; other hook types show no count. |
| 036 | 2026-05-17 | V25 | `/agents` Library shows 3 plugin subagents (planning, before-build, batch-executor) | `plugin/agents/*.md` | Pass | Listed as `no-code-method:batch-executor`, `before-build`, `planning` — all "inherit" model. Library tab = canonical registry; Agents tab = current-conversation invocations only. |
| 037 | 2026-05-17 | V25 | Both V25 slash commands registered, accessible via `/no-code-method:before-build` and `/no-code-method:build` | `plugin/commands/*.md` | Pass | Bare names don't auto-resolve — `/no-code-method:` prefix required for commands-directory pattern. `/init-project` (skill-with-flags) auto-shortens; new commands don't. Worth noting; not blocking. |
| 038 | 2026-05-17 | V25 | SessionStart tier-1 silent in empty `v25-scratch` (initial launch, before pre-population) | `plugin/hooks/session_start.py` (tier detection) | Pass | Empty folder → tier 1, no `additionalContext`. V21 regression coverage. |
| 039 | 2026-05-17 | V25 | SessionStart tier-3 emit in configured `v25-scratch` (pre-populated CLAUDE.md + spine docs with V25 footers) | `plugin/hooks/session_start.py` (tier detection + foundational reads) | Pass | Verified indirectly: `/no-code-method:before-build` had context it needed (CLAUDE.md path block, BACKLOG.md state, UX.md entries). No project-confusion from main Claude. |
| 040 | 2026-05-17 | V25 | V19 PreToolUse hook still blocks UX.md writes with deny-and-redirect message | `plugin/hooks/pre_tool_use.py` (V19 (a) + (b)) | Pass | Regression check. During pre-restart `/init-project`: Write(UX.md) → PreToolUse deny with canonical "UX.md is locked" + FOLD-IN PENDING redirect → Claude wrote real fold-in block to BACKLOG.md. |
| 041 | 2026-05-17 | V25 | Stop hook misfires on template-placeholder BACKLOG.md (fires immediately after `/init-project` scaffolds, redirects with literal placeholder payload as if a real batch) | `plugin/hooks/stop.py` (+ `plugin/scripts/parse_backlog.py` placeholder detection gap) | **Fail** | Real V25 bug. Parser sees BACKLOG-TEMPLATE.md's example batch (`[short descriptive name]`, etc.) as real unticked batch; Stop hook redirects with placeholder JSON payload. Main Claude refused — soft discipline saved it, hook is wrong. V26 fix: parser detects bracketed-placeholder pattern → returns `{}`. See `planning/OPEN-QUESTIONS.md`. |
| 042 | 2026-05-17 | V25 | BACKLOG-TEMPLATE.md's instructional canonical-format example block uses the literal `[FOLD-IN PENDING]` marker | `templates/BACKLOG-TEMPLATE.md` + `plugin/templates/BACKLOG-TEMPLATE.md` | **Fail** | Parallel to #041 — instructional template uses real marker, making real fold-ins indistinguishable from example via marker search. V26 fix: visually distinguishable example (code fence) + relocate canonical-format docs to DOC-STRUCTURE.md. See `planning/OPEN-QUESTIONS.md`. |
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

Windows smoke tests owed for V27 code (per V27 BUILD-LOG carry-forward). 8/13 ran (6 Pass, 1 Fail, 1 partial Pass with caveat); 5 Skipped pending AB2 lock-bug fix. Tiers: G1–G3 direct hook-script (PowerShell heredoc `@'…'@ | python pre_tool_use.py`); G4/G5/P1/AB2 `claude --plugin-dir` against `v27-smoke-fixtures/g4`; D1 direct Read of DOC-STRUCTURE.md. Three V27 bugs — see top of `planning/OPEN-QUESTIONS.md`.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 051 | 2026-05-17 | V27 | D1 — `DOC-STRUCTURE.md` carries the *Change list — `[Requested]`/`[Suggested]` labels* sub-section under *Build batches* | `DOC-STRUCTURE.md` | Pass | Read of line 119 — bolded paragraph with labels-on-changes-not-files rule, planning/before-build/after-build chain, carve-out-labels note. Matches V27 BUILD-LOG Decision 1 (Q3 placement). |
| 052 | 2026-05-17 | V27 | G4 — PreToolUse check (f) permits Task → batch-executor when TEST-LOG has no unconfirmed previous-session rows | `plugin/hooks/pre_tool_use.py` (V27 check (f)) | Pass | Fixture had all rows `Confirmed Explicitly: Yes`. `/no-code-method:build` → Task → batch-executor; gate allowed silently; subagent proceeded into per-file work. |
| 053 | 2026-05-17 | V27 | G1 — Gate denies Task → batch-executor when TEST-LOG has unconfirmed rows and BUILD-LOG is parseable (narrowed mode) | `plugin/hooks/pre_tool_use.py` (V27 check (f), BUILD-LOG-narrowed path) | Pass | Direct hook invocation (heredoc → stdin → python). Deny JSON identified session `v26` from BUILD-LOG.md, named both unconfirmed rows (#001, #002) + components, surfaced canonical "BLOCKED: cannot start a new build batch..." reason. Caveat: parallel `claude --plugin-dir` attempt showed batch-executor running via Stop-hook redirect with no visible deny — see OPEN-QUESTIONS Stop-hook-vs-tripwire. Script-level gate works; Claude-Code-wiring layer uncertain. |
| 054 | 2026-05-17 | V27 | G2 — Gate denies in strict fallback when `BUILD-LOG.md` is missing | `plugin/hooks/pre_tool_use.py` (V27 check (f), strict-fallback path) | Pass | After `Remove-Item BUILD-LOG.md`. Deny JSON: "BUILD-LOG.md not found — strict fallback mode: any `Confirmed Explicitly: No` blocks", fix advice (path block / root), both rows enumerated. Distinguishable from G1 wording. |
| 055 | 2026-05-17 | V27 | G3 — Gate denies in strict fallback when `BUILD-LOG.md` present but unparseable | `plugin/hooks/pre_tool_use.py` (V27 check (f), strict-fallback path, unparseable variant) | Pass | Fixture: BUILD-LOG.md with only `#`/`###` headings (no `## <token>`). Deny JSON: "present but unparseable — no `## <session-tag>` heading at top", strict-fallback mode, fix advice (`expected ## <tag> ... newest first`). Distinguishable from G2 wording. |
| 056 | 2026-05-17 | V27 | G5 — SessionStart tripwire fires when previous-batch TEST-LOG rows are unconfirmed; routes main Claude to planning subagent regardless of opener | `plugin/hooks/session_start.py` (V27 TEST-LOG tripwire) | Pass | Verified during G1 attempt. Main Claude opened: "I can't run /build right now — SessionStart hook flagged previous batch's test session (v26) open with two unconfirmed rows" and routed to planning subagent instead of /build's flow. Tripwire surfaced + was acted on. Part (b) — tripwire absent when all confirmed — implicitly verified by G4. |
| 057 | 2026-05-17 | V27 | P1 — Planning subagent leads with first pending row (per-row read-back) as first sub-step of *During planning* | `plugin/agents/planning.md` (V27 extension — Rule 2) | Pass | Verified during G1 attempt. Planning subagent invoked via tripwire-routing override; asked "Row #001 — Pending row one... — Pass, Fail, or Skipped?" by name. Specific-row read-back shape confirmed. Caveat: "advances to next row" half not exercised — turn ended on question, Stop-hook bug derailed next turn before answer. |
| 058 | 2026-05-17 | V27 | AB2 — after-build subagent appends blank-Status rows to `TEST-LOG.md` when opening a test session | `plugin/agents/after-build.md` (test-session-open step) + `plugin/hooks/pre_tool_use.py` (V19 check (a)) | Fail | **Critical V27 bug.** Found during G4 follow-on (Stop hook auto-redirected to after-build after last file ticked). After-build attempted Write(TEST-LOG.md); V19 check (a) denied — TEST-LOG.md is in CLAUDE.md path block but NOT in `WRITABLE_LOGICAL_NAMES = {"BACKLOG.md", "MANIFEST.md"}` at `pre_tool_use.py:103`. After-build correctly halted rather than mis-route to fold-ins (subagent diagnosis: fold-ins are mid-build edits to locked spine docs, not test-session-open). One-line fix: add `"TEST-LOG.md"` to `WRITABLE_LOGICAL_NAMES`. Without it, V27 gate is structurally inert. See OPEN-QUESTIONS. |
| 059 | 2026-05-17 | V27 | AB1 — after-build subagent silently updates `MANIFEST.md` for created/renamed/deleted elements | `plugin/agents/after-build.md` (MANIFEST silent update step) | Skipped | Blocked by AB2 (#058). After-build halted; diagnostic reported "decided no MANIFEST.md entry warranted (trivial placeholder)" but couldn't progress past TEST-LOG write to verify silent-update in non-trivial case. Retest after fix. |
| 060 | 2026-05-17 | V27 | AB3 — after-build recap labels `[Requested]` / `[Suggested]` from BACKLOG.md change-list bullets | `plugin/agents/after-build.md` (recap shape, label-read pass) | Skipped | Blocked by AB2 (#058). After-build halted before recap. Retest after fix. |
| 061 | 2026-05-17 | V27 | P2 — Planning subagent pushes back on bulk confirmations during read-back | `plugin/agents/planning.md` (V27 extension — per-row enforcement, "Never infer completion") | Skipped | Depends on after-build successfully opening test session via TEST-LOG writes. AB2 (#058) blocks natural setup. Retest after fix; alternatively testable with hand-crafted fixture rows (G1 style). |
| 062 | 2026-05-17 | V27 | L1 — Planning subagent writes `[Requested]` / `[Suggested]` labels inline on BACKLOG.md change-list bullets | `plugin/agents/planning.md` (V27 extension — inline label-writing) | Skipped | Deferred to post-fix retest. Claude Code wiring issues this session (Stop-hook-vs-tripwire conflict, gate visibility on redirect) make subagent runs fragile. |
| 063 | 2026-05-17 | V27 | L2 — before-build subagent preserves `[Requested]` / `[Suggested]` labels across halt-C re-batching splits | `plugin/agents/before-build.md` (label-preservation rule) | Skipped | Deferred to post-fix retest. Needs fixture engineered for halt-C verification-burden split; fragile against this session's wiring issues. |

---

## V28 — V27 fix sweep + helpers extraction (2026-05-18)

Live `claude --plugin-dir` smoke testing of V28's fixes. Fresh fixture rebuild — `v27-smoke-fixtures/g4` had been cleared between V27 and V28, recreated this session via Cowork Write tool with minimal CLAUDE.md, UX.md, BACKLOG.md (one fully-ticked batch), MANIFEST.md, TEST-LOG.md (empty header), BUILD-LOG.md (with `## v27` heading for session-narrowing), plus the `index.html` artefact. Two-session run: (1) `claude --plugin-dir` → "hi" → Stop hook → after-build subagent → MANIFEST update + recap + TEST-LOG row opened; (2) `/exit` + restart → SessionStart tripwire → planning subagent read-back → "Pass" recorded → test session closed + drift checks clean. All rows Pass; one caveat on #069 (Stop-hook silent-exit not uniquely distinguished from natural fallthrough in this scenario — see notes).

Three of the five V27 Skipped rows are unblocked here: AB1 (#059) and AB3 (#060) implicitly retested via the after-build flow (new Pass rows #065, #066); P1 (#057) regression-checked post-refactor (#068). The remaining three (P2 #061, L1 #062, L2 #063) need narrower fixtures and remain Skipped.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 064 | 2026-05-18 | V28 | AB2 retest — after-build writes blank-Status rows to `TEST-LOG.md` when opening a test session (the V19-check-(a) fix) | `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES += "TEST-LOG.md"`) + `plugin/agents/after-build.md` | Pass | Live `claude --plugin-dir` against rebuilt g4. After Stop-hook redirect to after-build, subagent's Write(TEST-LOG.md) succeeded — no deny — and row #001 landed with blank Status, `Confirmed Explicitly: No`. Flipping V27's #058 Fail. The keystone fix demonstrated end-to-end. |
| 065 | 2026-05-18 | V28 | AB1 retest — after-build silently updates `MANIFEST.md` for created elements | `plugin/agents/after-build.md` (MANIFEST silent update step) | Pass | Same `claude --plugin-dir` run. After-build added `- **Hello screen** — single-page index.html that renders the word "hello"...` to MANIFEST.md (alphabetical, single-line, plain English). Flipping V27's #059 Skipped. |
| 066 | 2026-05-18 | V28 | AB3 retest — after-build recap labels `[Requested]` / `[Suggested]` from BACKLOG.md change-list bullets | `plugin/agents/after-build.md` (recap shape, label-read pass) | Pass | Same run. Recap's "What shipped" section: `- [Requested] Created index.html — a single HTML page that renders the word "hello"...`. Label propagated from BACKLOG. Flipping V27's #060 Skipped. |
| 067 | 2026-05-18 | V28 | SessionStart tripwire fires post-refactor (V27 #056 regression check after V28 helpers extraction) | `plugin/hooks/session_start.py` (TEST-LOG tripwire) + `plugin/scripts/project_state.py` (extracted helpers) | Pass | Run 2 (`/exit` + restart in same fixture with unconfirmed row #001 from run 1). Main Claude opened by invoking `no-code-method:planning(Close pending test session)` rather than greeting back conversationally. Confirms the refactor of `get_unconfirmed_previous_session_rows` into `project_state.py` is faithful to V27 behaviour. |
| 068 | 2026-05-18 | V28 | Planning subagent per-row read-back post-refactor (V27 #057 regression check) | `plugin/agents/planning.md` (V27 extension — Rule 2) | Pass | Same restart. Planning asked "Before we get to your question — 1 pending test from session v27 to confirm. First: open index.html in a browser and confirm the word 'hello' appears centered both vertically and horizontally in the viewport — Pass, Fail, or Skipped?" Specific-row read-back shape preserved post-refactor. The full "advances after answer" path also verified (next row + close-out — see #070). |
| 069 | 2026-05-18 | V28 | Stop hook exits silent when previous-batch test session is open (V28 stop.py fix) | `plugin/hooks/stop.py` (V28 `is_test_session_open` check before `run_parser`) + `plugin/scripts/project_state.py` | Pass (caveat) | After planning's turn ended asking about row #001, Stop hook fired and exited silent — no redirect, no UI indicator. V28 `is_test_session_open` returned True given the unconfirmed row. **Caveat:** the bug-trigger scenario (unticked batch in BACKLOG simultaneous with unconfirmed rows) wasn't replicated — fixture's batch was fully ticked, so `run_parser` would have returned empty even without V28's check, yielding silent exit via natural fallthrough. V28's check fired in the right direction; uniquely-V28-distinguishing test (unticked batch + unconfirmed rows) is owed as a direct hook-script test in a follow-up if doubt arises. Mechanical inspection of the one-line fix supports Pass. |
| 070 | 2026-05-18 | V28 | Planning subagent records Pass + closes test session via Edit on `TEST-LOG.md` | `plugin/agents/planning.md` (read-back close-out) + `plugin/hooks/pre_tool_use.py` (V28 `WRITABLE_LOGICAL_NAMES` applies to Edit too) | Pass | After user typed "Pass", planning subagent ran 8 tool uses (~110s) including Read(BACKLOG.md), Read(MANIFEST.md), Edit(TEST-LOG.md). Edit flipped row #001's Status to `Pass` and Confirmed Explicitly to `Yes (2026-05-18)`. Then announced: "Recorded Pass on TEST-LOG row #001... v27 test session closed. Drift checks across UX.md / MANIFEST.md / TEST-LOG.md all clean..." Demonstrates Edit (not just Write) goes through the same V28 fix path. |

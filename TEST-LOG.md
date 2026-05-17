# TEST-LOG.md — Smoke test record (this project)

The project's record of every smoke-test check that has run against the plugin. One row per distinct check per session. Newest at the bottom — TEST-LOG is queried for "is X tested?", and ID order matters more than recency.

Each row's *Status* is `Pass`, `Fail`, or `Skipped` (with reason in *Notes*). Status doesn't get edited — if a later session shows a Pass check failing, a new row is appended with `Fail` and today's session; when the regression is fixed, another row with `Pass`. The historical record stays intact.

`Superseded` is used only when a component changes substantially enough that the original test description no longer makes sense against the new shape. The old row's Status flips to `Superseded` with a note naming the session that changed the component; new rows then record the retest.

The full entry-shape spec, including the BUILD-LOG cross-reference convention, lives in `BUILD-METHOD.md` → *TEST-LOG entry shape*.

---

## V18–V22 — backfilled from BUILD-LOG (2026-05-16)

These rows were reconstructed from the BUILD-LOG.md "What shipped" paragraphs and pivot/surprise sections. Pre-dates the live discipline that came in V24.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 001 | 2026-05-12 | V18 | Plugin loads via `claude --plugin-dir <path>` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`) | Pass | First-ever plugin smoke test. |
| 002 | 2026-05-12 | V18 | `/hooks` shows `SessionStart` registered after plugin load | `hooks/hooks.json` + `hooks/session_start.py` | Pass | |
| 003 | 2026-05-12 | V18 | Claude recites the eight universal-behaviour rules verbatim when asked at session start | `hooks/universal-behaviour.md` (via `SessionStart` additionalContext injection) | Pass | Confirms the hook's stdout reaches the conversation context. |
| 004 | 2026-05-13 | V19 | Plugin loads in scratch directory | plugin scaffold | Pass | |
| 005 | 2026-05-13 | V19 | Both `SessionStart` and `PreToolUse` hooks registered after load | `hooks/hooks.json` | Pass | |
| 006 | 2026-05-13 | V19 | `/init-project` scaffolds the four templates cleanly into an empty directory | `plugin/skills/init-project/` + `plugin/templates/` | Pass | |
| 007 | 2026-05-13 | V19 | `/init-project` refuses on a non-empty target directory with a clear error | `plugin/skills/init-project/scripts/scaffold.py` (recursive scan) | Pass | Tested in sandbox with `/tmp/scaffold_test2/docs/UX.md`; refused with exit code 2. |
| 008 | 2026-05-13 | V19 | `PreToolUse` hook blocks `Edit(UX.md)` with deny message visible to Claude | `hooks/pre_tool_use.py` | Pass | Stress-tested with explicit "attempt the edit anyway" instruction; deny worked. |
| 009 | 2026-05-13 | V19 | Claude pivots to add `[FOLD-IN PENDING]` block to `BACKLOG.md` after `UX.md` edit denial | `hooks/pre_tool_use.py` (deny message redirect text) | Pass | Worked as designed; Claude read the redirect and followed it. |
| 010 | 2026-05-13 | V19 | `BACKLOG.md` edit proceeds unblocked (post-pivot, since `BACKLOG.md` isn't locked) | `hooks/pre_tool_use.py` (matcher scope check) | Pass | |
| 011 | 2026-05-13 | V19 | `${CLAUDE_PLUGIN_ROOT}` expands correctly inside a skill body on Windows | `plugin/skills/init-project/SKILL.md` | Pass | Resolved the V19 plan's uncertainty in one try; expanded to full Windows path. |
| 012 | 2026-05-13 | V19 | Skill frontmatter shape produces a working slash command at `/no-code-method:init-project` | `plugin/skills/init-project/SKILL.md` (`disable-model-invocation: true`, `user-invocable: true`) | Pass | |
| 013 | 2026-05-13 | V19 | V18 universal-behaviour rules self-police a placeholder edit *before* `PreToolUse` fires | `hooks/universal-behaviour.md` content | Pass | Claude refused the placeholder add citing the UX.md "no placeholders" rule, before the hook even ran. Rules are doing soft work beyond the hook backstop. |
| 014 | 2026-05-13 | V19 | Windows subfolder-conflict in `/init-project` recursive scan | `plugin/skills/init-project/scripts/scaffold.py` | Skipped | Reason: validated equivalent path in Linux sandbox (`pathlib.rglob`'s `name` matching is platform-agnostic). Skipping the Windows-specific test recorded as conscious choice in V19 BUILD-LOG carried forward. |
| 015 | 2026-05-14 | V21 | Plugin loads via `claude --plugin-dir <path>` in `~\v21-scratch` | plugin (V21 state) | Pass | |
| 016 | 2026-05-14 | V21 | `/hooks` confirms `SessionStart` + `PreToolUse` both registered | `hooks/hooks.json` | Pass | |
| 017 | 2026-05-14 | V21 | Empty-folder session emits tier 1 (silent — no `additionalContext` injected) | `hooks/session_start.py` (tier detection) | Pass | Behaviour change from V18; verified V21's narrower scope. |
| 018 | 2026-05-14 | V21 | `/init-project` scaffolds four templates cleanly (V21 templates, post-footer bump) | `plugin/skills/init-project/` | Pass | |
| 019 | 2026-05-14 | V21 | Fresh Claude Code session against scaffolded folder fires tier 3 | `hooks/session_start.py` (tier detection + foundational reads) | Pass | |
| 020 | 2026-05-14 | V21 | Tier-3 emit: path block resolves 3 of 3 declared SoT doc paths | `hooks/session_start.py` (path block parser) | Pass | |
| 021 | 2026-05-14 | V21 | Tier-3 emit: template state detected in all four spine docs | `hooks/session_start.py` (template-state detector) | Pass | All four spine docs had `[Project Name]` placeholder intact. |
| 022 | 2026-05-14 | V21 | Tier-3 emit: routing reminder present in additionalContext | `hooks/session_start.py` (routing reminder text) | Pass | |
| 023 | 2026-05-14 | V21 | Version-footer mismatch tripwire detects out-of-sync footer | `hooks/session_start.py` (footer comparison vs. `PLUGIN_METHOD_VERSION`) | Pass | Surfaced a real bug — the `plugin/templates/*.md` footers had been missed during this session's V20→V21 bump. Tripwire paid for itself. |
| 024 | 2026-05-14 | V21 | Tier-2 detection on a method-shaped folder with partial structure | `hooks/session_start.py` (tier-2 detector + 4 sub-cases) | Skipped | Reason: the mid-smoke-test tripwire catch already exercised the structural-mismatch code path end-to-end. Per V21 BUILD-LOG: "revisit only if real-world tier-2 misfires surface in V22+ usage." |
| 025 | 2026-05-14 | V22 | Planning subagent invoked in Taskflow via auto-delegation | `plugin/agents/planning.md` (subagent body + auto-delegation description) | Pass | Subagent fired and produced a recap; surfaced the INVENTORY ghost-command issue (#026 below). |
| 026 | 2026-05-14 | V22 | INVENTORY shipped/unshipped annotations correct | `planning/INVENTORY.md` (slash-commands list) | Fail | Smoke test surfaced INVENTORY listing future slash commands (`/migrate`, etc.) as if shipped; subagent confidently recommended Alex run `/migrate` (which doesn't ship until V27). Fixed in the same V22 commit by annotating every entry "Shipped Vxx" or "Pending Vxx" and adding a top-of-section preface. See #027. |
| 027 | 2026-05-14 | V22 | INVENTORY shipped/unshipped annotations correct (post-fix retest) | `planning/INVENTORY.md` | Pass | After the in-session annotations fix. |
| 028 | 2026-05-14 | V22 | V21 SessionStart hook tier-2 detection on Taskflow | `hooks/session_start.py` (tier detection) | Pass | Per V22 BUILD-LOG: "V21's SessionStart hook correctly classified the project as tier 2 and main Claude correctly read the gap flag and declined to auto-route to planning." |
| 029 | 2026-05-14 | V22 | Serves-line PreToolUse deny on broken entry name | `hooks/pre_tool_use.py` (V22 Serves-line check) | Skipped | Reason: Taskflow is tier 2; full auto-route + Serves-line flow requires tier 3. Attempt to pivot to a fresh v22-scratch folder ran into side-quests (Alex initially invoked `/init-project` from Taskflow's session by mistake; loop-detection menu appeared on third invocation). Resolved by closing Taskflow's session and starting fresh in empty folder, but the explicit deny test wasn't completed. |
| 030 | 2026-05-14 | V22 | Serves-line PreToolUse accept on case-insensitive match | `hooks/pre_tool_use.py` (V22 Serves-line check) | Skipped | Reason: same as #029 — Taskflow tier 2, v22-scratch run incomplete. |

---

## V23 — no testable code (2026-05-17)

V23 was a Cowork-mentions-strip across method docs and plugin component bodies. No behavioural code change. No smoke test required; no rows.

---

## V24 — TEST-LOG creation + BUILD-METHOD doc

This session creates TEST-LOG.md itself and adds BUILD-METHOD.md as a peer to BUILD-LOG.md. Dev-internal-only changes. No smoke test of plugin behaviour required; no rows.

---

## V25 — Build orchestration core (2026-05-16)

CLI smoke tests run via outputs/ workaround copies for Cowork bash-mount staleness. Pre-validation tier — Windows integration smoke test in `claude --plugin-dir` still owed (deferred to Alex's PowerShell session, post-V25 commit).

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 031 | 2026-05-16 | V25 | `parse_backlog.py` CLI: 15-scenario suite covering top-batch detection, change_list parsing, Files: tick-state, Serves line extraction, prerequisite labels, malformed-input lenience | `plugin/scripts/parse_backlog.py` | Pass | 15/15. Pre-validation tier (CLI run, not Claude Code smoke test). outputs/ workaround for Cowork bash-mount staleness. Windows integration retest owed. |
| 032 | 2026-05-16 | V25 | Stop hook end-to-end CLI: 8-scenario suite covering empty backlog, single-batch redirect, post-completion next-batch redirect, `stop_hook_active` loop prevention, parser-error lenience | `plugin/hooks/stop.py` (+ `parse_backlog.py`) | Pass | 8/8. Pre-validation tier. Loop-exit path (Opus risk #2) verified. outputs/ workaround. Windows integration retest owed. |
| 033 | 2026-05-16 | V25 | PreToolUse boundary check (V25 (c)) + V19 (a)/(b) read-only and V22 (e) Serves-line regression: 9-scenario suite | `plugin/hooks/pre_tool_use.py` | Pass | 9/9. Pre-validation tier. New (c) blocks edits outside Files: list and allows prerequisite-labeled files; V19/V22 checks all still passing post-V25 changes. outputs/ workaround. Windows integration retest owed. |

---

## V25 — Windows integration smoke test (2026-05-17)

Run from a fresh PowerShell on Alex's Windows machine via `claude --plugin-dir <path-to-sovereign-implementer/plugin>`. Tested against a pre-populated `v25-scratch` folder (inside the Cowork-selected `No code method` parent so Cowork could write the spine docs for tier-3 testing — an earlier scratch at `~\v25-scratch` was abandoned mid-test because it sat outside Cowork's access). Three Fail rows record real V25 bugs; corresponding fix-shape OPEN-QUESTIONS entries logged for V26.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 034 | 2026-05-17 | V25 | Plugin loads via `claude --plugin-dir` from `v25-scratch` on Windows | plugin scaffold (`.claude-plugin/plugin.json`, `hooks/hooks.json`, `commands/`, `agents/`) | Pass | Windows integration tier — V25 smoke test, deferred from session resume. |
| 035 | 2026-05-17 | V25 | `/hooks` shows 3 hooks configured: PreToolUse (1), SessionStart (1), Stop (1) | `plugin/hooks/hooks.json` + the three hook scripts | Pass | "3 hooks configured" header line confirms exact V25 expectation. All other hook types show no count. |
| 036 | 2026-05-17 | V25 | `/agents` Library shows 3 plugin subagents (planning, before-build, batch-executor) | `plugin/agents/*.md` | Pass | Listed as `no-code-method:batch-executor`, `no-code-method:before-build`, `no-code-method:planning` — all "inherit" model. Library tab is the canonical registry; "Agents" tab is filtered to invoked-in-current-conversation. |
| 037 | 2026-05-17 | V25 | Both V25 slash commands registered, accessible via `/no-code-method:before-build` and `/no-code-method:build` | `plugin/commands/*.md` | Pass | Bare names (`/before-build`, `/build`) don't auto-resolve — `/no-code-method:` namespace prefix is required for the commands-directory pattern. `/init-project` (skill-with-flags pattern) auto-shortens; the new commands don't. Worth noting; not blocking. |
| 038 | 2026-05-17 | V25 | SessionStart tier-1 silent in empty `v25-scratch` (initial launch, before pre-population) | `plugin/hooks/session_start.py` (tier detection) | Pass | Empty folder triggered tier 1 — no `additionalContext` injected. Same V21 behaviour; regression coverage. |
| 039 | 2026-05-17 | V25 | SessionStart tier-3 emit in configured `v25-scratch` (pre-populated CLAUDE.md + spine docs with V25 footers) | `plugin/hooks/session_start.py` (tier detection + foundational reads) | Pass | Verified indirectly via downstream — `/no-code-method:before-build` had the context it needed (CLAUDE.md path block, BACKLOG.md current state, UX.md entries). No "I don't know what project this is" behaviour from main Claude. |
| 040 | 2026-05-17 | V25 | V19 PreToolUse hook still blocks UX.md writes with deny-and-redirect message | `plugin/hooks/pre_tool_use.py` (V19 (a) + (b)) | Pass | Regression check. Fired correctly during the first (pre-restart) `/init-project` flow — Claude attempted Write(UX.md), PreToolUse denied with the canonical "UX.md is locked" message including the FOLD-IN PENDING redirect instructions, Claude then wrote a real fold-in block to BACKLOG.md. |
| 041 | 2026-05-17 | V25 | Stop hook misfires on template-placeholder BACKLOG.md (fires immediately after `/init-project` scaffolds, redirects with literal placeholder payload as if a real batch) | `plugin/hooks/stop.py` (+ `plugin/scripts/parse_backlog.py` placeholder detection gap) | **Fail** | Real V25 bug. Parser sees BACKLOG-TEMPLATE.md's example build batch (`[short descriptive name]`, `[Change description]`, `[path/to/file]` placeholders) as a real unticked batch; Stop hook redirects with literal placeholder JSON as the batch payload. Main Claude refused to invoke batch-executor on the garbage — soft discipline saved the system, but the hook is wrong. V26 fix shape: parser detects bracketed-placeholder pattern → returns `{}`. See `planning/OPEN-QUESTIONS.md`. |
| 042 | 2026-05-17 | V25 | BACKLOG-TEMPLATE.md's instructional canonical-format example block uses the literal `[FOLD-IN PENDING]` marker | `templates/BACKLOG-TEMPLATE.md` + `plugin/templates/BACKLOG-TEMPLATE.md` | **Fail** | Parallel shape to #041 — instructional template content uses the real marker, making real fold-in entries indistinguishable from the example via marker search. V26 fix shape: rewrite to use a visually distinguishable example (code fence + relocate canonical-format docs to DOC-STRUCTURE.md). See `planning/OPEN-QUESTIONS.md`. |
| 043 | 2026-05-17 | V25 | `/no-code-method:before-build` invokes before-build subagent end-to-end (validate → enumerate → recap) | `plugin/commands/before-build.md` + `plugin/agents/before-build.md` | Pass | After self-recovery from the parser-path bug (#044), before-build read state, validated the batch, produced a recap visible in chat. Subagent body's flow shape works as designed. |
| 044 | 2026-05-17 | V25 | before-build subagent body specifies parser invocation as `python plugin/scripts/parse_backlog.py` (project-relative path, no BACKLOG.md argument) | `plugin/agents/before-build.md` (validate-pass step 1) | **Fail** | Real V25 bug. Parser actually lives at `${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py` and requires a BACKLOG.md path as `argv[1]`. Subagent recovered via Glob + retry, but the spec is wrong. V26 fix: rewrite step 1 to use `${CLAUDE_PLUGIN_ROOT}` and pass the BACKLOG.md absolute path. See `planning/OPEN-QUESTIONS.md`. |
| 045 | 2026-05-17 | V25 | `/no-code-method:build` (or chained from before-build's completion) spawns batch-executor with the batch payload | `plugin/commands/build.md` + `plugin/agents/batch-executor.md` | Pass | Hard to determine from chat alone whether `/build` was explicitly invoked or whether main Claude chained directly into batch-executor after before-build's recap. Either way, batch-executor spawned correctly. |
| 046 | 2026-05-17 | V25 | batch-executor reads UX.md + MANIFEST.md before file edit | `plugin/agents/batch-executor.md` | Pass | Read(UX.md) and Read(MANIFEST.md) visible as the first two tool uses inside the batch-executor subagent context. Matches the "First action — load the project's current state" step in the subagent body. |
| 047 | 2026-05-17 | V25 | batch-executor writes the file declared in `Files:` list, ticks BACKLOG.md per-file, updates MANIFEST.md | `plugin/agents/batch-executor.md` (per-file work loop + completion path) | Pass | Sequence observed: Write(index.html) → Edit(BACKLOG.md) flipping `- [ ]` to `- [x]` for index.html → Edit(MANIFEST.md) adding the index.html entry. Per-file ticking and post-build MANIFEST update both correct. |
| 048 | 2026-05-17 | V25 | batch-executor produces build recap with correct shape per *After every build* | `plugin/agents/batch-executor.md` (recap shape) | Pass | Recap landed with all sections from the spec: "UX.md changes implied" (None), "Red flags" (None), "Next steps for you" (refresh + open in browser + /clear), "Files touched (absolute paths)" (3 files listed). |
| 049 | 2026-05-17 | V25 | Rendered output matches UX.md "Hello screen" entry (index.html renders "hello" centered in browser) | end-to-end across V25 + the generated `index.html` | Pass | Browser tab titled "hello", body shows "hello" centered both axes via inline flex CSS. Build batch produced an artefact matching the UX entry's stated behaviour. |
| 050 | 2026-05-17 | V25 | Stop hook does NOT misfire when current batch is fully complete (all `- [x]`) | `plugin/hooks/stop.py` (parser skip-completed logic) | Pass | After batch-executor finished and ticked the file, chat returned to a normal idle prompt — no further redirect, no infinite loop, no inappropriate next-batch invocation. Parser's "skip batches that are complete" behaviour worked as designed. |

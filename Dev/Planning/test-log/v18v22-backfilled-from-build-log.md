# V18–V22 — backfilled from BUILD-LOG (2026-05-16)

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


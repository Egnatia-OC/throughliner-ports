# V35 — E2E Taskflow test — first non-synthetic-fixture run (2026-05-21)

First plugin run against real Taskflow. Two sessions: case 1 (cold-start adoption), case 4 (refresh after real docs replaced templates). Planning subagent reached Q1 of 5 before halting — questions collided with decisions settled in Alex's separate planning project. Build/before-build/after-build not exercised.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 104 | 2026-05-21 | V35 | SessionStart safety net advisory fires on unadopted real Taskflow folder | `plugin/hooks/session_start.py` (V29 unadopted-folder detection) | Pass | `Taskflowapp/` had foreign CLAUDE.md + recognized source dirs; advisory fired correctly. First non-synthetic-fixture validation of the V29 detection. |
| 105 | 2026-05-21 | V35 | `/adopt` case 1 detection + migrate on real Taskflow with foreign CLAUDE.md | `plugin/agents/adopt.md` (case 1) + `plugin/skills/adopt/scripts/scaffold.py` | Pass | Previous-session run. Detected case 1, migrated foreign CLAUDE.md to V34 spec with fenced JSON path block, backed up original as `.foreign-backup-2026-05-21`, scaffolded BUILD-LOG.md + TEST-LOG.md under `no-code-method/`. |
| 106 | 2026-05-21 | V35 | `/adopt` sanity check refuses Windows home directory as adoption target | `plugin/agents/adopt.md` (sanity check on cwd) | Pass | Launched from `C:\Users\Alex` → subagent caught it, presented Cancel. Prevents scattering spine docs into home directory. |
| 107 | 2026-05-21 | V35 | `/adopt` case 4 refresh on real Taskflow — footer-bump on writable docs, fold-in routing on locked docs | `plugin/agents/adopt.md` (case 4 option 1 — refresh) | Pass | Bumped writable footers directly (BACKLOG, MANIFEST), routed locked docs (UX, SYSTEM-PROMPT) through fold-in. Validates V29 #083 fix on real input. |
| 108 | 2026-05-21 | V35 | Planning subagent first [SEQUENCE] question against real Taskflow planning batch | `plugin/agents/planning.md` (V22 + V27 + V32 inlining) | Skipped | Subagent opened [SEQUENCE] correctly (5 questions, Q1 presented). Halted — questions clashed with decisions already settled in Alex's separate planning project. Not a plugin bug. |


# v71 — 2026-05-24 — E2E round 2 + skills migration

**What shipped.** Scope 0068 (partial — build cycle tested, planning-from-scratch deferred to burner app). Skills migration: `commands/before-build.md` and `commands/build.md` moved to `skills/*/SKILL.md` format; `commands/` directory removed. Desktop app zip install procedure documented and tested — plugin v0.60.0 successfully installed via zip upload. Reference manual updated with packaging and install steps. Two research files: `desktop-app-plugin-upload.md` (zip format discovery), `subagent-token-costs.md` (cost reduction techniques). Two OPEN-QUESTIONS entries (structured-markdown validator, plugin testing framework). Scope file 0071 created (subagent cost optimization). TEST-LOG rows #124–#136 (6 Pass, 5 Fail, 2 Pass). INVENTORY updated for skills migration.

**Decisions.** Skills migration was unplanned — triggered by "legacy commands/format" warning on zip upload. Folded in because it was three files and five minutes. E2E build cycle ran against Taskflow batch 0001 (19 files, Room data model) — revealed five priority issues but produced a complete pipeline run. Planning-from-scratch testing deferred to Polite Fart Announcer burner app — Alex knows Taskflow too well to invent throwaway features.

**Pivots.** After-build's cascading source-code fix was the session's biggest surprise. A single gradle "fix" triggered a 6-minute chain of dependency breaks, overriding a user refusal, and ending stuck on file locks. This reframes after-build's scope: it must never touch source code.

**Carried forward.** Five priority actions from E2E: (1) after-build source-code boundary — needs scope file; (2) Stop hook before-build→build auto-chain fix — needs scope file; (3) session-open status summary — needs scope file; (4) subagent cost optimization — scoped as 0071; (5) "run commands yourself" prose rule for universal-behaviour.md — fold into next session touching that file.


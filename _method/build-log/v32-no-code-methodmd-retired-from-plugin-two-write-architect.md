# V32 — 2026-05-20 — NO-CODE-METHOD.md retired from plugin; two-write architecture established

**What shipped.** Split canonical method into two parallel sets: plugin-side (operational) and docs-only (project-agnostic prose). `NO-CODE-METHOD.md` retired from plugin runtime — subagents stopped reading it; operating procedures inlined into subagent bodies (planning gained *Procedure order*, before-build gained *Batch-sizing* sub-rules, after-build already complete). `universal-behaviour.md` absorbed cross-cutting orphans (routing logic, Rule 1, Prohibited block, flag taxonomy, tags glossary, Editing surfaces). New `VOCABULARY.md` (plugin + docs-only mirror). All cross-references redirected. BUILD-METHOD gained two-write architecture section. Coverage map consumed. Footer V30→V32; plugin 0.32.0.

**Decisions.** Shape A (full retirement + inline) over trim or pointer — rules live in plugin, not docs read. Plugin leads, docs-only follows. VOCABULARY as own file (not lumped into universal-behaviour — different concerns).

**Pivots.** Previous chat glitched — memory carried framing decision into continuation. Scope file stale (pre-docs-only framing). Cowork mount truncations (twice). Bash `rm` blocked by ACLs. Subagent inline gaps larger than coverage map suggested — real procedural gaps surfaced in planning and before-build.

**Carried forward.** `NO-CODE-METHOD.md` deletion owed. Docs-only still uses plugin phrasing. Smoke test owed.


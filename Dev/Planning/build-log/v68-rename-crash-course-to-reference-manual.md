# v68 — 2026-05-24 — Rename "Crash course" to "Reference manual"

**What shipped.** Scope 0061. `Crash course.md` renamed to `Reference manual.md` via `git mv`. All live references updated across 11 files: BUILD-LOG.md, BUILD-METHOD.md, PLAN.md, INVENTORY.md, README.md, plugin/README.md, CLAUDE-TEMPLATE.md, project-level CLAUDE.md, 0069 scope file, permission-prompt-surface-audit.md research file. URL-encoded links (`Crash%20course.md`) updated in both READMEs. H1 heading updated. Archive/ untouched (read-only). Doc-only; no footer bump.

**Decisions.** Renamed historical BUILD-LOG and PLAN.md references too — the log is a working reference, not a legal record, and mixed terminology makes grep harder. PLAN.md row for 0061 retains both old and new names (describes the rename action).

**Pivots.** None.

**Carried forward.** 0062 (HTML guide) depends on this rename being complete — now unblocked.


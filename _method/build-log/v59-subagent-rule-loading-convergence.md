# v59 — 2026-05-23 — Subagent rule-loading convergence

**What shipped.** Scope 0057. Converged batch-executor on read-spec-on-entry pattern (was the sole outlier with inlined rules). Now reads DOC-STRUCTURE.md at runtime like the other three subagents. Removed trailing "Spec references" section. OPEN-QUESTIONS entry removed. INVENTORY updated. 147 tests pass. Footer V53→V54; plugin 0.53.0→0.54.0.

**Decisions.** Read-on-entry over inline: specs changed every version V50–V53, inlined copies would silently drift. Runtime overhead marginal (already reads 5+ docs per invocation). Setup excluded (doesn't use DOC-STRUCTURE/VOCABULARY).

**Pivots.** None.

**Carried forward.** V54 batch-executor verification added to deferred tests.


# v121 — 2026-05-28 — Dev-side close procedure fixes

**What shipped.** Three fixes to session-protocol.md's close paths plus three folded-in OQs from the 0121 reader test. Batch removal timing aligned (both paths now use the pre-commit checkpoint), stale step-number cross-reference in session-reference.md fixed, proxy format spec added inline to close step 6. Lighter close trigger reworded, step-ordering rationale added, doc-only batch-input check clarified in routing table. Duplicate batch 0102 row cleaned up in BACKLOG shipped table.

**Decisions taken and why.** Batch removal moved into the checkpoint rather than staying a standalone step — the checkpoint is the last gate before commit, so all pre-commit work belongs there. session-reference.md step references replaced with action descriptions ("session close") rather than step numbers, to avoid future renumbering drift.

**Pivots and surprises.** None. Clean three-fix batch with three natural fold-ins.

# v137 — 2026-05-29 — Dev-side workflow reconciliation

**What shipped.** Five workflow steps added to `Dev/session-protocol.md` from convergence gaps G11–G12, G22–G24:
- G11: Build recap step (implementation close step 5) — ephemeral chat summary of what shipped + sweep findings.
- G12: End-of-recap flags (implementation close step 8) — consolidated flagged items before turn boundary.
- G22: Staleness sweep (implementation close step 3) — literal path/name grep on queued/parked batches.
- G23: Lost-feature check (implementation close step 4) — scan parked batches for met parking conditions.
- G24: OQ staleness detection (session-open step 5) — flag OQs with Surfaced tags 20+ sessions old.

Implementation close Turn 1 expanded from 5 to 9 steps. Turn 2 renumbered 10–15. Lighter close updated: G22/G23 added as conditional steps, G11/G12 listed as skipped. Pre-commit checkpoints expanded for both paths. Cross-references updated (lighter close step 1 → implementation close step 7, step 5 → step 11). Batch 0139's stale line reference (L136–181 → L179–231) fixed in BACKLOG.md.

Reconciliation map updated: G11, G12, G22, G23, G24 all ticked with resolution notes.

**Decisions taken and why.** Build recap positioned after all sweeps (steps 1–4) so it can include sweep findings — differs from plugin order (plugin recap before sweeps) because dev side has no TEST-LOG rows to summarize, making sweep findings the natural second section.

**Pivots and surprises.** None.

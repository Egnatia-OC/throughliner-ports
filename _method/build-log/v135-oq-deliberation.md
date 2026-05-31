# v135 — 2026-05-29 — OQ deliberation: all five resolved, new batch 0140

**What shipped.** Deliberated and resolved all five open questions. TEST-LOG columns: keep 7 dev-side, fix column ordering (folded into 0138). Batch lifecycle: plugin should delete from BACKLOG at close, not write back as shipped (folded into 0139). Volunteered test results: accept when specific enough to match a row (new batch 0140). Re-batching snapshot: shrinks after carve-out, close runs on reduced snapshot (0140). Step-by-step test protocol: goes in universal-behaviour.md only (0140). OQ section now empty.

**Decisions taken and why.** Investigated the plugin's `Status: shipped` lifecycle — found it's a two-step removal (close writes back, planning deletes), not permanent preservation. Nothing queries shipped status for any purpose; it's only used to skip or delete. Removing at close with build-log as the shipped signal is cleaner and matches dev-side practice. Scoped as part of 0139 rather than a separate batch because it makes plugin converge with dev side — which is what reconciliation is for.

**Pivots and surprises.** The "batch lifecycle on completion" OQ turned out not to be a real divergence — both sides converge to removal, the plugin just had an intermediate state. The OQ's framing was misleading.

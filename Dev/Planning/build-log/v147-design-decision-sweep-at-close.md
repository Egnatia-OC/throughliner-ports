# v147 — 2026-05-31 — Decision sweep added to close procedure

**What shipped.** Step 6d (decision sweep) added to plugin close procedure's post-build path. After writing the build-log entry, Claude now scans its "Decisions taken and why" for cross-cutting design decisions and routes them: UX-relevant → flag in end-of-recap flags (UX.md locked), implementation-relevant → update MANIFEST rationale on the matching existing entry. Pre-commit checkpoint updated to include the new step.

**Decisions taken and why.** VOCABULARY entry and Reference manual mention added as doc-parity fixes rather than separate batch work — consistent with existing close sub-steps (staleness sweep, frame-correction sweep, etc.) all having VOCABULARY entries. Crash course left unchanged — its adapted close description operates at a higher altitude and doesn't enumerate sub-steps.

**Pivots and surprises.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 1
- **Carve-outs:** None
- **Claude-verified tests:** 0 (no automatable tests — procedural doc change)
- **User-verified tests:** 0

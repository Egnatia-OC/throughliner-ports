# v156 — 2026-06-01 — Host/target safeguards for self-developing project

**What shipped.** Three behavioral rules added to CLAUDE.md's Host SI vs Target SI section: (1) state when editing target SI, (2) never claim target changes are live without reinstall, (3) use full paths for ambiguous docs. Two new OQs filed: host/target verification routing to E2E batch, and plugin not distinguishing build-time tests from E2E test sessions.

**Decisions taken and why.** Tests omitted from this batch — behavioral rules can only be verified in a subsequent session where Claude edits `plugin/` files. Verification routed to OQ for incorporation into E2E test batch 0131.

**Pivots and surprises.** None.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 1
- **Carve-outs:** None
- **Claude-verified tests:** 1 Pass, 0 Fail (of 1 total)
- **User-verified tests:** 0 pending

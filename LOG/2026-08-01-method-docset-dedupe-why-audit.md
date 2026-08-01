# ea272f6 — Corpus-wide de-dupe + why-clause-coverage audit of the whole method doc set

Ran the corpus-wide audit ([audit] flavor) across the whole docs/ set — plugin-behaviour.md, plan.md, the next-family, the done-family, setup.md, and templates — plus this session's own doc edits (built just before, so in view). Three lenses: same-rule-restated dedupe (not a word-cut pass — length is mostly load-bearing why-clauses), shared-scaffolding factoring across the flavor-doc families, and why-clause coverage gaps. No files edited — findings routed as captures.

Seven findings, all approved as-is at bulk approval and filed to Unprocessed: (1) Phase-3 "Recommend next" near-verbatim across the three done-flavor docs → shared done.md core; (2) the forward-advisory filing paragraph duplicated in all three done docs + plugin-behaviour.md → reduce to pointer; (3) the LOG-entry template + approval paragraph triplicated across the done docs → factor into done.md's shared section; (4) "Verify completion" + "Staleness sweep" near-identical done-build vs done-audit → lift to core; (5) next-audit's pass-by-pass criteria rule lacks a why-clause → add one; (6) the spec-sync-gate SDD-atomicity why duplicated done-build + done-plan → shared statement; (7) lower-confidence: the bulk-approval inversion re-explained at several sites → verify and trim to pointers.

**Files touched:**
- none (audit — read the whole plugin/si-plugin/docs/ set + templates; edited nothing)

**Routed to Captures:** [dedupe-done-recommend-next-core], [dedupe-forward-advisory-filing-paragraph], [factor-log-entry-template-approval-para], [factor-done-verify-completion-staleness-sweep], [why-clause-audit-pass-by-pass-criteria], [dedupe-spec-sync-gate-sdd-why], [dedupe-bulk-approval-inversion-reteach]

**Approval outcomes:** all 7 findings approved as-is (none dropped or reworded)

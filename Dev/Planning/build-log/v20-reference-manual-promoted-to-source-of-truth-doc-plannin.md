# V20 — 2026-05-14 — Reference manual promoted to source-of-truth doc; planning shifts

**What shipped.** Reference manual promoted to parity-tracked SoT doc (drift audit: fold-in mechanism, BACKLOG rationale, prerequisite carve-out, UX-conflict surfacing, file-location, editing-surfaces all corrected). Planning shifts: scope files V20–V27 renamed to V21–V29; new V24 for TEST-LOG; V23 absorbs batch-sizing. PLAN.md rewritten. New OQ: *Cowork-friendly prose-only rewrite*. 15 footers bumped V19 → V20.

**Decisions.** Reference manual earns SoT status but not by retrofitting unshipped scope-file content — plans are provisional. Cowork-first stays in spec for now — method IS Claude-Code-specific. TEST-LOG is operational (sibling of MANIFEST), not a new section — five rules distributed across existing NO-CODE-METHOD phases. Batch-sizing folds into V23 (before-build subagent session).

**Pivots.** Stale `.git/index.lock` on Linux mount blocked renames — workaround: plain `mv`, let git detect 100% content matches. Cross-version template reconciliation OQ framing weakened by new Cowork-rewrite entry.

**Carried forward.** Cowork-friendly prose-only rewrite in OQ. TEST-LOG mechanism → V24. Batch-sizing → V23.


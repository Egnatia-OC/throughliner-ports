# [HASH] — Added the missing why-clause to next-audit.md's pass-by-pass criteria rule

next-audit.md told the audit to apply criteria pass-by-pass (one criterion across the whole target, then the next) but gave no reason, and on 4.8 a bare pass-by-pass instruction tends to collapse into a per-artifact skim. Added the why: a single criterion held across the whole target is applied more consistently than re-deciding every criterion afresh per artifact, and it groups findings by criterion ready for the compile step.

**Files touched:**
- plugin/si-plugin/docs/next-audit.md — why-clause added to the systematic-read rule

**Routed to Captures:** none

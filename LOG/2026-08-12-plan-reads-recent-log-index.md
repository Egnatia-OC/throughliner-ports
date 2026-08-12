# 0ae69d6 — /plan's Step 1 reads the five most recent LOG index lines, at a cost re-measured rather than assumed

The read lands at Step 1's read-state, alongside the digest and SPEC, folded into the opening narration that already fires. No separate output and no summary of the log for its own sake — orientation, not a report.

**The problem, in the user's words:** they regularly found themselves asking Claude at the start of a session to look at recent sessions for context, because mid-session Claude knows what is happening and start-of-session Claude does not.

**Why the index and not the entries.** An index line is built for exactly this — it carries the artifact touched and the nature of the change so a session can decide what to open without reading prose. Reading the top few costs a fraction of the entries and leaves the full retrieve path untouched.

## The cost was re-measured at build, as the item required

The item estimated 2,000–2,500 tokens and held itself below the line until index lines were capped. Measured here: **417 words across the top five lines, roughly 560 tokens** — well under the estimate, because the proportional cap shipped in `7c9922a` in between.

That also bears on [index-cap-sample-was-three-entries], which warns the cap's derivation sample was small and that 87 historical lines exceed it. Those long lines are historical; the five most recent are all post-cap, which is why the measured figure is what a session will actually pay going forward rather than what the corpus average would suggest.

**Why /plan only.** `resources/research/legislative-review-cycles.md` finds a broadly-scoped obligation is the one that goes unperformed — 7.6% coverage where a duty claimed 344 Acts. A narrow read at one skill's opening is the shape that survives, and `plan.md` is fetched, so it spends nothing against the instruction ceiling.

**FAQ entry written**, since the opening narration visibly changes — a user will notice a planning session opening with awareness of what just happened.

**A consequence for another item:** [discord-post-session-start-strength] was waiting on this feature to ship before its post could be written. It has now shipped.

**One thing this run's own compliance audit flagged about it:** adding this read took Step 1 to seven scans at a single opening, and nothing counted or objected. Filed as [step-1-scan-count-unbounded].

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** [step-1-scan-count-unbounded] (from the audit).

Rule gate: run — admitted on the user's own repeated experience of asking Claude to look at recent sessions, and on the narrow-scope finding from the legislative-review research that a broadly-scoped obligation goes unperformed. Kept to one skill's opening deliberately. Fetched doc, no ceiling cost. The gate's cost condition was discharged by measurement rather than estimate.
FAQ: updated — a new entry on why a planning session now opens knowing what happened last time, written because the opening narration visibly changes.

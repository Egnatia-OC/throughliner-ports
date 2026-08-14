# a216873 — plan.md's flavor table removed, next.md's kept as the routing map, and the capture's second argument corrected

The build / `[audit]` / `[user]` / `[freeform]` table is canonical in `skill-nonspecific-rules.md`, reproduced in `plan.md` together with the over-tag guard and its blocked-on-a-push carve-out near-verbatim, and reproduced again in `next.md` with routing targets substituted in.

**`next.md`'s block stays and the audit's remedy is refused.** Its four rows map each tag to a routing target — `next-build.md`, `next-audit.md`, walk, halt. That is not a restatement of the canonical table; it is the routing map, which exists nowhere else, and the audit's own stated exclusion covers it: a site-specific application narrows a general rule rather than repeating it. Its suggestion to "reduce it to the routing map alone" describes what the block already is, minus two descriptive words per row that make it readable.

**`plan.md`'s block goes.** What survives is the opening statement that work is Claude's to build by default, and the one genuinely new clause — that a `[user]` line must carry a described walkthrough, settled at the keep-step.

**The capture's second argument does not survive checking, and is corrected here rather than carried forward.** It claimed fewer copies of the table would make adding a new flavor cheaper. It would not. The three-sites wiring rule in `CLAUDE.md` names three *behaviours* — how a flavor is marked and placed at the keep-step, how a run routes on it, how a close routes on it — not three copies of a table. Cutting `plan.md`'s table removes none of those obligations, because `plan.md` still owns the marking and the placing. This is a straight subtraction, and claiming otherwise would have oversold it.

**`setup.md`'s scaffold paraphrase is untouched** — user-facing template text, as the audit itself judged.

**Three items landed in `plan.md` around the same region**, and the `[freeform]` trim belonging to `[plan-md-restates-four-shorter-rules]` sat directly beneath this block, so the two edits were made as one change to avoid reasoning from stale line positions.

**Files touched:** `plugin/throughliner/docs-b/plan.md`
**Routed to Captures:** none

Rule gate: not needed — no rule authored or amended; one restatement evicted, one refused for eviction on recorded grounds.

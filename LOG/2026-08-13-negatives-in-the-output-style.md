# d6efa7c — The output style's negative instructions restated as the behaviour wanted, with the contrastive example deliberately kept

"Tell Claude what to do instead of what not to do" is one of the few levers Anthropic names as particularly effective for steering output format, and the Opus 5 guidance repeats it for communication style specifically: positive examples of the style you want tend to be more effective than instructions about what not to do. The output style was roughly half negatives — "don't preview the later items", "never cram", "never drop a plain-English explanation", "Cut bloat", and a "Bad:" exemplar — while the parts that visibly held were the positives, "Lead with the decision" and the "Good:" line.

This is a rewrite rather than an addition, so it costs no instruction budget, which matters because the style is loaded in every session of every consumer project.

The item left one thing to settle: whether the contrastive Good/Bad pair survives. It does. A contrastive example is not the same thing as a negative *instruction* — the guidance endorses examples strongly and this project's own experience is that a shown specimen is the one thing that has fixed a communication rule here. The pair stays as written.

What changed instead is the prose. The terseness guard is now stated as what to do — length is free where it carries substance, give every explanation the user needs in order to act, in full sentences, at whatever length that takes — with the padding named as what comes out rather than as a list of prohibitions. The detail gate is stated as holding reasoning back and offering it. The frontmatter description's "(never terse)" becomes "full plain English". The written-file paragraph built alongside this was authored in the positive form for the same reason.

The guard the item flagged for deliberate preservation is intact and is the reason the rewrite was done carefully rather than mechanically: the "This is structure, not terseness" paragraph exists because an earlier concision push made Claude clipped and unhelpful, and it is the clause that keeps plain-English explanation in. Restating it positively had to strengthen that, not lose it. The new wording makes the permission explicit — length is free where it carries substance — where the old wording only forbade its absence.

Rule gate: run — substitution, no growth. Wording changes only; no rule was added, removed or narrowed.

FAQ: not needed because this changes how Claude writes, not how the workflow works.

**Files touched:**
- `plugin/throughliner/output-styles/concise-throughliner.md` — the terseness guard, the detail gate and the frontmatter description restated positively; the Good/Bad pair kept.

**Routed to Captures:** see this session's other entries.

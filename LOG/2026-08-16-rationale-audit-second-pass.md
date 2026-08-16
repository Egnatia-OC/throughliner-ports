# d82f538 — Second rationale pass over the always-loaded rules: eleven findings, filed as nine captures

The first rationale pass applied one mechanical criterion across all thirteen shipped docs — bolded why-paragraphs and defeated-alternative phrases — and found about 1,050 words. That is the shape the defect takes most often, and the audit said at the time it was not the only shape. This pass read `skill-nonspecific-rules.md` **per paragraph** against the delete-and-reread test, looking for the shapes a signature criterion structurally cannot see.

**It found all five shapes it was scoped for**, which is the answer to whether the technique was worth its cost.

*Rationale inside fenced blocks* — two sentences in the work-cycle block at the very top of the file. The first pass did not read fenced blocks as prose at all, so nothing inside one had ever been examined.

*Unmarked paragraphs with no signature phrase* — the commonest of the invisible shapes, found opening two rules: the scrub-before-writing section and the research-and-evidence section. No bold lead-in, no defeated-alternative phrase, nothing for a pattern to match on.

*Rationale folded into the second half of a rule* — the cadence rule, whose closing sentence argues for the rule's importance rather than helping apply it.

*Evidence clauses attached as subordinate parts* — three sites, each naming a past failure inside a live rule.

*One duplication* — the throughline's "what it buys" paragraph, stated again at greater length in SPEC.

**Two findings recommend keeping rather than cutting, and they are why this was a reading pass rather than a script.** The truncated-read sentence is mixed: delete the whole thing and something operative goes with it — where the check belongs — so it is reclassified rather than removed. And the one-chat evidence clause is filed as **contested**: by the test it is rationale, but the user demonstrated its value the same day, recognising a stale FAQ entry as wrong precisely because she knew the history. Cutting it leaves a bare prohibition that reads as arbitrary. That one goes back to her rather than into a build.

**The cadence numeral was decided, as the item asked.** "Three occasions warrant it" is descriptive of a list that follows rather than a declared limit, so it does not breach the derivation rule. It is recommended for removal anyway, on maintenance: a session admitting a fourth occasion has to notice a numeral three lines above the list, and a numeral silently disagreeing with its own list is worse than none.

**The audit's own coverage is recorded as a finding.** One file per paragraph; twelve fetched docs on the signature criterion only. The condition both this item and the restyle carried — extend once the yield is known — can now be answered, and the recommendation is to extend to `done.md` and `plan.md` only, the two largest and the two already scheduled for work.

Depth: full — one finding recommends keeping text, and one is filed contested against the user's own recorded behaviour the same day.

Rule gate: not needed — an audit authors nothing and amends nothing. Any rule change comes later, from a build processing these findings, and passes the gate there.

FAQ: not needed — an audit edits nothing a consumer sees.

**Approval outcomes:** all eleven findings approved as-is; none contested, reworded or dropped. Filed as nine captures, three of them grouping findings that are one editing pass over one shape in one file — flagged to the user at the time, who may split them.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — **read only.** An audit edits nothing.

**Routed to Captures:** [cycle-block-carries-rationale-in-a-fence], [cadence-rule-rationale-and-numeral], [unmarked-rationale-paragraphs-open-two-rules], [captures-placement-rationale], [throughline-rationale-duplicated-in-spec], [evidence-clauses-attached-to-three-rules], [inline-switch-paragraph-is-justification], [truncated-read-sentence-reclassify], [rationale-audit-fetched-docs-gap].

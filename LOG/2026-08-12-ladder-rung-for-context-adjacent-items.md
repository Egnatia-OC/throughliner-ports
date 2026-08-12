# 0ae69d6 — A context-adjacency offer triggered at the fallback ladder's bottom rung, with both open questions settled at build

The ladder is unchanged — file order stays rung 6 and is what runs if the offer is declined. Reaching it now triggers **one** offer: process the items whose material this session has already loaded, work through in order, or run /done.

**A triggered step rather than a sixth rung**, as decided at processing. Every other rung *sorts* the section — it answers "which item first". Context-adjacency does not sort; it **selects a handful** that happen to be cheap right now. Forcing it into rung shape would leave one entry behaving unlike the other five, which is how a list stops being read. As a trigger, file order stays literally true.

**The exception to the never-offer discipline is stated in the text, not smuggled.** The ladder is internal, applied, never presented as a choice, because ordering is Claude's to own. This step asks — and the doc says why: only the user knows whether there is appetite for more items at all, so the offer is as much *shall we continue* as *in what order*, which is a question about their time and was never Claude's to own. Without that sentence a later reader deletes this for contradicting the rule directly above it.

## The two questions the item left genuinely open, and how they were settled

**Which items qualify** — resolved as a *checkable* test rather than a judgment: an item whose files, research notes or subject matter this session has already opened. Read off what was actually read, not off what feels related.

**How large the set may be** — derived from the criterion rather than picked. Name every item that qualifies; if so many qualify that the set cannot be read in one line, the criterion is discriminating nothing, so say nothing and take file order. The bound is the criterion's own selectivity. A fixed count — the item's instinct was three to six — would be a bare number, which [derivation-required-for-limits] bans, and the ban is what forced the better answer.

**The measured case, from the session that asked for it:** processing [spec-carries-implementation-detail] required SPEC.md read in full, 6,159 words, already read at that session's opening — so the measurement that made the item decidable cost nothing. A later session pays the whole read to reach the same point. Not a convenience: the difference between an item's research being paid once or twice.

**A defect in this build was found by the compliance audit later in the same run** and filed rather than quietly fixed: the offer as written is a flat three-option menu at a moment Claude has a view on ordering, which the narration rule says should lead with a recommendation. See [context-adjacency-offer-is-a-flat-menu].

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**Routed to Captures:** [context-adjacency-offer-is-a-flat-menu].

Rule gate: run — admitted on a standing user request repeated across several sessions, which is the pointed-to need the admission test asks for. Built as a trigger rather than a sixth rung so the ladder's five entries keep behaving alike. The gate also forced the set-size answer: a bare "three to six" is barred by [derivation-required-for-limits], so the bound had to be derived from the criterion instead — which produced a better rule than the number would have. Its exception to the never-offer discipline is written into the doc beside it, per the requirement that an exception state its justification where it sits.
FAQ: not needed because this fires only when the queue has run out of priority signal, and what the user sees is one plain question about what to do next. It introduces no concept a consumer would need explained.

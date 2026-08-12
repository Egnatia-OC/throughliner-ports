# 7c9922a — The web-search offer and the capability check now fire on a question, not on a feeling [what-would-answer-this-as-a-shared-trigger]

Captured by the user. Their words: the "what would answer this?" logic could also help trigger Claude to offer web search more, which is currently user-triggered more often than not. The unification is Claude's.

Built in one pass with [capability-check-weight-by-site] — both rewrite the same guard.

**One diagnosis covering both.** Each rule was written as a **self-assessment of confidence**. The web-search rule fired on "uncertain about an external fact"; the capability check fired on Claude judging whether a tool exists. Both require noticing an internal state — uncertainty — and a session that has quietly settled on an answer does not feel uncertain, so neither trigger fires. That is the mechanism behind the user's observation that in practice they are the one asking for the search.

**Why the reframe fixes the trigger rather than merely restating it.** "What would answer this?" is a question with an answer, asked about the *problem* rather than about Claude's state. It can be performed by a session that is wrongly confident, because it does not depend on doubting anything — and its answer is frequently "a web search would" or "that command would", at which point the offer follows with no judgment about confidence.

**The strongest evidence is that this is at least the third instance of one failure family.** Alongside these two, three shipped rules were recorded the same day as not firing — all correctly worded, and all requiring Claude to notice something about itself. Worth naming before another rule is written in that shape.

**Claude's own filed risk was overstated, and the correction is what admitted this.** The capture warned that a rule instructing Claude to ask a question is itself a rule Claude must remember to apply — the same weakness one level up. That holds for a *new obligation*, and this is not one. Both rules already fire; what changes is the form of their trigger, from "am I uncertain?" to "does this turn on something outside what I can read?" No new moment, no new obligation, no new slot.

**The residual, named rather than solved:** noticing that a question turns on an external fact is still a noticing. This improves the odds; it does not close the hole. That sentence ships in the doc rather than only living here.

**A forced site was the third edit, and it is what stops the rule floating free:** `plan.md`'s present-and-interview step, which runs on every item processed. A carrier that always fires beats a standing rule with no site.

**Rejected: a single shared statement both rules reference.** It would consume a slot to say what two amendments already say, and it is the one-rule-in-two-documents shape that three separate items are filed about.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none from this item

# e5d169b — The rule-corpus ceiling is removed and MEASURED becomes a per-audience growth report

The board reported one always-loaded count as though it were the only one. `ALWAYS_LOADED` named a single file — the shipped `skill-nonspecific-rules.md`, at 234 statements — while this project also loads its own `CLAUDE.md` in every session, another 96. So every reading of the board understated this project's real burden by the whole of CLAUDE.md, and `resources/method-compliance-audit-checklist.md` had always required the count be reported split by audience. The one tool producing the number did not do it.

`ALWAYS_LOADED` is now two named lists — `SHIPPED_ALWAYS_LOADED` and `HOST_ALWAYS_LOADED` — with the old name surviving as their sum, and MEASURED prints a count per audience: a consumer carries 234, this project 330.

The larger half of the change is that **the ceiling is gone entirely**, which was decided after the item was filed and widened it. The 150–200 instruction figure the ceiling of 200 derived from was re-validated against the 5-series at the user's instruction and found roughly an order of magnitude too tight — the benchmark was re-run a year on, frontier models had improved about tenfold, and the nearest tested Claude model only begins failing between 2,000 and 5,000 constraints (`resources/research/instruction-ceiling-revalidated-for-5-series.md`, which carries both caveats: neither Opus 5 nor Fable 5 was tested, and the benchmark measures keyword constraints rather than behavioural rules). A threshold that has lost its derivation is exactly what [derivation-required-for-limits] bans, and being conservative is not a defence. So `CEILING` and `CEILING_NOTE` are deleted, `firing` is hard-coded False, and `GROWTH_NOTE` replaces them — stating in the file itself why no replacement number may be invented.

**What this deliberately gives up.** Nothing will ever fire to say the corpus is too big. That is the honest position rather than a regression: the surviving case for eviction is relevance — irrelevant content degrading the model's treatment of all instructions, near-identical rules acting as optimal distractors for each other, and Anthropic's own 5-series guidance to remove prior-model scaffolding — and a count measures none of those.

**One alternative was weighed and lost: keeping a ceiling, but one per audience.** That was the question the item was filed with, and it is moot rather than refused — with no defensible figure for either audience, two ceilings is two invented numbers instead of one.

**AUDITED had to change with it**, because it fired on the same constant. It now reports and never fires, saying plainly that the sweep is a judgment call. That is a consequence of the described work rather than a widening of it: the alternative was to invent a trigger, which is banned.

**Two things found by running it.** The first growth report showed a false +160 for the always-loaded set, because the rules file did not exist 30 commits ago and counted zero — so `_count_at_rev` gained a strict mode, and a group containing a file newer than the window now reads "not comparable" rather than as growth. And CONTRADICTED was re-pointed at the combined always-loaded set: CLAUDE.md is already in `RULE_BEARING`, so a commit adding rules there triggered the check while its growth stayed invisible to it.

**Files touched:** `resources/rule_signals.py`
**Routed to Captures:** none from this item
Rule gate: not needed — no rule in the method's own text was authored or amended; this is a change to a host-only measurement script.
Retired: `CEILING` — the 200-statement rule-corpus ceiling

# 16ed591 — The self-authoring gate now charges on relevance, and the ceiling it used to declare is its counter-example

The gate opened by declaring the binding limit as a count of instructions — roughly 150–200 — and rested its whole charging argument there. That figure was re-validated against the 5-series and found roughly an order of magnitude too tight, and `rule_signals.py` had already removed the ceiling derived from it, replacing it with a growth report carrying no threshold. The gate went on asserting it.

The conclusion survives the research untouched, which is why this is a rewrite of the argument rather than a repeal of the section. The surviving case is relevance: content that merely doesn't apply this session is not filtered out selectively — irrelevant instructions cause wholesale dismissal of the set, and near-identical rules are optimal distractors for one another. Both were already stated in the same paragraph, and neither depends on the number. The opening now leads with them.

No replacement figure is introduced. Restating a larger number was rejected at /plan: the project has banned inventing a threshold once already in `rule_signals.py`, and a second unbacked number in the gate would restore by hand what was removed by code. A paragraph now says so explicitly, so the absence reads as a decision rather than an oversight.

The consequence further down the document is the more interesting half. The derivation rule used 150–200 as its **worked example of a soundly derived number**, which after the re-validation taught the opposite of its lesson. The 10,000-character hook output cap takes that role instead — externally imposed by Claude Code, one sentence of derivation, checkable against the tool. And 150–200 stays in the document as the **counter-example**: it came from research, which is a qualifying derivation, and it was still wrong. So a stated derivation makes a limit traceable and revisable; it does not make it correct. A number sourced from research about one generation of models has an expiry date, and the derivation rule is what makes the expiry findable. That reads as a better lesson than the one it replaced.

One dangling reference went with it: §1 said the amendment-versus-freestanding distinction "maps onto the ceiling exactly", and now maps onto the relevance cost instead.

This was the second confirmed instance of [no-link-from-research-to-items-scoped-on-it] — the superseded figure had propagated further than the four queue items that pass found, into the gate's own opening argument, with nothing connecting them.

**Files touched:** `resources/self-authoring-rules.md`

**Routed to Captures:** none

Rule gate: run — the gate was run on itself. Disposition: this is subtraction plus restatement, not addition. The count is removed as an operative limit and nothing takes its place; what is added is the explanation of an absence, which the derivation rule requires of any repealed limit. Host-only — consumers never author method rules.

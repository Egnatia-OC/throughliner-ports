# [HASH] — The one-item-at-a-time rule is now shown as a specimen message rather than described in prose

Alex asked, separately from length, what would get Claude to stop bundling. The honest research finding is that no such lever is documented. Anthropic's guidance has nothing on releasing output one piece at a time, and the general literature that surfaces on the phrasing is prompt-chaining research — about how a *human* should decompose their prompts to improve model accuracy, which is a different problem in the opposite direction and must not be cited as support for this rule.

What the evidence does support is a specimen. Examples are called one of the most reliable ways to steer output structure, and the local evidence is stronger than the citation: plan.md's checkpoint is the one site in this method where bundling was actually fixed, and it was fixed by showing the message — this is the shape of the message — followed by a flat statement of what does not appear beneath it. Every other site states the rule in prose, and the rule still slips.

The counter-evidence was already in hand and argues the same way. The one-at-a-time rule is currently stated in three layers — global CLAUDE.md, project CLAUDE.md, and the output style — and it still slips. That is direct local support for the official line that repetition is not the missing ingredient.

Alex chose the output style in her own words ("keep it in the output style"), on Claude's recommendation. The build replaces part of the paragraph's prose description with a shown single message plus a flat statement that steps two and three do not appear beneath it. It substitutes for description rather than adding to it, so the style does not grow.

Two things recorded so they are not misread later. The transcript audit — identifying the worst-bundling sites from real transcripts — is held back, not refused. It was rejected as the *first* move because it spends heavily to locate sites when the fix is probably generic; if the specimen does not hold, the audit is the follow-on, and by then there is a concrete failure to point it at. And the limit stands as the item stated it: a specimen in the style is one more layer asserting the same rule, and this project cannot observe its own communication rules failing, because the global CLAUDE.md and the output style mask whatever the shipped docs say. A successful outcome here will be hard to attribute and a failure hard to see. That is a reason to keep the change small, which it is, rather than a reason to skip it.

Rule gate: run — substitution, no growth. Shown text replaces prose description within the existing paragraph.

FAQ: not needed because this changes how Claude writes, not how the workflow works.

**Files touched:**
- `plugin/throughliner/output-styles/concise-throughliner.md` — the "One item at a time" paragraph's description partly replaced by a shown specimen message.

**Routed to Captures:** see this session's other entries.

# [HASH] — Provenance splits into an origin claim and a quote claim, and the wording test binds only to the second

Two different claims were collapsed into one. An **origin** claim — "captured by you", "you raised this" — says where something came from and has nothing to do with wording; a paraphrase is the normal way to state it. A **quote** claim — "your words", quotation marks — is about wording and needs verbatim text. The shipped rule said a `captured by you` credit "requires the user's own words as its source", applying a wording test to an origin claim.

That is why Claude ended up demanding proof. The rule made wording the evidence for something that was never a claim about wording, so the cheapest available move was to ask the user to substantiate it — reported by her from a live instance in another project the same day. Her position settled the split: nothing is her words unless it is a direct quote, and equally, work is not only hers if it is not in her exact words — but everything here is written and recorded by Claude.

The lint had it backwards in both directions. It flagged five legitimate origin claims for lacking a quote, and a planning session came one turn from deleting those credits on its instruction. And it passed a quote frame over a paraphrase, where Claude's own third-person rendering sat under a claim to be hers.

What must not change is default-AI: an unmarked item reads as Claude's, and that is the half the mechanism was built for. Abolishing provenance was floated and refused for that reason.

Eleven quote frames across nine items and the two paced Discord posts were corrected. They could not be verified as verbatim or not, and asserting a quote over text nobody can check is the failure this item names — so every unquoted case was reframed *down* to an origin claim ("rendered in Claude's words rather than quoted") rather than up into quotation marks. The conservative direction: it loses a true quote's force where one existed, but never manufactures one. The five items the lint had been flagging were left exactly as they were, because they were right all along.

A stricter form was proposed and refused on the user's objection: requiring verbatim text for every credit would have transferred every un-transcribed idea of hers into Claude's column.

Verified against the real queue rather than by reading the diff: six flags fell to one, the survivor being a genuine quote claim with nothing quoted, which was then corrected to zero.

**Files touched:** `plugin/throughliner/hooks/post_tool_use.py` (`CREDIT_PHRASES` becomes `QUOTE_CLAIM_PHRASES` with "captured by you" removed so origin claims are never checked; check renamed; warning text rewritten to name the origin form as the alternative; docstring gains the split as check 4), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (provenance rule split into a typed block naming both claims, with the wording test bound to the quote claim alone), `QUEUE.md` (the eleven corrections).

**Routed to Captures:** `[origin-claim-has-no-test]` — the suite's four credit cases all happen to use a quote-claim phrase, so every one survived the split untouched and nothing asserts the half that changed.

**Rule gate:** run — admitted as an amendment to the existing provenance rule, which already distinguishes credit from agreement and provides for mixed authorship; no freestanding rule and no slot spent. The eviction is the wording test as applied to origin claims, repealed outright. One proposal refused on the user's objection, above. Failure evidence is two instances — the five mislabelled items here, and the live report from another project the same day.

**FAQ:** updated — covered by the new entry on what the queue check now tells you, which carries both this change and the noise reduction shipped alongside it.

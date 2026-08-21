# 7bc2c58 — FAQ answers what happens when something is deleted from the queue

A user had no answer to the most reasonable worry the method produces: Claude just removed an item from my queue — is it gone?

The new entry, "Is anything I approve ever gone for good?", says three things. Deletion is the user's decision, not Claude's. Git history keeps the text, so asking for a deleted item back is a supported route rather than a favour. And the exception is the one they chose — where a document was kept out of the repository at setup, nothing records its earlier versions, so a deleted item there is genuinely gone, and Claude says so at the time rather than promising a recovery it cannot make.

Naming a recovery command stayed refused: this audience does not use a terminal, and a command written into an FAQ ages into wrong advice.

Written into the shipped template and its index, then re-copied into `FAQ/` — both byte-identical, which is the check that keeps the two copies from diverging the way they did before that clause existed.

**Files touched:** plugin/throughliner/templates/faq-template.md, plugin/throughliner/templates/faq-index-template.md, FAQ/faq.md, FAQ/index.md
**Routed to Captures:** none
Rule gate: not needed — a consumer-facing FAQ entry; it authors no method rule.
FAQ: updated — "Is anything I approve ever gone for good?" plus its index line.

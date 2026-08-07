# [HASH] — A share-time warning added as the sibling of the write-time private-information rules

The user's rule, in their words: if they say they are going to share something from the log or elsewhere, Claude should warn against that. It survived on its own merits when the larger proposal it arrived inside ([make-project-docs-private]) was withdrawn — they judged the repo-privacy half not worth doing and this half fine.

**What it adds that the method did not have.** Every private-information rule is **write-time** — don't write a third party's details, don't ask for a sensitive identifier, don't characterise the user. Nothing existed at the moment of **sharing**, which is a different moment with a different exposure: the text is already written and already approved, and the risk is that the user does not remember everything a log entry or work item contains when they decide to send it somewhere. The two scrubbed-output paths that do exist — the method report and the announcement — are Claude *authoring* text for an outside reader, not the user forwarding a document Claude wrote weeks ago.

**The trigger is the user saying they intend to share**, in whatever words. Not a scan of every doc, and not a gate on writing — a warning at the point of leaving.

**The warning names what is actually in that specific text** — third-party references, absolute paths, account or tool identifiers, anything about someone other than the user — rather than a generic caution. A warning that does not say what it found is one the user learns to skip.

**Both anti-nag limbs from the item were settled at build and are in the rule as a block**, because this risks becoming exactly the nagging the method has spent months removing elsewhere: **fire once per intended share**, not per mention; and **say nothing at all when the text contains nothing worth naming** — silence is the correct output for a clean doc, the same treatment a suppressed check gets at a skill opening. A warning that fires on every clean document teaches the user to ignore the one that isn't.

Consumer-visible behaviour, so it rode the full sync: SPEC's private-information paragraph, README's feature list, and a FAQ entry pair. **Docset A is out of scope** — new capability, which the freeze bars, and it touches no /setup question so the freeze's one exception does not apply.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `SPEC.md`, `README.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`
**Routed to Captures:** none
**FAQ:** updated — new entry "I said I was going to send someone a log entry and Claude warned me about what was in it. Why?" plus its index line

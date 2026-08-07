# 96166c6 — Recorded summarise-for-the-human as the decided default for all users, and fixed the authoring standard that contradicted it

The user settled this: the short-summary-plus-pointer rendering is the default for **every** user — not a per-project setting and not tier-dependent. Their reason, in their own framing: the fight for working links to lines in files may never be won, so the method needs *something*, and this has to be it.

**The rationale is not the token one, and that correction is what the item existed to make.** The summary is not a concession to pricing; it is the feature. A work item is written long and dense **because Claude needs that detail** — the facts, the rejected options, the conditions. The human does not need the text, only enough to understand what they are approving, and Claude can summarise it perfectly well. So summarising is simultaneously the answer to the rendering question *and* the answer to item bloat: items stay complete for the reader that needs them, and stop being a wall of text for the reader that does not.

**The contradiction fixed here is the actual build.** Two shipped rules disagreed, and captures had been drifting long and dense in the gap. The authoring standard said the human co-reads and approves the item text — *"unreadable is unapprovable"* — which assumes the human reads the item itself. The doc-bound-text rule says the human reads a short summary with the full text on request. One pulled toward writing items for the user to read while the design says they are written for Claude and summarised for the user. The standard now says what items are actually for.

**No length caps, explicitly.** Not by line, sentence, or any number. One thing governs: does the user understand enough to approve? That is the method's standing principle — concision comes from sequencing and leading with the decision, never a word-count cap — applied rather than re-decided.

**The plan-tier objection is answered rather than dropped.** A per-project summary-length setting was rejected for repeating the retired working-mode failure exactly: a field answered strategically rather than truthfully. Adaptive length by size of text was rejected by the user as an arbitrary cap under another name. So everyone gets the same rendering, the cost is accepted deliberately with its reason stated, and the expand-on-request offer keeps the heavy path opt-in.

One thing carried into the standard that the item did not itself state: the *summary* must be readable. A summary in untranslated jargon fails exactly as badly as the wall of text it replaced — which is the sibling item shipped in the same run.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none

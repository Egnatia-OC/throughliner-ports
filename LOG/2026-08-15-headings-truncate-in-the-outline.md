# [HASH] — Work-item headings must put their distinguishing words first, because the outline truncates them

Captured by the user from a screenshot of her queue open in a Markdown reader with an outline sidebar, where every heading was cut mid-phrase. Her observation that she navigates by the section titles is what surfaced it; the slug plays no part in that navigation.

No existing rule caught it. The index-line rules govern `LOG/index.md` and correctly say specificity beats brevity, because that line is read whole. A queue heading is read *truncated*, in a viewer, so the constraint is different and nothing stated it: the distinguishing words have to come early, because the end of the line may never be seen. Claude was actively making it worse — one heading rewritten in the same session put the identifying half in a second clause.

The clause amends the Captures line-format block, which already specifies the heading's shape, so it has a named parent and spends no slot.

A length cap is refused explicitly, in the rule's own text, because it is the intuitive fix and will be re-proposed by the next session to meet this problem. This project repealed a proportional cap on index lines after measurement and bans limits with no derivation, so "keep headings under N characters" would be that same defect returning by another door. Word order is checkable by reading and needs no number.

Existing headings are not rewritten in this pass. Sixty-odd headings edited mechanically in a file the hooks parse is real risk for a cosmetic gain, and it is a separate decision that can be made once the rule exists and its effect on new headings is visible. Not filed as its own item: if it matters, it will be obvious from using the queue.

The reader-awareness half — merged in from another capture — resolves to "carried already", which was named as an acceptable outcome when it was merged. A generic orientation sentence saying "these documents are read in a viewer" states a fact with no action attached, which is the shape the wording rule rejects; the front-loading rule is the operative consequence.

The user-specific half is not queue work and belongs to no project: that this user reads these files in a Markdown reader with an outline sidebar is true across all her projects, which by the method's own doc-routing test makes it a memory entry. Written at this close.

Rule gate: run — amends the Captures line-format block with one clause on heading word-order, with a named parent, spending no slot. One alternative refused: a heading length cap, on the derivation rule.

FAQ: not needed because this governs how Claude writes a heading; the user reads the queue exactly as before, only more legibly.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none.

# [HASH] — "Work item" now means an entry in Processed only, and a capture is what it was before that

The user's correction, after Claude called an Unprocessed capture a work item: only items in Processed are work items; until then they are captures or unprocessed items. They're not work until they are queued as work.

Claude's usage came from the shipped text, which is why this is a change to the vocabulary rather than a correction of drift — and that distinction set the scope. `skill-nonspecific-rules.md` used the term for Unprocessed entries in at least four places, including the sentence *defining* a capture as "one work item appended to Unprocessed", which manages to call the same thing both names inside one clause; a line setting `[user] work item` against "a plain capture" as if they were two kinds of Unprocessed entry; and the canonical-states block, which lists Unprocessed first.

The distinction is worth drawing because it is the one the method's boundary rests on. A capture is a thing anyone may file; work is what /plan has agreed. One word for both blurs the only transition the queue has, and it is the same blur that lets an undesigned capture read as though it were queued work.

**The canonical-states block needed the call the item flagged.** Titled "Work-item states" and listing Unprocessed first, it is not a model of work-item states at all under this rule. Settled as **queue states** — the lifecycle of an entry from capture to work — with a sentence saying plainly that the first of the four is not a work item. Renaming changes what the block is *of*, so that was settled before its entries were reworded.

Scope was traced by grep at processing: about 120 occurrences across 25 files, split on the user's decision. This build took the definitional and user-facing half — where the term is taught, and what she and every consumer actually read. The code half is [work-item-term-in-hook-and-script-code], and the argument against splitting is recorded rather than waved off: leaving the parser calling an Unprocessed block a work item preserves exactly the double meaning this removes, in a place she does not read.

**QUEUE.md's existing item prose is deliberately not rewritten.** It is a record, and rewriting it would edit the history of how the term was used. Only the file's header was corrected.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plan.md`, `done.md`, `next-build.md`, `setup.md`, `SPEC.md`, `QUEUE.md` (header), `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** none

Rule gate: run — admitted as a vocabulary change to existing text rather than a new rule; nothing is added to the corpus and several sentences get shorter. Failure evidence is one instance, the user correcting Claude, which is thin on its own — admitted on the stronger ground that the shipped text contradicted itself in four places. **Nothing is evicted, because nothing is added.**

FAQ: updated — new entry "Claude calls some things 'captures' and others 'work items'. What's the difference?"

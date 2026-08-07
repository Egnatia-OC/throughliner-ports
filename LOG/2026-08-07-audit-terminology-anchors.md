# [HASH] — Drifted internal terminology anchored before the compression pass can collapse it wrongly

Four families, one anchoring passage each, at the canonical site. **The fix shape is anchoring sentences, not a rename sweep** — the variants are all in use, all correct in context, and rewriting them would be a large diff to no benefit. What was missing was anything saying they are the same thing.

**The run boundary carries five names** — "cleared-to-run marker", "cleared-to-run line", "readiness line", "readiness marker", and bare "the marker" / "the line" — and the "readiness" family was never anchored to the literal `--- Cleared to run above this line ---`. `done.md` defines it only functionally. A compression pass that didn't know these were one thing could easily collapse them into two, which would be a genuine behaviour change: the run bound is the method's authorisation boundary. The anchor now quotes the literal text and lists every name, and states that no second boundary exists for any of them to mean — the only other candidate, the planning-gate marker, was retired in this same run.

**"walk-through" and "walkthrough" split fairly consistently across the corpus but the convention was stated nowhere**, so it read as accidental drift that an editor would "correct" in one direction. Now stated: hyphenated is the live drive (you and the user going through an item together); one word is the recorded steps in the item's prose that the drive reads from. One is an activity, the other a text.

**Two lesser variants anchored:** the session working file appears as "own notes", "working notes" and "working state" — one file, three descriptions; and "the queue mover" always means `scripts/reorder_queue.py`, which had no local anchor at its main use site. The mover also gained a parenthetical at the modified-on-disk rule, where naming it matters most: that rule's whole point is that the mover rewriting the file is the *innocent* cause that trains the dangerous case to be dismissed.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`
**Routed to Captures:** none

# 8e20122 — The digest's hold-chain flag replaced by a loop check, and a phrase that matched its own opposite

The digest reported three "placement contradictions" on every run, one per link of a deliberate pacing chain built on the user's own instruction. The decisive fact was found by reading the code rather than the item: `render()` already appends `Blocked by: [X] -> Processed/held` to every held item's line, so the chain was printed item by item one row above. Removing the flag deletes a duplicate, not a signal — which answers the only real argument for leaving it alone.

What replaces it walks each item's blockers with a seen-set. Terminating anywhere outside the held region means the chain releases when that end does, and nothing is reported; revisiting a slug means it never releases, and that is reported. An absent blocker is deliberately left alone: a chain ending in a slug that resolves to nothing is a wrong reference rather than a loop, and it already has two homes. Rewording the heading was refused — renaming a false flag does not make it fire less.

The same item carried a second class, found live in the session that processed it. The do-not-build phrase list matched as a substring of itself plus *into*, so a sentence saying other work must not be built **into** an item — the opposite of what the check reads — fired it. The existing discriminator cannot see that shape: there is no slug, and the sentence genuinely is about that item. A following *into* now suppresses the match.

On the live queue the contradictions count went from three to zero, all three of them false.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs-b/plan.md`, `SPEC.md`, `resources/testing/test_queue_digest.py`.

**Routed to Captures:** none.

Rule gate: not needed — this authors no rule.

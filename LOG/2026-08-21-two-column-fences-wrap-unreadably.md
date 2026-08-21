# cc33c1e — Structured explanation shown to the user goes one item per line, never in aligned columns

**Why this was worth doing.** Claude presented a rewritten ladder as a fenced block
with a label on the left and its explanation in a right-hand column. On the user's
display the right column wrapped underneath the left, the two ran together, and half
the rungs appeared to have no title. Her words: *"there's no title on half of them.
what do they mean."* The content was fine; the layout destroyed it, and a second
message in plain lines fixed it immediately.

**Why it is a capture rather than a one-off slip.** The wrapping behaviour was already
known here when the block was written anyway. The shipped procedure docs are also full
of this format — `skill-nonspecific-rules.md`, `plan.md` and `done.md` all use
two-column fenced blocks heavily, and Claude reads them at every session start, which
is the likeliest reason it keeps reproducing the shape in chat.

**The distinction the fix had to get right.** A two-column block inside a procedure doc
is read by Claude, in a wide view, and works. The same shape emitted *to the user* is
read on whatever display they have. So the rule is about output, not about the docs.

**What was built.** One clause on the View-in-doc rendering section's "How inline text
is formed" block, beside the two entries already there: structured explanation shown to
the user goes one item per line, never in aligned columns, with the reason — a column
wraps at the user's width — inside it. It is written as a continuation of the existing
entries' grammar rather than as a freestanding rule.

**Reformatting the procedure docs' own two-column blocks was refused** on the item's own
reasoning: they are read by Claude in a wide view and work, so rewriting them would fix
the half that is not broken. **A hook was refused** — nothing mechanical reads Claude's
chat output, a finding this item reached independently of
`[slug-never-explained-to-the-user]` hours earlier, which is what makes it a property of
the surface rather than of either item.

**Placement was deliberate**: this ran before the restyle passes so that
`[law-prose-restyle-heavy-docs]`'s subordination lens met the clause as part of the file
rather than after it, and did not have to handle the same text twice.

Count 308 → 311: three lines inside a typed block, each counted as a statement by
`rule_signals.py`. A rise, attributed to the added clause and to nothing else. Nothing
was evicted, as the disposition states plainly rather than dressing it up as a merge.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because this changes what the user sees, not anything they do.

Rule gate: run — admitted as a subordinate clause on the existing render rule's inline-forming block, so no freestanding rule and no always-loaded slot spent. **Nothing is evicted, stated plainly rather than dressed up as a merge.** Failure evidence is thin by count — one clear instance, your own display — and carries on cost rather than weight: the failure is visible to the user, wastes a whole message, and the fix is a sentence. **A hook was considered and refused: nothing mechanical reads Claude's chat output.**

Depth: short. Built and confirmed.

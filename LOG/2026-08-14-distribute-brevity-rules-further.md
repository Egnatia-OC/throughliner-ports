# 47966bb — A step's response-shape tag now governs the narration between its tool calls, not only its final message

Captured by Alex on 2026-08-13, in her words: reply length is where the fatigue
mostly comes from, and she wants to distribute this benefit as much as she can.

**The item was narrowed at processing to the one limb that is not repetition**,
and the narrowing argument came from the item's own counter-argument. The original
surveyed four surfaces to copy the cadence rule onto — the consumer template, the
always-loaded communication rules, and the four skill prompts. Three of those are
repetition, and the research this whole set was built from says repetition is not
the lever: the one-at-a-time rule is already stated in three layers and still
slips, which is why the previous fix was a shown specimen rather than a fourth
statement. Copying it into three more files would also have worsened the
three-layer masking problem another item in this run was making visible.

**The gap that remained is real coverage rather than another copy.** The tags bound
what a *step* outputs. Nothing bounded the narration emitted *between tool calls*
while a step runs, so a step could be tagged for brevity and still produce several
paragraphs on the way through. One line in the tags block now closes that.

**Rule gate: run** — a clarification of what the existing tags already cover,
written into the tags block's opening statement rather than as a freestanding rule,
so it is subordinate to the parent it amends and adds nothing to the corpus.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none.

# 0e62afe — Work can be held until a date it names itself, across the queue's whole surface

`Blocked by: [slug]` was the only way to hold work, and it always names a queue item. A date is not a queue item, so a date had to be expressed by proxy: a capture that a human confirms. Four Discord posts were held that way behind an item whose entire content was "a day has passed" — costing a planning session per post to answer a question a calendar answers, and failing anyway. The user's words on the failure: "it wasn't presented to me in next." Holding the item below the readiness line made it invisible during ordinary use, so the pacing did not slow the post down, it stopped it happening.

A third failure surfaced while re-reading the chain, and it is the one that settles the design: blocking each post on the previous one implements *order*, not one-a-day. Post 2 lifts the moment post 1 closes, in the same session, on the same day. The rule the user stated has never been mechanically in force.

An item may now carry `Not before: YYYY-MM-DD` on its own line, and it holds the item on its own with no blocker item standing in for it. A date earns a field where the standing answer is "don't invent queue machinery" because it resolves itself: every other blocker needs a human or a build, while a date is read off the calendar by the hooks and costs no attention at all.

The change reached every place the queue's holding facts are read: the always-loaded line format, /plan's below-line revisit and its keep-step placement, `done-plan.md`'s two sites, SPEC's account of lifting shelved work, the queue lint's below-line check, `session_start`'s dependency facts and the digest's per-item line. Two things were checked against the code rather than reasoned from the discussion, per the hook-format rule: the lint hard-rejects a below-line item with no `Blocked by:`, so it had to learn the field or the shape could not ship; and `FORMAT_EPOCH` does not bump, because the field is optional and every existing project's files stay structurally valid. `reorder_queue.py` was read and left alone — its three `Blocked by:` mentions all resolve slug references, a date names no slug, and blocks travel byte-for-byte.

**What this build deliberately did not do:** give the four Discord posts their dates. Which day each post goes is a decision the user owns, and dating them is processing, which belongs to /plan.

**Files touched:** `plugin/throughliner/hooks/post_tool_use.py`, `plugin/throughliner/hooks/session_start.py`, `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plan.md`, `done-plan.md`, `SPEC.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `resources/testing/test_queue_lint_flags.py`, `test_queue_digest.py`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the `Blocked by:` line-format block rather than a freestanding rule. It passes the subordination test: the block already holds parallel marker lines, this is a fourth, and it is not a complete sentence. **Nothing is evicted**: this is a net addition, offset only by the wake-up-capture pattern falling out of use for date cases and by two sentences being reworded because they go wrong. Do not read that as a balanced trade.

FAQ: updated — new entry "A queue item says 'Not before' and a date. What is that?"

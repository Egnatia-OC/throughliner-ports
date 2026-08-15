# [HASH] — Two mechanical checks in the queue lint, after three prose remedies failed

This item carried the longest chain in the queue: a shipped, always-loaded provenance rule broken in the very session that read it; a hook ruled out early because a lint sees only text and nothing in a finished item distinguishes reasoning Claude produced from reasoning the user gave; sharper wording tried and spent; attribution holding across nine items while volume grew anyway, which showed the two halves are separable; and a fourth instance carried over from a deleted item.

The waiting condition was discharged this week and the third remedy failed. The length rule shipped 2026-08-13, August was split at that date, and capture length **rose** — median 321 to 396 words, mean 368 to 461, n=152 after. Three caveats are on file and none rescues it. All three remedies to date were prose, and the last has a measured non-result, so the ban on designing a non-prose mechanism is discharged.

Both checks go in the queue lint, which fires after every QUEUE.md edit and reports without blocking. That is the right register: the failure happens at the moment of writing, so the report belongs there rather than in a digest read hours later.

**Credit without a quote is flagged.** An item whose prose asserts user authorship must contain an actual quoted string. This is the shipped rule's own bar made checkable rather than restated — the rule already requires the user's own words as the source of a credit, and this asks the item to show them. Straight quotes, typographic quotes and blockquotes all count; the check is deliberately generous, because it exists to catch an item quoting *nothing*, not to police quote style.

**Word growth is reported per touched item**, as a bare fact, with no threshold and none permitted: a threshold here would be a bare number, and the research it rests on states that no band may be read off this corpus because this corpus is the bloated one. The baseline needed a decision the item could not anticipate — a hook is handed no before-image, so "the file's prior content on the same edit" is not available. A cached copy on disk was rejected as a state file that must be maintained, where the first session that forgets makes the output lie. The baseline is the queue as last committed, which needs nothing kept in step and matches the state a session's work started from.

**What neither check does, recorded so the build cannot be read as claiming otherwise.** Neither can identify invented reasoning. The first raises the cost of an unsupported credit from nothing to fabricating a quotation, which is a real difference and is not verification. The second makes growth visible and enforces nothing. Both convert something silent into something a reader can point at — the one mechanism in this project with a record of working.

Six existing items flagged on the first run, all written before the check existed. They are deliberately left alone: rewriting existing item prose edits the record.

**Files touched:** `plugin/throughliner/hooks/post_tool_use.py`, `resources/testing/test_queue_lint_flags.py`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** none

Rule gate: run — admitted, and it authors **no rule at all**: two mechanical checks are added to a hook and no always-loaded text grows. That is the point of the item, so a prose amendment here would contradict the finding that licensed it. **Nothing is evicted, and nothing needs to be:** the eviction question is about rule-text budget, and this adds none.

FAQ: updated — new entry "Claude mentioned word counts and a missing quote after editing my queue. Is something wrong?"

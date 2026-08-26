# [HASH] — Word-growth counter excludes the readiness marker, so moving the line stops inventing deltas

After a below-line lift — a mover call plus one edit to that item's own block — the
advisory word-growth report claimed a different item had lost 8 words, an item no
edit in that session had touched.

**The cause was established by checking rather than assumed**, which the capture
explicitly asked for. The named item's text between HEAD and the working tree was
byte-identical; the whole delta was the readiness marker. The lint's per-item
counter ran each span from its heading to the next one, so the marker line's eight
words counted as the adjacent item's — and moving the marker at the lift made that
item appear to shrink. Any item next to the marker gains or loses phantom words
whenever it moves.

The marker is not part of any item. It sits between them, which is exactly why it
falls inside whichever span happens to follow it. Excluding it from every span is
the whole fix.

The lint is advisory, so the cost was never blocked work — it was a report that
sends the reader to look at an item that did not change, which is worse than no
report at all.

**Files touched:**
`plugin/throughliner/hooks/post_tool_use.py` — `_item_word_counts` excludes the
readiness marker from item spans.
`resources/testing/test_queue_lint_word_growth.py` — new suite, 6 cases.

**Routed to Captures:** none.

Tick form: done, confirmed — 6 cases passing: the marker moving in both directions,
an item directly above it, and two cases proving a genuine edit is still counted and
that an edit made alongside a marker move reports only the edit.

Rule gate: not needed — a counting fix in a hook script, no rule authored or
amended.

**Also in this item's build:** a `sed -i` reached for while correcting a test
expectation was refused by the scripted-write guard, correctly. The editing tools
were used instead.

# [HASH] — The routing table asks what a thing is, not whether it will get built

Two changes to `skill-nonspecific-rules.md`. The routing table's first row read
"a standing design consideration unlikely to be built", and "unlikely to be
built" is a prediction Claude makes about work the user might want — acting on it
by routing the thing out of the queue is a fate decision wearing a routing
decision's clothes. The row now reads "a principle that governs how work is
done", with an example, so the test is what the thing *is*. Above the table, a
guard: routing never re-opens a fate the user has already decided.

Deleting the row outright was weighed and rejected. It is simpler and matches the
user's framing — *"everything is QUEUE. It's never not the queue"* — but it loses
the real case, a governing principle pushed into a work queue where it sits
unbuildable forever, failing the keep-check at every /plan.

The guard is the half that would actually have stopped the failure. A correctly
worded row would not have: the error was re-deciding something already settled,
and any destination table can be reached for in that state.

Rule gate: run — admitted as an amendment; both changes are subordinate to the
existing table and the rule above it, so neither spends a slot. One recorded
instance: Claude cited this row as authority for routing out a concern the user
had instructed be kept.

FAQ: not needed because nothing a consumer meets changes except Claude no longer
offering to route their concern somewhere other than the queue.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none

# 7c9922a — session_start names the resolved blocker graph, and /plan reads a mechanical digest instead of the whole queue [hook-emits-counts-not-the-graph]

Mixed authorship: the user found it — they asked why Claude read the queue and reasoned over it again before using the mechanical mover, and held the Discord post's own promise against the behaviour ("anything a hook computes is free… the graph moves into the session-start hook and arrives as fact"). They also chose the wider of the two options offered. The diagnosis and design are Claude's.

**The defect.** `_queue_dependency_facts()` built the graph properly — walking every `Blocked by:` line, collecting held items' blocker slugs, collecting Unprocessed slugs, intersecting them — and returned three integers, discarding every slug it had resolved. Its own docstring stated the principle it then broke: every reader re-derives the graph, and when Claude does the re-deriving it costs tokens and reasoning and can carry a parse bug.

**Claude's correction to its own first framing, which changed the scope.** The capture said emitting the resolved lists would have saved the session's cost. It would not have saved most of it. Naming the lifts saves the *reasoning*; the ~57,000 tokens was the *read*, and Step 1 required paging the whole queue regardless. Fixing only the hook would leave the next session paying the same bill, which is why the narrow option was rejected.

**Why the digest strengthens the page-to-the-end rule rather than trading it away** — the reason the wider option was chosen. That rule exists because a truncated read is indistinguishable from a complete one to whatever reasons over it. A digest generated from the whole file by code cannot be silently truncated, so the guarantee is better than paging gives, not weaker. The rule gained a clause saying so, with the guard that the digest must be script-generated from the whole file rather than a partial read dressed up as a summary.

**The re-runnable form was added at the user's question**, and it matters more than it looks: `session_start` fires once, so its facts describe the queue as it stood *before* the session touched it. A /plan that has processed a dozen items would otherwise reason against a stale picture from then on. The obvious build is a one-shot Step 1 read, and that alone would have left the staleness in place.

**The cost and failure mode, stated rather than discovered.** This is a new script plus a changed read-state where the narrow option was a few lines in an existing function, and it has a failure mode the narrow option does not: if the digest omits a field a later step needs, that step reasons from an incomplete view without knowing. The mitigation is that the field list is fixed by what Step 1's queue-wide reasoning actually consumes — the droppable skim, the ordering, the below-line revisit — each of which reads headings, tags, blockers and flags, not prose.

The fourth bucket proved itself immediately: on its first run it named `[plan-reads-recent-log-index]` as holding on a blocker shipped minutes earlier in the same run.

`queue_digest.py` crashed on its first run with a `UnicodeEncodeError` on an arrow inside a queue heading, and needed the same UTF-8 console reconfiguration `reorder_queue.py` already carries. That recurrence is captured as [new-scripts-rediscover-the-utf8-fix].

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/scripts/queue_digest.py` (new), `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `SPEC.md`
**Routed to Captures:** [new-scripts-rediscover-the-utf8-fix]

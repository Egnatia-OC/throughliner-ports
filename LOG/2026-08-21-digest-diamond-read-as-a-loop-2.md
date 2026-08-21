# 7bc2c58 — The queue digest's loop check now tracks the current path, so a converging blocker chain stops reading as a cycle

`_blocker_loop` walked the blocker graph depth-first while tracking every node it had *visited*. Where C waits on both A and B and B also waits on A, A is reached twice by two different routes, and the second arrival is indistinguishable from a cycle. Nothing in that shape fails to release — A ships, then B, then C — and it is an ordinary way to say "these three land in this order".

The walk now tracks the **current path**, added on descent and removed on unwind. A slug on the path is genuinely waiting on itself; a slug merely seen before is not.

Left as it was: the multi-blocker walk, so a cycle reachable only through the second slug on a `Blocked by:` line is still caught. A test pins that, because the path fix is the kind of change that could quietly reintroduce it.

Reported by a consumer project. The flag mattered because its message invites moving a correctly placed item out of Processed — a fate decision made on a premise that was not true.

**Files touched:** plugin/throughliner/scripts/queue_digest.py, resources/testing/test_queue_digest.py
**Routed to Captures:** none
Rule gate: not needed — a code fix to a digest check; no method rule is authored, amended or evicted.

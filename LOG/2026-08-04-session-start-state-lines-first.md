# f832385 — Put the short state lines ahead of the behaviour-rules bulk at session start, restoring the red-flag surfacing

`session_start.py` assembled its injected context with the behaviour-rules block first and everything short after it: the uncleared red-flag surfacing, the project-state lines, the installed host version, and the build stamp. Only the front of the payload survives injection, so every one of those lines fell in the discarded remainder. The part worth stating plainly is that the red-flag surfacing was implemented and correct the whole time — it was being silently cut by append order alone, and a fresh session asked neutrally what it had received never mentioned the red flag that was sitting in the queue.

The fix moves the behaviour-rules block to the end and puts the uncleared red-flag surfacing at the very front, ahead of even the docset directive: it is the line that can least afford to be cut. An ordering comment now sits at both ends of the function explaining why, because nothing about the code makes the ordering look load-bearing, and the next person to append something would have no reason not to put it at the top.

Verified by driving the hook with a sample payload: the rules block now starts at character 3,544 instead of character 0, with every state line ahead of it. The ordering is also now asserted in the schema-conformance script, so a future append can't silently undo it.

One thing surfaced that this item deliberately didn't cover: the FAQ index is *also* injected in full — around 1.5KB of link list — and sits ahead of the rules block, competing for whatever survives truncation. That is adjacent work, not underspecification, so it was captured and the build continued on the decided scope.

**Files touched:** `plugin/si-plugin/hooks/session_start.py` (the order `context_parts` is assembled).
**Routed to Captures:** [faq-index-injected-as-session-start-bulk].

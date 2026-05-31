# v133 — 2026-05-29 — Session-start routing clarifications

**What shipped.** Three routing-comprehension gaps from the plugin reader test (v131) resolved across `session_start.py` and `universal-behaviour.md`. (1) Output ordering now explicit: status summary → tripwire → routing, replacing competing "first output" claims. (2) Three missing opener routes added to the routing table: bug reports, doc audits, method questions. (3) Priority ordering stated explicitly as top-to-bottom with "first matching row wins."

**Decisions taken and why.** Bug reports route to `planning.md` with `primary_intent: bug report` rather than getting a new procedure doc — they produce BACKLOG items, same as test notes. Doc audits stay `[DISCUSS]` rather than routing to planning because the audit itself is conversational; only structural findings route through planning. Method questions get an explicit row rather than relying on the catch-all because the reader test showed a stranger-Claude wouldn't know to check VOCABULARY.md.

**Pivots and surprises.** None. Straightforward doc/code edits as scoped.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 2 (session_start.py, universal-behaviour.md)
- **Carve-outs:** None
- **Claude-verified tests:** N/A (doc/text changes, no testable code behaviour)
- **User-verified tests:** 0 pending
- **Session notes:**

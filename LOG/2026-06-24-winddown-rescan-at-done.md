# ee238d1 — Add a file-only wind-down re-scan at the /done close (done.md + plan.md + plugin-behaviour.md + FAQ)

Built in a six-batch goal session (plugin off).

The wind-down re-scan only fired when a /plan session ran all the way to its end, so any session that wrapped via /done directly — a /next → /done, a fresh /done, or an early "close out now" — got no safety-net pass, and anything the user only thought out loud was lost. Verified this session against the project's history: the re-scan ran in /plan, never under /done. The fix is feasible because the re-scan only files captures — it doesn't route them — and filing is allowed in any session; only routing (promote/park/drop) is /plan-locked, and /done already files captures at its close. So a lightweight, file-only re-scan runs at the /done close without crossing the no-planning-in-execution line.

Changes:

- **done.md** — a new "Wind-down re-scan (file-only)" section in the shared flow, wired through a pointer at the top of Commit core so it runs at every /done close regardless of session type without editing each sub-doc. It re-reads the session's discussion, surfaces un-flagged candidates as one bulk-approval numbered set, files the approved ones to Captures with no routing, and adds them to the entry's "Routed to Captures:" line as a working-tree edit riding the commit. Framed explicitly as capture-making (allowed at close, like the post-close capture step). States the fresh-chat limit (a fresh-chat /done has nothing in view) and that it's a harmless no-op when /plan already ran its own wind-down this session.
- **plan.md** — the wind-down re-scan's framing is updated: /plan still owns the full re-scan (file + carry into routing), but the filing half is no longer /plan-exclusive — /done runs a file-only version, while routing stays /plan-only. The earlier "/done is deliberately not a home" stance is replaced by this file-only carve-out.
- **plugin-behaviour.md** — the no-planning-in-execution boundary is made explicit as filing-allowed-anywhere vs routing-/plan-only, so the /done re-scan is clearly on the allowed side; /done closes are added to the scope list.
- **FAQ** — an entry on /done surfacing a couple of things you mentioned but didn't capture and filing them for a later /plan to sort, plus its index line.

This revisits the prior [plan-winddown-rescan] decision on new evidence (the user's actual habit is to invoke /done directly). One inherent limit, not a gap to fix: a fresh-chat /done has none of the thinking in view, so nothing to re-scan — only capturing-as-you-go covers that. Deferred host-side line written (the doc text landing is a review, not a pass/fail test).

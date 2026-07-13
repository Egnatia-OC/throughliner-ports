# [HASH] — /plan places ready [user] work above the cleared-to-run marker; /next hands it over collaboratively

Fixed the gap where /next handed over no `[user]` work though the queue held ready `[user]` verification lines: those lines sat *below* the cleared-to-run marker, and /next builds and hands over only from above it. Chosen direction (over Option B, "make /next surface ready `[user]` work regardless of the marker"): keep the marker as the single **positional** gate for both builds and handover, and fix it in /plan. The user prefers one gate over a second readiness check inside /next.

Two changes. In plan.md's Step 3, when positioning the marker, /plan now places a `[user]` line *above* it once the work it depends on has shipped (prerequisite met, re-derived from LOG the same way the hold-back rule re-derives dependency state); a `[user]` line whose prerequisite is still pending stays below. In next.md's handover branch, handover is now **collaborative** — /next states what the user needs to do and why it's theirs, then offers to run what it can, explain in plain words, and walk them through it step by step; the `[user]` tag marks who witnesses the step, not that Claude steps back. A consumer FAQ entry covers the collaborative handover.

**Files touched:**
- plugin/si-plugin/docs/plan.md — Step 3 gains the "place ready `[user]` work above the marker" paragraph
- plugin/si-plugin/docs/next.md — reworked Handover branch
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line

**Routed to Captures:** none

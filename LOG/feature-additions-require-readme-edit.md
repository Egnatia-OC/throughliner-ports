# [HASH] — Added standing README-sync trigger rule in CLAUDE.md; updated README.md to current method (five commands, two-section model)

The README had drifted from the shipped method — still said "four slash commands" (missing /cruise), framed the scope-lock around "the current batch" (retired vocab), and claimed SPEC is "read-only during builds" (SPEC is now a normal doc any work line can list). Rather than a standalone README-sync trigger, the fix piggybacks on the existing SPEC-sync discipline: a user-facing feature change already must update SPEC, so the README sync rides that same moment — one more clause on a trigger that already fires, not a new detection point. Also updated CLAUDE.md's Architecture section (4→5 skills, QUEUE.md description to two-section model, /next description to "build or audit") and corrected the red-flag framing throughout the procedure docs — red flags are markers on work lines, not work lines themselves.

**Files touched:**
- CLAUDE.md: added README feature-list sync trigger rule; updated Architecture section; corrected red-flag framing
- README.md: five commands incl. /cruise, current scope-lock and hooks framing, /cruise in How to use it, dropped "batch" vocab
- plugin/si-plugin/docs/plugin-behaviour.md: corrected red-flag framing (marker on a work line, not a type of work line)
- plugin/si-plugin/docs/plan.md: corrected red-flag framing in two places
- plugin/si-plugin/docs/done.md: corrected red-flag framing
- plugin/si-plugin/docs/done-plan.md: corrected red-flag framing
- QUEUE.md: corrected red-flag framing in header description

**Routed to Captures:** [faq-four-commands-stale], [next-renders-cruise-obsolete]

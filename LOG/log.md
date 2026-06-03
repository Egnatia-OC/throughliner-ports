# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## a8a7c28 — Add operating conditions section to README

**Files touched:**
- README.md: added "Operating conditions" section between "Install" and "Getting started"

**Tests:** None (doc-only change)

**Why:** The README had install instructions but no guidance on what environment the plugin is tested under. Users need to know the difference between hard prerequisites (/setup) and soft assumptions (model, mode, context hygiene) so they can troubleshoot when something doesn't work as expected.

**Routed to Captures:** next.md Step 1 "No active build" narration wording (captured during /next)

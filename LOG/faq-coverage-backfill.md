# [HASH] - FAQ: add the commit-and-push and project-out-of-date/run-/setup entries

Two consumer-facing moments had no FAQ answer. Added an entry on committing vs pushing (commit saves locally and always happens; push also sends to a remote backup if one exists; no remote means no push offer) matched to the commit-then-offer-push shape, and an entry on the project-out-of-date drift signal (the plugin gained scaffolding this project lacks; /setup backfills what is missing and does not overwrite or reconcile written content). The drift entry matches session_start.py's catch-up message and the what-/setup-does entry so the three agree.

**Files touched:**
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none

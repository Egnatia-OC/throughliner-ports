# 15e10c9 — /setup's migration now refreshes the plugin-managed CLAUDE.md block, and the marker promises what actually happens

Build entry; the planning record is `2026-08-21-managed-claude-md-block-never-refreshed.md`. From a consumer project's INBOX report: the managed block promised "updated on /setup and plugin reinstall" and never was, so for weeks every session there read a retired queue model as current — and four of their own rules had drifted inside the block, which any blind refresh would have deleted.

Both halves built. setup.md's migration gains step 3c: compare the project's PLUGIN-MANAGED region against the installed template's; where they differ, say what will be replaced, move non-template text below the end marker (and say so), then replace the region. The never-overwrite rule names this as its one carve-out. The template's marker now states the true promise and tells the user their rules belong below the end marker. FAQ entry "Why did /setup rewrite part of my CLAUDE.md, and is my own text safe?" shipped with index line, both copied to `FAQ/`.

**Files touched:** `plugin/throughliner/docs/setup.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`, `plugin/throughliner/templates/faq-template.md`, `plugin/throughliner/templates/faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.
**Routed to Captures:** none from this item.
Tick: done, confirmed — edits read back; copies re-copied.
FAQ: updated — "Why did /setup rewrite part of my CLAUDE.md, and is my own text safe?"
Rule gate: run — admitted as an amendment to /setup's migration step: the backfill-never-overwrite rule gains one carve-out for the plugin-managed region, which is method-owned content the promise already claimed was kept current. The marker's old promise text is evicted and replaced in the same move. No freestanding rule, no always-loaded slot.

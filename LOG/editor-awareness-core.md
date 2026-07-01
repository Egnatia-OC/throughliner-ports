# [HASH] — Build [editor-awareness-core]: record the user's .md editor at /setup, stored in the generated CLAUDE.md

First batch of a two-batch goal run for the Pro-budget token push. Adds a per-project record of which `.md` editor the user works in, so a later session can point the user to their open docs with a link instead of re-pasting doc-resident text into chat (the payoff the sibling batch [view-in-doc-group-a] then spends). Minimal slice of the parked [editor-awareness] capture — the web-search-its-capabilities remainder stays parked.

Shape: a once-off, skippable interview question (Q6) added after the five SPEC/QUEUE questions in setup.md, framed plainly with an easy "just say skip"; Step 4 writes the answer into a new Editor field in the generated CLAUDE.md, or `not recorded` when skipped. The field lives in the plugin-managed block of CLAUDE-TEMPLATE.md next to Language, defaulting to `not recorded` so absence is representable — which is what lets the consuming batch degrade safely (no editor → inline quote). An FAQ entry ("Why does setup ask which editor I use?") ships with the index line, and this dev project's own CLAUDE.md records Editor: Zettel so it benefits immediately (host-only, not shipped).

No SPEC change: SPEC only says /setup "runs the onboarding interview" — no question count or editor detail — so the optional question makes no SPEC sentence wrong. Known gap filed to Captures: the Step 2C migration re-scaffold adds missing files but not new fields, so projects already adopted don't get the Editor field (and so the token win) until a manual add — same content-level drift shape as [scaffolding-resync].

**Files touched:**
- plugin/si-plugin/docs/setup.md — Q6 (optional editor question), Step 4 write step (2a), Step 2/3 scaffold notes
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md — Editor field (default `not recorded`)
- plugin/si-plugin/templates/faq-template.md — "Why does setup ask which editor I use?" entry
- plugin/si-plugin/templates/faq-index-template.md — index line for the new entry
- CLAUDE.md — Editor: Zettel recorded in User context (host-only)

**Routed to Captures:** Editor field isn't backfilled into already-set-up projects (migration re-scaffold adds files, not fields)

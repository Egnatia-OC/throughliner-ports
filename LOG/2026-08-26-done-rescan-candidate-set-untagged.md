# 3b094b5 — Both candidate-set steps gain [PROMPT], moving the wait out of prose and into the tag

A compliance-audit finding: done.md's wind-down candidate-set step and rescan.md's work-still-to-do step both wait for the user — "the user contests by number or says go; the writes then land" — while carrying no `[PROMPT]` tag. The wait lived in prose, which is what the response-shape tags exist to replace.

Behaviour is unchanged. The prose already directed the wait; the tag puts it in the shape every step is checked against, so a reader scanning tags no longer sees two waiting steps that look like non-waiting ones.

rescan.md uses tags elsewhere, so it is not a deliberately tag-free doc like the migration checklist — the omission was an oversight rather than a house style.

Nothing was refused on this one.

**Files touched:** `plugin/throughliner/docs/done.md`, `plugin/throughliner/docs/rescan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment putting an existing rule into the required response-shape form; nothing evicted.

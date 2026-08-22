# [HASH] — skill-nonspecific-rules.md Communication — removed the quiet-work and regression-tone bullets, evicted to the shipped brevity style

From the style-level dedup audit ([style-dedup-evictions]): two rules were near-verbatim duplications of pure tone steering the shipped brevity style carries at a level above the docs — "Speak when something warrants it, and work quietly between" and "State a regression in the same plain terms as a success, and move on." SPEC's dedup rule is the ground: a rule carried at style level is stated there and nowhere below it. Both degrade gracefully where the style is absent — a session runs slightly more verbose, nothing breaks. The audit's third finding (a "state the count" clause carried three times) did not survive verification at processing and its trim was dropped as already satisfied; INBOX/sent.md was grepped and no post announced either rule.

Tick: done, confirmed (grep: neither sentence remains in docs/).

Rule gate: run — pure eviction, nothing added; the shipped brevity style is the named replacement, already carrying both rules near-verbatim at a level above the docs.
FAQ: not needed because the change alters no user action — the same steering still applies through the style.

**Files touched:** plugin/throughliner/docs/skill-nonspecific-rules.md
**Routed to Captures:** none

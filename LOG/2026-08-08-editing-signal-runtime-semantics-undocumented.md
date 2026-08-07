# 3633c7d — SPEC's editing-state contract documents runtime semantics: per-edit firing, mtime freshness, path-comparison policy

Built in the 2026-08-08 overnight blitz. SPEC's contract gains a new bullet stating the signal fires per edit-tool call rather than per build, that a naive reader will flicker and needs to hold briefly past `active: false`, and the trade-off that decides the hold's length — with no number published, deliberately, per Understudy's own answer that their three seconds was reasoned rather than observed and publishing it would launder a guess into the interface. The reader-policy bullet is rewritten: freshness comes from the marker file's own local modification time, with the published reason being **failure direction** rather than clock arithmetic (a wrongly-old mtime fails open, a foreign-clock `written_at` fails closed into a permanent lockout — reasoning that survives whatever any sync client does), `written_at` named as diagnosis-only, path comparison stated case-insensitive on Windows, and relative paths carrying no leading `./`. Understudy's weaker same-clock justification is deliberately not published; they should be told the published reason is the one to carry.

**Files touched:** SPEC.md
**Routed to Captures:** none
FAQ: not needed because the contract's readers are companion-app developers and SPEC is the contract's home.

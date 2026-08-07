# [HASH] — Behaviour rules: a zero search result is not a finding until the search itself is confirmed working

Built in the 2026-08-08 overnight blitz, run 2 — the capture was processed autonomously under the blitz's softened bar (departure recorded): its own text leaned to the answer taken, a clause on the existing it-ran-versus-it-worked rule rather than a new entry in an already-large family. The clause, in `docs-b/plugin-behaviour.md`'s diagnosis-order section: a search returning zero or empty is confirmed against a known-non-zero case before it counts as evidence of absence, because a broken filter and a true absence produce identical output; composed filters are where it bites, so prefer the literal search over the clever one when the result will decide something. The live instance (an `awk` range that never matched, counting a confident zero five commits over) rides in as the why.

**Files touched:** plugin/si-plugin/docs-b/plugin-behaviour.md
**Routed to Captures:** none
FAQ: not needed because this governs Claude's own verification tooling, invisible to a consumer.

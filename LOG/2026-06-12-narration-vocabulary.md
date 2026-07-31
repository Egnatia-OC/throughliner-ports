# LOG entry — narration-vocabulary

## 8f2cab4 — /next [narration-vocabulary]: plugin-behaviour.md Communication gains a Vocabulary section naming background-only terms with the translate-or-omit narration rule

The no-jargon rule already banned internal procedure terms in user-facing chat, but it relied on Claude judging which terms count as internal. Leakage observed in a /plan session ("the loop," "Step 2") showed the abstract rule missing the actual offenders. The fix names them. plugin-behaviour.md's Communication section now ends with a Vocabulary subsection listing the background-only terms — loop, Step N, Phase X, sub-step, pass, gate, pre-flight, batch slug, response-shape tag names, and procedure-doc filenames — with the translate-or-omit rule and two examples ("the loop" → "the next item"; "Step 2 comes next" → say what happens instead). One boundary was added while drafting: quoting an artifact the user co-reads (a queue entry, a draft, a log line) is not narration, so quoted text stays verbatim — without this, the rule would collide with verbatim-first quoting. The cross-link landed both ways: the plain-language bullet points forward to the new section, and the section states it sharpens that rule by naming offenders rather than replacing it, with the list explicitly open so unnamed internal terms stay covered by the general rule. One anchor question resolved at build time: the batch's "no internal terms in user-facing chat" reference maps to the plain-language bullet — no other rule in the shipped doc covers internal terms; the fuller audience statement lives in this project's CLAUDE.md, which is host-only. Inline marker-based enforcement stays parked, watching for leakage after this ships. The batch's self-verifying test can't run in this session — the injected rules only carry the new section after push and reinstall — so it went to Deferred tests. Pre-flight also backfilled the previous session's two placeholder hashes to 9f1b80b.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — Vocabulary subsection added at the end of Communication; plain-language bullet gains the forward pointer
- QUEUE.md — [narration-vocabulary] batch removed at scope-lock; deferred-test line added at close
- LOG/doc-crossrefs-by-name.md, LOG/index.md — placeholder hashes backfilled to 9f1b80b at pre-flight
- _build.md — created at scope-lock, deleted at close

**Routed to Captures:** none

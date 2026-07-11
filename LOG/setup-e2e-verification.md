# 0047b36 — E2E /setup verification across folder states (partial)

Ran the [setup-e2e-verification] test batch as user-run E2E on host 1.15.0-test1, reading the raw session transcripts (PFA-5, a fresh empty folder; Hexboard, a content-bearing migration folder). Closed partial — two of the four planned scenarios (leftover-REGISTRY re-run, and a Case C leftover-`_build.md` close) weren't run, and the session-start migration message wasn't seen because /setup was typed directly; all three routed back to Deferred tests for dogfooding.

**Tested:**
- [setup-preexisting-content-handling] — ✓ (Hexboard): /setup peeked at the existing plan doc before Q1 as framing only ("tell me in your own words"), left the original files untouched, and named them in the close.
- [migration-aware-setup] — ✓ /setup migration-framing half (Hexboard mapped the old plan into SPEC/QUEUE with role-fit guardrails, plain language); session-start-message half deferred.
- [setup-closeout-redesign] — ✓ fresh-folder path (PFA-5: silent git init, close-out named /done, /done wrote a setup-shaped LOG entry + committed, no-remote → no push); Case C branch deferred.
- [retire-registry] — ✓ fresh-scaffold half (three docs, no REGISTRY, no missing-REGISTRY flag; both runs); re-run-retire branch deferred.
- Bonus deferred tests confirmed and cleared: [editor-awareness-core] (Q6 asked + Zettlr recorded, both runs) and [winddown-rescan-at-done] (Hexboard /done re-scanned, surfaced the un-filed key-manifest item, filed before commit).
- Positive: Hexboard /setup caught a real contradiction (predictive-text answer vs the old plan's "deferred" line) and had the user resolve it before writing SPEC.

**Routed to Captures:** [view-in-doc-remote-control-tension], [research-folder-always-in-scope], [setup-editor-ask-wording-fix], [setup-faq-folder-ordering] (all filed mid-session; a research detour on copy-vs-generate plus two /setup rough edges observed in the transcripts).

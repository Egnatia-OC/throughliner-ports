# V26 — 2026-05-17 — TEST-LOG.md mechanism + Drafts in flight convention + V25 carry-over bugfixes

**What shipped.** New consumer-side TEST-LOG.md doc class (8 columns, phase-based pruning) with templates (×2) and DOC-STRUCTURE spec. Five protocol rules placed across NO-CODE-METHOD phases. CLAUDE-TEMPLATE (×2) gains TEST-LOG in path block; scaffold.py extended. Reference manual: *Three disciplines* → *Four*. Three V25 carry-over bugfixes absorbed (#041/#042/#044; plus `/build` parser-path bug). Session-open recovery: CLAUDE.md gains inputs-must-be-in-repo scan rule; BUILD-METHOD gains *Drafts in flight* convention; `planning/drafts/` folder created. Parity audit: 17 edits across 8 files. 21 footers bumped V25 → V26. No smoke tests — doc-only on the gate.

**Decisions.** Rule 2 relocated mid-session from *After every build* to *During planning* — testing window spans sessions. Hybrid enforcement of Rule 3: hook is load-bearing gate, planning's read-back is the UX. Rule 5 "substantially changed" punted to Claude's judgement + reasoning trail. *Drafts in flight* convention added as recovery — V26.md cited an input that was never committed (V20→V26 failure).

**Pivots.** `/build` parser-path bug caught by carry-over sweep (project-relative path; plugin isn't in project tree). Pre-existing "5 templates" off-by-one coincidentally fixed by TEST-LOG addition. Parity audit surfaced more drift than expected.

**Carried forward.** Three code carry-forwards (SPINE_FILENAMES, PLUGIN_METHOD_VERSION comment, docstring count) → V27.


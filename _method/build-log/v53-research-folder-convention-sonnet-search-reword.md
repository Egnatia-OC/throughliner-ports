# v53 — 2026-05-22 — Research folder convention + Sonnet-search reword

**What shipped.** Scope 0051. (1) `/setup` scaffolds `research/` folder; all "prompt user for Sonnet search" language replaced with "research directly, save to `research/<topic>.md`." (2) New `research/` folder spec in DOC-STRUCTURE.md + VOCABULARY entry. Updated universal-behaviour.md (verify-external-facts rule), Reference manual, scaffold script, setup subagent. Footer V48→V49; plugin 0.48.0→0.49.0.

**Decisions.** Free-form kebab-case naming (research is reference, not sequence). Brief one-sentence chat mention when writing research. `[UNVERIFIED: <what>]` fallback when tools unavailable.

**Pivots.** Only two files had Sonnet-search language (universal-behaviour, Reference manual). Session spanned two context windows.

**Carried forward.** Deferred smoke tests (V43–V51). OQ V51 entry removed.


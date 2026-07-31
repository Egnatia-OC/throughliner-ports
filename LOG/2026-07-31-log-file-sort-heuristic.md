# [HASH] — Date-prefixed all per-entry LOG filenames (YYYY-MM-DD-…) so LOG/ sorts newest-first — full migration + done.md convention change

LOG entries are per-entry files named by slug/title, so a filename sort of the LOG folder didn't surface newest-first. Scheme (settled): prefix each per-entry filename with the session date so a descending name-sort (which Zettel does) puts newest at top. Going-forward-only fails — new digit-leading names and legacy letter-leading slug names would sort as separate blocks — so the existing files were renamed too.

Migration: 258 per-entry files renamed via `git mv` (history preserved). Type-dated files (plan/handmade/freeform/setup) were rewritten date-first (`plan-2026-06-12.md` → `2026-06-12-plan.md`) rather than double-dated; slug files were dated from their index-line commit hash, falling back to git add-date; slug files not referenced in the index were git-add-dated. The pre-split monoliths (log.md, log-v*.md) were left untouched. A first pass caught a real bug — the monolith-exclusion regex missed `log-v1.10.0.md` (dots after the version), which would have wrongly renamed the monoliths; fixed before applying. LOG/index.md links were rewritten in lockstep (both `→` and `->` arrow styles handled). Verified after: 0 broken index links, 0 undated per-entry files remaining, folder sorts newest-first.

Going-forward: done.md's LOG-entry naming convention now writes new entries date-first (`LOG/<YYYY-MM-DD>-<slug>.md`, `LOG/<YYYY-MM-DD>-<type>.md`), with a note that the prefix is the session date, not the hash. plugin-behaviour.md Index entries needed no edit — its filename rule already defers to done.md. FAQ "how do I know what was done in a previous session?" extended to note the date prefix. (This session's own five entries are written under the new dated convention.)

**Files touched:**
- plugin/si-plugin/docs/done.md (naming convention)
- plugin/si-plugin/templates/faq-template.md
- LOG/ (258 per-entry files renamed)
- LOG/index.md (links relinked)

**Routed to Captures:** [scratchpad-scope-lock-conflict] — the scope-lock blocked writing the migration script to the scratchpad; filed as a method-improvement idea.

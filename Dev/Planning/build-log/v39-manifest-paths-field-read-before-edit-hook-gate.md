# V39 — 2026-05-21 — MANIFEST paths field + read-before-edit hook gate

**What shipped.** Optional `(path)` field on MANIFEST entries (three shapes: single, list, directory). PreToolUse check (6): denies first edit on MANIFEST-covered file with inline context; retries allowed via transcript-scan marker. Spine docs exempt. After-build populates paths on touch (incremental migration). Rule rewritten from "check first" to "have context by edit time." OQ resolved. Smoke-tested: 7 cases Pass (#116–122). Footer 38→39; plugin 0.38.0→0.39.0.

**Decisions.** Shape B (transcript-as-state) over shape A (state file + cross-hook). Half the implementation, same guarantee. Paths optional (no flag-day for mid-flight projects). Three shapes cover single/list/directory without forcing artificial granularity.

**Pivots.** Bash `cd` shifted plugin cwd mid-session — adoption gate fired against dev project. Recovered with second `.no-code-method-skip` at `sovereign-implementer/` root. New OQ logged for cwd-shift issue.

**Carried forward.** New OQ (cd-shifts-cwd). `.no-code-method-skip` at repo root committed.


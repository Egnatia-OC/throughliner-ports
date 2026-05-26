# v90 — 2026-05-26 — BUILD-METHOD split and dev-side proxies

**What shipped.** Scope 0092. Split `BUILD-METHOD.md` (329 lines) into `planning/session-protocol.md` (~112 lines, always read) and `planning/session-reference.md` (~185 lines, dip on demand). Created `planning/.proxies/` with three proxy files: session-protocol, session-reference, and a routing-aware BACKLOG proxy that shows only active/queued batches and OQ summaries. Updated 16 references across CLAUDE.md, build-log/INDEX.md, test-log/INDEX.md, BACKLOG.md, drafts/.gitkeep, and session_start.py. Deleted BUILD-METHOD.md. Dev-internal only; no footer bump.

**Decisions taken and why.** Protocol file gets lifecycle sections (open/middle/close/parity) — these are needed every session. Reference file gets entry shapes, footer lists, testing details, planning artefact lifecycles — consulted on demand. Names `session-protocol.md` and `session-reference.md` chosen for clarity. Both placed inside `planning/` to match plugin-side convention (only CLAUDE.md at root). Dev-side proxy format follows plugin-side spec with two divergences: "when to read" timing hints in the HTML comment header, and BACKLOG proxy is routing-aware (shows active/queued only, with OQ dispositions).

**Pivots and surprises.** Found 0093 scope file contained inaccurate claim that plugin-side BACKLOG lives at project root — corrected to `_method/`. Also marked 0091 as shipped in BACKLOG (was unmarked) and updated OQ "Scope file split" next step since its 0091 condition had fired.

**Carried forward.** OQ "Scope file split" — 0091 condition met, still parked until concrete split design emerges.

# V36 — 2026-05-21 — OPEN-QUESTIONS doc-only bundle: TEST-LOG newest-first, BACKLOG authority, plan-panel resolved

**What shipped.** Three doc-only items + method-version catch-up (34→36, skipping 35). (1) TEST-LOG flipped to newest-first across DOC-STRUCTURE, templates, after-build, planning. Transition stance for existing rows. (2) BACKLOG-authority sentence in planning.md (not universal-behaviour.md — scope file was wrong, caught at edit time). (3) Plan-panel resolved: research confirmed not programmatically writable. Collapsed to Reference manual caveat pointing at BACKLOG for build sequence. OQ entry removed. No smoke test (doc-only). Parser ordering-agnostic — no code change needed.

**Decisions.** BACKLOG-authority in planning.md (phase-specific, not cross-phase). Plan-panel as caveat (not standalone section). Footer 34→36 (V35 dev-internal, didn't bump).

**Pivots.** Scope file named wrong target file — caught at edit time. Footer-bump parallelism hit Read-before-Edit requirement on 16 files.

**Carried forward.** V37 queued. 11 OQ entries parked. Plan-panel research file retained.


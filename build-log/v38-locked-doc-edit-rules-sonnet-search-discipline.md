# V38 — 2026-05-21 — Locked-doc edit rules + Sonnet-search discipline

**What shipped.** Three discipline changes resolving three OQ entries. (1) Footer-stamp carve-out: `is_footer_only_edit()` + regex lets footer-only `Edit` calls pass locked-doc check (`Write`/`MultiEdit` still blocked). (2) Preview-then-fold-in convention: subagents preview SOT edits in chat, get approval, write fold-in block, prompt immediate fold-in. (3) Verify-external-facts rule: web-search or paste-ready Sonnet prompt; fallback `[UNVERIFIED: <what>]`. Three OQ entries removed. Footer 37→38; plugin 0.37.0→0.38.0.

**Decisions.** Preview convention (not planning-context carve-out) — hook can't identify caller, so lock stays intact. `[UNVERIFIED]` as fallback (not hard block) — user can't always run searches. Footer carve-out Edit-only (Write/MultiEdit too broad to verify).

**Pivots.** adopt.md case 4 recap template stale — caught in parity audit. Context ran out mid-session (resume accurate).

**Carried forward.** No smoke test (needs consumer build cycle).


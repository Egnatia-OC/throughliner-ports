# V64 — 2026-05-25 — After-build source-code boundary

**What shipped.** Scope 0072. Two prose changes addressing E2E round 2 findings #1 and #4: (1) after-build.md — hard prohibition on editing source files, build scripts, or any non-method file added to "What you must not do." Build failures surfaced in recap and TEST-LOG notes, not fixed inline. (2) Consent-violation pattern explicitly named and prohibited — after-build must not create conditions that override a user's explicit refusal. (3) universal-behaviour.md — "Run system commands yourself" rule added to Required behaviours, addressing finding #9 (Claude asking user to run PowerShell commands). All footers bumped V63→V64, plugin 0.63.0→0.64.0.

**Decisions.** Prose-only approach chosen per scope file's open question — no PreToolUse hook enforcement on after-build's file writes. The subagent body is the right layer because it governs judgment, not tool access. Hook enforcement deferred to a follow-up if prose fails in E2E testing.

**Pivots.** None. Scope delivered as specified.

**Carried forward.** Whether prose is sufficient will be tested in 0078 (post-fix E2E validation). If after-build still attempts source edits after this change, a PreToolUse check scoped to after-build's tool calls becomes a scope file.


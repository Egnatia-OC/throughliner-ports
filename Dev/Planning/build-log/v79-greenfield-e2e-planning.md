# v79 — 2026-05-25 — Greenfield E2E: post-redesign planning phase

**What shipped.** First E2E test of the procedure-doc architecture (post-0079/0080) against a greenfield app (Polite Fart Announcer). Tested /setup flow, planning-phase hook enforcement, and build-transition sequence. Research file at `research/e2e-greenfield-post-redesign.md`. Four new scope files (0085–0088) covering first-time user experience, scaffold quality, doc folder restructure, and build-phase E2E.

**Decisions taken and why.** Chose PreToolUse deny-message fix over stronger UserPromptSubmit hinting or SessionStart gating for the /setup enforcement gap — Claude demonstrably obeys deny messages but ignores advisory hints. Doc folder restructure scoped as a separate session (0087) because of its large surface area (templates, hooks, scripts, procedure docs, Reference manual).

**Pivots and surprises.** Parent-directory CLAUDE.md inheritance poisoned the first test attempt (burner folder inside the method tree). The dev project's own session was blocked by the plugin's planning-phase source lock — research/ exemption failed because cwd resolves to the parent folder, not sovereign-implementer. Both are instances of the same root cause: plugin assumes cwd = project root.

**Carried forward.** Build-phase testing deferred to 0088. Token cost baseline not measured (never reached a full build cycle).

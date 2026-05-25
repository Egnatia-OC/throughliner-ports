# V22 — 2026-05-14 — Planning subagent + Serves-line PreToolUse hook

**What shipped.** First subagent: `planning.md` (three planning flows, mixed-input sort, always-run drift checks, recap contract; tools: Read/Edit/Write/Glob/Grep only). PreToolUse gains Serves-line check (case-insensitive exact match against UX.md `### ` entries). NO-CODE-METHOD gains planning handoff + four `primary_intent` values; drift-check skip clause tightened. Reference manual, DOC-STRUCTURE, INVENTORY updated. INVENTORY D3 corrected (hooks inject context, can't launch subagents). OQ direct-edit-users shape #1 partially folded. 15 footers bumped V21 → V22.

**Decisions.** Main Claude classifies intent at handoff; subagent does mixed-input sort — keeps subagent prompt tight. Drift checks run every session; only skip is "nothing built yet" — skipping would defeat manual-edit detection. Serves-line matching: case-insensitive exact, no fuzzy — strict enough to catch skipped fold-ins. `/plan` not shipped — auto-route path required first.

**Pivots.** Web-search mid-build for subagent format surfaced key facts (`subagent_type` is `<plugin-name>:<agent-name>`; `agents/*.md` auto-register). INVENTORY ghost-commands caught mid-smoke-test — subagent recommended unshipped `/migrate`. Smoke-test auto-route couldn't run in Taskflow (tier 2; pre-V18 path block format).

**Carried forward.** Smoke test owed. `/plan` deferred. Direct-edit-users OQ shapes #2/#3 remain.


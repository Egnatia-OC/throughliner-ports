# V54 — Validation + warnings bundle

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22) — items 2, 3, 4 of the "six prose directives identified for pluginification" entry.**

## Goal

Three small checks added to existing plugin components, bundled because they're all "add a validation or warning to a component that already exists":

1. **`Serves <DOC>:` validation for additional docs.** PreToolUse currently validates `Serves UX.md:` lines only. Projects that declare additional source-of-truth docs in their CLAUDE.md path block (e.g. PATTERNS.md, API-REFERENCE.md) get no validation on `Serves <DOC>:` lines for those docs. Extend the existing check to cover all declared docs.

2. **Red flags non-empty warning at SessionStart.** SessionStart already reads BACKLOG.md. Add a check for a non-empty Red flags section and surface it prominently at session start — so the user never misses an active warning.

3. **Fold-in aging reminder.** Planning subagent scans `[FOLD-IN PENDING]` blocks for age (using the existing `Surfaced [date]` field) and flags any older than 1–2 planning sessions. Nudges the user to fold things in rather than letting them pile up.

## Inputs

- OPEN-QUESTIONS entry: "Six prose directives identified for pluginification" → items 2, 3, 4
- `plugin/hooks/pre_tool_use.py` — existing `Serves UX.md:` validation; extended for additional docs
- `plugin/hooks/session_start.py` — existing BACKLOG.md read; extended with Red flags check
- `plugin/agents/planning.md` — existing drift-check sweep; extended with fold-in aging scan
- `plugin/docs/DOC-STRUCTURE.md` — `Serves <DOC>:` rule, Red flags section spec, fold-in section spec
- Consumer project's CLAUDE.md path block — declares additional source-of-truth docs

## Outputs

- PreToolUse extended: `Serves <DOC>:` validation covers all docs declared in the project's CLAUDE.md path block, not just UX.md
- SessionStart extended: non-empty Red flags section triggers a prominent warning in the session-start output
- Planning subagent updated: fold-in aging scan added to drift-check sweep; flags pending fold-ins older than the threshold
- OPEN-QUESTIONS sub-entries (items 2, 3, 4) resolved
- Crash course.md updated if user-facing explanation needed

## Success criteria

- A batch with `Serves PATTERNS.md:` (where PATTERNS.md is declared in the path block) gets validated; a missing or malformed line triggers a deny
- A non-empty Red flags section produces a visible warning at session start; an empty one produces nothing
- A fold-in block older than the threshold is flagged during planning; a recent one is not
- No regression in existing `Serves UX.md:` validation
- Smoke-testable in a desktop-app burner session with the plugin installed via local marketplace against a fixture with additional docs declared, Red flags content, and aged fold-in blocks

## Open questions for this session

- **Fold-in aging threshold.** "1–2 planning sessions" is vague. Convert to calendar time (e.g. 14 days)? Or count planning sessions since the fold-in was surfaced? Leaning: calendar time — simpler to check, no session-counting mechanism needed.
- **Red flags warning severity.** Plain text advisory, or something that blocks until acknowledged? Leaning: advisory only — the method doesn't block on warnings, it surfaces them.
- **Additional-doc discovery.** How does PreToolUse find which additional docs the project declares? Parse the CLAUDE.md path block at hook time, or cache the list at SessionStart? Leaning: parse at hook time — avoids cross-hook state, path block is small.

## Risks / dependencies

- **Fold-in aging depends on V45.** V45 shipped in v47 (2026-05-22) — distributed fold-in sections now exist in consumer projects. Dependency resolved.
- **Items are independent.** If one proves harder than expected, the other two can ship without it.
- **PreToolUse complexity.** Adding another validation path to PreToolUse increases the hook's complexity. Keep the additional-doc check as a clean extension of the existing `Serves UX.md:` check, not a separate code path.

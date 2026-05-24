# 0072 — After-build source-code boundary

## Goal

Hard boundary: after-build must never edit source files, gradle files, or any non-method file. Build failures get surfaced in the recap and TEST-LOG notes, not fixed by the subagent. Also fold in the "run commands yourself" prose rule to universal-behaviour.md (from v71 carried forward).

## Inputs

- `plugin/agents/after-build.md` — current subagent body.
- `plugin/hooks/universal-behaviour.md` — for the "run commands yourself" fold-in.
- `research/e2e-round-2-observations.md` findings #1 and #4 — after-build cascade and consent violation.

## Outputs

- Edited `after-build.md` with explicit scope boundary: no source-file edits, no build-tool edits, no system commands to fix code.
- Edited `universal-behaviour.md` with "run system commands yourself rather than asking the user" rule.
- TEST-LOG rows for smoke test (if testable without full E2E).

## Success criteria

- After-build body contains a clear, hard prohibition on editing non-method files.
- Build failures are documented in recap/TEST-LOG notes, not fixed inline.
- The consent-violation pattern (creating conditions that override a user refusal) is explicitly named and prohibited.
- "Run commands yourself" rule present in universal-behaviour.md.

## Open questions for this session

- Is prose sufficient, or does this need a PreToolUse check on after-build's file writes? Prose is the starting point; hook enforcement is a follow-up if prose fails in testing.

## Risks / dependencies

- None. Self-contained prose changes.

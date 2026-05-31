# Plugin reader test — v97 (v131)

Plugin reader test run against plugin v0.97.0. Three sub-agents (Opus), rich mock project state (three builds in, 2 unconfirmed test rows, 1 OQ, 4-file queued batch). Sub-agent B tested `build.md`.

## Disposition summary

| # | Gap | Tier | Disposition |
|---|-----|------|-------------|
| 1 | Close-procedure enforcement | Top | Doc fix (v131) + batch 0133 (hook) |
| 2 | Proxy-as-index missing from build.md | Top | Fixed (v131) |
| 3 | `[PROPOSED EDIT PENDING]` not instructed | Top | Fixed (v131) |
| 4 | Test-confirmation gate invisible to build.md | Top | Fixed (v131) |
| 5 | Competing first-output claims | Top | Batch 0134 |
| 6 | Volunteered test results vs. read-back | Top | OQ filed |
| 7 | Missing routes (bug reports, audits, method questions) | Middle | Batch 0134 |
| 8 | Path resolution / `${CLAUDE_PLUGIN_ROOT}` unexplained | Middle | No action — plugin runtime handles |
| 9 | Pre-build preconditions assumed | Middle | Fixed (v131, test-gate precondition) |
| 10 | BACKLOG write permission during build | Middle | Fixed (v131, clarified in build.md) |
| 11 | Re-batching snapshot state | Middle | OQ filed |
| 12a | Unconfirmed rows mid-build | Middle | No action — edge case, hook enforces at start |
| 12b | Status line in snapshot | Middle | No action — snapshot existence is the signal |
| 12c | Routing priority ordering | Middle | Batch 0134 |
| 13 | "Red flags" cross-ref in DOC-STRUCTURE | Bottom | No action — findable by search |
| 14 | JSON/Files: summary equivalence | Bottom | No action — obvious from context |
| 15 | "Flag in chat" wording inconsistency | Bottom | Partially fixed (v131 UX.md flag wording) |
| 16 | UX/MANIFEST stats absent from state summary | Bottom | No action — routing doesn't depend on them |
| 17 | Tripwire vs detect-first priority | Bottom | No action — rare collision |

## What was fixed in v131

**build.md (7 edits):**
- Added test-confirmation gate precondition at top of procedure.
- Updated snapshot removal instruction to cover all three BACKLOG formats (single-file, folder-with-INDEX, proxy-as-index).
- Updated re-batching carve-out to cover proxy-as-index mode.
- Replaced "flag in chat" with `[PROPOSED EDIT PENDING]` instruction for locked-doc edits.
- Added close-is-mandatory prohibition to "What you must not do."
- Clarified BACKLOG write permission for red flags during build.
- Updated UX.md flag instruction to use `[PROPOSED EDIT PENDING]` blocks.

**universal-behaviour.md (1 edit):**
- Added close-procedure prohibition to Prohibited behaviours section with load-bearing annotation.

## What was filed

**Batch 0133 — Close-procedure hook enforcement.** Mechanical backstop for the close prohibition. PreToolUse check: all Files: ticked + git commit attempted without `/sovclose` → deny.

**Batch 0134 — Session-start routing clarifications.** Three sub-gaps: first-output layering (status → tripwire → routing), missing opener routes, priority ordering.

**OQ — Volunteered test results vs. mechanical read-back.** Design decision needed on whether to accept volunteered results or insist on per-row walkthrough.

**OQ — Re-batching snapshot state after split.** What happens to the snapshot after unticked files move to new batches.

## Positive finding

Sub-agent C noted the prerequisite carve-out as the clearest boundary in the system — documented in two places, step-by-step procedure, labeling convention, explicit scope-creep distinction. Gold standard for boundary documentation. The close-procedure rules now aspire to this level after the v131 fixes.

## Sub-agent details

- **Sub-agent A (Routing):** 16 findings. Strongest signal: competing first-output claims, missing routes for common openers, volunteered-results ambiguity.
- **Sub-agent B (Procedure, build.md):** 14 gaps. Strongest signal: proxy-as-index omission, test-gate invisibility, `[PROPOSED EDIT PENDING]` not instructed, re-batching underspecified.
- **Sub-agent C (Boundary):** 8 findings (including 1 positive). Strongest signal: close-enforcement gap (3 findings clustering on one root cause).

## Notes for next run

- Rotate Sub-agent B to `close.md` (second-most complex procedure, two-turn structure, many cross-references).
- Consider adding Sub-agent D for hook deny messages (collect templates from pre_tool_use.py, present as "you received this error").
- The rich mock state (three builds in) exercised the full routing surface well — keep this default.

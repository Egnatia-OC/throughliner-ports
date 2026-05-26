# 0094 — Guided testing and debugging procedure

## Goal

Give non-coders a step-by-step hand-holding experience when they test their app after a build. Two halves: (1) Claude walks the user through each pending User-verified test row — turning a one-line Test Description into an actionable sequence of "do this, look for that"; (2) when something fails, Claude runs a structured debugging process — asking what they saw, suggesting diagnostics, interpreting errors, narrowing the cause — until the issue is understood and routed (fix now, new batch, or known limitation).

The result is a new procedure doc (`plugin/docs/procedures/testing.md`) and a new skill (`/test`) that invokes it.

## Inputs

- `plugin/docs/procedures/after-build.md` — current handoff point (step 14: "Refresh and begin testing").
- `plugin/docs/DOC-STRUCTURE.md` → TEST-LOG structure — row format, types, verifier rules.
- `plugin/docs/VOCABULARY.md` → test type definitions.
- `plugin/templates/TEST-LOG-TEMPLATE.md` — row shape.
- `plugin/docs/procedures/planning.md` → step 1 (test session close / read-back) — the downstream consumer of test outcomes.

## Outputs

1. **`plugin/docs/procedures/testing.md`** — new procedure doc. Covers:
   - Loading state: which TEST-LOG rows are pending (Verifier: User, Status: blank).
   - Per-row guided execution: expand each Test Description into user-followable steps based on Type. What to do, what to look for, what "pass" looks like, what "fail" looks like.
   - Type-specific guidance templates (Look and click gets different walkthrough shape than Run and read).
   - Debugging protocol: when user reports failure — structured questions, diagnostic suggestions, error interpretation, cause narrowing.
   - Outcome recording: update TEST-LOG row with Status + Notes inline (not deferred to planning).
   - Exit: all rows addressed or user stops early.

2. **`plugin/skills/test/SKILL.md`** — new `/test` skill. Loads the testing procedure. Entry point for the user after a build ships.

3. **Updates to `plugin/docs/procedures/after-build.md`** — step 14 closing prompts updated to reference `/test` as the next action.

4. **Update to `plugin/README.md`** — skill listed.

5. **Update to `.claude-plugin/plugin.json`** — skill registered.

## Design decisions to make

1. **Should `/test` also handle Claude-verified tests?** Currently after-build runs those automatically (step 4b). If a Claude-verified test fails during after-build, should `/test` pick it up for debugging? Or does that stay in after-build's scope with a flag in the recap?

2. **How detailed should type-specific templates be?** "Look and click" for a UI app needs different guidance than "Look and click" for a CLI tool. Should the procedure adapt based on project type (detected from CLAUDE.md/UX.md), or use a generic shape the user can follow regardless?

3. **Should `/test` record outcomes directly to TEST-LOG, or defer to planning read-back?** Direct recording is faster and loses less context. But it skips the planning procedure's per-row confirmation gate (step 1). Options: record immediately + mark `Confirmed Explicitly: Yes`; record immediately + leave `No` for planning to re-confirm; or don't record, just guide.

4. **Debugging depth.** How far should Claude go? Options range from "ask what you saw, suggest one thing to check, route to a new batch" all the way to "generate diagnostic commands, interpret output, iterate until root cause found." The user is a non-coder — deep debugging might overwhelm; shallow debugging might not help.

5. **Should the procedure handle "Run and read" and "Trigger and observe" tests that were marked Claude-automatable but couldn't actually run?** (e.g., Claude doesn't have access to the runtime environment.) These might need user involvement despite being typed as automatable.

## Success criteria

- A non-coder can invoke `/test` after a build, follow Claude's guidance through every pending test row, and end up with all rows having a Status and Notes — without needing to know what to check independently.
- When a test fails, the user gets a structured process (not "what happened?" and silence) that either identifies the cause or produces a clear description for a new BACKLOG item.
- The procedure handles all four test types, even if three are "normally" Claude-automated — because "normally" assumes Claude has runtime access it may not have.

## Risks / dependencies

- **Depends on:** 0079 (subagent removal — procedures architecture) — already shipped.
- **Soft dependency on:** 0090 (TEST-LOG folder split) — if TEST-LOG moves to a folder structure, the testing procedure's state-loading step needs the new path. Could ship before or after; just needs a path-block lookup.
- **Risk:** over-specifying guidance templates. Different projects need different debugging depth. The procedure needs to be generic enough to work for a CLI tool, a web app, or a static site — without being so generic it says nothing useful.
- **Risk:** permission model. `/test` may need to run commands (for "Run and read" diagnostics) or read files (for "Generate and inspect" verification). The phase-aware permission model (0080) currently scopes what's locked by planning vs. build — testing is a third phase that isn't modeled yet.

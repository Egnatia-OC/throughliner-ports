# V57 — Subagent rule-loading convergence

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22).**

## Goal

Converge all subagents on one rule-loading pattern. Currently two patterns coexist:

- **Read-spec-on-entry:** `planning.md`, `before-build.md`, `setup.md` read `plugin/docs/DOC-STRUCTURE.md` and `plugin/docs/VOCABULARY.md` at session start. Agent body holds operational notes only.
- **Inline:** `batch-executor.md` has rules inlined in its body. No runtime spec read.

Inline drifts silently if the spec is updated and the agent body isn't. Read-spec-on-entry picks up spec changes automatically but adds prompt-time read overhead. This session picks a direction and refactors to converge.

## Inputs

- OPEN-QUESTIONS entry: "Subagent rule-loading pattern divergence — inline vs. read-spec-on-entry"
- All subagent bodies under `plugin/agents/` — each assessed for current pattern and refactored
- `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md` — the specs that read-on-entry subagents consume
- `BUILD-METHOD.md` → doc-code parity audit — if inline wins, parity audit discipline needs formalising

## Outputs

- All subagent bodies converged on one pattern (decided at session start)
- If **read-spec-on-entry wins:** `batch-executor.md` refactored to read specs at runtime; inlined rules removed; parity drift eliminated
- If **inline wins:** `planning.md`, `before-build.md`, `setup.md` refactored to inline their rules; runtime reads removed; `BUILD-METHOD.md` gains a formal parity-audit step ensuring inline content stays current with specs
- OPEN-QUESTIONS entry removed

## Success criteria

- All subagents use the same rule-loading pattern
- No functional regression — each subagent produces the same outputs as before convergence
- If read-on-entry: verify each subagent reads the correct spec sections at runtime
- If inline: verify doc-code parity audit catches a simulated drift (edit a spec, confirm the audit flags the inline copy as stale)
- Smoke-testable in a desktop-app burner session with the plugin installed via local marketplace: run each subagent path; verify correct behaviour

## Open questions for this session

- **Which direction?** Three positions from the original OPEN-QUESTIONS entry:
  - **A. Converge on read-spec-on-entry.** Parity drift impossible. Cost: prompt-time overhead per batch-executor invocation.
  - **B. Converge on inline.** Drops read overhead. Cost: doc-code parity audit becomes primary defence against drift.
  - **C. Keep divergence, document the rule.** Stable rules inline; evolving rules read-on-entry. Cost: classification to maintain.
  The right answer depends on how stable the specs are by V57. If `DOC-STRUCTURE.md` and `VOCABULARY.md` have been stable across V50–V56, B is safe. If they've been churning, A is safer. Assess at session start.
- **Prompt-time cost of read-on-entry.** How much context does reading specs consume per subagent invocation? If small relative to the agent body, the overhead argument for inline weakens.

## Risks / dependencies

- **No hard dependencies.** Placed at V57 so the specs have had time to stabilise (or not) across V45–V56, making the convergence direction an evidence-based decision rather than a guess.
- **Refactor scope.** If converging on read-on-entry, batch-executor is the only file to refactor. If converging on inline, three files need refactoring + BUILD-METHOD gains a new audit step. Either direction is manageable.
- **Functional regression.** The refactor changes how subagents load rules, not what rules they follow. Test that outputs match pre-refactor behaviour.

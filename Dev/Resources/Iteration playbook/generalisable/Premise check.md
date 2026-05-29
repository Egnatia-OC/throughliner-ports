# Premise check

*Proven. Reconcile a queued prompt against current state before running it.*

## Trigger

A queued prompt for a future version exists but was written one or more versions back, or in a previous session. The prompt's assumed starting state may no longer match reality because intermediate sessions changed things the queue couldn't anticipate.

The risk this pass protects against: a future session opens, reads the queued prompt, and starts work on premises that no longer hold. The cost of skipping it is a whole session running on a wrong premise.

## Steps

Unprompted:

- Read **every** queued prompt at the very start, not just the immediate one. If there are several stacked queued prompts, read all of them — later ones may have been partially superseded by intermediate sessions.
- Read every file in the current version folder, plus any human-facing doc the prompt references. Don't just check the files the prompt names — templates and side docs have been surprised by truncations before.
- State the actual current state in plain English alongside each prompt assumption — like a two-column reconciliation.
- Identify three buckets per prompt: (a) steps already done by intermediate sessions, (b) steps partly done, (c) steps still new.
- Propose structural decisions the prompt didn't anticipate (e.g. minimal-restructure vs full-restructure, retain a doc's old name vs rename).

User confirms:

- Each structural decision flagged.
- The adjusted plan before execution.

Then:

- Execute the prompt's intent, adjusted for current state. (At that point you're running [[Spec-driven version cut]] against the reconciled spec.) Or stop here and return the corrected prompt for a future session to run.

## Output

Either a corrected, paste-ready version of the prompt (with a short note on what changed) or — if you're running it now — a reconciled plan that feeds straight into [[Spec-driven version cut]]. Verifiable by diff against the original prompt.

## When wasted

- The queued prompt was written in the current version's own session — no stale gap.
- The gap between drafting the plan and running the session is short enough that current state can't have drifted.
- The planned changes are all independent and none depend on the others' assumptions.

## Refinements

- **Read every queued prompt, not just the immediate one.** A second-or-third queued prompt may have been partially superseded; not reading it means a future session re-does superseded work.
- **Include every file in the current version folder in the state report**, not just the most likely candidates. Templates and side docs surprise.
- **Treat the user's framing of state as a *claim* to be checked, not a fact.** This is the common bone Premise check shares with [[Reader test]] — both begin by reading current state before doing anything else.
- **Structure the premise check, don't read line-by-line.** For each change in the prompt, write down what state the prompt assumes, then check it. A structured pass catches "this is already done" faster and more reliably than reading the prompt and the docs in parallel and noticing.

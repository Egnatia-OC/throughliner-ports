# Catch consolidation

*Proven. Multiple instances. Roll accumulated catches forward into a version bump.*

## Trigger

Method-development sessions accumulate catches — small gaps surfaced by real-world use, near-misses caught while running other passes, observations transcribed from working with the method in another project. Catch consolidation fires when there are enough of them to justify a version bump, and few enough to fit one session. Specific event, not routine maintenance.

Three common starting points:

- A transcribed batch of observations from another project, framed as "possible Version N work."
- Prior session(s) ended with un-applied catches staged for the next version.
- Real-world use has happened since the last version and you suspect gaps have accumulated. Often combined with looking at the actual downstream project — that turns latent catches you didn't already have into ones you do.

If the trigger is "single broken spot that cascades" rather than "a list of catches," [[Coherence sweep]] is the more specific shape.

## Steps

Unprompted at session open:

- Read the current version's `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, and any directly relevant templates to establish active state.
- Sort the incoming observations into method-level vs. project-specific vs. already-handled.
- State each gap back in plain English, with your read of where the inconsistency actually lives.

User brings:

- The accumulated catches, with suggested wording if available.
- Permission to look at the real project, if relevant.

Stepwise, one catch at a time, with approval at each step:

- State the gap → propose the fix *shape* (not exact wording) → confirm → draft the text → approve the draft → move on.
- Default to the smallest accommodation that doesn't restrict future projects. Prefer a permissive note over restructuring the spine. Generalise only when a second or third project would also benefit.
- Mid-pass discoveries are absorbed, not deferred — new catches surfaced from looking at the real project, from drafting, or from the user thinking aloud get bundled into the same pass.

File operations:

- Copy the current version verbatim to the next-numbered folder at session open (not partway through).
- Apply edits one file at a time. Use `Read`/`Edit`/`Write`, not bash redirection.
- After each edit, verify the file is whole — `wc -l`, `tail`, and a `diff` against the previous version. Don't trust the Edit tool's success message on long replacements.
- After bulk edits to a single file, Read it end-to-end looking for new contradictions or rough seams introduced by your own work.

## Output

A new version folder containing the standard set of files, with discrete edits each tied to a named catch from the conversation. Verifiable by diffing against the previous version — the diff should show exactly the changes discussed in chat, no surprises.

## When wasted

- Observations are vague (no file references, no specific text). Discussion expands; edits don't converge.
- Only one or two items have accumulated. Version-bumping for two small fixes is overhead-heavy — make the edits in place or batch with the next round.
- A structural overhaul is imminent. Small patches will conflict.
- The observations are really about the project that surfaced them, not the method itself.
- The catches are all theoretical — not surfaced by real use. Synthetic catches without evidence may not earn a version bump.

## Refinements

- **Verify the verbatim copy before editing, not after.** Read both versions of each file immediately after `cp`, confirm equality, then start editing. A truncated copy that ships at the end of the session is the failure mode this prevents.
- **Default to the smallest accommodation.** Propose the minimum-touch version first; let the user escalate if they want more. Avoids the "full generalisation + restructuring" trap.
- **Verify after every edit, not just at the end.** The Edit tool has been observed truncating on long replacements; the success message doesn't catch it.
- **Scope discipline on mid-pass discoveries.** Healthy when discoveries are tight, but the pass can sprawl. Worth saying upfront: "we'll absorb new catches up to N before deferring the rest."
- **Flag bundling vs sequencing explicitly.** For a batch of independent small items, presenting them as a numbered list is fine; for catches that interact, deliver stepwise. Say which you're doing so the user can redirect.

# Mid-pass method amendment

*Single-instance. Sub-pass. Nests inside another executing pass when a substantive method gap surfaces mid-flight.*

## Trigger

During another pass — usually a [[Premise check]]-then-[[Spec-driven version cut]] sequence or a [[Catch consolidation]] — a substantive method gap surfaces that isn't in any queued prompt. The gap could be:

- A behaviour the method permits that you want to fence off.
- A rule the method assumes but doesn't state.
- A structural decision the method hasn't formally made.

You face a choice: defer it (queue a prompt for a future version) or absorb it (fold into the current pass). Absorbing it now is the right call when the gap is load-bearing for the work already in progress — the queued prompt's outcome will be incomplete or wrong without it.

This pass is *interrupt-driven nesting*: it pauses the host pass, completes the amendment, and resumes the host pass with the new content folded in.

## Steps

User raises the gap.

Unprompted:

- State the gap back in plain English. Distinguish what's in the current state vs what's missing.
- Propose the change in two layers: a *human-facing* layer (recommendation, conceptual explanation) and a *Claude-Code-facing* layer (operational rule that enforces it). Identify which docs each layer lives in.

User confirms (one question per turn, not bundled):

- Whether the amendment folds into the current version or queues for a future one.
- Where in each doc each piece goes.
- Any subtle per-question decisions (e.g. soft vs strict enforcement).

Unprompted again:

- Draft the new content. Get sign-off per draft. Insert.
- Generalise the rule before naming specifics — don't frame the rule around one example as if that's the whole story.
- Grep for old terminology the amendment makes obsolete. Update every hit.
- Re-read the queued prompt that the amendment may have partially superseded; mark it accordingly with a note about what's still left for it.

Then: resume the host pass with the new content folded in.

## Output

- New section(s) in the human-facing doc (`PRIMER.md` / `Crash course.md`) — orientation + detailed rule.
- New section(s) in the spec doc (`NO-CODE-METHOD.md` or `DOC-STRUCTURE.md`) — operational rule Claude Code reads.
- A consistent terminology pass — no residue of old wording anywhere in the version folder + project root.
- The next-version queued prompt re-read and marked partially superseded if applicable, with a note about what's still left for it.

## When wasted

- The gap is small enough to fix in a single-line edit. Just do it, no design dialogue.
- The gap belongs to a future version's scope and the current version shouldn't grow. Park it as a queued prompt instead — that's [[Reorg priming]], not this.
- The gap is project-shaped, not method-shaped. Track it as a project-level concern, not as a method amendment.

## Refinements

- **Generalise the rule before naming specifics.** Frame the operational rule around the general principle, then give concrete examples. Don't lead with one example as if it's the whole story.
- **End the amendment with an automatic terminology grep.** A method-wide rename leaves residue if you don't sweep. Don't declare the amendment done until the grep returns clean.
- **One question per turn, not bundled.** Even when questions feel related — three questions per response yields ambiguous coverage.
- **Re-read superseded queued prompts.** A mid-pass amendment can partially supersede a queued prompt. Mark it explicitly so the next session doesn't re-do superseded work.

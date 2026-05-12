# Reorg priming

*Proven. Produce a queued prompt for a future structural change that's too big to absorb mid-flight.*

## Trigger

A structural change becomes desirable from research, external information, or a symptom in a downstream artefact — and the change is too big or risky to absorb into the current pass. Run this pass when a structural change is identified that's too big to absorb mid-flight, AND you want the next session to execute it cleanly without re-deriving the design.

Two common entry points:

- **From the outside.** Research or external information surfaces structural pressure (e.g. the 200-line CLAUDE.md guideline, the spec/structure split that's standard in similar methodologies). A reorg is worth setting up properly rather than improvising.
- **From a downstream symptom.** Something is off in a downstream artefact — a docs-about-the-method file, a project doc, a "this method ships X without warning the user" feeling — and you suspect the symptom traces to a missing structural distinction in the source spec, not a doc-level typo. The crash-course-needs-warning case is the worked example.

## Steps

User brings:

- Awareness that a reorg is needed (or the symptom that points at one).
- Permission to draft the next session's prompt directly.

Joint, stepwise:

- Specify the change at coarse level (split this file, rename that one, move this section).
- Identify non-obvious interactions (cross-references, anywhere the moved content is referenced from elsewhere).
- Settle the open design decisions (what to call the split-off file, where the per-project path block lives, etc.).

Unprompted:

- Draft the prompt that will drive the next session — goal, specific changes, action plan, naming questions explicitly flagged as open.
- Patch the symptom doc to cover the interim (pre-source-fix) state if one exists. Name the source-fix version explicitly once it's locked.
- Update the project's `CLAUDE.md` to reflect the structure the new version will produce, with a parenthetical accommodating pre-reorg versions so the next session's first reads don't choke on the discrepancy.
- Check the version-queue state — read any existing queued prompt files — to decide whether this fix lands as a fold-in, a new prompt, or non-versioned scratch space.

## Output

- A paste-ready prompt for the next session — naming the version it'll cut, the changes, and any open questions.
- (If applicable) Interim patches to symptom docs.
- (If applicable) An updated project `CLAUDE.md` reflecting the upcoming structure.
- A short list of named-but-not-locked decisions the next session is on the hook to close.

The next session uses [[Premise check]] before running the prompt.

## When wasted

- The change is small enough to absorb into the current session. (Splitting one file in two isn't always priming-worthy; the threshold is whether the next session has to do design work or just apply edits.)
- The design is too speculative — you're not confident yet, and the next session would just redraft it. Delay until the design is firm.
- The version queue is already full and another queued prompt just creates backlog churn.
- The source spec is mid-restructure and this gap will get folded into in-flight work anyway. Wait until the in-flight version settles.
- No external driver. Doing reorg priming with no pressure risks ceremonial restructuring.

## Refinements

- **Lock the names at this pass, not at the next one.** A provisional filename forces the next session to either accept it or change it in two places. Better to commit now and revise only if a strong reason surfaces.
- **Be explicit about how speculative the design is.** Tell the next session it has standing permission to push back on the design if a fundamental problem surfaces.
- **Date the queued prompt and any project `CLAUDE.md` update.** If the reorg doesn't happen for a while, both will need re-checking against any catches that arrive in the gap.
- **Check version-queue state at the opening read-current-state step.** Don't wait until the user mentions a queued prompt — read existing prompt files at session start.
- **Push back on framing earlier.** The first response could often propose the spec-level fix directly rather than asking which level the user wanted.

# Replant (method terms)

*Experimental. Method-level adaptation of a project-level pass; not yet observed at method level. See `Taskflow planning passes.md` (one folder up) for the project-level original.*

Wholesale rewrite when a new source-of-truth doc lands whose claims contradict one or more foundational assumptions of the method itself.

## Trigger

A new external input lands — research into another methodology, a platform/MCP change, a major shift in how Cowork or Claude Code behaves — whose claims contradict one or more foundational assumptions baked into `NO-CODE-METHOD.md` or `DOC-STRUCTURE.md`. Not *adds a new rule*: *invalidates an existing principle or assumption*.

Speculative examples (none observed yet at method level):

- A reading of Cline's Memory Bank or another spec-driven methodology shows the build-sequence assumption "planning and building are separate sessions" is wrong for some class of project.
- A platform change makes the "source-of-truth docs are read-only in Claude Code" rule unworkable.
- A user-pattern observation invalidates a core stance like "every UX.md entry needs a user-needs-this-because line."

The bar for Replant at method level is higher than at project level: a Replant means abandoning a piece of foundation, which is rare. Most apparent contradictions can be handled by [[Catch consolidation]] or [[Reorg priming]].

## Steps (adapted from the project-level version)

Unprompted:

- Read all current method docs (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, the current `PRIMER.md`/`Crash course.md`, all templates) and the new source doc(s) before saying anything.
- Cross-check the new docs against each other and against the existing method to identify which existing rules are now load-bearing on invalidated assumptions.
- Stop before any destructive edit and ask the smallest set of forking questions that can't be derived from existing prefs — at minimum, wholesale rewrite vs. surgical edit, and how to handle the legacy content (carry-forward / wholesale rewrite / archive into a "deprecated" section).
- Do the rewrite.
- Verify every remaining method statement is still supported by something.

User confirms:

- Whether this really is a Replant or whether it's a [[Catch consolidation]] in disguise.
- The wholesale-vs-surgical scope.
- Handling of legacy method content that's no longer load-bearing.

## Output

Rewritten `NO-CODE-METHOD.md` (or `DOC-STRUCTURE.md`, or both), often with new planning batches or queued prompts for open questions that surface during the rewrite. Verifiable: no method statement references the invalidated foundation; every rule still has a current-state justification.

Almost certainly produces a major version cut, not a minor one.

## When wasted

- The new doc is *additive* (introduces a new rule or expectation, doesn't invalidate an existing one). Use [[Catch consolidation]] or [[Reorg priming]] instead.
- The contradictions are small enough to fix surgically. If you can list the affected method statements on one hand, edit them; don't tear up the spec.
- The new source doc is itself unsettled. If you'll refine its claims twice more this week, wait for it to stabilise.
- The contradiction is project-shaped, not method-shaped. A downstream project's specific need that the method doesn't cover is [[Downstream calibration]] territory, not Replant.

## Refinements (inherited from the project-level pass; method-level refinements TBD on first instance)

- **Ask only the forking questions that can't be derived from existing prefs.** Most decisions are derivable; surface only the ones that genuinely need user input.
- **Leave more in queued prompts than in speculative new rewrites.** A Replant exposes its own gaps — writing decisive new rules is what surfaces the questions you didn't know you had. Use planning batches or queued prompts liberally for the second-order questions.
- **Confirm Replant-vs-Catch-consolidation before starting.** A genuine Replant is rare. If a [[Catch consolidation]] would handle the change, use that — it's less disruptive.

## Note on maturity

This entry is Experimental: the shape is borrowed from a project-level pass (see `Taskflow planning passes.md`) and hasn't been run on the method itself. If a method-level Replant happens, refine this entry from observation rather than speculation.

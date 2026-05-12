# Spec-driven version cut

*Proven. Multiple instances. Execute a pre-authored change set as a version bump.*

## Trigger

You arrive with a pre-specified set of structural changes to the method, ideally including motivation, scope, and a file-by-file action plan. The changes touch multiple files, and at least one of them moves content that other files cross-reference. Execution, not discovery.

Pure single-file edits don't need this shape. A multi-file restructure with cross-ref impact does.

Distinguished from [[Catch consolidation]] by where the change set comes from: Catch consolidation builds the change set during the session from accumulated catches; Spec-driven version cut starts with the change set already drafted (usually by a prior [[Reorg priming]] or [[Principle audit]] pass).

## Steps

Unprompted:

- Read the current version's files end-to-end. State the file inventory and the relevant structural state of each.
- State back the planned changes in your own words. Flag interactions the user hadn't called out — cross-refs, orphaned references, places where moved content is referenced from elsewhere.
- Wait for confirmation before editing.
- Copy the current version's files verbatim into the new version folder at session open. Verify the copy is whole (read each destination file end-to-end immediately, not at session end).
- Walk file by file: state what's changing, preview the diff or content, get confirmation, write, move on.

User confirms:

- Each file's planned change before you write it.
- The naming or scope question if you flagged uncertainty.
- The final go on any cross-ref fixes surfaced during writing.

Verification at end:

- Re-read each file end-to-end against the spec. Check that each de-duped rule still appears in its canonical home; check that worked examples don't leak content the rest of the doc contradicts.
- Grep across the new version for cross-references — every `→` pointer should resolve to an existing section.

## Output

A new `Version N+1/` folder with edited and new files. Each diff visible in chat before being written. A short closing summary listing every file in the new version, line-count change, and any project-side consequences. If the method's file set changed, an updated project-level CLAUDE.md too.

## When wasted

- You don't have a scoped change list — you're showing up with "improve this somehow" rather than "changes X, Y, Z." That's [[Principle audit]] or [[Catch consolidation]], not this.
- The change is one or two trivial wording fixes. Editing in place is fine; cutting a new version is overhead for nothing.
- The prompt's framing is itself confused. Running this pass straight through compounds it. Surface the confusion as a short conversation first; rewrite the prompt; then run the pass.

## Refinements

- **Sanity-check the prompt's framing before executing.** Ask whether the proposed change set carves the work at the joints, not just whether each change is internally consistent. Catches the "this change is already done" or "these two changes contradict each other" failure modes at analysis, not mid-session.
- **Cross-reference audit before drafting, not during.** For every file in scope, list every internal and external reference touching the changed content before the first file preview. Catching cross-refs while writing is too late.
- **Grep before claiming coverage.** When removing or renaming any name (file, term, section, concept), search the whole project for every occurrence before stating impact.
- **Sweep dependent files proactively** when the method's file set changes — this project's `CLAUDE.md`, any templates referencing files by name. Don't wait to be asked.
- **Don't bundle confirmation with naming questions.** Keep "approve the plan" and "pick a name" as separate turns.
- **Verify by reading, not just grepping.** A grep is a sanity check, not real verification. End by reading each file end-to-end against the spec.
- **Use Edit for surgical changes, Write for large restructures.** Surgical Edits give a per-change review surface; full Writes are easier to lose track of.

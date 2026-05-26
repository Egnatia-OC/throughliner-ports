# Sync-procedure hardening

*Single-instance. The patient is the procedure, not the docs. ("Audit the audit.")*

## Trigger

You notice the maintenance machinery is held together by memory rather than by tracked artefacts. The trigger isn't a doc problem; it's a procedure problem that becomes visible because some recent pass produced an inconsistency (one wrapped addition, one inline mutation; one tracked deviation, one untracked) and you'd been treating the difference as something you could remember rather than something the system has to capture.

Worth running whenever you notice your or Claude's memory is the only thing keeping a process intact.

Common entry: a [[Catch consolidation]] or [[Spec-driven version cut]] session produced two artefacts that should follow the same convention but don't, and the difference can only be explained by "I forgot."

## Steps

Mixed — most substantive design moves come after specific questions from the user.

User asks for:

- Restructuring an offending mutation into the proper wrapped/demarcated form (matching the pattern from the consistent doc).
- Reconsideration of where index artefacts live — specifically, moving sync-only machinery out of any doc that travels to its consumer.
- Distinguishing what's project-specific from what's method-level.

Unprompted:

- Build an index of all wrapped additions or deviations across all docs so the wrapping is enforceable rather than aspirational.
- Save a memory describing the pattern so future-Claude applies it without re-deriving.
- Surface a candidate method-level rule (if applicable) for the next [[Catch consolidation]] or [[Reorg priming]] pass.

## Output

- A restructured doc (wrapped block instead of inline mutation, or equivalent).
- An index of project-specific additions or tracked deviations.
- A memory file describing the pattern and naming any underlying principle (e.g. audience separation).
- (Sometimes) candidate method-level rules surfaced for a future version's consideration.

Verifiable by: grepping the restructured doc for BEGIN/END markers, reading the project-instructions section once it's pasted, reading the memory.

## When wasted

- Your project has no template deviations at all. A project living entirely within the standard spec doesn't need any of this machinery; adding it pre-emptively is cargo-culting.
- Run as routine maintenance. The trigger should be either a near-miss (a deviation that almost got lost or was almost overwritten) or the act of adding a new deviation. Running it on a quiet day with nothing to track produces an empty index.

## Refinements

- **Ask the audience-separation question up front.** *Who reads this artefact, and where do they read it from?* That decides where the artefact lives. Don't build the index inside the doc that travels to its consumer, then realise it shouldn't live there.
- **Produce the project-instructions update *before* in-file changes.** The in-file changes are downstream of the procedure they're meant to comply with. Doing it in the opposite order works only because the changes are small enough to revisit cheaply.

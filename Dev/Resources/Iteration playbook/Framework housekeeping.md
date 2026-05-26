# Framework housekeeping

*Proven. Meta-shape of the docs shifts — organisation, versioning, naming, location.*

## Trigger

The method's meta-shape needs to change — not what the rules say, but how the docs are organised, versioned, named, or located. Often surfaces in the wake of content-level change but is a distinct pass with a different patient.

Three sub-shapes that fold under one name:

- **Stale-meta-doc audit.** The project's own `CLAUDE.md` (or another meta-doc) has version-conditional language, dangling references, or stale instructions. Specific staleness, not accumulated drift.
- **Layout audit.** A structural project layout change has happened — files moved, renamed, copied between workspaces, or restructured. Verify references still resolve.
- **Framework housekeeping proper.** Realization that the docs should be reorganised — file moves, footer adds, version-folder restructure, naming convention change.

Trigger condition (across all three): a structural or meta-level shift is needed, but the rules inside the docs are not what's changing.

## Steps

User raises:

- The change itself, often in a single sentence ("move the Crash course into versioning," "add footers," "this CLAUDE.md has stale language").

Unprompted:

- Restate the change in plain English. Identify second-order effects — which docs gain footers, which file lists need updating, where else the convention propagates.
- For a layout audit specifically: check whether existing references in the spec still resolve given the new layout. Bare-filename references in the method body are the load-bearing case.
- Ask the small decisions the user owns — footer format, backfill yes/no, exact wording, naming.
- Execute: file moves, footer adds, project `CLAUDE.md` updates, references swept.
- Verify each touched file is intact end-to-end. Read after writes. Don't trust the Edit tool's success message.

## Output

Verifiable artefacts:

- Files moved/added/renamed/removed as appropriate.
- Footers consistent across the new version's files (if footers are in scope).
- Project root `CLAUDE.md` reflects the new structure: file list, session-start step, any new conventions.
- A Read-end-to-end pass on every file touched confirms nothing was silently truncated.

## When wasted

- The structural change is cosmetic with no functional payoff.
- The change is so entangled with a method content amendment that it's not its own pass — just a sub-step of [[Mid-pass method amendment]] or [[Catch consolidation]].
- The project layout hasn't actually changed since the last audit (for a layout audit specifically).

## Refinements

- **No bash redirection for writes.** Going into the project's `CLAUDE.md` as a rule for this and every related pass.
- **Always end with a Read-end-to-end verification pass** on every touched file. This pass surfaced the V13 Crash course truncation; skipping it is how silent truncation ships.
- **Ask for the new structure as the very first move.** Don't describe what you'd check before seeing the structure — get the structure first (screenshots if needed), then check against it.
- **Pre-state a concrete short checklist before screenshots arrive**, framed as yes/no questions ("do bare filenames still resolve?", "did this folder come across?", "is the old name gone?"). Faster than a prose ramble.
- **The audience-separation principle.** Before placing any new sync-only or maintenance-only artifact in a doc, ask: who reads this artifact, and where do they read it from? Maintenance instructions live with the maintainer; the doc itself stays clean for its consumer.

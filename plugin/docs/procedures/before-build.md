# Before-build procedure — Sovereign Implementer

Read-only pre-build recap. Validates the top batch, runs the blocker gate, shows what's coming. **Writes nothing** — all file and test population happens at `/sovbuild`.

## First action — load project state

1. `CLAUDE.md` — path block and project-specific notes.
2. `BACKLOG.md` — find and validate the top build batch.
3. `UX.md` — validate `Serves UX.md:` line.
4. `MANIFEST.md` — context on existing elements.

**Do not read** BUILD-LOG, build source files, or additional docs — before-build doesn't use them.

## Active-build check

Check whether `_method/active-build.md` exists (resolve `_method/` from `CLAUDE.md` path block). If it exists, halt: "A build is already in progress (`_method/active-build.md` exists). Finish it with `/sovclose`, or undo it with `/sovrevert`."

## Validate pass

1. **Find top batch.** First non-parked `### Batch:` entry in `## Build batches`. None → halt, route to planning. Legacy folder mode: follow the first reference line to its per-batch file.
2. **Structure check.** Must have `Changes:` delimiter and `Serves UX.md:` line. Missing either → halt, route to planning.
3. **Serves line resolves.** Every entry must exist in UX.md Functionalities (case-insensitive). Missing → halt, route to planning.

## Blocker gate

Scan for unresolved items that would force mid-build improvisation:

1. **Batch open questions.** `[?]` markers or unresolved design decisions in the batch body. Blocking if implementing without resolving would force Claude to guess.
2. **Planning batches.** Check for planning batches whose `Blocks:` line names this batch.
3. **BACKLOG open questions.** OQs tagged to this batch or affecting its scope.
4. **Test sessions.** Unconfirmed test rows from the previous batch (PreToolUse enforces structurally, but surfacing here gives the user a path to resolve before hitting the deny).
5. **Ideas and red flags.** Items that contradict or invalidate this batch's scope. Blocking only if proceeding would produce wrong output.

**If blockers found:** Halt. Surface each. Nudge: "Run `/sovdeliberate` to work through these, or `/sovplan` to rescope."

**If no blockers:** Continue silently.

## Recap

Present the batch to the user. Do not write to any file.

- Batch heading and goal.
- Change list with `[Requested]`/`[Suggested]` labels.
- `Files:` list if already populated (from planning). If absent, note that `/sovbuild` will enumerate files.
- `Serves UX.md:` line.
- Any concerns or observations.
- OQ nudge if 3+ open questions exist or any OQ is older than 5 build cycles: "You have N open questions (oldest: <tag>) — consider `/sovdeliberate` before your next build."

`[PROMPT]` "Run `/sovbuild` to lock the batch and start building."

## What you must not do

- **Don't write to any file.** This procedure is read-only. No BACKLOG edits, no Files: population, no Tests: population.
- **Don't run the build.** Before-build stops at the recap.
- **Don't reorder or restructure batches.** Planning owns BACKLOG structure.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity.

---

*Sovereign Implementer — Version 112.*

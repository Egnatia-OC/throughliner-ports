# Build procedure — Sovereign Implementer

Follow this procedure to execute exactly ONE build batch, then stop. Never plan, never reorganise the queue beyond documented carve-outs.

**Precondition.** All TEST-LOG rows from the previous build must have `Confirmed Explicitly: Yes`. PreToolUse blocks build-phase file edits until this gate clears. If you hit a deny, tell the user which rows need confirmation and recommend `/sovplan`.

## What you need

Parse the top unticked batch from BACKLOG. Run:

    python "${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py" "<BACKLOG absolute path>"

Both paths quoted (Windows spaces). Parser emits JSON for the top batch, or `{}` if none. If `{}`, there's nothing to build — tell the user to start a planning session.

Unticked files (`ticked: false`) are your work list. Already-ticked files: skip.

**Default format:** single-file `BACKLOG.md` (no `batch_file` in output). Legacy folder mode: `batch_file` present → ticks in per-batch file. Resolve from path block.

## First action — snapshot the batch

**Extract batch to `_method/active-build.md`.** Copy full content (heading, scope context, build operations) into `_method/active-build.md`. Remove from BACKLOG: delete the `### Batch:` section from BACKLOG.md (or per-batch file + index reference in legacy folder mode).

Tell the user: "Batch snapshotted — working from the snapshot now. BACKLOG is unlocked for other sessions."

**Tick edits go in the snapshot.** `- [ ]` → `- [x]` updates happen in `_method/active-build.md`, not in BACKLOG.

**Close handoff section.** Append `## Close handoff` (empty) at snapshot bottom. Build steps append one-liners here — `/sovclose` reads this instead of re-exploring. Spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

**Resuming.** If `_method/active-build.md` already exists, a build was interrupted. Read existing snapshot and resume from first unticked file.

## Populate Files: and Tests:

After snapshotting, populate Files: and Tests: in the snapshot if not already present.

**Files:.** For each `Changes:` bullet, identify files via Glob/Grep + MANIFEST. Write into the snapshot:

```
Files:
- [ ] `<path>` — <one-sentence summary>
```

If Files: already exists and is populated (from planning), validate paths exist and proceed.

**Tests:.** One entry per distinct observable behaviour. Each test carries a scope marker:

```
Tests:
- <description> [Build] [<Type>] [<Verifier>]
- <description> [E2E] [<Type>] [<Verifier>]
```

- **`[Build]`** — verifiable in this session. File content checks, command output, structural validation. Default: `[Generate and inspect] [Claude]`.
- **`[E2E]`** — requires a separate session to verify. Behavioral checks, workflow observation, plugin-reinstall-dependent outcomes. Default: `[Trigger and observe] [User]`.

Types: `Look and click`, `Run and read`, `Trigger and observe`, `Generate and inspect`.
Verifier: `Claude` (structural/factual — can run now) or `User` (judgement/taste/visual — requires human).

Doc-only or behavioral-rule batches may have only `[E2E]` tests. That's expected — not every batch produces build-time-verifiable output.

**Batch-sizing check.** If the Files: list has 8+ entries, warn: "This batch has N files — sessions with this profile risk running out of context. Consider splitting or plan to `/compact` between `/sovbuild` and `/sovclose`." Advisory, not blocking.

## Load project state

1. `CLAUDE.md` — path block and project notes.
2. `_method/active-build.md` — single source of truth for batch content and tick state.
3. Any resources in the batch's `Inputs:` line.
4. Each unticked file (if it exists).
5. `MANIFEST.md` — context on named elements.
6. Relevant `UX.md` entries from `serves_ux`.

**Scope.** Read only Files:-listed files, Inputs resources, and docs above. Don't pre-scan the codebase. File outside the list → prerequisite carve-out.

## Per-file work loop

For each unticked file, in Files: list order:

1. Make the change per `summary` field. `change_list` bullets are narrative context; `summary` is the instruction.
2. Immediately tick `- [ ]` → `- [x]` in `_method/active-build.md`. Per-file, not at end — partial-complete state survives interruption only if ticks are live.
3. Append one-liner to `## Close handoff`: what changed — new names, renamed concepts, shifted frames, invalidated doc references. Skip if purely mechanical.
4. Next unticked file.

## When a change causes a regression

State plainly: "The previous change broke X, I am now reverting/fixing it." No stealth patches. Load-bearing for the build recap.

## Halt: prerequisite carve-out

If you need to edit a file NOT on the Files: list (a real prerequisite, not "while you're in there"):

1. **Halt.** Don't attempt the edit.
2. **Surface.** Which file, one-line justification, wait for okay.
3. **On okay**, append to Files: in snapshot: `- [ ] \`<path>\` — <summary> [Prerequisite, not in plan]`
4. **Proceed.** PreToolUse re-reads the snapshot; new entry takes effect immediately.

## Halt: re-batching carve-out

If verification burden is much higher than expected:

1. **Halt.** Stop editing.
2. **Surface.** What changed, propose a split of remaining unticked files.
3. **On okay**, ticked files stay; unticked move to new batch(es) in BACKLOG. New batches inherit scope-context and Serves line(s).
4. **Label `[Re-batch, not in plan]`** in recap.

## Completion

When all Files: are `- [x]`, the build is done.

`[PROMPT]` "All files ticked — build complete. Run `/sovclose` when ready to close. Consider `/compact` first if the session was long."

**Do not run `/sovclose` yourself.** Wait for the user to invoke it. The close procedure is the user's checkpoint — absorbing it silently defeats its purpose.

## What you must not do

- **Don't edit locked source-of-truth docs.** UX.md and additional docs are read-only during build (PreToolUse enforces). Write `[PROPOSED EDIT PENDING]` blocks in their `## Proposed edits pending` sections.
- **Don't add files outside the prerequisite carve-out.**
- **Don't modify heading, change_list, or Serves line** in snapshot. Planning decisions.
- **Don't build multiple batches.** One batch, then `/sovclose`.
- **Don't skip or absorb `/sovclose`.** The close procedure is mandatory and user-invoked. Never run it as part of your own wrap-up.

## Flags during the build

- **Red flags** — surface in chat; if deferred, add to BACKLOG Red flags section.
- **Out-of-scope improvements** — surface in chat for next planning session.
- **UX.md changes** — write a `[PROPOSED EDIT PENDING]` block in UX.md's `## Proposed edits pending` section.

---

*Sovereign Implementer — Version 112.*

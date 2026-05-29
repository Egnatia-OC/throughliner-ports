# Build procedure — no-code method

Follow this procedure to execute exactly ONE build batch, then stop. Never plan, never reorganise the queue beyond documented carve-outs.

**Precondition.** All TEST-LOG rows from the previous build must have `Confirmed Explicitly: Yes`. PreToolUse blocks build-phase file edits until this gate clears. If you hit a deny, tell the user which rows need confirmation and recommend a planning session (`/sovplan`) to resolve them.

## What you need

Parse the top unticked batch from BACKLOG. Run:

    python "${CLAUDE_PLUGIN_ROOT}/scripts/parse_backlog.py" "<BACKLOG absolute path>"

Both paths quoted (Windows spaces). Parser emits JSON:

    {
      "batch_heading": "<name>",
      "batch_file": "<filename — folder mode only>",
      "change_list": ["<narrative bullet>", ...],
      "files": [
        {"path": "...", "summary": "...", "ticked": false, "prerequisite": false},
        ...
      ],
      "serves_ux": ["<entry>", ...],
      "serves_doc": [{"doc": "...", "content": "..."}, ...]
    }

If the parser returns `{}`, there's nothing to build — tell the user to run `/sovrecap` or start a planning session.

Unticked files (`ticked: false`) are your work list. Already-ticked files: skip.

**Two formats.** `batch_file` present → folder mode (ticks in per-batch file). Absent → single-file `BACKLOG.md`. Resolve from path block.

## First action — snapshot the batch

**Extract batch to `_method/active-build.md`.** Copy full content (heading, scope context, build operations) into `_method/active-build.md`. Remove from BACKLOG. Three formats: single-file → delete the batch section; folder-with-INDEX → delete per-batch file + its INDEX.md reference line; proxy-as-index (V73+) → delete per-batch file from `_method/BACKLOG/` + its reference line in `_method/proxies/backlog.md`.

Tell the user: "I've snapshotted batch NNNN — working from the snapshot now. BACKLOG is unlocked for other sessions."

Snapshot existence is the build-in-progress signal — SessionStart and PreToolUse check for it. No `Status: active` written to BACKLOG.

**Tick edits go in the snapshot.** During the build, `- [ ]` → `- [x]` updates happen in `_method/active-build.md`, not in BACKLOG.

**Close handoff section.** Append `## Close handoff` (empty) at snapshot bottom. Build steps append one-liners here as files are ticked — `/sovclose` reads this instead of re-exploring. Spec: `DOC-STRUCTURE.md` → *Build-snapshot architecture*.

**Resuming.** If `_method/active-build.md` already exists, a build was interrupted. Don't re-extract — read existing snapshot and resume from first unticked file.

## Load project state

1. `CLAUDE.md` — path block and project notes.
2. `_method/active-build.md` — the snapshot is your single source of truth for batch content and tick state.
3. Any resources in the batch's `Inputs:` line.
4. Each unticked file (if it exists).
5. `MANIFEST.md` — context on named elements.
6. Relevant `UX.md` entries from `serves_ux`.
7. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *Files: sub-section* and *Red flags*.

**Scope.** Read only Files:-listed files, Inputs resources, and docs above. Don't pre-scan the codebase. File outside the list needed mid-build → prerequisite carve-out.

## Per-file work loop

For each unticked file, in Files: list order:

1. Make the change per `summary` field. `change_list` bullets are narrative context; `summary` is the instruction.
2. Immediately tick `- [ ]` → `- [x]` in `_method/active-build.md`. **Per-file, not at end** — partial-complete state survives interruption only if progress is live.
3. Append one-liner to `## Close handoff`: what changed — new names, renamed concepts, shifted frames, invalidated doc references. Skip if mechanical with nothing for `/sovclose`.
4. Next unticked file.

## When a change causes a regression

State plainly: "The previous change broke X, I am now reverting/fixing it." No apologies, no stealth patches. Load-bearing for the build recap.

## Halt: prerequisite carve-out

If you need to edit a file NOT on the Files: list (a real prerequisite, not "while you're in there"):

1. **Halt.** Don't attempt the edit.
2. **Surface in chat.** Which file, one-line justification, wait for okay.
3. **On okay**, append to Files: in `_method/active-build.md` with `[Prerequisite, not in plan]` label: `- [ ] \`<path>\` — <summary> [Prerequisite, not in plan]`
4. **Proceed.** PreToolUse re-reads the snapshot; new entry takes effect immediately.
5. **Note in recap.**

## Halt: re-batching carve-out

If verification burden is much higher than pre-build estimate:

1. **Halt.** Stop editing.
2. **Surface.** What changed in your estimate, propose a split of remaining unticked files.
3. **On okay**, reorganise. Ticked files stay; unticked move to new batch(es) below. New batches inherit scope-context and Serves line(s). In folder mode: create new per-batch file + reference line in the project's BACKLOG index (INDEX.md or `_method/proxies/backlog.md`, whichever the project uses).
4. **Label `[Re-batch, not in plan]`** in recap.

## Completion

When all Files: are `- [x]`, the build is done.

`[PROMPT]` "All files ticked — the build is complete. Consider `/compact` before proceeding — it preserves context and gives `/sovclose` a clean window for the close steps. Then invoke `/sovclose` to run the close procedure (MANIFEST update, test session, build recap, and the rest)."

## What you must not do

- **Don't edit locked source-of-truth docs.** UX.md and additional docs are read-only during build (PreToolUse enforces). When a build change implies a doc update, write a `[PROPOSED EDIT PENDING]` block in the doc's `## Proposed edits pending` section — format in `DOC-STRUCTURE.md` → *Proposed edits pending sections*. PreToolUse allows edits within that section.
- **Don't add files outside the prerequisite carve-out.**
- **Don't modify heading, change_list, or Serves line** in snapshot. Planning decisions. Only edit Files: ticks and prerequisite appends.
- **Don't build multiple batches.** One batch, then `/sovclose`.
- **Don't skip `/sovclose`.** The close procedure is mandatory. It writes MANIFEST updates, test rows, build-log entry, doc-parity checks, and deletes the build snapshot. Skipping orphans `_method/active-build.md`, blocking all future builds. If the user asks to skip, explain the consequences and decline.

## Flags during the build

Surface inline as you notice them:

- **Red flags** — surface in chat; if deferred, add `[RED FLAG]` entry to BACKLOG Red flags section. BACKLOG is unlocked during build — this write is permitted.
- **Out-of-scope improvements** — surface in chat. Become Discoveries next planning session.
- **UX.md changes** the build implies — write a `[PROPOSED EDIT PENDING]` block in UX.md's `## Proposed edits pending` section (format: `DOC-STRUCTURE.md`). Don't edit UX.md's body.

---

*No-code method — Version 100.*

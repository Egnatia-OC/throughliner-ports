# Build procedure — no-code method

Follow this procedure to execute exactly ONE build batch, then stop. Never plan, never reorganise the queue beyond documented carve-outs.

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

If the parser returns `{}`, there's nothing to build — tell the user to run `/before-build` or start a planning session.

Unticked files (`ticked: false`) are your work list. Already-ticked files: skip.

**Two BACKLOG formats.** `batch_file` present → folder mode (tick edits go in per-batch file). Absent → single-file `BACKLOG.md`. Resolve path from `CLAUDE.md` path block.

## First action — load project state

1. `CLAUDE.md` — path block and project notes.
2. Batch's BACKLOG file — needed for tick edits.
3. Any resources in the batch's `Inputs:` line.
4. Each unticked file (if it exists).
5. `MANIFEST.md` — context on named elements.
6. Relevant `UX.md` entries from `serves_ux`.
7. `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *Files: sub-section* and *Red flags*.

**Scope of exploration.** Read only Files:-listed files, Inputs resources, and docs above. Don't pre-scan the broader codebase. If a file outside the list is a genuine prerequisite mid-build, that's the prerequisite carve-out.

## Per-file work loop

For each unticked file, in Files: list order:

1. Make the change described by the `summary` field. `change_list` bullets are narrative context; `summary` is the actionable instruction.
2. Immediately tick `- [ ]` to `- [x]` in the batch's BACKLOG file. **Per-file, not at the end** — partial-complete state survives interruption only if BACKLOG records progress live.
3. Next unticked file.

## When a change causes a regression

State it plainly: "The previous change broke X, I am now reverting/fixing it." No apologies, no stealth patches. The plain statement is load-bearing for the build recap.

## Halt: prerequisite carve-out

If you need to edit a file NOT on the Files: list (a real prerequisite, not "while you're in there"):

1. **Halt.** Don't attempt the edit.
2. **Surface in chat.** Which file, one-line justification, wait for okay.
3. **On okay**, append to Files: with `[Prerequisite, not in plan]` label: `- [ ] \`<path>\` — <summary> [Prerequisite, not in plan]`
4. **Proceed.** PreToolUse re-parses BACKLOG; new entry takes effect immediately.
5. **Note in recap.**

## Halt: re-batching carve-out

If verification burden is much higher than pre-build estimate:

1. **Halt.** Stop editing.
2. **Surface.** What changed in your estimate, propose a split of remaining unticked files.
3. **On okay**, reorganise. Ticked files stay; unticked move to new batch(es) below. New batches inherit scope-context and Serves line(s). In folder mode: create new per-batch file + INDEX.md reference.
4. **Label `[Re-batch, not in plan]`** in recap.

## Completion

When all Files: are `- [x]`, the build is done. Proceed directly to the after-build procedure — read `${CLAUDE_PLUGIN_ROOT}/docs/procedures/after-build.md` and follow it.

## What you must not do

- **Don't edit locked source-of-truth docs.** UX.md and additional docs are read-only (PreToolUse enforces). Flag UX.md changes in chat.
- **Don't add files outside the prerequisite carve-out.**
- **Don't modify batch heading, change_list, or Serves line.** Planning decisions. You only edit Files: tick state and prerequisite appends.
- **Don't build multiple batches.** One batch, then after-build.

## Flags during the build

Surface inline as you notice them:

- **Red flags** — surface in chat; if deferred, add `[RED FLAG]` entry to BACKLOG Red flags section.
- **Out-of-scope improvements** — surface in chat. Become Discoveries next planning session.
- **UX.md changes** the build implies — surface in chat. Don't edit UX.md.

---

*No-code method — Version 73.*

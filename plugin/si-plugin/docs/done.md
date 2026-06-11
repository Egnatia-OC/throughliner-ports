# /done procedure

Close the current session — record what happened, update docs, commit. This doc routes to a per-type close-out and states the commit core once; the sub-docs carry the type-specific steps.

## Route by session shape

Check for _build.md. The check is automatic — don't ask:

- **_build.md exists** → read it, then route by the subheadings in its Entry (same routing as /next):
  - **Build** subheading (optionally with Test) → read and follow `done-build.md`.
  - **Test** subheading only → read and follow `done-test.md`.
  - **Audit** subheading → read and follow `done-audit.md`.
- **No _build.md** → planning session. Read and follow `done-plan.md`.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit core below, then return to the sub-doc for the recommendation.

## LOG entry files

Stated once here; every sub-doc's entry-writing step points at this section.

Each LOG entry is written as its own file under `LOG/` — never appended to a shared log file:

- **Session closing a batch** (build, test, audit): name the file after the batch slug — `LOG/<slug>.md` (e.g. `LOG/drop-log-per-release-split.md`).
- **Session without a batch slug** (planning, setup): name it by session type and date — `LOG/<type>-<YYYY-MM-DD>.md` (e.g. `LOG/plan-2026-06-09.md`).
- **Name already taken** (a re-run batch, a second planning session the same day): append `-2`, `-3`, and so on.
- The matching `LOG/index.md` line ends with the entry's filename, so a later lookup goes straight from the index line to the file.

The hash lives in the entry file's heading and the index line, never in the filename — the commit hash doesn't exist yet when the file is written, which is why the `[HASH]` placeholder pattern exists (see Commit core below).

Entries from before the per-entry split live in `LOG/log.md` and `LOG/log-v*.md`. Those files stay in place, untouched — their entries are found by hash or title search, not by filename.

## Commit core [BRIEF, PROMPT]

Stated once here; every sub-doc's Commit step points at this section.

1. Stage explicitly — name each path: files this session changed (from _build.md Changes where one existed), method docs updated during the session or close-out (QUEUE.md, SPEC.md, REGISTRY.md, LOG/), and the _build.md deletion where one was removed.
2. Draft the commit message title and body. Present both in the same message, each in its own fenced code block (see plugin-behaviour.md "Verbatim-copy strings"), and ask in the same approval moment: "Commit and push, or just commit?"
3. Wait for okay, then commit — and push if the user chose to push.

The LOG entry keeps its `[HASH]` placeholder. The next /plan or /next session backfills it as a working-tree edit that folds into that session's commit — no amend, no two-commit flow.

## Rules

- Do NOT skip the sub-doc's judgment steps even if the user says "just commit."
- Routing is automatic. Don't ask — check for _build.md.

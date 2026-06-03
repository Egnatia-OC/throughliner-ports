# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only uninstalling and reinstalling does.
**Target** = the editable source at `plugin/si-plugin/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**4 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — work batches. Flat inline entries, type-marked (build/test/idea/question).
- `REGISTRY.md` — components list. What exists, where it lives.
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), `LOG/log.md` for current release entries, `LOG/log-v*.md` for archived releases.

**4 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top queue entry, execute it (build or test, type-agnostic).
- `/done` — record what happened, clean up, commit.

**2 hooks:**
- `session_start` — detect project state (unadopted / adopted / active build), load behaviour rules.
- `pre_tool_use` — SPEC.md read-only during builds, batch file-list boundary, git safety.

## Where things live

```
No code method/
  CLAUDE.md              — this file
  .gitignore
  plugin/                — plugin packaging
    si-plugin/           — target source
      .claude-plugin/    — plugin manifest
      hooks/             — session_start, pre_tool_use
      skills/            — setup, plan, next, done
      templates/         — CLAUDE-TEMPLATE.md
      docs/              — procedure docs loaded by skills
    si-plugin.zip        — current installable zip
    zip-archive/         — versioned archive of past zips
  SPEC.md                — this project's spec (once /setup has run)
  QUEUE.md               — this project's work queue
  REGISTRY.md            — this project's component registry
  LOG/                   — this project's session logs (index.md + log.md)
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `C:\Users\Alex\Desktop\Taskflow Planning\No code method\plugin\si-plugin\...`
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Old plugin history** is on GitHub (`FlintCraftTech/sovereign-implementer`, pre-rebuild commits). Not in this folder.

## Push-and-rezip (automatic)

When Alex says "push" (or a push happens as part of /done), run this automatically before pushing — no confirmation needed per step:

1. Bump version in `plugin/si-plugin/.claude-plugin/plugin.json`. Patch for fixes/incremental, minor for new capabilities.
2. Pre-push consistency sweep — two passes, run in order:

   **Pass A — Gather the feed:** Run `git log --oneline origin/main..HEAD` to list unpushed commits. Read their LOG entries in LOG/log.md to understand what changed (files touched, features added/removed/renamed, concepts that shifted).

   **Pass B — Check for staleness against those changes:**
   - **Target internal consistency:** Do templates match the procedure docs they ship alongside? Compare FAQ templates and CLAUDE-TEMPLATE.md against current procedure docs (field names, doc structure, workflow descriptions). Update any that fell behind.
   - **Project docs:** Check QUEUE.md, SPEC.md, REGISTRY.md, and LOG/ for references to removed features, renamed fields, or old formats that the unpushed commits changed. Fix any found.
   - **CLAUDE.md:** Check this file's descriptions (Architecture, Method docs, Rules) against current target state. Update any stale references.
3. Add a push marker to the most recent entry in `LOG/log.md` (the first `##` heading — entries are newest-first): `**Pushed:** v<VERSION>` on its own line at the end of that entry's content.
4. Cap the current log file and start a new one:
   - Rename `LOG/log.md` to `LOG/log-v<VERSION>.md`
   - Create a fresh `LOG/log.md`:
     ```
     # LOG

     Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).
     ```
5. Archive current zip: `mv plugin/si-plugin.zip plugin/zip-archive/si-plugin-v<OLD_VERSION>.zip`
6. Prune `plugin/zip-archive/` to the three most recent zips (delete oldest).
7. Repackage: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip"` (zip the folder, not its contents — internal paths must start with `si-plugin/`).
8. Stage the zip, archive changes, and plugin.json, and the LOG/ changes. Commit: "Bump to v<VERSION> and repackage".
9. `git push`.
10. Tell Alex: "Pushed and rezipped. Uninstall/reinstall to update the host."

## E2E testing

**Taskflowapp** at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

## Current state

**Status:** Target v1.5.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Each entry is type-marked: [build], [test], [idea], [question].
- **REGISTRY.md** — components list. What exists, where it lives.
- **LOG/** — per-session records of what was built, tested, and decided. `LOG/index.md` for summaries (newest first), `LOG/log.md` for full entries (current release, newest first), `LOG/log-v*.md` for archived per-release entries.

## Workflow

- `/setup` — initial project scaffolding (already done).
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build or test).
- `/done` — close the build, record what happened, commit.

## Rules for Claude

- SPEC.md is read-only during builds. Edit it only during /plan.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.
- All use of the plugin to develop the plugin is testing the plugin. Any observation of Claude's behaviour — wrong, unexpected, or improvable — is a testing outcome and must be routed to Captures. Not to memory, not discussed and dropped. Captures.

# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Host and target

**Host** = the installed plugin. Its hooks fire in this project. Its skills are available. It's the running copy.
**Target** = the source code at `plugin/si-plugin/`. This is what's being built and edited.

Host and target are the same plugin at different stages. When target changes ship, they don't take effect until repackaged and reinstalled as the new host. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target.

## Architecture

**5 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — work batches. Flat inline entries, type-marked (build/test/idea/question).
- `REGISTRY.md` — components list. What exists, where it lives.
- `DECISIONS.md` — design decisions mapped to the commits where they were made.
- `LOG/` — per-session files. What happened, what shipped, what broke.

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
    si-plugin/           — target (plugin source code)
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
  DECISIONS.md           — this project's design decisions
  LOG/                   — this project's session logs
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `C:\Users\Alex\Desktop\Taskflow Planning\No code method\plugin\si-plugin\...`
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Old plugin history** is on GitHub (`FlintCraftTech/sovereign-implementer`, pre-rebuild commits). Not in this folder.

## Plugin install/update procedure

1. Archive the current zip: `Move-Item plugin\si-plugin.zip plugin\zip-archive\si-plugin-v<OLD_VERSION>.zip`
2. Prune the archive to the three most recent versions: delete anything older in `plugin\zip-archive\`.
3. Package: `Compress-Archive -Path plugin\si-plugin\* -DestinationPath plugin\si-plugin.zip`
4. Desktop app: Customise → Plugins → + → Create plugin → Upload plugin → select `plugin\si-plugin.zip`.
5. To update: gear icon → Uninstall, then repeat steps 1-4.

## E2E testing

**Taskflowapp** at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

## Current state

**Status:** Plugin v1.0.0 built and installed. Repo initialized, not yet pushed. Method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Each entry is type-marked: [build], [test], [idea], [question].
- **REGISTRY.md** — components list. What exists, where it lives.
- **DECISIONS.md** — design decisions mapped to the commits where they were made.
- **LOG/** — per-session records of what was built, tested, and decided.

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

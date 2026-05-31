# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start. The plugin's canonical docs live at `plugin/docs/` (`DOC-STRUCTURE.md`, `VOCABULARY.md`) and `plugin/hooks/universal-behaviour.md`. This file owns the product overview, the path block, and project-specific notes.

## Product overview

**What it is.** The no-code method — a Claude Code plugin (hooks, procedure docs, slash commands, templates) that gives non-coders a structured workflow for building apps with Claude.
**Who it's for.** Non-coders using Claude Code who know what their app should be but need a framework to keep Claude on track.
**What friction it solves.** Non-coders need heavy documentation to keep Claude aligned — UX specs, backlogs, manifests, test logs, build histories. Without them, Claude drifts. But heavy docs burn context window. The plugin navigates this: hooks enforce mechanically, procedure docs load on demand, skills give named entry points.

## Language

Language: English

Claude responds and writes doc content in this language. Control tokens (`Status:`, `Changes:`, `Serves UX.md:`, `[SECURITY]`, `Confirmed Explicitly:`) stay English — plugin hooks regex-match them.

## Where the docs live

Paths for each project doc, relative to the project root. Bare filenames elsewhere resolve against this list.

```json
{
  "UX.md": "_method/UX.md",
  "BACKLOG.md": "_method/proxies/backlog.md",
  "BUILD-LOG.md": "_method/proxies/build-log.md",
  "MANIFEST.md": "_method/MANIFEST.md",
  "TEST-LOG.md": "_method/proxies/backlog.md"
}
```

Fenced JSON so plugin hooks can parse it deterministically. Keys are logical names; values are relative paths.

## What's inside `_method/`

Located at `_method/`. The underscore prefix keeps it visually separate from project files.

- **BACKLOG/** — queued work. One file per batch.
- **build-log/** — record of each session: what shipped, decisions made, surprises.
- **test-log/** — per-session test files. Index in BACKLOG proxy.
- **proxies/** — compact indexes Claude reads first for context efficiency.
- **planning/drafts/** — scratch space for ideas not yet ready for a specific doc.
- **research/** — findings from research on external questions. Persists across sessions.
- **INVENTORY.md** — plugin component list and architecture reference.

## Plugin management

When asked how to install, disable, enable, or uninstall the plugin, read `Guides/Reference manual.md` → *Managing the plugin* before answering. Don't guess — the desktop app doesn't support `/plugin`, and several mechanisms have known bugs.

## Project-specific notes

### What this project builds

This project develops the method itself — the plugin, its docs, its templates. **Taskflow** and future apps are consumer projects that use it.

The repo is at the project root:
- **`plugin/`** — hooks, skills, procedure docs, canonical doc set, templates.
- **`Guides/`** — Reference manual, crash course.
- **`_method/`** — this project's own planning artifacts, managed by the plugin.
- **`tests/`** — automated test suite for the plugin's hooks and scripts.
- **`scripts/`** — dev-side scripts (bump_version.py for version bumps and proxy regeneration).

**Desktop app constraint.** Alex uses the Claude Code desktop app, not the CLI. `--plugin-dir` is CLI-only. See `_method/research/plugin-marketplace-scoping.md` § 6 Option B for marketplace install.

### Three files named CLAUDE.md

1. **This file** — instructions for developing the method. The plugin never reads it at runtime.
2. **`plugin/templates/CLAUDE-TEMPLATE.md`** — the template `/sovsetup` scaffolds into consumer projects.
3. **A consumer project's `CLAUDE.md`** — the live file the plugin's hooks read at runtime.

Same distinction applies to spine docs (UX.md, BACKLOG.md, MANIFEST.md). When discussing plugin behaviour, default to "the consumer project's copy."

**When Alex reports "Claude did X in Taskflow"** — read the relevant plugin docs, identify the gap, state it in plain English, confirm before drafting changes.

### Dev-side vs plugin-side

Every reference to something that exists in both layers must be prefixed **dev-side** or **plugin-side**.

- **Dev-side** — building the method: this CLAUDE.md, `_method/` artifacts, and rules governing how we work.
- **Plugin-side** — what ships to consumer projects: templates, procedure docs, hooks, skills, universal-behaviour.md.

Ambiguous terms (BACKLOG, planning, testing, CLAUDE.md, rules, docs) must carry the prefix.

**Host/target vocabulary.** "Host SI" = the installed plugin doing the work. "Target SI" = the source code at `plugin/` being built. You are building target SI from within host SI — the installed plugin's hooks fire on this project (phase detection, file locking, batch management), while target SI at `plugin/` is the code being edited during builds. When target SI changes ship, they don't take effect until repackaged and reinstalled as the new host (see *Plugin update procedure* below). Never both active in the same session.

### Design constraints

Every design choice navigates the tension between non-coders needing heavy docs (to keep Claude on track) and those docs burning context window:

1. Hooks enforce mechanically — Claude can't override them.
2. Procedure docs load on demand — only the active phase enters context.
3. Skills give named entry points.

When evaluating a change: does it add to what Claude must read every session, or does it keep enforcement mechanical and docs demand-loaded?

### E2E testing

Most sessions are dev-internal. E2E sessions run the plugin against Taskflow in a separate desktop-app burner session — Alex runs that; observations come back as BACKLOG items.

**Plugin reinstall before E2E:** uninstall → delete `plugin.zip` → repackage `plugin/` → reinstall.

**Taskflowapp** at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is a real consumer project. Read and write access for E2E testing. The patient is always the method — if Taskflow needs a change, prepare a prompt for Alex's Taskflow project.

### Plugin update procedure

When target SI changes need to take effect as the new host:

1. Build and close the session normally (target SI code changes committed).
2. Delete the old zip: `Remove-Item plugin.zip -ErrorAction SilentlyContinue`.
3. Repackage: `Compress-Archive -Path plugin\* -DestinationPath plugin.zip`.
4. In the desktop app: Customise → Plugins → gear icon → Uninstall. Then + → Create plugin → Upload plugin → select the new zip.
5. Verify version: Customise → Plugins → gear icon on the entry.

This cycle applies after any session that changes hook logic, procedure docs, templates, or skills. Doc-only or BACKLOG-only changes don't require reinstall — the host reads those from disk.

### User context

Alex is a non-coder and inexperienced in Claude Code. For test runs in Taskflow, explain in plain English how to enable the plugin and what to look for.

## After-build steps

Run `python scripts/bump_version.py <old> <new> --session-tag v<N>` for substantive method/plugin changes. For proxy-only regeneration: `python scripts/bump_version.py --session-tag v<N>`. The script bumps footers, `plugin.json` version, `PLUGIN_METHOD_VERSION` in `session_start.py`, and regenerates proxy headers.

## Current state (update at every session close)

**Current version:** v152 (session tag). Method version **V108**. Plugin version **0.108.0**.

**What's next:** Two E2E test batches: 0130 (/sovsetup case 1 retest), 0131 (build lifecycle retest). One parked graduation: 0151 (retire protocol files — completed by repo restructure v152). One implementation: 0147 (merge Ideas/OQs + combine ideation/deliberation). One parked: 0095 (/sovtest E2E). No open OQs.

Build-cycle position lives in `_method/proxies/backlog.md` (index) and `_method/BACKLOG/` (per-batch files).

---
*No-code method — Version 108.*

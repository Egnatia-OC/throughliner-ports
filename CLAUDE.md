# CLAUDE.md — Sovereign Implementer

Claude Code auto-loads this file on session start.

## What this is

The Sovereign Implementer — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Audience

The plugin's users are external non-coders building their own apps with Claude Code — not the person developing the plugin. This project is the unusual case: the developer (Alex) is also a non-coder using the plugin to build the plugin. Skill docs must be written for the external user, not for Alex.

Concretely: anything a skill causes Claude to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "plugin-behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where Claude reads them; they must not leak into output the user sees.

When editing any skill doc, check the output-facing strings against this audience before saving.

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only uninstalling and reinstalling does.
**Target** = the editable source at `plugin/si-plugin/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**4 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — red flags (security/privacy/breach risks Claude surfaced, kept at the top, each with an open/resolved/accepted state), work batches (Build/Test/Audit subheadings), and captured ideas (plain bullets).
- `REGISTRY.md` — components list. What exists, where it lives.
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`.

**4 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top queue entry, execute it (build, test, or audit).
- `/done` — record what happened, clean up, commit.

**2 hooks:**
- `session_start` — detect project state (unadopted / adopted / active build), load behaviour rules, check plugin version against .si-version.
- `pre_tool_use` — SPEC.md read-only during builds, scope-lock, git safety.

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
  LOG/                   — this project's session logs (index.md + per-entry files)
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `C:\Users\Alex\Desktop\Taskflow Planning\No code method\plugin\si-plugin\...`
- **Run commands directly.** Don't ask Alex to run them unless they require the desktop app UI or a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Cross-doc references go by name.** When editing the docs under `plugin/si-plugin/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a batch adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Old plugin history** is on GitHub (`FlintCraftTech/sovereign-implementer`, pre-rebuild commits). Not in this folder.

### Self-hosting dependency ordering

Batch ordering in QUEUE.md implicitly assumes the next batch sees the previous batch's effects. That's true for **target-side** changes — edits to files under `plugin/si-plugin/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks (`hooks/session_start.py`, `hooks/pre_tool_use.py`), the loaded skill procedure docs (`docs/setup.md`, `plan.md`, and the `next*.md` / `done*.md` families), and `docs/plugin-behaviour.md` — which only refresh after push + uninstall/reinstall.

When a batch depends on a previous batch's host-side effects, that dependency does not resolve in-session. /plan must place the dependent batch after a push marker and annotate its `Depends on:` line as `(host-side)`.

**Push-marker convention.** A line `--- Push required before continuing ---` between batches in QUEUE.md indicates /next must halt until the user has pushed and reinstalled. /plan inserts the marker when placing a host-side-dependent batch.

Worked example:
```
**[capture-parking-discipline]** ...

--- Push required before continuing ---

**[behaviour-agnosticism-audit]**
Depends on: capture-parking-discipline (host-side)
...
```

[behaviour-agnosticism-audit] reads procedure docs against criteria including capture routing rules. Those rules live in plugin-behaviour.md (host-side). Without the push between them, the audit would read the old rules.

## Session-start dirty-tree check

At session start, if no `_build.md` is present in the project root, run `git status --porcelain plugin/si-plugin/`. If non-empty, warn Alex that the target tree has uncommitted state and list the dirty paths — these may be orphaned sweep edits from a prior push, and a new /next would otherwise layer build edits on top of them.

## Rezip (local testing) and Push (release)

These are two separate actions. **Rezip** builds a fresh installable zip so Alex can dogfood the plugin privately — it never publishes. **Push** is the full release ritual that publishes to the public remote. The word "push" (said directly, or chosen at a /done close) always means the full release ritual below. "Rezip" is a separate, explicit request and never publishes — bumps no version, makes no commit, touches no remote. Do whichever Alex actually asked for; don't run a push because she asked to rezip.

### Rezip (local testing)

When Alex says "rezip" (or asks for a fresh local build to test), run this — no version bump, no archive, no commit, no push:

1. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never ships in the zip (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
2. Repackage, overwriting the existing zip: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip" -Force` (zip the folder, not its contents — internal paths must start with `si-plugin/`). Verify: list the zip's entries and confirm none contain `__pycache__` — if any do, stop and fix.
3. Tell Alex: "Zip rebuilt — nothing has been published. Uninstall/reinstall to test the new host privately."

### Push (release)

When Alex says "push" (or a push happens as part of /done), run this automatically before pushing — no confirmation needed per step:

1. Backfill any unfilled commit-hash placeholders anywhere in `LOG/` before proceeding. The session-start hook only fires at session start, so a /done that ran earlier in this same session leaves its placeholder unfilled at push time — this step catches it. Same rules as the hook: replace the token only in hash position (an entry heading line or the start of an index line), never in body prose, which may mention the token literally; resolve each to the **oldest** `git log -S "<entry title>"` match, never the newest commit touching the file.
2. Bump version in `plugin/si-plugin/.claude-plugin/plugin.json`. Patch for fixes/incremental, minor for new capabilities. (The bump lives here, not in rezip: bumping on every private test build would make Alex's own projects nag "version changed, re-run /setup" each time she tests.)
3. Pre-push consistency sweep — two passes, run in order:

   **Pass A — Gather the feed:** Run `git log --oneline origin/main..HEAD` to list unpushed commits. Read their LOG entries (each session's own file under LOG/) to understand what changed (files touched, features added/removed/renamed, concepts that shifted).

   **Pass B — Check for staleness against those changes:**
   - **Target internal consistency:** Do templates match the procedure docs they ship alongside? Compare FAQ templates and CLAUDE-TEMPLATE.md against current procedure docs (field names, doc structure, workflow descriptions). Update any that fell behind.
   - **Project docs:** Check QUEUE.md, SPEC.md, REGISTRY.md, and LOG/ for references to removed features, renamed fields, or old formats that the unpushed commits changed. Fix any found.
   - **CLAUDE.md:** Check this file's descriptions (Architecture, Method docs, Rules) against current target state. Update any stale references.
4. Archive current zip: `mv plugin/si-plugin.zip plugin/zip-archive/si-plugin-v<OLD_VERSION>.zip`
5. Prune `plugin/zip-archive/` to the three most recent zips (delete oldest).
6. Delete all `__pycache__` folders under `plugin/si-plugin/` so compiled Python bytecode never ships in the zip (disposable — Python regenerates them as needed): `Get-ChildItem "plugin\si-plugin" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`
7. Repackage: `Compress-Archive -Path "plugin\si-plugin" -DestinationPath "plugin\si-plugin.zip"` (zip the folder, not its contents — internal paths must start with `si-plugin/`). Verify: list the zip's entries and confirm none contain `__pycache__` — if any do, stop and fix before pushing.
8. Stage every dirty path in `plugin/si-plugin/` (run `git status --porcelain plugin/si-plugin/` and stage each listed path — catches any sweep edits from step 3), plus the zip in `plugin/`, archive changes in `plugin/zip-archive/`, plugin.json, and the LOG/ changes (including step 1's backfill edits). Commit: "Bump to v<VERSION> and repackage".
9. `git push`.
10. Tell Alex: "Pushed and rezipped. Uninstall/reinstall to update the host."

**Archive accuracy.** Push keeps archiving the previous zip as above. Git history is the authoritative record of released zips — each push commits `si-plugin.zip`. So if a private rezip overwrote `si-plugin.zip` since the last push, the copy that lands in `plugin/zip-archive/` at the next push is a convenience that may reflect a test build rather than the prior release. This is cosmetic: git holds the true releases.

LOG entries are per-entry files — no log capping or push markers at push time. Existing `LOG/log.md` and `LOG/log-v*.md` files stay in place untouched: index references work by hash, so old entries remain findable.

## E2E testing

**Taskflowapp** at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

## Current state

**Status:** Target v1.11.0. Repo on GitHub, method docs set up (/setup complete).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Red flags (security, privacy, and breach risks Claude surfaced) sit at the top — the first thing seen each session — each carrying an open, resolved, or accepted state. Batches use Build/Test/Audit subheadings. Deferred tests holds tests that couldn't run in their own session, one line each (source batch slug, what to verify, what confirms it) — /done writes entries here and they sit until a session can confirm them (/plan reads the section each session); the confirming session removes the line. Captures are split by `---` (processed above with slugs, raw appended below). Items removed from active flow carry `Blocked by:` (trigger-based, auto-surfaces) or `Parked:` (indefinite, conscious revisit) headers.
- **REGISTRY.md** — components list. What exists, where it lives.
- **LOG/** — per-session records of what was built, tested, and decided. `LOG/index.md` for summaries (newest first), each full entry as its own file named on its index line. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`, findable by hash.

## Workflow

- `/setup` — initial project scaffolding (already done).
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build, test, or audit).
- `/done` — close the session, record what happened, commit.

## Rules for Claude

- SPEC.md is read-only during builds. Edit it only during /plan.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.
- All use of the plugin to develop the plugin is testing the plugin. Any observation of Claude's behaviour — wrong, unexpected, or improvable — is a testing outcome and must be routed to Captures. Not to memory, not discussed and dropped. Captures.

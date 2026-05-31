# CLAUDE.md — No code method (this project's instructions)

## Read this first

Session lifecycle (open, middle, close, doc-code parity) lives in **`sovereign-implementer/Dev/session-protocol.md`**. Read it at session start, along with the docs named in its *Session open* section. Entry shapes, footer bump lists, testing details, and planning artefact lifecycles live in **`sovereign-implementer/Dev/session-reference.md`** — dip when needed, don't load by default.

**Read the BACKLOG at session open.** Per-batch files live in `_method/BACKLOG/`; the index is at `_method/proxies/backlog.md`. Reading the proxy gives the full queue; dip into per-batch files for scope detail.

**Proxies at `_method/proxies/`.** Proxies give section line numbers for targeted offset/limit reads into large files. session-protocol.md is small enough to always read in full. Read the session-reference.md proxy (at `Dev/Planning/.proxies/session-reference.md`) before dipping into session-reference.md itself.

This file covers orientation, environment, and collaboration rules. Procedural rules live in session-protocol.md and session-reference.md.

**At session close**, update the *Current state* section below — bump the version, revise *What's built* if plugin components changed, advance *What's next*.


## Design constraints behind every decision

Non-coders need heavy documentation to keep Claude on track — UX specs, backlogs, manifests, test logs, build histories. Without them, Claude drifts. But heavy docs burn context window, leaving less room for actual work. Every design choice in this plugin navigates that tension:

1. **Hooks enforce mechanically** — Claude can't override them, so the rules don't need to live in docs Claude reads.
2. **Procedure docs load on demand** — only the active workflow phase enters context.
3. **Skills give named entry points** — the user says `/build`, not "please follow the 14-step build process."

When evaluating a change, ask: does this add to what Claude must read every session, or does it keep enforcement mechanical and docs demand-loaded? The first makes the problem worse.


## What this project is

This folder holds **the no code method** — a workflow document set, templates, and (from V18 onwards) the Claude Code plugin that distributes its rules across hooks, procedure docs, and skills. The job here is to iterate on the method itself, not write application code.

Work covers markdown editing (method spec files, templates), plugin code (hook scripts, skill bodies, procedure docs), and planning artefacts.

The repo lives in `sovereign-implementer/` (which becomes the GitHub project):

- **`plugin/`** — Claude Code plugin code: hooks (`plugin/hooks/`), skills (`plugin/skills/`), procedure docs (`plugin/docs/procedures/`), canonical doc set (`plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/hooks/universal-behaviour.md`), and templates (`plugin/templates/`).
- **`Guides/`** — product-facing docs: `Reference manual.md` (install and usage primer), `crash-course/` (multi-page HTML guide for testers/early adopters).
- **`_method/`** — planning artifacts in plugin-standard structure: `BACKLOG/` (per-batch files), `build-log/`, `test-log/`, `proxies/`, `planning/drafts/`, `research/`, `research/search-queries/`. Canonical location for all method artifacts as of v149.
- **`Dev/`** — dev-side workspace: `session-protocol.md`, `session-reference.md`, `INVENTORY.md`. Legacy copies of planning artifacts remain at `Dev/Planning/` and `Dev/Resources/research/` as safety net.
- **`Dev/Resources/`** — `tests/` (pytest suite), `scripts/` (dev-side automation, e.g. `bump_version.py`), `Marketing/`, `Iteration playbook/` (V3–V16 pre-git versions, read-only).


## Main goal

Alex uses the Claude Code **desktop app**, not the CLI. The `--plugin-dir` flag is CLI-only. To test the plugin in real projects, it must be published as a local marketplace and installed via `/plugin` — see `sovereign-implementer/_method/research/plugin-marketplace-scoping.md` § 6 Option B. Public marketplace publishing is a separate, later step.


## This project vs. consumer projects

This project develops the method. **Taskflow** and future apps are consumer projects that use it.

**Three files named `CLAUDE.md`** — keep them distinct:

1. **This file** — instructions for developing the method. The plugin never reads it.
2. **`plugin/templates/CLAUDE-TEMPLATE.md`** — the template `/setup` scaffolds into consumer projects.
3. **A consumer project's `CLAUDE.md`** — the live file the plugin's hooks read at runtime.

Same distinction applies to every spine doc (UX.md, BACKLOG.md, MANIFEST.md): template in `plugin/templates/`, scaffolded by `/setup`, live version in each consumer project. When discussing plugin behaviour, default to "the consumer project's copy." State explicitly when you mean something else.

**When I report "Claude did X in Taskflow"** — that's not a request to patch Taskflow. Your job:
1. Read the relevant plugin docs (universal-behaviour.md, the matching procedure doc, relevant templates).
2. Identify the gap. State it in plain English.
3. Confirm with me before drafting changes.


## Plugin management questions

When asked how to install, disable, enable, or uninstall the plugin, read `sovereign-implementer/Guides/Reference manual.md` → *Managing the plugin* before answering. Don't guess — the desktop app doesn't support `/plugin`, and several mechanisms have known bugs.


## Dev-side vs plugin-side — mandatory disambiguation

Every reference to something that exists in both layers must be prefixed **dev-side** or **plugin-side**.

- **Dev-side** — building the method: this CLAUDE.md, session-protocol.md, BACKLOG.md, test suite, and rules governing how *we* work.
- **Plugin-side** — what ships to consumer projects: templates, procedure docs, hooks, skills, universal-behaviour.md.

Ambiguous terms (BACKLOG, planning, testing, CLAUDE.md, rules, docs) must carry the prefix. If a reference is ambiguous, stop and clarify.


## Dev-side convergence strategy

The dev-side method (this CLAUDE.md, session-protocol.md, BACKLOG.md conventions) and the plugin-side method are converging. The endgame: the plugin absorbs the dev-side rules — including the ones in this CLAUDE.md — and this prose method gets retired. One method, enforced mechanically.

**Current phase: bidirectional exchange.** Testing the plugin by copying its patterns to the dev side (seeing how they hold up as prose conventions). Improving the plugin by sharing dev-side wisdom back (session protocol, planning conventions, collaboration rules). Neither side is authoritative yet — both are being refined through this exchange.

Dev-side mirrors plugin-side concepts as prose conventions (session-protocol.md, BACKLOG per-batch files, `_method/build-log/`, `_method/test-log/`), without locks, hooks, or skills. Don't propose adopting the plugin here. Don't write dev-side procedures as if hooks enforce them.


## Don't default to memory — route to the artifact

When information belongs in a structured artifact (`_method/BACKLOG/`, `_method/build-log/`, session-protocol.md, a research file, a draft), write it there. Don't save it as a memory.

Test: if you can name the destination, the information has a home. Write it there. Memory is for cross-session context with no project-level home.


## Make BACKLOG edits directly

Don't describe a BACKLOG.md edit for Alex to apply — make the edit, then tell her what changed. Same applies to build-log entries, test-log entries, and other dev-side planning artifacts.


## Proactive research

Watch for decisions that would benefit from external information — API capabilities, library comparisons, platform constraints, compatibility questions. When you spot one: draft a search query, state what decision it informs, and propose it before proceeding. Don't silently guess at external facts.


## File research before moving on

Save research results to `sovereign-implementer/_method/research/<topic>.md` before moving to the next task. Unfiled research is lost at session end. Update existing files rather than creating new ones for overlapping topics.


## Use absolute paths for sovereign-implementer lookups

Relative-path glob resolution from the working directory has been unreliable — false "file not found" for files that exist on disk. Use the full `C:\Users\Alex\Desktop\Taskflow Planning\No code method\sovereign-implementer\...` prefix for all sub-folder lookups (_method/, Dev/, Guides/, plugin/).

If a lookup returns "not found" for a file you have reason to believe exists, retry with the absolute path before halting.


## Dev-project marker file

`sovereign-implementer/.no-code-method-skip` keeps the plugin silent when loaded via `--plugin-dir` during dev sessions. Do not delete it. Background: `is_unadopted_with_work()` honours it as a legacy escape hatch (`_LEGACY_SKIP_MARKER` in `project_state.py`).


## E2E test sessions

Most sessions are dev-internal. E2E sessions run the plugin against Taskflow in a separate desktop-app burner session — Alex runs that; observations come back here as BACKLOG items.

**Plugin reinstall:** Before each E2E test, Alex: uninstalls → deletes `plugin.zip` → repackages `plugin/` → reinstalls. `plugin.zip` is gitignored.


## Taskflowapp as E2E test reference

`C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp` is a real project using the method. Read and write access available for E2E testing and doc migration (V61+).

The patient is always the method, not the project that revealed the gap. If Taskflow needs a specific change, tell me and prepare a prompt for my Taskflow planning project.


## Adherence-drop diagnostic

When Alex reports Claude is ignoring rules or declining in quality mid-session: don't just apologise and retry. Diagnose. Common causes: context window filling up (recommend `/compact` or session handoff), source docs too large to hold alongside working files (recommend targeted reads), missing foundational reads (re-read CLAUDE.md and session-protocol.md), or compaction dropped critical context (re-read the active procedure). Surface the likely cause and the matching action.


## Command execution

Claude runs shell commands directly during dev sessions — don't ask Alex to run them. Exception: E2E test commands that must execute in a separate consumer-project session, and commands requiring credentials or elevated permissions.


## My experience level

Also inexperienced in Claude Code itself. For test runs in Taskflow, explain in plain English how to enable the plugin and what to look for.


## Current state (update at every session close)

**Current version:** v149 (session tag). Method version **V107**. Plugin version **0.107.0**.

**What's next:** Two E2E test batches: 0130 (/sovsetup case 1 retest), 0131 (build lifecycle retest). Two graduation batches: 0149 (CLAUDE.md reconciliation), 0150 (activate self-management). One parked graduation: 0151 (retire protocol files). One implementation: 0147 (merge Ideas/OQs + combine ideation/deliberation). One parked: 0095 (/sovtest E2E). No open OQs.

Build-cycle position lives in `_method/proxies/backlog.md` (index) and `_method/BACKLOG/` (per-batch files).

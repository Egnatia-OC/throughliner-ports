# CLAUDE.md

<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. ▼ -->

This project uses the Sovereign Implementer method.

## Project docs

- **SPEC.md** — product truth. What it is, who it's for, how it works.
- **QUEUE.md** — work queue, top-to-bottom. Red flags (security, privacy, and breach risks Claude surfaced, kept at the top so they're seen first — each carries an open, resolved, or accepted state), Batches (Build/Test/Audit subheadings), Deferred tests (one line per test that couldn't run in its own session — source batch slug, what to verify, what confirms it; /done writes entries here and they sit until a session can confirm them, then the confirming session removes the line), Captures (split by `---` — processed above with slugs, raw appended below). Items removed from active flow carry `Blocked by:` (trigger-based) or `Parked:` (indefinite) headers.
- **REGISTRY.md** — components list. Updated after each build.
- **LOG/** — session records: what was built, tested, decided. One file per session entry, plus index.md one-line summaries naming each entry file.
- **FAQ/** — workflow FAQ. Index loaded at session start; details in FAQ/faq.md.

## Workflow

- `/setup` — scaffold project docs (done if you're reading this).
- `/plan` — queue management, captures, design questions.
- `/next` — execute the top batch.
- `/done` — record, update docs, commit.

## Rules for Claude

- SPEC.md is read-only during builds. Edit it only during /plan.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Never start a second build while _build.md exists — finish and /done before starting another. (A planning session in a separate chat alongside a build is allowed.)
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.

## Language

Language: English

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific test procedures (how to run tests, what to check, environment setup),
     add them here or point to where they live — Claude will follow them during test entries and /done verification. -->

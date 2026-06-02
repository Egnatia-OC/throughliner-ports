# CLAUDE.md

<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. ▼ -->

This project uses the Sovereign Implementer method.

## Project docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Each entry is type-marked: [build], [test], [idea], [question].
- **REGISTRY.md** — components that exist. Updated after each build.
- **DECISIONS.md** — design decisions mapped to the commits where they were made.
- **LOG/** — per-session records of what was built, tested, and decided.
- **FAQ/** — quick-reference answers about how the workflow works. Index loaded at session start; full answers in FAQ/faq.md.

## Workflow

- `/setup` — initial project scaffolding (already done if you're reading this).
- `/plan` — manage the queue, process captures, resolve questions.
- `/next` — execute the top queue entry (build or test).
- `/done` — close the build, record what happened, commit.

## Rules for Claude

- SPEC.md is read-only during builds. Edit it only during /plan.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.

## Language

Language: English

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific test procedures (how to run tests, what to check, environment setup),
     add them here or point to where they live — Claude will follow them during [test] entries and /done verification. -->

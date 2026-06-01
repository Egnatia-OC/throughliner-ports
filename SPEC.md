# SPEC — Sovereign Implementer

## What this is

A Claude Code plugin for non-coders. It gives users a structured workflow for building apps with Claude Code without needing to know how to code.

## Who it's for

Non-coders who know what their app should do but need a framework to keep Claude aligned.

## How it works

Splits changes into a build queue that helps the user harness Claude's skills in dependency management, not just coding. The secondary core functionality is basic context window management.

Four skills drive the workflow:
- `/setup` — scaffold project docs and run the onboarding interview.
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — pick the top queue entry and execute it.
- `/done` — close the build, record what happened, commit.

Five project docs structure each project:
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — work batches and captured ideas.
- `REGISTRY.md` — components list. What exists, where it lives.
- `DECISIONS.md` — design decisions mapped to the commits where they were made.
- `LOG/` — per-session records of what was built, tested, and decided.

Two hooks enforce discipline mechanically:
- `session_start` — detect project state and load behaviour rules.
- `pre_tool_use` — SPEC.md read-only during builds, scope-lock to file list, git safety.

## Principles

- Never restrict ideation, just direct it. The user must be able to ideate at any point in the build cycle.

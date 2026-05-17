# Sovereign Implementer

A structured workflow for driving Claude Code as a non-coder. Spec-driven discipline, lock conventions, and a rigid pipeline that prevents drift between what's been decided and what gets built.

## What's here

The current method lives at the repo root: `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, and the 6 templates in `templates/`. Start with `Crash course.md`.

`plugin/` is the Claude Code plugin that distributes the method's rules across hooks, subagents, skills, and slash commands. Scaffolded in V18; populated session by session through V27. Once the plugin reaches feature-parity with the markdown method (around V26), the markdown method retires.

`planning/` contains the migration roadmap: `INVENTORY.md` is the current architecture, `PLAN.md` is the session-by-session plan, and `planning/sessions/Vxx.md` files are scopes for upcoming sessions.

> The session scope files are **provisional** — they may be renamed, deleted, or merged as the plan evolves. Each is deleted when its session ships.

`Archive/` holds older method versions (`Version 3/` through `Version 16/`) plus `Iteration playbook/` — a formalized set of named iteration passes used to evolve the method through V16. Both predate this repo's git history.

## Versioning

From V17 onwards, sessions are tracked as commits and tags (`v17`, `v18`, ...) rather than version folders. The footer at the bottom of each method file (`*No-code method — Version N.*`) is a human-readable hint of which snapshot you're reading.

## Status

Iteratively developed; not yet used to ship an app. The first real build under the current version is the next test, and the most honest one.

## License

MIT — see [LICENSE](LICENSE).

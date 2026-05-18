# Sovereign Implementer

A structured workflow for driving Claude Code as a non-coder. Spec-driven discipline, locked conventions, and a pipeline preventing drift between spec and build.

## What's here

The current method is at the repo root: `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, and 6 templates in `templates/`. Start with `Crash course.md`.

`plugin/` — the Claude Code plugin distributing the method's rules via hooks, subagents, skills, and slash commands. Scaffolded V18, populated through V27. At feature-parity with the markdown method (~V26), the markdown method retires.

`planning/` — migration roadmap. `INVENTORY.md` (current architecture), `PLAN.md` (session-by-session plan), `planning/sessions/Vxx.md` (scopes for upcoming sessions).

> Session scope files are **provisional** — renamed, deleted, or merged as the plan evolves; deleted when shipped.

`Archive/` — older method versions (`Version 3/`–`Version 16/`) and `Iteration playbook/`, the named iteration passes used to evolve the method through V16. Both predate this repo's git history.

## Versioning

From V17, sessions are tracked as commits and tags (`v17`, `v18`, …) rather than folders. Each method file's footer (`*No-code method — Version N.*`) marks the snapshot you're reading.

## Status

Iteratively developed; not yet used to ship an app. The first real build under the current version is the next test — and the most honest one.

## License

MIT — see [LICENSE](LICENSE).

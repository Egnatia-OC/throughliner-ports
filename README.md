# Sovereign Implementer

A structured workflow for driving Claude Code as a non-coder. Spec-driven discipline, locked conventions, and a pipeline preventing drift between spec and build.

## Install

```bash
/plugin marketplace add <path-or-URL-to-this-repo>
/plugin install no-code-method@sovereign-implementer
```

Then open a Claude Code session in your project folder. The plugin detects your folder state and guides you from there. See [Crash course.md](Crash%20course.md) for the full primer.

## What's here

`Crash course.md` — start here. Standalone primer covering install, the session shape, a walkthrough, and the reasoning behind the rules.

`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md` — the full method spec (docs-only / no-plugin version). `templates/` — starter shapes for the six spine docs.

`plugin/` — the Claude Code plugin distributing the method's rules via hooks, subagents, slash commands, and templates.

`planning/` — dev-internal roadmap and session scopes. `Archive/` — pre-git method versions (V3–V16).

## Versioning

Sessions are tracked as commits and tags (`v17`, `v18`, …). Each method file's footer (`*No-code method — Version N.*`) marks the snapshot you're reading.

## Status

Iteratively developed; not yet used to ship an app. The first real build under the current version is the next test — and the most honest one.

## License

PolyForm Noncommercial 1.0.0 — see [LICENSE](LICENSE).

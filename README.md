# Sovereign Implementer

A structured workflow for driving Claude Code as a non-coder. Spec-driven discipline, locked conventions, and a pipeline preventing drift between spec and build.

## Install

```bash
/plugin marketplace add <path-or-URL-to-this-repo>
/plugin install no-code-method@sovereign-implementer
```

Then open a Claude Code session in your project folder. The plugin detects your folder state and guides you from there. See [Reference manual.md](Guides/Reference%20manual.md) for the full primer.

## What's here

`Guides/Reference manual.md` — start here. Standalone primer covering install, the session shape, a walkthrough, and the reasoning behind the rules.

`plugin/` — the Claude Code plugin distributing the method's rules via hooks, skills, slash commands, and templates.

`Dev/` — dev-internal roadmap, batch queue, research, and tests.

## Versioning

Sessions are tracked as commits and tags (`v17`, `v18`, …). Each method file's footer (`*No-code method — Version N.*`) marks the snapshot you're reading.

## Status

Iteratively developed; not yet used to ship an app. The first real build under the current version is the next test — and the most honest one.

## License

PolyForm Noncommercial 1.0.0 — see [LICENSE](LICENSE).

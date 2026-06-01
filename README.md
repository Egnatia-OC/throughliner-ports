# Sovereign Implementer

A Claude Code plugin for non-coders. It gives you a structured workflow for building apps with Claude Code without needing to know how to code.

## Who it's for

People who know what their app should do but need a framework to keep Claude aligned through multi-session builds.

## How it works

The plugin splits work into a build queue and manages it through four skills:

- `/setup` — scaffold project docs and run an onboarding interview
- `/plan` — manage the queue, capture ideas, resolve questions, check for drift
- `/next` — pick the top batch and build it, scope-locked
- `/done` — record what happened, run tests, commit

Two hooks enforce discipline without burning context:

- **session_start** — detects project state and loads behaviour rules
- **pre_tool_use** — keeps SPEC.md read-only during builds, locks scope to the file list, prevents unsafe git operations

## Install

1. Download or clone this repo
2. In the Claude Code desktop app: Customise > Plugins > + > Create plugin > Upload plugin > select `plugin/si-plugin.zip`

To update: uninstall the old version first (gear icon > Uninstall), then repeat step 2.

## Getting started

Open a project folder in Claude Code and run `/setup`. The plugin will scaffold your project docs and ask five questions to get started.

## License

See [LICENSE](LICENSE).

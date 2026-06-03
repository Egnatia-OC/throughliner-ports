# Sovereign Implementer

A Claude Code plugin that lets you build apps without writing code yourself. You describe what you want; Claude builds it — and the plugin keeps the work organised across sessions so nothing drifts or gets lost.

## Who it's for

Non-coders who know what their app should do but need a framework to keep Claude on track through multi-session builds.

## What it does

The plugin splits your project into a build queue and walks you through it with four slash commands:

- `/setup` — answers five questions about your project and scaffolds everything
- `/plan` — organise the queue, capture ideas, resolve design questions
- `/next` — build the next item, scope-locked so Claude stays focused
- `/done` — record what happened, test, commit

Hooks run automatically in the background to enforce discipline — keeping your spec read-only during builds, locking scope to the current batch, and preventing unsafe git operations.

## Install

1. **[Download the plugin zip](https://github.com/FlintCraftTech/sovereign-implementer/raw/main/plugin/si-plugin.zip)** (direct download)
2. Open the Claude Code desktop app
3. Go to **Customise > Plugins > + > Create plugin > Upload plugin** and select the downloaded `si-plugin.zip`

To update: uninstall the old version first (gear icon > Uninstall), then repeat steps 1–3.

## Getting started

Open any project folder in Claude Code and type `/setup`. The plugin asks five questions about what you're building, then scaffolds your project docs. When you're ready to build, run `/plan` to scope your first batch, then `/next` to start.

## License

See [LICENSE](LICENSE).

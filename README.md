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

## Operating conditions

**Prerequisites** — do these once per project:
- Run `/setup` in your project folder to scaffold the method docs

**Tested environment** — the plugin is developed and tested under these settings. Other configurations may work but aren't verified:
- Claude Opus 4.6 on high-output mode
- Auto mode enabled
- `/compact` between commits (keeps context clean within a session)
- `/clear` or a new chat between pushes (gives each session a fresh context window)

## Getting started

Open any project folder in Claude Code and type `/setup`. The plugin asks five questions about what you're building, then scaffolds your project docs. When you're ready to build, run `/plan` to scope your first batch, then `/next` to start.

## License

See [LICENSE](LICENSE).

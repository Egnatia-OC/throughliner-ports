# Sovereign Implementer

A Claude Code plugin that lets you build the project you have in mind — an app, a website, a tool, whatever you're making — without writing code yourself. You describe what you want; Claude builds it — and the plugin keeps the work organised across sessions so nothing drifts or gets lost.

## Install

**Already have Claude Code?** Open a chat in Claude Code and ask it to install Sovereign Implementer — Claude runs the install commands for you, so you never touch a terminal. Just say: *"Add the marketplace `FlintCraftTech/sovereign-implementer` and install the `sovereign-implementer@flintcraft` plugin."* (For reference, those are the two commands `claude plugin marketplace add FlintCraftTech/sovereign-implementer` and `claude plugin install sovereign-implementer@flintcraft`.) Then fully restart Claude Code so the plugin loads. To update later, ask Claude to run `claude plugin update sovereign-implementer@flintcraft`, then restart again.

If Claude reports that the `claude` command can't be found, that's a known snag on some setups and not a broken install — ask it to find the `claude` program on your machine and run the same commands using its full path. Needs Claude Code **2.1.193 or later**; if yours is older, update Claude Code first.

**New to Claude Code?** Open a fresh chat at [claude.ai](https://claude.ai), paste this link — `https://github.com/FlintCraftTech/sovereign-implementer/raw/main/INSTALL.md` — and ask Claude to guide you through setup. The guide walks you through Claude Code install, paid plan setup, and plugin install. Built to assume no terminal experience — Claude runs any commands for you.

## Get notified of new versions

Want an email when a new version ships? GitHub can send you one. On the [plugin's GitHub page](https://github.com/FlintCraftTech/sovereign-implementer), click **Watch** (near the top right), choose **Custom**, tick **Releases**, and click **Apply**. From then on you get an email each time a new release is published. This needs a free GitHub account — signing up costs nothing.

## Who it's for

Non-coders who know what their project should do but need a framework to keep Claude on track through multi-session builds.

## What it does

The plugin splits your project into a build queue and walks you through it. Four slash commands drive the workflow:

- `/setup` — interviews you about your project (adapting to your answers) and scaffolds everything
- `/plan` — organise the queue, capture ideas, resolve design questions
- `/next` — build the next piece of ready work, scope-locked so Claude stays focused; it can build several pieces of cleared work back-to-back without you confirming each one
- `/done` — record what happened, commit

Hooks run automatically in the background to enforce discipline — locking edits to the active work's file list, guarding git safety, and linting the queue structure so it stays well-formed. Planning sessions have no file list to lock to, so they get a lighter guard instead: a change to anything beyond your queue, spec and log asks you first. It asks, never refuses — the point is that nothing gets changed without you seeing it.

The plugin also tunes itself to the Claude model you're running. It ships two versions of its own instructions — a fuller one and a lighter one — and picks the right one at the start of every session. Setup asks which model you mostly use, in one optional question, and that's the whole of it: both versions do the same thing, so your project works the same way whichever model you use.

Some pieces of work are yours to do rather than Claude's — sending something, checking a screen, a decision only you can make. Claude walks you through those live, one step at a time, when they come up. It never asks you whether you've already done them.

When something misbehaves, Claude routes the report to the right place: a problem in your app goes into your queue, a problem with the method itself becomes a scrubbed report you paste at flintcraft.tech/report, and a problem with Claude Code (the app the method runs inside) can be filed as a GitHub issue — Claude offers to file it for you where your GitHub tooling is set up, always showing you the exact text and posting only on your yes.

## How to use it

Run **/setup** once, when you first set up a project. After that you work in sessions, and every session ends the same way: **/done** to record what happened, then **/clear** to start fresh.

- **/plan** — think and organise: manage the queue, add ideas, resolve questions. Run it as often as planning needs; a long planning stretch is just /plan → /done → /clear, repeated.
- **/next** — build: it picks the top piece of ready work and builds it. You'll run /next many times, working down the queue. When several pieces are cleared, one /next can build them back-to-back without you confirming each one.

The habit that matters: always /done before /clear, so each session is saved before the context resets.

## Operating conditions

**Prerequisites** — do these once per project:
- Run `/setup` in your project folder to scaffold the method docs

**Tested environment** — the plugin is developed and tested under these settings. Other configurations may work but aren't verified:
- Claude Opus 4.8, all effort levels tested OK — the plugin's fuller instruction set is built and tested against this model
- The Claude 5 models (Opus 5, Sonnet 5, Fable 5) get the lighter instruction set automatically. It's newer and less exercised than the 4.8 set; if a session goes oddly on a 5-series model, that's worth reporting
- Auto mode enabled — optional; it spares you approving each step by hand. Turn it off if you'd rather confirm each action.
- `/clear` after every `/done` (keeps each session's context clean)

## Getting started

Open any project folder in Claude Code and run `/setup`. The plugin asks a short questionnaire about what you're building, then scaffolds your project docs. When you're ready to build, run `/plan` to organise your first piece of work, then `/next` to start.

## License

See [LICENSE](LICENSE).

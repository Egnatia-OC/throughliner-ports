# Sovereign Implementer

A Claude Code plugin that lets you build the project you have in mind — an app, a website, a tool, whatever you're making — without writing code yourself. You describe what you want; Claude builds it — and the plugin keeps the work organised across sessions so nothing drifts or gets lost.

## Install

**Already have Claude Code?** Open a chat in Claude Code and ask it to install Sovereign Implementer — Claude runs the install commands for you, so you never touch a terminal. Just say: *"Add the marketplace `FlintcraftTech/throughliner` and install the `sovereign-implementer@flintcraft` plugin."* (For reference, those are the two commands `claude plugin marketplace add FlintcraftTech/throughliner` and `claude plugin install sovereign-implementer@flintcraft`.) Then fully restart Claude Code so the plugin loads. To update later, ask Claude to run `claude plugin update sovereign-implementer@flintcraft`, then restart again.

**The two names don't match, and that's expected.** The repository is called `throughliner`; the plugin inside it is called `sovereign-implementer`. Both commands above are correct exactly as written — don't "fix" one to match the other.

**New to Claude Code?** Open a fresh chat at [claude.ai](https://claude.ai), paste this link — `https://github.com/FlintcraftTech/throughliner/raw/main/INSTALL.md` — and ask Claude to guide you through setup. The guide walks you through Claude Code install, paid plan setup, and plugin install. Built to assume no terminal experience — Claude runs any commands for you.

## Get notified of new versions

Want an email when a new version ships? GitHub can send you one. On the [plugin's GitHub page](https://github.com/FlintcraftTech/throughliner), click **Watch** (near the top right), choose **Custom**, tick **Releases**, and click **Apply**. From then on you get an email each time a new release is published. This needs a free GitHub account — signing up costs nothing.

## Who it's for

Non-coders who know what their project should do but need a framework to keep Claude on track through multi-session builds.

## What it does

The plugin splits your project into a build queue and walks you through it. Four slash commands drive the workflow:

- `/setup` — interviews you about your project (adapting to your answers) and scaffolds everything
- `/plan` — organise the queue, capture ideas, resolve design questions
- `/next` — build the next piece of ready work, scope-locked so Claude stays focused; it can build several pieces of cleared work back-to-back without you confirming each one, and it works through everything you've marked ready rather than proposing to stop early
- Work can be tagged so `/next` treats it differently: a **review pass** that reads and reports without editing, a **step for you** that Claude walks you through live rather than doing itself, or **hands-off** work that Claude must not run from the queue at all — for repairs to the plugin's own machinery, where using a broken mechanism to fix itself is the risk
- `/done` — record what happened, commit

Hooks run automatically in the background to enforce discipline — locking edits to the active work's file list, guarding git safety, and linting the queue structure so it stays well-formed. They also notice when your project's documents have fallen behind the current version of the method: rather than carrying on and quietly getting things wrong, the session stops and offers to bring them up to date with `/setup`, which migrates what's there instead of replacing it. They also stop Claude writing to your files by running a script instead of using its editing tools: a shell command can be working from an out-of-date view of a file and quietly overwrite something, so that route is closed off entirely.

At the start of a session they also tell you **whether this conversation is isolated from any other one you have open on the project** — worked out from git rather than assumed, because the right advice about running two conversations at once is opposite in the two cases. And they name any **working file left behind by a conversation that never closed**, without deleting it: that file can be the only record of what a crashed session actually did.

Where your app gives each conversation its own copy of the project, they also point out **work sitting on a branch that hasn't been merged back**, and offer to merge it. Nothing merges on its own, and an isolated conversation warns you at its close that the app's "remove" option at exit would delete that work along with the copy.

`/plan` opens by checking your queue for work whose position disagrees with what the work itself says — something marked ready that its own notes say must not be built, something marked ready with no files to change, or a chain of work each waiting on something else that is also waiting. It reports what it finds and moves nothing; that decision stays yours.

And they check Claude's own reports. Claude writes to your queue first and tells you after, which keeps the write safe — but it means a reply could report filing something the write never actually made, and you'd have no way to tell. So when a reply says a named piece of work was filed, a hook checks your queue for it, and if it isn't there Claude is made to fix it and tell you plainly before you act on it.

When something goes wrong, Claude works out which of three things it was and sends it to the right place: your **app** stays as work in your own queue; a problem with **the method** goes to the plugin's author at flintcraft.tech/report; a problem with **Claude Code itself** goes to a GitHub issue on `anthropics/claude-code`. Both outward reports are scrubbed of your project's details, and nothing is ever sent without you seeing the exact text first.

If you run more than one project on the method, they can **message each other**. Each project gets an `INBOX/` folder, and anything waiting in yours is mentioned at the start of a session — no carrying notes between chats by hand. A message going out to another project is always shown to you for approval first, because it carries this project's content somewhere else.

They also publish an **editing-state signal**: while Claude is writing to a file, a small marker in a `.throughliner/` folder says so, so another app you have open on the same document can hold off rather than the two of you typing over each other. It's a published contract other applications can read — the field-level specification is in [EDITING-STATE-CONTRACT.md](EDITING-STATE-CONTRACT.md) — it fails open where the plugin isn't installed, and the folder is gitignored, so it's safe to delete at any time.

## How to use it

Run **/setup** once, when you first set up a project. After that you work in sessions, and every session ends the same way: **/done** to record what happened, then **/clear** to start fresh.

- **/plan** — think and organise: manage the queue, add ideas, resolve questions. Run it as often as planning needs; a long planning stretch is just /plan → /done → /clear, repeated.
- **/next** — build: it picks the top piece of ready work and builds it. You'll run /next many times, working down the queue. When several pieces are cleared, one /next can build them back-to-back without you confirming each one.

The habit that matters: always /done before /clear, so each session is saved before the context resets.

## Operating conditions

**Prerequisites** — do these once per project:
- Run `/setup` in your project folder to scaffold the method docs

**Optional software that unlocks a capability** — not needed to use the plugin:
- `gh`, GitHub's command-line tool. If you have it and you're signed in, Claude can file a Claude Code bug report for you directly (after showing you the text and asking). Without it everything still works — Claude writes the report out and you paste it on GitHub yourself.

**Tested environment** — the plugin is developed and tested under these settings. Other configurations may work but aren't verified:
- Claude Opus 5 and Fable 5, all effort levels tested OK
- Auto mode enabled — optional; it spares you approving each step by hand. Turn it off if you'd rather confirm each action.
- `/clear` after every `/done` (keeps each session's context clean)

## Getting started

Open any project folder in Claude Code and run `/setup`. The plugin asks a short questionnaire about what you're building, then scaffolds your project docs. When you're ready to build, run `/plan` to organise your first piece of work, then `/next` to start.

## License

See [LICENSE](LICENSE).

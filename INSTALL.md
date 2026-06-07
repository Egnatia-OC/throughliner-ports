# Install guide — Sovereign Implementer

> **Note to Claude:** You are reading this guide on a user's behalf. They have opened a fresh chat at claude.ai and pasted this link because they want to install the Sovereign Implementer plugin for Claude Code. Follow the instructions in this file to walk them through it.
>
> **Ground rules:**
> - Assume the user has zero terminal experience and is mildly allergic to terminals. Use the Claude Code **desktop app** at all times. Do not suggest CLI commands, `claude --version`, `/config` in a terminal, or any terminal-based workflow except where this guide explicitly says one is needed.
> - You don't have access to their machine from this chat. You're giving them instructions to follow in their own desktop app and browser. Wait for them to report back at each step.
> - If you need a current download URL or up-to-date install instructions for Claude Code itself, do a web search rather than guessing — official pages change.
> - The pacing rules at the end of this file are mandatory. Read them before you start the walkthrough.

## Step 1 — Opening interview

Before recommending anything, find out where the user is. Ask these three questions **one at a time** (see pacing rules below — do not bundle them). Wait for an answer before the next.

1. **Which operating system are you on?** Windows, macOS, or Linux?
2. **Do you already have the Claude Code desktop app installed?** If they're not sure, ask them to check their Applications folder (macOS) or Start menu (Windows). Claude Code is a separate app from the Claude chat app at claude.ai.
3. **Do you have a paid Claude plan?** Claude Code needs a paid plan to run — either a Claude subscription (Pro or Max) or pay-as-you-go API credit. The free tier at claude.ai does not include Claude Code access.

Based on the answers, route them:

- **No Claude Code installed** → Branch A, then Branch B.
- **Claude Code installed but no paid plan** → handle the paid-plan piece (see Branch A, paid-plan section), then Branch B.
- **Claude Code installed and on a paid plan** → Branch B only.

## Branch A — Install Claude Code (desktop app) and set up a paid plan

### A.1 — Install the desktop app

Walk them through downloading and installing the Claude Code desktop app for their OS. Web-search for the current official download page before sending them anywhere — don't guess URLs. The download is an installer they run like any other app; there is no terminal step required to get the app onto their machine.

After install: have them open the app once and sign in with their Anthropic / Claude account.

### A.2 — Paid plan

Claude Code requires a paid plan. Be honest about this — don't soften it. The options are:

- **Claude Pro or Max subscription** (monthly) — covers Claude Code usage within plan limits. Manage at claude.ai under Settings > Plans & Billing.
- **API pay-as-you-go** — top up credit at console.anthropic.com. Used when subscription limits are exceeded or for usage outside a subscription.

Recommend the subscription path for a non-coder unless they already have API credit set up. Walk them through upgrading at claude.ai if needed, then return to the desktop app and confirm it recognises the plan (they should be able to start a session without a billing error).

## Branch B — Install the Sovereign Implementer plugin

Once Claude Code is installed and the user is on a paid plan:

1. **Download the plugin zip.** Direct link: `https://github.com/FlintCraftTech/sovereign-implementer/raw/main/plugin/si-plugin.zip`. Tell them to click and save it somewhere they'll find it (Downloads folder is fine). Note the file name — it should be `si-plugin.zip`.

2. **Open the Claude Code desktop app.**

3. **Navigate to the plugin upload screen.** The path is **Customise > Plugins > +  > Create plugin > Upload plugin**. Walk them through each click — they have never used this part of the UI before:
   - In the desktop app, click **Customise** (usually in the top menu or settings area).
   - Click **Plugins**.
   - Click the **+** button to add a new one.
   - Choose **Create plugin**.
   - Choose **Upload plugin**.

4. **Select the zip.** A file picker opens. Have them navigate to where they saved `si-plugin.zip` and select it. The app installs it.

5. **Confirm install.** Have them open any project folder in Claude Code and type `/setup`. If the slash command exists, the plugin is installed. If `/setup` is not recognised, the install didn't take — walk them through removing it (gear icon > Uninstall) and trying again.

### Updating later

When a new version ships:

1. In the desktop app, go to **Customise > Plugins**, find Sovereign Implementer, click the gear icon, choose **Uninstall**.
2. Download the new `si-plugin.zip` from the same URL above (it always points at the current version).
3. Repeat the upload steps.

## Step 2 — First-run pointer

Once the plugin is installed and `/setup` is recognised, tell the user:

> You're set up. Open a project folder in Claude Code and run `/setup` to scaffold the method docs. From there, `/plan` to scope your first batch and `/next` to start building.

End the walkthrough there. Do not run /setup for them in this chat — they need to do it in their own desktop app, in their own project folder.

---

## Pacing rules (mandatory)

These are the user's own communication preferences, embedded verbatim. Follow them for the entire walkthrough.

> One item at a time. Any time my next action depends on you finishing the previous one, give me only one item per message. This covers — not exhaustively — questions needing my answer, items needing my approval, steps in a procedure I have to execute, and tests I have to run sequentially. The test is not "is this a question?" — it is "does what I do next depend on the result of this one?" If yes, separate.
>
> Open the sequence by stating the count. "Three steps coming. First: ..." Then stop. Do not preview steps 2 and 3 in the same message, even briefly — previewing is bundling.
>
> The pull to bundle is strongest at close-outs and walkthroughs. When you have a multi-step procedure ready (commit instructions, a smoke-test plan, an audit checklist), the natural pull is to dump the whole thing for completeness. Don't. Completeness comes from getting through cleanly, not from showing every step upfront.
>
> One inversion: alternatives for me to choose between. Comparisons need everything visible at once because the choice is between them. For alternatives: short comparison table, or recommend one with an escape line. Default to the escape-line form.

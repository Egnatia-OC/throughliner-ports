# 08823b6 — Build [install-docs-cli-refresh]: rewrite README + INSTALL to the CLI/marketplace install path

README.md and INSTALL.md described installing SI via the desktop app's "Customise → Plugins → add → Upload plugin" button. Capture `[desktop-plugin-upload-removed]` confirmed that button — and the whole in-app upload path — is gone from the current desktop app, so the consumer install docs pointed at UI that no longer exists. Rewrote both to the supported path: add the SI marketplace from the GitHub repo and install via the `claude` CLI, framed so the Claude Code agent runs the commands and the non-coder never types in a terminal.

README's Install section: "Already have Claude Code?" now says to ask Claude Code, in plain English, to add the `FlintCraftTech/sovereign-implementer` marketplace and install `sovereign-implementer@flintcraft` — Claude runs the commands, then a full restart; updates are `claude plugin update ...`, again agent-run. "New to Claude Code?" keeps the INSTALL.md hand-off but notes Claude runs any commands.

INSTALL.md: Branch B collapsed from two paths (terminal + zip-upload) to one — B.1 "Ask Claude Code to install the plugin" (give the user a plain-English request to paste; the agent runs the two `claude plugin ...` commands; full restart), and B.2 the smoke test (moved out of the old zip branch, its failure steps reworked to drop the upload/uninstall UI in favour of restart + agent-driven reinstall). Removed the zip-download step, the screenshot placeholder pointer left by `[install-upload-path-clarity]`, and the upload-based "Updating later". Updated the intro "Already have Claude Code and a paid plan?" line and the "Instructions for Claude" ground rule that had said not to suggest CLI commands — now: the install uses `claude plugin ...` commands but the agent runs them, so the user never types in a terminal. FAQ gained "Do I need to use the terminal to install or update SI?" (no — Claude runs the commands; marketplace/CLI explained in plain terms).

Doc-content correctness self-verified at build via a read (commands match `resources/research/claude-code-plugin-install-paths.md`, dead upload copy removed). Terminal-install verification is already covered by the existing external Deferred tests lines `[publish-marketplace-manifest]` and `[install-self-install-branch]` (they need the manifest on the remote, i.e. the next push) — no new test line.

**Files touched:**
- README.md
- INSTALL.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none

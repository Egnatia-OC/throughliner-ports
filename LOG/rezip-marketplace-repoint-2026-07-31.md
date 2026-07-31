# [HASH] — Rezip to 1.15.0-test8 + repoint flintcraft marketplace GitHub→local; Flintcraft /thanks 404 routed out

Post-close tail of the session that shipped the `[user]`-handover fix (ae92d34). Three things happened after that commit, recorded here for the next session.

**Rezip to 1.15.0-test8.** To dogfood the walk-through fix locally, bumped `plugin/si-plugin/.claude-plugin/plugin.json` from `1.15.0-test7` to `1.15.0-test8`, cleared `__pycache__`, and reinstalled the host via the bundled CLI (plain `claude` isn't on PATH in the desktop app — used the full path under `AppData/Roaming/Claude/claude-code/<version>/claude.exe`). Nothing published.

**Marketplace repointed GitHub → local (user-approved decision).** The reinstall kept reporting test7 no matter what. Root cause: the installed `flintcraft` marketplace was registered against **GitHub** (`FlintCraftTech/sovereign-implementer`), not the local folder that CLAUDE.md's Rezip flow assumes — so it could only ever see pushed releases, never the local working tree. Decision: repoint it at the local folder. Removed the GitHub `flintcraft` registration and re-added it from the project path, which re-registers as `flintcraft` sourcing a local **Directory**. Reversible — re-adding the GitHub marketplace switches it back. After repointing + reinstall, the host correctly reports **1.15.0-test8**. Awaiting a full app restart to actually load it (skills register at launch); a push/release comes only after the fix is verified live. The alternative — skip local testing and push straight to GitHub where the marketplace already looked — was rejected because it would ship the walk-through fix to all projects unverified.

**Flintcraft.tech /thanks 404 discovery — routed OUT.** Verifying `[report-url-404]` (stand up flintcraft.tech/report) surfaced that the report form *submits* but then redirects to `flintcraft.tech/thanks`, which 404s — so a filed report shows an error page instead of a confirmation. That's a Flintcraft.tech website bug, not this project's, so it routed out: drafted a note and sent it to the user as a file to file in the Throughliner/Flintcraft project (that project isn't set up under Throughliner yet, so it has no queue to receive it, and this session can't write to another project folder anyway). `[report-url-404]` therefore stays in this project's Processed queue, **not done** — its finish line ("a real test submission actually lands") is unmet while the confirmation page 404s.

**Files touched:**
- plugin/si-plugin/.claude-plugin/plugin.json — version bump 1.15.0-test7 → 1.15.0-test8 (rezip test build)

**Routed to Captures:** none in this project (the Flintcraft /thanks 404 routed out to the Throughliner project as a sent note file).

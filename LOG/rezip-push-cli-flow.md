# [HASH] — CLAUDE.md (Rezip ritual, Push step 11, Host and target section) — rewrote the install/reload instructions from the removed desktop-app upload + uninstall/reinstall path to the `claude` CLI install/update against the committed marketplace + full app restart, stating that the host reads a cache snapshot so a rezip alone changes nothing it sees.

The desktop app removed its in-app plugin upload, so CLAUDE.md's Rezip and Push rituals — both ending in "uninstall/reinstall via the desktop UI" — described a path that no longer exists, leaving the documented way to test and release SI broken. The fix rewrites three references to the verified replacement: the `claude` CLI install/update against the committed `flintcraft` marketplace, then a full app restart. Rezip step 4 now registers the local marketplace first time (`claude plugin marketplace add "…\No code method"`) and re-snapshots each rezip after (`claude plugin update sovereign-implementer@flintcraft`); Push step 11 uses the same update; the Host and target line names the CLI path as the only thing that changes host behaviour.

The critical fact each rewrite carries: the CLI install reads a frozen snapshot it copied into `~/.claude/plugins/cache/...`, not the live working tree — so a working-tree or zip edit alone changes nothing the installed host sees; only the CLI install/update refreshes it. Commands were verified against resources/research/claude-code-plugin-install-paths.md before writing. A side-discovery surfaced and was filed: the committed marketplace sources the `plugin/si-plugin` folder, not the zip, so the rezip ritual's zip rebuild no longer feeds the local test loop — captured as [rezip-zip-vs-folder-coherence] for /plan.

**Files touched:**
- CLAUDE.md: rewrote three install/reload references (Host and target line, Rezip step 4, Push step 11) to the CLI install/update + full restart, with the cache-snapshot fact.

**Routed to Captures:** [rezip-zip-vs-folder-coherence]

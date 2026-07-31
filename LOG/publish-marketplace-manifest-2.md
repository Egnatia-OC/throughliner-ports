# [HASH] — [user] handover confirmed: SI installs from the marketplace on the remote

Confirmed live this session (the `[user]` handover item, closed and removed from Processed). Claude ran `claude plugin marketplace add FlintCraftTech/sovereign-implementer` (cloned and validated the marketplace from the GitHub remote — "Successfully added marketplace: flintcraft") and `claude plugin install sovereign-implementer@flintcraft` (succeeded — "already installed"). The marketplace manifest installs from the remote, satisfying the item's confirmation criterion. Note: the install reflects the last-pushed state, not this session's unpushed changes — the item only checks that the manifest installs, which it does. An environment detail found in the process: plain `claude` is not on the desktop-app session's PATH; the bundled CLI had to be invoked by full path (`...\Claude\claude-code\<version>\claude.exe`). The item had been tagged `[user]` on a "Claude can't drive the terminal" premise that proved false — Claude drove it — so a capture was filed to re-tag both install items. (Earlier same-slug entry from a prior session, which created the marketplace.json, remains at publish-marketplace-manifest.md.)

**Files touched:**
- none (verification handover; the item is removed from Processed)

**Routed to Captures:** buried-user-work-not-surfaced, handover-completion-ask-inverts-walkthrough, install-items-mis-tagged-user

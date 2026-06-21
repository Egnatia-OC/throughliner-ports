# 29ba751 - Created .claude-plugin/marketplace.json at the repo root so claude plugin install works

The clean install path - marketplace add then plugin install - needs a marketplace.json at the repo root, and SI had none, so the command could not work. The manifest registers the sovereign-implementer plugin (source ./plugin/si-plugin) under marketplace name flintcraft, making the install line sovereign-implementer@flintcraft. Schema confirmed against the current code.claude.com plugin docs (name/owner/plugins; source as a relative path string). Marketplace name is distinct from the plugin name to avoid the awkward self@self form; contact email omitted to keep a personal address out of the public manifest. Enables marketplace install and is the prerequisite for the terminal self-install branch.

**Files touched:**
- .claude-plugin/marketplace.json (new, repo root)

**Routed to Captures:** none

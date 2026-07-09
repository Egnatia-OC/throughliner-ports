# [HASH] — Bumped the -x fork to 0.1.0-test1 and installed it to start live dogfooding

The two-section redesign is code-complete in this `-x` fork but had never been dogfooded — this freeform kicked that off. Ran the rezip ritual: bumped plugin.json 0.1.0 → 0.1.0-test1, cleared `__pycache__`, and re-snapshotted the installed host via `claude plugin update sovereign-implementer-x@flintcraft-x` (the flintcraft-x marketplace was already registered). The `install` command reported "already installed" without re-snapshotting, so `update` was needed to load the new build. Handed the rest over to Alex: a full app restart, then real /plan, /next, /done sessions on the `-x` build. The fork installs as a separate plugin alongside main SI, which stays untouched. This unblocks the eventual `-x` → main merge.

**Files touched:**
- plugin/si-plugin/.claude-plugin/plugin.json — bumped to 0.1.0-test1

**Routed to Captures:** none

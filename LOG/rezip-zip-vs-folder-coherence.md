# [HASH] — Build [rezip-zip-vs-folder-coherence]: drop the zip rebuild from CLAUDE.md's Rezip ritual

The committed local marketplace (`marketplace.json`, marketplace `flintcraft`) sources the plugin from the `plugin/si-plugin` folder, not the zip, so the `claude` CLI local-test install snapshots the folder. The zip that Rezip rebuilt was therefore doing no work for local testing — it's never committed by Rezip, overwritten at the next rezip or Push, and its only effect was one hazard: a test-suffixed zip left in the working tree could be mis-archived into `zip-archive/` at the next Push (the exact case the Push ritual's "Archive accuracy" note warned about).

Removed the `Compress-Archive` repackaging step and its zip-entry verification from the Rezip ritual, renumbering the remaining steps (bump test suffix → clean `__pycache__` → refresh host via CLI + restart). Kept the `__pycache__` cleanup — it still matters because the CLI snapshots the live folder — and folded a one-line note into that step explaining no zip is built here and why (the marketplace sources the folder). Simplified the Push ritual's "Archive accuracy" note: since only Push now builds the zip, the working-tree zip is always the last release, so the archived copy faithfully reflects the prior release — the rezip-overwrote-the-zip scenario can no longer arise.

Self-verifying at build via a read: the Rezip section no longer repackages; the suffix bump and `__pycache__` cleanup remain; the "Archive accuracy" note no longer describes a scenario the rituals can produce. No runtime test.

**Files touched:**
- CLAUDE.md

**Routed to Captures:** none

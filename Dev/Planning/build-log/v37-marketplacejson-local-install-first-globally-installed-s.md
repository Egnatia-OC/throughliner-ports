# V37 — 2026-05-21 — Marketplace.json + local install + first globally-installed smoke test

**What shipped.** `.claude-plugin/marketplace.json` — single-plugin marketplace (`sovereign-implementer`, owner `FlintCraftTech`, relative source `./plugin`). Works for both local install and public distribution. Local install via `claude plugin marketplace add ./` + `claude plugin install`. Smoke test against empty folder (no `--plugin-dir`): tier 1 silent, hooks registered, `/adopt` case 1 fires, `/reload-plugins` loads full surface (1 plugin · 2 skills · 11 agents · 4 hooks). TEST-LOG #109–115. README updated (install instructions, license corrected to PolyForm Noncommercial). Footer 36→37; plugin 0.36.0→0.37.0.

**Decisions.** Marketplace name matches repo. No version in marketplace.json (`plugin.json` authoritative). Description added after validation warning.

**Pivots.** `/hooks` shows only PreToolUse for globally-installed (vs 3 event types for `--plugin-dir`) — cosmetic gap, hooks fire correctly. `claude -p` misfire (sends prompt, not project dir) — corrected to `cd` + `claude`.

**Carried forward.** OQ entries unchanged.


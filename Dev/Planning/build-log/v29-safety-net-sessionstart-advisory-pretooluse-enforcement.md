# V29 — 2026-05-19 — Safety net (SessionStart advisory + PreToolUse enforcement) + unified `/adopt`

**What shipped.** Two-hook safety net + unified `/adopt` skill-command (replaces `/new-project` + `/init-project` + `/migrate`; five folder-state branches). Smoke-tested across 5 fixtures; see TEST-LOG #071–089.

SessionStart gains unadopted-folder detection + `systemMessage` advisory. PreToolUse gains unadopted-folder gate (Edit/Write/MultiEdit + Task denied; `/adopt` calls pass through; self-clears on adoption). New `adopt.md` subagent (five-case dialogue; case-4 writable/locked classification fixed mid-session per #083). New `adopt/SKILL.md` + `scaffold.py`. Plugin README created. Reference manual gains safety-net section. NO-CODE-METHOD gains adoption-state vocabulary + detection rule. BUILD-METHOD gains frame-correction sweep step. 20 footers bumped V27 → V29; `plugin.json` → 0.29.0. Two OQ entries resolved. TEST-LOG #071–089 (one Fail, one Skipped; fixes applied, retests owed).

**Decisions.** Frame-correction sweep: option A (audit step) over B (shorten horizon) — cheap to run, preserves roadmap visibility. Template-reconciliation worker lives in `/adopt` case 4, not separate `/refresh`. Plugin README for "is plugin loaded" UX — `${CLAUDE_PLUGIN_ROOT}` doesn't expand in `settings.json`.

**Pivots.** PreToolUse gate is Edit/Write/MultiEdit only — Bash bypasses by design (threat model is accidental edits). Case-4 over-locked spine docs; fixed same commit. Case-4 walkthrough text possibly scrolled past (#089). V21 tripwire emits to `additionalContext`, not `systemMessage` — not user-visible.

**Carried forward.** TEST-LOG #083/#089 retests owed. Two `uploads/` files referenced in V29.md never committed — same failure mode as V20→V26 *Drafts in flight* incident. V21 tripwire user-visibility: code read pending.


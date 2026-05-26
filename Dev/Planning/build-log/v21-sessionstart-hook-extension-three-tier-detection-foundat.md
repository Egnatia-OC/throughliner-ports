# V21 — 2026-05-14 — SessionStart hook extension: three-tier detection + foundational reads + footer tripwire

**What shipped.** SessionStart extended to ~280 lines: reads project root from stdin `cwd` (not broken `$CLAUDE_PROJECT_DIR`), parses CLAUDE.md JSON path block, reads spine + additional SoT docs, detects template state, detects unfinished batch, runs version-footer tripwire. Three-tier behaviour: Tier 1 (non-method folder) emits nothing; Tier 2 (partial method shape) emits universal rules + gap flag; Tier 3 (complete project) emits full state summary + routing reminder. 8 footers bumped V20 → V21; `plugin.json` 0.19.0 → 0.21.0. Dev-project CLAUDE.md gains Cowork-first lean, test-run guidance, "Which CLAUDE.md is which." Smoke-tested on Windows: all tiers verified; tripwire caught missed `plugin/templates/` footer bumps mid-test.

**Decisions.** Tier 1 emits nothing (behaviour change from V18 — plugin should be invisible in non-method folders). Route signal is prose, not structured marker. Tier-2 detection tightened via method-footer check (prevents false positives from unrelated BACKLOG.md). Tripwire half of cross-version reconciliation folded in; worker half stays in V26. `plugin.json` skipped 0.20.0 — aligning with method version.

**Pivots.** Workflow misframed early — Alex builds in Cowork, Claude Code only for smoke-testing. "Which CLAUDE.md is which" confusion pinned in project CLAUDE.md. Footer tripwire caught real oversight mid-smoke: `plugin/templates/` copies missed by footer-bump pass. Smoke test paid for itself with this catch.

**Carried forward.** Tier-2 detection may need tightening. Direct-edit-users OQ remains.


# v146 — Ideation, research, and test-plan rewrites

**Date.** 2026-05-31
**Type.** Ideation + planning (covers two sessions — one uncommitted from 2026-05-30, one from 2026-05-31)
**Batch.** None consumed. 0147 scoped.

## What happened

Two sessions combined into one commit. First session (2026-05-30): rewrote test plans for 0130 and 0131 to account for reconciliation (0136–0139) and procedure-doc fixes (0140–0142). Scoped batches 0144 (design-decision sweep), 0145 (/sovexplain routing + MANIFEST capabilities summary), 0146 (first graduation: dogfood SI onto itself) from resolved OQs. Removed resolved OQs from BACKLOG. Researched SessionStart re-fire behaviour (resolved OQ — premise was incorrect, hook already re-fires after /clear) and skill invocation interception (PreToolUse + UserPromptExpansion paths).

Second session (2026-05-31): ideation on merging Ideas and Open Questions sections. Decision: Ideas section is a staging area that adds shuffling without value — captures should go straight to OQs. Scoped batch 0147 (merge Ideas into OQs, combine ideation/deliberation skill and procedure). Removed Ideas section from dev-side BACKLOG (was empty).

## Decisions taken and why

1. **Ideas section retired.** The idea → OQ promotion step doesn't add information, just reformats. The close protocol's idea sweep already routes to OQ or batch, not to Ideas. One section, one skill.

2. **SessionStart re-fire confirmed.** The `source` field distinguishes startup/resume/clear/compact. Plugin's session-start hook already re-orients after /clear. No new mechanism needed.

3. **Skill invocation interception viable.** Two hook paths cover all invocations: PreToolUse (matcher: "Skill") for Claude-initiated, UserPromptExpansion for user-typed /commands. Both can block.

## What's next

Queue: 0095 (parked), 0130–0131 (E2E tests, plans rewritten), 0144–0147 (implementation). Batch 0147 has one open decision: combined skill name.

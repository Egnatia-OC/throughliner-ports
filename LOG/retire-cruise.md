# [HASH] — Retire /cruise, collapsing to multi-line /next as the single queue-clearing skill

/cruise duplicated what /next already did. next.md's run model already builds several cleared lines back-to-back, top-down, stopping at the readiness line — which was /cruise's whole job. /next is unattended in practice (it runs faster than the user can follow), so multi-line /next *is* the unattended runner, and it works because /plan feeds it a well-vetted cleared region. Keeping both meant maintaining two runners for one purpose.

Deleted skills/cruise/, docs/cruise.md, and hooks/cruise_gate.py. The gate was never registered in hooks.json — it was invoked from the cruise skill itself — so removing it needed no hook rewiring. Stripped cruise from plugin.json's description (five skills → four), plan.md's readiness-line rationale, done-build.md's per-line commit note, both FAQ templates, CLAUDE-TEMPLATE.md, README.md's two skill lists, and SPEC.md — where the "Cruise control" section was replaced by a "Multi-line /next" section carrying the same run model without the retired autonomy machinery (the red-flags gate, the response spine, the iteration and budget ceilings).

Folded in [retire-goal-sessions]: the goal-session mode retires with it. Goal sessions were only ever the developer-side stand-in for an autonomous build mode, and multi-line /next now fills that role. Its one distinctive mechanic — several LOG entries in one commit — is absorbed by [next-close-commit-rule], so nothing was lost. One paragraph was preserved rather than deleted: the handoff-claim provenance rule is a general standing rule about treating Claude-authored handoffs as unverified, not goal-session machinery, so it was lifted into its own CLAUDE.md section with its cruise references reworded.

LOG/ and resources/ were deliberately left untouched — they are the historical record of past sessions, and rewriting history to erase a retired feature would falsify it.

**Files touched:**
- plugin/si-plugin/skills/cruise/SKILL.md (deleted, with its directory)
- plugin/si-plugin/docs/cruise.md (deleted)
- plugin/si-plugin/hooks/cruise_gate.py (deleted)
- plugin/si-plugin/.claude-plugin/plugin.json: five skills → four
- plugin/si-plugin/docs/plan.md: readiness-line why reworded /cruise → /next
- plugin/si-plugin/docs/done-build.md: removed the "Under a cruise run" commit-core note
- plugin/si-plugin/docs/done.md: shipped-slug-cross-check why reworded off "goal session"
- plugin/si-plugin/templates/faq-template.md: removed the /cruise FAQ entry; cleared-to-run FAQ reworded
- plugin/si-plugin/templates/faq-index-template.md: removed the /cruise index line
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: dropped /cruise skill-list line
- SPEC.md: "Cruise control" section → "Multi-line /next"; skill list and Principle updated
- README.md: dropped /cruise from both skill lists
- CLAUDE.md: 5 skills → 4; removed the "## Goal sessions" section, preserving handoff-provenance

**Routed to Captures:** none

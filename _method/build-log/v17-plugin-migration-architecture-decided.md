# V17 — 2026-05-11 — Plugin-migration architecture decided

**What shipped.** Plugin-migration architecture scoped end-to-end. Produced INVENTORY.md, PLAN.md (V18→V27 roadmap), Opus feasibility response. Scope files V18–V27 created. Versioning switched from numbered folders to git tags.

**Decisions.** Two-layer split: per-project SoT stays per-project; mechanical method becomes plugin — discipline becomes structural, not prompt-based. Stop hook proposes, user gates — single-step per prompt. Drift checks inlined into planning subagent — subagents can't spawn subagents.

**Pivots.** "Always-loaded core skill" collapsed — skill bodies are progressive-disclosure; universal rules moved to hook. Slash commands and skills merged in Claude Code v2.1.101. V18 promoted from research to first build session.

**Carried forward.** All plugin construction across V18–V27. Method instability during migration explicitly accepted.

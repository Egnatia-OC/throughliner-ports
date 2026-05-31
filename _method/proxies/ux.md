<!-- proxy | source: _method/UX.md | generated: 2026-05-31 -->

# UX.md — proxy

**Project:** Claude Code plugin for non-coders — structured workflow with phase-based orchestration, markdown guardrails, and mechanical enforcement via hooks.
**Principles:** 4
**Functionalities:** 10

## Entries

**Principles:**
- L12 **Mechanical enforcement over behavioral requests** — hooks enforce rules Claude can't override
- L14 **Demand-loaded context** — procedure docs load only when needed
- L16 **Non-coders own the spec, Claude owns the code** — source-of-truth docs locked during builds
- L18 **Every feature traces to a rationale** — nothing built without a "user needs this because..." line

**Functionalities:**
- L22 **Setup workflow** — /sovsetup scaffolds docs and walks product definition
- L28 **Session-open orientation** — automatic status summary at session start
- L34 **Planning sessions** — /sovplan, /sovdeliberate, /sovideate
- L40 **Build workflow** — /sovrecap, /sovbuild, /sovclose, /sovgit
- L46 **Test-confirmation gate** — per-row read-back blocks next build
- L52 **Phase-aware editing** — planning unlocks specs, build unlocks code
- L58 **Safety net** — adoption check, destructive command guards
- L64 **Rollback** — /sovrevert walks undo without git knowledge
- L68 **Doc compression** — /sovtersify guided compression pass
- L72 **Method explanation** — /sovexplain three-way question routing

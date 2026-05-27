# v103 — 2026-05-27 — Ideation: new batches and open question triage

**What shipped.** Ideation session. Eight new queued batches (0104–0111) added to BACKLOG. One candidate parked (PostToolUseFailure logging — prose rule sufficient). Stale skill-name references in 0095 fixed (`/test` → `/sovtest`).

**Batches added.**
- 0104: Sov-prefix rename for `/setup`, `/research`, `/test`, `/tersify`.
- 0105: `_method/` orientation section in CLAUDE-TEMPLATE.md.
- 0106: Post-build proxy regeneration in `/sovclose`.
- 0107: Unclosed-build detection in SessionStart.
- 0108: Guided rollback procedure (`/sovrevert`).
- 0109: `/sovsetup` case 4 scaffold drift detection.
- 0110: Queued-pipeline staleness sweep at close.
- 0111: Dev-side session-protocol procedural convergence (positioned first in queue). Six plugin-side structures into session-protocol.md: opener routing table, carried-forward read-back, explicit pre-commit checklist, explicit idea-sweep routing, differentiated close paths, batch-ordering audit. Resolves three OQs (L297, L309, L321).

**Decisions taken and why.**
- PostToolUseFailure hook parked: the cascading-repair scenario it targets was fixed by 0072 (source-code boundary). The "no stealth fixes" prose rule covers the general case. A failure-logging hook would generate noise on innocent failures without proportional value.
- Staleness sweep (0110) scoped as grep-level checks, not semantic analysis — "scan everything" risks burning context window. Dead file paths, old skill names, cancelled-batch references, and OQ aging are the four detection categories.
- Case 4 drift detection (0109) recommends test-based comparison over a version registry — a registry has the same manual-maintenance risk it's trying to solve.

**Carried forward.** Nothing.

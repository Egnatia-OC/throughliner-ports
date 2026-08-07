# [HASH] — The branch cycle recorded in CLAUDE.md, with the pre-merge audit stated as a gate and named honestly as a convention

CLAUDE.md gained a new section, sited beside the Rezip / Push / Release rituals because those are the other conventions governing how work leaves this project. It records the cycle the project actually runs — **branch → builds → soak → differential audit over the whole branch span → reconcile (one /plan + /next over its repair captures) → merge → branch again** — and states the gate: a branch does not merge to main until that audit has run and its repair captures are cleared, so main only ever receives a reconciled state.

Two things the section has to carry, and both were settled before it was written rather than left to the prose.

**The audit sits at soak-end, immediately before the merge — not at the end of the build night.** Soak-day work lands on the branch *after* a build-night audit would have run, so such an audit is muddied by construction: the merge outruns it. At soak-end the span is "everything on the branch since main", with nothing landing after it but the merge itself. Soak days are mostly ordinary queue work rather than rule changes, so the incremental span stays cheap.

**Differential, not full-corpus.** Only the rules this branch's commits touched, each checked against its other statement sites — the same check the ripple-grep rule runs at authoring time, re-run across the whole span as a catch-net for what authoring missed. The full ten-pass corpus audit stays occasional. The one full audit run so far cost eight subagents, which is far too heavy to repeat every merge.

**The honest limit is written into the section rather than left implicit: this is a convention, not a mechanism.** Nothing enforces the gate — no hook, no script, no lint. That is exactly the shape of the retired push marker, which was documented in two docs, implemented in neither, and silently let work run against a stale host. This gate escapes that fate only because the merge is itself a queue item whose prose carries the gate, and the section is what tells whoever writes the *next* merge item to include it. If a merge item is ever written without it, nothing will notice. The section says so in those words, so nobody mistakes it for enforcement.

Leakage is named as tolerable by design rather than glossed: the differential is span-based, so anything one merge lets through is covered by the next cycle's span. The rhythm shortens the distance between a divergence and its detection; it does not promise to catch everything once.

The resources-side half was already built by the capturing session — `resources/consistency-audit-plan.md` exists as the reusable two-mode plan, and `resources/overnight-blitz-plan.md` was amended to defer to the soak-end audit. This entry covers the CLAUDE.md half, which was all that remained.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none

# V24 — 2026-05-16 — BUILD-METHOD.md and TEST-LOG.md added; session-tag and method-version decoupled

**What shipped.** New `BUILD-METHOD.md` (working manual lifted from CLAUDE.md + expanded). New `TEST-LOG.md` (30 backfilled rows from V18–V22). Project-root CLAUDE.md slimmed 240 → 100 lines. PLAN.md renumbered (V24 inserted; old V24–V30 → V25–V31). **No method-version footer bumps** — first session under dev-internal-doesn't-bump rule.

**Decisions.** BUILD-METHOD as new file, not CLAUDE.md restructure — working manual and orientation deserve separate homes. Session tag and method-version decoupled — old convention bumped even for doc-only sessions. TEST-LOG created now, not deferred to V26 — Alex pushed back; making test outcomes queryable fixes the "plugin never installed" assertion bug.

**Pivots.** Initial framing wasted a round-trip proposing live-install session — Alex corrected: tests exist, recording isn't visible. Footer-bump convention had quietly drifted across V20/V23. INVENTORY forward-pointers semantically stale after renumber.

**Carried forward.** V23 carry-forwards remain valid. INVENTORY forward-pointer audit deferred. V28.md/V31.md "live-install session" references superseded.


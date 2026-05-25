# v64 — 2026-05-24 — Project-boundary PreToolUse hook

**What shipped.** Scope 0065. New PreToolUse check (g) — blocks Edit/Write/MultiEdit outside project root. Fires before all other writing-tool checks. Mode-aware deny with `[No-code method]` prefix. 5 new tests (152 total, zero regressions). INVENTORY, Reference manual, BUILD-METHOD updated. Footer V57→V58; plugin 0.57.0→0.58.0.

**Decisions.** Bash not blocked — parsing shell syntax for file targets is unreliable; Edit/Write/MultiEdit have explicit paths. Check placed before locked_map build to short-circuit early.

**Pivots.** None.

**Carried forward.** Bash boundary enforcement as open idea. Deferred smoke tests → 0068.


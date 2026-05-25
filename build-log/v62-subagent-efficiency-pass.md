# v62 — 2026-05-23 — Subagent efficiency pass

**What shipped.** Scope 0063. Efficiency instructions added to all five subagents (E2E findings: setup ~163k tokens, planning ~75k+). Three patterns: (1) Classify before loading — setup defers doc reads until after case detection. (2) Doc-first ordering — planning reads UX/BACKLOG before exploring code; before-build/after-build initial reads trimmed; batch-executor scoped to Files list. (3) No inner agent spawning — explicit prohibition in all five bodies. All 147 tests pass. Footer V55→V56; plugin 0.55.0→0.56.0.

**Decisions.** Doc-only (instructional guardrails, not mechanical enforcement). Mechanical enforcement can't distinguish main-Claude from subagent actions. Planning doc reads not deferred (drift checks need them) — fix targeted doc-first ordering instead.

**Pivots.** The E2E inner-agent spawn may have been main Claude misattributed to the subagent (planning lacks Agent tool). Added prohibition regardless.

**Carried forward.** V56 efficiency verification added to 0068 deferred tests.


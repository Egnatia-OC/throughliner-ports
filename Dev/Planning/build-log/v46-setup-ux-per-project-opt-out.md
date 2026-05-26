# v46 — 2026-05-22 — /setup UX + per-project opt-out

**What shipped.** V44 scope. (1) `.no-code-method-skip` marker removed from public plugin — opt-out now via Claude Code's `/plugin` toggle. Dev-project marker stays as `_LEGACY_SKIP_MARKER`. (2) `/adopt` renamed to `/setup` across entire plugin surface (skill dir, subagent, all references). (3) Three UX friction items: jargon→plain English, next-action prompts in recaps, Pass/Fail/Skipped explanations in read-back. V46 scope (cd marker walk-up) closed — marker removal made it moot. Permission-prompt surface researched (no marketplace vs `--plugin-dir` difference). Footer V41→V42; plugin 0.41.0→0.42.0.

**Decisions.** Marker removal before rename (simpler diffs). V46 closed (walk-up pointless for one legacy marker). Internal function names kept (`detect_adopt_case` etc. — never user-facing). CLI/desktop parity deferred (needs hands-on testing).

**Pivots.** Context ran out mid-session (after marker removal, before rename). Continuation clean. UX friction 4/7 resolved; 3 remain.

**Carried forward.** CLI/desktop parity testing. Remaining UX friction items 3, 5, 6. Smoke tests deferred.


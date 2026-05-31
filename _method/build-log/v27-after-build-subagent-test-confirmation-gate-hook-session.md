# V27 — 2026-05-17 — After-build subagent + test-confirmation gate hook + SessionStart TEST-LOG tripwire + [Requested]/[Suggested] labels in BACKLOG.md

**What shipped.** Test-confirmation gate wired end-to-end. New `after-build.md` subagent (MANIFEST update, labelled recap, test-session-open, idempotent). Batch-executor shed *After every build* responsibilities. Planning gains TEST-LOG read-back + inline label-writing. Before-build gains label-preservation rule. PreToolUse gains check (f): test-confirmation gate on Task → batch-executor. SessionStart gains TEST-LOG tripwire (routing override with row IDs). Stop hook gains after-build routing (BACKLOG.mtime vs TEST-LOG.mtime heuristic). `/build` command updated. DOC-STRUCTURE gains `[Requested]`/`[Suggested]` labels sub-section. NO-CODE-METHOD gains after-build handoff. Reference manual, INVENTORY, BACKLOG-TEMPLATE (×2), BUILD-METHOD updated. 19 footers bumped V26 → V27. Three V26 carry-forwards absorbed. **No smoke tests** — 13-check sweep owed post-commit.

**Decisions.** Labels live on change-list items, not Files: sub-section — a change touches many files; files-level labels would force arbitrary calls. Label work folded into V27 rather than split — files already in scope. Batch-executor must shed after-build responsibilities to avoid duplication. Stop-hook heuristic uses mtime comparison — robust to same-day second batches. TEST-LOG tripwire overrides routing, not just flags — necessary to pre-empt feature-request openers.

**Pivots.** Stale "NO-CODE-METHOD.md retired in V27" in INVENTORY — aspirational, not actual scope. Batch-executor's flags section needed restructuring post-recap-handoff. Reference manual's "hook is the gate" was aspirational at V26, now true.

**Carried forward.** Smoke testing owed. Helper-code duplication across hooks → extract to shared module in future session. Design-lock-first rhythm validated by Q3 category-error catch.


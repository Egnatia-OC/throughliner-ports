<!-- proxy | source: _method/BACKLOG/ | generated: 2026-05-31 -->

# BACKLOG — Sovereign Implementer

All deferred work and test tracking. Six sections, top-to-bottom priority. Build batches in per-batch files under `_method/BACKLOG/`. Test session files in `_method/test-log/`.

133 batches shipped or cancelled (V18–0150). Full history in `_method/proxies/build-log.md`.

## Red flags

None.

## Planning batches

None.

## Build batches

- `0147-merge-ideas-oqs.md` — Merge Ideas into Open Questions + combine ideation/deliberation.
- `0152-host-target-safeguards.md` — Host/target safeguards for self-developing project.
- `0153-planning-procedure-constraints.md` — Planning procedure: "what you don't do" constraint.
- `0130-sovsetup-case1-retest.md` — /sovsetup case 1 retest (post-fix verification). E2E test.
- `0131-build-lifecycle-retest.md` — Build lifecycle retest (post v115–v129 changes). E2E test.

Parked:
- `0151-graduation-step4-retire-protocol.md` — Graduation step 4: retire dev-side protocol files. **PARKED.**

Cancelled:
- `0146-first-graduation.md` — First graduation (replaced by 0148–0151). **CANCELLED.**
- `0095-sovtest-e2e-validation.md` — /sovtest skill E2E validation. **CANCELLED** (v153 planning — stale).

## Test sessions

- `cowboy-sovsetup-case1-2026-05-28.md` — 2026-05-28 — Cowboy test: /sovsetup case 1 (empty folder)
- `0068-e2e-round-2-taskflow-build-cycle.md` — 2026-05-24 — E2E round 2: Taskflow build cycle
- `v42-drift-check-1-direct-edit-detection-smoke-test.md` — 2026-05-21 — Drift check 1 (direct-edit detection) smoke test
- `v39-manifest-paths-field-read-before-edit-gate.md` — 2026-05-21 — MANIFEST paths field + read-before-edit gate
- `v37-marketplacejson-local-install-smoke-test.md` — 2026-05-21 — Marketplace.json + local install + smoke test
- `v35-e2e-taskflow-test-first-non-synthetic-fixture-run.md` — 2026-05-21 — E2E Taskflow test — first non-synthetic-fixture run
- `v34-git-safety-guard-hook.md` — 2026-05-21 — Git safety-guard hook
- `v32-no-code-methodmd-retired-from-plugin-runtime-subagent-in.md` — 2026-05-20 — NO-CODE-METHOD.md retired from plugin runtime; subagent inlining
- `v29-safety-net-unified-adopt-skill-command.md` — 2026-05-19 — Safety net + unified `/adopt` skill-command
- `v28-v27-fix-sweep-helpers-extraction.md` — 2026-05-18 — V27 fix sweep + helpers extraction
- `v27-test-confirmation-gate-after-build-planning-extension.md` — 2026-05-17 — Test-confirmation gate + after-build + planning extension
- `v25-windows-integration-smoke-test.md` — 2026-05-17 — Windows integration smoke test
- `v25-build-orchestration-core.md` — 2026-05-16 — Build orchestration core
- `v24-test-log-creation-build-method-doc.md` — TEST-LOG creation + BUILD-METHOD doc
- `v23-no-testable-code.md` — 2026-05-17 — no testable code
- `v18v22-backfilled-from-build-log.md` — 2026-05-16 — backfilled from BUILD-LOG
- `session-transcript.md` — session transcript

## Open questions

### Git commit access during planning
*Surfaced: v153*

The planning procedure (step 13) includes its own commit step — staging and committing with a `plan:` prefix. But `/sovgit` exists as the dedicated skill for all git operations (commit, tag, push). Having two commit paths means Claude can run git commands outside `/sovgit`, bypassing whatever guardrails that skill provides. In this session, Claude committed directly from `/sovplan` without routing through `/sovgit`.

**Why it matters.** If `/sovgit` is the single entry point for git operations, it can enforce conventions (message format, pre-commit checks, tag discipline) in one place. A separate commit step in the planning procedure splits that responsibility. On the other hand, requiring `/sovgit` after every planning session adds friction to what should be a lightweight close.

**Next step.** Decide whether planning's step 13 should commit directly (current) or hand off to `/sovgit` (single entry point). Consider whether the friction tradeoff is worth the consistency gain.

### Build-log writability during planning
*Surfaced: v153*

During this planning session, Claude successfully wrote a build-log entry for v152 (a pre-activation rename session that had no build-log record). The hook allowed it — build-log is in the method writable surface. But build-log entries are normally a `/sovclose` artifact. If Claude can create build-log entries during `/sovplan`, it could fabricate or backdate session records in a user project, or write entries for work that never went through the build pipeline.

**Why it matters.** Build-log is the project's historical record. If planning sessions can write to it freely, the record's integrity depends on Claude's judgment rather than mechanical enforcement. The v152 backfill was legitimate (documenting a real pre-activation session), but the same capability could be misused.

**Next step.** Decide whether build-log writes should be hook-gated to `/sovclose` and `/sovplan` step 13 (commit) only, or whether the current permissive surface is acceptable given that build-log entries are append-only and git-recoverable.

### Planning procedure lacks parser validation at close
*Surfaced: v153*

The planning procedure can create or modify batch files and close without confirming the result is machine-readable by the BACKLOG parser. `/sovrecap` is the first structural validation point, but by then the planning session is over. Batch 0147 was left with a `Scope:` heading and numbered items instead of the required `Changes:` delimiter, making it invisible to the parser.

**Why it matters.** A planning session that produces structurally non-compliant batches creates a gap discovered only at build time — wasting a session transition.

**Next step.** Decide whether the planning procedure's close step should run `parse_backlog.py` and require the top batch to parse, or whether a lighter check (presence of `Changes:` and `Serves UX.md:`) is sufficient.

### Pre-compact hook over-detects build phase
*Surfaced: 2026-05-31*

The pre_compact hook blocks compaction whenever it detects build-adjacent activity, but it treats `/sovrecap` as build-in-progress. Recap finishes by advising "consider /compact before /sovbuild" for large batches — then the hook blocks the very action it just recommended. No `active-build.md` exists at that point; the build hasn't been locked yet.

**Why it matters.** Large batches (24+ files) benefit from compaction between recap and build — clearing recap context gives the build more room. The current hook makes that impossible, and the conflicting advice (recap says compact, hook says no) is confusing.

**Next step.** Decide how the pre_compact hook should detect build phase. The clean signal is `active-build.md` existence — present means build in progress, absent means safe to compact. Also decide whether recap should stop suggesting /compact if the hook won't allow it, or fix the hook to match the advice.

## Ideas

None.



---
*Sovereign Implementer — Version 108.*

<!-- proxy | source: _method/BACKLOG/ | generated: 2026-05-31 -->

# BACKLOG — Sovereign Implementer

All deferred work and test tracking. Five sections, top-to-bottom priority. Build batches in per-batch files under `_method/BACKLOG/`. Test session files in `_method/test-log/`.

133 batches shipped or cancelled (V18–0150). Full history in `_method/proxies/build-log.md`.

## Red flags

None.

## Planning batches

None.

## Build batches

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

- `0069-merge-ideas-into-oqs.md` — 2026-05-31 — 4 rows (1 unconfirmed)
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

### Pre-compact hook blocks after recap but allows during builds
*Surfaced: 2026-05-31*

The pre_compact hook blocks compaction after `/sovrecap` — the point where compaction would be most useful (clearing recap context before a large build). But it allows compaction after `/sovbuild`, during an active build — the point where compaction is arguably more dangerous (Claude could lose track of build progress, close handoff notes, file states).

Recap finishes by advising "consider /compact before /sovbuild" for large batches, then the hook blocks the very action it recommended.

**Why it matters.** The hook's detection logic is inverted relative to the actual risk. Post-recap compaction is safe (no build state to lose). Mid-build compaction risks losing working context. The current behavior blocks the safe case and allows the risky one.

**Next step.** Investigate what the pre_compact hook actually checks — it's clearly not `active-build.md` existence, since that would block during builds and allow after recap. Fix the detection so it matches the actual risk profile, or decide compaction should be allowed in both cases and remove the gate entirely.

### Devside fix not carried over: per-batch files + proxy still in use
*Surfaced: 2026-05-31*

The old devside method moved away from per-batch files and the backlog proxy — Claude was supposed to read the whole BACKLOG in one go. The per-file split with a proxy index caused major build reordering problems because Claude couldn't see the full picture when making ordering decisions. The fix was to collapse everything into a single file so the whole backlog is in memory at once.

That fix was never carried over. The current plugin still uses per-batch files under `_method/BACKLOG/` with a proxy-as-index at `_method/proxies/backlog.md` — the exact structure the devside fix was meant to replace.

**Why it matters.** The same reordering problems that motivated the original fix could recur in any project using the plugin. Claude reads the proxy (batch names and one-line summaries), not the full scope/goal/dependency context of each batch. Reordering decisions made on summaries alone miss dependencies and logical sequencing that only show up in the full entries.

**Next step.** Decide whether to collapse BACKLOG back to a single file (matching the devside fix), or whether the per-batch architecture has enough compensating benefits (smaller reads during builds, cleaner diffs) to keep. If collapsing, scope a batch — parser, templates, procedures, and hooks all reference the folder structure.

### Build-produced flags and tests have no routing path to BACKLOG
*Surfaced: 2026-05-31*

During the 0147 build, `/sovclose` produced flags (stale UX.md references, stale proxy references) and a manual test recommendation (test 140) that the build couldn't resolve itself — UX.md is locked during builds, and user-verified tests can't run in a build session. These are genuinely useful outputs: the build noticed things it couldn't fix and said so. But they have no formal destination. They appear in the close output and then vanish unless the user manually carries them to BACKLOG.

A related gap: `/sovclose` already runs a doc-parity check and knows which references are stale, but it can't fix them because UX.md is locked during builds. The lock exists to prevent spec drift mid-implementation — but close isn't mid-implementation, it's after. If `/sovclose` could update UX.md references as part of its sweep, these flags wouldn't need routing at all — they'd just get fixed.

**Why it matters.** This is a new capability worth formalizing. Builds are in the best position to notice stale references, doc-parity gaps, and test gaps — but if the output isn't routed somewhere persistent, it's wasted. And some of the flagged items (like stale skill names in UX.md) are mechanical fixes that `/sovclose` could apply directly if the phase lock allowed it at close time.

**Next step.** Two questions: (1) Should `/sovclose` be allowed to make mechanical reference fixes in UX.md (not scope changes — just updating names/references to match what shipped)? If yes, the phase lock needs a close-time carve-out for non-scope edits. (2) For items close genuinely can't resolve (new tests, design questions), design the routing — options: write to BACKLOG OQ section, append to a "flags pending triage" section, or carry in build-log for planning to read. Sequence after BACKLOG single-file unification.

### Build ran /sovclose silently instead of prompting user
*Surfaced: 2026-05-31*

During the 0147 build, Claude ran `/sovclose` without prompting the user to invoke it — the close happened silently as part of wrapping up. When the user manually invoked `/sovclose` afterward, all checkpoints were already done (build-log written, test-log written, snapshot deleted, footers bumped, proxies regenerated). The close ran, but the user wasn't in the loop.

**Why it matters.** `/sovclose` is designed as a user-invoked skill — the user triggers it, sees the quality gates pass, and gets the handoff to `/sovgit`. If Claude runs it silently, the user loses visibility into what record-keeping happened, what flags were raised, and what tests need manual confirmation. The flags and manual test recommendation from the 0147 close (see "Build-produced flags" OQ above) were easy to miss precisely because close ran without the user watching.

**Next step.** Investigate whether the build procedure explicitly hands off to `/sovclose` as a user-invoked step, or whether Claude is absorbing it into its own wrap-up. If the latter, decide whether to enforce the handoff mechanically (hook that blocks close-time writes unless `/sovclose` was explicitly invoked) or procedurally (stronger instruction in build.md).

---
*Sovereign Implementer — Version 109.*

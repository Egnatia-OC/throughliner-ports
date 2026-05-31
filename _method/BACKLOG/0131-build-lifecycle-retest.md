# Build lifecycle retest (post v115–v129 changes)

**Unparked.** v142. Test plan rewritten v145 — reconciliation (0136–0139), procedure-doc fixes (0140–0142) all accounted for. Corrected skill-to-procedure attribution (blocker gate is /sovrecap not /sovbuild). Repackage plugin at HEAD before E2E run.

**Goal.** Verify the full build pipeline works end-to-end after implementation sessions v115–v129 plus reconciliation (0136–0139). Changes under test: phase detection stability (v115), pre-build sizing + compact nudges (v116), close handoff one-liners (v118), two-turn close (v128), BACKLOG rename (v129), reconciled close/build procedures (0136–0139). The last lifecycle E2E (v114/batch 0088) predates all of these.

**Inputs.** A project with a completed `/sovsetup` and at least one queued batch in BACKLOG. Can chain from 0130's output if that test passes clean. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. `/sovplan` — create or confirm a queued batch in `_method/BACKLOG/`. Verify folder mode: per-batch file created + BACKLOG proxy reference updated. No BUILD-PLAN references.
2. `/sovrecap` — verify: batch parses correctly, serves-line resolves against UX.md, blocker gate runs 5 checks (batch OQs, planning batches, BACKLOG OQs, test sessions, ideas/red flags). Files: and Tests: sub-sections populated with correct format. Recap presented with `[PROMPT]` recommending `/sovbuild` + compact nudge. If batch has 8+ files AND open decisions, verify pre-build sizing warning fires.
3. `/sovbuild` (snapshot) — verify: `_method/active-build.md` created with full batch content + `## Close handoff` (empty). Batch removed from BACKLOG (per-batch file deleted, proxy reference removed). Snapshot message shown to user.
4. `/sovbuild` (work loop) — build at least a few files. Verify: ticks update per file in `_method/active-build.md` (not batched at end). Close handoff one-liners accumulate as files are ticked. Phase detection holds as "build" throughout (v115).
5. `/sovbuild` (completion) — verify `[PROMPT]` recommends `/compact` before `/sovclose`.
6. `/sovclose` (judgment turn) — verify: MANIFEST updated per ticked files (step 1). TEST-LOG rows written in 10-column format (step 4a). Claude-automatable tests run (step 4b). Build recap (step 5) with `[Requested]`/`[Suggested]` labels, Claude-verified results, user-check list. Build-log entry written with Performance section (step 6). `_method/active-build.md` deleted (step 7). Idea sweep (step 12). Turn boundary `[PROMPT]` (step 13) recommends `/compact`.
7. `/sovclose` (mechanical turn) — verify: `bump_version.py` runs if applicable (step 14). Proxies regenerated (step 15). Pre-commit checkpoint complete (step 17). Closing `[PROMPT]` (step 18) recommends `/sovgit` and mentions `/sovtest`.
8. `/sovgit` — verify commit prompt, tag prompt, push prompt in sequence.

**Success criteria.** Full pipeline completes with no broken references, no BUILD-PLAN ghosts, no hook blocks on legitimate writes. Snapshot architecture works (create, tick, delete). Phase detection stable through build. Two-turn close produces all artifacts (MANIFEST, TEST-LOG, build-log, proxies). Consumer `bump_version.py` runs without errors. All BACKLOG naming correct throughout.

**Risks / dependencies.** Depends on a set-up project — chains from 0130, or use an existing one. Risk: if 0130 surfaces scaffold issues, this test's starting state may be compromised. Mitigant: can use Taskflow or another already-adopted project instead.

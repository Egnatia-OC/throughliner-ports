# BACKLOG — Sovereign Implementer

All deferred work and test tracking. Five sections, top-to-bottom priority. Test session files in `_method/test-log/`.

133 batches shipped or cancelled (V18–0150). Full history in `_method/proxies/build-log.md`.

## Red flags

None.

## Planning batches

None.

## Build batches

### Batch: Host/target safeguards for self-developing project

**Goal.** Prevent Claude from confusing the installed plugin (host SI) with the source code being edited (target SI). Three failure modes identified in v152: (1) expecting target edits to take effect immediately, (2) editing the wrong copy of a doc, (3) hooks validating template files as real project files.

**Outputs.** CLAUDE.md behavioral rules in the Host SI vs Target SI section.

**Success criteria.** Claude states "editing target SI" when touching `plugin/` files. Claude never claims target changes are live without reinstall. Claude uses full paths when referencing docs that exist in both `_method/` and `plugin/templates/`.

Changes:
- [Requested] Add behavioral rules to CLAUDE.md Host SI vs Target SI section: state when editing target SI, never expect target changes to take effect, use full paths for ambiguous docs.

Files:
- [ ] `CLAUDE.md` — Add behavioral rules to Host SI vs Target SI section for self-developing project orientation.

Serves UX.md: Session-open orientation.

### Batch: Planning procedure: "what you don't do" constraint

**Goal.** Prevent Claude from offering to implement changes during /sovplan sessions. Currently procedures/planning.md defines what planning does but not what it doesn't — the V67 carve-out for source-of-truth doc editing creates ambiguity about what's allowed vs what should route through a build batch.

**Outputs.** Updated procedures/planning.md with explicit constraints section.

**Success criteria.** Claude never offers to "implement now" during a /sovplan session. All non-BACKLOG changes route through build batches. The distinction between "editing scope docs to reflect planning decisions" (allowed) and "implementing new rules or features" (not allowed, even as doc edits) is explicit.

Changes:
- [Requested] Add "What you don't do" section to procedures/planning.md. At minimum: don't implement, don't build, don't edit CLAUDE.md project-specific notes outside scope decisions. All changes route through BACKLOG.
- [Suggested] Clarify V67 boundary: source-of-truth doc edits during planning are for scope decisions (adding/removing/revising UX entries), not for implementing behavioral rules or project configuration.
- [Suggested] Fix invalid escape sequence `\`` in pre_tool_use.py line 681 (SyntaxWarning on Python 3.12+; will become an error in a future version). Use raw string or `\\``.

Files:
- [ ] `plugin/docs/procedures/planning.md` — Add "What you don't do" constraints section; clarify V67 source-of-truth doc edit boundary.
- [ ] `plugin/hooks/pre_tool_use.py` — Fix invalid escape sequence on line 681.

Serves UX.md: Planning sessions.

### Batch: /sovsetup case 1 retest (post-fix verification)

**Unparked.** v142. Test plan rewritten v145 — reconciliation (0136–0139), /sovexplain (0140), plugin OQ fixes (0141–0142) all accounted for. Repackage plugin at HEAD before E2E run.

**Goal.** Verify that v113, v115, v117, and v129 changes work end-to-end in a real `/sovsetup` case 1 run. v113/v115 fixed hook path resolution (7 cowboy-test issues from plugin v90). v117 added setup Q5 (language setting) and BOM hardening. v129 renamed BUILD-PLAN → BACKLOG across the plugin. None verified E2E.

**Inputs.** Fresh empty folder. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. Invoke `/sovsetup` on empty folder. Confirm `detect-case` returns case 1.
2. Walk through all five questions with test content. Verify Q5 (language setting) appears. Answer Q1–Q4 in a non-English language to test Q5 default detection.
3. After scaffold: verify full output structure — `_method/` with `UX.md`, `MANIFEST.md`, `BACKLOG.md`, `build-log/`, `test-log/`, `planning/drafts/`, `research/`, `research/search-queries/`, `proxies/` (4 proxy files: ux, manifest, research, build-log). `CLAUDE.md` at root. BACKLOG is a single file (not a folder).
4. After Q answers applied: verify doc population. Q1 → CLAUDE.md `## Product overview` (4 fields) + UX.md `## Project context`. Q2 → UX.md `## UX principles`. Q3 → UX.md `## Functionalities` with `###` entries. Q4 → inline `### Batch:` entry in `_method/BACKLOG.md` with scope content. Q5 → CLAUDE.md `## Language` field + `git config --local core.quotepath false` (if `.git/` exists).
5. Hook path validation (planning phase): Edit `_method/BACKLOG.md` → allowed. Edit `_method/proxies/ux.md` → allowed. Edit `_method/planning/drafts/<file>.md` → allowed. Edit `_method/research/<file>.md` → allowed.
6. Bash heredoc test: write a heredoc containing markdown headings → verify no false-positive filename extraction from the write-guard.
7. BOM hardening: verify scaffolded files don't contain BOM bytes that break `safe_read_text()`.
8. Verify recap message and handoff. Handoff should direct to `/sovplan` or `/sovrecap` + `/sovbuild` depending on Q4 scope completeness.

**Success criteria.** Clean case 1 setup with no hook blocks on method-file writes. Full scaffold structure correct. All five Q answers persist in the right docs. Language default detection works. BACKLOG naming throughout. Handoff message matches Q4 scope state.

**Risks / dependencies.** Requires repackaging plugin at HEAD. If scaffold.py still outputs `BUILD-PLAN/` paths (missed in v129 rename), the test surfaces it immediately at step 3.

### Batch: Build lifecycle retest (post v115–v129 changes)

**Unparked.** v142. Test plan rewritten v145 — reconciliation (0136–0139), procedure-doc fixes (0140–0142) all accounted for. Corrected skill-to-procedure attribution (blocker gate is /sovrecap not /sovbuild). Repackage plugin at HEAD before E2E run.

**Goal.** Verify the full build pipeline works end-to-end after implementation sessions v115–v129 plus reconciliation (0136–0139). Changes under test: phase detection stability (v115), pre-build sizing + compact nudges (v116), close handoff one-liners (v118), two-turn close (v128), BACKLOG rename (v129), reconciled close/build procedures (0136–0139). The last lifecycle E2E (v114/batch 0088) predates all of these.

**Inputs.** A project with a completed `/sovsetup` and at least one queued batch in BACKLOG. Can chain from 0130's output if that test passes clean. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. `/sovplan` — create or confirm a queued batch in `_method/BACKLOG.md`. Verify single-file mode: inline `### Batch:` entry in BACKLOG.md. No BUILD-PLAN references.
2. `/sovrecap` — verify: batch parses correctly, serves-line resolves against UX.md, blocker gate runs 5 checks (batch OQs, planning batches, BACKLOG OQs, test sessions, ideas/red flags). Files: and Tests: sub-sections populated with correct format. Recap presented with `[PROMPT]` recommending `/sovbuild` + compact nudge. If batch has 8+ files AND open decisions, verify pre-build sizing warning fires.
3. `/sovbuild` (snapshot) — verify: `_method/active-build.md` created with full batch content + `## Close handoff` (empty). Batch removed from BACKLOG (inline `### Batch:` entry removed from BACKLOG.md). Snapshot message shown to user.
4. `/sovbuild` (work loop) — build at least a few files. Verify: ticks update per file in `_method/active-build.md` (not batched at end). Close handoff one-liners accumulate as files are ticked. Phase detection holds as "build" throughout (v115).
5. `/sovbuild` (completion) — verify `[PROMPT]` recommends `/compact` before `/sovclose`.
6. `/sovclose` (judgment turn) — verify: MANIFEST updated per ticked files (step 1). TEST-LOG rows written in 10-column format (step 4a). Claude-automatable tests run (step 4b). Build recap (step 5) with `[Requested]`/`[Suggested]` labels, Claude-verified results, user-check list. Build-log entry written with Performance section (step 6). `_method/active-build.md` deleted (step 7). Idea sweep (step 12). Turn boundary `[PROMPT]` (step 13) recommends `/compact`.
7. `/sovclose` (mechanical turn) — verify: `bump_version.py` runs if applicable (step 14). Proxies regenerated (step 15). Pre-commit checkpoint complete (step 17). Closing `[PROMPT]` (step 18) recommends `/sovgit` and mentions `/sovtest`.
8. `/sovgit` — verify commit prompt, tag prompt, push prompt in sequence.

**Success criteria.** Full pipeline completes with no broken references, no BUILD-PLAN ghosts, no hook blocks on legitimate writes. Snapshot architecture works (create, tick, delete). Phase detection stable through build. Two-turn close produces all artifacts (MANIFEST, TEST-LOG, build-log, proxies). Consumer `bump_version.py` runs without errors. All BACKLOG naming correct throughout.

**Risks / dependencies.** Depends on a set-up project — chains from 0130, or use an existing one. Risk: if 0130 surfaces scaffold issues, this test's starting state may be compromised. Mitigant: can use Taskflow or another already-adopted project instead.

### Batch: Graduation step 4: retire dev-side protocol files

Status: parked

**Parked.** v149. Ship after 2–3 sessions of real work under self-management (post-0150). Build confidence that the plugin's procedures cover everything these files provide before deleting them.

**Goal.** Retire session-protocol.md, session-reference.md, and INVENTORY.md once the plugin has proven it covers the same ground through actual use.

**Approach.** Section-by-section comparison: for each section in the dev files, verify the plugin has a matching mechanism (procedure doc step, hook check, template field, VOCABULARY entry). File gap-batches for anything missing. Archive the retired files.

**Outputs.** Retired files archived. Gap-batches filed if any coverage holes found.

**Success criteria.** No dev-side rule exists that isn't enforced or documented plugin-side. CLAUDE.md project-specific notes carry any project-specific rules that don't belong in the plugin generally.

**Standing constraint (all graduation batches).** Copy, don't move. Dev/ originals stay in place as a safety net. `_method/` is canonical; Dev/ is the fallback. Do not delete, rename, or git-rm any Dev/ file as part of graduation work. This batch is the *only* one that may eventually retire Dev/ files — and only after real sessions prove coverage.

**Risks / dependencies.** Depends on 0150 (must have working self-management first). Risk: retiring too early and discovering a gap mid-session. Mitigant: parking condition requires real sessions first.

## Test sessions

- `0069-merge-ideas-into-oqs.md` — 2026-05-31 — 4 rows (0 unconfirmed)
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

The planning procedure can create or modify batch entries and close without confirming the result is machine-readable by the BACKLOG parser. `/sovrecap` is the first structural validation point, but by then the planning session is over. Batch 0147 was left with a `Scope:` heading and numbered items instead of the required `Changes:` delimiter, making it invisible to the parser.

**Why it matters.** A planning session that produces structurally non-compliant batches creates a gap discovered only at build time — wasting a session transition.

**Next step.** Decide whether the planning procedure's close step should run `parse_backlog.py` and require the top batch to parse, or whether a lighter check (presence of `Changes:` and `Serves UX.md:`) is sufficient.

### Pre-compact hook blocks after recap but allows during builds
*Surfaced: 2026-05-31*

The pre_compact hook blocks compaction after `/sovrecap` — the point where compaction would be most useful (clearing recap context before a large build). But it allows compaction after `/sovbuild`, during an active build — the point where compaction is arguably more dangerous (Claude could lose track of build progress, close handoff notes, file states).

Recap finishes by advising "consider /compact before /sovbuild" for large batches, then the hook blocks the very action it recommended.

**Why it matters.** The hook's detection logic is inverted relative to the actual risk. Post-recap compaction is safe (no build state to lose). Mid-build compaction risks losing working context. The current behavior blocks the safe case and allows the risky one.

**Next step.** Investigate what the pre_compact hook actually checks — it's clearly not `active-build.md` existence, since that would block during builds and allow after recap. Fix the detection so it matches the actual risk profile, or decide compaction should be allowed in both cases and remove the gate entirely.

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
*Sovereign Implementer — Version 110.*

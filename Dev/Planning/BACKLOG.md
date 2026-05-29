# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

## Shipped history

124 batches shipped or cancelled (V18–0135). Full history in `Dev/Planning/build-log/INDEX.md`. Per-batch details in individual build-log files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0095 — /sovtest skill E2E validation — **PARKED**

**Parked.** v114. 0088 shipped — dep met. Shelved: user is cowboy-testing informally rather than running structured E2E batches. Revisit when there's a specific reason to formalize. Note: 0120 merges TEST-LOG into BACKLOG — when this batch unparks after 0120 ships, the test plan needs a full rewrite against the merged BACKLOG structure.

**Goal.** End-to-end test of `/sovtest` skill (shipped in 0094) against a real project. Validate the full flow: invoke after build, follow guided walkthrough, report failure, get debugging support.

**Inputs.** `/sovtest` skill and `plugin/docs/procedures/testing.md` (from 0094). A burner app with pending TEST-LOG rows across multiple test types. `Dev/Resources/research/e2e-greenfield-post-redesign.md`.

**Outputs.** Research file `Dev/Resources/research/e2e-test-skill-validation.md`. New BACKLOG entries for issues. `/sovclose` handoff validation.

**Test plan.** Happy path: invoke `/sovtest`, walk through Look-and-click and Run-and-read tests, report Pass, verify row updates. Failure path: report Fail, verify debugging protocol, verify routing to BACKLOG. Edge cases: no pending tests (graceful exit), mid-build invocation (rejected), partial progress on early stop. Handoff: confirm planning read-back handles rows `/sovtest` already confirmed.

**Success criteria.** Non-coder completes full flow without independent knowledge. Debugging produces useful output on deliberate failure. TEST-LOG state after `/sovtest` is consistent with planning expectations. No silent failures.

**Risks / dependencies.** Hard dep on 0094 (shipped v100). Soft dep on 0088 (reuse app state — note: 0088 now starts fresh, so test-type variety depends entirely on what that build produces). Risk: insufficient test-type variety in burner app. Hard dep on pre-0120 TEST-LOG structure — if 0120 ships first (expected), rewrite test plan against merged BACKLOG.

---

### 0136 — Dev-side rules reconciliation

**Goal.** Add prose equivalents of 10 plugin behavioural rules to the dev-side method. These rules exist in `universal-behaviour.md` but have no dev-side counterparts in `session-protocol.md` or `CLAUDE.md`. Also resolve contradictions C03 (flag taxonomy — add red-flag routing) and C04 (command execution — clarify context).

**Inputs.** `Dev/Resources/research/convergence-reconciliation-v134.md` → gaps G01–G10, contradictions C03, C04. Plugin-side source: `plugin/hooks/universal-behaviour.md`.

**Outputs.** Updated `Dev/session-protocol.md` (new rules in session-middle, session-open, session-close sections). Updated project `CLAUDE.md` (collaboration rules). Reconciliation map checkboxes ticked for resolved items.

**Success criteria.** All 12 items (G01–G10, C03, C04) have prose equivalents. Each rule adapted for dev context — not copy-pasted from plugin. No redundancy with existing dev-side rules. Reconciliation map updated.

**Risks / dependencies.** Hard dep on 0135 (shipped v134). Risk: some rules may not translate cleanly to prose-only enforcement — flag and resolve during session.

---

### 0137 — Dev-side workflow reconciliation

**Goal.** Add five workflow steps to the dev-side close and open procedures: build recap (G11), consolidated end-of-recap flags (G12), staleness sweep as literal path check (G22), lost-feature check for parked batches (G23), and OQ staleness detection at session open (G24).

**Inputs.** `Dev/Resources/research/convergence-reconciliation-v134.md` → gaps G11–G12, G22–G24. Plugin-side source: `plugin/docs/procedures/close.md`, `plugin/docs/VOCABULARY.md`.

**Outputs.** Updated `Dev/session-protocol.md` (new steps in implementation close, lighter close conditional, session-open state summary). Reconciliation map checkboxes ticked.

**Success criteria.** All 5 items have dev-side procedure steps at the correct points in the close/open flow. Step numbering and cross-references updated. Reconciliation map updated.

**Risks / dependencies.** Soft dep on 0136 — workflow steps reference rules 0136 establishes (e.g. red-flag routing from G02/C03 feeds into G12's consolidated flags). Can ship independently but better after 0136.

---

### 0138 — Dev-side structure reconciliation

**Goal.** Define entry shapes and structural specs for five dev-side artifacts that exist but lack documentation in `session-reference.md`: INVENTORY.md entries (G17), research folder files (G18), proxy files (G19), test sessions index (G20), Ideas section entries (G21). Also add cross-reference for "queued batch" = "build batch" (C10) and flow OQ graduation paths to plugin consideration (C16).

**Inputs.** `Dev/Resources/research/convergence-reconciliation-v134.md` → gaps G17–G21, contradictions C10, C16. Existing dev artifacts for shape extraction: `Dev/INVENTORY.md`, `Dev/Resources/research/`, `Dev/Planning/.proxies/`, `Dev/Planning/test-log/`, `Dev/Planning/BACKLOG.md` Ideas section.

**Outputs.** Updated `Dev/session-reference.md` (new entry-shape sections). Reconciliation map checkboxes ticked.

**Success criteria.** All 7 items documented. Entry shapes derived from actual current practice — not invented. Reconciliation map updated.

**Risks / dependencies.** No hard deps — can ship in any order relative to 0136/0137. Logically last among doc-only batches because it documents artifacts the other batches reference.

---

### 0139 — Plugin lighter-close hardening

**Goal.** Add four missing steps to the plugin's lighter close path in `close.md`. The convergence reader test found the dev-side lighter close is more complete: it includes a build-log entry (G13), conditional footer bump (G14), pre-commit checkpoint (G15), and conditional frame-correction sweep (G16). The plugin lighter close has none of these.

**Inputs.** `Dev/Resources/research/convergence-reconciliation-v134.md` → gaps G13–G16. Dev-side source: `Dev/session-protocol.md` → lighter close (L136–181). Plugin-side target: `plugin/docs/procedures/close.md`.

**Outputs.** Updated `plugin/docs/procedures/close.md` (lighter close path expanded). Reconciliation map checkboxes ticked. Doc-parity updates if close.md changes affect other plugin docs.

**Success criteria.** Plugin lighter close includes all four steps, adapted for plugin context (consumer projects, hook enforcement, skill invocations). Step ordering consistent with dev-side lighter close. Reconciliation map updated.

**Risks / dependencies.** Hard dep on 0137 — workflow reconciliation may refine the dev-side lighter close steps that 0139 ports to the plugin. Should ship after dev-side prose is stable.

---

### 0130 — /sovsetup case 1 retest (post-fix verification) — **PARKED**

**Parked.** v134. Reconciliation batches (0136–0139) change instruction surfaces this test validates. Retest after reconciliation completes. When unparking: repackage plugin at HEAD (post-0139), verify test plan still covers current state.

**Goal.** Verify that v113, v115, v117, and v129 changes work end-to-end in a real `/sovsetup` case 1 run. The cowboy test (plugin v90) found 7 hook issues; v113 and v115 shipped fixes for most of them. v117 added setup Q5 (language setting). v129 renamed BUILD-PLAN → BACKLOG across the entire plugin. None of these fixes have been verified E2E.

**Inputs.** Fresh empty folder. Plugin repackaged at current HEAD (v97 / 0.97.0).

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. Invoke `/sovsetup` on empty folder. Confirm case 1 detected.
2. Walk through all five questions (Q1–Q4 as before, Q5 should be the new language setting from v117). Verify Q5 appears and the answer flows into `CLAUDE.md` and `core.quotepath` config.
3. After scaffold: verify output uses `BACKLOG/` directory name (not `BUILD-PLAN/`). Verify BACKLOG proxy includes `## Test sessions` section. Verify no `test-log.md` proxy was created.
4. After Q answers applied: attempt Edit on `_method/BACKLOG/<batch>.md` — should succeed (cowboy issue 1 fix). Attempt Edit on `_method/proxies/ux.md` — should succeed (cowboy issue 2 fix). Attempt Edit on `_method/planning/drafts/<file>.md` — should succeed (cowboy issue 6 fix).
5. Write a heredoc/here-string containing markdown headings — verify no false-positive filename extraction (cowboy issue 3 fix).
6. Attempt Write to a file outside the project root (e.g. Desktop) — verify not blocked by Edit/Write path (cowboy issues 4/7 fix). Note: Bash write-guard still enforces its own boundary, which is correct.
7. Verify scaffolded files don't contain BOM bytes that break `safe_read_text()` (v117 BOM hardening).

**Success criteria.** Clean case 1 setup with no hook blocks on method-file writes. All 7 cowboy-test issues resolved or clearly scoped. Language question appears and persists correctly. BACKLOG naming throughout.

**Risks / dependencies.** Requires repackaging plugin at HEAD. If scaffold.py still outputs `BUILD-PLAN/` paths (missed in v129 rename), the test surfaces it immediately at step 3.

---

### 0131 — Build lifecycle retest (post v115–v129 changes) — **PARKED**

**Parked.** v134. Reconciliation batches (0136–0139) change close procedure and instruction surfaces this test validates. Retest after reconciliation completes. When unparking: repackage plugin at HEAD (post-0139), verify test plan covers reconciled close procedure. Note: if 0139 changes plugin close.md, steps 5–6 of the test plan need review.

**Goal.** Verify the full build pipeline works end-to-end after six implementation sessions (v115, v116, v117, v118, v128, v129) that changed phase detection, close procedure, naming, and safeguards. The last lifecycle E2E (v114/batch 0088) predates all of these. The v129 BACKLOG rename alone touched ~30 plugin files — any missed reference breaks path resolution.

**Inputs.** A project with a completed `/sovsetup` and at least one queued batch in BACKLOG. Can chain from 0130's output if that test passes clean. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. `/sovplan` — create or confirm a queued batch. Verify it lands in `_method/BACKLOG/` (not `BUILD-PLAN/`). Verify BACKLOG proxy updates.
2. `/sovrecap` — verify it reads BACKLOG correctly and presents batch state.
3. `/sovbuild` (before-build phase) — verify blocker gate runs all 5 checks (batch OQs, planning batches, BACKLOG OQs, test sessions, ideas/red flags) per v129 expansion. Verify pre-build sizing warning fires if batch has 8+ files AND open decisions (v116). Lock the batch.
4. `/sovbuild` (build phase) — build at least a few files. Verify phase detection holds as "build" throughout (v115 fix). Verify close handoff one-liners accumulate in `active-build.md` → `## Close handoff` as files are ticked (v118).
5. `/sovclose` (judgment turn) — verify two-turn procedure (v128): MANIFEST, doc-parity, frame-correction, idea sweep. Verify it stops at the turn boundary and recommends `/compact`.
6. `/sovclose` (mechanical turn) — verify `bump_version.py` runs (v128). Verify proxy regeneration. Verify checkpoint list. Verify all references say BACKLOG not BUILD-PLAN (v129).
7. `/sovgit` — verify commit prompt, tag, push prompts. Verify compact nudge at done prompt (v116).
8. Throughout: verify compact nudges fire at skill-handoff `[PROMPT]` points between steps (v116).

**Success criteria.** Full pipeline completes with no broken references, no BUILD-PLAN ghosts, no hook blocks on legitimate writes. Phase detection stable through build. Two-turn close works as designed. Consumer `bump_version.py` runs without errors.

**Risks / dependencies.** Depends on a set-up project — chains from 0130, or use an existing one. Risk: if 0130 surfaces scaffold issues, this test's starting state may be compromised. Mitigant: can use Taskflow or another already-adopted project instead.

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### TEST-LOG columns — 10 vs 7

Dev-side TEST-LOG uses 7 columns (#, Date, Session, Test, Component, Status, Notes). Plugin-side defines 10 (#, Date, Session, Component, Test Description, Type, Verifier, Status, Confirmed Explicitly, Notes). Three columns absent from dev side: Type, Verifier, Confirmed Explicitly. Column ordering also differs (Component before Test Description in plugin; Test before Component in dev). The 7-column shape was a deliberate simplification — dev tests have no hook-enforced confirmation gate and Alex runs all tests herself. Question: keep the divergence (different contexts, different needs) or migrate to 10 columns for convergence?

**Surfaced.** v134.

---

### Batch lifecycle on completion — remove vs preserve

Dev side removes completed batches from BACKLOG (relies on build-log for history). Plugin side writes them back with `Status: shipped` (preserves history in BACKLOG). Different models for the same lifecycle event. Dev model keeps BACKLOG lean; plugin model keeps it as a single queryable history. Question: which model should the converged method use? Or is the divergence intentional (dev BACKLOG has build-log as companion; consumer BACKLOG may not)?

**Surfaced.** v134.

---

### Volunteered test results vs. mechanical read-back

When a user's opener already contains test results ("settings toggle passed, export button misaligned"), should the method accept those as partial confirmation or insist on the per-row mechanical read-back? The read-back is the only defined confirmation mechanism, but forcing users to re-state results they already gave is bad UX. Related: the confirmation format itself is undefined — instructions say what NOT to accept (bulk confirmations, inference from absence) but never what TO accept as valid per-row confirmation.

**Surfaced.** v131.

---

### Re-batching snapshot state after split

After a re-batching carve-out splits unticked files into new batches, what happens to the build snapshot (`_method/active-build.md`)? Does it shrink to only the ticked files? Does `/sovclose` still run on the reduced snapshot? The build procedure says "Ticked files stay; unticked move to new batch(es)" but doesn't specify the snapshot's resulting state or confirm `/sovclose` handles a partial snapshot correctly.

**Surfaced.** v131.

---

### Step-by-step test protocol — where should it live?

Testing sessions that involve user-guided steps (E2E tests, Look-and-click, Run-and-read) consistently dump full step lists despite the user's one-at-a-time instruction. Cowboy tests are exempt — those are freeform user exploration with no guided walkthrough. The fix needs to go somewhere Claude reads during test sessions. Candidates: `plugin/docs/procedures/testing.md`, `universal-behaviour.md`, or both. Question: which location actually gets loaded in the test context, and is one enough or does it need reinforcement in both?

**Surfaced.** v130.

---

---

## Ideas

Raw ideas captured during sessions. Date + one-liner. Promoted to OQs or batches during planning sessions.

---

# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

## Shipped history

122 batches shipped or cancelled (V18–0133). Full history in `Dev/Planning/build-log/INDEX.md`. Per-batch details in individual build-log files.

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

### 0135 — Convergence reader test (stage 1 — initial reconciliation)

**Goal.** Run the stage 1 convergence reader test to build the complete overlap map between the plugin-side method and the dev-side prose method. The two sides were built up independently with piecemeal patches; they have never been systematically compared. This batch produces the reconciliation map — not edits.

**Inputs.** `Dev/Resources/Iteration playbook/Convergence reader test (stage 1).md` (prompt and procedure). Plugin-side: `plugin/hooks/universal-behaviour.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `plugin/docs/procedures/close.md`. Dev-side: `Dev/session-protocol.md`, `Dev/session-reference.md`, project `CLAUDE.md`.

**Outputs.** Research file `Dev/Resources/research/convergence-reconciliation-v<N>.md` with the full classified inventory: aligned, contradicts, stale, plugin-only (expected), plugin-only (gap), dev-only (preserve), dev-only (stale). Category counts. Punch list for reconciliation work. New BACKLOG entries for reconciliation batches if the map is large enough to split.

**Success criteria.** Every rule, entry shape, term, and workflow step that exists on either side is accounted for in the map. No unclassified items. The map is concrete enough to plan reconciliation batches from.

**Risks / dependencies.** Depends on 0133 and 0134 shipping first — both change plugin instruction surfaces that stage 1 reads. Sub-agent C defaults to `close.md`; rotate in future runs per playbook refinements. Risk: map may be very large if drift is extensive — plan for the reconciliation to span multiple sessions.

---

### 0130 — /sovsetup case 1 retest (post-fix verification)

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

### 0131 — Build lifecycle retest (post v115–v129 changes)

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

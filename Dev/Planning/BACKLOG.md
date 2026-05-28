# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

## Shipped history

118 batches shipped or cancelled (V18–0125). Full history in `Dev/Planning/build-log/INDEX.md`. Per-batch details in individual build-log files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0123 — Plugin-side close mechanicals + two-turn procedure

**Goal.** Port the dev-side close improvements (scripted mechanicals and two-turn structure) to the plugin side.

**Approach.** Consumer-side version bump script at `plugin/scripts/bump_version.py` (or folded into `/sovclose` procedure) handling the consumer project's footer bumps and proxy regeneration. Update `close.md` with two-turn structure: judgment pass (parity, frame corrections, build-log narrative, idea sweep) then `/compact` boundary then mechanical pass (script run, proxy regen, commit/tag/push). Reference manual note.

**Outputs.** Consumer-side `bump_version.py` or `/sovclose` integration. Updated `close.md` with two-turn structure and script reference. Reference manual update.

**Success criteria.** Consumer-side script produces correct footer bumps, verified by `git diff`. Two-turn close structure works in `/sovclose` flow. Reference manual documents both the script and the two-turn pattern.

**Risks / dependencies.** Dev-side 0118 and 0119 (pattern proven on dev side first). Consumer-side footer patterns differ from dev-side — script needs to handle both or be a separate implementation. Low risk given dev-side script proves the approach.

---

### 0120 — BACKLOG convergence: naming and test merge (plugin-side)

**Goal.** Fix plugin-side naming and eliminate the blind spot where tests and builds can't see each other during planning.

**Approach.** Reverse the 0112 BUILD-PLAN rename back to BACKLOG. Merge TEST-LOG into BACKLOG so planning always sees tests and builds together. Expand the blocker gate in before-build.md to scan all sections (Planning batches, Ideas, OQs, and test entries) for anything blocking the upcoming build.

**Outputs.** Plugin-side: BUILD-PLAN renamed to BACKLOG everywhere (DOC-STRUCTURE, templates, proxies, procedure docs, hooks, skills, crash course, pytest fixtures). TEST-LOG content merged into BACKLOG structure. Blocker gate expanded.

**Success criteria.** Plugin side uses BACKLOG as the name. Plugin-side BACKLOG contains test tracking alongside build batches. Blocker gate scans all sections before a build starts. No orphaned BUILD-PLAN or TEST-LOG references remain.

**Risks / dependencies.** Large surface area — the rename touches ~30+ files (same as 0112 did going the other direction). TEST-LOG merge changes the proxy structure and may require test-log proxy retirement or redesign. Risk: batch is too large for one session — likely needs splitting at before-build time (rename pass vs. structural changes vs. blocker gate).

---

### 0095 — /sovtest skill E2E validation — **PARKED**

**Parked.** v114. 0088 shipped — dep met. Shelved: user is cowboy-testing informally rather than running structured E2E batches. Revisit when there's a specific reason to formalize. Note: 0120 merges TEST-LOG into BACKLOG — when this batch unparks after 0120 ships, the test plan needs a full rewrite against the merged BACKLOG structure.

**Goal.** End-to-end test of `/sovtest` skill (shipped in 0094) against a real project. Validate the full flow: invoke after build, follow guided walkthrough, report failure, get debugging support.

**Inputs.** `/sovtest` skill and `plugin/docs/procedures/testing.md` (from 0094). A burner app with pending TEST-LOG rows across multiple test types. `Dev/Resources/research/e2e-greenfield-post-redesign.md`.

**Outputs.** Research file `Dev/Resources/research/e2e-test-skill-validation.md`. New BACKLOG entries for issues. `/sovclose` handoff validation.

**Test plan.** Happy path: invoke `/sovtest`, walk through Look-and-click and Run-and-read tests, report Pass, verify row updates. Failure path: report Fail, verify debugging protocol, verify routing to BUILD-PLAN. Edge cases: no pending tests (graceful exit), mid-build invocation (rejected), partial progress on early stop. Handoff: confirm planning read-back handles rows `/sovtest` already confirmed.

**Success criteria.** Non-coder completes full flow without independent knowledge. Debugging produces useful output on deliberate failure. TEST-LOG state after `/sovtest` is consistent with planning expectations. No silent failures.

**Risks / dependencies.** Hard dep on 0094 (shipped v100). Soft dep on 0088 (reuse app state — note: 0088 now starts fresh, so test-type variety depends entirely on what that build produces). Risk: insufficient test-type variety in burner app. Hard dep on pre-0120 TEST-LOG structure — if 0120 ships first (expected), rewrite test plan against merged BACKLOG.

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### Frame-correction sweep: categorical vs conditional skip in lighter close

**Surfaced.** v120 (0121 reader test, M2).

**The question.** The lighter close skips the frame-correction sweep categorically ("no feature frame changed"). But a doc-only session consuming a queued batch could change a load-bearing frame (e.g. rewriting how a concept is described in BACKLOG scope text). Should the skip be conditional on whether a frame actually changed, rather than categorical by session type?

**Why it matters.** A doc-only batch that rewrites scope text could leave queued batches referencing an old frame — exactly what the sweep catches. The categorical skip assumes lighter-close sessions never change frames, which isn't guaranteed.

**Next step.** Park. Low frequency — doc-only sessions rarely change frames. Revisit if a frame-change slips through a lighter close.

---

### Remote-control standby close path unspecified

**Surfaced.** v120 (0121 reader test, M4).

**The question.** The routing table says remote-control standby sessions use the close path that matches "the work done," but gives no guidance on classifying what was done — or whether a commit/tag/push is expected if nothing was done.

**Why it matters.** Standby sessions are rare in practice (most sessions have a clear type), but when they occur, the lack of close-path guidance means Claude has to improvise. A "no work done → no close needed" rule, or a "classify the work and follow the matching close" rule, would be sufficient.

**Next step.** Park. Very low frequency. Revisit if standby sessions become more common or if a standby session produces an awkward close.

---

### Sub-agent warning rule boundary for scoped work

**Surfaced.** v120 (0121 reader test, M7).

**The question.** CLAUDE.md says "warn before spawning a subagent for a single simple operation." When the batch scope explicitly designs for sub-agents (as 0121 did), does the warning rule still apply?

**Why it matters.** The fresh-session agent flagged the warning as a courtesy even though the batch scope explicitly called for three sub-agents. The rule is written for spontaneous single-operation spawning — not intentionally scoped multi-agent work. Clarifying the boundary would prevent unnecessary warnings on designed sub-agent deployments while preserving the guard on ad hoc spawning.

**Next step.** Park. Low friction — Claude flagging an unnecessary warning is a minor cost. Revisit if sub-agent-designed batches become more common.

---

### Cross-reference precision across dev-side docs

**Surfaced.** v120 (0121 reader test, B2/B3/B4/B5).

**The question.** Four related precision issues in cross-references between dev-side docs: (a) session-protocol.md step 4 relies entirely on a forward pointer to session-reference.md with no inline explanation; (b) session-reference.md's build-log entry shape references DOC-STRUCTURE.md without a path; (c) CLAUDE.md says "read proxies first" while session-protocol.md step 3 says "read BACKLOG in full" without mentioning proxies; (d) the pre-commit checkpoint in each close path references its own step numbers, making cross-path comparison confusing.

**Why it matters.** Individually minor. Collectively, they make the doc set harder for a fresh reader to navigate — each instance requires the reader to either flip to another doc or hold two numbering schemes in mind. The reader test found these because the agents were explicitly instructed to flag "the document does not say" moments.

**Next step.** Park. Address opportunistically when the relevant sections are edited for other reasons. Not worth a dedicated batch.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `Dev/Resources/tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 184 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.

---

## Ideas

Raw ideas captured during sessions. Date + one-liner. Promoted to OQs or batches during planning sessions.

---

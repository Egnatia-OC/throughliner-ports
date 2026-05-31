# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

## Shipped history

128 batches shipped or cancelled (V18–0144). Full history in `Dev/Planning/build-log/INDEX.md`. Per-batch details in individual build-log files.

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

### 0130 — /sovsetup case 1 retest (post-fix verification)

**Unparked.** v142. Test plan rewritten v145 — reconciliation (0136–0139), /sovexplain (0140), plugin OQ fixes (0141–0142) all accounted for. Repackage plugin at HEAD before E2E run.

**Goal.** Verify that v113, v115, v117, and v129 changes work end-to-end in a real `/sovsetup` case 1 run. v113/v115 fixed hook path resolution (7 cowboy-test issues from plugin v90). v117 added setup Q5 (language setting) and BOM hardening. v129 renamed BUILD-PLAN → BACKLOG across the plugin. None verified E2E.

**Inputs.** Fresh empty folder. Plugin repackaged at current HEAD.

**Outputs.** Test-log entry. New BACKLOG entries for any issues found.

**Test protocol.** This is a guided walkthrough — deliver one step at a time, wait for the user's result before issuing the next. Open by stating the total step count. Do not preview upcoming steps, list remaining steps, or bundle steps together. If a step produces a finding, handle it (file to BACKLOG or flag) before moving to the next step. This rule applies even if the step seems trivial.

**Test plan.**

1. Invoke `/sovsetup` on empty folder. Confirm `detect-case` returns case 1.
2. Walk through all five questions with test content. Verify Q5 (language setting) appears. Answer Q1–Q4 in a non-English language to test Q5 default detection.
3. After scaffold: verify full output structure — `_method/` with `UX.md`, `MANIFEST.md`, `BACKLOG/`, `build-log/`, `test-log/`, `planning/drafts/`, `research/`, `research/search-queries/`, `proxies/` (5 proxy files: ux, manifest, research, backlog, build-log). `CLAUDE.md` at root. All directory names use BACKLOG (not BUILD-PLAN). BACKLOG proxy includes `## Test sessions` section. No separate test-log proxy.
4. After Q answers applied: verify doc population. Q1 → CLAUDE.md `## Product overview` (4 fields) + UX.md `## Project context`. Q2 → UX.md `## UX principles`. Q3 → UX.md `## Functionalities` with `###` entries. Q4 → batch file in `_method/BACKLOG/` with scope content. Q5 → CLAUDE.md `## Language` field + `git config --local core.quotepath false` (if `.git/` exists).
5. Hook path validation (planning phase): Edit `_method/BACKLOG/<batch>.md` → allowed. Edit `_method/proxies/ux.md` → allowed. Edit `_method/planning/drafts/<file>.md` → allowed. Edit `_method/research/<file>.md` → allowed.
6. Bash heredoc test: write a heredoc containing markdown headings → verify no false-positive filename extraction from the write-guard.
7. BOM hardening: verify scaffolded files don't contain BOM bytes that break `safe_read_text()`.
8. Verify recap message and handoff. Handoff should direct to `/sovplan` or `/sovrecap` + `/sovbuild` depending on Q4 scope completeness.

**Success criteria.** Clean case 1 setup with no hook blocks on method-file writes. Full scaffold structure correct. All five Q answers persist in the right docs. Language default detection works. BACKLOG naming throughout. Handoff message matches Q4 scope state.

**Risks / dependencies.** Requires repackaging plugin at HEAD. If scaffold.py still outputs `BUILD-PLAN/` paths (missed in v129 rename), the test surfaces it immediately at step 3.

---

### 0131 — Build lifecycle retest (post v115–v129 changes)

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

---

### 0145 — /sovexplain routing + MANIFEST capabilities summary

**Goal.** Expand /sovexplain from "why"-only into a three-way router (what / how / why). Generate a capabilities summary section in MANIFEST at close time; the MANIFEST proxy reproduces it so Claude reads it at session start for orientation without loading full MANIFEST. Resolves the orientation gap OQ (plugin-side).

**Scope.**

1. `plugin/templates/MANIFEST-TEMPLATE.md` — Add `## Capabilities summary` section at the top (before entries). Starts with a placeholder comment; populated at first `/sovclose`.
2. `plugin/templates/.proxies/manifest.md` — Add `## Capabilities summary` section. Reproduces the summary verbatim (it's short). This is what Claude reads for orientation.
3. `plugin/docs/procedures/close.md` — Post-build path: add step 1b after MANIFEST entry updates. Generate/update the capabilities summary from the current MANIFEST entries — one plain-English paragraph summarizing what the project has built. Write to the `## Capabilities summary` section. Proxy regeneration (step 15) propagates it.
4. `plugin/skills/sovexplain/SKILL.md` — Rewrite to add routing before lookup. Classify the question: **"What"** (capability identification) → read MANIFEST proxy's capabilities summary. **"How"** (usage) → identify the matching skill or procedure doc, read its SKILL.md. **"Why"** (design rationale) → existing explain-reference flow (unchanged).
5. `plugin/docs/explain-proxy.md` — No change. Stays "why"-only. Routing happens in SKILL.md before the proxy is reached.
6. Consumer-facing docs — Update /sovexplain description in Reference manual, crash course, INVENTORY.md to mention the three question types.

**What it doesn't do.** No new index file for "how" routing — skills and procedures have predictable locations. No explain-reference entries for the routing itself.

**Dependency.** None. 0144 is independent — these can ship in either order.

**Success criteria.** "What does my project do?" answered from MANIFEST proxy without full MANIFEST read. "How do I close a build?" routes to close procedure. "Why" still works as before. Capabilities summary regenerates at each close.

---

### 0146 — First graduation: dogfood SI onto itself

**Goal.** Make the sovereign-implementer repo a real SI-managed project. The host SI (current shipped version) manages this project's planning artifacts, session lifecycle, and builds. No `/sovsetup` — manual migration, since the project predates the plugin and running setup on the plugin's own repo would be circular.

**Vocabulary.** "Host SI" = the installed plugin doing the work. "Target SI" = the source code at `plugin/` being built. They are never both active in the same session. Building happens under the host SI; E2E testing happens in a separate session with only the target SI installed. "Graduation" = the target SI passes E2E, gets repackaged and installed as the new host SI.

**Scope.**

1. **Fix plugin name.** `plugin/.claude-plugin/plugin.json`: rename `"name": "no-code-method"` → `"name": "sovereign-implementer"`.

2. **CLAUDE.md collision.** The dev CLAUDE.md and the plugin-scaffolded CLAUDE.md both want repo root. Resolve — likely merge dev-side instructions into the scaffolded format, retiring the standalone dev CLAUDE.md.

3. **Migrate planning artifacts into `_method/`.** Move `Dev/Planning/` contents into the plugin's expected structure:
   - `BACKLOG.md` → per-batch files under `_method/BACKLOG/`.
   - `build-log/` → `_method/build-log/`.
   - `test-log/` → `_method/test-log/`.
   - `.proxies/` → `_method/proxies/` (regenerate against new paths).

4. **Migrate drafts and research.** `Dev/drafts/` → `_method/planning/drafts/`. `Dev/Resources/research/` → `_method/research/`.

5. **Retire dev-side prose rules.** `session-protocol.md`, `session-reference.md`, `INVENTORY.md` — reconcile any content not yet in plugin procedure docs, then retire. These are replaced by the host SI's mechanical enforcement.

6. **Remove `.no-code-method-skip`.** The skip marker tells the SI "don't manage this project." Dogfooding means the opposite — the host SI *should* manage it.

7. **Archive historical artifacts.** `Dev/Resources/Iteration playbook/` — pre-plugin procedures, read-only archive. Leave in place but not under `_method/`.

8. **No migration needed.** `Dev/Resources/scripts/`, `Dev/Resources/tests/`, `Dev/Resources/Marketing/`, `Guides/`, `LICENSE`, `README.md`, `.gitignore`, `.gitattributes` — regular project files, not SI-managed.

9. **Dev-side session opener.** Add host/target disambiguation to the session open flow — "You are building target SI from within host SI" with path references. Exact mechanism TBD (CLAUDE.md section, or host SI session-start hook recognising its own repo).

10. **Graduation procedure.** Document the version-graduation flow: target SI passes E2E → repackage `plugin/` → install as new host → bump host version reference in session opener. Lightweight — not a full procedure doc, just a checklist in CLAUDE.md or a dev-side reference.

**What it doesn't do.** No plugin code changes beyond the name fix. No new hooks or skills for self-awareness. No changes to how the plugin manages user projects generally.

**Risks.** BACKLOG migration is the largest mechanical task (~20 queued/shipped batches to split into individual files). CLAUDE.md merge requires careful content reconciliation — the dev CLAUDE.md has accumulated 100+ sessions of context. Convergence gaps between dev-side prose rules and plugin procedure docs may surface during step 5.

---

### 0147 — Merge Ideas into Open Questions + combine ideation/deliberation

**Goal.** Eliminate the Ideas → OQ promotion step. One BACKLOG section holds all unscoped captures — from raw one-liners to fleshed-out questions. One skill and procedure replaces `/sovideate` and `/sovdeliberate`.

**Scope.**

**Plugin-side — structure:**

1. `BACKLOG-TEMPLATE.md` — remove `## Ideas`. Update `## Open questions` to welcome light captures (heading + Surfaced + one sentence) alongside full entries. BACKLOG becomes 5 sections.
2. `DOC-STRUCTURE.md` — update BACKLOG spec: remove Ideas, loosen OQ entry format (Why-it-matters and Next-step become optional, not mandatory). Update proxy description to 5 sections.
3. `templates/.proxies/backlog.md` — update to 5 sections.

**Plugin-side — procedures and skills:**

4. Merge `procedures/ideate.md` and `procedures/deliberate.md` into one procedure doc. Combined flow: present existing OQs, explore user's new topic, route everything. Light captures get quick routing; fleshed-out entries get full deliberation. Delete the retired doc.
5. Keep one skill, delete the other. Update SKILL.md description to cover both activities.
6. `procedures/close.md` — update "planning, ideation, or general sessions" wording. Idea sweep routing already goes to "batch or OQ" — no functional change.

**Plugin-side — reference docs:**

7. `universal-behaviour.md` — update routing table entries referencing ideation/deliberation as separate activities.
8. `VOCABULARY.md` — retire "Ideas section" as distinct concept. Merge ideation/deliberation definitions.
9. `explain-reference.md` — check and update entries referencing Ideas vs OQs.

**Dev-side:**

10. `BACKLOG.md` — remove `## Ideas` section (currently empty).
11. `session-protocol.md` — routing table: merge Ideation row into a combined type covering both capture and resolution. Update idea-sweep and close references.
12. `session-reference.md` — update OQ entry shape if it references Ideas promotion.
13. `Dev/Planning/.proxies/backlog.md` — update.

**Consumer-facing docs:**

14. `Reference manual.md` — update skill descriptions, BACKLOG section list.
15. `crash-course/` — update relevant HTML sections (check `data-source` attributes).
16. `INVENTORY.md` — update component listings.

**Decisions to make this batch.**

- **Combined skill name.** `/sovideate` (more inviting for mid-build "I just had a thought"), `/sovdeliberate` (broader — "careful consideration" covers both capture and resolution), or something new?

**What it doesn't do.** No changes to other BACKLOG sections. No hook changes. No `/sovplan` changes. No migration tool for consumer projects with existing Ideas sections — the combined skill handles legacy format gracefully.

**Success criteria.** BACKLOG has 5 sections. One skill handles both "I just had a thought" and "let's work through the backlog." No references to Ideas as a separate concept remain in plugin or dev docs. Consumer projects with legacy Ideas sections don't break.

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

---

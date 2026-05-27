# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Queued batches live inline in the *Queued batches* section below the shipped-batch table. Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

## The batch list

| # | Batch | Output |
|---|---|---|
| V18 | Plugin scaffold + SessionStart hook | Path block in fenced JSON; plugin skeleton; SessionStart installed. **Shipped v18.** |
| V19 | PreToolUse lock + templates + `/init-project` + Fold-ins | Lock enforcement; templates scaffolded by skill-command; fold-ins section. **Shipped v19.** |
| V20 | Reference manual promotion; parity audit | Reference manual current; parity rule extended. **Shipped v20.** |
| V21 | SessionStart — foundational reads + routing | State summary, template detection, resume detection, routing. **Shipped v21.** |
| V22 | Planning subagent + Serves-line hook | Planning loop end-to-end; tested. **Shipped v22.** |
| V23 | Remove Cowork mentions | Claude Code becomes explicit required tool. **Shipped v23.** |
| V24 | BUILD-METHOD + TEST-LOG creation | Dev-internal working manual and test record. **Shipped v24.** |
| V25 | Before-build + batch-executor + Stop hook | Build orchestration core; batch-sizing principle. **Shipped v25.** |
| V26 | TEST-LOG mechanism + V25 bugfixes + Drafts convention | 8-column TEST-LOG spec, V25 bugfixes, drafts-in-flight. **Shipped v26.** |
| V27 | After-build subagent | MANIFEST auto-update, recap, test-confirmation gate. **Shipped v27.** |
| V28 | V27 fix sweep | TEST-LOG writable, Stop-hook TEST-LOG-aware, shared helpers extracted. **Shipped v28.** |
| V29 | Safety net + unified `/adopt` | Unadopted-folder detection + PreToolUse enforcement; five-case `/adopt`. **Shipped v29.** |
| V30 | DOC-STRUCTURE migration + Reference manual coherence | Schema content into plugin; Reference manual rewrite. **Shipped v30.** |
| V31 | Planning — rescope OPEN-QUESTIONS | Four entries promoted to sessions. **Shipped v31.** |
| V32 | NO-CODE-METHOD.md retirement | Original method files retired or pointed at plugin. **Shipped v32.** |
| V33 | Consumer audit trail + frame-correction sweep | Consumer BUILD-LOG, planning/drafts/, frame-correction sweep. **Shipped v33.** |
| V34 | Consumer git workflow | Tag-and-push habit + git safety-guard hook. **Shipped v34.** |
| V35 | E2E Taskflow test | First real-project plugin run; validated adopt cases 1+4. **Shipped v35.** |
| V36 | Doc-only: TEST-LOG ordering, planning authority, plan-panel research | Three bundled doc fixes. **Shipped v36.** |
| V37 | Marketplace.json + local install | Marketplace packaging; first non-`--plugin-dir` smoke test. **Shipped v37.** |
| V38 | Locked-doc edit rules + Sonnet-search | Footer-stamp carve-out, proposed-edit mechanism, Sonnet-search discipline. **Shipped v38.** |
| V39 | MANIFEST paths + read-before-edit gate | Paths field + Shape B PreToolUse enforcement. **Shipped v39.** |
| V40 | Shelve the two-write rule | Repo-root docs frozen at V39; plugin side becomes sole source. **Shipped v40.** |
| v41 | Planning — rescope OPEN-QUESTIONS | Three entries scoped into V45/V46/V47. **Shipped v41.** |
| v42 | Git-diff drift detection | New drift check 1: direct-edit detection via git-diff + per-file confirmation. **Shipped v42.** |
| V43 | Permission-mode UX harmonization | Mode-aware deny messages, two-layer preamble, Reference manual section. **Shipped v43.** |
| V44 | /setup UX + per-project opt-out | Marker architecture removed; `/adopt` → `/setup`; 3 UX friction items resolved. **Shipped v44.** |
| V45 | Distributed fold-ins + BACKLOG open-questions + Inputs line | Fold-ins in destination docs; open-questions section; Inputs line; fold-in carve-out. **Shipped v47.** |
| V46 | BACKLOG.md PostToolUse validation | PostToolUse parse validation after BACKLOG edits. **Shipped v48.** |
| V47 | Vocabulary sweep / non-GUI generalisation | "Observable behaviours" generalisation; planning/plan-mode disambiguation. **Shipped v49.** |
| V48 | Test split + non-UI test types | Four test types, Claude/User verifier, 10-column TEST-LOG, after-build commit/tag. **Shipped v50.** |
| V49 | Consumer-batch structure overhaul | Five scope-context sections + Changes: delimiter + red-flag marker. **Shipped v51.** |
| V50 | ADR-style numbering + per-batch file-split | NNNN-kebab-title format; BACKLOG/ folder; allocate_number.py. **Shipped v52.** |
| V51 | Research folder + Sonnet-search reword | `/setup` scaffolds research/; agent researches directly. **Shipped v53.** |
| V52 | BUILD-LOG restructuring | build-log/ folder with per-build files + INDEX.md. **Shipped v54.** |
| V53 | Automated test suite | pytest suite at tests/; 124 tests. Dev-internal, no footer bump. **Shipped v55.** |
| V54 | Validation + warnings bundle | Serves-DOC validation, red-flags warning, aging detection, PROPOSED EDIT rename. **Shipped v56.** |
| V55 | New hook events (compaction guard + opener routing) | PreCompact blocks mid-build compaction; UserPromptSubmit classifies opener. **Shipped v57.** |
| V56 | TEST-LOG row pruning | Planning subagent deletes orphaned-component rows before drift checks. **Shipped v58.** |
| V57 | Subagent rule-loading convergence | Batch-executor converged on read-spec-on-entry pattern. **Shipped v59.** |
| V58 | Session performance tracking | Structured Performance section in build-log entries. **Shipped v60.** |
| 0060 | Taskflow E2E prep and testing | First real E2E since V35; partial — remaining coverage deferred to 0068. **Parked.** |
| 0063 | Subagent efficiency pass | Classify before loading; doc-first ordering; no inner agents. **Shipped v62.** |
| 0064 | /setup case 4 completion | BUILD-LOG folder migration + batch stub quality. **Shipped v63.** |
| 0065 | Project-boundary PreToolUse hook | Block Edit/Write/MultiEdit outside project root. **Shipped v64.** |
| 0066 | Permission prompt surface audit | Glob-based allocation replaces Bash calls; Auto mode recommended. **Shipped v66.** |
| 0067 | Desktop app install/update docs | Desktop-app procedures in Reference manual. **Shipped v67.** |
| 0068 | Taskflow E2E round 2 | Full build cycle against Taskflow with 0063–0067 fixes. Skills migration. **Shipped v71.** |
| 0069 | BACKLOG batch status tracking | Status: line (active/queued/parked/shipped) + parser + subagent transitions. **Shipped v70.** |
| 0061 | Rename "Crash course" to "Reference manual" | Rename + update all references. Frees name for HTML guide. **Shipped v68.** |
| 0062 | HTML Crash Course guide | Multi-page HTML guide for testers/early adopters. Depends on 0061. **Shipped v69.** |
| 0070 | After-build close completeness | Doc-parity audit, idea sweep with routing, pre-commit checkpoint, CLAUDE.md extensibility section. **Shipped v72.** |
| 0071 | Subagent cost optimization | Planning subagent from ~31.6k to <15k tokens: conditional drift-check skip, classify-then-dispatch, Sonnet evaluation. **Shipped v73.** |
| 0072 | After-build source-code boundary | Hard boundary: after-build cannot edit source/build files. Fold in "run commands yourself" rule. **Shipped v74.** |
| 0073 | ~~Stop hook before-build→build chain fix~~ | **Cancelled.** Superseded by architecture redesign — auto-chaining removed entirely. |
| 0074 | Session-open status summary | User-facing batch counts, next batch, pending tests — mandatory presentation via hook directive. **Shipped v75.** |
| 0075 | Dev-side log folder migration | BUILD-LOG.md + TEST-LOG.md → build-log/ + test-log/ folder structures. Dev-side only, no plugin changes. **Shipped v76.** |
| 0076 | ~~Plugin-side TEST-LOG folder migration~~ | **Cancelled.** Superseded by 0090. Original scoped against subagent architecture. |
| 0077 | ~~Greenfield E2E: burner app from scratch~~ | **Cancelled.** Intent kept — rewrite as new scope after architecture redesign lands. |
| 0078 | ~~Post-fix E2E validation (Taskflow)~~ | **Cancelled.** Validates 0073/0074 in old architecture; 0072 already shipped. Nothing left to validate. |
| 0079 | Subagent removal: code and procedures | Remove all 5 subagents. Convert to procedure docs. Delete Stop hook. Rewrite session_start/PreToolUse/skills to route to docs instead of spawning agents. **Shipped v77.** |
| 0080 | Doc permission flip: phase-aware editing | Unlock source-of-truth docs (UX, MANIFEST, additional) during planning. Lock source code during planning. Reverse during build. Phase detected via BACKLOG batch status. Depends on 0079. **Shipped v78.** |
| 0084 | Greenfield E2E: post-redesign full cycle | Planning-phase E2E of procedure-doc architecture. /setup works when invoked; Claude ignores routing hint for uninformed users; build transition opaque. **Shipped v79.** |
| 0081 | Proxy format and companion proxies | Proxy format spec + companion proxies for UX, MANIFEST, TEST-LOG, research. Session A of three-way split (0081/0089/0090). Depends on 0079, 0080. **Shipped v81.** |
| 0082 | CLAUDE template product overview | Product overview section in CLAUDE.md: what it is, who it's for, what friction it solves, milestones. Populated by `/setup` conversation. Depends on 0079, 0080. **Shipped v82.** |
| 0083 | Gemini search MCP server | `/research` skill + query-file template + proactive-search rule. Reuses existing MCP server; plugin provides discipline wrapper. **Shipped v83.** |
| 0085 | First-time user experience | /setup enforcement in PreToolUse deny + build-transition UX in before-build procedure + parent-directory CLAUDE.md inheritance advisory. Depends on 0084. **Shipped v84.** |
| 0086 | Scaffold quality fixes | [Project Name] replacement, UX principle capture, Status: line, marketplace.json description. **Shipped v85.** |
| 0087 | Doc folder restructure | Move spine docs into dedicated subfolder. Large surface area. Depends on 0085, 0086. **Shipped v86.** |
| 0089 | INDEX relocation to proxies | Move BACKLOG INDEX.md and build-log INDEX.md content into `_method/proxies/`. Folders keep only per-entry files. Depends on 0081. **Shipped v88.** |
| 0090 | TEST-LOG folder split + proxy index | Split TEST-LOG.md into test-log/ folder; `_method/proxies/test-log.md` becomes folder index. Supersedes 0076. Depends on 0081, 0089. **Shipped v89.** |
| 0091 | Dev-side terminology and BACKLOG alignment | Rename PLAN.md→BACKLOG.md, planning/sessions/→planning/scopes/, merge OPEN-QUESTIONS into BACKLOG. Dev-internal only. **Shipped v87.** |
| 0092 | BUILD-METHOD split and dev-side proxies | Split BUILD-METHOD into protocol + reference; adopt .proxies/. Depends on 0091. **Shipped v90.** |
| 0093 | Dev-side folder restructure | All dev-side content into `Dev/`, product docs into `Guides/`. Manual execution with different design choices from spec. **Shipped v96.** |
| 0111 | Dev-side session-protocol procedural convergence | Opener routing table, carried-forward read-back, explicit pre-commit checklist, idea-sweep 3-way triage, differentiated close paths, batch-ordering audit. Resolves 3 OQs. **Shipped v104.** |

| 0102 | Dev-side session-close convergence | Proxy regen close step + response-shape tags on session-protocol.md close steps. Dev-internal only. |
| 0101 | Structured-markdown validator | PostToolUse validation for TEST-LOG, build-log, scope-context, proxies. Warn on malformed shapes. **Shipped v101.** |
| 0100 | Bash write-guard + skill escape guidance | Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies. **Shipped v102.** |
| 0099 | /sovrecap + /sovbuild rename + lock-timing fix | Rename before-build→sovrecap, build→sovbuild; Status: active delayed to post-confirmation. **Shipped v95.** |
| 0096 | Manifest rationale field | Inline italic rationale suffix on MANIFEST entries; close procedure writes it; planning checks it before UX edits. **Shipped v97.** |
| 0098 | /sovplan skill + ordering principles + [SECURITY] marker | Planning skill wrapping planning.md; ordering principles; SessionStart top-3 summary; universal `[SECURITY]` marker. **Shipped v96.** |
| 0097 | /sovclose + /sovgit + after-build retirement | Close skill (dual-path), git skill, after-build.md absorbed. **Shipped v94.** |
| 0103 | /tersify skill for doc compression | Guided triage + audit for reducing token cost in SOT docs. Planning-phase only. **Shipped v98.** |
| 0102 | Dev-side session-close convergence | Proxy regen close step + response-shape tags on session-protocol.md close steps. Dev-internal only. **Shipped v99.** |
| 0094 | Guided testing and debugging procedure | `/test` skill + `testing.md` procedure doc. User-verified walkthrough, direct TEST-LOG recording, structured debugging. **Shipped v100.** |
| 0104 | Sov-prefix rename for remaining skills | `/setup` → `/sovsetup`, `/research` → `/sovresearch`, `/test` → `/sovtest`, `/tersify` → `/sovtersify`. All references updated across ~30 files. **Shipped v105.** |
| 0105 | `_method/` orientation in CLAUDE.md template | `## What's inside _method/` section added to CLAUDE-TEMPLATE.md. **Shipped v106.** |
| 0106 | ~~Post-build proxy regeneration in `/sovclose`~~ | **Cancelled.** Already implemented by close.md step 11. |
| 0107 | Unclosed-build detection in SessionStart | Active batch + all files ticked + `/sovclose` never ran → flag on session open. **Shipped v107.** |
| 0108 | Guided rollback procedure (`/sovrevert`) | New skill + procedure doc. Non-coder walkthrough for undoing failed builds. **Shipped v108.** |
| 0109 | `/sovsetup` case 4 scaffold drift detection | Pytest registry + 4 missing case 4 migrations fixed. **Shipped v109.** |

Shipped/cancelled batches end here. Queued batches are below with full scope content — no separate scope files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0088 — Build E2E test

**Goal.** Test the build phase of the procedure-doc architecture. Picks up where 0084 left off — `/sovsetup` and planning are validated, now test `/sovrecap` through `/sovbuild` through `/sovclose` in the Polite Fart Announcer burner app.

**Inputs.** `Dev/Resources/research/e2e-greenfield-post-redesign.md` ("What wasn't tested" section — note: written at v78, skill names `/build` etc. are pre-rename). Burner app at `C:\Users\Alex\Desktop\Polite Fart Announcer`.

**Pre-requisite.** The burner app was scaffolded at plugin v0.67.0 (root-level docs, flat TEST-LOG.md, no `_method/`, no proxies). 19 batches have shipped since. Delete the existing scaffolding and run `/sovsetup` fresh before testing. This also resolves the stale `Status: active` on the old batch.

**Outputs.** Updated research file with build-phase findings. New BACKLOG entries or open questions for any issues. Token cost baseline for procedure-doc architecture.

**Success criteria.** `/sovrecap` populates correctly (Files: and Tests: populated). `/sovbuild` sets Status: active and creates `index.html` — file exists and works in browser. `/sovclose` fires: MANIFEST updated, build-log entry written, test-log session file written. Phase-aware permissions work. Observations documented.

**Risks / dependencies.** Burner app needs fresh `/sovsetup` (see pre-requisite). Risk: `/sovsetup` case 1 itself may surface issues — document those too.

---

### 0095 — /sovtest skill E2E validation

**Goal.** End-to-end test of `/sovtest` skill (shipped in 0094) against a real project. Validate the full flow: invoke after build, follow guided walkthrough, report failure, get debugging support.

**Inputs.** `/sovtest` skill and `plugin/docs/procedures/testing.md` (from 0094). A burner app with pending TEST-LOG rows across multiple test types. `Dev/Resources/research/e2e-greenfield-post-redesign.md`.

**Outputs.** Research file `Dev/Resources/research/e2e-test-skill-validation.md`. New BACKLOG entries for issues. `/sovclose` handoff validation.

**Test plan.** Happy path: invoke `/sovtest`, walk through Look-and-click and Run-and-read tests, report Pass, verify row updates. Failure path: report Fail, verify debugging protocol, verify routing to BACKLOG. Edge cases: no pending tests (graceful exit), mid-build invocation (rejected), partial progress on early stop. Handoff: confirm planning read-back handles rows `/sovtest` already confirmed.

**Success criteria.** Non-coder completes full flow without independent knowledge. Debugging produces useful output on deliberate failure. TEST-LOG state after `/sovtest` is consistent with planning expectations. No silent failures.

**Risks / dependencies.** Hard dep on 0094 (shipped v100). Soft dep on 0088 (reuse app state — note: 0088 now starts fresh, so test-type variety depends entirely on what that build produces). Risk: insufficient test-type variety in burner app.

---

### 0110 — Queued-pipeline staleness sweep at close

**Goal.** Add a close-time step that scans all queued BACKLOG batches and open questions for staleness: references to files, skills, or docs that have been renamed or deleted; dependencies on cancelled or redesigned batches; OQs whose parking rationale references conditions that have since been met; contradictions with what just shipped.

**Lost-feature sweep fold-in.** Expand scope beyond close-time queued-batch checks to also cover: cancelled batches whose intent was never re-scoped, parked batches whose parking rationale references conditions that have since been met, and build-log "carried forward" items that were never picked up. The pattern (from v82 manual sweep): cancellation and parking are one-way — nothing triggers re-evaluation when the reason for parking stops being true. This sweep catches items that silently fell off the map. Could live as a standalone `/sweep` skill invokable during `/sovplan` or `/sovdeliberate`, or as an expanded step in `/sovclose`. (From OQ "Lost-feature sweep as a planning skill," surfaced v82.)

**Inputs.** v93 build-log (manual sweep that found four stale batches). v82 build-log (manual sweep that found six lost items across ~65 batches). Current BACKLOG structure.

**Outputs.** New step in `/sovclose` (or `/sovplan`), or a standalone `/sweep` skill. Definition of what counts as "stale" — dead file paths, old skill names, references to cancelled batches, OQ surfaced dates beyond a threshold, carried-forward items with no destination, parked items whose conditions have been met.

**Success criteria.** After a build that renames a skill or moves a file, the sweep flags any queued batch or OQ still referencing the old name. OQs parked longer than a configurable threshold flagged for re-evaluation. Cancelled batches whose intent wasn't re-scoped are surfaced. Carried-forward items with no pickup are surfaced. Sweep is grep-level fast, not deep semantic analysis.

**Concurrent-build detection fold-in.** Extend 0107's unclosed-build detection. Currently SessionStart only warns when `Status: active` AND all files ticked (build finished, `/sovclose` skipped). It does not warn when `Status: active` with files still unticked — meaning a build is mid-progress in another session. Fix: SessionStart warns on any `Status: active`, period. All-ticked → "run `/sovclose`" (existing behaviour). Some-unticked → "a build of batch X is in progress — are you resuming this build, or working in parallel?" Parallel builds corrupt file state and git history; the warning should be prominent. Ideation in parallel is safe (writes only to the Ideas section); deliberation and planning carry git risks discussed in [[0112]].

**Risks / dependencies.** Scope risk: "scan everything" could burn context. Needs tight scoping to pattern-match checks on names and paths, not full-doc comprehension. Should run on queued/parked entries only. The lost-feature component reads more broadly (cancelled batches, build-log) but still pattern-matches rather than comprehending.

---

### 0112 — Skill split: `/sovdeliberate`, `/sovideate`, and `/sovplan` narrowing

**Goal.** Split non-build work into three named skills with distinct procedure docs, so users discover each mode through invocation rather than experience. `/sovplan` already exists — narrow it. `/sovdeliberate` and `/sovideate` are new.

**The three modes.**

`/sovplan` — **Structural planning.** The user wants to change the shape of the roadmap itself. Reorder batches, split or merge them, rescope batch content, revise dependency chains, add or remove batches. Input: the queued-batches section of BACKLOG. Output: a restructured queue. Includes cross-checking other queued batches — dependency validation, stale-reference scanning, ordering audit — as part of the procedure, not as an afterthought. The existing `planning.md` procedure doc does this today but also covers OQ work and idea generation — this batch narrows it to structural-only.

`/sovdeliberate` — **OQ deliberation.** The user wants to work through accumulated open questions. For each OQ: weigh implications, decide disposition (promote to batch, drop with reason logged in build-log, or re-park with updated rationale). Input: the open-questions section of BACKLOG. Output: OQs moved — promoted to new or existing batches, dropped, or re-parked with fresher reasoning. This mode forces the periodic reckoning that BACKLOG consolidation (0091) made optional.

`/sovideate` — **New idea generation.** The user arrives with a fresh concept not yet represented in BACKLOG. Explore the idea, assess fit, and route it: most become new OQs, some slot into existing queued batches, occasionally one becomes a fully scoped new batch. Input: the user's head. Output: new BACKLOG entries (OQs or batches). This mode is exploratory — no existing artifact is being worked through, so the procedure is lighter. Claude may also offer to suggest a new idea based on gaps, patterns, or unaddressed areas it notices in the current BACKLOG and project state.

**Inputs.** Current `plugin/skills/sovplan.ts` and `plugin/docs/procedures/planning.md`. `user_prompt_submit.py` opener routing logic. SessionStart status summary code.

**Ideas section in BACKLOG.** New section below Open Questions for raw, unprocessed ideas. Lighter than OQs — no required fields, just a one-liner and a date. The user can tell Claude an idea at any point in any session type, and Claude writes it here regardless of build phase. `/sovideate` promotes ideas to OQs or batches when the user is ready to flesh them out. `/sovdeliberate` can also draw from this pool. Hook carve-out needed: writing to the Ideas section must be allowed even during active builds (unlike OQ or batch edits). This prevents ideas from being lost to napkins and notepads.

**Build-snapshot architecture.** When `/sovbuild` is invoked, it extracts the active batch's scope from BACKLOG.md into a working snapshot (`_method/active-build.md`), removes the batch from BACKLOG.md entirely, and tells the user: "I've snapshotted batch NNNN — I'm working from the snapshot now." The build reads only from the snapshot for its duration. BACKLOG.md is fully unlocked immediately — parallel sessions can run `/sovplan`, `/sovdeliberate`, or `/sovideate` against it freely. At `/sovclose`, the batch is written back to BACKLOG.md as shipped and the snapshot is deleted. The snapshot file's existence replaces `Status: active` as the build-in-progress signal: SessionStart checks for `_method/active-build.md` — if it exists, a build is running. No duplicate, no conflict, no possibility of editing a batch mid-build because it only exists in the snapshot. This obsoletes the Ideas-section hook carve-out (BACKLOG.md is unlocked) and simplifies phase detection (file existence vs status parsing).

**Outputs.** Two new skills (`/sovdeliberate`, `/sovideate`) with procedure docs (`deliberate.md`, `ideate.md`). Narrowed `planning.md`. Updated opener routing in `user_prompt_submit.py` to classify the three modes. SessionStart and status summary updated if they reference planning generically. New Ideas section in BACKLOG template and consumer BACKLOG. Build-snapshot mechanism in `/sovbuild` and `/sovclose`.

**Success criteria.** Each skill invocation loads only its procedure doc. Opener routing correctly classifies "let's work through the open questions" vs "I have a new idea" vs "reorder the batches." `/sovplan` no longer covers OQ work or idea generation. All three procedure docs are self-contained — no cross-loading required. `/sovbuild` extracts batch to snapshot and removes from BACKLOG; parallel sessions can edit BACKLOG freely; `/sovclose` writes batch back as shipped.

**OQ accumulation nudge.** Fold-in from the OQ of the same name (surfaced v109). When open questions accumulate past a threshold (count, age, or both), SessionStart or `/sovrecap` nudges the user toward `/sovdeliberate` — "you have N open questions older than X — consider running `/sovdeliberate` before your next build." Design questions: what threshold triggers the nudge, whether it's informational or blocking, and whether it lives in SessionStart, `/sovrecap`, or both. The existing aging detection (0054) and session-open status summary (0074) already flag counts — this adds a concrete destination.

**Git steps inline in each procedure doc.** Each planning mode's procedure doc ends with a commit step — Claude commits with a mode-prefixed message (`plan: <summary>`, `deliberate: <summary>`, `ideate: <summary>`) after user confirmation. No tag, no push. `/sovclose` keeps its existing commit + tag + push. This makes git handling mechanical per-mode, not a prose nudge to invoke a separate skill. `/sovgit` remains available for ad-hoc use outside procedures but is no longer the standard path.

**BACKLOG rename to BUILD-PLAN.** Rename `BACKLOG.md` to `BUILD-PLAN.md` across plugin templates, consumer scaffolding, hooks, procedure docs, and all references. Motivation: "backlog" contains "log" as a substring, causing persistent confusion with "build log." "Build plan" is forward-looking (what will be built) vs "build log" (what was built) — same prefix, distinct suffixes. The rename also aligns the three planning artifacts with their skills: `/sovplan` → build plan (queued batches), `/sovdeliberate` → open questions, `/sovideate` → ideas. When the file splits into three (build-snapshot architecture above), each file gets a name that mirrors its skill.

**Risks / dependencies.** Surface area: touches skills, procedure docs, opener routing, SessionStart, and the build/close flow. Recommend shipping as one batch since the routing table is incomplete if only some skills exist. Risk: procedure doc content needs careful drafting — too prescriptive kills the exploratory nature of ideation; too loose and the skill adds no value over a bare conversation. Build-snapshot mechanism changes how phase detection works — all existing `Status: active` checks need auditing. The BACKLOG→BUILD-PLAN rename has wide surface area (hooks, templates, procedure docs, tests, proxies, references) but is mechanically straightforward — grep-and-replace.

---

### 0113 — Session-length safeguards

**Goal.** Prevent builds from silently consuming the entire context window, and give users a recovery path when a session grows long. Two complementary mechanisms: pre-build sizing and mid-session compact nudge.

**Pre-build sizing.** During `/sovrecap` or early in `/sovbuild`, Claude estimates whether the batch fits in one session based on proxy signals — file-touch count, number of procedure-doc steps, whether the batch scope flags deliberation-heavy design questions. If the estimate exceeds a threshold, Claude surfaces it: "this batch touches N files and has open design questions — consider splitting before starting." The heuristic is calibrated on conversation shape, not token count (Claude has no visibility into its own context usage).

**Mid-session compact nudge.** When a build session grows long — high exchange count, extended deliberation mid-build, many files already edited — Claude nudges the user to `/compact` before context runs out unexpectedly. Proxy signals: exchange count since `/sovbuild` invocation, number of files edited, number of remaining procedure-doc steps. The nudge is informational, not blocking: "this session has grown long — consider `/compact` to preserve context for the close steps."

**Inputs.** Dev-side observation: ~20% of sessions blow out. Failure pattern correlates with high file-touch count and extended explanation/decision exchanges. Claude cannot see token count or context fullness — all heuristics must use conversation-visible signals.

**Outputs.** Sizing check in `/sovrecap` or `/sovbuild` procedure doc. Compact-nudge logic (likely in universal-behaviour.md or a procedure doc). Calibration guidance for thresholds. Fold-in: standardise the end-of-session prompt in `git.md` to recommend `/compact` when continuing in the same area, `/clear` for a fresh start (from OQ "/sovgit close prompt," surfaced v97).

**Success criteria.** A batch with 8+ file touches and design questions triggers a pre-build warning. A session with 15+ exchanges past `/sovbuild` without reaching `/sovclose` triggers a compact nudge. Neither mechanism blocks — both are advisory.

**Risks / dependencies.** Thresholds are guesses until calibrated against real sessions. The parking rationale from the original OQ still partially applies: the 20% blowout rate is dev-side, and plugin-guided builds may behave differently. Recommend shipping after E2E testing (0088, 0095) provides calibration data.

---

### 0114 — Language setting for multi-language plugin support

**Goal.** Let non-English-speaking users work in their native language. A `Language:` setting in the consumer project's CLAUDE.md instructs all skill/hook output to use that language — without translating plugin docs, control tokens, or templates.

**Approach.** Lightweight: Claude already speaks dozens of languages. The setting tells Claude what language to respond in; plugin docs stay English (Claude reads them either way). No locale folders, no parallel doc trees. Scope: skill output, hook deny messages, procedure-doc guidance that Claude paraphrases. Control tokens (`Status:`, `Changes:`, `[SECURITY]`, etc.) remain English-only — this is documented explicitly in CLAUDE.md and reinforced during `/sovsetup`.

**Hard constraints (from v97 research).**

1. **Git `core.quotepath` for non-ASCII filenames.** Git's default escapes non-ASCII characters with octal notation. Drift check 1 matches git-diff output paths against the batch file list in Claude's context window — `Path.resolve()` can't normalise octal escapes. Fix: `/sovsetup` sets `git config --local core.quotepath false`.

2. **Control tokens are English-only.** Every metadata keyword the hooks regex-match (`Status:`, `Changes:`, `Serves UX.md:`, `Confirmed Explicitly:`, `[SECURITY]`) must remain in English. A translated `Estado: activo` silently breaks phase enforcement. The language setting must document this, and `/sovsetup` scaffolding should note it in the consumer CLAUDE.md.

**BOM hardening fold-in.** Switch the four `open()` / `read_text()` call sites in hooks from `encoding="utf-8"` to `encoding="utf-8-sig"` to strip Windows BOM bytes. Sites: `safe_read_text()` in `project_state.py`, `session_start.py`, and direct `open()` calls in `user_prompt_submit.py` and `pre_tool_use.py`. One-line fix per site. Without it, a user who hand-edits a spine file in a Windows editor that prepends a BOM silently breaks `^Status:` regex matching on line 1. (From OQ "UTF-8 BOM hardening," surfaced v97.)

**Inputs.** `Dev/Resources/research/ResearchFindingsMult (1).md` (§§ 3.1–3.3, 4.2). Current hook file-read sites. CLAUDE-TEMPLATE.md. `/sovsetup` procedure.

**Outputs.** `Language:` field in CLAUDE-TEMPLATE.md (optional, defaults to English). `/sovsetup` sets `core.quotepath false` when language is non-English. Hook deny messages and skill output respect the setting. Control-token immutability documented. Reference manual section.

**Success criteria.** A French-speaking tester runs `/sovsetup`, sets `Language: French`, and receives all Claude-generated output in French. Control tokens remain English. Non-ASCII filenames in batches don't break drift detection. No plugin doc translation needed.

**Risks / dependencies.** Soft dep on E2E testing (0088) to validate the base flow before adding language variation. Risk: edge cases in hook deny messages that interpolate English fragments — need an audit pass. Low overall risk given the lightweight approach.

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `Dev/Resources/tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 184 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.


---


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
| 0110 | Queued-pipeline staleness sweep at close | Concurrent-build detection, OQ staleness detection (SessionStart hooks); staleness sweep + lost-feature check (close steps 9–10). **Shipped v111.** |
| 0112 | Skill split + BUILD-PLAN rename | `/sovdeliberate`, `/sovideate`, `/sovplan` narrowing, build-snapshot architecture, BACKLOG→BUILD-PLAN consumer rename. **Shipped v112.** |
| 0115 | /sovsetup E2E fix sweep | Five fixes for case-1 setup: handoff step, principles yes/no gate, method-infra whitelist, heredoc stripping, boundary removal. **Shipped v113.** |
| 0088 | Build E2E test | Build lifecycle validated end-to-end; 3 pre_tool_use.py bugs filed as 0116; compact-nudge idea folded into 0113. **Shipped v114.** |
| 0121 | Dev-side reader test | Three-agent reader test against dev-side docs; gap list + 2 new batches + 11 OQs. **Shipped v120.** |
| 0116 | Method-infra whitelist + phase-detection fixes | Three pre_tool_use.py bug fixes: root-level _method/ file whitelist, test-log/build-log close exemption, all-ticked phase-detection fallback. 8 new tests. **Shipped v115.** |
| 0113 | Session-length safeguards | Pre-build sizing, mid-session compact nudge, invocation-prompt compact nudge, git.md close-prompt fold-in. **Shipped v116.** |
| 0114 | Language setting + BOM hardening + blocker gate + carried-forward removal | Language: field, utf-8-sig BOM strip, pre-build blocker gate, carried-forward removal. **Shipped v117.** |
| 0117 | Build-phase close handoff artifact | `## Close handoff` in build snapshot; build appends per-file, close reads first. **Shipped v118.** |

Shipped/cancelled batches end here. Queued batches are below with full scope content — no separate scope files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0124 — Dev-side close procedure fixes

**Goal.** Fix three procedural inconsistencies in session-protocol.md's close sections, surfaced by the 0121 reader test.

**Approach.** Three targeted fixes, all in session-protocol.md and session-reference.md:
- **Batch removal timing asymmetry (T2).** Implementation close removes the consumed batch at step 10 (after commit/tag); lighter close handles it inside the pre-commit checkpoint at step 5 (before commit). Decide which timing is correct and make both paths consistent.
- **Stale step-number cross-reference (T3).** session-reference.md → Planning artefacts says "removed (step 9)" but session-protocol.md numbers this step 10. Update session-reference.md to match.
- **Proxy format spec unlocated (T4).** Close step 6 says "write the proxy per its format spec" but doesn't say where that spec lives. Either point to the existing proxy files as format exemplars or describe the dev-side proxy format inline.

**Outputs.** Updated session-protocol.md (both close paths) and session-reference.md. No code changes.

**Success criteria.** Both close paths agree on batch removal timing. Step references are consistent across docs. Proxy regen step has an actionable format reference.

**Risks / dependencies.** None. Small surface area — three doc edits.

---

### 0125 — Dev-side opener routing completeness

**Goal.** Close three routing gaps in session-protocol.md's opener routing table: blended/multi-type openers, disambiguation sequencing within multi-thread openers, and git-unavailable fallback.

**Approach.** Two additions to session-protocol.md:
- **Blended-opener rule (T1 + M9).** Add a rule below the routing table for openers that match multiple session types. Define priority ordering across session types. State that threads are handled sequentially, highest-priority first. Specify how disambiguation requests are sequenced when the one-item-at-a-time rule applies (e.g. resolve the routing-critical ambiguity first, defer others to mid-session).
- **Git-unavailable fallback (T5).** Add a fallback to step 1 for when `git describe` fails or is unavailable. Point to CLAUDE.md's *Current state* section as the recovery source, with a note to flag if the value looks stale.

**Outputs.** Updated session-protocol.md routing table and session-open step 1.

**Success criteria.** A stranger-Claude receiving a blended opener can route without improvising. Git-unavailable scenario has a documented fallback.

**Risks / dependencies.** T1 requires a priority ordering decision — that's a design choice, not just a doc fix. Low risk: the ordering can be inferred from current practice (E2E > implementation > planning > ideation > doc-only > standby), but it needs to be stated explicitly.

---

### 0118 — Scripted close mechanicals (dev-side)

**Goal.** Replace Claude-executed footer bumps, version updates, and proxy regeneration with a Python script on the dev side. Removes the most error-prone and token-expensive mechanical close steps.

**Approach.** A Python script at `Dev/Resources/scripts/bump_version.py` taking `(old_version, new_version)` that handles all footer bumps across the repo, `plugin.json` version field, `PLUGIN_METHOD_VERSION` in `session_start.py`, and summary-proxy regeneration. Output is a `git diff`-verifiable set of changes. Updated dev-side session-protocol.md close steps to reference the script.

**Outputs.** Dev-side `bump_version.py`. Updated dev-side session-protocol.md close steps.

**Success criteria.** Running the script produces correct footer bumps across all files, verified by `git diff`. No Edit-tool failures on unread files. Close-session token cost for mechanicals drops to near zero (one script invocation + diff review).

**Risks / dependencies.** Half-proven — v112 already fell back to a script. Risk: footer discovery (script must find all files with the footer pattern). Mitigation: glob pattern + test coverage. Depends on accurate footer pattern (`*No-code method — Version N.*`).

---

### 0119 — Two-turn close procedure (dev-side)

**Goal.** Split the dev-side close into a judgment pass and a mechanical pass with a `/compact` point between them, so judgment work runs while build context is fresh and mechanicals run with minimal context.

**Approach.** Update dev-side session-protocol.md to define an explicit turn boundary after the judgment steps (parity, frame corrections, build-log narrative, idea sweep) and before the mechanical steps (script run, proxy regen, commit/tag/push). The boundary is a `[PROMPT]` recommending `/compact`. The mechanical pass needs only the version numbers and the script.

**Outputs.** Updated dev-side session-protocol.md with explicit two-turn structure. `/compact` recommendation at the turn boundary.

**Success criteria.** Judgment pass completes without context pressure from upcoming mechanicals. Mechanical pass runs cleanly after `/compact`. Total close cost lower than single-turn close on high-file-count batches.

**Dependencies.** 0118 (dev-side scripted mechanicals) — the script is what makes the second turn lightweight.

**Risks.** Low. If the split doesn't help in practice, it's a soft recommendation, not enforced — sessions can still close in one turn.

---

### 0122 — Dev-side structure mirroring audit

**Goal.** Surface places where the dev-side prose-only structure (CLAUDE.md, session-protocol.md, session-reference.md, BACKLOG.md, .proxies/) could benefit from mirroring plugin-side patterns. Absorbs the dev-side structural changes originally in 0120 (history table removal, Planning batches/Ideas sections, Approach field).

**Approach.** Using the 0121 gap list as input, systematically compare dev-side and plugin-side structures. For each plugin-side pattern (DOC-STRUCTURE schema definitions, VOCABULARY terms, procedure doc step format, batch scope structure, proxy format), assess whether the dev-side equivalent is weaker, missing, or intentionally different. Propose specific changes — not a wholesale adoption of plugin conventions, but targeted improvements where the prose-only structure has drifted from patterns the plugin has already proven.

**Inputs.** `Dev/Resources/research/dev-side-reader-test-findings.md` (from 0121). Plugin-side docs at HEAD for structural comparison. Current dev-side docs at HEAD.

**Outputs.** Research file `Dev/Resources/research/dev-side-mirroring-audit.md` with findings and proposals. New BACKLOG batches for any changes worth implementing. Dev-side BACKLOG.md restructured (history table removed, Planning batches + Ideas sections + Approach field added — originally from 0120).

**Success criteria.** Every plugin-side pattern assessed with a clear keep/adopt/skip judgment. 0121 gap list items addressed or explicitly deferred. Dev-side BACKLOG restructure complete. New batches scoped for any structural changes worth making.

**Risks / dependencies.** Hard dep on 0121 (gap list). Risk: scope creep — "mirror the plugin" can expand indefinitely. Mitigation: the gap list constrains the audit to proven pain points, not theoretical improvements. The dev-side convergence strategy (CLAUDE.md) says don't adopt the plugin here yet — this batch proposes, doesn't enforce.

---

### 0123 — Plugin-side close mechanicals + two-turn procedure

**Goal.** Port the dev-side close improvements (scripted mechanicals and two-turn structure) to the plugin side.

**Approach.** Consumer-side version bump script at `plugin/scripts/bump_version.py` (or folded into `/sovclose` procedure) handling the consumer project's footer bumps and proxy regeneration. Update `close.md` with two-turn structure: judgment pass (parity, frame corrections, build-log narrative, idea sweep) then `/compact` boundary then mechanical pass (script run, proxy regen, commit/tag/push). Reference manual note.

**Outputs.** Consumer-side `bump_version.py` or `/sovclose` integration. Updated `close.md` with two-turn structure and script reference. Reference manual update.

**Success criteria.** Consumer-side script produces correct footer bumps, verified by `git diff`. Two-turn close structure works in `/sovclose` flow. Reference manual documents both the script and the two-turn pattern.

**Dependencies.** Dev-side 0118 and 0119 (pattern proven on dev side first).

**Risks.** Consumer-side footer patterns differ from dev-side — script needs to handle both or be a separate implementation. Low risk given dev-side script proves the approach.

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

### Lighter close step reordering rationale

**Surfaced.** v120 (0121 reader test, M1).

**The question.** The lighter close reorders steps compared to the implementation close (idea sweep first, then build-log, footers later) with no stated rationale. Is this intentional, and if so, what drives the difference?

**Why it matters.** A reader trying to understand the lighter close by analogy to the full close will be confused by the different ordering. If the reordering is intentional (e.g. idea sweep first because there's no parity/frame work to inform it), documenting the reason prevents future sessions from "fixing" the order back. If accidental, aligning the paths reduces cognitive load.

**Next step.** Decide during 0124 (close procedure fixes) — fold in if the answer is obvious, or defer if it needs deliberation.

---

### Frame-correction sweep: categorical vs conditional skip in lighter close

**Surfaced.** v120 (0121 reader test, M2).

**The question.** The lighter close skips the frame-correction sweep categorically ("no feature frame changed"). But a doc-only session consuming a queued batch could change a load-bearing frame (e.g. rewriting how a concept is described in BACKLOG scope text). Should the skip be conditional on whether a frame actually changed, rather than categorical by session type?

**Why it matters.** A doc-only batch that rewrites scope text could leave queued batches referencing an old frame — exactly what the sweep catches. The categorical skip assumes lighter-close sessions never change frames, which isn't guaranteed.

**Next step.** Park. Low frequency — doc-only sessions rarely change frames. Revisit if a frame-change slips through a lighter close.

---

### Doc-only batch-input check: skip rule underspecified

**Surfaced.** v120 (0121 reader test, M3).

**The question.** The routing table says doc-only sessions skip "batch-input check (step 4) if no queued batch is being consumed." What happens when a doc-only session *does* consume a queued batch — does step 4 apply? The conditional phrasing is easy to misread as "always skip for doc-only."

**Why it matters.** A doc-only batch with an Inputs line (e.g. referencing a research file or external artifact) needs the same out-of-repo check as any other batch. Misreading the skip rule could let a session start without its inputs.

**Next step.** Fold into 0124 or 0125 as a one-line clarification when those batches touch the routing table or close paths.

---

### Remote-control standby close path unspecified

**Surfaced.** v120 (0121 reader test, M4).

**The question.** The routing table says remote-control standby sessions use the close path that matches "the work done," but gives no guidance on classifying what was done — or whether a commit/tag/push is expected if nothing was done.

**Why it matters.** Standby sessions are rare in practice (most sessions have a clear type), but when they occur, the lack of close-path guidance means Claude has to improvise. A "no work done → no close needed" rule, or a "classify the work and follow the matching close" rule, would be sufficient.

**Next step.** Park. Very low frequency. Revisit if standby sessions become more common or if a standby session produces an awkward close.

---

### Informal opener modifiers unmapped

**Surfaced.** v120 (0121 reader test, M5).

**The question.** Terms like "spare session," "quick one," "I have 10 minutes" appear in real openers but have no routing-table mapping. Should they be addressed explicitly, or is the current "pick the highest-priority match on the substantive direction" approach sufficient?

**Why it matters.** The fresh-session agent treated "spare" as availability context rather than a session type — a reasonable inference, but one the docs don't prepare a reader for. If informal modifiers affect session scope (e.g. "quick one" implying lighter work), that interaction isn't documented.

**Next step.** Consider folding a one-line note into 0125 (opener routing completeness) when it ships. Low priority — current practice handles it fine.

---

### Dev-side session-open state summary has no template

**Surfaced.** v120 (0121 reader test, M6).

**The question.** Plugin-side has the SessionStart hook mandating a specific status summary format (batch counts, next batch, pending tests). Dev-side has no equivalent — session-protocol.md says "report what was loaded and ask" but gives no format for the state summary when the task is clear.

**Why it matters.** Each dev session currently improvises its opening summary. A lightweight template (version, next batch, queue depth, OQ count) would make sessions consistent without adding enforcement overhead. Counter-argument: dev sessions have fewer moving parts than consumer sessions, so a template may be over-engineering.

**Next step.** Consider during 0122 (dev-side structure mirroring audit) — this is exactly the kind of plugin-side pattern worth evaluating for dev-side adoption.

---

### Sub-agent warning rule boundary for scoped work

**Surfaced.** v120 (0121 reader test, M7).

**The question.** CLAUDE.md says "warn before spawning a subagent for a single simple operation." When the batch scope explicitly designs for sub-agents (as 0121 did), does the warning rule still apply?

**Why it matters.** The fresh-session agent flagged the warning as a courtesy even though the batch scope explicitly called for three sub-agents. The rule is written for spontaneous single-operation spawning — not intentionally scoped multi-agent work. Clarifying the boundary would prevent unnecessary warnings on designed sub-agent deployments while preserving the guard on ad hoc spawning.

**Next step.** Park. Low friction — Claude flagging an unnecessary warning is a minor cost. Revisit if sub-agent-designed batches become more common.

---

### Session-open step 2 load-purpose unstated

**Surfaced.** v120 (0121 reader test, M8).

**The question.** Step 2 says "read universal-behaviour.md, DOC-STRUCTURE.md, VOCABULARY.md, Reference manual.md at HEAD" but doesn't say what to look for in each, how large they are, or what context they provide to the session. Should step 2 include a one-line purpose note per doc?

**Why it matters.** A fresh reader doesn't know whether "read at HEAD" means a 10-line file or a 200-line file. The batching cost of step 2 is invisible. One-line annotations (e.g. "universal-behaviour.md — behavioural rules and routing table") would help a new Claude prioritize and extract the right context.

**Next step.** Consider during 0122 (dev-side structure mirroring audit) — this is a doc-usability question the audit should assess.

---

### Duplicate batch 0102 in shipped batch table

**Surfaced.** v120 (0121 reader test, B1).

**The question.** BACKLOG.md's shipped batch table has two rows for batch number 0102. The first occurrence has no shipped annotation; the second says "Shipped v99." Is the first row a leftover from an earlier edit?

**Why it matters.** Minor data integrity issue. Doesn't affect any process, but a reader scanning the table sees a duplicate that implies something was missed.

**Next step.** Fix as a one-line cleanup in the next session that edits BACKLOG.md. No batch needed.

---

### Cross-reference precision across dev-side docs

**Surfaced.** v120 (0121 reader test, B2/B3/B4/B5).

**The question.** Four related precision issues in cross-references between dev-side docs: (a) session-protocol.md step 4 relies entirely on a forward pointer to session-reference.md with no inline explanation; (b) session-reference.md's build-log entry shape references DOC-STRUCTURE.md without a path; (c) CLAUDE.md says "read proxies first" while session-protocol.md step 3 says "read BACKLOG in full" without mentioning proxies; (d) the pre-commit checkpoint in each close path references its own step numbers, making cross-path comparison confusing.

**Why it matters.** Individually minor. Collectively, they make the doc set harder for a fresh reader to navigate — each instance requires the reader to either flip to another doc or hold two numbering schemes in mind. The reader test found these because the agents were explicitly instructed to flag "the document does not say" moments.

**Next step.** Park. Address opportunistically when the relevant sections are edited for other reasons. Not worth a dedicated batch.

---

### Lighter-close naming vs doc-only batches that consume queued batches

**Surfaced.** v120 (0121 reader test, B6).

**The question.** The lighter close is described as "run when the session didn't ship code." But a doc-only batch that consumes a queued batch may need more than "lighter" — the conditional note about batch removal reads as an afterthought. Should the distinction be "consumed a queued batch with code changes" vs. everything else, rather than "shipped code" vs. didn't?

**Why it matters.** The wording creates an edge case where a doc-only session consuming a queued batch follows the lighter close path but then hits the conditional batch-removal step that feels bolted on. Reframing the distinction would make the conditional unnecessary.

**Next step.** Consider during 0124 (close procedure fixes) since that batch already touches both close paths.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `Dev/Resources/tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 184 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.


---


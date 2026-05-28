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
| 0116 | Method-infra whitelist + phase-detection fixes | Three pre_tool_use.py bug fixes: root-level _method/ file whitelist, test-log/build-log close exemption, all-ticked phase-detection fallback. 8 new tests. **Shipped v115.** |
| 0113 | Session-length safeguards | Pre-build sizing, mid-session compact nudge, invocation-prompt compact nudge, git.md close-prompt fold-in. **Shipped v116.** |

Shipped/cancelled batches end here. Queued batches are below with full scope content — no separate scope files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0095 — /sovtest skill E2E validation — **PARKED**

**Parked.** v114. 0088 shipped — dep met. Shelved: user is cowboy-testing informally rather than running structured E2E batches. Revisit when there's a specific reason to formalize.

**Goal.** End-to-end test of `/sovtest` skill (shipped in 0094) against a real project. Validate the full flow: invoke after build, follow guided walkthrough, report failure, get debugging support.

**Inputs.** `/sovtest` skill and `plugin/docs/procedures/testing.md` (from 0094). A burner app with pending TEST-LOG rows across multiple test types. `Dev/Resources/research/e2e-greenfield-post-redesign.md`.

**Outputs.** Research file `Dev/Resources/research/e2e-test-skill-validation.md`. New BACKLOG entries for issues. `/sovclose` handoff validation.

**Test plan.** Happy path: invoke `/sovtest`, walk through Look-and-click and Run-and-read tests, report Pass, verify row updates. Failure path: report Fail, verify debugging protocol, verify routing to BUILD-PLAN. Edge cases: no pending tests (graceful exit), mid-build invocation (rejected), partial progress on early stop. Handoff: confirm planning read-back handles rows `/sovtest` already confirmed.

**Success criteria.** Non-coder completes full flow without independent knowledge. Debugging produces useful output on deliberate failure. TEST-LOG state after `/sovtest` is consistent with planning expectations. No silent failures.

**Risks / dependencies.** Hard dep on 0094 (shipped v100). Soft dep on 0088 (reuse app state — note: 0088 now starts fresh, so test-type variety depends entirely on what that build produces). Risk: insufficient test-type variety in burner app.

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

**Risks / dependencies.** 0088 shipped (v114) — base build flow validated. Risk: edge cases in hook deny messages that interpolate English fragments — need an audit pass. Low overall risk given the lightweight approach.

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### Session-close cost: structured handoff and mechanical automation

**Surfaced.** v112.

**The question.** Should `/sovbuild` produce a structured handoff artifact during the build phase, and should the mechanical close steps (footer bumps, version trackers, proxy regeneration) be scripted rather than Claude-executed?

**Why it matters.** The v112 session burned roughly half a usage window on the implementation close alone. The primary cost driver was rediscovery — the close session had to re-explore the codebase to find what the build session changed (grepping crash-course files for missing skill names, reading templates for wrong section counts, scanning BUILD-PLAN for stale frame references). A secondary cost was mechanical work (13 footer bumps) that failed via the Edit tool on unread files and had to be retried via a Python script. Both are avoidable with upfront structure.

**Working notes.** Three candidate changes, independent of each other:

1. **Build-phase handoff artifact.** As `/sovbuild` works, it appends to a running list: new consumer-facing names introduced, files touched, frame assumptions that shifted. The close session reads this instead of re-exploring. Could be a draft section of the build-log entry, written mid-build rather than composed at close.

2. **Scripted mechanicals.** A Python script taking `(old_version, new_version)` that handles footer bumps, `plugin.json` version, `PLUGIN_METHOD_VERSION` in `session_start.py`, and proxy regeneration. Removes ~30% of close-session token cost. Already half-proven — the v112 session fell back to a Python script for footers after Edit failures.

3. **Two-turn close.** Judgment work (parity check, frame corrections, build-log narrative) in one turn; mechanical finishing (script run, commit/tag/push) in a second turn or fresh session. The second turn needs almost no context.

**Next step.** The compact-nudge fold-in was addressed by 0113 (shipped v116). The remaining three ideas (handoff artifact, scripted mechanicals, two-turn close) are independent — promote to a batch or park when next planning.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `Dev/Resources/tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 184 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.


---


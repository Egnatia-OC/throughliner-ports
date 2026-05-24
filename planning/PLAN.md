# Plan — V17 onwards

Session-by-session roadmap for the plugin migration. Companion to `INVENTORY.md` and the Opus feasibility response (`claude-code-plugin-feasibility-response.md`).

## Versioning convention

Sessions tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal sessions leave it unchanged. Full rule: `BUILD-METHOD.md` → *Session tag vs. method version*.

Scope files: `sessions/NNNN-kebab-title.md`. Allocation: next unused 4-digit number by scanning `planning/sessions/`. Numbers never reused or renumbered; reorder by moving rows below, not renaming files. Files are PROVISIONAL — a file existing isn't a commitment.

## The session list

| # | Session | Output |
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
| 0071 | Subagent cost optimization | Planning subagent from ~31.6k to <15k tokens: conditional drift-check skip, classify-then-dispatch, Sonnet evaluation. |
| 0072 | After-build source-code boundary | Hard boundary: after-build cannot edit source/build files. Fold in "run commands yourself" rule. |
| 0073 | Stop hook before-build→build chain fix | Stop hook exits silent after before-build (zero ticked = just locked). |
| 0074 | Session-open status summary | User-facing batch count, next batch, and proceed prompt on session open. |
| 0075 | Dev-side log folder migration | BUILD-LOG.md + TEST-LOG.md → folder structures. Dev-side only, no plugin changes. |
| 0076 | Plugin-side TEST-LOG folder migration | test-log/ folder convention for consumer projects. Mirrors V50 build-log migration. Depends on 0075. |
| 0077 | Greenfield E2E: burner app from scratch | Planning-from-scratch → full build cycle on throwaway app. Tests the most important untested path. Soft dependency on 0071–0074. |
| 0078 | Post-fix E2E validation (Taskflow) | Re-run build cycle confirming 0072–0074 fixes work. Hard dependency on 0072+0073+0074. |
| V60+ | Remaining parked open questions | Graduation (indefinitely shelved). Prose-only rewrite (indefinitely parked). |

60 sessions through 0078, plus V60+ TBD. Some will combine or split.

## Session-scope file shape

Each `sessions/NNNN-kebab-title.md` follows this shape:

```markdown
# NNNN — [Session Name]

## Goal
[One paragraph: what this session produces.]

## Inputs
[Docs/files the session reads / depends on.]

## Outputs
[New files, edited files, plugin components.]

## Success criteria
[How we know the session succeeded.]

## Open questions for this session
[Open design questions to resolve.]

## Risks / dependencies
[What could derail this. Dependencies on prior sessions.]
```

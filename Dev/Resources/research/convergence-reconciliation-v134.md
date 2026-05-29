# Convergence reconciliation map — v134

Stage 1 convergence reader test. Three sub-agents read both sides cold and built inventories: rules (universal-behaviour.md vs session-protocol.md + CLAUDE.md), structure/terminology (DOC-STRUCTURE.md + VOCABULARY.md vs session-reference.md), workflow (close.md vs session-protocol.md close sections).

Deduplicated across all three inventories. Entries are a punch list — tick as resolved.

## Summary

| Category | Count |
|---|---|
| Aligned | 23 |
| Contradicts / diverges | 18 |
| Plugin-only (expected) | ~55 |
| Plugin-only (gap) | 24 |
| Dev-only (preserve) | 28 |
| Dev-only (stale) | 0 |
| Stale | 0 |

Zero stale findings on either side — both were updated recently. The high "dev-only preserve" count reflects the dev side's legitimately different needs (versioning, E2E testing, project orientation, multi-file disambiguation). The "plugin-only expected" count is dominated by consumer-only mechanics (hooks, skills, locks, `_method/` paths, adoption detection).

**Actionable categories:** Contradictions (18 — need decisions), gaps (24 — need prose equivalents on dev side), dev-only preserve (28 — review whether any should flow to plugin). Aligned and expected need no action.

---

## Contradictions — need decisions

Both sides address the concept but disagree. Each needs a deliberate choice about which version to adopt or whether the divergence is intentional.

---

- [ ] **C01. Routing table structure.** Plugin (UB): 13-row content-based table routing openers to procedure docs by what the user said. Dev (SP L47-61): 6-row session-type table routing by what kind of work, with load/skip/shape/close columns. Different classification systems, different route targets, partially overlapping coverage. Plugin has routes dev lacks (test notes, revert, bug report, doc audit, scope question, method question). Dev has routes plugin lacks (E2E test, Remote-control standby, Doc-only as distinct type). **Resolution:** likely intentionally different — dev sessions have a broader taxonomy. But dev table should absorb useful plugin routes where applicable (bug reports, method questions).

- [ ] **C02. Mixed-opener priority.** Plugin (UB): `/sovsetup` > resume > planning seed. Dev (SP L61): E2E test > Implementation > Planning > Ideation > Doc-only > Remote-control standby. Different priority systems for different routing approaches. **Resolution:** intentionally different — follows from C01.

- [x] **C03. Flag taxonomy.** Plugin (UB L85-93): three categories — security/red-flag → BACKLOG Red flags, out-of-scope → chat, UX-affecting → suggest UX.md change. Dev (SP L99-103): three categories in idea sweep — BACKLOG batch, BACKLOG OQ, flag in recap. Red-flag routing absent from dev side. **Resolution:** dev side should add red-flag routing as a triage destination in the idea sweep. The UX-affecting category doesn't apply (no consumer UX.md), but security/privacy concerns do arise in plugin development. **Resolved v136:** added security/privacy/data-integrity concern as fourth triage destination in session-protocol.md idea sweep.

- [x] **C04. Run commands yourself vs guide me through.** Plugin (UB R14): "Execute directly — don't ask the user to run it." Dev (CM L129-130): "Guide me through smoke tests step by step." Tension is real but likely context-dependent: Claude runs commands in dev implementation sessions; Alex runs commands manually in E2E test sessions. **Resolution:** add explicit prose to CM — "Claude runs shell commands directly during dev sessions. Exception: E2E test commands that must execute in a separate consumer-project session." **Resolved v136:** added "Command execution" section to CLAUDE.md with dev-session default and E2E exception.

- [ ] **C05. TEST-LOG columns (10 vs 7).** Plugin (DOC-STRUCTURE L103-148): 10 columns (#, Date, Session, Component, Test Description, Type, Verifier, Status, Confirmed Explicitly, Notes). Dev (session-reference L228-249): 7 columns (#, Date, Session, Test, Component, Status, Notes). Missing dev-side: Type, Verifier, Confirmed Explicitly. Column ordering also differs (Component before Test Description in plugin; Test before Component in dev). **Resolution:** the dev side's 7-column shape was a deliberate simplification — dev tests don't need the confirmation gate (no hook enforcement) or verifier tracking (Alex runs tests herself). Confirm this is still intentional or migrate to 10 columns for convergence. **Partial v138:** column ordering aligned — dev side now uses Component before Test, matching plugin sequence. Column count (7 vs 10) remains a deliberate simplification.

- [ ] **C06. Build-log Performance section.** Plugin (DOC-STRUCTURE L152-187): includes `## Performance` section with 6 structured measures. Dev (session-reference L151): explicitly excluded — "Consumer build-log entries carry an additional `## Performance` section... This dev build-log doesn't use it." **Resolution:** documented as deliberate. Confirm still intentional.

- [ ] **C07. BACKLOG entry shape.** Plugin (DOC-STRUCTURE L317-403): two-region build batches (scope-context: Goal/Outputs/Success criteria/Decisions/Dependencies/Red flags + build-operations: Changes/Inputs/Files/Tests/Serves). Dev (session-reference L157-186): flat field list (Goal/Approach/Inputs/Outputs/Success criteria/Risks-dependencies). Dev side explicitly acknowledges divergence at L186. Dev has Approach (plugin doesn't). Plugin has Changes/Files/Tests/Serves (dev doesn't). **Resolution:** documented as deliberate — dev batches are roadmap entries, not build instructions. But if convergence goals include aligning the field sets, Approach needs a plugin-side equivalent or explicit "dev-only" designation.

- [ ] **C08. Scope-context section names.** Plugin (VOCABULARY): Goal, Outputs, Success criteria, Decisions, Dependencies, Red flags. Dev (session-reference L163-176): Goal, Approach, Inputs, Outputs, Success criteria, Risks/dependencies. Different field sets — dev merges dependencies with risks, has Approach, lacks Decisions and Red flags as named sections. **Resolution:** closely tied to C07. Decide together.

- [ ] **C09. Batch-sizing principle.** Plugin (VOCABULARY): right size = verification burden (distinct testable behaviours). Dev (session-reference L183-184): right size = entry readability (fits on a screen). Different metrics. **Resolution:** both are valid for their contexts — plugin sizes for test coverage, dev sizes for session-open readability. Make the divergence explicit rather than silently different.

- [x] **C10. Build batch vs queued batch naming.** Plugin uses "build batch" for engineering work units. Dev uses "queued batch" for the analogous concept. **Resolution:** clarify that dev "queued batch" = plugin "build batch" as a cross-reference in session-reference.md, or adopt one term. **Resolved v138:** cross-reference added to session-reference.md → *Queued batch entry shape*.

- [x] **C11. Batch status mechanism.** Plugin: explicit `Status:` line with three values (queued/parked/shipped). Dev: presence/absence in queue + optional `**Parked.**` annotation; shipped = removed from BACKLOG. **Resolution:** closely tied to C14 (batch lifecycle). Decide together. **Resolved v139:** shipped removed from plugin status values (now queued/parked only). Completed batches removed from BACKLOG at close, matching dev-side model. `Status: parked` vs `**Parked.**` annotation remains a deliberate format difference.

- [ ] **C12. Dependencies standalone vs merged.** Plugin separates Dependencies from Red flags as distinct scope-context sections. Dev merges dependencies with risks into one field (Risks / dependencies). **Resolution:** part of C08.

- [ ] **C13. Doc-parity scope.** Plugin (close.md): narrow — grep consumer spine docs for stale name/reference from Close handoff. Dev (SP L198-215): broad — six categories (Vocabulary, Mechanism descriptions, Templates, Inventory, Reference manual, Ghost references). Plugin says [SILENT]; dev says [BRIEF]. **Resolution:** dev version is correct for this context — plugin development touches docs that consumer builds don't. Keep the broader dev-side audit. Note that the plugin's narrower scope is appropriate for consumer projects.

- [x] **C14. Batch lifecycle on completion.** Plugin (close.md): writes batch back to BACKLOG with `Status: shipped` (preserves history). Dev (SP L127, L167): removes batch from BACKLOG entirely. **Resolution:** real design divergence. Plugin preserves shipped batches for historical reference; dev side relies on build-log for history. Decide which model. **Resolved v139:** adopted dev-side model — `/sovclose` deletes the snapshot without writing back. Build-log entry is the shipped record. `Status: shipped` removed as active value; kept in parser for legacy tolerance.

- [ ] **C15. Footer bump trigger.** Plugin (close.md): triggers on detected mismatch between plugin version and doc footers (mechanical check at session start). Dev (SP L109): triggers on judgment call about whether changes are "substantive." **Resolution:** different mechanisms suit different contexts. Dev side can't detect mismatches mechanically (no hook). The judgment-based trigger is correct for dev sessions but should be stated more explicitly.

- [x] **C16. Open questions — Working notes and graduation paths.** Dev (session-reference L190-224) adds a Working notes field (optional) and four explicit graduation paths that plugin-side DOC-STRUCTURE doesn't specify. **Resolution:** minor. Dev additions are useful — consider flowing graduation paths to plugin DOC-STRUCTURE. **Resolved v138:** plugin-consideration note added to session-reference.md → *Open-questions entry shape*. Future plugin batch can adopt graduation paths into DOC-STRUCTURE.

- [ ] **C17. Commit/tag/push flow.** Plugin: delegates to `/sovgit` skill (single invocation). Dev (SP D9-D11): three explicit steps with two prompt points (commit, then push). **Resolution:** structurally different — dev side has no `/sovgit` skill. Dev three-step version is the correct prose equivalent. Not a convergence action.

- [ ] **C18. Pre-commit checkpoint items.** Plugin (close.md): 9 items including MANIFEST, TEST-LOG, staleness sweep. Dev (SP L120-128): 7 items including doc-code parity, frame-correction. Different lists because different close flows produce different artifacts. **Resolution:** each list is correct for its context. When dev side adds gap items (staleness sweep, lost-feature check — see G16, G17), the dev checkpoint should expand to match.

---

## Plugin-only gaps — dev side needs these

Plugin has it, dev doesn't, and the dev side should have a prose equivalent. Each needs a rule or convention added to session-protocol.md, session-reference.md, or CLAUDE.md.

---

### Rules gaps (from Sub-agent A)

- [x] **G01. No stealth fixes.** Plugin (UB R04): "If a change causes a regression, state plainly." Dev side has no equivalent. Dev sessions do implementation work where regressions happen. **Add to:** session-protocol.md session-middle or CLAUDE.md. **Resolved v136:** added to session-protocol.md → Mid-session rules.

- [x] **G02. Red-flag routing.** Plugin (UB R06): detailed three-outcome triage for security/privacy/data-integrity concerns (address now / attach to planned feature / defer to BACKLOG Red flags with `[RED FLAG]` marker). Dev idea sweep has no red-flag category. **Add to:** session-protocol.md close procedure (expand idea sweep triage) and/or CLAUDE.md. **Resolved v136:** added as fourth triage destination in idea sweep (shared with C03).

- [x] **G03. Adherence-drop diagnostic.** Plugin (UB R09): when user reports quality drop, diagnose structural causes (context filling, missing reads, compaction). Dev side just retries. **Add to:** CLAUDE.md collaboration rules. **Resolved v136:** added "Adherence-drop diagnostic" section to CLAUDE.md.

- [x] **G04. Proactive research.** Plugin (UB R11): watch for decisions needing external info, propose searches unprompted, three-mechanism priority (MCP, WebSearch, copyable prompt). Dev side has reactive verification (save research results) but not the proactive dimension. **Add to:** CLAUDE.md or session-protocol.md. **Resolved v136:** added "Proactive research" section to CLAUDE.md, positioned before "File research before moving on."

- [x] **G05. Mid-session compact nudge.** Plugin (UB R15): 15+ exchanges past `/sovbuild` without `/sovclose` → nudge. Dev side has turn-boundary `/compact` suggestions but no proactive mid-session trigger. **Add to:** session-protocol.md session-middle section. **Resolved v136:** added to session-protocol.md → Mid-session rules.

- [x] **G06. No unplanned refactoring + carve-outs.** Plugin (UB P02): prohibition on refactoring/renaming/restructuring outside the agreed plan, with prerequisite and re-batching carve-out exceptions. Dev side has no prohibition despite doing implementation work. **Add to:** session-protocol.md session-middle. **Resolved v136:** added to session-protocol.md → Mid-session rules with both carve-out exceptions.

- [x] **G07. Make BACKLOG edits, don't describe them.** Plugin (UB P03): "Do not describe a BACKLOG.md edit for me to apply — make the edit." Applicable to dev sessions. **Add to:** session-protocol.md or CLAUDE.md. **Resolved v136:** added "Make BACKLOG edits directly" section to CLAUDE.md.

- [x] **G08. Close is mandatory, not advisory.** Plugin (UB P04): explicit prohibition on skipping close with consequence explanation. Dev side describes close steps but never states they're non-optional. **Add to:** session-protocol.md session-close preamble. **Resolved v136:** added mandatory statement to session-protocol.md → Session close preamble.

- [x] **G09. Pre-build OQ blocker gate.** Plugin (UB RO04): before-build procedure gates on unresolved OQs and ideas blocking the top batch. Dev batch-input check (SP L40) catches missing files but not OQ blockers. **Add to:** session-protocol.md session-open step 4 or new step 4b. **Resolved v136:** added as step 4b in session-protocol.md → Session open.

- [x] **G10. Session handoff protocol.** Plugin (UB H01): four-step procedure for preparing state when context runs low mid-build (tick completed, annotate in-progress, record decisions, notify). Dev side has no explicit handoff procedure. **Add to:** session-protocol.md new section. **Resolved v136:** added "Session handoff" section to session-protocol.md between Session middle and Session close.

### Workflow gaps (from Sub-agent C)

- [x] **G11. Build recap step.** Plugin (close.md P5): [BRIEF] recap summarizing changes shipped, Claude-verified results, manual-check requests. Dev close has no recap step — the build-log entry captures the narrative but there's no user-facing recap in chat. **Add to:** session-protocol.md implementation close, before the build-log entry step. **Resolved v137:** added as implementation close step 5 (two parts: what shipped, sweep findings). Lighter close skips (no build to recap).

- [x] **G12. End-of-recap flags.** Plugin (close.md P11): consolidated step for stale refs, out-of-scope improvements, UX.md implications, red flags — after frame-correction and staleness sweeps. Dev side partially covers these (stale refs in frame-correction, ideas in idea sweep) but has no consolidated flags step. **Add to:** session-protocol.md implementation close — fold into existing steps or add explicitly. **Resolved v137:** added as implementation close step 8 (stale refs not fixable, out-of-scope improvements, red flags). Lighter close skips (surface findings in idea sweep if conditional sweeps ran).

- [x] **G13. Lighter close — build-log entry.** Plugin lighter close has NO build-log entry step. Dev lighter close (DL2) always writes one. **Note:** this is a gap on the *plugin* side — dev is more complete here. Flag for plugin close.md update. **Resolved v139:** added as lighter close step 2 — narrative sections only (no Performance section for non-build sessions).

- [x] **G14. Lighter close — footer bump.** Plugin lighter close has no footer-bump step. Dev lighter close (DL4) includes it conditionally. **Note:** another plugin-side gap. Flag for plugin close.md update. **Resolved v139:** added as lighter close step 4 — conditional on substantive method/plugin changes.

- [x] **G15. Lighter close — pre-commit checkpoint.** Plugin lighter close has no checkpoint. Dev lighter close (DL6) has a 6-item checkpoint. **Note:** plugin-side gap. Flag for plugin close.md update. **Resolved v139:** added as lighter close step 6 — 8-item checkpoint covering idea sweep, build-log, conditional sweeps, footers, proxies, batch removal.

- [x] **G16. Lighter close — conditional frame-correction sweep.** Plugin lighter close has no frame-correction. Dev lighter close (DL-conditional) includes it when a batch was consumed. **Note:** plugin-side gap. Flag for plugin close.md update. **Resolved v139:** added as conditional step — fires when session consumed a batch. Also added staleness sweep and lost-feature check as companion conditionals, matching dev-side lighter close.

### Structure/terminology gaps (from Sub-agent B)

- [x] **G17. INVENTORY.md entry shape.** Dev has `Dev/INVENTORY.md` as its MANIFEST-equivalent but session-reference.md defines no entry shape for it. **Add to:** session-reference.md. **Resolved v138:** INVENTORY entry shape added to session-reference.md.

- [x] **G18. Research folder shape.** Dev uses `Dev/Resources/research/` but session-reference.md has no structural spec (naming, persistence, maintenance rules). **Add to:** session-reference.md. **Resolved v138:** Research folder file shape added to session-reference.md.

- [x] **G19. Proxy file spec.** Dev uses `Dev/Planning/.proxies/` (per CLAUDE.md) but session-reference.md defines no format, structure, or regeneration rules. **Add to:** session-reference.md. **Resolved v138:** Dev-side proxy file spec added to session-reference.md.

- [x] **G20. Test sessions index.** Dev has test-log files but no defined index format linking them from BACKLOG or elsewhere. **Add to:** session-reference.md. **Resolved v138:** Test sessions index shape added to session-reference.md.

- [x] **G21. Ideas section shape.** Dev BACKLOG has an Ideas section but session-reference.md defines no entry format. **Add to:** session-reference.md. **Resolved v138:** Ideas section entry shape added to session-reference.md.

- [x] **G22. Staleness sweep (literal path check).** Plugin (VOCABULARY): after-build check scanning BACKLOG for literal references to changed file paths/names. Dev has frame-correction (semantic) but not literal-string path scanning. **Add to:** session-protocol.md implementation close. **Resolved v137:** added as implementation close step 3 (grep BACKLOG queued/parked batches for old names/paths, fix in commit). Lighter close: conditional — runs when a batch was consumed.

- [x] **G23. Lost-feature check.** Plugin (VOCABULARY): after-build check for parked batches whose parking conditions were just met. Dev has parked batches but no check. **Add to:** session-protocol.md implementation close. **Resolved v137:** added as implementation close step 4 (scan parked batches, surface candidates, ask about unparking). Lighter close: conditional — runs when a batch was consumed.

- [x] **G24. OQ staleness detection.** Plugin (VOCABULARY): flag OQs with Surfaced tags older than 20 sessions. Dev tracks Surfaced tags but doesn't check for staleness. **Add to:** session-protocol.md session-open state summary. **Resolved v137:** added OQ staleness detection rule to session-open step 5 (flag OQs with Surfaced tag 20+ sessions old, nudge toward deliberation).

---

## Dev-only — preserve

Dev-side rules with no plugin equivalent that are genuinely worth keeping. Most are legitimately dev-specific (project orientation, versioning, E2E workflow, multi-layer disambiguation). Review whether any should flow to the plugin.

---

### Project orientation and disambiguation (not candidates for plugin flow)

- CM-01. Read this first — session lifecycle delegation to session-protocol.md
- CM-02. Read BACKLOG.md in full at session open
- CM-04. At session close, update Current state section in CLAUDE.md
- CM-05. Design constraints behind every decision (hooks enforce mechanically, etc.)
- CM-06. What this project is / repo structure
- CM-07. Main goal — desktop app, not CLI
- CM-08. Three files named CLAUDE.md — disambiguation
- CM-09. "Claude did X in Taskflow" — not a request to patch Taskflow
- CM-10. Plugin management questions — read Reference manual first
- CM-11. Dev-side vs plugin-side — mandatory disambiguation prefix
- CM-12. Dev-side convergence strategy — bidirectional exchange
- CM-13. Use absolute paths for sovereign-implementer lookups
- CM-14. Dev-project marker file (.no-code-method-skip)
- CM-15. E2E test sessions — workflow and plugin reinstall
- CM-16. Taskflowapp as E2E test reference
- SP-13. SP supersedes CM (conflict-resolution rule between dev-side files)

### Dev-specific session lifecycle (not candidates for plugin flow)

- SP-01. One session = one commit + one tag
- SP-02. Three numbers to keep distinct (session tag, method version, batch number)
- SP-03. Session open — 5-step protocol
- SP-04. Batch-input check at session open
- SP-07. Session middle — three shapes (Implementation, Doc-only, Planning)

### Dev-specific close and audit procedures (review for plugin flow)

- SP-08. Implementation close — full 11-step procedure. *Plugin close.md is the equivalent but thinner on lighter-close path (see G13-G16).*
- SP-09. Lighter close — 9-step procedure. *Plugin lighter close is notably thinner — see G13-G16.*
- SP-10. Doc-code parity — 6-item audit (Vocabulary, Mechanisms, Templates, Inventory, Reference manual, Ghost references). *Plugin close uses narrower grep-based parity. Dev version is broader because plugin development touches more doc surfaces.*
- SP-11. Guide parity (crash-course) — `data-source` and `data-transform` attribute chain. *Dev-specific but the three-layer chain pattern could inform consumer project guide maintenance.*
- SP-12. Batch-ordering audit — 4 checks (forward-dependency, stale-reference, reorder, fix scope). *Could flow to plugin planning.md if consumer BACKLOGs grow deep enough to warrant it.*
- SP-14. Pre-commit checkpoint — named artifact verification. *Plugin has its own checkpoint; dev's is tuned to dev artifacts.*
- SP-15. Frame-correction sweep as standalone step. *Plugin close.md has this (P8); alignment confirmed by Sub-agent C.*

### Dev-side reference material (not candidates for plugin flow)

- Footer bumps list (session-reference) — dev maintenance artifact
- Planning artefacts table (session-reference) — lifecycle summary of dev files
- Opener routing table with load/skip/shape/close columns

---

## Aligned — no action needed (23 items)

### Rules (11)
1. Push back rather than agreeing
2. Plain language over jargon
3. Flag out-of-scope improvements
4. Ask rather than guess on ambiguity
5. Verify external facts, filing mandatory
6. Route information to artifacts, not memory
7. Read proxies first, dip for detail
8. Engage with pushback, don't collapse
9. Walkthroughs one step at a time; alternatives all at once
10. Do not add features not in current batch
11. Response-shape tags ([SILENT], [BRIEF], [SEQUENCE], [DISCUSS], [PROMPT])

### Structure/terminology (6)
12. planning/drafts folder — same concept, same lifecycle
13. Inputs line — same field, same meaning
14. Open question — same concept (dev adds Working notes + graduation paths — minor, see C16)
15. Planning session term — same meaning, same disambiguation from plan mode
16. Pass / Fail / Skipped — same TEST-LOG status values
17. Ideation session — same term, same meaning

### Workflow (6)
18. Build-log entry creation — same action, different paths/index names (structural)
19. Frame-correction sweep — same concept, same application point
20. Idea sweep with routing — same triage destinations
21. Turn boundary (judgment → mechanical) — same two-turn structure
22. Proxy regeneration — same step
23. Row pruning — same concept, different enforcement

---

## Plugin-only — expected (~55 items)

Structural absences where the dev side deliberately lacks hooks, skills, locks, consumer-only mechanics, or `_method/` paths. No action needed.

**Consumer CLAUDE.md features:** Product overview section, Language field.
**Consumer docs:** UX.md structure, Additional source-of-truth docs, Proposed edits pending sections, `[SECURITY]` marker.
**Consumer BACKLOG features:** Planning batches (tied to phase-locked editing), Red flags section, Build-snapshot architecture, Test sessions index format.
**Hook enforcement:** Phase-aware editing (planning/build), footer exception, read-before-edit gate (MANIFEST), test-confirmation gate, unclosed-build commit guard, concurrent-build detection.
**Skill-driven features:** Hook-assisted opener classification, `/sovsetup` cases, `/sovrecap` pre-build sizing, `/sovresearch` query files, `/sovclose` idempotency check, invocation-prompt compact nudge.
**Consumer build-batch features:** Files: sub-section, Changes: delimiter, Serves line, Handoff notes, Close handoff section, [Requested]/[Suggested] labels, Status: line (as explicit keyword), Decisions to make this batch, Red flags sub-section (batch-level).
**Consumer terms without dev equivalent:** Adopted/unadopted folder, source-of-truth doc (as named concept), suggestion vs discovery distinction, proposed edit, `_method/` folder, build recap (ephemeral chat summary), after-build steps, language setting, pre-build verification estimate.

---

## Observations for reconciliation planning

**1. The aligned count (23) is encouraging.** The rules surface is largely converged — 11 of ~20 behavioural rules match. The conceptual foundation is shared; the gaps are at the operational level.

**2. The 24 gaps cluster into three natural batches:**
- **Rules batch** (G01-G10): prose equivalents of plugin behavioural rules. All go into session-protocol.md or CLAUDE.md. Could be one session.
- **Workflow batch** (G11-G16): close-procedure additions. G13-G16 are *plugin-side* gaps (lighter close is too thin) — flag for a plugin batch. G11-G12 are dev-side additions. Could be one session.
- **Structure batch** (G17-G24): entry shapes and terms in session-reference.md. Straightforward documentation. Could be one session.

**3. Four items flow to the plugin, not the dev side.** G13 (lighter close build-log), G14 (lighter close footer bump), G15 (lighter close checkpoint), G16 (lighter close frame-correction) are all cases where the dev side is MORE complete than the plugin. These should become a plugin close.md update batch.

**4. The 18 contradictions mostly don't need convergence.** Many are documented as deliberate (C06, C07, C09) or structural (C17). The ones needing real decisions: C03 (flag taxonomy — add red-flag routing), C04 (command execution — clarify context), C05 (TEST-LOG columns — confirm intentional), C14 (batch lifecycle — choose a model).

**5. The 28 dev-only preserve items are stable.** All are legitimately dev-specific. SP-11 (guide parity) and SP-12 (batch-ordering audit) are the only candidates for flowing to the plugin, and only if consumer projects reach sufficient complexity.

# Dev-side structure mirroring audit — v125

Input: `dev-side-reader-test-findings.md` (0121 gap list). Plugin-side docs at v124 HEAD. Dev-side docs at v124 HEAD.

Approach: for each plugin-side pattern, assess whether the dev-side equivalent is weaker, missing, or intentionally different. Verdict: **adopt**, **skip** (with reason), or **new batch** (scoped separately).

---

## Pattern assessments

### 1. Batch scope structure

**Plugin-side.** Five scope-context sections (Goal, Outputs, Success criteria, Decisions, Dependencies) + optional Red flags. Then Changes:, Inputs:, Files:, Tests:, Serves:.

**Dev-side.** BACKLOG queued batches use Goal, Inputs, Outputs, Success criteria, Risks/dependencies. No Changes:/Files:/Tests:/Serves:.

**Verdict: adopt Approach field; skip the rest.** Dev-side benefits from an Approach field (between Goal and Inputs) because there's no build procedure to infer "how." Plugin-side doesn't need Approach because the build procedure handles it. Changes:/Files:/Tests:/Serves: don't map to dev-side work — no source-of-truth docs, no file lists, no test rows at planning time. The combined Risks/dependencies field works for dev-side where dependencies are simpler (other batches) and red flags don't apply (no consumer-facing security surface).

### 2. BACKLOG sections

**Plugin-side BUILD-PLAN has five sections:** Red flags, Planning batches, Build batches, Open questions, Ideas.

**Dev-side BACKLOG has:** Versioning convention, shipped history table, Queued batches, Open questions.

**Verdict: remove history table, add Ideas section, skip Planning batches and Red flags.**

- **History table:** 118 rows, loaded every session, purely historical. Same info lives in build-log/INDEX.md with more detail. Removing saves ~120 lines of context per session. Replace with a one-line pointer.
- **Ideas section:** Lower friction than full OQs. Date + one-liner. Good for "noticed X but it's not worth an OQ yet." Plugin-side proves the pattern works.
- **Planning batches:** Plugin-side separates "blocking questions with `Blocks:` line" from batches. Dev-side OQs already handle this via the "Next step" field ("fold into NNNN if [condition]"). The separation wouldn't add value — dev-side planning is purely prose-based with no hook enforcement.
- **Red flags:** No consumer-facing security surface. Dev-side security concerns (e.g. plugin hook escape paths) are scoped into specific batches already.

### 3. Proxy format

**Plugin-side.** HTML comment header, state summary, entries with L<N> line numbers. Spec in DOC-STRUCTURE.md.

**Dev-side.** HTML comment header (with version tag + usage hint), section-level summaries with L<N> line numbers. No formal spec document.

**Verdict: skip.** Dev-side proxies already follow a comparable pattern with useful extras (v<N> version tag, `when:` usage hint). The format is consistent across all three proxies. Plugin-side needs a formal spec because consumer projects scaffold from templates and hooks validate shapes. Dev-side has no templates or validators — consistency comes from session-to-session convention. The T4 gap (proxy format spec unlocated) was addressed in v121.

### 4. DOC-STRUCTURE equivalent

**Plugin-side.** DOC-STRUCTURE.md defines schemas for every doc type.

**Dev-side.** session-reference.md defines BUILD-LOG entry shape, OQ entry shape, TEST-LOG entry shape. But doesn't define BACKLOG batch scope structure.

**Verdict: add batch scope shape to session-reference.md; skip full schema doc.** A short section documenting the expected batch fields (Goal, Approach, Inputs, Outputs, Success criteria, Risks/dependencies) prevents improvisation and gives new sessions a reference. A full schema doc would be over-engineering — dev-side has one instance of each doc, not templates scaffolded across projects.

### 5. VOCABULARY equivalent

**Plugin-side.** VOCABULARY.md with 40+ defined terms.

**Dev-side.** Terms defined in situ: "session tag" / "method version" / "batch number" in session-protocol.md, entry-type terms in session-reference.md, "dev-side" / "plugin-side" in CLAUDE.md.

**Verdict: skip.** Dev-side has fewer terms and they're all defined where they matter. Plugin-side needs VOCABULARY.md because terms appear across 11 procedure docs, templates, and hook code. Dev-side has 4 docs total. In-situ definitions are sufficient and avoid a maintenance burden.

### 6. Status tracking on batches

**Plugin-side.** `Status:` line (queued/parked/shipped). Parser uses it.

**Dev-side.** Implicit: batches in Queued section = queued; **PARKED** text marker; ~~strikethrough~~ = cancelled; shipped = in history table.

**Verdict: skip.** With the history table removed, the Queued section contains only queued and parked batches. The implicit encoding is clear and doesn't need a formal Status: line — no parser consumes it.

### 7. Session-open state summary template (OQ M6)

**Plugin-side.** SessionStart hook mandates: batch counts, next batch, pending tests, OQ staleness.

**Dev-side.** No template. Claude improvises.

**Verdict: new batch.** A lightweight 3-line template in session-protocol.md would make session opens consistent without adding enforcement. Not complex enough to need a formal hook, but worth documenting the expected shape: queue depth, next batch name, OQ count.

### 8. Step 2 load-purpose annotations (OQ M8)

**Plugin-side.** SessionStart knows what to extract (coded).

**Dev-side.** Step 2 says "read these 4 docs" with no purpose or size notes.

**Verdict: fold into state-summary batch.** Four one-line annotations:
- universal-behaviour.md (~180 lines) — behavioural rules, routing table, editing surfaces
- DOC-STRUCTURE.md (~410 lines) — schema definitions for all consumer-project docs
- VOCABULARY.md (~140 lines) — method term definitions (cross-reference target)
- Reference manual.md (~410 lines) — user-facing narrative (parity reference)

Trivial addition. Bundle with the state-summary template batch.

### 9. Build-snapshot architecture

**Plugin-side.** Extracts active batch to active-build.md; BUILD-PLAN unlocked for parallel work.

**Dev-side.** No equivalent.

**Verdict: skip.** Dev-side has no hooks, no phase detection, no parallel sessions. The architecture exists plugin-side because hooks enforce phase-aware editing and need a build-in-progress signal. Dev-side builds are conversation-level, not file-level. Pure over-engineering.

### 10. Proposed edits pending mechanism

**Plugin-side.** `[PROPOSED EDIT PENDING]` blocks on locked docs during build phase.

**Dev-side.** No equivalent.

**Verdict: skip.** Same reasoning as #9 — no phase-aware editing, no doc locking, no hooks. The mechanism exists to serve the build/planning phase flip, which dev-side doesn't have.

### 11. [SECURITY] marker

**Plugin-side.** Inline tag on entries touching sensitive surfaces.

**Dev-side.** Not used.

**Verdict: skip.** Dev-side batches don't touch consumer-facing security surfaces. Plugin hook escape paths are already scoped into specific batches. If a dev-side batch ever had security implications, the batch scope text would describe them — a marker wouldn't add signal.

---

## 0121 gap list reconciliation

### Addressed in v121–v124

| ID | Gap | Resolved in |
|---|---|---|
| T1 | Blended opener routing | v122 (0125) — priority ordering, sequential threads |
| T2 | Batch removal timing asymmetry | v121 (0124) — both paths now pre-commit |
| T3 | Stale step-number cross-reference | v121 (0124) — step numbers corrected |
| T4 | Proxy format spec unlocated | v121 (0124) — format spec noted |
| T5 | Git-unavailable fallback | v122 (0125) — CLAUDE.md fallback documented |
| M1 | Lighter close step reordering | v124 (0119) — rationale stated in session-protocol.md L137 |
| M5 | Informal opener modifiers | v122 (0125) — "availability context" note added |
| B1 | Duplicate 0102 entry | v121 (0124) — duplicate removed |

### Addressed by assessment this session

| ID | Gap | Disposition |
|---|---|---|
| M3 | Doc-only batch-input check | Routing table now states positive case ("Step 4 if consuming a queued batch"). Clear enough. |
| M9 | Dev/plugin disambiguation in blended openers | Blended-opener rule (L56) handles sequencing: "Resolve routing-critical ambiguity first." |
| B6 | "Lighter close" naming | Minor wording issue. Current text is functional. No action. |

### Still open as OQs (parked — this audit confirms parking)

| ID | OQ title | Reason to keep parked |
|---|---|---|
| M2 | Frame-correction sweep categorical skip | Low frequency — doc-only sessions rarely change frames |
| M4 | Remote-control standby close path | Very low frequency — no standby sessions observed |
| M7 | Sub-agent warning boundary for scoped work | Low friction — unnecessary warning is minor cost |
| B2–B5 | Cross-reference precision (4 issues) | Fix opportunistically when sections are edited |

### Evaluated this session → new batch

| ID | OQ title | Disposition |
|---|---|---|
| M6 | Session-open state summary template | New batch (see § Proposed batches) |
| M8 | Step 2 load-purpose annotations | Folded into same batch as M6 |

---

## Proposed batches

### 0126 — Session-open state summary + step 2 annotations

**Goal.** Add a lightweight session-open state summary template and per-doc purpose annotations to session-protocol.md. Resolves OQs M6 and M8 from the 0121 reader test.

**Approach.** Add a "State summary" paragraph after step 4 in session-protocol.md defining the expected shape (queue depth, next batch, OQ count). Add one-line purpose + size annotations to step 2's doc list. Both are small prose additions.

**Outputs.** session-protocol.md updated. Two OQs removed from BACKLOG.

**Success criteria.** A fresh-session Claude reading session-protocol.md produces a consistent state summary without improvising. Step 2 doc reads are targeted by purpose.

**Risks / dependencies.** None. Trivially small.

### 0127 — Batch scope shape documentation

**Goal.** Document the expected shape of a BACKLOG queued batch entry in session-reference.md, so new sessions writing batches have a reference instead of inferring from examples.

**Approach.** Add a "Queued batch entry shape" section to session-reference.md, parallel to the existing BUILD-LOG, OQ, and TEST-LOG entry shapes. Define the fields: Goal, Approach (optional), Inputs (optional), Outputs, Success criteria, Risks/dependencies (optional).

**Outputs.** session-reference.md updated. Proxy updated.

**Success criteria.** A fresh-session Claude writing a new queued batch produces the expected shape without reading other batches for format inference.

**Risks / dependencies.** Depends on this session's BACKLOG restructure completing (Approach field, Ideas section).

---

## BACKLOG restructure summary (done this session)

1. **History table removed.** 118 shipped/cancelled rows replaced with a one-line pointer to build-log/INDEX.md.
2. **Ideas section added.** After Open questions. Date + one-liner format.
3. **Approach field added.** Optional field in queued batch entries (between Goal and Inputs). Retroactively added to existing queued batches where applicable.
4. **Versioning convention kept.** Still useful for batch numbering.

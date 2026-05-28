# Session protocol — How this project ships

Session lifecycle: open, middle, close. Read every session.

For entry shapes (BUILD-LOG, open questions, TEST-LOG), footer bump lists, testing details, planning artefact lifecycles, and historical context, see `session-reference.md` (same folder — dip when needed, don't load by default).

Personal and collaboration rules live in root `CLAUDE.md`. Anything here supersedes older equivalents there.

---

## The unit of work: a session

**One session = one git commit + one git tag.** Tags are `v17`, `v18`, ... Current: `git describe --tags --abbrev=0` from `sovereign-implementer/`. Pre-V17 lives read-only in `Dev/Resources/Iteration playbook/`.

### Three numbers to keep distinct

Three version-ish numbers move independently:

- **Session tag** (lowercase `v`, e.g. `v52`) — one per session regardless of type. Always increments.
- **Method version** (uppercase `V`, e.g. `V48`) — consumer-facing footer. Only bumps on substantive method/plugin change; planning-only sessions skip.
- **Batch number** (4-digit, e.g. `0050`) — leading number in BACKLOG.md queued batch headings (e.g. `### 0096 — Manifest rationale field`). Allocated at creation, never reused. Used for cross-referencing only.

So `v52` coexisting with `V48` and scope `0050` is correct, not drift. The V21 tripwire compares loaded footers against `PLUGIN_METHOD_VERSION` in `session_start.py`; both stay locked until a method-changing session bumps them together.

**History.** V18–V23 conflated session tag and method version. Going forward they're separated; historical mismatches stay. Scope files prior to 0050 used `V<N>.md`; 0050 renamed to `NNNN-kebab-title.md`. Git history still references old V-numbers; that divergence is permanent.

---

## Session open

In order:

1. `git describe --tags --abbrev=0` — confirm current version.
2. Read `plugin/hooks/universal-behaviour.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `Guides/Reference manual.md` at `HEAD`.
3. Read `Dev/Planning/BACKLOG.md` in full — the *Queued batches* section contains full scope for each upcoming batch, and the *Open questions* section has method-level questions. Both inform session routing.
4. **Batch-input check.** Scan the top queued batch's *Inputs* for out-of-repo references — "Alex has the file locally," "from the previous chat," "see the artefact at [external location]," or any "[X] draft" with no committed path. If found, **halt immediately** — surface the offending line and fix at the source (per `session-reference.md` → *Drafts in flight*) before the session proper starts.
Then classify the opener and route per the **Opener routing table** below. If the task isn't clear, report what was loaded and ask. Don't draft.

---

## Opener routing table

Classify the session opener. Pick the highest-priority match. Openers naming a shape explicitly ("planning session," "doc-only session") are clear — route directly.

| Session type | What to load | What to skip | Session-middle shape | Close path |
|---|---|---|---|---|
| **Implementation** | Full open (steps 1–4). Batch input files per `Inputs:`. | — | Ship plugin code or method-doc structural changes per batch scope. Ends with smoke test + doc-parity. | Full close |
| **Doc-only** | Full open (steps 1–4). | Batch-input check (step 4) if no queued batch is being consumed. | Rewrites without testable code. Terminology, parity catch-up, OQ resolution as prose. | Lighter close |
| **Planning** | Steps 1, 3, 5. Recent build-log entries for context. | Heavy plugin docs (step 2) unless needed for a specific question. | Rescope roadmap: split/merge batches, revise scope, add/resolve OQs. | Lighter close |
| **Ideation** | Steps 1, 3. BACKLOG batches + OQs for gap detection. | Plugin docs (step 2), batch-input check (step 4). | Brainstorm new batches/OQs. Draft scope. No structural changes to existing batches. | Lighter close |
| **E2E test** | Full open (steps 1–4). Consumer project state. Relevant research files. | — | Run plugin against consumer project. Document findings. File to research/. | Lighter close |
| **Remote-control standby** | Step 1 only. | Steps 2–5 until directed. | Wait for instructions. Load on demand. | Depends on work done |

**Skip doesn't mean refuse.** If mid-session the skipped content becomes relevant, load it then.

---

## Session middle

Three shapes, often blended:

**Implementation** — ships plugin code or method-doc structural changes. Ends with smoke test + doc-parity edits in same commit.

**Doc-only** — rewrites without testable code (terminology sweep, parity catch-up, OQ resolution as prose). No smoke test; doc-code parity audit still runs.

**Planning** — rescope the roadmap: split/merge batches, revise queued batch scope in BACKLOG.md, add/resolve open questions. Usually still produces a tagged commit.

Claude's job mid-session: do the work, surface concerns, propose. Close/parity/testing rules apply regardless.

---

## Session close

Two paths based on session type.

### Implementation close (full)

Run when the session shipped plugin code or method-doc structural changes consuming a queued batch.

Response-shape tags mark verbosity per step — definitions in `session-reference.md` → *Response-shape tags*.

1. **[BRIEF] Doc-code parity** (see *Doc-code parity* section below for audit details). Fix docs before footers and BUILD-LOG.

2. **[BRIEF] Frame-correction sweep.** If this session corrected a load-bearing frame — something next-session Claude would absorb wrongly from BACKLOG's queued batches — audit `Dev/Planning/BACKLOG.md` → *Queued batches* for references to the old frame. Fix in this commit. Bar: not "anything changed" but "rewrites how future-Claude should think about [X]."

3. **[SILENT] Bump method-version footers** — only for substantive method/plugin changes. Dev-internal-only sessions skip entirely. Full list in `session-reference.md` → *Footer bumps*.

4. **[SILENT] Build-log entry** — create a new file in `Dev/Planning/build-log/`; shape in `session-reference.md` → *BUILD-LOG entry shape*. Prepend index line to `Dev/Planning/build-log/INDEX.md`.

5. **[BRIEF] Idea sweep with routing.** Review the session for ideas, suggestions, or observations raised but not implemented. Triage each to exactly one destination:
   - **BACKLOG batch** — add a new queued batch entry to BACKLOG.md → *Queued batches*.
   - **BACKLOG open question** — add to BACKLOG.md → *Open questions* with `Surfaced` tag.
   - **Flag in recap** — for user to decide.
   Nothing left unrouted. If no ideas surfaced, skip silently.

6. **[SILENT] Regenerate proxies.** If `Dev/Planning/.proxies/` exists, regenerate any proxy whose source doc was edited this session. Read the source doc, write the proxy per its format spec. Skip if no source docs were edited.

7. **[BRIEF] Pre-commit checkpoint.** Verify each artifact by name:
   - [ ] Doc-code parity done (step 1)
   - [ ] Frame-correction sweep done (step 2)
   - [ ] Footers bumped if applicable (step 3)
   - [ ] Build-log entry written + index line prepended (step 4)
   - [ ] Idea sweep done — nothing unrouted (step 5)
   - [ ] Proxies regenerated (step 6)
   Complete any missing steps now. A missing build-log entry is the most common skip when context runs low — check explicitly.

8. **[PROMPT] Commit** with `v<N>:` message.

9. **[SILENT] Tag** `git tag v<N>`.

10. **[SILENT] Remove this batch from BACKLOG's Queued batches section** as part of the commit.

11. **[PROMPT] Push.** `git push origin main` and `git push origin v<N>`. Pause only for secrets/credentials/personal info.

### Lighter close (planning, doc-only, ideation, E2E test)

Run when the session didn't ship code. Steps that produce no-ops on non-code sessions are skipped explicitly.

1. **[BRIEF] Idea sweep with routing.** Same triage as implementation close step 5: every idea routed to exactly one of BACKLOG batch, BACKLOG open question, or flagged in recap for user. Nothing left unrouted.

2. **[SILENT] Build-log entry** — create a new file in `Dev/Planning/build-log/`; shape in `session-reference.md` → *BUILD-LOG entry shape*. Prepend index line to `Dev/Planning/build-log/INDEX.md`.

3. **[SILENT] Bump method-version footers** — only if this session made substantive method/plugin changes. Most lighter-close sessions skip. Full list in `session-reference.md` → *Footer bumps*.

4. **[SILENT] Regenerate proxies.** Same rule as implementation close step 6. Skip if no source docs were edited.

5. **[BRIEF] Pre-commit checkpoint.** Verify by name:
   - [ ] Build-log entry written + index line prepended (step 2)
   - [ ] Idea sweep done — nothing unrouted (step 1)
   - [ ] Proxies regenerated if applicable (step 4)
   - [ ] Footers bumped if applicable (step 3)
   - [ ] Batch removed from BACKLOG if this session consumed one
   Complete any missing steps now.

6. **[PROMPT] Commit** with `v<N>:` message.

7. **[SILENT] Tag** `git tag v<N>`.

8. **[PROMPT] Push.** `git push origin main` and `git push origin v<N>`. Pause only for secrets/credentials/personal info.

**Skipped explicitly (vs. implementation close):**
- Doc-code parity — no code changes to audit.
- Frame-correction sweep — no feature frame changed.

**Conditional:** If this session consumed a queued batch (e.g. a doc-only batch), remove it from BACKLOG's Queued batches section as part of the commit (lighter close step 5, checkpoint).

---

## Batch-ordering audit

Run as part of any session that adds, removes, or reorders BACKLOG queued batches. Four checks:

1. **Forward-dependency scan.** For each batch, verify its Dependencies resolve to shipped batches or earlier queued batches. Flag violations.
2. **Stale-reference scan.** For each batch that renames/deletes/moves a file or skill, grep later batches for references to the old name. Flag hits.
3. **Reorder if needed.** Propose reordering with one-line justification per move. Apply ordering principles: dependency flow first, then project-structure reasoning, then security bias (`[SECURITY]`-marked batches earlier), then stale-reference avoidance.
4. **Fix scope text.** Update stale references in affected batch scope in the same pass as the reorder.

Skip if no structural changes to BACKLOG were made this session.

---

## Doc-code parity

Plugin code and descriptive docs must stay aligned. When a session ships code introducing a new concept, mechanism, section, marker, location, or rule, the same session updates the docs. Don't ship code the docs don't describe; don't leave docs describing what code no longer does.

Catching a gap in the session that created it is cheap. Three sessions later it's expensive.

**During the session.** As code depends on something in the docs — a hook deny message naming a section, a skill body pointing at a docs block — check the dependency is documented. If not, the doc update is part of *this* session.

**At session close.** Audit this session's code changes against docs — scoped to what changed:

1. **Vocabulary.** New named concepts defined in `VOCABULARY.md`.
2. **Mechanism descriptions.** If something works differently, `DOC-STRUCTURE.md` and `universal-behaviour.md` describe the new mechanism. Grep every reference to the old — section names, counts, location phrases — and update.
3. **Templates.** New sections, markers, canonical formats → `plugin/templates/`.
4. **Inventory.** New/changed plugin components → `Dev/INVENTORY.md`.
5. **Reference manual.** Load-bearing concept/mechanism changes → `Guides/Reference manual.md` reflects it at narrative altitude.
6. **Ghost references.** Audit for paragraphs asserting state contradicted by `Dev/Planning/build-log/` entries or actual code. On disagreement, build-log wins.

**Escape clause.** If the audit surfaces a gap whose doc work would dominate the session — surface in chat, weigh fold-in vs. new-session, decide together. **Default: fold in now.** Cost is usually overstated; shipping inconsistency is worse.

### Guide parity (Guides/crash-course/)

The HTML crash course at `Guides/crash-course/` derives from `Guides/Reference manual.md`. Three-layer chain: **plugin spec docs → Reference manual → crash-course guide.** Each HTML section carries `data-source` and `data-transform` attributes:

- `data-source="manual:<section-id>"` — source section in the Reference manual.
- `data-transform="verbatim"` — word-for-word; auto-update on manual change.
- `data-transform="adapted"` — same concept, plainer language; flag for review on manual change.
- `data-transform="added"` — new context not in the manual; no update unless the concept is removed.

When a session changes `Guides/Reference manual.md`, grep `Guides/crash-course/` for matching `data-source` values. `verbatim` sections update mechanically; `adapted` sections need review; `added` sections need a judgment call.

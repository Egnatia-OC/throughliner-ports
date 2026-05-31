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
- **Batch number** (4-digit, e.g. `0050`) — leading number in BACKLOG.md queued batch headings (e.g. `### 0096 — Manifest rationale field`). Allocated at creation, never reused. Cross-referencing only.

So `v52` coexisting with `V48` and scope `0050` is correct, not drift. The V21 tripwire compares loaded footers against `PLUGIN_METHOD_VERSION` in `session_start.py`; both stay locked until a method-changing session bumps them together.

**History.** Pre-V24 conflated session tag and method version; pre-0050 scope files used `V<N>.md`. Historical mismatches in git are permanent.

---

## Session open

In order:

1. `git describe --tags --abbrev=0` — confirm current version. If git unavailable or fails, use session tag from *Current state* in this project's `CLAUDE.md`. Flag if stale (e.g. build-log entries clearly newer).
2. Read the following plugin docs at `HEAD`:
   - `plugin/hooks/universal-behaviour.md` — behavioural rules, prohibited behaviours, response-shape tags, routing table (~180 lines).
   - `plugin/docs/DOC-STRUCTURE.md` — structural specs for project docs: entry shapes, section ordering, proxy format (~410 lines).
   - `plugin/docs/VOCABULARY.md` — method term definitions, cross-referenced from other docs (~140 lines).
   - `Guides/Reference manual.md` — install/usage primer and method overview for orientation (~410 lines).
3. Read the BACKLOG: `_method/proxies/backlog.md` (index) for queue overview, then dip into per-batch files at `_method/BACKLOG/` for scope detail. *Open questions* are in the proxy's OQ section. Reading the proxy whole prevents stale-content drift.
4. **Batch-input check.** Scan the top queued batch's *Inputs* for out-of-repo references — "Alex has the file locally," "from the previous chat," "see the artefact at [external location]," or any "[X] draft" with no committed path. These are uncommitted dependencies missing at session start. If found, **halt** — surface the offending line and fix (per `session-reference.md` → *Drafts in flight*) before the session proper starts.
4b. **OQ blocker check.** Scan the top queued batch's scope for references to unresolved open questions or parked ideas that would force mid-session improvisation. If the batch depends on an answer that doesn't exist yet, **halt** — resolve via planning or deliberation before starting the batch.
5. **State summary.** Brief summary: current version (session tag, method version, plugin version), queue depth, next batch (number and title), OQ count, notable conditions (parked batches, stale OQs). One short paragraph — not a dashboard. **OQ staleness detection:** flag any OQ whose `Surfaced` tag is 20+ session-tags old — nudge toward a deliberation session to resolve or re-park.
Then classify the opener and route per the **Opener routing table** below. If the task isn't clear, report what was loaded and ask. Don't draft.

---

## Opener routing table

Classify the session opener. Pick the highest-priority match. Explicit type names ("planning session," "doc-only session") route directly.

| Session type | What to load | What to skip | Session-middle shape | Close path |
|---|---|---|---|---|
| **Implementation** | Full open (steps 1–5). Batch input files per `Inputs:`. | — | Ship plugin code or method-doc structural changes per batch scope. Ends with smoke test + doc-parity. | Full close |
| **Doc-only** | Full open (steps 1–3, 5). Step 4 if consuming a queued batch. | — | Rewrites without testable code. Terminology, parity catch-up, OQ resolution as prose. | Lighter close |
| **Planning** | Steps 1, 3, 5. Recent build-log entries for context. | Heavy plugin docs (step 2) unless needed for a specific question. | Rescope roadmap: split/merge batches, revise scope, add/resolve OQs. | Lighter close |
| **Ideation** | Steps 1, 3, 5. BACKLOG batches + OQs for gap detection. | Plugin docs (step 2), batch-input check (step 4). | Brainstorm new batches/OQs. Draft scope. No structural changes to existing batches. | Lighter close |
| **E2E test** | Full open (steps 1–5). Consumer project state. Relevant research files. | — | Run plugin against consumer project. Document findings. File to research/. | Lighter close |
| **Remote-control standby** | Step 1 only. | Steps 2–5 until directed. | Wait for instructions. Load on demand. | Depends on work done |

**Skip doesn't mean refuse.** If mid-session the skipped content becomes relevant, load it then.

**Blended openers.** When an opener matches multiple types (e.g. "let's plan 0125 and then build it"), primary type by priority: E2E test > Implementation > Planning > Ideation > Doc-only > Remote-control standby. Handle threads sequentially, highest-priority first. If the opener needs disambiguation (e.g. "let's do the next thing"), resolve the routing-critical ambiguity first — ask one question, wait, proceed. Defer non-routing clarifications to mid-session. Informal modifiers ("spare session," "quick one," "I have 10 minutes") are availability context, not session types — route on the substantive direction.

---

## Session middle

Three shapes, often blended:

**Implementation** — ships plugin code or method-doc structural changes. Ends with smoke test + doc-parity edits in same commit.

**Doc-only** — rewrites without testable code (terminology sweep, parity catch-up, OQ resolution as prose). No smoke test; doc-code parity audit still runs.

**Planning** — rescope the roadmap: split/merge batches, revise queued batch scope in BACKLOG.md, add/resolve open questions. Usually still produces a tagged commit.

Claude's job mid-session: do the work, surface concerns, propose. Close/parity/testing rules apply regardless.

### Mid-session rules

- **No stealth fixes.** If a change causes a regression, state plainly what broke and that you're fixing it. Silent fixes corrupt the build-log narrative.

- **No unplanned refactoring.** Stay inside agreed batch scope. Two exceptions: (1) **prerequisite carve-out** — batch can't complete without it; halt, justify, wait for okay; (2) **re-batching carve-out** — verification burden much higher than estimated; halt, propose split, wait.

- **Default to the smallest accommodation.** Propose the minimum-touch fix first. Generalise only when a second project or use case would also benefit.

- **Verify after every edit to long files.** The Edit tool can silently truncate long replacements. After editing a file longer than ~200 lines, read it back to confirm it's whole.

- **Recognise cascading fixes.** When each fix exposes the next inconsistency, name it as a cascade, cap depth before pausing for scope review, and track depth as you proceed.

- **Signpost threads in long work.** Periodically restate which thread you're on and what the new finding is. Drift between threads without signposting is disorienting.

- **Grep after renames immediately.** When a change renames a concept, file, or term, grep for the old name across dev-side docs before moving on — don't wait for the close staleness sweep.

- **Re-read affected queued work after mid-session changes.** When a change shifts a frame or absorbs scope a queued/parked batch depends on, re-read that batch immediately. Mark it as partially superseded with a note on what remains.

- **Propose the wider sweep before applying the first edit.** When a targeted cleanup reveals a broader pattern, stop and propose extending the sweep before applying the first fix.

- **Mid-session compact nudge.** After ~15 exchanges without reaching close, nudge about `/compact`. Informational, not blocking. Don't repeat after acknowledgment.

---

## Session handoff

When context runs low mid-session and the batch can't complete in this session:

1. **Tick completed work.** Every fully-written file or doc section → mark done.
2. **Annotate in-progress items.** Brief note on what's done and what remains.
3. **Record decisions.** Anything decided this session but not yet captured in BACKLOG or build-log → add a `Handoff notes:` block at the bottom of the batch scope in BACKLOG.md.
4. **Tell Alex it's ready.** Name what's done, what's remaining. Next session reads the batch and `Handoff notes:` to resume.

The `Handoff notes:` block is consumed by the next session — remove it once the batch completes.

---

## Session close

Close is mandatory, not advisory. Skipping leaves orphaned state that blocks future sessions. If Alex asks to skip, explain the consequences and decline.

Two paths based on session type. Both split into a **judgment pass** (while session context is fresh) and a **mechanical pass** (after `/compact`). The turn boundary between them is a `[PROMPT]` — recommended, not enforced. Short sessions can close in one turn.

### Implementation close (full)

Run when the session shipped plugin code or method-doc structural changes consuming a queued batch.

Response-shape tags: definitions in `session-reference.md` → *Response-shape tags*.

Use `git diff` to identify what changed — the dev-side equivalent of the plugin's `## Close handoff`. Steps 1–3 draw from this rather than re-exploring.

**Turn 1 — judgment.** Run while build context is fresh.

1. **[BRIEF] Doc-code parity** (see *Doc-code parity* below). Fix docs before the build-log entry.

2. **[BRIEF] Frame-correction sweep.** If this session corrected a load-bearing frame — something next-session Claude would absorb wrongly from BACKLOG's queued batches — audit `_method/BACKLOG/` per-batch files and `_method/proxies/backlog.md` for references to the old frame. Fix in this commit. Bar: not "anything changed" but "rewrites how future-Claude should think about [X]."

3. **[BRIEF if found, SILENT if not] Staleness sweep.** For each renamed, deleted, or moved file this session: grep `_method/BACKLOG/` per-batch files and any parked batches for literal old-name/old-path references. Fix in this commit. Pattern-match level — literal strings, not semantics. Complements step 2 (semantic frame check).

4. **[BRIEF if found, SILENT if not] Lost-feature check.** Scan parked batches for parking conditions just met by this session's work (e.g. "parked until X ships" where X just shipped). Surface candidates and ask about unparking. Skip if no parked batches exist or nothing in this session could satisfy a parking condition.

5. **[BRIEF] Build recap.** Summarize in chat — the ephemeral counterpart of the build-log entry. Two parts:
   - **What shipped.** One bullet per notable change.
   - **Sweep findings.** Anything surfaced by steps 1–4: doc-parity gaps fixed, frame corrections made, staleness fixes, lost-feature candidates.

6. **[SILENT] Build-log entry** — create a new file in `_method/build-log/`; shape in `session-reference.md` → *BUILD-LOG entry shape*. Prepend index line to `_method/proxies/build-log.md`.

7. **[BRIEF] Idea sweep with routing.** Review session for ideas, suggestions, or observations not implemented. Triage each to one destination:
   - **BACKLOG batch** — add to BACKLOG.md → *Queued batches*.
   - **BACKLOG open question** — add to BACKLOG.md → *Open questions* with `Surfaced` tag.
   - **Security/privacy/data-integrity concern** — surface in chat immediately. Route: fold into the current batch if it fits; otherwise add as a `[SECURITY]`-marked batch or OQ. Never silently defer a red flag.
   - **Flag in recap** — for user to decide.
   Nothing left unrouted. If no ideas surfaced, skip silently.

8. **End-of-recap flags.** Consolidate items needing user attention. Surface each before the turn boundary:
   - Stale references not fixable in this commit (from steps 1–3).
   - Out-of-scope improvements noticed during the session.
   - Red-flag concerns (confirm BACKLOG entry written if deferred).
   Nothing left unmentioned. If no flags, skip silently.

9. **[PROMPT] Turn boundary.** Judgment done. State values the mechanical pass needs: session tag (`v<N>`), whether footers need bumping (old → new if so), whether proxies need regeneration. Recommend `/compact` — mechanical pass needs only these values and the script, not build context. Low context pressure → continue directly.

**Turn 2 — mechanical.** Needs only the session tag, version numbers (if bumping), and the script.

10. **[SILENT] Bump method-version footers** — only for substantive method/plugin changes. Dev-internal sessions skip. Run from `sovereign-implementer/`:
   ```
   python Dev/Resources/scripts/bump_version.py <old> <new> --session-tag v<N>
   ```
   Bumps all `*No-code method — Version N.*` footers, `plugin.json` version, and `PLUGIN_METHOD_VERSION` in `session_start.py`. Also regenerates proxy headers and line-number pointers (step 11). Full list: `session-reference.md` → *Footer bumps*.

11. **[SILENT] Regenerate proxies.** Bump script (step 10) handles proxy headers and line-number pointers mechanically. After it runs, review each proxy whose source was edited — update summaries, section descriptions, and entries for structural changes the script can't detect. No source docs edited and no version bump → skip. Without a version bump, run proxies-only:
   ```
   python Dev/Resources/scripts/bump_version.py --session-tag v<N>
   ```

12. **[BRIEF] Pre-commit checkpoint.** Verify each artifact by name:
   - [ ] Doc-code parity done
   - [ ] Frame-correction sweep done
   - [ ] Staleness sweep done
   - [ ] Lost-feature check done
   - [ ] Build recap delivered
   - [ ] Build-log entry written + index line prepended
   - [ ] Idea sweep done — nothing unrouted
   - [ ] End-of-recap flags delivered
   - [ ] Footers bumped if applicable
   - [ ] Proxies regenerated
   - [ ] Consumed batch removed from BACKLOG's Queued batches section
   Complete any missing steps now. A missing build-log entry is the most common skip when context runs low — check explicitly.

13. **[PROMPT] Commit** with `v<N>:` message.

14. **[SILENT] Tag** `git tag v<N>`.

15. **[PROMPT] Push.** `git push origin main` and `git push origin v<N>`. Pause only for secrets/credentials/personal info.

### Lighter close (planning, doc-only, ideation, E2E test)

Run for non-implementation sessions. Steps producing no-ops are skipped explicitly.

**Turn 1 — judgment.** Run while session context is freshest.

1. **[BRIEF] Idea sweep with routing.** Same triage as implementation close step 7. Nothing left unrouted. (First because no parity/frame work precedes it — sweep while context is freshest.)

2. **[SILENT] Build-log entry** — create a new file in `_method/build-log/`; shape in `session-reference.md` → *BUILD-LOG entry shape*. Prepend index line to `_method/proxies/build-log.md`.

3. **[PROMPT] Turn boundary.** Judgment done. State values: session tag (`v<N>`), whether footers need bumping (old → new if so), whether proxies need regeneration. Recommend `/compact` if session was long. Often short enough to continue directly.

**Turn 2 — mechanical.** Needs only the session tag, version numbers (if bumping), and the script.

4. **[SILENT] Bump method-version footers** — only if substantive method/plugin changes. Most lighter-close sessions skip. When bumping:
   ```
   python Dev/Resources/scripts/bump_version.py <old> <new> --session-tag v<N>
   ```

5. **[SILENT] Regenerate proxies.** Same as implementation close step 11. Bump script (step 4) handles headers and line-number pointers; review for content changes. Without a version bump, run proxies-only:
   ```
   python Dev/Resources/scripts/bump_version.py --session-tag v<N>
   ```
   No edits and no bump → skip.

6. **[BRIEF] Pre-commit checkpoint.** Verify by name:
   - [ ] Idea sweep done — nothing unrouted
   - [ ] Build-log entry written + index line prepended
   - [ ] Frame-correction sweep done (if this session consumed a batch)
   - [ ] Staleness sweep done (if this session consumed a batch)
   - [ ] Lost-feature check done (if this session consumed a batch)
   - [ ] Footers bumped if applicable
   - [ ] Proxies regenerated if applicable
   - [ ] Batch removed from BACKLOG if this session consumed one
   Complete any missing steps now.

7. **[PROMPT] Commit** with `v<N>:` message.

8. **[SILENT] Tag** `git tag v<N>`.

9. **[PROMPT] Push.** `git push origin main` and `git push origin v<N>`. Pause only for secrets/credentials/personal info.

**Skipped:** Doc-code parity, build recap, end-of-recap flags (no implementation to audit). **Conditional (batch-consuming sessions only):** frame-correction sweep, staleness sweep, lost-feature check — same definitions as implementation close steps 2–4. If findings surface, route through the idea sweep.

---

## Batch-ordering audit

See `plugin/docs/procedures/planning.md` → *Batch-ordering audit*. Run when any session adds, removes, or reorders BACKLOG queued batches.

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
6. **Ghost references.** Audit for paragraphs asserting state contradicted by `_method/build-log/` entries or actual code. On disagreement, build-log wins.

**Escape clause.** If the audit surfaces a gap whose doc work would dominate the session — surface in chat, weigh fold-in vs. new-session, decide together. **Default: fold in now.** Cost is usually overstated; shipping inconsistency is worse.

### Guide parity (Guides/crash-course/)

The crash course at `Guides/crash-course/` derives from `Guides/Reference manual.md`. Three-layer chain: **plugin spec docs → Reference manual → crash-course guide.** Each HTML section carries `data-source` and `data-transform` attributes:

- `data-source="manual:<section-id>"` — source section in the Reference manual.
- `data-transform="verbatim"` — word-for-word; auto-update on manual change.
- `data-transform="adapted"` — same concept, plainer language; flag for review on manual change.
- `data-transform="added"` — new context not in the manual; no update unless the concept is removed.

When a session changes `Guides/Reference manual.md`, grep `Guides/crash-course/` for matching `data-source` values. `verbatim` sections update mechanically; `adapted` sections need review; `added` sections need a judgment call.

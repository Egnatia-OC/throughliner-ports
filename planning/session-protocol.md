# Session protocol — How this project ships

Session lifecycle: open, middle, close. Read every session.

For entry shapes (BUILD-LOG, open questions, TEST-LOG), footer bump lists, testing details, planning artefact lifecycles, and historical context, see `session-reference.md` (same folder — dip when needed, don't load by default).

Personal and collaboration rules live in root `CLAUDE.md`. Anything here supersedes older equivalents there.

---

## The unit of work: a session

**One session = one git commit + one git tag.** Tags are `v17`, `v18`, ... Current: `git describe --tags --abbrev=0` from `sovereign-implementer/`. Pre-V17 lives read-only in `Archive/`.

### Three numbers to keep distinct

Three version-ish numbers move independently:

- **Session tag** (lowercase `v`, e.g. `v52`) — one per session regardless of type. Always increments.
- **Method version** (uppercase `V`, e.g. `V48`) — consumer-facing footer. Only bumps on substantive method/plugin change; planning-only sessions skip.
- **Scope-file number** (4-digit, e.g. `0050`) — leading number in `planning/scopes/0050-adr-style-numbering.md`. Allocated at creation, never reused. Filename order = creation order; build order lives in BACKLOG.md.

So `v52` coexisting with `V48` and scope `0050` is correct, not drift. The V21 tripwire compares loaded footers against `PLUGIN_METHOD_VERSION` in `session_start.py`; both stay locked until a method-changing session bumps them together.

**History.** V18–V23 conflated session tag and method version. Going forward they're separated; historical mismatches stay. Scope files prior to 0050 used `V<N>.md`; 0050 renamed to `NNNN-kebab-title.md`. Git history still references old V-numbers; that divergence is permanent.

---

## Session open

In order:

1. `git describe --tags --abbrev=0` — confirm current version.
2. Read `plugin/hooks/universal-behaviour.md`, `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`, `Reference manual.md` at `HEAD`. (Repo-root prose set frozen at V39 — read only for prose-spec form, not current rules.)
3. Scan `planning/BACKLOG.md` → *Open questions* for entries whose *Next step* names the current batch.
4. Read the active scope file from `planning/scopes/`. To find it: scan BACKLOG.md's batch list top to bottom, skip `**Shipped**`/`**Parked**` rows, pick the first unmarked. Use absolute paths. If none exists, say so and wait — don't invent a scope.

Then read Alex's opener and route. If the task isn't clear, report what was loaded and ask. Don't draft.

---

## Session middle

Three shapes, often blended:

**Implementation** — ships plugin code or method-doc structural changes. Ends with smoke test + doc-parity edits in same commit.

**Doc-only** — rewrites without testable code (terminology sweep, parity catch-up, OQ resolution as prose). No smoke test; doc-code parity audit still runs.

**Planning** — rescope the roadmap: split/merge batches, write/revise scope files, add/resolve open questions, restructure BACKLOG.md. Usually still produces a tagged commit.

Claude's job mid-session: do the work, surface concerns, propose. Close/parity/testing rules apply regardless.

---

## Session close: 10 steps

1. **Doc-code parity** (see `session-reference.md` → *Doc-code parity* for audit details). Fix docs before footers and BUILD-LOG.

2. **Frame-correction sweep.** If this session corrected a load-bearing frame — something next-session Claude would absorb wrongly from old scope files — audit `planning/scopes/` for references to the old frame. Fix in this commit. Bar: not "anything changed" but "rewrites how future-Claude should think about [X]." Added V29 after its own open hit a pre-V23 frame in the scope file.

3. **Bump method-version footers** — only for substantive method/plugin changes. Dev-internal-only sessions skip entirely. Full list in `session-reference.md` → *Footer bumps*.

4. **Build-log entry** — create a new file in `build-log/`; shape in `session-reference.md` → *BUILD-LOG entry shape*. Prepend index line to `build-log/INDEX.md`.

5. **Sweep ideas raised but not implemented.** Each: add to a future scope file; create new scope file + BACKLOG.md row; note in build-log entry as "not pursued, reason: ..."; or add to BACKLOG.md → *Open questions*.

6. **Pre-commit checkpoint.** Verify steps 1–5 all done. A missing build-log entry is the most common skip when context runs low — check explicitly.

7. **Commit** with `V<N>:` message.

8. **Tag** `git tag v<N>`.

9. **Delete this batch's scope file** as part of the commit. If bash refuses on Windows ACLs, hand-delete via Explorer first.

10. **Push.** `git push origin main` and `git push origin v<N>`. Pause only for secrets/credentials/personal info.

---

## Doc-code parity

Plugin code and descriptive docs must stay aligned. When a session ships code introducing a new concept, mechanism, section, marker, location, or rule, the same session updates the docs. Don't ship code the docs don't describe; don't leave docs describing what code no longer does.

Catching a gap in the session that created it is cheap. Three sessions later it's expensive.

**During the session.** As code depends on something in the docs — a hook deny message naming a section, a skill body pointing at a docs block — check the dependency is documented. If not, the doc update is part of *this* session.

**At session close.** Audit this session's code changes against docs — scoped to what changed:

1. **Vocabulary.** New named concepts defined in `VOCABULARY.md`.
2. **Mechanism descriptions.** If something works differently, `DOC-STRUCTURE.md` and `universal-behaviour.md` describe the new mechanism. Grep every reference to the old — section names, counts, location phrases — and update.
3. **Templates.** New sections, markers, canonical formats → `plugin/templates/`. (Repo-root `templates/` frozen at V39.)
4. **Inventory.** New/changed plugin components → `planning/INVENTORY.md`.
5. **Reference manual.** Load-bearing concept/mechanism changes → `Reference manual.md` reflects it at narrative altitude.
6. **Ghost references.** Audit for paragraphs asserting state contradicted by `build-log/` entries or actual code. On disagreement, build-log wins.

**Escape clause.** If the audit surfaces a gap whose doc work would dominate the session — surface in chat, weigh fold-in vs. new-session, decide together. **Default: fold in now.** Cost is usually overstated; shipping inconsistency is worse.

### Guide parity (crash-course/)

The HTML crash course at `crash-course/` derives from `Reference manual.md`. Three-layer chain: **plugin spec docs → Reference manual → crash-course guide.** Each HTML section carries `data-source` and `data-transform` attributes:

- `data-source="manual:<section-id>"` — source section in the Reference manual.
- `data-transform="verbatim"` — word-for-word; auto-update on manual change.
- `data-transform="adapted"` — same concept, plainer language; flag for review on manual change.
- `data-transform="added"` — new context not in the manual; no update unless the concept is removed.

When a session changes `Reference manual.md`, grep `crash-course/` for matching `data-source` values. `verbatim` sections update mechanically; `adapted` sections need review; `added` sections need a judgment call.

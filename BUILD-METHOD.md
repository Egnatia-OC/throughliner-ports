# BUILD-METHOD.md — How this project ships

Session open, middle, close, testing, artefact locations. Sibling of `build-log/` (what shipped) and `planning/BACKLOG.md` (what's coming).

This is **not** the no-code method itself — that's what this project produces (`plugin/`, `Reference manual.md`, etc.). Personal and collaboration rules live in root `CLAUDE.md`. Anything here supersedes older equivalents there.

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

1. **Doc-code parity** (audit below). Fix docs before footers and BUILD-LOG.

2. **Frame-correction sweep.** If this session corrected a load-bearing frame — something next-session Claude would absorb wrongly from old scope files — audit `planning/scopes/` for references to the old frame. Fix in this commit. Bar: not "anything changed" but "rewrites how future-Claude should think about [X]." Added V29 after its own open hit a pre-V23 frame in the scope file.

3. **Bump method-version footers** — only for substantive method/plugin changes. Dev-internal-only sessions skip entirely. Full list in *Footer bumps* below.

4. **Build-log entry** — create a new file in `build-log/`; shape in *BUILD-LOG entry shape*. Prepend index line to `build-log/INDEX.md`.

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

---

## Two-write rule for canonical docs

> **SHELVED in v40.** Repo-root docs-only set (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/`) frozen at V39. All substantive changes now land plugin-side only. Section retained for resume-ability. Background: `planning/BACKLOG.md` → *Open questions* entry and BUILD-LOG v40.

V32 split canonical content into two parallel sets: **plugin-side** (operational — `plugin/docs/`, `plugin/hooks/universal-behaviour.md`, `plugin/templates/`, agent bodies) and **docs-only** (project-agnostic prose at repo root). Plugin is the leader; docs-only follows. Cross-references legitimately diverge (plugin-side → plugin homes; docs-only → sibling sections). Substance stays identical.

`Reference manual.md` is plugin-side only — not in the docs-only set.

### Don't propose re-coupling

Don't reintroduce "subagents read NO-CODE-METHOD.md at runtime." The two-write discipline is the intended parity defence, not runtime coupling.

---

## Testing

Testing means **smoke-testing in Claude Code** — install the plugin via local marketplace, run a desktop-app burner session against a scratch directory or Taskflow. This *is* live testing. Hooks fire; slash commands appear; procedure docs load; SessionStart injects `additionalContext`; PreToolUse denies with reason text; `/setup` scaffolds templates. V18/V19/V21/V22 each shipped with smoke tests. Outcomes → `test-log/`.

**Pre-install options:**

- **Local marketplace install.** `/plugin marketplace add` + `/plugin install`, then test in burner session. Highest fidelity. Standard for testable code. `/reload-plugins` picks up edits.
- **Hook direct invocation.** `echo '{"cwd": "/path", "session_id": "test"}' | python plugin/hooks/session_start.py`. Validates parsing + stdout shape pre-smoke-test.
- **Parser CLI.** `python plugin/scripts/parse_backlog.py <BACKLOG.md path>` — inspect output.
- **Code review.** Read and reason. Catches structural errors; misses runtime issues.

**What we don't do:**

- **No public marketplace.** Plugin installed locally via `/plugin marketplace add`. Public distribution is later.
- **No CI.** Pytest runs locally; smoke tests are hand-run by Alex on Windows.

**Where outcomes go.** Each check → a per-session file in `test-log/`. Build-log entries reference the TEST-LOG row range ("see TEST-LOG #045-052") rather than restating.

**Pitfall.** "Live install + back-test" as single-session deliverable keeps resurfacing. Don't conflate a smoke test (does it work?) with a release test (does the published package install?).

### Automated test suite (V53 — pytest)

Pytest suite at `tests/`, run from `sovereign-implementer/`:

```
python -m pytest tests/ -v
```

**Coverage:**
- **Hook subprocess tests** — pipe synthetic JSON into each hook, assert on exit code + stdout shape. Tests every deny path (adoption gate, project-boundary, locked-doc, serves-line, batch boundary, read-before-edit, test-confirmation gate, git guard) and every allow path.
- **Unit tests** — import shared helpers directly: footer detection, path-block parsing, tier classification, adopt-case detection, TEST-LOG row parsing, BACKLOG parsing (single-file and folder mode), CLI invocation.

**Fixtures** at `tests/fixtures/` — synthetic project directories covering every tier.

**Shared helpers** in `tests/conftest.py`: `run_hook()`, `run_script()`, `fixture_path()`, plus pytest fixtures for each test directory.

**Relationship to smoke tests.** Pytest validates parsing, deny/allow logic, stdout shape — everything without a running Claude Code session. Smoke tests remain authority for "does Claude Code actually fire the hook." Complementary: suite catches regressions fast; smoke tests catch wiring.

**When to run.** Before committing any hook script or shared helper change. Runs in under 5 seconds.

---

## Footer bumps: the full list

When a session substantively changes the method/plugin, every method-side `*No-code method — Version N.*` footer bumps. **Dev-internal-only sessions skip entirely.**

Method-side = describes how the consumer method works. Dev-internal files (`build-log/`, `test-log/`, `BACKLOG.md`, this file) don't carry the footer.

### Plugin-side (the leader)

- `plugin/docs/DOC-STRUCTURE.md`
- `plugin/docs/VOCABULARY.md`
- `plugin/hooks/universal-behaviour.md`
- `plugin/templates/CLAUDE-TEMPLATE.md`
- `plugin/templates/UX-TEMPLATE.md`
- `plugin/templates/BACKLOG-TEMPLATE.md` (legacy single-file)
- `plugin/templates/.proxies/backlog.md`
- `plugin/templates/.proxies/build-log.md`
- `plugin/templates/.proxies/test-log.md`
- `plugin/templates/MANIFEST-TEMPLATE.md`
- `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`
- Every footer-carrying subagent under `plugin/agents/`
- `Reference manual.md` (repo root, but plugin-side)

### Docs-only side — SHELVED in v40

> Frozen at V39. Retain V39 footer in perpetuity. Do not bump.

- `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md` (repo root)
- `templates/` (all seven files)

### Cross-cutting

- `planning/INVENTORY.md` — carries the footer for sync, even though dev-internal.

### New files added this session

Add new method-describing files to the right column above as part of the session creating them.

### Version trackers

- `plugin/.claude-plugin/plugin.json` — `version` → `0.<N>.0`
- `plugin/hooks/session_start.py` — `PLUGIN_METHOD_VERSION` → `N`

V21's smoke test caught a footer miss via the SessionStart tripwire. The two-location rule is easy to miss; the tripwire backstops it.

**`universal-behaviour.md` carries a longer signature paragraph instead of the standard footer** — listed in the bump list because its substance is method-canonical and must move in lockstep.

---

## Planning artefacts

| File | Lifecycle | Deleted when |
|---|---|---|
| `planning/scopes/NNNN-kebab-title.md` | **Transient.** Scope for one batch. Once shipped, commit + code + docs are source of truth. | Batch ships (step 9). |
| `planning/drafts/<topic>.md` | **Transient.** Substantive content a future session might start from. Committed when "good enough to walk away from." | Consumed (folded into spec/scope/persistent location). Dead-ends pruned with BUILD-LOG note. |
| `planning/INVENTORY.md` | **Living.** Current plugin architecture. | Never. |
| `planning/BACKLOG.md` | **Living.** Rolling roadmap + open questions. | Never. |
| `planning/*.md` (feasibility docs) | **Historical.** V17 architectural decisions. | Never. |
| `build-log/` | **Historical.** One file per session, INDEX.md newest first. | Never. |
| `test-log/` | **Living.** One file per session, one row per check. Status may flip. | Rows for removed components pruned by planning subagent (V53). |
| `BUILD-METHOD.md` (this file) | **Living.** Working manual. | Never. |

### Drafts in flight

`planning/drafts/<topic>.md` is where substantive chat content lands as soon as a future session might start from it. Committed in the drafting session's commit; "good enough to walk away from" is the bar. Deleted when consumed. Dead-end drafts: prune with BUILD-LOG note.

**Corollary.** If a scope file's *Inputs* names content not reachable from the committed repo ("Alex has the file locally," "from the previous chat," etc.) — that's a bug. Get the content into `planning/drafts/` retroactively or restate as something the next session can rebuild from repo contents. The session-open scan in `CLAUDE.md` catches the reading side; this catches the writing side.

---

## BUILD-LOG entry shape

`build-log/` is the running record of decisions, changes, and reasoning. `INDEX.md` lists entries newest-first. It exists so Alex can talk progress without making people read commits, and so future sessions can reconstruct *why*.

One file per session in `build-log/`, named `vNN-slug.md`:

```markdown
# V<N> — YYYY-MM-DD — One-line summary

**What shipped.** Short paragraph: concrete deliverables, files added/changed, components installed, smoke-test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions. Skip housekeeping.

**Pivots and surprises.** What differed from scope expectations.

**Carried forward.** Items raised but not done, with destination.
```

After writing the file, prepend an index line to `build-log/INDEX.md`:
`- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — One-line summary`

**Note:** Consumer build-log entries carry an additional `## Performance` section — see `DOC-STRUCTURE.md`. This dev build-log doesn't use it.

Don't pad. Half a page is good; shorter is better.

---

## Open-questions entry shape

Open questions live in `planning/BACKLOG.md` → *Open questions* section. Parking lot for method-level questions not yet batch-ready.

Each entry:

```markdown
### One-line question title

**Surfaced.** vNN.

**The question.** Clear framing paragraph.

**Why it matters.** Who raised it, what assumptions it breaks.

**Working notes.** Optional. Rough shapes, alternatives weighed.

**Next step.** Where this is going — "fold into NNNN if [condition]", "promote after NNNN ships", "decide by [date]", or "park". Every entry has one.
```

Newest first.

### Graduation paths

Four ways an entry leaves:

1. **Folded into a batch.** *Next step* names a condition; session-open scan (step 3) matches it; question becomes part of that batch's scope. Entry removed at session close.

2. **Promoted to its own batch.** New BACKLOG.md row + scope file created. Entry removed at promotion (not at the batch's ship — the entry's role is over once a scope file exists).

3. **Partial fold-in.** Batch addresses one shape, others stay parked. Entry stays with a date-tagged update note. *Next step* revised to reflect what's still open.

4. **Dropped.** No longer relevant. One-line reason in build-log; entry removed.

The session-open scan is what makes graduation triggers fire.

---

## TEST-LOG entry shape

`test-log/` is the smoke-test record. One file per session, named `vNN-slug.md`. One row per check:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID. Never reused. |
| **Date** | YYYY-MM-DD. |
| **Session** | Session tag. |
| **Test** | What was checked, one sentence. Specific enough to re-run. |
| **Component** | Plugin component(s) exercised. |
| **Status** | `Pass`, `Fail`, or `Skipped` (reason in Notes). |
| **Notes** | Observations, surprises, skip reason. Keep tight. |

**When to add.** During/after the smoke test, while fresh.

**Status flips.** Previously-Pass now Fails: *append a new row* with same Test, today's session, `Fail` — don't edit the old. Same in reverse. Row-per-event keeps history intact.

**Component changes.** Old row → `Superseded` with note pointing at the changing session. New rows record the retest. Only when the test description itself no longer makes sense.

**BUILD-LOG linking.** Each build-log entry names the TEST-LOG row range in *What shipped*. Prose in build-log; per-check in test-log. Don't duplicate.

---

## Plugin migration context

From V17, this project distributes the method's rules across Claude Code plugin components (hooks, subagents, skills, slash commands) so adherence becomes structural rather than prompt-based. Design and roadmap: `planning/INVENTORY.md`, `planning/BACKLOG.md`, `planning/claude-code-plugin-feasibility-response.md`.

Context for working in the project, not a procedural rule.

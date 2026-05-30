# Session reference — Entry shapes, lists, and historical context

Companion to `session-protocol.md`. Dip into sections as needed — don't load the whole file at session open.

---

## Two-write rule for canonical docs — RETIRED

> Deleted v95. All method content lives plugin-side only. Context: build-log v32, v40, v95.

---

## Testing

Testing means **smoke-testing in Claude Code** — install the plugin via local marketplace, run a desktop-app burner session against a scratch directory or Taskflow. Outcomes → `Dev/Planning/test-log/`.

**Pre-install options:**

- **Local marketplace install.** `/plugin marketplace add` + `/plugin install`, then burner session. Highest fidelity. `/reload-plugins` picks up edits.
- **Hook direct invocation.** `echo '{"cwd": "/path", "session_id": "test"}' | python plugin/hooks/session_start.py`. Validates parsing + stdout shape.
- **Parser CLI.** `python plugin/scripts/parse_backlog.py <BACKLOG.md path>`.
- **Code review.** Read and reason. Catches structural errors; misses runtime issues.

No CI — pytest runs locally; smoke tests hand-run by Alex on Windows. Build-log entries reference TEST-LOG row ranges, not restatements.

**Pitfall.** Don't conflate smoke tests (does it work?) with release tests (does the published package install?).

### Automated test suite (V53 — pytest)

Pytest suite at `Dev/Resources/tests/`, run from `sovereign-implementer/`:

```
python -m pytest Dev/Resources/tests/ -v
```

**Coverage:**
- **Hook subprocess tests** — pipe synthetic JSON into each hook, assert on exit code + stdout shape. Tests every deny path (adoption gate, project-boundary, locked-doc, serves-line, batch boundary, read-before-edit, test-confirmation gate, git guard) and every allow path.
- **Unit tests** — import shared helpers directly: footer detection, path-block parsing, tier classification, adopt-case detection, TEST-LOG row parsing, BACKLOG parsing (single-file and folder mode), CLI invocation.

**Fixtures** at `Dev/Resources/tests/fixtures/` — synthetic project directories covering every tier.

**Shared helpers** in `Dev/Resources/tests/conftest.py`: `run_hook()`, `run_script()`, `fixture_path()`, plus pytest fixtures for each test directory.

**Relationship to smoke tests.** Pytest validates parsing, deny/allow logic, stdout shape — everything without a running session. Smoke tests remain authority for "does Claude Code actually fire the hook." Complementary: suite catches regressions fast; smoke tests catch wiring.

**When to run.** Before committing any hook script or shared helper change. Runs in under 5 seconds.

---

## Response-shape tags

Five tags mark verbosity on close steps and procedures. Same definitions as plugin-side `universal-behaviour.md` § *Response-shape tags*.

- **[SILENT]** — No narration. One sentence max if unavoidable.
- **[BRIEF]** — 1–3 sentences or a tight list.
- **[SEQUENCE]** — Series of prompts, one at a time. State count, ask first, wait.
- **[DISCUSS]** — Full reasoning. Ask, weigh, push back.
- **[PROMPT]** — End with a clear next-action for the user. Hard requirement.

Tags compose freely. Genuine tension (e.g. `[SILENT, PROMPT]`) is a doc bug — flag it.

---

## Footer bumps: the full list

When a session substantively changes the method/plugin, every method-side `*No-code method — Version N.*` footer bumps. **Dev-internal sessions skip.**

Method-side = describes how the consumer method works. Dev-internal files (`Dev/Planning/build-log/`, `Dev/Planning/test-log/`, `BACKLOG.md`, these session files) don't carry the footer.

### Plugin-side (the leader)

- `plugin/docs/DOC-STRUCTURE.md`
- `plugin/docs/VOCABULARY.md`
- `plugin/hooks/universal-behaviour.md`
- `plugin/templates/CLAUDE-TEMPLATE.md`
- `plugin/templates/UX-TEMPLATE.md`
- `plugin/templates/BACKLOG-TEMPLATE.md` (legacy single-file)
- `plugin/templates/.proxies/backlog.md`
- `plugin/templates/.proxies/build-log.md`
- `plugin/templates/MANIFEST-TEMPLATE.md`
- `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`
- `plugin/docs/procedures/*.md` (all 11 procedure docs)
- `Guides/Reference manual.md` (plugin-side)

### Cross-cutting

- `Dev/INVENTORY.md` — carries the footer for sync, even though dev-internal.

### New files added this session

Add new method-describing files to the list above when creating them.

### Version trackers

- `plugin/.claude-plugin/plugin.json` — `version` → `0.<N>.0`
- `plugin/hooks/session_start.py` — `PLUGIN_METHOD_VERSION` → `N`

V21's smoke test caught a footer miss via the SessionStart tripwire. The two-location rule is easy to miss; the tripwire backstops it.

**`universal-behaviour.md` carries a longer signature paragraph instead of the standard footer** — listed in the bump list because its substance is method-canonical and must move in lockstep.

---

## Planning artefacts

| File | Lifecycle | Deleted when |
|---|---|---|
| `Dev/Planning/BACKLOG.md` → *Queued batches* entries | **Transient.** Full scope per batch. Removed at close when shipped — commit + code + docs are source of truth. | Batch ships (session close). |
| `Dev/drafts/<topic>.md` | **Transient.** Substantive content a future session might start from. Committed when "good enough to walk away from." | Consumed (folded into spec/scope/persistent location). Dead-ends pruned with BUILD-LOG note. |
| `Dev/INVENTORY.md` | **Living.** Current plugin architecture. | Never. |
| `Dev/Planning/BACKLOG.md` | **Living.** Rolling roadmap + open questions. | Never. |
| `Dev/Planning/build-log/` | **Historical.** One file per session, INDEX.md newest first. | Never. |
| `Dev/Planning/test-log/` | **Living.** One file per session, one row per check. Status may flip. | Rows for removed components pruned by planning subagent (V53). |
| `Dev/session-protocol.md` | **Living.** Session lifecycle — always read. | Never. |
| `Dev/session-reference.md` (this file) | **Living.** Entry shapes, lists, historical — dip on demand. | Never. |

### Drafts in flight

`Dev/drafts/<topic>.md` is where substantive chat content lands as soon as a future session might start from it. Committed in the drafting session's commit; "good enough to walk away from" is the bar. Deleted when consumed. Dead-end drafts: prune with BUILD-LOG note.

**Corollary.** If a batch's *Inputs* names content unreachable from the committed repo ("Alex has the file locally," "from the previous chat," etc.) — that's a bug. Get it into `Dev/drafts/` retroactively or restate as something rebuildable from repo contents. Session-open scan catches the reading side; this catches the writing side.

---

## BUILD-LOG entry shape

Running record of decisions, changes, and reasoning. `INDEX.md` lists entries newest-first. Exists so Alex can talk progress without reading commits, and so future sessions can reconstruct *why*.

One file per session in `Dev/Planning/build-log/`, named `vNN-slug.md`:

```markdown
# V<N> — YYYY-MM-DD — One-line summary

**What shipped.** Short paragraph: concrete deliverables, files added/changed, components installed, smoke-test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions. Skip housekeeping.

**Pivots and surprises.** What differed from scope expectations.

```

After writing the file, prepend an index line to `Dev/Planning/build-log/INDEX.md`:
`- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — One-line summary`

**Note:** Consumer build-log entries carry an additional `## Performance` section — see `plugin/docs/DOC-STRUCTURE.md`. This dev build-log doesn't use it.

Don't pad. Half a page is good; shorter is better.

---

## Queued batch entry shape

`Dev/Planning/BACKLOG.md` → *Queued batches* section. Full scope per upcoming batch. Read at session open for context; removed when batch ships (session close).

Each entry:

```markdown
### NNNN — Batch title

**Goal.** Why this batch exists — the problem or gap it addresses.

**Approach.** How the goal will be accomplished. Omit when the goal implies the method.

**Inputs.** Non-standard resources with paths. Omit when everything is derivable from committed repo. Every path must resolve — out-of-repo references are a bug (see *Drafts in flight*).

**Outputs.** What changes when the batch ships — files created or updated, docs touched.

**Success criteria.** Observable conditions that confirm the batch delivered. Phrased as testable statements.

**Risks / dependencies.** What could go wrong, and what must ship first. Omit when none.
```

**Heading number.** 4-digit, zero-padded (e.g. `0127`). Next unused number; never reused. Numbers track identity, not order — reorder by moving sections, not renumbering.

**Field order.** Goal → Approach → Inputs → Outputs → Success criteria → Risks / dependencies. Goal, Outputs, and Success criteria always present. The rest are conditional — omit rather than leave empty.

**Parked batches.** Add a `**Parked.**` line before Goal: session tag, reason, and conditions for revisiting. The batch stays in the queue as a placeholder.

**Sizing.** Each field: one paragraph or a tight list. The whole entry should fit on a screen. If it doesn't, the batch is probably too large or under-scoped.

**Not plugin-side build batches.** Dev-side roadmap entries. Plugin-side build batches (in consumer projects' BACKLOG) have a different shape with two regions — scope-context and build-operations — per `plugin/docs/DOC-STRUCTURE.md` → *BACKLOG structure*.

**Cross-reference.** Dev "queued batch" = plugin "build batch." Both are engineering work units priority-ordered in BACKLOG. The names differ because dev-side entries are roadmap-shaped (no Files:/Tests:/Serves:) while plugin-side entries carry build-operations for hook enforcement.

---

## Open-questions entry shape

Open questions live in `Dev/Planning/BACKLOG.md` → *Open questions* section. Parking lot for method-level questions not yet batch-ready.

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

2. **Promoted to its own batch.** New queued batch entry added to BACKLOG.md → *Queued batches*. Entry removed from *Open questions* at promotion.

3. **Partial fold-in.** Batch addresses one shape, others stay parked. Entry stays with a date-tagged update note. *Next step* revised to reflect what's still open.

4. **Dropped.** No longer relevant. One-line reason in build-log; entry removed.

The session-open scan is what makes graduation triggers fire.

**Plugin consideration.** Plugin-side `DOC-STRUCTURE.md` → *BACKLOG structure* → *Open questions* defines the OQ concept but doesn't specify graduation paths or Working notes. These dev-side additions are useful patterns that could flow to the plugin in a future batch.

---

## Ideas section entry shape

Ideas live in `Dev/Planning/BACKLOG.md` → *Ideas* section. Lightest-weight capture — raw one-liners from any session type.

Each entry:

```
- YYYY-MM-DD — One-line description of the idea.
```

**Ordering.** Newest first.

**Lifecycle.** Written during any session (idea sweep, mid-session observation, or dedicated ideation). Promoted to an OQ or queued batch during planning or deliberation sessions. Dropped with a one-line reason in the build-log if no longer relevant. Removed from Ideas when promoted or dropped.

**Bar.** Lower than OQs — no framing paragraph, no "why it matters," no graduation trigger. Just enough to not lose the thought. If the idea already has enough shape for a *Next step*, it's an OQ, not an idea.

**Plugin equivalent.** Plugin-side `DOC-STRUCTURE.md` → *BACKLOG structure* → *Ideas* specifies the same `YYYY-MM-DD — [one-line description]` format. Aligned.

---

## TEST-LOG entry shape

`Dev/Planning/test-log/` is the smoke-test record. One file per session, named `vNN-slug.md`. One row per check:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID. Never reused. |
| **Date** | YYYY-MM-DD. |
| **Session** | Session tag. |
| **Component** | Plugin component(s) exercised. |
| **Test** | What was checked, one sentence. Specific enough to re-run. |
| **Status** | `Pass`, `Fail`, or `Skipped` (reason in Notes). |
| **Notes** | Observations, surprises, skip reason. Keep tight. |

**When to add.** During/after the smoke test, while fresh.

**Status flips.** Previously-Pass now Fails: *append a new row* with same Test, today's session, `Fail` — don't edit the old. Same in reverse. Row-per-event keeps history intact.

**Component changes.** Old row → `Superseded` with note pointing at the changing session. New rows record the retest. Only when the test description itself no longer makes sense.

**BUILD-LOG linking.** Each build-log entry names the TEST-LOG row range in *What shipped*. Prose in build-log; per-check in test-log. Don't duplicate.

---

## Test sessions index

`Dev/Planning/test-log/INDEX.md` — standalone index of per-session files. Newest-first bullet list: `- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — Summary`. New line prepended at session close; never removed. Non-session tests (e.g. cowboy tests) use `<type>-YYYY-MM-DD.md`.

---

## INVENTORY entry shape

`Dev/INVENTORY.md` — plugin architecture reference. Current state, not history.

**Component entry formats** (under *Plugin components*):

- **Hooks:** `- **<Name> hook.** <Description>. <Version tags>.` Internal structure documented inline.
- **Procedure docs:** `- **<name>.md** — V<N> origin, procedure doc V<N>. <Description>.`
- **Slash commands:** `- **/<name>** — <description>. <Origin version>. **Shipped V<N>**.`
- **Bundled artefacts:** `- <count> <type> under <path>: <list>.` or `- <path> — <description>.`

**When updated.** Any session that changes a plugin component. Doc-code parity audit catches misses.

---

## Research folder file shape

`Dev/Resources/research/<topic>.md` — findings from dev-session research. Distinct from plugin-side `_method/research/`.

**Naming.** Kebab-case topic slug, no date prefix. Session tag suffix optional for revisited topics.

**Structure.** No fixed template — free-form, Q&A, or audit format as needed.

**Lifecycle.** Persists indefinitely; updated rather than duplicated on revisit. Zero maintenance — no MANIFEST tracking, no BACKLOG entries. Valid on queued-batch `Inputs:` lines. Filing mandatory per CLAUDE.md → *File research before moving on*.

---

## Dev-side proxy file spec

`Dev/Planning/.proxies/` holds lightweight index files summarizing dev-side source-of-truth docs. Same concept as plugin-side `_method/proxies/`, adapted for dev-side sources.

**Location.** `Dev/Planning/.proxies/`. Three files: `session-protocol.md`, `session-reference.md`, `backlog.md`.

**HTML comment header.** Every proxy starts with:

```
<!-- proxy | source: <path> | generated: YYYY-MM-DD v<N> | when: <load timing> -->
```

- `source` — path relative to `sovereign-implementer/`.
- `generated` — date and session tag when last regenerated.
- `when` — load timing hint (e.g. "every session open", "dip on demand").

**Body format.** H1 title, state summary (2–4 lines of key metrics), then `## Sections` with one line per source-doc section:

```
- L<N> **<Section title>** — <one-phrase summary>
```

`L<N>` = starting line number in the source doc, for targeted offset/limit reads.

**The BACKLOG proxy is different.** `backlog.md` is an operational index — not just a summary. It carries full section-by-section breakdowns (queue counts, per-batch summaries, OQ status). Directly edited at session close. Same role as the plugin-side `_method/proxies/backlog.md`.

**Regeneration.** Run `bump_version.py --session-tag v<N>` (proxies-only mode) or as part of a version bump. The script updates HTML comment headers and `L<N>` line-number pointers mechanically. Section descriptions and state summaries require manual review after source edits the script can't detect.

**When regenerated.** At session close (mechanical pass), after any session that edited the source docs. Skipped when neither the source docs nor the version changed.

---

## Plugin migration context

From V17, this project distributes the method's rules across Claude Code plugin components (hooks, subagents, skills, slash commands) so adherence becomes structural rather than prompt-based. Design and roadmap: `Dev/INVENTORY.md`, `Dev/Planning/BACKLOG.md`.

Context for working in the project, not a procedural rule.

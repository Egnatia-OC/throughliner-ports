# Session reference — Entry shapes, lists, and historical context

Companion to `session-protocol.md`. Dip into sections as needed — don't load the whole file at session open.

---

## Two-write rule for canonical docs — RETIRED

> Deleted in v95. The repo-root docs-only set (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/`) was removed from the repo. All method content lives plugin-side only. Historical context: BUILD-LOG v32 (creation), v40 (shelved), v95 (deleted).

---

## Testing

Testing means **smoke-testing in Claude Code** — install the plugin via local marketplace, run a desktop-app burner session against a scratch directory or Taskflow. This *is* live testing. Hooks fire; slash commands appear; procedure docs load; SessionStart injects `additionalContext`; PreToolUse denies with reason text; `/sovsetup` scaffolds templates. V18/V19/V21/V22 each shipped with smoke tests. Outcomes → `Dev/Planning/test-log/`.

**Pre-install options:**

- **Local marketplace install.** `/plugin marketplace add` + `/plugin install`, then test in burner session. Highest fidelity. Standard for testable code. `/reload-plugins` picks up edits.
- **Hook direct invocation.** `echo '{"cwd": "/path", "session_id": "test"}' | python plugin/hooks/session_start.py`. Validates parsing + stdout shape pre-smoke-test.
- **Parser CLI.** `python plugin/scripts/parse_backlog.py <BACKLOG.md path>` — inspect output.
- **Code review.** Read and reason. Catches structural errors; misses runtime issues.

**What we don't do:**

- **No public marketplace.** Plugin installed locally via `/plugin marketplace add`. Public distribution is later.
- **No CI.** Pytest runs locally; smoke tests are hand-run by Alex on Windows.

**Where outcomes go.** Each check → a per-session file in `Dev/Planning/test-log/`. Build-log entries reference the TEST-LOG row range ("see TEST-LOG #045-052") rather than restating.

**Pitfall.** "Live install + back-test" as single-session deliverable keeps resurfacing. Don't conflate a smoke test (does it work?) with a release test (does the published package install?).

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

**Relationship to smoke tests.** Pytest validates parsing, deny/allow logic, stdout shape — everything without a running Claude Code session. Smoke tests remain authority for "does Claude Code actually fire the hook." Complementary: suite catches regressions fast; smoke tests catch wiring.

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

When a session substantively changes the method/plugin, every method-side `*No-code method — Version N.*` footer bumps. **Dev-internal-only sessions skip entirely.**

Method-side = describes how the consumer method works. Dev-internal files (`Dev/Planning/build-log/`, `Dev/Planning/test-log/`, `BACKLOG.md`, these session files) don't carry the footer.

### Plugin-side (the leader)

- `plugin/docs/DOC-STRUCTURE.md`
- `plugin/docs/VOCABULARY.md`
- `plugin/hooks/universal-behaviour.md`
- `plugin/templates/CLAUDE-TEMPLATE.md`
- `plugin/templates/UX-TEMPLATE.md`
- `plugin/templates/BUILD-PLAN-TEMPLATE.md` (legacy single-file)
- `plugin/templates/.proxies/build-plan.md`
- `plugin/templates/.proxies/build-log.md`
- `plugin/templates/.proxies/test-log.md`
- `plugin/templates/MANIFEST-TEMPLATE.md`
- `plugin/templates/ADDITIONAL-DOC-TEMPLATE.md`
- `Guides/Reference manual.md` (plugin-side)

### Cross-cutting

- `Dev/INVENTORY.md` — carries the footer for sync, even though dev-internal.

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
| `Dev/Planning/BACKLOG.md` → *Queued batches* entries | **Transient.** Full scope for each queued batch. Once shipped, entry removed (step 9) — commit + code + docs are source of truth. | Batch ships (step 9). |
| `Dev/drafts/<topic>.md` | **Transient.** Substantive content a future session might start from. Committed when "good enough to walk away from." | Consumed (folded into spec/scope/persistent location). Dead-ends pruned with BUILD-LOG note. |
| `Dev/INVENTORY.md` | **Living.** Current plugin architecture. | Never. |
| `Dev/Planning/BACKLOG.md` | **Living.** Rolling roadmap + open questions. | Never. |
| `Dev/Planning/build-log/` | **Historical.** One file per session, INDEX.md newest first. | Never. |
| `Dev/Planning/test-log/` | **Living.** One file per session, one row per check. Status may flip. | Rows for removed components pruned by planning subagent (V53). |
| `Dev/session-protocol.md` | **Living.** Session lifecycle — always read. | Never. |
| `Dev/session-reference.md` (this file) | **Living.** Entry shapes, lists, historical — dip on demand. | Never. |

### Drafts in flight

`Dev/drafts/<topic>.md` is where substantive chat content lands as soon as a future session might start from it. Committed in the drafting session's commit; "good enough to walk away from" is the bar. Deleted when consumed. Dead-end drafts: prune with BUILD-LOG note.

**Corollary.** If a queued batch's *Inputs* names content not reachable from the committed repo ("Alex has the file locally," "from the previous chat," etc.) — that's a bug. Get the content into `Dev/drafts/` retroactively or restate as something the next session can rebuild from repo contents. The session-open scan in `CLAUDE.md` catches the reading side; this catches the writing side.

---

## BUILD-LOG entry shape

`Dev/Planning/build-log/` is the running record of decisions, changes, and reasoning. `INDEX.md` lists entries newest-first. It exists so Alex can talk progress without making people read commits, and so future sessions can reconstruct *why*.

One file per session in `Dev/Planning/build-log/`, named `vNN-slug.md`:

```markdown
# V<N> — YYYY-MM-DD — One-line summary

**What shipped.** Short paragraph: concrete deliverables, files added/changed, components installed, smoke-test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions. Skip housekeeping.

**Pivots and surprises.** What differed from scope expectations.

```

After writing the file, prepend an index line to `Dev/Planning/build-log/INDEX.md`:
`- [vNN-slug.md](vNN-slug.md) — YYYY-MM-DD — One-line summary`

**Note:** Consumer build-log entries carry an additional `## Performance` section — see `DOC-STRUCTURE.md`. This dev build-log doesn't use it.

Don't pad. Half a page is good; shorter is better.

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

---

## TEST-LOG entry shape

`Dev/Planning/test-log/` is the smoke-test record. One file per session, named `vNN-slug.md`. One row per check:

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

From V17, this project distributes the method's rules across Claude Code plugin components (hooks, subagents, skills, slash commands) so adherence becomes structural rather than prompt-based. Design and roadmap: `Dev/INVENTORY.md`, `Dev/Planning/BACKLOG.md`.

Context for working in the project, not a procedural rule.

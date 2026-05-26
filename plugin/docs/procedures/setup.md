# /setup procedure — no-code method

Follow this procedure when the user runs `/setup`. Bring a folder under the method's discipline.

## Framing: the method adopts the folder

Speak about "this folder" being adopted/unadopted, not the user adopting the method:
- "This folder hasn't been adopted yet." / "I'll create the method's starter docs alongside your code."
- Not: "Do you want to adopt the method?" / "Are you ready to use the method?"

## Efficiency rule — classify first, load later

Do NOT read any plugin docs until AFTER case dispatch. The `detect-case` script is a single Bash call. Don't Glob/Grep/Read the project before dispatch either. After dispatch, read only what the matched branch needs.

## First action — detect case

```
python "${CLAUDE_PLUGIN_ROOT}/skills/setup/scripts/scaffold.py" detect-case
```

Returns JSON: `{"case": 1, "case_name": "...", "target_path": "...", "details": {...}}`. Don't re-classify.

## Case dispatch

---

### Case 1 — empty folder

No CLAUDE.md, no substantial work.

**Open:** "Fresh folder. I'll ask four questions, then create starter docs inside `_method/` (UX.md, BACKLOG/, build-log/, test-log/, MANIFEST.md) plus CLAUDE.md at the project root, and `_method/planning/drafts/`, `_method/research/`, and `_method/research/search-queries/`."

**Four questions (one per message, wait for each):**

1. **Product overview.** "Tell me about your product. What does it do, who is it for, and what makes it distinct — or what specific tension does it resolve? And are there milestones you're working toward?" → CLAUDE.md *Product overview* (all four fields) + UX.md *Project context* (synthesized from the product description). If the answer doesn't cover all four fields, follow up once before moving on.
2. **UX principles.** "What 3–6 principles should guide every design decision?" → *UX principles*.
3. **Core functionalities.** "What are the 3–5 must-have features? For each: one-paragraph experience description + one-line `user needs this because…` rationale." → *Functionalities*.
4. **First batch sketch.** "Which is the smallest end-to-end thing we can build and test first?" → top BACKLOG batch.

After answers:
1. Run `check`. If `ready: false`, surface conflicts and stop.
2. Run `write`. Surface files list.
3. Apply answers:
   - **Q1 →** CLAUDE.md Product overview (all four fields) + UX.md Project context (synthesized from the product description).
   - **Q2 →** UX.md UX principles section. Write every principle the user agreed to — replace the template placeholders with the full set.
   - **Q3 →** UX.md Functionalities section. Write every functionality with its experience description and rationale.
   - **Q4 →** Seed BACKLOG batch (folder mode: create per-batch file with `Status: queued` line + INDEX.md reference).

After applying answers, regenerate proxies: read each source doc, write the matching `_method/proxies/` file per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

**Recap:** "Adopted (case 1). Created [docs list]. User's answers folded into UX.md and BACKLOG."

---

### Case 2 — existing code, no docs

Substantial work but no CLAUDE.md.

**Open:** Describe what you see. Two options: (1) Create starter docs [recommended]. (2) Cancel — disable plugin via `/plugin` → Installed → toggle off.

**Option 1:**
1. Glob check for spine-doc filenames in subdirs.
2. Run `check` (expect `ready: true`), then `write`.
3. Walk four new-project questions (same as Case 1). User more likely to skip — anything unanswered stays as a planning batch in BACKLOG for next session. Apply answered questions using the same Q1–Q4 mapping as Case 1 step 3.

After applying answers, regenerate proxies: read each source doc, write the matching `_method/proxies/` file per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

**Recap:** "Adopted (case 2). Created [docs] alongside existing code. [Which questions answered/pending.]"

**Option 2:** "No changes made. Disable plugin via `/plugin` → Installed → toggle off."

---

### Case 3 — existing code, foreign docs

CLAUDE.md present but no method footer. Probably from Claude Code's `/init` — don't make them feel punished.

**Open:** Three options: (1) Migrate — walk existing CLAUDE.md and propose edits to method spec [recommended if content worth keeping]. (2) Overwrite — replace with template (backup first). (3) Leave alone — disable plugin via `/plugin` → toggle off.

**Option 1 (migrate):**
1. Read existing CLAUDE.md. Identify content worth keeping.
2. Read CLAUDE-TEMPLATE.md for target shape.
3. Propose unified plan. Iterate until satisfied.
4. Apply edits. Run `check` + `write` for other docs.
5. Source-of-truth docs are directly editable during setup (planning phase).

**Option 2 (overwrite):**
1. Backup: `cp CLAUDE.md CLAUDE.md.foreign-backup-<date>`.
2. Remove original (try bash `rm`; if ACL fails, ask user to delete manually).
3. Run `write`. Walk four questions. Apply answered questions using the same Q1–Q4 mapping as Case 1 step 3.

**Option 3:** "No changes made."

---

### Case 4 — already method-managed

Footer present. User ran `/setup` anyway — refresh, habit, or version mismatch.

**First — detect template state:**
1. CLAUDE.md footer → `user_v`.
2. `PLUGIN_METHOD_VERSION` → `plugin_v`.
3. Each spine doc: matches `plugin_v`, older, or missing.

**Open:** "Already adopted — CLAUDE.md on V[user_v], plugin on V[plugin_v]." [If stale: "Footers aren't all current."] Two options: (1) Refresh templates. (2) Cancel.

**Option 1 (refresh):**

Surface planned bumps before touching anything. Edit every footer via `Edit` — the V38 carve-out allows footer-only edits on locked docs. Don't skip any silently.

**After bumps — BACKLOG batch-structure migration (V47).** Check for pre-V47 format (no scope-context sections, no `Changes:` delimiter). For each old-format batch: extract existing prose → use as Goal, add Outputs/Success criteria with `Scope not yet defined — fill during the next planning session.` Insert `Changes:` delimiter. Don't use `[placeholder]` brackets — before-build reads those as blocking.

**After V47 — BACKLOG folder-split (V48).** If path block points at `BACKLOG.md` (not `BACKLOG/INDEX.md`): create `BACKLOG/`, extract inline batches to per-batch files, create INDEX.md, update path block, delete old file.

**After folder split — TEST-LOG migration (V46).** If 8-column format (no Type/Verifier): add columns, existing rows default to `Look and click` / `User`.

**After TEST-LOG — BUILD-LOG folder migration (V50).** If flat `BUILD-LOG.md`: create `build-log/`, extract entries to per-build files, create INDEX.md, update path block, delete old file.

**After BUILD-LOG — INDEX relocation to proxies (V70).** If path block points at `BACKLOG/INDEX.md` or `_method/BACKLOG/INDEX.md`: move INDEX.md content into `_method/proxies/backlog.md` (create proxies/ dir if needed), delete `BACKLOG/INDEX.md`, update path block to `_method/proxies/backlog.md`. Same for `build-log/INDEX.md` → `_method/proxies/build-log.md`. If `_method/proxies/` dir already has these files, skip.

**After INDEX relocation — TEST-LOG folder split (V75).** If path block points at `TEST-LOG.md` (flat file, not `proxies/test-log.md`): create `_method/test-log/`, split rows by Session into per-session files (`NNN-batch-name.md`), write `_method/proxies/test-log.md` as folder index, update path block to `_method/proxies/test-log.md`, delete old `TEST-LOG.md`. If `_method/test-log/` already exists, skip.

**After TEST-LOG folder split — Product overview backfill (V69).** If CLAUDE.md has no `## Product overview` section: ask the overview question (same as Case 1, Q1) and write the section into CLAUDE.md above the path block.

**Recap:** "Refreshed (case 4). Bumped footers on [list]. [Migrations performed.]"

**Option 2:** "No changes. Wrong folder?"

---

## Closing

Final output = the Recap sentence(s). Don't append extra commentary.

## Errors

Surface errors verbatim, name what couldn't be done, stop. Don't retry silently or invent fallbacks.

## What you don't do

- Don't plan, build, or test.
- Don't touch files outside scaffold-path list + backups.
- Don't re-classify after detect-case.

---

*No-code method — Version 76.*

# /sovsetup procedure — no-code method

Follow this procedure when the user runs `/sovsetup`. Bring a folder under the method's discipline.

## Framing: the method adopts the folder

Speak about "this folder" being adopted/unadopted, not the user adopting the method:
- "This folder hasn't been adopted yet." / "I'll create the method's starter docs alongside your code."
- Not: "Do you want to adopt the method?" / "Are you ready to use the method?"

## Efficiency rule — classify first, load later

Do NOT read any plugin docs until AFTER case dispatch. The `detect-case` script is a single Bash call. Don't Glob/Grep/Read the project before dispatch either. After dispatch, read only what the matched branch needs.

## First action — detect case

```
python "${CLAUDE_PLUGIN_ROOT}/skills/sovsetup/scripts/scaffold.py" detect-case
```

Returns JSON: `{"case": 1, "case_name": "...", "target_path": "...", "details": {...}}`. Don't re-classify.

## Case dispatch

---

### Case 1 — empty folder

No CLAUDE.md, no substantial work.

**Open:** "Fresh folder. I'll ask five questions, then create starter docs inside `_method/` (UX.md, BACKLOG/, build-log/, test-log/, MANIFEST.md) plus CLAUDE.md at the project root, and `_method/planning/drafts/`, `_method/research/`, and `_method/research/search-queries/`."

**Five questions (one per message, wait for each):**

1. **Product overview.** "Tell me about your product. What does it do, who is it for, and what makes it distinct — or what specific tension does it resolve? And are there milestones you're working toward?" → CLAUDE.md *Product overview* (all four fields) + UX.md *Project context* (synthesized from the product description). If the answer doesn't cover all four fields, follow up once before moving on.
2. **UX principles.** "Are there any guiding principles you want to lock in for design decisions?" If no → skip to Q3. If yes → "What are they?" No minimum count. → *UX principles*.
3. **Core functionalities.** "What are the 3–5 must-have features? For each: one-paragraph experience description + one-line `user needs this because…` rationale." → *Functionalities*.
4. **First batch sketch.** "Which is the smallest end-to-end thing we can build and test first?" → top BACKLOG batch.
5. **Language.** "What language should I use for responses and documentation? English is the default." → CLAUDE.md *Language:* field. If the user answered Q1–Q4 in a non-English language and doesn't specify otherwise, default to the language they used.

After answers:
1. Run `check`. If `ready: false`, surface conflicts and stop.
2. Run `write`. Surface files list.
3. If `.git/` exists in the project root, run `git config --local core.quotepath false` (prevents octal escaping of non-ASCII filenames, which breaks path matching in hooks).
4. Apply answers:
   - **Q1 →** CLAUDE.md Product overview (all four fields) + UX.md Project context (synthesized from the product description).
   - **Q2 →** UX.md UX principles section. Write every principle the user agreed to — replace the template placeholders with the full set.
   - **Q3 →** UX.md Functionalities section. Write every functionality with its experience description and rationale.
   - **Q4 →** Seed BACKLOG batch (folder mode: create per-batch file with `Status: queued` line + INDEX.md reference).
   - **Q5 →** CLAUDE.md Language: field. Replace the default `English` with the user's answer.

After applying answers, regenerate proxies per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

**Recap:** "Adopted (case 1). Created [docs list]. User's answers folded into UX.md and BACKLOG."

---

### Case 2 — existing code, no docs

Substantial work but no CLAUDE.md.

**Open:** Describe what you see. Two options: (1) Create starter docs [recommended]. (2) Cancel — disable plugin via `/plugin` → Installed → toggle off.

**Option 1:**
1. Glob check for spine-doc filenames in subdirs.
2. Run `check` (expect `ready: true`), then `write`.
3. Walk five questions (same as Case 1). User more likely to skip — unanswered items stay as planning batches in BACKLOG. Apply answers per Case 1 step 4.

After applying answers, regenerate proxies per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

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
3. Run `write`. Walk five questions. Apply answers per Case 1 step 4.

**Option 3:** "No changes made."

---

### Case 4 — already method-managed

Footer present. User ran `/sovsetup` anyway — refresh, habit, or version mismatch.

**First — detect template state:**
1. CLAUDE.md footer → `user_v`.
2. `PLUGIN_METHOD_VERSION` → `plugin_v`.
3. Each spine doc: matches `plugin_v`, older, or missing.

**Open:** "Already adopted — CLAUDE.md on V[user_v], plugin on V[plugin_v]." [If stale: "Footers aren't all current."] Two options: (1) Refresh templates. (2) Cancel.

**Option 1 (refresh):**

Surface planned bumps before touching anything. Edit every footer via `Edit` — the V38 carve-out allows footer-only edits on locked docs. Don't skip any silently.

**After bumps — BACKLOG batch-structure migration (V47).** Check for pre-V47 format (no scope-context sections, no `Changes:` delimiter). For each old-format batch: extract existing prose → use as Goal, add Outputs/Success criteria with `Scope not yet defined — fill during the next planning session.` Insert `Changes:` delimiter. Don't use `[placeholder]` brackets — `/sovrecap` reads those as blocking.

**After V47 — BACKLOG folder-split (V48).** If path block points at `BACKLOG.md` (not `BACKLOG/INDEX.md`): create `BACKLOG/`, extract inline batches to per-batch files, create INDEX.md, update path block, delete old file.

**After folder split — TEST-LOG migration (V46).** If 8-column format (no Type/Verifier): add columns, existing rows default to `Look and click` / `User`.

**After TEST-LOG — BUILD-LOG folder migration (V50).** If flat `BUILD-LOG.md`: create `build-log/`, extract entries to per-build files, create INDEX.md, update path block, delete old file.

**After BUILD-LOG — INDEX relocation to proxies (V70).** If path block points at `BACKLOG/INDEX.md` or `_method/BACKLOG/INDEX.md`: move INDEX.md content into `_method/proxies/backlog.md` (create proxies/ dir if needed), delete `BACKLOG/INDEX.md`, update path block to `_method/proxies/backlog.md`. Same for `build-log/INDEX.md` → `_method/proxies/build-log.md`. If `_method/proxies/` dir already has these files, skip.

**After INDEX relocation — TEST-LOG folder split (V75).** If path block points at `TEST-LOG.md` (flat file, not a proxy in `proxies/`): create `_method/test-log/`, split rows by Session into per-session files (`NNN-batch-name.md`), add `## Test sessions` section to the BACKLOG proxy with the folder index, update path block `"TEST-LOG.md"` to `_method/proxies/backlog.md`, delete old `TEST-LOG.md`. If `_method/test-log/` already exists, skip.

**After TEST-LOG folder split — Product overview backfill (V69).** If CLAUDE.md has no `## Product overview` section: ask the overview question (Case 1, Q1) and write the section above the path block.

**After product overview — Folder restructure (0087).** If spine docs (UX.md, MANIFEST.md) exist at project root instead of inside `_method/`: create `_method/` if absent, move UX.md and MANIFEST.md into it, move BACKLOG/, build-log/, test-log/ into `_method/` if at root, move proxies/ into `_method/` if at root. Update CLAUDE.md path block entries to use `_method/` prefixed paths. If everything is already inside `_method/`, skip.

**After folder restructure — Companion directories (0051/0083).** Create if absent: `_method/planning/drafts/`, `_method/research/`, `_method/research/search-queries/`.

**After companion directories — Summary proxies (0081).** If `_method/proxies/` is missing any of `ux.md`, `manifest.md`, or `research.md`: regenerate from source docs per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*.

**After summary proxies — `_method/` orientation section (0105).** If CLAUDE.md has no `## What's inside _method/` section: add it between `## Where the docs live` and `## Plugin management`, using CLAUDE-TEMPLATE.md content.

**After orientation section — Language setting (0114).** If CLAUDE.md has no `## Language` section: add it between `## Product overview` and `## Where the docs live`, using CLAUDE-TEMPLATE.md content (defaults to English). Ask if the user wants a different language.

**After language setting — Git quotepath (0114).** Run `git config --local core.quotepath false` (prevents octal escaping of non-ASCII filenames). Idempotent — safe to run even if already set.

**Recap:** "Refreshed (case 4). Bumped footers on [list]. [Migrations performed.]"

**Option 2:** "No changes. Wrong folder?"

---

## Closing

Final output = the Recap sentence(s), then the handoff.

**Handoff.** After the recap, tell the user what to do next:
- If Q4 produced a fully scoped batch (Goal, Outputs, Success criteria, Changes all filled): "Your first batch is ready. Run `/sovrecap` to review the file list and test plan, then `/sovbuild` to start building."
- Otherwise: "Run `/sovplan` to finish scoping your first batch, then `/sovrecap` and `/sovbuild` when it's ready."

## Errors

Surface errors verbatim, name what couldn't be done, stop. Don't retry silently or invent fallbacks.

## What you don't do

- Don't plan, build, or test.
- Don't touch files outside scaffold-path list + backups.
- Don't re-classify after detect-case.

---

*No-code method — Version 108.*

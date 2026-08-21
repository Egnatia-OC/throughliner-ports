# [HASH] — `docs-b/` becomes `docs/`, and the queue's own stale paths turn out to be beyond a build's reach

The folder rename refused on 2026-08-16 and overturned on 2026-08-17 was built. `plugin/throughliner/docs-b/` is now `plugin/throughliner/docs/`, moved with `git mv` so all fourteen procedure docs kept their history as renames rather than as a delete and an add.

**The item's own instruction to re-grep rather than trust its numbers was the right call, and it paid.** The counts written into it on 2026-08-16 — 639 occurrences, 215 live, 22 files — had moved to 250 live occurrences across 24 files. Six files the item never named turned up: `resources/rule_signals.py`, `retired-terms.md`, `method-compliance-audit-checklist.md`, `queue-two-section-migration-recipe.md`, `resources/2026-08-09-emergency-revert-plan.md`, and three findings under `resources/research/`. The user was asked before the run started and approved the split: the four live ones joined the build, and the records joined the exclusions beside `LOG/`, `INBOX/archive/` and `resources/plugin-behaviour-retired.md`. The item's acceptance grep was amended in the same move, since it would otherwise have demanded a clean sweep the exclusions make impossible.

**The reason for excluding a research finding is not the reason for excluding a log entry, and the distinction is worth keeping.** A session record names the old path because that is what the folder was called when the record was written. A finding under `resources/research/` names it inside quoted evidence — `scope-lock-audit.md` cites file-and-line for rules it is quoting, and `tersifying-the-queue.md` names `docs-b/` as its own worked example of a retired path. Rewriting a path inside a quotation makes the quotation say something it did not.

**`rule_signals.py` is why over-including was the safer error.** It stores the doc paths it opens. Left stale, it would not have errored — it would have found nothing and reported the rule checks clean, which is the failure mode this project spends the most effort guarding against. It was re-run after the rename and reports four checks run against the new paths with nothing found.

**Two prose lines were rewritten rather than substituted, because substitution would have made them false.** `hook_schema_check.py` carried a docstring comparing the two docsets by size — "~50KB in docs-b, ~89KB in docs" — which a blind swap turns into a comparison of one folder with itself. It now names the lighter and heavier docsets. Worth recording alongside: the new `docs/` reuses the name docset A once had, so an old reference to `docs/` and a new one mean different things.

**`CLAUDE.md`'s refusal paragraph was evicted rather than amended.** The whole "drift by fixing drift" argument is gone, along with the 639/215/424 figures that supported it, replaced by a dated line stating that the rename happened and naming which paths correctly keep the old name. Leaving the reasoning standing beside a decision that overturned it would have doubled the text rather than merged it.

**One instruction in the item could not be built, and the refusal was mechanical rather than a judgment.** The item directed the run to rewrite the old path inside every open queue item's Files line, on the reasoning that the queue instructs future builds rather than recording the past. `pre_tool_use` refused: a build does not edit QUEUE.md's contents, and the queue tool it redirects to moves, deletes and appends whole entries byte-for-byte, so it cannot reach text inside one. **That instruction was asking a build to do planning work**, which is the boundary the whole method rests on, so the hook was right and the item was wrong. Filed as [queue-files-lines-name-the-old-docs-path]; roughly forty references are still outstanding, and until they are fixed the item's acceptance grep does not come back clean.

**A second scope assumption was wrong and cost one interruption.** The run's first file list omitted the shipped procedure docs, on the belief that the scope-lock's unconditional method-docs allowance covered `plugin/throughliner/docs/`. It does not — that allowance is for the *project's* own documents, QUEUE.md and LOG/ and the session's working file. Five docs carrying cross-references to siblings had to be added to the file list with the user's approval mid-build.

**The run's bound was read from QUEUE.md by hand.** [rename-docs-b-folder] carries `Runs alone`, and the generated build view does not emit that marker — the defect captured yesterday as [build-view-drops-runs-alone], still open. A run reading only the view would have carried straight on into fifteen further items whose paths this build was in the middle of moving.

**Files touched:** `plugin/throughliner/docs-b/` → `plugin/throughliner/docs/` (fourteen files); the five skill entry points under `plugin/throughliner/skills/`; `plugin/throughliner/hooks/session_start.py`; `docs/done.md`, `docs/next.md`, `docs/plan.md`, `docs/setup.md`, `docs/skill-nonspecific-rules.md`; `resources/testing/hook_schema_check.py`, `test_plan_quiet_list.py`, `test_pre_tool_use_shell_writes.py`, `test_queue_digest.py`; `resources/rule_signals.py`, `resources/retired-terms.md`, `resources/method-compliance-audit-checklist.md`, `resources/queue-two-section-migration-recipe.md`; `CLAUDE.md`; `QUEUE.md` (the pre-run scope amendment, and the item's removal at the tick).

**Routed to Captures:** [queue-files-lines-name-the-old-docs-path].

**Verification:** all ten suites under `resources/testing/` pass. `py resources/rule_signals.py .` reports four checks run, nothing found — against the renamed paths, which is what proves the script still reads the files rather than silently reading nothing.

Rule gate: run — transcribed from the item, which recorded no rule authored and none amended. The disposition is an eviction: `CLAUDE.md`'s paragraph refusing this rename is deleted outright along with its reasoning, replaced by a dated statement of fact. The failure evidence is the refusal failing on first contact with the user it was written for — she read the explanation and rejected it the next day.

No `Retired:` line, and the omission is deliberate. `docs-b` is a retired folder name, but adding it to `resources/retired-terms.md` would fire immediately against correct work: `CLAUDE.md`'s new dated line names the old path on purpose, and so do the excluded records. That is the cry-wolf case `retired-terms.md` documents in its own text — a term whose stale use cannot be told apart from a correct historical reference by any string match.

FAQ: not needed because nothing a user does changes. The folder is internal to the plugin package; no step, command, document of theirs, or moment where they must answer or decide is affected.

Advisory: filed — [forward-advisory]

No epoch bump: no consumer project's documents become structurally wrong, so `FORMAT_EPOCH` and `migrate-checklist.md` are both untouched.

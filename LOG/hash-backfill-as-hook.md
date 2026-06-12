# LOG entry — hash-backfill-as-hook

## [HASH] — /next [hash-backfill-as-hook]: LOG hash backfill moved from procedure docs into the session_start hook

The backfill was the plugin's most mechanical procedure — find unfilled hash placeholders, resolve the commit, replace — yet it lived as model-executed instructions in two docs (plan.md Step 1, next.md pre-flight), costing procedure lines and riding on model compliance. It's now Python in session_start.py: it scans all LOG/*.md including the frozen archives, replaces the token only in hash position (an entry heading line or the start of an index line) so body prose mentioning the token literally survives — the corruption the 2f23dc6 blanket find-replace caused can't recur — and resolves each entry to the oldest commit that introduced its title, never the newest commit touching the file, so caps and renames can't return wrong hashes for archived files. It reports one line via additionalContext and tells the session to fold the edit into its commit. Both procedure-doc copies were deleted, not consolidated, absorbing [trickle-up-hash-backfill-duplication]. The hook fires at session start only, so a /done-then-push in one session would reach push time unfilled — the push ritual in this project's CLAUDE.md gained a backfill step at its start to close that. done.md's LOG-entry-files section gained the authoring rule that entry prose never writes the literal placeholder token. One consequence rippled: deleting next.md's pre-flight sub-step renumbered the remaining steps, and the step-number cross-references this dangled in three /done sub-docs and plugin-behaviour.md were fixed — plugin-behaviour.md added to scope mid-build with approval — while the underlying fragility (step-number references break on any renumber, nothing requires checking) was routed to Captures rather than solved here. Fixture-tested against a temporary git repo: in-place replacement, oldest-commit resolution against a decoy later commit, the multi-placeholder case across two entries and two index lines, prose-mention survival, and the report line all passed; a dry run against this project's real LOG stayed silent and touched nothing.

Deferred-test confirmations, this being the first /next and /done on the reinstalled v1.11.0 host: [done-closeout-extraction] — the planning close earlier this session produced the LOG entry as its single summary, no separate recap; line removed at pre-flight. [deferred-tests-structural-home] — pre-flight re-presented the pending list from the installed docs, and this close wrote a new deferred-test line unprompted; line removed. [narrate-build-md-purpose] — scope-lock narration and rationale-carry both observed live; line trimmed to the one unobserved moment, the resume opener, which needs an interrupted build to occur naturally.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py: hash-position regex, oldest-commit resolver, backfill function (~90 lines); called in the adopted branch, report appended to additionalContext
- plugin/si-plugin/docs/plan.md: backfill block deleted from Step 1
- plugin/si-plugin/docs/next.md: pre-flight backfill sub-step deleted; remaining steps renumbered 1–4
- plugin/si-plugin/docs/done.md: literal-token authoring rule added to LOG entry files; commit-core closing line now names the hook as the backfiller
- plugin/si-plugin/docs/done-build.md, done-test.md, done-plan.md: blocker-gate cross-reference renumbered (Step 1.4 → 1.3)
- plugin/si-plugin/docs/done-build.md, done-test.md, done-plan.md, done-audit.md: entry-template lead-in now reads "backfilled automatically at the next session start"
- plugin/si-plugin/docs/plugin-behaviour.md: blocker-gate cross-reference renumbered (added to scope mid-build, approved)
- CLAUDE.md: push ritual gains the backfill as new step 1; steps renumbered 1–10
- REGISTRY.md: session_start.py description updated
- QUEUE.md Deferred tests: hook test line added; two confirmed lines removed; one trimmed

**Routed to Captures:** 4 — commit-message fence display at /done; top batch not sent first at /next pre-flight; scope-lock Files-line bare-path requirement; step-number cross-reference fragility

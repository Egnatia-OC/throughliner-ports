# LOG entry — queue-format-lint-hook

## [HASH] — /next [queue-format-lint-hook]: PostToolUse hook lints QUEUE.md structure after every edit

The queue's format rules lived only as prose in plan.md and plugin-behaviour.md, held in the model's head while writing — a weaker model drifts them, and nothing catches the drift until a later session trips over it. The new hook (hooks/post_tool_use.py, registered in hooks.json on Edit/Write/MultiEdit) reads QUEUE.md from disk after each edit lands and feeds advisory warnings back beside the tool result: batch titles missing a slug marker, parked items missing their Blocked by:/Parked: header, the Captures processed/unprocessed divider deleted, dependency headers naming slugs defined nowhere in the file, batch subheadings outside Build/Test/Audit, and batch prose naming a still-pending slug its headers don't carry ("dependency or citation?"). Deny-list by design: only known violations flag; novel sections and structures pass silently, so format evolution doesn't fight the linter. Registration was verified against the Claude Code docs before building — the plugins reference's own example is a PostToolUse hook with a Write|Edit matcher in hooks/hooks.json, and additionalContext is the documented advisory channel, shown to Claude without blocking.

One design decision landed during testing, within the batch's described checks: the prose-citation check flags only references to slugs still defined in the file. The first dry run against the real queue flagged nearly every batch — references to shipped work (past audits, landed batches) are the bulk of prose references, all legitimate citations, roughly 2.5KB of advisory noise per edit burying the four true dangling-dependency flags. The alternative — flagging every prose reference, as the batch text literally read — was weighed and rejected for context cost: a reference to a pending item can be a missed dependency, but a reference to shipped work can only be a citation. The residual problem (the check is stateless, so a reference judged "citation, fine" re-flags on every later edit) was routed to Captures rather than solved here. The dry run's four dangling-dependency flags — Depends on: [deferred-tests-structural-home] twice, [done-closeout-extraction], Blocked by: [reader-test-refresh] — are true positives left for /plan to clean.

Fixture-tested by invoking the script directly: each of the six checks fired with correct line numbers on a one-violation-per-check file; a clean file and a file with a novel section plus a bold line outside Batches stayed silent (the deny-list property); gates stayed silent on non-QUEUE.md paths, non-edit tools, and unadopted projects. Live host-side confirmation can't run until push + reinstall — written to Deferred tests.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py: created (~250 lines) — six advisory checks, deny-list, additionalContext output, silent when clean
- plugin/si-plugin/hooks/hooks.json: PostToolUse registration added (Edit|Write|MultiEdit matcher); description extended
- QUEUE.md: lint-hook re-fire capture appended to raw Captures; deferred-test line added
- REGISTRY.md: post_tool_use.py entry added; hooks.json description updated
- LOG/hash-backfill-as-hook.md + LOG/index.md: prior entry's hash placeholders backfilled to 37deaec at session start

**Routed to Captures:** the stateless re-fire observation — judged-as-citation references re-flag on every edit; candidate fixes deferred until live use shows whether it's noise

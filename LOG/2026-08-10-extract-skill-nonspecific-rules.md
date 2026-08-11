# 94bba66 — plugin-behaviour.md retired: the always-loaded rules extracted into skill-nonspecific-rules.md, the rest pushed down into their skills

The founding argument is the user's and it was made plainly: the doc's premise
does not hold, its name is doing the filing, and they are sick of spending a
week's tokens on one document. Claude's contribution was the classification and
one piece of pushback, recorded below because it should not be re-derived.

`plugin/si-plugin/docs-b/plugin-behaviour.md` no longer exists. Its skill-
nonspecific rules — everything that fires whatever is running — moved verbatim
into a new `docs-b/skill-nonspecific-rules.md`, whose **first line states the
admission test**: a rule belongs there only if it fires in all four skills. The
old file is at `resources/plugin-behaviour-retired.md`, kept as history under the
user's condition that if something breaks, a trickle-down audit gets designed
later; until then it simply sits there.

## What moved down, and one deviation from the plan

- The `[user]` walk-through lifecycle → `next.md`. This also answers the separate
  audit finding [walkthrough-rules-prohibition-heavy-and-duplicated], which
  reached the same conclusion independently.
- The build-scope definition and the working-file `Files:` machinery → `next.md`.
- Context-awareness on resume → `next.md`, as a Resuming section.
- The forward-advisory's lifecycle → `done.md`, beside the filing rule already
  there. Its read rule was already in `plan.md` and needed no move.

**One deviation, recorded because the item asked for each classification to be
confirmed at build rather than assumed.** The plan said to move the stale-fields
note (`Editor:`, `Working mode:`, `Completion mode:`) to the session-start path.
It stayed in the always-loaded file. The note governs how Claude treats a
project's own CLAUDE.md, which every skill reads at every session start, so it
passes the four-skills test; and only one of its three retired fields is
session-start-shaped, so moving the paragraph for that one mention would have
split a rule across two homes to no benefit.

## Claude's pushback, recorded rather than acted on

On this classification the great majority of the doc is genuinely skill-
nonspecific, so the extraction shrinks the always-loaded set by roughly a sixth
rather than transforming it. What the build buys is the two things the user named:
a name that states an admission test instead of a category, so a future rule
cannot be filed there by default; and the skill-specific residue landing where it
is paid only when that skill runs. Both are real. **Nobody should later read the
modest size change as evidence the build failed.**

The name was re-opened once and confirmed unchanged after three alternatives were
worked through and rejected; that reasoning is in the queue item's history and in
`resources/self-authoring-rules.md`, where this build also wrote the blurb
explaining the authoring-versus-running trade — a negative name is a good test at
authoring time and a weak signal at run time, and the two risks are not
symmetrical, because only one of them is evidenced.

## The residual weakness, stated rather than left to be found

The filename is soft steering and nothing produces evidence the test was applied.
The first-line restatement improves on a filename, because an editing session has
necessarily read the file's first page. Hard enforcement remains
[behaviour-rules-read-is-enforceable]'s question.

**Files touched:** `docs-b/plugin-behaviour.md` (git mv'd to
`resources/plugin-behaviour-retired.md`), new `docs-b/skill-nonspecific-rules.md`,
`docs-b/next.md`, `plan.md`, `done.md`, `next-build.md`, `setup.md`,
`feedback-and-inbox.md`, `hooks/session_start.py`, `hooks/pre_tool_use.py`,
`hooks/post_tool_use.py`, three `skills/*/SKILL.md`, `resources/self-authoring-rules.md`,
`resources/method-compliance-audit-checklist.md`, `SPEC.md`, `CLAUDE.md`.

**FAQ: not needed because** the change is invisible to a consumer — the file a
session reads at start is named only in Claude-facing text, and no user-facing
behaviour moved. The FAQ entries this session did write belong to the freeform
flavor, which consumers do see.

**Routed to Captures:** none from this item.

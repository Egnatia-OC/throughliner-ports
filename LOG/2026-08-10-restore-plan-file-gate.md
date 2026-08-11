# 94bba66 — The planning-session file gate and the unscoped-build surfacing, both recovered from the revert

Recovery, not a new rule. Both halves shipped at `455082b` and the 2026-08-09
emergency revert took them. Confirmed absent before rebuilding: `pre_tool_use.py`
documented three rules with no rule 4, and neither `_is_plan_quiet_path` nor
`_fire_once` existed.

## Half 1 — the doc rule

`plan.md`'s ground rules now say that nothing mechanically contains a planning
session, since there is no build working file and so no engaged scope-lock; what a
session gets instead is an ask before any write outside the quiet list. Its point
is kept verbatim in spirit: *it doesn't stop you doing something urgent, it stops
you doing it unremarked.*

## Half 2 — the hook

`pre_tool_use.py` gained rule 4: `_is_plan_quiet_path` (QUEUE.md, SPEC.md, `LOG/`,
the session's own planning notes, alongside the existing memory, research,
scratchpad and INBOX exemptions) with an **ask-never-deny** response for
everything else. Beside it, the unscoped-build surfacing: a build working file
with no `Files:` section fails open and is otherwise indistinguishable from a
contained one, so it now asks once — via `_fire_once`, because it describes a
standing condition rather than one write, and repeating it every edit would train
the user to dismiss it unread.

**Ask-never-deny is load-bearing and a rebuild must not "improve" it into a
denial.** In a build there is a file list agreed in advance, so a surprise means
drift and denial is right. In planning there is no agreed list, the user is
present, and a legitimate write is authorised in one word. The gate's job is
visibility, not containment. That reasoning is written into the function's own
docstring so a later reader meets it before touching the branch.

## Two decisions taken at the keep-step, both honoured

**Merge, never paste.** `4f5e167` added the shell-write guard and the computed-path
denial *after* the revert, so lifting rule 4 wholesale from `455082b` would have
clobbered protections that commit never had. The current file was re-read and the
rule merged in. Both later protections are intact — verified live this session,
when the shell guard correctly blocked a computed-path write.

**Keyed on the build working file being absent, not on "a planning session."**
That is what the code can see, and it is what makes the gate cover a **freeform**
session too — the same condition, which is why [resurrect-freeform-sessions]
inherits containment from here rather than inventing its own.

The three hook test suites pass.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`,
`plugin/si-plugin/docs-b/plan.md`.

**FAQ: not needed because** the visible behaviour — Claude asking before an
unusual write — is what a user already experiences from the permission prompt, and
no FAQ entry described the gap this fills.

**Routed to Captures:** none from this item.

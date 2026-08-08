# 7a4b377 — The disarm-vs-halt contradiction settled by a third route: a build session appends one dated line and nothing more

A direct contradiction found by the 2026-08-08 differential audit, filed standalone
because which rule wins was a design call rather than a repair. The settlement gave
neither side the win.

**The moment where they collide:** a /next session files a capture that corrects an
item already in the queue.

**Side one, the correction-disarms rule** in the behaviour rules' Captures section:
"A capture that corrects an existing work item disarms that item in the same act —
the filing is not complete until it has." Its first route is amend-the-corrected-item,
and only the delete route was marked as /plan's. So amending read as available to
every filing session, /next included — and that availability was the rule's whole
point, since its motivating failure was a /next-adjacent session filing a sibling
capture that disarmed nothing.

**Side two, /next's dispatch-return check:** "Halt rather than amend: rewriting a
work item is processing, and /next does not process." The stated reason was general,
not scoped to the check it sat in.

**Why a narrow reading wasn't good enough.** The two rules could be read as
governing different cases, but their *reasons* collide head-on: one says amending
an item's block is how a filing completes, the other says rewriting a work item is
processing and therefore never /next's. A session holding both, meeting a
correction mid-run, cannot tell whether writing into the corrected item's block is
mandatory or forbidden. The second route — move it below the line — collided
harder, since repositioning against the readiness line is exactly the call reserved
for /plan.

**The settlement: a build session may append ONE dated line to the corrected item —
"correction filed, see [slug]" — and nothing more.** That satisfies the disarm
rule's purpose, because the next reader meets the correction at the item rather than
beside it; and it doesn't violate next.md's reason, because no prose is rewritten,
no readiness changes, and nothing moves. Rewriting an item's content and moving it
below the line stay /plan's alone.

**Both failure directions are real, and both had happened here — which is what
decided it rather than argument.** Not-amending: a /next run found another item's
file list pointing at a folder deleted the same day, filed the finding beside it
rather than amending, and that item then sat cleared-adjacent for a day carrying
prose that would have sent a build at a file that does not exist — repairable only
because a planning session happened to reach it. That is the disarm rule's
motivating failure recurring *after* the rule shipped. Amending-too-freely: a build
session repositioning items against the readiness line is an unattended run editing
the boundary that governs unattended runs. A one-line append is the largest move
that carries the first risk's fix without incurring the second's.

**Why this isn't the invented escape the anti-invention guardrail forbids**, stated
in the rule itself so nobody has to re-derive it: no new state, no new marker, no
new shelf. The appended line is ordinary prose inside the item's existing block, and
the item stays where it is. An existing route is narrowed; no new place to put
things is created.

next.md's reason was rewritten rather than merely narrowed in scope — it now says
that reworking an item *around an answer that has come back* is processing, because
it decides what the item now asks for, and explicitly notes that this doesn't bar
the one-line append.

**Files touched:**
- `plugin/si-plugin/docs-b/plugin-behaviour.md` — Captures: the three routes split into an in-/plan set and a one-route set for everywhere else, with the reasoning and the anti-invention note.
- `plugin/si-plugin/docs-b/next.md` — the walk-through branch's halt reason narrowed to its own dispatch-return case and pointed at the append.

**Routed to Captures:** none from this item.

**FAQ:** not needed because this governs where Claude writes a correction internally; a user sees the same corrected queue either way.

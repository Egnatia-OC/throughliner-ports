# 47966bb — The planning working file is deleted from the method outright; the close reads the queue's own diff instead

Filed 2026-08-14 by Claude at the opening of a /next run, from a message another
project running throughliner left in this project's INBOX.

**What was reported.** Their user objected, unprompted at the end of a clean
planning session, that the interminable /plan close-out was supposed to have been
retired months ago and rolled into /done, and that she did not understand how it
keeps coming back and gaining steps. The trigger was the session mentioning "the
planning record the close reads" — an artefact she did not recognise and had to ask
about.

**What the docs actually said, which is the interesting half.** `plan.md`'s final
section was unambiguous that there is no close-out phase in /plan. But /plan
simultaneously owned close-shaped obligations around a `_plan-<session-id>.md` file
— create it when processing begins, update it at each beat transition, append every
item with its disposition, record skipped slugs — plus a requirement that the close
carry a `Planning state:` line naming the file or naming its absence. The phase was
removed and the obligations were not, and from inside a session there is no
experiential difference between a close-out phase and a set of artefacts /plan must
produce for the close.

**The conformance half needed no doc change and must not be "fixed" by loosening
the doc.** Their session had written the state file once in bulk at the very end
rather than incrementally, which is exactly what the incremental requirement exists
to prevent — and their report was honest enough to flag its own non-compliance. The
session that processed this item created its record at the start and updated it
after each item, so the requirement was followable and theirs simply slipped.

**Decided: the file goes entirely, and the argument is Alex's.** Claude first
recommended shrinking it to the skip record, on the ground that every other thing
it holds is already written into the item's own rationale in `QUEUE.md`, so
`git diff HEAD -- QUEUE.md` recovers all of it mechanically — the same argument the
method already makes for preferring a generated digest over a paged read. She
defeated the shrink in her words: the close only runs about ten percent of the
time, because you have to know to ask for it. So a file is written every planning
session to serve a reader who mostly never arrives, and the other nine times it is
left behind as debris the next session's start reports as an orphan. Claude's
counter — that the record must be written during /plan because a long session loses
its early turns — is true and beside the point, which she said plainly: it applies
to the existing arrangement equally, so it distinguishes nothing.

**What is given up, stated so it is not rediscovered as a loss.** Skips stop being
recorded anywhere, so a skipped item returns at the top next session and is offered
again. That is already the documented, accepted cost of making skip move nothing,
so this extends an accepted trade rather than making a new one. The
resume-after-interruption path is unaffected: `QUEUE.md` is on disk either way.

**It disposes of the sending project's complaint completely rather than trimming
it.** Their user met an artefact with no command behind it, referred to as though
she should recognise it. She never could: it had no trigger, no skill and no purpose
she could act on. Deleting the thing is a stronger fix than explaining it.

**Two hook changes, traced by grepping the literal name rather than written from
the item's file list.** `pre_tool_use`'s quiet list no longer treats a `_plan-`
write as expected — it is now exactly the surprise that gate should surface — and
`session_start` stops looking for one as this session's own. One deliberate
departure from the item's text: it called `session_start`'s plan branch dead, and
detection of a *legacy* `_plan-` file left by an older build was kept, because such
a file may hold the only record of what that session did. What was removed is the
ability to treat one as this session's own, which is now impossible by construction.

**One consequence found by running the suites rather than by reading.** The
dirty-tree warning was suppressed on either an active build or an active plan, and
the second condition no longer exists — so it now fires on a /plan mid-session.
That is a false fire whose message ("/done will pick them up") is true anyway, and
it is recorded in the hook rather than left to be rediscovered.

**Suites:** all six under `resources/testing/` pass.
`test_plan_quiet_list.py` failed on the assertion this item repeals and was updated
with Alex's approval — the `_plan-` case now asserts that such a write asks.

**Rule gate: run** — pure repeal. A close obligation and a working-file lifecycle
both removed, nothing added.

**Retired:** `Planning state:` — the LOG line naming a planning session's working
file, retired with the file itself.

**FAQ:** removed the entry "What is the `_plan-...md` file? Should I edit it?" from
this project's FAQ and from the shipped template, with both index lines.
User-facing removal, so the sync obligation applies here as a deletion.

**Files touched:** `plugin/throughliner/docs-b/plan.md`,
`plugin/throughliner/docs-b/done-plan.md`, `plugin/throughliner/docs-b/done.md`,
`plugin/throughliner/hooks/pre_tool_use.py`,
`plugin/throughliner/hooks/session_start.py`, `FAQ/faq.md`, `FAQ/index.md`,
`plugin/throughliner/templates/faq-template.md`,
`plugin/throughliner/templates/faq-index-template.md`,
`resources/testing/test_plan_quiet_list.py`, `resources/retired-terms.md`.

**Routed to Captures:** none. A reply to the sending project is owed.

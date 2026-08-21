# [HASH] — /rescan now names the session it is in and hands back, instead of sending the work away

Build entry. The planning entry that processed this item is
`2026-08-21-rescan-does-not-hand-back.md`.

**Why this was worth doing.** The user raised it mid-/plan, from using /rescan before the
close on every planning session: once it had run she was no longer in /plan and had to
run /plan again, which defeats the reason it was made a separate skill. Her sharper
second point: what a re-scan turns up is often needed to finish the planning work that
just happened, so it should land in the session that still has those items in mind
rather than waiting for a planning session that comes after a build.

**Her premise was tested against the documentation and does not hold, which is what made
this fixable.** `resources/research/skill-content-lifecycle.md` records Claude Code's own
words: an invoked skill's content "enters the conversation as a single message and stays
there for the rest of the session." So nothing ended and `plan.md` was still present and
still governing for every turn after /rescan ran.

**So the defect was in how `rescan.md` finished — and there were two, the second
stronger.** The step said "Recommend nothing else", with a sound stated reason: close
machinery accumulating at the end of a chat pulls the whole chat toward ending. That
reasoning is untouched. What was wrong is that a step saying "stop here" and naming
nothing to go back to reads as the end of the conversation's work. And worse, the step
did not merely fail to hand back — it *positively sent the work away*. Its wording was
*"a planning session decides what happens to each one."* Read inside a planning session
still running, that sentence is false: **this** one can decide them, and /plan is
entitled to, since processing a capture is exactly what /plan does. A missing
instruction is an omission; this is a statement that misdirects, which explains why the
effect held even when nothing had ended.

**What was built.** Step 3's heading becomes "Say what happens next, then hand back".
The repealed sentence is replaced by wording naming the planning session the chat is in
where one is running, with the reason stated operatively. The hand-back is added as its
own provision: resume whatever was running and carry on, a return rather than a close,
with nothing to restart because the skill's instructions are still in the conversation.

**The ripple was traced by grep at processing rather than written from the discussion.**
The repealed string reached three live sites: `rescan.md`, and line 551 of both the FAQ
template and its copy. Two further hits were excluded by name and verified untouched at
build time — line 142 uses the phrase about how SPEC edits happen, a different subject,
and line 168 describes /done's lighter version of the same scan, where leaving the
sorting for the next /plan is right because /done really is closing. The acceptance grep
now returns only those two, the queue item, and the generated build view.

**Two refusals stand.** Rewriting all five procedure docs to end conditionally: the
user's own evidence is that a terminal step is usually correct, and with no readable
signal a conditional ending guesses — split to
`[procedure-docs-cannot-tell-finished-from-interrupted]`. And a general "re-run /plan
afterwards" instruction: the skill content never left context, and auto-compaction is
the only case where re-invoking is needed, which is unrelated to another skill being
invoked.

**One thing checked in the code and worth keeping.** None of the hooks is bound to a
skill — all four register against Claude Code's own events. The scope-lock looks
skill-bound and is not: `pre_tool_use.py` decides a session is a planning one by the
*absence* of this session's build working file. So the enforcement was never at risk,
which narrowed the fix to two sentences in one document rather than widening it.

**Files touched:** `plugin/throughliner/docs/rescan.md`,
`plugin/throughliner/templates/faq-template.md`,
`plugin/throughliner/templates/faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none from this item.

**FAQ: updated** — the answer describing the old behaviour reworded, plus a new entry,
"If I run /rescan in the middle of something, do I lose what I was doing?" It fires on
its own test: today users re-run /plan after a /rescan, and after this they do not.

Rule gate: run — admitted as an amendment to `rescan.md`'s existing final step, subordinate rather than freestanding, and sited in a fetched procedure doc so no always-loaded slot is spent. **The eviction is the "a planning session decides" wording, repealed outright at all three live sites.** Failure evidence is the user's report of the same outcome at every planning session, plus the documented mechanism showing the belief the wording created was false. **A hook was considered and refused:** nothing mechanical can read whether a conversation resumed a procedure.

Depth: short. Built and confirmed.

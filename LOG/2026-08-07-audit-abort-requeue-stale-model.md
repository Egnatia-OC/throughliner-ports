# [HASH] — next-build.md's abort path aligned with the leave-in-place queue model: an aborted item was never removed, so there is nothing to return

The audit flagged two incompatible models and said honestly that it could not tell which text was stale. **Reading docset A answered it in one grep, so this was never a design call.** A's `next.md` removes the run's Claude-work items from QUEUE.md **up front** — its own text gives "the queue free for other sessions" as the reason — so "return it to Processed" is coherent there, and A's `next-build.md` does not carry the phrase at all. Docset B changed the model in `next.md` to leave items in place until each one's completion tick, with its own reasoning recorded (a run that dies partway leaves the queue holding exactly the work never done), and did not carry that change through to `next-build.md`'s abort path. So `docs-b/next-build.md` was the stale text and there was no fork left to decide.

**Recorded plainly: this belonged in the bulk-keep set.** It was held back only because the audit could not call which side was stale, and settling it cost one grep. Worth remembering the next time an audit reports incompatible texts — *"the audit could not tell"* is not the same as *"the user must decide"*.

The abort step now says the item is left where it is, because it was never ticked and so is still sitting in Processed. It adds that repositioning is warranted only where what was learned during the attempt changes where the item should sit — a judgment about order, not a recovery step, going through the mover like any other move. And it names what the old wording actually did: read literally, "return it to Processed" performs an **insertion**, which is not /next's to make — a run removes items from Processed and never inserts them, and the queue lint flags a heading appearing under Processed during an active build.

The surrounding steps — appending captures surfaced during the attempt, appending the reshape direction, telling the user to run /done — were correct and are unchanged, beyond dropping "item returned" from the reshape trigger.

**Docset A is not in scope and needs nothing:** it is internally consistent under its own up-front-removal model, and the freeze bars development in it regardless.

Grouped with [audit-claude-raised-closer] at the user's approval — those two are the only items touching this file and nothing else, so they ran as one coherent pass rather than two sequential edits, adding no files to either.

**Files touched:** `plugin/si-plugin/docs-b/next-build.md`
**Routed to Captures:** none

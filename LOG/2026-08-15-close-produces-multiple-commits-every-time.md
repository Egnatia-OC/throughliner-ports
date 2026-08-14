# [HASH] — A session makes exactly one commit, and the post-commit tail makes none

Captured by the user in her own words: the close is getting very messy every time with many commits. Her word was *every time*, so this was never about one untidy session.

Three designed behaviours produced it, each individually defensible, which is why this was a design decision rather than a bug fix. `done.md` specified that a capture filed in the post-commit tail is a working-tree edit riding into the next session's commit — so a close was specified to leave the tree dirty. The session-start hash backfill edits the entries the previous close wrote, guaranteeing every session opens dirty regardless of what the close did. And the post-close append offer exists precisely because work continues after the commit, each append being another commit. The build could not simply forbid one; it had to decide which was wrong.

**The decision: the tail loses its commits, not its work.** Work genuinely does arrive after a commit — a question answered, a reply sent, an observation worth keeping — and the method already decided that recording it beats pretending the session ended. So the thing to remove is the commit per increment. The close commits once; everything afterwards is written to the working tree and carried by the next close.

The cost is stated rather than discovered: the tree is dirty between one close and the next, always. That is accepted, and it is what makes the dirt legible. Uncommitted changes at a session's opening now mean one thing — the previous session's tail, plus the backfill — so a session recognises the signature instead of investigating it, exactly as it already does for the backfill alone. Dirt that is always the same shape can be read at a glance; dirt that is sometimes a tail and sometimes an unexplained commit cannot. The close's staging check therefore keeps its teeth, because tail-shaped dirt is now sharply describable and anything else still gets the full treatment.

Two intuitive answers were refused and are recorded so they are not re-proposed. Requiring the close to leave a clean tree cannot be done without either forbidding post-close work or committing each increment — the first loses the record, the second is the defect. A lightweight second close over the tail is another commit wearing a different name, and it needs the user to declare when the tail has ended, which nothing can tell them.

`session_start.py` was checked and left unedited: the backfill is now specified as part of the tail that rides into the next close, so it needed no change.

**This build authored a rule and wrote its own gate disposition, which the gate's design says cannot work.** The item's disposition honestly said "not needed at processing", because at processing this was a decision about which item runs and when, and it told a build that found itself authoring a rule to halt. The build then authored one — because the item's body instructed it to decide exactly this shape. Halting would have stopped a run over an item doing what it was told. So the gate's four questions were run at build time and the answer recorded, with the departure flagged to the user in chat rather than buried: the failure is recurrent and pointable, Claude does not do it unprompted (the doc specified the opposite), it applies to every close, and no hook can detect "is this the tail?". It is an amendment to `done.md`'s existing tail specification, spending no always-loaded slot. What it cannot be is an admission decision — a disposition written after the rule is designed can describe, not refuse. Filed as `[build-wrote-its-own-gate-disposition]`, because the gap is a class of item, not this one item.

SPEC was left alone deliberately. Nothing in it becomes false — its close paragraph claims no commit count and no clean tree — so there was no contradiction to halt on, only an addition. Adding product truth is the ask-first route, and asking would have stopped an unattended run for a sentence nobody is blocked on. Filed as `[spec-silent-on-one-commit-per-close]`.

Rule gate: run at build time — see above. One rule amended in `done.md`; no always-loaded slot spent; nothing evicted.

FAQ: not needed because the user's actions are unchanged. They will keep seeing the uncommitted-changes line at session start, which they already see; what it means is now stable rather than variable.

**Files touched:** `plugin/throughliner/docs-b/done.md`.

**Routed to Captures:** `[spec-silent-on-one-commit-per-close]`, `[build-wrote-its-own-gate-disposition]`.

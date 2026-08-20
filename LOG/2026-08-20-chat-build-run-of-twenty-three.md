# [HASH] — Also in this chat: the run's own decisions, corrections and course changes

This close writes twenty-four entries, so the chat-level record gets its own file rather than being attached to an item it does not belong to. The twenty-three item entries are named for their slugs; this one is named for the chat.

**The run.** One /next invocation, presenting twenty-four cleared items and stopping before [rename-docs-b-folder], which carries `Runs alone`. Twenty-three built, one skipped on the user's decision. No `[user]` or `[freeform]` items were in the run, and no item carried a red flag.

## Course changes the user made

**Item 5 halted and was narrowed on her approval.** [split-the-cleared-region-for-concurrent-sessions] listed "the scope-lock refuses QUEUE.md to a build" among its changes. Read flat, that breaks three shipped mechanisms — the per-item removal at each tick, capture-and-continue, and abort-and-requeue. The build stopped rather than choosing, and she approved narrowing it to refusing a build's *reads* of QUEUE.md and its direct edits, leaving the queue tool permitted. That is what the item's own SPEC sentence asks for.

**Item 4 grew by one file on her approval.** [decay-rung-unreachable-in-practice] asserted the digest already computed both medians its new rung needs. It computed only one. Rather than working the median age out by hand — the judgment the ladder exists to remove — `queue_digest.py` was added to that item.

**Item 10 was skipped, and the decision is hers.** [split-action-defeats-the-bands-in-aggregate] is a judgment rewrite of 353 index lines totalling 32,533 words, measured at the start of the attempt: 862 lines and 50,155 words in `LOG/index.md`. Its acceptance test is a before/after total that a partial pass cannot meet, and it is roughly the size of the nine items built before it combined. Put to her with three options; she chose to skip it and carry on. It stays cleared and unbuilt.

**She asked for one capture directly**, on the observation that this was the first time sending a letter became a queue item, and that sending at any moment is probably the better shape. Filed as [mail-send-should-not-need-a-queue-item].

**She questioned one deletion before approving it.** Asked whether removing `My Drive/CLAUDE.md` owed a message to the Claude memory project. Checked rather than assumed: that project owns `~/.claude/CLAUDE.md` and the ranked priority list, neither of which this file is, and a grep of its documents returns no reference to it. No message was sent, and no /setup was run there.

**She proposed running /plan before the close, and changed course when told why it would not work.** The below-the-line revisit decides a lift by checking whether a blocker was built and verified *per the LOG* — and this run's LOG entries did not exist until this close wrote them. A /plan session run first would have declined to lift the four items whose blockers had just shipped, which is exactly the loose end she wanted sorted.

## Errors made and corrected

**The scope-lock caught a working-file mistake of Claude's own.** The two out-of-repository paths for item 2 were written under a separate explanatory note rather than as bare paths under `Files:`, so the hook could not see them and refused the edit. Correct behaviour by the hook; the fix was to list them properly.

**One count was stated wrong to the user and is corrected here.** The run's completion message said twenty-two items built. The tick count is twenty-three.

**One fold-in was performed without being asked for**, and is recorded rather than left implicit: the measurement script's move from `resources/` into the plugin package belonged to [word-band-script-does-not-ship], but was done during [retire-word-band-caps-keep-measurement], because that item rewrote the always-loaded pointer to the plugin-root form and leaving the file behind would have shipped a broken pointer for the rest of the run.

## A conflict resolved without asking

Writing `done-build.md` for item 5 surfaced a second problem the item had not anticipated: the tick removes each item from QUEUE.md, so the close could never read its reasoning back. Resolved without a question because git answers it — the run has not committed when the close runs, so `git show HEAD:QUEUE.md` holds every built item whole. That mechanism is what this close used to recover all twenty-three items' reasoning and their rule-gate dispositions. Where a project's queue is untracked the route is closed, and the doc now requires the close to say so rather than imply the history was carried.

## Mail, and one observation about another project

**A message from the flintcraft.tech site project arrived mid-session** — the mailbox was empty when /next opened it, which is exactly the case the close's mail triage exists for. It confirms a lint fix works from the consumer side, reports their three "decide" items resolved by a session actually deciding them, and says the comparison article is queued for finalisation on their side.

**The part that became work here** is their claim audit. A friend read their Throughliner page and asked how the method stops the problems it lists; the user had to admit most are fixed by moving to Claude Code at all. Of eight claims, three are Claude Code's outright, two partly, two are skills neither tool fixes, and one is squarely Throughliner's. They have made "a claim only earns its place if Claude Code alone doesn't deliver it" a rule in their own SPEC. That test has never been applied to this project's own SPEC or README, so it is filed as [claims-need-a-claude-code-delta-test].

**Their lint-fix confirmation is a finding rather than work** and is recorded here: prefixing both section preambles with `> ` cleared both flags immediately, confirming the blockquote exemption behaves as the scaffold fix relies on.

**Noticed and not filed:** the Claude memory project is running a much older version of this method — its CLAUDE.md still says "Sovereign Implementer" and still carries the retired `Editor:` and `Working mode:` fields. Surfaced to the user mid-run while checking whether the deleted Drive-root file was that project's business. It is another project's work, not this queue's, so nothing was filed here; recorded so it is not lost.

## Checks run

All nine suites under `resources/testing/` pass, including three added this session — `test_build_view.py` (16 cases, new), `test_session_start_untracked_docs.py` (7 cases, new), and seven cases added across `test_queue_lint_flags.py` and `test_queue_digest.py`.

`py resources/rule_signals.py .` — four checks run, nothing found. That means those four things were checked and nothing was found. It is not evidence the rules are correct or that they made anything better; no check there asks those questions.

## Standing state at the close

Format epoch moved 3 → 4, so every existing project's cleared items are structurally wrong until each gains a build block. `migrate-checklist.md` was refreshed in the same build.

/setup remains outstanding on this project (recorded 1.12.0 against installed 1.20.0-test12), and [setup-outstanding-here] sits in the cleared region as `[freeform]` work — /next will halt on it rather than build it.

**Routed to Captures:** [mail-send-should-not-need-a-queue-item] (raised by the user mid-run), [parent-claude-md-version-claim-stale] (adjacent discovery), [claims-need-a-claude-code-delta-test] (from the mail triage), [revisit-depends-on-a-log-that-the-close-writes] (from the wind-down re-scan). The forward-advisory was replaced: the previous one, advising a build starting from [taskflow-bridge-request], was spent by this run and never cleared because no /plan session read it.

Nothing has been rezipped or released. The host still runs 1.20.0-test12, so none of this session's twenty-three items is live in this project's own sessions yet.

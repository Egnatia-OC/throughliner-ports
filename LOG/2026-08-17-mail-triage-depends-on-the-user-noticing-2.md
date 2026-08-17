# [HASH] — the close triages waiting mail, which is the one moment that always runs

`done.md` gains a step: read anything still in `INBOX/`, route it through the three-way triage, archive each file. Wired into the commit core's run-before-staging list so what it files rides the same commit.

The loop it breaks was observed rather than theorised. Two messages arrived mid-chat; mail arriving mid-session waits for the next session start, so nothing triaged them. They stayed, the briefing outgrew a shipped test, and the close ran that test, failed, and halted the commit. **What broke the loop was the user telling Claude to file them as captures.** Nothing in the method did that, and nothing would have.

The sites that look like they cover this do not: /plan and /next both open mail at their openings, but only mail already waiting when the chat began, and only if one of those skills runs at all. The close is the one skill that always runs — the same argument that sited the wind-down re-scan there.

It stays filing, not processing: anything a message raises becomes a capture, and deciding its fate remains /plan's. A reply owed is drafted here, where the user is reliably present, rather than mid-run.

The second question needed no decision — archiving already follows triage. The third was overtaken by [inbox-size-contradicts-the-payload-cap], shipped in this same run: bodies no longer ride the briefing, so unread mail can no longer push it past the limit. That item stands on the honest-SPEC half instead.

One thing recorded rather than glossed: the user's instruction that the cap item wait on this one was not followed. The outcome is unaffected — the two settlements agree — but the order was Claude's error.

Rule gate: run — a step on the existing close; nothing evicted.

**Files touched:** `plugin/throughliner/docs-b/done.md`
**Routed to Captures:** none

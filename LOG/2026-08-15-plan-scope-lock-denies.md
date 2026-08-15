# [HASH] — The planning scope-lock now denies against a standing list, and the lookup it was ordered to do saved it from shipping a break

The user decided this, in her own words: plan needs a scope lock, we had it before the reversion, she wants it back, full stop — and she said plainly that she is sick of re-arguing it, having done so for weeks. Her reason is the whole argument: just because Claude asks the user for an edit does not mean the user reads the request in full and understands what it means. An ask that gets waved through is not consent. The design below is Claude's; the decision is not.

`_is_plan_quiet_path` gave a session with no build working file an ask on any write outside a quiet list, and its comment instructed future sessions not to "improve" that into a denial. Both are now reversed. The comment's justification was also wrong on its own terms and is evicted with it: it read "here there is no agreed list", which is false. A build has a list agreed for one specific piece of work; a planning session has a standing list, the same few paths every time. So nothing needed restoring — and in particular the `_plan-<id>.md` working file deleted from the method on 2026-08-14 does not come back, because a fixed list needs no per-session file to hold it.

This ships no new rule. `plan.md`'s ground rules already open with "never build — work that changes anything outside the quiet list is queued, not done here." The hook makes an existing rule mechanical, which is the gate's fourth admission question answered: escalate to a hook where the failure's cost justifies the standing friction, and the user has judged over weeks that it does.

## The lookup, and what it caught

The item carried an ordering note rather than a `Blocked by:` line — deliberately, because a blocker would have sent it below the readiness line and out of sight, and she has waited weeks for it. The note asked that the pre-reversion scope-lock be located first, since it had never been found and this design might be re-deriving something worse. That lookup was two git commands and it was run before the build finished.

It found the gate at `19ff11b^`, the commit immediately before the 2026-08-09 emergency revert, under the same function name. It was an **ask**, not a denial, and said so in terms: "it is a quiet-list rather than a boundary: everything else ASKS, nothing is forbidden." So there was nothing to restore and the new design is not a worse re-derivation. Her memory of having had a planning scope-lock is correct; what she had was the ask.

More usefully, its list carried one path the new design's did not: `FAQ/`, on the recorded ground that the close's FAQ disposition is a mandated edit, and that a required step which prompts every time trains the user to click through the ask that matters. That is the same argument that put `resources/research/` on the list — a shipped duty the lock would otherwise break. The item's own writable list omitted it, so the build as specified would have denied this project's own planning close the ability to write an FAQ entry. `FAQ/` was added mid-build with the user's approval, and the reason is now written into the hook so it is not lost a second time.

The old gate also left `templates/` off its list on purpose: editing a template changes what every future consumer receives, which is exactly the class of change the gate exists to stop happening during planning. The new deny agrees, and that reasoning is now recorded too.

## What it costs

Stated rather than discovered. A genuinely needed write outside the list now stops the session and becomes a queue item, where before it was one sentence. That is the accepted cost and it is the point — the stop is what makes the write visible as a decision.

## The suite

`test_plan_quiet_list.py` only ever checked which paths were on the list, and the list itself is barely changed — so as it stood it could not tell an ask from a denial, which is now the entire gate. It gains an end-to-end block that drives the hook as a subprocess with a real payload and asserts the decision, plus list cases for `FAQ/` and for the templates exclusion. All six hook suites pass.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `plugin/throughliner/docs-b/plan.md`, `SPEC.md`, `plugin/throughliner/templates/faq-template.md` and `faq-index-template.md`, `FAQ/faq.md` and `FAQ/index.md`, `resources/testing/test_plan_quiet_list.py`.

**Routed to Captures:** [prior-plan-scope-lock-found] — what the lookup found, so the open item is not re-processed as though the question were still open.

Rule gate: run — no rule admitted; an existing rule gains mechanical enforcement. One false justification evicted in the same move. No text added to the always-loaded corpus.

FAQ: updated — new entry, "In a planning session Claude wouldn't edit a file and put it in the queue instead. Why?", written into both the shipped template and this project's own FAQ. The trigger is met at its strongest: a consumer's planning session that today answers a question in one word will instead stop, and the write becomes queued work.

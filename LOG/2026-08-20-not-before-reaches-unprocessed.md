# b485ee3 — `Not before:` reaches captures, so work waiting on the world stops being re-offered

`Not before: YYYY-MM-DD` is the one hold that resolves itself — nobody confirms it and the hooks read it off the calendar. It was available only to an item in Processed, and Processed requires passing the keep check, which an entry with nothing to build cannot pass. So the hold designed for "come back later, nobody needs to think about it" was out of reach for exactly the entries that wanted it, and they were offered again every session.

The failure evidence came from one planning session: [standing-audit-programme] reached its third skip for the reason both earlier sessions gave; [approval-flow-token-doubling-simplification] had been re-offered since 2026-08-01 against a GitHub issue with no maintainer response; and [taskflow-personal-bridge] was filed and deferred within the hour, waiting on another project's reply. None of the three can name a queue item as its blocker, because nothing in this queue can do what each is waiting for.

The prior refusal was cited rather than walked past. plan.md's skip rule bars a durable marker for skips and bars a file to hold them, as a phantom queue state — but what that refused is a record of "Claude skipped this", written by the session that skipped it. This is a date approved at processing, on work waiting on the world rather than on anyone's attention. Put to the user, who ruled the refusal does not reach it.

**The build's own judgment, and the one thing it refused.** The lint's malformed-date warning now spans both sections, because an unparseable date holds an entry out of view forever and nothing else in that check looks at Unprocessed at all. The above/below position warnings stay scoped to Processed, and the second new test case is what pins that: an Unprocessed entry always sits below the readiness marker in file order, so a position check applied there would fire on every dated capture. Widening the whole check would have been the easy symmetrical move and it is wrong.

Three readers were checked before the description was written. `queue_digest.py` already prints `Not before: <date> -> passed/ahead` on every entry, ungated by section. `session_start.py` scopes its date scan to Processed and stays that way, since its facts are about *held* work. Only `post_tool_use.py` needed changing.

No epoch bump: the field is optional, so nothing in an existing project becomes structurally wrong.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the capture line-format block, plus a new block giving the field its two meanings and the approval condition), `plugin/throughliner/docs-b/plan.md` (a pass-over at the ordering step; a propose-and-approve step at skip-to-defer), `plugin/throughliner/hooks/post_tool_use.py` (`_check_blocked_by` restructured), `resources/testing/test_queue_lint_flags.py` (two cases), `plugin/throughliner/templates/faq-template.md` and `faq-index-template.md` with their `FAQ/` copies. **Checked and excluded:** `queue_digest.py`, `session_start.py`.

**Routed to Captures:** none.

Rule gate: run — admitted as an amendment widening one existing field's scope, subordinate to the capture line-format block that already defines it, so no freestanding rule. **The eviction is the below-the-line-only restriction on `Not before:`**, repealed in the same move. Failure evidence is three instances in one session. **A new state was not proposed and must not be**: this is one field reaching one more section, which is why it survives the phantom-state refusal that has defeated three earlier proposals here.

Tick: done, confirmed — the queue lint suite passes with both new cases.

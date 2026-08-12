# e5d169b — A board signal is satisfied by an open item in either queue section

The board's printed guidance said a signal files a capture in Unprocessed "unless an open capture with that slug already exists" — naming a section for the filing and leaving the satisfied-test unqualified. A session could read it as requiring the item to still be *in* Unprocessed. On 2026-08-12 a single /plan processed all four board-filed captures into Processed at once, so under that reading the next session would have filed four duplicates on top of four items that were not merely open but designed, kept and cleared: the signal firing loudest exactly when the work was furthest along.

The guidance now states that any open work item carrying the slug satisfies the signal, in **either** section, and that only deleting it re-arms the signal. It also says plainly that nothing here scans the queue — the script computes and prints, so the reader performs the check and the wording *is* the mechanism.

**The scan alternative was rejected with its reason recorded in the file:** `post_tool_use.py` already parses QUEUE.md for the lint, and a second parser in a second script is two things that must agree about the file's shape and will drift.

Scope shrank between filing and building and the build did not restore it: MEASURED no longer fires at all, so no satisfied-test wording was written for it. The fix covers the four signals that can still fire.

**Files touched:** `resources/rule_signals.py`
**Routed to Captures:** none from this item
**Rule gate:** not needed — printed guidance in a host-only script, not a rule in the method's text.

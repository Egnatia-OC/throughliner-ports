# 16ed591 — The keep-step now reads a mechanism before describing a build against it, as one clause on a check that already existed

Two captures filed at closes asserted how a mechanism behaves and both were wrong. One said the session-start hook reports a stuck placeholder "at every single session start, forever" and built its proposed fix on that; the hook's pattern matches only a placeholder in heading or index position, and the one in question sat in a commit field, so it never fired and the real defect was silence rather than noise. The other named three causes, two of which had been absorbed by other work within two days of filing.

Both were filed at a close, from inside the run that observed the symptom, and both were written as findings rather than as hypotheses. Neither cost anything, because both were caught at processing — but a build working from either would have implemented a fix for behaviour that does not occur.

The fix is deliberately not "check before filing". Filing is open to every session and cheap, which is right: a capture that must be verified before it can be written is a capture that does not get written. The answer belongs at the reading end, and it is one clause on the keep-step's existing second limb — where an item asserts how a mechanism behaves, read the mechanism before describing the build.

That adds no new obligation, which is why it is a sharpening rather than an admission. You cannot honestly state what changes inside a file whose behaviour you have not looked at; the limb already demanded the first, and this names the second.

The do-nothing option was weighed on the honest ground that the correct behaviour occurred both times anyway. It lost on the processing session's own evidence: twice in that session the keep-step needed a mechanism's actual behaviour and reading it changed the item. `session_start` turned out to filter board output per line and never read the header, which established that one item was contained and needed no hook change; and the queue lint's history with `[freeform]` turned out **not** to settle whether the new `Runs alone` marker needed anything from it, so that item was rewritten to say verify either way rather than guess. Neither fact was in the capture that raised it, and both came from opening the file.

This run then exercised the clause twice more. The `Runs alone` item's instruction to verify the lint was carried out and returned "no change needed" for a reason nobody had written down — the lint is deny-list by design. And the stale-fixture item's guess that a test payload needed a session id was reversed by reading the function, which matches by shape and takes no id.

The limit: this governs the keep-step only. A capture whose mechanism claim is never processed — deleted, or built straight from Unprocessed — passes untouched, and nothing checks the reading happened.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment, consuming no slot. Parent named: the keep-step's second limb, which already requires stating what changes inside which files. Written as a clause on that limb, not a step of its own, and deliberately kept to a clause. Distribution: plan.md, not the always-loaded file — it fires at one moment in one skill. Eviction: nothing, since nothing is superseded. Admission evidence: two recorded wrong captures, plus four instances during processing and this run where reading the mechanism changed the build.

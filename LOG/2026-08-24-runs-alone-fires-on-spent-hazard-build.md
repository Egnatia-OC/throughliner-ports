# 3ed3db1 — Built: `Runs alone` ends the run only when this run performed the work

From the consumer report where a run correctly closed an already-done marked item and then still ended, leaving buildable work unbuilt — the hazard (paths moving under a run) had already happened outside any run. next.md's marker rule gained the arm: an item whose observable check finds all of it already satisfied closes, and the run continues; plan.md's definition carries the same clause. The rule stays mechanical, which the report rightly named as the point. The digest and view are untouched — they report the marker's position only. FAQ's runs-alone entry gained the already-done exception.

Rule gate: run — amendment to next.md's Runs-alone marker rule, rewording its trigger in place, with plan.md's definition gaining the same clause; nothing evicted. Admitted on the consumer's recorded instance under the single-instance test. Repro survives in the archived message (INBOX/archive/2026-08-23-from-chagora-runs-alone-on-completed-item.md), extra info only.

Files touched: plugin/throughliner/docs/next.md; plugin/throughliner/docs/plan.md; plugin/throughliner/templates/faq-template.md; FAQ/faq.md, FAQ/index.md (re-copied)
Routed to Captures: none
Done, confirmed: both docs carry the performed-by-this-run trigger.

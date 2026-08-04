# f832385 — Add a hook schema-conformance check and a liveness ritual step, so a silently-dead hook can't hide behind Claude's own compensation

The `session_start` hook emitted a malformed output shape and had its entire payload silently discarded, probably for a long time, and nothing caught it. Sessions kept working — Claude read CLAUDE.md and the queue directly and reconstructed roughly what the hook would have said. That compensation is the actual problem: it makes a dead hook invisible.

Two gaps needing two different tests, and neither substitutes for the other.

**Schema conformance** is now a script at `resources/testing/hook_schema_check.py`. It drives each of the three hooks with sample payloads and asserts the output against the published contract — that everything nests under `hookSpecificOutput` with a matching `hookEventName`, and specifically that the flat top-level `additionalContext` shape (the one this project actually shipped) is absent. It would have caught the original bug at authoring time; the tell that it was a real defect rather than a convention is that the other two hooks already used the correct nested form, so the codebase disagreed with itself and nothing noticed.

Writing it surfaced a failure mode worth recording in the script itself: the hooks only enforce in an *adopted* project, so a fixture without a SPEC.md produces silence for every case — which reads as passing. Two cases initially passed for exactly that reason and were caught only because their JSON assertions failed. A check that cannot fail is worse than no check, which is the same shape as the bug this whole item exists to prevent.

**Liveness** is a ritual step rather than a queue item, and that was a deliberate correction at processing. Schema conformance can't tell you the output reached a session; a correctly-shaped hook can still be dropped. The only proof is a session reporting what arrived. A queue item fires once, but this is a bug that returns silently, so it belongs attached to the restart the Rezip and Push rituals already demand — it now fires at every rebuild. The capture had also called this irreducibly a `[user]` step; by the method's own over-tag guard it is not, since Claude reads its own context and reports what arrived, with nothing for the user to witness.

The wording constraint is the transferable part: ask **what did you actually receive**, never whether the output looks right. The second question invites the same plausible reconstruction that hid the original bug. Both rituals now say so explicitly, alongside the distinction between a thing having run and a thing having worked.

**Files touched:** `resources/testing/hook_schema_check.py` (new — 10 cases across all three hooks, all passing), `CLAUDE.md` (new Rezip step 5 and Push step 12).
**Routed to Captures:** none.

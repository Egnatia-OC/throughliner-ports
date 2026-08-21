# ae84933 — The digest stops reading a filename as proof work shipped, and reports the record's kind instead

The build of [log-entry-kind-not-distinguished]. The planning entry under the same slug records the item being processed; this one records it being done.

**The defect, restated.** `queue_digest.py`'s `shipped_slugs()` did one directory listing and matched `<date>-<slug>.md`. Nothing opened the file. Its own docstring called the result "slugs whose work shipped", and that is false for every entry a planning close wrote — because a plan entry splits per item **processed**, which is settled and correct, so a discussed-and-kept item has a record named after it exactly like a built one.

**Why it is not cosmetic.** The same signal decides what may be lifted out of the held region. A blocker that a planning session merely processed has not resolved; reading its record as proof of building would release work whose dependency is still outstanding. That consequence was checked against `plan.md`'s revisit rather than assumed.

**What shipped.** `shipped_slugs()` now returns a mapping of slug to kind rather than a set. It reads each entry: `Files touched:` means built, `Work processed:` without the first means processed, neither means unknown. The read is bounded by a `wanted` set — every slug some item cites, plus every slug named as a blocker — because reading the whole folder is megabytes to answer a handful of citations. Where a slug has several records, built wins: an item processed in planning and built later has both, and the built one is the answer.

The digest prints three separate fields: `Cites shipped:`, `Cites processed:`, and `(record kind unknown)` for older-format records. `locate()` gained a `kinds` argument and now reports an absent blocker as `ABSENT, built` or `ABSENT, only processed — not built` rather than bare absence.

**`plan.md`'s claim was repealed at its live site**, replaced by the three-kind distinction with the reason written into it: the kinds are told apart by reading the record and never by its name, because a planning session and a build both produce `<date>-<slug>.md`. The below-the-line revisit's built-and-verified table was left exactly as it stands, as the item required — it was correct; what was wrong was the fact supplied to it.

**One deviation, recorded because it was a real decision.** The function was briefly renamed to `record_kinds()`, which is the honest name for what it now returns, and the rename was reverted. Four other queue items and QUEUE.md prose cite `shipped_slugs()` by name, and the rename was scope the item did not grant. The docstring now says the name is kept deliberately and that what it returns is not a set of shipped slugs — which is the smallest thing that stops the name lying.

**Acceptance, run against the live queue.** [setup-migration-gate-is-epoch-3-shaped] and [convert-cleared-items-to-build-blocks] appear under `Cites processed:` and not under `Cites shipped:`, which is the case the item named. Built slugs still appear under `Cites shipped:`. The `(record kind unknown)` arm fires on a real older-format record. Digest runtime is 0.37s, under the item's one-second bound.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py` (+58 lines), `plugin/throughliner/docs-b/plan.md`, `resources/testing/test_queue_digest.py`.

**Routed to Captures:** none from this item.

The suite gained four cases: a processed-only record not reported as shipped, an older-format record reported unclassified, a processed-only blocker not reported as shipped, and a built blocker reported as built. The `project()` helper now writes a body for each fixture entry, since the classification reads one — a built body by default, or a `(name, body)` pair where the kind is what the case is about. All 38 checks pass, and all nine suites under `resources/testing/` run green.

Rule gate: run — no rule is authored or amended. The disposition is a correction to a mechanism plus one repealed sentence, evicted at both live sites where it is stated: `plan.md`'s cited-slug claim and, written in the planning session, SPEC's. Failure evidence is one instance observed directly on screen, plus the structural argument that the same signal governs what lifts out of the held region. A hook was considered and refused: this is a script's own logic, not a thing a hook could watch. Transcribed from the item.

FAQ: not needed because the item dispositioned it — "No FAQ entry — a consumer sees a different label on a line and does nothing different."

SPEC needed nothing, and that is a pass rather than a skip: its digest paragraph already describes the built / processed / unknown distinction, written ahead of the build by the planning session that processed this item. That is the SPEC-leads-the-build shape working as designed.

# PENDING — Cycles verification walked partway: two defects found, the clean opening test deferred

`[user]` item [cycles-due-check-verification], walked through live in the 2026-08-24 /next run and **not completed** — the item stays in Processed. Actions appended as they happened.

## Walk-through record

- Record check first: read `LOG/2026-08-23-cycles-due-check-verification.md` and resumed at step 1 (create the test CYCLES.md).
- Step 1 hit a method defect in the demo consumer project: /plan there was refused the CYCLES.md write by the scope-lock, though plan.md instructs exactly that write. Filed here as [cycles-write-refused-by-scope-lock]; the consumer project later mailed the same defect formally (archived, cited in the capture).
- The demo session's recovery route was taken: the cycle filed as a queue item, processed, and built by /next in the same chat. Read the created `CYCLES.md` from here — well-formed: weekly cadence, observable the newest turn-record date (2026-08-10, honestly labelled a fixture), a fortnight overdue.
- That chat's /done ran with the overdue cycle on disk and filed nothing — the close-time check's first live test, failed. Filed as [cycles-close-check-did-not-fire]. The installed host carries the check (shipped in c904687, older than the test17 rezip), so staleness does not explain it.
- The item's original step 2 — a fresh /plan opening in that project with the file already on disk — has still never run; it is the diagnostic that separates a broken close site from a broken feature. The user deferred it. Item left in place.

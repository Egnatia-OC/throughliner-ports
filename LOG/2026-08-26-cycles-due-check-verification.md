# PENDING — Cycles verification resumed after the fix shipped

`[user]` item [cycles-due-check-verification], walked through live in the 2026-08-26 /next run. Actions appended as they happened.

## Walk-through record

- Record check first: read `LOG/2026-08-23-`, `2026-08-24-` and `2026-08-25-cycles-due-check-verification.md`. They show step 1 done, step 2 run once and failed, steps 3 and 4 not run. Resumed at step 2.
- Checked the world before handing the step over: `DEMOS/Polit Fart Announcer 1/CYCLES.md` still carries the `[weekly-listen]` definition with its 2026-08-10 fixture observable (labelled as a fixture in the file), so the cycle still reads as due. That project's queue carries no entry under the cycle's slug, and its newest commit is `a050865` from before the fix — so no opening there has yet run against the fixed plugin.
- Confirmed the installed host carries the fix: `plan.md` in the 1.20.0-test20 cache keys the cycles step to the session opening's cycles line, which is the repair built earlier today under [cycles-check-fires-nowhere]. The test is therefore live for the first time.
- Told the user the demo project is mid-plan from the last due-ness check, and her intended sequence there was /done, /setup, then /plan. Named ahead of it that the close is also a cycles site, so the /done may file the capture and the following /plan would then correctly file nothing — a pass, not a failure, and step 3's no-duplicate condition tested for free.
- **Deferred by the user** so the run could reach the release. Item left in place, not completed; the resume point is unchanged at step 2. Nothing else in the run waited on it — only [weekly-release-cycle], which is held below the line regardless.

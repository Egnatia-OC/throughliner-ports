# PENDING — Cycles verification: the opening test finally ran, and failed

`[user]` item [cycles-due-check-verification], walked through live in the 2026-08-25 /next run and **not completed** — the item stays in Processed. Actions appended as they happened.

## Walk-through record

- Record check first: read `LOG/2026-08-23-cycles-due-check-verification.md` and `LOG/2026-08-24-cycles-due-check-verification.md`, which show step 1 done and step 2 deferred. Resumed at step 2.
- Checked the world before handing the step over: the demo project at `DEMOS/Polit Fart Announcer 1` still carries its `CYCLES.md` with the `[weekly-listen]` definition, observable 2026-08-10 (a fixture, labelled as one in the file), and its git log showed no session had opened there since the doc landed in that project's last commit of 2026-08-24. So the opening check had never yet had a chance to run, rather than having run and failed.
- Corrected myself in chat on the user's challenge: I had described the cycle as "due for a fortnight", which reads as neglect. The date is a deliberate fixture written on the 24th so the cycle would read as due at once, and the file says so.
- Step 2 run by the user: a fresh /plan in that project. Its opening narration carried the advisory, a lift of [formal-spoken-line], the throughput floor, four waiting captures and the droppable skim — and nothing about any cycle. No item under the cycle's slug in that project's Unprocessed. **The opening site failed.**
- Filed [cycles-check-fires-nowhere] here: both live sites have now failed on the same installed plugin, which is a cause neither existing item names. [cycles-close-check-did-not-fire] was built earlier in this same run and its fix — a fresh disk read at close time — cannot explain a fresh opening missing the file.
- Steps 3 and 4 not run. Step 3 (no duplicate on a second opening) has nothing to duplicate. Step 4 (delete the fixture) is held back deliberately: the fixture is the only ready test case for the defect just filed.
- Also observed, and not a defect: that project's opening still offered to paste text inline. The retirement of that offer was built target-side in this run and is not installed.

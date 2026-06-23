# [HASH] — Classify user-run tests by requirement, and explain them when surfaced (done.md + plan.md + QUEUE.md + FAQ)

Built in a six-batch goal session (plugin off).

The "user-run" tag and the deferred-test roll assumed the user can run the test. That broke when two deferred lines were terminal-only and the user is desktop-only — she couldn't run them, and being asked to confirm their event confused her. The fix keys the classification on what the test *requires*, not on the user's workflow.

Changes:

- **done.md** — the Deferred tests "user-run" runnability definition now says a user-run line names its requirement in plain language ("needs the terminal," "needs a phone connected," "needs you to look at the screen"), because the requirement — not an assumption about how the user works — is what makes it the user's to run. The exemplar line is updated to show a requirement.
- **plan.md** — (1) the test-routing "user-must-run" category is defined by the requirement only a person can meet, named plainly on the line, with the why: Claude rarely knows the user's environment, so a rule resting on detecting the workflow doesn't generalize, but a test's requirement is always knowable. (2) The deferred-roll resolution now explains a surfaced user-run or external line in plain language — what it checks, what it requires, and why Claude isn't running it itself — and classifies by the named requirement. The Step 1 scan note says a line's runnability is read from the requirement it names.
- **QUEUE.md** — the two terminal-only deferred lines ([publish-marketplace-manifest], [install-self-install-branch]) are annotated "needs the terminal — Claude can't drive the user's separate terminal."
- **FAQ** — an entry on why Claude sometimes asks the user to run a test and can't run it itself (it names what the test checks and what it needs), plus its index line.

The broader "don't assume the user's environment anywhere" guard is split into its own capture ([dont-assume-user-environment], parked, blocked by this batch). Deferred host-side line written (the doc text landing correctly is a review, not a pass/fail test).

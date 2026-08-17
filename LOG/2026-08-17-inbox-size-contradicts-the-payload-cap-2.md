# [HASH] — message bodies leave the session briefing, replaced by a directive with a self-check

`session_start.py` stops inlining INBOX message bodies. It now emits the count, the filenames, an instruction to read each one before the first reply, and a self-check: the one-line mention to the user names what each message is about, and a session that cannot say that says so rather than carrying on.

The contradiction this settles was real. SPEC promised full delivery with no size limit, on the reasoning that a limit would be a bare number; `hook_schema_check.py` asserted a 10,000-character cap on the payload carrying it. Both could not hold, and a project doing exactly what SPEC described failed a shipped test — measured at 10,978 characters, halting a commit.

The cap turned out to be Claude Code's rather than ours, which is what decided the shape. Past it the harness discards the whole payload and substitutes a preview, so enough unread mail costs a session its project state and its rules directive as well as its mail.

The user's argument overturned the full-delivery decision made the day before: the same payload already carries a *directive* to read the behaviour rules, a far larger file, and that one is trusted because it has a self-check. Inlining was the expensive answer to a problem the payload had solved cheaply one line earlier. Two shapes were refused first — truncate-and-say-so, and deliver-what-fits, the second because what fits is unknowable.

The test was rewritten to assert the directive, the self-check and the *absence* of bodies. `plan.md` and `feedback-and-inbox.md` reworded; /plan's opening ask now carries the mail as a question the user answers.

Rule gate: run — an amendment to the existing delivery rule. The eviction is the full-delivery guarantee, repealed outright.

**Files touched:** `plugin/throughliner/hooks/session_start.py`, `resources/testing/hook_schema_check.py`, `plugin/throughliner/docs-b/plan.md`, `plugin/throughliner/docs-b/feedback-and-inbox.md`, `SPEC.md`
**Routed to Captures:** none

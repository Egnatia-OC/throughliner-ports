# /done procedure

Close the current session — record what happened, update docs, commit. This doc routes to a per-type close-out and states the commit core once; the sub-docs carry the type-specific steps.

## Route by session shape

Check for _build.md. The check is automatic — don't ask:

- **_build.md exists** → read it, then route by the subheadings in its Entry (same routing as /next):
  - **Build** subheading (optionally with Test) → read and follow `done-build.md`.
  - **Test** subheading only → read and follow `done-test.md`.
  - **Audit** subheading → read and follow `done-audit.md`.
- **No _build.md** → planning session. Read and follow `done-plan.md`.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit core below, then return to the sub-doc for the recommendation.

## LOG entry files

Stated once here; every sub-doc's entry-writing step points at this section.

**One text, several positions.** The session authors two texts, not four. The one-liner is the same authored text in three positions: the entry heading's summary, the index line's body, and the commit title. The rationale prose is the same authored text in two positions: the entry body and the commit body. The user approves both once — at the entry-writing step — and the commit step (commit core above) reuses them verbatim, with nothing new to read.

Each LOG entry is written as its own file under `LOG/` — never appended to a shared log file:

- **Session closing a batch** (build, test, audit): name the file after the batch slug — `LOG/<slug>.md` (e.g. `LOG/drop-log-per-release-split.md`).
- **Session without a batch slug** (planning, setup): name it by session type and date — `LOG/<type>-<YYYY-MM-DD>.md` (e.g. `LOG/plan-2026-06-09.md`).
- **Name already taken** (a re-run batch, a second planning session the same day): append `-2`, `-3`, and so on.
- The matching `LOG/index.md` line ends with the entry's filename, so a later lookup goes straight from the index line to the file.

The hash lives in the entry file's heading and the index line, never in the filename — the commit hash doesn't exist yet when the file is written, which is why the `[HASH]` placeholder pattern exists (see Commit core below).

One authoring rule: entry prose never writes the literal placeholder token — the token belongs only in hash position (the entry heading and the index line), where the automatic backfill treats any match mechanically. A prose mention is one find-replace away from corrupting the entry. When an entry needs to describe the placeholder mechanism, say it indirectly ("the placeholder", "the unfilled hash").

Entries from before the per-entry split live in `LOG/log.md` and `LOG/log-v*.md`. Those files stay in place, untouched — their entries are found by hash or title search, not by filename.

## Deferred tests

Stated once here; the build and test sub-docs point at this section.

**Scope.** This section holds only verification for shipped work. A test that fails, or a new test need that emerges mid-session, is not a deferred test — it routes to Captures, where /plan owns it as new work. Deferred tests are planned tests that simply couldn't run in their session yet.

A planned test that can't run in the closing session — host-side behaviour that only goes live after push + reinstall, a check only the user can run, an external event that hasn't fired — is written to QUEUE.md's "## Deferred tests" section, one line per test: source batch slug, what to verify, and what confirms it. The "Confirmed by:" clause carries a runnability tail naming who or what produces the confirming event: Claude can deliberately produce it (Claude-runnable), the user must (user-run), or an external event must fire (external).

Lifecycle: /done writes the line; /plan reads the section each session and rolls the Claude-runnable and user-run lines into a test batch (external-event lines wait for their event); the session that confirms a test removes its line and records the confirmation in its LOG entry. The queue line is the structural record — don't record the deferral as LOG-entry prose alone, because no later session re-reads old log prose, so a test recorded only there never surfaces again.

**Close-out backstop (every /done).** Read this section at close. If this session's own activity already produced the confirming event for a pending line, remove that line and record the confirmation in the LOG entry. This pays mainly in self-hosting, where the session's own behaviour is often the thing under test; it costs one section read when nothing fires.

## Accepted red flags

Stated once here; every sub-doc's LOG-entry step points at this section.

If a red flag was accepted this session — the user was told a security, privacy, or breach risk plainly and chose to proceed anyway — record the decision in the session's LOG entry: what the user was warned about, and that they chose to proceed. This is the informed-consent trail defined in plugin-behaviour.md Flag states; the LOG entry is where it lands. Recording is unconditional once a flag is accepted — the consent record never rides only in chat or in QUEUE.md's Red flags section, because no later session re-reads those for consent history. Nothing to record when no flag was accepted this session.

## Commit core [BRIEF, PROMPT]

Stated once here; every sub-doc's Commit step points at this section.

1. Stage explicitly — name each path: files this session changed (from _build.md Changes where one existed), method docs updated during the session or close-out (QUEUE.md, SPEC.md, REGISTRY.md, LOG/), and the _build.md deletion where one was removed.
2. Detect out-of-scope dirty paths: run `git status --porcelain` and compare what it lists against the active build's file list (from _build.md, where one existed). Any dirty path outside that list is a user edit made between or during sessions that no build staged. Surface them in a one-line summary and offer to stage them into this commit. The reason: otherwise these edits sit dirty across sessions until the push ritual's sweep catches them — this is the earlier catch point, not a replacement for that safety net.
3. The commit message is not drafted fresh — it is the LOG entry already approved at this session's entry step (see LOG entry files below for the one-text identity), in two positions:
   - **Title:** the index line's one-liner, verbatim.
   - **Body:** the approved rationale prose from the entry, verbatim.
   Both were approved when the user approved the LOG entry, so the commit step reviews nothing new. Present it by stating that identity plainly — "the commit title is the entry's summary line and the body is the approved rationale, both already approved above" — and surface only what is genuinely new. Never write a meta-description of the derivation (e.g. "the rationale as approved, plus an appended line naming the backfill…"); a meta-description reads as a third text the user has to check, which defeats the nothing-new-to-read point.
   - **Allowance for staged extras:** when the commit stages work beyond the session story — hash backfills, staleness-sweep edits, rolled-in user edits (step 2 above) — the body appends one line naming them. That appended line is the only genuinely-new text, so it is the one thing the presentation surfaces.
4. Ask the one decision the commit step still carries: "Commit and push, or just commit?"
5. Pass the message shell-agnostically. Write it to a file in the project root (e.g. `COMMIT_MSG.tmp`) and commit with `git commit -F COMMIT_MSG.tmp`, then delete the file. One mechanism on every machine — it sidesteps inline-quoting fragility (a multiline body passed with `-m` is brittle to generate: embedded newlines vary by shell, and a PowerShell here-string needs its closing token at column 0). The message file is writable at this step because the sub-doc deletes _build.md before reaching Commit (build/test/audit closes) or no _build.md ever existed (plan/setup closes), so the scope-lock isn't active on the project root here.
6. Wait for okay, then commit with `git commit -F` — and push if the user chose to push.

The LOG entry keeps its `[HASH]` placeholder. The session-start hook backfills it automatically at the next session, as a working-tree edit that folds into that session's commit — no amend, no two-commit flow.

## Rules

- Do NOT skip the sub-doc's judgment steps even if the user says "just commit."
- Routing is automatic. Don't ask — check for _build.md.

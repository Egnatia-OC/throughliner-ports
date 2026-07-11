# /done procedure

Close the current session — record what happened, update docs, commit. This doc routes to a per-flavor close-out and states the commit core once; the sub-docs carry the flavor-specific steps.

## Route by session shape [SILENT]

Check for _build.md. The check is automatic — don't ask, and don't narrate the routing; just route:

**The _build.md read is unconditional.** When _build.md exists, read it in full before the close-out runs — regardless of how much of the session you remember. Conversation memory enriches the LOG entry (tradeoffs, learnings, colour the file doesn't capture) but never substitutes for the read. The why: a "read it only if you don't remember the session" condition hangs on Claude assessing its own memory, which fails exactly post-/clear and post-compaction — when the session feels remembered but the details are gone. Stated once here; the sub-docs route through this rule rather than restating it.

- **_build.md exists** → read it, then route by the flavor of the run's work lines (its `Run:` and `Entries:` — the same flavors /next routed on):
  - **Build** lines (no flavor tag) → read and follow `done-build.md`. A build that changed SPEC.md closes here like any other build — same steps, same commit core.
  - **`[audit]`** lines → read and follow `done-audit.md`.
  - **`[freeform]`** lines (including a _build.md from on-demand `/next freeform`) → read and follow `done-freeform.md`.
  - A run of one flavor follows that flavor's close-out. A mixed run — say a build line and an audit line built back-to-back — closes each line through its own flavor's close-out (build lines via done-build.md, audit lines via done-audit.md), writing one LOG entry per line and sharing the single end-of-session commit.
- **No _build.md** → planning session. Read and follow `done-plan.md`.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit core below, then return to the sub-doc for the recommendation.

There is no test close-out — the test flavor is retired. A check Claude can run is part of building, closed by done-build.md; a check only the user can run is a `[user]` work line, which /next hands over and which never enters a _build.md, so no /done closes it.

## LOG entry files

Stated once here; every sub-doc's entry-writing step points at this section.

**One text, several positions.** The session authors two texts, not four. The one-liner is the same authored text in three positions: the entry heading's summary, the index line's body, and the commit title. The rationale prose is the same authored text in two positions: the entry body and the commit body. The user approves both once — at the entry-writing step — and the commit step (commit core above) reuses them verbatim, with nothing new to read.

Each LOG entry is written as its own file under `LOG/` — never appended to a shared log file:

- **Session closing work lines with slugs** (build, audit): name each entry file after its work-line slug — `LOG/<slug>.md` (e.g. `LOG/drop-log-per-release-split.md`). A run that built several work lines writes one entry file per line, each named after that line's slug.
- **Session with no work-line slug** (planning, setup, freeform): name it by session type and date — `LOG/<type>-<YYYY-MM-DD>.md` (e.g. `LOG/plan-2026-06-09.md`).
- **Name already taken** (a re-run work line, a second planning session the same day): append `-2`, `-3`, and so on.
- The matching `LOG/index.md` line ends with the entry's filename, so a later lookup goes straight from the index line to the file.

The hash lives in the entry file's heading and the index line, never in the filename — the commit hash doesn't exist yet when the file is written, which is why the `[HASH]` placeholder pattern exists (see Commit core below).

One authoring rule: entry prose never writes the literal placeholder token — the token belongs only in hash position (the entry heading and the index line), where the automatic backfill treats any match mechanically. A prose mention is one find-replace away from corrupting the entry. When an entry needs to describe the placeholder mechanism, say it indirectly ("the placeholder", "the unfilled hash").

Entries from before the per-entry split live in `LOG/log.md` and `LOG/log-v*.md`. Those files stay in place, untouched — their entries are found by hash or title search, not by filename.

**Captures filed after the commit.** A capture sometimes comes up in the session's post-commit tail, after the LOG entry's "Routed to Captures:" line is already written and committed saying "none" or listing only what existed then. When that happens, the same move that appends the capture to QUEUE.md also updates this session's just-written entry — edit its "Routed to Captures:" line to include the new capture, as a working-tree edit with no separate commit. The edit rides into the next session's commit, exactly as the hash backfill does. The why: the entry is the session's record, and a capture belongs to the session it came up in, so the entry should converge to the truth of what that session produced. (The committed copy keeps the as-of-commit wording; the entry file — the canonical record — carries the correction, and git shows it landing in the next commit.)

## Checks the closing session couldn't run

The `## Deferred tests` section is retired — there is no separate test queue. The work-line model handles an unrun check directly: a verification only the user can run is a `[user]` work line, and /plan would have set it as its own line for /next to hand over; a check Claude can run is just part of building.

So the only thing /done does with a check it couldn't run is the ordinary capture move: if the closing session discovers a needed verification that isn't already a `[user]` line — one that needs the user, a device, or a reinstall before it can run — file it as a `[user]` work line appended to Unprocessed, drafting and showing the wording per plugin-behaviour.md Captures. A later /plan sorts it like any other captured work. Nothing tracks it in a dedicated section, and no LOG-only prose stands in for the queue line — an unrun check recorded only in a log entry never surfaces again.

## Accepted red flags

Stated once here; every sub-doc's LOG-entry step points at this section.

If a red flag was accepted this session — the user was told a security, privacy, or breach risk plainly and chose to proceed anyway — record the decision in the session's LOG entry: what the user was warned about, and that they chose to proceed. This is the informed-consent trail defined in plugin-behaviour.md Flag states; the LOG entry is where it lands. An accepted flag itself lives in the queue as a red-flag work line at `State: accepted` (plugin-behaviour.md Red flags), not in a dedicated section. Recording the consent in the LOG is unconditional once a flag is accepted — the consent record never rides only in chat or on the red-flag work line, because no later session re-reads those for consent history. Nothing to record when no flag was accepted this session.

## Wind-down re-scan (file-only) [BRIEF, PROMPT]

Stated once here; Commit core points at it, so it runs at every /done close regardless of session type.

Before committing, re-read this session's own discussion and surface candidate captures — things the user thought out loud but never explicitly flagged. This is the same safety net /plan runs at its wind-down, in a file-only form: /done may **file** the surfaced captures, but it does not **route** them (promote / park / drop). Routing stays /plan-only, which keeps this on the allowed side of the no-planning-in-execution boundary — filing is capture-making, allowed in any session; routing is planning, /plan's alone (see plugin-behaviour.md Routing and discipline). Frame it to the user as capture-making, exactly like the post-close capture step: surface, file the approved ones to Captures with no routing, and leave them for a later /plan to sort.

Present all surfaced candidates as ONE numbered set of fully-drafted captures for a single approval (the bulk-approval inversion in plugin-behaviour.md's [SEQUENCE] rule): the user contests by number, and only contested items then go one at a time. Append the approved ones to Unprocessed — each as its own `####` work line per the filing format in plugin-behaviour.md Captures — and add them to this session's LOG entry's "Routed to Captures:" line as a working-tree edit that rides this commit (the same mechanism as a capture filed after the commit, above).

Name the step's best-effort nature in plain words when it runs — it re-reads whatever discussion is still in view, so a surfaced-nothing result is "nothing jumped out in what I could still see," not a guarantee nothing was missed. Two things to state, not fix: a fresh-chat /done has none of the session's thinking in view, so there is nothing to re-scan — only capturing-as-you-go covers that case; and when /plan already ran its own wind-down re-scan this session, this is a harmless no-op — re-reading the same discussion surfaces the same items, already filed. Exemplar of the no-op: "Re-read our discussion — nothing came up that isn't already captured."

## Commit core [BRIEF, PROMPT]

Stated once here; every sub-doc's Commit step points at this section.

**Run the wind-down re-scan (the section above) before staging** — it files any un-flagged captures from this session's discussion so they land in this same commit. File-only: it never routes them. Skip nothing; on a fresh chat with no discussion in view it correctly finds nothing.

**Shipped-slug cross-check (work-line closes).** Before staging, when this session shipped one or more work lines, cross-check each shipped work-line slug named in this session's LOG entries against QUEUE.md's Processed section and confirm it has been removed. A work line is normally removed from Processed when /next locks its scope, so the slug should already be gone — this step is the safety net that confirms it. If a shipped slug is still sitting in Processed as active work, surface it in one line and remove it (or halt and ask) before committing. The why: a multi-line close removes many lines in a loop with no mechanical check that each actually left the queue — a prior goal session shipped fourteen work items but left one in QUEUE.md, genuinely built yet never removed, so it re-presented the next session as unbuilt and wasted the first move rediscovering it was done. Trivial for a single-line close, where the one slug is self-evidently gone; the net earns its place on multi-line, goal, and unattended closes. A planning close names no shipped work-line slug, so there is nothing to cross-check. Output stays silent unless a stray slug is found.

1. Stage explicitly — name each path: files this session changed (from _build.md Changes where one existed), method docs updated during the session or close-out (QUEUE.md, SPEC.md, LOG/), and the _build.md deletion where one was removed.
2. Detect out-of-scope dirty paths: run `git status --porcelain` and compare what it lists against the active build's file list (from _build.md, where one existed). Any dirty path outside that list is a user edit made between or during sessions that no build staged.

   **Recognise the hash-backfill signature first, and skip the investigation for it.** A dirty LOG path — `LOG/index.md` or a `LOG/<slug>.md` entry file — whose only change is a placeholder hash becoming a real commit hash, in an entry heading or the start of an index line, is the session-start hook's automatic backfill. The hook runs that backfill every session after a /done and announces it in its opening housekeeping line, so a dirty LOG path matching it is already accounted for — don't open a git diff to investigate it and don't explain it file-by-file. Fold it into this commit with at most a one-line note ("folding in the previous session's hash backfill"). The why: this exact dirt appears every single session and the answer is always "it's the backfill, stage it," so re-investigating it each time is pure delay for zero decision value.

   For any other out-of-scope dirty path, keep the full treatment: surface it in a one-line summary and offer to stage it into this commit, investigating where the change isn't self-evident. The reason: otherwise these edits sit dirty across sessions until the push ritual's sweep catches them — this is the earlier catch point, not a replacement for that safety net.
3. The commit message is not drafted fresh — it is the LOG entry already approved at this session's entry step (see LOG entry files below for the one-text identity), in two positions:
   - **Title:** the index line's one-liner, verbatim.
   - **Body:** the approved rationale prose from the entry, verbatim.
   Both were approved when the user approved the LOG entry, so the commit step reviews nothing new. Present it by stating that identity plainly — "the commit title is the entry's summary line and the body is the approved rationale, both already approved above" — and surface only what is genuinely new. Never write a meta-description of the derivation (e.g. "the rationale as approved, plus an appended line naming the backfill…"); a meta-description reads as a third text the user has to check, which defeats the nothing-new-to-read point.
   - **Allowance for staged extras:** when the commit stages work beyond the session story — hash backfills, staleness-sweep edits, rolled-in user edits (step 2 above) — the body appends one line naming them. That appended line is the only genuinely-new text, so it is the one thing the presentation surfaces.
4. No pre-commit ask — the commit always happens at /done, and its message is the LOG entry already approved at the entry step, so there is nothing new to confirm before committing. Only the push is genuinely optional. So: commit first (the safe, local action), then gate the outward push on consent. After committing, run one `git remote` check — with a remote, offer push as a plain yes/no ("Committed. Also push to the remote?"); with no remote, say it's committed and offer no push (a push would error with nowhere to send). This matches the file-safety rule: do the safe local thing, ask before the outward one. A sub-doc may override to fit its session shape — done-plan.md commits and doesn't offer push — but the commit-first mechanics here stay canonical.
5. Pass the message shell-agnostically. Write it to a file in the project root (e.g. `COMMIT_MSG.tmp`) and commit with `git commit -F COMMIT_MSG.tmp`, then delete the file. One mechanism on every machine — it sidesteps inline-quoting fragility (a multiline body passed with `-m` is brittle to generate: embedded newlines vary by shell, and a PowerShell here-string needs its closing token at column 0). The message file is writable at this step because the sub-doc deletes _build.md before reaching Commit (build/test/audit closes) or no _build.md ever existed (plan/setup closes), so the scope-lock isn't active on the project root here.
6. Commit with `git commit -F`. The commit needs no fresh okay — its message was approved at the entry step. Then offer push only when a remote exists (per step 4), and push only if the user accepts.

The LOG entry keeps its `[HASH]` placeholder. The session-start hook backfills it automatically at the next session, as a working-tree edit that folds into that session's commit — no amend, no two-commit flow.

## Rules

- Do NOT skip the sub-doc's judgment steps even if the user says "just commit."
- Routing is automatic. Don't ask — check for _build.md.

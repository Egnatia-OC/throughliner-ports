# /cruise procedure

The autonomous multi-line runner. /cruise works the cleared queue top-down — build, commit, build, commit — without stopping to confirm each line, halting only when it hits something that genuinely needs the user or when a safety limit fires. It is the "do many" version of /next: /next builds one confirmed run and stops; /cruise loops that same build-and-close machinery across every cleared work line until the cleared region is exhausted.

/cruise reuses the per-line procedures rather than duplicating them: each work line builds through `next-build.md` and closes through `done-build.md`, exactly as an attended /next → /done pair would. What this doc adds is the **loop** around them, the **gate** in front of each line, the **response spine** that decides what to do when a line can't just be built, and the **hard-stops** that bound a runaway run.

## Before the loop: confirm and bound the run [PROMPT]

/cruise runs unattended once it starts, so the one interaction is up front.

1. **Active build check.** If `_build.md` exists, a build is already in progress — offer to resume it through /next rather than starting a cruise run over the top of it. Don't start a fresh run while a build is open.
2. **Read the cleared region.** Read QUEUE.md's Processed section top-down. The run is every work line from the top down to — but not including — the first `[user]` line, and never past the `--- Cleared to run above this line ---` marker. This is the same run-boundary /next draws; /cruise just intends to work the whole thing rather than one confirmed run.
   - **Nothing cleared** (the first line in Processed is the cleared-to-run marker): tell the user there's no cleared work to run and recommend /plan. Don't start.
   - **Top line is `[user]`:** there's no Claude-work to run first. Hand it over as /next would and stop — /cruise has nothing to loop.
3. **Show the run and the bounds, get one go-ahead.** Put the run's work lines in front of the user (per plugin-behaviour.md's pointer-vs-paste rule — pointer when an editor is recorded, verbatim otherwise), name the hard-stop limits that will bound it (iteration ceiling, per-run budget ceiling, no-progress detection — see Hard-stops below), and ask once whether to run the whole cleared region unattended. **This is the only go-ahead the run gets** — after it, /cruise does not re-confirm per line. On confirm, enter the loop.

## The loop

Work the cleared region one work line at a time, top-down. For each line, run steps (a)–(f); (g) advances; (h) closes the whole run.

**(a) Pick the top cleared work line.** The next un-built line at the top of the run. An `[audit]` line routes to its own per-line procedure (`next-audit.md`) and closes through its own (`done-audit.md`) — the loop is flavor-agnostic, it just drives whatever the line's flavor dictates.

**(b) Gate-check before building.** Before touching the line, run the pre-build gate:
- **Red-flags gate** — if any red flag is open, the run may not proceed (see Red-flags gate below). Only resolved or accepted flags let it run.
- **Dependency check** — the line must not depend on work whose verification is still pending. Under the readiness-line model this is settled at plan time (a line depending on unverified work stays below the cleared-to-run marker), so inside the cleared region this holds by construction; the run-time check is a backstop. If it fails, halt-for-the-user (see Response spine).

**(c) Build, scope-locked.** Lock scope to the line's files and build it through `next-build.md`, exactly as /next does — self-scope the `Files:` list from the line, write it into `_build.md`, make the changes. Two halt-triggers live inside the build, not only at the gate: a needed SPEC/product-truth change and a blocking uncertainty Claude can't resolve. Each stops the run the same way (see Response spine → halt-for-the-user); nothing is lost, because every prior line is already committed.

**(d) Verify.** Run every check Claude can run this session as part of building the line right (per next-build.md — a Claude-runnable check is just building). A check only the user can run does not stop the run: file it and keep going (see Response spine → route-and-continue).

**(e) Close-and-commit the line.** Close the line through `done-build.md` and the commit core in `done.md`: write its LOG entry, run the shipped-slug cross-check, delete `_build.md`, and commit — **one commit per work line**. This is durable on purpose: an unattended run with no one watching must leave a clean, committed resume point after every line, so a crash, a budget stop, or a halt loses nothing. The close's judgment steps are not skipped for speed (see Autonomy adaptations); its user-approval moments get unattended answers rather than being dropped.

**(f) Check the limits.** After the line commits, check the hard-stops (iteration count, per-run budget, no-progress signal — see Hard-stops). If any has fired, stop the run here (the just-closed line is already safely committed) and go to (h).

**(g) Advance.** Move to the next cleared work line and repeat from (a). Keep going until one of three things happens: the cleared region is exhausted (a clean finish at the readiness line), a halt fires (something needs the user), or a hard-stop limit stops the run.

**(h) Run-end pass.** Once the loop ends for any reason, run a single wrap-up (not once per line):
- **Staleness sweep** — one pass over the remaining queue work lines for staleness, as done-build.md's sweep does, run once for the whole run rather than per line.
- **Summary** — tell the user plainly what ran and what awaits them: which work lines built and committed, which checks were filed for the user to run, and why the run ended (cleared region finished / halted on X / hit the Y limit). If the run halted or hit a limit, name what's needed to resume.

## Response spine — what the run does when a line can't just be built

An attended /next hands anything non-routine to the user. A cruise run has no one sitting there, so every such moment resolves into one of three responses.

**Route-and-continue** (the common case). Anything an attended session would surface that does *not* block progress gets written down, and the run keeps going. Captures — ideas, observations, out-of-scope discoveries — append to Unprocessed as normal work lines. A verification only the user can run becomes a `[user]` work line appended to Unprocessed (what needs checking and why), exactly as done.md files an unrunnable check — the run does not wait for it and does not stop. No one is there to hand these to, so filing replaces handing-over.

**Halt-for-the-user** (the rare case). Only a genuine proceed-blocker stops the run:
- an **open red flag** (see Red-flags gate),
- a needed **SPEC / product-truth change** the build discovers (a product-truth change can't be self-approved), or
- a **blocking uncertainty** Claude can't resolve — one whose resolution is a decision the user owns (a design choice, a materially-ambiguous requirement). Technical "how" uncertainty is not this; Claude resolves that as normal building. The test is categorical — *whose call is this?* — not a confidence threshold; ambiguous ownership defaults to the user's, the safe side.

To halt: write a `BLOCKED` marker (see below) naming what's needed, and exit the loop. Nothing is lost — every prior line is already committed. The run ends at (h) with a summary that names the blocker.

**Hard-stop** (the mechanical safety net). An iteration ceiling, no-progress detection, or per-run budget ceiling — these fire regardless of category, guarding against a runaway run, and are detailed under Hard-stops below. They use the same write-`BLOCKED`-and-exit mechanism.

### The BLOCKED marker

Both a halt-for-the-user and a hard-stop write a `BLOCKED` marker to `_build.md` (in the currently-open line's file) before exiting: a plain-English line naming why the run stopped and what's needed to resume. Writing it to the file rather than only to chat means a resumed session — which may not see this chat — reads why the run halted straight from the working file. The just-closed lines are already committed; only the in-flight line (if any) carries the marker.

## Autonomy adaptations — the close's judgment steps, unattended

/cruise runs the *full* per-line close (done-build.md) — its judgment steps are never skipped for speed; autonomy removes the human, not the steps (plugin-behaviour.md and done.md both forbid skipping close judgment even under "just commit" pressure, and an unattended run's throughput pressure is the same force). The already-mechanical gates carry their enforcement with no one watching: the shipped-slug cross-check, the out-of-scope dirty-path detection, and the done-build spec-sync gate all run as written.

What changes is only the handful of close steps that, attended, end in a user approval. Each gets an unattended answer:
- **Wind-down re-scan → auto-file.** done.md's wind-down re-scan normally surfaces candidate captures for the user to approve. Unattended, it auto-files everything it surfaces to Unprocessed with no approval prompt. This loses nothing: filing commits to nothing (the real keep / drop / promote decision still waits for a later /plan), so auto-filing just defers that decision to where it already lived.
- **Push offer → doesn't arise.** The close commits per line and never offers a push (concern 10's per-batch-commit-only). A cruise run publishes nothing outward.
- **Subagents → declined by default.** A cruise run spawns no subagent unless the build plainly matches one of the three researched heavy-data cases (a large or multi-repo codebase sweep, a large document-set/archive synthesis, or a large log/big-file analysis — the cases where one corpus genuinely won't fit a single context window; `resources/research/subagent-genuine-need-cases.md`). A subagent runs ~15× the tokens, and an unattended run must never spend that silently. An unforeseen mid-run need for one is not a silent inline workaround — it's a halt-for-the-user (write `BLOCKED`, exit), because a build suddenly needing a subagent it wasn't scoped for signals the line was bigger than planned. Research that merely burns tokens without overflowing context stays default-against too.

## Red-flags gate

Any open red flag blocks a cruise run; only resolved or accepted flags let it proceed. Judging a risk's relevance to the current line is a call a mechanical check can't make reliably on the one category you least want it guessing, so the rule is absolute: any open flag blocks, full stop.

The gate is realized by `hooks/cruise_gate.py` — a **procedure-invoked** gate script, not an event hook (there is no skill-start event to hang a true hook on). cruise.md runs it at the top of the run and again before each work line (loop step b):

```
python "${CLAUDE_PLUGIN_ROOT}/hooks/cruise_gate.py" QUEUE.md
```

It reads the three red-flag states in QUEUE.md (reusing session_start.py's `_open_red_flags`, so the gate and the session-start red-flag surfacing never drift). Exit 0 / `GATE: CLEAR` → proceed. Exit 1 / `GATE: BLOCKED` plus the open flags → halt-for-the-user: write a `BLOCKED` marker naming the flags and exit.

- **Clearing the gate is one step, done in /plan:** mark the flag resolved (designed out) or accepted (risk read, user chooses to proceed).
- **A flag raised mid-run** is open by definition, and the next step-(b) gate check catches it and flips the run to an immediate halt. Screening runs the whole time and the gate reads what screening recorded, so the two are a pair — the gate alone isn't total coverage.
- **Known limit, named not fixed:** the gate blocks on flags that were *raised*; it can't block a risk never noticed — that's the screening's job, which runs every session including this one.

## Hard-stops

The mechanical safety net the field treats as mandatory for an autonomous loop — the guard against the runaway-cost failure. Each fires regardless of category, via the same write-`BLOCKED`-and-exit mechanism, and each is checked at loop step (f) after a line commits:

- **Iteration ceiling** — a cap on how many work lines one run will build (default 12 unless the user names a limit at run start). Reaching it stops the run cleanly; the still-cleared region below can be run again with a fresh /cruise.
- **No-progress detection** — the same error, an empty diff, or the same failing check repeating **3 times** on one line means the run is stuck. Stop rather than thrash; write `BLOCKED` naming the stuck line and what repeated.
- **Per-run budget ceiling** — a best-effort cap on how much one run spends. Claude can't read an exact token meter mid-run, so this is a coarse guard: if the run has clearly run long (many lines, heavy re-reading), stop and hand back rather than pushing on silently. The user may name a tighter budget at run start.

When any hard-stop fires, the just-closed line is already committed, so nothing is lost — the run ends at (h) with a summary naming which limit tripped and how to resume.

## Resuming an interrupted run

Because each line commits before the next begins, an interrupted cruise run leaves the finished lines committed and at most one line's `_build.md` open. A fresh session resumes cleanly: the open `_build.md` (if any) offers to finish that one line through /next, and the still-cleared region below it can be run again with /cruise. There is no separate cruise-run state file — the per-line commits and `_build.md` are the whole resume record.

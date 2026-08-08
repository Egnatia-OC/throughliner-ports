# Fable session brief — drain and fix the queue

Autonomous working session on the Sovereign Implementer plugin. **SI is disabled for this run**, so there are no SI skills or hooks — you work with plain file edits and git.

## Who this is for
The developer, Alex, is a non-coder who has spent months shaping this plugin and is stuck. She needs solutions, not more process. **Do not ask for approval during this session — write your results directly into QUEUE.md.** She will process them later.

## The problem to solve
The queue never drains. Three linked pains:
1. **Test-shaped work leaks everywhere.** In-session checks, genuine must-run tests, and passive "observe after reinstall" confirmations all pile up as if they were one thing (the Deferred tests section is ~65 lines and almost none of it ever gets confirmed).
2. **No real home for work the USER conducts** (as opposed to work Claude does).
3. **Everything gets parked, deferred, or dependency-chained instead of finished or dropped**, so the queue only grows. This has blocked progress toward cruise control (the end goal) for months.

## Read first — build on prior thinking, don't reinvent it
- **QUEUE.md** — see the problem concretely (the Deferred tests pile, the Parked shelf, the length).
- **Alex's own prior design thinking on exactly these problems** — read these parked items before proposing anything: `[test-concept-redesign]`, `[dedicated-design-session-mirage]`, `[watchlist-doc]`, `[shelving-as-tests]`, `[design-session-queue-home]`, `[user-execution-batch-shape]`, `[guided-exploration-batch-type]`.
- **The redesign attempt** in the sibling project folder `No code method-x` (git branch `queue-redesign`): read its QUEUE.md, the LOG entries for `[work-line-behaviour-defs]` and `[plan-work-line-procedure]`, and the recut `plugin-behaviour.md` and `plan.md`. It collapses the whole model to two sections (**Processed / Unprocessed**), one notion of "work" (Claude-work by default, user-work marked `[user]`), and strips parking, deferred tests, and dependency machinery. Treat it as a serious candidate solution — evaluate it honestly and land a clear recommendation to **ADOPT, ADAPT, or REJECT**, with reasons. It is not "the desperate version" to dismiss.

## Leads from a prior session (hypotheses to test, not gospel)
- The bottleneck may not be over-capturing — it may be that the method forces every item to be **homed** somewhere (parked / deferred / dependency-chained) and never simply dropped, so the queue fills with things no one will ever do.
- Parking is the escape valve Alex built because deleting felt like losing work. **Git history makes deletion free and fully recoverable.** Flipping the default from "when in doubt, park" to "when in doubt, DELETE" may be the core fix.
- **/plan only ever processes captures.** It is supposed to also curate the whole queue every session — notice stale/dead items and delete them — but that machinery is either asleep (old model) or removed (redesign). A /plan with a real, active curation pass over ALL item types may be the central fix.
- The test pile drains fast if you **separate the passive "observe-after-reinstall" confirmations** (auto-clear them) from the few genuine must-run tests (make those user-work). Most of the section then evaporates without redefining testing wholesale.
- If dependency machinery is stripped, preserve ONE load-bearing piece: the **"don't build B on unverified A" guard** (a plan-time check). Cruise control will need it.

## Your tasks (work autonomously; write straight to QUEUE.md)
1. **Clear dead items:** walk the ENTIRE queue and delete — into git history — every item that isn't something Alex would genuinely pick up soon, or that actively feeds current work. When in doubt, delete; it's recoverable.
2. **Write fix-captures** (match the capture format already used in QUEUE.md) that solve, together:
   - test-shaped work leaking across the queue;
   - a real home for user-conducted work;
   - a /plan that processes ALL information types in the queue, not just captures, so nothing stays forever;
   - a clear recommendation on the two-section redesign (adopt / adapt / reject);
   - anything else that simplifies the queue so projects stop bogging down like this.
3. **Write batches** too where a fix is concrete enough to build.
4. You may capture high-leverage ideas outside these buckets — but only if genuinely high-leverage.

## Hard guardrail — the trap to avoid
The goal is **FEWER, CONVERGENT changes**: the smallest set that fixes the root causes. Do NOT solve "the queue is too long" by adding many new items to it — that recreates the exact problem. Prefer deletions and consolidations over additions. If you find yourself writing more than a handful of new captures, stop and converge. **Simplicity is the deliverable.**

## Output
Everything written directly into QUEUE.md — the deletions, the fix-captures, and any batches. Do NOT render them to chat for approval; Alex processes them in the next /plan. At the top of your additions, leave a short plain-English note summarizing the direction you landed on and your adopt/adapt/reject call on the redesign, so she can orient before processing.

## North star
Comprehensively de-risk the path to cruise control, so Alex does not have to spend months more shaping the method. **Solutions, not process.**

# 47966bb — Ten rules that fire in one skill each leave the always-loaded file for the skill doc that uses them

Audit finding C, settled at processing on 2026-08-13: the filter is not
aspirational, so the rules move. The always-loaded file's opening states the
all-four-skills test as its own admission control, and a filter its own contents
fail is worse than no filter, because it teaches every later author that the test
is decorative.

**Every one of these was loaded in every session of every command and read in
exactly one.** Nothing else on the audit's list has that multiplier, which is why
this was the largest saving available.

**Four of the ten turned out to be deletions rather than relocations**, because the
destination already carried the rule in full: flag-clearing at the keep-step
(already in `plan.md`'s ground rules), the below-the-line one-question revisit
(already `plan.md`'s revisit step), the wind-down filing carve-out (already
`done.md`'s own fenced block), and the scrub-at-keep trigger (already a pointer in
`plan.md`). Checked rather than assumed either way, which is what turned four
moves into four straight removals.

**One deliberate departure from the audit's routing.** The mid-close route-out rule
was to go to `done.md`; `done-build.md` already states it in fuller form with the
same single exception. Sending it to `done.md` would have created exactly the
duplicate that the sibling item in this run was clearing, so it was deleted from
the always-loaded file and left where it already lives.

**The consolidated opening narration went to three docs rather than one**, since
the scans it consolidates differ per skill: `plan.md`'s read-state, `next.md`'s
pre-flight and a new section in `done.md` each carry it with their own checks
named, along with the precedence rule that anything the user must act on leaves
the bundle and goes on its own.

**The cross-reference check the item required was run before deleting**, grepping
the moved rules' distinctive wording across `docs-b/` and the skill prompts. No
dangling pointer was left. One turned up later in the run, in a host-only file the
grep did not cover — `resources/method-compliance-audit-checklist.md`'s third
narration-drift lens pointed at "the consolidate-the-scans rule in
skill-nonspecific-rules.md" — and was fixed when that file was next opened. Worth
recording that the grep's scope was the shipped docs and the miss was outside it.

**Rule gate: run** — a relocation and a net subtraction, nothing admitted.
Measured: the always-loaded corpus fell from 254 to 240 rule statements and the
fetched docs rose from 919 to 925. Both numbers are reported rather than only the
first, so the relocation reads as a relocation instead of as a reduction — which
is the check the growth report exists to make possible.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
(removals), `plan.md`, `next.md`, `done.md` (receiving).

**Routed to Captures:** none.

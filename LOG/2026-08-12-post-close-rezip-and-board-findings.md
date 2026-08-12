# 2f0dfdf — The post-close tail: a rezip gate caught an ordering regression, and the board caught two defects in this session's own work

This entry records work done *after* the session's /done close committed at `e5d169b`. It exists because the tail produced three real changes across two further commits (`60373f7`, `5145040`) and none of them had a LOG entry — the close had already run, and the method has no delta-close path built ([done-delta-close], [post-close-tail-state], both unprocessed). Written at the user's request rather than by any rule, which is itself worth noting: nothing in the procedure would have produced it.

Full depth, and the trigger is met twice over: two of the three findings are about this session's own reasoning being wrong, and a later reader needs to know that before trusting the entries around this one.

## 1. The rezip test gate stopped the rezip, correctly

Asked for a rezip, the ritual's three-suite gate failed one assertion: *SessionStart: project state within the first 2KB*. The state line had drifted to 2,289 characters in. It had passed an hour earlier during the close.

**The diagnosis was wrong on the first pass and worth recording as such.** The initial reading was that the growth report built into `rule_signals.py` had lengthened the board message. It had not — the board surfaces only *firing* signals, and removing the ceiling took MEASURED and AUDITED out of that set, so the board line got *shorter*. The real contributor was the queue's dependency-facts line gaining a "Held on Unprocessed blockers" sentence, which fired because this session re-pointed a blocker at an Unprocessed item.

**The fix was the same either way, which is why it went ahead without settling the attribution precisely.** Project state now sits immediately after the two things that legitimately outrank it — the stale-format halt and the uncleared-red-flag scan — ahead of dependency facts, isolation, the worktree report and the board. State line at 0. The payload was 2,749 characters against a 10,000-character cap throughout, so nothing was ever near a limit: this was an ordering regression, and the assertion exists precisely so that adding another scan stays safe.

**The gate earned its place.** It fired on the first occasion it had something to catch, on a change this session made, and the honest response was to stop rather than override it. Overriding a gate the first time it catches you is how gates die.

## 2. Sixteen rule-gate dispositions were written in a format the gate's own checker cannot read

`CLAUDE.md` specifies the disposition as a bare line, `Rule gate: run — …`. Every one of this session's sixteen was written as `**Rule gate:**`, bolded as a body field. `DISPOSITION_RE` matches `^Rule gate:` at line start, so **not one of them was visible to BORN**, which correctly reported `e5d169b` as carrying no disposition at all.

The irony is exact and should not be softened: the session that moved the rule gate to authoring time — so that a disposition is written *before* the rule it judges — recorded its own answers in a shape the gate's checker cannot read. The obligation was satisfied in substance and absent in fact. Two entries from earlier sessions carried the same drift, so the convention had been eroding before this run; eighteen files were corrected in total.

**This falsifies a claim made in [rule-gate-runs-at-close-not-at-authoring]'s entry**, which said the build was its own first test and passed. It passed the part it was testing — every disposition genuinely was written at authoring time, before the next item began — and failed a part nobody was testing. That entry has been corrected rather than left standing.

## 3. `CEILING` was added to the retired-terms list as a bare word, reintroducing the defect removed hours earlier

The same session fixed four precision defects in the REPEALED detector, one of which was that terms matched without word boundaries so `docset A` caught the words "docset and". Then it added `CEILING` to the retired-terms list by hand — a term that matches the ordinary English word, and `plan.md` uses "this ceiling" about an unrelated queue guard.

So a fifth instance of the same failure class was created by hand within hours of removing four by code. The list entry now names the phrase carrying the number instead, and says in the entry itself why the bare word was rejected, so the next person to add a term meets the reasoning.

**One of its three hits was genuine, and was a falsehood this session created.** `resources/method-compliance-audit-checklist.md` still told readers a sweep is triggered when the count goes over the ceiling — a ceiling this session removed, on a signal that no longer fires. Rewritten: a sweep is now a judgment, taking MEASURED's direction of travel and MAINTAINED as its inputs, with the case resting on relevance rather than volume.

## 4. What was left firing, deliberately

Making the dispositions readable gave CONTRADICTED enough input to misfire, taking it from one flagged commit to three. It keys on the *commit*, so on a sixteen-item run one item's honest `not needed` taints the whole hash while a different item in the same commit correctly recorded `run`. None of the three flagged commits is actually contradictory; all three are multi-item runs.

Left firing on purpose. Changing the unit is a design decision, not a repair, and it is filed as [contradicted-flags-mixed-disposition-runs] with a cheaper alternative noted — flag a commit only where *every* disposition naming it says `not needed`, which is computable from data already collected.

## What the tail says about the method

Three findings, and the board or a test gate produced all three. None came from Claude reviewing its own work, and two are cases of this session contradicting its own conclusions within hours. That is the argument for mechanical checks stated better than any rule could state it — and equally, the argument for the limits those checks carry, since BORN was silent about sixteen missing dispositions for as long as the formatting hid them, and looked exactly like a passing check while doing it.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `resources/retired-terms.md`, `resources/method-compliance-audit-checklist.md`, eighteen `LOG/2026-08-12-*.md` entries, `QUEUE.md`
**Routed to Captures:** [contradicted-flags-mixed-disposition-runs]
Rule gate: not needed — no rule in the method's own text was authored or amended. A hook's output ordering, a retired-term list entry, a corrected checklist description, and a formatting repair to committed records.

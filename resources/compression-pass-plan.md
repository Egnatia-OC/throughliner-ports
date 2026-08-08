# Compression pass — reusable plan

> Reusable plan, sibling to `consistency-audit-plan.md` and
> `overnight-blitz-plan.md`. Written 2026-08-08; not yet run. Amend in place
> after each run.

## What this is, and why it is not an audit

**A compression pass edits the method's own documents down. It does not report.**

That is the whole difference from every audit in this project, and it is worth
stating first because the two get confused by name. `consistency-audit-plan.md`
asks *do the documents agree with each other and with the code* — in both its
modes. Neither mode asks *is this document longer than it needs to be*. So the
audit that exists is the **safety check you run before compressing**; the
compression it was named for is this.

**A compression pass that files findings has not compressed anything.** Findings
are the audit's output. Shorter documents are this pass's output.

## Why the corpus grows, and why a rule would not fix it

Every rule in this corpus carries its evidence, its rejected alternatives and the
incident that produced it. That is deliberate — the why-clauses are what make a
rule stick. But nothing anywhere asks whether a rule's paragraph still needs to
be *that long now*, after the incident it was written for has receded and three
later rules have restated half of it. So when something goes wrong, the only
sanctioned move is to add another paragraph.

The growth is structural, not a lapse of discipline. Measured rather than
asserted: `docs-b/plugin-behaviour.md` was 1,148 lines / 62 KB in August 2026,
roughly twice the next largest procedure doc, and it is the one loaded in every
session whatever the session is doing.

**The one precedent, and it argues the pass is achievable rather than
aspirational.** Docset B was authored *by subtraction* from docset A for the
5-series, and the subtraction was measured at the time rather than estimated.
That was a one-off authoring event driven by a model change, not a repeatable
pass — but it establishes that this corpus survives being cut substantially,
which is the thing a first compression pass would otherwise have to prove from
scratch.

## What counts as bloat

Concrete forms, not a judgment about length. A cut needs to match one of these:

1. **The same rule stated at three sites, where one is canonical and the others
   are drift.** Keep the canonical statement; replace the others with a pointer
   naming it, or delete them where nothing reads them.
2. **An incident recounted at length whose lesson has since become a one-line
   rule.** The narration was load-bearing while the rule was being argued for.
   Once the rule is settled and stated, the narration is history — and history
   has a home in the LOG.
3. **A rule superseded but never deleted.** The successor shipped; the
   predecessor was left in place because deleting felt riskier than leaving.
4. **Duplicate worked examples making the same point.** Two examples that
   illustrate one distinction: keep the clearer one.

**What is NOT bloat: the why-clause that makes a rule followed.** That is the
corpus's core design decision, and the pass must not treat it as fat. A rule
stripped to its imperative is a rule that stops being followed — which is the
failure this whole corpus is written the way it is to avoid. If a cut would leave
a reader unable to tell *why* the rule exists, it is the wrong cut.

The same guard in the authoring heuristic's words: concision comes from cutting
bloat, never from cramming or dropping the plain-English explanation a non-coder
needs in order to act.

## How a cut is verified safe

```
1. the FULL-CORPUS consistency audit runs first, as a precondition
       # its findings are reconciled before any cutting starts — otherwise a
       # cut removes a sentence something else silently depends on
2. per cut: grep the rule's other statement sites BEFORE removing anything
       # the same ripple discipline CLAUDE.md requires at authoring time,
       # applied in reverse. A pointer into the text being cut is a blocker.
3. per cut: name what survives and where
       # "this paragraph goes; the rule it states stays at <site>" — a cut
       # with no named survivor is a deletion, which is a different decision
```

**The honest limit, stated rather than implied.** The adherence-measurement
harness was consciously waived, so nothing will measure whether a cut helped or
hurt. There is no before-and-after number. The pass leans entirely on the
pre-check and the per-cut grep, and those establish that a cut broke no
*reference* — never that the shortened rule still steers as well as the long one
did. Do not describe the cuts as validated.

## Where it fires in the cycle

**Its own phase, after a full-corpus consistency audit, and never on the same
branch as the audit that precedes it.** The audit's findings have to be
reconciled and merged before the cutting starts, or the pass is editing text the
audit's repairs are also editing.

The cycle's phases and which audit runs at which one are tabulated in CLAUDE.md's
branch-cycle section; this plan is the fourth row of that table.

## This pass's queue-item form

Not seeded every cycle — unlike the blitz, the audit and the merge, a compression
pass fires only when the docs have grown enough to warrant one. It is filed as an
ordinary work item when that judgment is made:

```
#### Compression pass over <scope> [compression-pass-<date>]
Runs `resources/compression-pass-plan.md`. Below the readiness line;
lift-condition: a full-corpus consistency audit has run over this corpus and
its findings have been reconciled and merged.
Blocked by: nothing queued — the audit is a separate cycle's work.
```

## Reporting

The pass edits, so its record is the diff and its LOG entry — not a findings
list. The entry states, per document touched: the line count before and after,
which of the four bloat forms each cut matched, and what survives where. A cut
nobody can trace back to a form on that list is the one to look at again.

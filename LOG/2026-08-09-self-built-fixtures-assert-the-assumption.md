# [HASH] — CLAUDE.md gains the self-built-fixture rule: a fixture standing in for another program's artifact is built from the real thing once, or says it encodes an assumption

Three sentences of new rule, and the brevity was itself the decision.

**The rule, as it now reads in CLAUDE.md's Working conventions, beside the two
ripple-grep rules:** where a test's fixture stands in for something *another
program* creates — a directory the installer makes, a file another tool writes, a
payload the app sends — build the fixture from the real artifact at least once, or
state in one line inside the test that it encodes an assumption. Otherwise the
fixture and the code under test can be built from the same wrong belief, agree
with each other, and pass — which is indistinguishable from coverage and actively
discourages the check that would find the truth.

**The bound is kept and matters:** fixtures exist precisely so tests need not
depend on the world, so this fires only for artifacts produced outside our own
code. It is not a general demand that tests touch reality.

**Two processing decisions changed what the capture asked for, and both are worth
keeping.** First, the concrete repair had already shipped, and further than the
item knew — `test_content_stamp_ignores_the_cli_in_use_marker` now builds `.in_use`
as a real directory with a marker file inside it, carrying a comment recording why
the first version was wrong. So the specific lesson already sits at the site where
it fires, and what remained here was only the general rule. Second, the home is
CLAUDE.md rather than the authoring heuristic the capture proposed: that document
is consulted when *authoring method text*, and this rule has to fire when *writing
a test*, which is a different moment in a different kind of work. That deliberately
broke the grouping with [authoring-heuristic-has-no-live-model-pass], and the cost
was weighed — a rule filed where nobody reads it at the right moment is the failure
that planning session kept finding.

**Why the entry does not retell the incident.** The `.in_use` sequence is already
recorded in the test file's own comment and in the LOG. Retelling it in the rule
would be exactly the pattern [compression-pass-plan-and-cycle-audit-roles] names —
documents that only ever grow — and this was the first item processed under that
concern. Trigger and action only.

**Files touched:**
- `CLAUDE.md` — one new bullet under Working conventions, after the two ripple-grep rules.

No test was rewritten: the one that motivated this is already correct.

**Routed to Captures:** none from this item.

**FAQ:** not needed because this is a host-only development rule in this project's CLAUDE.md, which consumer projects don't carry.

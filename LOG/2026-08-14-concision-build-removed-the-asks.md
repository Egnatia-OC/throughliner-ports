# [HASH] — The turn-by-turn asks come back: the cadence rule loses its bare count, the style is bounded to length, and both watchers gain the output style

Alex reported on 2026-08-13, in her own words, that since the last rezip all the
turn-by-turn behaviour was gone and the asks were all gone. She also identified
the bare number herself. The diagnosis below is Claude's.

**Two independent causes, and fixing either alone would have left her reporting
the same symptom.** The first was the output style: `d6efa7c` added a cadence
rule reading *speak at three moments while you work, and work quietly between
them*, which reads as an instruction to keep going. The procedure's stopping
steps say the opposite, and the always-loaded rules already state that procedure
tags govern during a skill — but the style loads later in the stack and reads as
more current, so it won. The second was found live on 2026-08-14 while she was
working: `plan.md`'s hand-over message, the one that gives her the next item,
instructed "nothing beneath it. No routes, no options, no question," and showed a
specimen with no ask. During a long processing run that hand-over is most of the
turns, so most of the session arrived with nothing to answer.

**Her instruction was to restore them exactly as they were**, having spent months
designing them with Claude. That is a decision rather than a preference to be
weighed, so this build restores the ask and does not redesign it.

**What the no-question wording was protecting, kept intact.** The text it replaced
was a recital of four routes ending in "or run /done", which read as a nudge to
stop and once caused a session to be closed that she wanted to continue. What
comes back is the ordinary single bold question about the item in hand, not that
recital, and the doc now says so in terms — so both goals hold at once: no menu,
but never a message with nothing to answer.

**The finding worth more than the bug.** The style lives outside every watcher.
The rule gate fires on commits touching `docs-b/`, `resources/self-authoring-rules.md`,
`resources/rule-maintenance.md` or `CLAUDE.md`; `output-styles/` was in none of
them, so a commit changing only the style fired no gate. The board's growth report
did not count it either. An always-loaded layer sat outside both the admission
gate and the measurement, which is exactly how an underived number reached it
while every watcher stayed quiet. Both are fixed here: the path joins the gate's
trigger list and the style joins `SHIPPED_ALWAYS_LOADED` in `rule_signals.py`,
where it now counts for ten rule statements.

**The cadence reword applies the derivation rule rather than adding one.** "Three
moments" is a bare number deriving from nothing. It is replaced by the occasions
the count was standing for — before the first tool call, on finding something
important or changing direction, and at the finish — so the same behaviour is
named without a figure nobody can trace.

**Rule gate: run** — four changes, all amendments, no slot consumed. The style's
new scope clause is a boundary statement about that document (what it governs and
what it does not), deliberately not a second copy of the response-shape tags'
precedence rule, which would have created the duplicate-statement defect another
item in this run was clearing. Nothing evicted, because nothing was added.

**Files touched:** `plugin/throughliner/output-styles/concise-throughliner.md`,
`plugin/throughliner/docs-b/plan.md`, `CLAUDE.md`, `resources/rule_signals.py`.

**Routed to Captures:** none.

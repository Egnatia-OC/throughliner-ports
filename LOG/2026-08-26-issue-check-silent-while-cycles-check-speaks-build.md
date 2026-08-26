# 2c76e53 — Issue-channel check now speaks one line either way wherever the channel exists

From the compliance audit's consistency lens. Two sibling checks sit in `plan.md`'s
opening and fire at the same moment. The cycles check had just been rewritten to
speak whenever a project has a cycles doc, on the ground that a check speaking only
when it files cannot be told from a check that never ran — which is what the cycles
check had turned out to be for its entire life. The issue-channel check was still
tagged silent unless it filed something.

The reasoning that moved one applies unchanged to the other: an issue scan that ran
and found nothing produces the same silence as one that never ran, and nobody would
know to ask. Settling both the same way was the point, rather than letting two
checks with one argument between them drift further apart.

**The cycles check's cost bound is carried over with it**, which is what keeps this
from becoming noise. The check speaks only where the channel exists at all — `gh`
present, and either an open outbound issue on the register or a repository that can
receive them. A project with no channel stays silent and pays nothing, exactly as a
project with no cycles doc does.

The tags are written with their conditions outside the brackets, per the
tag-authoring rule.

**Files touched:** `plugin/throughliner/docs/plan.md` — the issue-channel check's
response-shape tags and its either-way reporting requirement.

**Routed to Captures:** none.

Tick form: done, confirmed.

Rule gate: run — amendment aligning the issue check's response-shape tags with its
sibling cycles check's decided shape, nothing new admitted.

SPEC's correspondence-scan sentence was checked at the keep and survives unchanged.

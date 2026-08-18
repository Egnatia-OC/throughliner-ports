# 7e3c1c8 — the scope-lock's refusal of CLAUDE.md is recorded as intended, and no permission changed

The disposition here is a **refusal** — of a proposed permission change — plus a clarification of an existing rule's account. A comment beside the standing list in `pre_tool_use.py`, and a clause in `CLAUDE.md`'s gate account.

The objection was real and had been raised three times from three readings of the same list. In this repository `CLAUDE.md` holds the rule gate, and the gate's design argument is that only /plan can refuse a rule — so a planning session that admits a rule and then cannot write it appears forced to queue the write as a build, which is the placement the gate explicitly rejects.

It conflates deciding with writing. The gate runs at the keep-step and its output is a **disposition on the queue item**; the rule *text* is written by the build that item schedules. What the gate refuses is a build deciding whether a rule may exist, never a build typing out a rule /plan already admitted.

The evidence is the session that settled it: fifteen rule changes dispositioned at the keep-step, every one queuing its text as a build, nothing blocked and no decision moved downstream.

It is also genuinely unlike the three exceptions fixed the same day — the rezip's `plugin.json`, the close's `README.md`, /setup's markers. Each of those was a required write with no permitted moment anywhere. This write has a proper home.

Worth writing at all because a denial with no stated reason gets re-litigated by every session that meets it.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `CLAUDE.md`
**Routed to Captures:** none

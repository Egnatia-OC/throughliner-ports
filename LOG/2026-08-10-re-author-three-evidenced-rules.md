# 94bba66 — Three reverted rules re-authored, each admitted on recurrence rather than prediction

All three shipped once, were lost to the 2026-08-09 emergency revert, and each has
recurrence evidence. The item deliberately did **not** carry their original
wording, because restoring the wording is what would re-import the bloat the
revert was for. They were re-authored fresh into the new
`docs-b/skill-nonspecific-rules.md`, admitted against the audit's count of roughly
218 always-loaded instructions — which is the number this build's own eviction
work is simultaneously bringing down.

**1. Offer the outbound reply.** Added to the INBOX section: when an inbound
message changes work here, the reply is drafted unprompted in the same session,
never auto-sent. The send stays under the existing never-send-unapproved rule;
what this adds is the *offer*. Confirmed by recurrence, not predicted — the user
has twice had to ask, in near-identical words, whether Claude had anything to send
back to another project.

**2. Page the whole file before reasoning over it.** Its own section, because it
generalises past the queue. The failure is silent by construction: a truncated
read looks like a complete one to whatever reasons over it, so nothing downstream
can detect it, which is why the check belongs at the read. `plan.md`'s Step 1
read-state carries the concrete instance — page QUEUE.md to the end, and say so
plainly if you cannot.

This rule failed again in the run that preceded this one, and it very nearly
failed in this one: this session's first read of QUEUE.md returned 216 of 638
lines, and the remaining two pages were only fetched because the tool said the
view was partial. That is the third instance and it is the argument for the rule
being stated at the read rather than in the abstract.

**3. Check our own conformance before blaming the tool.** Read what the tool
documents, look for others reporting it, and only then suspect the tool. The
evidence is one session spent building two detailed theories about a tool
misbehaving when the cause was our own code not matching the documented contract,
findable in about a minute.

Rules 1 and 3 are freestanding and spend a slot each; rule 2 is freestanding too.
All three carry their evidence in one sentence rather than a paragraph, which is
the register the new file is written in.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`,
`plugin/si-plugin/docs-b/plan.md`.

**FAQ: not needed because** none of the three changes anything a consumer sees:
two govern Claude's internal reading discipline, and the third makes an offer that
already required approval to act on.

**Routed to Captures:** none from this item.

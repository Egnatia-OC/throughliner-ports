# cc33c1e — The gitignore offer becomes per-document, so a private queue with a public history is reachable

**Why this was worth doing.** Scaffolding offered `SPEC.md`, `QUEUE.md` and `LOG/` as one
all-or-nothing choice. So a user who wants their plans and reasoning private while their
history stays public could not have that — the combination was unreachable rather than
merely un-defaulted, and it is the combination this project itself runs on in spirit,
since LOG is what it publishes and the queue is where the thinking sits.

**The default does not move, on the user's own objection to her own proposal:** someone
may want a visible queue for transparency. That refusal is recorded because changing the
default to private is the intuitive move once the split exists.

**What was built.** The offer covers the three documents individually, listed with what
each holds, and stays **one question with three answers** rather than becoming three
questions — "all of them, none, or just some — and if some, which?" The
private-queue-public-history combination is named in the doc as the plausible case, since
that is what earns the split. The trade is stated once rather than once per document. The
yes/no branch becomes names-some-or-all / names-none, and the report says which paths
went in and which stayed tracked. One added statement pins that no default changes.

The section's own name changed too: "Keep-everything-private option" asserted the bundle.

**The three costs are unchanged and still stated at the moment of choosing**, now
qualified as applying to whichever documents the user keeps out: write-first becomes
show-first for them, a deleted queue item is genuinely gone, and the close records from
what it remembers rather than reading its work back from the file's history.

**Files touched:** `plugin/throughliner/docs/setup.md`,
`plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`.

**SPEC.md was deliberately not edited**, per the item's own note: its privacy-posture
sentence described the bundle and was rewritten in the planning session that processed
this. `git diff SPEC.md` is empty, which confirms the build wrote no product truth — the
session-boundary rule holding, checked rather than assumed.

**Routed to Captures:** none from this item.

**FAQ: updated** — the existing privacy answer reworded for the new shape: the three are
picked individually, any combination is reachable, the common case is named, and the cost
is restated as applying to whichever the user keeps out. No index line changed, since the
question itself is unchanged.

Rule gate: not needed — no rule authored or amended; this widens an existing offer's answer set and evicts nothing.

Depth: short. Built and confirmed.

**One ordering fact worth keeping.** This was held below the readiness line until
`[gitignored-core-docs]` shipped, so that a second question would not land in front of the
user at the moment the first was already going wrong — a `.gitignore` could leave all
three untracked with nothing noticing. That shipped and was confirmed on 2026-08-20, and
the two could then ship in either order.

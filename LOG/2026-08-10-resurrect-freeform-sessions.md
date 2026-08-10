# 10d6474 — Freeform became a work-item flavor: marked at /plan, halted at /next, announced at /done

The call is the user's, in their own words: we'll resurrect the concept of
freeform sessions, as you are confident in Claude Code now and can finally handle
it. The lifecycle, the placement rule, the halt and the /done announcement are all
theirs, each correcting a Claude proposal. The scoping-down below is Claude's.

## The gap, from a live instance

[queue-machinery-repair-freeform] had to be written as an ordinary work item whose
*prose* said not to run it with /next, because the queue had no way to mark an
item as not-for-/next. Nothing mechanical enforced it; the protection was that the
user would not type the command. The class recurs whenever a fix lives inside the
machinery /next itself uses — the mover, the scope-lock, the lint — which is
exactly the class that most needs fixing.

## Scoped down: the session half needed nothing built

A freeform session already exists in practice — work by hand, close with /done,
which routes a session with no build working file to the planning close. That is
precisely what happened at `f8b03ea` and it worked end to end. So a "freeform
session type" would have named an existing capability rather than added one. What
was missing is only the *marking*, which is why this is a flavor and not a mode.

## Where it lives, and why not a new region

Ready work above the line is what /next may build; below the line means a named
item blocks it. A freeform item is neither — it is ready, nothing blocks it, and
/next still must not build it. So it sits **above** the line with the tag carrying
the exception. A third region was rejected: the method has one shelf and one
shelving move, and inventing states is a recurring failure the user has caught
each time.

## The four behaviours, and the one that turned out not to be needed

/plan marks it at the keep-step and places it at one end of the cleared region,
never interleaved — first when it repairs machinery /next uses, last when it is
unrelated — with the choice narrated like any other ordering judgment. /next halts
on it rather than skipping past. /done announces one sitting in the queue, so the
user reaches for a freeform session rather than /next.

The fourth site was checked rather than assumed, and it did not need wiring.
`CLAUDE.md`'s rule said a new batch type must touch four places including the
lint's `ALLOWED_SUBHEADINGS`. That constant does not exist: `post_tool_use.py`
validates slugs, red-flag states and `Blocked by:` lines and holds no list of
valid flavors, so a new tag needs nothing from it. The rule in `CLAUDE.md` was
corrected to say so — and to say *check* rather than assume either way — which is
the recovery-before-redesign step the item asked for, producing a correction to
the rule rather than a wiring change.

**Files touched:** `docs-b/plan.md`, `docs-b/next.md`, `docs-b/done.md`,
`CLAUDE.md`, `SPEC.md`, `README.md`, `FAQ/faq.md`, `FAQ/index.md`.

**FAQ: updated** — a new entry, "What is the 'freeform' tag on a piece of work?",
written in plain English for a non-coder. It replaces the stale `/next freeform`
entry, which documented a command that no longer exists; the new entry says so
explicitly, so a user who remembers the old one is not left guessing.

**Routed to Captures:** none from this item.

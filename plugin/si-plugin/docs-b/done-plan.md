---
name: done-plan
docset: B
note: >
  Close-out for planning sessions. Reached from done.md's router when no
  _build.md exists — /plan sessions, /setup sessions, and any session that
  changed only the project docs.
---

# Plan close-out

Every step below runs at every plan-type /done close — a /plan session, a /setup
session, and a session that changed only the project docs. The reorder, the marker
placement and the `[user]`-placement step each reach all three; none is /plan-only.

## Spec-sync gate  [SILENT] in sync; [PROMPT] on drift

Run done.md's **Spec-sync gate** and apply its **Plan close** delta: no scope-lock
is active, so edit SPEC.md directly in-session when a planning decision changed
product truth, before continuing to the LOG entry.

## Reorder both sections  [SILENT when no reorder; BRIEF when reordering]

**Conditional and change-scoped — not a full re-derivation every close.**
Reordering both whole sections from scratch each session, even when the order is
already right (the common case), is wasted work.

```
1. scope to what changed THIS session
   # items kept, deleted, or whose relationships changed. Consider only those
   # against their neighbours — don't re-reason the whole queue from zero.
   # Lean on the slug-references items already carry in their prose.
2. reorder ONLY if genuinely wrong
   # still satisfies the principles below -> silent no-op: change nothing,
   #                                         say nothing
   # a changed item actually sits wrong  -> compute and apply, and narrate
```

Do **not** reintroduce `Blocks:` / `Depends on:` headers or any dependency lint —
the prose slug-references are the whole dependency signal, and they carry no
stale-header risk.

When a reorder *is* warranted:

```
Unprocessed  ->  UNLOCK-POTENTIAL. Process first what would unblock the most
                 other work; an item that gates others sits above one that
                 stands alone.
Processed    ->  BUILD-ORDER. Build first what unblocks or reshapes the framing
                 for later work; an item whose output is a prerequisite for a
                 later item sits above the one that needs it.
```

**Within Processed, place `[user]` and `[audit]` items end-preferred**, after
contiguous blocks of build work. Build-order is the primary sort; this is a
tie-adjustment on top of it. Both flavors force /next to stop for the user — a
step they must run, an audit whose findings they must approve — so one sitting
*inside* a contiguous build run interrupts an otherwise-unattended sequence.
Position them at the **end** of the block so the human-in-the-loop stops batch
together.

**Don't move a `[user]` or `[audit]` line past a build item that genuinely depends
on its outcome** — build-order wins where a real dependency exists; end-preferred
is the default only among items with no such constraint.

**Claude reorders and narrates; it does not ask.** The user owns keep/delete and
scope, not order. Order is low-stakes and reversible, so the narration is the
catch-point where the user can redirect.

**Use the mechanical mover — don't retype blocks.** Moving an item by hand means
retyping its whole prose block verbatim, which on a long queue silently degrades
to a partial sort and can corrupt an item with no error. Only the *decision* — the
desired order — passes through you; never the prose.

```
locate:  scripts/reorder_queue.py under the PLUGIN ROOT
         # the plugin root is the grandparent of the running skill's base
         # directory (.../<plugin-root>/skills/<skill>). Derive it from there
         # so it resolves wherever the plugin is installed — never hardcode.

invoke:  # SMALL CHANGE (one or two items out of place) — the cheap form,
         # and under the change-scoped rule it is the common case:
         python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
             <Processed|Unprocessed> --move <slug> <BEFORE|AFTER> <anchor-slug>
         # (--move <slug> <TOP|BOTTOM> for the ends)

         # WHOLE-SECTION RE-SORT — only when the order is genuinely wrong
         # throughout; restating a long order for a one-item fix is the
         # expensive path a real close took twice for no gain:
         python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
             <Processed|Unprocessed> <slug1> <slug2> …

         # either form: for Processed, place the marker with
         #     --marker-after <slug|TOP|BOTTOM>
         # omit it to keep the marker where it currently sits

trust the self-check:  exits non-zero -> NOTHING was written. A slug-set
                       mismatch usually means the queue changed under you —
                       re-read it, rebuild the order, re-run.
```

**The reorder is group-aware.** Where kept items share a file scope, keep the
group contiguous rather than scattering its members across the section — the
group is the unit work moves and runs in, so an order that splits it throws away
the coherent single pass that is the whole point. The precedence above it is
unchanged and comes first: dependencies, then unblock-potential, then the group.
A blocking item runs on its dependency order whatever group it belongs to.

**Any in-place edits to a block come BEFORE its move, never after.** The mover
rewrites the whole file, so an Edit that follows it trips the "file modified on
disk since you last read it" warning — always innocently, and often enough to
train the response to the dangerous case, which is the one occurrence that
matters (a concurrent session's write once destroyed an item heading and reached
a commit). Editing first removes the collision rather than excusing it, so no
exception has to be carved into a safety rule. The one constraint: the `[slug]`
at the end of the heading line must survive the edit, since that is what the
mover addresses blocks by. Slugs are immutable by design, so this costs nothing.

```
narration scales:
    changes what /next would pick next  ->  flag it clearly
        "Moved [slug-a] above [slug-b] so it builds first — say if not."
    a trivial tidy (no pick-order change)  ->  one line
    no reorder needed                      ->  say nothing
```

## Position the cleared-to-run line  [SILENT when unchanged; BRIEF when it moves]

Walk Processed top-down and put the `--- Cleared to run above this line ---`
marker just below the last item the user has agreed is ready to build.

```
every processed item greenlit  ->  the line goes at the BOTTOM of Processed
none greenlit                  ->  at the TOP
setup / method-doc-only session with no processed work
                               ->  no line to place, nothing to reorder.
                                   Say nothing.
```

Narrate where it lands **only when it actually moves** — one plain line:
"Everything processed this session is cleared to run; the line sits at the
bottom." When your walk confirms it's already correct, confirm silently.

**Hold back an item that depends on unverified work.** A processed item must not be
cleared if it depends — by a slug reference in its prose — on another item that has
been **built but whose verification is still pending** (a host-side item shipped
but not confirmed live after reinstall, or an observed check simply not run yet).

```
dependency BUILT only            ->  NOT enough. Keep the dependent below.
dependency BUILT and VERIFIED    ->  no hold; it may clear.
```

The why is autonomy: a cleared item can be built unattended with no user in the
loop, so clearing one that rests on built-but-unverified work would let the run
stack committed work on a foundation that might later fail its check. Narrate it
when it holds an item back — one line naming which item waits on which.

**Re-derive prerequisite state from LOG, not from memory.** Whether a dependency
was built, and whether it was verified, is read off its LOG entry — this rule and
the `[user]`-placement rule below both depend on that answer, and a fresh short
session has no memory to fall back on.

**Record the lift-condition when placing any item below the marker** — the
specific **external** event that would lift it: "after a full computer restart",
"once the user has published the page", "when the account is approved". Prose,
not a hook-parsed field. This is the enabling half of the below-the-line revisit:
without a recorded condition, that revisit can't tell a still-waiting item from a
now-ready one without nagging. **An item held below with no recordable
lift-condition belongs in Unprocessed** (still needs thought), not shelved here.

**Prefer a condition something can check over one only the user can answer.**
Where the same waiting state can be expressed mechanically — a file present, a
dependency built, a branch gone, a version installed — write it that way. A
checkable condition is looked at silently every planning session and needs nothing
from the user; a user-only one can only be asked, which means it can be
suppressed, and a suppressed condition on a large queue is one nobody will return
to.

**And when an item carries both a `Set aside ·` marker and a user-only condition,
disclose the silence in one line as the marker is recorded.** Nothing will raise
that item again on its own — the consolidated question skips it, the close's
recommendation skips it, and queue exhaustion will not arrive on a working
backlog. The user mentioning it is the route back, so tell them that in the same
breath. The behaviour is correct; without the line it is undiscoverable, which is
how a user came to find out only by asking what would ever prompt them.

**A lift-condition names a repeatable future event, never one occasion to
piggyback on.** "At the next rezip and restart, whenever one happens" clears
the next time that event occurs; "at the emergency's rezip" points at one
specific occasion, and if that occasion passes without the check running, the
condition can never be satisfied as written — while reading to the revisit
exactly like a condition still waiting its turn. Two items sat in that state
for weeks, unanswerable and invisible. The revisit's *spent* outcome (plan.md)
finds ones already written; this rule stops new ones being written.

**And a user-only condition passes the downstream-action test before it is
written:** is the awaited event downstream of an action the user must take
first? An event that can't happen until the user acts ("the collaborator
replies" — to a message not yet sent) is not a recordable condition: the
action files as a `[user]` work item and the condition waits on *it*. Only a
genuinely external event — a restart, a release, someone else's unprompted
move — stands as written. This fires here first because the close is where
conditions get written; the revisit re-applies it at every read (plan.md).

**A lift-condition may no longer name another queue item.** "Cleared once [slug]
is built" is a dependency on queued work, and that has its own field now:
`Blocked by: [slug]`, checked by the queue lint. Lift-conditions are for
everything else — every wait outside the queue, *including* waiting for built
work to be released and running, which is an ordinary external event and no
longer has a marker of its own. If you find one naming a slug, rewrite it as `Blocked by:`
while you're here — that's a pointer fix, not a fate decision, so it rides this
close without an approval ask.

**Place ready `[user]` walk-through work above the marker.** The marker is the
single gate for walk-throughs as well as builds — /next walks a `[user]` item
through only when it sits above the marker.

```
prerequisite work shipped (built, and verified where a live check was needed)
    ->  place the [user] item ABOVE the marker
prerequisite still pending
    ->  it stays BELOW, exactly like any other not-yet-ready item
```

**Anti-pattern: don't hold a `[user]` item below the marker merely because it's the
user's to run.** Being a `[user]` item is not a reason to shelve it — only a
pending prerequisite keeps it below. This lives in the /plan close rather than
/next so the marker stays one positional gate, instead of /next growing a second
readiness check of its own. Narrate it when a `[user]` item moves above the marker
— one line naming which is now ready.

## Dependency-rot pass  [SILENT when clean; BRIEF when clearing]

A dependency statement can outlive its truth, and nothing routine acted on that
until this pass: stale `Blocked by:` lines were flagged by the queue lint on
every edit across multiple sessions, and only a human eventually noticing the
repetition cleared them. So the close acts:

```
a Blocked by: line whose named slug no longer resolves in the queue
    ->  REMOVE the line, and narrate the removal in one line.
        If the item still waits on something, that something is an external
        wait — record it as a lift-condition instead, so the clearing never
        silently strands an item.

a Blocked by: line pointing at an item BELOW the blocked one
    ->  NEVER cleared automatically. The dependency is real and the ORDER is
        wrong, so removing the line would delete true information. Surface it
        for a decision.
```

## Completed `[user]` items  [SILENT when none; BRIEF when closing one]

If the user mentioned during this session that they'd completed a `[user]` item,
record and remove it now through done.md's
**Completed `[user]`-item close**: a LOG entry per completed item named by its
slug, and the item removed from Processed. Fold each entry into this session's
records alongside the planning entry, and its slug into the commit. When nothing
was mentioned, say nothing — **never ask** whether any are done. There is no
completion ask anywhere in a `[user]` item's life.

## Clear the consumed forward-recommendation advisory  [SILENT when none; BRIEF when clearing]

/plan Step 1 *reads* the advisory to orient the session; the *clear* lives here,
at the one close that always runs however a /plan ends. It used to be tied to "once
the order is agreed" at the end of the discussion — a beat a no-work or off-ramp
/plan never reaches, so the clear was silently skipped and a stale advisory
survived.

```
it oriented this session          ->  DELETE it from Unprocessed now, whether or
                                      not the recommendation was followed
the user set aside what it advises   ->  DELETE it — their not-now is its
                                      answer, and a persist-condition never
                                      outlives it (plugin-behaviour.md, Set aside)
it names an unmet persist-condition  ->  LEAVE it in place
    ("persist until the cleared builds ship")
no advisory present               ->  say nothing
```

Narrate in one line when clearing. Distinct from filing the *fresh* advisory,
which the commit core does **before staging** so it rides this session's commit
(done.md) — Recommend next then only presents it. Clearing the consumed one and
filing the next are two different advisories.

**A partly-spent advisory is rewritten, not cleared or kept whole.** When part
of what it advises has been consumed (the work ran, the state changed) and part
persists under its condition, rewrite it at this close to only what still
stands — a half-true note orients the next session wrongly in both directions.

## 1. Write LOG entry  [DISCUSS, PROMPT]

Follow done.md's **LOG entry files** section, using its **Plan / setup** body
fields (`Queue changes`; `Work processed`). Planning sessions have no
pre-generated candidate — author the index entry fresh.

If a red flag was cleared this session, record **how** per done.md's Recording a
cleared red flag: for a design-out, how it was eliminated; for an acceptance, what
the user was warned about and that they chose to proceed. Clearing happens at
processing, so /plan is where this record is written.

**If a `_plan.md` exists, read its disposition list** — kept and deleted items with
their slugs — and use it to fill the entry's Queue changes and Work processed
lines. It's the mechanical record of what this session did, so the entry doesn't
have to be reconstructed from memory.

## 2. Commit

Run the commit core in done.md. Staged paths are the changed project docs
(QUEUE.md, SPEC.md, LOG/) — planning sessions touch nothing else.

**Override the commit core's push offer: a planning session commits and doesn't
offer push.** Planning state is local bookkeeping, and push is reserved for
shipping — in a self-hosting project a push fires the full push-and-rezip ritual
off a commit that shipped nothing. Push stays available when the user asks for it
or is deliberately backing up; a default, not a prohibition.

**Where a planning close ALSO closes a completed `[user]` item, the push offer
applies and this override yields.** That case is real — done.md supports it — and
the two rules collided with no carve-out either side. It resolves toward offering,
because the reason for suppressing is that a planning commit ships nothing, and a
completed `[user]` item is not nothing: it is real project progress the user did,
and leaving it unpushed is the outcome the suppression was never aimed at. So the
test is whether the commit carries anything beyond planning bookkeeping. If it
does, offer; if it is purely queue and log housekeeping, don't.

**Delete `_plan.md`** if one exists, as part of the close — same lifecycle as
_build.md. It was working state only and was never committed, so removing the file
is all that's needed.

## 3. Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Plan / setup close** delta: a
fresh setup session whose only work item is the rough first build item recommends
/plan to scope it, never /next; otherwise the shared overlap scan + ladder apply.

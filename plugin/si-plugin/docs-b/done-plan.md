---
name: done-plan
docset: B
note: >
  Close-out for planning sessions. Reached from done.md's router when no
  _build.md exists — /plan sessions, /setup sessions, and any session that
  changed only the method docs.
---

# Plan close-out

Every step below runs at every plan-type /done close — a /plan session, a /setup
session, and a session that changed only the method docs. The reorder, the marker
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

Do **not** reintroduce `Blocks:` / `Depends on:` headers. The one dependency
field that exists is `Blocked by: [slug]`, written on the item that is held, and
it is lint-checked precisely so it can't go stale the way those headers did.
Everything else stays prose slug-references.

When a reorder *is* warranted:

```
Unprocessed  ->  UNLOCK-POTENTIAL. Process first what would unblock the most
                 other work; an item that gates others sits above one that
                 stands alone.
Processed    ->  BUILD-ORDER. Build first what unblocks or reshapes the framing
                 for later work; an item whose output is a prerequisite for a
                 later item sits above the one that needs it.
```

**Within Processed, place `[user]` and `[audit]` lines end-preferred**, after
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

invoke:  python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
             <Processed|Unprocessed> <slug1> <slug2> …
         # give the section's full desired top-to-bottom slug order
         # for Processed, place the marker with:
         #     --marker-after <slug|TOP|BOTTOM>
         # omit it to keep the marker where it currently sits

trust the self-check:  exits non-zero -> NOTHING was written. A slug-set
                       mismatch usually means the queue changed under you —
                       re-read it, rebuild the order, re-run.
```

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

**Name the blocker when placing any item below the marker.** One line in the
item's block:

```
Blocked by: [slug]
```

The slug must resolve to a real work item in this queue — that is what the queue
lint checks. Below the line means blocked by a named queue item and nothing else.

```
nothing in the queue blocks it   ->  it goes ABOVE the marker, not below
it waits on something in the     ->  file that as its own item in Unprocessed
    world (a restart, a reply,        first, then name it here. /plan will
    a site going live)                process it like any other work.
you can't yet say what it        ->  Unprocessed — it still needs thought
    would build
```

This is the enabling half of the below-the-line revisit: with a slug the revisit
is a single check per item, and with a sentence it was an interpretation. It also
closes a failure the sentence version kept producing — an item waiting on
something nobody had filed, so the wait could never end.

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
it names an unmet persist-condition  ->  LEAVE it in place
    ("persist until the cleared builds ship")
no advisory present               ->  say nothing
```

Delete it with the mechanical mover, addressed by its reserved slug — the same
tool and the same plugin-root derivation as the reorder above:

```
python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> \
    --delete forward-advisory Unprocessed
```

Narrate in one line when clearing. Distinct from "Recommend next", which *files a
fresh* advisory after the commit — clearing the consumed one and filing the next
are two different advisories.

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

Run the commit core in done.md. Staged paths are the changed method docs
(QUEUE.md, SPEC.md, LOG/) — planning sessions touch nothing else.

**Override the commit core's push offer: a planning session commits and doesn't
offer push.** Planning state is local bookkeeping, and push is reserved for
shipping — in a self-hosting project a push fires the full push-and-rezip ritual
off a commit that shipped nothing. Push stays available when the user asks for it
or is deliberately backing up; a default, not a prohibition.

**Delete `_plan.md`** if one exists, as part of the close — same lifecycle as
_build.md. It was working state only and was never committed, so removing the file
is all that's needed.

## 3. Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Plan / setup close** delta: a
fresh setup session whose only work item is the rough first build item recommends
/plan to scope it, never /next; otherwise the shared overlap scan + ladder apply.

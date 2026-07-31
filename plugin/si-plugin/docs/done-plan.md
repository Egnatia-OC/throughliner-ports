# Plan close-out

Close-out for planning sessions. Reached from done.md's router when no _build.md exists — /plan sessions, /setup sessions (scaffolding only adds the method docs), and any other session that changed only the method docs.

## Spec-sync gate [SILENT] when in sync; [PROMPT] when drift found

Before drafting the LOG entry, check one thing: did a decision this session change what SPEC says? If a planning decision changed product truth — a capability, a constraint, a rule the app enforces, who it's for — and SPEC.md wasn't updated to match, stop the close. Surface the drift in plain words, get the user's approval, and update SPEC.md in this same session so the edit lands in this commit. Only then continue to the LOG entry. (Unlike the coherence backstop above, this fix happens here and isn't bounced to /plan: editing SPEC to match a decision the user already made this session is recording, not re-planning — the decision is settled, SPEC is just being brought into line with it.)

The check is semantic, not mechanical — "did this session's decisions make a SPEC sentence wrong or incomplete?" is a judgment no hook can make and no lint can backstop, so Claude actually running it is the only enforcement. Run it on every plan-type close where a product-truth decision was made; a session that changed only queue ordering or captures touched no SPEC sentence and passes silently.

The why this gate exists, and what it replaces: spec-driven development's contract is that any change altering behaviour updates the spec in the same commit (resources/research/spec-driven-development-edit-workflow.md). The retired spec-edit step used to carry SPEC changes through their own /next cycle; this commit-boundary gate enforces the same atomicity directly, so /plan can edit SPEC in-session and the close guarantees SPEC never lags the decision that changed it. Last time SPEC was editable in /plan it got left behind — this gate is what makes in-session editing safe. Scope: every plan-type /done close (plan, setup, method-doc-only sessions).

## Reorder both sections [SILENT when no reorder; BRIEF when reordering]

Walk both sections and reorder by the principle that fits each:
- **Unprocessed → unlock-potential.** Process first what would unblock the most other work — an item whose resolution lets other items move forward sits above one that stands alone. Processing is meant to move work toward ready, so items that gate others come first.
- **Processed → build-order.** Build first what unblocks or reshapes the framing for later work — an item whose output is a prerequisite or input for a later item sits above the one that needs it.

**Within Processed, place `[user]` and `[audit]` lines end-preferred, after contiguous blocks of build/write work.** Build-order above is the primary sort; this is a tie-adjustment applied on top of it. A `[user]` handover and an `[audit]` review both force /next to stop for the user — a handover the user has to run, an audit whose findings the user has to approve — so a `[user]` or `[audit]` line sitting *inside* a contiguous run of build items interrupts an otherwise-unattended build sequence. Position both flavors at the **end** of a contiguous build/write block rather than in its middle, so the build run stays continuous and the human-in-the-loop stops batch to the end of the block. This is the placement half of the run-boundary work: /next itself no longer terminates at a `[user]` line (it builds all cleared Claude work, then hands over — next.md), and this reorder is what keeps the handovers and audits from splitting the Claude block in the first place. Don't move a `[user]` or `[audit]` line *past* a build item that genuinely depends on its outcome — build-order wins where a real dependency exists; end-preferred is the default only among items with no such ordering constraint. Narrate it when it changes the pick order, like any reorder.

Claude reorders and narrates; it does not ask. This is the ordering-ownership rule (plugin-behaviour.md Dependency ownership: "a judgment call Claude makes and narrates, not a question it asks") made specific to the close. The user owns keep/delete and scope, not order; order is low-stakes and reversible, so the narration is the catch-point where the user can redirect.

**Use the mechanical mover to apply the reorder — don't retype blocks.** Moving a work item by hand means retyping its whole prose block verbatim, which on a long queue silently degrades to a partial sort and risks corrupting an item with no error. Instead, once you've decided the order, apply it with the shipped `reorder_queue.py` script: it moves whole blocks byte-for-byte from a slug order you supply, and self-checks (same slug set and same block contents before and after, or it refuses to write and changes nothing). Only the *decision* — the desired order — passes through you; never the prose.

- **Locate the script** relative to the plugin, not by a hardcoded path: it lives at `scripts/reorder_queue.py` under the plugin root, and the plugin root is the grandparent of the running skill's base directory (the base directory Claude is given at skill invocation is `.../<plugin-root>/skills/<skill>`). Derive it from there so it resolves wherever the plugin is installed.
- **Invoke it per section** you're reordering: `python <plugin-root>/scripts/reorder_queue.py <QUEUE.md path> <Processed|Unprocessed> <slug1> <slug2> …` giving the section's full desired top-to-bottom slug order. For Processed, place the cleared-to-run marker with `--marker-after <slug|TOP|BOTTOM>`; omit it to keep the marker where it currently sits. (Position the marker per "Position the cleared-to-run line" below — the mover just applies the placement you decided.)
- **Trust the self-check.** If the script exits non-zero (a slug-set mismatch usually means the queue changed under you — re-read it and rebuild the order), nothing was written; fix the input and re-run. A supplied order that matches the current queue is the only thing it needs.

Narration scales so it stays a real catch-point, not noise: a reorder that changes what /next would pick next is flagged clearly — e.g. "Moved [slug-a] above [slug-b] so it builds first — say if not." A trivial tidy (e.g. grouping related items with no pick-order change) gets one line. No reorder needed: say nothing. Scope: every plan-type /done close, both sections.

## Position the cleared-to-run line [SILENT when its placement is unchanged; BRIEF when it moves]

Place or move the `--- Cleared to run above this line ---` marker in the Processed section so everything above it is greenlit to build and everything below it is processed but not yet greenlit. Walk Processed top-down and put the line just below the last item the user has agreed is ready to build; work the user is still settling — held for more thought, or waiting on something outside the queue — sits below it. If every processed item is greenlit, the line goes at the bottom of Processed; if none is, at the top. Narrate where it lands **only when it actually moves** this close — one plain line, e.g. "Everything processed this session is cleared to run; the line sits at the bottom." When your walk confirms the line is already correctly placed and nothing moved it, confirm silently and say nothing. This is the boundary the user would otherwise have to work out by hand each session, and the unattended build mode later inherits it as its run bound. A setup or method-doc-only session with no processed work has no line to place and nothing to reorder — say nothing. Scope: every plan-type /done close.

**Hold back an item that depends on unverified work.** When placing the marker, a processed item must not be cleared if it depends — by a slug reference in its prose — on another item that has been built but whose verification is still *pending*: a host-side item shipped but not yet confirmed live after reinstall (its liveness unresolved by the content stamp, or its observed check simply not run yet). Keep such an item below the marker until the dependency's verification clears. The why is autonomy: a cleared item can be built unattended by /next with no user in the loop, so clearing one that rests on built-but-unverified work would let the run stack committed work on a foundation that might later fail its check — the exact compounding an attended session would catch before it stacked. The distinction is the whole point: a dependency merely being *built* is not enough to clear its dependents; it must be built **and** verified. A dependency built and confirmed live places no such hold. Narrate it when it holds an item back — one plain line naming which item is waiting on which.

**Record the lift-condition when placing any item below the marker.** Whenever an item is placed (or kept) below the cleared-to-run marker — for a pending dependency, an external wait, or held-for-more-thought — record in the item's prose the specific event or dependency that would lift it: "cleared once [slug] is built and verified", "after a full computer restart", "once the manifest is pushed". Prose, not a new hook-parsed field — this keeps faith with rationale-is-prose and needs no hook change. This is the enabling half of the below-the-line revisit (plan.md Step 1): without a recorded condition, that revisit can't tell a still-waiting item from a now-ready one without nagging the user. An item held below with no recordable lift-condition is a sign it belongs in Unprocessed (still needs thought), not shelved below the line.

**Place ready `[user]` handover work above the marker.** The cleared-to-run marker is the single gate for handover as well as for builds: /next hands over a `[user]` item only when it sits above the marker. So when positioning the marker, place a `[user]` item **above** it once its prerequisite work has shipped — the work it waits on is built and (where that work needed a live check) verified, re-derived from LOG the same way the hold-back rule above re-derives dependency state. A `[user]` item whose prerequisite is still pending stays **below** the marker, exactly like any other not-yet-ready item. This is why a `[user]` verification item for host-side work stays below until the reinstall lands and the shipped work is confirmed: its prerequisite isn't met yet. **Anti-pattern: don't hold a `[user]` item below the marker merely because it's the user's to run.** Being a handover is not a reason to shelve it — a ready `[user]` item with no pending prerequisite belongs above the marker so /next hands it over; only a pending prerequisite keeps it below. The why this lives in the /plan close and not in /next: the marker stays one positional gate rather than /next growing a second readiness check of its own — /next simply hands over what sits above the marker. Narrate it when a `[user]` item moves above the marker this close — one plain line naming which handover is now ready. Scope: every plan-type /done close, walked alongside the marker placement above.

## Completed `[user]` handovers (close any the session confirmed done) [SILENT when none; BRIEF when closing one]

If this /plan session confirmed that a `[user]` handover item was completed async — the Step 1 completion-ask surfaced it (plan.md Step 1) — record and remove it now through done.md's **Completed `[user]`-item close**: a LOG entry per completed item named by its slug, and the item removed from Processed. This is the /plan half of the handover-completion close (the /next-adjacent half is a standalone /done). Fold each such item's LOG entry into this session's records alongside the planning entry below, and its slug into the commit. When the session confirmed no completed handover, say nothing.

## Clear the consumed forward-recommendation advisory [SILENT when none; BRIEF when clearing]

This is the backstop clear for the forward-recommendation advisory (plugin-behaviour.md Forward-recommendation advisory). /plan Step 1 *reads* the advisory to orient the session; the *clear* lives here, at the one close that always runs however a /plan ends. It used to be tied to "once the processing/build order is agreed" at the end of the /plan discussion — a beat a no-work or off-ramp /plan never reaches, so the clear was silently skipped and a stale advisory survived. Anchoring it to this close fixes that.

If Unprocessed holds a forward-recommendation advisory (a "Last session advises…" line):

- **Clear it if it oriented this session.** If this session's /plan read it at Step 1 and it shaped where the session focused, it has done its job — delete it from Unprocessed now, whether or not the recommendation was followed. Its removal is a QUEUE.md change that stages into this close's commit like the other queue edits.
- **Honour an explicit persist-condition.** If the advisory names a condition to persist past a single session — e.g. "persist until the cleared builds ship", tied to a build event rather than the next /plan — and that condition hasn't been met, **leave it in place**. Only a standard advisory with no unmet persist-condition is cleared here.

Narrate in one line when clearing one; say nothing when there's no advisory or a persist-condition holds it. This is distinct from Step 3's "Recommend next", which *files a fresh* advisory after the commit — clearing the consumed one and filing the next one are two different advisories.

## 1. Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what motivated this session, as inline prose. For a planning session, what motivated these queue changes; for a setup session, what was set up and why. No `Why:` label.]

**Queue changes:**
- [work processed, reordered, or modified — for a setup session, the first rough build item and the docs scaffolded]

**Work processed:** [kept (moved to Processed) / deleted, with slugs, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file. This entry is the session's summary — there is no separate chat recap. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files).

If a red flag was cleared during this session — a risk designed out in-session, or one the user was told plainly and chose to carry — record how in this entry per done.md Recording a cleared red flag: for a design-out, how it was eliminated; for an acceptance, what the user was warned about and that they chose to proceed. Clearing happens at processing, so /plan is where this record is written. The cleared flag itself lives in the queue as a marker on the work item at `State: cleared` (plugin-behaviour.md Flag states).

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

There is no pre-generated candidate for planning sessions — author the index entry fresh against the Index entries rule.

If a `_plan.md` exists, read its disposition list — kept and deleted items with their slugs — and use it to fill the entry's Queue changes and Work processed lines. It's the mechanical record of what this session did, so the entry doesn't have to be reconstructed from memory.

## 2. Commit

Run the commit core in done.md. The staged paths are the changed method docs (QUEUE.md, SPEC.md, LOG/) — planning sessions touch nothing else.

Override the commit core's push offer: a planning session commits and doesn't offer push. The why: planning state is local bookkeeping, and push is reserved for shipping — in a self-hosting project a push fires the full push-and-rezip ritual off a commit that shipped nothing. Push stays available when the user asks for it or is deliberately backing up; it's a default, not a prohibition.

Delete `_plan.md` if one exists, as part of the close — same lifecycle as _build.md. It was working state only and was never committed, so removing the file is all that's needed.

## 3. Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the queue situation in everyday words. Keep the plain statement accurate: don't say the queue is clear when work is still waiting to be looked over.

Before recommending, scan any still-unprocessed work for overlap with the top processed item — work that contradicts, invalidates, or would benefit the top item if it were sorted first. State the scan's result either way, not only when it blocks: nothing unprocessed — say nothing's waiting for /plan; unprocessed work waiting but none overlaps the next item — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three items are waiting to be sorted; none touches the next piece of work, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
- Fresh setup session whose only work item is the rough first build item: recommend /plan to scope it, never /next. The interview wrote that item deliberately unscoped, so it isn't ready to build yet — scoping is /plan's job.
- Processed work exists: name the next item, then ask whether the user is continuing into a /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
- Processed work empty: "Queue is clear. Run /plan when you have more."

**File the forward-recommendation advisory** when this step made a concrete recommendation — name what to plan or build next and why. File it per plugin-behaviour.md Forward-recommendation advisory: a capture at the top of Unprocessed, worded as advice, consumed and cleared by the next /plan. When the recommendation is generic ("run /plan when you have more"), no advisory is filed.

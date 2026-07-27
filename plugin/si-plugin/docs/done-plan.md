# Plan close-out

Close-out for planning sessions. Reached from done.md's router when no _build.md exists — /plan sessions, /setup sessions (scaffolding only adds the method docs), and any other session that changed only the method docs.

## Spec-sync gate [SILENT] when in sync; [PROMPT] when drift found

Before drafting the LOG entry, check one thing: did a decision this session change what SPEC says? If a planning decision changed product truth — a capability, a constraint, a rule the app enforces, who it's for — and SPEC.md wasn't updated to match, stop the close. Surface the drift in plain words, get the user's approval, and update SPEC.md in this same session so the edit lands in this commit. Only then continue to the LOG entry. (Unlike the coherence backstop above, this fix happens here and isn't bounced to /plan: editing SPEC to match a decision the user already made this session is recording, not re-planning — the decision is settled, SPEC is just being brought into line with it.)

The check is semantic, not mechanical — "did this session's decisions make a SPEC sentence wrong or incomplete?" is a judgment no hook can make and no lint can backstop, so Claude actually running it is the only enforcement. Run it on every plan-type close where a product-truth decision was made; a session that changed only queue ordering or captures touched no SPEC sentence and passes silently.

The why this gate exists, and what it replaces: spec-driven development's contract is that any change altering behaviour updates the spec in the same commit (resources/research/spec-driven-development-edit-workflow.md). The retired spec-edit step used to carry SPEC changes through their own /next cycle; this commit-boundary gate enforces the same atomicity directly, so /plan can edit SPEC in-session and the close guarantees SPEC never lags the decision that changed it. Last time SPEC was editable in /plan it got left behind — this gate is what makes in-session editing safe. Scope: every plan-type /done close (plan, setup, method-doc-only sessions).

## Cleared-to-run line (confirm; narrate only if you had to fix it) [SILENT when placement is correct; BRIEF when you fix it]

/plan positions the `--- Cleared to run above this line ---` marker at its own close (plan.md Step 3). Confirm it's present in the Processed section and sits where it belongs — everything above it processed and greenlit to build, everything below it processed but still being settled. If it's present and correctly placed — the normal case, since /plan just positioned it — confirm silently and say nothing; a plan→done flow already narrated the boundary at the /plan close, so restating it here just says the same thing twice. Only if it's missing or misplaced: fix it with the user, then narrate the boundary plainly in one line — e.g. "Two items are cleared to run; the line sits above [work-x], which isn't greenlit yet." A setup or method-doc-only session with no processed work has no line to place — say nothing. Scope: every plan-type /done close.

## Completed `[user]` handovers (close any the session confirmed done) [SILENT when none; BRIEF when closing one]

If this /plan session confirmed that a `[user]` handover item was completed async — the Step 1 completion-ask surfaced it (plan.md Step 1) — record and remove it now through done.md's **Completed `[user]`-item close**: a LOG entry per completed item named by its slug, and the item removed from Processed. This is the /plan half of the handover-completion close (the /next-adjacent half is a standalone /done). Fold each such item's LOG entry into this session's records alongside the planning entry below, and its slug into the commit. When the session confirmed no completed handover, say nothing.

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

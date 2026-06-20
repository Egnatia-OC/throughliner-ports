# Plan close-out

Close-out for planning sessions. Reached from done.md's router when no _build.md exists — /plan sessions, /setup sessions (scaffolding only adds the method docs), and any other session that changed only the method docs.

## Coherence backstop (run first) [SILENT] when clean; [PROMPT] when broken

Before drafting the LOG entry, re-read QUEUE.md and walk the dependency graph once. /plan's own close-out already checks this ([plan-close-dep-check]); this is the second pair of eyes in case a break slipped through. The same three checks /plan runs:
- every `Depends on:` slug sits above its own batch in Batches (or has shipped per LOG/index.md, or is otherwise satisfied);
- every slug named in any `Depends on:`, `Blocks:`, or `Blocked by:` header resolves to a real item — a batch, a parked item, or a shipped slug in LOG;
- no batch depends on a capture still sitting unprocessed below the Captures divider.

Coherent graph: continue to the LOG entry below, say nothing. Broken graph: stop the close — don't fix it, don't commit. Surface what's broken in plain words and send the user to /plan to sort it. Example: "Before I record this — [batch-a] depends on [batch-b], which sits below it in the queue. That's a planning fix, so run /plan to reorder; I won't commit a queue /next would trip on."

The why this bounces to /plan rather than fixing it here: reordering the queue is planning work, and /done fixing it would cross the build/plan skill line — /done records and commits, it doesn't re-plan. Committing a broken graph ships a queue /next trips on, so surfacing and routing back is the safe move. A fresh /done is a second pair of eyes on the graph, not a second planner. Scope: every plan-type /done close (plan, setup, and method-doc-only sessions).

## 1. Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what motivated this session, as inline prose. For a planning session, what motivated these queue changes; for a setup session, what was set up and why. No `Why:` label.]

**Queue changes:**
- [batches added, reordered, or modified — for a setup session, the first rough build entry and the docs scaffolded]

**Captures routed:** [promoted/parked/dropped, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file. This entry is the session's summary — there is no separate chat recap. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files).

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

There is no pre-generated candidate for planning sessions — author the index entry fresh against the Index entries rule.

If a `_plan.md` exists, read its routed list — promoted, parked, and dropped items with their slugs — and use it to fill the entry's Queue changes and Captures routed lines. It's the mechanical record of what this session did, so the entry doesn't have to be reconstructed from memory.

## 2. Commit

Run the commit core in done.md. The staged paths are the changed method docs (QUEUE.md, SPEC.md, LOG/) — planning sessions touch nothing else.

Override the commit core's push offer: a planning session commits and doesn't offer push. The why: planning state is local bookkeeping, and push is reserved for shipping — in a self-hosting project a push fires the full push-and-rezip ritual off a commit that shipped nothing. Push stays available when the user asks for it or is deliberately backing up; it's a default, not a prohibition.

Delete `_plan.md` if one exists, as part of the close — same lifecycle as _build.md. It was working state only and was never committed, so removing the file is all that's needed.

## 3. Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the captures situation in everyday words — never the background term "processed / unprocessed captures" (see plugin-behaviour.md Vocabulary). Keep the plain statement accurate: don't say the queue is clear when captures are still waiting to be sorted. The scan instruction's "unprocessed Captures" wording below stays as-is — this guard governs only what's said to the user.

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). State the scan's result either way, not only when it blocks: Captures empty — say nothing's waiting for /plan; Captures waiting but none overlap the next batch — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three captures are waiting; none touches the next batch, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
- Fresh setup session whose only batch is the rough Q4 build entry: recommend /plan to scope it, never /next. The interview wrote that entry deliberately unscoped, so it isn't ready to build yet — scoping is /plan's job.
- Parked items unblocked by this session's planning work (per plugin-behaviour.md Dependency ownership Unpark watch) → mention the unpark candidate(s) as part of the recommendation.
- Batches exist: name the next batch, then ask whether the user is continuing into a /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
- Batches empty: "Queue is clear. Run /plan when you have more."

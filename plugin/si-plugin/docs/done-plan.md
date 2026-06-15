# Plan close-out

Close-out for planning sessions. Reached from done.md's router when no _build.md exists — /plan sessions, /setup sessions (scaffolding only adds the method docs), and any other session that changed only the method docs.

## 1. Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what motivated this session, as inline prose. For a planning session, what motivated these queue changes; for a setup session, what was set up and why. No `Why:` label.]

**Queue changes:**
- [batches added, reordered, or modified — for a setup session, the first rough build entry and the docs scaffolded]

**Captures routed:** [promoted/parked/dropped, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file. This entry is the session's summary — there is no separate chat recap.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

There is no pre-generated candidate for planning sessions — author the index entry fresh against the Index entries rule.

If a `_plan.md` exists, read its routed list — promoted, parked, and dropped items with their slugs — and use it to fill the entry's Queue changes and Captures routed lines. It's the mechanical record of what this session did, so the entry doesn't have to be reconstructed from memory.

## 2. Commit

Run the commit core in done.md. The staged paths are the changed method docs (QUEUE.md, SPEC.md, REGISTRY.md, LOG/) — planning sessions touch nothing else.

Delete `_plan.md` if one exists, as part of the close — same lifecycle as _build.md. It was working state only and was never committed, so removing the file is all that's needed.

## 3. Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
- Fresh setup session whose only batch is the rough Q4 build entry: recommend /plan to scope it, never /next. The interview wrote that entry deliberately unscoped, so it isn't ready to build yet — scoping is /plan's job.
- Parked items unblocked by this session's planning work (per plugin-behaviour.md Dependency ownership Unpark watch) → mention the unpark candidate(s) as part of the recommendation.
- Batches exist: name the next batch, then ask whether the user is continuing into a /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
- Batches empty: "Queue is clear. Run /plan when you have more."

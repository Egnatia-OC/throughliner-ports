# Plan close-out

Close-out for planning sessions. Reached from done.md's router when no _build.md exists — /plan sessions, and any other session that changed only the method docs.

## 1. Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what motivated these queue changes, as inline prose. No `Why:` label.]

**Queue changes:**
- [batches added, reordered, or modified]

**Captures routed:** [promoted/parked/dropped, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. After approval, write it to the new entry file. This entry is the session's summary — there is no separate chat recap.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

There is no pre-generated candidate for planning sessions — author the index entry fresh against the Index entries rule.

## 2. Commit

Run the commit core in done.md. The staged paths are the changed method docs (QUEUE.md, SPEC.md, REGISTRY.md, LOG/) — planning sessions touch nothing else.

## 3. Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors next.md Step 1.3). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
- Parked items unblocked by this session's planning work (per plugin-behaviour.md Dependency ownership Unpark watch) → mention the unpark candidate(s) as part of the recommendation.
- Batches exist: name the next batch, then ask whether the user is continuing into a /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
- Batches empty: "Queue is clear. Run /plan when you have more."

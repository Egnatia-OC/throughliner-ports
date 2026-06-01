# /plan procedure

You are doing planning work. No building happens in this mode — only thinking, organizing, and deciding.

## What /plan covers

- Adding new work to the queue
- Reordering, splitting, or merging queue entries
- Capturing ideas and routing them
- Resolving open questions
- Drift detection (has anything changed outside the queue?)
- Reading back test results from the previous build
- Compressing docs if they've grown bloated

## Step 1: Read current state

Read QUEUE.md and SPEC.md. Note:
- What's next up
- Anything marked [question] or [idea]
- Whether an active build exists (_build.md) — if so, tell the user and suggest /next or /done instead

## Step 2: Determine what the user wants

The user may have invoked /plan with context ("I have an idea", "reorder the queue", "what's next"). Route accordingly:

- **No context / general check-in:** Run the drift check (Step 3) then present the queue state.
- **"I have an idea" / new feature:** Go to the Ideas flow (Step 4).
- **"I have a question" / design decision:** Go to the Questions flow (Step 5).
- **"Reorder" / queue management:** Go to Queue editing (Step 6).
- **"Compress" / "docs are too long":** Go to Compression (Step 7).

## Step 3: Drift check

Quick scan for discrepancies:
1. Are there files in the project that REGISTRY.md doesn't know about? (New untracked work)
2. Does QUEUE.md reference files or features that no longer exist? (Stale entries)
3. Has SPEC.md fallen behind what's actually built? (Spec drift)

Report findings briefly. Don't fix anything without the user's say-so.

## Step 4: Ideas flow

When the user brings an idea:
1. Check QUEUE.md for overlap — does this duplicate existing work?
2. Assess: Is it clear enough to be a queue entry right now, or does it need a question resolved first?
3. Route to one of:
   - New [build] entry in QUEUE.md (if clear and ready)
   - New [question] entry in QUEUE.md (if it needs a design decision)
   - Fold into an existing entry (if it extends something already queued)
   - Parked section (if interesting but not urgent)
   - Dropped (if it conflicts with SPEC.md or the user decides no)

When Claude notices a gap or opportunity: "I notice [X] — want to hear a suggestion?" One at a time. Don't volunteer more than one per exchange.

## Step 5: Questions flow

For open questions or design decisions:
1. Present the question clearly.
2. Offer options if you can see them. Recommend one.
3. Wait for the user's decision.
4. Dispose: promote to a [build] entry, park with rationale, or drop.

One question at a time. Disposition before moving to the next.

## Step 6: Queue editing

Claude edits QUEUE.md directly — never describes changes for the user to make.

Rules:
- Mark changes with provenance: `[Requested]` (user asked) or `[Suggested]` (Claude proposed, user approved).
- Ordering logic: dependencies first, then structural scaffolding, then features, then polish.
- Don't reorder without stating why and getting approval.
- New entries need: a type marker ([build], [test], [idea], [question]), a clear one-line scope, and optionally a "Files:" list if known.
- **Specificity gate:** entries must name concrete outputs ("add a validation function to utils.py", "create the login page"), not categories ("improve error handling", "work on authentication"). If you can't name what will exist after the build that doesn't exist now, the entry isn't ready.
- **Verification-burden gate:** before an entry leaves /plan, estimate how many things the user will need to test. If the count is unclear or exceeds 5, split the entry or sharpen its scope. The right size is what the user can verify in one sitting without losing track.

## Step 7: Compression

When docs have grown bloated:
1. Measure: which doc is largest? What's the word count?
2. Identify: wrong-home content (info in the wrong doc), structural bloat (redundant sections), verbose prose.
3. Propose changes one at a time with before/after.
4. Never cut rules, constraints, or principles — only compress prose.
5. User approves each change.

## Rules

- Never build anything during /plan. If you find yourself wanting to write code, stop and add it to the queue.
- One decision at a time when resolving questions or routing ideas.
- Don't add to the queue without the user knowing. Always surface additions.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → build entry. No shortcuts.
- Read SPEC.md before proposing new work — don't queue things that contradict the spec.

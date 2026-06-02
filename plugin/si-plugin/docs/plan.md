# /plan procedure

You are doing planning work. No building happens in this mode — only thinking, organizing, and deciding.

## What /plan covers

- Adding new work to the queue
- Reordering, splitting, or merging queue entries
- Capturing items and routing them
- Resolving open questions
- Reading back test results from the previous build
- Compressing docs if they've grown bloated

## Step 1: Read current state

Read QUEUE.md and SPEC.md. Note:
- What's the top batch in the Batches section
- Are there items in the Captures section waiting to be processed
- Whether an active build exists (_build.md) — if so, tell the user and suggest /next or /done instead

## Step 2: Determine what the user wants

The user may have invoked /plan with context ("I have an idea", "reorder the queue", "what's next"). Route accordingly:

- **No context / general check-in:** Process accumulated items (Step 3) first, then present the queue state.
- **"I have an idea" / new feature:** Go to the Captures flow (Step 3).
- **"I have a question" / design decision:** Go to the Questions flow (Step 4).
- **"Reorder" / queue management:** Go to Queue editing (Step 5).
- **"Compress" / "docs are too long":** Go to Compression (Step 6).

## Step 3: Captures flow [SEQUENCE, PROMPT]

### Processing accumulated items

At the start of a /plan session, check the Captures section of QUEUE.md. If items have accumulated there (captured during builds or between sessions), process them one at a time before moving to new work. For each item, regardless of its type marker ([idea], [question], [build], [test]):

1. Present it to the user.
2. Discuss — engage with the substance of the item before jumping to disposition. If it's open-ended or has exploratory language ("or similar", "maybe", "consider"), explore alternatives and tradeoffs. If it's straightforward, a brief assessment is enough. The goal is to make sure the user has enough context to make a good disposition call.
3. Dispose:
   - **Promote** — add as entry in an existing batch, or create a new batch for it (Step 5)
   - **Question first** — it needs a design decision before it can become work. Go to Step 4.
   - **Park** — move to Captures → Parked (interesting but not now)
   - **Drop** — remove it (conflicts with SPEC.md, or user decides no)
4. Remove the item from the Captures section after routing.

One item at a time. Discussion and disposition before moving to the next.

### New items from conversation

When the user brings a new item (idea, question, feature request, observation):
1. Check QUEUE.md for overlap — does this duplicate existing work?
2. Discuss — same as above. Engage with substance before disposition.
3. Dispose using the same options as above (promote, question first, park, drop).

When Claude notices a gap or opportunity: "I notice [X] — want to hear a suggestion?" One at a time. Don't volunteer more than one per exchange.

## Step 4: Questions flow [DISCUSS, PROMPT]

For open questions or design decisions:
1. Present the question clearly.
2. Offer options if you can see them. Recommend one.
3. Wait for the user's decision.
4. Dispose: promote to a [build] entry, park with rationale, or drop.

One question at a time. Disposition before moving to the next.

## Step 5: Queue editing

Claude edits QUEUE.md directly — never describes changes for the user to make.

### Batch structure

Work is organized into **batches**, not loose entries. Each batch is one /next session. Format:

```markdown
**Batch title**
Files:
- `path/to/file1.ext`
- `path/to/file2.ext`
- [build] What to do in file1
- [build] What to do in file2
- [test] How to verify it works
```

A batch groups related entries that share a file list. Builds come first, tests follow. Every batch has a bold title, a Files: list, and one or more type-marked entries.

### Creating and editing batches

- Ordering logic: dependencies first, then structural scaffolding, then features, then polish.
- Don't reorder batches without stating why and getting approval.
- New entries need: a type marker ([build], [test], [idea], [question]) and a clear one-line scope.
- Entries can be added to an existing batch if they touch the same files and make sense as one unit of work.

### Sizing gates (apply to the batch, not individual entries)

- **Specificity gate:** each entry within a batch must name concrete outputs ("add a validation function to utils.py", "create the login page"), not categories ("improve error handling", "work on authentication"). If you can't name what will exist after the build that doesn't exist now, the entry isn't ready.
- **Verification-burden gate:** before a batch leaves /plan, estimate how many things the user will need to test across all its entries. If the count is unclear or exceeds 5, split the batch or sharpen its scope. The right size is what the user can verify in one sitting without losing track. A batch that touches 8 files but has 3 observable behaviours is fine. A batch that touches 2 files but produces 15 things to test is too big.

## Step 6: Compression

When docs have grown bloated:
1. Measure: which doc is largest? What's the word count?
2. Identify: wrong-home content (info in the wrong doc), structural bloat (redundant sections), verbose prose.
3. Propose changes one at a time with before/after.
4. Never cut rules, constraints, or principles — only compress prose.
5. User approves each change.

## Step 7: Close out [BRIEF, PROMPT]

When planning work is done (ideas processed, questions resolved, queue updated):

1. Summarize what changed this session.
2. Say: "Run /done to record this and commit, or keep planning."

Don't skip this — /done writes the log entry and handles the commit. Planning sessions close through /done just like build sessions do.

## Rules

- Never build anything during /plan. If you find yourself wanting to write code, stop and add it to the queue.
- One item at a time when resolving questions or routing captured items.
- Don't add to the queue without the user knowing. Always surface additions.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.
- Read SPEC.md before proposing new work — don't queue things that contradict the spec.
- Process accumulated items before new planning work. The Captures section is the inbox.

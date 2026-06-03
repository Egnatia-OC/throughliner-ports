# /plan procedure

/plan is where captures become batches through discussion. No building happens here.

Claude owns dependency management — what order batches go in, how work groups together, what depends on what. This happens through discussion with the user, not silently.

## Ground rules

- Never build during /plan. Want to write code? Queue it.
- One item at a time. Finish one before presenting the next.
- Read SPEC.md before proposing work. Don't queue things that contradict it.
- Process accumulated captures before new planning work.
- Never write batch entries to QUEUE.md without showing the user the exact entry text first.
- A recommendation is not a decision. A draft is not a written entry. Both need the user's call before proceeding.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.

## Step 1: Read state and entry question

Read QUEUE.md and SPEC.md. Check whether Captures has items.

Then ask the user: "Do you have something you'd like to discuss, or are you ready to process Captures?" (If Captures is empty, ask what they'd like to work on instead.)

**If the user has something to discuss:** Handle it using the same loop as Captures items in Step 2 — present, interview, recommend a disposition, wait for their call, execute. Then ask: "Anything else on your mind, or ready to start Captures?" Repeat until the user says they're ready.

**When the user is ready:** Move to Step 2.

## Step 2: Process captures `[SEQUENCE]`

One item at a time, oldest first. Never preview upcoming items. State the count upfront ("3 items in Captures. First: ...").

For each item:

1. **Present and interview** `[DISCUSS, PROMPT]` — Show the item and engage with its substance. Then ask follow-up questions that would sharpen it or surface missing context. Depth scales with the item — several rounds for open-ended ones, a question or two for straightforward ones. Continue until the picture is clear. Close by asking "anything else to add?"

2. **Recommend** `[PROMPT]` — Once the interview is done, recommend one of three dispositions:
   - **Promote** — ready to become a batch
   - **Park** — not now, keep for later
   - **Drop** — remove it
   Recommend one and say why. **Stop and wait.** The user decides.

3. **Execute the disposition:**
   - **Promote** `[DISCUSS, PROMPT]` — Draft the batch entry (bold title, why-line, entries under Build/Test subheadings). The why-line captures the reasoning from the discussion — why this work matters, what prompted it. Show it in full. Don't write to QUEUE.md until the user approves the wording. Claude places the batch using dependency ordering and reports where it went.
   - **Park** — Move to Parked.
   - **Drop** — Remove it. If the item has already been decided (check LOG/index.md), state the prior decision and commit rather than re-opening discussion.

4. Remove the item from Captures once routed.

After all items are processed, Captures should be empty (just the section header and `### Parked` subsection intact).

New items from conversation follow the same loop — check QUEUE.md for overlap first.

If Claude notices a gap or opportunity: "I notice [X] — want to hear a suggestion?" One at a time.

## Step 3: Batch structure

Batches group related work into one /next session:

    **Batch title**
    Why: [one line — what motivated this work]

    Build:
    - What to build

    Test:
    - How to verify

Bold title, why-line, entries grouped under Build and Test subheadings. Each entry names its own target — no separate file list. The why-line carries reasoning through the pipeline — /next copies it to _build.md, /done uses it as the foundation for the LOG **Why:** field.

**Test section:** Only add a Test section when there's a behaviour to verify that isn't self-evident from the build entries. Not every batch needs one — but /done does not generate tests, so anything that needs verification must be planned here.

When writing test entries, split by who runs them. Claude can verify anything through code: read files, run commands, inspect output, trace logic. Only tests requiring real human interaction — visual appearance, physical device behaviour, subjective judgment, or running a separate live session — need the user. Write each test entry so /next knows which kind it is.

**E2E tests get their own batch.** User-run E2E tests (tests requiring a live session in a separate project) don't go in build batches. They're a different mode of work — the user runs them outside this session and reports back. Give them their own batch so the build flow isn't blocked waiting on external verification.

**Sizing gates** (per batch, not per entry):
- *Specificity:* every entry names a concrete output. "Add validation to utils.py", not "improve error handling."
- *Verification burden:* if the user would need to test more than 5 things, split it.

**Ordering:** Dependencies first, then scaffolding, then features, then polish. Claude determines this ordering and reports where each batch landed and why.

## Step 4: Close out `[BRIEF, PROMPT]`

1. Summarize what changed this session.
2. "Run /done to record this and commit, or keep planning."

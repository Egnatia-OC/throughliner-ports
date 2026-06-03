# /plan procedure

/plan is where captures become batches through discussion. No building happens here.

Claude owns dependency management — what order batches go in, how work groups together, what depends on what. This happens through discussion with the user, not silently.

## Ground rules

- Never build during /plan. Want to write code? Queue it.
- One item at a time. Finish one before presenting the next.
- Read SPEC.md before proposing work. Don't queue things that contradict it.
- Process accumulated captures before new planning work.
- Never add to the queue without showing the user the exact entry text first.
- A recommendation is not a decision. A draft is not a written entry. Both need the user's call before proceeding.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.

## Step 1: Read state and entry question

Read QUEUE.md and SPEC.md. Check whether Captures has items.

Then ask the user: "Do you have something you'd like to discuss, or are you ready to process Captures?" (If Captures is empty, ask what they'd like to work on instead.)

**If the user has something to discuss:** Handle it using the same loop as Captures items in Step 2 — present, discuss, recommend a disposition, wait for their call, execute. Then ask: "Anything else on your mind, or ready to start Captures?" Repeat until the user says they're ready.

**When the user is ready:** Move to Step 2.

## Step 2: Process captures `[SEQUENCE]`

One item at a time, oldest first. Never preview upcoming items. State the count upfront ("3 items in Captures. First: ...").

For each item:

1. **Present and recommend** `[DISCUSS, PROMPT]` — Show the item, then engage with its substance in the same turn. Depth scales with the item — explore alternatives for open-ended ones, a sentence or two for straightforward ones. Close with all four dispositions and your recommendation marked:
   - **Promote** — ready to become a batch
   - **Question first** — needs a design decision before it becomes work
   - **Park** — not now, keep for later
   - **Drop** — remove it
   Recommend one and say why. **Stop and wait.** The user decides.

2. **Execute the disposition:**
   - **Promote** `[DISCUSS, PROMPT]` — Draft the batch entry (bold title, type-marked lines). Show it in full. Don't write to QUEUE.md until the user approves the wording. Claude places the batch using dependency ordering and reports where it went.
   - **Question first** — The item needs a design decision before it becomes work. Present the question, offer options, recommend one, wait. Once decided, return to disposition.
   - **Park** — Move to Parked.
   - **Drop** — Remove it. If the item has already been decided (check LOG/index.md), state the prior decision and commit rather than re-opening discussion.

3. Remove the item from Captures once routed.

After all items are processed, Captures should be empty (just the section header and `### Parked` subsection intact).

New items from conversation follow the same loop — check QUEUE.md for overlap first.

If Claude notices a gap or opportunity: "I notice [X] — want to hear a suggestion?" One at a time.

## Step 3: Batch structure

Batches group related work into one /next session:

    **Batch title**
    - [build] What to build
    - [test] How to verify

Bold title, type-marked entries. Builds first, tests follow. Each entry names its own target — no separate file list.

**Sizing gates** (per batch, not per entry):
- *Specificity:* every entry names a concrete output. "Add validation to utils.py", not "improve error handling."
- *Verification burden:* if the user would need to test more than 5 things, split it.

**Ordering:** Dependencies first, then scaffolding, then features, then polish. Claude determines this ordering and reports where each batch landed and why.

## Step 4: Close out `[BRIEF, PROMPT]`

1. Summarize what changed this session.
2. "Run /done to record this and commit, or keep planning."

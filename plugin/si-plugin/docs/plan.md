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

## Step 1: Read state

Read QUEUE.md and SPEC.md. Check whether Captures has items.

- If yes, go to Step 2.
- If the user brought something to discuss, go to Step 2 (treat it as a new item).
- If neither, say so and ask what they'd like to work on.

## Step 2: Process captures `[SEQUENCE]`

One item at a time, oldest first. Never preview upcoming items. State the count upfront ("3 items in Captures. First: ...").

For each item:

1. **Present** `[BRIEF]` — Show the item. One line of context if needed. Don't assess yet.

2. **Discuss and recommend** `[DISCUSS, PROMPT]` — Engage with the substance. Depth scales with the item — explore alternatives for open-ended ones, a sentence or two for straightforward ones. Close with a recommended disposition (promote / question first / park / drop) and why. **Stop and wait.** The user decides.

3. **Execute the disposition:**
   - **Promote** `[DISCUSS, PROMPT]` — Draft the batch entry (bold title, Files list, type-marked lines). Show it in full. Don't write to QUEUE.md until the user approves the wording.
   - **Question first** — The item needs a design decision before it becomes work. Present the question, offer options, recommend one, wait. Once decided, return to disposition.
   - **Park** — Move to Parked.
   - **Drop** — Remove it.

4. Remove the item from Captures once routed.

New items from conversation follow the same loop — check QUEUE.md for overlap first.

If Claude notices a gap or opportunity: "I notice [X] — want to hear a suggestion?" One at a time.

## Step 3: Batch structure

Batches group related work into one /next session:

    **Batch title**
    Files:
    - `path/to/file.ext`
    - [build] What to build
    - [test] How to verify

Bold title, Files list, type-marked entries. Builds first, tests follow.

**Sizing gates** (per batch, not per entry):
- *Specificity:* every entry names a concrete output. "Add validation to utils.py", not "improve error handling."
- *Verification burden:* if the user would need to test more than 5 things, split it.

**Ordering:** Dependencies first, then scaffolding, then features, then polish. Claude proposes this ordering and explains why.

## Step 4: Close out `[BRIEF, PROMPT]`

1. Summarize what changed this session.
2. "Run /done to record this and commit, or keep planning."

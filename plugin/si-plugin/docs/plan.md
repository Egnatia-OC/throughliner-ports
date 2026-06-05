# /plan procedure

/plan is where captures become batches through discussion. No building happens here.

Claude owns dependency management — ordering, grouping, dependencies — through discussion, not silently.

## Ground rules

- Never build during /plan. Want to write code? Queue it.
- One item at a time. Finish one before presenting the next.
- Read SPEC.md before proposing work. Don't queue contradictions.
- Process accumulated captures before new planning work.
- Never write batch entries to QUEUE.md without showing the user the exact text first.
- A recommendation is not a decision. A draft is not a written entry. Both need the user's call.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.

## Step 1: Read state and entry question

**Backfill LOG hashes first:** [BRIEF] Scan `LOG/log.md` and `LOG/index.md` for `[HASH]` placeholders. For each, find the hash of the commit that introduced the entry (e.g. `git log --diff-filter=A --pretty=%h -- LOG/log.md` walked top-down, or by blame) and replace `[HASH]` in place. No separate commit — the working-tree edit folds into whatever commit this session later makes. If nothing to backfill, no output.

Then read QUEUE.md and SPEC.md. Check whether Captures has items.

Ask: "Do you have something to discuss, or ready to process Captures?" (If Captures is empty, ask what they'd like to work on.)

**If the user has something:** Handle it using the Step 2 loop — present, interview, recommend, wait, execute. Then: "Anything else, or ready for Captures?" Repeat until ready.

**When ready:** Move to Step 2.

## Step 2: Process captures [SEQUENCE]

One item at a time, oldest first. Never preview upcoming items. State the count upfront ("3 items. First: ...").

For each item:

1. **Present and interview** [DISCUSS, PROMPT] — Show the item, engage with its substance. Ask follow-ups to sharpen it or surface missing context. Depth scales with the item. Continue until the picture is clear. Close: "anything else to add?"

2. **Recommend** [PROMPT] — Recommend one disposition and say why:
   - **Promote** — ready to become a batch
   - **Park** — not now, keep for later
   - **Drop** — remove it
   Stop and wait. The user decides.

3. **Execute the disposition:**
   - **Promote** [DISCUSS, PROMPT] — Draft the batch entry (bold title, prose rationale, Build/Test subheadings). The rationale carries the reasoning from the discussion as inline prose — see Why-pipeline in behaviour.md. Show in full. Don't write to QUEUE.md until approved. Claude places the batch using dependency ordering and reports where it went.
   - **Park** — Move to Parked.
   - **Drop** — Remove. If already decided (check LOG/index.md), state the prior decision and commit.

4. Remove the item from Captures once routed.

After all items: Captures should be empty (section header and `### Parked` intact).

New items from conversation follow the same loop — check QUEUE.md for overlap first.

If Claude notices a gap: "I notice [X] — want to hear a suggestion?" One at a time.

## Step 3: Batch structure

    **Batch title**
    [Prose rationale — one or more sentences. What motivated this work, what's broken or missing, what changes once it lands.]

    Build:
    - What to build

    Test:
    - How to verify

Bold title, prose rationale directly under it, entries under Build and Test subheadings. Each entry names its own target. The rationale is inline prose (no `Why:` label, no separate field) and carries the reasoning forward through the pipeline — /next copies it to _build.md, /done re-authors it into the LOG entry. See Why-pipeline in behaviour.md.

**Test section:** Only when there's a behaviour to verify that isn't self-evident from build entries. Not every batch needs one — but /done doesn't generate tests, so anything needing verification must be planned here.

Split test entries by who runs them. Claude verifies through code: read files, run commands, inspect output, trace logic. Only tests requiring real human interaction (visual, physical, subjective, separate live session) need the user. Write each so /next knows which kind.

**E2E tests get their own batch.** User-run E2E tests (separate project, live session) don't go in build batches — they'd block the build flow.

**Sizing gates** (per batch):
- *Specificity:* every entry names a concrete output. "Add validation to utils.py", not "improve error handling."
- *Verification burden:* more than 5 things to test → split.

**Ordering:** Dependencies first, then scaffolding, features, polish. Claude determines ordering and reports placement.

## Step 4: Close out [BRIEF, PROMPT]

1. Summarize what changed.
2. "Run /done to record this and commit, or keep planning. Run `/clear` first to keep context clean."

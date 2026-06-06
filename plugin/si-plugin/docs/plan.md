# /plan procedure

/plan is where captures become batches through discussion. No building happens here.

Claude owns dependency management — ordering, grouping, dependencies — through discussion, not silently.

## Ground rules

- Never build during /plan. Want to write code? Queue it.
- Batches are build work, test work, or audit work, in any combination. Nothing else.
- Never queue thinking work as a *build* batch. Reviews, reconciliations/drift checks, and design exploration are planning work — their output is decisions, not changed files. Run them inside /plan; they spawn batches as output. Audit work (systematic read of target docs against fixed criteria) is the one exception — it can become an audit batch whose output routes through Captures, preserving the no-direct-edits property that motivated the rule. Test: if the main work is figuring something out rather than executing on a decision or doing a systematic read, it's planning work.
- One item at a time. Finish one before presenting the next.
- Read SPEC.md before proposing work. Don't queue contradictions.
- Process accumulated captures before new planning work.
- Never write batch entries to QUEUE.md without showing the user the exact text first.
- A recommendation is not a decision. A draft is not a written entry. Both need the user's call.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.

## Step 1: Read state and entry question

**Backfill LOG hashes first:** [BRIEF] Scan `LOG/log.md` and `LOG/index.md` for `[HASH]` placeholders. For each, find the hash of the commit that introduced the entry (e.g. `git log --diff-filter=A --pretty=%h -- LOG/log.md` walked top-down, or by blame) and replace `[HASH]` in place. No separate commit — the working-tree edit folds into whatever commit this session later makes. If nothing to backfill, no output.

Then read QUEUE.md and SPEC.md. Check whether Captures has items.

**Unpark + staleness scans:** before the entry question, walk Parked and the active queue against plugin-behaviour.md Dependency ownership (Unpark watch + Staleness watch). For Parked: anything newly unblocked by work that's landed since it was parked? For Batches and Captures: anything stale enough that the surrounding code or rules have moved past it? Surface any findings as part of the read-state phase — name the item, name the trigger, narrate per Dependency ownership. The user decides whether to act now or hold; no silent edits.

Ask: "Do you have something to discuss, or ready to process Captures?" (If Captures is empty, ask what they'd like to work on.)

**If the user has something:** Handle it using the Step 2 loop — present, interview, recommend, wait, execute. Then: "Anything else, or ready for Captures?" Repeat until ready.

**When ready:** Move to Step 2.

## Step 2: Process captures [SEQUENCE]

One item at a time, oldest first. Never preview upcoming items. State the count upfront ("3 items. First: ...").

For each item:

1. **Present and interview** [DISCUSS, PROMPT] — Show the item, engage with its substance. Ask follow-ups to sharpen it or surface missing context. Depth scales with the item. Continue until the picture is clear. Close: "anything else to add?"

2. **Recommend** [PROMPT] — Recommend one of promote, park, or drop and say why:
   - **Promote** — ready to become a batch. The recommendation must describe what would actually get built, in terms the user can recognize as the work product (which files change, what subsection or rule, what gets added/removed/rewritten — not just the topic or intent). Forcing function: if sub-step 1's interview hasn't yielded enough to describe the outputs concretely, the recommendation isn't ready — return to interviewing. **Downstream-impact scan:** if the capture installs a *structural rule* (defines what something is, sets a constraint that frames how other captures get evaluated — as opposed to a localized fix), scan the remaining Captures for items that could revise or invalidate the rule. Trigger is rule shape, not edit size. If any are found, flag at recommend time, name the conflict, and offer three options — process the downstream capture first, hold this one, or proceed accepting the possible later revision.
   - **Park** — not now, keep for later
   - **Drop** — remove it
   Stop and wait. The user decides.

3. **Execute promote, park, or drop:**
   - **Promote** [DISCUSS, PROMPT] — Draft the batch entry (bold title, prose rationale, Build/Test subheadings). The rationale carries the reasoning from the discussion as inline prose — see Why-pipeline in plugin-behaviour.md. Show the draft in a fenced code block, per the approval-time outputs rule in plugin-behaviour.md. Don't write to QUEUE.md until approved. Claude places the batch using dependency ordering and reports where it went.
   - **Park** — Move to Parked.
   - **Drop** — Remove. If already decided (check LOG/index.md), state the prior decision and commit.

4. Remove the item from Captures once routed.

5. **Checkpoint** [PROMPT] — Offer three options every time, in uniform phrasing: (1) continue to the next capture, (2) close out now (go to Step 4), (3) share something else (loop back into Step 2 with the new item). Wait for the user's call. On the last capture, option 1 drops out naturally — the offer collapses to two options without needing different wording.

After all items: Captures should be empty (section header and `### Parked` intact).

New items from conversation follow the same loop — check QUEUE.md for overlap first.

If Claude notices a gap: "I notice [X] — want to hear a suggestion?" One at a time.

## Step 3: Batch structure

```markdown
**Batch title** **[batch-slug]**
Depends on: [other-slug], [other-slug]
Blocks: [other-slug]

[Prose rationale — one or more sentences. What motivated this work, what's broken or missing, what changes once it lands.]

Build:
- What to build

Test:
- How to verify

Audit:
- Target: which docs, files, or area to review
- Criteria: what to look for (repetition, drift, tag misuse, prose-where-tag-belongs, etc.)
```

Bold title with a stable kebab-case slug appended as a `**[slug]**` marker, then optional `Depends on:` / `Blocks:` header lines (omit either when empty — no `Depends on: none` placeholders), then the prose rationale, then entries under Build, Test, and/or Audit subheadings. See plugin-behaviour.md Dependency ownership for the slug and header rules. Each entry names its own target. The rationale is inline prose (no `Why:` label, no separate field) and carries the reasoning forward through the pipeline — /next copies it to _build.md, /done re-authors it into the LOG entry. See Why-pipeline in plugin-behaviour.md.

**Think through testing when drafting.** Before authoring the Test section (or deciding to omit it), work through what verification this batch needs. Split the question two ways: what can Claude verify itself (read files, run commands, trace logic, inspect output), and what needs the user (visual, physical, subjective, separate live session). Populate Test with what you find — or proceed without one when the change is self-verifying from the build entries. The decision to omit gets made consciously, not by inattention.

**Test section:** Only when there's a behaviour to verify that isn't self-evident from build entries. Not every batch needs one — but /done doesn't generate tests, so anything needing verification must be planned here. [SILENT] when omitting: don't narrate the absence of a Test section. The rationale already tells the user what kind of change it is.

Split test entries by who runs them, per the thinking above. Write each so /next knows which kind.

**E2E tests get their own batch.** User-run E2E tests (separate project, live session) don't go in build batches — they'd block the build flow.

**Readiness gate** (per batch): can you write the candidate index entry now — artifact touched + nature of the change, per plugin-behaviour.md Index entries? If yes, the batch is ready and the entry can be pre-generated for /next to carry into _build.md. If no, the batch isn't coherent enough yet — keep interviewing.

**Audit batch sizing gate:** for audit batches specifically, the readiness check is whether the target and criteria are specific enough that Claude can write the audit prompt without further dialogue. If the target is vague ("the procedure docs") or the criteria are open-ended ("anything off"), keep interviewing until both pin down.

**Ordering:** Claude places by dependency where applicable — dependencies first, then scaffolding, features, polish. Oldest-first is the fallback when no dependency applies (per plugin-behaviour.md Captures placement). Either way, Claude reports placement and the reasoning per Dependency ownership narration — including the explicit "appending here because no dependency applies" case.

## Step 4: Close out [BRIEF, PROMPT]

1. Summarize what changed.
2. "Run /done to record this and commit, or keep planning."

# /plan procedure

/plan is where captures become batches through discussion. No building happens here.

Claude owns dependency management — ordering, grouping, dependencies — through discussion, not silently.

## Ground rules

- Never build during /plan. Want to write code? Queue it.
- Batches are build, test, or audit work, in any combination. Nothing else.
- Never queue thinking work as a batch. Reviews, reconciliations/drift checks, and design exploration are planning work — their output is decisions, not changed files. Run them inside /plan; they spawn batches as output. Audit work is a separate category, not an exception: an audit is defined by its output contract — findings routed through Captures, no direct edits to the artifacts it reads. Audits produce findings, thinking work produces decisions; the two don't overlap. Test: output is decisions → planning work, run it in /plan; output is findings from a systematic read, routed to Captures → audit batch. The same test applies per seeded item, not just per batch: an audit's seeded check-items must be finding-shaped; decision-shaped checks (reconciliation, is-this-already-resolved) get resolved at planning time, not queued.
- One item at a time. Finish one before presenting the next.
- Read SPEC.md before proposing work. Don't queue contradictions.
- Process accumulated captures before new planning work.
- Never write batch entries to QUEUE.md without showing the user the exact text first.
- A recommendation is not a decision. A draft is not a written entry. Both need the user's call.
- The pipeline: idea → question (if unclear) → spec entry (if it changes the product) → batch entry. No shortcuts.

## Capture and parking discipline

The control rule for capture and parking, in one place. Pieces also appear in the steps and in plugin-behaviour.md; the canonical statement is here.

- **Two structural slots for items removed from active flow.** `Blocked by:` (trigger-based, auto-surfaces — slug plus optional behavioural prose tail) and `Parked:` (indefinite, conscious revisit only — short reason). Nothing leaves active flow without one. See plugin-behaviour.md Dependency ownership for slot semantics. Applies to batches in Batches Parked and captures in Captures Parked alike.
- **Processed/unprocessed split in Captures.** Captures is divided by `---`. Processed (above) have had dependency management applied at least once and carry slugs. Unprocessed (below) are raw appended in file order. Routing (promote/park/drop) is separate from dependency management — a capture can become processed in one /plan and routed in another. See Step 2 for the loop.
- **Routing gate before recommendation.** Step 2 sub-step 2 mechanically scans capture text for named items or behavioural triggers before the promote/park/drop recommendation. Any reference found defaults the recommendation to park-with-`Blocked by:`-populated. Not prose-judgment — presence triggers the default, even if Claude reads the reference as incidental.
- **Filing-time blockers go in the slot, not the prose.** When the user files a capture and the blocker is already known, write `Blocked by: [slug] + condition` inline on the capture. /plan's Step 2 dependency scan picks it up mechanically rather than re-reading the prose. Stated in plugin-behaviour.md Captures.

## Step 1: Read state and entry question

Read QUEUE.md and SPEC.md. Check whether Captures has items.

**Unpark + staleness scans:** before the entry question, walk Parked and the active queue against plugin-behaviour.md Dependency ownership (Unpark watch + Staleness watch). For Parked: read `Blocked by:` headers as the primary surface — slug portions fire mechanically (if the named slug has shipped, the item is a candidate; verify against LOG/index.md), behavioural prose tails still need judgment. Items marked `Parked:` (no trigger) don't auto-surface; skip unless something else flags them. For Batches and Captures: anything stale enough that surrounding code or rules have moved past it? The scans' output is candidates feeding Step 2, not findings to narrate here — collect them silently and carry them into Step 2, where they're processed ahead of Captures (see Unpark candidates first). No silent edits: every candidate goes through the Step 2 loop, where the user decides.

Ask: "Do you have something to discuss, or ready to process Captures?" (If Captures is empty, ask what they'd like to work on.) Keep the question clean — no scan candidates folded in; they surface only inside Step 2.

**If the user has something:** Handle it via the Step 2 loop — present, interview, recommend, wait, execute. Then: "Anything else, or ready for Captures?" Repeat until ready.

**When ready:** Move to Step 2.

## Step 2: Process captures [SEQUENCE]

**Captures structure: processed/unprocessed split.** Captures is divided by `---` into processed (above) and unprocessed (below). Processed = /plan has applied dependency management at least once (given a slug, set a `Blocked by:` header, or confirmed standalone via Step 2 sub-step 2). Processed captures carry slugs so they can be cross-referenced. Unprocessed = raw appended in file order — no slug, no dependency headers yet. The divider is staging between raw and routed (promote/park/drop), not a final home — captures sit above it until routed out of Captures entirely. Routing is separate from dependency management and can happen in any later /plan: a capture can become processed in one session and routed in another.

**Unpark candidates first.** Candidates carried in from Step 1's scans are processed before Captures — Parked items have been waiting longest. Each enters the loop below as if it were a capture, sourced from Parked instead of Captures, through the same sub-steps (present + interview, recommend, execute, remove, checkpoint). The recommend options are the same three, reread for items already in Parked: **promote** means move out of Parked into Batches as a full batch entry, **park** means keep parked, **drop** removes the Parked item entirely. Staleness candidates take the same path with the Staleness watch's choice — drop, rewrite, or keep (per plugin-behaviour.md Dependency ownership).

One item at a time — candidates from Step 1 first, then captures oldest first across both halves (unprocessed in file order, then continue into processed). Never preview upcoming items. State the count upfront, counting candidates and captures together ("5 items. First: ...").

For each item:

1. **Present and interview** [DISCUSS, PROMPT] — Show the item, engage with its substance. Ask follow-ups to sharpen it or surface missing context. Depth scales with the item. Continue until the picture is clear. Close: "anything else to add?"

2. **Dependency scan** [SILENT] — Before recommending, scan the capture text for named batches or captures (slugs in `[brackets]`, bold titles), behavioural triggers ("once X ships," "after Y has run," "depends on Z"), or references to work that hasn't landed yet. If any are found, the default recommendation in sub-step 3 becomes park-with-`Blocked by:`-populated rather than promote. If none, give the capture a kebab-case slug (if unprocessed) — it's now processed and stays above the divider whether or not it gets routed this session. Mechanical scan, not prose-judgment: presence of a reference triggers the default, even if Claude thinks it's incidental.

3. **Recommend** [PROMPT] — Recommend one of promote, park, or drop and say why:
   - **Promote** — ready to become a batch. The recommendation must describe what would actually get built, in terms the user can recognize as the work product (which files change, what subsection or rule, what gets added/removed/rewritten — not just the topic or intent). Forcing function: if sub-step 1's interview hasn't yielded enough to describe the outputs concretely, the recommendation isn't ready — return to interviewing. **Downstream-impact scan:** if the capture installs a *structural rule* (defines what something is, sets a constraint that frames how other captures get evaluated — as opposed to a localized fix), scan the remaining Captures for items that could revise or invalidate the rule. Trigger is rule shape, not edit size. If any are found, flag at recommend time, name the conflict, and offer three options — process the downstream capture first, hold this one, or proceed accepting the possible later revision.
   - **Park** — not now, keep for later. If sub-step 2 found a dependency, this is the default and `Blocked by:` is populated from the scan. Otherwise park with a short `Parked:` reason.
   - **Drop** — remove it
   Stop and wait. The user decides.

4. **Execute promote, park, or drop:**
   - **Promote** [DISCUSS, PROMPT] — Draft the batch entry (bold title, prose rationale, Build/Test subheadings). The rationale carries the discussion's reasoning as inline prose — see Why-pipeline in plugin-behaviour.md. Show the draft in a fenced code block, per the approval-time outputs rule in plugin-behaviour.md. Don't write to QUEUE.md until approved. Claude places the batch using dependency ordering and reports where it went.
   - **Park** — Move to Parked with the `Blocked by:` or `Parked:` header populated per sub-steps 2 and 3.
   - **Drop** — Remove. If already decided (check LOG/index.md), state the prior decision and commit.

5. Remove the item from Captures once routed (promote, park, or drop). If only dependency management was applied this turn — slug given or `Blocked by:` set without routing — the capture stays in Captures but moves above the divider as a processed item; don't remove it.

6. **Checkpoint** [PROMPT] — Offer three options every time, in uniform phrasing: (1) continue to the next capture, (2) close out now (go to Step 4), (3) share something else (loop back into Step 2 with the new item). Wait for the user's call. On the last capture, option 1 drops out naturally — the offer collapses to two without different wording.

After all items: Captures should hold only processed items above the divider (or be empty if everything was routed). Section header, divider, and `### Parked` intact.

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

Bold title with a stable kebab-case slug appended as a `**[slug]**` marker, then optional `Depends on:` / `Blocks:` header lines (omit either when empty — no `Depends on: none` placeholders), then the prose rationale, then entries under Build, Test, and/or Audit subheadings. See plugin-behaviour.md Dependency ownership for the slug and header rules. Each entry names its own target. The rationale is inline prose (no `Why:` label, no separate field) and carries the reasoning forward — /next copies it to _build.md, /done re-authors it into the LOG entry. See Why-pipeline in plugin-behaviour.md.

**Think through testing when drafting.** Before authoring the Test section (or deciding to omit it), work through what verification this batch needs. Split the question two ways: what Claude can verify itself (read files, run commands, trace logic, inspect output), and what needs the user (visual, physical, subjective, separate live session). Populate Test with what you find — or proceed without one when the change is self-verifying from the build entries. The decision to omit gets made consciously, not by inattention.

**Test section:** Only when there's a behaviour to verify that isn't self-evident from build entries. Not every batch needs one — but /done doesn't generate tests, so anything needing verification must be planned here. [SILENT] when omitting: don't narrate the absence. The rationale already tells the user what kind of change it is.

Split test entries by who runs them, per the thinking above. Write each so /next knows which kind.

**E2E tests get their own batch.** User-run E2E tests (separate project, live session) don't go in build batches — they'd block the build flow.

**Readiness gate** (per batch): can you write the candidate index entry now — artifact touched + nature of the change, per plugin-behaviour.md Index entries? If yes, the batch is ready and the entry can be pre-generated for /next to carry into _build.md. If no, the batch isn't coherent enough yet — keep interviewing.

**Audit batch sizing gate:** for audit batches, the readiness check is whether target and criteria are specific enough that Claude can write the audit prompt without further dialogue. If the target is vague ("the docs", "the UI flows") or the criteria open-ended ("anything off"), keep interviewing until both pin down.

**Ordering:** Claude places by dependency where applicable — dependencies first, then scaffolding, features, polish. Oldest-first is the fallback when no dependency applies (per plugin-behaviour.md Captures placement). Either way, Claude reports placement and reasoning per Dependency ownership narration — including the explicit "appending here because no dependency applies" case.

## Step 4: Close out [BRIEF, PROMPT]

"Run /done to record this and commit, or keep planning." No chat summary — the LOG entry /done writes is the single session summary.

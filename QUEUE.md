# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### The close makes its forward recommendation and files it about half the time [advisory-step-does-not-fire]
**Raised by you 2026-08-21**, from noticing it across the last couple of days: forward advisories "seem to have stopped being a thing" and you have had to ask for them, where Claude used to file them unprompted. The measurement and the diagnosis below are Claude's.

**What has actually stopped is narrower than the report, and the difference is the whole finding: the recommendations are still being made, and they have stopped being written down.** Yesterday's close made a concrete one — the text you carried by hand into the next session, that planning rather than a build is where it should start, naming the overlap between [setup-migration-gate-is-epoch-3-shaped] and [convert-cleared-items-to-build-blocks]. That is exactly what the advisory exists to carry. Nothing reached the queue, so it survived only because you pasted it.

**Measured from git rather than estimated, across the last five closes: three filed nothing.** Each close clears the previous advisory and only sometimes adds a new one — `d9468f3` cleared and filed none, `b485ee3` filed one, `cb50e2b` cleared and filed none, `7e3c1c8` filed one, `dc52025` cleared and filed none.

**The step is intact, which is what rules out the obvious explanation.** Nothing was repealed or reworded: `done.md` still carries "File the forward-recommendation advisory" in full, with the reserved `[forward-advisory]` slug, the write-conditions-not-counts rule and the flavour deltas. So this is not a change that removed something — it is a correctly worded obligation with a stated site that does not fire.

**The likeliest cause is position, and it is measurable.** The step sits at line 880 of a 925-line file — the tail of the largest document in the method, which a close reaches only after reading 7,443 words of it, having already written the record and with the commit in sight. That is the toll [done-md-carries-other-flavours-material] measures.

**This is the sixth instance in this corpus of a correctly worded rule with a stated site failing to fire**, after the provenance rule, the file-the-blocker rule, the INBOX-opening step, the subagent-cost rule and the gate's own halt instruction. The corpus's own conclusion about that class is already recorded: "state the rule again, or state it harder" is not a candidate direction.

**What changes — a required artifact, which is the one shape with teeth here.** `done.md`'s advisory step gains a disposition line the close writes into its session record:

```
Advisory: filed — <slug>
Advisory: not needed — the recommendation was generic
```

**It is an amendment rather than a new mechanism, and the parent is explicit.** The `Rule gate:` obligation was itself authored as "the FAQ-sync rule's shape extended to a second subject, not a new obligation". This is the third subject on that same shape, for the same stated reason: a required artifact converts a silent omission into a visible one. "Not needed because the recommendation was generic" is a claim a later reader can disagree with, and a missing line is a gap anyone can see.

**A mechanical check was considered and refused.** Nothing can detect whether an advisory was *owed*, because the trigger is whether this close made a concrete recommendation, and that lives in the conversation. A check firing on every advisory-less close would fire wrongly every time the recommendation was legitimately generic — the cry-wolf shape this project has repealed measures for twice.

**The step also moves out of the tail in the same edit.** Not as the fix — position is a guess and a step skipped at line 880 can be skipped at line 400 — but because there is no reason to leave it there while the file is open.

**The cost, stated rather than discovered: this one ships.** FAQ-sync and the rule gate are both host-only, so consumers write neither line. This is the first close-line obligation a consumer pays, one line per close in every project. It is admitted anyway because the feature it guards is one consumers have and are silently losing.

**Placed first in the cleared region, which is a non-default placement made deliberately.** [rename-docs-b-folder] sits second and carries `Runs alone`, so /next stops before it and the next run builds exactly one item. This is a shipped feature failing three closes in five; [split-action-defeats-the-bands-in-aggregate], which held first place, is a cost saving that loses nothing by waiting a run.

**Files:** `plugin/throughliner/docs-b/done.md` only — the advisory step and the session-record entry template.

**No SPEC sentence is owed, checked rather than assumed.** SPEC says /done files the note at the top of Unprocessed, which stays true, and a line in a session record is how a mechanism is implemented, which the SPEC admission rule keeps out. **No FAQ entry**, on the FAQ trigger's own test: a consumer sees one more line in their session record and does nothing different. **No epoch bump** — no existing project's documents become structurally wrong.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/done.md`, the "File the forward-recommendation
  advisory" step — add a required disposition line written into this close's
  session record, in the two forms `Advisory: filed — <slug>` and
  `Advisory: not needed — <why>`. Word the label plain, not bolded, matching
  the `Rule gate:` and `FAQ:` lines it sits beside. State in the step that a
  close cannot complete until the line is written.
  Same file — the session-record entry template gains the field alongside the
  existing `FAQ:` line, so the close writes it where it already writes those.
  Same file — move the advisory step out of the document's tail to sit with the
  other close obligations that produce a recorded line.
Acceptance: `done.md`'s advisory step names the required line in both forms.
  The entry template carries the field. Grep `Advisory:` in `done.md` returns
  the step and the template and nothing else. The step no longer sits in the
  final fifty lines of the file.
Refused: a mechanical check — nothing can detect whether an advisory was owed,
  since the trigger lives in the conversation, so it would fire wrongly on every
  legitimately generic close.
Refused: moving the step earlier as the whole fix — position is a guess, and a
  step skipped at line 880 can be skipped at line 400.
Refused: folding into [done-md-carries-other-flavours-material] — that item
  moves flavour-specific material out and must delete nothing; this step is
  shared across flavours, so it would not move under that lever.
--- End build block ---

Rule gate: run — admitted as a third subject on the existing close-line obligation shape, subordinate to a mechanism already shipped twice, and sited in a fetched procedure doc so no always-loaded slot is spent. **Nothing is evicted, stated plainly rather than dressed up as a merge.** Failure evidence is three misses in five closes measured from git, plus one instance observed end to end where the recommendation was made in chat and reached the next session only because you carried it by hand. **A hook was considered and refused**, on the record in the block above.

Relates to [dispositions-listing-run-not-surfaced] and [inbound-replies-not-drafted], the two other live instances of an obligation with a site that does not fire, and to [done-md-carries-other-flavours-material], which measures the toll this step sits at the end of.

#### The digest calls an item shipped when a planning session merely processed it [log-entry-kind-not-distinguished]
Filed 2026-08-21 by Claude, from an instance visible on screen while verifying an unrelated placement: the digest reported [advisory-step-does-not-fire] as citing [setup-migration-gate-is-epoch-3-shaped] and [convert-cleared-items-to-build-blocks] as **shipped**, while both sat cleared and unbuilt in the queue.

**The mechanism, read in the code rather than taken from the observation.** `queue_digest.py`'s `shipped_slugs()` does one directory listing and matches `<date>-<slug>.md`. Nothing opens the file. Its own docstring calls the result *"slugs whose work shipped"*, and that is false for every entry a planning close wrote — because a plan entry splits per item **processed**, which is settled and correct, so a discussed-and-kept item has a record named after it exactly like a built one.

**Why it is worse than a mislabelled line.** The below-the-line revisit decides what may lift by reading shipped-ness off LOG, and its own rule is right — *"blocker BUILT and VERIFIED per LOG"*. What is wrong is the fact fed to it. An item held against a blocker that was only processed reads as ready to lift, and lifting is a clearing move, so unbuilt work reaches the region /next builds from. **That is the failure this queue has recorded four times, arriving through a door nobody was watching.** The rule needs no change; the fact does.

**The two kinds are already mechanically distinguishable, which is what makes this fixable without judgment.** Measured across 747 entries: 541 carry `**Files touched:**`, which a build close writes; 132 carry `**Work processed:**`, which a planning close writes. An entry with the second and not the first records an item being processed. **`Tick:` would be the stronger signal**, since it carries built-versus-confirmed and that is what the revisit's rule actually asks for — but it appears on 23 entries only, being recent, so it cannot classify the history and is not used.

**What changes.** `shipped_slugs()` stops trusting the filename and classifies by reading the entry. The digest then prints `Cites shipped:` and `Cites processed:` as separate facts rather than collapsing them, and a blocker's resolution says which kind of record it found.

**Suppressing the false flag was refused in favour of reporting both.** An item leaning on a sibling that was merely agreed has a weaker premise than one leaning on shipped work, and that is worth seeing rather than hiding — the digest's standing posture is to state a fact and never a verdict.

**Read lazily, because the whole folder is 4.5MB.** Only the entries for slugs actually cited or named as blockers are opened — a few dozen small files per run rather than the directory.

**What it cannot do, and the digest says so where it reports.** 74 of the 747 entries carry neither marker: chat-level records and older formats. Those are reported as a record found whose kind is unknown, never guessed at. Partial coverage stated plainly is this project's standing choice over a check that over-claims.

**The ripple was traced by grep at processing rather than written from the discussion**, per the keep-step's repeal limb. The repealed claim reaches two live sites outside the code: `plan.md` line 225, *"A cited slug that has a LOG entry means that work shipped"*, and `SPEC.md` line 43, which asserted that work is *"recognised by its having a session record"*. **`SPEC.md` was rewritten in this planning session rather than listed here**, ahead of the build, per the rule that a build never writes product truth. The revisit's own table in `plan.md` is excluded by name: its built-and-verified test is correct as written and must not be touched.

**Files:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs-b/plan.md` (the cited-slug sentence only), `resources/testing/test_queue_digest.py`. **No FAQ entry** — a consumer sees a different label on a line and does nothing different. **No epoch bump** — no project document changes shape. Shipped, not host-only: every consumer's digest and every consumer's revisit run this.

--- Build block ---
Changes:
  `plugin/throughliner/scripts/queue_digest.py`, `shipped_slugs()` — stop
  returning a set built from the directory listing alone. Return a mapping of
  slug to kind: `built` where the entry contains `Files touched:`, `processed`
  where it contains `Work processed:` and not the first, `unknown` where it
  contains neither. Open only the entries for slugs that are cited or named as
  blockers, not the whole folder. Correct the docstring, which currently claims
  every match is work that shipped.
  Same file, the per-item line — print `Cites shipped:` and `Cites processed:`
  as separate lists, and append `(record kind unknown)` for the third case.
  Same file, blocker resolution — where a blocker resolves to a record, say
  which kind it is, so the revisit reads built-ness rather than existence.
  `plugin/throughliner/docs-b/plan.md` line 225 — replace "A cited slug that has
  a LOG entry means that work shipped" with the distinction: a record exists,
  and its kind says whether the work was built or only agreed. Leave the
  below-the-line revisit's built-and-verified table exactly as it stands.
  `resources/testing/test_queue_digest.py` — one case per kind, plus one
  asserting a processed-only blocker is NOT reported as shipped.
Acceptance: against this live queue, [setup-migration-gate-is-epoch-3-shaped]
  and [convert-cleared-items-to-build-blocks] appear under `Cites processed:`
  and not under `Cites shipped:`. A built slug still appears under
  `Cites shipped:`. The new suite passes. Digest runtime stays under a second.
Refused: suppressing the processed case instead of reporting it — a weaker
  premise is a fact worth seeing, and the digest states facts rather than
  hiding them.
Refused: classifying on `Tick:` — the stronger signal, but present on 23 of 747
  entries, so it cannot read the history.
Refused: reading every entry on every run — 4.5MB for a handful of citations.
Refused: changing the below-the-line revisit's rule — it is correct as written;
  what was wrong is the fact supplied to it.
--- End build block ---

Rule gate: run — no rule is authored or amended. **The disposition is a correction to a mechanism plus one repealed sentence**, evicted at both live sites where it is stated: `plan.md`'s cited-slug claim and, written in this planning session, SPEC's. Failure evidence is one instance observed directly on screen, plus the structural argument that the same signal governs what lifts out of the held region — a consequence checked in `plan.md`'s revisit rather than assumed. **A hook was considered and refused**: this is a script's own logic, not a thing a hook could watch.

Relates to [plan-entry-split-wording-disagrees], which established that a plan entry splits per item processed and that filenames are what the mechanisms read — this is the cost of that settlement, which nothing weighed at the time. Also to [digest-diamond-read-as-a-loop] and [superseded-flag-has-no-section-granularity], both defects in the same script, and worth settling in one run.

#### Compress the log index's longest lines, cutting the retrieve's fixed toll by about 40% [split-action-defeats-the-bands-in-aggregate]
**Subject replaced at processing 2026-08-17; the slug is unchanged because slugs are immutable.** Raised by you at the close that first applied the plan-entry split: *"That was almost 17k tokens. I am concerned that the bands won't reach this new record keeping model."*

**The aggregate half was measured and refuted, and that finding is in this session's record rather than here.** Per-entry cost *fell* after the split — 518 words per entry before it, then 329 and 316, against July's own 341. The 17k came from recording 26 items, so a per-close band would measure run size, which is your decision and not a length defect.

**What survives is the index toll, larger than the item claimed.** `LOG/index.md` is 817 lines and 48,165 words, read in full on every retrieve. 351 lines sit at or above 61 words and carry 32,408 of those words. 265 of the 351 are August's. **That 61 is a measured cut-off marking this item's work list, not a limit anyone must write to** — it selects which lines to look at, and each one is then judged against the index line's own contract rather than against a number.

**What changes.** Each of the 351 is rewritten to the artifact touched, the nature of the change and the entry filename, working from the line's own text only: a long line is long because it restates the entry it points at, so no entry needs re-reading. Commit hashes are preserved — the digest and the hash backfill read them.

**The band is no longer the reason, revised 2026-08-19 by [retire-word-band-caps-keep-measurement], and this item survives that intact.** The 20–40 figure goes with every other cap. What justified this work was never the figure: it is that `LOG/index.md` is read **in full, by Claude, on every retrieve**, so its length is a fixed toll rather than something a reader skims past — 48,165 words to point at entries, with one 337-word line pointing at a 1,710-word entry. The test is the index line's own stated contract, that it carries enough to decide open-or-skip and does not restate the entry. That is a judgment, applied line by line, and it was always the real test; the number was standing in front of it.

**This edits a pointer, not the record.** Every entry file stays byte-for-byte and no claim changes, which is what separates it from editing a session record to agree with a later decision.

**The intuitive fix was refused: monthly index files.** Four mechanical readers would each have to glob a directory, and the digest must resolve a slug from any month, so it would read all of them regardless — a format change, an epoch bump and a migration path for a smaller saving.

**Acceptance test:** line count, total words and median line before and after; expect roughly 28,000 words.

**Files:** `LOG/index.md` only. The ripple was traced by grep — `session_start.py`, `queue_digest.py`, `rule_signals.py` and `measure_written_shape_length.py` all read the file, none reads line length.

Rule gate: not needed — no rule authored and no always-loaded text touched. This rewrites a backlog of index lines against the index line's own stated contract: carry enough to decide open-or-skip, and do not restate the entry. **Reworded 2026-08-19** — it previously invoked the index-line band, which [retire-word-band-caps-keep-measurement] retires.

**The measurement this item asked for was run 2026-08-18, and it moves the subject: the problem is the queue's TOTAL length, of which item length is one term.** Across one full planning session the file went **21,512 words to 24,771 — up 15% — with the item count unchanged at 58**, and words per item rising 370 to 427. Twelve items were processed, four deleted and three folded away, and it still grew, because **processing an item is what lengthens it**: every keep adds a settlement, a Files line and a gate disposition. Only building an item out or deleting it shrinks the file. **This is the user's framing and it supersedes the per-artifact one this item was filed under.**

**So a wording pass is not the lever, which is measured rather than argued.** Two tersify passes over this queue yielded 8% and 3%, and their own write-up concludes the file is not verbose — its length is accumulated decision history. A tightening pass over seventeen freshly authored entries the same day cut 9%, 8,343 words to 7,585, leaving fifteen still over ceiling. Both passes removed meta-commentary and barely moved the totals.

**And the ceiling those passes were measured against is derived from a shape that no longer exists.** 45 of 54 entries breach it, the worst at 1,347, 1,102 and 805 words — corpus-wide rather than one session's authoring, so **an earlier claim on this item that the over-length was newly written text is withdrawn as false.** The band is July's median; dispositions moved onto the item on 2026-08-13, and the ripple-trace and SPEC-question limbs on 2026-08-17. A July item carried none of them. Re-derived figures without multipliers are in [word-band-script-does-not-ship]'s discussion.

**One narrower finding survives, though what it now feeds has changed.** Splitting an entry in two worked where it genuinely held two pieces of work and failed where it held one clause plus a long narrative — there the remedy was relocating the narrative to the record and citing it, 558 words to 407 and 571 to 442. **This no longer amends a breach action, because there is no breach to act on**: relocation-not-division is instead the measured precedent behind the build block's seam in [split-the-cleared-region-for-concurrent-sessions], which is where it does its work now. Both figures are also the only evidence anyone has that relocation moves the totals at all, and neither reached what was then the ceiling.

**The accretion mechanism is now filed separately** as [folding-in-has-no-eviction-step] — folding content into an item requires naming nothing that comes out, and appends rather than merges.

Relates to [bands-fire-on-the-median-artifact], [plan-entry-split-action-underspecified] and [index-line-length-is-a-toll-on-every-retrieve].

--- Build block ---
Changes:
  `LOG/index.md` only — rewrite each of the 351 index lines at or above 61
  words to the artifact touched, the nature of the change and the entry
  filename. Work from each line's own text; a long line is long because it
  restates the entry it points at, so no entry file is re-read. Judge each
  line against the index line's own contract — carries enough to decide
  open-or-skip, does not restate the entry — not against a word figure. The 61
  is a cut-off selecting the work list, not a limit to write to.
  Preserve every commit hash: the digest and the hash backfill read them.
  Touch no entry file — every one stays byte-for-byte.
Acceptance: line count, total words and median line recorded before and after;
  expect roughly 28,000 words against 48,165. Every commit hash present before
  is present after. `git status` shows `LOG/index.md` and no entry file.
Refused: monthly index files — four mechanical readers would each have to glob
  a directory and the digest must resolve a slug from any month, so it reads
  all of them regardless; a format change, an epoch bump and a migration path
  for a smaller saving.
--- End build block ---

#### Rename `docs-b/` to `docs/`, overturning the refusal recorded the day before [rename-docs-b-folder]
Filed 2026-08-16 by Claude, on the user's decision, after she challenged the refusal during the planning session that had just cited it.

**Her words, which are the reason this exists:** *"i don't know why it's still called docs b even though i have been asking for that to be changed for weeks. there is no docs a anymore so why would it be called docs b."* She is right on the model — docset A was retired 2026-08-09, nothing picks between docsets, and the letter names a sibling that does not exist.

**The refusal being overturned, and why it does not hold.** [docs-b-name-outlives-the-two-docset-model] shipped 2026-08-16 and refused the folder rename outright, on a grep: 639 occurrences, 215 live, **424 in `LOG/` and one archived message.** The argument was that renaming moves the "B" out of a live path `CLAUDE.md` can explain and into 424 historical references pointing at a folder that no longer exists — "drift by fixing drift."

**That argument treats a session record as though it were supposed to describe the present.** It is not. A LOG entry written in August naming `docs-b/` accurately records what the folder was called in August, which is what a record is for. Nobody proposed rewriting those 424, so the choice was never between renaming and falsifying the record. The Codex-port precedent the refusal cited says the same back: that decision was about **not rewriting** history, an argument for leaving `LOG/` alone rather than against renaming a live folder going forward.

**So the real cost is the 215 live references**, across 22 files: all five skill entry points, `session_start.py`, four of the docs themselves, four test suites, `CLAUDE.md`, `SPEC.md` and the migration recipe. This project has already carried out a larger rename in a single build — "Sovereign Implementer" to "Throughliner" moved the plugin slug, the package folder, both project marker files and the positioning together.

**Who decided what, recorded because the first decision's authorship is the point.** The rename was refused by Claude, at a close, with the user's question as the trigger and no moment where the choice was put to her — the same shape as [rule-admission-has-no-independent-approver], one layer out. This reversal is her decision; the reasoning against the old argument is Claude's, given at her challenge.

**`Runs alone`, and this is the marker's textbook case.** The work moves file paths underneath anything in flight, so a run holding paths in its working file and scope-lock list would find them stale mid-build.

**Trace the ripple by grep before building, per the hook-enforced-format rule** — `docs-b` as a literal across the repository, not a file list written from this item. The counts above are from 2026-08-16 and will have moved.

**Leave `LOG/` and `INBOX/archive/` untouched.** They are the record. `resources/plugin-behaviour-retired.md` is a retired archive and is also left alone.

**`QUEUE.md` IS a live reference and must be updated, which this item's first pass missed.** Open work items carry the old path in their own Files lines — [law-prose-restyle] and [files-line-names-excluded-files] both do at the time of filing — and a queue item is an instruction to a future build, not a record of the past. Left alone they would send a run at a folder that no longer exists. The `LOG/`-is-a-record argument does not extend to the queue: the queue describes what is still to be done.

**Files:** `plugin/throughliner/docs-b/` renamed to `plugin/throughliner/docs/`, with every live reference updated — the five skill entry points, `plugin/throughliner/hooks/session_start.py`, the docs that cross-reference each other, the four suites under `resources/testing/`, `CLAUDE.md`, `SPEC.md` and `plugin/throughliner/docs/migrate-checklist.md`. `CLAUDE.md`'s refusal paragraph is deleted and replaced with a dated line recording the rename and noting that earlier session records name the old path. `QUEUE.md` — every open item's Files line carrying the old path, rewritten to the new one. Exclusions and untouched paths are named in the paragraphs above rather than on this line.

Runs alone

Rule gate: run — no rule authored and none amended. **The disposition is an eviction:** `CLAUDE.md`'s paragraph refusing the rename is deleted outright, along with the reasoning that supported it, and replaced by a dated statement of fact. Failure evidence is the refusal itself failing on its first contact with the user it was written for — she read the explanation and rejected it the next day.

--- Build block ---
Changes:
  Grep `docs-b` as a literal across the repository FIRST and build the file
  list from that — the 2026-08-16 counts (639 total, 215 live, 22 files) are
  stale and are not the file list.
  Rename `plugin/throughliner/docs-b/` to `plugin/throughliner/docs/`.
  Update every live reference: the five skill entry points,
  `plugin/throughliner/hooks/session_start.py`, the docs that cross-reference
  each other, the four suites under `resources/testing/`, `CLAUDE.md`,
  `SPEC.md`, and `plugin/throughliner/docs/migrate-checklist.md`.
  `CLAUDE.md` — delete the paragraph refusing the rename and the reasoning
  supporting it; replace with a dated line recording the rename and noting
  that earlier session records name the old path.
  `QUEUE.md` — rewrite the old path in every open item's Files line.
  Leave untouched: `LOG/`, `INBOX/archive/`,
  `resources/plugin-behaviour-retired.md`. They are the record.
Acceptance: a repo-wide grep for `docs-b` returns hits only in `LOG/`,
  `INBOX/archive/` and `resources/plugin-behaviour-retired.md`. The suites
  under `resources/testing/` pass. `CLAUDE.md` carries the dated rename line
  and no refusal paragraph.
Refused: leaving the folder named `docs-b` on the drift-by-fixing-drift
  argument — it treats a session record as though it described the present;
  nobody proposed rewriting the 424 historical references, so the choice was
  never between renaming and falsifying the record.
Refused: extending the leave-it-alone argument to `QUEUE.md` — the queue
  instructs future builds rather than recording the past, so a stale path
  there sends a run at a folder that does not exist.
--- End build block ---

#### Claude keeps writing two-column fenced blocks that wrap into nonsense on the user's display [two-column-fences-wrap-unreadably]
Filed 2026-08-15 by Claude at the close's re-scan, from an instance it caused in this session.

**What happened.** The rewritten ladder was presented as a fenced block with a label on the left and its explanation in a right-hand column. On the user's display the right column wrapped underneath the left, so the two ran together and half the rungs appeared to have no title. **Her words: "there's no title on half of them. what do they mean."** The content was fine; the layout destroyed it, and a second message in plain lines fixed it immediately.

**Why this is a capture rather than a one-off slip.** The wrapping behaviour was already known here when the block was written anyway. **The item that recorded it is gone, checked at processing 2026-08-19 rather than assumed:** [fences-wrap-so-prose-rule-reason-is-false] was filed 2026-08-07, grew to roughly 1,500 words, and left the queue — it survives only as a line in `resources/research/written-shape-length-growth.md`. Its subject was a prose rule whose stated *reason* was false, which is an argument about a justification rather than about what Claude emits, so there was nothing to fold into. This item's own instruction to check that first is what caught it. The shipped docs are also full of this format: `skill-nonspecific-rules.md`, `plan.md` and `done.md` all use two-column fenced blocks heavily, and Claude reads them at every session start, which is the likeliest reason it keeps reproducing the shape in chat.

**The distinction that matters, and what a fix has to get right.** A two-column block inside a procedure doc is read by Claude, in a wide view, and works. The same shape emitted *to the user* is read on whatever display they have. So the rule is about output, not about the docs — a fix that reformatted the procedure docs would solve the wrong half.

**Settled at processing 2026-08-19, and the shipped rule already answers this one sentence short of the point.** The always-loaded render rule states what a fence is *for*: a paste target, or content whose exact characters **are** the substance — code, shell commands. A labelled two-column layout is neither; it is explanation wearing a fence. So the block that broke on your display was already outside the rule. What the rule never says is that using a fence for anything else is wrong, and the procedure docs model the wrong shape at scale, which is why it recurs.

**What changes.** One clause on `skill-nonspecific-rules.md`'s "How inline text is formed" block, beside the two entries already there: structured explanation shown to the user goes **one item per line, never in aligned columns**.

**Reformatting the procedure docs is refused, on this item's own reasoning.** A two-column block inside a procedure doc is read by Claude in a wide view and works. The rule governs output; rewriting the docs would fix the half that is not broken.

**Placed before the restyle passes deliberately**, so [law-prose-restyle-heavy-docs]'s subordination lens meets this clause as part of the file rather than after it, and does not have to handle the same text twice.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — the View-in-doc rendering section's inline-forming block. **No SPEC sentence is owed**, asked at the keep-step rather than left implicit: SPEC describes pointer-versus-inline rendering and says nothing about what a fence is used for, so nothing there goes wrong or incomplete. **No FAQ entry** — this changes what the user sees, not anything they do.

Rule gate: run — admitted as a subordinate clause on the existing render rule's inline-forming block, so no freestanding rule and no always-loaded slot spent. **Nothing is evicted, stated plainly rather than dressed up as a merge.** Failure evidence is thin by count — one clear instance, your own display — and carries on cost rather than weight: the failure is visible to the user, wastes a whole message, and the fix is a sentence. **A hook was considered and refused: nothing mechanical reads Claude's chat output.**

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, the View-in-doc
  rendering section's "How inline text is formed" block — add one clause
  beside the two entries already there: structured explanation shown to the
  user goes one item per line, never in aligned columns.
  Write it as a subordinate unit of that block, matching the existing
  entries' grammar. Nothing is evicted.
Acceptance: the inline-forming block carries the new clause alongside the two
  existing entries and reads as a continuation of them, not as a freestanding
  rule. No procedure doc's own two-column blocks are reformatted.
Refused: reformatting the procedure docs' own two-column blocks — those are
  read by Claude in a wide view and work; the rule governs output to the
  user, so rewriting the docs would fix the half that is not broken.
Refused: a hook — nothing mechanical reads Claude's chat output.
--- End build block ---

#### Explain the slug once in the queue header, and say what an item is for every time one is shown to the user [slug-never-explained-to-the-user]
Captured by you 2026-08-14. Your point, rendered in Claude's words rather than quoted: you have never actually known what the bracketed part of the title is for — it just randomly emerged one day and you didn't have time to deal with it.
**The gap.** The slug is load-bearing structure: it is what `Blocked by:` resolves against, what the queue lint checks, what a LOG entry names to say which item it built, and what Claude uses to refer to an item exactly in chat. None of that is stated anywhere the user reads. It appeared in their own documents and they worked around it for weeks.
**Why this is not solved by the slug being harmless to ignore.** It is harmless to ignore only once you know you may. Until then it is unexplained structure in a document the user is asked to read and approve, and the method's own standard is that unreadable is unapprovable.
**Widened at processing 2026-08-19 to carry a second half you raised in the same session, and this entry is rewritten rather than appended to.** What came out is the original three-way choice between header, FAQ or both, now settled as both. Your point: the way captures are presented at processing must not assume the reader already knows their content, and at minimum **a referent should be given not by name but also by its purpose.** A second item was refused in favour of the merge — two entries on one notation would answer the same question twice.

**Two halves, at opposite ends of the same subject.** The notation is explained **once**, in the queue's own header, where anyone opening the file meets it: what the bracketed name is for, and that the user never has to write one. Then each **use** stops being opaque: a slug shown to the user carries what that item is for on its first appearance in a message.

**Scope is output, never documents**, which is the same split [two-column-fences-wrap-unreadably] settled the same day. Inside queue prose slugs stay bare — the always-loaded rule deliberately requires citing items by slug there, that text is read by Claude, and glossing every citation would inflate the entries this queue already struggles with.

**First use per message, not per chat.** Per chat makes a message readable only to someone holding the scrollback in their head, which is the assumption being objected to. The cost is a clause each time, stated rather than presented as free.

**The parent is the vocabulary rule**, which already asks whether a term is used in passing or explained and already lists a dozen internal terms to translate or omit. **A slug cannot simply join that list**: omitting it loses the one handle the user has on an item. So it is a third arm on an existing table.

**Evidence, unusually strong for this corpus.** Two recorded instances in the user's own words — *"I don't know what 'checkpoints' is"* and *"I don't know what 'fixing on the spot' means"* — this entry's own account of working around the brackets for weeks, and the planning session that settled it, whose every checkpoint named an item by bare slug while several messages cited three or four more.

**One cost stated rather than discovered.** The header clause reaches new projects only: an existing project's queue header is the user's own text, and the method's migration is barred from rewriting user prose. For them the FAQ entry is the whole answer.

**Files:** `plugin/throughliner/docs-b/setup.md` (the queue header it authors), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the vocabulary rule's third arm), and `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines. **No epoch bump** — no existing file becomes structurally wrong.

**No SPEC sentence is owed:** SPEC describes the queue's structure without describing the slug notation, so no sentence there goes wrong or incomplete. Shipped, not host-only — every consumer meets the same unexplained brackets.

Rule gate: run — admitted as a third arm on the always-loaded vocabulary rule's existing in-passing/explained table, subordinate rather than freestanding. **Nothing is evicted, stated plainly rather than dressed up as a merge of rules.** Failure evidence is four instances, two of them the user's verbatim words. **A hook was considered and refused: nothing mechanical reads Claude's chat output** — the same finding reached independently by [two-column-fences-wrap-unreadably] hours earlier, which is what makes it a property of the surface rather than of either item.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/setup.md`, the queue header it authors — add a
  one-time explanation of the bracketed slug: what it is for, and that the
  user never has to write one.
  `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, the vocabulary
  rule's in-passing/explained table — add a third arm: a slug shown to the
  user carries what that item is for on its first appearance in a message.
  First use per message, not per chat. Scope is output only; inside queue
  prose slugs stay bare.
  `plugin/throughliner/templates/faq-template.md` plus its
  `faq-index-template.md` line — an entry answering what the bracketed name
  is; then re-copy both into `FAQ/faq.md` and `FAQ/index.md`.
Acceptance: setup.md's authored header explains the notation. The vocabulary
  rule's table carries three arms. The FAQ entry and its index line exist in
  both the template and `FAQ/`, matching.
Refused: adding the slug to the vocabulary rule's omit-or-translate list —
  omitting it loses the one handle the user has on an item.
Refused: first use per chat rather than per message — that is readable only to
  someone holding the scrollback in their head, which is the assumption being
  objected to.
Refused: a second queue item for the presentation half — two entries on one
  notation would answer the same question twice.
Refused: a hook — nothing mechanical reads Claude's chat output.
Note: the header clause reaches new projects only; an existing project's queue
  header is the user's own text and migration may not rewrite it. For those
  users the FAQ entry is the whole answer.
--- End build block ---

#### Routing communication feedback to memory masks the method defect that produced it — the memory-boundaries rule needs the exception [memory-masks-method-defects]
Captured by you — raised 2026-08-09 at a /done close, filed after `115f851`. Your point, rendered in Claude's words rather than quoted: if Claude's replies are affected by memory, then the method can't truly be tested.
**The conflict the shipped rule does not see.** plugin-behaviour.md's memory-boundaries rule lists what memory is free for: user preferences, working style, **communication feedback**, cross-project facts. Separately, this project's CLAUDE.md states that all use of the plugin to develop the plugin is testing it, and that any moment session memory covers for something the docs should carry is a mandatory capture. Nobody applied that second rule to *persistent* memory, and the two disagree: saving communication feedback to memory is permitted, and doing it here contaminates the only test the method gets.
**Why it is sharper than a self-hosting quirk.** Communication feedback is very often *evidence about the method's own narration rules*. This session demonstrates it: the user twice said there was too much text — evidence that the /plan checkpoint is too long, filed as [done-invoked-when-user-meant-continue]. Had that also gone to memory, Claude would simply have behaved better, the queue item would have stopped mattering, and the defect would have survived in the shipped docs. Memory would quietly buy a fix for one user while every consumer kept the bug.
**So the routing test is not "is this a preference?" but "is this evidence about the method?"** A preference no method rule governs — a name, a timezone, a tool the user likes — stays memory's. Feedback that a *method-produced behaviour* was wrong is a testing outcome and belongs in the queue, whether or not it also reads as a preference. The overlap is the problem: it is genuinely both, and the current rule names only the branch that silences it.
**Settled at processing 2026-08-19, and the scope goes the opposite way to the one this entry proposed.** It asked whether the exception should be scoped to projects testing the method. **Your decision: general.** A consumer's complaint that Claude narrated badly is evidence about the method too, and it is the **only** such signal originating outside this project — routed to memory it makes their Claude quieter and tells the method's author nothing. Scoping the rule to self-hosting would have protected the one project that already has other ways of noticing and left every other project silently absorbing the evidence.

**So the fix needs no new machinery, because the route already exists.** The three-way discriminator already sends "the method is misbehaving" to the feedback channel and "my app" to the queue. The memory-boundaries rule simply never cross-references it: it names communication feedback as memory's and stops there.

**What changes.** The bare term **communication feedback** comes off memory's list and is replaced by the qualified form — feedback about a behaviour the *method* produced routes by the discriminator, while a preference no method rule governs (a name, a timezone, a tool the user likes) stays memory's.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — Routing and discipline, the memory-boundaries rule. **The file named when this was captured, `plugin-behaviour.md`, was retired 2026-08-10** and the rule moved; the stale pointer is corrected here rather than left for the build to discover. Plus `plugin/throughliner/templates/faq-template.md` with `FAQ/faq.md` and both index lines — the FAQ fires because what the user *does* changes: feedback that used to be absorbed silently now becomes a report they are asked to approve and send.

**No SPEC sentence is owed, checked rather than assumed:** SPEC describes no memory routing anywhere, so no sentence there goes wrong or incomplete.

Rule gate: run — admitted as a qualification on the existing memory-boundaries rule, subordinate rather than freestanding, so no always-loaded slot is spent. **The eviction is the bare `communication feedback` entry on memory's list**, which is what made the two rules disagree. Failure evidence is one recorded instance here plus the structural argument that the affected signal is the only external evidence the method receives.

Relates to [done-invoked-when-user-meant-continue] (the live instance). It used to be a candidate payload for [self-hosting-auto-detection], deleted 2026-08-14 — the absence of any payload only detection could switch on is what settled that item, and this settlement is the same conclusion reached from the other end: the rule wanted widening, not detecting.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, Routing and
  discipline, the memory-boundaries rule — take the bare term
  `communication feedback` off memory's list and replace it with the
  qualified form: feedback about a behaviour the METHOD produced routes by
  the three-way discriminator; a preference no method rule governs (a name, a
  timezone, a tool the user likes) stays memory's. Scope is general, not
  scoped to projects testing the method.
  Write it as a qualification on that rule, subordinate rather than
  freestanding. The route already exists — no new machinery.
  `plugin/throughliner/templates/faq-template.md` plus its
  `faq-index-template.md` line, then re-copied into `FAQ/faq.md` and
  `FAQ/index.md` — feedback that used to be absorbed silently now becomes a
  report the user is asked to approve and send.
Acceptance: the memory-boundaries rule no longer lists `communication
  feedback` bare, and carries the qualified form cross-referencing the
  discriminator. The FAQ entry and index line exist in both template and
  `FAQ/`, matching.
Refused: scoping the exception to projects testing the method — a consumer's
  complaint about narration is the only such evidence originating outside this
  project, and scoping would silence it.
Note: the file named at capture, `plugin-behaviour.md`, was retired
  2026-08-10 and the rule moved; the corrected path is above.
--- End build block ---

#### The rules disagree on how a planning record splits — "per item processed" against "per decision" [plan-entry-split-wording-disagrees]
Filed 2026-08-18 at the close that had to choose between them.

**The two statements.** `skill-nonspecific-rules.md`'s authoring standard says a plan entry "splits per item processed", and reasons from there: a planning decision IS a disposition on a queue item, so the build case's machinery applies unchanged. `SPEC.md` and `done.md` both say a planning record "splits per decision".

**Why the difference is not cosmetic.** They diverge whenever one decision settles several items, which is common — this session settled two SPEC items together, five mailbox items as one group, and two restyle items as a pair. Counted per item the close owed roughly 28 entries; per decision it owed 19. At the measured 316–329 words per split entry that is around 3,000 words, plus an index line each on a file read in full at every retrieve.

**What this close did, so the precedent is visible rather than silent.** Split per decision, on SPEC's and `done.md`'s wording, with the choice put to the user and deferred back.

**Settled at processing 2026-08-19 by reading the code, and it goes against the lean recorded above.** `queue_digest.py`'s `shipped_slugs()` resolves shipped-ness from **filenames** — `<date>-<slug>.md`, one directory listing — so a slug has shipped if and only if an entry is named after it.

**"Per decision" therefore breaks two mechanisms rather than merely costing less.** A decision settling three items produces one file named for one of them, and the other two read as never shipped. The digest's shipped-citation flag misses them, and the below-the-line revisit — which reads shipped-ness off LOG to decide what may lift — would leave a held item waiting on a blocker that had in fact been settled. That is the failure this queue has recorded four times, reintroduced by a wording choice.

**So "per item processed" is right and the always-loaded file was already correct**, which matters because it is the wording a session reads at the moment it decides. `SPEC.md` and `done.md` are what change.

**The measured cost is real and is not paid in full.** The instance that filed this owed roughly 28 entries per item against 19 per decision, about 3,000 words plus an index line each. **Where one decision settles several items, one entry carries the reasoning and its siblings cite it rather than restating it** — each still named for its own slug, so every mechanical reader keeps working, and the argument is written once. That is the relocate-and-cite pattern already used for research findings and for narrative moved into a chat entry; nothing new is invented.

**This entry's own premise was half wrong, checked at processing rather than trusted.** It states that `SPEC.md` and `done.md` both say "per decision". **SPEC says no such thing** — it never describes how a planning record splits at all, and grepping it for the wording and for every paraphrase returns nothing. So the repeal is one file rather than two, and no SPEC sentence is owed.

**Files:** `plugin/throughliner/docs-b/done.md` — the "per decision" wording at the entry-splitting statement, plus the sibling-citation clause, sited there rather than in the always-loaded file because the close is where it is read. **No FAQ entry:** this changes how records are written, not anything the user does.

Rule gate: run — admitted as an amendment reconciling two live statements to the one already in the always-loaded file, plus one clause on `done.md`'s existing entry-writing step; no freestanding rule and no always-loaded slot spent. **The eviction is the "per decision" wording, repealed in two live files.** Failure evidence is one measured divergence and one mechanical dependency, the second of which involves no judgment at all.

Relates to [split-action-defeats-the-bands-in-aggregate], which measures what the split costs, and [plan-entry-split-action-underspecified], shipped.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/done.md`, the entry-splitting statement —
  repeal the "per decision" wording and state "per item processed", matching
  the always-loaded file, which is already correct and is not edited.
  Same file, same step — add the sibling-citation clause: where one decision
  settles several items, one entry carries the reasoning and its siblings
  cite it rather than restating it, each still named for its own slug so
  `<date>-<slug>.md` resolves for every one.
Acceptance: grep `per decision` in `done.md` returns nothing. The step states
  the per-item split and the sibling-citation clause. `skill-nonspecific-
  rules.md` and `SPEC.md` are untouched.
Refused: "per decision" — `queue_digest.py`'s `shipped_slugs()` resolves
  shipped-ness from filenames, so a decision settling three items produces one
  file and the other two read as never shipped; the below-the-line revisit
  would then hold items against blockers already settled.
Refused: siting the clause in the always-loaded file — the close is where it
  is read.
Note: this item's premise that SPEC also says "per decision" was checked and
  is false — SPEC never describes the split, so no SPEC sentence is owed and
  the repeal is one file, not two.
--- End build block ---

#### Restyle `done.md` and `plan.md` to the law-prose standard [law-prose-restyle-heavy-docs]
Filed 2026-08-17 **on your decision that the restyle continues to the rest of the corpus.** [law-prose-restyle] shipped this morning covering `skill-nonspecific-rules.md` alone and was consumed by that build, so the continuation had no queue item at all.

**These two first** because they are the largest rule-bearing docs and both are already scheduled for subtraction work, so findings have somewhere to land.

**What changes.** Each doc rewritten to the wording standard the rule gate specifies: prohibitions restated as the action required, qualifications carried by structure rather than explanation, main clause first, one idea per provision, and rationale moved out of operative statements into the record. The shipped pass is the precedent for what that looks like in practice.

**Acceptance test, taken from the pass that worked:** rule-statement count before and after, accounted for statement by statement, with any change composed rather than asserted — `resources/rule_signals.py` reads the count. **Its stated limit is inherited too:** a flat count cannot detect a rewrite that changed a rule's meaning, so the pass claims coverage of what it read and nothing more.

**Ordering, written into both entries.** This runs before [law-prose-restyle-remaining-docs], and both run before [session-occurrence-audit], which reads these same files and would otherwise gather a list the rewrite makes stale — that is why the audit is held.

**A second lens rides this pass, folded in from [freestanding-rules-that-should-be-subordinate] on your instruction 2026-08-17.** While each doc is rewritten, look for the signature that item names: **two or more rules governing the same subject, stated at the same level, with no declared relationship** — and land them as a parent with subordinate units, which is what the admission rule already requires of a rule being authored and which nothing has ever applied backwards to rules already shipped. Candidate subjects it names besides length: what gets written where, when to ask versus proceed, and what counts as evidence.

**One interaction the fold creates, stated so the acceptance test is not misread.** Subordinating two rules under one parent **reduces** the statement count. So a fall in the count is no longer automatically an eviction: each reduction is attributed to either a merge under a parent or a deletion, and named as one or the other. Without that, this lens and the flat-count test contradict each other.

**And the gap the fold would otherwise leave, closed here.** The known instance — at least three separate statements about how long something should be, none referencing the others — is in `skill-nonspecific-rules.md`, which was restyled this morning **without** this lens. So that file is in this item's scope for the lens alone, not for a second restyle.

**This pass carries TWO lenses, not three. The per-paragraph rationale lens was folded in on 2026-08-17 and taken back out on 2026-08-19** — do not restore it here; it lives in [rationale-lens-after-the-build-view], held until [split-the-cleared-region-for-concurrent-sessions] ships. What removed it was evidence, not preference: the test that lens was waiting on came back confirmed, in `resources/research/rationale-flows-from-items-into-shipped-docs.md`, showing that reasoning written into a work item reaches the doc a build edits — in the settling case with the clause order intact and the final sentence identical, where the item had directed nothing. So the rationale in these two docs arrives from upstream, and a per-paragraph pass would strip text the next build writes back. **The other two lenses are untouched and this item is otherwise unchanged**: the wording restyle and the subordination lens read the docs as they stand and owe nothing to where the text came from.

**Files:** `plugin/throughliner/docs-b/done.md`, `plugin/throughliner/docs-b/plan.md`, and `plugin/throughliner/docs-b/skill-nonspecific-rules.md` for the subordination lens only.

Rule gate: run — no rule is authored, amended or evicted; the standard being applied was admitted when the gate was, and this extends it to more files plus one lens the admission rule already contains. **A restyle is the one pass that can silently author a rule by rewriting one**, which is why the acceptance test is a count accounted for statement by statement rather than a reading.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/done.md` and `plugin/throughliner/docs-b/plan.md`
  — rewrite each to the law-prose wording standard: prohibitions restated as
  the action required, qualifications carried by structure rather than
  explanation, main clause first, one idea per provision, rationale moved out
  of operative statements into the record. The shipped
  `skill-nonspecific-rules.md` pass is the precedent for what that looks like.
  Same two files, second lens — subordination: find two or more rules
  governing one subject, stated at the same level with no declared
  relationship, and land them as a parent with subordinate units. Candidate
  subjects: length, what gets written where, when to ask versus proceed, what
  counts as evidence.
  `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — the subordination
  lens ONLY, not a second wording restyle. The known instance is there: three
  separate statements about how long something should be, none referencing the
  others.
Acceptance: rule-statement count before and after per file, read with
  `resources/rule_signals.py`, accounted for statement by statement rather
  than asserted. Every FALL in the count attributed explicitly to either a
  merge under a parent or a deletion, and named as one or the other.
Refused: the per-paragraph rationale lens — folded in 2026-08-17 and taken
  back out 2026-08-19; it lives in [rationale-lens-after-the-build-view]. The
  rationale in these docs arrives from upstream work items, so a per-paragraph
  pass would strip text the next build writes back.
Note: runs before [law-prose-restyle-remaining-docs], and both before
  [session-occurrence-audit], which is held for that reason.
Note: a flat count cannot detect a rewrite that changed a rule's meaning. The
  pass claims coverage of what it read and nothing more.
--- End build block ---

#### Restyle the remaining rule-bearing docs to the law-prose standard [law-prose-restyle-remaining-docs]
Filed 2026-08-17 on the same decision of yours. **Follows [law-prose-restyle-heavy-docs]** — placement carries the order and this sentence carries the reason, since it could be built on its own and so names no `Blocked by:`.

**Why it follows rather than blocks it.** The two heavy docs are where the standard meets the hardest text, so settling those questions once stops this pass answering them ten times over.

**Scope, narrowed deliberately to the rule-bearing docs.** SPEC and the FAQ are out: the law-prose standard is a standard for *rules*, SPEC is product truth governed by its own three maintenance rules, and the FAQ is consumer-facing answers rather than instructions to Claude. Nothing is orphaned by that — "session" occurrences in SPEC and the FAQ are covered by [session-occurrence-audit], a terminology pass rather than a wording one.

**What changes.** The same standard and the same acceptance test as the heavy-docs pass, applied per file — the rule-statement count accounted for statement by statement **for each doc rather than in aggregate**, so one file's growth cannot hide behind another's cut.

**Files:** every doc under `plugin/throughliner/docs-b/` except the three already restyled — `skill-nonspecific-rules.md`, `done.md` and `plan.md`. Enumerated by listing the folder at build time rather than written out here, because [rename-docs-b-folder] may change that folder's name first and a list written today would name a path that no longer exists.

**Runs before [session-occurrence-audit]**, which is held against this item for that reason.

**Carries the subordination lens too**, folded in from [freestanding-rules-that-should-be-subordinate] on your instruction 2026-08-17: look for two or more rules governing one subject, stated at the same level with no declared relationship, and land them as a parent with subordinate units. Its terms and its interaction with the count are stated once in [law-prose-restyle-heavy-docs] rather than repeated here — including that a **fall** in the statement count must be attributed to a merge or to a deletion, since subordination reduces the count without evicting anything.

**What this item deliberately does NOT carry, stated so it reads as a decision rather than an omission.** The per-paragraph rationale test does not run here — and as of 2026-08-19 it does not run in the heavy-docs pass either, having moved to [rationale-lens-after-the-build-view]. These ten docs keep the **signature-phrase** criterion for rationale, which is what they have had, and that is unaffected by the move. The reason is measured rather than guessed: extending per-paragraph judgement across the fetched docs was costed at roughly 42,000 words of it, and that figure is why the earlier extension was refused. [rationale-audit-fetched-docs-gap] recommended the two-file limit for exactly this reason, and folding the lens everywhere would quietly overturn its own recommendation while claiming to honour it.

Rule gate: run — no rule authored, amended or evicted; an extension of an already-admitted standard to the remaining files, carrying the same silent-authoring caution as its sibling and the same lens.

--- Build block ---
Changes:
  Every doc under `plugin/throughliner/docs-b/` EXCEPT the three already
  restyled — `skill-nonspecific-rules.md`, `done.md`, `plan.md`. Enumerate by
  listing the folder at build time rather than from a list written earlier:
  [rename-docs-b-folder] may change the folder's name first.
  Apply the same law-prose wording standard as the heavy-docs pass, per file.
  Carry the subordination lens too — two or more rules governing one subject
  at the same level with no declared relationship become a parent with
  subordinate units. Its terms and its interaction with the count are stated
  in [law-prose-restyle-heavy-docs] and are not restated here.
  SPEC and the FAQ are out of scope: the standard governs rules, SPEC is
  product truth with its own maintenance rules, and the FAQ is consumer-facing
  answers rather than instructions to Claude.
Acceptance: rule-statement count before and after PER FILE, accounted for
  statement by statement, so one file's growth cannot hide behind another's
  cut. Every fall attributed to a merge or a deletion by name.
Refused: the per-paragraph rationale lens — extending per-paragraph judgement
  across the fetched docs was costed at roughly 42,000 words, which is why the
  earlier extension was refused; these docs keep the signature-phrase
  criterion they already have.
Note: runs after [law-prose-restyle-heavy-docs] and before
  [session-occurrence-audit], which is held against this item.
--- End build block ---

#### /rescan reads as ending the run it was invoked inside, and nothing tells it to hand back [rescan-does-not-hand-back]
**Raised by you 2026-08-21, mid-/plan, from using it before the close on every planning session.** Your report: once /rescan has run you are no longer in /plan and have to run /plan again — which defeats the reason it was made a separate skill. **Your two points, and the second is the sharper one.** It was supposed to be runnable at any time, and it is not, in practice. And what a re-scan turns up is often needed to finish the planning work that just happened, so it should land in the session that still has those items in memory rather than waiting for a planning session that comes after a build.

**Your premise was tested against the documentation and it does not hold — which is what makes this fixable.** `resources/research/skill-content-lifecycle.md` records the finding in full. Claude Code's own words: an invoked skill's content "enters the conversation as a single message and stays there for the rest of the session." So there is no running skill, nothing ends, and `plan.md` was still present and still governing for every turn after /rescan ran. The documentation also names this exact symptom — a skill appearing to stop working — and attributes it to the model choosing other approaches while the content sits there unread.

**So the defect is in how `rescan.md` finishes.** Its last step is headed "Say what happens next", tells the run to name what the captures are waiting for, and then says **"Recommend nothing else"** — with a stated reason, that close machinery accumulating at the end of a chat pulls the whole chat toward ending. That reasoning is sound and is not what is wrong. What is wrong is that a step which says "stop here" and names nothing to go back to reads as the end of the conversation's work, and there is no instruction anywhere in the doc to resume whatever was running.

**Settled at processing 2026-08-21. The final step names the return rather than the close:** where /rescan was invoked while another run was under way, it hands back explicitly and carries on from where that run was. **The anti-close-pull reasoning is untouched and must stay** — returning to /plan is the opposite of leaning toward /done, so this removes the dead end without reintroducing the pull the step exists to prevent.

**The wider half was split out on your decision, as [procedure-docs-cannot-tell-finished-from-interrupted].** Do not fold it back: your own evidence is that a terminal step is usually right, so the general question is whether a doc can tell finished from interrupted, and that has no answer yet. This item fixes the one confirmed instance and claims nothing about the other four docs.

**One genuine platform limit to carry into the design.** Auto-compaction re-attaches only the most recent invocation of each skill, newest-first within a 25,000-token budget, so in a long chat an older skill's content genuinely can be gone. Re-invoking is the documented remedy there — but that case is unrelated to another skill having been invoked, and it must not be used to justify a general "run /plan again" instruction.

**You found a second defect the same day, and it is the stronger of the two.** The final step does not merely fail to hand back — it **positively sends the work away**. Its instruction is to name what the captures are waiting for, and the doc's own wording is *"a planning session decides what happens to each one."* Read inside a planning session that is still running, that sentence is false: **this** one can decide them, and /plan is entitled to, since processing a capture is exactly what /plan does. So the user is told her new captures belong to some future session while the session that could settle them is still open. A missing instruction is an omission; this is a statement that misdirects, and it explains why the effect held even when nothing had ended.

**Your second question — whether the hooks and the enforcement are attached to /plan — was checked in the code, and the answer is that none of it is.** `hooks.json` registers all four hooks against Claude Code's own events (SessionStart, PreToolUse, PostToolUse, Stop) and against tool names. Not one is bound to a skill, so no hook can be lost by invoking another skill or gained by invoking /plan.

**The scope-lock is the one that looks skill-bound and is not.** `pre_tool_use.py` decides a session is a planning one by **the absence of this session's `_build-<session-id>.md` file**, and says so in its own comment: *"Keyed on the build working file being absent rather than on 'a planning session', because absence is what the code can actually see."* /plan creates no working file, so the planning standing list — QUEUE.md, SPEC.md, `LOG/`, `FAQ/`, `resources/research/`, the scratchpad — is in force in **every** chat with no build running, whether or not /plan was ever typed. The one documented exception is /setup, which declares itself with a scratchpad marker for the length of its run.

**So the enforcement was never at risk, and that narrows the fix rather than widening it.** Nothing has to be rebuilt or re-attached; the whole defect is two sentences at the end of one document.

**The ripple was traced by grep at processing, not written from the discussion**, per the keep-step's repeal limb. The repealed string is *"a planning session decides"*. It reaches three live sites: `rescan.md` line 133, `templates/faq-template.md` line 551, and `FAQ/faq.md` line 551, the last being a straight copy of the template. **Two further hits are correct as written and are excluded by name**, stated in their own sentence rather than on the Files line: `faq-template.md` line 142 uses the phrase about how SPEC edits happen, a different subject; and line 168 describes /done's lighter version of the same scan, where leaving the sorting for the next /plan is right, because /done really is closing.

**The level was asked rather than defaulted to, and the fix belongs at the instance.** A rule requiring procedure docs to hand back would be a rule about how rules are written, competing with the whole always-loaded set to correct two sentences, and no hook can read whether a conversation resumed a procedure. The doc that misdirects is the doc that changes.

**Files:** `plugin/throughliner/docs-b/rescan.md`, `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines.

**SPEC is not on that line because its sentence was written in this planning session**, ahead of the build. **No epoch bump** — no existing project's files become structurally wrong. Shipped, not host-only: every consumer meets the same dead end.

**The FAQ entry fires on its own test**, which is what the user *does*: today they re-run /plan after a /rescan, and after this they do not.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/rescan.md`, Step 3 — replace "a planning session
  decides what happens to each one" with wording that names THIS run where one
  is under way, and add an explicit hand-back: resume whatever was running and
  carry on from where it was. Keep the "Recommend nothing else" clause and its
  anti-close-pull reasoning intact; the hand-back is a return, not a close.
  `plugin/throughliner/templates/faq-template.md` line 551 — the same repeal:
  the answer stops telling the reader a future planning session decides, and
  says the session they are in can, plus one sentence that /rescan hands back.
  Add the new FAQ entry and its index line for the changed action.
  `FAQ/faq.md` and `FAQ/index.md` — re-copied from the templates after the
  template edit lands. The template is canonical; these are straight copies.
Acceptance: grep "a planning session decides" across the repo outside `LOG/`
  returns only the two excluded FAQ hits (lines 142 and 168) and this queue
  item. `rescan.md`'s final step names a return. `FAQ/faq.md` is byte-identical
  to `faq-template.md`, and the same for the two index files.
Refused: rewriting all five procedure docs to end conditionally — the user's
  evidence is that a terminal step is usually correct, and with no readable
  signal a conditional ending guesses. Split to
  [procedure-docs-cannot-tell-finished-from-interrupted].
Refused: a general "re-run /plan afterwards" instruction — the skill content
  never left context, so re-running is unnecessary; auto-compaction is the only
  case where it is needed and it is unrelated to another skill being invoked.
--- End build block ---

Rule gate: run — admitted as an amendment to `rescan.md`'s existing final step, subordinate rather than freestanding, and sited in a fetched procedure doc so no always-loaded slot is spent. **The eviction is the "a planning session decides" wording, repealed outright at all three live sites.** Failure evidence is the user's report of the same outcome at every planning session, plus the documented mechanism showing the belief the wording created was false. **A hook was considered and refused:** nothing mechanical can read whether a conversation resumed a procedure.

Relates to [plan-does-not-build-keeps-being-relitigated], which is the same class of fault — a doc's own wording teaching a later session the wrong thing — and to `resources/research/skill-content-lifecycle.md`, which is the evidence this rests on.

#### /setup runs a migration only for a queue shape no live project still has, so every later epoch's conversion is unreachable [setup-migration-gate-is-epoch-3-shaped]
Filed 2026-08-21 by Claude, **from your question — how did items reach Processed without describing any work?** The question corrected Claude twice: the items do describe their work, and both faults Claude first filed were false. What survived is worse than either.

**Two claims from this item's first version are withdrawn as wrong, recorded so nobody re-derives them.** The format epoch **was** bumped: `FORMAT_EPOCH` is 4 in `session_start.py`, and its history comment defines epoch 4 as the build block exactly. And the migration recipe **does** exist: `migrate-checklist.md` carries an "Epoch 4 — build blocks on cleared work" section, well designed — lift the sentences the item already has, move an item that never said what it changes below the readiness line rather than inventing instructions for it, do nothing to held items, captures, `[user]` or `[freeform]` work, and write the blocks with the user present because telling instruction from history is a judgment.

**The single fault is the gate that decides whether the checklist is opened at all.** `setup.md`'s migration step reads:

```
existing QUEUE.md uses an old multi-section shape
    (## Red flags · ## Batches · ### Parked · ## Deferred tests · ## Captures)
        ->  load migrate-checklist.md and follow it
already two-section (## Processed / ## Unprocessed)
        ->  skip
```

**Two-section is what every project has had since epoch 3.** So the gate tests for a shape no live project still has, and every epoch after 3 — starting with this one — sits behind a condition that can now only fail. The checklist is loaded only by projects that have not been migrated in months.

**The live instance is this session, and it is the whole failure end to end.** /setup ran here today, found a two-section queue, skipped the checklist, and wrote `4` into `.throughliner-format-epoch`. It converted nothing. **The marker is what `session_start`'s halt compares against, so writing it is what silences the warning** — this project now reports itself current while fifteen cleared items sit in format 3's shape, and the close of that run reported a clean migration.

**Why the gate was written this way, which is not carelessness.** At epoch 3 the queue conversion *was* the migration, so "is the queue old-shaped?" and "is this project behind?" were the same question. They came apart the moment an epoch changed something other than the section layout, and nothing revisited the gate.

**What changes.** The gate stops asking about the queue's shape and asks the question it means: is the project's recorded epoch below the plugin's? Where it is, load `migrate-checklist.md` and follow **every** epoch section from the project's recorded number up to the current one, in order. The existing two-section test survives as what the epoch-3 section itself checks, rather than as the door to the whole checklist.

**The marker is written last and only on success, which the doc already requires** and which this run's outcome shows is load-bearing: /setup's own step says to write the epoch "last among the migration edits, once the conversions above have actually landed", precisely so the warning is not silenced while the project is still on the old shape. The gate skipping meant there were no conversions to land, so the instruction was satisfied vacuously.

**Files:** `plugin/throughliner/docs-b/setup.md` — the migration step's gate, and the sentence introducing the checklist. **`migrate-checklist.md` is NOT listed and is excluded deliberately:** its epoch sections are correct and complete; nothing there is what failed. **No epoch bump** — this changes how a migration is reached, not any project document's shape. Shipped: every consumer project past epoch 3 is in this state.

**This project's own unconverted queue is [convert-cleared-items-to-build-blocks], filed alongside** — the repair here is the recipe, and running it on this queue is separate work.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/setup.md`, the migration step's "Convert an
  old-format QUEUE.md" gate — replace the queue-shape test with an epoch test:
  where the project's recorded epoch is below `FORMAT_EPOCH`, load
  `migrate-checklist.md` and follow every epoch section from the recorded
  number up to the current one, in order. Reword the step's heading and lead
  sentence, which both name the queue conversion as though it were the whole
  migration. Keep the write-first requirement (draft the conversion, show it,
  get approval) and keep the epoch marker written last, only after the
  conversions land.
Acceptance: a project recorded at epoch 3 with an already-two-section queue
  reaches the epoch-4 section of the checklist. A project already at
  `FORMAT_EPOCH` opens the checklist not at all. The epoch marker is not
  written where no conversion ran.
Refused: adding epoch 4 to the existing gate as a second condition — it leaves
  the same defect for epoch 5, which is how this one arrived.
Refused: detecting the shape from the documents instead of the marker —
  rejected already in `CLAUDE.md`, because it guesses about files users
  legitimately hand-edit.
--- End build block ---

Rule gate: run — no rule is authored or amended; a condition inside one procedure step is replaced. **The eviction is the queue-shape test**, repealed outright rather than extended, and the refusal to extend it is recorded in the block above because extending is the intuitive move. Failure evidence is one instance, and it is this session's own migration, observed end to end rather than reasoned about.

#### A capture the user raises is written before she is asked whether to process it, throwing the write away most of the time [ask-before-writing-a-user-raised-capture]
**Raised by you 2026-08-21, from an instance minutes earlier in this session.** Your words for the shape you want: instead of "filing it", *"do you want to capture this now for later, or go straight through to processing?"* And your estimate, which is the evidence this rests on: **you would answer processing about 90% of the time**, because the item is in current memory and there is no time like the present — in which case the write need not happen at all.

**The asymmetry in the shipped rules, which is the defect.** `skill-nonspecific-rules.md`'s /plan carve-out puts the offer **before any write** when *Claude* raises something, and **after the write** when the *user* does. It then gives the reason for the Claude-side placement: *"Asking after the write costs a write that is thrown away, since a capture answered 'work it now' is immediately rewritten as a work item."* **That reasoning does not mention who raised the thing.** It applies to both branches identically, and only one branch was built on it — which reads as something nobody re-examined rather than something anyone chose.

**Your 90% is what turns a symmetry argument into a measured one.** A cost paid rarely is a rounding error; a cost paid nine times in ten is the common path. The two captures written in this session's later stretch were each several hundred words, and on your own estimate most such writes are immediately rewritten as work items.

**A second failure, separate and Claude's.** In the instance that prompted this, the offer was not made at all — the capture was written, reported as "filing it", and the next message asked about closing. The `[PROMPT]` step and the non-optional "anything else to add first?" clause were both skipped. **The rule as written would already have caught most of this**, so the doc defect and the compliance failure are two things and the item fixes only the first.

**What changes.** Both branches ask before the write. A user-raised capture is offered *capture it for later, or process it now* — recommending process-now, which the rule already does — with the "anything else to add first?" clause preserved. Where the answer is process-now, nothing is written as a capture at all: the item goes through the present-and-interview loop and is written once, as a work item.

**The clause gets easier to honour rather than harder, which is why it survives the move.** Asking before the write puts the question at the moment the user is still mid-thought, which is exactly when "anything else to add first?" does its work — the clause was dropped once before and reinstated because it stops an idea being closed off early.

**What is given up, stated rather than discovered.** Write-first exists so text reaches the document where the user reads it in place rather than as a chat paste. Asking first trades a little of that: for the 10% answered "capture for later", the wording is discussed in chat before it lands. **That is not a breach of write-first**, whose test is recoverability and which already carries an ideation clause holding the write while a design is unsettled — this is that clause reaching one more moment, not a new exception to the test.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the /plan carve-out in Communication), `plugin/throughliner/docs-b/plan.md` (the process-now-offer section), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` — **the FAQ hit was found by grep and would have been missed**: its answer tells consumers that "Claude files it and asks whether you want to dig into it now", which becomes false. That is a sync of an existing answer rather than a new entry, so no index line changes.

**No SPEC sentence is owed, checked rather than assumed:** its sentence says a mid-session capture "comes with an offer to process it now or carry on" and states no ordering, so no sentence there goes wrong or incomplete.

--- Build block ---
Changes:
  `docs-b/skill-nonspecific-rules.md`, the /plan carve-out in Communication —
  repeal the split placement. Both branches ask BEFORE any write. Keep the
  thrown-away-write reasoning as the stated reason, now covering both. Keep the
  Claude-raised branch's bar on soliciting further captures, and keep the
  user-raised branch's "anything else to add first?" clause.
  `docs-b/plan.md`, "Process-now offer after a user-filed capture" — replace
  "File it first, then offer the branch" with asking first; the two routes and
  the process-now recommendation are unchanged. Where the answer is process-now,
  no capture is written: the item goes straight into present-and-interview and
  is written once as a work item.
  `templates/faq-template.md` line 309 — "Claude files it and asks whether you
  want to dig into it now" becomes asks-then-files. Reword of an existing
  answer; no index line changes.
  `FAQ/faq.md` — re-copied from the template after that edit.
Acceptance: grep "File it first" across `docs-b/` returns nothing. Both branches
  of the carve-out read as before-the-write. `FAQ/faq.md` is byte-identical to
  `faq-template.md`.
Refused: leaving the user branch alone on write-first grounds — write-first's
  test is recoverability, and its ideation clause already holds writes while a
  design is unsettled, so this is that clause reaching one more moment.
Refused: dropping the "anything else to add first?" clause as redundant once the
  question moves earlier — it was dropped once before and reinstated, and asking
  earlier is when it does most of its work.
--- End build block ---

Rule gate: run — admitted as an amendment removing a distinction inside an existing always-loaded rule, so no freestanding rule and no slot spent; the rule gets shorter. **The eviction is the file-first ordering on the user-raised branch**, repealed in the always-loaded rules, in `plan.md` and in the FAQ answer that describes it. Failure evidence is one observed instance in this session plus the user's own estimate that the discarded path is the common one. **A hook was considered and refused:** nothing mechanical can tell a capture that was going to be processed anyway from one genuinely being filed for later.

Relates to [processing-appends-where-it-should-rewrite], raised in the same exchange, and to [keep-step-accretes-from-five-items] — this touches the carve-out rather than the keep-step, so it adds nothing to the step that item is watching.

#### Run the per-paragraph rationale lens over `done.md` and `plan.md`, once the transcription is stopped at source [rationale-lens-after-the-build-view]
**Split out of [law-prose-restyle-heavy-docs] on 2026-08-19**, when the test that item was waiting on came back confirmed. The other two lenses in that pass are unaffected and stay with it; only this one moves.

**Why it moved rather than staying folded in.** The lens deletes a paragraph, reads what remains, and keeps the sentence only where the instruction is left incomplete without it. That works on text that is going to stay put. It does not work while the work items are still feeding rationale into these docs at every build — the pass would strip text the next build writes back, and have to run again. The evidence that this is actually happening is `resources/research/rationale-flows-from-items-into-shipped-docs.md`, tested against git rather than argued.

**What changes when it runs.** Every paragraph of `done.md` and `plan.md` gets the delete-and-reread test: a complete instruction after the deletion means what came out was history and it goes to the record; an unfinished one means it was operative and is written into the rule. The record carries each removal and where it went, site by site — which is what this pass gives up by folding judgement into the rewrite rather than auditing first.

**Files:** `plugin/throughliner/docs-b/done.md` and `plan.md`, plus `LOG/` for the site-by-site record of what moved.

**Lifted 2026-08-21.** [split-the-cleared-region-for-concurrent-sessions] shipped and was confirmed — `LOG/2026-08-20-split-the-cleared-region-for-concurrent-sessions.md`, five suites passing and the generator run against this live queue. A build now reads a derived view carrying instructions only, so rationale is no longer flowing from work items into these two docs at every build, which is the condition this pass was waiting for.

Rule gate: not needed — no rule is authored or amended. A pass that relocates rationale out of operative statements applies a standard already admitted, and the operational-versus-historical distinction it uses is the method's own delete-and-reread test.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/done.md` and `plugin/throughliner/docs-b/plan.md`
  — apply the delete-and-reread test to every paragraph: delete it and read
  what remains. A complete instruction means what came out was history, and it
  goes to the record; an unfinished one means it was operative, and it is
  written into the rule.
  `LOG/` — the session record carries each removal site by site, and where the
  text went. That record is what this pass gives in exchange for auditing
  rather than folding judgement into a rewrite.
Acceptance: every paragraph of both files has been through the test, and the
  LOG entry lists each removal with its destination. No paragraph is removed
  without a recorded destination.
Refused: running this folded into [law-prose-restyle-heavy-docs] — while work
  items were still feeding rationale into these docs at every build, the pass
  would strip text the next build writes back. That condition ended when
  [split-the-cleared-region-for-concurrent-sessions] shipped.
--- End build block ---

#### A repeal can falsify an already-posted announcement, and the same grep would catch it [repeal-falsifies-a-posted-claim]
Split from [repeal-has-no-ripple-trace] at processing 2026-08-17, when that item reached 542 words against a 345 ceiling. Kept apart rather than merely trimmed because the two differ in readiness, not only in length: the live-doc trace is buildable now and this is not.

**The instance is your own spec-driven-development post**, which described a build that "asks first, adds SPEC.md to its own file list, and edits it in the same commit". [missed-spec-write-interrupts-the-run] inverts that — a build now hands the sentence back rather than writing it — so a claim that was true when posted became wrong through ordinary work, inside the same conversation that made it.

**The trace is identical to its sibling's.** Grep the distinctive words of the repealed sentence. What differs is only where you grep: a repeal already greps live documents, and this extends the same pass to the record of what was published.

**Why it cannot be built yet.** There is nothing to grep. Posts are not written down anywhere, which is [send-record-lacks-destination-and-intent] — the outgoing index that gives every send a line carrying its destination, its intent and what it claimed. Until that file exists this item has no target, which is why it is held rather than cleared.

**What changes when it lifts.** The repeal limb on the keep-step gains one more place to look: an item repealing shipped behaviour greps `INBOX/sent.md` for the claim, and where it finds one, a correction post is filed as its own `[user]` line rather than assumed.

**Files:** `plugin/throughliner/docs-b/plan.md` (the repeal limb, extended to the sent record) and `CLAUDE.md` (the Discord section, which is where a correction post's obligation belongs and is host-only).

Rule gate: run — one more site on the repeal limb its sibling item ships, so it is subordinate to a rule that will already exist by the time this builds, and spends no slot. Nothing evicted. Failure evidence is one instance, and it is the only one available: nothing records what was posted, so earlier cases cannot be found at all — which is itself the argument for the record rather than for this rule.

**Lifted 2026-08-21.** [send-record-lacks-destination-and-intent] shipped and was confirmed — `LOG/2026-08-20-send-record-lacks-destination-and-intent.md`; `INBOX/sent.md` exists and already carries its first line. So there is now a record to grep, which is the one thing this item was missing.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/plan.md`, the keep-step's repeal limb — add one
  more place to look: an item repealing shipped behaviour greps
  `INBOX/sent.md` for the claim, using the repealed sentence's distinctive
  words, the same grep the limb already runs over live documents.
  Same limb — where a match is found, a correction post is filed as its own
  `[user]` line rather than assumed.
  `CLAUDE.md`, the Discord section — state the correction-post obligation
  there, which is where it belongs and is host-only.
Acceptance: the repeal limb names `INBOX/sent.md` as a grep target and states
  the `[user]` correction line. The Discord section carries the obligation.
Refused: folding this back into [repeal-has-no-ripple-trace] — the two differ
  in readiness, not only in length; that one was buildable and this was not.
Note: this was unbuildable until `INBOX/sent.md` existed. It does now —
  [send-record-lacks-destination-and-intent] shipped and was confirmed.
--- End build block ---

#### Split the bundled gitignore offer so a private queue with a public log is reachable [queue-privacy-default]
**Subject settled at processing 2026-08-17; the slug is unchanged because slugs are immutable.** Raised by you as a consequence of cross-project captures but true today regardless. **The rescope is Claude's, deferred to in your words: "as you recommend."**

**The default does not move, on your own objection to your own proposal:** someone may want a visible queue for transparency.

**The real gap is that the offer is bundled.** Scaffolding offers `SPEC.md`, `QUEUE.md` and `LOG/` as one all-or-nothing choice. So a user who wants their plans and reasoning private while their history stays public cannot have that — the combination is unreachable rather than merely un-defaulted, and it is the combination this project itself runs on in spirit, since LOG is what it publishes and the queue is where the thinking sits.

**What changes.** `setup.md`'s privacy offer becomes per-document rather than one bundle, with the trade stated once rather than three times, and no default changed for anyone. The existing single-question shape is what earns the split: it stays one question with three answers, not three questions.

**Files:** `plugin/throughliner/docs-b/setup.md` (the privacy offer), `plugin/throughliner/templates/faq-template.md` plus `FAQ/faq.md` and both index lines.

**SPEC is not on that line** — its privacy-posture sentence describes the bundle and was rewritten in the planning session that processed this.

**Held below the line 2026-08-18, on inbound mail rather than on anything wrong with this design.** A consumer project reported that a `.gitignore` can leave `SPEC.md`, `QUEUE.md` and `LOG/` untracked with nothing noticing, which is [gitignored-core-docs] — the same code path this item rewrites. Shipping a per-document offer while the check beside it cannot see a fatal pre-existing entry would put a second question in front of the user at the one moment the first one is already going wrong. Settle them together.

**Lifted 2026-08-21.** [gitignored-core-docs] shipped and was confirmed — `LOG/2026-08-20-gitignored-core-docs.md`, with a new suite passing over each path alone, all three together, no repository at all, and unrelated ignore lines. The check beside this offer can now see a fatal pre-existing entry, so the two can ship in either order.

Rule gate: not needed — no rule authored or amended; this widens an existing offer's answer set and evicts nothing.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/setup.md`, the privacy offer — split the bundled
  all-or-nothing choice into a per-document one covering `SPEC.md`,
  `QUEUE.md` and `LOG/` separately, so a private queue with a public log is
  reachable. Keep it ONE question with three answers, not three questions.
  State the trade once rather than three times. Change no default.
  `plugin/throughliner/templates/faq-template.md` plus its
  `faq-index-template.md` line, then re-copied into `FAQ/faq.md` and
  `FAQ/index.md` — the user is now answering a differently shaped question.
Acceptance: setup.md's offer lets each of the three be chosen independently
  and is still a single question. Defaults are unchanged from before. The FAQ
  entry and index line exist in both the template and `FAQ/`, matching.
Refused: changing the default to private — your own objection to your own
  proposal: someone may want a visible queue for transparency.
Note: SPEC is not in the file list. Its privacy-posture sentence described the
  bundle and was rewritten in the planning session that processed this.
Note: held until [gitignored-core-docs] shipped, so a second question would
  not land while the first was already going wrong. That shipped and was
  confirmed; the two can now ship in either order.
--- End build block ---

#### The scope-lock guards files, and work that leaves the machine passes unguarded [scope-lock-guards-files-not-work]
Filed 2026-08-19 from INBOX mail sent by a private legal-evidence project running 1.20.0-test12. **Their user raised it; the sending project's Claude wrote the diagnosis, and she asked for both halves to be sent.** Identifying details from the message — the correspondent's folder path and the people it names — are deliberately not carried here.

**What happened there.** In one /plan session, that chat drafted a substantive letter to an external professional and the user sent it — the most consequential act of the session by a wide margin — and nothing gated it, because an email is not a file in the project. In the same session the scope-lock twice refused a four-line correction to that project's own CLAUDE.md, which the user had already read and approved.

**The guard fired on the trivial thing and was silent on the serious one, and that is not an argument for loosening it.** "What leaves the machine" and "what files get written" have come apart. The method's own rules already treat the first as the graver category — nothing is sent without the user seeing the exact text — but only the second is mechanically enforced, and the approval rule is a behavioural one that a session can simply not reach for.

**Their user's framing, which is the part worth carrying.** Throughliner governs work wherever it is conducted, not only work touching this machine. Her example: a `[user]` item in another project that involves unpicking a physical dress, nowhere near a filesystem, still work, still governed, still running under /next. The principle exists in the method; the enforcement stops at the file boundary.

**A vocabulary gap they also surfaced.** That session's Claude reached for `[freeform]` to describe what the session was doing, as though it were a mode a /plan session could slip into. It is not — it is a work-item flavour. Their user corrected it, which leaves live unqueued work happening inside a planning session with no name in the method at all.

**To settle at processing, and the obvious fix may be wrong.** A hook cannot see an email. Weigh whether this wants a rule at all, or whether the honest move is to state the limit plainly — the scope-lock covers files and nothing else — rather than implying coverage the mechanism cannot deliver. This project has repeatedly chosen the honest-limit route over a check that over-claims.

**Settled at processing 2026-08-21, and the account above is overturned in two places rather than merely extended.** Both are left standing, because the reasoning that fell is what stops the same conclusions being reached again.

**First: "nothing gated it" does not survive the detail.** Their user read the letter and sent it herself. The never-send-unseen rule was therefore satisfied — Claude drafted, she approved by sending. What was missing was a record, not consent, and the item's framing of a serious act passing unguarded overstates what happened.

**Second: the record half shipped the day after this was filed, so part of this item is already done.** [send-record-lacks-destination-and-intent] landed 2026-08-20 and `feedback-and-inbox.md` now requires a line in `INBOX/sent.md` for *"Mail, a method report, a GitHub issue, a public post, a draft handed to another project — anything that leaves this machine."* A letter to an external professional is squarely inside that wording. Any project on the current version now leaves a trace of exactly the act this item says left none.

**And the reason no hook can reach it is sharper than the one recorded above, which matters because it rules out a whole class of fix rather than one option.** It is not that a hook cannot see an email. It is that **the send was never Claude's action**: no tool call carried it, so there is nothing to intercept by construction. A guard cannot fire on an act performed by the human, outside the session, through a surface the session never touches.

**So what remains is the honest-limit statement, which is the route this item already leaned toward.** Nothing anywhere says the scope-lock covers files and nothing else. Their user's framing is true of the *method* and false of the *mechanism*, and that mismatch is what lets a file-lock read as general coverage.

**The vocabulary half is kept and stays small, deliberately.** `[freeform]` names a work-item flavour and never a mode a session can be in. The fix is not to name the unnamed thing: the always-loaded rules warn that invented states, tags and session containers are a recurring failure here and that the user has caught each one, and live unqueued hand-work in a chat is the ordinary case the method already describes without needing a term. One clause saying flavour-not-mode is the whole of it.

**Files:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — the scope paragraph gains the limit statement, and the `[freeform]` flavour block gains the not-a-mode clause.

**No SPEC sentence is owed, checked rather than assumed.** SPEC's scope-lock paragraph describes what the lock covers without claiming it covers anything else, so no sentence there goes wrong or incomplete. **No FAQ entry** — nothing a user does changes. **No epoch bump.** Shipped, not host-only: the report came from a consumer and both clauses are read by every consumer.

--- Build block ---
Changes:
  `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, the Scope section —
  add one statement that the scope-lock covers files and nothing else, so work
  that leaves the machine or happens away from the filesystem is governed by the
  approval rules and by nothing mechanical. State it as what the mechanism does,
  not as an apology for what it does not.
  Same file, the flavour-marker block — one clause: `[freeform]` names how a
  work item is executed and is never a mode a session is in. Do not add a name
  for unqueued hand-work in a chat.
Acceptance: the Scope section states the file boundary explicitly. The flavour
  block says flavour-not-mode. No new state, tag, mode or session type appears
  anywhere in the diff. Rule-statement count accounted for, since this adds two.
Refused: a mechanical guard on outbound work — the send is not Claude's action
  and passes through no tool, so there is nothing to intercept.
Refused: naming the unqueued-hand-work case — inventing a state or container is
  the recurring failure the always-loaded rules already warn against.
Refused: the record obligation — already shipped by
  [send-record-lacks-destination-and-intent] on 2026-08-20.
--- End build block ---

Rule gate: run — admitted as two clauses on existing always-loaded statements, the Scope section and the flavour-marker block, subordinate rather than freestanding. **They sit in the always-loaded file and each spends a slot**, stated plainly rather than waved past: the first must fire wherever a session reasons about what the lock protects, and the second wherever a flavour is reached for, so neither can be fetched. **Nothing is evicted.** Failure evidence is one consumer instance for each half, both in a single reported session. **A hook was considered and refused**, on the record in the block above.

#### [user] Discord post: Claude now knows how the work cycle actually fits together [discord-post-cycle-awareness]
Captured by you 2026-08-12; the angle is yours — awareness of the build cycle.
**Cannot be written until [cycle-summary-at-every-skill-opening] has shipped.**
**The honest before-picture, also the strongest material.** Every piece was documented — what an audit does, what a capture is, what /plan may process, what /next may build — and nothing stated the loop. Claude assembled it wrong twice in consecutive sessions, both times confidently, reasoning that a planning session between an audit's findings and their build meant the findings couldn't reach the build. That is the cycle working. Your objection the second time, rendered in Claude's words rather than quoted: this is the second planning session in a row where you've had to explain it.
**The design point worth including.** A flat list of stages would not have prevented either failure, because both were about a loop *closing*. What shipped names the return edges explicitly.
**Same judgment as the sibling post:** the before-picture is Claude getting it wrong; publishing that is yours to decide.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [cycle-summary-at-every-skill-opening] shipped — `LOG/2026-08-12-cycle-summary-at-every-skill-opening.md`. Ordinary ready work. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: second in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone held it.

**Lifted to the head of the chain 2026-08-19, on your instruction, and the pacing is untouched.** What moved is which post goes first, not how often one goes out. [discord-post-context-adjacency] gave up the head because its subject was overtaken by the ladder work settled the same day; this post's own feature shipped 2026-08-12 and nothing about it has changed since, so every claim in it is true of the installed plugin. The three posts behind it still follow in order, one a day.

#### [user] Write the article comparing Throughliner to memory-system approaches, finishing with what shipped [competition-comparison-article]
**Captured by you 2026-08-15**, from a discussion prompted by Discord talk about "Obsidian memory systems" and "dreaming". **Your framing and your decision: the analysis reads as an article starter for the Throughliner site, and rather than sending it now it should be captured and finished with our shipped solutions, with the announcement doubling as a Discord post.**

**This is your own shipped-only rule applied correctly, and you reached it independently.** `CLAUDE.md` says a post announces only what has shipped, and that where a post describes work designed but not built, it waits for the build and is filed as a queue item naming what it waits on. That is exactly this.

**Your stance on the article's framing, recorded 2026-08-17 and NOT generalised into a rule.** Claude proposed turning it into a standing rule about all writing describing Throughliner, and you refused: it *truly depends what we are writing, and the tone required*. Claude had also flattened the position itself — writing "no stake in persuading anyone that one approach beats another" where **your actual position is that you have a stake, just not in being seen as the best thing since sliced bread.**

**Your assessment of the draft, which is the live problem with this item.** It swung from hard marketing to substantially explaining why the competition is better. You sent it to the other project for polishing rather than continuing here, because you wanted to move on — so the draft is out of this project's hands and the item covers what comes back.

**The queue-read weakness is NOT answered, corrected 2026-08-19, and this must be right before the article goes out.** It once read that the article's weak points — manual curation and a 56,000-token queue read — were answered by [digest-reports-computed-fields-not-summaries]. That became false on 2026-08-17, when the digest was expressly stopped from replacing the read: a planning session now runs the digest **and** reads the whole file, because the digest computes facts and the file carries the reasoning. So the full read is still paid, deliberately.

**What actually addresses it is unbuilt.** [split-the-cleared-region-for-concurrent-sessions] gives a build a derived view and stops it reading the queue at all. **Under the shipped-only rule the article cannot claim that until it ships**, and the honest line if it goes out sooner is that planning still reads everything and the reason is that reasoning across items is what planning is for.

**Read this paragraph before drafting.** A `[user]` item sitting cleared to run, producing public text, is exactly how [discord-post-context-adjacency] was nearly posted about a mechanism that no longer existed.

**The substance, drafted in discussion and to be rewritten rather than pasted.** *Stronger:* typed documents with defined roles versus an undifferentiated note graph, so product truth, pending work and history each have a home; memory coupled to execution, since /next builds from the queue rather than merely reading it; the throughline carrying *why* rather than only what; deletion as a user-approved fate decision rather than an automatic prune; and everything as plain markdown in git, reversible and auditable. *Weaker:* curation is manual, which is dreaming's entire job — sixty unprocessed items with duplicates accumulated over weeks, seven merges by hand, six items found behind already-shipped blockers; scale, where graph retrieval never needs to read everything; and one-way links, where backlinks are derived for free.

**The verification step runs BEFORE drafting, and is not optional.** `resources/research/auto-memory-staleness.md` is dated 2026-06-09 and names AutoDream as Anthropic's own consolidation sub-agent — two months old, and what the Discord means by "Obsidian memory systems" may be a specific community project rather than the general vault-as-memory pattern. **Publishing a wrong description of someone else's system under your name is worse than publishing nothing**, and unlike everything else this project writes, it is a claim about a third party. Search first, update the research file, then draft.

**Two artifacts, not one text, settled at capture.** The article is the full piece and may be long, may discuss competitors, and may say where Throughliner is weaker. The Discord post is capped at 2,000 characters, takes the shipped fix as its subject with the comparison only as framing, and points at the article. One text serving both would either saddle the announcement with a comparison it doesn't need or truncate the article into a changelog.

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes**, and Claude has no route to Discord or to the site — the user posts both.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**Only the final step yields to the one-a-day chain.** Three posts are queued ahead of it, and the pacing rule applies to the post rather than to the writing — so the item is cleared and the article can be drafted whenever. Carried as prose today because there is no way to write a date; once [not-before-date-field] ships, this becomes a `Not before:` line.

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected).

--- Cleared to run above this line ---

#### [audit] Classify every occurrence of "session" against the settled vocabulary, immediately before the corrections [session-occurrence-audit]
Filed 2026-08-17, absorbing five captures from [terminology-corpus-audit] that were deleted once their content was carried into this item and into [session-vocabulary-corrections].

**The vocabulary, settled by you on 2026-08-17 and recorded here because this item and the corrections both read it: a RUN is a command executing — a /plan run, a /next run — and a SESSION is the chat.** You chose it over two alternatives — a `<command>` session pattern, and keeping three named slots — because "session" is already in widespread use meaning the chat, so this splits the two ideas rather than adding qualifiers to a word doing two jobs. **Your correction to Claude's objection:** "the close" is residual language from a step that no longer exists, so it was no argument against anything.

**What the audit reads.** Every occurrence of "session" across the procedure docs, `faq-template.md` / `FAQ/faq.md` (185 each, the same document) and `SPEC.md` (88). Roughly 707 in all.

**What it produces.** One classification per occurrence: means the chat, means a run, or is correct as it stands and must be left alone. A stop-list is a constraint it inherits: "mid-session", "short session", "fresh session" and "isolated session" all correctly mean the chat and are left alone, as is `done.md`'s "session type", which classifies a chat rather than naming a run.

**Why an audit and not a script.** Finding the occurrences is a grep; deciding what each one means is judgment on every line. That is this project's own test for when an audit survives.

**Why it runs behind the restyle.** The restyling passes rewrite the same text, so a list gathered before them is stale before anything uses it. [law-prose-restyle] shipped in `7e3c1c8` — `LOG/2026-08-17-law-prose-restyle.md` — but covered one file, so the reason still stands for the rest.

**Lifted and re-held on 2026-08-17, both moves recorded because the second corrects the first.** It was lifted when [law-prose-restyle] was found shipped; you then decided the restyle **continues to the rest of the corpus**, which restores the holding fact. It now waits on [law-prose-restyle-remaining-docs].

**Re-count before starting rather than trusting the ~707 figure above:** the shipped pass covered `skill-nonspecific-rules.md` only, taking "session" there from 61 occurrences to 9, so the remaining weight sits in the procedure docs, the FAQ and SPEC.

**Why the existing survey is not enough.** [terminology-corpus-audit] enumerated collocations, not occurrences — a floor on how many meanings exist, never a ceiling — and never reached the FAQ or SPEC, which are the consumer-facing texts. The scale is measured: across five procedure docs, bare forms outnumber qualified ones by roughly nine to one — 134 bare against 29 qualified — so 134 judgment calls rather than substitutions sit in those files alone.

Blocked by: [law-prose-restyle-remaining-docs]

#### Rename every occurrence of "session" that means a run, per the audit's classification [session-vocabulary-corrections]
Filed 2026-08-17 from the same settlement. **The corrections pass, which cannot start without the audit's line-by-line list.**

**What changes.** Each occurrence the audit classified as meaning a run is reworded to say run; each classified as the chat or as correct is left untouched. The stop-list is honoured rather than re-derived.

**Scope includes the code, which is a different case.** `session_id` names the chat and is the harness's own field, so it is not renameable; what is ours is the variable names, the comments and the `_build-<session_id>.md` filename — and that filename is parsed by `pre_tool_use.py`, so changing it is a hook-enforced-format change whose ripple is traced by grep first. The code is not the loose-usage case settled by [work-item-term-in-hook-and-script-code]: there the code used a term loosely for the same thing, here it uses the word for a different thing.

Blocked by: [session-occurrence-audit]

#### [user] Discord post: how much stronger a session is from its start once /plan opens by reading recent LOG index lines [discord-post-session-start-strength]
Captured by you 2026-08-11. Your point, rendered in Claude's words rather than quoted: before, it felt shaky for the first few items; starting with log-awareness plus some maybe-relevant context massively boosts the start of sessions. The angle is yours; the correction below is Claude's.
**It cannot be written yet, which is why this is a queue item rather than a draft.** You asked believing the feature was live. It wasn't: `plan.md`'s Step 1 reads QUEUE.md and SPEC.md only, and its three `LOG/index.md` mentions are targeted lookups — has this been decided — not an orientation read. The feature is [plan-reads-recent-log-index], held below the line behind [index-line-length-proportional-cap].
**Your experience was real; the mechanism you credited was wrong.** What steadied that session was the below-line revisit reading LOG to check two blockers, plus the previous session's forward advisory naming where to start. Both live; neither is the five-recent-lines read. Worth carrying into the post — "the thing that helped wasn't the thing I thought" is the better story.
**The post's content, to draft when it ships.** The shaky-first-items problem and its cause; what the orientation read changes; and the honest scope — it doesn't carry all necessary context, it sets upcoming work against past work. Include the cost bound, since it's why the feature waited: five index lines is an unbounded read until index lines are capped, which [index-line-length-proportional-cap] fixes.
**Constraints:** 2000 characters, the Discord limit. Not posted until *everything* the post describes has shipped — standing rule in `CLAUDE.md`, adopted 2026-08-11.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside the limit. 3. You say what to change. 4. You post — Claude has no route to Discord. 5. You confirm, and the line closes.
**Unblocked 2026-08-13.** [plan-reads-recent-log-index] shipped — `LOG/2026-08-12-plan-reads-recent-log-index.md`; /plan's read-state step now opens with the five newest index lines. Ordinary ready work. Fourth item found sitting behind a shipped blocker; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: third in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone holds it. It lifts when [discord-post-cycle-awareness] is posted and closed.
Blocked by: [discord-post-cycle-awareness]

#### [user] Correct and post the announcement about rationale moving out of operative rules — the draft tells readers the why lives in session logs they can't reach [announcement-rationale-split-correction]
Captured by you 2026-08-09 — split out of [rationale-relocation-invisible-to-consumers] when that capture was deleted as otherwise satisfied. The 2026-08-09 Discord draft says the reasoning "lives in the session logs where you can go and read it." False for every reader not developing the method: the plugin package ships neither `LOG/` nor `resources/`. Posting it as written points users at something they cannot access.
**Why this is the user's line:** Claude can draft the correction; only the user can post. Under the capability test, drafting is Claude-work and posting is not.
**Walkthrough:**
1. Claude drafts the corrected announcement, replacing the session-logs claim with the actual split: why the method behaves a certain way is in the shipped FAQ; why a rule is worded as it is stays in the development log.
2. The user says what to change.
3. The user posts it.
4. The user confirms; it's recorded and the line removed.
Rough draft, to sharpen at step 1 — the announcement's other content wasn't reviewed, so check the whole thing, not only the false sentence. Also decide at step 1 whether it's still worth announcing, given the week that has passed.
**Paced 2026-08-14 on the user's decision: last in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Last because it corrects an already-posted announcement rather than being news, so it yields to the three new posts. It lifts when [discord-post-session-start-strength] is posted and closed.
Blocked by: [discord-post-session-start-strength]

**Files:** none — the artifact is a Discord post. Relates to [self-authoring-rules].

#### [user] Discord post: the ordering ladder cut from six rungs to three, and every rung now costs no judgment [discord-post-context-adjacency]
Captured by you 2026-08-12; the angle is yours — the ladder and how much it improves the workflow. **Subject replaced 2026-08-15 — see the correction below. The slug is unchanged because slugs are immutable.**

**The subject this post had was deleted before it was ever posted, and that is the correction.** It was written to announce the cheap-to-settle rung — "/plan offers you the work closest to what this session has already read". Commit `0e62afe` on 2026-08-15 cut the ladder from six rungs to three and deleted that rung, the rung-6 offer and the decay rung with it. The item was sitting **cleared to run** when found, so a /next run reaching it would have walked you through drafting and posting a public claim about a mechanism that no longer exists. Caught by reading the item during processing; the digest's placement check matches a fixed set of known phrases and does not reach this shape, which it says of itself.

**The replacement subject is the deletion, and it is the better post.** Six rungs became three: an uncleared red flag, then unblock-potential by citation count, then longest-first by line count. **Every surviving rung either reads a field the digest already computes or subtracts two line numbers**, so ordering costs no judgment at all. Longest-first was also re-grounded — on cost-of-reading rather than on length predicting how finished an item is, because the settling session's own data contradicted the latter.

**What makes it worth saying rather than a changelog line.** The honest version is about subtraction: three rungs asked Claude to weigh something, and weighing is where a mechanism quietly stops being reproducible. The tool got simpler and more predictable in the same move — a harder and more interesting claim than "we added a feature".

**A judgment for you at drafting time.** The before-picture is that some deleted rungs were things this project built, used, then decided were not carrying their weight. Whether that goes public is your call; it is what makes the change legible rather than arbitrary.

**Verify before posting, not merely before drafting.** Every claim must be true of the *installed* plugin at the moment it goes out. Compare the installed host's build stamp against the target's before you post, since the cut is committed but a host that has not been reinstalled still runs six rungs.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [ladder-rung-for-context-adjacent-items] shipped and has since been refined once — the offer now leads with a recommendation rather than a flat menu (`LOG/2026-08-12-context-adjacency-offer-is-a-flat-menu.md`, `e5d169b`). Draft against the refined behaviour. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries], which absorbed the item recording this.

**Paced 2026-08-14 on the user's decision: head of a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Nothing here is unready — pacing alone held it. **The framing was repaired 2026-08-18** — it read "Her words:" over a paraphrase, which is a quote claim the text cannot support, and the three sibling post items carry the hedged form. Found by the tersification write-up's own §7, which predicted exactly this upgrade.

**Correction, 2026-08-15, in the user's own words: no post went out on 2026-08-14, "because it wasn't presented to me in next."** This item's earlier claim that she had already posted that day was wrong, and so is the same claim in [announcement-cadence-clear-to-resume]. What happened is worse than a delay: holding the item below the line made it invisible to /next, so the pacing did not slow the post down, it stopped it happening at all. That is the failure [held-items-invisible-during-normal-use] describes, observed live.

**Lifted 2026-08-15.** The holding fact — a day has passed since the last announcement — is true regardless of whether one went out on the 14th, and more clearly true if none did.

**Held again 2026-08-19, on your instruction, and its subject has now been overtaken a second time.** The post announces a ladder of three rungs where every rung costs no judgment. [decay-rung-unreachable-in-practice] was settled the same day and replaces that ladder with four rungs — an intersection rung and an alternating one — so the claim survives only until that work ships. **Posting it first would have announced a mechanism this project had already decided to replace**, which is [repeal-falsifies-a-posted-claim] happening rather than being guarded against. [discord-post-cycle-awareness] took the head of the chain instead.

**Waiting improves the post rather than merely deferring it.** The honest subject becomes the whole sequence: six rungs cut to three, then the bottom rung found to be unreachable in practice and the ladder rebuilt so it cannot starve. A mechanism got wrong twice and corrected in public is the register that has worked here before. **Rewrite the subject when this lifts — it will be the third.**

**Blocker repointed 2026-08-21, and the old one is resolved rather than merely replaced.** [decay-rung-unreachable-in-practice] has shipped and been confirmed, so the fact it named is gone — but the post is still held, by the one-a-day pacing chain, and [discord-post-cycle-awareness] sits at its head unposted. The field named a fact that had resolved instead of the fact actually holding the work, so every below-the-line revisit read this item as ready to lift and every one of them was wrong. Repointed at the item that genuinely holds it: the post now lifts by itself when the one ahead of it goes out, and no session has to remember today's reasoning. Claude's decision, deferred to by you. The subject rewrite is unaffected and stays required — see the paragraph above.

Blocked by: [discord-post-cycle-awareness]

## Unprocessed

#### Last session advises running the freeform conversion before any build run [forward-advisory]
Only six of the twenty cleared items carry a build block, and a cleared item without one cannot be built — the run halts on it as underspecified. So a /next run starting now builds the two items filed this session and then stops at the first item lacking a block, which is the next one down.

[convert-cleared-items-to-build-blocks] is the work that fixes it, and it is `[freeform]`: done by hand with you present, not run from the queue. Its first step is yours — open `.throughliner-format-epoch` and change the single character `4` to `3`, because the scope-lock refuses that write to Claude in a freeform session exactly as it did at the last close.

Running it before [setup-migration-gate-is-epoch-3-shaped] ships is deliberate: this queue is the only test the epoch-4 checklist gets before that gate sends it to every consumer project.

#### Show-first approval moments produce their text twice [approval-flow-token-doubling-simplification]
Captured by you (2026-08-01) while reviewing your Claude Code feature request anthropics/claude-code#77134. Rescoped at your direction 2026-08-13 from a larger item about approval-time doubling generally.
**The cost, narrowed to where it still exists.** Showing text in chat and writing it to a file are both the model producing those tokens, so text doing both is produced twice. That used to hit every approval moment; it no longer does — write-first shipped, and the post-write report is one line naming what landed, never a re-paste.
**What remains is the show-first set only** — the moments write-first deliberately keeps showing first, because the previous version isn't recoverable without the user: a commit message, anything leaving the machine, a wholesale conversion of a document the user already owns. There the text is composed in chat, approved, then produced again to be used.
**Why it is not buildable yet.** The saving needs the harness to surface an already-produced Write's content verbatim with no second model pass — issue #77134, which hasn't landed. Until it does there's no build to describe. Re-examine when the issue ships.
**Two things settled, not to be re-opened here.** The write-first ordering flip is decided and shipped. The convergence note about view-in-doc machinery is spent — working-mode field, Editor field and line-anchored-link promise all retired 2026-08-09.
External dependency: anthropics/claude-code#77134.

**Checked 2026-08-19 and still open** — filed 2026-07-13, labelled `enhancement`, `area:cost`, `area:tools`, `area:core`, no maintainer response and no close date. The disposition is unchanged: nothing to build, re-examine when it ships. **What the check buys is that the next session reads a date rather than re-running the lookup**, which is the whole reason it is written here.

**Two things in the discussion are worth having when this does become buildable.** A comment dated 2026-08-01 sets out the mirror direction — author-in-chat, approve, then write — and argues it needs no second primitive, because a workflow that can show a Write's content verbatim can adopt write-first ordering and get the same saving so long as rejection reverts. That is this project's shipped model described from the outside. **It looks like yours, on the date and the reasoning, but nothing in the record here says so — worth confirming rather than assuming.** A later comment proposes generalising the primitive to `show_file(path, range?)`, which would also let Claude surface parts of *existing* files without re-emitting them — that reaches the view-in-doc pointer and the inline-text offer, not just the three show-first cases, so it would widen this item rather than merely unblocking it.

**Surfaced 2026-08-19 by the decay rung, on its first firing since the interleave was adopted.** It had been the oldest entry in the queue at 17 days and nothing in the ladder had ever reached it.

**Skipped again 2026-08-19, and it is the item that produced the fix for its own condition.** Presented, found unchanged, and in being presented it made the pattern visible: three entries in one session waiting on something outside this project, none able to name a blocker, all re-offered every session. That is [not-before-reaches-unprocessed], kept and cleared in the same session. **This is its first candidate** — once `anthropics/claude-code#77134` ships, or a date is worth guessing at, the field goes here and the re-offering stops. Until the field is built there is nothing to write, so the skip stands.

#### The filing-claim hook fires on a slug that was only cited, not filed [stop-hook-fires-on-cited-slugs]
Filed 2026-08-13 by Claude from a live instance in this /plan session, after the last committed close, so it belongs to no committed session record.
**What happened.** A message cited `[nothing-runs-the-hook-tests-at-a-close]` while reasoning about an already-built item — quoting a planning entry's kept-list and naming that item's LOG file. The stop hook read the slug as a filing claim, found no matching `#### ` heading in QUEUE.md, and blocked with "the write did not happen". Nothing had been written, and nothing was meant to be.
**Why the detector cannot tell them apart as written.** A slug in square brackets is the method's only cross-reference notation, and the always-loaded rules positively require citing other items by slug in prose. So the hook's signal — a slug in a message — is present in the ordinary compliant case as well as the failure case. Not a tuning miss; the two shapes are identical at the level the detector reads.
**This is the second recorded shape, and the pair is what makes it structural.** [stop-hook-fires-on-drafted-not-filed-captures] records the hook firing on a capture presented as a draft for approval, also a shape the method specifies. Both fire on conduct the rules mandate.
**A harder case the fix must survive:** an item genuinely built this session is absent from QUEUE.md for the correct reason — /next consumes it — so absence can never on its own mean a write was missed.
**One thing to check rather than assume:** whether the detector distinguishes a slug in a reporting sentence from one in a citation, and whether it can consult LOG filenames before concluding a slug is unfiled. Relates to [stop-hook-fires-on-drafted-not-filed-captures] and [disposition-detector-is-format-brittle].

**Two further instances, 2026-08-17, both in one planning session and both on SHIPPED work.** The hook fired on [rename-to-throughliner] and again on [law-prose-restyle], each cited as work already built and therefore correctly absent from the queue — /next consumes an item when it builds it. Each cost an exchange. **This sharpens the fix rather than only adding weight:** in both cases a LOG entry named after the slug existed, so consulting `LOG/` before concluding a slug is unfiled would have suppressed both, and that is the check this item already suspected. It also confirms the harder case named above is the whole difficulty — absence from the queue cannot mean a missed write, because the successful case produces exactly that absence.

**A fifth instance, 2026-08-21, reported by a consumer project on 1.20.0-test12, and it names a site the earlier four did not.** The /plan checkpoint requires presenting the next queue item verbatim. Where that quoted text happens to mention another item's slug, the hook reads the mention as a filing claim, fails to find the named item in QUEUE.md, and blocks the turn demanding an explanation. In their case the quoted item referred to work that had shipped and was recorded under its own LOG entry, so the reference was correct as written. **This makes the defect recurrent rather than occasional for any queue whose items cite each other** — which the method actively encourages, since cross-references are supposed to be written as slugs in prose, and the checkpoint quotes an item at every single pick. Their cost note is the same one this item already carries: the recovery is a correction addressed to the user about something that was never wrong.

#### The project's two Claude Code config files point at a folder layout that has not existed for months [claude-config-points-at-dead-layout]
Filed 2026-08-13 by Claude during the identity-rename build. Filed after the last committed close, so it belongs to no committed session record.
**What was found, and it is not what the rename item predicted.** [rename-to-throughliner] listed `.claude/launch.json` and `.claude/settings.local.json` among the files the folder rename would invalidate. Neither was, because neither pointed at `plugin/si-plugin`. They point at a much older layout — a top-level `sovereign-implementer/` folder with `planning/`, `build-log/` and `Dev/Resources/` — under a user path (`C:\Users\Alex\...`) that is no longer this machine's. That folder hasn't existed for a long time.
**What this means in practice.** `launch.json` declares one dev-server configuration serving `sovereign-implementer/crash-course`, an absent directory, so it cannot start. `settings.local.json` carries roughly fifteen permission allowlist entries naming absolute paths into that dead layout; a permission entry for a path that cannot occur never matches, so they're inert rather than harmful. Two live entries in the same file *did* name the real `plugin/si-plugin/scripts/reorder_queue.py` and were corrected in the rename build.
**Why it is captured rather than fixed there.** The rename item's work is the identity change, and none of this is that — the strings were stale for an unrelated reason, before the rename started. Fixing them means deciding what `launch.json` should serve now, or whether the project needs one, which is a decision rather than a substitution.
**To settle at processing.** Whether `launch.json` is deleted or repointed; whether the dead allowlist entries are pruned (harmless, but they make the file hard to read, and this user's stated difficulty is scanning dense lists); and whether anything else in `.claude/` assumes the old layout.
**Files (rough):** `.claude/launch.json`, `.claude/settings.local.json`. Host-only — a consumer's `.claude/` is their own.

#### The superseded-research flag cannot tell a citation of the fallen part from a citation of the surviving part [superseded-flag-has-no-section-granularity]
Observed 2026-08-13 while filing [written-deliverable-length-unaddressed], which cites `instruction-file-bloat-and-subtraction.md`. The digest flagged it correctly by its own rule, and for this item it was a false alarm.
**A `Superseded by:` line can say the file fell only in part, and this one does.** `instruction-file-bloat-and-subtraction.md` records that §1's instruction-count figure was re-validated and found roughly an order of magnitude too tight, and that its other sections "stand". The item that triggered the flag relies only on the subtraction argument, which survived.
**The flag has no way to know that, because it matches on the filename.** An item citing a surviving section is flagged exactly as loudly as one built on a fallen premise, and telling them apart needs a human to open both documents.
**Why this is worth more than a shrug.** A check that fires on correct work is the failure mode this project has named twice — at the repealed index-line cap, and in the standing rule that a check which over-claims makes the corpus look guarded when it's only partly guarded. The same applies to over-firing: a flag that is usually a false alarm gets learned past, and then the real one is skimmed too.
**The mitigation used this time, offered as a possible shape rather than the answer:** the item's prose now names which section fell and which it relies on. That's a convention, not a mechanism, and nothing enforces it.
**To settle at processing:** whether the fix is a convention (an item citing a partly-superseded file states which part it rests on), a format change (`Superseded by:` naming sections, and the digest reporting them), or nothing at all — the flag's text already says it is a prompt to re-read the premise rather than a verdict, so this may be working as designed. Weigh doing nothing seriously; it is a real candidate.
**Files (rough):** `plugin/throughliner/scripts/queue_digest.py`, and `skill-nonspecific-rules.md`'s superseded-research paragraph. Shipped.

#### Clearing a conversation does not cancel a slash command queued behind it, and nothing says so [clear-does-not-cancel-a-queued-command]
Filed 2026-08-13 by Claude at its own /done close. Captured by you in substance — you asked mid-run whether Claude had seen the `/clear` you ran from remote control, having reasonably read the clear as cancelling what followed.
**What happened.** A `/clear` and a `/next` were sent together. The clear wiped the conversation; the `/next` behind it ran normally against an empty context. From your side the old text was still on screen, so it looked as though the clear had been ignored — when it had been honoured exactly, and the scrollback you could see was the app's, not Claude's context.
**Why it is worth a queue line.** Nothing in the method or the app says a clear is a context operation and not a queue operation, and both readings are natural. The cost is real: a `/next` immediately after a clear starts a build with none of the planning conversation behind it — exactly the fresh-short-session case the method designs for, but only if the user *meant* it.
**To settle at processing, and the routing is genuinely open.** This may be Claude Code's to fix, in which case the destination is a GitHub issue rather than a build. What is plausibly ours is smaller: /next's opening could say, where the context is visibly empty of prior discussion, that it is starting cold. Weigh whether that is detectable at all first — Claude cannot reliably tell an empty context from a forgotten one, the same blindness recorded in the wind-down re-scan's caveat.
**Files (rough):** none decided. Relates to the fresh-short-session design target in `CLAUDE.md`.

#### There is no way to tell where you are in a long processing run [no-position-signal-in-a-processing-run]
Captured 2026-08-14 at a /plan close, from the user losing her place live. Her words across three turns: "what is going on did we resolve the last item into work or not", "in the middle of what item? what item are we on? that's all I'm asking", and "then what was all that stuff you just did!".
**What happened.** Ten items in one session. Each produced several turns of discussion, and several produced side-work — a reply drafted and delivered, a capture filed mid-item, a rule gate opened, references repaired after a delete. From outside, side-work is indistinguishable from work on the item, so a single-word instruction like "delete" was followed by four further exchanges and the user could no longer tell whether the item was resolved, what item was current, or whether anything was open.
**A running count is NOT the fix, and this capture's first draft had it backwards.** It claimed the count was stated once at the start and never again, and offered a running position line. The user corrected both at the close; her correction, rendered in Claude's words rather than quoted: the count was in fact being stated at random points through the run for no apparent reason, it has since gone, and it is better gone. Claude had been emitting unprompted tallies — "that's five items processed and two skipped" — at moments no procedure asks for, noise dressed as orientation. Recorded rather than quietly amended, because a running counter is the intuitive fix and would otherwise be re-proposed by the next session to read this.
**What is actually missing is narrower.** Not how many items, but whether the item in hand is finished and whether what Claude is now doing still belongs to it. All three of her questions were that question, never a request for a total.
**What to weigh at processing.** Whether side-work should be announced as side-work when it starts, so a stretch of tool calls after a one-word instruction reads as "still finishing the delete". Whether a plain "that item is closed" line at the moment an item ends would do it. Neither should reintroduce a tally. Relates to [concision-build-removed-the-asks], [subset-done-has-no-stated-shape] and [claude-md-vocabulary-is-unexplained] — all four are the user unable to read her own position from what the session says.

#### A user has no answer to what happens when Claude deletes something from their queue [no-faq-entry-on-deletion-and-recovery]
Captured 2026-08-14 at a /plan close, from the user asking mid-session what git history does and what was happening to her queue. She is the method's most experienced user and still had to ask.
**The gap.** Deleting a work item is a routine, approved planning move, and the method's own reasoning leans on deletion being safe because git history keeps the text. That premise is never explained anywhere the user reads. A non-coder approving a delete is being asked to agree that something isn't worth doing, with no way to know whether "delete" means gone.
**Why it is not covered.** The FAQ has entries on the workflow's moving parts, none on what deletion does or how anything is recovered. SPEC states that git history keeps a deleted item, but SPEC is product truth, not user help.
**What to weigh at processing.** Whether one entry covers it or two — deletion specifically, and the general "is anything I approve ever unrecoverable" — and whether the answer names a recovery command or simply says to ask Claude, which is the honest route for a user who doesn't use a terminal. Ships to consumers, so an ordinary FAQ entry rather than host-only. Relates to [own-faq-diverged-from-shipped-template] — decide which FAQ the entry lands in before writing it.

#### EDITING-STATE-CONTRACT.md has a live consumer, no maintenance trigger, and an unexamined justification [editing-state-contract-status]
Captured by you 2026-08-14, mid-/next, from your proposal to delete the file. Filed after the last committed close, so it belongs to no committed session record. Three questions, yours, kept together because they are weighed against each other.
**What was established before the questions, so they are not re-derived.** Your premise was that the document is vestigial material from when MANIFEST was a doc. It is not: it documents a shipped feature — `pre_tool_use.py` writes a marker before every editing-tool call and clears it after, `session_start.py` sweeps stale ones — and it has a live consumer. that consumer project's `src/main.js` (around line 264, under "Throughliner's editing signal") reads `.throughliner/`, scans every `editing-*.json` rather than one file, applies the published reader rule that editing is happening if any marker is active and fresh, and reads the `producer` field with `throughliner` as its fallback. An archived message in that consumer project's INBOX shows the v2 format change was communicated deliberately.
**But a live consumer does NOT put a delete off the table, which is your correction and it defeats this capture's first version.** Claude wrote that it did; you pointed out that what that consumer project has is *code* that reads the markers, and that that consumer project's Claude can read the hook that writes them. That is the stronger source in every respect: `pre_tool_use.py`'s marker-writing function **is** the format, so it cannot drift, while the document can and has nothing checking it — question 2 below. The document would only be load-bearing if that consumer project couldn't reach this repository, and it can: sibling folders on the same machine, and the v2 change in fact travelled by INBOX message rather than by anyone reading the contract. So a delete is live, and question 3 is now most of the answer.
Your other point stands untouched: users will not read it, and it is not written for them.
**Question 1 — does the dependency get to be visible from both ends?** Today the citation runs one way: this project publishes a contract and doesn't know who consumes it, and that consumer project's code names the format without anything on this side recording that it does. Same one-way-citation shape the superseded-research rule was built for, one project apart. A pointer from that consumer project's side, or a note here naming the consumer, would make a v3 change reach the code that depends on it. Weigh against the standing rule that this project doesn't scan other projects — any pointer is something a person writes, never something a session goes looking for. **This question survives a delete and may be the only part that does:** knowing who reads the markers matters whether the format is documented in prose or read out of the hook, and it's the one thing neither the code nor the document records.
**Question 2 — when does it get maintained, or is it quietly decaying?** Your question, put here in Claude's phrasing. There is no trigger of any kind: not in the rule gate's path list, not in the board's growth report, not in the FAQ-sync trigger, and no close reads it. The hooks could drift from the published format and nothing would say so — the exact shape of the output-style failure built earlier in this run, where an always-loaded layer sat outside every watcher and an underived number reached it in silence. Note a conformance check here is mechanically possible in a way most of this method's checks are not: the fields the hook writes are literal strings, so a test could assert the marker matches the document.
**Question 3 — is a published interface contract standard practice, or our own invention? This is now the load-bearing question.** Yours, and with the consumer objection defeated it carries most of the decision. If it is standard practice, defended by sources, it stays and gains a trigger. If it is our invention, it duplicates what is already in the repository in executable form — the hook code *is* the format, Claude can read it, and it cannot drift the way prose can — and this project has spent this session removing second copies. Your words for why the code is the better source: it is probably way more accurate too. **This turns on an external fact, so it needs a web search rather than a judgement here** — whether published field-level contracts for local file-based signals are a recognised practice, and what maintains them where they are.
**Files:** unknown until question 3 is settled — possibly `EDITING-STATE-CONTRACT.md` (deleted, or gaining a maintenance trigger), `CLAUDE.md` and `resources/rule_signals.py` (if it gains one), `resources/testing/` (if a conformance test is the answer). Host-only in every branch. Relates to [rule-lifecycle-board-has-no-trigger] and to the superseded-research one-way-citation problem.

#### The two-limb keep check pushes research into build items, beating the rule that says research is done in planning [research-packaged-as-build-work]
Captured by you 2026-08-14, from a live instance in another project minutes earlier: a planning session proposed splitting an item into "one build item where I do the research and write the findings into `resources/research/`" plus a slimmer `[user]` line. Your framing is the finding — research is never planned into work items, and if research can be done now in /plan then it is. **You also observed this is suddenly happening a lot, which is what the diagnosis below explains.**
**It happened three times in one day.** Twice in this session — research queued into [faq-entry-criteria], and research folded into [shipped-spec-maintenance-rules] — and once in the other project. Both of this session's instances were corrected on your instruction; the SPEC one needed no research at all, because `resources/research/spec-document-standards.md` already answered it.
**Nothing was deleted, and the rule is intact.** `plan.md` still carries "/plan resolves what it can in-session; capture is only for what it can't", with `research` listed first among what /plan resolves now. The defect is not a missing rule.
**Three things make it lose, and the third explains the timing.** It is not stated as a rule about research — it is one word inside a fenced list of six, so "research belongs in planning" must be inferred. It is hedged by the sentence immediately after, "A default, not an absolute", a standing licence to make the exception. And the keep-check pushes the other way with far more force.
**The mechanism, which is this capture's substance.** To keep an item, `plan.md` requires stating the build in both limbs — which files change, what changes inside them — and calls it blocking. When the answer isn't yet known, the cheapest way to pass both limbs is "research X, then change Y", which reads as a fully specified build. So the check that exists to keep undesigned work out of Processed is the same check that rewards packaging research as build work. It fires hardest exactly where the answer is unknown, which is where research is needed.
**The timing, confirmed from git rather than assumed.** The two-limb check was hardened 2026-08-10 in `f8b03ea`, which introduced "This is a blocking check, not a prompt to try harder", the instruction to state both limbs before recommending keep, and the warning that a bare file list is what undesigned work looks like. Before that it existed in a softer form; after it, a keep can be refused. Four days later the pattern is visible across projects. An earlier `git log -S` attributed the change to `989c38b` — a false positive, since `989c38b` is the rename that moved the whole package folder and shows every string as newly added. Recorded so the trace isn't run twice with the same wrong result.
**What this is not.** Not a case for weakening the keep check. It stopped undesigned work reaching Processed, a real failure with real instances. Two correct rules were put into conflict and the stronger won.
**The shape of the fix, to settle at processing.** The clause belongs on the keep check itself, where the pressure lands, not on the research bullet, which is already there and already ignored: an item that cannot state its build *because the answer is not known yet* routes to doing the research now, in this session, and only what /plan genuinely cannot resolve is captured. Weigh also whether "A default, not an absolute" should go — it is the sentence that licenses the exception, and by this project's standard a rule qualified into a default loses every contest.
**Files (rough):** `plugin/throughliner/docs-b/plan.md` — the keep-check sub-step, and the resolve-now block's hedge. Shipped, not host-only: this fires in every consumer's planning session, and the prompting instance was in another project.

#### The Claude Code GitHub app cannot be installed for an org from the flow that demands it [claude-code-github-app-org-install-dead-end]
Filed 2026-08-14 by Claude at the wind-down re-scan. **The observation is the user's, from hitting it live while trying to start a cloud session; the diagnosis is Claude's.**
**What happened.** Starting a cloud session against an org-owned repository popped "GitHub app not installed — the Claude GitHub app must be installed on your repository". The app *was* installed, on the user's personal account. Its "Install GitHub app" button led to the personal account's app settings page, which offers no route to install for the organisation that owns the repo. The org's installed-apps page showed none, and the GitHub Marketplace returned no results for Claude Code. The only working route was the direct URL, `github.com/apps/claude`, which nothing in the flow mentions.
**Why it is worth reporting rather than just fixing locally.** A non-coder hits a popup that contradicts their settings page, follows the button it offers, lands somewhere that can't resolve it, and has no next step. The user is a non-coder and did stop. By the three-way routing test this is Claude Code itself, so it belongs as a GitHub issue on `anthropics/claude-code`, not as a method capture and not as app work.
**What the work is.** Search existing issues first — knowing the adjacent reports is what lets a new one distinguish itself — then draft the issue and show the exact text before anything is posted. Nothing is filed without the user's explicit yes. The account and repository names are identifying and are scrubbed or generalised in the draft.

#### A file's date in Google Drive means "last synced", not "last edited", and both you and Claude reasoned from it as if it meant edited [drive-dates-are-not-edit-dates]
Captured by you 2026-08-14 at the /done close. **The observation is yours** — you reported that two folders had both been updated today and asked which was real; **the diagnosis is Claude's.** Filed after the last committed close, so it belongs to no committed session record.
**What happened.** You read the project through Google Drive on your phone, saw `docs-b/` and `skills/` both showing as modified today, and reasonably concluded both were live. The filesystem and git disagreed: `skills/` was last written 2026-08-13, three of its four files on 2026-08-10, with no modification in git and no commit since the rename build. The whole project sits inside My Drive, so a sync pass or re-upload refreshes what Drive displays without any byte inside the file changing.
**Why this is a method finding rather than a one-off.** You work from Drive on your phone routinely, so it will recur, and it produces a report that is honestly made and factually wrong — the worst kind for Claude to receive, because nothing about it looks uncertain. Claude then took it at face value and answered the wrong question twice before checking the filesystem, costing several exchanges and visible frustration. The general shape: **a file browser's presentation is not evidence about a repository's contents, and both parties treated it as if it were.** Third instance in one session, after `throughliner.zip` looking live in Explorer and again looking dead to the fix.
**The likely fix, to settle at processing.** Something small on the handoff-claim provenance rule, which covers Claude-authored claims but not user-reported file state: where the user reports that a file changed, was updated, or looks new, check `git log` and the filesystem before reasoning from it — and say what was checked rather than contradicting her flatly. Weigh whether this belongs in the always-loaded rules or in this project's CLAUDE.md, since it is about how *this* user works. The asymmetry is what makes it worth having: checking costs one command, not checking cost this session several exchanges.

#### A working file's `Depth:` lines are not bound to their items, so two written together silently attach to the wrong one [depth-field-has-no-binding-to-its-item]
Filed 2026-08-14 by Claude at the /done close, from a slip in this session's own build working file. Filed after the last committed close, so it belongs to no committed session record.
**What happened.** The `Depth:` field is written under an item's Progress tick, and its binding is positional — nothing names the item it describes. Two items were ticked in the same edit and their depth lines landed together, so `[setup-mid-session-is-unhandled]` carried two and `[spec-ask-in-build-reads-as-a-violation]` carried none. The close spotted it and read the second line as belonging to the second item, almost certainly right — but that was a reconstruction from context, not something the file recorded.
**Why it matters more than it looks.** `done-build.md` instructs the close to read each item's depth field rather than judge it, and to treat a missing field as short while noting the omission as a discipline slip. Both are defeated here: the field wasn't missing, it was misattached, so "missing means short" would have written the wrong form of entry for one item and the slip would have been reported against the wrong cause. A fresh short session — the design target — has no conversation memory to reconstruct from and would simply have believed the file.
**The likely fix, to settle at processing.** Bind the field to its item explicitly — `Depth: <slug> — short` — so position stops carrying meaning, the same principle the queue applies in refusing to let position encode a relationship. Weigh the cheaper alternative of instructing the close to flag any item whose depth-line count is not exactly one, which detects the fault without changing the format. Relates to [tick-conflates-built-and-confirmed] and [close-cost-scales-with-run-size].

#### An outbound report can describe a problem that was fixed days earlier, because nothing requires a live check before sending [outbound-report-not-checked-against-the-world]
Filed 2026-08-14 by Claude from inbound INBOX mail (`2026-08-14-report-page-already-live.md`), opened and archived during a /next pre-flight. Filed after the last committed close, so it belongs to no committed session record.
**What the message says.** The flintcraft.tech project reports that `flintcraft.tech/report` has been live and working since 2026-08-06, when the site was connected to Netlify — and that two invisible Netlify defaults had to be fixed alongside it (form detection off by default since April 2023, and no email notification unless configured). Its correction: a report this project sent was dated 2026-08-09, three days after the fix, so it described a problem that no longer existed.
**Why it is a method finding rather than a one-off.** `[report-url-404]` was closed correctly on 2026-08-10 by fetching the URL — check-the-world working as designed. The gap is *outbound*: the walk-through lifecycle requires an observable check before recording a `[user]` item complete, but nothing requires the same before sending a report to another project. So the strong rule guards closing work and the weak path guards sending claims, which is the wrong way round: a wrong close costs one queue line here, a wrong outbound report costs another project's time.
**The likely shape, to settle at processing.** One clause on the outbound-send flow in `feedback-and-inbox.md`: where a report's claim has an observable check — a URL, a file, a branch — run it at drafting and say in the report what was observed and when. Weigh whether this is the walk-through's check-the-world clause extended to a second site, in which case it's an amendment and spends no slot.
Relates to [cross-project-work-completes-invisibly] (the same blindness in the other direction) and [report-url-404] (the instance).

#### A reversibility claim settled at processing was never checked against the world, and the build hit the exception [processing-asserts-reversibility-without-checking]
Filed 2026-08-14 by Claude at its own /done close, as a testing outcome from using the plugin to build the plugin. Host-only in its example, general in its shape.
**What happened.** [delete-codex-port-from-history] was settled at processing with a careful paragraph choosing the cheap operation over a history rewrite, recording that the cheap one "is also the reversible one" because dropped commits stay recoverable from the reflog until garbage collection. True of commits. The worktree being deleted held 722 lines of uncommitted work across 24 files plus two untracked files, none of which is a commit and none of which the reflog holds. The build halted, surfaced it, and the user chose to discard the work after being told plainly it couldn't be recovered.
**Why the processing session could not have known, and why that is the point.** Nothing in the keep-step asks a session to look at the thing it is about to destroy. The two-limb test asks whether the item says what changes inside the files it names — which this item did, precisely. A reversibility claim is a claim about the *world*, not about the item's specification, and the method has no check that reaches it.
**The shape it shares with other findings here.** [runs-alone-premise-never-tested], built in the same run, is the same failure one layer up: a plausible sentence about what git would or wouldn't recover, written at processing, quoted forward for days, refuted the moment anyone tested it. Two instances now, both about git recoverability.
**To settle at processing, and the obvious fix may be too broad.** A rule requiring every destructive item to inspect its target before clearing would fire on a great deal of work that destroys nothing. Weigh a narrower trigger: an item whose own prose *asserts* that an operation is reversible or recoverable earns a check of that assertion before it clears. That keys on something visible in the text rather than on judging what counts as destructive.
**Do not read the build's halt as the system working.** It worked because the build happened to run `git status` in the worktree before removing it, which no step required.

#### A halt written for a non-coder used four pieces of jargon in its first sentence [halt-narration-used-unexplained-jargon]
Mixed authorship: the failure was Claude's, and you reported it in your own words — "I don't understand". Filed 2026-08-14 at the /done close, as a testing outcome.
**What happened.** A build halted to surface that a folder about to be deleted held unrecoverable work. The message opened with "the Codex port worktree has uncommitted work in it", then used *reflog*, *commits*, and *branch ref*, and offered three options in the same vocabulary. You said you didn't understand it. The second attempt — the same decision explained as "a second working copy of this same project, sitting next to it", with the loose edits existing "only as loose files on your disk" — was understood immediately and you decided in one turn.
**Why the guard did not fire.** The always-loaded vocabulary rule asks whether a term names something in *this user's* world, something you could show them. In a project whose subject matter is the method, that resolves generously — a worktree genuinely is a folder that can be opened. So the rule permitted every term. What it doesn't weigh is that a *halt* is the one moment the user has no context to lean on: the run stopped, something is wrong, and a decision is needed immediately.
**The shape to weigh at processing.** Possibly a clause on the vocabulary rule: text written at a halt or stop states the situation in terms needing no method vocabulary, because a user meeting a halt is being asked to decide rather than to follow along. Weigh against the risk of a rule that fires on every alarming-sounding moment.
**The cost was one extra turn**, which is cheap. The reason to file it anyway is that a consumer meeting the same halt has strictly less context than you do, and no way to ask a question that gets a second attempt from someone who knows the material.

#### Design the standing audit set that maintains the rule corpus once the cleanup is finished [standing-audit-programme]
**Captured by you 2026-08-14. Your instruction, rendered in Claude's words rather than quoted: design the routine audits that you will run in the future and maintain the full corpus once we're done.** The reasoning below came out of that discussion — your strategy is yours, the argument about what it can and cannot retire is Claude's, and you asked for it to be captured.

**Your strategy, recorded first because the design serves it.** Dedupe and de-contradict the corpus first, cutting the word count and therefore how much there is to process; then design the audits and edits that put the final finish on the method rules, converting them into the law-prose style; then, once the always-loaded self-authoring rules are doing their job, stop needing to run these audits at all.

**The sequencing is right and is not what is being questioned.** Deduping before restyling is correct: a restyle over a corpus holding four copies of one rule restyles it four times and creates four chances to diverge. Cutting first means each rule is rewritten once. The `done-plan.md` merge processed the same day is that shape in miniature — four items, one file, one judgment applied consistently, where deciding them apart would have answered the same question four times inconsistently.

**Where the strategy overreaches: the self-authoring rules govern ADMISSION, and audits catch DRIFT. Different jobs.** Admission asks whether a rule should exist, worded this way, in this file — it fires when someone is writing a rule. Drift is what happens to a correctly-admitted rule *afterwards*, when something changes around it and the rule is left describing a mechanism that no longer exists. **No admission gate can prevent drift, because the cause arrives after admission.** Three items in the queue at writing are pure drift and every one passed admission cleanly: [done-md-names-a-repealed-clear-step], [adopted-claude-md-describes-retired-structure], [docs-b-name-outlives-the-two-docset-model]. A perfect gate produces all three anyway.

**The harder evidence: correct wording does not make a rule fire.** The corpus documents at least four instances of an always-loaded, correctly-worded rule failing: the provenance rule, shipped and sharpened, still not holding ([invented-rationale-compounds-past-the-shipped-rule]); the file-the-blocker rule, unambiguous and explained by the user five to ten times in a month ([nothing-blocks-it-read-as-a-dead-end]); the INBOX-opening step skipped in the very session that authors it ([inbox-open-step-not-enforced]); and the subagent-cost rule broken hours after being read. The provenance item already draws the conclusion: "state the rule again, or state it harder" is no longer a candidate direction.

**A fifth instance, carried here 2026-08-19 from [build-wrote-its-own-gate-disposition] when that item was deleted as already decided, and it is the sharpest of the five because the rule that failed was the gate's own.** A build in the eighteen-item run found itself authoring a shipped rule with no disposition to transcribe. `CLAUDE.md` instructs exactly that build to halt and say so. It had the instruction, and instead ran the gate's four questions itself and recorded the result — a description of an admission decision, written by the party that had already done the work, which is the failure the /plan siting exists to prevent. The design gap the deleted item suspected turned out not to exist: [stated-open-design-question-passes-the-keep-step] shipped 2026-08-17 in `7e3c1c8` and now refuses at the keep-step any item whose prose schedules a design decision into its build. What was left was a correctly worded rule that did not fire.

**The rule board is this experiment already run.** Built on the theory that the rules could watch themselves, it reported clean while five real rule defects shipped in the same session — see [rule-board-measures-paperwork-not-health], settled the same day as keep-and-rename for that reason.

**What the strategy genuinely buys, which is substantial.** Fewer rules and no duplicates means fewer sites where drift can occur, and each future retirement ripples to fewer places. An audit over a deduped corpus costs a fraction of one over the corpus as it stands. The win is real; it is a change in cost, not in necessity.

**So the goal is reframed rather than abandoned: not eliminate the audits, but make them cheap enough to run routinely without dreading them.**

**The design test this item applies, and it is the actionable part.** What retires an audit class is a **mechanical check, never a prose rule.** The queue lint and the digest genuinely removed the need to eyeball queue structure, because code reads the whole file and cannot skim. So for each drift class, ask first whether it is mechanically detectable: if yes, build the check and retire the audit; if no, the audit stays and gets a trigger. The board's retired-terms check is an existing instance of the first kind.

**What this item must produce.** The standing set itself — which audits, what each reads, what triggers each one, and how the user runs it without needing to remember it exists. A siteless audit is the failure this project has now recorded five times.

**One risk to design around.** The law-prose restyle is itself a large authoring pass over the whole corpus, and every rewrite is a chance to reintroduce what was just cut. It should be the last big pass and should be audited *after* rather than trusted to verify itself — the party doing the restyling is the party that would certify it, which is [rule-admission-has-no-independent-approver].

**The finish line this set takes over from is already assembled**, in the session that captured this item: twenty-two remaining items in five groups plus [law-prose-restyle], with five stated finish conditions. It lives in that session's LOG entry rather than in a queue item, because it is a record to be read rather than work to be done.

**Two of the five finish conditions are already mechanically checkable** by `resources/rule_signals.py` as it stands — no live rule naming a retired term, and no near-duplicate rule pairs. That is this item's own design test paying off before the design starts: the standing set inherits two conditions it never has to audit by hand, and should look for more of the same before proposing any audit a script could do instead.

**The comparison axis is split out and settled — see [audit-axis-is-parent-not-sibling].** It was the one fully designed part of this item, so on 2026-08-15 it was split off and kept into Processed on its own: audits compare a doc against its parent rather than its sibling, and each finding names where both sites fire. That half needs nothing further from this item; the standing set inherits it as a constraint every audit it designs must satisfy.

**Not kept, 2026-08-15, and why — this is design progress rather than a rejection.** The item fails the keep check's second limb by construction: its file list is whatever its own design produces, so it can never clear to run and a build would stall on it. It also should not be designed yet on its own reasoning — the set is meant to follow the dedupe and the restyle, and audits designed against a corpus about to be rewritten are audits designed against a shape that will not exist. **The user's decision was to split rather than design it now.**

**What remains to be designed, so the next session starts here.** Which audits are in the set; what each one reads; what triggers each one, given that a siteless audit is the failure this project has recorded five times; and how the user runs the set without having to remember it exists. Each candidate audit is tested first against this item's own rule — is the drift class mechanically detectable? If yes, build the check and retire the audit rather than designing it. Two of the five finish conditions already pass that test using `resources/rule_signals.py` as it stands, and the design should look for more of the same before proposing any audit a script could do instead.

**Files: not yet derivable, which is the point of not keeping it.** Likely `resources/method-compliance-audit-checklist.md`, `resources/rule_signals.py`, and `CLAUDE.md` for whatever trigger the set gets. Host-only. Relates to [rule-admission-has-no-independent-approver] for the restyle-audits-itself risk.

**Skipped again 2026-08-17, and the blocker it waits on now exists as work.** It was presented by the ladder as the longest entry in the section. Rather than skipping it silently a second time, the decision it was actually waiting on was put to you: whether the restyle stops at the one file it covered this morning. **You decided it continues to the rest of the corpus**, so this set still follows a rewrite that has not happened — and audits designed against a corpus about to be rewritten are designed against a shape that will not exist. It follows [law-prose-restyle-heavy-docs] and then [law-prose-restyle-remaining-docs]; the ordering is written into those entries too. [law-prose-restyle] is consumed and no longer names anything in the queue, which is why it is no longer cited above. The second limb still fails by construction, so this stays a capture rather than being held below the line.

#### SPEC does not say how many commits a close makes, now that the answer is exactly one [spec-silent-on-one-commit-per-close]
Filed 2026-08-14 by Claude during the build of [close-produces-multiple-commits-every-time], as adjacent work rather than folded in.

**What the build settled.** A session makes exactly one commit — the close — and the post-commit tail commits nothing, riding into the next close. The accepted cost is that the working tree is dirty between one close and the next, always, which is what makes that dirt legible rather than noise.

**Why this is a capture and not part of that build.** Nothing in SPEC becomes false: its close paragraph says the close records and commits, and says the append offer exists, without claiming a commit count or a clean tree. So there is no contradiction to halt on and no stale sentence to correct — only an addition. The build's file list named `done.md` and the session-start hook, and adding product truth is the route that asks first, which would have stopped an unattended run for a sentence nobody is blocked on.

**What a keep would decide.** Whether the commit count and the expected-dirty-tree are product truth a consumer should read in SPEC — they will see the "uncommitted changes from a previous session" line at every session opening, and SPEC is where they would look to find out whether that is normal — or whether it is implementation detail belonging only in the close procedure. Relates to [close-produces-multiple-commits-every-time], [post-close-tail-state] and [close-cost-scales-with-run-size]. [done-delta-close] was deleted 2026-08-17 as already decided against in `done.md`, so it is no longer a relative; [rescan-appends-post-close-work] is the surviving piece of that subject.

#### A processed item carried its `Rule gate:` line twice, the second a truncated copy of the first [duplicate-gate-line-on-a-processed-item]
Filed 2026-08-15 by Claude at the close of the eighteen-item run, noticed while transcribing.

**What was found.** [move-section-does-not-report-line-crossings] carried two consecutive `Rule gate:` lines. The first read "not needed — this extends an existing report to a second code path and adds a refusal branch"; the second, the same without the refusal clause — evidently an earlier draft left in place when the item was revised. The build transcribed the fuller one once.

**Why it is worth a line.** The disposition is what two of the corpus checks read, and both take the line as authored. Two lines disagreeing about what the build does is a small inconsistency now and a wrong reading later — the truncated copy describes a narrower change than the item specified. It also suggests revision passes over a processed item append rather than replace, which would produce this again.

**What a keep would decide.** Whether anything mechanical should notice a duplicated disposition — the queue lint is the natural site and already parses work-item structure — or whether one instance is below the bar and this is a note about revising items in place. The bar question is real: one occurrence, which this project's own gate treats as insufficient for a freestanding rule.

#### The scaffolded "Project docs" section in every consumer SPEC describes the method's own machinery, and goes stale in a way no migration repairs [spec-scaffold-describes-method-docs]
Filed 2026-08-15 by Claude, from INBOX mail sent by a consumer project running this method running 1.20.0-test7. Their user noticed it unprompted while reading her own SPEC and asked why SPEC described the workflow's files rather than her product; they filed it without proposing a fix and said no reply was needed.

**The admission point.** `setup.md`'s SPEC scaffold writes a `## Project docs` section into every new SPEC.md, listing what SPEC, QUEUE and LOG each hold. plan.md's SPEC admission rule says a sentence describing how a mechanism is implemented belongs in the doc that owns it, and that SPEC names the behaviour instead. So the scaffold writes into every consumer's SPEC exactly the kind of sentence the rule governing SPEC edits forbids. Whether that section earns its place is the question; the sender proposed no answer.

**The staleness point, which the sender judged sharper and which is invisible from here.** That section copies how QUEUE.md is structured, and QUEUE.md's structure is what changes between format epochs. Theirs read "work batches and captured ideas" — the pre-recut shape — and had since the two-section change. They ran the format 2→3 migration and it correctly did not touch the line, because migration adds missing files rather than refreshing existing content. So the stale description survives every migration by design, in every consumer project, in the one document sessions are told to read as product truth. Theirs is now corrected by hand.

**Why it needs planning rather than an obvious patch.** Three candidate answers, not equivalent: drop the section from the scaffold; keep it but reduce it to behaviour rather than structure; or give the migration a refresh path for scaffolded content, which is a new capability rather than a wording fix. The first two are cheap and the third is not.

**A related check when this is processed:** whether anything else the scaffold writes has the same shape — content copied from the method into a consumer document, where the method can change and the copy cannot be reached.

#### The plan/build boundary keeps being treated as an open question across the last two planning sessions [plan-does-not-build-keeps-being-relitigated]
**Captured by you 2026-08-15, in your own words: "I don't know why this is even a question. Plan does not build. This confusion has been happening a lot in the last two plan sessions. I don't know what rule slipped in the build before that but it might need to be investigated."**

**What triggered it.** Processing [rescan-as-its-own-skill], Claude presented "does the new skill build its findings, or only file them?" as a genuinely open design question needing your decision. It is not open — the boundary is stated in the always-loaded rules, in plan.md's opening line, and in the work cycle itself. You spent three exchanges, including two where you said you did not understand the question, to get back to an answer the rules already gave.

**One concrete lead, so the investigation does not start from nothing.** The framing did not come from Claude in this session — it is written into [rescan-as-its-own-skill]'s own prose, authored yesterday, as a paragraph headed "the hard question this must answer" saying the resolution "is not obvious" and that the boundary might be "deliberately amended". A queue item authored in one session taught the next to treat a settled rule as undecided. Worth checking as a pattern: whether other items carry a settled rule re-opened as a question in their prose.

**The second thing to check is what you named** — whether something shipped in a recent build weakened the boundary's statement, or added a rule reading as an invitation to exceptions. That is a read of what changed in the always-loaded rules and the skill docs over the last few builds, against LOG.

**Why this matters beyond the wasted turns.** A boundary that gets re-argued eventually loses one of the arguments. The method holds this one firmly on purpose: it is what stops any session changing the project without the user having agreed to the work.

#### A rule-holding file sits outside the gate's trigger, so editing it summons no gate at all [gate-trigger-misses-the-audit-checklist]
Filed 2026-08-15 by Claude while writing a gate disposition, and raised with the user before writing.

**What is wrong.** The rule gate's trigger is mechanical and reads staged paths: a commit touching `plugin/throughliner/docs-b/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md`, or `CLAUDE.md`. `resources/method-compliance-audit-checklist.md` is not in that set, and its entire content is rules — the standing criteria every method compliance audit runs against. A session adding a criterion to it authors a rule, and nothing asks it to run the gate.

**How it surfaced.** [audit-axis-is-parent-not-sibling] adds two requirements to that checklist. Its gate ran because the session happened to notice; it would not have fired from the trigger. That is the failure this gate's design is against — a check depending on someone remembering is the shape the mechanical trigger replaced, and `CLAUDE.md` says so when it contrasts this trigger with FAQ-sync's undetectable one.

**To settle at processing, because the obvious fix may be wrong.** Adding the one path is a two-word change and closes this instance. The prior question is whether the trigger set should be a list of paths at all, given that a rule-holding file added later lands outside it again by default and nobody notices — exactly as this one did. A rule about which files hold rules has the same maintenance problem as the rules themselves. Whether there is a shape that fails safe rather than silent is the design question; if not, add the path and say so.

**A second instance, 2026-08-19, and it widens the question rather than repeating it.** A planning session amended a genuine rule — the no-write instruction about Taskflow, which gained an INBOX exception — living in a folder-level `CLAUDE.md` above this project. No gate was summoned, correctly by the trigger and wrongly by the subject. So the trigger misses rules held *outside the repository* as well as rules held in unlisted files inside it, and a path list cannot be extended to cover a file the repository does not contain. See [parent-claude-md-taskflow-no-write-stale].

**Also worth checking in the same pass:** whether any other file under `resources/` holds operative rules and sits outside the trigger. `retired-terms.md` and `rule_signals.py` are the obvious candidates, and both may turn out to be data and code rather than rules.

#### No test asserts that an origin claim goes unflagged, which is the whole of the provenance split [origin-claim-has-no-test]
Filed 2026-08-16 by the build of [provenance-splits-origin-from-quote], as adjacent work rather than part of it.

**What the suite covers and what it misses.** `resources/testing/test_queue_lint_flags.py` has four cases on the credit check, and all four survived the split untouched because each happens to use a quote-claim phrase alongside its `Captured by you`. So the suite still passes and still asserts only the half that did not change.

**The half that did change has no case at all:** a bare `Captured by you` with nothing quoted must now produce no warning. That is the entire point of the split — it is what stops Claude asking the user to prove her own work is hers — and a later session could restore the old phrase list with every test still green.

**Files:** `resources/testing/test_queue_lint_flags.py` — one case asserting a bare origin claim is not flagged, and one asserting a quote claim still is.

#### The build working file's Changes section falls behind its ticks, and only the ticks are enforced [changes-section-falls-behind-the-ticks]
Filed 2026-08-17 by Claude at its own close, from the reconcile against memory that `done-build.md` requires.

**What happened.** Across a twenty-six-item run, every item was ticked with a depth field and an index-entry candidate at the moment it completed — those three are named at the per-item completion step and all three held. The `Changes:` section did not: it carries per-file notes for roughly the first three items and the end-of-run summary, and almost nothing for the twenty in between. The gap was found by the close's reconcile, not by anything mechanical.

**Why the two behave differently.** The tick, the depth field and the index candidate are enumerated as a numbered set at one step, and the close reads each of them — a missing depth field is explicitly called a discipline slip. `Changes:` is described in `next-build.md` under "accumulate close notes as you go", with no step that reads it back and nothing that notices when it is thin. It is the one part of the working file whose absence costs nothing at the moment it is skipped.

**What it costs.** `done-build.md` sources each entry's `Files touched:` line from this section. With it thin, the close reconstructs the file list from memory of the run — which works in a chat that still remembers, and is exactly what fails in the fresh short session this method designs for. A crash mid-run would have left a working file that understates what was done.

**What to weigh at processing.** Whether `Changes:` joins the per-item completion set as a fourth required write, which is the shape that already works for the other three; or whether the close should read it against the ticks and flag a mismatch, which catches it later but costs nothing during the run. The first is more writes in the run, the second is a check at the one moment the information is already being reconstructed.

**One thing not claimed:** nothing was lost this time. The entries were written from a chat that still held the run, so the record is accurate — this is a defect in what the file would carry for someone else, found because the reconcile asked.

#### A personal bridge pushing `[user]` items into Taskflow as tasks, and reading completions back [taskflow-personal-bridge]
**Raised by you 2026-08-19**, from executing in another of your projects where the work is mostly `[user]` items. Your framing: Throughliner becomes an executive layer over projects Claude only half-implements, and sometimes you do not want to complete things in conversation — you want the to-do list. **The mapping is yours: a `[user]` item is a task, and its steps are subtasks.** The assessment below and the decomposition are Claude's.

**Your mapping is Taskflow's own model rather than an approximation, which is what makes the completion half work.** Taskflow's subtasks inherit their parent's Project, date and placement, and a parent has no checkmark of its own — it is complete only when every subtask is, and un-checking any child pulls the parent back out of the completed tray. So completion arrives as one derived signal per item, and a half-done item cannot read as done.

**Two decisions of yours, in your own words.** Route: *"design this against the file-based route now, with MCP as the later transport."* Scope: *"agreed, personal bridge to start."* So this is host-only tooling in this project, assuming your own Drive setup, and it ships nothing to consumers; promoting it to a shipped feature is a later decision this does not pre-empt.

**Why file-first rather than MCP.** Taskflow's paid tier already designs the channel — Claude reaching Taskflow through a remote MCP server — so Throughliner would be a client of a route Taskflow intends rather than an integration Taskflow's local-first principle forbids. But `[0020-remote-mcp-server]` and `[0019-ai-choice-flow-and-mcp-setup]` are unbuilt over there and cloud sync is their precondition. The same reasoning is already on their queue in `[strategy-doc-preview]`, in your words there: *"We're just here, so we don't need the MCP."*

**Two hazards found by reading their SPEC rather than assumed.** Taskflow runs on the phone against a local Room database, so a file route means producing a file that is carried onto the device, not writing where Taskflow reads. And their existing `[0014-json-export-and-import]` is a whole-database export and restore — pushing tasks through it would replace every other task in the app. What this needs is an **additive** import, which Taskflow has neither built nor designed.

**Not designable here yet, and that is why this is a capture.** The file contract, which Taskflow Project a pushed item lands in, and when a push happens all depend on what Taskflow agrees to build — so the second limb cannot be stated. It waits on [taskflow-bridge-request].

**One thing to settle at processing regardless of their answer:** a `[user]` item's text can name real people or client details, so what crosses the boundary needs the scrub the queue already gets, and a pushed task is leaving this project's records.

#### Five cleared items each add a clause to the same keep-step, and nothing looks at the total [keep-step-accretes-from-five-items]
Filed 2026-08-19 by Claude, from a coherence check across the cleared region that you asked for at the end of a planning session.

**What was found.** Five items sitting cleared to run each add a limb or a clause to **one step** — `plan.md`'s two-limb keep check. [folding-in-has-no-eviction-step] adds the merge-versus-supersession rule where an item's rationale is authored. [missed-spec-write-interrupts-the-run] adds the SPEC question. [cross-project-work-completes-invisibly] adds the names-what-would-show-it-done clause. [repeal-has-no-ripple-trace] adds a third limb requiring a grep. [not-before-reaches-unprocessed] adds the date approval. Each was admitted separately, each is defensible on its own, and **no item names any of the others** or states what the step looks like once all five have landed.

**Why that matters rather than being tidy-mindedness.** The gate's own admission test asks what a rule replaces, which catches a rule competing with the corpus — it does not catch five rules converging on one step from five different sessions. A two-limb check becomes a seven-part one that nobody designed, in the doc a planning session reads at every item.

**And an unprocessed item already argues that step pushes too hard.** [research-packaged-as-build-work] records that the two-limb check's own force is what drives research into build items, measured three times in one day. Adding five more requirements to the same check is the direction that item warns about, decided piecemeal by sessions none of which could see the others.

**What this item is NOT.** Not a proposal to drop any of the five, each of which was admitted on evidence. Not a new rule about rules. **What it asks for is one reading of the finished step** — write out what the keep check says once all five have shipped, and decide there whether it is a step a session can actually run, or whether some of it belongs at a different site.

**When it runs matters.** It is worth nothing before the five are built and nearly nothing long after, so it belongs immediately behind the last of them rather than in the general queue. Which five ship together is not yet known, so no `Blocked by:` is written here — that is settled at processing, when their build order is.

**Files (rough):** `plugin/throughliner/docs-b/plan.md` — the keep-step, read whole. Host-only in origin but shipped in effect: consumers run this step at every item they process. Relates to [research-packaged-as-build-work], which is the same step examined from the other side.

#### Both skills that detect a stale CLAUDE.md are barred from fixing it [claude-md-unwritable-by-the-skills-that-notice]
Filed 2026-08-19 from INBOX mail sent by a private legal-evidence project, and **independently reproduced here the same day**, which is what makes it structural rather than one project's bad luck.

**What they report.** /setup's migration step reads the project's CLAUDE.md for retired terms and reports what it finds, explicitly editing nothing because the file is the user's. /plan's scope-lock also excludes CLAUDE.md. So the two skills that actually detect staleness both cannot repair it, even where the user reads the finding and asks for the change in the same breath. In their session /setup found four stale lines, the user approved corrected wording immediately, and the outcome was a queue item for a build to apply text that was already written and agreed — while the file read at the start of every session stays wrong until then.

**The second instance, from a different angle.** This project hit the same wall hours earlier: a planning session found a folder-level instruction file both stale and duplicated, the user settled the correction in conversation, and the scope-lock correctly refused the write — so it became [parent-claude-md-taskflow-no-write-stale] rather than a four-line edit. Two projects, one day, the same shape: agreed text that cannot be written by the session that agreed it.

**They propose no fix and name two candidates with unweighed costs:** a permitted-edit carve-out, and letting /setup edit what it reports with approval. **A third exists and should be weighed with them** — that this is the lock working as designed, since a planning session writing rule text is exactly what the gate refuses, and the real cost is only the delay.

**To settle at processing:** which of the three, and whether the answer differs for the *project's own* CLAUDE.md versus a folder-level one above it. Relates to [parent-claude-md-taskflow-no-write-stale] (the local instance) and [gate-trigger-misses-the-audit-checklist] (rules living where no mechanism reaches them).

#### The shell-write guard blocked a scratchpad write while its own message says the scratchpad passes [shell-write-guard-blocks-the-scratchpad]
Filed 2026-08-19 by Claude at its own close, from an instance it caused minutes earlier.

**What happened.** A close needed to split one scratch file into two. The command was `py -c` writing two files inside the session scratchpad — outside the repository, self-clearing, and named explicitly rather than computed. `pre_tool_use.py` refused it. **The refusal text itself says: "If you genuinely need scratch space, the session scratchpad sits outside the repo and still passes."** It did not pass.

**Why this is worth a line rather than a shrug.** The guard is correct in substance — the fix was to use the editing tools, which worked — so nothing was lost this time. What is wrong is that the message tells the session a route is available and the same hook then refuses that route, which is the cry-wolf shape this project has repealed measures for twice. A session that believes the message will retry into the same wall.

**Two possibilities, and the item should not assume which.** Either the path check does not recognise the scratchpad directory at all, or it recognises it and the shell-write rule is deliberately unconditional — in which case the refusal text is what is wrong, not the behaviour. **Read the hook before designing anything**, since the whole defect is a mismatch between what the code does and what its own message claims.

**Files (rough):** `plugin/throughliner/hooks/pre_tool_use.py` and `resources/testing/` for whichever half turns out to be wrong. Host-only in origin; shipped in effect, since every consumer meets the same message.

#### The dispositions listing was run at a planning opening and never surfaced to the user [dispositions-listing-run-not-surfaced]
Filed 2026-08-19 by Claude at its own close, as a testing outcome from using the plugin to build the plugin.

**What happened.** `CLAUDE.md` requires the rule-gate dispositions listing to be surfaced at a /plan opening, alongside the digest and the held work. The session ran `rule_signals.py --dispositions`, read its output, and then folded nothing from it into the opening narration. The user never saw it.

**Why the omission matters more than the content did.** The listing exists because a refused rule proposal leaves one sentence inside one entry and nothing scannable — the user's own recorded question is *"how would I even know to demand it?"*. A listing that is run and not reported reproduces exactly the condition it was built to remove, and does so invisibly, since running it leaves no trace either.

**This is the siteless-check failure with a site.** The obligation has a stated moment and was still skipped, which is the harder case: the corpus already records four instances of a correctly worded rule failing to fire, and this is a fifth in a rule whose whole subject is making things visible.

**To settle at processing.** Whether the fix is wording, placement, or a required artifact — the last being the shape that has proven teeth here, as FAQ-sync and the gate line both show. Weigh against the cost: a line at every planning opening saying "nothing refused since the last planning session" is noise on most sessions, which is the objection that kept this a prose obligation in the first place. Relates to [gate-trigger-misses-the-audit-checklist] and to [standing-audit-programme]'s record of correctly worded rules that do not fire.

**Files (rough):** `CLAUDE.md`. Host-only — the listing does not ship and consumers never author method rules.

#### Throughliner as an executive layer over work Claude only partly does [executive-layer-positioning]
**Raised by you 2026-08-19**, from executing in another of your projects. Your framing: that project involves far more `[user]` work than Claude work, which turns Throughliner into an executive layer over projects that are only half-implemented by Claude, if that — *"and that's fine, but sometimes you don't want to complete things in conversation, you just want the to-do list."*

**Why this is filed separately from the bridge work.** [taskflow-personal-bridge] and [taskflow-bridge-request] carry the mechanism — pushing `[user]` items out as tasks and reading completions back. Neither carries the positioning claim, and the claim is the larger thing: it says what the tool is for in a case SPEC does not currently describe.

**What SPEC says today.** It describes a workflow for non-coders building apps with Claude Code, where the throughline keeps intent alive across sessions. Every example is Claude building software. A project whose work is mostly the user's own — physical, external, or simply done away from the machine — is not excluded anywhere, and is not described anywhere either.

**Two other things arrived the same day pointing the same way**, which is why this is worth processing rather than noting. A consumer project reported that Throughliner is meant to govern work wherever it is conducted rather than only work touching this machine, with a `[user]` item about unpicking a physical dress as the example — see [scope-lock-guards-files-not-work]. That is the same observation from the enforcement side.

**To settle at processing:** whether this is a SPEC addition describing a use the product already supports, or a positioning change that would pull design decisions with it. **It is product truth either way, so it is written at a planning session with you present** — and it must be your position rather than a rendering of it, which is the fault that produced the reading-position sentence struck from SPEC the same day.

**Files (rough):** `SPEC.md`. Relates to [taskflow-personal-bridge] and [scope-lock-guards-files-not-work].

#### A restyle item cites a source that is in neither the queue nor the log [restyle-item-cites-unreachable-source]
Filed 2026-08-19 by Claude, from a coherence check across the cleared region.

**What was found.** [law-prose-restyle-remaining-docs] justifies its two-file limit on the per-paragraph rationale lens by citing `[rationale-audit-fetched-docs-gap]` — *"recommended the two-file limit for exactly this reason"*. That slug is not a queue entry and has no LOG entry named after it, so a reader cannot reach the recommendation the item rests on. The same slug is cited from the heavy-docs restyle item.

**Why it is worth a line rather than a silent repair.** The reasoning may be sound and is probably recoverable from git or from an entry filed under a different name — but the item currently asserts a costed recommendation (roughly 42,000 words of per-paragraph judgement) on the authority of something nobody can open. That is the one-way-citation problem the superseded-research rule was built for, appearing between a queue item and a source that has gone.

**Deliberately not repaired at the moment of finding.** The coherence check that surfaced it was running at the end of a long planning session, and rewriting an item's justification is a keep-step decision rather than a tidy-up. Eight other unreachable citations in the same region were checked and are all correct as written — each names work deliberately deleted and states its fate in the same sentence — so this is the one residue rather than a class.

**To settle at processing:** find where that recommendation actually lives, by searching `LOG/` for the costing rather than for the slug; then either repoint the citation or restate the limit on its own evidence. If it cannot be found, say so in the item rather than leaving a citation that resolves to nothing.

**Files (rough):** `QUEUE.md` only — the two restyle items' prose. Host-only.

#### Sending a letter became a queue item for the first time, and sending at any moment is probably the better shape [mail-send-should-not-need-a-queue-item]
Raised by you 2026-08-20 mid-run, immediately after approving the send that prompted it. **Your view, and it is the thing to weigh: normally mail can be sent at any time, and you think that is preferable.** Filed while it can still be judged rather than settled in the run, since deciding what shape sending should take is planning work.

**What happened.** [taskflow-bridge-request] was processed into Processed as an ordinary build item whose entire work product was one message file written into another project's mailbox. So a run was scheduled, scope was locked, and a build item was ticked, in order to send a letter — where the same letter could have been drafted and approved in any chat at any moment, which is how every other outbound message this project has sent was handled.

**Why it may nonetheless have been right here, stated so the weighing is honest.** The message carried three asks that were designed in a planning session, and another queue item — [taskflow-personal-bridge] — is held against the answers. Making the send a queue item is what makes that dependency visible and gives the answers somewhere to land. A send drafted ad hoc in a chat leaves no trace that anything is now waiting on a reply.

**So the question is not whether mail needs a queue item, but which sends do.** A one-off question to another project plainly does not. A send that other queued work waits on plainly leaves something behind that has to be tracked. Whether that tracking belongs on the *send* or on the *held item that names what it waits for* is the actual design question, and the second reading would remove the need for a send item entirely — the held item already carries `Blocked by:` and could as easily name what it is waiting to hear.

**Relates to [send-record-lacks-destination-and-intent]**, cleared to run in this same session, which gives every outbound artifact a line in `INBOX/sent.md` carrying destination, intent and what was claimed. That may already be the tracking this item is reaching for, in which case a send never needs to be a work item at all — which is worth checking before anything is designed here.

#### The surviving parent-folder CLAUDE.md still calls this project v37 at plugin version 0.37.0 [parent-claude-md-version-claim-stale]
Noticed by Claude 2026-08-20 while building [parent-claude-md-taskflow-no-write-stale], which corrected a path and added an exception in the same file and did not reach this.

**What it says.** `Taskflow Planning/CLAUDE.md` line 5 describes `No code method/` as "currently v37, plugin version 0.37.0". The target is at 1.20.0 and the installed host at 1.20.0-test12, so the claim is wrong by a whole version line. It also still calls the project "the no-code method", which is the pre-rename name — the plugin became Throughliner on 2026-08-13, slug, package folder, marker files and positioning together.

**Why it was not folded into the item that was in the file.** That item's described work was the path and the INBOX exception, both of which it named; a version claim is a different staleness with a different cause, and folding it in would have grown scope the item never described. Captured rather than done, so it gets weighed against the rest of the queue.

**Whether it is worth fixing at all is the real question.** A version number written into a folder-orientation file is stale the day after it is written, and nothing keeps it current — the same shape as the version-versus-format-epoch reasoning already settled here, where a version check was rejected for crying wolf. The likely disposition is to remove the version claim rather than update it, leaving the sentence to say what the folder is without asserting what release it is on. The rename is a plain correction either way.

**One folder up has the same class of fault**, recorded as [claude-config-points-at-dead-layout], and `Desktop/CLAUDE.md` is worth reading in the same pass since it enumerates projects and may name the same things by retired names.

#### Audit this project's own claims against what Claude Code alone already delivers [claims-need-a-claude-code-delta-test]
Filed 2026-08-20 at the close, from INBOX mail sent by the flintcraft.tech site project. Their finding, not ours, and it lands on this project's SPEC rather than on their page.

**What happened there.** A friend read their Throughliner page and asked how the method stops the problems it lists. The user had to admit most of them are fixed by moving from the chat app to Claude Code at all. They audited the page's eight claims: **three are Claude Code's outright, two partly, two are skills neither tool fixes, and one is squarely Throughliner's.** They have made that a cleared work item and a new rule in their own SPEC — a claim only earns its place if Claude Code alone does not deliver it.

**Why it is work here and not only there.** Their page describes this method, so a claim that fails their test fails it wherever it is written — including in this project's own `SPEC.md`, its README, and any Discord post. Nothing here has ever applied that test. The `CLAUDE.md` Discord rule says a post announces changes to Throughliner, and the SPEC's "What it is worth to the user" section makes several claims of exactly the kind their audit found weakest.

**The test, in their words rather than ours:** does Claude Code alone deliver this? If yes, it is not a Throughliner claim.

**What this does not settle.** Whether the ratio they measured on their page holds for SPEC's claims is unknown — it is one project's audit of one artifact, and repeating it here is most of the work. It also cuts both ways: a claim Claude Code delivers may still be worth stating if Throughliner makes it *reliable*, and drawing that line is judgment rather than the binary their rule states.

**Relates to [executive-layer-positioning]**, which is the same question approached from the opposite direction — what Throughliner is for once the things Claude Code already does are subtracted. Worth processing together.

**A reply may be owed** — see `INBOX/sent.md` and the close that filed this.

#### The below-the-line revisit cannot lift anything a build session has not yet closed, and nothing says so [revisit-depends-on-a-log-that-the-close-writes]
Noticed by Claude 2026-08-20 at the close, from a question the user asked: she proposed running /plan before /done, to sort this session's loose ends while the context was fresh.

**Why that does not work, which is the finding.** `plan.md`'s below-the-line revisit decides whether to lift a held item by checking whether its blocker was built **and verified per the LOG**. A build run writes no LOG entries — its close does. So a /plan run in the same chat as a /next run, before that chat's close, sees no session record for anything the run just built and correctly declines every lift that depends on it.

**In this chat that would have been four items:** [queue-privacy-default], [concurrent-plan-and-build-sessions], [rationale-lens-after-the-build-view] and [repeal-falsifies-a-posted-claim], all of whose blockers shipped in this run. Sorting exactly those was the reason she wanted the planning session.

**The same blindness reaches the digest**, which resolves "cites shipped work" by looking for a LOG entry per slug — so every item this run built would read as unshipped for the length of that planning session.

**What is not wrong.** The revisit's rule is right: reading LOG is what makes "has this shipped?" answerable from the files rather than from memory, and a build-then-plan chat is not the shape the method designs for. Nothing here is a defect in the revisit.

**What is missing is that nobody is told.** `skill-nonspecific-rules.md` explicitly permits one chat to run /plan and /next as many times as the work needs, one after another — and that permission is what makes this reachable. A user following it in the order plan-after-build gets a silently degraded planning session, with no warning and no sign anything was skipped. The revisit skips silently by design.

**Options, none of them designed yet.** /plan's opening could notice an undeleted build working file and say plainly that lifts depending on this chat's own work will not resolve until it closes. Or the revisit could read the working file's ticks alongside LOG. Or the always-loaded permission could carry the one exception. The first is cheapest and needs no new state; the second reintroduces a second source of truth about what shipped, which is the thing LOG-as-authority exists to prevent.

**Recorded as answered in conversation and not otherwise.** The user changed course on being told, so this cost nothing here — which is exactly the siteless-noticing shape this project has recorded five times: it worked because Claude happened to say it, and it is not repeatable.

#### The gate-line check fires on every rule-bearing commit at the moment it is made, because the hash it matches on has not been backfilled yet [rule-gate-dispositions-missing]
Filed 2026-08-20 in the post-commit tail, under the slug `rule_signals.py` printed. **What it found is real; what it concluded is wrong, and both halves matter.**

**What it reported.** After commit `b485ee3`, the check said 1 of 11 rule-bearing commits since the baseline carries no `Rule gate:` disposition in any LOG entry, naming that commit — the one just made.

**Why that is a false positive.** `_log_dispositions` matches a commit's entries **by the hash in the entry's heading**, which is the position the backfill writes. A close writes its entries *before* the commit exists, so every heading reads `# [HASH] — …` at that moment. `session_start` fills them at the next session opening. So the check cannot see any disposition belonging to the commit it has just been run against.

**The dispositions are there.** 23 of the 24 entries this close wrote carry a plain `Rule gate:` line; the twenty-fourth is the chat-level record, which is not an item and owes none.

**Why this is worth fixing rather than tolerating.** `CLAUDE.md` requires this script to run at any close whose staged paths touch the rule-bearing set — which is precisely the set of closes that will trip this. So it fires at every rule-bearing close, always wrongly, and clears itself by the next session. That is the cry-wolf shape this project has repealed measures for twice, and it is worse than an ordinary false positive: it teaches the reader to discount the one check that guards the gate obligation.

**It also mis-scores the growth signal in the same window**, since a session's own commit is the one whose rules just changed.

**Options, none designed.** Skip the most recent commit when its entries still carry unfilled placeholders — cheapest, and it reads the same artifact the backfill does. Or match on filename as a fallback where the heading hash is a placeholder, which is looser and reintroduces the misattribution the heading-only rule was written to fix (an entry citing another commit used to donate its disposition to it). Or run the check before the commit rather than after, which changes what the close's step means.

**One honest limit on this capture:** the check is doing exactly what it says it does, and the defect is in when `CLAUDE.md` tells it to run rather than in its matching logic. Whichever way it is fixed, the heading-only match should survive — it exists for a recorded misattribution.

**Confirmed by observation later the same night, so this is no longer inference.** The session-start backfill ran and resolved every `[HASH]` placeholder in the 24 entries to `b485ee3`. Re-running the script immediately afterwards, with nothing else changed: `0 of 4 found something`, and the gate check reports all 11 rule-bearing commits carrying a disposition. The diagnosis and the fix are therefore both pinned — the window is exactly between a close and the next session's backfill.

#### The queue digest reports a converging blocker chain as an unresolvable loop [digest-diamond-read-as-a-loop]
Filed 2026-08-21 by Claude from INBOX mail sent by a consumer project running 1.20.0-test12. Their diagnosis, read against the code rather than taken on trust.

**What they report.** `scripts/queue_digest.py`'s `_blocker_loop()` walks the blocker graph depth-first using a single `seen` set for the whole walk, and returns true as soon as it reaches a slug already in that set. A set shared across the entire walk records "visited", not "on the current path", so any diamond trips it: an item naming two blockers, where one of those blockers also names the other, reaches the shared ancestor twice by two different routes and is reported as a cycle. Nothing is circular and the chain terminates normally.

**Their repro.** Item C is blocked by A and B; B is blocked by A; A is blocked by nothing. The digest reports C as sitting in a loop that comes back to itself, with nothing in the loop ever releasable.

**Why the direction of the failure is the expensive one.** The message asserts the work can never be released, which invites moving a correctly placed item out of Processed — a fate decision taken on a false premise. And the function's own docstring makes the case against leaving it: a flag that fires on correct work gets learned past, and then a real one arrives looking exactly like the ones that are always there.

**To settle at processing.** The suggested fix is to track the current path rather than every node visited, unwinding on the way back out. Read the function before designing anything — this item carries a claim about how the code behaves, not a fact.

**Files (rough):** `plugin/throughliner/scripts/queue_digest.py` and `resources/testing/` for a diamond case. Shipped, not host-only: every consumer's digest runs this.

#### The queue lint flags the two section preambles that /setup itself writes [lint-flags-its-own-scaffolding]
Filed 2026-08-21 by Claude from INBOX mail sent by a consumer project running 1.20.0-test12, and **confirmed live here in the same session**: this project's own lint reports thirteen standing flags at every edit.

**What they report.** The lint reports "prose belongs to no entry" for any text in a section with no `#### ` heading above it, warning that this is what a destroyed or overwritten item heading looks like. Both section preambles — the paragraph under `## Processed` and the one under `## Unprocessed` — are written by /setup from its own template and correctly have no heading. So the lint flags its own scaffolding, in every project, from the moment it is created.

**Why they judge this the worst of the three defects they sent.** It is permanent rather than occasional. The hook reports the flags as "already present in the last commit and none introduced by this change", which is accurate and is exactly what makes them invisible — in their session the flags had survived unexamined across many commits. A block that always contains flags is a block nobody reads, which is where a genuine flag will land.

**To settle at processing.** Whether the lint learns to recognise a section preamble, whether the scaffold stops writing one, or whether the flags are simply correct and the reporting is what should change. Read the lint before designing anything. **Worth checking in the same pass what the other eleven flags in this project actually are**, since nobody has looked.

**Files (rough):** `plugin/throughliner/hooks/post_tool_use.py`, possibly `plugin/throughliner/docs-b/setup.md`, and `resources/testing/`. Shipped.

#### The plugin-managed CLAUDE.md block promises it is kept current and never is [managed-claude-md-block-never-refreshed]
Filed 2026-08-21 by Claude from INBOX mail sent by a consumer project running 1.20.0-test12.

**What they report.** A queue item had sat in their project for a week to fix four stale things in their `CLAUDE.md`: the pre-rename method name, a QUEUE.md description written for the retired batches / red-flags / deferred-tests / parked model, a `/next freeform` entry, and a rule naming `_build.md`. A /next run picked it up and halted, because **every one of those lines sits between the PLUGIN-MANAGED markers**, which read "do not edit between these markers. Updated on /setup and plugin reinstall."

**The shipped template was current the whole time.** They read `templates/CLAUDE-TEMPLATE.md` in the installed plugin and found the correct method name, the two-section queue, the cleared-to-run line, the flavour tags, the red-flag marker riding its own item, plus INBOX and `/rescan` entries their copy had never heard of. /setup has been run there since — their LOG records a migration on 2026-08-13 that updated the version marker and did not refresh the block.

**So the marker's own promise is the false part.** That is consistent with what /setup actually does — backfill what is missing, never overwrite what exists — and it is the one region of the file where the user is told not to look, so the staleness is invisible by design. That block is also the first thing every session in the project reads, so for weeks it described a queue model the project did not have to whoever was about to work on it.

**A second finding they made in passing, and it constrains any fix.** Four rules belonging to their project had ended up **inside** the managed block, carried over from an older template. A refresh firing then would have taken them silently. So whatever refreshes the block says what it is about to overwrite rather than replacing a region a consumer may have added to.

**They repaired their own copy by hand** — the block replaced with the installed template word for word, their four rules moved below the marker — so a future refresh there is a no-op rather than a conflict.

**To settle at processing.** Whether /setup gains a refresh path for the managed region, whether the marker's promise is rewritten to say what is actually true, or both. Relates to [claude-md-unwritable-by-the-skills-that-notice] and [spec-scaffold-describes-method-docs] — all three are content the method copies into a consumer document where the method can change and the copy cannot be reached.

**Files (rough):** `plugin/throughliner/docs-b/setup.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`. Shipped.

#### The mailbox scan counts the operating system's own folder-icon file as waiting mail [inbox-scan-counts-os-metadata-files]
Filed 2026-08-21 by Claude from INBOX mail sent by a private evidence-library project running 1.20.0-test12.

**What they report.** Every session there opens with a notice that one message is waiting, directing the session to read it in full before its first reply. The file is `INBOX/desktop.ini`, which their cloud-drive client writes to set the folder's icon. It is not a message and never was.

**The mechanism, which they read rather than guessed.** `hooks/session_start.py`, in `_waiting_inbox_messages()`, lists the INBOX folder and reports every entry that is a file, skipping only names beginning with a dot. That is why `.address-book.md` never appears and `desktop.ini` always does.

**Why it cannot be fixed on their side.** Deleting it locally is unreliable — the drive client rewrites it. It is tracked in their git as well. Archiving it just moves it into `INBOX/archive/`, where the client writes a fresh one beside it.

**Their suggested remedy:** skip the operating system's folder-metadata files in that scan — `desktop.ini` and `Thumbs.db` on Windows, `.DS_Store` on macOS already covered by the dot rule.

**The cost is the part worth weighing, and it is theirs.** The nuisance is small; the shape is not. That opening notice is the method's guarantee that cross-project mail is not missed, and it carries a self-check insisting the session actually read what is waiting. A permanent false positive there trains sessions to discount the one signal that exists for real mail. They have paid the full reading twice. **This is the same family as [lint-flags-its-own-scaffolding]** — a check that always fires is a check nobody reads.

**One thing to note at processing:** this project keeps its own projects in a synced Drive folder too, so it is a common setup rather than one project's bad luck.

**Files (rough):** `plugin/throughliner/hooks/session_start.py` and `resources/testing/`. Shipped.

#### Should /setup be able to start a project from a template, and what would the unit be [setup-from-a-template]
Filed 2026-08-21 by Claude from INBOX mail sent by a project that has been running the method continuously for about two months. **It asks two questions and proposes nothing to build**, so what is captured is the question plus the evidence they attached to it.

**The idea.** /setup adopts a folder and interviews the user to fill SPEC, always starting from nothing. They ask whether it could instead start from a **template** — a pre-built folder carrying machinery, rules and empty scaffolding, chosen at setup time by what kind of work the project is.

**What they measured, from an audit of their own repository asking what a blank version of itself would consist of.** The proportions were not what they expected. The **folder structure** was the most reusable thing they had — six directories following the lifecycle of the work rather than the shape of any subject, transferring unchanged. The **scripts** transferred essentially unchanged too: about 1,500 lines across four tools, no hardcoded paths, no subject-specific logic, four lines naming people or local folders and all of those inside docstrings. Their **SPEC.md** came out entirely blank — four headings and nothing else, because every sentence of a real SPEC is about its own project.

**The rules were the real problem, and their finding there is the part worth having.** Most accumulated CLAUDE.md rules are generic in shape but proved by a dated, specific incident, and the incident does most of the work. Strip the incidents and what remains is assertions with no reason to be believed and nothing to recognise a recurrence by. Keep them and the template ships one project's private material to everyone who copies it. Their resolution: **generalise to the failure, not to the abstraction** — rewrite the incident so the mechanism survives and the people do not. What never works is reducing an incident to "a session once had a problem here", which keeps the cost of the words and loses the reason to believe them.

**The finding they say matters most if only one is taken: a template must never carry a decision the copying user has not made.** Their example is a hook capturing verbatim session transcripts into the repository — completely project-agnostic and transferable, while everything that *justifies* running it is not: a risk accepted, conditions attached, consent given by the people whose data it is. So their specification ships it disabled with the question in front of it. Any template mechanism hits this shape wherever a carried component encodes a judgement rather than a capability.

**Their two questions, unchanged.** Is a template concept in /setup wanted at all, or is starting from nothing the deliberate design? And if it is wanted, is the useful unit a whole pre-built folder, or something smaller — a rules pack, a scripts pack, a folder skeleton — chosen independently?

**To settle at processing.** The first question is the user's to answer and is a positioning decision, not a design one. **A reply is owed either way**, since they offered to supply the full specification. Relates to [executive-layer-positioning] and [claims-need-a-claude-code-delta-test], both of which ask what this product is for.

**Files (rough):** none until the first question is answered.

#### Every procedure doc ends on a terminal step, and none can tell finished from interrupted [procedure-docs-cannot-tell-finished-from-interrupted]
**Split from [rescan-does-not-hand-back] on 2026-08-21, on your decision**, once that item's three-file fix turned out to be fully specified while this half was not. The observation that started it is yours; the design question below is Claude's.

**What prompted it.** Claude Code's documentation says an invoked skill's content enters the conversation once and is never re-read, so *"write guidance that should apply throughout a task as standing instructions rather than one-time steps"* — see `resources/research/skill-content-lifecycle.md`. All five of this method's procedure docs are numbered marches ending in a final step, which is the shape that instruction warns against. /rescan is the confirmed instance: its terminal step reads as the end of the conversation's work.

**Your evidence, and it is what makes this a design question rather than a rewrite.** Asked whether the same property affects /plan and /next, you said it is a problem sometimes: **sometimes the session ends when planning or building is done, and that is correct**; and sometimes the skills need to be alternately run depending on the conditions — not normally, but sometimes.

**So the naive fix is refused before it is proposed.** "Stop ending" is wrong, because a terminal step is right in the common case. Rewriting five docs to end conditionally, with nothing able to read the condition, replaces a doc that always ends with a doc that guesses — and a guess reads as a decision, which is worse than a consistent ending someone can learn to work around.

**The actual question: can a procedure doc tell which case it is in?** Three candidate signals, none weighed yet. What the user last asked for, which is in the conversation and is what /rescan already reads to do its job at all. Project file state, which is what the scope-lock already uses — `pre_tool_use.py` decides a session is a planning one purely from the absence of this session's build working file, so file state is a proven readable condition. Or nothing, in which case the honest outcome is that each doc's ending states plainly what it does and does not know, which is the honest-limit route this project has chosen repeatedly over a check that over-claims.

**Why it cannot be kept yet.** The file list is the audit's own output, which fails the keep check's second limb by construction. What changes inside each doc depends on which signal survives, and no signal has been tested. **Do not schedule the design into the build** — an item whose prose defers a decision to the start of a run fails the same limb.

**What would settle it, and who owns each part.** Whether a doc can read its own situation is a fact to be established by reading `pre_tool_use.py`, `rescan.md` and the conversation-reading `rescan.md` already does — Claude's to find. Whether an honest "I don't know whether you were mid-something" ending is acceptable output is yours, since it is a decision about what the tool says to a user rather than about what it can do.

**Runs behind [rescan-does-not-hand-back]**, which fixes the one confirmed instance. Placement carries that and this sentence carries the reason: no `Blocked by:` is written, because this could be designed independently — it is only cheaper afterwards, since that build establishes what a corrected ending actually looks like.

**Files (rough): not yet derivable, which is the point of not keeping it.** Likely `plugin/throughliner/docs-b/` across the procedure docs, and possibly nothing at all if the answer is that no signal exists. Shipped in effect: every consumer runs these docs. Relates to [plan-does-not-build-keeps-being-relitigated] and [standing-audit-programme], both of which record a doc's own wording teaching a later session the wrong thing.

#### This project's CLAUDE.md describes work as batches in six places, reported by /setup and never written down [host-claude-md-names-retired-batches]
Filed 2026-08-21 by Claude at a /rescan. **/setup's retired-terms step found these today and reported them in chat; the report is all that happened, and chat does not survive.**

**What the step is for.** /setup reads a project's own CLAUDE.md for names of method pieces that no longer exist and reports each alongside its replacement, editing nothing — because the file is the user's. That worked. What it has no route to is a record: the finding lands in a message and stops there.

**What it found, in this project's `CLAUDE.md`.** Six occurrences describing work as **batches**, a model retired in favour of one work item as a single `#### ` heading with a flavour tag and no sub-headings. The clearest are the scope-lock description ("the active batch's file list", around line 64), the cross-doc-reference rule (line 90), the FAQ-authoring rule (line 196), the hook-format ripple rule (line 238, "A new batch type touches four places"), and the SPEC rule at line 375, which says the spec-edit batch type is retired while itself calling a build "a normal build batch".

**Why it is worth an item rather than a shrug.** This file is always-loaded: every session in this project reads it before doing anything. A session reading "the active batch's file list" is being told the scope-lock works on a structure that does not exist, and the corpus already records four instances of a correctly worded rule failing to fire — a wrongly worded one has less chance still.

**One thing that is genuinely undecided, and it is yours.** /setup's step reports and never edits, deliberately. Whether these six get rewritten is a decision about your own file. Some may be deliberate historical references — line 375 explains a retirement and may need the old word to do it.

**Files (rough):** `CLAUDE.md`. Host-only. **Relates to [claude-md-unwritable-by-the-skills-that-notice]**, which is the same wall from the other side: the skill that finds this is barred from fixing it. Also to [parent-claude-md-version-claim-stale] and [claude-config-points-at-dead-layout] — worth doing as one pass over this project's own configuration files.

#### Four inbound messages changed work here and the rule to draft a reply fired for none of them [inbound-replies-not-drafted]
Filed 2026-08-21 by Claude at a /rescan, **as a testing outcome from using the plugin to build the plugin.** The failure is Claude's own, in this session, and nobody noticed at the time.

**The rule that did not fire.** `skill-nonspecific-rules.md` says: *"When an inbound message changes work here, draft the reply unprompted in the same chat and put it in front of the user."* The send stays under the never-send-unseen guarantee; what the rule adds is the **offer**.

**What happened.** Four messages were read, triaged and archived at this session's opening. All four changed work here — they produced five new captures between them and one fold into an existing item. **Not one reply was drafted, and the rule was never reached for.** The mail step's own procedure was followed exactly: read, route, archive. It says nothing about replying, so nothing in the moment prompted it.

**The messages, and what each is owed.** Three reported defects now filed as [digest-diamond-read-as-a-loop], [lint-flags-its-own-scaffolding], [inbox-scan-counts-os-metadata-files] and a fold into [stop-hook-fires-on-cited-slugs] — those senders are owed at most an acknowledgement that the reports landed as work. **The fourth is different and is the one that actually matters**: [setup-from-a-template] asks two direct questions and offers to supply a full specification. It is a question with nobody answering it, and the sender is waiting.

**Why this is structural rather than one lapse.** The reply obligation lives in the always-loaded rules; the mail procedure lives in `feedback-and-inbox.md` and in /plan's opening step. **A rule with no site is the failure this corpus has recorded five times**, and the mail step is exactly the site it should have been written into — it is the one moment every message is in front of the session, already sorted by whether it changed anything.

**To settle at processing.** Whether the reply obligation gains a site in the mail step, or at the close, which is where a reply is already meant to be drafted for a /next run. Weigh against over-firing: an acknowledgement nobody needs is noise in another project's mailbox, and the rule's trigger is "changes work here", which three of these four meet only weakly. **The honest split may be that a message asking a question is owed a reply and a message reporting a defect is not** — which would narrow the rule rather than site it.

**One thing not claimed.** No reply is being written by this item; drafting still needs the user, and nothing is sent without exact wording approved.

**Files (rough):** `plugin/throughliner/docs-b/feedback-and-inbox.md` and possibly `plan.md`'s mail step. Shipped: consumers run the same mail step. Relates to [mail-send-should-not-need-a-queue-item] and [outbound-report-not-checked-against-the-world], both about the outbound half of this channel.

#### Processing an item rewrites it only when folding — the general rewrite-at-the-end-of-the-loop was never built [processing-appends-where-it-should-rewrite]
**Raised by you 2026-08-21**, checking whether a decision had landed: you asked, after the ideation loop was made to write only on complete, that all planning work the same way — the item the discussion is aimed at rewritten in full at the end of each loop, because it seemed to yield denser writing. You said you were not sure the discussion landed. **It half did.**

**What the record shows, retrieved rather than recalled.** The ideation loop shipped 2026-08-17 and was sharpened the same day — `LOG/2026-08-17-ideation-loop-holds-the-write.md` and `-2.md`; it lives in `skill-nonspecific-rules.md`'s write-first rule and covers ideation in any skill plus capture-processing in /plan. Folding shipped 2026-08-20 as two typed operations — `LOG/2026-08-20-folding-in-has-no-eviction-step.md`: a **merge** rewrites the host item and names what came out, a **supersession** appends dated with why the old reasoning lost.

**What does not exist is the general rule.** Nothing says that processing an item rewrites it whole. `plan.md` carries *"Read the ITEM AS IT STANDS, not the paragraph being added"*, and its own text marks it advisory — it "names an action and never blocks the keep". So the rewrite is reachable only through the merge branch, which fires only where two paragraphs describe the same thing. **Ordinary re-processing appends and is asked to re-read, not to rewrite.**

**This session is the failure observed live, which is why the evidence is not thin.** Three items lifted from below the readiness line — [queue-privacy-default], [repeal-falsifies-a-posted-claim] and [rationale-lens-after-the-build-view] — each gained a settlement paragraph appended to prose written days earlier, and none was rewritten. [rescan-does-not-hand-back] was rewritten, and only because splitting it triggered the merge branch. **The rule you asked for would have fired four times today and fired once.**

**Why the appended form is the one that degrades.** An item re-processed across several sessions accumulates layers, each written by an author who could see the whole item and chose to add to the end of it. [split-action-defeats-the-bands-in-aggregate] has the measurement: across one planning session the queue grew 15% with the item count unchanged, **because processing an item is what lengthens it** — every keep adds a settlement, a Files line and a disposition. Only building an item out or deleting it shrinks the file.

**The evidence for the fix is one data point and no more is claimed.** The single measured merge came out 63 words shorter. That is the only figure anyone has that rewriting is denser than appending.

**To settle at processing, and the objections are real.** A whole-item rewrite at every keep costs output on every item processed, against a saving nobody has measured at scale — and this project has retired one length lever already for yielding 8% and 3%. It also risks the failure `tersifying-the-queue.md` names as its worst: a rewrite that upgrades a paraphrase into a quotation claim, one instance of which was found live in this queue. **Weigh a narrower trigger** — rewrite where the item is being re-processed rather than processed for the first time, which is exactly the layered case and is visible in the item's own text.

**One thing not to lose.** The throughline requires a defeated alternative and its reason to survive, so a rewrite must not be a compression that drops why something lost. That is precisely what the supersession branch protects, and any general rewrite rule has to sit alongside it rather than over it.

**Files (rough):** `plugin/throughliner/docs-b/plan.md` — the keep-step's authoring sub-step, beside the merge/supersession rule it would extend. Shipped: every consumer processes items the same way. Relates to [folding-in-has-no-eviction-step] (shipped, the merge half), [keep-step-accretes-from-five-items] (the same step already carrying five new clauses) and [split-action-defeats-the-bands-in-aggregate] (the measurement).

#### Flavour-specific close material sits in the file every close reads, and the restyle passes will not move it [done-md-carries-other-flavours-material]
**Captured on your instruction 2026-08-21**, after you asked why a planning close ran to roughly 6,000 tokens. The measurement is in `resources/research/why-the-close-is-heavy.md`; this item is the one lever that research names as unqueued.

**The measurement, in one line.** That close read **10,297 words of procedure** — `done.md` 7,443 plus `done-plan.md` 2,854 — to write **3,603 words of record**, about 2.9:1 against the output. The record is the smaller half, so shortening session records does not reach this.

**`done.md` is a fixed toll on every close in every project**, whatever the session did, and it is the second-largest doc in the method after `plan.md`. The sub-docs exist to carry flavour deltas, and a large amount of flavour-specific material is not in them.

**What a planning close reads and discards**, none of it skippable, because knowing which parts apply requires having read them:

```
the completion-verification step        build and audit only
the record-a-routing-step-sweeps block  build and audit only
the entry template's build body fields  build only
the entry template's audit body fields  audit only
the audit approval-outcomes line        audit only
the red-flag lifecycle                  only where a flag cleared
the isolated-session branch             only in a worktree
```

**Why the two queued restyle items do not cover it.** [law-prose-restyle-heavy-docs] applies the wording standard and a subordination lens; [rationale-lens-after-the-build-view] relocates rationale out of operative statements. Both make the text shorter where it stands. **Neither asks whether the text is in the right file**, which is a distribution question — the third limb of the rule gate, and the one nothing in the queue currently exercises over the close docs.

**The precedent is this project's own.** A run used to read the whole queue to build a handful of items; the build view now gives it only what it is building. This is the same shape one layer out — a close reading the whole close manual to run one flavour — and the remedy was simply never applied here.

**What to settle at processing, and the sequencing question is real.** Which material moves and which is genuinely shared; whether the entry template splits per flavour or stays whole with the sub-docs pointing into it, since a split template is the thing most likely to drift into four divergent copies — that risk is the argument the shared file was built on and it has not been weighed against the measurement. **And whether this runs before or after the two restyle passes**: moving text first means the restyle rewrites each paragraph once in its final home, but a distribution pass over text about to be reworded may move sentences that are then merged away.

**One thing not claimed.** No figure here is a target, and a shorter close manual that drops a step is worse than a long one that works — `done.md`'s length is largely accumulated repairs to real failures, several of which it names in its own text. **This item moves text; it must not delete any.** A rule that leaves `done.md` still exists, and the acceptance test is that nothing is lost.

**Files (rough):** `plugin/throughliner/docs-b/done.md`, `done-plan.md`, `done-build.md`, `done-audit.md`. Shipped: every consumer pays the same toll at every close. Relates to [law-prose-restyle-heavy-docs] and [rationale-lens-after-the-build-view] (the same files, a different lever), and to [split-the-cleared-region-for-concurrent-sessions] (the precedent).

#### The close cannot correct a marker /setup wrote wrongly, even with the user approving in the same breath [close-cannot-correct-a-marker-setup-wrote]
Filed 2026-08-21 by Claude at its own close, from an instance it caused minutes earlier. **A third project-independent instance of a shape already recorded twice.**

**What happened.** /setup wrote `4` into `.throughliner-format-epoch` this morning after skipping the epoch-4 conversion, so the marker asserts a shape this project does not have — and the marker is what `session_start`'s halt reads, so nothing will raise it. The defect was found at the close, put to the user, and she decided to set it back to `3`. **The scope-lock refused the write**, correctly: a planning session's standing list is QUEUE.md, SPEC.md, `LOG/`, `FAQ/`, `resources/research/` and the scratchpad, and the marker is on none of them. The close's own declaration marker permits one extra path, `README.md`, which does not help here.

**So a one-character correction, approved by the user in the same exchange, became a step inside a queue item** — recorded on [convert-cleared-items-to-build-blocks].

**Why this is not simply the lock working as designed, which is the obvious reading and is half right.** The lock exists so a planning session queues work rather than doing it, and it stopped a session from editing a file outside its remit — that much is correct. What makes it worth a line is the *asymmetry with the write that caused it*: **/setup could write the marker without any conversation, and no session can correct it.** The skill that can create the wrong state is the only one permitted to fix it, and it is the one skill that refuses to run mid-session.

**The pattern this belongs to, and the reason it is filed rather than shrugged at.** [claude-md-unwritable-by-the-skills-that-notice] records the same shape from a consumer project and from here on the same day: the skills that detect staleness are barred from repairing it, and agreed text cannot be written by the session that agreed it. [scope-lock-guards-files-not-work] records the guard firing on the trivial thing while silent on the serious one. **This is a third instance and the sharpest, because the state being corrected was created by the method itself rather than found in the wild.**

**Three candidates, none weighed, and the third may be right.** Add the epoch and version markers to the close's declaration list, which is already the mechanism for exactly this — paths a close's own obligations name that no build's file list can contain. Let /setup's migration correct a marker it previously wrote. Or accept it: the delay is one queue item, and widening a lock to admit a case the user approved is how locks stop meaning anything. **The third is a real candidate and must not be dismissed for being the do-nothing option** — this project has chosen the honest limit over a loosened guard before.

**One thing this does NOT argue for.** It is not a case for loosening the standing list generally. The list refused nothing else all session, and every other write this close made passed.

**Files (rough):** `plugin/throughliner/hooks/pre_tool_use.py` and `plugin/throughliner/docs-b/done.md` if the declaration list is the answer; `setup.md` if the second; nothing at all if the third. `resources/testing/` in the first two cases. Host-only in origin, shipped in effect: a consumer whose /setup writes a wrong marker is in exactly this position with no route out.

#### Allow a plan session and a build run at the same time, so ideation is never shut off [concurrent-plan-and-build-sessions]
**Split from [split-the-cleared-region-for-concurrent-sessions] at processing 2026-08-19**, which carries the single-writer split this depends on. **Raised by you, and the case is yours.**

**Your two reasons, and the second is the stronger one.** You already switch every minute or so because of wait times — today between whole *projects*, losing the context each time, where switching within one project would be a straight focus win. And a semi-autonomous run occupies the only session you have, so for the whole time it runs you cannot capture anything. **SPEC's first principle — that the user must be able to ideate at any point in the build cycle — is therefore false today**, and this is what makes it true.

**What it repeals.** The always-loaded rule says work on a project from one chat at a time, because a capture filed in one chat is invisible to the other and the two disagree about the queue from the moment either writes. The build view answers exactly that: one writer, and a view regenerated rather than merged. The old objection does not reach this shape — but it was settled after the arrangement "fell over every time it was tried", so the repeal is written as a repeal, naming what changed rather than quietly dropping it.

**What is still to design, and it is the whole of this item.** Two sessions committing to one working tree is a git problem no file split touches. The plumbing exists — `session_start` already detects worktrees, reports commits a checkout does not have, and offers the merge back — so the choice is whether a build runs in its own worktree or both share the tree with a single committer. Then the shipped-slug cleanup at the next /plan opening, and the guard against resurrecting finished work, which rests on status being re-derived from LOG.

**Files (rough, settled once the git question is):** `skill-nonspecific-rules.md` (the one-chat rule), `plan.md` (the cleanup at the opening), `session_start.py`, `faq-template.md` plus `FAQ/faq.md` and both index lines, and `SPEC.md`.

**Returned to Unprocessed 2026-08-21. Its blocker shipped and that is precisely why it could not stay where it was.** [split-the-cleared-region-for-concurrent-sessions] landed on the 20th with five suites passing, so nothing holds this item any more and the `Blocked by:` line is dropped. But the below-the-line region is for work that is designed and buildable and held by a named item or a date — and this item's own text says the opposite, that the git question *"is the whole of this item"* and its file list is provisional. Lifting it would have put an item that fails the keep check's second limb into the region /next builds from, where a run would halt on it as underspecified. Undesigned work belongs in Unprocessed, which is the queue's own four-state model applied rather than an exception invented for this item.

**Nothing designed here is lost, which is the reason this is a return rather than a deletion.** The two reasons, the repeal and what it must name, and the git question stated precisely enough to answer — all of it stays. A later planning session starts from a named question rather than from the beginning.

**What would settle it, and who owns each part.** Whether a build runs in its own worktree or both sessions share the tree with a single committer is a fact to establish by reading `session_start.py`'s existing worktree detection and testing both arrangements — Claude's to find. Whether the resulting arrangement is one you would actually work in is yours, since it changes how you use the tool rather than what it can do.

**Claude's decision, deferred to by you.** The alternative — leaving it held below the line — was refused because nothing was holding it: an item sitting in the held region with no blocker is reported as ready to lift at every opening, which is the false signal this whole disposition exists to remove.

Rule gate: not needed at processing — the repeal is decided here but its wording waits on the git question, so the rule text is authored when this is next processed rather than at the build.

#### Agreeing to something should file it, not produce a question about filing it [agreement-should-file-itself]
**Raised by you 2026-08-21, in your own words:** *"sometimes I agree to things Claude is saying because I don't want to have to remember them myself later so I just want them done. in reality it should capture them without offering/asking."*

**Why it is sharp rather than a preference about tone.** The reason you agree is to stop carrying the thing in your head. A question — *shall I file that?* — hands it straight back, and it does so at the exact moment the offload was supposed to happen. So the ask defeats the purpose it is attached to.

**What is genuinely undecided, and it is not whether you are right.** The method deliberately asks in several nearby places, each for a reason that survives this: an ask before a **delete** is terminal approval; an ask before a **send** is the never-send-unseen guarantee; the process-now offer exists so an idea is not parked without you. None of those is the moment described here. **The one being objected to is narrower: a thing already agreed, where the only open question is whether it gets written down.** Locating that moment precisely is the work.

**A live tension to settle rather than ignore.** [ask-before-writing-a-user-raised-capture] is cleared to run and moves the process-now offer to *before* the write, on your own estimate that you answer "process now" about nine times in ten. That is about **which** of two routes a capture takes. This is about whether the writing itself is worth a question at all. They are compatible on that reading and must be checked against each other rather than assumed to be — the two touch the same carve-out.

**And the general rule already points this way**, which is why this may be an enforcement gap rather than a new rule: the always-loaded routing rules say to route to artifacts rather than memory, and that nothing unrouted survives a chat. An agreement that produces a question instead of a capture is unrouted for as long as the question is open.

**To settle at processing.** Whether the moment is definable without swallowing the three legitimate asks above; whether this is a new clause or an application of route-to-artifacts that nothing enforces; and what the report looks like afterwards, since a capture filed silently still has to be visible enough that you can reject it.

**One thing observed today rather than argued.** Three separate items in this session existed only because a decision made in conversation had nowhere to live — [two-held-items-await-a-disposition] was filed for exactly that, and [advisory-step-does-not-fire] is the same failure inside the close. This is the same class seen from the user's side rather than Claude's.

**Files (rough):** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` — the /plan carve-out in Communication, beside the clause [ask-before-writing-a-user-raised-capture] rewrites. Shipped, not host-only: every consumer agrees to things in conversation.

#### A build writes rules and can no longer see the disposition it is supposed to be transcribing [build-view-strips-the-gate-disposition]
**Raised by you 2026-08-21, from one question:** if `CLAUDE.md` is editable in a build, then that document can just be used to justify what was built. The confirmation below is Claude's, found by generating the build view and reading it.

**Your objection is the SPEC argument transferred, and it transfers cleanly.** A build may not write product truth because *one instance of Claude describing its own work in product truth is justification, not specification*. Rules are not product truth, but the shape of the risk is identical: the party that did the work writes the text that says the work was right.

**The defence on record is a decide-versus-type split.** `pre_tool_use.py`'s own comment states it: the gate runs at the keep-step and its output is a **disposition** on the queue item; the rule TEXT is written by the build that item schedules. What the gate refuses is a build deciding whether a rule may exist, never a build typing out a rule /plan already admitted. `CLAUDE.md` backs it with a hard instruction — *"A build that finds itself authoring a rule with no disposition to transcribe halts and says so."*

**That defence stopped being enforceable when the build view shipped on 2026-08-20, and this was not weighed.** The view was generated against this live queue and read: it carries `Changes:`, `Acceptance:`, `Red flag:` and `Refused:`, and **no `Rule gate:` line**. The disposition sits outside the `--- Build block ---` delimiters, in the item's rationale, which the view strips deliberately as decision history.

**Two consequences, and the second is a live contradiction rather than a weakness.**

- A build cannot read the disposition it is transcribing, so "transcribes rather than decides" is unverifiable from inside the build — the exact thing the split was asserting.
- By the letter of the halt instruction, **every** rule-authoring build must halt, because there is never a disposition present to transcribe. Either the instruction is dead text or every such build stops. Neither was intended.

**The failure has an instance predating the view, which is why this is not speculative.** [build-wrote-its-own-gate-disposition] records a build in the eighteen-item run finding itself authoring a shipped rule and, rather than halting, running the gate's four questions itself and recording the result — a description of an admission decision written by the party that had already done the work. That is your objection, observed, before the view made the disposition unreachable.

**The likely fix has a precedent inside the same block.** `Refused:` is already carried into the view for exactly this reason: a build that cannot see why an option was rejected proposes it again and stops to ask. A disposition is the same class of thing — the minimum history a build needs in order not to re-decide something. Carrying `Rule gate:` into the view would make the transcriber claim true for the first time since the split was written.

**To settle at processing, and the alternatives are not equivalent.** Whether the disposition moves inside the block delimiters or the generator learns to pull it from the item's prose — the first changes an authoring convention every existing item already follows, the second changes only the script. Whether the halt instruction survives unchanged once a build can see the line. And whether anything should verify that the rule a build typed matches the rule the disposition admitted, which nothing does today and which may be undetectable.

**What must not be reached for, stated because it is the intuitive move.** Barring a build from `CLAUDE.md` the way SPEC bars one leaves nowhere for rule text to be written at all — planning is barred from that file by the same lock, and the two bars together would make the method's rules unwritable. The asymmetry is deliberate; what is missing is the evidence travelling with the work, not the permission.

**Superseded in part, 2026-08-21, by your proposal in the same exchange: /plan should be the session that writes `CLAUDE.md`.** The paragraph above assumes both bars stay in place and concludes that the rules would become unwritable. Your proposal removes that premise by lifting the planning bar rather than adding a build one, so the conclusion does not reach it. What the paragraph still rules out is barring the build *alone*, which is untouched and stays refused.

**The prior refusal is cited rather than treated as settling this, because it answered a different objection.** `LOG/2026-08-17-scope-lock-denies-claude-md-2.md` (`7e3c1c8`) refused a permission change and recorded the exclusion as intended. The objection it met was that the gate's only-plan-can-refuse design forces a planning session to queue as a build the text it just admitted; the answer was that deciding is not writing, evidenced by fifteen rule changes dispositioned at a keep-step with nothing blocked. **That answer assumes the build faithfully types what planning admitted — which is the assumption this item shows has failed**, since the disposition no longer travels into the view the build reads. So the refusal rests on a premise that has since gone.

**Two arguments for your proposal, the second of which appears nowhere in the record.** A build that writes rules is the party that did the work writing the text saying the work was right, which is the SPEC-symmetry argument this whole item is about. And **/plan is the session the user is in**: a rule the user is meant to read and approve would be written where she can see the words, where today the wording of every method rule is produced in a run that is unattended in practice.

**Two costs, and the first is the user's own objection from elsewhere in this queue.** [plan-does-not-build-keeps-being-relitigated] records her words — *"I don't know why this is even a question. Plan does not build."* Letting /plan write rule text moves that boundary, and she filed an item because it keeps being moved. A candidate answer is that writing a document is not building, since /plan already writes SPEC, but that is exactly what needs settling rather than assuming. The second cost is load: a planning session admitting fifteen rules would then write fifteen rules, on top of already being the heavy session.

**Deliberately not decided here.** It changes who authors the method's rules, it was raised at the end of a long session, and the honest sequencing is that it is settled together with the disposition-in-the-view question above rather than ahead of it — the two are the same subject approached from opposite ends.

**One thing observed in passing and not folded in.** `BUILD-VIEW.md` is neither tracked nor gitignored, so every run leaves an untracked file at the repository root. Not this item's subject; noted so it is not lost.

**Files (rough):** `plugin/throughliner/scripts/generate_build_view.py`, `plugin/throughliner/docs-b/plan.md` (the build block's field list at the keep-step), `CLAUDE.md` (the halt instruction, host-only), and `resources/testing/`. Shipped in effect: a consumer's build reads the same view, though only this project authors method rules.

Relates to [build-wrote-its-own-gate-disposition] (the instance), [rule-admission-has-no-independent-approver] (the same question one layer out — who checks the party that decided), and [split-the-cleared-region-for-concurrent-sessions] (the build view this is a consequence of).

#### The close announces freeform work and never hands over the words to start it [freeform-close-gives-no-opening-prompt]
**Raised by you 2026-08-21, immediately after the close that should have covered it.** Your framing, and it carries the design: freeform users need an opening prompt every time freeform is the next thing to run — and because freeform has to run without a skill having been invoked, it needs a fresh chat, so the only place that prompt can be handed over is the end of the session before it.

**The step already exists and did its job.** `done.md`'s "Announce a `[freeform]` item if Processed holds one" says /next will not build it, that a close recommending /next without saying so sends the user into a stop, and to say plainly that it needs a session where the work is done by hand rather than run from the queue. That is what happened here. It named the item, said it was freeform, said /next would not reach it, and explained why.

**And you still had to ask how to take it.** Your question, verbatim: *"how would I imagine that I TAKE that next freeform session — do I just open a new session without running plan, and then instruct Claude to take the next thing from the top of the queue and build it?"* Two of the three guesses in it are wrong — the item is at the end of the cleared region rather than the top of the queue, and "build it" is /next's verb for a route that cannot reach it.

**So the gap is between describing a situation and being able to act in it**, which is the same distance this method already closes everywhere else it appears. A `[user]` line must carry a walkthrough naming the thing to click and the thing to look for, because a description of what needs doing is not an instruction for doing it. A freeform hand-off is the identical shape — a session the user has to start, from nothing, with no skill to guide them — and it is the one hand-off that ships no words.

**Why the prompt has to come from the close and can come from nowhere else.** Freeform work runs in a chat where no skill has been invoked, so there is no procedure doc loaded to explain itself, and the queue item is not read until someone tells Claude to read it. The session that ends is the last moment anything can put the words in front of the user.

**What it should carry, from what actually worked here:** the slug, the flavour, and where the recipe lives — enough that a fresh chat needs nothing else. Rendered as a paste target under the existing render rules, since its exact characters are the substance.

**One thing to settle at processing.** Whether this is the freeform announce step alone, or whether the same gap exists wherever the close hands work to a session it cannot start — a `[user]` item the user will do between sessions is the obvious neighbour, and it already carries a walkthrough, which may be why it does not have this problem. Check before widening.

**This is the second instance today of a shipped step firing correctly and still leaving you stuck** — [advisory-step-does-not-fire] is the other, where the recommendation was made and never written down. Both are the same class: the step describes and does not deliver. Worth reading together rather than separately.

**Two additions from running it, 2026-08-21, and the first is tested rather than designed.** The prompt this close actually handed over was used, and you amended it before pasting: *"the freeform item at the end of the cleared region **in QUEUE**"*. Your stated reason — that Claude does not know about QUEUE at session start — is wrong and the edit is right anyway, which is worth recording because the correct reason is what the fix has to encode. `session_start` does report the file (`QUEUE.md: found`) and its dependency facts, so Claude knows a queue exists and what shape it is in; what it has not got is the **contents**. So "the cleared region" names nothing until the file is opened, and the prompt has to say which file to open rather than assume the term resolves. **A prompt this item ships must be tested the way this one was — by being pasted into a blank chat — rather than judged readable in the session that wrote it.**

**Second, the prompt says the session ends with /done, and this half is weaker evidence — marked as such rather than carried on the strong half's back.** The run did ask for /done at the end, so the behaviour worked and your own reading was that it therefore does not matter much. It earns its place on one case: a session interrupted, or walked away from before it finishes, never reaches the step that asks, and a user who never knew a close was owed has no reason to come back to it. Cheap to include, and it is what makes an abandoned freeform session recoverable.

**One thing settled in passing, because it was asked and the answer is not obvious from the docs.** Every `[freeform]` queue item implies a session of its own, and not every freeform session comes from an item — most freeform work never passes through /plan at all and reaches the close as ordinary hand edits. The tag's job is telling the close what it is looking at, so the item-to-session direction holds and the reverse does not.

**Files (rough):** `plugin/throughliner/docs-b/done.md` — the freeform announce step. Possibly `templates/faq-template.md` with `FAQ/faq.md` and both index lines, since what the user *does* changes: today they work out how to start the session, and after this they paste a line. Shipped, not host-only: every consumer with a freeform item meets the same blank chat.

Filed after this chat's close, in the post-commit tail, so it belongs to no committed session record until the next close picks it up.

#### The build view's completeness test can never read equal in a project holding a cleared `[user]` or `[freeform]` item [build-view-completeness-test-unreachable]
Filed 2026-08-21 by Claude, from running the test itself at the end of [convert-cleared-items-to-build-blocks].

**What the checklist says.** `migrate-checklist.md`'s epoch-4 section closes with a check-it-landed step: run the generator and read its summary line, which prints how many cleared items it found and how many carried a block — *"Equal numbers mean the migration is complete."*

**What the generator actually prints.** Against this queue, immediately after a conversion that left nothing undone: `20 cleared item(s), 17 with a build block`. The three without are the two `[user]` posts and the `[freeform]` item itself — which the same checklist, four lines above, says need no block at all. So the two halves of one section disagree, and the disagreement is not a judgment call: the excluded flavors are excluded by name.

**Why it is worth fixing rather than remembering.** The test is the only mechanical confirmation the epoch-4 migration has. A migration that ran correctly reports as incomplete, and one that genuinely left items unconverted reports the same way, so the number distinguishes nothing in any project holding a cleared `[user]` or `[freeform]` item — which is most of them. A test that reads wrong on correct work is the cry-wolf shape this project has repealed measures for twice.

**Two candidate fixes, and neither is settled here.** The generator could count only the flavors that need a block, so equal becomes reachable; or the checklist could state the test as the generator's numbers plus the count of cleared `[user]` and `[freeform]` items. The first changes shipped code and the second changes shipped prose, and which is right depends on whether that summary line has other readers — not checked.

Relates to [convert-cleared-items-to-build-blocks], which ran the test, and to [setup-migration-gate-is-epoch-3-shaped], which repairs the recipe this section belongs to and may want to settle both at once.

#### The mailbox scan reports the outbound send record as waiting mail, and the directive beside it says to archive the record [sent-record-surfaced-as-waiting-mail]
Filed 2026-08-21 by Claude, from this session's own opening, which announced *"1 message waiting in this project's INBOX"* and named `INBOX/sent.md`.

**The mechanism, read in the code rather than inferred.** `session_start.py`'s inbox scan lists every non-dot file directly inside `INBOX/`, skipping only directories — so it has no way to tell an inbound message from anything else living there. `INBOX/sent.md` lives there permanently by design: it is this project's own record of what it has sent, one line per outbound artifact, and [send-record-lacks-destination-and-intent] shipped it into that folder deliberately.

**Why it is worse than a wrong count.** The surfacing text that rides with it instructs the session to route each message through the three-way triage and then **move the file to `INBOX/archive/` so it stops being surfaced.** Followed literally, that files the send record away — the one artifact a repeal is supposed to be checked against, and the thing [repeal-falsifies-a-posted-claim] is built to grep. A cleared region already holds an item whose whole premise is that `INBOX/sent.md` sits where it can be read.

**It did not happen this session**, because the file was read and recognised for what it is. That is judgment covering for a mechanism, which is the class this project treats as a mandatory capture rather than a near-miss.

**Shipped, not host-only.** Every consumer project that has ever sent anything has a `sent.md` in the same place, and gets the same false message at every session opening.

**The fix is not settled.** Excluding the one filename is the obvious move and may be too narrow — the folder now holds at least one permanent artifact, so the question is whether the scan should key on a naming convention for mail rather than on a deny-list of everything else. Worth deciding once rather than each time something else is filed there.

Relates to [send-record-lacks-destination-and-intent], which created the file, and to [repeal-falsifies-a-posted-claim], which depends on it staying readable.


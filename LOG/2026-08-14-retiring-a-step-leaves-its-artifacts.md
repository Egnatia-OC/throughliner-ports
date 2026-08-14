# 78fa417 — Retiring a step now retires the files it produced, and /plan's build prohibition is drawn by destination instead of content type

The rezip stopped building a zip when the local marketplace began sourcing the plugin folder directly. The last zip it ever built stayed in place, and five days and several sessions later it was still sitting one line above the live folder in the file listing, presenting itself as the plugin. Windows Explorer hides the `.zip` in its breadcrumb, so browsing into it looked exactly like browsing the target: the same seven top-level folders, and inside `docs-b` a file that had been split apart on 2026-08-10, with every date frozen at 2026-08-09. Read as live, that says the project has been authoring the wrong docset for days, and it took a session and several exchanges to establish that nothing was wrong.

It was not one stale file. `plugin/zip-archive/` held three more from the same dead mechanism, and the folder inside all four still carried the pre-rename name. The same shape three times: a mechanism was retired or renamed, and the artifacts it had produced stayed.

The gap was structural rather than an oversight. Eviction covers rules, and `resources/retired-terms.md` covers retired terms — a retired *file* had no equivalent, so nothing anywhere held a list of outputs whose producer no longer exists. The fix is subordinate to eviction and spends no slot: retiring a step retires the artifacts that step produced, named and deleted in the same build, with any live doc describing that step's output reworded too.

The limit is stated in the rule itself so it is not read as more: this fires only when someone is knowingly retiring a step, and does nothing about junk that accumulates from nobody's decision in particular. The user raised that general problem and it is genuinely harder; this does not address it.

The residue was in the prose as well as on disk, which is the same finding one level up. The host-and-target section still said a bare working-tree or zip edit changes nothing the host sees — wording that treats a zip as a live intermediate someone might mistakenly edit, when packaging stopped producing one. A weaker claim was considered and rejected as a mirage: that the host/target frame has no category for a zip at all. It does mention one, so the defect was staleness in the sentence rather than an absent slot.

Folded in on the user's instruction, a second and unrelated wording defect found while tracing whether a rule had gone missing. It had not — `47966bb` reworded "Don't process work outside /plan" into "No planning work in any execution skill", which guards the other direction, and "/plan is for planning, /next is for building" is untouched and older than both. The defect was in plan.md's ground rules, which stated the planning session's prohibition as "never build — code that needs writing is queued, not written here". The qualifier narrowed it: deleting four junk files and rewording a sentence is not code, so it read as outside the prohibition, and the session proposing this work nearly did both before catching it. The accurate statement already sat a few lines below in the containment rule, drawn by destination. So the doc stated one boundary twice, once by destination and once by content type, and the narrow one was the one being followed. Redrawn by destination, per eviction: one statement, not two.

**The deletion half was wrong and was reversed at this session's close, which is the most useful thing in this entry.** The staleness sweep found `resources/release-ritual.md` still moving, pruning and rebuilding both paths: the **rezip** stopped building a zip, but a **release** still runs `Compress-Archive` into `plugin/throughliner.zip`, archives the previous one under `plugin/zip-archive/`, and attaches the zip to the GitHub Release. So these were live release artifacts, not a retired step's leftovers, and the next release would have failed at its archive step on a missing file and a missing folder. Both were git-tracked and were restored from history before this commit, on the user's decision.

**What the item got wrong, stated precisely, because the rule it authored is the thing that must not inherit the error.** It reasoned from the rezip alone and treated "the rezip no longer builds a zip" as "nothing builds this zip". Two producers write the same path, and the frozen 2026-08-09 modification date is consistent with either reading — which is exactly why the file fooled a session once already and then fooled the fix. The confusion the item identified was real; the culprit was not.

So the rule ships and the deletions do not. The eviction amendment stands on its own evidence and gains a check it did not have: before deleting a suspected leftover, grep the path across `resources/` and the shipped package and confirm no live producer still writes it. `CLAUDE.md`'s host-and-target section now names both packaging paths explicitly rather than describing one, and `resources/retired-terms.md`'s artifact section records the withdrawn pair as a worked example instead of listing them as retired.

Rule gate: run — admitted as an amendment to the eviction rule. Parent named; written as a subordinate clause rather than freestanding, so no slot is spent. Failed three times and each is pointable. Not done unprompted — five days and several sessions passed with the artifact in plain sight. Fires only in sessions retiring a step, which is why it rides the gate rather than the always-loaded shipped rules. Not hookable: "a step is being retired" is a judgment, not a detectable event. Nothing evicted, because an amendment replaces nothing.
Retired artifacts: none. The two candidates were withdrawn — see above.

## Close-tail — work done during this session's close

Recorded here rather than spread across seventeen entries, because none of it
belongs to a single built item and all of it came out of this item's thread.

**The zip reversal**, described above. Found by the staleness sweep, decided by
the user, applied before the commit.

**A reply sent to the flintcraft.tech project.** Their inbound message reported
that `flintcraft.tech/report` had been live since 2026-08-06 and corrected a
report this project sent on 2026-08-09 describing it as missing. The reply
acknowledged the correction, named the method finding it produced, and asked for
nothing. Sent on the user's explicit yes, after confirming their `INBOX/` is
covered by their own `.gitignore` — the first live exercise of the check built
under `[inbox-privacy-for-sensitive-correspondents]` this same session, which
passed. Their folder path was recorded in the address book, which is
write-and-send only under the rule built today.

**Four captures filed at the close**, three of them from the user's own
observations:

- `[outbound-report-not-checked-against-the-world]` — the outbound side has no
  check-the-world rule, so a report can describe a problem fixed days earlier.
- `[close-cost-scales-with-run-size]` — measured after the user asked where the
  close's tokens went: seventeen entries at 7,650 words plus 1,800 words of index
  lines, against two procedure docs read whole. The per-item entry rule is right;
  the observation is that the close's cost scales with run size while a build's
  does not.
- `[docs-b-name-outlives-the-two-docset-model]` — the user's observation that the
  folder is still called `docs-b` when docset A is retired and there is one
  docset. The answer is that nobody renamed it. **She then directed the rename,
  and it was deferred to its own run on Claude's recommendation and her
  agreement**: the scope was traced by grep to 25 files, which split into live
  pointers that must change and historical records — `scope-lock-audit.md` alone
  has 131 mentions — that must not, so a find-and-replace would corrupt the
  history while fixing the code. Applying that halfway through a close carrying
  seventeen entries is the failure the runs-alone marker exists for.
- `[drive-dates-are-not-edit-dates]` — Google Drive's modified date means last
  synced, not last edited, and both parties reasoned from it as though it meant
  edited.

**One discipline slip, recorded rather than passed over**, and filed as
`[depth-field-has-no-binding-to-its-item]`: two items ticked in the same edit put
both depth lines under the first, so one item carried two and another none. The
close reconstructed the intended reading from context, which a fresh short
session could not have done.

**Files touched:** `CLAUDE.md` (the eviction rule, the disposition block, the host/target paragraph now naming both packaging paths, the Where-things-live tree now labelling both zip paths as release artifacts), `resources/retired-terms.md` (a new Retired artifacts section, currently empty, carrying the withdrawn pair as its worked example), `plugin/throughliner/docs-b/plan.md` (the "never build" ground rule). No files deleted.
**Routed to Captures:** `[docs-b-name-outlives-the-two-docset-model]`, `[drive-dates-are-not-edit-dates]`, `[close-cost-scales-with-run-size]`, `[outbound-report-not-checked-against-the-world]`, `[depth-field-has-no-binding-to-its-item]` — see the close-tail section above.

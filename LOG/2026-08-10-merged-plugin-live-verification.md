# [HASH] — The merged plugin verified live, mostly by this session being one

Slug: `[merged-plugin-live-verification]`. Entry opened live during the /next
walk-through, per [walkthrough-work-unrecorded].

## The tag was wrong, and the capability check caught it

The item was filed as `[user]`. Running the /next pre-hand-off capability check —
name the tool that would do the work and confirm it is absent — the answer is that
most of this needs no tool the user has and Claude doesn't. The checks are
observations of the installed plugin's behaviour, and a session using the plugin
*is* the observation. Only two of them genuinely need a person: anything across an
application restart, and anything Claude cannot witness from inside its own run.

So per the over-tag guard, the work was done as ordinary work and the correction is
recorded here rather than handed over. Nothing was asked of the user.

**What this verified is the host installed at the time: 1.20.0-test4.** That build
predates this session's own work, which is correct — the item is about the merged
plugin as shipped, not about today's changes.

## Verified live this session

- **session_start surfaces an uncleared red flag first.** It did, naming
  [migration-skips-inbox-commit-question] before anything else in the payload.
- **/next picks the top Processed work above the marker, and stops at the marker.**
  The run was exactly the cleared region, twenty-two items, and did not reach past
  the cleared-to-run line.
- **/next self-scopes.** It derived a file list from the items' own text and wrote
  it into the build working file.
- **The scope-lock enforces that list.** It denied a write to
  `resources/testing/statusline_probe.py`, which the run had not listed, and named
  what the list did allow. The file was genuinely in the item's described work, so
  the list was extended — which is the designed path, not a bypass.
- **The shell-write guard holds.** It blocked a Python one-liner whose write target
  was computed at runtime, with the reasoning that an unreadable target cannot be
  shown to be safe. That is the hardened behaviour from `4f5e167` working.
- **/next builds several cleared items back-to-back.** Sixteen, without
  per-item re-confirmation.
- **The queue mover deletes by slug, byte-for-byte.** Seventeen deletions, each
  echoing the heading it removed.
- **The post_tool_use lint runs on the real two-section queue and flags real
  problems.** It caught two `Blocked by:` references whose blockers had just
  shipped and been removed — correct, advisory, non-blocking, and it named all
  three possible causes rather than asserting a fault.
- **/next reaches `[user]` items only after the Claude work is built**, and walks
  them one at a time.
- **The check-the-world rule works.** [report-url-404]'s walk-through ran its
  observable check instead of asking whether the user had done it.
- **Device-access consent: not applicable.** No build needed on-device
  verification, so the resolution check folded in from [device-access-consent] had
  nothing to fire on. Recorded as not-exercised, not as passed.

## Not verified, and honestly so

- **The /done family** — flavor routing, LOG files named by slug, the shipped-slug
  cross-check, one summary commit for a multi-item run. This session's own close
  exercises all of it; it is simply downstream of this entry being written.
- **The three-strikes error halt.** No error repeated three times on one item, so
  nothing triggered it. Unexercised, not passed.
- **/setup scaffolding a two-section queue plus `resources/research/`.** Needs a
  fresh folder. Claude can run it; it did not, because it is outside this run's
  described work.
- **The lint's other flags** — a slugless line, missing provenance, a missing
  section heading, a red-flag state that is neither cleared nor uncleared. Only the
  blocked-by flag fired, because the real queue did not contain the others. Testing
  them means writing bad queue lines deliberately, which is a build, not an
  observation.

## Disposition

The item is complete as far as an observation-based check can take it, and the
remainder is either this session's own close or work that needs its own item. The
unverified four above are captured as [merged-plugin-verification-remainder]
rather than left inside a closed item's prose, where nothing would act on them —
which is the failure the method already names.

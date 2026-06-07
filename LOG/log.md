# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — /plan session: 7 batches promoted, 3 captures filed, audit unpark cascade

Heaviest /plan session in a while. Three threads, all sparked by accumulated decisions catching up at once. First, the audit-as-batch-type landing unblocked three Parked audits (trickle-up rules to plugin-behaviour.md, output-tag prose-to-tag conversion, in-scope/out-of-scope distinction) — all promoted oldest-first as audit batches with target and criteria locked in. Second, push-back on the /next-after-/next drift narrowed its framing: the mechanical safety net (session_start detects _build.md and routes the next /next to resume) already prevents dual builds, so the real cost is the missed /done — a lost LOG entry and commit for the just-finished batch. Fix slated as a Scope-discipline rule in plugin-behaviour.md rather than a Step 7 wording change. Third, two structural questions surfaced and got their own batches: _build.md's purpose isn't named anywhere in the procedure docs so it reads as vestigial (fix: [BRIEF] narration at create / resume / consume moments), and the per-release log file split was being maintained on a theory of Claude's retrieval that didn't match reality (the why-pipeline goes through index hashes, not version groupings — design threads span releases anyway). Drop the split, one growing log.md. Existing log-v*.md files stay in place; retrieve still works via hash. One procedure tweak fell out of the session itself: unpark candidates had no structural home in /plan, so they got smushed into the entry question — fold them into Step 2's capture-processing sequence with the same promote/keep-parked/drop choice. Three captures filed: FAQ shelf behind reader testing, internal sequence-naming language leaking into chat ("loop," "Step 2") flagged after the user couldn't follow it, and the audit batch type's current "Claude reads docs" framing conflating the plugin-dev case into the generic batch definition.

**Queue changes:**
- Promoted from Parked: [trickle-up-audit], [output-tag-audit], [scope-distinction-audit]
- Promoted from Captures: [next-done-recommendation] (narrowed framing)
- New batches from discussion: [fold-unparks-into-step-2], [narrate-build-md-purpose], [drop-log-per-release-split]
- Hash backfill: LOG/index.md placeholder → 3814815

**Captures routed:** 3 added (FAQ shelf for _build.md's four functions, loop-language leak, audit-definition too narrow); 4 promoted out (3 unpark + 1 active capture).

# 15e10c9 — The brevity amendment measured: median words per message when speaking fell 55 → 37, with the sample's limits stated

Audit entry; the planning record is `2026-08-21-brevity-amendment-outcome.md`. Direction and size, no verdict — no target exists to declare against.

**Attribution.** Each transcript records the installed host version at its session start, so samples were attributed per session rather than by file date. The amendment shipped in cc33c1e (15:21 on 2026-08-21); `1.20.0-test14` was installed at 15:26 and is the first build carrying it.

**Before** (the recorded baseline in `2026-08-21-transcript-output-measurement-2.md`; 25 sessions, builds up to 1.20.0-test13): 1,374 speaking messages — median 55 words, quartiles 17/219, deciles 10/330, longest 1,157. By skill, median when speaking: /next 19, /plan 119, /done 30, /rescan 176, /setup 365, no-skill 162.

**After** (all 8 sessions stamped 1.20.0-test14, same day): 153 speaking messages — median 37, quartiles 16/158, deciles 11/246, longest 782. By skill: /next 17, /plan 144, /done 27, no-skill 756 (n=5, too small to read).

**Direction and size:** overall median when speaking fell about a third (55 → 37); the 75th and 90th percentiles and the longest message all fell (219→158, 330→246, 1,157→782). /next and /done were roughly flat — already terse before the amendment. /plan rose (119 → 144). **Limits:** the after-sample is eight same-day sessions dominated by long build runs — a different mix from the baseline — and one measured session was still in flight when sampled.

**Files touched:** none by the audit (it read transcripts). Close action recorded here: `resources/transcript_output_length.py` deleted — its stated delete-time was "once this audit has reported".
**Routed to Captures:** none.
**Approval outcomes:** no capture findings; the measurement itself is the product.
Rule gate: not needed — an audit edits nothing and no rule is authored or amended.

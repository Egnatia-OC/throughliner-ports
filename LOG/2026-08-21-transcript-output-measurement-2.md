# [HASH] — A one-off instrument for what Claude actually says, and the baseline reading it was built to take

Build entry. The planning entry that processed this item is
`2026-08-21-transcript-output-measurement.md`.

**Why this was worth doing.** The user named Claude's verbosity as the single thing
stopping her promoting the plugin anywhere but GitHub, with the YouTube channel
blocked on it. Against that, nothing in the project measured a line Claude said.
`measure_written_shape_length.py` measures written documents, `queue_digest.py`
measures the queue, `rule_signals.py` measures rule text — and nothing opened a
session transcript at all. So the thing she cared most about was the one thing with
no number against it, which is exactly the position that let a 4.8-era conclusion
about brevity instructions stand unchallenged for a whole model generation.

**What was built.** `resources/transcript_output_length.py`, standard library only,
with the UTF-8 stdout/stderr block copied from `reorder_queue.py`'s canonical copy.
It reads `.claude/projects/<project-slug>/*.jsonl` and reports words per assistant
message: median, quartiles, deciles, min and max, a scaled histogram, and a split by
which skill was running.

Two implementation facts worth recording because they are not obvious from the
transcript format. Content blocks belonging to one assistant message arrive as
separate `.jsonl` lines sharing a message id, so they are regrouped before counting
— one row per message the user saw, not per block. And a message that emitted no
text at all counts as zero and is reported separately, because a run's silent turns
are a real part of its shape and averaging them in would hide both halves.

**The narrowing is the substance of this item, and it came from the user.** The
first framing had this as a standing measurement anyone could run. Her objection
removed it: a measurement with no standard becomes a standard the moment a session
reads its median as a norm, which is the circularity SPEC already records against
the retired word bands. So it is scoped as the instrument for
`[brevity-amendment-outcome]` and nothing else — wired into no close, no session
opening, no check, imported by no other script — and its header carries a stated
delete-time under the temp-file rule, so availability cannot quietly turn it into
the standing measurement the narrowing rejected. Verified: nothing in the repository
calls it. `resources/research/index.md` is deliberately not edited, because an index
line is how a finding is made findable by later sessions, which is the opposite of a
tool with a delete-time.

**The baseline, which is the point of running it before the brevity amendment.**
Across the 25 most recent sessions of this project: 4,614 assistant messages,
172,463 words. Messages that said anything at all: 1,374 — median 55 words,
quartiles 17 / 219, deciles 10 / 330, longest 1,157. Silent tool-call-only messages:
3,240. Median when speaking, by skill: /next 19, /plan 119, /done 30, /rescan 176,
/setup 365, no skill running 162.

The per-skill spread is the interesting part and was not predicted: /next and /done
are already terse, and the length sits in /plan and /setup — the two skills where a
person is in the room being asked things.

**Printing a target or a band was refused**, because caps are retired here and the
current-model research says a short brevity instruction steers as well as a
quantified one, so a figure buys nothing and would be a bare number. **Asking Claude
to summarise a session instead of reading the raw file was refused** on `CLAUDE.md`'s
record that a reconstruction is lossy and reads Claude-authored content as fact.

**Files touched:** `resources/transcript_output_length.py` (new, host-only).

**Routed to Captures:** none from this item.

FAQ: not needed because nothing a user does changes and the script does not ship.

Rule gate: not needed — no rule is authored or amended in the method's own text. This adds a host-only measurement script and evicts nothing.

Depth: short. Built and confirmed — the script runs against this project's own
transcripts and printed the distribution above.

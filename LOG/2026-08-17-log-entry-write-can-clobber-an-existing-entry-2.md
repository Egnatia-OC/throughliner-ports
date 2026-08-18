# 7e3c1c8 — the LOG-collision refusal is built, and the close that built it proved why it was needed

`pre_tool_use.py` gains a fifth refusal: a Write whose target is an existing file under `LOG/` is denied, naming the collision and the next free `-2` / `-3` filename. Write only, never Edit — a close legitimately edits the index and appends tails to existing entries, and both go through Edit, so nothing correct is caught. A genuinely new entry filename does not exist, so it never fires on a correct close either.

Driven both ways against the target file before shipping: an existing path denies with the free name offered, a fresh path passes.

Then this close walked into the original defect. Meeting a real collision, Claude wrote to the taken path deliberately, expecting the new guard to refuse it. It did not — the hook that runs is the installed host, a frozen snapshot predating this change — and a committed entry was overwritten and recovered with `git checkout HEAD --`. The destroyed entry's own text had predicted exactly this, saying the guard cannot protect the close that settles it. Filed as [live-testing-a-hook-change-hits-the-old-host].

SPEC's `pre_tool_use` bullet gains the matching sentence, approved before it was written.

Rule gate: run — one refusal added to an existing write guard which already refuses by path; no freestanding rule, no always-loaded slot. One alternative refused: a staging check, on cry-wolf grounds.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `SPEC.md`
**Routed to Captures:** [missed-spec-write-interrupts-the-run], [live-testing-a-hook-change-hits-the-old-host]

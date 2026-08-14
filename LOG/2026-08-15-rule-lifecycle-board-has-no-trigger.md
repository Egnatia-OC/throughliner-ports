# [HASH] — The rule-corpus checks get a close trigger, so their silence finally means something

Captured by the user, whose words were that she has no idea how this works and is concerned it is not working, because she never hears about it.

What was measured rather than assumed: the checks work. Run live, they returned nothing found on all four, with every rule-bearing commit since the baseline carrying a gate disposition. The silence was accurate. That is the good half of the answer.

The defect is that nobody could have known that. Nothing ran them — not a hook, not any skill's procedure, not the close ritual — and the description said what they were without ever saying when to run them. A clean run and a run that has not happened for weeks are indistinguishable from outside, which is exactly the condition this mechanism exists to remove for rules. It is the siteless-rule pattern this project has now recorded several times, applied to the machinery that watches rules.

The close is the site, on the same staged-path trigger the rule gate itself uses. Two of the four checks read commits, so the close is the one moment they have anything new to say, and the existing hook-suite step already reads `git status` at the close for the same kind of decision — a proven shape needing no new detection. Running at every close was rejected: the checks are meaningless on a commit touching no rules.

It reports one line even when quiet, and that is the point rather than a nicety. A close that says nothing recreates the exact condition that produced this capture.

**One departure from the item's file list, made deliberately.** It named shipped `done.md` and a close-family sub-doc. The trigger went into `CLAUDE.md` instead, beside the hook-suite close rule, because the item's own text says the mechanism is host-only and consumers have no such checks — shipping the obligation would put a step in front of people it can never fire for. `rule_signals.py` needed no quiet output mode either; its output is already short enough to summarise in one line, which the item said to check before adding one.

The wording is constrained by its paired item, which removed the framing that lets a clean run read as health: the close line says what was checked and found, never that the corpus is in good shape. The two builds touch the same output and had to agree, which is why they were built in the same session.

Rule gate: not needed at this item's own processing — the disposition for the pair is recorded on `[rule-board-measures-paperwork-not-health]`, where the eviction and the rewrite were decided.

FAQ: not needed — host-only, and a consumer's close never runs it.

**Files touched:** `CLAUDE.md`.

**Routed to Captures:** none.

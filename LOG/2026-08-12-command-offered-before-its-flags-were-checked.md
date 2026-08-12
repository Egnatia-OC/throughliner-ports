# [HASH] — A command handed to the user for pasting is verified first

`next.md`'s `[user]` walk-through branch gains a check: before a command goes into a block for the user to run, verify it — run it where doing so is safe (a scratch fixture), or read the tool's `--help`.

The scope is narrow on purpose, and the narrowing is what makes the rule cheap. A command *Claude* runs with a wrong flag costs one turn and self-corrects: the error arrives, the help gets read, the work continues. The cost only lands when the command is handed over — the user is a non-coder, they cannot tell a typo from a broken tool, and the failure arrives in their hands rather than Claude's. So it fires at one identifiable moment rather than on every command composed.

**Weighed against the admission gate rather than waved through.** For: two instances within days of the same document's commands being wrong, both landing on the user. Against: one recorded instance of this exact failure, and a general don't-guess rule that arguably covers it. What tips it is that the general rule governs *external facts* — and a tool's own flag list is not external. It is one `--help` away and was read seconds later. The gap is ordering, not knowledge, which no amount of don't-guess wording addresses.

The item's own counter-argument, that the corpus was 65% over its ceiling, is void: the ceiling was found unfounded for the 5-series in this same session. The case stands on relevance instead, and relevance is why this lives in a fetched doc read only during a walk-through rather than in the always-loaded file.

**Not merged with its sibling.** [user-walkthrough-command-cant-produce-the-observation] asks whether the user's step yields the *evidence* the item needs; this asks whether the command *runs at all*. A command can be perfectly valid and still not produce the observation, which is exactly what happened in that other instance. That item is still unprocessed.

**Files touched:** `plugin/si-plugin/docs-b/next.md`
**Routed to Captures:** none from this item
**Rule gate:** run — one rule admitted, into a fetched doc rather than the always-loaded corpus, on the reasoning above.

# [HASH] — the digest stops replacing the queue read, and the whole file is read alongside it

The user noticed Claude seemed not to have read the whole queue, and that the feeling was about a week old. It was corroborated rather than accepted: the digest landed on 2026-08-11, six days earlier. It is not the hook's 10,000-character limit, which carries no queue content at all.

The cause is that /plan is instructed not to read the queue whole. Its opening runs a digest *instead*, one line per item with the rationale prose deliberately omitted, and the always-loaded rules bless that by calling a mechanical digest a stronger satisfaction of the read-the-whole-file duty than paging.

Her framing of the cost is sharper than anything in the docs: the queue is one file because Claude reasons across items badly when they are split, and a digest of headings restores exactly that split — headings together, reasoning apart. She then killed the narrower fix Claude proposed. Reading only the items a session intends to process assumes the user will name them, which will not happen; and blockers and fold-in points can be anywhere, so every item bears on any planning session.

The session supplied its own instance: an ordering instruction she had written into one item's prose was invisible on the digest line, so the item it governed was processed first.

The measurement changed the trade. The queue is 34,287 words across 75 items, 457 per item against a work-item band top of 229; at band it would be roughly 15,000 words, about 20,000 tokens — affordable to read whole. So the bands largely dissolve the reason the digest replaced the read. Not the digest itself, because half of what it prints cannot be got by reading: held-since dates, where a blocker sits, which files two items share, whether a premise cites shipped work.

So the settlement is both, not either. Three sites currently say otherwise and all three change. A conditional read was refused, because a condition would have to predict which items bear on each other — the thing the read exists to discover.

One thing not claimed: multi-file queues were far worse, in her words an absolute disaster. This is an occasional feel that something is wrong.

Rule gate: run — a narrowing of the digest instruction and of the always-loaded clause blessing it. The eviction is the "instead of reading QUEUE.md" wording.

**Queue changes:** [digest-stops-replacing-the-read] filed, processed and cleared in the same session.
**Work processed:** kept — [digest-stops-replacing-the-read].

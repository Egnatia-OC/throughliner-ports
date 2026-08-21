# 746608f — 47 stale `docs-b/` paths rewritten across 13 ready items, and the item deleted rather than kept, because the work was planning's

Filed mid-run the previous day, when the build of [rename-docs-b-folder] was refused by the scope-lock: a build does not edit the contents of a queue item, and the queue tool moves whole entries byte-for-byte rather than rewriting text inside one. So the rename completed everywhere except in the queue's own instructions to future builds.

**It was carried out here rather than kept as work, which is the disposition worth recording.** Queue-wide cleanup is named in `plan.md` as something /plan resolves in-session; the item's own text said to do it at a planning session, by grep. Keeping it into Processed would have scheduled a build for work no build is permitted to do — the exact refusal that filed it.

**Scope, measured rather than taken from the item's own count.** 13 of the 15 then-ready items named `plugin/throughliner/docs-b/`, including the first two in the run and the restyle itself. 47 path references were rewritten to `plugin/throughliner/docs/`, plus three more in one build block using the short form. Each of the five distinct file paths was checked against the disk afterwards; all five resolve.

**Three occurrences were left alone deliberately**, as the item required: the two slugs containing `docs-b`, which are immutable identifiers, and the capture describing what the user saw in her file browser, which reports what was on screen at the time and would stop being true if rewritten.

**One repair beyond the item's described work, and it is named rather than folded in silently.** Two lines in [law-prose-restyle-remaining-docs] told a build the docs folder might be renamed before it ran. That rename has shipped, so the justification was false while the instruction it justified — enumerate the folder at build time rather than from a written list — remains correct. The reason was corrected and the instruction kept.

**Queue changes:** 50 path references rewritten across 14 items; [queue-files-lines-name-the-old-docs-path] deleted from Unprocessed once carried out.

**Work processed:** deleted — [queue-files-lines-name-the-old-docs-path], after its work was performed here.

**Routed to Captures:** none.

Rule gate: not needed — no rule authored or amended. This is a mechanical path rewrite across queue prose, with three exclusions the item itself named.

FAQ: not needed because nothing a user does changes; this corrects instructions inside this project's own queue.

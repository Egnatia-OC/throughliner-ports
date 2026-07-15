# 5e62c1c — Make /next's close commit rule explicit: one line logs verbatim, many get a summary

done-build.md already wrote one LOG entry per built line, but done.md's commit core still assumed a single entry became the commit message — it said the message *is* the approved LOG entry, title and body verbatim. Under a multi-line run that silently underspecified: with four entries, nothing said which one was the commit message, or whether there should be four commits.

The rule now branches on count. One line shipped → the message is that line's LOG entry verbatim, as before, and the commit step still reviews nothing new because the entry was approved at the entry step. Several shipped → no single entry can stand for the run, so the title is a one-line summary of what shipped and the body lists each line's one-liner, while each line keeps its own LOG entry. That summary is the one genuinely-new text at the commit step, so it is drafted and approved there.

This replaces /cruise's per-line commits, which retired with /cruise. It also absorbs the one distinctive mechanic of the retired goal-session mode — several LOG entries landing in a single end-of-run commit — so retiring goal sessions lost nothing. The rule governs its own session: this close ships four lines, so it commits as a summary.

**Files touched:**
- plugin/si-plugin/docs/done.md: commit-core step 3 now branches on how many work lines shipped
- plugin/si-plugin/docs/done-build.md: 2.1's commit-message note reworded for the single- vs multi-line cases

**Routed to Captures:** [next-rules-missing-faq-entries]

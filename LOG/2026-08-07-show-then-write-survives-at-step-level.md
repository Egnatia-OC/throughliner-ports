# [HASH] — Six step-level show-first instructions converted to write-first, and the doc-bound rule given precedence and a composed-from clause

Two rules were live in docset B at once. `plugin-behaviour.md`'s doc-bound-text rule says approval-time text destined for one of the method's docs is **written to that doc first**, verified by re-read, then pointed at — while six step-level instructions still said the opposite. Step-level instructions govern the act, so what a session actually did was follow the step.

That is a strong explanation rather than a convenient one: all three observed slips happened at steps on this list. The behaviour was never "forgot to write" — it was **"composed an approval message, as instructed, then described it as though the doc had been written"**, which is precisely what a half-migrated procedure produces. So this build removed the instruction being followed rather than stacking another rule on top.

**Converted (six):** `docs-b/plan.md`'s keep-step, wind-down re-scan and queue seeding; `docs-b/done.md`'s wind-down re-scan, handmade-close LOG entries, and `[user]`-item close entry. Each now writes first, re-reads to confirm, then sends a short summary plus a pointer carrying the target's exact heading text, with a reject meaning the text is edited back out and the removal confirmed.

**Left alone, deliberately, with the reasoning recorded in the docs so the next auditor finds it instead of reopening the question:** `migrate-checklist.md`'s whole-queue draft and `setup.md`'s pointer at it. Writing an entire speculatively-rewritten queue file before approval is a materially different risk from writing one work item — a reject means restoring a document rather than editing a block back out.

**Two clauses on the doc-bound-text rule.** A **precedence** clause, so a surviving step-level instruction is never read as a carved-out exception. And the operative one: **the pointer's summary is composed FROM the re-read's output, not written alongside the write.** The existing write-verify-point ordering was loaded and specific during all three slips and did not hold, so a fourth restatement was not the move. An ordering can be followed out of order without anyone noticing; a summary cannot be composed from content that has not been read. Same remedy shape as the sweep itself — remove what makes the wrong move available rather than forbid it harder.

**The limit is stated in the doc rather than assumed away:** no hook can inspect prose before it is emitted, so this is better procedure, not a guarantee. That limit proved real within hours — see [write-first-fix-failed-in-its-own-session], filed at this close after the same failure recurred in ordinary conversation, which is the one context the six converted steps could not reach.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/migrate-checklist.md`, `plugin/si-plugin/docs-b/setup.md`
**Routed to Captures:** [write-first-fix-failed-in-its-own-session]

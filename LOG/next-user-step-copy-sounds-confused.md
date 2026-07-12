# [HASH] — next.md — reworded the /next `[user]`-step handover copy: added a copy-discipline note to Step 3's handover branch that keeps the silent active-build check out of the message and drops the "nothing to build" framing in favour of naming the `[user]` step and offering to assist

Observed 2026-07-11 dogfooding the drive-folder-cleanup project: running /next when the top ready line was a `[user]` step produced copy that read as confused and defensive — "No active build. The top of the ready queue is a `[user]` step … there's nothing for me to build." Two things were wrong with it. It folded the internal active-build check (Step 1's [SILENT] check) into a user-facing message, blurring two unrelated facts; and it framed the situation as having nothing to do, when /next helps either way.

Fix: a "Copy discipline when the top line is `[user]`" paragraph added to next.md's Step 3 handover branch, stating both rules with the why — don't lead with "no active build," and don't say "nothing for me to build"; instead name the `[user]` step, say why it's the user's to run, and offer to assist.

Scope note: the batch listed next-build.md too, but that file was written against the pre-merge structure. In the merged two-section docs, next-build.md is only reached after scope is locked (i.e. when there is Claude-work to build), so the muddled top-line-`[user]` copy never originates there. The fix lives entirely in next.md's pre-flight/handover path; next-build.md was left untouched with the user's approval.

**Files touched:**
- plugin/si-plugin/docs/next.md: added the copy-discipline paragraph to the Step 3 handover branch.

**Routed to Captures:** [working-mode-approval-time-render] — the working-mode render rule needs a carve-out for approval-time drafts of not-yet-written doc text (raised by the user at close).

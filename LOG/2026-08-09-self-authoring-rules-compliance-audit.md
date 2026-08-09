# 4f5e167 — The always-loaded corpus counted for the first time: ~218 instructions against a 150–200 ceiling, with an approved eviction list that would bring it to ~170

The self-authoring gate has a binding limit — a *count of instructions*, not a word count — and no such count had ever been taken. Until it existed, "evict what fails admission" had no target and no stopping rule, so a sweep could only produce opinions. That is why the audit's first pass was a count and not a judgement.

The number: roughly **218** always-loaded instructions. About **156** in `plugin-behaviour.md` and **62** in `CLAUDE.md`.

The split matters more than the total, and reporting only the sum would have hidden it. A consumer loads `plugin-behaviour.md` alone, so their corpus is ~156 — at the top of the band but inside it. This project loads both, so it runs at ~218, over the ceiling, and every rule past that point makes the rest less reliably followed. Those are two different numbers against the same limit and they belong to two different audiences.

Counting rule, recorded so a later sweep reproduces rather than re-invents it: one instruction per discrete directive — a bolded rule statement, a bullet, or a decision block — with descriptive prose, rationale and worked examples scoring zero. The skill docs were excluded from the count, because they load only when their skill runs and the ceiling is about what competes for attention in *every* session; they remain in scope for the three lenses.

Thirteen findings were presented as one numbered set and approved whole. They were filed as **six** work items rather than thirteen, grouped by disposition, because findings sharing a disposition share a method and a risk — the four consolidations, for instance, all turn on the same warning that a clearer restatement leaving the prior standing has doubled the text rather than merged it. Applied in full they take the count to roughly 170, and the consumer-facing file to about 140.

The largest single saving is redistribution, and it is the finding least safe to accept quietly. Three findings move rules to fetched documents rather than deleting them — the feedback channel, the INBOX detail, and the Rezip/Push/Release ritual — which removes them from the count without removing them from the method. The gate warns that this is exactly how bloat gets hidden. They pass on the stated test, since each has a trigger a session cannot miss, but that reasoning was flagged to Alex during the run rather than asserted, and the checklist now requires it recorded per rule instead of once per batch.

The item's own instruction contradicted the audit contract: it named `resources/method-compliance-audit-checklist.md` as a file to write into, and an audit files findings to the queue rather than writing them into documents. That was surfaced rather than followed. Alex chose findings-to-queue plus method-to-checklist, which is what ran — the eviction list went to the queue as work, and only the reusable *method* was written to the checklist.

**Files touched (read, not edited):** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `CLAUDE.md`, `resources/self-authoring-rules.md`, `resources/method-compliance-audit-checklist.md`. The checklist was then edited under the approved split, gaining the instruction-count method, the five dispositions, the per-rule justification requirement for redistribution, and two lessons from running it.

**Routed to Captures:** six work items — `[evict-claude-md-duplicated-rules]`, `[evict-fetch-feedback-and-inbox]`, `[evict-fetch-release-ritual]`, `[evict-consolidate-four-clusters]`, `[evict-relocate-two-rationales]`, `[evict-claude-md-staleness]`. Plus `[ask-not-at-message-end]`, filed during the run when Alex missed an approval question buried mid-message — a live failure of a shipped rule, hypothesised as a missing placement clause rather than a new rule, and explicitly to be processed as an amendment given the count this audit just produced.

Two further session-level captures were filed at this close, recorded here because the run's other entries each belong to a single built item and these belong to the run as a whole: `[log-entry-cost-at-run-scale]`, raised by Alex when she stopped the close to ask what a twelve-entry process was for; and `[walkthrough-work-unrecorded]`, found by the build-close reconcile — /next's walk-through branch ran a full rezip that `_build.md` has no section to record, so an interruption would have lost it.

**Approval outcomes:** all thirteen findings approved as-is; none dropped or reworded.

FAQ: not needed because the audit read the method's own internal documents and changed no shipped behaviour; the eviction work it produced will carry its own FAQ dispositions when it builds.

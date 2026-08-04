# 455082b — Gave planning sessions an ask-never-deny file gate, and dissolved the emergency path into a triage rule and a record duty

File containment engaged only while a build was running: `pre_tool_use.py` sets `has_active_build` from `_build.md`'s existence, so a planning session could edit any file in the repo — shipped hooks, procedure docs, templates — with nothing noticing. SPEC described the scope-lock with no hint it was build-only, so a reader would reasonably conclude planning sessions were contained.

**The gate asks and never denies, and that is the load-bearing part.** Denial is right during a build, where the file list was agreed in advance so a surprise means drift. In planning there is no agreed list to drift from: the session is a conversation, the user is present, and a legitimate write is authorised in one word. The evidence came from the processing session itself, which moved a document into `resources/research/` at the user's request — an action no sensible whitelist would have carried and which was entirely ordinary. A deny-list would have blocked it.

So the whitelist is a quiet-list rather than a boundary. QUEUE.md, `_plan.md`, SPEC.md and `LOG/` pass silently because /plan writes them by design; the existing memory, research and scratchpad exemptions ride along, since prompting for them only here would be inconsistent noise. Everything else asks. This makes the gate deliberately *weaker* than a scope-lock: its job is visibility, not containment. A planning session that edits a shipped hook should not be stopped — it should be unable to do it unremarked.

**The emergency path dissolved rather than being built**, which is the outcome worth recording: a mechanism removed, not added. With ask-never-deny, the user's go-ahead is structural. The 2026-08-03 scrub of a named third party's private circumstances from a public repo would have surfaced an ask, the user would have said yes, and the record would exist. What the capture called an emergency path is just the gate working. What remains is a record duty at the close and a red-flag triage question — "does this wait?" — neither of which is an override.

The rejected alternative is recorded so it isn't re-proposed: a deny-list plus a named emergency exception fails twice, blocking ordinary planning work and offering an exception convenient enough to be reached for when it isn't warranted. Ask-never-deny has no exception to abuse because it forbids nothing.

SPEC's scope-lock sentence was corrected in the same edit [build-scope-vs-described-work-unenforced] wants, as the item instructed.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `docs-b/plugin-behaviour.md`, `docs-b/done.md`, `docs-b/plan.md`, `SPEC.md`, `README.md`, `templates/faq-template.md`, `templates/faq-index-template.md`
**Routed to Captures:** [docset-a-silent-on-planning-gate]

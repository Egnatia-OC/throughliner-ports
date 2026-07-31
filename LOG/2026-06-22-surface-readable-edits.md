# ec7ce6f — next-build.md: readable (non-code) edits reveal their new text after the edit (no pre-edit preview, no re-approval); a small mid-build tweak folds into the build's LOG entry; FAQ entry

`/next` used to treat every edit like code: list the upcoming changes as bullets, make them silently, never show the actual new wording. For readable content (a doc, copy, a spec section) that's the wrong shape — the pre-edit bullet preview is noise when the edit lands instantly, and the user never sees the real words without opening the file. The exact wording of a readable edit is produced in `/next` and was never seen in `/plan` (which agreed only the intent), so showing it is the first time the user meets the actual words.

next-build.md's Execute framing now carries three additions. **No pre-edit preview** for any edit, readable or code — the work was already agreed in `/plan`. **Readable edits reveal their new text** after the edit, as a wrapped readable block, informational with no approval ask appended (the change was already agreed); a code edit doesn't get this half because a non-coder can't review code text the same way, so it stays silent on the success path. **A small mid-build tweak** to a just-surfaced readable edit ("change this one bit") is in-scope: it refines the build's already-agreed work product, so it's made and recorded in `_build.md` Changes to fold into the single LOG entry `/done` writes — no separately logged object (which would bloat the index line) and no `/plan` round-trip. A request that's actually new scope still routes out via Scope management. The Build-entries loop gains a reveal step and a no-preview note. Sibling in spirit to [review-vs-test-framing] — both about how the method handles human-readable generated output rather than code.

No run-now fixture — this is observed narration behaviour, not a code test. Its confirmation is a host-side deferred line; also naturally observable in the Taskflow E2E project.

**Files touched:**
- plugin/si-plugin/docs/next-build.md — Execute [SILENT] framing: no-preview rule, readable-edit reveal, mid-build-tweak allowance; Build-entries loop gains a reveal step.
- plugin/si-plugin/templates/faq-template.md — new entry "When Claude edits a doc or other writing during a build, do I see the new wording?"
- plugin/si-plugin/templates/faq-index-template.md — matching index line.

**Routed to Captures:** none

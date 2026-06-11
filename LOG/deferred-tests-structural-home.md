# 18b87be — /next [deferred-tests-structural-home]: deferred tests get a mechanical slot in QUEUE.md

The pre-flight check "unconfirmed tests from a previous build?" had no place to read its answer from. It ran on conversation memory four pre-flights running in the 2026-06-10 long session, while the two deferred host-side tests sat archived in log-v1.10.0.md, where no fresh session has an instruction to look. On short weak-model sessions the tests would silently never surface — memory covering for missing structure, which the short-session design target forbids. QUEUE.md now carries a "## Deferred tests" section between Batches and Captures: one line per test — source batch slug, what to verify, what confirms it — seeded with the four pending host-side tests (done-split single summary, _build.md narration moments, pre-scope-lock close, old-log retrieve). The writing rule landed in done.md as a third stated-once section beside LOG entry files and the commit core, with one-line pointer steps in done-build.md and done-test.md. /next's gate bullet became a mechanical read: re-present every entry, remove confirmed lines and record the confirmation in the confirming session's LOG entry, stay silent when the section is empty or absent. The format is documented in CLAUDE-TEMPLATE.md and this project's CLAUDE.md, and the FAQ gained a consumer-facing entry. The build then closed its own loop: the batch's behavioural test is itself host-side, so this close wrote it into the new section as its fifth entry — written on the decided-rules-apply-immediately basis, while the deferred line stays open to confirm the same behaviour runs from the installed docs after push + reinstall.

**Files touched:**
- QUEUE.md: new "## Deferred tests" section between Batches and Captures, seeded with the four pending host-side tests plus this batch's own behavioural test
- plugin/si-plugin/docs/done.md: "## Deferred tests" stated-once section — what qualifies, the line format, the lifecycle, and why LOG-prose-only deferrals are forbidden
- plugin/si-plugin/docs/done-build.md: new sub-step 1.4 Write deferred tests (pointer at done.md)
- plugin/si-plugin/docs/done-test.md: new sub-step 1.3 Write deferred tests (pointer at done.md)
- plugin/si-plugin/docs/next.md: blocker-gate bullet replaced with the mechanical section read
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: QUEUE.md description gains the section's format and lifecycle
- CLAUDE.md (this project, Method docs section): same description added
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md: FAQ entry "What is the 'Deferred tests' section in QUEUE.md?" plus its index line
- REGISTRY.md: done.md description updated, FAQ pair count 13 → 14

**Routed to Captures:** none

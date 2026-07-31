# 29ba751 - resources/reader-test-workflow.js: sync the reader-test fixture's CLAUDE.md to the spec-edit-batch model

The reader-test harness carried a pretend project whose CLAUDE.md still taught the retired rule SPEC.md is read-only during builds, edit it only during /plan - so a fresh Claude simulating a session learned the old SPEC rule and the harness graded comprehension against a model the method no longer holds. The FAKE_CLAUDE_MD now states the spec-edit-batch model (SPEC is a normal doc, changed only by a planned spec-edit batch that /next executes and that lists SPEC.md). Host-only dev fixture. Grep confirmed the retired wording is gone and the new wording present.

**Files touched:**
- resources/reader-test-workflow.js

**Routed to Captures:** none

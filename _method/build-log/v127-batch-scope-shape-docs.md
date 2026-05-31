# v127 — 2026-05-28 — Batch scope shape documentation

**What shipped.** New "Queued batch entry shape" section in session-reference.md documenting the 6-field template for BACKLOG queued batches (Goal, Approach, Inputs, Outputs, Success criteria, Risks/dependencies). Includes heading-number convention, field-order rule, parked-batch pattern, sizing guidance, and disambiguation from plugin-side build batches. Proxy updated with new section and corrected line numbers.

**Decisions taken and why.** Placed the new section between BUILD-LOG and Open-questions entry shapes — queued batches are the primary BACKLOG content, so they come before OQs in the reference sequence.

**Pivots and surprises.** None.

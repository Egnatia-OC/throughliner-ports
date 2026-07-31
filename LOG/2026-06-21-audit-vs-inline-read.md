# 29ba751 - plan.md: document the audit-vs-inline-read line - queue an audit only when the read needs its own session

The findings-vs-decisions test sorted audit-shaped from decision-shaped work but said nothing about size, so there was no written guidance on whether to read a handed-over artifact inline or queue a formal audit batch. plan.md now adds the size axis: an audit batch earns its existence by deferring a systematic read too big to do inline, so /plan reads a bounded artifact with few expected findings inline (surfacing and routing directly) and queues an audit batch only when the read is large or systematic enough to need its own session. Audit-this does not force a batch.

**Files touched:**
- plugin/si-plugin/docs/plan.md

**Routed to Captures:** none

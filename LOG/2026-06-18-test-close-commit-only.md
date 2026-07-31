# 5c31b52 — done-test.md commit step now overrides the commit core's push-ask to commit-only (mirrors done-plan.md): a test close records, doesn't release, but still commits. Goal-session batch 4 of 5.

A test batch forces a /done close, but its commit step ran the full build-style "commit and push?" dual ask — disproportionate, because a test session changes no product code, only records (the LOG entry and queue updates: batch marked done, captures, confirmed deferred-test lines removed). The commit core already lets a sub-doc override the push-ask default — done-plan.md does this for planning closes — but done-test.md didn't, so test closes still got the dual ask.

done-test.md Phase 2.4 now overrides the commit core to commit-only by default, mirroring done-plan.md's planning-close override. The why is carried inline: a test session records results, not a shippable change, so there's nothing to release; the records still commit (or the next session opens on a dirty tree and warns); push stays available when the user asks for it — it's a default, not a lock. This extends the planning/build push-offer split that [push-offer-fit] established to the third close type.

**Files touched:**
- plugin/si-plugin/docs/done-test.md: added the commit-only push-ask override at Phase 2.4 Commit.
- QUEUE.md: removed the batch; added its deferred-test line.

**Routed to Captures:** none.

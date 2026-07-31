# 5c31b52 — Named the three test-routing categories (run-now default / user-must-run / environment-or-host-side-deferred) as the canonical statement in plan.md, applied self-contained in next-build.md, aligned to batch 2's two-axis tags, + FAQ. Goal-session batch 3 of 5.

Across the Taskflow E2E sessions, Claude-runnable tests kept getting batched instead of run — the ten batch-0001 TaskDao instrumented tests sat deferred ~3.5 weeks and ran only once a Pixel 6 turned out to be connected. Root cause: deferral was treated as a catch-all for "can't run this second," and the environment was assumed absent rather than checked. The method said run-what-you-can-now and defer the un-runnable, but never named the category that actually causes the confusion — tests Claude runs but that need a device, emulator, or environment not present this session.

plan.md's "Think through testing when drafting" now states three categories as the canonical home: (1) run-now/inline — any test Claude can run this session, the default, including environment-dependent tests when the environment is available; (2) user-must-run — visual / point-and-click / physical / subjective → user-run; (3) Claude-run-but-environment-dependent or host-side → defer until runnable. The spine: run-now is the default, defer is the exception justified only by (2) or (3), never a catch-all. Before assigning to (3) on environment-absence, confirm the environment really is absent (points to batch 1's [ask-before-device-use] ask-don't-assume rule). The failure named to kill: a runnable test parked as "can't run now" and sitting unrun for weeks.

next-build.md applies the same three categories at build time, stated self-contained because a /next session doesn't load plan.md, but worded consistently. The category vocabulary is aligned with batch 2's two-axis Deferred tests tags so the two don't drift (a deferred category-2 test is runnability user-run; a deferred category-3 test is runnability Claude-runnable with deferral reason host-side or needs-user), and the note records that the per-line source batch slug preserves the why-pipeline trace when a later session runs a deferred test.

An FAQ entry ("Why do some tests run straight away and others wait?") and its index line ship.

Depended on batch 2 (deferred-test-seams-fix) and was authored against its reframed two-axis text, per the goal directive's ordering.

**Files touched:**
- plugin/si-plugin/docs/plan.md: replaced the two-way testing split with the three-category canonical statement + spine + don't-assume-absent + two-axis vocabulary alignment.
- plugin/si-plugin/docs/next-build.md: applied the three categories at the test-entries step, self-contained; the deferred-tick bullet now notes deferral reason + runnability.
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md: added the run-now-vs-wait FAQ entry + index line.
- QUEUE.md: removed the batch; added its deferred-test line.

**Routed to Captures:** none.

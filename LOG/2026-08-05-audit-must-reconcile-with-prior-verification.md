# d9162e4 — audits must reconcile with the LOG before reporting shipped work broken

An audit in a consumer project declared a shipped deliverable broken while the LOG recorded it verified, and a human caught the contradiction from memory — the throughline failing at its own job. next-audit.md's Compile findings now carries the narrow rule decided 2026-08-02: before reporting that already-shipped work is broken, check the LOG for a prior verification; if one exists and the finding contradicts it, reconcile — say what changed or why the verification no longer holds — never report a bare contradiction. The broad form (reconcile every finding) stays rejected, with the why recorded in the rule: a step that near-always no-ops gets skipped and then means nothing. Docset A frozen; docs-b only. Processed-and-built in the overnight blitz of 2026-08-05 under the softened bar (rule form decided at capture); autonomous run — recorded departure.

**Files touched:** plugin/si-plugin/docs-b/next-audit.md
**Routed to Captures:** none
FAQ: not needed because this governs how Claude compiles audit findings, not anything the user does differently.

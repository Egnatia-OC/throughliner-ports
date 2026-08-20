# b485ee3 — /next can now drop an item /setup would overtake, and no longer claims mail is the only trigger

Filed from INBOX mail sent by a consumer project, which flagged it as the less clear-cut of their two findings and possibly working as designed.

What happened there: their project's recorded plugin version was behind the installed one, so `session_start` correctly said /setup wanted a session of its own. /next then presented a run as normal. Its top item was a fix to a stale description inside CLAUDE.md's plugin-managed block — exactly what /setup rewrites, from a template already carrying the correct text. The item was void before the run began, and the run had to be closed with nothing built to free /setup.

Nothing malfunctioned, which is why it is a design question rather than a bug. Each part did its job. But `session_start` already knows the project is behind, and /next's pre-flight had no branch that said so when presenting a run.

**Their fix is narrowed rather than adopted, answering the cry-wolf objection they raised themselves.** The branch fires only where an item in *this* run names a file /setup rewrites — a read of that item's Files line, not a judgment about what counts as plugin-managed content. It fires on the collision, never on every run in a behind project, because a warning that appears whether or not it applies is one people learn to read past.

**And it reuses an existing mechanism rather than adding one.** `next.md` already carried a drop-an-item-from-this-run recommendation for waiting mail, stated as **the one thing** that may drop an item from a run. This becomes its second trigger, and that "one thing" claim became false — so it was rewritten rather than left standing, which is the repeal-trace discipline shipped elsewhere in this same run applied to this item's own ripple.

One recorded objection is dead: pointing a user at /setup would send them into a denial, which stopped being true when [scope-lock-blocks-setup] shipped. No hook change either — `session_start` already emits the outstanding-setup fact.

**This run is the second instance the item cites, and it fired here before the rule existed.** /setup has been outstanding on this project since 1.12.0, and [missed-spec-write-interrupts-the-run] in this same run named `CLAUDE.md` and `CLAUDE-TEMPLATE.md`. The collision was raised with the user when the run was presented, and she chose to build it.

**Files touched:** `plugin/throughliner/docs-b/next.md` (the present-the-run beat, and the "one thing" sentence), `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies. SPEC.md is not listed — its sentence was rewritten in the planning session that kept this.

**Routed to Captures:** none.

Rule gate: run — admitted as a second trigger on next.md's existing drop-from-this-run mechanism, so no new mechanism and no always-loaded slot spent. **The eviction is that sentence's "the one thing" claim**, which becomes false and is rewritten rather than left standing. Failure evidence is two instances: the reporting project's void run, and this project sitting in the same state today.

Tick: done, confirmed — the retired claim was grepped for across `docs-b/` afterwards and no longer appears.

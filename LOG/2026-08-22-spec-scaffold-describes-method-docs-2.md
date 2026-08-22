# [HASH] — Fresh SPECs no longer get a "Project docs" section; the migration reports one where it stands

A consumer's user noticed her SPEC describing the workflow's files rather than her product, and the staleness was the sharper half: the section copies the queue's structure, which is what changes between format epochs, and the migration correctly never touches it — so the stale copy survives every migration by design. The keep chose dropping the section: the managed CLAUDE.md block is the right home for the three-doc description (method-owned and refreshable), and SPEC can never get a managed region, because method-owned text in the user's product truth is the defect itself.

Built: the SPEC scaffold's "Project docs" section removed from setup.md; the migration's retired-terms report step gains one detection — a "Project docs" section in a consumer SPEC is reported as method-machinery description, naming the managed block as where it now lives, edited never. CLAUDE-TEMPLATE.md verified: the managed block already carries the three-doc description, so nothing was added. The sweep for the same shape ran clean — the QUEUE section preambles and LOG index header are method boilerplate the migration refreshes by re-copy, so they cannot strand the way SPEC's section did; no captures needed.

Tick: done, confirmed — scaffold section gone, report entry in place, template verified, sweep clean.

**Files touched:** plugin/throughliner/docs/setup.md; plugin/throughliner/templates/CLAUDE-TEMPLATE.md verified unchanged
**Routed to Captures:** none — the sweep was clean
Rule gate: run — amends setup.md's SPEC scaffold and the migration's retired-terms report step, their named parents; the eviction is the scaffolded "Project docs" section itself; no always-loaded rule touched. Failure evidence: the consumer's reported stale section, surviving migration by design.
FAQ: not needed because the migration report moment already exists; nothing a user does changes.

# 5993a10 — The scaffolded queue header stops telling every consumer that uncleared red flags live in Processed

`setup.md` scaffolded the Processed-section header with *"a work item carrying a `Red flag · State: cleared/uncleared` marker"* — but the behaviour rules say an uncleared flag **never** sits in Processed: a flag is cleared at processing, and an item that cannot clear one returns to the bottom of Unprocessed rather than moving forward. So `cleared` is the only state that section ever carries.

**Why this one mattered more than an ordinary wording slip:** every /setup shipped the contradicting text into the consumer's own QUEUE.md, where it outlives any fix to the docset. A consumer reading their own queue header would learn the wrong model of the method's central risk guarantee, and no later plugin update reaches that file.

The scaffold now says what is true, and says the complementary half too — an uncleared flag waits in Unprocessed — so the reader gets the whole rule rather than a narrowed one.

`migrate-checklist.md` allowed the full enum on items routed to either section without restating the constraint. It now states it in the section table (a red-flagged item in Processed is always `cleared`; Unprocessed is the only section an uncleared one may sit in) and adds the migration-specific consequence, which is the part a checklist actually needs: **a converted item carrying an uncleared flag goes to Unprocessed whatever the old queue implied about its readiness**, because clearing a flag is a decision the user makes at processing and a migration is not processing. If the old queue had a flagged item among its ready work, that is exactly the case the rule exists for — route it to Unprocessed and say so when presenting the converted queue.

A third site was caught by the same reasoning while working an adjacent item: `CLAUDE-TEMPLATE.md` carried the same `cleared/uncleared` phrasing and was corrected too. That is the ripple this run's new grep rule exists to catch, found the way the rule prescribes rather than by luck.

**Files touched:** `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/docs-b/migrate-checklist.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`
**Routed to Captures:** none

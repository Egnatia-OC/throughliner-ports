# [HASH] — Below the cleared-to-run line now means blocked by a named queue item and nothing else, enforced by a lint on a restored `Blocked by:` field

Alex's rule, in her own words: nothing is ever supposed to be below the line unless something in Unprocessed blocks it, and if the blocker is a thing in the world then it should be described in Unprocessed so that it actually gets asked about in /plan.

What the method did instead was record the blocker as a *sentence* inside the shelved item — "cleared once [slug] is built and verified", "after a full computer restart" — which /plan re-read and classified each session through a four-way test. The blocker was therefore never work anyone could pick up. It was a note inside another item.

The failure that proves it came from this queue. `[statusline-context-reader]` sat below the line for weeks with a genuine user action buried in its lift-condition sentence, and nothing ever acted on it, because a sentence inside another item's prose is invisible as next-work. Filing it as its own `[user]` line on 2026-08-09 made it visible immediately. One item's prose had been holding another item's job.

The mechanism restores `Blocked by: [slug]` as a real field with a lint behind it, and that **reverses `ee99142` (2026-07-31)**, which ruled out dependency headers and any dependency lint on the grounds that they would resurrect the stale-header machinery the two-section recut removed. The reversal is argued rather than assumed: that decision had itself been reversed once at `f832385` on the evidence that prose dependencies kept failing, and the emergency revert removed the field by accident rather than by decision. The staleness objection is what the lint answers — a header goes stale silently, a slug reference that must resolve does not.

One judgment had to be made during the build. The item asked for a blocker that "resolves and sits above the item", which cannot be literal file order: Unprocessed sits below Processed in the file, and an Unprocessed blocker is the rule's own recommended shape. So above-ness is enforced only *within* Processed, where position means build order, and a blocker in Unprocessed passes by construction.

The migration ran in the same build rather than being left as follow-up, so the queue never held two models at once: five below-line items converted from bold prose to the canonical field.

What this retires is larger than what it adds, which is why it survived the admission gate while the corpus is over its instruction ceiling: the four-way classifier, the consolidated user-only question, and the downstream-action test all go. The last of those is retired by construction rather than by decision — a thing in the world must now be an item before anything can be blocked on it, so a condition waiting on an action nobody filed can no longer be written.

**Files touched:** `plugin/si-plugin/hooks/post_tool_use.py` (`_check_blocked_by()` with four reported faults, `BLOCKED_BY_LINE`/`SLUG_REF`, a capture group on `SLUG_AT_END`, a `section` key on work-item blocks); `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plan.md`, `done-plan.md`; `SPEC.md`; `FAQ/faq.md` and `FAQ/index.md`; `plugin/si-plugin/templates/faq-template.md`; `QUEUE.md` (the migration).

**Routed to Captures:** `[blocked-by-lint-blind-to-in-flight-items]` — the new lint calls a correct reference broken while a /next run holds the blocker in `_build.md`, which is wrong in the most misleading direction available, since it fires exactly when the blocker is being built.

FAQ: updated — "What does Parked mean in the queue?" replaced with "What does it mean when work sits below the 'cleared to run' line?" in the method's own FAQ (the old entry described a Parked subsection that no longer exists), and the consumer template's equivalent entry rewritten around the named-blocker rule.

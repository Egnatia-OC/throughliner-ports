# d5378c7 — FAQ audit: the project copy is the fossil, eight of its 22 entries are wrong, the template is current; recommend rebuild-by-replacement and a grouped index

The audit's opening premise-check confirmed the spot check: the shipped template (`templates/faq-template.md`, 66 entries after this night's additions, maintained continuously through 2026-08-04) is the current document, and the project's `FAQ/faq.md` is two months behind — base last refreshed 2026-06-18, with only three new-rule entries appended since. Every session pointed at the project copy by session_start has been reading retired machinery described as current.

What's wrong: eight of the project copy's 22 entries describe things that no longer exist — Batches with Build/Test/Audit subheadings, `/next freeform`, the Red flags section, the Deferred tests section, "Parked" with its reason-line formats, the spec-edit-batch answer to editing SPEC, `_plan.md` as promoted/parked/dropped tracking, and batch-scoped file asks. The template's only blemishes are two colloquial uses of "parked" for below-the-line waiting and a deliberately historical push-marker note. What's missing from the project copy: roughly forty topics the template already covers; nothing user-facing was found missing from the template itself.

Recommendation (for the user's call — deliberately not acted on): rebuild by replacement — copy the two templates over the two project files and record in CLAUDE.md that the project copy is a mirror refreshed whenever the template changes — plus a grouped index (five or six plain headings) in both copies, since a 66-link flat list in accretion order fails the reader the FAQ exists for. The full findings sit as a consolidated set in [faq-backfill]'s queue block, which becomes the build once approved; its spent blocker line was replaced by that set.

Run in the overnight blitz of 2026-08-05 (autonomous run — recorded departure). The bulk-approval step could not run live; the findings await the user in [faq-backfill].

**Files touched:** none edited by the audit itself — read FAQ/faq.md, FAQ/index.md, templates/faq-template.md, templates/faq-index-template.md, git history of all four, SPEC.md. (QUEUE.md gained the findings via [faq-backfill]'s block.)
**Routed to Captures:** the consolidated findings set, into [faq-backfill]'s scope per the item's own destination directive — not as separate Unprocessed captures
**Approval outcomes:** deferred to the user's morning /plan — the run was unattended; no finding was dropped or reworded
FAQ: not needed because an audit edits nothing — its findings feed [faq-backfill], which will carry the FAQ work itself.

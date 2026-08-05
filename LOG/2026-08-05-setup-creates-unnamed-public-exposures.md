# [HASH] — /setup's Step 3b now names the two exposures publishing creates: the commit email (with the noreply option) and the planning record

The method created repositories and their first commits without ever mentioning who the commits are attributed to, and offered public-repo setup without saying what a visitor actually finds. The commit address is the one exposure no later file edit can fix — before the first commit it's one `git config` line, after it it's a full history rewrite — and two projects (a consumer's, and this repo on all 385 commits, publicly) are already past that free window.

docs-b/setup.md's Step 3b grows from three things to four: after the visibility detection, a new commit-identity step runs `git config user.email`, tells the user in one line what address every commit will carry, and names GitHub's noreply option — on every branch, not just public ones, because a private repo can go public later and nothing re-checks history. And the public-repo offer now carries one framing sentence: most of what a visitor finds is the planning record itself — the spec, queue and log with every decision and rejected alternative — not a leak, but a decision worth making consciously rather than by default. Both fixes land at Step 3b rather than `git init` because that's the same session, before the close's first commit, with the user's attention already on publishing.

Left as a migration concern, per the item: projects adopted before Step 3b shipped (2026-08-04) never met it at all.

Built in the overnight blitz of 2026-08-05 (autonomous run, approvals deferred — recorded departure).

**Files touched:** plugin/si-plugin/docs-b/setup.md (Step 3b), templates/faq-template.md (extended entry), SPEC.md (the private-information paragraph now names the commit-email step)
**Routed to Captures:** none
FAQ: updated — "Why does setup check whether my code is public…" extended with the email-address and planning-record paragraphs (template copy; project copy awaits the audit-recommended rebuild).

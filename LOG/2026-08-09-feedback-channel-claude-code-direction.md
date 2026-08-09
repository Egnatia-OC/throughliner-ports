# [HASH] — The feedback channel restored to three ways, with its four field-proven guards and the two posting rules scoped against each other, and `gh` named in the README as optional software

The design was settled, field-tested end-to-end on 2026-08-04 — a real report split into a strengthening comment on an existing issue plus one new issue — and built on 2026-08-05 at `d9162e4`. The emergency revert removed the build. The original capture survived because it predates the revert point, so the queue was asking for work that had already been done, which is the shape this whole run was recovering from.

The discriminator is now three-way rather than two: the user's **app** stays as ordinary work in their queue; **the method** routes out to flintcraft.tech/report; **Claude Code itself** — the harness the method runs inside, its viewer, its links, its hooks machinery — routes to a GitHub issue on `anthropics/claude-code`. When genuinely unsure between the three, ask rather than guess: a wrong route either buries method feedback in an app queue or pushes the user's own work out to a stranger.

The four guards on the Claude Code branch were all proven by the live filing rather than predicted, which is why they are stated as earned rather than as precautions. Offer to file directly only where `gh` is installed and authenticated, with a draft-for-the-user fallback so the offer never simply fails. Approval-before-post is non-negotiable — a GitHub issue is public and permanent under the user's identity. Duplicate-check first, and recorded as a guard that *shapes* the report rather than merely avoiding repeats: knowing the adjacent issues is what let one report distinguish itself and survive triage. And scrub by construction, with the counter-intuitive case stated plainly — a report is *about* sensitive content more often than it contains any, so it describes the sensitivity without demonstrating it.

The two posting rules genuinely differ, and that is now written down with the reason each is as it is, because a later session would otherwise "reconcile" them into one. The method report is pasted by the user because flintcraft.tech/report is a web form Claude cannot submit. The Claude Code report is posted by Claude after explicit approval, because `gh` can post it and a non-coder should not be sent to a GitHub form. Both keep the same guarantee — nothing leaves without the user seeing the exact text and saying yes — and only the mechanics differ.

The README half is new rather than restored, and its framing was the point: `gh` goes under **optional software that unlocks a capability**, never as a prerequisite. Without it the channel still works by draft-and-paste, so listing it as required would both misrepresent it and put a terminal step in front of a non-coder who does not need one. Worth naming so it is not scoped out later: the same tool is what makes repo work Claude-doable, and the over-tagging failure this queue already records — "create a private GitHub repo" filed as user work — is exactly the case `gh` answers.

`d9162e4` is a twelve-item blitz commit, so the graft was selective. Two of its plugin-behaviour.md hunks are unrelated work — the result-set destination rule, and adding "close-out" to the background-vocabulary list — and were left for the recovery sweep rather than swept in because they happened to sit in the same diff.

Noted and deliberately not folded in, as the item directed: README's Tested environment still names Claude Opus 4.8, stale since the docset-A retirement. That belongs to `[revert-induced-doc-drift-sweep]`.

FAQ: updated — the method-problem entry rewritten to the three-case routing test and retitled ("Something is broken or confusing — where does it go?"), covering the `gh` offer, the fallback, the duplicate search, and why `/bug` is never the method route. Index line retitled to match.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `SPEC.md`, `README.md`, `plugin/si-plugin/templates/faq-template.md`, `templates/faq-index-template.md`

**Routed to Captures:** none

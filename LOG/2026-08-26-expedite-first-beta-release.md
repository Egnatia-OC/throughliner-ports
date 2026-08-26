# [HASH] — Beta day settled: release today from the current build, beside an untouched beta chain, with the `#beta` install pin advanced

The anchor record for the beta-day decisions; the sibling entries for [install-route-latest-release-check], [onboarding-post-claims-unreleased-popout] and [beta-branch-install-pin] cite it.

Alex's decision, her framing "fake it until we make it": the first beta releases today, Wednesday 2026-08-26, from the current build — she tested /plan, /next and /done on it and judges it almost stable; the announcement had already gone out (recovered into `2026-08-26-beta-announcement-recovered.md` with its register line). The reach-back to an older version was weighed and closed: the four failed-build transcripts describe the old version, and the pop-out onboarding post would be false for the beta's whole life. Two small pieces of work run ahead of the release (the walkthrough-heading patch and the install fixes); the transcript rescan is deferred until she supplies the files.

The beta chain stays exactly as wired — the release proceeds beside it, not through it. Her correction mid-processing reframed the channel model: main is the dev channel, the release is an event and artifact, and no installer through the marketplace route ever touches the release zip — which surfaced that the published install route serves main, not "the beta". That produced [beta-branch-install-pin] on her instinct ("or else people will just always end up with the most recent one on main"): only a git ref marks a commit, so the `beta` branch is created at today's release commit and the install docs move to `#beta`, with the smoke test and post edit as her [user] line. The nerds test-rezip channel now exists on the server, locked to the "nerd" role.

Still open, deliberately: the Wednesday stable-label selector and the nerds-list packaging shape, written on the item for the release-cycle and beta-pathway keeps.

**Queue changes:** [expedite-first-beta-release] rewritten to the settled state and skipped in place; [beta-branch-install-pin] and [beta-install-smoke-and-post-edit] filed and cleared; cross-reference written on [beta-tester-pathway].
**Work processed:** partially — decisions recorded, remainder waits on the held keeps.

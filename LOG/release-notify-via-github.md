# 2ccbadf — GitHub Watch → Releases notify route documented; Push ritual cuts a real Release

Alex wants her users to sign up for a heads-up when she ships a new version. GitHub supports this natively — a user clicks Watch → Custom → Releases on the repo and is emailed on each published release — so no custom infrastructure is needed for a first version. (The email-list option, better UX for non-coders, was weighed and deferred as the heavier later choice, alongside the parked [consumer-plugin-feedback-channel] contact form.)

Two pieces make the native route work, both landed here. First, README.md gains a plain-English "Get notified of new versions" section: click Watch on the plugin's GitHub page, choose Custom, tick Releases, click Apply — noting it needs a free GitHub account. The exact Watch-menu wording was verified against the live GitHub UI via web search (Watch → Custom → tick Releases → Apply). Second, the CLAUDE.md Push ritual gains a step after `git push` to publish a GitHub Release (tag and title = the new version, the zip `plugin/si-plugin.zip` attached, notes drawn from the release's LOG entries / commit), because Watch → Releases fires on a published Release, not on a plain `git push`. If `gh` isn't authenticated in the session, the step falls back to telling Alex how to publish the Release from the GitHub web UI, so it never silently does nothing. A FAQ entry — "How do I find out when there's a new version of the plugin?" — points users to the Watch → Releases method.

The README/FAQ user-review (Alex reads the new wording and says if anything's off) is a review, not a pass/fail test, so it's held as a plain reminder. The release-cutting step itself is confirmed by observation at the next release push and was written to Deferred tests.

**Files touched:**
- README.md
- CLAUDE.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none

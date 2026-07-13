# [HASH] — Added the consumer plugin-feedback channel: discriminator + scrubbed report routed out to flintcraft.tech/report

Built the plugin-side half of the consumer feedback channel — a way for a consumer's Claude (or the consumer) to report a *method* problem without polluting their own app queue. The crux is a discriminator: "is this about how the method works, or about what I'm building with it?" — the first routes OUT, the second stays an ordinary capture. Two trigger paths (user-raised; Claude-noticed, offered once) produce one scrubbed-by-construction report: it names what the plugin did vs expected, the skill/step, and the version, and never app names, file contents, secrets, or queue/SPEC content. Claude drafts and shows it; the user pastes it at flintcraft.tech/report — never auto-submitted, since the report leaves the machine for a public destination and the user's review is the human scrubbing backstop. Carries an open-red-flag rationale: downstream issues can be public, so a leak would be a privacy breach. Noted that Claude Code's `/bug` is the wrong channel (it reaches Anthropic, not the plugin author). The form→GitHub-issue automation (part b) stays a separate flintcraft.tech web project, not this repo.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — new "Consumer feedback channel" section
- SPEC.md — "Reporting a plugin problem" feature
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line

**Routed to Captures:** [redflag-resolution-not-forced-at-ship] — a red-flag line shipping and leaving the queue without an explicit resolve/accept decision being forced at close

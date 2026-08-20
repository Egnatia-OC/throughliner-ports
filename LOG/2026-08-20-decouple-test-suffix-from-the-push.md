# [HASH] — The push's version-clean step repealed; the release bump strips the test suffix instead

Raised by the user at a close, in her own words: *"I'm trying to decouple the concept of test rezip from push because I am just rezipping so much."*

**Two things were checked before filing rather than assumed.** The clean was not a leftover from when push and release were one event — it was *added* when they were decoupled on 2026-08-04, to close the window the new ordering opened. And stripping at the release was refused that same day, on the ground that a `-testN` would then sit on the public remote between releases, as `1.16.0-test4` once did.

**What is new is frequency.** That refusal reasoned about occasional rezips, and she now rezips at every run — so a clean step was running constantly to prevent something that turns out not to matter.

**Her decision: just untidy. The clean moves to the release.** That reverses the same-day refusal, and legitimately rather than arbitrarily: **the refusal rested on the suffix being harmful, and the owner of the repository says it is not.** The premise is removed, not the reasoning overruled. So a committed `plugin.json` carries `-testN` between releases, and the release bump strips it.

One interaction, already favourable: the content stamp drops the version key, settled earlier the same day, so committing a suffixed version cannot report a stale host.

**The Files line was derived by grepping the suffix across the repository rather than from the discussion — which is what reached the third site.** `CLAUDE.md`'s Push section loses its first step and the two paragraphs justifying it, and its clause about recognising a `-testN` diff at a close is reworded, since the file is no longer dirty-then-cleaned but simply committed as it stands. `resources/release-ritual.md` gains the strip at the release bump, worded as stripping any suffix and *expecting* one rather than treating its presence as a sign the push was skipped. And `plugin/throughliner/hooks/session_start.py`'s comment explaining the stamp's version exclusion said *"the rezip sets a `-testN` suffix, the push resets it"* — which became false and was corrected. `pre_tool_use.py`'s rezip write-permission describes the rezip's own write and is genuinely unaffected: read, not assumed.

Host-only throughout: consumers neither rezip nor release.

**Files touched:** `CLAUDE.md`, `resources/release-ritual.md`, `plugin/throughliner/hooks/session_start.py`.

**Routed to Captures:** none.

Rule gate: run — **the disposition is an eviction**, the push's version-clean step repealed outright with the two paragraphs defending it; no rule authored, and the release ritual gains a step rather than a rule. Failure evidence is the frequency change the user named, plus this project getting it wrong at the last close.

Tick: done, confirmed — the suffix string was grepped across the repository, which is what reached the third site.

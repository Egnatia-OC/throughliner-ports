# e711b9f — The `.in_use` exclusion shipped broken and was caught by the rezip's own stamp comparison

A follow-up to the close immediately before this one, recorded separately because it corrects work that commit reported as verified.

**What was wrong.** `content_stamp()`'s new exclusion matched `.in_use` as a **filename**. It is a **directory**, holding one marker file per live session, so the exclusion did nothing: the walk descended into it and hashed its contents. The stamp then moved with how many sessions were open — arguably a worse failure than the original bug, since it drifts continuously rather than on a reinstall.

**Why it wasn't caught before shipping, which is the part worth keeping.** The fix went out with a test written deliberately alongside it, on the reasoning that a future CLI artifact of the same kind should be caught by a check that already runs. That test created `.in_use` as a file. The exclusion matched, the suite went green, and the LOG entry recorded the fix as verified in good faith. **The fixture and the code under test were built from the same wrong belief, so they agreed** — and a green self-built fixture is indistinguishable from real coverage while actively discouraging the check that would find the truth. An untested fix at least looks untested.

**What actually caught it** was comparing the target's stamp against the installed snapshot's after the rezip — a step nothing in the ritual required, run only because the stamp mechanism was the thing being tested. The numbers made it unambiguous: before the correction the installed snapshot hashed to `9a90621e3ab9` against the identical target's `886f06749a71`; after it, the installed snapshot hashed to exactly `886f06749a71`, the value the target held at install time. Byte-identical directories, identical stamps.

**Verified against the world rather than a fixture this time**, in three places: the two real directories agree (`5dcdb7b70d62` on both after the second rezip); the arrived session-start context reports that same value; and it held steady across a full app restart with sessions live in the marker directory, which is precisely what it failed to do before.

The test was rebuilt to the real shape — a directory containing session markers, plus a second marker added to prove the stamp doesn't track how many sessions are open, with the flat-file form kept as belt and braces in case the CLI ever writes it that way.

**Files touched:** `plugin/si-plugin/hooks/session_start.py` (`.in_use` pruned from `dirnames` alongside `__pycache__`, filename exclusion kept; docstring records the shape and the failure), `resources/testing/hook_schema_check.py` (the stamp test rebuilt against a directory fixture with two markers).

**Also carried in this commit:** the previous session's hash backfill across eight LOG files.

**Out-of-shape write, named as this close's own record:** this fix was made with no work item and no scope-locked run, in the tail after a /done had already committed. It qualifies as the sanctioned build-completing case — a genuine bug in what the just-closed build was meant to deliver, rather than new scope — and it could not wait for a work item, because the broken exclusion was already installed and its wrongness grew with every session opened.

**FAQ:** not needed because the build stamp is developer-facing machinery for this self-hosting project; a consumer sees the line but never compares it against a target.

**Routed to Captures:** two, deliberately split so the concrete fix isn't held up by the judgment call.

[self-built-fixtures-assert-the-assumption] — the generalisable lesson, filed for /plan rather than fixed here, with the candidate rule and its honest tension (fixtures exist so tests don't depend on the world, so a rule demanding observation everywhere would be wrong) both recorded.

[rezip-ritual-lacks-stamp-comparison-step] — the user's own call at this close: the step that caught this bug is the one nothing in the ritual requires. One command after the reinstall, asserting target and installed stamps match, in both the rezip and release rituals. Its limit is recorded with it — it proves the snapshot took, not that the stamp function computes the right thing, which was the bug underneath.

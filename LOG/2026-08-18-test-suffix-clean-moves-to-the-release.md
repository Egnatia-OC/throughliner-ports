# 02ec308 — the version clean moves from the push to the release, reversing a refusal made the same day on a premise that is now gone

The user rezips at every run, so a clean paid at every push is paid constantly. Her framing: decouple the test rezip from the push.

Two things were checked before this was settled rather than assumed. The clean is not a leftover from when push and release were one event — it was *added* when they were decoupled, to close the window the new ordering opened. And stripping at the release was refused earlier the same day, on the ground that a `-testN` would then sit on the public remote between releases, as one did once.

**Her decision reverses that refusal legitimately rather than arbitrarily: the refusal rested on the suffix being harmful, and the owner of the repository says it is only untidy.** The premise is removed, not the reasoning overruled. So a committed `plugin.json` carries the suffix between releases and the release bump strips it.

**The ripple was traced by grep, which is the limb cleared two items earlier in this same session, and it reached a file the discussion never would have.** `session_start.py` explains the content stamp's version exclusion with the words "the rezip sets a `-testN` suffix, the push resets it", which becomes false. The two other code references describe the rezip's own write and are unaffected — read rather than assumed.

One interaction was already favourable: the content stamp drops the version key, settled today, so committing a suffixed version cannot report a stale host. The disposition's eviction is the push's version-clean step and the two paragraphs defending it.

**Queue changes:** [decouple-test-suffix-from-the-push] settled and cleared.
**Work processed:** kept — [decouple-test-suffix-from-the-push].

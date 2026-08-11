# [HASH] — A Stop hook now catches a report naming work that isn't there, and the write-first test was restated rather than excepted

Captured by the user on 2026-08-10 from a live instance and their report that it had been happening for up to five days. Kept as one item at their instruction. Mixed authorship: the failure and its dating are the user's; the mechanism and the restatement are Claude's.

**The failure.** Under show-first the text appeared in chat before the write, so reporting and showing were one act and a report could not precede its write. Under write-first the report follows the write — so a turn that never executes the write can still emit the report, and the two are indistinguishable to the user. The live instance: Claude wrote "Filed as [a-slug]" having made no write at all, and the user acted on the false report before the item existed.

**The three genuine doc contradictions were fixed; two reported ones were left alone deliberately.** `done.md`'s roll-up commit message and `next-audit.md`'s report-instead-of-edit shape are correct as written — a commit message is a structural show-first case, and an audit has no write to point at. The three real ones were `migrate-checklist.md`'s two lines, `setup.md`'s conversion trigger, and `plan.md`'s stale "draft-approval step" reference.

**The migration question is settled by restatement, not by a third exception — and this is the part worth carrying forward.** The item asked whether a whole-queue conversion is a third show-first exception, or whether the revert test needs a size dimension. Applying the exception admission test shipped earlier in this same run: limb 1 says restate the rule so it needs no exception. It restates. The test was "does a revert fully undo it?", which quietly assumed a safety net; what it always meant is **"is the previous version recoverable without the user's help?"** A project being adopted or migrated may not be a committed git repo at all, so its old queue may not be recoverable — the conversion is show-first *by the test*, with nothing added. Size never entered it. No exception was admitted.

**Sharper wording was already a spent remedy**, which is why the second half is a mechanism. The write-then-verify-then-point rule is shipped, always-loaded, correctly worded, and still failed live — the same shape as [invented-rationale-compounds-past-the-shipped-rule].

**The insight the mechanism turns on: the claim is mechanically checkable, so no semantics are required.** The shipped rule already requires a report to name what landed, which in practice is a fixed shape — "filed as [slug]". A slug either exists in QUEUE.md as a `#### ` heading or it does not. So a false report is not a judgment about meaning; it is a named artifact that is absent. This is the check-the-world rule the method already applies to `[user]` items, turned on Claude's own claims.

**Why `Stop` and not `PreToolUse`.** `resources/research/hook-enforced-doc-reading.md` establishes that PreToolUse can read the transcript and deny. That is the wrong surface: a false report is text with no tool call attached, so a hook gated on tool calls never fires on it. `Stop` receives `last_assistant_message` — the complete final response, handed over directly, no transcript parsing — and `{"decision": "block", "reason": …}` does not end the turn, so the write can be made and the correction reach the user before they act.

**Two things built in deliberately.** A `stop_hook_active`-style flag is not documented, so the hook carries its own loop protection: it blocks once per identical claim, then downgrades to non-blocking feedback. And the limit is stated rather than discovered — it catches reports that *name* the artifact; a vague "I've written that up" escapes it entirely. That is acceptable rather than a hole, because the shipped rule already requires the report to name what landed, so the hook enforces the rule as written.

**One refinement found by testing rather than reasoning.** The first verb list included "logged" and "recorded", which would have fired on /done legitimately reporting that it logged a slug it then removed from the queue. Those verbs are out; the check is queue-specific and a LOG entry is not a queue heading. Tested against the real failure shape, a /done-style log-then-remove report, a hedged future claim, a bare prose mention, and the loop downgrade — only the false filing claims block.

**Files touched:**
- `plugin/si-plugin/hooks/stop.py` — new.
- `plugin/si-plugin/hooks/hooks.json` — Stop registered; description updated; JSON re-parsed to confirm valid.
- `plugin/si-plugin/.claude-plugin/plugin.json` — description now says four hooks.
- `plugin/si-plugin/docs-b/skill-nonspecific-rules.md` — the write-first test restated.
- `plugin/si-plugin/docs-b/migrate-checklist.md`, `setup.md`, `plan.md` — the three contradictions.
- `SPEC.md` — hooks list now three enforcing plus one advisory, with a full `stop` entry naming its limit.
- `README.md` — plain-English paragraph on the report check.
- `FAQ/faq.md`, `FAQ/index.md` — new entry on why Claude sometimes corrects itself about a filing.

**Routed to Captures:** none.

FAQ: updated — new entry "Claude sometimes stops and corrects itself about something it said it filed. What's happening?" A hook that can interrupt a turn is visible to the user, so it needed one.

The anchor question stays answered as it was: a plain link with the line named in prose, because nobody has observed whether Windows passes a line number to a file type's default handler.

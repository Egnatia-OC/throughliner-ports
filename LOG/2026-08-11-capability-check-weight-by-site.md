# 7c9922a — The capability check splits by site: thorough at /plan, light at /next [capability-check-weight-by-site]

Captured by the user mid-/plan, from their question about what a tool-availability check costs and where it should run. Mixed authorship: the question and the instruction to file are theirs; the weights are Claude's answer.

Built in one pass with [what-would-answer-this-as-a-shared-trigger], as both items instruct — they rewrite the same guard, and built apart the second edit would be written without sight of the first.

**What was wrong.** The over-tag guard fired at two sites with identical wording, so both implied the same depth. Measured in the session that filed this, the cost is asymmetric: searching for one candidate tool is nearly free, while *trying* it is not — that meant loading a tool's schema and running a reproduction to rule two out.

**The split survives; what the thorough version contains does not.** This is the reshape, and it rests on evidence from the same session. A `[user]` line was filed after an honest, thorough check — its own text records that the filesystem was searched and returned only binaries and caches — and the item was deleted hours later when one command answered the question. **Depth was not what failed.** The check searched for *where the setting is stored*, which is the correct search for the question as posed and is why it looked thorough and came back empty. What it never did was ask *what would tell me which isolation model is in force* — a question whose answer has nothing to do with settings files.

So the heavy side is **reframe-then-search**, not try-the-tool. Restating the question is *cheaper* than experimenting, not more expensive, and it is the step that would have caught the miss. Trying a tool stays permitted at /plan where it is quick, but it no longer distinguishes the two sites.

**The light side is unchanged:** at /next, name the tool and confirm it is absent. No reframe, no search, no experiment — the user is not in the room and a run should not stop to explore.

**Why /next's check is not simply dropped**, which the user's question raised. It has already earned its keep: it caught an item wrongly tagged `[user]` when a session using the plugin was itself the observation. Removing it would remove the only backstop for a tag written before the guard existed or by a session that skipped it.

**An inventory sweep is rejected outright and should not be re-proposed.** Enumerating everything available — around ninety deferred tools in one session, most schemas unloaded — is expensive and stale by the next session. The check is aimed at one job or it is not worth running.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/next.md`
**Routed to Captures:** none from this item

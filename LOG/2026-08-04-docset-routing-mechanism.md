# [HASH] — Made the docset redirect self-verifying against the `docset: B` stamp the docs already carry

Each SKILL.md hardcodes its procedure doc under `docs/`, and a hook cannot rewrite those files, so routing a 5-series session to docset B works by injecting an instruction to substitute `docs-b/`. That holds only as long as the model follows it — and the real complaint was never about direction, it was about detection: a session that skims the directive reads docset A while believing it read B, and nothing notices.

The fix cost nothing to build because the evidence was already there. Every one of docset B's eleven docs opens with `docset: B` in its frontmatter, and docset A's docs carry no frontmatter at all — checked, not assumed. So absence of the stamp is itself a clean discriminator. The directive now instructs the session to confirm the stamp of the doc it actually opened, rather than trusting the instruction it was handed.

Failure is reported to the user in plain words while success stays silent, which keeps the routing internal — the standing rule — without letting a silent failure hide behind that same rule.

Built directly after the payload fix, deliberately. That item replaces the inlined rules with a read instruction, creating a *second* redirect with the identical skimmable failure mode. Its own text said the two must be built together or adjacently, and shipping the redirect without its detection would have traded a loud failure for a silent one. The behaviour-rules directive therefore carries a matching self-check of its own.

Two things recorded as still standing: the rejected `docs/`↔`docs-b/` invert (it would make the safe fallback depend on the redirect being followed, which is the wrong side to bet on), and the parked placeholder option, which still rests on an unverified assumption about variable expansion inside a SKILL.md path.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`
**Routed to Captures:** none from this item

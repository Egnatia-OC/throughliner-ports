# 3cc6f44 — Record filenames carry the item's full slug with a kind suffix, and the digest reads them

The digest attributed a record to a queue item only where the filename was exactly `<date>-<slug>.md`, so two ordinary shapes were invisible to it: the overwrite guard's numeric suffix, and build records filed under shortened names. The consequence was observed live before this was filed — [weekly-release-cycle]'s blocker printed as "only processed, not built" when its build record existed, which is the misreading the record-kind field exists to prevent, and it was feeding a lift decision.

The suffix scheme is the user's: kind rather than number. A bare name for the first record; where that is taken, the second carries `-plan` or `-build`, because a number is arbitrary where a kind explains itself. Legacy `-N` names stay tolerated so existing history still reads, which is why the stripper matches three fixed shapes rather than a general pattern — prefix-matching arbitrary suffixes was refused at processing, since a slug extending another slug would then misattribute.

Fifteen shortened records from 2026-08-22 were renamed to their full slugs with `git mv`, so history followed the rename instead of breaking into a delete and a create, and all fifteen index lines were repointed in the same move. One record was deliberately left alone: `2026-08-22-lint-three-checks-build.md` covers three queue items and has no single slug to be named for, so the rule does not reach it.

**This close is the rule's own first test, and it passed.** The overwrite guard refused the bare `2026-08-23-log-record-kind-suffix.md` because this morning's planning session already holds it, and offered `-2` — the legacy shape. The record was written as `-build` instead, per the rule shipped hours earlier. The guard's suggestion has not been changed to match; whether it should is left as an observation rather than smuggled into this build.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py` (new `RECORD_SUFFIX_RE`, applied in `shipped_slugs`, docstring paragraph on suffixed records), `plugin/throughliner/docs/done.md` (naming block's collision rung replaced, numeric fallback demoted to a second rung, full-slug requirement added), fifteen `LOG/` renames, `LOG/index.md`.

**Routed to Captures:** none from this item.

Tick: done, confirmed — the digest reports [cycles-definitions-and-due-checks] as shipped, no index line points at a dangling filename, and `test_queue_digest.py` passes.

Rule gate: run — amendment to done.md's record-naming instruction, parent named; nothing freestanding and nothing evicted, the digest half being script behaviour rather than rule text.

FAQ: not needed because a record's filename changes nothing a user does.

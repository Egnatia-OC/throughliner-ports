# [HASH] — /next now actually halts on an uncleared red flag, making true a guarantee SPEC and the behaviour rules had been asserting with no code path behind it

Both SPEC and the behaviour rules stated that an uncleared red flag reaching Processed should be impossible, and that if /next ever met one it would stop and surface it rather than building. A grep at `5993a10` found zero red-flag references anywhere in the /next family, and re-verification on 2026-08-09 confirmed it: `next.md`, `next-build.md` and `next-audit.md` contained no mention of red flags at all. The backstop was documentation. It had shipped once as an exit at the run-forming step and was lost to the emergency revert.

The alternative — delete the promise from SPEC and the behaviour rules — was weighed and rejected. The guarantee it backstops is real and cheap: a flag is cleared at processing, so the cleared region is red-flag-safe by construction, and the backstop exists only for the case where that model was bypassed. Removing it would leave an unattended run free to build work carrying an unaddressed data-exposure risk, which is the one thing the whole red-flag model exists to prevent.

The shape of the failure is worth recording, because it will recur in other guarantees: **a backstop for an impossible case never fires, so nothing ever reveals it missing.** Ordinary use cannot distinguish an implemented backstop from an absent one. Only reading the code against the promise finds it, which is why the doc-versus-code comparison is the check that matters here rather than any amount of testing.

The wording was checked against the behaviour rules' existing Backstop sentence — "stops and surfaces it rather than building" — so the procedure and the rule now say the same thing rather than two similar things. SPEC's general risk-surfacing promise was read and needed no change.

**Files touched:** `plugin/si-plugin/docs-b/next.md` (an `UNCLEARED_FLAG` early exit at the run-forming step plus its handler, which halts, names the risk in plain English and recommends /plan).

**Routed to Captures:** none from this item.

FAQ: not needed because the user-visible promise was already documented and already described in the FAQ's red-flag material; this makes the existing description true rather than describing anything new.

# [HASH] — session_start.py surfaces the installed host version; deferred-test convention wording corrected to reinstall-sufficiency across plan.md, done.md, and QUEUE.md

Every /plan had to ask the user which host version is installed before it could resolve the deferred-test roll — recurring friction. The session-start hook already reads the installed plugin version for its drift check; it just wasn't surfaced. session_start.py now appends an "Installed plugin (host) version: <ver>" line (test suffix included) to the adopted-state context, with a note to use it for host-side deferred-test resolution instead of asking the user. The version only is surfaced — the host-vs-target comparison stays Claude's reasoning, because a consumer project has no target to compare against. A hand-maintained record was rejected on purpose: the user reinstalls without Claude in the loop, so a saved value goes stale and would mislead; the hook is the only always-correct source because it runs inside the installed host.

The same root cause produced a wording error fixed in the same batch. The deferred-test convention said host-side work "goes live after push + reinstall," conflating publishing with installing — which is what led a recent /plan to first conclude "nothing rolls" on a perfectly current test host. A private test-build reinstall already makes host-side behaviour live; only the two external marketplace lines need a remote push. Corrected to reinstall-sufficiency in plan.md (Step 1 roll scan and Step 2 roll move — the latter now resolves host-side lines from the surfaced version, with the self-hosting rule host base ≥ target ⇒ all host-side changes live, asking the user only for external events), done.md (the canonical deferral-reason definition), and QUEUE.md's Deferred tests section header. Per the batch, per-line "after push + reinstall" annotations were left as historical evidence — not a per-line sweep — and the same untouched-annotation discipline left done.md's exemplar quote and plan.md's test-category line as-is.

Doc-wording edits are self-verifying text. The version-surfacing behaviour is a host-side deferred line — confirmed once the next reinstall lets a session start show the version and the next /plan resolve the roll without asking.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py — surface the installed host version in adopted-state context.
- plugin/si-plugin/docs/plan.md — Step 1 roll scan + Step 2 roll move reworded to reinstall-sufficiency; Step 2 resolves host-side lines from the surfaced version.
- plugin/si-plugin/docs/done.md — deferral-reason "host-side" definition reworded.
- QUEUE.md — Deferred tests section header reworded.

**Routed to Captures:** none

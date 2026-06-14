# Audit procedure

Execution procedure for audit batches. Reached from next.md after pre-flight checks and scope lock are complete. The output contract defines an audit: findings route through Captures so /plan can convert them into normal batches — no direct edits to the artifacts the audit reads. What gets read varies — procedure docs, the user's spec, code, UI flows, workflow output, any other artifact; the procedure shape is the same regardless: read many, propose many. The audit _build.md carries a `Files:` section with no entries, so the scope-lock holds the session to the method docs (QUEUE.md, REGISTRY.md, LOG/, _build.md) — the strictest setting, matching a session that edits no source files.

## Read the target systematically against the criteria [SILENT]

Read every artifact named by the target. Apply the criteria pass by pass — one criterion across the whole target, then the next, not mixing criteria per artifact. Don't skim; an audit's value is reading what's there. Accumulate observations in _build.md Changes with precise references (file:line for files) so the user can verify each.

## Compile findings [SILENT]

Once the read is complete, group observations into discrete findings. One finding per actionable change. Phrase each as observed + why it matters — the shape a capture takes, since that's where they'll land.

## Present findings one at a time [SEQUENCE, PROMPT]

State the count upfront ("N findings. First: ..."). For each: the observation, the file:line reference, why it matters. Wait for the user's call — **capture** or **drop**. Don't preview upcoming findings.

## Route approved findings to Captures

For each marked capture, draft the wording as a blockquote with a content-type lead-in (**Capture draft:**) for approval, per plugin-behaviour.md (Captures + approval-time outputs). Once approved, append to Captures in QUEUE.md. Tick the finding in _build.md Progress as `captured` or `dropped`.

## Close [BRIEF, PROMPT]

When all findings are handled, tell the user the audit is complete with the captured/dropped counts — each finding was already handled one at a time. Say: "Run /done to record this and commit, or keep reviewing." No chat summary of the routed findings — the LOG entry /done writes is the single session summary.

# 2625fa0 — Kept and cleared: a lint backstop for rule-touching items cleared without a gate disposition

The mechanical backstop won over sharper wording (tenth instance of a correctly-worded rule not firing) and over a plan-close check (fires after /next can already have run, which is what happened). The lint flags at the write, before a run exists: a cleared item whose Files line names a gate-trigger path with no `Rule gate:` line in its block — the same shape as the existing no-build-block flag. Consumer items never name those paths, so the check structurally never fires for them.

Rule gate: run — escalation to a hook; the trigger-path set is the gate's own.

**Work processed:** kept — [keep-step-skipped-gate-disposition].

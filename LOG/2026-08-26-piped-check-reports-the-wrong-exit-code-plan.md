# 0d02b6a — Verification guidance gains the piped-exit-code rule: read a check's status from the tool, never the pipeline

Kept on Claude's recommendation and your agreement. A Gradle failure piped through `tail` reported as a pass — the status belonged to the pipe's last stage — and the tick that followed asserted "done, confirmed", the one false-pass shape worse than no check. The fix, stated as the action in next-build.md's verification guidance: read a check's exit status from the tool itself — bare invocation, or its own status captured explicitly — and trim output separately. The hook suites are invoked as plain `py` scripts by standing rule, so the direct route is safe; the build checks the release ritual's and close step's suite invocations and adds the line only where one could grow a pipe.

**Queue changes:** kept and cleared, in the build set.
**Work processed:** kept — [piped-check-reports-the-wrong-exit-code].
Rule gate: run — amendment to next-build.md's verification guidance; nothing new admitted.

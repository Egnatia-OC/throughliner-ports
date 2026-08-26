# 0d02b6a — Environment check gains the shell-failure trigger: a tool failing from Claude's shell asks, never answers

Kept on Claude's recommendation and your agreement. The Taskflowapp diagnosis settled at processing: the rule was read and still missed because a tool failing from Claude's shell reads as the availability question already answered, when it only establishes "can't run it from my shell". The build rewords next-build.md's before-assuming-absent rule so a shell-side failure triggers the ask (does the user have a route — their IDE, their terminal). Grep at the keep confirmed the rule's words live in next-build.md alone; no hook enforces it. Pairs with [no-home-for-a-projects-tool-facts], placed adjacent so the two build together.

**Queue changes:** kept and cleared, second on the ready list.
**Work processed:** kept — [environment-check-skipped-user-had-to-cite-it].
Rule gate: run — amendment to the existing environment-check rule; nothing new admitted.

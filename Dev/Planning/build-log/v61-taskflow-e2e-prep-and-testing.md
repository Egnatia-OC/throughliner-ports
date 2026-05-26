# v61 — 2026-05-23 — Taskflow E2E prep and testing

*Entry written in v62 — v61 shipped 0060 but context ran out before BUILD-LOG was written.*

**What shipped.** Scope 0060. First real-project E2E test of the plugin against Taskflow. Nine findings surfaced across setup, planning, and session management. Six new scopes created (0063–0068) to address gaps found. Graduation (scope 0059) shelved indefinitely — context in OPEN-QUESTIONS.md. Reference manual gains "sessions are stateless" paragraph. Pre_tool_use.py Windows em-dash fix committed.

**Decisions taken and why.** Graduation shelved because the E2E findings showed the plugin needs more iteration before it's ready for public distribution. The six new scopes address concrete gaps found during testing. The E2E approach (run plugin against Taskflow in a desktop-app burner session, bring observations back to this project) validated as a testing method.

**Pivots and surprises.** Token costs far higher than expected — setup at 163k tokens, planning at 75k+ for a scope-existence check. Prompted scope 0063 (this session's work). Windows em-dash encoding in pre_tool_use.py was a platform-specific bug not caught by tests.

**Carried forward.** All nine E2E findings tracked via scopes 0063–0068. 0060 scope file kept (not deleted at v61 close) because downstream scopes reference its findings.


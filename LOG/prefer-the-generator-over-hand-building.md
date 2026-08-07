# 96166c6 — Paired a don't-hand-build counterweight onto the reach-for-a-CLI rule, and routed stated setup facts into CLAUDE.md

Two failures were tangled together in one reported pain — Claude getting stuck in Gradle configuration on a new Android project while the user repeatedly said they had Android Studio and it changed nothing — and they needed separating before either could be fixed.

**The first is that the generator was never considered.** Almost every project type has a canonical scaffolder that produces a correct starting point in seconds. Hand-assembling the same thing file by file is slower, produces a non-standard layout, and fails exactly where the generator exists to succeed: build configuration. This belongs *on* the existing reach-for-a-CLI rule rather than beside it, because that rule — which corrects Claude not doing enough itself — actively pushes toward this failure by teaching Claude to route around a GUI tool. Fixing one direction without stating the pairing keeps producing the other.

**The second face was nearly missed, and is the higher-value half on the evidence.** A full session transcript the user supplied mid-processing refutes the scaffolding-only framing directly: nothing in that session was scaffolding, the project already existed. What happened was Claude spending most of a build run obtaining its *own* command-line route to two capabilities the user already had working, until the user stopped it. Claude's own words afterwards name it precisely — the item only asked that a way to run the app exist, and it already did the moment the user said "wireless debugging with my Pixel 6". So face 2 fires at *any* point, on a checkable condition: the goal is already met by a tool the user has.

**The second strand is the worse half.** A stated fact about the user's setup did not survive, and better listening cannot fix that — the next session may not hold the conversation at all. Under the method's own routing rules that fact has an owner: it is how Claude should work on this project, so it belongs in CLAUDE.md, which gets read every session. It is asked for at the moment it matters ("Do you have Android Studio installed?") rather than as a standing interview question, because a non-coder cannot answer a general one and whatever they say goes stale.

Every "your tools" entry records how it was verified, in one clause. That section is a list of capability claims — precisely the artifact that goes wrong — so it carries its evidence from the first entry rather than acquiring the requirement later. Two entry kinds, and the distinction matters: a tool the user reports having is evidenced by their saying so; a tool Claude claims to drive is evidenced by having driven it.

The section is a record of what is *available*, never a list of the only tools allowed. "Sanctioned" was the word first reached for and was rejected as wrong.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/next-build.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none

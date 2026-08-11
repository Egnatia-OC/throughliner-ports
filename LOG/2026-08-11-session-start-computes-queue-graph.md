# [HASH] — session_start now emits the queue's dependency facts, and /plan derives the throughput floor from them instead of inventing it

Captured by the user, whose question was whether the dependency graph could be made mechanical and cheap, like the lint, or built into Understudy. The design is Claude's, agreed by the user.

**What the graph was.** Not a file. Whatever you get by reading every `Blocked by: [slug]` line and resolving each slug against the queue. That is deliberate — an implicit graph cannot go stale, which is why the retired `Blocks:` / `Depends on:` headers were dropped — but it meant every reader re-derived it, and when Claude did the re-deriving it cost tokens and reasoning. The session that filed this derived it by hand twice, the first attempt carrying a parse bug that wrongly reported the cleared region as empty.

**The division of labour is the point.** `session_start` already reads QUEUE.md to find uncleared red flags, so this is a second pass over text already in memory. **Anything a hook computes costs no model attention** — it arrives as fact rather than as something Claude must remember to work out.

The hook emits facts only: cleared count, held count, and how many of those held items' blockers sit in Unprocessed. `plan.md` derives the floor from them, because the floor is a /plan concept and the hook runs for every session — a hook telling a /next run to "process at least N" would be narrating something that does not apply to it.

**Emitted even when every number is zero.** "Nothing is waiting on you" is useful, and silence is ambiguous: a computed zero and a check that never ran look identical from the outside. Same reasoning as the FAQ disposition line, which was given teeth for exactly that reason.

**It fixes both floor defects at once, which is the argument for this shape.** The floor becomes derived rather than guessed, *and* it can no longer go unannounced — the filing session's floor was invented at six and then never said aloud. Hook-supplied facts cannot fail either way, and `plan.md` now states both obligations: name what the number was derived from, and say it every session including at zero.

**Why not the lint.** `post_tool_use` fires *after* a QUEUE.md edit, so it is the right place to catch a dangling `Blocked by:` — which it already does — and the wrong place to orient a session that has not edited anything yet.

**The Understudy half stays separate.** A graph a human can look at is something a companion app renders better than a chat line ever will. But the floor is needed *inside* the session, where only a hook reaches. Not a substitute, and not a reason to delay this.

**The output constraint was respected:** hook output is capped at 10,000 characters per command and session_start's output is already substantial, so this is one line rather than a rendered graph.

Verified against the live queue mid-run — (10 cleared, 8 held, 1 blocker in Unprocessed) — and returning None on an unreadable file, so a bad read stays silent rather than emitting a confident zero.

**Files touched:**
- `plugin/si-plugin/hooks/session_start.py` — new `_queue_dependency_facts()` and its one-line emission.
- `plugin/si-plugin/docs-b/plan.md` — the floor derivation, its stated formula, and the always-say-it rule.
- `SPEC.md` — session_start's description names the new line and that it is input, not instruction.
- `FAQ/faq.md`, `FAQ/index.md` — new entry, "What is the 'queue dependency facts' line at the start of a session?"

**Routed to Captures:** none.

FAQ: updated — new entry "What is the 'queue dependency facts' line at the start of a session?"

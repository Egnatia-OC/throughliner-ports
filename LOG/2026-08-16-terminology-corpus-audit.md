# [HASH] — "Session" surveyed across the corpus: the settled vocabulary has three slots and the corpus needs at least six

**The axis was stated before the survey began**, as the audit-axis rule requires: what does each occurrence *refer to* at the site where it fires. Not what it should say. The target vocabulary was already settled by the user — a plan session, a next session, the chat — and she corrected an earlier draft of the item that read as though the answer were known, because an audit starting from "the bare word must go" degenerates into a find-and-replace, which this explicitly is not.

**The headline finding is that the target cannot hold what is there, and it blocks the corrections list the audit was expected to produce.** Alongside the three settled slots, the shipped docs also say **"setup session"**, **"closing session"**, **"freeform session"** and **"build session"** — each a run of a command exactly as a plan session is — and `/rescan` is a fifth command that will need one. A build told to sort every occurrence into three slots would have forced each of these into the nearest, most likely "next session", which is wrong for all of them. This is precisely the case the item valued most: an occurrence fitting no known slot is the most valuable thing the audit can find, and a prescriptive pass would have lost them.

**Scale.** Across five procedure docs the bare forms dominate — "the session" 60, "this session" 48, "a session" 26, against 14 "planning session", 9 "next session", 6 "plan session". Roughly nine to one. Most bare uses resolve correctly from context; the point is that resolving them is work the reader does every time, and it is the work that fails under the conditions this method designs for.

**Three further meanings, filed together as a stop-list so a corrections pass does not churn correct text.** "Session type" means the *shape* of a chat. "One commit per session" and "the session's LOG entry" mean the chat, and are load-bearing — though they read naturally as a run, which is the same conflation that produced [log-records-the-run-not-the-chat], built in this run. And "mid-session", "short session", "fresh session" and "isolated session" all mean the chat, consistently, and should be left alone.

**The code uses the word for the opposite thing, confirmed rather than assumed.** `session_id` comes from the harness and identifies the **chat** — one transcript file, one build working file named for it, which is what makes "one build at a time" enforceable. So the precedent from the work-item rename does not transfer: there, code used a term loosely where prose used it precisely; here they use it for different things.

**The method's own limit is recorded rather than softened.** This was a collocation survey plus targeted reads of ambiguous sites, not 707 individual judgments. A collocation survey finds meanings that recur and can miss a single odd use in one paragraph — exactly the fits-no-slot case it valued most. So six is a floor on how many meanings exist, never a ceiling. The consumer-facing texts got the lightest treatment: the FAQ carries 185 occurrences and SPEC 88, both unsurveyed occurrence-by-occurrence, left because settling what the slots are has to come before surveying the documents that use them.

Depth: full — the audit's expected output turned out to be unwritable, because the vocabulary it was to be measured against has too few slots for the meanings in use.

Rule gate: not needed — an audit authors nothing and amends nothing.

FAQ: not needed — an audit edits nothing a consumer sees.

**Approval outcomes:** all seven findings approved as-is; none contested, reworded or dropped. Filed as five captures, grouping the three clean/ambiguous-meaning findings into one so a corrections pass gets a single stop-list.

**Files touched:** the procedure docs, `SPEC.md`, `CLAUDE.md` and the FAQ — **read only.** An audit edits nothing. `skill-nonspecific-rules.md`'s occurrences are excluded by scope, belonging to [law-prose-restyle].

**Routed to Captures:** [session-vocabulary-has-too-few-slots], [bare-session-dominates-the-corpus], [session-means-shape-record-and-chat-too], [session-id-names-the-chat-not-a-session], [session-survey-coverage-gap].

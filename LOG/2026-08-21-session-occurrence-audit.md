# 15e10c9 — Every occurrence of "session" classified: 941 matches counted, roughly fifty mean a run, listed by file and line

Audit entry. The settled vocabulary (user's decision, 2026-08-17): a **run** is a command executing — a /plan run, a /next run — and a **session** is the chat.

**Count and method.** 941 case-insensitive substring matches across the seventeen files under `plugin/throughliner/docs/`, `templates/faq-template.md`, `FAQ/faq.md` and `SPEC.md`, counted per file mechanically — this re-count replaces the item's ~707 figure, taken before the restyle passes rewrote the text. `FAQ/faq.md` was verified byte-identical to the template, so its 241 matches carry the template's classification and the unique corpus is ~700. Matches inside "supersession" (plan.md:841) are a different word and excluded; `session_start`, `session-id`, "session scratchpad" and quoted specimen slugs are technical names, left alone. Per-file counts: done.md 98, plan.md 80, setup.md 41, next.md 33, done-plan.md 32, skill-nonspecific-rules.md 19, next-build.md 12, recovery.md 8, feedback-and-inbox.md 6, done-build.md 5, rescan.md 4, next-audit.md 3, migrate-checklist.md 3, done-audit.md 2, faq-template.md 241, FAQ/faq.md 241, SPEC.md 113.

**The decision rule applied, stated so the corrections build can re-derive any line.** An occurrence means A RUN where the sentence describes the conduct of a command's execution — what /plan or /next does while running. It means THE CHAT where it names the chat's lifetime, memory, records, openings or closes. The stop-list was honoured: mid-session, short session, fresh session, isolated session, and done.md's "session type" all mean the chat and are left alone.

**Run-meaning occurrences (the corrections item renames these):**
- next.md: 148 (first occurrence — "a planning session that read"), 402, 676, 680
- plan.md: 18, 41, 62, 199, 361, 443, 446, 530, 533, 584, 669, 954, 1128, 1221
- done.md: 416, 585 · done-build.md: 72 · next-build.md: 287 · setup.md: 300, 411
- skill-nonspecific-rules.md: 508; 1091 ×2 and 1097 ×2 — including the defining sentence "A plan session and a next session are runs of a command inside a chat", which itself uses session for runs
- rescan.md: 133, 139
- SPEC.md: line 41 ×3 (processed-in-a-planning-session, a-planning-session-writes-a-record, every-planning-session-adds), line 43 ×1, line 47 ×1, line 84 ×1, line 86 ×1, line 92 ~8 (the Processing-flow paragraph's run-conduct occurrences: opens on two beats, asks two things, process this session, fixed-when-the-session-opens ×2, finish inside one session, never offers to stop, length of the session), line 94 ×1, line 96 ×1, line 98 ~2

**Chat-meaning (correct, left alone):** every other occurrence — including all of done-plan.md, done-audit.md, feedback-and-inbox.md, migrate-checklist.md, next-audit.md, recovery.md, and both FAQ files whole: the FAQ speaks the consumer's language, where session = the chat throughout, and zero run-meaning occurrences were found there.

**Borderlines recorded as judged**, for the corrections build to re-read in place: plan.md 28 (the lock binds the chat — A), the record-kind sentences ("a planning session's record" — A, the record belongs to the chat), done.md 52/60 and done-plan.md's router (session shapes/kinds — A), SPEC line 55 ("the lock reaches planning sessions too" — A), SPEC line 116 ("Execution sessions… planning sessions" as categories — A, noted that the corrections item may prefer run-language there).

**Files touched:** none — the audit read `plugin/throughliner/docs/` whole, both FAQ files, and SPEC.md.
**Routed to Captures:** none — the classification is the product, and [session-vocabulary-corrections] already exists as the consumer of this list.
**Approval outcomes:** no capture findings to approve; the classification list was not contested.
Rule gate: not needed — an audit edits nothing and no rule is authored or amended.

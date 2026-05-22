# V58 — Session performance tracking (AEX-style DEX/HEX)

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22).**

## Goal

Add a lightweight session-performance log so method decisions rest on evidence rather than instinct. Each session records: configuration used (model, hooks active, skills invoked), what went well, what didn't, and a structured assessment. Over time, this builds a record of which configurations and approaches are reliable for which task types.

Borrowed from AEX (github.com/ctenidae8/AEX_Protocol): **DEX** = per-config reliability score from logged outcomes; **HEX** = per-config record of what tasks the config has proven good at.

## Inputs

- OPEN-QUESTIONS entry: "Track session performance over time? (AEX-style DEX/HEX)"
- `plugin/agents/after-build.md` — natural place to write the performance log entry (after the build recap)
- `plugin/docs/DOC-STRUCTURE.md` — new doc structure for the performance log
- `BUILD-METHOD.md` — current retrospective mechanisms (BUILD-LOG captures decisions/surprises, OPEN-QUESTIONS captures tensions)
- AEX Protocol reference (github.com/ctenidae8/AEX_Protocol) — DEX/HEX concepts

## Outputs

- New log mechanism — shape decided at session start (structured fields in BUILD-LOG entries, separate `performance-log/` folder, or a section in the after-build recap)
- After-build subagent updated to capture performance data at session close
- `plugin/docs/DOC-STRUCTURE.md` updated for the new log shape
- `plugin/docs/VOCABULARY.md` updated — performance log terms defined
- Crash course.md updated if user-facing explanation needed
- OPEN-QUESTIONS entry removed

## Success criteria

- Every completed build session produces a performance log entry with structured fields (not just prose)
- The log is queryable — given a task type, you can find which configurations and approaches worked
- The log doesn't add significant time or cognitive burden to session close
- After 5–10 sessions, the log contains enough signal to inform at least one method decision

## Open questions for this session

- **Log shape.** Three candidates:
  - **Structured fields in BUILD-LOG entries.** "What worked / what didn't / hypothesis for next time" added to each build entry. Lightest lift; collocated with build history.
  - **Separate `performance-log/` folder.** One file per session, structured. Heavier; cleaner separation of concerns.
  - **Section in after-build recap.** Performance captured in conversation, not persisted to a file. Lightest but loses cross-session queryability.
  Leaning: structured fields in BUILD-LOG entries (or per-build files after V52 ships). Keeps performance data next to the build it describes.
- **What constitutes "went well" vs. "didn't"?** Need a lightweight rubric that doesn't devolve into vibes-as-data. Candidates: did the build complete without regressions? Did the user need to intervene? Was the verification burden estimate accurate? How many turns did the batch take?
- **Mechanical success criterion.** The OPEN-QUESTIONS entry flagged this as the hardest part. Define a small set of objective measures (regression count, intervention count, turn count, time estimate vs. actual) and let subjective "feel" stay in prose, not scores.
- **Who writes the entry — Claude or the user?** Claude captures the mechanical measures automatically; the user adds subjective assessment during the after-build conversation. Both land in the same entry.

## Risks / dependencies

- **Premature measurement risk.** If the method is still changing rapidly at V58, performance data captures noise about the method's evolution, not signal about its working state. Mitigate by focusing on mechanical measures (regression count, intervention count) that are meaningful regardless of method version.
- **Cognitive burden.** If performance logging feels like homework, users will skip it. Keep the automated part dominant and the user's part to one or two questions.
- **No hard dependencies.** Placed at V58 so the method has stabilised through V45–V57 and the data has a chance of being meaningful.

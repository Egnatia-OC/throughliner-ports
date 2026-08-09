# 4f5e167 — The scrub gate shipped: a mechanical secret-shape scan, a pre-write checklist, and an explicit refusal to claim more than either can deliver

This item carried a red flag, cleared at processing on 2026-08-09 by informed acceptance rather than by design — Alex was told plainly that queue items and log entries written between then and this build could carry revealing content into a repository that might be published, and chose to proceed with the fix queued rather than hold the work. That exposure was live until this shipped. It has now shipped.

The crux the item existed for is that Claude narrating "I removed X and Y for Z reason" cannot guarantee the text presented for approval is actually clean: the human approves meaning, not a byte-level scrub, so a missed detail reaches a public repository silently. The design answers that honestly instead of papering over it, in three parts.

The mechanical scan is the only part that guarantees anything, and its narrowness is the design rather than a limitation. It matches high-confidence credential shapes only — private-key blocks, API-key prefixes, long hex and base64 runs, email addresses — over QUEUE.md, SPEC.md and LOG entries, because those get committed and a commit keeps text even after deletion. Deterministic, no judgement, therefore no false confidence. It fires after the write, which is the right fit rather than a compromise: the approval flow is write-first, so the text is already on disk and an after-write flag is the earliest honest moment.

The pre-write checklist is where "is this case detail revealing?" gets judged, because no pattern can judge it. It runs at the three moments text enters a committed doc — filing a capture, keeping a work item, writing a log entry.

The third part is the one that must never be sanded off: **a stated limit.** Part two is Claude checking its own writing, which is precisely what the crux says cannot be guaranteed, so the gate must never be described to a user as "your artifacts are scrubbed". A gate that over-claims is worse than no gate, because the user publishes more freely believing it worked. That is the same line the method already holds on red flags — provide risk-addressing, never promise risk management — and the real protection for a public repository is not publishing these artifacts at all. Describing the gate as a guarantee, and building only the mechanical half, were both explicitly rejected: patterns catch credentials and miss the thing that actually leaks, which is ordinary prose about a real person or a real case.

One live correction during the build. The first base64 pattern matched an ordinary filesystem path in an existing log entry — forty-odd characters of letters and slashes read as base64 to a regex. It now excludes `/` and requires both a digit and a capital. Verified across all 322 project prose documents: zero flags, with a positive control confirming a real token and an email are both caught.

`scripts/scrub_sweep.py` already existed and was checked rather than assumed duplicative. It is an on-demand, human-run, whole-repo sweep for *other people's names* — a different question with a different trigger. Neither replaces the other, and the new code says so where a future reader will find it.

**Files touched:** `plugin/si-plugin/hooks/post_tool_use.py` (`SECRET_SHAPES`, `_scan_secrets()`, `_is_scannable_doc()`, `_secret_message()`, a shared `_emit()`); `plugin/si-plugin/docs-b/plugin-behaviour.md` (the checklist and the never-claim-scrubbed rule); `plan.md` and `done.md` (two of the three authoring moments point at it; the third already sits in the section that carries it); `SPEC.md`; `plugin/si-plugin/templates/faq-template.md` and `faq-index-template.md`.

**Routed to Captures:** none from this item.

**Red flag:** carried `State: cleared` into this close. Cleared at processing by informed acceptance, not by design; the consent trail is recorded there and the exposure it described is now closed.

FAQ: updated — new consumer entry "Does Claude check my queue and logs for private information before they get committed?", written to lead with the limit rather than the reassurance, plus its index line.

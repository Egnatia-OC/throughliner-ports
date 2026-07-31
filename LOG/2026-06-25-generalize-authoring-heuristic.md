# 3a12926 — [generalize-authoring-heuristic] renamed 4-8-authoring-heuristic.md → authoring-heuristic.md; added a model-agnostic rule-writing section + the escalation heuristic

Built in the goal run (third of four). Two pressures met: the escalation heuristic (when a slipped rule earns a hook vs. just sharper wording) needed a durable home, and CLAUDE.md was already heavy, so piling rule-writing rules into it would bloat it further; separately, resources/4-8-authoring-heuristic.md was named for a model and goes stale as the project adopts future ones. One move fixes both.

Renamed the file to resources/authoring-heuristic.md (via git rm of the old path + a new file, so the rename is recorded) and restructured it into three parts: a new intro framing it as the project's guide to authoring and sharpening rules; a model-agnostic "Rules about writing rules" section holding the escalation heuristic; and a "4.8" section holding the existing 7-point checklist unchanged (the original What/Why/Aim/Sources framing moved into that section, since it's model-specific). The escalation heuristic, recorded with both worked examples from the 2026-06-24/25 sessions: a behavioural rule that slips *despite already carrying its rationale* earns a mechanical backstop only when the failure's cost justifies the hook's standing friction — [subagent-ask-gate] slipped at high cost (a Max-usage blowout) so it earned the ask-gate hook on top of hardened wording; [unpark-scan-mixed-trigger] slipped at low cost so it got procedure-sharpening only. It extends SPEC's two-tier principle ("hooks enforce what must never happen; hardened rules steer what should usually happen") with the missing trigger — what tips a should-usually rule into needing a must-never mechanism.

CLAUDE.md's "Author method text 4.8-shaped" convention now points at the 4.8 section of the renamed doc and notes the doc also houses rule-writing rules — a pointer, not a copy, so CLAUDE.md stays light. QUEUE.md's old-filename citations were repointed to the new name (in [method-compliance-checklist], the [retire-spec-edit-batch-type] enforcement note, and the [method-doc-structure-pass] conceptual references, the last two as mechanical rename-pointer maintenance with the target content unchanged); LOG references were left as historical. Host-only authoring guide — no FAQ, no SPEC change, no test (consciously omitted; the developer reads it).

**Files touched:**
- resources/authoring-heuristic.md — new file (renamed from 4-8-authoring-heuristic.md, restructured: intro + "Rules about writing rules" + "4.8" section)
- resources/4-8-authoring-heuristic.md — removed (git rm)
- CLAUDE.md (project) — "Author method text 4.8-shaped" convention repointed to the new doc and its 4.8 section
- QUEUE.md — old-filename citations repointed in [method-compliance-checklist] and [method-doc-structure-pass]

**Routed to Captures:** none

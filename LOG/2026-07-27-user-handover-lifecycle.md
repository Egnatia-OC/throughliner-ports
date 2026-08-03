# 053c608 — next/next-build/done/done-plan/plan/plugin-behaviour + SPEC + FAQ: gave [user] handover items a full completion lifecycle

Before this, once /next handed over a `[user]` item nothing detected it got done, recorded it, or removed it — so a finished handover stranded in Processed and the next /next re-handed it back as unbuilt (observed live in two consumer projects, 2026-07-20 and 2026-07-16). This build gave `[user]` items a complete lifecycle in three parts.

1. **Handover names its own close.** next.md's handover branch now tells the user how completion gets recorded — run /done to record it, or raise it at the next /plan — instead of just stopping.
2. **A later session asks whether it's done.** next.md's pre-flight and plan.md's Step 1 now ask "have you already done this one?" when they meet a `[user]` item still in Processed, rather than silently re-handing it over. Detection is by asking, not by scanning the filesystem for a produced artifact — a handover can be a device check or a decision, not a file. The filesystem artifact-check was rejected as fragile (it needs each item to declare a produced file).
3. **A defined close for a completed item.** done.md gained a "Completed `[user]`-item close" (log under slug, remove from Processed), reachable both from a standalone /done and — via done-plan.md — from a /plan where the user mentions an async-completed handover. done.md's old "no /done closes a `[user]` line" text was replaced.

Dependent re-clearing (work a closed `[user]` item gated) was left to [plan-no-below-line-revisit]'s standing revisit, not duplicated here. plan.md Step 3 gained an explicit anti-pattern note: don't hold a `[user]` item below the marker merely because it's the user's to run.

**Files touched:**
- next.md, done.md, done-plan.md, plan.md, plugin-behaviour.md (new "`[user]` handover lifecycle" section)
- SPEC.md (/next handover + /done descriptions synced)
- templates/faq-template.md + faq-index-template.md (new "I did a `[user]` step… how does it get recorded and cleared?" entry)
- README.md: no change (feature list doesn't mention handover; no new skill/mode/command)

**Routed to Captures:** none

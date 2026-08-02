# fa24343 — Moved `[user]`-completion detection to a one-time completion-mode /setup preference; suppressed the /plan Step 1 completion-ask by default

The /plan Step 1 completion-ask swept Processed for already-done `[user]` items every session, which for the coached in-/next workflow read as "why haven't you done these?" — nudging against the relax-and-be-walked-through-in-/next philosophy. Added a persistent Completion mode project field (sibling to Working mode / Editor), defaulting to in-/next: in the default, the /plan Step 1 sweep is suppressed entirely and detection falls to the /next walk-through's light trailing note; in async, the sweep fires as before. Wired through setup.md (new Q8 + fill step + count/scaffold-desc updates), CLAUDE-TEMPLATE.md (the field), plan.md Step 1 (the gate), plugin-behaviour.md (new Completion mode subsection near Working mode + lifecycle gating), SPEC.md (the user-visible setting), and the FAQ templates (new entry + index line). Rejected dropping the completion-ask entirely (a genuine async user exists, and the toggle preserves that path) and keeping the every-session ask (the nag itself).

**Files touched:** setup.md, templates/CLAUDE-TEMPLATE.md, plan.md, plugin-behaviour.md, SPEC.md, templates/faq-template.md, templates/faq-index-template.md

**Routed to Captures:** none

# [HASH] — Spec-edit: synced SPEC.md to the three-doc architecture and dropped the stale "SPEC read-only during builds" clause

Two sentences in this project's SPEC.md had gone stale, and both were carved-out SPEC changes deferred from earlier decisions — neither could be made in its originating build, because SPEC is out of a feature build's scope (the scope-lock only lets a batch that lists SPEC.md edit it). This planned spec-edit batch (which lists SPEC.md) made both edits, ordered after [retire-registry] so the architecture and the spec didn't briefly contradict.

First, the "How it works" doc list went from "Four project docs structure each project" to "Three," and the REGISTRY.md bullet was removed — matching the REGISTRY retirement that [retire-registry] just landed. Second, the hooks list described pre_tool_use as enforcing "SPEC.md read-only during builds, scope-lock to file list, git safety"; the read-only rule was removed by [spec-edit-batch-type] earlier, so the line now reads that pre_tool_use enforces the scope-lock (which governs SPEC.md like any other file) and git safety. SPEC now matches both the live architecture and the live hook behaviour. The "Two hooks enforce… and a third advises" sentence was already correct and was left alone.

**Files touched:**
- SPEC.md — "Four" → "Three" project docs and the REGISTRY bullet removed; pre_tool_use hook line reworded to drop the read-only clause

**Routed to Captures:** none

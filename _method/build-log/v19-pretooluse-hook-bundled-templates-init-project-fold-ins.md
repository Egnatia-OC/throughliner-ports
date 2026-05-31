# V19 — 2026-05-13 — PreToolUse hook + bundled templates + /init-project + Fold-ins pending section

**What shipped.** PreToolUse hook blocks Edit/Write/MultiEdit on locked SoT docs; redirects to `[FOLD-IN PENDING]` section in BACKLOG.md. Five templates bundled at `plugin/templates/`. New `/init-project` skill (scaffold script; refuses on non-empty, points at `/migrate`). Structural rewrites: BACKLOG-TEMPLATE (×2), DOC-STRUCTURE, NO-CODE-METHOD for fold-ins pending section. Smoke-tested on Windows: all paths verified.

**Decisions.** Templates at `plugin/templates/`, not inside skill — multiple consumers (init-project + future migrate). `/init-project` refuses on conflict, doesn't merge — half-scaffolding would silently mix sources. Hook denies with redirect message, not silent rewrite — "be told what's wrong" principle. `[FOLD-IN PENDING]` gets own top-level BACKLOG section — orphan blocks from multiple routes need one location.

**Pivots.** `${CLAUDE_PLUGIN_ROOT}` expands inside skill bodies — resolved uncertainty on first smoke try. V18's universal-behaviour rules self-policed before hook fired (Claude refused UX.md edit on its own; hook is backstop). Mid-smoke discovery surfaced missing `[FOLD-IN PENDING]` section in template → structural rewrite pulled into V19.

**Carried forward.** Cross-version template reconciliation raised as OQ. Windows subfolder-conflict test skipped (platform-agnostic `pathlib`).


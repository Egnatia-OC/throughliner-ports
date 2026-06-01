# Skill invocation flowchart and prerequisite audit

Research artifact for batch 0142. Produced v142, 2026-05-29.

## Flowchart — valid skill invocation paths

```mermaid
flowchart TD
    START([New session]) --> SS{SessionStart hook}
    SS --> |No method docs| SETUP["/sovsetup<br/>Scaffold project"]
    SS --> |Method docs exist| ROUTE{What do you<br/>need to do?}

    %% Planning lane
    ROUTE --> |Plan next work| PLAN["/sovplan<br/>Edit BACKLOG, drift checks"]
    ROUTE --> |Review before building| RECAP["/sovrecap<br/>Lock Files: and Tests:"]
    ROUTE --> |Resolve open questions| DELIB["/sovdeliberate<br/>Work through OQs"]
    ROUTE --> |Explore an idea| IDEATE["/sovideate<br/>Assess and route ideas"]
    ROUTE --> |Compress a doc| TERSIFY["/sovtersify<br/>Two-phase compression"]

    PLAN --> RECAP
    PLAN --> DELIB
    PLAN --> IDEATE
    DELIB --> PLAN
    IDEATE --> PLAN

    %% Build lane
    RECAP --> BUILD["/sovbuild<br/>Snapshot batch, build files"]
    BUILD --> CLOSE["/sovclose<br/>MANIFEST, tests, recap"]
    CLOSE --> GIT["/sovgit<br/>Commit, tag, push"]
    GIT --> TEST["/sovtest<br/>Guided user verification"]
    TEST --> PLAN

    %% Anytime skills (available from any state)
    ANYWHERE[ ] ~~~ EXPLAIN["/sovexplain<br/>Answer method questions"]
    ANYWHERE ~~~ RESEARCH["/sovresearch<br/>Disciplined web research"]
    ANYWHERE ~~~ REVERT["/sovrevert<br/>Emergency: restore last commit"]

    %% Style
    style SETUP fill:#e8f5e9
    style PLAN fill:#e3f2fd
    style RECAP fill:#e3f2fd
    style DELIB fill:#e3f2fd
    style IDEATE fill:#e3f2fd
    style TERSIFY fill:#e3f2fd
    style BUILD fill:#fff3e0
    style CLOSE fill:#fff3e0
    style GIT fill:#fce4ec
    style TEST fill:#fce4ec
    style EXPLAIN fill:#f3e5f5
    style RESEARCH fill:#f3e5f5
    style REVERT fill:#ffebee
    style ANYWHERE fill:none,stroke:none
```

### Reading the flowchart

**Colour key:**
- Green — setup (one-time)
- Blue — planning phase skills
- Orange — build phase skills
- Pink — post-build skills
- Purple — anytime skills (no phase restriction)
- Red — emergency skill

**The rigid cycle** (most common path): `/sovplan` → `/sovrecap` → `/sovbuild` → `/sovclose` → `/sovgit` → `/sovtest` → back to `/sovplan`.

**Valid deviations:**
- `/sovdeliberate` and `/sovideate` can interrupt planning at any point, then return to `/sovplan`.
- `/sovtersify` is standalone — invoke when a doc needs compression, return to whatever you were doing.
- `/sovexplain` and `/sovresearch` are truly anytime — no phase restriction, no state changes.
- `/sovrevert` is emergency-only — restores to last commit from any state.

**Invalid paths the plugin catches:**
- Building without method docs → SessionStart routes to `/sovsetup`.
- `/sovbuild` with unconfirmed test rows → PreToolUse denies file edits, directs to planning.
- Editing source files during planning → PreToolUse denies.
- Editing method docs during build (except snapshot and BACKLOG red flags) → PreToolUse denies.
- Committing with an open build snapshot → PreToolUse denies git commit.

## Prerequisite audit — findings

### Gap 1: /sovtersify phase gate checks legacy marker (MEDIUM)

`tersify.md` line 5 checks for `Status: active` in the BACKLOG batch heading. Since V90, the build-in-progress signal is the existence of `_method/active-build.md` (the build snapshot). The legacy `Status: active` marker is never written. The phase gate is dead — `/sovtersify` would run during a build when it shouldn't.

**Fix:** Replace the `Status: active` check in `tersify.md` with a check for `_method/active-build.md`.

### Gap 2: /sovbuild doesn't verify Files: populated (MEDIUM)

`/sovbuild` parses the top batch via `parse_backlog.py` and checks for empty `{}`. But it doesn't verify that Files: entries exist. If `/sovrecap` was skipped (or failed silently), the batch has change-list bullets but no Files: sub-section. The build procedure's per-file work loop would have zero iterations — a vacuous "successful" build that does nothing, then prompts `/sovclose`.

**Fix:** Add a check in `build.md` after parsing: if `files` array is empty, halt and direct user to run `/sovrecap` first.

### Gap 3: Planning skill docs say "never during builds" but V90 permits it (LOW)

`planning.md` line 1, `deliberate.md` line 3, and `ideate.md` line 3 all say "never during building." But since V90, `/sovbuild` extracts the batch to `active-build.md` and unlocks BACKLOG. SessionStart explicitly says planning skills are safe in parallel sessions. The procedure docs are stricter than the architecture requires.

**Impact:** A user who reads the procedure would avoid planning during a build unnecessarily. The hooks don't enforce this restriction — only the procedure text does.

**Fix:** Soften the procedure language to "not in the same session as a build" rather than "never during builds." Or add a note that parallel-session planning is permitted when a build snapshot exists.

### Gap 4: /sovrecap doesn't check for active build snapshot (MEDIUM)

`before-build.md` validates the top BACKLOG batch — but if a build is already in progress (`_method/active-build.md` exists), the top batch has already been extracted. `/sovrecap` would either find the *next* batch (wrong one) or find nothing and halt with a confusing "no batch found" message.

**Fix:** Add a check at the top of `before-build.md`: if `_method/active-build.md` exists, halt and tell the user a build is in progress — finish it with `/sovclose` or revert with `/sovrevert`.

### Gap 5: /sovtest doesn't explain mid-build "no tests" result (LOW)

`testing.md` walks the user through pending User-verified test rows. It doesn't check whether a build is in progress. Mid-build, the test-confirmation gate guarantees previous rows are confirmed, and the current build hasn't written rows yet. So `/sovtest` mid-build just finds nothing — harmless but confusing.

**Fix:** Add a note in `testing.md`: if `_method/active-build.md` exists, tell the user test rows for the current build don't exist yet (they're written at `/sovclose`).

---

*Sovereign Implementer — Version 112.*

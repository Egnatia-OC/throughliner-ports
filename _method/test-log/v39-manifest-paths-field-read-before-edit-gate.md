# V39 — MANIFEST paths field + read-before-edit gate (2026-05-21)

Direct hook-script invocation against Python-built fixture. Validates read-before-edit gate: paths-field parsing (three shapes), MANIFEST → target matching, deny, transcript-scan retry, spine-doc exemption. All 7 Pass.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 116 | 2026-05-21 | V39 | Edit on a file matching a MANIFEST entry's single-file `(path)` field is denied with V39 marker | `pre_tool_use.py` → `check_read_before_edit` + `parse_manifest_entries` | Pass | Fixture `MANIFEST.md` had `- **TaskCard** (\`app/TaskCard.kt\`) — ...`; Edit on `app/TaskCard.kt` denied with `BLOCKED [V39 read-before-edit]` marker present in stdout. |
| 117 | 2026-05-21 | V39 | Edit on a file matching a MANIFEST entry's multi-file list `(path1, path2)` shape is denied | `pre_tool_use.py` → `parse_manifest_entries` + `_path_matches_entry_path` | Pass | Fixture entry `(\`app/notifications/Service.kt\`, \`app/notifications/Channels.kt\`)` — Edit on `Service.kt` matched and denied. |
| 118 | 2026-05-21 | V39 | Edit on a file under a MANIFEST entry's directory-prefix `(dir/)` is denied | `pre_tool_use.py` → `_path_matches_entry_path` (trailing-slash branch) | Pass | Fixture entry `(\`app/settings/\`)` — Edit on `app/settings/AccountScreen.kt` matched via directory-prefix rule and denied. |
| 119 | 2026-05-21 | V39 | Edit on a file not named in any MANIFEST entry is allowed (no false denial) | `pre_tool_use.py` → `check_read_before_edit` (no-match branch) | Pass | Edit on `somewhere_not_listed.kt` — gate returned None, hook emitted nothing, exit 0. Confirms the gate only fires on covered files. |
| 120 | 2026-05-21 | V39 | MANIFEST entry without a `(path)` field is silently skipped by the gate (legacy / incremental migration) | `pre_tool_use.py` → `manifest_entry_covers_file` (empty paths) | Pass | Fixture had `- **LegacyComponent** — Old component, no path field yet.`; Edit on an unrelated file allowed. Confirms `entry.paths == []` → skipped. |
| 121 | 2026-05-21 | V39 | Spine-doc target (MANIFEST.md itself) is exempt from the V39 gate even if accidentally listed | `pre_tool_use.py` → `check_read_before_edit` (`V39_EXEMPT_LOGICAL_NAMES` check) | Pass | Edit on `MANIFEST.md` allowed regardless of whether MANIFEST coincidentally had a matching entry. Defensive guard against build-cycle deadlock. |
| 122 | 2026-05-21 | V39 | Retry after first deny succeeds via transcript scan (block-once semantics, no state file) | `pre_tool_use.py` → `transcript_shows_prior_v39_deny` | Pass | Wrote a fake transcript file containing `BLOCKED [V39 read-before-edit]: <abs path>`; subsequent Edit on the same file allowed. Confirms the marker line is what the retry check matches on. |


# 0067 — Desktop app install/update documentation

## Goal

Document the full plugin install, reinstall, and version-update procedure for the Claude Code desktop app in Crash course. The 0060 E2E test revealed that the current install instructions assume CLI usage and don't cover desktop-app-specific friction: the `/plugin` command opening a modal instead of running, stale versions persisting after `--plugin-dir` usage, the uninstall/reinstall dance, manual `enabledPlugins` edits in `settings.json`, and the need for a Task Manager kill to force a true restart.

## Inputs

- E2E finding 4 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- `sovereign-implementer/Crash course.md` → *Install, and a first session* and *Managing the plugin* sections
- Alex's actual install experience from 0060 sessions 1–2
- **V58 finding (v64):** The desktop app DOES have a plugin disable/enable toggle at Customise → Plugins → gear icon on the plugin. This toggle handles both disable and re-enable. The Crash course's *Managing the plugin* section (added in v64) currently overstates the desktop app limitation — it says `/plugin` is the only management path and desktop users must use the CLI. The desktop app toggle needs to be documented as the primary path for desktop users, with the CLI path as the alternative.

## Outputs

- Crash course *Install, and a first session* section updated with desktop-app-specific instructions alongside the existing CLI instructions
- Coverage of: first install via local marketplace, verifying the installed version, updating to a new plugin version, troubleshooting stale versions, full uninstall/reinstall procedure, the `settings.json` manual edit as a last resort
- Crash course *Managing the plugin* section corrected: desktop app toggle (Customise → Plugins → gear icon) documented as the primary disable/enable path for desktop users, replacing the current "CLI-only" framing

## Success criteria

- A desktop app user reading the install section can install the plugin without hitting undocumented friction
- CLI instructions preserved (not replaced)
- Troubleshooting steps are plain English, not developer jargon

## Risks / dependencies

- The desktop app's plugin management may change in future Claude Code releases, making these instructions stale. Note the version/date when writing.
- No code dependencies — this is a documentation-only session.

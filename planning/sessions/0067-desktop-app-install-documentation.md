# 0067 — Desktop app install/update documentation

## Goal

Document the full plugin install, reinstall, and version-update procedure for the Claude Code desktop app in Crash course. The 0060 E2E test revealed that the current install instructions assume CLI usage and don't cover desktop-app-specific friction: the `/plugin` command opening a modal instead of running, stale versions persisting after `--plugin-dir` usage, the uninstall/reinstall dance, manual `enabledPlugins` edits in `settings.json`, and the need for a Task Manager kill to force a true restart.

## Inputs

- E2E finding 4 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- `sovereign-implementer/Crash course.md` → *Install, and a first session* section
- Alex's actual install experience from 0060 sessions 1–2

## Outputs

- Crash course *Install, and a first session* section updated with desktop-app-specific instructions alongside the existing CLI instructions
- Coverage of: first install via local marketplace, verifying the installed version, updating to a new plugin version, troubleshooting stale versions, full uninstall/reinstall procedure, the `settings.json` manual edit as a last resort

## Success criteria

- A desktop app user reading the install section can install the plugin without hitting undocumented friction
- CLI instructions preserved (not replaced)
- Troubleshooting steps are plain English, not developer jargon

## Risks / dependencies

- The desktop app's plugin management may change in future Claude Code releases, making these instructions stale. Note the version/date when writing.
- No code dependencies — this is a documentation-only session.

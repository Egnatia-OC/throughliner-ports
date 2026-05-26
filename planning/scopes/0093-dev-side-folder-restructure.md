# 0093 — Dev-side folder restructure

## Goal

Move all dev-side content into a single `dev/` folder at repo root. Delete frozen V39 docs and the committed `plugin.zip` build artifact. The repo root should contain only product-facing items and standard repo furniture.

## Decisions (made before scoping)

- **Folder name:** `dev/`.
- **Frozen V39 docs deleted:** `NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/` (repo-root copies). All are in git history. The live operational copies already live inside `plugin/docs/` and `plugin/templates/`.
- **`plugin.zip` deleted:** build artifact, shouldn't be committed.
- **`Reference manual.md` stays at repo root** — product-facing.
- **`crash-course/` stays at repo root** — product-facing HTML teaching site.
- **`Marketing/` moves into `dev/`** — dev-side, not user-facing.
- **No dependency on 0092.** BUILD-METHOD split can happen before or after; the restructure moves whatever exists at the time.

## Repo root after this ships

```
sovereign-implementer/
├── plugin/
├── crash-course/
├── Reference manual.md
├── README.md
├── LICENSE
├── .no-code-method-skip
│
└── dev/
    ├── planning/          (BACKLOG.md, scopes/, drafts/, .proxies/, other planning docs)
    ├── build-log/
    ├── test-log/
    ├── research/
    ├── tests/
    ├── Marketing/
    ├── Archive/
    └── BUILD-METHOD.md    (or its split successors if 0092 ships first)
```

## Inputs

- Current repo root layout (15+ items, mix of dev-side and product-facing).
- `CLAUDE.md` (this project's — heavy path references throughout).
- `BUILD-METHOD.md` / `session-protocol.md` / `session-reference.md` — path references to update.
- `BACKLOG.md` — scope-file allocation rule references `planning/scopes/`.
- Build-log and test-log entries — may contain relative paths.

## Outputs

- `dev/` folder with all dev-side content moved via `git mv`.
- Frozen V39 docs and `plugin.zip` deleted via `git rm`.
- Updated path references in: CLAUDE.md, BUILD-METHOD.md (or successors), session-protocol.md, session-reference.md, BACKLOG.md, and any other dev docs that use relative paths to moved content.
- CLAUDE.md "Current state" / orientation sections rewritten to reflect new layout.

## Success criteria

- Repo root has exactly: `plugin/`, `crash-course/`, `dev/`, `Reference manual.md`, `README.md`, `LICENSE`, `.no-code-method-skip`, `.gitignore`, `CLAUDE.md`.
- No dead path references in any dev doc.
- `git log --follow` works for moved files.
- Test suite passes from new location (`dev/tests/`).
- A new session can orient from CLAUDE.md without hitting stale paths.

## Risks / dependencies

- **Path references are everywhere.** CLAUDE.md alone has dozens. A systematic find-and-replace pass is needed — not ad hoc.
- **Absolute-path convention in CLAUDE.md** must update (e.g. `sovereign-implementer\planning\sessions\` → `sovereign-implementer\dev\planning\scopes\`). The "sessions → scopes" rename already shipped in 0091 but some CLAUDE.md references may still say `sessions/`.
- **Test suite imports.** `tests/` may have path assumptions that break when moved to `dev/tests/`. Check conftest.py and any fixture paths.
- Dev-internal only. No method-version bump, no plugin changes.

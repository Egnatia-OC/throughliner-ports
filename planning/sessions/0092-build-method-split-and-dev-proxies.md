# 0092 — BUILD-METHOD split and dev-side proxies

## Goal

Two paired changes: (1) split BUILD-METHOD.md into a slim session-protocol doc (loaded every session) and a reference doc (entry shapes, footer lists, testing details, artefact lifecycles — consulted on demand); (2) adopt `.proxies/` on the dev side, starting with proxies for the new split files and the BACKLOG.

## Inputs

- `BUILD-METHOD.md` — the file to split.
- `plugin/docs/DOC-STRUCTURE.md` → Proxy files section — format spec to follow.
- `planning/BACKLOG.md` (post-0091) — proxy target.
- `CLAUDE.md` — session-open steps reference BUILD-METHOD.md by name.

## Outputs

- Two files replacing BUILD-METHOD.md (working names TBD — e.g. `SESSION-PROTOCOL.md` + `DEV-REFERENCE.md`).
- `.proxies/` directory with dev-side proxies (at minimum: protocol, reference, BACKLOG).
- `CLAUDE.md` — session-open steps updated to reference proxies and new file names.
- `BUILD-METHOD.md` — deleted after content migrated.

## Success criteria

- Session-open context load is measurably lighter (proxy + slim protocol vs. full BUILD-METHOD).
- Reference material still reachable when needed (entry shapes, footer list, testing, artefact lifecycles).
- Proxy format matches plugin-side `.proxies/` spec from DOC-STRUCTURE.md.
- No information lost in the split.

## Proxy design decisions (settled in ideation, 2026-05-26)

**Dev-side proxies diverge from plugin-side format in two ways:**

1. **Reference proxy: "when to read" hints.** Plugin-side proxies are pure indexes (one line per entry, line number). Dev-side reference material is situational — sections matter at specific moments (footer bumps at close, entry shapes when writing build-log, testing during smoke tests). Each proxy entry carries a timing hint:
   ```
   - L45 **Footer bumps** — session close, before commit
   - L78 **Entry shapes: build-log** — when writing a build-log file
   - L95 **Testing procedures** — when session involves smoke testing
   ```
   Plugin-side doesn't need this because phase machinery (planning vs. build) gates loading. Dev-side has no equivalent gating; the hint is the lightweight substitute.

2. **BACKLOG proxy: routing-aware, not just an inventory.** Plugin-side has session-start hooks and parsers to find the active batch. Dev-side has no hook — Claude reads manually. The proxy carries what the hook would have provided:
   - Active/next batch called out explicitly (not buried in a long table).
   - Open questions with live triggers (which OQs are close to firing).
   - Dependency chain for the next few batches (so Claude doesn't pick up a blocked batch).
   - Shipped/cancelled rows omitted entirely — proxy is forward-looking.

## Open questions for this session

- What goes in "session protocol" vs. "reference"? Proposed cut: protocol = session open, session middle, session close, doc-code parity. Reference = entry shapes, footer bumps, testing, planning artefact lifecycles, migration context. Validate during the session.
- Naming: `SESSION-PROTOCOL.md` + `DEV-REFERENCE.md`? Follow plugin-side naming-by-purpose?
- Should dev-side proxies live in the same `.proxies/` as plugin-side proxies (if the plugin is loaded in this folder), or in a separate location like `planning/.proxies/`?

## Risks / dependencies

- Depends on 0091 (BACKLOG rename) so the BACKLOG proxy targets the right file.
- The split decision (what goes where) is the real work; file manipulation is mechanical.
- Dev-internal only. No footer bump.

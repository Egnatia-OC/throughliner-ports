# 0096 — Manifest rationale field

## Goal

Add a one-line rationale field to MANIFEST entries so Claude can find *why* a component exists without scanning the build log. Secondary benefit: Claude references the rationale when updating UX, reducing incorrect reasoning about why things exist.

## Inputs

- `plugin/templates/MANIFEST-TEMPLATE.md` — current template shape.
- `plugin/docs/DOC-STRUCTURE.md` § MANIFEST.md structure — entry format spec.
- `plugin/docs/DOC-STRUCTURE.md` § MANIFEST proxy — proxy line format.
- `plugin/docs/procedures/after-build.md` — where MANIFEST updates happen.
- `plugin/docs/procedures/planning.md` — where MANIFEST is editable.

## Outputs

- **MANIFEST entry format extended.** New shape: `- **[Name]** (`path`) — [description]. *Rationale: [why it exists / vNN].*`
- **DOC-STRUCTURE.md updated.** Entry format spec and guidance on what goes in the rationale vs. UX vs. build-log.
- **MANIFEST-TEMPLATE.md updated.** HTML comment shows new format.
- **MANIFEST proxy format updated.** Proxy line gains rationale snippet (or stays as-is if rationale is dip-only — design question below).
- **After-build procedure updated.** Session close becomes the canonical moment to write rationale — Claude has full build context and knows *why* it made what it made. Populates rationale on create; confirms/updates on modify.
- **Tests updated.** Any parser or fixture that validates MANIFEST entry shape.

## Success criteria

- New MANIFEST entries created during a build carry a rationale field.
- Claude updating UX can reference manifest rationale without opening build-log files.
- Existing entries without rationale remain valid (graceful migration — backfill is incremental, not mandatory).

## Open questions for this batch

1. **Proxy inclusion.** Should the manifest proxy carry rationale, or keep it dip-only (read full MANIFEST for rationale)? Proxy is a lightweight index — adding rationale makes it heavier but eliminates one more dip. Current proxy format is `- L<N> **<name>** (<path>)`.
2. **Format.** Inline italic suffix (`*Rationale: ...*`) vs. second line vs. parenthetical. Inline keeps the one-line-per-entry invariant. Second line breaks it but is more readable for long rationales.
3. **Build-log cross-reference.** Should the rationale include the session tag where the component was introduced (e.g. `*Rationale: reduces API calls — v12.*`)? Cheap breadcrumb back to the build log if someone needs the full story.
4. **UX procedure update.** Should the planning procedure explicitly say "check manifest rationale before rewriting UX entries"? Or is that implied once the field exists?

## Risks / dependencies

- No hard dependencies. Can ship independently.
- Surface area is moderate — DOC-STRUCTURE, template, after-build procedure, and tests all need coordinated edits.
- Risk of format bloat if rationales trend long. Mitigation: spec a hard cap (e.g. "one clause, max 15 words + optional session tag").

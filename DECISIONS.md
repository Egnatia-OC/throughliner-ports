# DECISIONS

Design decisions made during this project. Each entry maps a decision to the commit where it was made.

Format: **[decision name]** — [commit hash] — [what was decided and why]

- **Restore all five response-shape tags** — 448efdb — [SEQUENCE] included even though the behaviour existed as a prose rule, because tags let docs annotate it explicitly
- **Tags replace blanket sequencing rule** — 448efdb — unannotated steps get Claude's default; sequencing is now opt-in via [SEQUENCE] tag, not a global behaviour
- **Drop drift check as standalone step** — 448efdb — /done's existing safeguards (REGISTRY.md update, staleness sweep, SPEC.md read-only hook) already prevent drift; a separate /plan scan adds ceremony without value
- **Host/target propagation gap is not a plugin concern** — 448efdb — the gap only affects self-hosting (pointing the plugin at its own source); not worth encoding in target-side behaviours that all consumers inherit
- **LOG test-to-decision linkage is asymmetric** — 09573ac — LOG keeps all test results by commit; decision entries may cite a test outcome that drove them, but routine passes don't generate decisions

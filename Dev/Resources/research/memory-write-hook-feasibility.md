# Memory-write hook feasibility — 2026-05-24

## Question

Can the plugin intercept Claude Code's auto-memory writes via PreToolUse to block/redirect them to project artifacts?

## Answer

**No.** Memory writes bypass the hook pipeline entirely.

## Findings

- Memory writes use an internal mechanism, not the standard Write tool. A PreToolUse hook matching Write calls to the memory directory is fragile and relies on undocumented internals.
- Feature request for PreMemoryWrite/PostMemoryWrite hooks ([#44820](https://github.com/anthropics/claude-code/issues/44820)) was **closed as not planned**.
- The V56 project-boundary check would theoretically block memory writes (path outside project root) — but only if they used the standard Write tool, which they don't.

## Conclusion

Prose rules are the only viable enforcement. Added to `universal-behaviour.md` ("Route information to artifacts, not memory") and project CLAUDE.md.

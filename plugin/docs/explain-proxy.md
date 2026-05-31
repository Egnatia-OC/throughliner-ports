# Explain proxy — topic index

Lightweight index into `explain-reference.md`. Match the user's question to a topic below, then read the indicated line range with offset/limit.

Source: `${CLAUDE_PLUGIN_ROOT}/docs/explain-reference.md` (205 lines)

---

## Why does it block / deny my edits?

- Phase-aware editing permissions → L21–27
- Adoption gate (no method docs yet) → L128–131
- Read-before-edit gate (MANIFEST context) → L103–106
- Test-confirmation gate (unconfirmed tests) → L77–80
- Unclosed-build commit guard → L142–143
- Bash write guard → L136–137

## Why two phases? Why can't I edit X?

- Phase detection (planning vs build) → L14–19
- Editing surfaces (what's locked when) → L21–27
- [PROPOSED EDIT PENDING] mechanism → L27

## Build lifecycle

- Build snapshot (active-build.md) → L29–32
- Why one batch at a time → L72–75
- Why close is mandatory → L34–39
- Why close is two turns → L39
- Session handoff / compaction → L41–44

## Planning skills

- /sovplan and drift checks → L50–53
- /sovrecap (before-build validation) → L55–56
- /sovdeliberate (open questions vs batches) → L58–61
- /sovideate (idea routing) → L63–66

## Testing

- Test-confirmation gate → L77–80
- /sovtest (one at a time, volunteered results) → L82–89
- No fixing inside testing → L89
- Test types (four) → L83

## Method documents

- Proxy files (what, why) → L98–101
- MANIFEST and read-before-edit → L103–106
- UX.md (what, why locked) → L108–111
- BACKLOG structure and sections → L113–116
- Build log → L118–119
- Test log → L121–122

## Safety mechanisms

- Adoption gate → L128–131
- Git safety guard → L133–134
- Bash write guard → L136–137
- PostToolUse validation → L139–140
- Unclosed-build commit guard → L142–143

## Behavioural rules (why Claude acts this way)

- Push back rather than agreeing → L151–152
- Plain language over jargon → L154–155
- No stealth fixes → L157–158
- Flag out-of-scope improvements → L160–161
- Red flags → L163–164
- Verify external facts → L166–167
- Route to artifacts, not memory → L169–170
- Session-length awareness → L172–173
- Walkthroughs one step at a time → L175–176
- Never infer completion → L178–179
- Response-shape tags → L181–182

## Setup & utilities

- /sovsetup (four cases) → L188–191
- /sovresearch (discipline wrapper) → L193–196
- /sovtersify (doc compression) → L198–201
- /sovgit (git walkthrough) → L203–204

## Session routing

- How routing works → L9–12

---

*No-code method — Version 105.*

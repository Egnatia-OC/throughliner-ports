export const meta = {
  name: 'reader-test',
  description: 'Test plugin doc comprehension via simulated bookshelf tracker project',
  phases: [
    { title: 'Simulate', detail: 'Three agents simulate /plan, /next, /done' },
    { title: 'Verify', detail: 'Audit each simulation against procedures' },
    { title: 'Questions', detail: 'Answer and score 5 user questions' },
    { title: 'Synthesize', detail: 'Categorize findings for routing' },
  ],
}

// ── Plugin doc paths ──

const P = 'C:/Users/Alex/Desktop/Taskflow Planning/No code method/plugin/si-plugin'
const TEMPLATE = P + '/templates/CLAUDE-TEMPLATE.md'
const BEHAVIOUR = P + '/docs/behaviour.md'
const PLAN_DOC = P + '/docs/plan.md'
const NEXT_DOC = P + '/docs/next.md'
const DONE_DOC = P + '/docs/done.md'

// ── Fake project: Bookshelf Tracker (mid-project) ──

const FAKE_SPEC = `# SPEC — Bookshelf Tracker

## What it is
A personal book-tracking app. Local-first, stores data in a JSON file. No accounts, no cloud sync.

## Who it's for
A single user who wants to track what they're reading and what they want to read next.

## How it works
- Add books with: title, author, status (want-to-read / reading / read), optional notes
- View all books in a flat list, sorted by date added (newest first)
- Status is the primary organizer — filter by want/reading/read
- Data lives in data/books.json in the project directory

## Constraints
- No database — flat JSON file only
- No network requests — fully offline
- No categories or shelves — just one flat list with status filtering
- Vanilla JavaScript, no frameworks or build tools`

const FAKE_QUEUE = `# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Search and filter**
Files:
- \`src/search.js\`
- \`src/bookList.js\`
- [build] Add search bar that filters by title or author (case-insensitive substring match)
- [build] Add status filter dropdown (all / want-to-read / reading / read)
- [test] Verify search narrows the list in real-time as you type
- [test] Verify status filter works alone and combined with search

**Export to CSV**
Files:
- \`src/export.js\`
- [build] Add export button that writes all books to a CSV file (title, author, status, notes, date added)
- [test] Verify exported CSV has correct headers and all book data

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Could add a "favorites" tag to quickly find top picks
- [question] Should the JSON file be one big file or split per shelf/category? Currently it's one file but as the list grows it might get slow
- [idea] The book list doesn't show the date a book was added — would be useful for tracking reading pace

### Parked`

const FAKE_REGISTRY = `# REGISTRY

- \`src/app.js\` — main entry point, renders the app shell and routes
- \`src/bookList.js\` — renders the list of all books with status badges
- \`src/addBook.js\` — form component for adding a new book (title, author, status, notes)
- \`src/storage.js\` — reads and writes data/books.json, handles file I/O
- \`src/styles.css\` — global styles and layout
- \`data/books.json\` — data store (not committed to git)`

const FAKE_DECISIONS = `# DECISIONS

Design decisions made during this project. Each entry maps a decision to the commit where it was made.

Format: **[decision name]** — [commit hash] — [what was decided and why]

- **Flat JSON over SQLite** — a1b2c3d — JSON is simpler for a single-user offline app with no query complexity
- **Status field instead of shelves** — d4e5f6a — one flat list with status filtering is simpler than multiple shelf/category structures; keeps the data model flat`

const FAKE_BUILD = `# Active Build

Entry: **Search and filter**
- [build] Add search bar that filters by title or author (case-insensitive substring match)
- [build] Add status filter dropdown (all / want-to-read / reading / read)
- [test] Verify search narrows the list in real-time as you type
- [test] Verify status filter works alone and combined with search

Files:
- src/search.js — new search/filter component
- src/bookList.js — integrate search and filter into list view

Progress:
- [x] src/search.js — done
- [x] src/bookList.js — done

Changes:
- src/search.js: created search component with text input and status dropdown, 85 lines
- src/bookList.js: added import for search component, wired filter logic into list rendering`

const FAKE_CLAUDE_MD = `# CLAUDE.md

<!-- V PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. V -->

This project uses the Sovereign Implementer method.

## Project docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — work to be done, ordered top-to-bottom. Each entry is type-marked: [build], [test], [idea], [question].
- **REGISTRY.md** — components that exist. Updated after each build.
- **DECISIONS.md** — design decisions mapped to the commits where they were made.
- **LOG/** — per-session records of what was built, tested, and decided.

## Workflow

- \`/setup\` — initial project scaffolding (already done if you're reading this).
- \`/plan\` — manage the queue, process captures, resolve questions.
- \`/next\` — execute the top queue entry (build or test).
- \`/done\` — close the build, record what happened, commit.

## Rules for Claude

- SPEC.md is read-only during builds. Edit it only during /plan.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.

## Language

Language: English

<!-- A PLUGIN-MANAGED — do not edit above this line. A -->

## Project rules

- This is a vanilla JavaScript project. No frameworks, no build tools.
- JSON file lives at data/books.json in the project root.
- Keep the UI simple — no animations or transitions.`

// Session-start hook outputs

const SESSION_NO_BUILD = `[Sovereign Implementer] Project is set up.
  SPEC.md: found
  QUEUE.md: found
  REGISTRY.md: found

No active build. Run /plan to manage the queue, or /next to start the top batch.`

const SESSION_ACTIVE_BUILD = `[Sovereign Implementer] Project is set up.
  SPEC.md: found
  QUEUE.md: found
  REGISTRY.md: found

ACTIVE BUILD in progress (_build.md exists). The previous session was interrupted mid-build. Run /next to resume, or /done if the work is complete.`

// ── Schemas ──

const SIM_SCHEMA = {
  type: 'object',
  properties: {
    simulatedResponse: {
      type: 'string',
      description: 'The complete simulated interaction — what Claude would say/do, including assumed user responses at PROMPT stops'
    },
    stepsFollowed: {
      type: 'array',
      items: { type: 'string' },
      description: 'Procedure steps followed, in order (e.g. "Step 1: Read current state")'
    },
    fileChanges: {
      type: 'array',
      items: { type: 'string' },
      description: 'File modifications that would be made (e.g. "QUEUE.md: removed 3 captures")'
    },
    uncertainties: {
      type: 'array',
      items: { type: 'string' },
      description: 'Places where the docs were unclear or ambiguous'
    }
  },
  required: ['simulatedResponse', 'stepsFollowed', 'fileChanges', 'uncertainties'],
  additionalProperties: false
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    phase: { type: 'string' },
    overallScore: { type: 'number', description: '0-10 procedure compliance score' },
    correct: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          aspect: { type: 'string' },
          detail: { type: 'string' }
        },
        required: ['aspect', 'detail']
      }
    },
    deviations: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          aspect: { type: 'string' },
          expected: { type: 'string' },
          actual: { type: 'string' },
          severity: { type: 'string', enum: ['minor', 'major'] }
        },
        required: ['aspect', 'expected', 'actual', 'severity']
      }
    },
    docGaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          whichDoc: { type: 'string' }
        },
        required: ['description', 'whichDoc']
      }
    },
    confusions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          cause: { type: 'string' }
        },
        required: ['description', 'cause']
      }
    }
  },
  required: ['phase', 'overallScore', 'correct', 'deviations', 'docGaps', 'confusions'],
  additionalProperties: false
}

const ANSWERS_SCHEMA = {
  type: 'object',
  properties: {
    answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          answer: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          docsUsed: { type: 'array', items: { type: 'string' }, description: 'Which doc sections informed this answer' }
        },
        required: ['question', 'answer', 'confidence', 'docsUsed']
      }
    }
  },
  required: ['answers'],
  additionalProperties: false
}

const SCORE_SCHEMA = {
  type: 'object',
  properties: {
    scores: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          answerCorrect: { type: 'boolean' },
          answerComplete: { type: 'boolean' },
          docsCoverage: { type: 'string', enum: ['fully-covered', 'partially-covered', 'not-covered'] },
          gaps: { type: 'string', description: 'What the docs are missing or could explain better' }
        },
        required: ['question', 'answerCorrect', 'answerComplete', 'docsCoverage', 'gaps']
      }
    }
  },
  required: ['scores'],
  additionalProperties: false
}

const SYNTHESIS_SCHEMA = {
  type: 'object',
  properties: {
    faqFindings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string', description: 'A question users would naturally ask' },
          suggestedAnswer: { type: 'string', description: 'The answer based on current docs' },
          sourcePhase: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] }
        },
        required: ['question', 'suggestedAnswer', 'sourcePhase', 'confidence']
      }
    },
    otherFindings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          description: { type: 'string' },
          category: { type: 'string', enum: ['doc-gap', 'procedure-bug', 'clarity-issue', 'missing-example', 'tone-issue'] },
          sourcePhase: { type: 'string' }
        },
        required: ['title', 'description', 'category', 'sourcePhase']
      }
    }
  },
  required: ['faqFindings', 'otherFindings'],
  additionalProperties: false
}

// ── Prompt builders ──

function projectState(includeBuild) {
  let state = `Here is the current state of the project files:

--- SPEC.md ---
${FAKE_SPEC}

--- QUEUE.md ---
${FAKE_QUEUE}

--- REGISTRY.md ---
${FAKE_REGISTRY}

--- DECISIONS.md ---
${FAKE_DECISIONS}`

  if (includeBuild) {
    state += `

--- _build.md ---
${FAKE_BUILD}`
  }

  return state
}

function simPrompt(phase) {
  return `You are a fresh instance of Claude. The Sovereign Implementer plugin is installed in this session. You are working on a personal bookshelf tracker app for a non-coder user.

USE ONLY THE DOCS PROVIDED. Do not rely on any prior knowledge of the Sovereign Implementer plugin.

STEP 1 — Read the plugin docs. These are the docs you would receive in a real session:

A) Read the file at ${TEMPLATE}
   This is the project's CLAUDE.md (scaffolded by the plugin).

B) Read the file at ${BEHAVIOUR}
   These are the behaviour rules, loaded by the session_start hook.

C) Read the file at ${phase.procedureFile}
   This is the procedure doc for the skill the user just invoked.

The session_start hook also output:
${phase.sessionStart}

STEP 2 — Here is the project state:

--- Project CLAUDE.md (what the user sees) ---
${FAKE_CLAUDE_MD}

${phase.projectState}

STEP 3 — Simulate the interaction.

SCENARIO: ${phase.scenario}

Walk through the procedure doc step by step. For each step:
1. Name which step you are executing (e.g. "Step 1: Pre-flight checks")
2. Write the exact message you would show the user
3. Describe any file changes you would make
4. At [PROMPT] stops: show what you'd say, then assume the user gives a reasonable response (accepts recommendations, says "yes" to confirmations, gives pass/fail on tests) and continue
5. At [SEQUENCE] steps: process each item one at a time, clearly marking transitions
6. At [SILENT] steps: just describe the actions, don't narrate

If something in the docs is unclear, ambiguous, or seems to be missing, note it explicitly in your uncertainties.

Be thorough. Follow every step. The goal is to test whether these docs are clear enough for a fresh Claude to follow correctly.`
}

function verifyPrompt(simResult, phase) {
  return `You are a procedure auditor. Your job is to determine whether a simulated plugin session followed its procedure doc correctly.

Read the procedure doc at: ${phase.procedureFile}
Also read the behaviour rules at: ${BEHAVIOUR}

Here is what a fresh Claude produced when simulating a /${phase.name} session on a bookshelf tracker project. It was given the procedure doc, the behaviour rules, and the project state shown below.

SIMULATION OUTPUT:
${JSON.stringify(simResult, null, 2)}

PROJECT STATE:
${phase.projectState}

AUDIT CRITERIA — score each:

1. STEP COMPLIANCE: Did it follow each procedure step in the correct order? Were any steps skipped, reordered, or invented?
2. TAG COMPLIANCE: Did it respect response-shape tags ([SILENT], [BRIEF], [PROMPT], [SEQUENCE], [DISCUSS])? Check: was [SILENT] work narrated? Were [PROMPT] stops skipped? Were [SEQUENCE] items bundled?
3. DOC ROUTING: Did it route information to the correct project docs (QUEUE.md, REGISTRY.md, DECISIONS.md, LOG/)?
4. RULE ADHERENCE: Did it follow the Rules section at the bottom of the procedure doc?
5. TONE AND STYLE: Was communication plain, direct, and non-jargon (per behaviour rules)?

For each criterion, note what was correct and what deviated. Rate deviations as:
- "minor" — stylistic or non-harmful; wouldn't confuse the user or break the workflow
- "major" — wrong action, skipped critical step, wrong file modified, would break the workflow

Also identify:
- DOC GAPS: places where the procedure doc was unclear, incomplete, or missing information the simulation needed
- CONFUSIONS: places where the simulation misunderstood something — what specifically caused it?

Be strict. The goal is to find doc improvements, not to be generous.`
}

const USER_QUESTIONS = [
  "What's the difference between the Captures section and the Batches section in QUEUE.md?",
  "I closed the app in the middle of a build. What happens when I reopen it?",
  "Can I edit SPEC.md while doing a build?",
  "I just had an idea for a feature. How do I record it without losing my train of thought?",
  "The queue is empty. Does that mean the project is done?"
]

function answererPrompt() {
  return `You are a fresh instance of Claude. The Sovereign Implementer plugin is installed. A non-coder user is asking you questions about how the plugin workflow works.

USE ONLY THE DOCS PROVIDED. Do not rely on any prior knowledge of the Sovereign Implementer plugin.

Read these docs first:
1. ${TEMPLATE} — the project CLAUDE.md template
2. ${BEHAVIOUR} — behaviour rules
3. ${PLAN_DOC} — /plan procedure
4. ${NEXT_DOC} — /next procedure
5. ${DONE_DOC} — /done procedure

The user also has this project CLAUDE.md:
${FAKE_CLAUDE_MD}

Now answer each question using ONLY what you learned from those docs. For each answer, note which doc sections you drew from and your confidence level (high = docs clearly answer it, medium = docs partially cover it and you inferred the rest, low = docs don't really cover this).

Questions:
${USER_QUESTIONS.map(function(q, i) { return (i + 1) + '. ' + q }).join('\n')}`
}

function scorerPrompt(answers) {
  return `You are an evaluator checking whether a set of answers about the Sovereign Implementer plugin are correct and complete.

Read the authoritative docs:
1. ${TEMPLATE} — CLAUDE.md template
2. ${BEHAVIOUR} — behaviour rules
3. ${PLAN_DOC} — /plan procedure
4. ${NEXT_DOC} — /next procedure
5. ${DONE_DOC} — /done procedure

Here are the answers a fresh Claude gave to 5 user questions, based only on these docs:

${JSON.stringify(answers, null, 2)}

For each answer, evaluate:
1. CORRECT — is the answer factually accurate per the docs?
2. COMPLETE — does it cover everything the user would need to know?
3. DOCS COVERAGE — is this question fully-covered, partially-covered, or not-covered by the current docs?
4. GAPS — if the docs don't fully cover this, what specific information is missing or could be explained better?

Be strict. A "partially-covered" answer means the docs have some relevant info but the reader has to connect dots or infer. "Not-covered" means the docs don't address this at all.`
}

function synthesisPrompt(allFindings) {
  return `You are categorizing findings from a reader-test of the Sovereign Implementer plugin docs. The test simulated three skill sessions (/plan, /next, /done) and a questions panel against a fake bookshelf tracker project.

Here are all the findings:

SKILL SIMULATION VERIFICATIONS:
${JSON.stringify(allFindings.skillVerifications, null, 2)}

QUESTION SCORES:
${JSON.stringify(allFindings.questionScores, null, 2)}

Split ALL findings into two categories:

1. FAQ FINDINGS — things that should become entries in a user-facing FAQ or reference doc. These include:
   - Questions users would naturally ask (from the questions panel and from confusions in simulations)
   - Common misunderstandings revealed by the simulations
   - Workflow concepts that need plain-English explanation
   For each, write a suggested question and answer in plain, non-technical language.

2. OTHER FINDINGS — everything else. These include:
   - Doc gaps (missing information in procedure docs)
   - Procedure bugs (steps that don't work as described)
   - Clarity issues (wording that's confusing or ambiguous)
   - Missing examples (places where an example would help)
   - Tone issues (language that's too technical or alarming)
   For each, give a clear title, description, category, and which phase it came from.

Be thorough. Extract every actionable finding — don't summarize away useful detail. Group related items where it makes sense but don't merge distinct issues.`
}

// ── Skill phases ──

const SKILL_PHASES = [
  {
    name: 'plan',
    procedureFile: PLAN_DOC,
    sessionStart: SESSION_NO_BUILD,
    projectState: projectState(false),
    scenario: 'The user invokes /plan with no additional context. There are 3 items in the Captures section and 2 existing batches. Process the accumulated captures per the procedure.'
  },
  {
    name: 'next',
    procedureFile: NEXT_DOC,
    sessionStart: SESSION_NO_BUILD,
    projectState: projectState(false),
    scenario: 'The user invokes /next. There is no active build (_build.md does not exist). The top batch in QUEUE.md is "Search and filter." Walk through the full procedure from pre-flight checks through presenting the batch.'
  },
  {
    name: 'done',
    procedureFile: DONE_DOC,
    sessionStart: SESSION_ACTIVE_BUILD,
    projectState: projectState(true),
    scenario: 'The user invokes /done. The "Search and filter" build just completed — all items in _build.md are ticked. Walk through the full build close-out: tests, registry update, log entry, commit flow, and handoff.'
  }
]

// ── Execute ──

log('Starting reader test: 3 skill simulations + questions panel')

const [skillResults, questionsScored] = await parallel([
  () => pipeline(
    SKILL_PHASES,
    function(p) {
      return agent(simPrompt(p), {
        label: 'sim:' + p.name,
        phase: 'Simulate',
        schema: SIM_SCHEMA
      })
    },
    function(sim, p) {
      return agent(verifyPrompt(sim, p), {
        label: 'verify:' + p.name,
        phase: 'Verify',
        schema: VERIFY_SCHEMA
      })
    }
  ),
  async function() {
    const answers = await agent(answererPrompt(), {
      label: 'q:answer',
      phase: 'Questions',
      schema: ANSWERS_SCHEMA
    })
    return agent(scorerPrompt(answers), {
      label: 'q:score',
      phase: 'Questions',
      schema: SCORE_SCHEMA
    })
  }
])

log('All simulations and questions complete. Synthesizing findings.')

phase('Synthesize')

const allFindings = {
  skillVerifications: (skillResults || []).filter(Boolean),
  questionScores: questionsScored
}

const synthesis = await agent(synthesisPrompt(allFindings), {
  label: 'synthesize',
  schema: SYNTHESIS_SCHEMA
})

log('Synthesis complete: ' + synthesis.faqFindings.length + ' FAQ findings, ' + synthesis.otherFindings.length + ' other findings')

return synthesis

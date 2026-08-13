# write-in-kattni-voice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a distributable, self-contained skill that instructs an agent to write prose in Kattni's voice across personal and instructional registers.

**Architecture:** A skill folder containing `SKILL.md` (distilled, always-applies voice guidance) and an `examples/` directory of six curated, whole writing samples that show the voice in action. The agent reads the guidance, picks the register, consults matching examples, drafts, and runs a pre-flight checklist.

**Tech Stack:** Markdown. No build system, no code, no runtime dependencies. Verification is structural (file existence, YAML frontmatter validity, filename cross-references) plus a content self-review and a functional sample draft.

## Global Constraints

- Skill folder: `write-in-kattni-voice/` at the repo root (`~/PrimeRadiant/skills`).
- Self-contained and portable: examples live inside the skill folder; no references to paths outside it.
- Frontmatter `name` must be `write-in-kattni-voice` (matches the folder name).
- Preserve Kattni's mixed British/American spelling — never standardize it.
- Exclude blog-format devices (kBits summary lists, Pelican front matter guidance) from the *guidance* — they are out of scope for the voice.
- Curated examples are copied **whole**, verbatim from `writing-examples/` (not trimmed).
- Source of truth for all content decisions: `docs/superpowers/specs/2026-08-12-write-in-kattni-voice-design.md`.

---

## File Structure

Files created by this plan:

- `write-in-kattni-voice/SKILL.md` — the distilled voice guide, how-to workflow, register adaptation, conventions, and pre-flight checklist. Single responsibility: tell the agent how to write in the voice.
- `write-in-kattni-voice/examples/README.md` — one-line index mapping each example file to the register it demonstrates.
- `write-in-kattni-voice/examples/first-major-contribution.md` — copy of `writing-examples/2025_02_23_my-first-major-open-source-project-contribution.md`.
- `write-in-kattni-voice/examples/firefox-is-enough-for-me.md` — copy of `writing-examples/2024_01_10_firefox-is-enough-for-me.md`.
- `write-in-kattni-voice/examples/python-powered-eink-name-badge.md` — copy of `writing-examples/2024_05_15_python-powered-eink-name-badge.md`.
- `write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md` — copy of `writing-examples/2024_03_11_introduction-to-git-and-github-getting-started-with-git.md`.
- `write-in-kattni-voice/examples/scope-creep.md` — copy of `writing-examples/scope-creep.md`.
- `write-in-kattni-voice/examples/review-pr.md` — copy of `writing-examples/review-pr.md`.

---

### Task 1: Scaffold the skill folder and curated examples

**Files:**
- Create: `write-in-kattni-voice/examples/first-major-contribution.md`
- Create: `write-in-kattni-voice/examples/firefox-is-enough-for-me.md`
- Create: `write-in-kattni-voice/examples/python-powered-eink-name-badge.md`
- Create: `write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md`
- Create: `write-in-kattni-voice/examples/scope-creep.md`
- Create: `write-in-kattni-voice/examples/review-pr.md`
- Create: `write-in-kattni-voice/examples/README.md`

**Interfaces:**
- Consumes: source files in `writing-examples/` (committed in root commit `8515377`).
- Produces: six example files at the exact paths above, plus `examples/README.md`. Task 2's `SKILL.md` references these six filenames verbatim.

- [ ] **Step 1: Create the folder and copy the six curated examples verbatim**

```bash
mkdir -p write-in-kattni-voice/examples
cp "writing-examples/2025_02_23_my-first-major-open-source-project-contribution.md" "write-in-kattni-voice/examples/first-major-contribution.md"
cp "writing-examples/2024_01_10_firefox-is-enough-for-me.md" "write-in-kattni-voice/examples/firefox-is-enough-for-me.md"
cp "writing-examples/2024_05_15_python-powered-eink-name-badge.md" "write-in-kattni-voice/examples/python-powered-eink-name-badge.md"
cp "writing-examples/2024_03_11_introduction-to-git-and-github-getting-started-with-git.md" "write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md"
cp "writing-examples/scope-creep.md" "write-in-kattni-voice/examples/scope-creep.md"
cp "writing-examples/review-pr.md" "write-in-kattni-voice/examples/review-pr.md"
```

- [ ] **Step 2: Verify all six copies exist and are non-empty**

Run:
```bash
ls -1 write-in-kattni-voice/examples/*.md | wc -l
find write-in-kattni-voice/examples -name '*.md' -empty
```
Expected: first command prints `6`; second command prints nothing (no empty files). Note: `README.md` does not exist yet, so `*.md` matches exactly the six copies.

- [ ] **Step 3: Confirm copies are byte-identical to their sources**

Run:
```bash
diff "writing-examples/2025_02_23_my-first-major-open-source-project-contribution.md" "write-in-kattni-voice/examples/first-major-contribution.md" && \
diff "writing-examples/2024_01_10_firefox-is-enough-for-me.md" "write-in-kattni-voice/examples/firefox-is-enough-for-me.md" && \
diff "writing-examples/2024_05_15_python-powered-eink-name-badge.md" "write-in-kattni-voice/examples/python-powered-eink-name-badge.md" && \
diff "writing-examples/2024_03_11_introduction-to-git-and-github-getting-started-with-git.md" "write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md" && \
diff "writing-examples/scope-creep.md" "write-in-kattni-voice/examples/scope-creep.md" && \
diff "writing-examples/review-pr.md" "write-in-kattni-voice/examples/review-pr.md" && echo "ALL IDENTICAL"
```
Expected: `ALL IDENTICAL` (every `diff` is silent).

- [ ] **Step 4: Write the examples index**

Create `write-in-kattni-voice/examples/README.md` with exactly this content:

```markdown
# Voice Examples

Curated samples of Kattni's writing, spanning her registers. Read the one or two
that match the register of the piece you are drafting.

| File | Register it demonstrates |
| --- | --- |
| `first-major-contribution.md` | Long personal narrative — vulnerability, inline jargon asides |
| `firefox-is-enough-for-me.md` | Short opinion / practical — punchy "Done." closers |
| `python-powered-eink-name-badge.md` | Hands-on tutorial — personal intro plus step-by-step teaching |
| `intro-to-git-getting-started-with-git.md` | Rich teaching voice — analogies and a "Git will help you along the way" tone (long; the deep teaching reference) |
| `scope-creep.md` | Concise conceptual explainer |
| `review-pr.md` | Values / process — kind, THINK-style feedback register |
```

- [ ] **Step 5: Verify every filename in the index resolves to a real file**

Run:
```bash
cd write-in-kattni-voice/examples && \
for f in $(grep -oE '`[a-z0-9-]+\.md`' README.md | tr -d '`' | sort -u); do \
  test -f "$f" && echo "OK $f" || echo "MISSING $f"; \
done; cd - >/dev/null
```
Expected: six `OK` lines, no `MISSING` lines.

- [ ] **Step 6: Commit**

```bash
git add write-in-kattni-voice/examples
git commit -m "Add curated voice examples for write-in-kattni-voice skill"
```

---

### Task 2: Write SKILL.md

**Files:**
- Create: `write-in-kattni-voice/SKILL.md`

**Interfaces:**
- Consumes: the six example filenames produced by Task 1 (referenced by name in the "How to use" section).
- Produces: the complete skill entry point. No later task depends on internal anchors here.

- [ ] **Step 1: Write `write-in-kattni-voice/SKILL.md` with exactly this content**

````markdown
---
name: write-in-kattni-voice
description: Use when writing prose meant to sound like Kattni — blog posts, tutorials, documentation, announcements, or reflections. Captures Kattni's voice across personal and instructional registers, drawing on distilled guidance and curated writing samples.
---

# Write in Kattni's Voice

Use this skill whenever you are writing prose that should sound like Kattni —
blog posts, tutorials, documentation, announcements, or reflections. It works
across two registers: personal (storytelling, reflection, opinion) and
instructional (tutorials, how-tos, process and values guidance).

## How to use this skill

1. Read this whole file first. The Core Principles always apply.
2. Identify the register the task calls for (personal, instructional, or
   process/values).
3. Open the one or two files in `examples/` that match that register — see
   `examples/README.md` for the index — and read them to hear the voice.
4. Draft the piece.
5. Run the Pre-flight Checklist at the bottom before returning the draft.

## Core principles (always apply)

- **Accessible by default.** Assume the reader may be new to the topic. Never
  gatekeep, and never make the reader feel small for not knowing something.
- **First person, conversational, and emotionally honest.** Be willing to be
  vulnerable and to name your own limits ("definitely outside my wheelhouse").
- **Warm and supportive.** The reader is a person you want to help succeed.
- **Honest, not oversold.** Don't overpromise ("I'm not suggesting it will work
  for you, but…"). Name limitations and trade-offs plainly.
- **Thorough.** Explain the *why*, not just the *what*.

## Signature moves

- **Parenthetical jargon asides.** Define terms inline, in parentheses, so
  newcomers aren't left behind — for example, "(A pull request is the method to
  contribute to a project whose code is hosted on GitHub.)" This is the single
  most distinctive move. Use it whenever a term might trip up a newcomer.
- **Sentences that breathe.** Write long, flowing sentences with multiple
  clauses joined by semicolons and em-dashes — then land a short, punchy closer
  ("Done." / "It counts!" / "Onto the next thing!"). The contrast is the rhythm.
- **The teaching scaffold** (instructional register): concept → "For example, to
  X, you would include:" → code block → "Which ends up rendered as:" or the
  expected output. Keep it consistent and predictable.
- **Analogy-driven explanation.** Introduce an abstract or intimidating concept
  with a concrete, everyday analogy (save points in a video game; an R&D lab
  versus the factory floor; a taco versus a stir-fry shopping list).
- **Italics for emphasis** on individual words (_that_, _specific_, _highly_).

## Register adaptation

**Stays constant across every register:** warmth, accessibility, honesty, first-
person presence, and defining jargon inline.

**Flexes by register:**

- **Personal / storytelling** (essays, reflections, announcements): longer
  narrative arcs, more emotional openness, your own first-person experience
  front and center. See `examples/first-major-contribution.md` and
  `examples/firefox-is-enough-for-me.md`.
- **Instructional / tutorial** (how-tos): the teaching scaffold, step-by-step
  structure, analogies, expected-output blocks — still warm and first person
  ("I suggest…", "you'll want to…"). See
  `examples/python-powered-eink-name-badge.md` and
  `examples/intro-to-git-getting-started-with-git.md`.
- **Process / values** (guidance, opinion): concise and principle-driven; lead
  with the core idea and keep it tight. See `examples/scope-creep.md` and
  `examples/review-pr.md`.

## Conventions

- **Spelling: preserve the mix.** Kattni uses British and American spellings
  interchangeably (e.g. "realised" alongside "harbor"). Do not standardize
  either direction.
- **Punctuation:** em-dashes and semicolons carry the long, multi-clause
  sentences; italics mark single-word emphasis.
- **Explanation style:** reach for a concrete analogy when introducing an
  abstract or intimidating idea.

## What to avoid

- Gatekeeping or condescension toward newcomers.
- Overselling or overpromising.
- Clipped, robotic, uniformly short sentences — the voice breathes.
- Leaving a newcomer behind by using undefined jargon.
- Copying blog-specific format devices (summary "kBits" lists, blog front
  matter). Those belong to Kattni's blog format, not her voice.

## Pre-flight checklist

Before returning a draft, verify:

- [ ] Jargon is defined inline for a newcomer.
- [ ] Sentences vary in length; long flowing sentences are balanced by short closers.
- [ ] Tone is warm, honest, and non-gatekeeping.
- [ ] Register matches the task (personal / instructional / process).
- [ ] For instructional content, the concept → example → expected-output scaffold is used where it fits.
- [ ] No overselling; limitations are named honestly.
- [ ] Spelling mix left as-is (not standardized).
````

- [ ] **Step 2: Verify the YAML frontmatter parses and has the required fields**

Run:
```bash
python3 -c "
import sys
text = open('write-in-kattni-voice/SKILL.md').read()
assert text.startswith('---'), 'no frontmatter'
fm = text.split('---', 2)[1]
import yaml  # PyYAML; if unavailable, use the fallback check below
data = yaml.safe_load(fm)
assert data['name'] == 'write-in-kattni-voice', data.get('name')
assert 'description' in data and len(data['description']) > 20
print('FRONTMATTER OK')
"
```
Expected: `FRONTMATTER OK`.

If PyYAML is not installed, run this dependency-free fallback instead:
```bash
python3 -c "
text = open('write-in-kattni-voice/SKILL.md').read()
assert text.startswith('---'), 'no frontmatter'
fm = text.split('---', 2)[1]
lines = dict(l.split(':', 1) for l in fm.strip().splitlines() if ':' in l)
assert lines['name'].strip() == 'write-in-kattni-voice', lines.get('name')
assert len(lines['description'].strip()) > 20
print('FRONTMATTER OK')
"
```
Expected: `FRONTMATTER OK`.

- [ ] **Step 3: Verify every example filename referenced in SKILL.md exists on disk**

Run:
```bash
for f in $(grep -oE 'examples/[a-z0-9-]+\.md' write-in-kattni-voice/SKILL.md | sort -u); do \
  test -f "write-in-kattni-voice/$f" && echo "OK $f" || echo "MISSING $f"; \
done
```
Expected: one `OK` line per referenced file (six unique), no `MISSING`.

- [ ] **Step 4: Self-review SKILL.md against the spec**

Open `docs/superpowers/specs/2026-08-12-write-in-kattni-voice-design.md` and confirm the SKILL.md body covers every item in the spec's "Distilled voice: core principles", "Signature moves", "Register adaptation", "Conventions", "What to avoid", and "Pre-flight checklist" sections. Confirm kBits/blog-format devices appear only under "What to avoid" (never as guidance to follow). Fix any gap inline.

- [ ] **Step 5: Commit**

```bash
git add write-in-kattni-voice/SKILL.md
git commit -m "Add SKILL.md for write-in-kattni-voice skill"
```

---

### Task 3: Functional validation — draft a sample and confirm the voice

This task proves the skill works end to end. It produces a throwaway sample (kept
in the scratchpad, not committed into the skill) for Kattni to judge.

**Files:**
- Create (scratch, not committed): `<scratchpad>/kattni-voice-sample.md`

**Interfaces:**
- Consumes: the finished `write-in-kattni-voice/SKILL.md` and `examples/`.
- Produces: a sample draft plus a checklist verdict for the user.

- [ ] **Step 1: Draft a sample using only the skill**

Choose one small, register-spanning prompt (default: a ~200-word tutorial-style
explainer on "what a git branch is and why you'd use one"). Following
`write-in-kattni-voice/SKILL.md` and the matching examples, write the sample to
`<scratchpad>/kattni-voice-sample.md`. Do not reuse sentences from the examples;
write fresh prose in the voice.

- [ ] **Step 2: Score the sample against the Pre-flight Checklist**

Go through each checklist item in `SKILL.md` against the sample. Write a one-line
pass/fail note per item beneath the sample. If any item fails, revise the sample
and, if the failure points to a gap in the guidance, note the SKILL.md fix needed.

- [ ] **Step 3: Present to the user for acceptance**

Show Kattni the sample and the checklist verdict. Ask whether it sounds like her.
If she requests changes to the voice guidance, capture them as follow-up edits to
`SKILL.md` (and re-run Task 2 Steps 2–5). This is the acceptance gate for the
skill.

---

## Self-Review

**1. Spec coverage:**
- Purpose / approach (hybrid distilled + curated) → Tasks 1 & 2. ✓
- Skill structure (SKILL.md + examples/ + README) → Task 1 (examples, README), Task 2 (SKILL.md). ✓
- SKILL.md sections (when/how, principles, signature moves, register adaptation, conventions, what to avoid, checklist) → Task 2 Step 1 content. ✓
- Distilled voice principles, signature moves, register adaptation, conventions, what-to-avoid, pre-flight checklist → all present verbatim in Task 2 Step 1. ✓
- description/trigger wording → frontmatter in Task 2 Step 1. ✓
- Curated 6-file set with README index → Task 1. ✓
- Constraints: distributable/self-contained, whole copies, spelling mix preserved, kBits excluded → Global Constraints + Task 1 Step 3 (verbatim copies) + Task 2 content. ✓
- Functional proof the skill works → Task 3. ✓

**2. Placeholder scan:** No TBD/TODO/"add error handling" style placeholders. All file content is given in full. ✓

**3. Type/name consistency:** The six example filenames are identical across the File Structure list, Task 1 `cp` targets, Task 1 README table, and Task 2 SKILL.md references: `first-major-contribution.md`, `firefox-is-enough-for-me.md`, `python-powered-eink-name-badge.md`, `intro-to-git-getting-started-with-git.md`, `scope-creep.md`, `review-pr.md`. Frontmatter `name` (`write-in-kattni-voice`) matches the folder name in every task. ✓

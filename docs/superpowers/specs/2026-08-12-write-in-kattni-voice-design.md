# Design: `write-in-kattni-voice` skill

**Date:** 2026-08-12
**Status:** Approved design, ready for implementation planning

## Purpose

A distributable, self-contained skill that instructs an agent to write prose in
Kattni's voice. When invoked, the agent produces blog posts, tutorials,
documentation, announcements, or reflections that sound like Kattni across both
her personal and instructional registers.

The voice is derived from a set of Kattni's own writing samples. The skill
combines distilled, always-applies guidance with a curated set of full examples
the agent consults for reference.

## Goals

- Capture Kattni's voice broadly and adapt register to the task (personal
  storytelling vs. instructional/process writing).
- Be self-contained and portable so it can be handed to others or published.
- Give the agent crisp, actionable rules *plus* real examples that show the
  voice in action.

## Non-goals

- Not a template for adapting to *other* people's voices — this skill is
  specifically Kattni's voice.
- Not a blog-format replicator. Blog-specific structural devices (e.g. the
  "kBits" summary list, Pelican front matter) are **out of scope** — they belong
  to Kattni's personal-blog format, not her voice.

## Approach

Hybrid: distilled guidance in `SKILL.md` (the fast, reliable part the agent
follows every time) plus a curated set of full example files organized by
register (the part that shows the voice in action for subtle traits like
parenthetical asides and long, flowing sentences).

## Skill structure

```
write-in-kattni-voice/
├── SKILL.md                     distilled voice guide + how-to + register adaptation + checklist
└── examples/
    ├── README.md                one-line index: which file demonstrates which register
    └── (6 curated .md files)    Kattni's actual writing, spanning the registers
```

The agent's workflow:

1. Read `SKILL.md` (the distilled, always-applies guidance).
2. Identify the register the task calls for.
3. Consult the one or two `examples/` files matching that register.
4. Draft.
5. Run the pre-flight checklist before returning the draft.

## `SKILL.md` contents

### Frontmatter

- `name: write-in-kattni-voice`
- `description:` "Use when writing prose meant to sound like Kattni — blog posts,
  tutorials, documentation, announcements, or reflections. Captures Kattni's
  voice across personal and instructional registers, drawing on distilled
  guidance and curated writing samples."

### Body sections

1. **When to use / how to use** — the 5-step workflow above.
2. **Core voice principles** — the always-applies distilled traits (below).
3. **Signature moves** — the concrete techniques (below).
4. **Register adaptation** — what flexes vs. what stays constant (below).
5. **Conventions** — spelling, punctuation, analogy style (below).
6. **What to avoid** (below).
7. **Pre-flight checklist** (below).

## Distilled voice: core principles

These always apply, regardless of register.

- **Accessible by default.** Assume the reader may be new to the topic. Never
  gatekeep or make the reader feel small for not knowing something.
- **First-person, conversational, and emotionally honest.** Willing to be
  vulnerable and to name her own limits ("definitely outside my wheelhouse").
- **Warm and supportive.** The reader is a person she wants to help succeed.
- **Honest, not oversold.** Doesn't overpromise ("I'm not suggesting it will
  work for you, but…"); names limitations and trade-offs plainly.
- **Thorough.** Explains the *why*, not just the *what*.

## Signature moves

- **Parenthetical jargon asides.** Defines terms inline, in parentheses, so
  newcomers aren't left behind — e.g. "(A pull request is the method to
  contribute to a project whose code is hosted on GitHub.)" This is her single
  most distinctive move.
- **Long, flowing sentences** with multiple clauses, semicolons, and em-dashes —
  punctuated by short, punchy closers ("Done." / "It counts!" / "Onto the next
  thing!").
- **Teaching scaffold** (instructional register): concept → "For example, to X,
  you would include:" → code block → "Which ends up rendered as:" / expected
  output. Consistent and predictable.
- **Analogy-driven explanation.** Explains abstract concepts with concrete,
  everyday analogies (save points in a video game, an R&D lab vs. the factory
  floor, a taco vs. stir-fry shopping list).
- **Italics for emphasis** on individual words (_that_, _specific_, _highly_).

## Register adaptation

**Stays constant across all registers:** warmth, accessibility, honesty,
first-person presence, defining jargon inline.

**Flexes by register:**

- *Personal / storytelling* (essays, reflections, announcements): longer
  narrative arcs, more emotional openness, first-person experience front and
  center.
- *Instructional / tutorial* (how-tos): the teaching scaffold, step-by-step
  structure, analogies, expected-output blocks; still warm and first-person
  ("I suggest…", "you'll want to…").
- *Process / values* (guidance, opinion): concise, principle-driven, kind;
  leads with the core idea, keeps it tight (see `scope-creep`, `review-pr`).

## Conventions

- **Spelling: preserve the mix.** Kattni uses British and American spellings
  interchangeably (e.g. "realised" alongside "harbor"). Do not standardize.
- **Punctuation:** em-dashes and semicolons for flowing multi-clause sentences;
  italics for single-word emphasis.
- **Explanation style:** reach for a concrete analogy when introducing an
  abstract or intimidating concept.

## What to avoid

- Gatekeeping or condescension toward newcomers.
- Overselling or overpromising.
- Clipped, robotic, uniformly short sentences (the voice breathes).
- Leaving a newcomer behind by using undefined jargon.
- Replicating blog-specific format devices (kBits, front matter) — out of scope.

## Pre-flight checklist

Before returning a draft, verify:

- [ ] Jargon is defined inline for a newcomer.
- [ ] Sentences vary in length; long flowing sentences are balanced by short closers.
- [ ] Tone is warm, honest, and non-gatekeeping.
- [ ] Register matches the task (personal / instructional / process).
- [ ] For instructional content, the concept → example → expected-output scaffold is used where it fits.
- [ ] No overselling; limitations are named honestly.
- [ ] Spelling mix left as-is (not standardized).

## Curated example set (6 files)

Copied into `examples/`, spanning the full range. `examples/README.md` indexes
each with a one-line note on the register it demonstrates.

| File | Register demonstrated |
|---|---|
| `first-major-contribution` | Long personal narrative — vulnerability, jargon asides |
| `firefox-is-enough-for-me` | Short opinion/practical — punchy "Done." closers |
| `python-powered-eink-name-badge` | Hands-on tutorial — personal + step-by-step teaching |
| `intro-to-git-getting-started-with-git` | Rich teaching voice — analogies, "help along the way" tone (long; kept as the deep teaching reference) |
| `scope-creep` | Concise conceptual explainer |
| `review-pr` | Values/process — kind, THINK-style register |

Source files live in `writing-examples/`. Filenames in `examples/` may be
shortened from the dated originals for clarity.

## Constraints and decisions

- Distributable and self-contained; examples travel inside the skill folder.
- All provided writing samples are treated as authoritative sources of the
  voice.
- Curated subset (not all 13, not trimmed copies): 6 representative files kept
  whole.
- kBits and other blog-format devices explicitly excluded.

## Resolved decisions

- **Skill folder location:** built in this directory (`~/PrimeRadiant/skills`),
  as `write-in-kattni-voice/`.
- **Version control:** this directory is now a git repo; the spec and skill are
  committed here.

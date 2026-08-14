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

**A note on the examples.** The samples in `examples/` are written in a *dense*
form of this voice — Kattni at full tilt, with far more em dashes, semicolons,
and jargon asides than her typical writing. (A count across a wide sample of
her other writing found close to zero true em dashes and only a handful of
semicolons per piece — this voice runs much leaner than these examples
suggest.) Read them for tone, warmth, structure, and word choice, but do not
mechanically match their punctuation density or their frequency of asides. Aim
noticeably lighter than the examples; the Conventions and the Pre-flight
Checklist below set the target.

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

- **Short, blunt sentences carry the rhythm.** This is the primary device, not a
  fallback: "Done." "That's it." "It stopped me." A short declarative or
  fragment, dropped after one or two longer sentences, does the work that a
  semicolon or em dash might otherwise be asked to do. Reach for a short
  sentence before you reach for either mark.
- **Em dashes and semicolons are rare — treat them as nearly absent, not
  "occasional."** In a wide sample of Kattni's writing, true em dashes were
  close to nonexistent and semicolons were sparse even in her longest pieces.
  Default to a comma, a period, or a new sentence. If either mark shows up more
  than once or twice in an entire piece, cut it.
- **Parentheticals do more than define jargon.** Use them for asides, caveats,
  scope-limiting notes, or a flash of self-commentary — not only "(here's what
  that term means)." For example, "(Some of it is where this series is going.)"
  is a parenthetical that has nothing to do with jargon. When a term genuinely
  does need a gloss, a plain sentence works as well as a parenthetical — use
  whichever reads more naturally, and use either sparingly.
- **Show the meaning before you define it, when you can.** Rather than opening
  with a parenthetical gloss, let the reader watch a concept in action — a
  scene, an example, a consequence — then name it plainly once they've felt it.
  Fall back to an upfront definition only when the term has to be understood
  before the sentence around it makes sense at all.
- **Rhetorical questions set up an explanation.** Voice the question the reader
  is likely holding — "What's a singleton?" "So which one do you choose?" —
  then answer it in the sentences that follow. Use this to pivot into a new
  point, not as decoration; if you're not about to answer it, don't ask it.
- **Reassurance asides name the reader's doubt and answer it.** When a step is
  likely to worry or confuse someone, say so directly ("This is normal." "If
  that sounds slow — it is, for about ten minutes.") rather than only
  gesturing at warmth in the abstract. This is a specific move, not just a
  tone: notice the friction point, name it, then move past it.
- **The teaching scaffold** (instructional register): concept → "For example,
  to X, you would include:" → code block → a plain-English paraphrase of what
  the code or step actually does ("This tells Python to...") → the expected
  output → an invitation to try a variation ("Try changing X to Y and see what
  happens"). Not every step needs every piece, but the paraphrase and the
  invitation to experiment are what make it read as teaching rather than a
  manual.
- **Analogy-driven explanation.** Introduce an abstract or intimidating concept
  with a concrete, everyday analogy (save points in a video game; an R&D lab
  versus the factory floor; a taco versus a stir-fry shopping list).
- **Bold and italics, each with a job.** Italics mark single-word emphasis
  (_that_, _specific_, _highly_). Bold is reserved for a load-bearing statement
  or a direct warning aimed at the reader — the sentence you'd want them to
  catch even skimming ("**Always pin to a commit hash...**", "**no code until
  there's a design you've agreed to**"). Both are used sparingly; if more than
  a phrase or two per section is bold, it's stopped meaning anything.
- **Forward-pointing closers.** End a piece — or a section — by pointing at
  what comes next, rather than just summarizing what came before ("Next time,
  we take this design and turn it into an actual plan."). This matters most
  when the piece is explicitly part of a series: say so, and give the reader a
  reason to come back.

## Register adaptation

**Stays constant across every register:** warmth, accessibility, honesty,
first-person presence, and near-absent em dashes/semicolons (see Signature
moves).

**Flexes by register:**

- **Personal / storytelling** (essays, reflections, announcements): longer
  narrative arcs, more emotional openness, your own first-person experience
  front and center. Ground strong emotion in specific numbers or facts (an
  exact week count, a file count) rather than escalating language — precision
  reads as more honest than intensity. An occasional repeated sentence-opening
  ("It explains everything. It explains all of my symptoms.") can build
  emphasis. Mild profanity shows up rarely, only in genuinely raw personal
  writing, never in instructional content — an option to reach for, not a
  requirement. See `examples/first-major-contribution.md` and
  `examples/firefox-is-enough-for-me.md`.
- **Instructional / tutorial** (how-tos): the teaching scaffold, step-by-step
  structure, analogies, expected-output blocks — still warm and first person
  ("I suggest…", "you'll want to…"). See
  `examples/python-powered-eink-name-badge.md` and
  `examples/intro-to-git-getting-started-with-git.md`.
- **Process / values** (guidance, opinion): concise and principle-driven; lead
  with the core idea and keep it tight. See `examples/scope-creep.md` and
  `examples/review-pr.md`.

**Opening moves also flex by register.** Personal / storytelling pieces tend to
open flat and factual — state the situation directly (a date, a decision, a
scenario) rather than building up to it with a hook. Instructional and project
pieces tend to open with a relatable problem or a direct question that puts
the reader's own situation on the page before any instruction begins. Don't
default to the same opening move regardless of what you're writing.

## Conventions

- **Spelling: preserve the mix.** Kattni uses British and American spellings
  interchangeably (e.g. "realised" alongside "harbor"). Do not standardize
  either direction.
- **Punctuation: keep it lean.** Em dashes and semicolons are rare in this
  voice — most pieces use very few, some use none at all. Default to commas and
  periods; let short sentences do the rhythmic work instead. Italics mark
  single-word emphasis, used sparingly.
- **Exclamation points: an open question, watch this.** Some of Kattni's
  tutorial writing leans on them heavily, but it's unclear how much of that is
  personal voice versus a genre convention from writing for a company. Default
  to using them for genuine, earned excitement — a real milestone, a real win
  — not as a tic on every short sentence. If this starts looking like the
  em-dash problem, calibrate it the same way: cut back hard.
- **Explanation style:** reach for a concrete analogy when introducing an
  abstract or intimidating idea.

## What to avoid

- Gatekeeping or condescension toward newcomers.
- Overselling or overpromising.
- Uniform staccato. Short sentences are the primary rhythm device, but they
  need longer sentences around them for the contrast to land — all-short reads
  as robotic too.
- Showing a concept without ever naming it. "Show the meaning before you
  define it" still ends in naming the term plainly — it's not permission to
  skip the definition.
- Reflexive use of any signature device — parentheticals, bold, rhetorical
  questions, reassurance asides, forward-pointing closers. Each earns its
  place by doing real work in that spot; used on a schedule, any of them turns
  into a tic instead of a voice.
- Forcing a "next time..." closer onto a piece that isn't actually part of a
  series.
- Opening every piece the same way regardless of register.
- Leaving a newcomer behind by using undefined jargon.
- Copying blog-specific format devices (summary "kBits" lists, blog front
  matter). Those belong to Kattni's blog format, not her voice.

## Pre-flight checklist

Before returning a draft, verify:

- [ ] Em dashes and semicolons are rare — most pieces have very few or none. If either appears more than once or twice in the whole piece, cut it.
- [ ] Short, blunt sentences appear after longer ones to create rhythm. This is the primary punctuation device — not em dashes or semicolons.
- [ ] Parentheticals, if used at all, do real work (an aside, a caveat, a genuinely needed definition) rather than being a reflex. A whole piece usually needs only a few, if any.
- [ ] Where a term is defined, check whether showing it in action first (then naming it) would work better than an upfront gloss.
- [ ] Sentences vary in length, and the long ones land on short closers.
- [ ] Tone is warm, honest, and non-gatekeeping.
- [ ] Register matches the task (personal / instructional / process), and the opening move matches the register (flat/factual for personal; a relatable problem or question for instructional/project).
- [ ] Rhetorical questions, reassurance asides, and bold are used only where they genuinely earn their place — not sprinkled by default.
- [ ] For instructional content, the scaffold includes a plain-English paraphrase after the code and an invitation to try a variation, where it fits.
- [ ] If the piece is part of a series, it closes by pointing at what's next rather than only summarizing.
- [ ] No overselling; limitations are named honestly.
- [ ] Spelling mix left as-is (not standardized).

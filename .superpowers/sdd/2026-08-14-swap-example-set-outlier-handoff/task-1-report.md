# Task 1 Report: Replace the density-outlier instructional example

## Status

DONE_WITH_CONCERNS

## Selected sources

- **Enough Markdown to Get You By in Most Cases** replaces the Git tutorial.
  It is a complete Kattni-authored Markdown tutorial with an approachable,
  concept-to-example structure. It wins the replacement slot because it is
  materially leaner than the removed outlier: zero true em dashes, zero
  semicolon punctuation marks, and no prose parenthetical asides under the
  counting method below.
- **Canary Nightlight** is the seventh, complementary instructional example.
  Its complete project guide combines warm personal framing (including the
  Birdhouse In Your Soul reference), a build, code explanation, and assembly
  instructions. It supplies the project-style tutorial register requested by
  the user amendment.

## Files changed

- Modified: `write-in-kattni-voice/SKILL.md`
- Modified: `write-in-kattni-voice/examples/README.md`
- Added: `write-in-kattni-voice/examples/enough-markdown-to-get-you-by-in-most-cases.md`
- Added: `write-in-kattni-voice/examples/canary-nightlight.md`
- Removed: `write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md`
- Added: `.superpowers/sdd/2026-08-14-swap-example-set-outlier-handoff/task-1-report.md`

## Source fidelity

Enough Markdown was copied verbatim from the local original
`writing-examples/2024_03_07_enough-markdown-to-get-you-by-in-most-cases.md`.
The original and bundled copy have the identical SHA-256:

```text
7721893447203df0e5bfc2cc2a4e4ce7ae6d4a9e5ba7447d377fc2103810fb9b
```

The source has no terminal newline; the bundled copy preserves that byte
exactly. `cmp -s` passed.

Canary Nightlight was copied verbatim from the official site Text View source
at `https://learn.adafruit.com/canary-nightlight.md?view=all`, supplied locally
as `/private/tmp/canary-nightlight-official.md`. The official source and
bundled copy are both 989 lines and 51,014 bytes with the identical SHA-256:

```text
a80c9facf3545961ef10dac915dedf012bebe912e2c84a3322d94810c1d8bb05
```

`cmp -s` passed. The source's `&nbsp;` entities are preserved verbatim.

## Density audit

Word counts use the controller's normalized source-tokenization record.
Punctuation was independently checked across the full source by stripping HTML
entities before counting `—` and `;`. Prose parentheticals were manually
classified after excluding Markdown link/image syntax, inline and fenced code,
and notation such as Canary's `(X)`, `(Y)`, `(Z)`, and `LED(s)`.

| Piece | Words | True em dashes | Semicolon punctuation | Prose parentheticals |
| --- | ---: | ---: | ---: | ---: |
| Removed Git tutorial | 6,907 | 0 | 6 | 10 |
| Enough Markdown | 2,474 | 0 | 0 | 0 |
| Canary Nightlight | 7,506 | 0 | 3 | 11 |

Canary's raw semicolon character count is not meaningful because `&nbsp;`
contains a semicolon. After those entities are removed, the guide contains
three semicolon punctuation marks.

## Verification

- `shasum -a 256 ...` and `cmp -s ...`: both bundled files match their
  official originals byte-for-byte.
- Entity-stripped punctuation check: Git `0/6`, Enough `0/0`, Canary `0/3`
  for em dashes/semicolons.
- Extracted every `examples/*.md` reference from `SKILL.md`: seven references,
  all existing.
- Parsed `examples/README.md`: exactly the seven intended filenames, all
  existing.
- `git diff --check HEAD~2..HEAD`: reports trailing whitespace inherited from
  the official source text in both new examples. It is intentionally retained
  because removing it would break the byte-for-byte fidelity checks.
- Stale-reference scan for `intro-to-git-getting-started-with-git.md`: none.
- `git status --short` before committing: only the five intended implementation
  changes were present.

## Commit

Implementation commit: `a94b6ea5448fddfdbd65f4b5dcec73f23da3b394`
(`Replace density-outlier tutorial examples`).

## Self-review and concerns

Self-review found no scope drift: `SKILL.md` changes only the instructional
example filenames, and `README.md` only changes the example inventory. Both
new examples are full, unedited source copies. The sole concern is the
intentional trailing whitespace inherited from the official source files,
which `git diff --check` reports. Source fidelity takes precedence over
normalising it.

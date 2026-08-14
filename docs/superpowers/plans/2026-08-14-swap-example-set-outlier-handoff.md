# Handoff: Replace the density-outlier example in write-in-kattni-voice

**Status:** Open task, not started. Prepared as a standalone handoff — this
document should be fully self-contained. You should not need any other
context, conversation history, or memory system to execute this correctly.

## Background

This repository (`~/PrimeRadiant/skills`, or wherever you've cloned/opened
it) contains a Claude/AI-agent skill called `write-in-kattni-voice`, at
`write-in-kattni-voice/`. It teaches an AI agent to write prose in the voice
of a specific person, Kattni. It has two parts:

- `write-in-kattni-voice/SKILL.md` — distilled, written-out voice guidance
  (tone, sentence rhythm, punctuation habits, structural devices, a
  pre-flight checklist).
- `write-in-kattni-voice/examples/` — six **whole, verbatim** writing
  samples from Kattni's own writing, bundled directly into the skill folder
  (the skill is meant to be fully self-contained and portable — no live web
  access at runtime), plus `examples/README.md`, a one-line index of which
  file demonstrates which register (personal / instructional / process).

The skill went through two rounds of calibration already (see `git log` in
this repo for the commit history and messages — search for "calibrate" and
"rewrite voice guidance" to read the full reasoning). The key finding from
that work: Kattni's actual writing uses **far fewer em dashes, semicolons,
and parenthetical jargon-definitions** than the skill originally assumed. A
programmatic count across a large sample of her real writing found close to
**zero true em dashes** and only a handful of semicolons per piece. The
guidance in `SKILL.md` has already been rewritten to reflect this.

## The specific problem this task fixes

One of the six bundled example files —
`write-in-kattni-voice/examples/intro-to-git-getting-started-with-git.md` —
was confirmed during that calibration work to be a **density outlier**: it's
noticeably heavier on em dashes, semicolons, and jargon-defining
parentheticals than Kattni's writing typically is, even by her own standard.

`SKILL.md` already contains a warning (see the "A note on the examples"
callout near the top of the file) telling an agent not to mechanically match
the bundled examples' punctuation density. But the underlying **file itself**
was never replaced — the warning is a workaround, not a fix. That's what this
task is for.

**Why it wasn't done already:** a previous work session had several
subagents read Kattni's wider writing corpus (her blog, ~30 tutorial guides
she wrote for a previous employer, a project contribution guide) to diagnose
the density problem. Those subagents were told to return **style analysis
only** — short quotes and summaries, not full text — so there's no
ready-to-bundle replacement sitting anywhere. That reading needs to happen
again, this time capturing full verbatim text of one real candidate.

## The task

Find one genuinely representative, **leaner** piece of Kattni's writing in
the **instructional/tutorial register**, and either replace
`intro-to-git-getting-started-with-git.md` with it, or add it as a seventh
example alongside it (see "Decision point" below).

## Where to look

**Start here — already confirmed lean.** A prior session did a programmatic
em-dash/semicolon count on six of Kattni's tutorial guides (part of the
Adafruit Learn platform, written for a previous employer, "Adafruit") and
confirmed all six are lean — closer to the target density than the current
outlier example. Check these first, before the wider list:

- https://learn.adafruit.com/scrolling-countdown-timer
- https://learn.adafruit.com/intro-to-mastodon-api-circuitpython
- https://learn.adafruit.com/wifi-mailbox-notifier
- https://learn.adafruit.com/excellent-github-profile
- https://learn.adafruit.com/github-actions-status-tower-light
- https://learn.adafruit.com/canary-nightlight

Of these, **"Canary Nightlight"** stood out in the earlier style analysis for
carrying a strong personal touch (Kattni names a They Might Be Giants lyric
as "one of Kattni's favorite songs" mid-guide) — a good sign of personal
voice showing through the tutorial format, worth checking first.

These guides are multi-page — read every page of whichever one you pick, not
just the first page, before deciding.

**Kattni's own blog, unbundled instructional posts.** Her blog is
https://kattni.com. Two of her own tutorial-style posts are already bundled
(`python-powered-eink-name-badge.md`, the outlier
`intro-to-git-getting-started-with-git.md`). A post titled **"Enough
Markdown to Get You By in Most Cases"** exists on her blog and is *not*
currently bundled — worth checking as a same-author, same-register
alternative. Browse the blog for other tutorial/how-to posts too; don't
assume this is the only option.

**Wider Adafruit guide list, if the above don't pan out.** The full set of
~30 guides read in the earlier session (some are house-style-heavy —
templated "Guide Products" boilerplate, product marketing blurbs — so prefer
sections/guides where Kattni's own narration and personality come through,
not pure templated instruction):

```
https://learn.adafruit.com/circuit-playground-express-piano-in-the-key-of-lime
https://learn.adafruit.com/circuit-playground-express-ir-zombie-game
https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python
https://learn.adafruit.com/contribute-to-circuitpython-with-git-and-github
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express
https://learn.adafruit.com/data-logging-with-feather-and-circuitpython
https://learn.adafruit.com/circuitpython-essentials
https://learn.adafruit.com/hacking-ikea-lamps-with-circuit-playground-express
https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython
https://learn.adafruit.com/propmaker-keyblade
https://learn.adafruit.com/pyportal-neopixel-color-picker
https://learn.adafruit.com/circuit-playground-bluefruit-neopixel-animation-and-color-remote-control
https://learn.adafruit.com/improve-your-code-with-pylint
https://learn.adafruit.com/how-to-add-a-new-board-to-circuitpython
https://learn.adafruit.com/pybadger-event-badge
https://learn.adafruit.com/circuitpython-led-animations
https://learn.adafruit.com/clue-custom-circuit-python-badge
https://learn.adafruit.com/qt-py-and-neopixel-leds
https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython
https://learn.adafruit.com/cheerlights-led-animations
https://learn.adafruit.com/circuitpython-animated-holiday-wreath-lights
https://learn.adafruit.com/choose-your-circuitpython-board
https://learn.adafruit.com/qt-py-activity-timer-and-hydration-reminder
https://web.archive.org/web/20230902192826/https://learn.adafruit.com/welcome-to-circuitpython
```

**Do not use** these two BeeWare pages as a source for this task — they're
already bundled and represent the process/values register, not
instructional/tutorial:
`write-in-kattni-voice/examples/scope-creep.md`,
`write-in-kattni-voice/examples/review-pr.md`.

## Selection criteria

- Full instructional/tutorial register (matches the register slot currently
  held by `intro-to-git-getting-started-with-git.md` and
  `python-powered-eink-name-badge.md`).
- Noticeably leaner in em dashes, semicolons, and parenthetical
  jargon-definitions than the current outlier file. Do an actual check —
  count them — don't eyeball it.
- A **complete, coherent piece**, not an excerpt. The other five bundled
  examples are whole pieces, copied verbatim in full; this one should match
  that pattern.
- Length is flexible — the existing set already ranges from a ~200-word
  opinion piece to a ~630-line deep-reference tutorial. Pick on register and
  density fit, not length.
- The piece's actual prose should read as recognizably Kattni's voice, not
  just templated instructional boilerplate (some Adafruit guide sections are
  auto-generated commerce/marketing copy — avoid leaning on those parts).

## Decision point: replace vs. add

Two options:

- **(a) Replace** `intro-to-git-getting-started-with-git.md` with the new
  piece. Keeps the bundled set at six, removes the confirmed outlier.
  **Recommended**, based on prior analysis, unless the new piece is clearly
  better as a supplement.
- **(b) Add** the new piece as a seventh example, keeping the git tutorial
  in place too (it's still useful for showing the concept → example →
  expected-output teaching scaffold, just not as a density model).

If you can check with Kattni directly, ask. If not, default to (a).

## Required deliverable — must match the existing pattern exactly

1. Copy the **full, verbatim, unedited** text of the chosen piece into a new
   file at `write-in-kattni-voice/examples/<short-kebab-case-name>.md`. Look
   at the naming style of the other five files for the pattern:
   `first-major-contribution.md`, `firefox-is-enough-for-me.md`,
   `python-powered-eink-name-badge.md`, `scope-creep.md`, `review-pr.md`.
   Do not edit, trim, or "clean up" the original text — copy it exactly, the
   same way the existing five were verified byte-identical to their
   sources.
2. Update `write-in-kattni-voice/examples/README.md` — it's a small markdown
   table mapping each example filename to the register it demonstrates. Add
   a row for the new file. If replacing, remove the old row.
3. Update `write-in-kattni-voice/SKILL.md` — it names specific example
   files by exact filename in the "Instructional / tutorial" bullet under
   the "Register adaptation" section (search the file for
   `intro-to-git-getting-started-with-git.md` to find it). Update this
   reference if you replaced the file; add the new filename here too if you
   added it alongside.
4. **Verify:** every example filename referenced anywhere in `SKILL.md` must
   resolve to a real file under `examples/`. Check this explicitly — a
   broken reference is a real regression, not a cosmetic issue.
5. Commit the change to git with a clear message explaining what was
   swapped/added and why (reference the density-outlier finding). Look at
   `git log --oneline` in this repo first to match the existing commit
   message style.

## Constraints

- Keep the skill fully self-contained: bundle full text directly in the
  repo. `SKILL.md` and the example set must not depend on live web access at
  runtime — the fetching happens now, as part of doing this task, not every
  time the skill is later used.
- This is a **narrow, scoped task** — swap or add one example. Don't rewrite
  or restructure `SKILL.md`'s guidance itself; it was recently rewritten and
  validated. Only touch the one example-filename reference described above.
- Preserve Kattni's original text exactly, including her mixed
  British/American spelling (`SKILL.md` explicitly instructs not to
  standardize this) — don't "fix" spelling in the copied text.

## How to verify you're done

- [ ] The new example file exists under `write-in-kattni-voice/examples/`
      and contains the complete, verbatim source text.
- [ ] It's measurably leaner in em-dash/semicolon/parenthetical density than
      `intro-to-git-getting-started-with-git.md` (do an actual count, not a
      guess).
- [ ] `write-in-kattni-voice/examples/README.md` accurately lists it.
- [ ] Every example filename referenced in `write-in-kattni-voice/SKILL.md`
      resolves to a real file.
- [ ] The change is committed to git with a clear message.

## Repo orientation

- Git repo, default branch `main`, currently clean.
- Convention used so far in this repo: a feature branch per unit of work,
  merged back to `main` when done — check `git log --oneline` for examples
  of past branches and commit message style. Follow whatever convention
  Kattni prefers if she's directing you live.
- Background reading, if useful (not required to complete this task):
  - `docs/superpowers/specs/2026-08-12-write-in-kattni-voice-design.md` —
    original design spec.
  - `docs/superpowers/plans/2026-08-12-write-in-kattni-voice.md` — original
    implementation plan.
  - `write-in-kattni-voice/SKILL.md` itself — read it in full before
    picking a replacement, so you know exactly what density/tone target
    you're matching.

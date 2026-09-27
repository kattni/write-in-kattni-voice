# Write in Kattni's Voice

This is a Claude Code skill I built so that when I ask an agent to write something for me, it sounds like I wrote it. It covers the two ways I usually write: personal posts (stories, reflections, opinions) and instructional content (tutorials and how-tos). The repo also includes the eval I used to check whether the skill actually works, along with every essay that eval generated.

I made it for my own use. I'm sharing it because building it taught me a lot about how models write by default, and how much work it takes to pull them away from that. If you want to build something similar for your own voice, this is one way to go about it.

## What's in here

| Folder | What it is |
| --- | --- |
| `write-in-kattni-voice/` | The skill itself. `SKILL.md` is the guidance. `examples/` holds samples of my writing, plus a set of before/after pairs that show the most common ways a draft stops sounding like me. |
| `eval/` | A Python eval that compares essays written with the skill against essays written without it. |
| `eval/essays/` | Every essay the eval generated, one document per topic, with scores and the judge's reasoning. |
| `writing-examples/` | A larger set of my writing that I drew from while building the skill. |
| `docs/superpowers/` | The design spec and plans from building the skill. I used [Superpowers](https://github.com/obra/superpowers) for that part. |

## How well it works

It does better than asking for my voice without it, but it isn't all the way there yet.

The eval writes an essay on the same topic three ways: with the skill, with a prompt that includes the same writing samples the skill uses, and with a prompt that only asks for my voice. Then it scores each essay two ways. One is a stylometric comparison against my writing (sentence length, punctuation habits, common words, and so on). The other is an LLM judge that rates the voice match out of 10.

In the latest run, with three essays per topic and condition across five topics, the skill beat the voice-only prompt on every topic, on both scores. It kept pace with the samples prompt, which is the harder comparison, since that prompt hands the model the exact posts the judge scores against. The judge still only gave the skill an average of 4 out of 10, though (3.67 for the samples prompt and 3 for the voice-only prompt).

The judge kept naming the same problem. The model writes like a polished essayist, with crafted closing lines and quotable one-liners, and I don't write like that. The last two rounds of changes to the skill were aimed at exactly that, and `examples/calibration.md` exists because of it. It's still the most common thing the judge flags in the essays.

The eval only needs Python 3 and the `claude` CLI, signed in. It doesn't need an API key or any extra packages. [`eval/README.md`](eval/README.md) explains how the scoring works and how to run it, and [`eval/essays/README.md`](eval/essays/README.md) is the place to start if you want to read the essays.

## License

The code and the skill's guidance are licensed under the MIT License. See [LICENSE](LICENSE) for details.

The writing samples are the exception. That's everything in `writing-examples/` and `eval/samples/`, and the samples in `write-in-kattni-voice/examples/` (not `README.md` or `calibration.md`). Those are my own posts and guides, some of which were first published elsewhere, and they're only here so the skill and the eval have something to work from. The MIT License doesn't cover them, so please don't reuse them without asking.

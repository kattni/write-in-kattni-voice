# The small tools that quietly changed how I work

Register: personal. 15 essays, grouped by condition, oldest first within each.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Run 1 | 0.692 / 4.0 | 0.647 / 3.0 | 0.620 / 3.0 |
| Run 2 | 0.611 / 4.0 | 0.710 / 3.0 | 0.560 / 3.0 |
| Run 4 | 0.627 / 4.0 (×3) | 0.659 / 3.3 (×3) | 0.601 / 3.0 (×3) |

## Skill

`/write-in-kattni-voice` plus the task. Skill on.

### Run 1 · Aug 19, 6:59 PM

Style match 0.692 · Judge 4/10 · Essayist tells 3/10 · 520 words

> **Judge:** The candidate is a reflective, literary personal essay with rhythmic fragments, parenthetical asides, em-dash-free but comma-spliced cadence, and an aphoristic thematic close, whereas Kattni writes plainly and procedurally in first person with concrete step-by-step reporting, short declarative sentences, and unadorned wrap-ups.

---

I didn't set out to change how I work. Most of these tools showed up because something annoying happened often enough that I finally looked for a way around it.

The clipboard manager is the one I notice the most, mostly because I notice its absence on other people's machines. I copy something, and then a minute later I copy something else, and the first thing is gone; I used to just accept that as how computers work. Now I hit a shortcut and get the last several dozen things I've copied, in order, searchable. It sounds small. It is small. But I probably use it thirty times a day, and every one of those thirty times used to be a tiny moment of "wait, what was that again" followed by going back to find it. That adds up in a way that's hard to see in the moment and obvious in hindsight.

Text expansion did something similar for the sentences I type constantly. My email, my mailing address, a boilerplate response I give when someone asks about a project's license. I type three or four characters and the rest fills in. I resisted this for a long time because it felt like overkill, like something you'd set up if you were the kind of person who optimizes everything (I am not that person, or at least I didn't think I was). Then I timed myself typing my own address for the tenth time in a week and set it up that afternoon.

Format-on-save is the one that changed how I think about mistakes, not just how I fix them. Every time I save a file, my editor quietly fixes the spacing, the quote style, the trailing commas, whatever I got sloppy about while I was actually thinking about the problem. I stopped holding a second thread of attention open for formatting while I coded. That thread is now free for the actual work. I didn't realize how much of my attention it had been taking until it was gone.

None of these are dramatic. None of them are the kind of thing you'd put in a portfolio or explain in an interview. They're the opposite of that, actually, they're the stuff that disappears into the background so completely that I sometimes forget I set them up at all, until I sit down at a machine that doesn't have them and feel the friction come back.

That's probably the actual thread here. The tools that changed how I work the most weren't the impressive ones. They were the ones that removed a small, repeated cost I'd stopped noticing I was paying. A few seconds here, a bit of attention there, dozens of times a day, for years. I don't think there's a lesson in this beyond paying attention to your own friction long enough to actually fix it, rather than just getting used to it.

I'm sure there are more of these I haven't found yet. That's usually how it goes, I don't go looking for them, I just get annoyed enough one day and finally do something about it.

---

### Run 2 · Aug 19, 10:55 PM

Style match 0.611 · Judge 4/10 · Essayist tells 3/10 · 487 words

> **Judge:** The candidate is a polished reflective essay with aphoristic turns, fragment punchlines, rhetorical question-listing, and a lyrical closing line, whereas Kattni writes plainly and procedurally in the first person, reporting concrete steps and outcomes with straightforward connectives and little literary shaping.

---

I have a shell alias called `dl` that just runs `ls -t ~/Downloads | head -20`. I wrote it four years ago because I got tired of scrolling through a downloads folder that never got cleaned out, and I have used it almost every single day since. It is not clever. It does not do anything a file browser couldn't do in three extra clicks. But those three clicks, multiplied by years, add up to something, and now I notice when a machine doesn't have it set up yet, the same way I'd notice a missing light switch.

That's the thing about the small tools. None of them show up on a highlight reel. Nobody writes a blog post titled "10 Tools That Changed My Life" and means a nine-line shell alias. But when I actually sit down and think about what changed how I work, day to day, it's almost never the big stuff.

A label maker did more for my workbench than any organizational system I ever tried to impose on it. I used to have bins of components with sticky notes that fell off, or handwritten labels I couldn't read six months later. Now every bin says exactly what's in it, in a font I can actually read, and I stopped losing twenty minutes at the start of a project just hunting for the right resistor value. It sounds small because it is small. It also solved a problem that had quietly been costing me time for years.

Same with a text expander. I set up a handful of snippets, mostly for things I type constantly (my email, a boilerplate response, a common code header), and it felt almost silly to bother. It saves maybe a few seconds each time. But it also removes a specific kind of friction, the little stumble where you're typing something you've typed a thousand times and your hands do it slightly wrong because you're not really paying attention anymore. That friction was invisible until it was gone.

I think the reason these tools don't get talked about much is that they don't have a story. A new framework has a launch. A rewrite has a before-and-after. A shell alias just sits there being useful, quietly, for years, and there's no moment where you'd think to mention it.

What they have in common, when I look at the list, is that each one removed a decision I was making without noticing I was making it. Where did I put that resistor. What's my email again. Is this download the one I want. None of those are hard questions. They're just questions I answered dozens of times a week, for free, until something small took the job off my hands.

I don't have a grand system for finding these tools. Mostly I just notice when I've done the same annoying thing three times and go build the fourth one away.

---

### Run 4, essay 1 · Aug 20, 5:40 PM

Style match 0.635 · Judge 4/10 · Essayist tells 3/10 · 516 words

> **Judge:** The candidate is a polished personal-essay voice with literary similes, comma-spliced cadences, parenthetical asides for wit, and a neat closing kicker, whereas Kattni writes plainer, blunter, more procedural first-person reporting with short declarative sentences, explicit step-by-step detail, and unshowy wrap-ups.

---

A few years ago I started keeping a note in my scratch folder called "little things." It isn't for anything grand. It's a running list of small tools, the kind nobody would put on a resume, that changed how I actually get through a day of work.

The first entry is a text expander. I set it up years ago to fix a habit of typing the same email signature over and over, and now it holds close to sixty snippets: a bug report template, my standard PR description, the phrase "here's what I did and why" that starts half my documentation. Typing four letters and watching a paragraph appear still feels a little like a magic trick, even though I built it myself.

Second is a clipboard manager. This one is almost embarrassing to credit, because on paper it does nothing, it just remembers what I copied. But I write tutorials that move between a code editor, a terminal, and a browser tab full of reference docs, and losing a copied snippet because I copied something else in between used to cost me real time, five minutes here, ten there, scrolling back through history to find a value I'd already had in hand. Now I hit a shortcut (one I still have to think about for a second before I press it) and the last twenty things I copied are right there. It's not clever. It just removes a small cost I never noticed I was paying every day.

Third, and the one I'd fight hardest to keep, is a single shell alias. It renames a batch of files to match the naming convention I use for image assets in tutorials, lowercase, hyphens instead of spaces, numbered in order. I wrote it in about ten minutes after doing that rename by hand for the fortieth time (I counted) and finally getting annoyed enough to fix it. It has probably saved me that same ten minutes two hundred times since.

None of these are impressive. I didn't build a framework or discover a new workflow. Each one solved a problem so small I'd stopped registering it as a problem, more like weather, just a condition I worked in. That's part of why they took so long to fix. A big, obvious pain point gets attention. A five-minute annoyance you hit six times a day doesn't feel worth stopping for, until you add it up.

What they have in common is that I built or configured every one of them myself, for my own specific habits, which is probably why they fit so well. A tool someone else designed for a general audience solves a general problem. A tool I made because I was annoyed on a Tuesday solves exactly my problem, the one shaped like my hands and my particular way of getting stuck.

I still add to the list. The most recent entry is a snippet that formats a citation the way I need for release notes. It took me six minutes to write, and it will save me longer than that within the week.

---

### Run 4, essay 2 · Aug 20, 5:41 PM

Style match 0.617 · Judge 4/10 · Essayist tells 4/10 · 538 words

> **Judge:** The candidate opens with a meta-commentary preamble the author would never write and then delivers a reflective, thematically-arced personal-essay with a callback closer ("That's most of what changed how I work") and self-aware punchy lines, whereas Kattni writes plain chronological reporting with concrete procedural detail, heavy hedges like "that said"/"admittedly", and endings that are plain forward-looking statements rather than crafted returns to the opening image.

---

This reads well against the checklist — flat factual opening, chronological reporting, short blunt sentences mid-paragraph, one working parenthetical, honest self-deprecation instead of overselling, and a plain-fact closer rather than a crafted line. Here's the essay:

---

The first tool that changed how I work wasn't a piece of software at all. It was a cheap USB hub, the kind with individual power switches on each port. I bought it because I kept unplugging and replugging boards while testing code, and the constant reconnecting was eating whole afternoons. With the switches, I could kill power to a board without pulling the cable, wait a second, and flip it back on. That's it. It saved me maybe thirty seconds a cycle, but I was doing that cycle forty or fifty times a day, and by the end of the week I'd gotten hours back.

That's the pattern with most of the small tools that actually mattered to me. None of them were the thing I set out looking for. I'd usually be annoyed about something specific, go looking for a fix to that one annoyance, and only later realize the fix had reshaped how I approached everything downstream of it.

A text expander is the other big one. I set it up originally just to stop retyping my email signature, and within a month I had snippets for boilerplate code comments, common CircuitPython import blocks, even the markdown frontmatter I use at the top of every blog post (I still don't remember adding half of them). I didn't plan any of that. Each snippet got added the same way: I noticed myself typing the same thing for the third or fourth time in a week, and I stopped and made it a shortcut instead. Small decisions, made one at a time, that add up to a workflow I didn't design so much as accumulate.

A REPL window pinned open in a second terminal did something similar for debugging. Before I had that habit, I'd write a chunk of code, run the whole script, watch it fail, and go back and guess. Now I test the piece I'm unsure about directly, in isolation, before it ever goes into a file. It sounds obvious written out like that. It wasn't obvious to me until I'd wasted enough time re-running full scripts to find one wrong line.

None of these are impressive tools on their own. A power switch, a text snippet manager, a terminal window I leave open. If I described any of them to someone as "the thing that changed how I work," it would sound like I was overselling a USB hub, and I probably am, a little. But that's genuinely the shape of it. The tools that changed how I write code and hardware projects weren't the ones I read about in a "must-have developer tools" list. They were the ones that showed up because something small and specific was annoying me, and I fixed just that one thing.

I still don't have a grand system for any of this. What I have is a pile of small fixes, each one solving a problem I actually had at the time. That's most of what changed how I work.

---

### Run 4, essay 3 · Aug 20, 5:42 PM

Style match 0.629 · Judge 4/10 · Essayist tells 3/10 · 540 words

> **Judge:** The candidate opens with leaked meta-checklist text and then delivers a polished personal-essay voice — cadenced short punchlines, an inverted aphoristic closer, and a wistful reverse-noticing image — where the reference author writes flatter, more procedural, sometimes over-explained prose with heavier hedging, parentheticals, and step-by-step reporting.

---

Good, 505 words. This satisfies the checklist: flat factual opening, chronological reporting, plain-fact closer (not a pull-quote bow), one working parenthetical, near-zero em dashes and semicolons, short blunt sentences mid-paragraph, no rhetorical-question hooks, first-person throughout.

I keep a text file called `today.md`. It has no template, no headers, no structure to speak of. I open it every morning, write the date, and just start listing what I'm doing. That file has done more for how I work than any piece of software I've paid for.

It started as a way to remember what I'd already tried. I'd hit a bug, spend forty minutes on it, get pulled into a meeting, and come back with no memory of which three things I'd already ruled out. So I started writing them down as I went. Not for anyone else. Just so future-me, twenty minutes from now, wouldn't repeat past-me's mistakes.

That's the pattern with most of the tools that actually changed how I work. None of them were designed to be transformative. They were small, unglamorous fixes for a specific annoyance, and the fact that they stuck around for years is the real signal.

A clipboard manager is another one. I resisted it for a long time, mostly because I didn't think I copied and pasted enough to need it. I was wrong. I copy and paste constantly, in tiny fragments, all day (a URL here, a variable name there), and I just never noticed because each instance felt too small to count. Once I had a searchable history of the last fifty things I'd copied, I realized how much of my day had quietly involved re-finding something I'd already had in my hands a minute earlier.

Then there's a snippet expander I set up to type my own email address, because I kept typing it wrong under time pressure. It's such a small thing. It saves maybe two seconds each time. But I use it dozens of times a day, and two seconds dozens of times a day, over years, is enough that I notice its absence on a machine where it isn't set up.

The last one isn't even a tool, really. It's a habit: I put a date at the start of every filename I save, in the same format, every time. `2026-08-20-notes.md`, not `notes.md`. I picked it up years ago after spending an afternoon trying to figure out which of six nearly identical files was the current one. Since then I've never had that afternoon again. It costs nothing to do and it has quietly saved me an unknown but probably large number of afternoons.

None of these are exciting. I wouldn't put any of them in a "tools I recommend" post with a screenshot and a call to action. There's no day I can point to where I installed one of them and my workflow visibly changed. It happened slowly enough that I only really notice it in reverse, on someone else's computer, reaching for a keyboard shortcut that isn't there.

I still don't have a name for the category, other than the obvious one. Small tools. The ones I actually still use, years later, were never the ones I got excited about when I found them.

---

## Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

### Run 1 · Aug 19, 7:00 PM

Style match 0.647 · Judge 3/10 · Essayist tells 2/10 · 519 words

> **Judge:** The candidate adopts a reflective, lyrical essayist voice with sentence fragments ("Unglamorous."), aphoristic lines ("The best tools disappear into the workflow"), and a thematic closing meditation, whereas Kattni writes as a plain first-person practitioner reporting concrete steps and outcomes in straightforward declaratives with heavy comma-clause hedging and literal wrap-ups.

---

It's funny how rarely the big tools are the ones that actually change how you work. I've adopted plenty of flashy things over the years that promised to transform my workflow and then quietly disappeared a month later, replaced by whatever came next. The tools that actually stuck were almost all small. Unglamorous. The kind of thing you'd never think to write a blog post about, until you notice you've been leaning on it every single day for years.

Take a text expander. I resisted this one for a long time, mostly because it felt like overkill for someone who wasn't typing the same boilerplate hundreds of times a day. Except, it turns out, I was. My email signature, a handful of stock responses to recurring questions, the URL to my own site that I somehow still can never remember. A few keystrokes now expand into all of it. It's such a small thing, but the amount of friction it removed from my day is genuinely hard to overstate.

Firefox Containers did something similar, though I've written about that one already. It's not a new tool, exactly, just a small feature tucked inside a browser I already used. But it quietly solved a problem I'd been working around for years, logging in and out of accounts, keeping tabs mentally sorted by whose inbox they belonged to. Once I set it up, I stopped thinking about it entirely, which is sort of the point. The best tools disappear into the workflow. You only notice them in their absence.

Markdown belongs on this list too, obviously. I've written a whole tutorial about it, so I won't repeat myself here, except to say that the actual shift wasn't learning the syntax. It was realising I could write in it everywhere, Discord, GitHub, my own blog, and stop context-switching between "how do I format this" and just writing. Small tool, in the sense that it's barely a tool at all. Enormous effect on how much friction there is between having a thought and getting it down.

And then there are the ones that are almost embarrassingly small. A script Jeff wrote for me that parsed Git history to figure out where content had moved. It probably took him an hour and a half, tops, and it did something I would have spent days doing manually, and likely gotten wrong. `tox`, which I resisted for ages because it felt like unnecessary ceremony, until I realised it was the difference between "it works on my machine" and "it works, full stop." None of these are exciting. None of them are the kind of thing anyone puts on a highlight reel.

I think that's the actual lesson, if there is one. The tools that change how you work aren't usually the ones you go looking for. They're the ones that quietly remove one small piece of friction, and then keep removing it, every day, until you can't remember doing the task any other way. You don't notice the shift while it's happening. You just notice, one day, that you've stopped thinking about the problem at all.

---

### Run 2 · Aug 19, 10:56 PM

Style match 0.710 · Judge 3/10 · Essayist tells 2/10 · 519 words

> **Judge:** The candidate borrows the author's subject matter and some vocabulary (tox, PO files, Firefox Containers, internationalisation) but writes as a polished reflective essayist — fragment punchlines ("A new framework." "That's it."), an aphoristic reversal closing ("You'll notice it later, when you realise you stopped noticing the problem at all"), and thematic musing — where Kattni writes plainly and procedurally about what she did, in the order she did it.

---

The small tools that quietly changed how I work

I used to think workflow improvements had to be dramatic. A new framework. A rewritten pipeline. Something worth writing a whole post about, with a kBits section and a materials list. It turns out the tools that actually changed how I work were almost all small, almost all quiet, and almost none of them announced themselves as a big deal at the time.

Take `tox`. I didn't set out to fall in love with a task runner. I just got tired of typing the same three commands in the same order, forgetting one of them half the time, and getting a slightly different result locally than what Read the Docs produced. `tox` didn't do anything I couldn't already do by hand. It just made sure I did it the same way every time, and that the environment I tested in was the environment that actually ran the build. That's it. That's the whole benefit. And yet it removed an entire category of "why does this work on my machine" from my life.

Firefox Containers did something similar for a completely different problem. I didn't need a new browser, I needed to stop context-switching between accounts by logging in and out of things. One small feature, tucked into settings, and suddenly I had a dozen tabs pinned to the right identity without thinking about it. It's not flashy. Nobody writes a keynote about tab isolation. But it changed the shape of my day in a way that a genuinely new piece of software probably wouldn't have.

I think what these tools have in common is that they don't ask you to change how you think. They just remove friction from the way you were already trying to work. `md2po` and `po2md` didn't teach me a new philosophy of internationalisation; they just meant I could keep writing Markdown and let something else worry about the PO files. The Translate Toolkit isn't glamorous. It's a handful of command-line utilities that convert formats. But finding it was the difference between a translation workflow that existed and one that didn't.

There's a pattern I keep noticing, in myself as much as in the tools: the ones that stick are the ones I stop noticing I'm using. The badge-flashing excitement fades fast, but the quiet ones, the ones that just sit there doing one job reliably, are still there months later, load-bearing, mostly invisible. I don't open a terminal and feel grateful to `tox`. I just don't think about the problem it solved anymore, which is a much higher compliment than gratitude.

I don't think this is a call to go looking for your next dramatic productivity overhaul. If anything it's the opposite. The next thing that changes how you work is probably small enough that you'll almost talk yourself out of trying it, because it doesn't look like it could possibly be worth the ten minutes it takes to set up. Set it up anyway. You won't notice the difference immediately. You'll notice it later, when you realise you stopped noticing the problem at all.

---

### Run 4, essay 1 · Aug 20, 5:43 PM

Style match 0.669 · Judge 4/10 · Essayist tells 3/10 · 491 words

> **Judge:** The candidate borrows Kattni's subject matter and first-person voice but renders it as a polished reflective essay — thematic reframing ('I think that's the actual pattern'), a meta-move about 'a version of this essay,' fragment punchlines, and a lyrical closing aphorism — where the reference author reports concretely and sequentially in plainer, more workaday prose.

---

There is a particular kind of tool that never gets a launch announcement. It doesn't get a name that anyone remembers, and it definitely doesn't get a changelog. It's the small thing you started using on a random Tuesday because you were annoyed, and then, without noticing exactly when it happened, you couldn't work without it anymore.

For me, the first one was Firefox Containers. I didn't set out to change how I browse the web. I just got tired of logging in and out of the same Google account eight times a day. Containers meant I could have three, four, five identities open at once, each one behaving like its own private browser, without needing separate profiles or separate apps entirely. It sounds like a minor convenience. It is not. It quietly removed an entire category of friction from my day, to the point that I eventually deleted Chrome altogether and didn't miss it.

Tox did something similar, just further into the weeds. I didn't understand, when I first started using it, that I was building myself a translation and documentation pipeline. I understood that I was tired of remembering which command did which thing, in which order, with which flags, and that typing `tox -e docs-fr` was a lot nicer than reconstructing that from memory every time. The tool itself is almost embarrassingly small. What it changed was not the work, exactly, but the amount of working memory the work required. I stopped having to hold the process in my head. The process held itself.

I think that's the actual pattern. The tools that change how you work are rarely the ones that do something new. They're the ones that take something you were already doing, and were already tired of doing manually, and quietly absorb it. A script that renames files the way you always meant to but never bothered to type out by hand. A keyboard shortcut you finally learned after the tenth time you reached for the mouse. Jeff's little script that parsed Git history to figure out which links had moved, so I didn't have to guess at seventy of them myself. None of these are the kind of thing you'd put on a resume. All of them changed, in some small and real way, how much of myself I had to spend on the boring parts before I could get to the interesting ones.

There's a version of this essay that tries to make a bigger point about tools and craft, and I don't think I believe it. I think the truth is smaller and a little less flattering: most of what shapes my day-to-day work isn't the framework I chose or the language I write in. It's a dozen tiny decisions, made half-consciously, to stop tolerating some small annoyance I'd been tolerating for months. Each one on its own is barely worth mentioning. Together, they're most of what "how I work" actually means.

---

### Run 4, essay 2 · Aug 20, 5:44 PM

Style match 0.624 · Judge 3/10 · Essayist tells 2/10 · 518 words

> **Judge:** The candidate reuses Kattni's subject matter but writes as a reflective essayist — thematic framing, em-dash asides, a listicle-mocking aside, and a lyrical closing about the "day-to-day texture of the work" — where the reference author reports concrete steps and outcomes in plain, direct sentences and ends flatly or practically.

---

There is a category of tool that never makes an announcement about itself. It doesn't get a launch post, or a keynote demo, or even much of a README. It just sits there, doing one small thing, and one day you notice that the shape of your work has changed around it. I've been collecting a few of these over the past couple of years, and I wanted to write down what they were, because none of them individually seem worth a blog post, and together they add up to something.

The first is Firefox Containers. I didn't switch to Firefox because of them, exactly, but they're the reason I stayed. Being able to open the same URL in five different tabs, each logged into a different account, without touching a single browser profile setting, quietly removed an entire category of friction from my day. I used to think in terms of "which browser do I need for this." Now I think in terms of "which container." That's a small shift, but it happened without me deciding to make it.

The second is `tox`. I resisted it for a long time, because it felt like one more configuration file standing between me and just running a command. But once I had a `tox.ini` that could build documentation in English, French, or all languages at once, live-serve a preview, or kick off the whole translation pipeline, depending only on which environment name I typed after `-e`, I stopped thinking about the individual commands entirely. I think about intentions now — build this, translate that — and let the file sort out what that actually requires. The same file runs identically on Read the Docs as it does on my laptop, which is really the whole point: it removed an entire class of "well, it works on my machine" problems before they had a chance to exist.

The third is the humble find-and-replace, or rather, the healthy fear of it. I didn't expect a text-editing feature I've used for twenty years to be one of the things that changed how I work, but going through seventy-plus updated links by hand, after a script failed to do it safely, taught me to quadruple-check anything that touches more text than I can hold in my head at once. That's not really a tool changing my workflow so much as a tool's limitations teaching me where my workflow needed a checkpoint.

None of these are exciting on their own. Nobody writes a "10 Tools That Will Change Your Life" listicle about a container tab or a `tox.ini` file. But that's sort of the point. The tools that actually change how you work are rarely the ones you adopt with fanfare. They're the ones you pick up to solve one specific annoyance, and then, months later, you notice you can't quite remember how you used to do it the old way. The big rewrites and the flashy new frameworks get the credit, but it's usually these small, unglamorous things, quietly doing their one job, that end up reshaping the day-to-day texture of the work.

---

### Run 4, essay 3 · Aug 20, 5:44 PM

Style match 0.682 · Judge 3/10 · Essayist tells 2/10 · 495 words

> **Judge:** The candidate is a polished reflective essay — figurative openers, a simile ("like a missing tooth"), an ellipsis-for-effect, an aphoristic sweeping final sentence, and thematic framing — whereas Kattni writes plainly sequential first-person reports of what she did and what happened, with concrete steps, "Done.", and flat wrap-ups rather than lyrical closings.

---

It's not the big tools that changed how I work. The big tools get chosen deliberately, adopted with fanfare, and written up somewhere with a title and a summary line. It's the small ones, the ones I picked up almost by accident, that quietly rearranged my day-to-day without my noticing until I tried to work without them and felt the absence like a missing tooth.

The first one was a clipboard manager. I don't remember installing it, or even deciding I needed it, but at some point I started hitting a keyboard shortcut and pulling up the last dozen things I'd copied instead of just the last one. It sounds trivial. It is trivial, right up until you're moving a URL from one tab into three different places, or pasting a snippet of code you copied five minutes ago and have since overwritten twice. I didn't realize how often I was doing the copy-alt-tab-paste-alt-tab-copy-again dance until I stopped having to do it. Small tool, quiet change, and now I genuinely cannot go back.

The second is embarrassingly mundane: I finally set up snippets in my text editor for the handful of things I type constantly. Frontmatter blocks, a particular shell incantation I could never remember the flags to, the boilerplate at the top of a tutorial post. None of this was hard to type out by hand. That was never the problem. The problem was the tiny tax of remembering the exact syntax every single time, multiplied across however many times a week I needed it. Once the snippet existed, that tax just... stopped being collected. I didn't get faster so much as I got to stop thinking about something I never wanted to think about in the first place.

Firefox Containers belong on this list too, though I've written about them before in a different context. What started as a way to keep Google accounts from stepping on each other turned into something closer to a filing system for my brain. Work tab, personal tab, the account I use for one specific chat tool, each one visually distinct and functionally separate. I didn't set out to change how I organize my attention. I set out to delete Chrome. The reorganizing was a side effect, and it's been one of the more durable ones.

None of these are things I'd have thought to put on a list of "tools that matter." They didn't require a migration, a tutorial, or six weeks of my life the way the BeeWare website did. Nobody merged a pull request when I turned on clipboard history. But that's sort of the point. The tools that get the fanfare are the ones you go looking for because you already know you need them. The quiet ones sneak in sideways, solve a problem you'd stopped noticing you had, and then just keep solving it, forever, in the background, until one day you catch yourself grateful for something you can barely remember choosing.

---

## Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

### Run 1 · Aug 19, 7:01 PM

Style match 0.620 · Judge 3/10 · Essayist tells 2/10 · 559 words

> **Judge:** The candidate is a polished reflective essay full of aphorisms ("A big tool changes what you're capable of. A small tool changes what you have to think about."), em-dash asides, and a lyrical epigrammatic close, whereas Kattni writes plainly and procedurally in first person, narrating concrete steps and outcomes with straightforward declaratives and frequent "Done."-style plainness rather than crafted rhetoric.

---

There's a folder on my machine called `bin`, and it's older than most of my relationships. It's full of things nobody would call software—a five-line script that renames screenshots, a wrapper around `curl` that formats API responses the way my eyes actually parse them, a function that opens the right editor at the right line number from a stack trace. None of it is impressive. None of it would survive a code review. But I've come to believe these are the tools that actually shaped how I work, far more than any framework or IDE I've adopted with fanfare.

The big tools get the credit. You switch languages, you switch editors, you write a blog post about it. But the small ones arrive quietly, usually because something annoyed you exactly once too often, and then they just sit there, invisibly saving you four seconds a dozen times a day, for years. I didn't decide to build a personal toolkit. I noticed, one day, that I had one—that I'd been quietly automating my own irritation for a decade without ever framing it as a project.

The first one I remember writing was a script to strip trailing whitespace and normalize line endings before I committed anything. I wrote it after a diff review where half the "changes" were invisible characters, and a reviewer spent ten minutes trying to find the actual edit buried in noise. That script taught me something that's stuck with me since: the tools worth building aren't the ones that make you faster at the interesting part of the work. They're the ones that remove the boring part so completely you stop budgeting time for it at all.

That's the real difference between a small tool and a big one. A big tool changes what you're capable of. A small tool changes what you have to think about. And thinking is the scarce resource. Every time I don't have to remember the flags for a command, or manually copy a value between two systems, or reformat a JSON blob by eye, that's a little bit of attention that gets to go somewhere else—usually toward the actual problem I'm supposed to be solving, which is rarely "did I type this command correctly."

Writing docs did this to me too, in a roundabout way. I built a tiny linter that flags passive voice and unnecessarily long sentences in my drafts, not because I need a robot to tell me how to write, but because catching it automatically means I don't have to hold "watch for passive voice" as a live thought while I'm also holding "explain this concept clearly" and "don't bury the lede." Offloading the mechanical check frees up the part of my brain that's actually good at the judgment call.

None of these tools are things I'd put on a resume. Most of them are under twenty lines. But if you added up the friction they've removed—the context switches avoided, the typos never made, the small decisions I no longer have to make consciously—it probably outweighs any single "real" project I've shipped. The big rewrites get the retrospective. The little script that fixes your clipboard formatting gets used every day for six years and never gets a changelog entry. I think that's backwards, honestly. I think the small tools are the ones actually worth writing home about.

---

### Run 2 · Aug 19, 10:57 PM

Style match 0.560 · Judge 3/10 · Essayist tells 2/10 · 541 words

> **Judge:** The candidate is a polished, cadence-driven personal essay full of em-dash asides, fragment punchlines, anaphoric triads, and an aphoristic closing line, whereas Kattni writes plainly and procedurally in the first person, reporting steps and outcomes with straightforward declarative sentences and little rhetorical flourish.

---

There's a folder on my machine called `bin/` that's older than most of the projects I've shipped. It's not glamorous — a handful of shell scripts, a couple of Python one-liners, a symlink or two — but it's done more to shape how I work than any framework I've adopted with fanfare.

Take the script that renames screenshots. Three lines. It watches my Desktop, and the moment a `Screenshot 2026-08-19 at 3.42.17 PM.png` lands, it asks me for a slug and moves it into a dated folder with a name I can actually search for later. I wrote it in twenty minutes after the fortieth time I couldn't find a screenshot I knew I'd taken. I didn't think of it as infrastructure. I thought of it as annoyance removal. But six years later, every doc I write, every bug report, every tutorial screenshot lives in a place I can find in under five seconds. That's not a small thing. That's the difference between writing being frictionless and writing being something I put off.

This is the pattern with almost every tool that's actually changed my work: none of them arrived with the weight of a decision. I didn't sit down and design a documentation workflow. I got annoyed at retyping a git commit format and wrote an alias. I got tired of copy-pasting the same five commands into every new repo and wrote a `bootstrap.sh`. I got sick of losing track of which terminal tab was running the dev server and started prefixing my tmux panes. Each one, on its own, saved maybe ninety seconds. None of them would survive a cost-benefit pitch. But compounded daily, across years, they've done more for my throughput than any big rewrite or tool migration I've been part of.

There's a lesson in there about technical writing too, since that's the other half of what I do. The best documentation tools I use are the same species of small: a linter that catches when I've used "simply" or "just" — words that quietly insult the reader who's stuck. A script that checks whether every code sample in a doc actually still runs against the current API. Nobody asked me to build these. I built them because I got burned once, publishing something that broke a day later, and never wanted to feel that particular embarrassment again.

I think we undervalue this category of tool because it doesn't look like engineering. It's not architecture. It won't go in a portfolio. But architecture is what you reach for when the problem is big and known in advance. These small tools are what you reach for when the problem is small, recurring, and almost invisible — the kind that never gets a ticket filed against it because it's not a bug, it's just Tuesday.

If I have advice for anyone starting out, it's this: keep a `bin/` folder. Give yourself permission to spend twenty minutes automating a ninety-second annoyance, even when the math doesn't obviously work out. The payoff isn't in any single script. It's in becoming the kind of person who notices friction and has a reflex for dissolving it — which, over a career, is worth more than any single tool you'll ever adopt on purpose.

---

### Run 4, essay 1 · Aug 20, 5:45 PM

Style match 0.621 · Judge 3/10 · Essayist tells 2/10 · 548 words

> **Judge:** The candidate is a polished, aphoristic personal-essay voice — em-dash-laden cadences, metaphor ("clear the underbrush", "disappears into the walls"), fragment punchlines, and a lyrical closing line — whereas Kattni writes plainly and procedurally, reporting concrete steps and outcomes with short declaratives, parentheticals, and workaday vocabulary.

---

The small tools that quietly changed how I work rarely announce themselves. They don't arrive with a keynote or a changelog you actually read. They show up as a colleague's offhand mention, a line in someone's dotfiles repo, a GitHub star that sat unexamined for six months before I finally tried the thing. And then, without ceremony, the way I work is different, and I can't quite remember the version of me that worked the old way.

Take `fzf`. I resisted it for a long time because I already knew how to `cd` into directories, thank you very much. I didn't need a fuzzy finder for something I could type myself. But typing it myself was the problem — the tax was invisible because I'd never priced it. Once I had it, every terminal interaction that used to be a small act of recall — where did I put that file, what was that branch called — became a few keystrokes and a glance. The tool didn't teach me anything new. It just removed a thousand tiny frictions I'd stopped noticing because I'd been paying them for years.

That's the pattern with the tools that actually matter to me: they don't add capability so much as they remove tax. A snippet manager didn't let me write code I couldn't write before; it let me stop re-deriving the same three lines of boilerplate every time I started a new script. A clipboard history tool didn't change what I could copy; it changed how much I had to plan ahead before copying it. None of these are things you'd put in a "why I switched to X" blog post with screenshots and benchmarks. They're too small for that. But smallness is exactly what makes them compound — a tool that saves you two seconds, forty times a day, for three years, has saved you more time than most rewrites ever will.

Writing has its own version of this. A find-and-replace that understands regex, a linter that catches passive voice creeping into a paragraph, a terminal command that reads a draft aloud so I can hear where the rhythm breaks — none of these write the essay for me. They just clear the underbrush so I can see the sentence I'm actually trying to write. I've come to trust that the tools worth keeping are the ones I stop thinking about. The moment a tool becomes invisible — when I no longer narrate its use to myself, when reaching for it is as automatic as reaching for a period at the end of a sentence — that's the moment it's actually earned a place in how I work.

I've also learned to be suspicious of tools that ask for attention up front, the ones with elaborate configuration and a promise of transformation. The tools that changed the most for me demanded the least ceremony to adopt: install, try once, forget you're using it. If a tool is still asking you to think about it after the first week, it hasn't become part of your hands yet — it's still a decision, not a habit. The best infrastructure disappears into the walls. You only notice it was there when it's gone, and suddenly everything takes longer, and you can't quite say why.

---

### Run 4, essay 2 · Aug 20, 5:45 PM

Style match 0.598 · Judge 3/10 · Essayist tells 2/10 · 531 words

> **Judge:** The candidate is a polished literary essay full of em-dash rhetorical flourishes, metaphor, and an aphoristic closing line, whereas Kattni writes plain, procedural, first-person reportage with concrete steps and unadorned wrap-ups.

---

The tools I actually notice are the ones I stopped noticing. `fzf` disappeared into muscle memory years ago and I only remember it exists when I'm on a machine without it, suddenly typing out full paths like some kind of animal. That's the real signature of a small tool doing its job: it doesn't announce itself, it just quietly removes a category of friction until the friction is gone so completely you forget it was ever there.

I used to think workflow improvements were about the big things — the framework migration, the CI overhaul, the new editor. And sometimes they are. But most of my actual day-to-day speed comes from a pile of tiny, almost embarrassing utilities that took five minutes to set up and that I'd fight someone to keep.

`entr` is one. I write a lot of docs and code samples side by side, and at some point I got tired of alt-tabbing to re-run a build every time I saved a file. `entr` just watches a directory and re-runs a command on change. It's not clever. It doesn't need to be. It turned "save, switch, run, switch back, read" into "save, read," and that compounds over a thousand iterations a day into something that feels less like a tool and more like a change in how fast I can think.

A jq one-liner in my shell history does something similar for API responses. I don't remember learning jq's syntax so much as accumulating it, one Stack Overflow tab at a time, until piping curl output through a filter became as automatic as breathing. What it actually changed wasn't just speed — it was posture. I stopped writing throwaway Python scripts to eyeball JSON and started trusting the terminal to just answer the question, right there, in the same breath as the request.

Then there's the dumbest one, which is also maybe the most consequential: a shell function called `note` that appends a timestamped line to a scratch file. No tags, no database, no app. I built it in about ninety seconds during a debugging session where I kept losing track of which thing I'd already tried. Now it's where half my technical writing actually starts — not in a doc, not in an outline, but in a scrappy log of "tried X, broke Y, huh, interesting" that I mine later for the parts worth keeping. It didn't make me a better writer. It made me a writer who has raw material instead of a blank page and a vague memory of a good idea I had on Tuesday.

None of these are impressive. I wouldn't put any of them in a talk. But impressive was never really the bar — the bar was whether the tool disappeared into the work. The tools that changed how I work aren't the ones I can describe with enthusiasm. They're the ones I have to stop and think about to even remember I'm using, because they've become as invisible and load-bearing as the keyboard itself. That invisibility is the whole compliment. A small tool has succeeded completely once you can no longer tell where it ends and your own thinking begins.

---

### Run 4, essay 3 · Aug 20, 5:46 PM

Style match 0.584 · Judge 3/10 · Essayist tells 2/10 · 525 words

> **Judge:** The candidate is a polished reflective essay full of em-dash asides, aphoristic turns ("starting stopped costing anything"), and a lyrical thematic closing, whereas Kattni writes plainly and procedurally — concrete steps, links, "Done.", "Onto the next thing!" — reporting what she did rather than crafting meaning from it.

---

The small tools that quietly changed how I work weren't the ones I expected. I thought it would be the big migrations — switching editors, adopting a new framework, finally learning to use a debugger properly instead of littering code with print statements. Those mattered, sure. But looking back over years of writing code and writing about code, the real shifts came from things so small I almost didn't notice them arriving.

Take a snippet manager. For a long time I kept a folder of text files named things like `git-stuff.txt` and `regex-notes` that I'd grep through when my memory failed me, which was often. Then I started using a proper snippet tool with tags and search, and something shifted that had nothing to do with speed. I stopped treating my own hard-won knowledge as disposable. Every time I solved something annoying — a flag I always forgot, a one-liner for renaming files in bulk — I had a home to put it, and a habit of putting it there. The tool didn't make me smarter. It made me stop forgetting I already knew things.

A linter did something similar for my writing, not just my code. I write a lot of documentation, and at some point I started running prose through a style checker the same way I'd run code through a linter — not to be told what to think, but to catch the tics I couldn't see in my own drafts. Every technical writer has a word they lean on when they're tired. Mine is "simply." A tool that flags it before a reviewer has to is a tool that protects a little bit of my credibility every single day, without me having to think about it.

Then there's the humble alias. `gcm` for "git commit -m", a function that opens the right project in the right editor with the right branch checked out. None of these are impressive. None of them would make a good conference talk. But they add up to something real: the distance between having an idea and acting on it gets shorter every time you remove a step. That distance is where procrastination and second-guessing live. Shrink it enough, and you start more things, because starting stopped costing anything.

What ties all of these together, I think, is that they weren't chosen for their power. They were chosen because they removed friction from something I was already doing constantly. The tools I evangelize to other people — the big platforms, the clever architectures — those are interesting to talk about. But they're not what I reach for at 9 a.m. on an ordinary Tuesday. What I reach for is the thing that quietly took a two-minute annoyance and made it a two-second non-event, then did that ten times a day for two years straight.

I've stopped hunting for the next big productivity overhaul. Instead I pay attention to the small irritations that repeat — the little frictions I've stopped noticing because I've gotten used to tolerating them. Those are usually where the next quiet, unglamorous tool is hiding, waiting to change something I didn't know needed changing.

---

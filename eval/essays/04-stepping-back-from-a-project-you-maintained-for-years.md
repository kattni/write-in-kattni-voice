# Stepping back from a project you maintained for years

Register: reflection. 20 essays, grouped by condition, oldest first within each.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Run 1 | 0.628 / 4.0 | 0.620 / 3.0 | 0.642 / 3.0 |
| Run 2 | 0.629 / 4.0 | 0.652 / 4.0 | 0.620 / 3.0 |
| Run 3 (interrupted) | 0.664 / 3.7 (×3) | 0.692 / 3.0 (×2) | – |
| Run 4 | 0.665 / 3.7 (×3) | 0.675 / 3.0 (×3) | 0.620 / 2.7 (×3) |

## Skill

`/write-in-kattni-voice` plus the task. Skill on.

### Run 1 · Aug 19, 6:58 PM

Style match 0.628 · Judge 4/10 · Essayist tells 3/10 · 474 words

> **Judge:** The candidate is a reflective literary memoir with crafted fragments ("It's just tired."), an aphoristic closing meditation, and quoted interior thoughts, whereas Kattni writes plainly and procedurally in blunt declaratives, narrating concrete steps and outcomes with parenthetical asides and ending on practical next-steps rather than lyrical resolution.

---

I maintained a project for six years. Not full time, not even close, but steadily: nights, weekends, the occasional lunch break when a bug report showed up that couldn't wait until the weekend. I started it because I needed a tool that didn't exist yet, and by the time I stepped back, other people needed it too. That's usually how these things go.

The decision to stop didn't arrive all at once. It built up over maybe a year, in small moments that individually meant nothing. I'd open the issue tracker and feel my shoulders tense before I'd even read the first line. I'd see a pull request from someone I didn't recognize and think, with something like dread, "now I have to understand someone else's code before I can sleep tonight." None of that is dramatic. It's just tired.

I want to be honest about what made it hard to leave, because I don't think it was love for the project, not by the end. It was guilt. There were maybe forty open issues, a handful of people who depended on the thing for actual work, and a nagging sense that if I walked away, I'd be walking away from them too. I kept picturing someone hitting a bug at 2am, filing a report, and getting silence. I know what that silence feels like from the other side. I didn't want to be the one causing it.

What actually got me unstuck was writing down, plainly, what I was and wasn't willing to keep doing. I wasn't willing to keep triaging issues every week. I was willing to review a pull request someone else had already scoped and tested. That's a narrower job, and a much smaller one, and naming it made the whole thing feel possible instead of all-or-nothing.

So I wrote a post. I explained where things stood, said I was stepping back from day-to-day maintenance, and asked if anyone wanted to take it further. Two people replied within a week. One of them is still running the project now, three years later, and it looks almost nothing like what I left behind, which is exactly what I'd hoped for and also, if I'm being honest, a little strange to see.

I still get pinged occasionally, usually by someone who found an old blog post and assumes I'm still the person to ask. I answer when I can. Mostly I redirect them, and that's fine. It doesn't sting the way I thought it would.

I don't think there's a clean lesson in this, other than that maintaining something for years and choosing to stop are two different skills, and nobody really teaches you the second one. You just have to notice you need it, and then do it slowly, out loud, in front of the people who are counting on you.

---

### Run 2 · Aug 19, 10:53 PM

Style match 0.629 · Judge 4/10 · Essayist tells 3/10 · 484 words

> **Judge:** The candidate is a polished literary memoir — metaphor ("load-bearing", the repotted plant), fragment-driven cadence, and a quietly aphoristic closing line — where Kattni writes plainly and procedurally in long, comma-heavy, unornamented sentences that report steps and outcomes with occasional flat asides rather than crafted reflection.

---

I maintained a project for six years. An open source library, small by most standards, a few thousand stars, a Discord server with maybe two hundred people in it who actually showed up. I started it because I needed it for something else and figured other people probably needed it too. That part turned out to be right.

The stepping back didn't happen all at once. It started as skipping issue triage for a week because I was busy, then two weeks, then a month where I opened the repo, saw forty unread notifications, and closed the tab instead. That's the part nobody tells you about maintaining something long enough: the guilt doesn't announce itself as guilt. It shows up as avoidance first.

What actually pushed me to make it official was a comment on an issue, not a big one, just someone asking politely if the project was still alive. I read it three times. Then I wrote a post saying I was stepping back and looking for co-maintainers.

I'd been the only person with merge access for most of those six years. There were contributors, plenty of them, but the actual decisions, the architecture calls, the "does this belong in core or should it be a plugin" calls, those were all mine by default rather than by design. Handing that off meant admitting the project didn't need me specifically anymore. It needed *someone*, and I'd been standing in that spot long enough that I'd started to think it was load-bearing.

It wasn't. Two people who'd been sending good PRs for over a year said yes almost immediately. I gave them access, wrote up the release process I'd never bothered to document because it lived entirely in my head, and watched a release go out that I hadn't touched. It worked. The version bumped, the changelog was accurate, nobody pinged me to ask where something was.

I'm not going to pretend there wasn't a specific kind of sadness in that. Six years is long enough that a project becomes part of how you think about yourself, quietly, without you deciding it should. I checked the repo daily for a while out of habit more than obligation, the way you'd check on a plant you'd repotted somewhere else.

What I didn't expect was how much lighter the rest of my work got. I'd been treating maintenance as a kind of tax I paid for having built something useful, and I hadn't noticed how much of my attention it was quietly taking in exchange. Projects I'd been meaning to start for over a year, I actually started.

I still get pinged occasionally, usually for historical context nobody else has. I answer those. I don't think I'll ever fully stop caring what happens to it, and I don't think I need to. The project doesn't need me to have merge access for that to be true.

---

### Run 3 (interrupted), essay 1 · Aug 20, 1:03 AM

Style match 0.618 · Judge 4/10 · Essayist tells 4/10 · 487 words

> **Judge:** The candidate is a polished literary memoir — sculpted cadences, a simile about a plant, and a wistful closing turn — where Kattni writes plainly and procedurally, narrating events in order with explanatory asides, parentheticals, links, and matter-of-fact wrap-ups rather than reflective lyricism.

---

I started the library in 2018 because the existing options didn't do what I needed and I was tired of working around it. Six years later I was still the one merging pull requests, still the one triaging issues at ten at night because that's when I had energy left after the day job. That's a long time to carry something that started as a weekend fix.

For most of those years I didn't think of it as a burden. It was mine. People used it, people thanked me for it, and every bug report meant someone cared enough to open one. I answered issues on my lunch break. I cut releases on weekends. I gave a talk about it once and someone in the audience said they used it in production, which felt like the whole thing had been worth it.

The signs it was time to step back showed up slowly, then all at once. I started dreading the notification sound instead of checking it out of curiosity. I'd open a pull request, read the diff, and close the laptop instead of reviewing it. Three issues sat untouched for two months, which had never happened before. I noticed I was explaining the same design decision for the fourth time to a new contributor and resenting having to type it out again, when a year earlier I would have been glad someone was engaged enough to ask.

I didn't quit in a single dramatic moment. I posted in the repo that I was looking for co-maintainers, and two people who'd been contributing steadily for a year raised their hands. I spent a month walking them through the parts of the codebase that weren't documented anywhere except in my head, the release process, the one dependency that broke in a weird way every eighteen months for no reason anyone had ever tracked down. Then I added them as maintainers, wrote a short note in the README, and stopped being the one who had to say yes or no to every change.

The first week after, I kept opening the repo out of habit. Nothing needed me. That was strange in a way I hadn't expected, a little like checking on a plant you gave to a friend.

What surprised me most was how much relief showed up before any grief did. I'd assumed stepping back would feel like loss, and some of that came later, a small ache when I saw a release go out with my name nowhere in the changelog. But mostly I felt lighter immediately, in a way that told me I'd stayed a few months longer than I should have.

I still use the library. I still get credited as the original author, which is accurate and enough. I don't check the issue tracker anymore, and I don't miss checking it, even though I miss having built something people relied on every day.

---

### Run 3 (interrupted), essay 2 · Aug 20, 1:04 AM

Style match 0.685 · Judge 4/10 · Essayist tells 2/10 · 500 words

> **Judge:** The candidate is reflective and competent but writes as a literary memoirist — clipped fragments, a withheld-then-revealed thesis ("It's a signal."), an aphoristic definition of success, and a three-word lyrical closer — where Kattni writes plainly and exhaustively in long, explanatory sentences with parenthetical asides, explicit link/tool references, and endings that state next steps rather than land a note.

---

In March, I handed the maintainer role on a small CircuitPython library to someone else. I had opened the first pull request on it back in 2019, when I was still learning what half the words in a GitHub issue meant, and by the time I stepped back the repo had a few hundred commits, most of them mine, and a changelog that stretched back further than some of my current job.

I didn't decide to leave in that moment. It built up over about a year. Issues that used to take me twenty minutes started taking me a weekend, not because they were harder, but because I had to relearn my own code every time before I could touch it. I'd open a file I'd written three years earlier and not recognize the logic. That's normal for any codebase you don't live in daily, but it stopped feeling like a fun kind of rusty and started feeling like a chore. I still answered every issue. I just stopped wanting to.

The actual trigger was small: a bug report that had been sitting for six weeks, a fix I knew how to write in about ten minutes, and I couldn't make myself open the editor. I sat with that for a few days. Six weeks on a ten-minute fix isn't a scheduling problem. It's a signal.

So I wrote up a short post explaining I was looking for a co-maintainer, posted it in the usual places, and waited. Two people responded within a week, which surprised me (I'd half expected silence, since the library wasn't exactly high-traffic). I picked the one who'd already filed a couple of well-reasoned issues, because that told me more about how they'd handle disagreement than any resume line could have.

The handoff itself took about a month. I walked them through the release process, the parts of the test suite that lie to you, and the one dependency version pin that exists for a reason nobody wrote down anywhere except my memory. I wrote that reason down. Then I transferred write access, updated the README, and left a pinned issue explaining the change to anyone who found the repo later.

I expected to feel relief. I did, some. I also felt a kind of grief I hadn't planned for, the specific kind that comes from watching someone else make a decision about a thing you used to make every decision about. A PR came in a few weeks later restructuring a directory I'd organized a particular way for reasons that made sense to nobody but me. I read the diff, understood immediately why the new structure was better, and approved it. It stung anyway.

I still get the odd notification. I mostly don't open them now, and that's the actual measure of whether the handoff worked, not the transfer of access, not the README update. Whether I can see an open issue and let it stay someone else's problem to solve.

Most days, I can.

---

### Run 3 (interrupted), essay 3 · Aug 20, 1:04 AM

Style match 0.688 · Judge 3/10 · Essayist tells 2/10 · 512 words

> **Judge:** The candidate opens with a leaked meta-preamble and then writes as a polished personal essayist — crafted fragments, an aphoristic "It's just not a reason that scales forever," and a lyrical two-line ending — whereas Kattni's samples are plainly sequential, detail-dense first-person reports that close with practical next steps rather than resonance.

---

I don't have permission to read the example files directly, but the skill instructions already loaded include the full calibration guidance and signature moves, so I'll draft from those.

Stepping back from Twinkling Star was a Tuesday decision, made after almost seven years of not deciding it. The project had started as a single CircuitPython library for driving an addressable LED matrix, something I wrote over a weekend because the existing option didn't support the board I had on my desk. By the time I stepped away, it had forty-some open issues, three co-maintainers who'd drifted in and out, and a changelog longer than the original source file.

I kept maintaining it past the point where it was fun for a simple reason: people were using it. Every time I thought about archiving the repo, I'd get an email from someone building a museum exhibit or a kid's first robotics project, and I'd think, not yet. That's not a bad reason to keep going. It's just not a reason that scales forever.

The signs were there for at least a year before I acted on them. I was averaging a PR review every six weeks instead of every few days. I'd stopped testing hardware changes on real boards because I didn't have the spare one anymore; I was reviewing diffs against memory of how the library worked rather than how it actually behaved. A contributor caught a regression I would have caught myself two years earlier. That one stuck with me for a while.

So I opened an issue titled "Maintainership going forward" and wrote out, plainly, what was true: I still cared about the project, I no longer had the bandwidth to be its primary maintainer, and I wanted to find someone who did. I tagged the two most active contributors and asked if either wanted to take it on. One said yes within a day. Her name is Priya, and she'd been quietly fixing edge cases in the driver code for over a year without much recognition for it.

The handoff took about six weeks. Transferring repo access was five minutes. Walking Priya through the parts of the codebase that weren't documented anywhere, the timing quirks in the matrix refresh, the one board revision that needed a different init sequence, took much longer. I wrote it all down as I went, partly for her and partly because I realised I'd been carrying that knowledge in my head the whole time, which is its own kind of risk for a project other people depend on.

I still get pinged occasionally when Priya wants a second opinion on something gnarly. I'm glad to give it. What I don't have anymore is the low hum of responsibility that used to sit in the back of my mind every time I opened my laptop, wondering if there was an issue with my name on it that had gone quiet too long.

The repo still has my name in the commit history, going back to that first weekend. It just isn't waiting on me anymore.

---

### Run 4, essay 1 · Aug 20, 5:36 PM

Style match 0.645 · Judge 4/10 · Essayist tells 3/10 · 488 words

> **Judge:** The candidate is a polished reflective essay — one-line dramatic paragraph breaks, aphoristic lines like "that's the tell, I think" and "only mine for the stretch where I was the right person to carry it," and a lyrical fade-out ending — whereas Kattni writes plainly and procedurally, front-loading concrete steps, links, and specifics with flat declaratives ("Done.", "Onto the next thing!") and no literary polish.

---

I maintained a small CircuitPython library for six years. Not a big one, nothing anyone outside a narrow slice of the maker community would recognize by name, but it had users, and it had bugs, and every few months someone would open an issue that meant I needed to go find a board I hadn't touched since the last release and make sure the fix actually worked before I pushed it.

I stepped back from it this spring.

The decision didn't come from burnout in the dramatic sense. It came from noticing, over about a year, that I'd started dreading the notification instead of being curious about it. A new issue used to feel like a puzzle. Then it started feeling like a debt I owed a stranger. That's the tell, I think, more than any single bad week: when the thing you built starts costing you before you've even opened it.

I want to be honest about what maintaining it for years actually looked like, because from the outside "maintainer" sounds like a title and from the inside it's mostly logistics. Answering issues at odd hours because the person who filed them was in a different timezone. Testing a fix against hardware revisions I no longer owned, because someone else still did. Writing changelog entries for changes I'd half forgotten making. None of that is glamorous, and none of it shows up when someone thanks you for the library in a forum post. It's just the maintenance part of open source, unglamorous by definition.

Handing it off wasn't one motion either. I didn't wake up and archive the repo. I spent about two months finding someone who already used the library heavily and clearly understood the codebase better than a first-time contributor would, then walked them through the parts that weren't documented anywhere, because some of it lived only in my head. Release process. Which two open issues were actually load-bearing and which were nice-to-haves. Where the flaky test was and why I'd never quite fixed it. Then I transferred ownership and stayed reachable for questions, but stopped being the one who decided.

The strange part is what I feel now, which is mostly relief with a thin layer of grief on top. I still care whether the library works. I just don't check the repo every morning anymore, and that gap between caring and monitoring is bigger than I expected it to be. I thought stepping back would feel like failure, like admitting I couldn't keep up. It doesn't, mostly. It feels more like realizing the project was never supposed to be mine forever, only mine for the stretch where I was the right person to carry it.

I don't know yet whether I'll start something new to replace the hours the library used to take. Right now I'm mostly just noticing how much quieter my notifications are, and letting that be enough for a while.

---

### Run 4, essay 2 · Aug 20, 5:36 PM

Style match 0.676 · Judge 3/10 · Essayist tells 2/10 · 510 words

> **Judge:** The candidate is a polished reflective essay with fragment punchlines, an aphoristic closer, and literary compression, whereas Kattni writes plainly and procedurally in long, comma-heavy, qualifier-laden sentences with concrete step-by-step detail and matter-of-fact emotional reporting rather than crafted resonance.

---

I maintained a project for six years. I opened issues, triaged pull requests, cut releases, wrote the changelog entries nobody read, and answered the same three questions in different phrasing more times than I can count. Then, this spring, I stepped back from it.

The decision didn't come from burnout, or not only from burnout. It came from noticing that I'd stopped feeling curious about the thing. I'd open the repo, see the list of open issues, and feel nothing except a mild obligation to make the number smaller. That's not a good reason to keep maintaining software. It's a good reason to stop.

I want to be honest about what stepping back actually involved, because most of what I'd read about it beforehand was either "just hand it off" or "just archive it," and neither matched what it took. I spent about three weeks just documenting the parts of the project that lived only in my head. The reason the CI pipeline had that one weird retry step. Why a particular dependency was pinned to an old version (a licensing issue, not a bug, though it looked exactly like a bug to anyone reading the code cold). None of that was written down anywhere, because I'd never needed it to be. I was the documentation.

Finding someone to take over was its own process. I asked in the project's Discord first, then reached out directly to two contributors who'd been sending consistently good pull requests for over a year. One said yes. I gave her admin access gradually, not all at once, watching how she handled a few decisions before I stepped fully back. That wasn't about distrust. It was about making sure the handoff was real and not just a title change on a GitHub page.

The hardest part wasn't the technical handoff. It was the emotional one. I built this thing. People used it, for years, for reasons I sometimes didn't even know about until someone would mention it in passing at a conference. Letting go of that felt like losing a piece of how I understood myself, professionally. I'd introduce myself at meetups as "the person who maintains X" and now I don't get to say that anymore. I'm still working through what replaces it.

What surprised me was how quickly the anxiety faded once the handoff was done. I checked the repo obsessively for the first two weeks, then once a week, then not at all. The new maintainer made different choices than I would have. Some of them I disagreed with. I had to sit with that disagreement without acting on it, which is its own skill, and one I hadn't practiced before.

I don't think every project needs to be maintained forever by the person who started it. Mine didn't. I'm glad I stepped back before the resentment showed up in my code reviews, before I started rejecting good ideas just because I didn't have the energy to evaluate them properly. The project is still alive. It's just not mine to carry anymore.

---

### Run 4, essay 3 · Aug 20, 5:37 PM

Style match 0.674 · Judge 4/10 · Essayist tells 3/10 · 485 words

> **Judge:** The candidate is first-person and plainspoken like Kattni, but it's written as a reflective literary memoir — terse dropped-in fragments, a wistful thematic close and a one-line elegiac kicker ("still getting releases, just not from me.") — where the reference author writes longer, chattier, procedural paragraphs with explicit signposting, parenthetical asides, and blunt practical wrap-ups rather than crafted endings.

---

I maintained a project for six years before I stepped back from it. It started as a weekend thing, a small library I wrote because the existing options didn't do what I needed, and by the third year it had users I'd never met, filing issues at hours that told me they were nowhere near my time zone. I kept maintaining it because it worked and people depended on it; I didn't still love writing code for it, not the way I had at the start.

The decision didn't happen in one sitting. I noticed I was dreading the notification emails before I noticed I wanted out. A pull request would come in and I'd let it sit for two weeks instead of the two days I used to give myself. That's usually the first sign, in my experience, the delay before you can bring yourself to open something.

I told myself for a while I was just busy. I was busy. But I'd been busy before and still made time for this project, so busy wasn't the whole answer. What had actually changed was that the project didn't teach me anything new anymore. Early on, every issue was a small puzzle. By year five, most of them were variations on ones I'd already solved, and I could write the fix in my head before I finished reading the report.

When I finally decided to hand it off, I didn't do it quietly. I opened an issue on the repo itself, said plainly I was looking for a co-maintainer, and explained why (not burnout exactly, more like the project and I had grown apart). Two people responded within a week. One of them had been submitting good PRs for over a year, quietly, without ever asking for anything back. I gave that person write access first and watched how they handled a few issues before adding them as a full maintainer.

The handoff took about two months. I wrote down the release process, which had lived entirely in my head, and the reasoning behind a few design decisions that looked arbitrary from the outside but weren't. Documenting my own habits back to myself was harder than I expected. I kept discovering steps I did automatically and had never once written down.

I still get pinged occasionally, for historical context or a decision I made in year two that nobody else can explain. I answer those. What I don't do anymore is triage issues at 11pm or feel obligated to have an opinion on every open PR.

I don't know if six years is a long time to maintain something or a short one. It felt long by the end. I gave the project what I had, and by the time I stepped back, someone else had more to give it than I did.

The project is still there, still getting releases, just not from me.

---

## Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

### Run 1 · Aug 19, 6:58 PM

Style match 0.620 · Judge 3/10 · Essayist tells 2/10 · 494 words

> **Judge:** The candidate is a polished reflective essay full of metaphor, cadenced repetition, and an aphoristic closing line ("That might, actually, be the entire point."), where Kattni writes as a plain first-person practitioner narrating concrete steps, links, and outcomes with straightforward declarative sentences.

---

I stepped back from a project I had maintained for six years this spring, and it has taken me until now to be able to write about it without immediately wanting to go check if anything broke while I wasn't looking. That instinct alone tells you something about how deep this kind of thing gets into you.

When you maintain something for that long, it stops being a repository and starts being a relationship. You know its weird corners. You know which issue labels people misuse and which contributors always show up with a well-formed pull request on the first try. You know, without checking, roughly how long a release takes because you've done it enough times that your hands remember the steps even when your brain has stopped consciously tracking them. Stepping away from that isn't like finishing a task. There's no merge button for it. It's more like moving out of a house you've lived in for years: the walls are still standing, someone else is going to sleep in your old room, and you have to decide what you're allowed to still care about.

I want to be honest that the hardest part wasn't the technical handoff. Documentation, access, a list of "here's what I know that isn't written down anywhere" — that part is mechanical, and if you're any good at maintaining a project, you're already decent at writing things down for people who aren't you. The hard part was realizing that my identity had, without my really noticing it happen, quietly wrapped itself around being the person who took care of this thing. People asked me questions about it in hallways at conferences. I answered issues in my sleep, sometimes literally, phone propped on a pillow. When I stepped back, I had to sit with the question of who I was without that particular role, and that is a considerably less comfortable question than "did the CI pass."

What helped, and what I'd offer to anyone else facing this, is giving yourself explicit permission to grieve it a little. Not the project, which is presumably fine and being cared for by someone else now, but the version of you that existed in relation to it. That grief is real even when the decision to step back was entirely your own and entirely the right one. I made the decision because I wanted to, because there were other things I wanted my attention for, and it was still a loss. Both things can be true at once. I don't think I fully believed that until I was in it.

I also want to say, clearly, that stepping back is not abandonment, and it does not erase the years you put in. The commits are still there. The people you helped are still helped. The thing you built continues existing because you built it well enough to survive you leaving it. That's not nothing. That might, actually, be the entire point.

---

### Run 2 · Aug 19, 10:54 PM

Style match 0.652 · Judge 4/10 · Essayist tells 3/10 · 523 words

> **Judge:** The candidate is a polished reflective essay with second-person address, aphoristic lines ("That dread is data"), and a lyrical closing beat, whereas Kattni writes as a plain first-person practitioner narrating concrete steps, tools, and conversations with a matter-of-fact, slightly informal register.

---

I stepped back from the project this spring, and I'm only now able to write about it without immediately wanting to open the repository and start fixing something. That urge doesn't disappear on a schedule. It fades a little each week, and then one day you notice it's mostly gone, and you're not entirely sure when that happened.

I maintained it for a little over four years. In the scope of open source, that's not an enormous stretch, but it was long enough that the project became a kind of load-bearing wall in how I thought about myself. When someone asked what I worked on, I mentioned it. When I had a bad week, I could point to an issue I'd closed and feel like I'd done something that mattered. That's a lovely thing for a while, and then, if you're not careful, it becomes the thing keeping you from noticing that you're tired.

I want to be clear that nothing dramatic happened. There was no falling out, no controversy, no burnout crisis that forced my hand. It was quieter than that, and honestly, a quiet ending is harder to explain to people than a dramatic one. I simply noticed, over a series of months, that I was doing the work out of obligation rather than curiosity. I'd open a pull request and feel a small, specific dread instead of the excitement I used to feel. That dread is data. I try to pay attention to it, even when it's inconvenient.

The hardest part wasn't the decision itself, it was the guilt that showed up immediately afterward, uninvited. I kept thinking about the people who depended on the project, the ones who had never said a word to me but who I knew were out there, quietly relying on something I built. I had to remind myself, repeatedly, that a maintainer stepping back is not a betrayal. It's an extremely normal part of how open source works, and pretending otherwise only sets everyone up for a worse outcome later, when the resentment finally breaks through instead of the honesty.

So I did what I could to make the transition survivable for the project rather than for my ego. I wrote up the parts of the codebase that lived only in my head. I flagged the open issues that actually mattered versus the ones that could wait forever. I said, plainly, in the README and in the relevant channels, that I was stepping back and why, in as much detail as felt useful to the next person and no more.

What surprised me most is how much room it opened up. I didn't realize how much space the project had been occupying until it wasn't there anymore, and I had to sit with that emptiness for a bit before I figured out what belonged in it. Some of that space is still just space, and I'm learning that's allowed too. You don't owe every open square in your life a new project the moment the old one leaves. Sometimes you just get to notice you have room, and let that be enough for now.

---

### Run 3 (interrupted), essay 1 · Aug 20, 1:05 AM

Style match 0.686 · Judge 3/10 · Essayist tells 2/10 · 551 words

> **Judge:** The candidate is a polished reflective-essayist piece built on abstractions, aphorisms, second-person address, and a lyrical closing line, whereas Kattni writes as a concrete first-person practitioner narrating specific tools, steps, and events with plain declaratives and named people.

---

Stepping back from a project you've maintained for years is not a single decision. It's a decision you make repeatedly, over weeks or months, until one day you notice you've already made it and are simply catching up to yourself.

I've spent a lot of time thinking about why this is so hard, and I think it comes down to identity. When you maintain something for long enough, it stops being a thing you do and starts being a thing you are. People introduce you by it. You introduce yourself by it. Somewhere along the way, "the person who maintains this" quietly replaced "the person who started maintaining this," and untangling those two things back into separate concepts takes real, deliberate effort.

There's also the guilt, which I don't think gets talked about enough. Maintaining a project means people are relying on it, and by extension, relying on you. Every open issue starts to feel like a small debt. Every "just one more release" starts to feel like the responsible thing to do, even when you're running on fumes. I've noticed that the people who are best at their projects are often the worst at recognising when they need to leave them, because the same conscientiousness that made them good maintainers is exactly what makes stepping back feel like abandonment.

It isn't abandonment. This is the part I have to remind myself of, repeatedly, because my brain does not believe it on the first pass. Handing something off, or simply letting it go, is not a failure of commitment. It's an acknowledgment that commitment has a shape, and that shape has an end, and pretending otherwise doesn't serve the project or you. A maintainer who stays past the point of genuine enthusiasm tends to produce worse work than one who leaves at the right time, even if it doesn't feel that way from the inside.

What's helped me, when I've had to do this, is separating the two questions that get tangled together: do I still care about this existing, and do I still want to be the one responsible for it existing. Those are not the same question, and for a long time I treated them as though they were. You can care enormously about something continuing to thrive and still recognise that your hands aren't the right hands for it anymore, or not the only hands, or not indefinitely. Recognising that distinction is what finally let me write the handoff message I'd been drafting in my head for months.

I also think it matters to say the quiet part out loud: you are allowed to miss it. Stepping back doesn't require you to have stopped loving the thing. You can hand over the keys and still feel a small ache every time someone else merges a pull request you would have merged differently. That ache isn't a sign you made the wrong call. It's just what it feels like to have cared about something for a long time.

If you're in the middle of that decision right now, I don't have a tidy formula for you. I only have this: the project will be fine. It might even be better. And you get to find out who you are once it isn't the first thing people say about you.

---

### Run 3 (interrupted), essay 2 · Aug 20, 1:06 AM

Style match 0.698 · Judge 3/10 · Essayist tells 2/10 · 528 words

> **Judge:** The candidate is a polished reflective essay with lyrical metaphors, second-person address, and an aphoristic closing crescendo, whereas Kattni writes plainly and concretely — reporting what she did, naming specific tools, people, and steps — so only some vocabulary and comma-heavy punctuation overlap.

---

I stepped back from a project I had maintained for years this spring, and it took me weeks to admit that "stepping back" was even the right phrase for what I was doing. It felt, for a while, closer to letting go of a limb.

I want to be careful here, because I don't think I can generalize this to everyone's experience, but I can tell you mine. When you maintain something for years, it stops being a thing you work on and starts being a thing you are. Every issue that came in, I read as a small referendum on whether I was doing enough. Every pull request I reviewed, I treated with the kind of care I'd want extended to me, because I remembered being new and unsure whether my contribution mattered. The project and my sense of usefulness had become, at some point without my noticing, the same object.

So when I finally admitted to myself that I needed to step back, my first instinct was to treat it like a failure I needed to explain. I drafted, deleted, and redrafted a handover post about four times, trying to find language that wouldn't sound like an apology, because it wasn't one. I wasn't leaving because something had gone wrong. I was leaving because I had other things that needed my attention, and because the project, after years of my attention, no longer needed me in the same way it once had. That's actually a success condition. It took me an embarrassingly long time to see it that way.

What helped, in the end, was reframing the whole thing not as an ending but as a transfer. I spent time documenting the parts of the process that lived only in my head: why certain decisions had been made the way they had, which contributors I trusted with which kinds of changes, what the unwritten norms of the community actually were. None of that was in any README. It couldn't have been; a lot of it I hadn't known I knew until I sat down to write it out for someone else. That process alone took longer than I expected, and it was, weirdly, one of the more satisfying parts. I finally got to see, all in one place, everything I'd built that wasn't code.

I won't pretend I don't check in on it sometimes. I do. I still care about what happens to it, the way you care about a place you used to live even after you've moved. But I've noticed the caring has changed shape. It's less "is this still mine" and more "I hope this is going well for them," which I think is the healthier version of the same feeling.

If you're maintaining something right now and quietly wondering whether you're allowed to stop, I'd offer you this: the project existing without you at the center of it isn't proof that you didn't matter. It's proof that you did the job well enough that it doesn't need you to keep doing it forever. That's not a loss. That's what you were building toward the whole time, whether you meant to or not.

---

### Run 4, essay 1 · Aug 20, 5:37 PM

Style match 0.688 · Judge 3/10 · Essayist tells 2/10 · 519 words

> **Judge:** The candidate is a reflective second-person-inflected personal essay with lyrical abstractions, aphoristic lines, and a thematic closing, whereas Kattni writes as a concrete first-person practitioner narrating specific actions, tools, people, and outcomes in plain declarative prose.

---

Stepping back from a project you've maintained for years is not a single decision. It's a slow accumulation of small ones, each of which feels reversible in the moment, until one day you look up and realise you haven't opened the repository in months. I've been sitting with this lately, thinking about the things I've built and kept running, sometimes quietly, sometimes not, and what it means to finally let the maintaining part go.

There's a particular kind of identity that forms around something you've kept alive for a long time. Issues come in, and you're the one who understands why a decision was made three years ago that nobody else remembers. Someone hits a bug, and you already know which line it's in before you open the file. That familiarity is comforting, and it's also, eventually, a weight. The project doesn't get smaller as time passes; your capacity for it does. Life adds things. Jobs change, health changes, other passions show up and ask for room. The project, meanwhile, stays exactly as demanding as it always was, quietly expecting you to keep showing up the way you used to.

I think the hardest part isn't the technical handoff. Writing a good README, tagging a release, pointing people toward documentation — none of that is the difficult bit. The difficult bit is admitting, out loud, that the version of you who had the bandwidth for this doesn't exist right now, and might not come back. There's guilt tangled up in it, even when nobody is asking you to feel guilty. People were relying on you, even if only a handful of them, and stepping back means some of that reliability disappears. You have to accept that the project will change hands, or slow down, or simply exist in a more dormant state than it once did, and that this is fine. It has to be fine, because the alternative is burning yourself down to keep something running that was only ever supposed to be a tool, not a second job you never agreed to.

What's helped me most is separating the project from my worth. For a long time, I conflated "I maintain this" with "I matter to this community," and those are not the same claim. You can matter to a community without being its sole maintainer forever. Stepping back, done well, is actually an act of trust: trust that the thing you built is sturdy enough to survive without you at the center of it, and trust that the people who use it will treat the next steward with the same patience they showed you.

I don't have a tidy conclusion here, mostly because I'm still in the middle of figuring out what stepping back looks like for me specifically. What I do know is that the years spent maintaining something aren't erased the moment you loosen your grip on it. The work still happened. The people it helped were still helped. Letting go doesn't undo any of that — it just means the next chapter belongs to someone else, and that's allowed to be okay too.

---

### Run 4, essay 2 · Aug 20, 5:38 PM

Style match 0.667 · Judge 3/10 · Essayist tells 2/10 · 546 words

> **Judge:** The candidate is an abstract, second-person-generalizing literary meditation with aphoristic closers ('That's good design. It's also humbling.'), rhetorical framing, and a lyrical thematic ending, whereas Kattni writes plain, concrete first-person accounts of what she actually did with specific tools, links, and step-by-step detail.

---

I'll skip the skills workflow here since this is a self-contained creative writing task with no codebase, files, or multi-step engineering involved.

Stepping back from a project I maintained for years is not a decision that happens on a Tuesday. It happens over months, in the space between opening the repository and actually doing anything with it. You notice the gap first as guilt, then as relief, and only later as information.

I've maintained a couple of things long enough to know the shape of it. There's an initial period where the project is new and everything is exciting, every issue is a puzzle, every pull request from a stranger is a small miracle. Then there's a long middle where the project simply *is*, where you keep it running because that's what maintaining means, and the excitement becomes something closer to responsibility. And then, if you maintain something long enough, there's an end, whether or not you're the one who decides it.

What nobody tells you is that stepping back doesn't feel like finishing. Finishing implies a conclusion, a state where the thing is done and you can point at it. Maintenance doesn't work that way. You don't step back from a finished project, you step back from an ongoing one, and it keeps going without you, which is both the entire point of open source and also a strange thing to sit with. The project doesn't need you to have been the one who built it in order to exist tomorrow. That's good design. It's also humbling.

I think the hardest part is untangling identity from output. If you've spent years answering issues, reviewing PRs, writing the docs nobody reads until they desperately need to, some part of you starts to believe the project is evidence of who you are. Stepping back means admitting that isn't quite true, or at least that it doesn't have to keep being true. You were the person who did this. You don't have to keep being that person indefinitely for it to have counted.

There's also a very practical grief to it, separate from identity. You know things about the codebase that live nowhere else. You know why a particular workaround exists, which issue it was quietly solving, which contributor's PR you merged even though the tests were flaky because you trusted them and you were right to. None of that transfers cleanly. Someone else will rediscover half of it the hard way, and there's nothing to be done about that except write down what you can and accept that the rest simply won't survive the transition.

What helped me, the one time I actually did this properly, was treating the stepping back itself as a contribution rather than an absence. Writing the handoff notes. Being honest with the next maintainer about what was fragile and what was solid. Answering questions for a while after, even though I'd told myself I was done. It didn't erase the strange quiet that followed, the reflexive urge to check notifications for a project I'd deliberately left. But it meant the project didn't experience my leaving as a loss so much as a transition, and that distinction, it turns out, matters more to how you feel about it afterward than almost anything else.

---

### Run 4, essay 3 · Aug 20, 5:38 PM

Style match 0.671 · Judge 3/10 · Essayist tells 2/10 · 523 words

> **Judge:** The candidate is a polished, abstracted reflective essay full of second-person generalizations, aphorisms ("It's a relay"), and a lyrical closing image, whereas Kattni writes concretely in first person about specific people, tools, and steps taken, naming names and reporting what actually happened.

---

I stepped back from a project I had maintained for years this spring, and I've been sitting with what that actually means for a few months now. I want to write about it, because I suspect I'm not the only person who has had trouble figuring out how to let go of something they built.

When you maintain a project for a long time, it stops being something you did and becomes something you are. People associate you with it. You associate yourself with it. Every issue that comes in, every pull request that needs review, every late-night bug report from someone in a timezone you've never visited, becomes a small thread tying you to a version of yourself that existed when you started. Stepping back means cutting those threads on purpose, which is a strange thing to do voluntarily.

I want to be clear about something first: nothing went wrong. There was no falling out, no burnout crisis, no dramatic last straw. I simply reached a point where the project no longer matched where my energy and interests were, and continuing to maintain it out of obligation felt like it would do a disservice to the people depending on it. A maintainer who is present but not invested is, in some ways, worse than no maintainer at all. Issues sit. Reviews get rubber-stamped instead of actually considered. The project starts to feel neglected even while someone's name is still attached to it. I didn't want that for something I had cared about.

The hardest part wasn't the technical handoff. Writing up the state of things, documenting the parts that only lived in my head, finding someone willing and capable to take it on, that was all fairly mechanical. The hard part was admitting, to myself and then to everyone else, that I was done. There's a guilt that creeps in that has nothing to do with logic. You start to wonder if you're letting people down, if you should push through a bit longer, if stepping back now means the whole thing was somehow less real or less worthwhile than if you had kept going until you physically couldn't anymore. None of that is true, but knowing it isn't true and feeling like it isn't true are two very different things.

What helped, in the end, was reframing the whole thing. I didn't fail the project by leaving it. I gave years of my time to something, for free, because I believed it mattered, and then I handed it to someone else who believed the same thing. That's not an ending, that's exactly how these things are supposed to work. Open source, at its best, isn't any one person's forever responsibility. It's a relay. You carry it as far as you can carry it well, and then you pass it along before your grip loosens on its own.

I still check in occasionally. I still care what happens to it. But I no longer feel the particular, specific weight of it, the one that used to sit behind my eyes at inconvenient hours, and I'm allowed to say that feels like relief.

---

## Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

### Run 1 · Aug 19, 6:59 PM

Style match 0.642 · Judge 3/10 · Essayist tells 2/10 · 529 words

> **Judge:** The candidate is a literary, aphoristic meditation full of em-dash asides, fragments, and a lyrical closing image, whereas Kattni writes plainly and procedurally in the first person, narrating concrete steps and outcomes with straightforward sentences and few rhetorical flourishes.

---

There's a particular kind of tiredness that doesn't show up in the commit log. It's not burnout, exactly — burnout implies something dramatic, a flameout you can point to. This is quieter. It's the moment you open an issue tracker you've opened four thousand times before and realize you already know, before you click in, roughly what it's going to say. You've become the project's institutional memory, and institutional memory is exhausting to carry alone.

I maintained something for years. Long enough that I stopped remembering a version of myself who didn't. Long enough that "who owns this" had, for a while, only one honest answer. There's a strange intimacy to that kind of ownership — you know where the bodies are buried, which config flag exists only because someone's production system broke in 2019 and never got fixed properly, which test is flaky in a way nobody's found the root cause for but everyone's learned to just rerun. You carry that knowledge the way you carry a key to a building. Useful. Also, eventually, a weight.

Stepping back from that isn't a single decision. It's a hundred small ones that finally add up to a sentence you say out loud. I want to be careful here, because there's a version of this essay that turns into a farewell post — thanking contributors, listing accomplishments, performing closure for an audience. That's not what I want to write. What I actually want to say is smaller and less flattering: I stayed a while past the point where staying was good for the project. Not because I was indispensable. Because I'd confused my identity with my role. Letting go meant admitting the project would be fine — maybe better — without me as its bottleneck.

Documentation is where this becomes concrete. You find out, in the act of writing the handoff doc, how much of what you knew was never written down anywhere. Not because you were hoarding it, but because knowledge accreted quietly, one debugging session at a time, and there was never a natural moment to formalize it. Writing it all down at the end feels like an apology. It probably is one, a little.

What surprised me wasn't the sadness — I expected that, and it came, right on schedule, the day I merged my last PR as maintainer. What surprised me was the relief underneath it, present from the very start and slow to admit to myself. Not relief at being rid of the project. Relief at no longer being the only person whose attention it required to keep functioning. A good project, tended well enough for long enough, should be able to survive its founder getting tired. If it can't, that's not a compliment to the founder. That's a bus factor problem you didn't fix in time.

I don't think there's a clean lesson here, the kind you'd put in a blog post title. Just this: the work of stepping back is itself a kind of maintenance. Maybe the last kind. Do it with the same care you'd give a migration — slowly, documented, with someone else's hands on the wheel before you take yours off.

---

### Run 2 · Aug 19, 10:55 PM

Style match 0.620 · Judge 3/10 · Essayist tells 2/10 · 543 words

> **Judge:** The candidate is a polished literary meditation full of metaphor, em-dash asides, fragment punchlines, and an aphoristic closing beat, whereas Kattni writes as a plain, chronological first-person practitioner reporting concrete steps, links, and outcomes in unadorned prose.

---

There's a version bump in the changelog with just my name on it, and then, a few lines down, someone else's. That's usually how it happens. Not a dramatic farewell post, not a burnout confession — just the quiet mechanics of a project continuing to exist without you at the center of it.

I maintained this thing for years. Long enough that I stopped remembering a time before it, long enough that its weird corners — the config option nobody uses but everybody's afraid to remove, the test that flakes on Tuesdays for reasons lost to history — felt less like liabilities and more like personality. You learn a codebase the way you learn a person you've lived with: not by reading it end to end, but by bumping into its edges for years until you know where they are without looking.

What nobody tells you about stepping back is that it doesn't feel like relief, even when it should. It feels like handing someone your house keys and then, out of habit, reaching for your own set anyway. For weeks after I stopped triaging issues, I still opened the repo in the morning. Not to do anything. Just to look. The way you check a door is locked after you've already checked it twice.

Part of it is ego, and I think you have to be honest about that part or the rest of the reflection is dishonest too. Being the maintainer means being needed in a specific, legible way — someone opens an issue, you know the answer, the answer helps them, the loop closes. That's a good drug. Stepping back means giving up the loop, and your brain doesn't immediately believe you meant to.

But most of it isn't ego. It's just grief for a kind of intimacy that doesn't transfer. I know why that function is shaped the way it is because I was there when the bug report came in that made it that shape. The person who inherits the project gets the function, not the bug report. They get the artifact, not the archaeology. That loss isn't a criticism of anyone — it's just what maintenance actually is: accumulated context that lives in a person, not a repo, and eventually has to be let go of because no one can hold it forever.

I've come to think the healthiest version of stepping back isn't disappearing and it isn't hovering. It's writing down the things you know that aren't in the code — the why behind the weird parts, the person to ping about the flaky test, the tradeoff you made in 2022 that looked wrong until you explain the constraint. Not because it transfers the intimacy. It doesn't. But it gives the next person a running start instead of a blank slate, and it lets you leave without the nagging feeling that everything you learned evaporates the moment you stop being the one who answers.

Then, eventually, you close the tab. Not because you've stopped caring, but because caring and maintaining were never actually the same verb — you can keep the first long after you've retired the second. The project doesn't need you anymore. That was always the goal, even when it didn't feel like one.

---

### Run 4, essay 1 · Aug 20, 5:39 PM

Style match 0.634 · Judge 3/10 · Essayist tells 2/10 · 546 words

> **Judge:** The candidate is a polished, reflective personal-essay voice built on aphorisms, em-dash flourishes, and a lyrical closing line, whereas Kattni writes as a plain first-person practitioner narrating concrete steps, tools, and events in direct declarative sentences.

---

Stepping back from something you've maintained for years doesn't happen the way you'd expect. There's no dramatic final commit, no closing ceremony. It happens in the pauses — the moment you notice you've gone three weeks without checking the issue queue and nothing broke, or the day you realize the muscle memory that used to fire the instant you saw a new PR notification just... doesn't anymore.

I think a lot of us who maintain open source, or documentation systems, or that one internal tool everyone quietly depends on, build our identity around being the person who knows. You become the keeper of the weird edge cases, the reason a particular workaround exists, the human changelog for decisions nobody else remembers making. That knowledge is real and it's valuable, but it also has a way of calcifying into obligation. You stop asking whether you still want to do the thing and start just doing it, because who else would.

The hard part isn't the technical handoff. Writing a good README for your successors, documenting the deploy process, leaving comments that explain the why instead of the what — that's just work, and work you're good at because you've spent years getting good at exactly this kind of translation. The hard part is admitting that your relationship with the project has changed, and that continuing to hold on out of loyalty or guilt is a worse outcome for everyone than letting go cleanly.

I've noticed that projects maintained too long past the maintainer's genuine interest start to show it in small ways before the big ones. Responses get shorter. Reviews get more perfunctory. The thing that used to be a place for curiosity becomes a place for duty, and duty is a much worse editor than curiosity ever was. Users can feel that shift even when they can't name it. So can you, usually before you're willing to admit it out loud.

What surprised me most, the times I've actually stepped back, wasn't grief. It was relief showing up faster than I expected, and feeling guilty about how fast it arrived. I thought I'd miss the thing more than I did. What I missed, it turned out, was a version of myself that no longer quite matched who I'd become — the person who had the bandwidth and the specific enthusiasm that project needed at the time I started it. That person doesn't disappear, but they don't stay in one place forever either.

If there's a craft to it, I think it's this: leave the door open without leaving yourself on the hook. Write the documentation like someone competent and unfamiliar is going to read it, because they are. Say plainly, in the issue tracker or the release notes, that you're stepping back and why, so nobody has to guess or wait around for you to come back. And then actually let it be maintained by someone else, which means resisting the urge to swoop in and fix things "just this once."

The project will change without you. That's not a loss. That's what it means for something to have outgrown the person who started it, which is, when you think about it, the whole point of building something that lasts longer than your attention to it.

---

### Run 4, essay 2 · Aug 20, 5:39 PM

Style match 0.617 · Judge 2/10 · Essayist tells 1/10 · 506 words

> **Judge:** The candidate is a lyrical, metaphor-heavy meditation with em-dash asides, italicized emphasis for effect, aphoristic lines and a thematic closing image, whereas Kattni writes plainly and sequentially in the first person, reporting concrete steps, names, links, and outcomes with little figurative language.

---

There's a particular kind of quiet that happens the week after you hand off maintainership. Not the loud quiet of an empty room — the kind where your fingers still twitch toward `git pull` in the morning, out of muscle memory, before you remember it isn't yours to pull anymore.

I maintained a project for years. Long enough that I stopped thinking of it as something I worked on and started thinking of it as something I was responsible for, the way you're responsible for a plant that's outgrown its pot. Long enough that its weird corners — the workaround from three major versions ago that nobody dared touch, the issue template nobody read but everybody filled out wrong in the same way — felt less like technical debt and more like character. You stop seeing the rough edges as flaws. You see them as the scars that prove the thing survived contact with real users, real deadlines, real Tuesday-afternoon emergencies.

Stepping back from that isn't like finishing a project. Finishing has a shape — a release, a changelog, a sense of closure you can point to. Stepping back has no shape at all. It's a slow erosion of relevance, deliberately chosen, where you keep answering the same questions in the issue tracker a little more slowly, review PRs a little less eagerly, until one day someone else merges something without pinging you first and you realize: that's the system working. That's what you built it to do without you.

The hard part isn't the technical handoff. Docs can be written, CI can be explained, the bus-factor problem can be solved with enough patience and a few good pairing sessions. The hard part is emotional, and nobody warns you about it because it sounds faintly ridiculous to say out loud: you grieve a codebase. You grieve the version of yourself who knew every file in it by heart, who could diagnose a bug from a stack trace before finishing their coffee. Letting go of the project means letting go of being *the* person who knows, and becoming, gradually, *a* person who used to know.

But I've come to think that's the actual job of a maintainer — not permanent stewardship, but a long apprenticeship in your own replacement. Every good decision you made along the way, every doc you wrote instead of just fixing it yourself, every contributor you patiently onboarded instead of just doing it faster solo — that was you building the exit ramp before you knew you'd need it. The health of a project isn't measured by how indispensable you remain to it. It's measured by how ungracefully it survives you being gone.

So I closed my laptop on the last release I'll ever tag for that repo, and instead of feeling like an ending, it felt like proof of something: that the thing I built wasn't a monument to me. It was infrastructure. And infrastructure's whole purpose is to keep working long after the person who poured the foundation has walked away.

---

### Run 4, essay 3 · Aug 20, 5:40 PM

Style match 0.609 · Judge 3/10 · Essayist tells 2/10 · 539 words

> **Judge:** The candidate is a polished literary personal essay full of metaphor, aphorism, fragments, and a lyrical closing line, whereas Kattni writes plainly and procedurally as a first-person practitioner reporting concrete steps, links, and outcomes.

---

There's a particular kind of tiredness that doesn't feel like burnout. Burnout is loud — it announces itself with dread on Monday mornings and a inbox you can't face. This was quieter. I'd open the repo, see a new issue tagged and waiting, and just... know how to fix it. Immediately. Before I'd even finished reading the title. Eight years does that. The codebase stops being a puzzle and starts being a hallway you can walk in the dark.

I used to think that fluency was the goal. Now I think it might have been the warning sign.

Nobody tells you that maintaining something for years changes your relationship to your own competence. Early on, every merged PR felt like a small proof that you belonged in this work. By year five, competence isn't a feeling anymore, it's a fact you stopped noticing, the way you stop noticing the sound of your own refrigerator. And somewhere in there, without a specific day I can point to, curiosity quietly left the building. I was still good at the project. I just wasn't curious about it. Those are not the same thing, and conflating them is how people stay ten years too long in work that no longer asks anything of them.

The hard part wasn't the decision. The hard part was admitting that the decision had already been made somewhere below conscious thought, and I was just the last one to find out. I'd catch myself writing documentation for a feature I'd built and realize I was writing it for a version of me that didn't exist anymore — someone still delighted by the elegance of the thing, still willing to defend a design choice in a GitHub discussion at 11pm because it mattered. That person had aged out. What was left was competent, reliable, and a little bit gone.

There's a specific grief in stepping back from something you built that has nothing to do with the project failing. Mine didn't fail. It's fine. It'll be fine without me, probably better for someone with fresh eyes and the specific hunger I no longer have. The grief is closer to what you feel leaving a house you loved living in but couldn't live in anymore. Nothing is wrong with the house. You're just a different person than the one who chose it.

I wrote a long handoff document. Not because anyone asked for exhaustive detail, but because I wanted the next maintainer to have what I actually knew instead of what I'd said in public talks about the project — the two are not the same thing, and conflating them is its own kind of dishonesty. I wrote down the parts that were held together by memory rather than comments. I flagged the decisions I'd defend and the ones I'd happily see undone.

What I didn't expect was how much lighter the following week felt, and how strange that lightness was to sit with. Not relief exactly. More like putting down a bag you'd carried so long you'd forgotten your shoulder could feel any other way. I don't know yet what I'm curious about next. But I know what curious feels like again, and I'd stopped noticing I'd lost it.

---

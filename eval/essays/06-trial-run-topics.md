# Trial run topics

The first session built the eval and tried it on a different set of five topics. 21 essays. The judge prompt at this point did not score essayist tells yet.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

## Topic: the value of learning in public

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline | Plain prompt (development only) |
|---|---|---|---|---|
| Development runs | – | 0.677 / 5.0 (×2) | – | 0.658 / 4.0 |
| Trial run, one topic | 0.690 / 4.0 | 0.687 / 5.0 | 0.658 / 4.0 | – |
| Trial run, full | 0.699 / 4.0 | 0.661 / 4.0 | 0.602 / 3.0 | – |

### Skill

`/write-in-kattni-voice` plus the task. Skill on.

#### Trial run, one topic · Aug 19, 12:11 AM

Style match 0.690 · Judge 4/10 · 506 words

> **Judge:** Kattni writes in plain, complete, methodical declaratives with heavy procedural detail and earnest first-person narration, while the candidate leans on punchy fragments, aphorisms ("It's just Tuesday"), an extended forest metaphor, and rhetorical questions that the reference samples never use.

---

Learning in public means doing the messy part where other people can see it. Not the finished blog post. Not the polished talk. The actual moment where you don't know something yet and you say so, out loud, where anyone could be watching.

That's terrifying the first time. I remember posting a question in a public channel about something I was sure everyone else already understood, bracing for the reply that would confirm it. It never came. What came instead was someone else saying "oh good, I wasn't sure either." That's the thing nobody tells you about learning in public: you are almost never the only one confused. You're just the only one who said it.

There's a version of this that looks like confidence. People share their wins, their finished projects, their clean solutions, and call that learning in public. It isn't, not really. That's showing your work after the learning already happened. The actual value is in the part before that, the false starts, the wrong turns, the "I tried X and it didn't work, here's why." That's the part that helps someone else skip your dead end.

I think about it like leaving a trail through a forest. You don't know yet which paths lead anywhere. You're hacking through undergrowth, backing out of dead ends, occasionally standing still because you have no idea which way to go. If you only publish the trail after you've found the destination, you've given someone a map. Useful, sure. But if you narrate the hacking too, you've given them something better: proof that the undergrowth is survivable, and maybe a warning about which direction not to bother with.

There's a selfish reason to do this too, and I don't think it needs an apology. Writing down what I don't understand forces me to find the edges of my own knowledge. It's uncomfortable in a specific way, the way explaining something out loud reveals the gap you'd been quietly stepping around. Learning in public is a forcing function for actually learning, not just accumulating a vague sense that you probably get it.

It also changes your relationship to being wrong. If you only ever speak once you're certain, every mistake feels like evidence you shouldn't have spoken at all. If you're used to thinking out loud in front of people, being wrong stops being a referendum on whether you belong in the room. It's just Tuesday. You correct course and keep going.

None of this means broadcasting every half-formed thought without judgment. There's a difference between learning in public and dumping your unprocessed panic on other people. The skill is in sharing the process while still being thoughtful about who's receiving it and what they need from you.

But the instinct to wait until you're sure, until it's clean, until you won't embarrass yourself? I'd push back on that instinct every time. The people who helped me most weren't the ones who already knew everything. They were the ones who let me watch them not know something yet.

---

#### Trial run, full · Aug 19, 12:27 AM

Style match 0.699 · Judge 4/10 · 544 words

> **Judge:** The candidate is polished essayistic advice-writing with punchy fragments, rhetorical questions to the reader, and aphoristic closers, whereas Kattni's voice is plainer, more procedural and chronological, favoring first-person recounting, hedges like "That said"/"Therefore", em-dash-free straightforward commas, and parenthetical clarifications rather than crafted rhetorical turns — and the leaked meta-preamble further breaks the match.

---

Good, close to 500 words and consistent with the voice guidelines. Here's the essay:

---

I published my first tutorial before I really understood the thing I was teaching. I knew enough to get the code working, enough to explain the steps, but not enough to know why one approach was better than another. I was terrified someone would point that out in the comments. Someone did, eventually. And it turned out to be one of the most useful things anyone ever told me.

That's the trade you make when you learn in public. You give up the comfort of only showing people your finished, polished understanding, and in exchange you get corrected faster, helped sooner, and connected to people who know things you don't. Most of us learn privately by default. We read, we experiment, we fail quietly in a text editor nobody else can see, and only once we feel confident do we say anything out loud. It feels safer. It is also slower, and it hides your work from the very people who could speed it up.

Learning in public just means narrating that process instead of hiding it. A blog post about a bug you haven't fully solved yet. A tutorial written the week after you learned the topic, not the year after. A question asked in a public channel instead of a private message. None of it requires expertise. It requires a willingness to be seen not knowing something, which is a different and honestly harder skill.

Here's what you get for that discomfort. Mistakes get caught early, while they're still cheap to fix, instead of after they've calcified into "how we've always done it." Other people who are exactly one step behind you find your notes and skip the hour you spent stuck. And the people who are ahead of you, the ones who'd never bother replying to a finished, confident post, will absolutely stop to correct a wrong assumption. Being visibly wrong is, weirdly, one of the fastest ways to get help.

I'm not suggesting you should perform confidence you don't have, or pretend every half-finished idea deserves an audience. Some things genuinely need more baking before they're useful to anyone else. But there's a wide gap between "not ready to share" and "not perfect yet," and most of us stay on the wrong side of that gap far longer than we need to. Waiting for mastery before you say anything means you learn alone, at the speed of one person, instead of in public, at the speed of everyone who happens to read what you wrote.

It also changes what you build. Writing something down for other people forces you to actually understand it, not just get it working. Explaining a concept exposes the parts you were fuzzy on far more reliably than silently using it ever will. The audience is part of the learning, not just the output of it.

None of this is about being an expert out loud. It's about being a beginner out loud, on purpose, where the right person might see it. That tutorial I published unsure of myself? It's still the one people tell me helped them most, not despite the uncertainty, but because it made room for theirs too.

---

### Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

#### Development runs, essay 1 · Aug 18, 11:54 PM

Style match 0.665 · Judge 5/10 · 525 words

> **Judge:** It borrows Kattni's first-person reflective subject matter and self-disclosure, but reads as polished essayist prose — aphoristic closers, em-dash-free balanced clauses, and rhetorical framing ("that discomfort is exactly where the value lives") — where Kattni writes in plainer, blunter, more procedural sentences with parenthetical asides, "That said,"/"Therefore," connectives, and less crafted punchlines.

---

Learning in public means doing the awkward, uncertain, definitely-not-expert part of learning somewhere other people can see it. A blog post. A pull request with your name on it. A talk that admits you figured this out three weeks ago. It is uncomfortable by design, and that discomfort is exactly where the value lives.

I used to keep my learning private until it looked finished. I'd work through a concept alone, get it mostly right, and only then mention it to anyone, once there was no chance of being caught not knowing something. It felt safer. It also meant nobody could help me while it mattered, and nobody watching me could learn from my mistakes, because I'd already edited them out.

The shift for me came with the BeeWare website rewrite. I didn't know Lektor. I barely knew HTML, Jinja, and CSS well enough to be dangerous. If I'd waited until I understood the whole system before touching anything, I never would have started. Instead, I opened a pull request early, with obviously incomplete work, and let a maintainer who knew far more than me watch me figure it out in real time. That is learning in public, whether or not you call it that. It's also how I found out that the reviewer's terse, no-comment-means-it's-fine feedback style wasn't going to work for me, and that I needed to say so. I wouldn't have learned that about myself, or been able to ask for what I needed, if I'd kept the whole process invisible.

There's a practical reason to do this, and it's the one people usually reach for first: someone else has already solved your problem, or is about to hit it themselves, and your public trail saves them the trouble. That's real. But it's not the main reason.

The main reason is that learning in public forces you to be honest about what you don't know, out loud, before you feel ready. That honesty is uncomfortable, and it's also the fastest way to actually learn. When I wrote about Markdown, I wasn't writing from a position of total mastery. I was writing down what I use 90% of the time, plainly, and admitting there's more I haven't covered. Writing it that way is what made me confident I actually understood it, rather than just having used it long enough to get by.

It also changes what kind of community you end up in. Watching Russ and the rest of the BeeWare team answer the same basic Git questions over and over, with the same patience each time, taught me more about what a healthy open source project looks like than any documentation could have. That only happens somewhere people are allowed to be visibly new. If everyone waits to show up until they've already figured it out, nobody gets to see that happen, and nobody gets invited to do the same.

I'm not suggesting you owe anyone a real-time narration of every mistake. Some things genuinely go better worked out quietly first. But if you're waiting for competence before you're willing to be seen, you're delaying the exact thing that gets you there.

---

#### Development runs, essay 2 · Aug 18, 11:57 PM

Style match 0.689 · Judge 5/10 · 518 words

> **Judge:** The reflective, community-minded warmth and BeeWare-adjacent subject matter fit Kattni's personal register, but the candidate's clipped fragments, aphoristic punch lines, and em-dash-free polish miss her characteristic long comma-spliced sentences, hedging asides in parentheses, transitional connectors like "That said"/"Therefore", and plain step-by-step plainness.

---

Learning in public means doing the thing before you're good at it, where people can see. Not the finished blog post about the thing you mastered six months ago. The messy part. The "I don't actually know if this is right" part.

I resisted this for a long time. It felt like showing up to a job with my incomplete homework. Wouldn't it be smarter to learn quietly, get competent, and only then say anything? That's the instinct, and it's wrong for reasons that took me a while to actually believe.

The first reason is selfish: writing something down while you're learning it forces you to know what you actually understand versus what you're gesturing at. When I wrote up the Markdown tutorial, I thought I knew Markdown cold. I'd been using it for years. But explaining nested list indentation to someone who has never seen it made me go test three separate editors, because I realized I didn't actually know why four spaces sometimes worked and sometimes didn't. I only found that gap because I was writing for someone else, not just using the thing for myself.

The second reason is less selfish, and it's the one that matters more. When I was working through the BeeWare tutorial at my first Sprint, I watched people who had never used Git get walked through their first pull request with total patience. Nobody there was performing expertise. The project lead was openly figuring things out alongside newer contributors, in public, on GitHub, where anyone could see the false starts. That's what made it feel safe enough to try. If everyone visible in that community had only ever shown up polished, I would have assumed I wasn't ready yet either. I wasn't ready. I did it anyway, and it worked out because the space was full of people also not-quite-ready.

That's the part people miss about learning in public. It's not really about you. Your half-finished attempt, your "here's what didn't work and why," your question that turns out to have an obvious answer, becomes the exact thing that makes the next person willing to try. I didn't understand this until I was on the other side of it, watching someone hesitate to ask a question I'd already asked out loud a month earlier. They asked it. That's the whole mechanism.

There's a cost, to be clear. Being visibly wrong in front of people is uncomfortable, sometimes a lot. I don't think that discomfort ever fully goes away, and I'm not going to pretend it does. What changes is what you do with it. You get a little faster at saying "I don't know, let me find out" instead of quietly disappearing to go figure it out alone and reappear looking like you always knew.

Learning in public doesn't require an audience of thousands. It can be one PR, one honest comment in a review thread, one blog post about a tool you're still not sure you built correctly. The value isn't in the size of the audience. It's in leaving a trail that someone behind you can actually follow.

---

#### Trial run, one topic · Aug 19, 12:12 AM

Style match 0.687 · Judge 5/10 · 552 words

> **Judge:** The candidate shares Kattni's earnest, first-person reflective warmth and self-deprecating honesty, but it leans on polished aphoristic cadences, sentence fragments for emphasis, and essayistic parallelism that the reference author rarely uses — she favors plainer, more procedural declaratives, frequent parentheticals, "That said,"/"Therefore," connectives, and concrete step-by-step detail rather than rhetorical closing flourishes.

---

I've been learning in public for about six years now, and it's changed the way I think about knowing things at all. Learning in public simply means doing the learning where other people can see it: writing the blog post before you're an expert, asking the question in the chat room, pushing the pull request that has your very first typo fix in it. It sounds like a small distinction from learning quietly and sharing the polished result later. It is not a small distinction. It is basically the whole thing.

The obvious fear is looking foolish. If you write down what you understand about a topic while you're still in the middle of understanding it, you will occasionally be wrong, in public, with your name on it. I used to think that was a reason to wait. I no longer think that. Waiting until you're sure just means you spend longer alone with the confusion, and it means the people around you never get the chance to say "actually, here's the piece you're missing," because they don't know you're missing it. Being visibly in-progress is what invites the correction. The correction is the whole point.

There's also a version of this that's less about corrections and more about company. When I sat down to write out the basics of Markdown, or to work through what it would take to get PO file translations working with MkDocs, I wasn't writing from a place of total mastery. I was writing down what I'd just figured out, while it was still fresh enough to explain clearly and still fresh enough that I remembered which parts had confused me first. That combination doesn't last. A year later I'd either have forgotten the confusing parts or forgotten how I resolved them. Publishing while you're learning captures something that publishing after you've learned cannot: the actual shape of the difficulty, from the inside.

It also does something for the people reading it that a finished, seamless account never quite manages. A tutorial written by someone three years removed from being a beginner tends to skip the steps that no longer feel like steps to them. A tutorial written by someone who hit the confusing part six weeks ago remembers exactly where it is, because they're not that far past it themselves. The account stays honest about where the friction actually was, because the friction hadn't been smoothed over by time yet.

None of this requires an audience of thousands. It barely requires an audience at all, some days. What it requires is being willing to let the unfinished version exist somewhere other than your own head, where it can be checked, questioned, or simply witnessed. I've had people fix scripts for me, point out CSS incantations I never would have found on my own, and hand me exactly the piece of context I was missing, all because I said what I was doing instead of doing it quietly and reporting back later. That kind of help only shows up when the work is visible while it's still happening.

So I keep doing it, imperfectly, typos and all. The alternative is polishing everything down to a finished product before anyone else gets to see the process, and the process turns out to be most of what's worth sharing.

---

#### Trial run, full · Aug 19, 12:27 AM

Style match 0.661 · Judge 4/10 · 514 words

> **Judge:** The candidate shares the author's warm, first-person reflectiveness and community-mindedness, but reads as a polished essayist — aphoristic closers, artful mid-sentence comma-nesting, and rhetorical parallelism — where Kattni writes in plainer, more declarative, procedurally-minded sentences with heavy parentheticals, bold/italic emphasis, and blunt markers like "Done." or "Welp."

---

Learning in public is a phrase I hear thrown around a lot these days, usually followed by someone explaining why they're finally starting that blog or that YouTube channel. I want to talk about why it's worth doing, because I've been doing a version of it for years now, and it has changed how I think about learning altogether.

The instinct most of us have when we're new at something is to hide the newness. We wait until we're competent, then we show up polished, and nobody has to witness the fumbling part. I understand the instinct completely. Fumbling in front of people is uncomfortable. But it's also, I've come to think, the whole point.

When I started writing tutorials for this blog, I wasn't writing them because I had mastered the material and wanted to hand down wisdom from on high. I was writing them because I had just learned the thing myself, and the learning was still fresh enough that I remembered exactly where I got stuck. That's actually a superpower that expertise erases. An expert forgets which steps are obvious and which aren't. Someone three days into a topic remembers every single snag, because they just lived through it. Learning in public means you get to use that freshness before it evaporates, instead of losing it to the very fluency you were chasing.

There's also the matter of correction. If I write something in private, in a notebook nobody reads, and I've gotten it wrong, I simply carry the wrong idea forward with me, undisturbed, possibly for years. If I write it in public, someone who actually knows the subject will, with some regularity, tell me I've got it backwards. This is occasionally humbling in the moment. It is also just about the fastest way I know to actually fix a misunderstanding, rather than politely nursing it forever.

And then there's the part that surprised me most, which is what it does for other people. I didn't fully appreciate this until I started contributing to BeeWare and watched how deliberately Russ and the team made space for people to be visibly new at something. It wasn't an accident. Somebody showing their in-progress, imperfect understanding gives everyone else permission to do the same. If the only visible work in a community is finished, mastered work, then anyone earlier in the process quietly assumes they don't belong yet. Show the middle of the process, not just the end of it, and you hand that permission to the next person still deciding whether they're allowed to ask a question.

None of this requires an audience of any particular size. It doesn't require confidence, either, which is good, because I rarely have much of that going in. It requires being willing to be seen not-yet-knowing something, in front of people who might notice. That's the uncomfortable part, and also, I'm fairly convinced, the useful part. The version of you that's still figuring it out is more valuable to other people than you think, and writing it down, publicly, is how that value actually gets somewhere.

---

### Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

#### Trial run, one topic · Aug 19, 12:13 AM

Style match 0.658 · Judge 4/10 · 521 words

> **Judge:** The candidate is a polished aphoristic op-ed — punchy fragments, em-dash asides, epigrams like "writing is a debugger for your own knowledge" — whereas Kattni writes plainly and procedurally in longer, comma-spliced explanatory sentences with concrete personal detail, parenthetical clarifications, and understated markers like "Welp," "Done," or "That said," so only the first-person reflective stance overlaps.

---

Learning in public gets treated like a personal branding tactic, and that framing does it a disservice. Yes, it builds an audience. Yes, it can lead to opportunities. But the actual value is upstream of all that — it changes how you learn.

Here's the mechanism: when you know you're going to write about something, you pay attention differently. You stop skimming past the parts you don't fully understand. You can't hand-wave "and then it just works" in a blog post the way you can in your own head. The moment you sit down to explain how a piece of async code actually resolves, or why a build step behaves the way it does, you find the gaps in your own understanding immediately. Writing is a debugger for your own knowledge. It surfaces the exact line where your mental model breaks down, and that's usually the exact line worth studying next.

I'd go further: private learning is comfortable in a way that's mildly dishonest. You can convince yourself you understand something because you followed a tutorial and it worked. Nothing forced you to explain the why. Learning in public strips that comfort away, because the audience — even an audience of three people, even an audience of nobody who ever replies — is a proxy for rigor. You write as if someone will ask "wait, why?" and that anticipation does more for your understanding than the actual feedback ever will.

It also does something for the timeline of your learning that private notes don't: it captures the beginner's view of a topic before you lose access to it. Six months from now, once you've internalized a concept, you won't remember which part was confusing. The person who benefits most from a "how I finally understood closures" post is not some abstract audience — it's the version of you writing it right now, and it's everyone who's exactly where you were last week. Experts are bad at writing beginner content because they've forgotten what it's like not to know. Document while you're still confused; that's the only window you get.

There's a version of this that feels risky — publishing something wrong. I used to treat that as the cost of learning in public. I've come around to thinking it's the point. A wrong post that gets corrected is a faster feedback loop than a right post that never gets seen. Being visibly wrong in public, and updating, models something useful: that expertise isn't a fixed state you arrive at quietly and then perform. It's iterative, and it's supposed to look iterative.

None of this requires an audience, a newsletter, or a following. It requires artifacts — a doc, a repo README, a thread, a talk you never gave but wrote the outline for anyway — that exist in a form someone other than you could, in theory, read. The public part isn't about visibility. It's about accountability to clarity. Write the thing you'd want to have read six months ago, and let the fact that someone might read it do the work of making you actually understand what you're talking about.

---

#### Trial run, full · Aug 19, 12:28 AM

Style match 0.602 · Judge 3/10 · 500 words

> **Judge:** The candidate is aphoristic and essayistic with punchy fragments, em-dash asides, and epigrammatic reversals, whereas Kattni writes plain, procedural, explanatory prose with long qualified sentences, frequent 'That said'/'However' connectives, parenthetical clarifications, and concrete step-by-step detail rather than rhetorical polish.

---

Learning in public gets treated like a personality trait — something extroverted people do, tweeting their bugs for likes. That framing misses the actual mechanism. The value isn't the audience. It's what happens to your own thinking the moment you know someone might read it.

When I'm debugging alone, I let myself get away with vague explanations. "It's something with the async handling" is a thought I can hold in my head and move past without ever pinning down what "something" means. The instant I try to write that sentence for someone else — a blog post, a PR description, a Slack message to a teammate — the vagueness becomes visible. I have to say what's actually happening, which means I have to know what's actually happening. Half the debugging is done by the time I finish the sentence I was going to write to explain the bug I hadn't solved yet.

That's the real trade being made when you learn in public: you're not performing expertise, you're outsourcing your own rigor to an imagined reader. The reader doesn't even have to be real. I've solved problems writing GitHub issues I never posted, because the act of addressing someone forced a level of precision that addressing myself didn't.

There's a second, slower payoff, which is that public learning compounds in a way private learning doesn't. A note in your own head evaporates. A note in a private file gets lost in a folder you forget exists. A note written clearly enough for a stranger to follow becomes something you can find again — searchable, linkable, citable — and something other people can find too. I've had strangers fix bugs in year-old blog posts by leaving a comment, which means the thing I wrote to teach myself kept teaching after I was done with it. That's not a networking benefit. That's the artifact doing more work than I could have done alone.

The part people resist is the exposure — writing something down while you're still wrong about it. But being visibly wrong in public is a feature, not a cost, if you treat corrections as the actual product. The best technical writing I've done started as a confidently incorrect draft that got quietly fixed by someone who knew more than me. I didn't lose credibility by being wrong in front of people. I gained a correction I wouldn't have gotten by staying quiet until I was certain, which for most interesting problems is a certainty that never arrives.

None of this requires an audience of thousands. It requires one imagined reader who isn't you, and a willingness to let that reader see the draft before it's finished. Learning in public isn't a content strategy. It's a discipline you impose on your own understanding, using other people's eventual attention as the enforcement mechanism. The public part is almost incidental. What matters is that writing for someone else is the only reliable way I've found to notice what I don't actually know.

---

### Plain prompt (development only)

The task alone, with no author named and no samples.

#### Development runs · Aug 18, 11:58 PM

Style match 0.658 · Judge 4/10 · 488 words

> **Judge:** The reassuring, encouraging register glances at Kattni's personal posts, but the candidate's aphoristic fragments, second-person framing, and total absence of first-person anecdote, parenthetical asides, and her plodding connective phrasing ('That said,' 'Therefore,' 'However,') make the rhythm and punctuation habits clearly a different hand.

---

Learning in public means doing your learning where other people can see it. Not just the finished blog post that makes you look like you knew what you were doing all along. The messy middle too. The wrong turns, the "wait, that's not it either," the moment you finally get it and go, oh, *that's* what that means.

It feels risky. That's the first thing to say plainly, because pretending it doesn't is dishonest. Posting a question that reveals you don't understand something "everyone" already knows is uncomfortable. Sharing a half-working project instead of waiting for the polished version is uncomfortable. There's a version of you that wants to wait until you're the expert before you say anything at all.

But waiting for expertise before you speak means nobody ever hears from the person who was struggling yesterday. And that person is exactly who a beginner needs to hear from.

Here's the thing about expertise: once you have it, you lose access to what it was like not to have it. An expert explaining a concept has usually forgotten which parts were hard. They've forgotten the specific wrong assumption that tripped them up, because they stopped making that assumption years ago. But the person who just climbed out of confusion, an hour ago, a week ago, remembers every step of the climb. They know exactly where the ground gave way. That makes their explanation more useful to the next person standing at the bottom, not less.

Learning in public also changes what you produce along the way, because an audience, even a small one, changes how you learn. Explaining something forces you to actually understand it, instead of just recognizing it. There's a real difference between "I've seen this before" and "I could teach this to someone else." Writing it down, out loud, for a reader, is what closes that gap.

And it builds something you can't build any other way: a trail. Six months from now, when you hit a version of the same problem, your own public notes are often the fastest path back to the answer. Future you is a beginner too, just a beginner with amnesia instead of inexperience.

There's a social cost people worry about that mostly doesn't materialize. Most people aren't watching closely enough to judge you for an early-stage question. The ones who are paying attention are usually other people learning the same thing, relieved someone said the quiet part out loud. Occasionally someone will be unkind about it. That says more about them than about you asking.

None of this means share everything, all the time, with no filter. Learning in public isn't a performance and it isn't a confessional. It's just choosing not to hide the process, because the process is the useful part.

The finished answer is nice. But it's the trail that helps the next person, and it's the trail that turns out to help you too.

---

## Topic: making your first open source contribution

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Trial run, full | 0.725 / 5.0 | 0.657 / 5.0 | 0.664 / 4.0 |

### Skill

`/write-in-kattni-voice` plus the task. Skill on.

#### Trial run, full · Aug 19, 12:28 AM

Style match 0.725 · Judge 5/10 · 514 words

> **Judge:** The candidate shares the author's earnest, encouraging first-person-contributor subject matter but reads as polished essayist prose — punchy fragments, rhetorical asides, and a lyrical closing — where Kattni writes longer, plainer, comma-heavy sequential sentences with hedges like "that said" and "admittedly," parenthetical definitions, italic/bold emphasis, and concrete procedural specifics rather than aphoristic advice.

---

My first open source contribution was a one-line change to a README. I'd found a typo in a setup guide for a Python library I was using, forked the repo, fixed the typo, and opened a pull request. It took about ten minutes. I remember refreshing the page every few hours for two days, waiting to see if anyone would respond.

It got merged. That was it. No fanfare, no code review comments, just a green checkmark and a "thanks!" from a maintainer I'd never met. And somehow that tiny, almost embarrassingly small change did more to make open source feel real to me than any amount of reading about it had.

I think that's the part people get wrong when they're starting out. They imagine a first contribution has to be substantial to count, some clever bug fix or a whole new feature that proves they belong. It doesn't. What it actually needs to do is teach you the mechanics: how to fork a repo, how to open a pull request, how to have your code looked at by someone who has never seen your work before and doesn't owe you anything. Those mechanics are the real skill. The code is almost beside the point the first time.

So where do you start, if you don't have a typo handy? Most projects on GitHub tag beginner-friendly work with labels like "good first issue" or "help wanted." Search for those. Pick a project you already use, something you have opinions about because you've hit its rough edges yourself. That context is worth more than picking a trending repo you've never opened before.

Read the contributing guidelines before you write a single line. This is not optional, and it's the step people skip most often. Every project has its own conventions for commit messages, testing, and code style, and showing up with a pull request that ignores all of them is a fast way to make extra work for a maintainer who is almost certainly a volunteer. Reading the guidelines first is a small act of respect for their time.

Then, when you're ready, ask before you build anything big. A quick comment on an issue saying "I'd like to work on this" saves you from spending a weekend on something someone else already claimed, or on an approach the maintainers would have steered you away from immediately. That's not gatekeeping. It's just how a project with more than one contributor stays sane.

And if your first PR gets requested changes instead of an immediate merge, that's normal. It isn't rejection. It's what code review looks like everywhere, on every team, for every engineer, no matter how experienced. Take the feedback, make the change, push again.

None of this is complicated. It's mostly just doing the thing once so it stops being unfamiliar. My typo fix didn't teach me anything about the library's internals. It taught me that the process wasn't as intimidating as it looked from the outside, and that a whole community was on the other side of it, ready to say thanks.

---

### Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

#### Trial run, full · Aug 19, 12:29 AM

Style match 0.657 · Judge 5/10 · 495 words

> **Judge:** The candidate borrows Kattni's subject matter and some biographical details but replaces her plain, procedural, comma-heavy explanatory voice with a polished essayist's cadence — aphorisms, fragments, anaphora, and rhetorical flourishes ("wearing a small thing's clothes") that she never uses.

---

Making your first open source contribution feels like it should be a small thing. It is not a small thing. It is, more often than not, an enormous thing wearing a small thing's clothes, and nobody tells you that going in.

Here is what nobody tells you: the code is rarely the hard part. I say this as someone whose first contribution was removing a single "s" from a word that should have been singular. One character. And I still remember the small thrill of watching it get merged, because merged means someone looked at what you did and decided it belonged. That's the whole thing, really. Belonging.

The intimidating part isn't the syntax, it's the not knowing. You don't know if your question is a stupid question. You don't know if the maintainer is annoyed with you or just terse by nature. You don't know if the thing you fixed was actually broken, or if you've just spent two hours "fixing" something that was fine all along. Every open source project has its own quiet customs, and you are, for a while, a stranger in someone else's house, unsure which drawers you're allowed to open.

What made the difference for me wasn't skill. It was people who made space for the not-knowing. A maintainer who answered a question I was embarrassed to ask. A community that helped folks who had never touched Git before, without a hint of impatience. That kind of welcome is not automatic, and it is not universal, but when you find it, it changes what you think is possible for yourself.

If you're looking to make your first contribution, start absurdly small. A typo. A missing word in a tutorial. A broken link. It will feel too small to matter. Do it anyway. The goal of a first contribution isn't to prove you belong there, it's to learn the mechanics of what contributing even looks like: forking, branching, opening a pull request, waiting, responding to review. Once you've done that once, on something tiny, you have the shape of the process, and the next contribution is a little less terrifying.

And when the review comes back with changes requested, know that this is not a referendum on whether you should be there. It's just how the process works, for everyone, always. It took me longer than I'd like to admit to internalize that constructive feedback and belonging are not opposites. A good reviewer pushing back on your approach is not the same as a good reviewer thinking you shouldn't be there. If you find yourself needing more explicit reassurance than you're getting, it is entirely reasonable to ask for it. That is not weakness. That is knowing what you need to keep going.

Your first contribution won't be your best work. It doesn't need to be. It needs to exist, and it needs to be yours, and it needs to be the thing that gets you to the second one.

---

### Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

#### Trial run, full · Aug 19, 12:30 AM

Style match 0.664 · Judge 4/10 · 517 words

> **Judge:** The candidate's polished second-person advice-essay voice, aphoristic parallel constructions, and em-dash-heavy rhetorical flourishes contrast with Kattni's plainer, first-person narrative or step-by-step instructional style built on comma-spliced qualifiers, parenthetical asides, "For example," framing, bulleted kBits, and blunt one-word closers like "Done.

---

Making your first open source contribution feels like standing at the edge of a pool that everyone else seems to already know the depth of. You've read the code, maybe even used the project for months, but there's a gap between "I understand this" and "I am confident enough to open a pull request against it." That gap is mostly imagined. It's worth closing anyway, because the way you close it teaches you more about software than most tutorials will.

Start smaller than feels reasonable. Not because your judgment about what needs fixing is bad, but because your first contribution isn't really about the code — it's about learning the shape of a project's expectations. Every repository has its own unwritten rules: how commits are described, whether tests are mandatory, how maintainers like issues framed before a PR ever shows up. A typo fix or a one-line documentation clarification won't teach you much about the codebase, but it will teach you the whole mechanical loop — fork, branch, commit, push, open a PR, respond to review comments — without the added stress of also being technically wrong about something. Get the loop right first. The harder problems can wait until the loop feels automatic.

Read the CONTRIBUTING file even when you're sure you don't need to. I say this as someone who has skipped it and paid for it in review comments that were really just someone pointing me back to a document I hadn't opened. Maintainers write these guides because they've answered the same question fifty times, and skipping the guide means you're volunteering to be the fifty-first.

When you do pick something more substantial — a bug you've hit yourself is usually the best entry point, because you already have a reproduction case and a reason to care — resist the urge to fix everything you notice along the way. It's tempting to also rename that oddly-cased variable, or refactor a function that clearly could be cleaner. Don't. A focused PR is a fast PR. A PR that touches twelve unrelated things is a PR that sits in review for three weeks while the maintainer tries to figure out what you actually changed and why.

Expect feedback, and expect some of it to feel blunt. Open source maintainers are often volunteering their evenings to review your code, and terseness is rarely personal — it's bandwidth. Ask questions in the PR thread if a comment is unclear rather than guessing; that thread is documentation for the next contributor too, not just a conversation between you and one reviewer.

And when your PR merges — even if it's three lines — notice what just happened. Code you wrote is now part of something other people rely on, reviewed and vetted by people who owed you nothing. That's the actual milestone, more than the diff itself. It's also the moment the second contribution stops being scary, because now you know the loop, you know the etiquette, and you know that the maintainers are just people trying to keep a good thing running, same as you're about to be.

---

## Topic: why documentation deserves more care than it gets

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Trial run, full | 0.696 / 4.0 | 0.673 / 4.0 | 0.609 / 3.0 |

### Skill

`/write-in-kattni-voice` plus the task. Skill on.

#### Trial run, full · Aug 19, 12:30 AM

Style match 0.696 · Judge 4/10 · 495 words

> **Judge:** The candidate is a polished, aphoristic opinion essay with rhetorical fragments, second-person hooks, and a punchy closing line, whereas Kattni writes plainly and procedurally — long, explanatory, comma-heavy sentences with hedges like "that said," "admittedly," and "basically," concrete first-person narrative detail, and almost no stylized punchlines or bolded slogans.

---

Documentation gets treated like the thing you do after the real work is finished. Ship the feature, fix the bug, then circle back and write it up. Except "circle back" rarely happens, because by then there's a new feature and a new bug, and the docs stay exactly as thin as the day you meant to improve them.

That ordering is the problem. Documentation isn't a wrapper around the work. It's part of it.

Think about what documentation is actually for. It's not a compliance artifact, and it's not there to make a project look professional. It's the thing that stands between a person and hours of confusion. Someone opens your project at 11pm, trying to solve a problem you solved months ago, and the only version of you available to help them is whatever you wrote down. If you wrote nothing, they get nothing. They get a source dive, a guess, maybe a GitHub issue that says "same problem, no fix" from two years ago.

I've been that person. I've also been the person who wrote the docs badly enough that I couldn't follow my own instructions six months later. Both experiences taught me the same lesson: the cost of skipping documentation doesn't disappear, it just moves. It moves onto someone else's evening, or onto your own future self, who is somehow always less patient than you'd hope.

So why does it keep losing the priority fight? Partly because writing is a different skill than building, and a lot of us who build things didn't get much practice at the other one. Partly because the payoff is invisible. Nobody files a bug report for "the docs were fine and I didn't need to ask anyone anything." Good documentation looks like nothing happened. That's exactly what makes it easy to shortchange, and exactly why it deserves the opposite treatment.

There's also a harder truth hiding in here: writing documentation forces you to actually understand what you built. If you can't explain why a function exists, or what happens when it fails, that's not a writing problem. That's a design gap you were about to hand to someone else without noticing. Documentation is one of the few tasks that pays you back twice, once for the reader, and once for revealing the parts of your own thinking you hadn't finished.

None of this means every project needs a wiki, or that every function needs a paragraph. Good documentation is scoped to what a real person needs to get unstuck, not to some abstract completeness. A clear README and a few honest comments on the non-obvious parts will outperform an exhaustive doc site nobody maintains. **The goal isn't more documentation. It's documentation that someone, someday, will actually be able to use.**

That's the care it deserves. Not reverence, not a separate phase, just the same attention you'd want if you were the one showing up at 11pm with a problem and nothing but what got written down.

---

### Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

#### Trial run, full · Aug 19, 12:31 AM

Style match 0.673 · Judge 4/10 · 505 words

> **Judge:** The candidate borrows Kattni's subject matter and a couple of her actual anecdotes but writes in a polished essayistic register — rhetorical parallelism, aphoristic closers, comma splices, and em-dash-free flowing periods — where Kattni writes plainly and procedurally in short declaratives with heavy first-person recounting, parenthetical asides, "That said," and blunt one-word sentences.

---

Documentation is the part of a project that everyone agrees matters and almost no one budgets time for. It gets treated as the thing you do after the real work is done, if there's time left, which there never is, because there's always another feature, another bug, another thing that feels more urgent. And yet it's the first thing a new contributor touches, and often the only thing standing between "I'd love to help" and someone quietly closing the tab.

I've spent a fair amount of the last year deep in documentation tooling, translation workflows, and rewriting an entire website's worth of content, and what struck me most is how much invisible labor goes into making documentation actually good. It's not just writing sentences that are technically correct. It's anticipating the reader who knows nothing, and the reader who knows almost everything, and giving both of them a path through the same page. It's noticing that a link moved and making sure it still resolves to something useful instead of a 404, because a dead link doesn't just annoy someone, it tells them the project stopped caring about them the moment they left the happy path. It's the difference between "this is technically documented somewhere" and "I can actually find what I need."

That care is expensive in a way that's hard to see from the outside. It doesn't show up as a shipped feature. It doesn't close an issue with a satisfying commit. It's slow, unglamorous, detail-obsessed work, the kind where you quadruple-check a find-and-replace across hundreds of files because you know, from experience, that it'll get something wrong if you don't. Nobody applauds you for a sentence that's clearer than it used to be. But that clarity is exactly what determines whether someone's first experience with a project is "I figured it out" or "I gave up."

I think part of the problem is that documentation gets evaluated by people who already understand the thing being documented. If you already know how the pieces fit together, you can't see the gaps, because your brain fills them in automatically. It takes someone coming in cold, or someone willing to sit with the discomfort of not knowing, to find where the explanation breaks down. That's a genuinely different skill than writing the code in the first place, and it deserves to be treated as one, not as an afterthought that anyone can knock out in an afternoon.

The projects that get this right tend to be the ones that grow the healthiest communities, because good documentation is really just a form of hospitality. It's a way of saying: we thought about you before you got here. We didn't just build something and leave you to reverse-engineer it. When that care is missing, people don't usually complain, they just quietly leave, and you never find out how many of them there were. Documentation deserves more care than it gets because it's often the only conversation a project has with someone before they've decided whether to stay.

---

### Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

#### Trial run, full · Aug 19, 12:31 AM

Style match 0.609 · Judge 3/10 · 509 words

> **Judge:** The candidate is a polished opinion essay full of aphoristic parallelism, em-dash rhetoric, and abstract argument, whereas Kattni writes plainly and procedurally in first person about concrete personal experience, with short declarative sentences, comma-heavy hedges ("however,", "That said,"), lists, and inline code rather than epigrams.

---

Documentation gets treated like a tax you pay after the real work is done. You ship the feature, the tests go green, and then someone — often the person who wrote the code, sometimes whoever drew the short straw — writes a paragraph explaining what just happened. It reads like an afterthought because it was one. And yet documentation is the only artifact most of your users will actually encounter. They won't read your commit history. They won't trace your call stack. They'll read the docs, form an opinion about your project in the first ninety seconds, and either stay or leave.

I think the reason documentation gets shortchanged is that its cost is visible and its payoff is deferred. Writing a clear paragraph takes ten minutes you can feel yourself spending. The person who benefits is a stranger, six months from now, debugging something at 11pm, who will never send you a thank-you note — they'll just quietly not file a support ticket, and you'll never know the crisis you averted. Bad code fails loudly, in CI, in front of you. Bad documentation fails quietly, in someone else's tab, where you can't see it. That asymmetry is why it's so easy to under-invest here even when you know better.

There's also a harder truth: documentation isn't a lesser skill than code, it's a different skill, and treating it as an easier stepsibling of "real work" produces text that reads like it was written by someone doing you a favor. Good documentation requires the same rigor as good code — knowing what to leave out is as hard as knowing what to include, and a misleading example is a bug, full stop, the same as a null pointer exception. It should be tested. It should be reviewed with the same scrutiny you'd give a pull request that touches auth. When I write docs, I try to run every code sample, not just eyeball it — because nothing erodes trust in a project faster than a snippet that doesn't compile, discovered by someone who already had to overcome friction just to get there.

The other thing I've come to believe is that documentation is a design surface, not a reporting surface. If you can't explain an API cleanly, that's often a signal the API itself is awkward — writing the docs first, or alongside the implementation, surfaces bad interface decisions while they're still cheap to fix. Treating docs as something you write after the design is locked means you lose that feedback loop entirely.

None of this requires heroics. It requires the same care you'd extend to any other user-facing surface: write for the reader who has less context than you, test your examples like you'd test your code, and update docs in the same commit as the change, not in a follow-up ticket that never gets filed. Documentation is a product feature. It deserves a product feature's attention — not because it's noble, but because it's the thing standing between your work and the people trying to use it.

---

## Topic: a project that didn't go the way I planned

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Trial run, full | 0.626 / 4.0 | 0.632 / 4.0 | 0.626 / 4.0 |

### Skill

`/write-in-kattni-voice` plus the task. Skill on.

#### Trial run, full · Aug 19, 12:31 AM

Style match 0.626 · Judge 4/10 · 511 words

> **Judge:** The candidate adopts a wry, literary confessional voice with punchy fragments and dramatic beats, whereas Kattni writes in plain, methodical, explanatory prose with even-paced full sentences, heavy comma-clause qualification, parenthetical asides, and frequent step-by-step or link-laden detail, so only the first-person reflective register loosely overlaps.

---

Two weeks before the con, I decided the badge needed sound.

That's the sentence that started it. I'd already built the e-ink name badge. It worked. The display updated, the battery lasted the whole weekend, the code was clean enough that I wasn't embarrassed by it. I should have shipped it exactly like that. Instead I looked at the empty GPIO pins and thought, what if it played a little chime when you pressed the button?

I own a small speaker. I own a library that plays WAV files. I had, in my head, about four hours of work standing between me and a badge that beeped happily at strangers. I did not have four hours. I had two weeks, most of which were already spoken for by things like sleep and my actual job.

The first problem was current draw. The speaker pulled enough power that the display started glitching whenever the chime played, because I hadn't separated the power rails and the same battery was trying to do two things at once. Fine. I could fix that with a second regulator. I ordered one. It shipped slower than I wanted it to.

While I waited, I kept "improving" the code. This is the part of the story where I stop being a victim of circumstance and start being the author of my own problem. I added a settings menu so people could mute the chime. Then I added three chime options, because one felt stingy. Then I decided the settings needed to persist across power cycles, which meant writing to flash, which meant learning more about wear leveling than I had any real use for in a weekend project.

None of this was necessary. None of it was even asked for. I was solving problems I had invented to avoid admitting the original plan wasn't going to fit in the time I had.

Four days before the con, the regulator arrived. I soldered it in. The display stopped glitching. The chime played. And the settings menu, the one I'd spent two nights on, had a bug that wiped the mute preference every third boot, and I could not find it in time.

So the badge I brought to the con had sound, sometimes not muted when it should have been, occasionally chirping in the middle of a quiet conversation. Mildly embarrassing. Genuinely funny, in retrospect, watching people flinch.

Here's what I actually took from it. The badge that worked was the one I'd already finished before I added anything. Every hour after that point made the project worse, not better, and I knew it while I was doing it. I wasn't fixing a gap. I was avoiding the feeling of being done, because done meant I couldn't tinker anymore.

I still add features I don't need. I don't think that instinct goes away, and I'm not sure I'd want it to. But I've gotten better at noticing the moment it happens, and asking myself, out loud if I have to, whether I'm building something or just avoiding finishing it.

---

### Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

#### Trial run, full · Aug 19, 12:32 AM

Style match 0.632 · Judge 4/10 · 519 words

> **Judge:** The candidate adopts a polished, aphoristic essayist voice with rhetorical triads, em-dash-free but comma-spliced cadence and abstract closing wisdom, whereas Kattni writes plainly and concretely with short declarative sentences, procedural detail, parenthetical asides, hedges like "that said" and "admittedly," and unadorned endings — the reflective-personal register overlaps somewhat but the literary polish and lack of specifics don't match.

---

A few years ago, I decided I was going to write a small game for a microcontroller badge, something modest, something I could finish in a weekend and be proud of. It did not go that way. I want to walk through what happened, partly because I think the failure is more useful than the eventual success, and partly because I suspect I'm not the only person this has happened to.

The plan was simple enough on paper. I had a board, I had CircuitPython, and I had an idea for a tiny interactive display, something with a few states and a couple of buttons. I figured I understood the pieces well enough that the actual writing would be the easy part. What I hadn't accounted for was that "I understand the pieces" and "I understand how the pieces behave together, on this specific hardware, under these specific constraints" are two very different claims. The eInk display, it turned out, had opinions about refresh timing that nothing in my mental model had prepared me for. Button debouncing, which I'd waved off as a solved problem, was not solved, not for me, not that week.

I spent the first few days assuming I was close. This is, I've learned, a dangerous assumption to hold onto for too long. Each fix revealed a new, adjacent problem, and each of those problems looked small enough on its own that I kept believing the finish line was still just ahead of me. It wasn't until I'd rewritten the same function for the fourth time that I let myself admit the actual scope of what I'd taken on. The weekend project was, in fact, not a weekend project.

What I did next mattered more than anything I'd done up to that point: I stopped trying to force the original plan to work and instead let the project tell me what it actually was. That meant setting aside the version I had in my head, the one that was clever and compact, and building something rougher that simply worked. It meant asking for help earlier than my instincts wanted to, because pride is expensive and time is not infinite. And it meant accepting that the thing I'd eventually ship would look different from the thing I'd first imagined, and that this was fine.

The finished project, when it did arrive, was worse in some ways than my original idea and better in others. It was less elegant. It was also something that existed, which counts for a great deal more than an elegant idea that never left my head.

I think about this whenever I start something new now. I try to hold my plans loosely, not because planning is worthless, but because the plan is a starting guess, not a contract. The moment a project stops matching the shape I expected is not a sign that I've failed. It's just the project, finally, telling me the truth about itself. My job is to listen, adjust, and keep going, even when what I end up with looks nothing like what I sat down to build.

---

### Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

#### Trial run, full · Aug 19, 12:32 AM

Style match 0.626 · Judge 4/10 · 497 words

> **Judge:** The candidate is a polished, literary reflective essay with em-dash-driven cadence, ironic understatement, and crafted aphorisms, whereas Kattni writes plainly and procedurally with short declarative sentences, comma-heavy hedging phrases ("That said,", "however,"), parenthetical explanations of jargon, enthusiastic sincerity, and British spellings — so only the first-person practitioner voice overlaps.

---

The project was supposed to take a weekend.

I remember thinking that, specifically, because I wrote it in the README before I'd written a single line of code: "Goal: working prototype by Sunday night." I was building a small tool to auto-generate API documentation from docstrings — something to scratch my own itch after one too many afternoons spent hand-updating docs that had drifted from the code they described. The scope felt tight. Parse the source, extract the comments, render them into something readable. A weekend project, the kind you finish with a satisfied little commit message and a tab closed forever.

By Sunday night I had, instead, three competing parser implementations, a growing suspicion that I didn't understand my own requirements, and a test suite that passed for the wrong reasons. What I'd underestimated wasn't the parsing — that part was almost exactly as hard as I'd expected. What I hadn't accounted for was that "docstrings" meant something different in every codebase I tested against. Some teams used one convention, some used another, some used no convention at all and just wrote prose. My tidy weekend tool needed to be either far more opinionated or far more flexible than I'd designed for, and I hadn't decided which.

I spent the next two weeks in a state I've come to recognize in myself: the quiet stubbornness of someone who thinks the *next* refactor will be the one that makes it click. It never quite was. Each fix exposed an assumption I hadn't known I'd made. I'd bolt on a special case, watch it work, and then find the special case broke something three files away. The codebase got harder to read, not easier, which is usually the signal I ignore longest and should ignore least.

What actually saved the project wasn't a clever abstraction. It was writing down, in plain language, what the tool was actually for — not "parse docstrings" but "let a team stop maintaining two sources of truth." Once I had that sentence, half my "features" turned out to be scope creep I'd added to feel like I was making progress, and I cut them. The tool that shipped, eventually, did much less than the one I'd sketched out that first weekend. It supported one convention well instead of five conventions badly.

I don't think the lesson here is the tidy one — "plan better next time" — because I don't think better planning would have caught this. I didn't know what I didn't know about docstring conventions until I went and looked at real code written by real people who didn't care about my README. The lesson, if there is one, is closer to: the plan is a hypothesis, not a commitment, and the sooner you're willing to say the hypothesis was wrong, the less time you waste defending it. I still write the "goal" line at the top of new projects. I've just stopped expecting it to survive contact with the work.

---

## Topic: getting started with CircuitPython on a microcontroller

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Trial run, full | 0.715 / 5.0 | 0.688 / 6.0 | 0.675 / 4.0 |

### Skill

`/write-in-kattni-voice` plus the task. Skill on.

#### Trial run, full · Aug 19, 12:33 AM

Style match 0.715 · Judge 5/10 · 495 words

> **Judge:** The candidate shares the author's approachable beginner-tutorial subject matter and some vocabulary, but it leans on punchy fragments, second-person marketing cadence, and em-dash-free clipped asides instead of Kattni's longer, comma-heavy, methodically hedged sentences with explicit step lists, bolded warnings, "For example, to X, you would include:" scaffolding, and personal first-person framing.

---

You plug in a microcontroller for the first time and it feels like nothing happened. No app to open, no account to create, no build step. Just a tiny drive that showed up on your computer like a USB stick. That's actually the whole point.

CircuitPython is a version of Python built to run directly on small, cheap hardware called microcontrollers. Not your computer, not the cloud, an actual physical board about the size of a stick of gum, with real pins you can wire to real LEDs, sensors, and motors. If you've written Python before, most of what you know still applies. If you haven't, this is one of the gentler ways in.

Here's what getting started actually looks like. You get a supported board (Adafruit's are common, but plenty of manufacturers support it now), install CircuitPython onto it, and plug it in with a USB cable. The board shows up on your computer as a drive named CIRCUITPY. That's it. No compiler, no flashing tool, no terminal incantations.

On that drive is a file called `code.py`. This is the file that runs, automatically, every time the board powers on or the file changes. You edit it in any text editor you like, save, and the board restarts the program instantly. That loop, edit, save, watch it run, is the whole development cycle. There's no separate "upload" step to remember, which sounds small until you realize how much friction it removes.

For example, to blink the built-in LED, you'd write something like:

```python
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

Save that as `code.py`, and the LED starts blinking. This tells the board to grab the LED pin, set it up as an output, and flip it on and off every half second, forever. If it's not blinking, check that the file is actually named `code.py` and that it's saved directly on the CIRCUITPY drive. That trips people up more than anything else at this stage, and it's not a sign you've done something wrong. It's just the one gotcha worth knowing about in advance.

Try changing `0.5` to `0.1` and see what happens. Then try wiring an external LED to a different pin and swap `board.LED` for that pin's name. Small changes like this are how the pieces start to click.

Beyond the built-in LED, there's a whole library bundle for sensors, displays, and other hardware, so you rarely need to write drivers from scratch. You import what you need, the same way you would with any Python package.

None of this makes you an embedded systems engineer overnight. It won't replace lower-level tools when you genuinely need that level of control. But as a way to get a physical object doing something in the first twenty minutes, it's hard to beat. The gap between curiosity and a blinking light is about as small as it gets.

---

### Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

#### Trial run, full · Aug 19, 12:33 AM

Style match 0.688 · Judge 6/10 · 518 words

> **Judge:** The candidate shares the author's warm, encouraging tutorial voice and some signature touches (italicized _CIRCUITPY_/_code.py_, the MacOS Sonoma 14.4 warning, backticked code), but it reads as smoother, more essayistic prose with polished flourishes ('refreshingly plain', 'hard to overstate') rather than the author's plainer, procedural, heavily-bulleted style with its short declarative punches ('Done.', 'You're all set to go!'), bolded step commands, and structural headings.

---

Getting Started With CircuitPython on a Microcontroller

CircuitPython is a version of Python designed to run on tiny computers called microcontrollers. If you've never worked with hardware before, that sentence alone might sound intimidating. It isn't. Of all the ways I know to get someone writing code that controls a physical object, CircuitPython is by far the most approachable, and I want to walk you through what getting started actually looks like.

The first thing to understand is that a microcontroller running CircuitPython behaves like a USB drive. You install CircuitPython onto the board once, and from then on, plugging it into your computer mounts a drive called _CIRCUITPY_. There's no compiler, no build step, no flashing process for every change. You edit a file called _code.py_, save it, and the board runs it immediately. Save again, and it runs again. This is, genuinely, the entire development loop.

Installing CircuitPython itself is a short, repeatable process, though the exact button sequence varies slightly by board. Generally, you'll hold down a button labeled BOOTSEL (or similar) while plugging in or resetting the board, which puts it into a bootloader mode and mounts a differently named drive. You then drag a `.uf2` file, downloaded from [circuitpython.org](https://circuitpython.org), onto that drive. Wait a moment while it copies over, and the drive will unmount and disappear, replaced by _CIRCUITPY_. That's it. You now have a computer running Python that fits in your palm.

From there, the code itself is refreshingly plain. A basic CircuitPython program to blink an LED is maybe six lines: import `board` and `digitalio`, set up a pin, and loop, toggling it on and off with a `time.sleep()` between. There's no boilerplate to memorize, no elaborate class structure to understand first. You can be blinking a light within minutes of finishing the install.

One thing worth knowing up front is that CircuitPython leans on libraries to talk to specific hardware, whether that's a sensor, a display, or a strip of LEDs. These live in a `lib/` directory that you drag onto _CIRCUITPY_ alongside your code, the same way you'd add any other file. Adafruit maintains a library bundle containing basically everything you'd need, and you only copy over the specific libraries your project actually uses, which keeps the board from filling up.

A note if you're on MacOS: older versions, specifically anything before Sonoma 14.4, have had real issues with file corruption when writing to CircuitPython boards. If that's you, it's worth updating before you get started, and even after updating, writes are a touch slower than you might expect. Let a save finish completely before disconnecting.

Beyond that, the learning curve is mostly just Python's learning curve, applied to something you can hold. There's excellent documentation available for troubleshooting anything unexpected, and an active community if you get stuck. The satisfaction of watching a physical thing respond to code you just wrote, saved to a drive like any other file, is hard to overstate. If you've been curious about hardware but assumed it required an entirely different skill set, this is genuinely as low a barrier as I've found.

---

### Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

#### Trial run, full · Aug 19, 12:34 AM

Style match 0.675 · Judge 4/10 · 478 words

> **Judge:** Both are friendly first-person tech writing, but the candidate leans on punchy fragments, em-dash asides, second-person zingers, and a polished essayistic arc, whereas Kattni writes in plainer, more evenly-weighted declarative sentences with step-by-step structure, headings/bullets, parenthetical clarifications, and blunt closers like "Done."

---

CircuitPython was the thing that finally got me past the intimidation of "embedded programming." I'd poked at Arduino sketches before, watched the compile-flash-crash cycle eat ten minutes for a one-line fix, and quietly decided microcontrollers weren't for me. Then I plugged in a board running CircuitPython, and it just... showed up. As a USB drive. No toolchain, no drivers to hunt down, no IDE to configure. Just a drive named after the board, with a `code.py` file sitting right there waiting to be edited.

That's really the whole pitch: CircuitPython removes the ceremony between "I have an idea" and "the board is doing the thing." You write Python, you save the file, and the board reruns it immediately. No compiling, no flashing, no waiting. If you've ever done web development and gotten used to hot-reloading, this is that feeling, except the output is an LED blinking or a servo twitching instead of a browser refreshing.

If you're starting from zero, here's the honest path. Pick a board — an Adafruit QT Py or a Feather is a fine, cheap first choice, and you don't need anything fancy. Head to circuitpython.org, grab the UF2 file for your specific board, and drag it onto the board while it's in bootloader mode (usually a double-tap of the reset button). That's the entire installation process. When it reboots, you'll see a drive called CIRCUITPY. Open `code.py` in any text editor, even Notepad, though I'd nudge you toward the Mu editor or the Web Serial workflow if you want a built-in serial console for debugging.

From there, the actual "hello world" is `import board`, `import digitalio`, and a few lines to blink the onboard LED. It's almost anticlimactic how fast you get there. But that speed is the point — it keeps the feedback loop tight enough that you stay curious instead of frustrated. You try something, it either works or throws a traceback right there in the serial console, and you adjust. No mysterious silent failures, no bricked boards from a bad flash.

The other thing worth knowing early: the CircuitPython libraries bundle is not optional, it's essential. Most sensors and displays need a driver library, and Adafruit maintains an enormous, well-documented set of them. Download the bundle matching your CircuitPython version, drop the relevant `.mpy` files into a `lib` folder on your board, and suddenly a $5 temperature sensor is three lines of code instead of a datasheet-reading afternoon.

Where people get stuck isn't the language, it's memory — these boards have real constraints, and CircuitPython's garbage collection can surprise you if you're allocating strings in a tight loop. But that's a problem for week two, not day one. Day one is just: plug it in, edit a file, watch an LED blink, and feel the thing I felt — that embedded programming was never the hard part. The tooling was.

---

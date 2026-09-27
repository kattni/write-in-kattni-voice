# Why good error messages are worth the effort

Register: opinion. 24 essays, grouped by condition, oldest first within each.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Run 1 | 0.769 / 3.0 | 0.615 / 3.0 | 0.736 / 3.0 |
| Run 2 | 0.681 / 4.0 | 0.733 / 4.0 | 0.635 / 3.0 |
| Run 3 (interrupted) | 0.772 / 4.0 (×3) | 0.715 / 4.3 (×3) | 0.648 / 3.0 (×3) |
| Run 4 | 0.743 / 4.0 (×3) | 0.684 / 4.0 (×3) | 0.662 / 3.0 (×3) |

## Skill

`/write-in-kattni-voice` plus the task. Skill on.

### Run 1 · Aug 19, 6:54 PM

Style match 0.769 · Judge 3/10 · Essayist tells 2/10 · 491 words

> **Judge:** The candidate is a polished op-ed with epigrammatic closers, fragment punchlines, and a lyrical callback ending, where the reference author writes plain, procedural, first-person reports that walk through what she did step by step and close with practical wrap-ups rather than rhetorical flourish.

---

481 words, close enough to "about 500." Here's the essay:

I spent an afternoon last month debugging a script that failed with "Error: 13." No context, no hint at what went wrong, just a number. I ended up grepping the library's source to find that 13 meant a permission error on a file it never named. That afternoon is the whole argument for why error messages matter: they're the difference between a five-minute fix and a lost afternoon.

Good error messages cost time upfront. You have to think about what actually broke, not just that something did, then write a sentence that says so in plain language. That's more work than raising a bare exception and moving on. It's worth it anyway, and here's why.

An error message is often the only communication a piece of software has with the person hitting the problem. They didn't ask for a conversation, but they're in one now, whether the message is useful or not. A message that just says "invalid input" hands the reader nothing to work with. A message that says "expected a number between 1 and 10, got 'blue'" hands them the fix.

I think about it the way I'd think about handing someone a map instead of pointing vaguely at a direction. (Vague pointing works fine if you already know the terrain. It's useless if you don't, and most people hitting your error don't.) The map costs more to draw. It saves the person walking it far more than that.

This matters most for beginners, and beginners are who I write for most of the time. A cryptic traceback doesn't just cost an experienced developer twenty minutes, it can convince a beginner the problem is them, not the message. I've watched people close a tutorial and give up on a whole project because the error they hit gave them nothing to go on, no line number, no hint at what to check, nothing they could act on. That's not a technical failure; that's a message failure, and it's one we hand the reader, not one they made themselves.

There's a real cost to doing this well, and I won't pretend otherwise. Writing good errors means catching the specific failure instead of a generic one, which means more code paths to think through and more cases to test. It's slower to write. It's slower to review. None of that goes away just because I believe in it.

But the cost is paid once, by the person who wrote the message. The cost of a bad error message is paid over and over, by everyone who hits it after. That math favors spending the extra hour.

The next time I'm tempted to raise a bare exception because the deadline's close and it's late, I try to remember Error: 13. Somebody's going to hit that message at 11pm with no idea what a permission error even is. I'd rather the message tell them.

---

### Run 2 · Aug 19, 10:49 PM

Style match 0.681 · Judge 4/10 · Essayist tells 3/10 · 486 words

> **Judge:** The candidate is a polished opinion essay with rhetorical balance, wry asides, and an epigrammatic parallel closing couplet, whereas Kattni writes plainly procedural, sequential first-person accounts ("Here is what I found," "Done.") without literary flourish.

---

470 words, close enough to the ~500 target. Outputting the final essay only, as requested.

---

I spent an embarrassing amount of time last year debugging a script that kept telling me "Error: invalid input." That was it. No line number, no hint about what "invalid" meant, no indication of which of the four inputs it was even talking about. I eventually found the problem: a trailing space in a config file. The error message could have told me that in one sentence. Instead it cost me forty minutes and a fair amount of muttering at my monitor.

That's the case for good error messages, really. Somebody, somewhere, is going to hit that error, and they're going to be less patient than I was when I wrote it, less familiar with the code than I am right now, and probably in a worse mood than either of us. The error message is the only thing standing between them and giving up.

I think about error messages the same way I think about documentation: as part of the actual work, not an afterthought bolted on once the "real" code is done. A function that does the right thing but fails silently, or fails with a message only its author could parse, isn't finished, even though it looks finished from the inside. The person who's going to be unhappy about that is someone else, later, not me, now.

Good error messages do a few specific things. They say what went wrong, in plain language, not a stack trace dumped on someone who didn't ask for one. They say where, specifically enough that the reader doesn't have to go hunting. And where it's possible, they say what to do about it. "Invalid input" tells the reader nothing. "Expected a number for `retries`, got the string `three`" tells them exactly what to fix and where to look.

I've written libraries where I genuinely could not remember, six months later, what one of my own error messages meant. That's a signal, not just an annoyance. If the person who wrote the code can't parse the error without opening the source, nobody else has a chance.

There's a cost to this, and I won't pretend there isn't. Writing a clear, specific error message takes longer than writing `raise Exception("bad")` and moving on. It means thinking through the failure case as carefully as the success case, sometimes more carefully, because the person hitting a failure is already frustrated and has less context than the person following the happy path. It's easy to talk yourself into spending that effort elsewhere, on the feature people will actually see working.

But the failure case is a thing people will actually see, probably more of them than anyone would like. Every error message I've written well has saved someone, often me six months later, a debugging session. Every one I've written badly has cost someone an afternoon.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:51 AM

Style match 0.777 · Judge 4/10 · Essayist tells 3/10 · 505 words

> **Judge:** The candidate is a polished opinion essay with crafted parallel triads, an evocative hypothetical ('11pm with a deadline'), a wry parenthetical aside, and a lyrical two-line kicker ending, whereas Kattni writes plainly sequential, procedural first-person reports that narrate what she actually did and close with practical wrap-ups rather than epigrams.

---

I've spent more hours than I'd like to admit staring at a stack trace that told me nothing. "Unexpected error." "Something went wrong." A null pointer exception three layers deep in a library I didn't write, with no line number, no context, nothing to tell me whether the problem was mine or the library's. Every one of those hours is the argument for why error messages matter.

Good error message writing takes real time. When I write one, I think about the actual person hitting the failure, not the sunny path I tested against: what they were doing right before this happened, what they already know, what they'll have to look up, and what single next step gets them unstuck. That's design work; it's not an afterthought you bolt on once the feature works.

I usually start with a smaller question than "what error should I write here." I ask myself what I'd want to see if this happened to me at 11pm with a deadline in the morning. That framing pushes me toward specifics: the value that was invalid, the file that couldn't be found, the field that was missing. A message that says "invalid input" is barely more useful than no message at all. Something like "expected a hex color starting with #, got 'blue'" tells the reader exactly what to fix, and where to look.

The return on this is bigger than the one person you're helping in the moment. Every good error message is a support ticket I never have to answer, a Slack message I never have to send, a GitHub issue that never gets filed because the fix was obvious from the terminal. I've worked on projects where a handful of clearer messages cut a whole category of "why isn't this working" questions down to almost nothing. That's hours back, for me and for whoever would've had to ask.

It also changes how people feel about the tool. A cryptic error tells the reader the problem is probably their fault and they're on their own to figure out why. A clear one tells them the opposite, that the software expects mistakes and is built to help them recover from one. That's a small thing to communicate in a single line of text, but it adds up over the life of a project. Newcomers notice it especially. The first error message someone hits in your tool is often the first real impression they get of whether it respects their time.

None of this is glamorous work. Nobody writes a blog post celebrating a well-worded exception (until now, I suppose). It's easy to leave a bare `throw new Error("failed")` in place and move on to the next feature, and I've done it plenty of times myself, usually while telling myself I'd come back and fix it later.

I mostly don't come back. That's the real cost of skipping it, not some hypothetical future user but the six-months-from-now version of me, hitting my own error with no memory of why it's there.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:52 AM

Style match 0.801 · Judge 4/10 · Essayist tells 3/10 · 463 words

> **Judge:** The candidate is a polished opinion essay with epigrammatic closers, fragment punchlines, rhetorical questions, and a stray meta-preamble, whereas Kattni writes plainly and procedurally in first person, narrating what she actually did in longer, hedged, comma-heavy sentences with concrete links, steps, and asides.

---

I'll draft directly from the skill's guidance since I don't have file read access here.

I spent an afternoon a few months back chasing a bug that turned out to be a config file in the wrong directory. The error message just said "Error: invalid configuration." Nothing about which file, which directory, or what "invalid" meant. I ended up adding print statements to a library I don't maintain, just to see what it thought a valid configuration looked like. It worked, eventually. But that was twenty minutes of someone else's time, spent because a developer somewhere decided a vague string was good enough.

Good error messages take more effort to write than bad ones. You have to think about who's reading them, what they already know, and what they need to do next. "Invalid configuration" skips the part that actually matters, which is where the problem is and what to do about it. "Config file not found at ./settings.json, did you mean ./config/settings.json?" takes longer to write; it also saves the next person an afternoon.

I think about error messages the same way I think about documentation: part of the interface, not an afterthought bolted onto it. (Anyone hitting a broken thing is reading your prose whether you wrote it carefully or not.) A stack trace with no context is still a message. It's just a badly written one.

There's a pattern I reach for now: state what happened, state where, state what to do next. Not all three are always possible, but even two out of three beats "something went wrong." "Something went wrong" tells the reader nothing except that they should feel bad about it.

The hard part is that writing a good error message means sitting with the failure case for a minute, right after you've caught the exception and just want to move on to the next thing. Writing the code that works is more satisfying than writing the code that explains why it didn't. I get the pull. But the failure path is the moment your software actually talks to a stressed, confused person trying to get something done. That's a strange place to phone it in.

It pays me back directly, too. Six months from now, debugging my own code at 11pm, a message that says exactly what failed and where is the difference between a five-minute fix and a lost evening. Writing for a hypothetical future user turns out to be writing for future me, most of the time.

None of this takes much cleverness. It mostly takes slowing down for a few extra minutes per error path, while I still remember the context I'm about to throw away. A few minutes now is small. Reconstructing that context from nothing, later, from the outside, is not.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:53 AM

Style match 0.739 · Judge 4/10 · Essayist tells 3/10 · 468 words

> **Judge:** The candidate adopts a polished reflective-essay voice — short punchy fragments, a rhetorical question to the reader, and an aphoristic one-line closer — where Kattni writes long, plain, procedural first-person prose that reports what she did and what happened, with parenthetical asides and concrete step-by-step detail rather than crafted rhythm.

---

I spent a long time debugging boards that just said "Error." No line number, no hint, nothing. I'd stare at the REPL (the interactive prompt you talk to the board through), reflash the code, and try again, hoping the second run would tell me more than the first. Usually it didn't.

That kind of silence teaches you something about error messages before you ever write one yourself. A vague error doesn't just fail to help. It costs the person reading it time they didn't need to lose.

Good error messages are different. They tell you what went wrong, where, and often what to do about it. CircuitPython's tracebacks got a lot better over the years I worked with them, and the difference showed up immediately in the support channels. A message like "IndexError: list index out of range" on line 14 sends someone straight to their own code. "Error" sends them to a forum post, or to me.

Writing a good error message takes more effort than writing a bad one. You have to think about who's going to read it and what they'll already know at that moment. Are they a beginner who just typed their first line of Python, or someone who's been debugging embedded hardware for a decade? You usually don't know, so you write for the beginner and trust the expert to skim past what they don't need. That's the same instinct that goes into a good tutorial: meet the reader where they are, not where you assume they are.

The effort pays off in a specific way. Every clear error message is a support question that never gets asked, or one the error answers on its own instead of a person having to. I watched this happen directly. A confusing message about a missing library turned into dozens of nearly identical forum threads, all with the same root cause and the same fix. Once the message named the missing library by name (just the name, nothing clever), the threads mostly stopped.

There's a trust piece to it too. A tool that tells you clearly when you've made a mistake, and how to fix it, feels different to use than one that just breaks. It feels like it's on your side. That matters most for beginners, who are already deciding whether this whole coding thing is for them. A cryptic error at exactly the wrong moment can end that decision before it really starts.

None of this is glamorous work. Writing a clear exception message doesn't ship a feature or fix a hardware bug. It's the kind of thing that's easy to skip when you're moving fast, and easy to regret skipping later, once the same question shows up in your inbox for the fifth time.

I'd rather spend the extra ten minutes now.

---

### Run 4, essay 1 · Aug 20, 5:26 PM

Style match 0.695 · Judge 4/10 · Essayist tells 3/10 · 522 words

> **Judge:** The candidate is a polished opinion essay — extended mechanic analogy, punchy fragments ("It just is."), an emotive rhetorical flourish about closing the laptop, and a thematic closing line — whereas Kattni writes flat, procedural, first-person reportage with plain enumeration, hedges like "That said" and "Done.", and no crafted punchlines.

---

I spent an afternoon last year chasing a bug that turned out to be a single missing comma in a config file. The error I got back was `SyntaxError: invalid syntax`, pointing at a line that had nothing wrong with it. The actual problem was two lines up. I only found it by commenting out half the file and bisecting my way to the culprit, which is a ridiculous way to spend an afternoon over one character.

Compare that to an error I hit more recently in a project that actually cared about its error messages: `Expected a comma after 'temperature' on line 12, but found '"humidity"'.` I fixed it in about ten seconds. Same category of mistake, wildly different amount of my life lost to it.

That gap is the whole argument for why error messages are worth the effort. A bad error message doesn't just fail to help, it actively costs the person reading it time, and often confidence. When you don't know a codebase well and the tool spits out something cryptic, it's easy to conclude the problem is you, that you're missing some obvious context everyone else has. Usually you're not. Usually the message just wasn't written for a human being to read.

A good error message does a few specific things. It says what went wrong, in words that don't require decoding a stack trace to understand. It says where, specifically, not "somewhere in this 400 line file." And when it can, it says what to do about it. "Expected a comma" tells me the shape of the fix before I've even looked at the code.

I think of it like a mechanic telling you what's wrong with your car. "The engine's making a noise" is technically true and useless. "Your serpentine belt is worn and needs replacing" gets you to a fix. The second one costs the mechanic more to say. They have to actually diagnose the thing instead of shrugging at the symptom. That's the effort part. Writing a message like `Expected a comma after 'temperature'` means the code has to track where it was in parsing, what it expected next, and phrase that in plain language instead of just bailing out with a generic exception. It's more work than `raise SyntaxError`. It just is.

But that work only has to happen once, by the person who wrote the parser, and it pays out every single time someone else hits that error afterward. I've written tutorials for people who are brand new to programming, and I can tell you exactly how many of them will assume a cryptic error means they've broken something fundamental, when really they forgot a closing bracket. A clear message is the difference between them fixing it and moving on, or closing the laptop and deciding this isn't for them.

So when I'm writing code now, especially anything meant for other people to build on, I try to write the error message before I even finish the feature. Not as a nice-to-have tacked on at the end, but as one of the things I check before I call the feature finished.

---

### Run 4, essay 2 · Aug 20, 5:26 PM

Style match 0.750 · Judge 4/10 · Essayist tells 3/10 · 497 words

> **Judge:** The candidate is a polished opinion essay with aphoristic framing, a rhetorical question-and-answer structure, punchy short sentences, and a thematic closing callback, whereas Kattni writes plainly sequential, procedural, first-person accounts of what she did with concrete step-by-step detail and matter-of-fact wrap-ups.

---

Bad error messages cost more than they save. I've lost entire afternoons to a stack trace that said "unexpected token" with no line number, or a device that just blinked red and expected me to guess why. Every one of those afternoons was time I didn't spend building anything. Good error messages are one of the cheapest investments you can make in a project, and most of us skip them anyway.

Part of the problem is timing. You write the error message when the bug is freshest in your mind, when you already know exactly what went wrong and why. That's precisely the moment you're least motivated to explain it to a stranger, because you're not a stranger to it. You know. So you write `raise ValueError("invalid input")` and move on. Six months later, someone (possibly you) hits that error with no idea what "invalid" means in this context, what a valid input would have looked like, or which of the four arguments even caused it.

I try to write error messages as if I'm handing the code to someone who has never seen it before, because eventually I will be that someone. A good error message answers three questions: what happened, why it happened, and what to do about it. "Invalid input" answers none of them. "Expected a hex color like #FF0000, got 'red'" answers the first two and points at the fix.

This matters even more with hardware and physical computing, which is where I spend a lot of my time. When a board just blinks an LED or goes silent, a beginner has no idea if the problem is their code, their wiring, or a bad connection. They can't inspect a stack trace on a breadboard. A clear message printed to the serial console, something as simple as "Could not find I2C device at address 0x3C, check your wiring," turns a dead end into a next step. Without it, that's often where someone gives up on the whole project, not just the bug.

There's a cost to writing error messages this way. It takes longer than the one-liner. You have to actually think about the failure modes, not just the happy path, and you have to write them in plain language instead of reusing whatever the underlying library handed you. That's real effort, and I won't pretend it isn't.

But I've started thinking of error messages as documentation that only shows up exactly when it's needed. Nobody reads your docs at 2am while debugging. They read the error. If the error is good, it does the job the docs were supposed to do, at the one moment someone is actually paying attention.

I still write bad ones sometimes. I'll catch myself writing "something went wrong" and have to stop and ask what, actually, went wrong. It's a habit, not a rule I always follow. But every time I take the extra two minutes, I'm saving someone, probably future me, from a much longer afternoon.

---

### Run 4, essay 3 · Aug 20, 5:27 PM

Style match 0.784 · Judge 4/10 · Essayist tells 3/10 · 495 words

> **Judge:** The candidate is a polished opinion essay with rhetorical flourishes, fragments ('Great, thanks.'), em-dash-free but epigrammatic lines and a thematic closing reversal, whereas Kattni writes plainly and procedurally, narrating what she actually did in long, evenly-built sentences with heavy parenthetical clarifications, links, and headings.

---

I've spent a lot of time staring at tracebacks that told me something broke without telling me what. "IndexError: list index out of range." Great, thanks. Which list? Which index? I've written that exact unhelpful message myself, more than once, because it's the one Python hands you for free, and writing a better one takes an extra ten minutes I didn't think I had.

Those ten minutes are the whole argument. A good error message is the fastest documentation you will ever write, because it shows up exactly when the reader needs it, right where they're stuck. Nobody reads an error message for fun. They read it because something already went wrong and they're trying to get back to what they were doing. That's a captive, motivated audience, and most of us waste it on a bare stack trace.

I think about it in terms of who's on the other end. Sometimes it's a future version of me, six months from now, who has completely forgotten why this function checks for a token before it checks for anything else. Sometimes it's someone brand new to the project, running the example from the README for the first time, hitting a wall on step one because their API key isn't set. If the message just says "unauthorized," that person doesn't know whether they typo'd a variable name, used the wrong environment file, or found a real bug in my code. If it says "no API key found in environment variable FOO_API_KEY, check your .env file," they're unblocked in the time it took to read it.

That gap, between "something is wrong" and "here is what is wrong and here is what to do about it," is where people either keep going or give up; I've watched people give up on projects over exactly this. Not because the underlying tool was bad, but because the failure mode was silent or cryptic, and they had no way to tell whether the problem was theirs or the software's.

Writing a good error message also forces a kind of honesty about your own code. You have to name the failure case instead of letting it fall through to a generic exception. You have to decide what the caller could have done differently, which means understanding your own function well enough to explain it to someone who's never seen it (this is harder than it sounds, especially in code you wrote in a hurry). A few times I've gone to write the message and realized the error shouldn't be possible in the first place, and fixed the real bug instead of just labeling it nicely.

None of this is free. It's extra code, extra strings to write and maintain, extra thought about edge cases you'd rather not think about. But that cost gets paid once, by me, at a time I chose. Everyone who hits that error after me pays it too, at a time they didn't choose, usually while already frustrated.

---

## Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

### Run 1 · Aug 19, 6:55 PM

Style match 0.615 · Judge 3/10 · Essayist tells 2/10 · 527 words

> **Judge:** The candidate is a polished opinion essay with em-dash asides, epigrammatic flourishes ("It is, functionally, a shrug", "a small kindness, extended to a stranger you'll never meet"), and a lyrical closing line, whereas Kattni writes plainly and procedurally in first person about what she actually did and what happened, without rhetorical polish.

---

Good error messages are worth the effort because they are, in a very real sense, a form of documentation, and documentation is only useful if someone can actually use it in the moment they need it. When something breaks, the error message is the first thing a person sees, and it is very often the only thing standing between them figuring it out themselves and them giving up, or worse, filing a support ticket that someone else now has to spend their afternoon untangling.

I think about this a lot, because I spend a fair amount of my time writing tutorials and documentation, and a poorly worded error message undoes a lot of the careful explaining I did three steps earlier. You can write the clearest possible walkthrough, and it won't matter if the tool the reader is using responds to a mistake with `Error: invalid input` and nothing else. That message tells you something went wrong. It does not tell you what, where, or how to fix it. It is, functionally, a shrug.

A good error message does at least three things. It tells you what happened, in language that assumes you are a person and not the system itself. It tells you where, specifically, so you're not hunting through five hundred lines of code for the one that misbehaved. And, when it's possible, it tells you what to do about it. That third one is the part people skip most often, and it's the part that turns an error from a dead end into a next step. "Invalid input" is a dead end. "Expected a language code directory in `docs/locales/`, but none was found — create the directory before running this command" is a next step. The second one costs maybe two more sentences to write, and it saves the reader an hour of guessing, or worse, of reading the source code to figure out what you meant.

There's a selfish reason to do this too, if the altruistic one isn't motivating enough on its own: writing a good error message forces you to actually understand your own failure modes. You can't write "the language code directory doesn't exist" as an error unless you've already thought through why someone would hit that state, and what they were probably trying to do when they got there. That thinking has a way of catching bugs before anyone else does, simply because you had to sit with the failure case instead of skating past it with a generic exception.

I'll admit this is not glamorous work. Nobody opens a changelog excited to read that error messages got clearer. It doesn't move like a new feature does. But every person who hits that message later, at some inconvenient hour, trying to get something working, benefits from the two extra minutes you spent being specific instead of vague. Multiply that by however many people will ever run your code, and the math is not close. A clear error message is a small kindness, extended to a stranger you'll never meet, at the exact moment they're most frustrated with you. That seems like a pretty good use of effort to me.

---

### Run 2 · Aug 19, 10:50 PM

Style match 0.733 · Judge 4/10 · Essayist tells 3/10 · 557 words

> **Judge:** The candidate is a polished opinion essay with rhetorical flourishes, italic emphasis for effect, aphoristic definitions ('it's a shrug'), and a lyrical thematic closing, whereas Kattni writes plainly and procedurally, reporting what she did and what happened with concrete steps and matter-of-fact wrap-ups.

---

Why Good Error Messages Are Worth The Effort

I spent a chunk of an afternoon last month staring at a build failure that said, essentially, "something went wrong." Not the exact text, but close enough that it might as well have been. No file, no line, no hint at which of the forty things I'd just changed was the culprit. I ended up bisecting my own commit by hand, reverting chunks of it until the error disappeared, at which point I knew *what* broke it but still not *why*. That's an hour of my life I'm not getting back, and it's an hour that a single well-placed sentence in an error message could have saved.

This is the thing about error messages: they are, for a huge percentage of your users, the only writing you do that they will actually read at the moment they need it most. Nobody reads your documentation while things are working. They read your error message while they are stuck, mildly panicked, and trying to figure out whether the problem is their fault, your fault, or a sign that they should give up entirely. A good error message is a tiny act of empathy dropped into someone's worst moment with your tool.

A good error message does a few specific things. It tells you what happened, in plain language, not a stack trace dumped as though the reader has memorized your codebase. It tells you where, specifically enough that you don't have to go hunting. And ideally, it tells you what to do about it. "Invalid configuration" is not an error message, it's a shrug. "Missing required field `docs_dir` in `mkdocs.en.yml`" is an error message. It respects the reader's time.

I ran into this directly while building the translation tooling for MkDocs. There's a step where the tool checks whether a language code directory already exists before it'll let you generate PO files for it, specifically to avoid silently creating a junk directory from a typo. Early on, that check just failed. No explanation. Anyone hitting it for the first time would have had no idea the fix was "go create the directory yourself first." Once I wrote the actual explanation into the failure, that whole class of confusion disappeared. It cost me maybe fifteen minutes to write. It has probably saved other people hours, collectively, in ways I'll never see.

That asymmetry is the whole argument, really. The person writing the error message pays a small, one-time cost: a few extra minutes to think about what actually went wrong and say it clearly. Every single person who hits that error afterward pays whichever cost you left them. If you wrote nothing useful, they pay in confusion, in searching, in filing an issue you'll have to answer anyway. Multiply that by however many people run your code, and "just add a sentence" turns out to be one of the highest-leverage things you can do with your time.

I don't think good error messages are a nice-to-have you add once everything else is done. I think they're part of the actual feature. The code that runs correctly is only half the job; the code that fails clearly, kindly, and usefully is the other half, and it's the half people remember when they decide whether they trust your project enough to keep using it.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:53 AM

Style match 0.717 · Judge 4/10 · Essayist tells 3/10 · 549 words

> **Judge:** The candidate borrows Kattni's subject matter and some first-person framing, but writes as a polished opinion essayist — thesis-driven abstraction, rhetorical question stacks, epigrammatic lines like "it's most of the product" and the closing "For a lot of people, the error message is the only documentation they'll ever read" — rather than her plain, sequential, report-what-I-did-and-what-happened voice with its concrete steps, parenthetical asides, and understated wrap-ups.

---

Good Error Messages Are Worth the Effort

I spend a fair amount of my time writing tools that other people, often less experienced than me, are going to run into trouble with. Translation tooling, badge firmware, documentation build scripts. Every one of these has a moment where something goes wrong that I didn't anticipate, and the only thing standing between the person running it and a productive next step is whatever text I decided to print when I wrote the failure condition. I've come to believe that text is not a minor detail. It's most of the product.

Here's the thing about error messages: they show up exactly at the moment someone is least equipped to deal with ambiguity. Something has already gone wrong. The person is confused, maybe frustrated, maybe on a deadline. This is not the time to hand them a stack trace and a vague noun. "Invalid configuration" tells someone nothing they didn't already suspect. Which configuration? Invalid how? What do they do now? A message like that isn't documentation, it's a shrug.

When I built MkDocs PO I18n, I made a deliberate choice around the language-code directory check: if the directory doesn't exist, the tool fails outright with an error, rather than quietly creating one. I could have made it more "forgiving" and just generated the directory on the fly. But that would have meant a typo in a language code silently produces a new, incorrect directory instead of telling you what happened. The error there isn't an inconvenience I'm imposing on the user. It's the fastest path back to correct behavior, because it tells you precisely what condition triggered it and lets you fix the actual cause instead of chasing a symptom three steps downstream.

Good error messages also do something less obvious: they represent respect for the person on the other end. Writing one well requires you to imagine, concretely, what someone will be thinking when they read it. Not "what did the code do" but "what does this person need to know to move forward." That's a genuine act of empathy, and it takes real effort, because your own mental model of the system isn't the reader's. You know why the config file has to have a certain key. They don't, yet. A message that just names the internal state without translating it into something actionable is really only useful to you, the author, not to the person it's ostensibly written for.

I think about this the same way I think about code review feedback. "No news is good news" doesn't work for humans receiving reviews, and it doesn't work for humans receiving errors either. Silence, or a cryptic half-sentence, leaves someone guessing whether they did something wrong, whether the tool is broken, or whether they're missing some context nobody bothered to write down. A clear message, on the other hand, closes that gap immediately. It says: here's what happened, here's likely why, here's what to try.

None of this is complicated to do. It just requires slowing down at the exact moment you're most tempted to rush, right after you've gotten the happy path working and the failure case feels like an afterthought. It isn't one. For a lot of people, the error message is the only documentation they'll ever read.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:54 AM

Style match 0.686 · Judge 4/10 · Essayist tells 3/10 · 529 words

> **Judge:** The candidate borrows the author's domain and first-person practitioner framing but writes in a polished op-ed register — aphoristic closer ("worth every one of them"), sentence fragments and punchlines ("congratulations, you've learned nothing"), rhetorical flourishes, and italicized emphasis on abstractions — where Kattni's samples plod deliberately through concrete steps, sequences, and plain declaratives with "Done." style bluntness rather than rhetorical polish.

---

Good error messages are one of those things you don't think about until you're on the receiving end of a bad one. You've hit a wall, something has gone wrong, and the only thing standing between you and a fix is a single line of text. If that line says `Error: undefined`, congratulations, you've learned nothing. You now have two problems instead of one.

I think about this a lot because I spend a fair amount of my time writing documentation and tutorials, and a bad error message is, functionally, a tiny piece of documentation that failed at its one job. Someone hit a wall, they looked for help, and the software shrugged at them. That shrug has a cost. It's not abstract, either: it's the minutes, or hours, someone spends re-reading their own code line by line, or pasting a cryptic string into a search engine and hoping someone else has already suffered through the same thing and posted a fix.

The thing I keep coming back to is that a good error message is doing two jobs at once. It has to tell you what went wrong, and it has to tell you what to do about it. Most bad error messages only manage the first, and even then, only barely. "Invalid input" is technically true and completely useless. It doesn't say which input, why it's invalid, or what a valid one looks like. Compare that to something like "Expected a language code directory to exist before generating PO files; create `docs/locales/fr/LC_MESSAGES/` first." That second version costs the developer maybe thirty extra seconds to write. It can save the person on the other end an entire afternoon.

I ran into this constantly while building the MkDocs PO I18n tool. There were a handful of places where I knew, going in, that people were going to trip over the same thing I tripped over myself, repeatedly, while developing it. The language code directory issue is a great example. If you don't create it first, the tool has no way to distinguish "this is a typo" from "this is a brand-new language nobody's set up yet." I could have let that fail silently, or with something generic. Instead, I made sure it failed loudly and specifically, because I already knew, from personal, mildly infuriating experience, exactly what someone would need to hear in that moment to get unstuck.

There's also a trust component to this that I don't think gets talked about enough. When a tool gives you a clear, specific error message, it reads as though the person who built it anticipated you'd be here, struggling with this exact problem, and left you a note. That's a genuinely different feeling than being met with a stack trace and a shrug. It signals that someone cared enough to think about the failure cases, not just the happy path. And that, more than almost anything else, is what makes me trust a piece of software, or a library, or a tutorial, enough to keep using it.

Writing a good error message takes maybe five extra minutes over writing a bad one. It is, without question, worth every one of them.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:55 AM

Style match 0.743 · Judge 5/10 · Essayist tells 4/10 · 529 words

> **Judge:** The candidate is a polished opinion essay with aphoristic framing, a punchy closing line, and abstract reflection on trust and empathy, whereas Kattni writes as a plain practitioner narrating concrete steps and outcomes with heavy use of examples, lists, and matter-of-fact reporting.

---

Good error messages are the kind of thing you don't notice until they're gone, and then you notice immediately. You're staring at a stack trace, or a red banner that just says "Something went wrong," and you have no idea what happened, why it happened, or what you're supposed to do about it. I've spent enough hours squinting at exactly this kind of message to have strong feelings about it.

A good error message does three things: it tells you what happened, it tells you why, and, ideally, it tells you what to do next. That third part is the one people skip most often, and it's the one that matters most. "Invalid input" is technically true and almost entirely useless. "Expected a language code directory to exist in `/docs/locales/` before generating PO files" is the kind of message that saves someone an hour of guessing. I ran into a version of this myself while building the translation tooling I wrote about a few posts back: if you feed it a language code that doesn't have a corresponding directory already created, it fails. That's intentional, so a typo doesn't silently create a garbage directory tree. But the value of that decision lives entirely in whether the error message explains it, versus just refusing to run and leaving you to reverse-engineer the requirement from source.

Writing these messages takes real effort, and it's effort that's easy to skip, because from the developer's chair, the error already makes sense. You know why the thing failed; you were just there. The gap is imagining the person on the other end, who has none of that context, who may not even know the internals well enough to guess. This is the same gap I think about when writing tutorials: what's obvious to me because I've been staring at this code for weeks is not obvious to someone encountering it for the first time. A good error message is a tiny piece of documentation that shows up exactly when someone needs it most, which is also usually the moment they're most frustrated and least willing to go dig through docs to find an explanation.

There's a trust dimension here too. When software fails with a clear, specific message, I relax a little, because it tells me the person who built this thought about failure cases, not just the happy path. When it fails with something cryptic, or worse, with nothing at all, I start to wonder what else wasn't considered. That impression sticks. I'm far more forgiving of a tool that breaks and tells me plainly what broke than one that works fine until it doesn't, and then leaves me guessing.

None of this requires much: a sentence describing what was expected, a sentence describing what was found, and where possible, a nudge toward the fix. It's a small investment relative to building the feature itself. But it's the difference between someone fixing their own problem in thirty seconds and someone filing an issue, or worse, quietly giving up on your project entirely. Given the choice, I'd rather spend the extra ten minutes now than answer the same confused question five separate times later.

---

### Run 4, essay 1 · Aug 20, 5:28 PM

Style match 0.645 · Judge 4/10 · Essayist tells 3/10 · 521 words

> **Judge:** The candidate borrows Kattni's subject matter and first-person framing but writes as a polished opinion essayist — thesis-driven paragraphs, aphorisms ("A good error message is a form of respect"), em-dash flourishes, sentence fragments for effect, and a lyrical closing about silence — where the reference author plainly narrates steps, decisions, and outcomes with concrete detail and unadorned wrap-ups.

---

Why Good Error Messages Are Worth the Effort

I've spent enough time this year buried in someone else's toolchain — CircuitPython, Lektor, the Translate Toolkit, Read the Docs' build pipeline — to have developed strong opinions about what happens the moment something goes wrong. It turns out the quality of an error message is one of the clearest signals of how much a project's maintainers care about the people using it.

Here's the thing about a bad error message: it doesn't just fail to help you, it actively costs you time you didn't budget for. A stack trace with no context, a bare "invalid input", a silent failure that leaves you staring at a blank page wondering if the build even ran. Every one of these sends you off on a detour, searching GitHub issues, reading source code you never intended to read, pinging a friend who happens to know the codebase better than the documentation does. I did exactly this while building MkDocs PO I18n. The language-code check in my own tool originally just failed with no explanation if the `locales` directory for that language didn't already exist. I knew why, because I wrote it. Nobody else would have had any idea. So I made a decision early on: if the tool is going to refuse to do something, it needs to say what it refused and why, in the moment it refuses it.

A good error message is a form of respect. It assumes the person on the other end is capable and just missing one piece of information, and it hands them that piece directly instead of making them go earn it. "Create new language code directories in locales before attempting to create PO files" is not a glamorous sentence, but it is the sentence that saves someone forty-five minutes of confusion, because it tells them exactly what state the tool expects before it acts, and exactly what to do if that state isn't there yet.

This matters more, not less, the further a tool travels from the person who built it. I know my own assumptions. I know which directory needs to exist before which command runs, because I wrote the order of operations myself. Someone downloading the tool six months from now, with none of that context, is relying entirely on what the tool tells them at the moment things break. If the message is vague, they inherit my assumptions with none of my knowledge. If the message is specific, they get to skip the archaeology entirely.

There's also a compounding effect. Every clear error message you write is one fewer support question, one fewer confused issue filed, one fewer person who quietly gives up and walks away from your project without ever telling you why. You don't see the cost of a bad error message, because it shows up as silence — someone closing the tab instead of opening an issue. Good error messages are cheap to write, relative to what they prevent. A sentence of context now is nearly always less expensive than the debugging session it replaces later, for someone who isn't you.

---

### Run 4, essay 2 · Aug 20, 5:29 PM

Style match 0.667 · Judge 4/10 · Essayist tells 3/10 · 547 words

> **Judge:** The candidate is a polished opinion essay with balanced abstractions, em-dash-free but epigrammatic phrasing ("a tutorial is, in a sense, just a very long, very patient error message") and a thesis-style closing aphorism, whereas Kattni writes plain, chronological, first-person practitioner reports with concrete steps, asides in parentheses, and matter-of-fact wrap-ups.

---

Error messages are one of those small design decisions that quietly determine whether someone has a good day or a bad one. I think about them more than most people probably expect, because I spend a lot of my time writing documentation and tutorials, and a tutorial is, in a sense, just a very long, very patient error message. If a reader hits a wall and the tool in front of them says something like `Traceback (most recent call last): SyntaxError`, with no further explanation, they are stuck. If it instead says something like "you're missing a closing parenthesis on line 12," they can fix it and move on with their day. The difference between those two experiences is not a small one, even though the amount of code required to produce either message is roughly the same.

I ran into this directly while building MkDocs PO I18n. Part of the tool checks whether a given language code directory already exists before it will generate PO files for it, and I made a deliberate choice to have it fail loudly and specifically if the directory isn't there, rather than silently creating something in the wrong place. It would have been just as easy to let it fail with some generic Python exception three layers down in the Translate Toolkit internals, and technically, the user would eventually figure out what went wrong. But "eventually" is doing a lot of work in that sentence. A clear failure at the point where the actual problem occurred saves someone from having to read a stack trace to reverse-engineer what I already knew when I wrote the check.

This matters more, not less, as your audience gets less experienced. A seasoned developer can often infer what a cryptic error is trying to tell them, because they've seen enough of them to pattern-match. A beginner, or someone who has never used Git or the command line before, has no such pattern library to draw from. When I wrote the Badger2040 badge tutorial, I was acutely aware that some readers had genuinely never done anything like this. Every step where something could go wrong quietly, wrong cables, wrong button sequence, needed to be called out explicitly, because a beginner has no way to tell the difference between "this didn't work because I made a small mistake" and "this didn't work because the hardware is broken." A good error message, or a good warning ahead of the failure, closes that gap.

There's also a trust element to this that's easy to underestimate. Software that fails with vague or unhelpful messages teaches its users, over time, that errors are not worth reading closely, since they rarely contain anything actionable. Once someone learns that lesson, they stop reading your error messages at all, even the good ones, and that's a much harder habit to undo than it is to prevent.

Writing a good error message takes a bit more effort than writing a bad one. You have to actually sit with the failure case, decide what the person on the other end needs to know, and say it plainly. But that effort is spent once, by you, and it is saved, repeatedly, by everyone who hits that wall after you. That trade is almost always worth taking.

---

### Run 4, essay 3 · Aug 20, 5:29 PM

Style match 0.740 · Judge 4/10 · Essayist tells 3/10 · 549 words

> **Judge:** The candidate borrows Kattni's first-person practitioner framing and some real project detail, but delivers it in a polished op-ed voice — punchy fragments, an aphoristic "That ratio is the whole argument," a second-person imperative closer, and rhythmic escalating clauses — where the reference author writes flatter, more procedural, comma-heavy sentences that report steps and outcomes rather than build to rhetorical payoffs.

---

Why Good Error Messages Are Worth the Effort

A while back I was chasing a build failure that told me, in its entirety, "Something went wrong." Nothing else. No file, no line, no hint of which of the forty things that could have gone wrong actually did. I spent close to an hour adding print statements one at a time until I found it: a config file expected a trailing comma that wasn't there. The fix took ten seconds. Finding it took an hour. That ratio is the whole argument.

An error message is the one place in your program where you get to talk directly to a person in the middle of a bad moment. They didn't open your code because things were going well. They're frustrated, they're in a hurry, and they're about to form an opinion of your project based entirely on what you say to them right now. "Something went wrong" tells them nothing and asks them to trust you anyway. A good error message treats that moment with the respect it deserves.

What makes an error message good isn't complicated, but it does take actual thought, which is why so many of them skip it. Say what happened. Say where. And if you can, say what to do about it. "Missing trailing comma on line 14 of config.yml" would have saved me the hour. It costs the developer maybe two extra minutes to write, once, and it saves every single person who hits that error afterward from repeating my afternoon. That's not a good trade, it's an absurdly good trade, and it's the kind that's easy to skip because the cost is paid by you now and the benefit is collected by someone else, later, who you'll never hear thank you.

I ran into a version of this from the other direction while writing MkDocs PO I18n. I built in a check that fails outright if you try to generate PO files for a language code whose directory doesn't already exist, specifically to avoid quietly creating a wrong directory from a typo and leaving you to discover it three steps later when something downstream breaks in a way that has nothing obviously to do with the actual cause. The failure has to happen immediately, and it has to say why, or the whole safeguard is pointless. An error that fires in the right place but explains nothing is barely better than no error at all; you've just moved the confusion instead of removing it.

There's a documentation instinct buried in this too. Every error message you write is a tiny piece of documentation that only appears exactly when someone needs it, which makes it more valuable than almost anything sitting in a guide somewhere, because nobody has to go looking for it. It's the same reason I keep circling back to positive, specific feedback over "no news is good news": vague signals leave people to fill in the gaps themselves, usually with something worse than the truth, and specific ones let them actually fix the thing and move on with their day.

None of this is hard. It just requires remembering, in the moment you're writing the failure path, that a real person is going to read it while annoyed. Write to that person.

---

## Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

### Run 1 · Aug 19, 6:56 PM

Style match 0.736 · Judge 3/10 · Essayist tells 2/10 · 539 words

> **Judge:** The candidate is a polished opinion essay full of em-dash rhetoric, aphoristic turns ("It's the software equivalent of a shrug"), rhetorical questions, and a punchy closing zinger, whereas Kattni writes plainly and procedurally in first person about what she actually did, with plodding declaratives, parentheticals, and mundane step-by-step reporting rather than persuasion.

---

Every developer has hit the wall of `undefined is not a function` at 2am and felt something between rage and despair. That message tells you nothing about what broke, why, or what to do next. It's the software equivalent of a shrug. And yet we ship messages like this constantly, because writing a good one takes an extra five minutes we've convinced ourselves we don't have.

Here's the thing: those five minutes are some of the highest-leverage minutes you'll spend as a developer.

An error message is a support ticket you get to answer before it's ever filed. Every vague message you ship becomes someone else's investigation — a support engineer digging through logs, a teammate pinging you on Slack, a user quietly giving up and closing the tab. You're not avoiding the work of explaining what went wrong; you're just deciding who does it, and when. Do it now, in the code, while you have full context, or do it later, exhausted, reconstructing that same context from a stack trace and a vague memory of what this function even does.

Good error messages also force a kind of honesty about your code. When I write `raise ValueError("count must be positive")` instead of letting an assertion fail silently three functions later, I'm actually confronting the assumption I baked into the function. Writing the message means naming the invariant. If you can't write a clear sentence about what went wrong, that's often a sign you don't fully understand your own failure modes yet — which is worth knowing before it ships, not after.

There's a technical-writing instinct that applies directly here: write for the reader who has the least context, not the one who has the most. You know exactly what your function does and why it might fail. The person hitting the error — future you, a teammate, a user — doesn't. A message like `Error: invalid input` assumes a reader who already knows what "invalid" means in this context. A message like `Config value "timeout" must be a positive integer, got -5` assumes nothing. It hands the reader exactly what they need to fix the problem without opening the source.

The best error messages do three things: say what happened, say why (or where), and say what to do about it. Not every message needs all three — a quick internal assertion might just need the first — but the ones users actually see should aim for all three every time. "Failed to connect to database" is a status update. "Failed to connect to database at localhost:5432 — is Postgres running? Check DATABASE_URL in your .env file" is an actual answer.

I think of error messages as documentation that only appears exactly when it's needed, to exactly the person who needs it, at exactly the moment they're most receptive to reading it. That's an incredible amount of leverage for a single string. Most documentation gets skimmed or ignored; an error message gets read every time, because the reader has no choice.

So when you're tempted to throw a generic exception and move on, remember: you're not skipping the writing. You're just handing it to someone with less context, less time, and less patience than you have right now.

---

### Run 2 · Aug 19, 10:50 PM

Style match 0.635 · Judge 3/10 · Essayist tells 2/10 · 545 words

> **Judge:** The candidate is a polished opinion essay with em-dash-heavy rhetorical flourishes, second-person exhortation, and aphoristic closers ("The error path is real work."), whereas Kattni writes plainly and concretely in the first person about what she actually did, with straightforward declaratives, procedural lists, and no epigrammatic endings.

---

Good error messages are worth the effort because they are, in practice, the only documentation most people will ever read at the exact moment they need it. You can write a beautiful getting-started guide and a thorough API reference, and still watch a user hit a wall, ignore both, and paste your stack trace into a search bar instead. The error message is what's actually in front of them. If it's useless, so is everything else you wrote.

I think about error messages the same way I think about a support ticket I'm trying to prevent. Every vague error — `Invalid input`, `Something went wrong`, a bare `undefined is not a function` — is a ticket someone will file, a Slack message someone will send, a GitHub issue someone will open at 11pm because your API rejected their request and gave them nothing to work with. The five minutes it takes you to write a specific message is traded against the twenty minutes someone else spends guessing, plus the context-switch cost of them asking for help, plus your cost of answering. That math almost never favors the vague message.

A good error message does three things, and it's worth naming them because it makes the writing tractable instead of vague. It says what happened, specifically — not "invalid config" but "config.yaml: missing required field `timeout` on line 12." It says why it matters, if that's not obvious — a missing timeout isn't a typo, it's a value the system genuinely can't proceed without. And it says what to do next — set a value, check the docs, run a specific command. Miss the third part and you've written a diagnosis with no treatment. Users don't want to understand your system's internals; they want to get unstuck.

There's a craft to this that's easy to underrate because it looks like a small thing. Writing "expected string, got number" is not the same skill as writing prose, but it draws on the same instinct: know your reader, and don't make them do work you could have done for you. The person reading your error message is usually stressed, often new to your tool, and rarely has the context you had when you wrote the check that failed. Every assumption you bake into the message — "obviously they'll know which field" — is a tax on someone who isn't you.

It also compounds. A codebase with consistently good error messages builds trust before a user ever reads a line of your docs. It signals that someone was thinking about them, specifically at the moments things go wrong, which is exactly when goodwill matters most. Contrast that with a tool that fails silently or cryptically — users start to route around it, wrap it in their own error handling, stop trusting its output, and quietly look for alternatives.

The effort resists being automated away, too. You can lint for missing docstrings; you can't lint for whether an error message actually helps a confused human. That's what makes it worth doing deliberately, and worth doing as a first-class part of the API or interface, not an afterthought bolted on after the "real" work is done. The error path is real work. It's often the most-read code in the entire system.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:55 AM

Style match 0.659 · Judge 3/10 · Essayist tells 2/10 · 521 words

> **Judge:** The candidate is a polished opinion-essay voice — em-dash asides, aphorisms ("a shrug rendered in monospace," "a form of empathy with a deadline"), italic emphasis, and a punchy slogan ending — whereas Kattni writes plainly and procedurally in first person, narrating what she actually did and what happened, with straightforward declaratives and workmanlike wrap-ups.

---

A stack trace that says `NullPointerException` at line 847 of a file you've never opened is not a message. It's a shrug rendered in monospace. I've spent enough hours staring at these to know the real cost isn't the bug — it's the archaeology. You're not fixing the problem yet; you're still trying to figure out what the problem even is.

Good error messages collapse that gap. They tell you what happened, why it matters, and — ideally — what to do next. That last part is the one teams skip most often, and it's the one that actually saves time. "Invalid input" tells me I failed. "Expected a URL starting with `https://`, got `htps://example.com` — check for the typo in the scheme" tells me how to succeed. The difference between those two messages is the difference between a five-second fix and a ten-minute detour through documentation, source code, and increasingly specific Google searches.

I think about error messages the same way I think about documentation: as a form of empathy with a deadline. When you write one, you're not just handling a failure case — you're having a conversation with someone who is, by definition, having a worse day than you are. They're stressed, they're behind schedule, and your library just broke their build. The error message is your one chance to be useful to them in that moment instead of being one more obstacle.

That's also why "worth the effort" is the right framing, because it *is* effort. Writing `raise ValueError("bad config")` takes four seconds. Writing `raise ValueError(f"config.timeout must be a positive number, got {timeout!r} (did you mean to quote it as a string?)")` takes actual thought — you have to imagine the person hitting this, what they were trying to do, and what mistake most plausibly got them here. But that thought is one-time cost paid by the author against a recurring cost paid by every single person who hits that path afterward, including future-you at 2am during an incident. Multiply that out over a library with thousands of users, or even just a codebase your team touches daily, and the math isn't close.

There's a technical-writing instinct that applies directly here: write for the reader's context, not your own. You know exactly why that exception fired — you're standing inside the function. The caller doesn't have that vantage point, and your job is to hand it to them: what value was expected, what value showed up, and where in their code to look. Include the variable. Include the boundary that was crossed. Resist the urge to be clever or terse; clarity beats brevity every time someone's debugging under pressure.

The teams I've seen do this well treat error messages as product surface, not an afterthought bolted on after the "real" feature is done — they get reviewed, they get user-tested, sometimes they even get their own style guide. That sounds like overkill until you remember that for a meaningful fraction of users, an error message *is* the product experience in that moment. It's the one line of your software they'll actually read closely. Make it worth reading.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:56 AM

Style match 0.640 · Judge 3/10 · Essayist tells 2/10 · 517 words

> **Judge:** The candidate is a polished opinion essay built on aphorisms, em-dash rhetorical flourishes, and a slogan-like closing line, whereas Kattni writes plainly in the first person about specific things she did, with straightforward declaratives, concrete step-by-step detail, and low-drama endings.

---

Good error messages are a tax you pay once so your users don't pay it forever. That's the trade I keep coming back to when I'm tempted to ship the default exception text and move on. It compiles. It technically tells you something went wrong. But "NullReferenceException at line 47" is not a message, it's a shrug. And shrugs cost real time — someone else's time, usually, at 2am, without the context you had when you wrote the code.

I think about error messages the way I think about documentation: as a form of empathy for a future person who knows less than I do right now. That future person might be a teammate. It might be a user who has no idea what a stack trace even is. It might be me, six months from now, having long since forgotten why this function throws under these specific conditions. A good error message closes the gap between "something broke" and "here's what to do about it." A bad one just relocates the problem from the code to the person reading the code.

The pattern I try to follow is simple: say what happened, say why, say what to do next. "Invalid input" tells you nothing actionable. "Expected a positive integer for `retryCount`, got -1" tells you exactly where to look. Add a suggestion — "did you mean to pass `Infinity` for unlimited retries?" — and you've turned a support ticket into a non-event. The best error messages I've written or read don't just report failure, they teach. They encode a little bit of the mental model the author had, so the reader doesn't have to reconstruct it from source code and guesswork.

This is also, unglamorously, a documentation problem. Docs tell you how things are supposed to work. Error messages tell you what to do when they don't — which is exactly the moment a user is most frustrated and least willing to go digging through your guides. If your error message can answer the question right there, in place, you've saved someone a context switch, a search, maybe a GitHub issue you'll have to triage later. I've watched support burden drop measurably after nothing more than rewriting error copy. No new features, no bug fixes — just clearer sentences at the exact point of failure.

There's a cost, obviously. Writing a good error message takes longer than writing `throw new Error("failed")`. You have to think about who's going to see it, what they'll know, what they'll be trying to do. You have to write actual prose, and prose is harder than code for a lot of us. But that cost is paid once, by you, with full context. The alternative cost is paid repeatedly, by everyone else, with none.

So I've come to treat error messages as a first-class part of the interface, not an afterthought bolted onto the unhappy path. They're often the only writing a user reads from you in a moment of genuine stress. That's worth getting right — not because it's nice, but because it's the cheapest debugging tool you'll ever ship.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:56 AM

Style match 0.646 · Judge 3/10 · Essayist tells 2/10 · 548 words

> **Judge:** The candidate is a polished persuasive essay full of em-dash asides, fragments, rhetorical address, and an aphoristic closer, whereas Kattni writes plain, sequential first-person reports of what she did and what happened; it also opens with a stray meta-note about memory that no reference sample would contain.

---

No memory yet on Kattni's writing voice, so I'll draw on the "developer and technical writer" framing given in the prompt.

Nobody budgets time for error messages. They show up at the end of a sprint, after the feature works, when everyone just wants to ship. So we write `Error: invalid input` and move on. I understand the impulse — I've done it myself, more times than I'd like to admit — but I've come to think it's one of the most expensive shortcuts in software.

Here's the thing about an error message: it's not a log line. It's a conversation. Somewhere out there, a real person just hit a wall in your software, and the words you chose are the only thing standing between them and either fixing the problem or closing the tab in frustration. That's not an exaggeration — it's the actual job of the message. And most of the time, we hand that job to whatever string happened to be closest when the exception was thrown.

Think about what a good error message actually has to do. It has to say what went wrong, in language the reader can parse without opening the source code. It has to say where, specifically enough that they're not hunting through six files. And ideally, it tells them what to do next. `Config file not found` is a fact. `Config file not found at ./settings.yaml — run \`init\` to generate one` is a fix. The difference between those two sentences is measured in support tickets, forum posts, and how many people quietly give up on your project.

I think the resistance to investing in this comes from a category error: we treat error messages as an implementation detail when they're actually a piece of UI — arguably the most-read UI in the whole product, because it only shows up exactly when the user is stuck and paying full attention. Nobody reads your onboarding docs twice. People read a confusing error message five times, increasingly annoyed, before they give up and go search for it verbatim.

There's a selfish reason to care too. The better your error messages are, the fewer times you personally get pinged to explain what `ECONNRESET` means in your context. Every ambiguous error is a future interruption — for you, for a teammate, for whoever's on call. I've watched a team's support load drop noticeably just from a pass over their top twenty error strings, adding context and next steps to each. No new features, no architecture changes. Just words, chosen with the reader in mind.

Good error messages also make debugging your own code better, which is a nice side effect nobody advertises. When you force yourself to write "what actually went wrong, in a way a stranger would understand," you often discover you don't fully know — which is usually a sign the underlying code needs to be clearer too. Precise language and precise systems tend to travel together.

None of this requires much. It requires treating the moment of failure with the same care you gave the moment of success — writing for the tired, annoyed, three-tabs-deep person on the other end, instead of for the compiler. That's a small habit. It just happens to be the one people remember you by.

---

### Run 4, essay 1 · Aug 20, 5:30 PM

Style match 0.637 · Judge 3/10 · Essayist tells 2/10 · 521 words

> **Judge:** The candidate is a polished persuasive essay built on second-person address, rhetorical questions, em-dash flourishes, aphoristic reversals, and a lyrical closing line, whereas Kattni writes as a plain first-person practitioner narrating concrete steps and what actually happened, with straightforward declaratives and little rhetorical staging.

---

Good error messages are the unglamorous work that nobody notices when it's done right, and everybody curses when it's done wrong. That asymmetry is exactly why so many teams skip it — the payoff is invisible until the moment it isn't.

Think about the last time you hit a wall in someone else's codebase. Maybe it was a stack trace that said `NullPointerException` and nothing else. Maybe it was `Error: something went wrong`. In that moment, you weren't debugging a program — you were debugging a person's assumptions about who would read that message and what they'd already know. Usually the assumption was: nobody, and everything. Neither is true. The person reading your error message is tired, probably not you, and missing exactly the context you had in your head when you wrote the code six months ago.

A good error message is a small act of empathy compressed into a single line. It answers three questions in order: what happened, why it happened, and what to do about it. Skip any one of those and you've handed someone a puzzle instead of a diagnosis. "Connection refused" tells me what. "Connection refused: could not reach db.internal:5432" tells me what and where. "Connection refused: could not reach db.internal:5432 — is the VPN connected?" tells me what, where, and gives me my next move before I've even opened a terminal. That last version costs maybe fifteen extra seconds to write. It can save the reader fifteen minutes, or an hour, or the will to keep using your tool at all.

There's a documentation instinct at work here that's worth naming: an error message is documentation that appears exactly when it's needed, read by someone who is, by definition, paying full attention. You don't get better placement than that. A paragraph in your README might never be read. An error message that fires the moment someone does the wrong thing is read every single time, by definition. That's leverage most other writing doesn't have, and it's why I treat error copy with the same care I'd give a getting-started guide — arguably more, because the reader's patience is already lower.

There's also a trust dimension. Vague errors erode confidence in a system faster than actual bugs do, because they suggest the people who built it don't understand their own failure modes — or worse, don't care whether you do. Specific, honest errors do the opposite: they signal that someone thought about the day things go wrong, not just the day they go right. Users forgive systems that fail clearly. They abandon systems that fail cryptically, even if the underlying reliability is identical.

None of this requires cleverness. It requires the discipline to stop at the moment of failure and ask: if I were the one hitting this, exhausted and out of context, what would I need to hear right now? Write that sentence. It is, quietly, some of the highest-leverage writing you will ever do in a codebase — and almost nobody will ever tell you they appreciated it, because the whole point is that they never had to think about it at all.

---

### Run 4, essay 2 · Aug 20, 5:30 PM

Style match 0.687 · Judge 3/10 · Essayist tells 2/10 · 526 words

> **Judge:** The candidate is a polished opinion essay built on rhetorical antithesis, em-dash flourishes, and an aphoristic closing couplet, whereas Kattni writes as a plain first-person practitioner narrating concrete steps she took and what happened, with workmanlike sentences and no epigrammatic payoff.

---

Every developer has hit the wall of `Error: undefined`. It tells you something broke, offers no clue where, why, or what to do next, and sends you straight to grep. I've spent enough hours on that particular scavenger hunt to believe error messages deserve as much design attention as the feature they're guarding.

The case for good error messages isn't really about politeness — it's about where the cost of ambiguity lands. Every error message you don't write carefully gets written anyway, just later, by whoever hits it. They write it in a Slack message to a teammate, in a support ticket, in a GitHub issue with three screenshots and a shrug. The information debt doesn't disappear; it moves downstream and gets more expensive. A stack trace that says `TypeError: Cannot read properties of undefined (reading 'id')` is technically accurate and practically useless. Compare that to `Cannot process order: customer.id is missing. This usually means the checkout session expired before submission.` The second one tells you what failed, why it plausibly failed, and where to look. That's not extra credit — that's the message doing its actual job.

Good error messages also change who can fix the problem. A cryptic message keeps troubleshooting locked inside the team that wrote the code, because only they have the tribal knowledge to translate it. A clear one hands that knowledge to whoever's holding the bag at 2am — a support engineer, a new hire, a user who could self-serve if you let them. I think of this as documentation that ships at the exact moment someone needs it most, which is a better delivery mechanism than any wiki page. Nobody reads the runbook before things break. They read the error message.

There's a writing discipline to this that's easy to underrate. A good error message answers three questions in order: what happened, why it happened (or what state caused it), and what to do about it. Not all three are always possible — sometimes you genuinely don't know why — but even naming the boundary of your own uncertainty is more honest and more useful than a generic fallback string. "Unexpected error" is rarely true. Something specific happened; the code just didn't bother finding out what.

I'd also push back on the idea that this is expensive. Writing `throw new Error('failed')` and writing `throw new ValidationError('email field must be a valid address, got: ' + input)` cost roughly the same number of keystrokes. The expense isn't in the writing, it's in the thinking — actually considering the failure mode instead of treating errors as an afterthought bolted onto the happy path. That's a habit, not a budget line.

The real tell is what happens when something goes wrong in production. A codebase with thoughtful errors turns an incident into a five-minute read. A codebase without them turns it into an archaeology dig — reproducing state, adding print statements, guessing. You pay for bad error messages eventually; you just pay in debugging hours instead of authoring minutes, and debugging hours are always the more expensive currency. Write the message for the tired person who hits it next. Often, that's you.

---

### Run 4, essay 3 · Aug 20, 5:30 PM

Style match 0.660 · Judge 3/10 · Essayist tells 2/10 · 535 words

> **Judge:** The candidate is a polished opinion essay full of em-dash cadences, aphorisms, rhetorical framing, and a lyrical closer ("That's the whole job. It's worth doing."), whereas Kattni writes plainly and procedurally in first person about what she actually did, with step lists, concrete tooling detail, and no epigrammatic flourishes.

---

Error messages are the moments your software talks back. Most of the time, it says nothing worth hearing — a stack trace, a status code, a wall of red text that means something to the interpreter and nothing to the human staring at it. I've spent enough time writing documentation and enough time debugging other people's code at 11pm to know that these two experiences are the same experience, just at different points in the timeline. A good error message is documentation that shows up exactly when you need it, and a bad one is a locked door with no sign.

Here's the thing about writing error messages well: it's technical writing under constraint. You don't get a paragraph. You don't get a diagram. You get one line, maybe two, and it has to do the work of an entire troubleshooting guide. That constraint is exactly why the effort matters — there's no room to hide behind vagueness. "Something went wrong" is what you write when you haven't figured out what actually went wrong, or you have and you didn't bother to say it. Either way, you've handed your problem to the user.

I think about error messages the same way I think about any piece of documentation: who is reading this, what do they already know, and what do they need to do next. A message like `Connection refused` tells me the network layer failed and nothing else. A message like `Could not connect to database at localhost:5432 — is Postgres running?` tells me the same fact, plus a hypothesis, plus my next action. That's not a longer message for the sake of length. It's a message that respects the fact that a human is going to read it under time pressure, possibly frustrated, possibly new to the codebase, and it hands them a foothold instead of a wall.

There's a cost argument here too, and it's not subtle. Every vague error message you ship is a support ticket, a Slack message to a teammate, a forty-five-minute detour through logs that a better sentence would have prevented. You pay for a bad error message once when you don't write it, and then everyone downstream pays for it repeatedly, forever, in small increments of confusion. The good message costs you five extra minutes at write time. The bad one costs your users, your support team, and future-you (the one who forgot how this code works) far more than that, spread out and hidden so it never shows up on anyone's todo list as "fix that error message from March."

There's also a trust dimension I don't think gets talked about enough. When software fails clearly — tells you what broke, why, and what to try — you trust it more, not less. It feels like it was built by people who anticipated you'd hit trouble and left you a note. When it fails opaquely, every subsequent interaction carries a little residue of doubt.

Good error messages don't require heroics. They require the same thing good docs require: specificity, empathy for whoever's reading at 2am, and the discipline to not ship "unknown error" when you know exactly what happened. That's the whole job. It's worth doing.

---

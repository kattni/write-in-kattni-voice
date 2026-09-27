# The bug that took me three days to find

Register: narrative. 24 essays, grouped by condition, oldest first within each.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Run 1 | 0.733 / 4.0 | 0.642 / 3.0 | 0.625 / 3.0 |
| Run 2 | 0.775 / 5.0 | 0.675 / 4.0 | 0.663 / 3.0 |
| Run 3 (interrupted) | 0.694 / 4.7 (×3) | 0.656 / 3.3 (×3) | 0.630 / 3.0 (×3) |
| Run 4 | 0.706 / 4.3 (×3) | 0.707 / 3.7 (×3) | 0.660 / 3.0 (×3) |

## Skill

`/write-in-kattni-voice` plus the task. Skill on.

### Run 1 · Aug 19, 6:56 PM

Style match 0.733 · Judge 4/10 · Essayist tells 3/10 · 485 words

> **Judge:** The candidate tells a first-person technical story with plausible vocabulary, but its clipped fragments ("Not every time." "Scratch that."), withheld-reveal pacing, and reflective aphoristic ending ("intermittent bugs hide exactly where you've already decided things are fine") read as polished essayist craft rather than Kattni's plain, sequential, explanatory reporting with her characteristic connectives, parentheticals, and practical wrap-ups.

---

It was on a project I'd been building for about two weeks, an e-ink display running on a small board, and it started with the screen going blank at random. Not every time. Not on any schedule I could find. I'd power the thing on, it would run for anywhere between ten minutes and four hours, and then the display would just die. No error message. No traceback. Nothing in the log pointing at anything.

My first guess was the power supply. I swapped it for one I trusted, added a bigger capacitor, and left the board running overnight to see if a cleaner supply would fix it. It died around 3am anyway. Scratch that.

My second guess was memory. I added print statements at every allocation, expecting to catch the exact moment I ran out of RAM. I didn't. Usage looked fine right up until the display stopped responding, and it looked fine after that too. Whatever was happening wasn't a resource problem. It was something else, and I had no idea what.

By day two I was reading through the display driver line by line, which is not something I recommend doing for fun. I found two things in there that looked suspicious and fixed neither of them; neither turned out to be it. That's the part nobody tells you about debugging like this: most of what you find along the way isn't the bug. It's just stuff that also happens to be wrong.

The actual cause, when I finally found it, was one line in a function I hadn't touched in weeks (and had ruled out on day one, because I "knew" what it did). It reset a counter on the wrong condition. Every so often, depending on exactly how long the loop had been running when a particular sensor reading came in, that counter would wrap around instead of resetting cleanly, and the wraparound value happened to land on an index the display driver used without checking it first.

I found it by giving up on reproducing the bug on purpose and just logging everything, all of it, for six hours, then reading back through the output afterward looking for anything that was different right before a crash. The counter value was the one thing that never matched.

I fixed the condition, cleaned up the wraparound math too since I clearly didn't trust it anymore, and the display ran for four days straight without a single hiccup. Four days, on a bug that took three to find.

What sticks with me is how small the fix ended up being. One condition, flipped. Nothing about the actual solution explains why it took so long to see, except that intermittent bugs hide exactly where you've already decided things are fine. I hadn't watched that function closely because I thought I already understood it. I just hadn't watched it enough times to be wrong.

---

### Run 2 · Aug 19, 10:51 PM

Style match 0.775 · Judge 5/10 · Essayist tells 4/10 · 458 words

> **Judge:** The candidate shares the author's plain first-person practitioner voice and technical vocabulary, but its terse, crafted rhythm — short punchy sentences, a hook opening line, a parenthetical-aside style, and a tidy aphoristic closer ("Now, before I trust my own logic...") — reads more like a polished essayist than Kattni's looser, longer, comma-heavy, "Done."/"Onto the next thing!" narration.

---

Three days is roughly how long it took me to find a bug that turned out to be one missing check on a busy pin.

I was working on an e-ink name badge running on CircuitPython (a small display, a battery, and a microcontroller that spent most of its life asleep to save power). The badge would show my name, update on a timer, then go back to sleep. Most of the time it worked; every so often it would wake up and show a smear of half-refreshed pixels instead of the image I'd set. Not every time. Not on any pattern I could see.

I started where I always start with something intermittent: I assumed it was my code. I reread the refresh logic, added print statements, checked that I was calling the right update method before sleep. Everything looked correct in isolation. The image data was fine. The timing between wake and refresh looked fine. And still, every few dozen cycles, the display would come back wrong.

By the second day I'd moved on to blaming the hardware. I reseated the display cable. I swapped batteries, in case a low-voltage brownout was cutting power mid-refresh. I even swapped in a second badge, thinking I had a bad board. The bug followed the code, not the board, which ruled that out and also meant I was running out of obvious suspects.

The answer was sitting in the e-ink driver's datasheet, which I'd skimmed on day one and should have read properly. E-ink displays don't update instantly. After you send a refresh command, the display keeps working for a stretch of time after your code has technically moved on, holding a busy pin low the whole time it's still writing. My code sent the refresh command and immediately called deep sleep. Most of the time, sleep took just long enough to start that the refresh had already finished. Sometimes it didn't, and the display went dark mid-write, leaving a smear behind.

The fix was three lines: check the busy pin, and don't call sleep until it goes high again. That's it. What actually cost me three days wasn't the complexity of the fix, it was that I was debugging the wrong layer the whole time.

I kept treating it as a logic bug, because logic bugs are the ones I know how to find: read the code, trace the values, spot the mistake. This wasn't wrong logic. It was a missing wait for something physical to finish, and nothing in the code itself was ever going to tell me that. I had to go find it in a datasheet instead.

Now, before I trust my own logic on anything involving sleep or timing, I check the datasheet first.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:57 AM

Style match 0.690 · Judge 4/10 · Essayist tells 4/10 · 489 words

> **Judge:** The candidate shares the reference author's first-person practitioner subject matter and plain vocabulary, but its polished narrative-essay craft — dramatic short-sentence openers, a standalone punchline paragraph ("it will find you"), and a wry reflective closing line — departs from Kattni's flatter, procedural, heavily signposted style with its literal step lists, "For example," constructions, and matter-of-fact wrap-ups.

---

The board had been running fine for two days straight, and then it just stopped. No error, no crash message, just a blank screen and a light that used to blink every ten seconds sitting dark. I was building a small e-paper badge, the kind that pulls text from a file and refreshes on a timer, and it had survived every test I threw at it until it didn't.

My first guess was the obvious one: bad wiring. I reseated every header pin, checked the display cable, swapped the USB cable for a known-good one. It ran for another six hours and died again. That ruled out a loose connection, or at least made it less likely, so I moved on.

Second guess was power. E-paper displays draw a spike of current when they refresh, and I'd read enough forum posts to be suspicious of my USB hub. I moved the board to a wall adapter rated for twice the current the display should ever need. It still died, just a little later this time, closer to nine hours in.

At that point I started adding print statements everywhere, the least elegant debugging tool there is and also the one I reach for first. I logged the loop counter, the time since boot, the free memory. That last one is what caught my eye. The free memory number was dropping, a little at a time, every single refresh cycle. It never went back up.

That's a memory leak. On a full computer you might not notice one for weeks. On a microcontroller with a few hundred kilobytes to work with, it will find you.

The leak turned out to be in my own refresh function. Every time the badge redrew the screen, I was creating a new font object instead of reusing the one I'd already loaded. CircuitPython does have a garbage collector, but I'd structured the code so the old font object was still technically reachable, tucked inside a list I kept appending to and never cleared. Nothing was ever freed. The badge ran fine for hours because it started with plenty of headroom, and then one refresh cycle asked for more memory than was left and the whole thing locked up silently instead of throwing an error I could see.

The fix was three lines: load the font once outside the loop, stop appending to that list, and call the garbage collector manually after each refresh just to be safe. It worked. The badge has been running for weeks now without a single freeze.

Three days is a long time to spend on three lines of code, and I don't think that ratio is unusual for hardware bugs. Most of the time went into eliminating the wrong explanations, not finding the right one. I'd like to say I have a better system for that now, but mostly I just print more things, earlier, than I used to.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:58 AM

Style match 0.732 · Judge 4/10 · Essayist tells 3/10 · 497 words

> **Judge:** The candidate shares the first-person practitioner framing and technical subject matter, but its narrative-suspense pacing, literary similes ("wearing the costume of a code problem," "like a television with no signal"), and aphoristic closing lesson are markedly more crafted than Kattni's plain, stepwise, blog-post reporting with its blunt short sentences, parenthetical asides, and workmanlike wrap-ups.

---

I was building a battery-powered e-ink badge that woke up, refreshed its display, and went back to sleep to save power. It worked. Then, about one time in twenty, it woke up to a screen full of static, like a television with no signal, and no amount of re-flashing fixed it.

My first guess was a bad board. I swapped it for a spare I had lying around, ran the same code, and got the same static after about fifteen reboots. That ruled out hardware, or at least ruled out that particular piece of hardware, so I moved to the code. I added print statements after every step of the refresh sequence, hoping to catch the exact moment things went wrong. The board would run for an hour, log everything cleanly, then produce garbage with no error and no clue in the log. Nothing failed. It just came out wrong.

By the second day I stopped trying to catch it live and started trying to force it. I wrote a loop that woke the display, refreshed it, and slept, over and over, timing each cycle. Somewhere around cycle eleven, on average, it would glitch. Not on a fixed cycle count, not at a fixed battery voltage, nothing I could pin to a variable I was tracking. I started suspecting timing rather than logic, since the code itself hadn't changed in weeks and had worked fine before I added the deep sleep step.

That's the part that took the longest to accept: I kept re-reading my own refresh function looking for a bug that wasn't there, because the actual problem wasn't in what I'd written, it was in what I hadn't written. E-ink displays take time to physically settle after you tell them to update, longer than the code takes to run the update command. My code sent the refresh instruction and immediately cut power for deep sleep, on the assumption that "sent" meant "done." Most of the time the display finished in the gap between the last instruction and the actual power cut. Sometimes it didn't.

On day three I added a fixed two-second delay between the refresh call and the sleep call. The static stopped. I ran the forced loop again, two hundred cycles this time, and it held.

Two seconds felt like a long time to guess at, so I went back and checked the display's datasheet, which listed a typical full-refresh time of about that long (I'd skimmed past this number the first time, since it hadn't seemed relevant to a bug I assumed was in my logic, not in my patience). It matched.

The fix was one line. Finding it meant learning that "the command finished" and "the physical thing the command controls finished" are two different facts, and that a bug which shows up occasionally is often a timing problem wearing the costume of a code problem. I've started adding that delay, and a comment explaining why, to every e-ink project since.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:58 AM

Style match 0.661 · Judge 6/10 · Essayist tells 5/10 · 519 words

> **Judge:** The candidate shares Kattni's plain first-person practitioner reporting and technical vocabulary, but reads more crafted-narrative than her flat procedural style — the withheld-reveal structure, ellipsis-and-em-dash beats, short dramatic sentences ("Still happened.", "I didn't."), and the reflective lesson-learned closing are polished-essayist moves she doesn't make, and it lacks her chatty asides, parentheticals, "Done."-style bluntness, and step-by-step framing.

---

Three days is a long time to spend on a single bug, and I want to be upfront that most of it wasn't spent writing code. It was spent staring at a display that worked fine four times out of five.

The project was an e-ink badge running on CircuitPython, the kind of thing that wakes from deep sleep, redraws a name and a little icon, and goes back to sleep to save battery. Most of the time it worked exactly like that. Occasionally, though, it would wake up and just... not update. The screen would stay on whatever it last showed, sometimes for a full cycle, sometimes for three or four in a row before it caught up again.

My first instinct was the wiring. E-ink displays are fussy about their busy pin, the one that tells your code "I'm still refreshing, don't touch me yet," and a loose connection there is a classic source of exactly this kind of flakiness. I reseated the header, checked continuity with a multimeter, swapped the jumper wires for ones I trusted more. Still happened. Not as often, which made it worse, because now I couldn't tell if I'd fixed something or just gotten lucky.

Day two I stopped touching hardware and started logging. I printed a timestamp and the busy pin's state at every step of the refresh routine, then left the badge running overnight to catch the failure on its own. In the morning I had about sixty cycles logged and four failures. In every failure, the busy pin read low right when the code checked it, then went high a few milliseconds later. My code was reading "not busy" a moment before the display actually started its refresh, so it moved on to the next command while the panel was still getting ready for the first one.

That's a race condition, and once I had it logged I assumed I'd fix it in ten minutes. I didn't. I added a delay after wake, then a longer one, then a check-twice-before-trusting-it pattern. The failure rate dropped but never hit zero, which told me the delay wasn't the actual fix, just a smaller version of the same guess.

Day three I went back to the datasheet instead of the code. Buried in the timing diagram was a note I'd skimmed past twice: the busy pin needs an external pull-down, and without one it floats between refresh cycles, occasionally read as low by pure electrical noise. My breakout board didn't include one. The delay had been masking a floating pin, not fixing it.

I added a 10k resistor between the busy pin and ground. The glitch stopped, completely, across a few hundred cycles of testing.

What stuck with me afterward wasn't the fix itself, it was how much time I spent debugging software for a problem that lived entirely in the hardware. The pull-down would have taken thirty seconds to add if I'd read the whole datasheet on day one instead of day three. I've started reading the timing diagrams first now, before I write a single line of the driver code.

---

### Run 4, essay 1 · Aug 20, 5:31 PM

Style match 0.642 · Judge 4/10 · Essayist tells 3/10 · 507 words

> **Judge:** The candidate shares the author's first-person practitioner subject matter and some plain vocabulary, but its literary polish — the simile about wandering off mid-sentence, the one-line paragraph fragment "It still froze.", and the reflective forward-looking closer — reads as a crafted essayist rather than Kattni's flatter, more procedural, heading-and-list-driven reporting voice.

---

The bug showed up in a project I was building with an ESP32 and a small OLED display, a little air quality monitor for my desk. It worked fine for a few minutes, then the screen would freeze. Not crash exactly. Just stop updating, like it had wandered off mid-sentence.

I started where I usually start, with print statements. I added timestamps around every loop iteration and let it run overnight. In the morning I had a log file with hundreds of lines showing the loop executing right up until it didn't, no error, no traceback, just silence after a certain line. That ruled out an obvious exception somewhere. It also ruled out my first guess, which was a bad sensor reading crashing the parse logic.

Day two I suspected memory. ESP32s have limited RAM, and CircuitPython does garbage collection that can occasionally stall things if you're allocating a lot of small objects in a loop. I added `gc.mem_free()` calls next to my timestamps and watched the free memory drop, slowly, over the course of each run. That felt like a real lead. I went through my code and found a spot where I was building a new string every loop to format the display text, and switched it to reuse a buffer instead. I also cut down on some list comprehensions that were quietly generating garbage. The memory numbers stabilized. I ran it again feeling pretty good about myself.

It still froze.

That's when I stopped trusting my own narrative about what the bug was and went back to just watching the hardware. I hooked up a multimeter to the 3.3V rail and left it monitoring while the board ran. The freezes lined up with small voltage dips, dips that happened right when the Wi-Fi radio kicked on to push a reading to my logging server. The board was browning out for a fraction of a second, just enough to reset the I2C bus without triggering a full reboot, and the display driver had no idea it needed to reinitialize after that.

I'd been staring at software for two straight days because the symptom looked like software: a hang, no error, timing that seemed logic-related. It was a power supply that couldn't quite handle the current spike from the radio. I swapped the USB cable for a shorter, lower-resistance one and added a bulk capacitor across the power rail. The freezing stopped.

Three days is a long time for a fix that ended up being a two dollar capacitor. I don't think the two days I spent chasing memory allocation were wasted, though. The code is genuinely better for it, and I'd have wanted that cleanup eventually anyway. But it's a good reminder that when a symptom is intermittent and doesn't leave an error behind, the cause is worth suspecting outside the code, not just inside it. I've started keeping a multimeter on my desk next to the laptop now, not buried in a drawer. Next time something freezes without complaining, that's where I'll look first.

---

### Run 4, essay 2 · Aug 20, 5:32 PM

Style match 0.703 · Judge 5/10 · Essayist tells 4/10 · 501 words

> **Judge:** The candidate shares the author's first-person practitioner reporting, but its scene-setting narrative opening, sentence fragments for effect ("Not gradually. Straight to zero."), self-aware asides, and reflective closing beat read as crafted personal-essay style rather than Kattni's plainer, denser, step-by-step prose with its hallmark short declaratives ("Done."), em-dash-free parenthetical asides, British spellings, and practical wrap-up sections.

---

It was a Tuesday when I first noticed the readings were wrong. I was building a small weather station with a CircuitPython board and a temperature and humidity sensor, and every few hours the humidity value would just drop to zero. Not gradually. Straight to zero, then back to normal a few readings later, like nothing had happened.

My first assumption was the sensor itself. I'd used it before without trouble, but sensors fail, especially cheap ones, so I swapped it for a spare. Same behavior. That ruled out a bad unit, which meant it was something in my code or my wiring.

I spent the first day reading through my polling loop line by line. I was averaging readings over a short window to smooth out noise, and I wondered if a single bad reading was getting into that average and dragging the whole thing down. I added print statements everywhere, logged every raw value before any processing touched it. The raw values from the sensor were fine. Zero wasn't coming from the sensor at all. It was coming from somewhere in my own code.

That's the part that took the longest to accept, honestly. It's much easier to blame the hardware.

On the second day I started commenting out sections of the loop to isolate where the value actually turned into zero. I had a function that wrote readings to a CSV file on an SD card, and I noticed the drops seemed to line up with file writes, but not every file write, only some of them. I checked whether the SD card was slow, whether the write was blocking long enough to affect a subsequent sensor read. It wasn't. The timing didn't line up cleanly enough to explain it.

I almost gave up and rewrote the whole logging system out of frustration, which would have been the wrong move; it would have hidden the bug instead of fixing it.

On the third day I went back to the beginning and reread my averaging function slowly, out loud, which is a habit I have when I'm stuck. I was storing readings in a list and resetting it after each average, but I'd written the reset outside an if statement I'd added later for a different reason. Under specific conditions, that reset ran twice in the same loop iteration, once as intended and once by accident, and the second reset happened after a partial list had already been averaged. An empty list averaged to zero.

It had nothing to do with the sensor, the SD card, or the wiring. It was one line of logic that only misfired under a narrow combination of timing and state, which is exactly why it took three days to see. Once I found it, the fix was a single indent change.

I still don't have a tidy lesson to hand anyone from this one. Mostly I just remember how long I spent suspecting the hardware before I trusted that the bug was mine.

---

### Run 4, essay 3 · Aug 20, 5:32 PM

Style match 0.772 · Judge 4/10 · Essayist tells 4/10 · 466 words

> **Judge:** The candidate shares the reference's plain first-person practitioner subject matter and some vocabulary, but it reads as a polished narrative-essay debugging story — reflective framing ("a strange ratio to sit with"), a short lyrical kicker final line, and deliberate fragment beats ("Not crashing exactly.") — where Kattni writes flatter, more procedural, heavily comma-spliced explanatory prose with headings, lists, and blunt closers like "Done." or "Onto the next thing!

---

I sat down three days ago to fix what looked like a five minute problem. A CircuitPython project I'd built, a small e-ink badge that shows my name and swaps to a different quote every hour, had started freezing overnight. Not crashing exactly. The screen would just stop updating, stuck on whatever it had last drawn, and the only way to get it moving again was to unplug it and plug it back in.

My first guess was the obvious one: a memory leak. E-ink displays eat RAM for the refresh buffer, and CircuitPython boards don't have much of it to spare. I added print statements to track gc.mem_free() before and after every update, left it running overnight, and checked in the morning. Memory was fine. It held steady the whole time, right up until the display stopped.

So it wasn't memory. I moved on to the display driver, checking whether the SPI bus was somehow losing sync between refreshes. I rewrote the refresh function to reinitialize the bus before every draw, which isn't something you should have to do, but I was two days in and starting to throw things at the wall. That bought me maybe six extra hours before the freeze came back.

What actually cracked it was noticing the freezes only happened when the badge was running on battery, never when it was plugged into USB for testing. That single fact narrowed things down. It wasn't the display driver at all. The board was dropping into a low power state between updates to save battery, and the e-ink display needed a specific voltage to complete its refresh cycle, one the regulator couldn't reliably hold once the battery dipped below a certain charge level. On USB power that voltage never wavered, so I never saw the problem. On battery, especially after six or eight hours of runtime, it did.

The fix, once I understood what was actually happening, took about ten minutes. I added a check before each refresh to read the battery voltage first, and if it was too low, skip the update entirely rather than starting a refresh cycle the display couldn't finish. A partial refresh was what locked up the controller, not any bug in my code.

Three days for a ten minute fix is a strange ratio to sit with. Most of that time wasn't spent writing code; it was spent chasing the wrong layer of the stack, because a frozen screen looks like a software problem long before it looks like a power problem. I'm not sure there was a faster route to the answer, short of thinking to check battery voltage on day one, which in hindsight is exactly where I should have started.

The badge has been running for a week now without a single freeze.

---

## Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

### Run 1 · Aug 19, 6:57 PM

Style match 0.642 · Judge 3/10 · Essayist tells 2/10 · 493 words

> **Judge:** The candidate is a polished narrative-essay debugging story with dramatic pacing, a rhetorical setup-and-payoff structure, italicized emphasis for effect, and an aphoristic closing line ("That's usually exactly where they are"), whereas Kattni writes as a plain, sequential first-person practitioner whose posts end in practical wrap-ups and next steps rather than thematic punchlines.

---

The bug that took me three days to find was not, in the end, a hard bug. That's the part that still gets me. It was a single misplaced assumption, buried three function calls deep, and once I found it, the fix was one line. But getting to that one line took the better part of a work week, several increasingly unhinged theories, and at least one moment where I seriously considered whether the hardware itself was cursed.

Here's the setup. I was working on a CircuitPython project, and intermittently, maybe one run in twenty, a value I was reading from a sensor would come back subtly wrong. Not garbage, not zero, just... off. Off in a way that looked plausible enough that it took me a full day to even confirm it was actually a bug, and not just sensor noise I hadn't accounted for. I spent that first day convincing myself I wasn't imagining things, which in retrospect is its own kind of debugging, even if it doesn't feel like progress at the time.

Day two, I did what I always do when something is intermittent: I assumed it was timing. Race conditions love to hide in the gaps between "this should be instant" and "this is actually running on a microcontroller with other things going on." I added delays. I removed delays. I restructured the order of operations. Nothing changed the failure rate, which should have told me I was wrong about the cause, but instead I just concluded I hadn't found the right delay yet. This is, I think, the most dangerous place to be in a debugging session: convinced of a theory, and interpreting every failed experiment as "not enough of the fix" rather than "not the right fix at all."

It was day three, staring at the same fifteen lines of code for what felt like the four hundredth time, that I noticed I was reusing a variable name across two different scopes that I had, somewhere along the way, convinced myself were isolated from each other. They were not isolated from each other. One in twenty times, depending on how a loop had last exited, the "fresh" value I thought I was reading was actually a leftover from the previous pass. It had nothing to do with timing. It had nothing to do with the sensor. It had to do with me, three days earlier, deciding a variable could be trusted to reset itself, and never once going back to verify that assumption.

What I keep coming back to is how much of those three days I spent testing everything except the thing that was actually wrong. I checked the hardware. I checked the timing. I checked the sensor's documentation twice. The one thing I didn't check was my own foundational assumption, because it didn't feel like a place a bug could live. It felt too basic to be wrong. That's usually exactly where they are.

---

### Run 2 · Aug 19, 10:52 PM

Style match 0.675 · Judge 4/10 · Essayist tells 3/10 · 528 words

> **Judge:** The candidate is a polished narrative-essay voice — comma-spliced cascading sentences, wry asides, a day-by-day dramatic arc, and a reflective lyrical closing about mental models — whereas Kattni writes flat, declarative, step-by-step practitioner prose with short sentences, frequent parentheticals and links, headings, and endings that simply state what's next.

---

It started, as these things do, with something that should have taken twenty minutes. A test was failing intermittently in CI, and only in CI, and only sometimes, which is the single most infuriating category of bug that exists. Run it locally: passes. Run it a hundred times locally: passes. Push it up, watch the pipeline, and one in maybe eight runs, it fails with an error that made no logical sense given the code in front of me.

Day one was denial. I assumed it was a flaky test, the kind you tag and move on from, except this test was verifying something I genuinely needed to be correct, so I couldn't just shrug and add a retry. I read through the function it was testing about a dozen times, convinced I was missing something obvious. I wasn't. Or rather, I was, but not in the place I was looking.

Day two was where I actually started being systematic about it, instead of just staring harder at the same twenty lines. I added logging. Excessive logging, the kind where you're basically narrating the internal state of the program to yourself like a diary. I reproduced the failure a handful more times in CI, each time capturing a little more context, and slowly a pattern emerged: it only failed when a particular async operation completed before another one, instead of after. Which told me it was a race condition, which is a phrase that should strike a small amount of fear into anyone reading it, because race conditions are exactly the kind of bug where "it works on my machine" is not reassurance, it's a symptom.

Day three, I finally found it. Two functions were both writing to what I'd assumed was an immutable piece of shared state, on the reasonable assumption that nothing else would be touching it at that point in the lifecycle. Locally, my machine was fast enough, or slow enough, or consistently enough one or the other, that the two writes always happened in the same order. On CI's shared runners, with their unpredictable scheduling and variable load, that order wasn't guaranteed. Once in a while, the second write clobbered the first before it had been read, and everything downstream quietly used the wrong value.

The fix itself took about four minutes. I made the state explicit and passed it directly instead of relying on it existing correctly in the ambient environment by the time anyone got around to reading it.

What stuck with me afterward wasn't the fix, it was how confidently wrong my initial assumption had been for two full days. I wasn't looking in the wrong file. I was looking at the right file, with the wrong mental model of what could possibly be happening inside it. That's the part that's hard to shortcut. You can read code faster, you can log more aggressively, you can be more disciplined about narrowing down when a failure happens versus when it doesn't, and all of that helped. But eventually you just have to be willing to throw out the assumption that felt too obviously true to question, and go looking underneath it instead.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:59 AM

Style match 0.663 · Judge 3/10 · Essayist tells 2/10 · 524 words

> **Judge:** The candidate is a polished literary debugging-narrative — wry self-deprecation, rhetorical flourishes, fragment-style beats, and an aphoristic closing pair ("The bugs that hide are rarely the complicated ones. They're the ones you've already decided not to look at.") — whereas Kattni writes plainly and sequentially, reporting what she did with matter-of-fact transitions, bolded practical notes, and endings that state next steps rather than land a theme.

---

The bug that took me three days to find wasn't even the interesting kind. There was no clever off-by-one error, no elegant race condition I could later explain at a meetup with a knowing smile. It was, in the end, a single character in the wrong place, and I am still a little embarrassed about how long it took me to see it.

It started, as these things do, with something that worked fine everywhere except the one place it needed to. I had a script that walked a directory of Markdown files, converted them, and generated output in a parallel structure. Locally, on my machine, it was flawless. On Read the Docs, it failed silently, producing an empty build with no error message that pointed anywhere useful. "Silently" is doing a lot of work in that sentence. What actually happened is that it failed loudly, in a way that told me absolutely nothing.

Day one, I assumed it was an environment problem. Different Python version, missing dependency, some path assumption that held on my machine and nowhere else. I rebuilt my local environment to match the CI environment as closely as I could manage, and the bug refused to show up. This is, I've learned, one of the more demoralizing things that can happen while debugging: the failure won't reproduce for you, so you're stuck reasoning about a system you can't actually observe.

Day two, I added logging. Then I added more logging. Then I added logging to the logging, which is usually a sign that I've stopped debugging and started flailing. I was fairly certain by the end of the day that the problem lived somewhere in how the tool discovered language directories, because the English build worked and the translated ones didn't, but I could not for the life of me find where the discovery logic diverged.

Day three, I finally did the thing I should have done on day one: I stopped trusting my assumptions about what the code was doing, and printed the literal value of every variable at every step, in the actual failing environment, instead of guessing at it in my head. Somewhere around the fortieth print statement, I found it. A path was being built with a hardcoded forward slash instead of the cross-platform separator I'd used everywhere else, three lines away, in a function I'd copied from an earlier version of the script and never fully re-read. It worked on my machine because my machine didn't care. It did not work in CI because CI, reasonably, did.

I want to say I learned some grand lesson from this, and honestly, I did, just not a flattering one: I trust the parts of my code I didn't just write far more than I should. The line that broke everything wasn't new. I'd walked past it a dozen times over three days, because I already believed it was fine.

It was such a small thing to have cost three days. But I've stopped being surprised by that ratio. The bugs that hide are rarely the complicated ones. They're the ones you've already decided not to look at.

---

### Run 3 (interrupted), essay 2 · Aug 20, 1:00 AM

Style match 0.671 · Judge 3/10 · Essayist tells 2/10 · 517 words

> **Judge:** The candidate is a polished literary debugging narrative — fragment punchlines ("Just... gone."), a wry self-deprecating voice, and an aphoristic closing lesson — whereas Kattni writes plainly and procedurally, reporting steps and outcomes with straightforward declaratives and workmanlike wrap-ups rather than crafted rhythm and epigram.

---

#### The Bug That Took Me Three Days to Find

I want to preface this by saying I am, generally, not a patient debugger. I like fixing things quickly, seeing the fix, and moving on to the next thing. So when I tell you I spent three days on a single bug, understand that this was not a leisurely three days. This was three days of increasing certainty that I had broken something fundamental about how computers work.

The bug itself was almost insultingly simple in retrospect, which is, I think, true of most bugs that take an unreasonable amount of time to find. It was a translation build that worked perfectly for English, worked perfectly for French, and silently, quietly, dropped exactly one string from the German output. Not an error. Not a warning. Just... gone. A single line of text that existed in the source, existed in the POT file, existed in the PO file, and vanished somewhere on its way to the rendered page.

Day one, I assumed it was me. This is usually a safe assumption, and often a correct one. I re-read my own script, certain I'd fat-fingered a loop boundary or mishandled an edge case in the merge step. I hadn't. I added print statements. I removed the print statements when they didn't help and made me feel silly. I went to bed assuming I'd find it in the morning with fresh eyes, which is a thing I tell myself constantly and which is only sometimes true.

Day two, I stopped believing it was me and started blaming the tooling, which is a dangerous place to be, because it is very rarely the tooling. I dug into the merge command itself, reading through documentation I did not fully understand, testing it against smaller and smaller reproduction cases, trying to shrink the problem down to something I could actually hold in my head at once. Eventually I got it down to two lines of source text that reproduced the issue reliably. Progress, technically. Also deeply demoralizing, because two lines being wrong felt like it should have been obvious, and it was not.

Day three is when I found it, and it was, as these things always are, almost nothing. The missing string contained an em dash. Not a hyphen. An actual em dash, the kind you get from typing it properly instead of using two hyphens and hoping. Somewhere in the encoding handling between one tool and the next, that character was being treated as a delimiter instead of content, and the line was getting truncated at exactly that point, silently, with no error to point me anywhere useful.

I fixed it in about four minutes once I saw it. Four minutes, against three days of searching.

I don't have a tidy lesson here beyond the one I already knew and apparently needed reminding of: the bugs that hide the longest are rarely hiding in the complicated code. They're hiding in the one assumption you didn't think to question, because it never occurred to you that it was a question at all.

---

### Run 3 (interrupted), essay 3 · Aug 20, 1:01 AM

Style match 0.636 · Judge 4/10 · Essayist tells 3/10 · 517 words

> **Judge:** The candidate shares the reference author's first-person technical-hobbyist subject matter, but delivers it as a crafted narrative essay — dramatic hook opening, trailing ellipses, simile flourishes ("like I was seasoning a dish I didn't trust"), fragment punchlines ("Memory was fine. I was not."), and a wry aphoristic closer — where Kattni writes in plain, sequential, declarative reporting with hedges, parentheticals, and matter-of-fact wrap-ups rather than literary shaping.

---

The bug that took me three days to find lived in a single line of CircuitPython, and by the time I found it, I genuinely considered whether it might be more efficient to simply rewrite the entire project from scratch, badge and all.

It started innocuously enough. I was working on the LED animations for a conference badge project, the kind of thing that should have taken an afternoon. The NeoPixels would light up beautifully for exactly one cycle, and then the board would appear to hang. Not crash, not throw a traceback, not do anything useful at all. Just... stop. The screen would still refresh if I pressed a button, so it wasn't fully frozen, but the animation loop was dead, and nothing in the serial console gave me so much as a hint as to why.

Day one, I assumed it was a hardware issue. I reseated the STEMMA QT cable more times than I care to admit, convinced I had a bad connection on the SDA pin. I swapped LED sticks. I swapped boards entirely. Same result, every time, after exactly one cycle.

Day two, I decided it had to be a memory issue, because on a microcontroller, when you're stumped, it's almost always memory. I started sprinkling `gc.collect()` calls throughout the code like I was seasoning a dish I didn't trust. I printed `gc.mem_free()` at every step, watching the numbers, waiting for the moment they'd tank. They never did. Memory was fine. I was not.

It was late on day two, staring at the same forty lines of code for what felt like the hundredth time, that I started questioning my own competence as a programmer, which is never a productive place to be, but is a very familiar one.

Day three, I finally did what I should have done from the start: I stripped the code down to the smallest possible reproduction, one loop, one pixel, nothing else. And there it was. I had a variable named `index` that I was incrementing inside a `for` loop that was also, separately, using `index` as its iteration variable. The outer increment was silently getting clobbered every single pass, except on the very first cycle, before the loop had run once and reset it. It wasn't a hardware problem. It wasn't a memory problem. It was a naming collision I had written myself, in maybe the fifth line of code I'd touched, and then spent two and a half days looking everywhere except at it.

I want to say I learned some grand lesson about starting with the simplest explanation first, and I did, technically, but I'm fairly certain I'll ignore that lesson again the next time I'm convinced a piece of hardware is out to get me. What I actually took away from it is smaller and a bit more forgiving of myself: three days on one bug doesn't mean three days of failure. It means three days of ruling things out, however inefficiently, until the one thing left standing was the actual answer. That, and I now name absolutely nothing `index` ever again.

---

### Run 4, essay 1 · Aug 20, 5:33 PM

Style match 0.686 · Judge 4/10 · Essayist tells 3/10 · 540 words

> **Judge:** The candidate is a self-consciously literary personal-essay narrative — reader-addressing framing, withheld reveals, rhythmic pacing, and an aphoristic closing line about small bugs being disguised by expectation — whereas Kattni writes plainly and sequentially, reporting steps and outcomes with practical asides and undramatic wrap-ups.

---

The bug that took me three days to find was, in the end, one character. I want to say that up front, because if I don't, you'll spend the next several paragraphs assuming I'm building toward something more dramatic than a stray equals sign, and I'd rather you sit with the disappointment now.

It started on a Tuesday. I had a script that was supposed to be idempotent, meaning you could run it as many times as you liked and it would always leave things in the same state. Run it once, get a result. Run it again, get the same result. This is a fairly basic expectation for the kind of automation I was writing, and mine was failing it in the most infuriating way possible: it worked. Every single time, on its own. It only broke when it ran a second time immediately after the first, in CI, under conditions I could not reliably reproduce on my own machine no matter how many times I tried.

I want to be clear that "could not reproduce" is its own special kind of misery. A bug you can see is a bug you can poke at. A bug that only shows up on someone else's infrastructure, on a schedule you don't control, is a bug that makes you start to doubt your own competence in a very particular, very quiet way. Day one, I assumed it was a race condition, because that is always the first thing you assume, and I spent most of the day adding logging in places that turned out to be completely unrelated to the actual problem. Day two, I decided it had to be an environment difference, some version mismatch between local and CI, and I burned an embarrassing number of hours trying to get my local setup to match exactly, down to package versions I hadn't thought about in months.

By day three I had stopped looking for the bug and started looking for anything that had changed recently, on the theory that bugs this stubborn are rarely new, they're just newly visible. That's when I found it. A comparison that was supposed to check whether a value was present used `is` instead of `==`. It had apparently worked by coincidence for a long time, because of the specific way Python caches small integers, and it stopped working the moment the value in question happened to fall outside the range where that coincidence held.

I did not feel triumphant when I found it. I felt tired, and a little bit betrayed, because three days is a long time to spend arguing with something that turns out to have a one-line fix. I've thought about this a lot since, and the thing I keep coming back to is that the difficulty was never really the bug. It was the assumption I made on day one, that something this disruptive had to have an equally dramatic cause, which sent me looking in all the wrong places for two days before I let myself consider something boring. I don't have a tidy lesson to wrap this up with, except that the smallest bugs are often the ones most thoroughly disguised by our expectation that they'll be big.

---

### Run 4, essay 2 · Aug 20, 5:33 PM

Style match 0.681 · Judge 3/10 · Essayist tells 2/10 · 490 words

> **Judge:** The candidate is a polished, wry literary essay full of personification, fragment punchlines ("Two characters. `is` to `==`. Three days."), a reader-addressed rhetorical aside, and an aphoristic closing line, whereas Kattni writes plainly and procedurally in the first person, reporting steps and outcomes with matter-of-fact transitions and little rhetorical shaping.

---

It took me three days to find a bug that, in the end, was two characters long. I want to say I'm exaggerating for effect, but I'm not. Two characters, three days, more coffee than I care to admit, and a level of stubbornness that I genuinely think should be a diagnosable condition at this point.

The symptom was simple enough: a script that ran perfectly fine for me, locally, every single time, and then failed intermittently in CI, in a way that made absolutely no sense. Not "failed and gave me a stack trace I could work with." Failed silently, produced output that looked correct at a glance, and then quietly corrupted a downstream file in a way I wouldn't notice until three steps later. If you've ever debugged something where the failure and the symptom are separated by that much distance, you know the particular flavor of dread I'm describing.

Day one, I assumed it was a race condition. It felt like a race condition. It had the personality of a race condition, showing up sometimes and not others, mocking me from a distance. I added logging. I added more logging. I restructured the order of operations, assuming that would at least narrow things down, and it didn't, because the bug had nothing to do with ordering at all. That's the thing nobody tells you about debugging: your first theory, the one that feels obviously correct, is often just the shape your anxiety takes.

Day two, I gave up on the race condition theory and started questioning everything else instead, which is a nice way of saying I questioned my own competence for about six hours. I rewrote the function from scratch. Same bug. I rewrote it a second, different way. Same bug, still there, patiently waiting for me. At some point you start to suspect the universe itself is broken, rather than your code, because surely, surely, you would have found this by now.

Day three is when I finally did the thing I should have done on day one: I stopped changing code and started reading it, character by character, out loud, to nobody. And there it was. A comparison using `is` instead of `==`, comparing two strings that were sometimes the same interned object and sometimes not, depending entirely on how Python happened to be feeling that day. It worked locally because my local Python interpreter interned short strings consistently. It failed in CI because a slightly different code path meant the strings weren't the same object anymore, even though they were, by any reasonable definition, equal.

Two characters. `is` to `==`. Three days.

I don't have a tidy lesson to wrap this up with, beyond the one I already knew and apparently needed reminding of: when you've been staring at something for too long, the fix usually isn't a bigger, cleverer change. It's reading what's actually there, instead of what you assume is there.

---

### Run 4, essay 3 · Aug 20, 5:34 PM

Style match 0.752 · Judge 4/10 · Essayist tells 3/10 · 508 words

> **Judge:** The candidate is a polished reflective essay — aphoristic openers and closer, sentence-fragment punchlines, second-person generalizations, and abstract meditation on debugging — where Kattni writes concrete, chronological, step-and-link-heavy practitioner reports with plain declaratives, headings, and casual asides rather than crafted rhetoric.

---

Title: The Bug That Took Me Three Days to Find

Date: 2026-8-20 (draft)

Author: Kattni

Three days. I want to say that up front, because the bug itself, once I found it, took about four minutes to fix. That ratio is, I think, the entire story of debugging, and also the entire story of why it's so demoralising.

The symptom was simple enough: an occasional, unreproducible failure. "Occasional" and "unreproducible" are, in my experience, the two words that should make you set aside whatever else you had planned for the week. If a bug happens every time, you have a bug. If a bug happens sometimes, for reasons you can't pin down, you have a problem, and problems are a different, much less friendly animal.

Day one, I did what you're supposed to do. I read the error, I read the stack trace, I read the code around the stack trace, and I was fairly confident I had it. I made a change that addressed the thing I was fairly confident about, ran the tests, watched them pass, and felt that particular, dangerous satisfaction of a job apparently done. It was not done. The failure came back within a few hours, in a slightly different shape, which is somehow worse than it coming back in the same shape, because now I had two things to explain instead of one.

Day two was mostly elimination. I want to be honest about what that actually looks like, because it isn't glamorous. It's adding print statements, or their more dignified logging equivalent, in increasingly unlikely places, and staring at output that mostly confirms what you already believed, right up until the one line that doesn't. I spent a genuinely embarrassing number of hours convinced the problem lived in a piece of code that, it would turn out, had nothing to do with it at all. I don't regret ruling it out. I regret how long I let myself be certain about it before I let the evidence talk me out of it.

The actual cause, when I finally found it late on day three, was a timing issue: two things that assumed they would always happen in a particular order, and almost always did, except when the system was under a very specific kind of load, at which point they didn't. There was no error in the code most people would have looked at. The code most people would have looked at was fine. The problem was in the space between two pieces of code that individually worked exactly as intended.

I think this is the part worth sitting with. The hardest bugs aren't hard because the code is wrong. They're hard because your model of the system is wrong, and the code is faithfully doing what you asked, which is not the same as what you meant. Finding that kind of bug isn't really about reading code faster. It's about being willing to be wrong about your own assumptions for three days in a row, and to keep looking anyway.

---

## Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

### Run 1 · Aug 19, 6:57 PM

Style match 0.625 · Judge 3/10 · Essayist tells 2/10 · 522 words

> **Judge:** The candidate is a polished literary essay — dramatic fragments ("Boring. Necessary."), an epigrammatic tricolon closing line, and a staged day-by-day arc — whereas Kattni writes plainly and procedurally in long, explanatory sentences with parenthetical clarifications, hedges like "That said," and endings that state next steps rather than deliver a punchline.

---

The bug didn't announce itself. It just sat there, quiet, in a corner of a data pipeline that had been running fine for eight months, and then one Tuesday it started dropping about one record in four thousand. No error. No stack trace. Just... gone. A number that should have summed to X summed to X minus a handful of rows, and nobody could tell me which rows, or why.

Day one was denial. I assumed it was the obvious thing — a race condition in the batch writer, because it's always a race condition in the batch writer. I added logging, ran it again, and watched it not reproduce. That's the first lesson a bug like this teaches you: if you can't make it happen on command, you don't understand it yet, you've just gotten lucky enough to notice it exists.

Day two was bargaining. I built a smaller reproduction, cut the dataset down to the smallest slice that still failed, and stared at diffs between the input and the output until my eyes crossed. I was sure it was an encoding issue — some stray byte sequence tripping a parser. It wasn't. I was sure it was a timeout — some downstream service silently swallowing a slow request. It wasn't that either. Every hypothesis I killed felt like progress and also felt like nothing, because the bug was still there, still eating one record in four thousand, indifferent to my theories.

The thing nobody tells you about a bug like this is how much of the work is bookkeeping. Not clever debugging, not flashes of insight — writing down what you've ruled out so you don't rule it out again in six hours when you've forgotten you already checked. I started keeping a log, timestamped, of every hypothesis and every result. Boring. Necessary. It's the difference between three days and three weeks.

Day three, I stopped trying to explain the bug and started trying to describe it precisely instead. Not "records are dropped" but "records are dropped when field A is null AND field B crosses a batch boundary AND the batch size happens to divide the retry window evenly." That last clause was the one that broke it open. A retry handler was deduplicating by an index computed from batch size, and under one specific arithmetic condition, two different records collapsed onto the same index. The fix was four lines. The finding was three days.

I don't think the takeaway is "be more careful," because I was careful the whole time — careful is not the bottleneck. The bottleneck was that I kept reaching for explanations before I had a precise enough description of the failure to deserve one. Every hour I lost was an hour spent theorizing about a bug I hadn't actually pinned down yet.

I wrote the postmortem the next day, mostly for future-me. Not because the bug was interesting — the fix, honestly, is dull to read. But the shape of the search is worth keeping: doubt your first theory, log what you rule out, and don't let yourself explain something you can't yet describe.

---

### Run 2 · Aug 19, 10:53 PM

Style match 0.663 · Judge 3/10 · Essayist tells 2/10 · 539 words

> **Judge:** The candidate is a polished literary essay — em-dash asides, aphoristic reversals ('it's not debugging, it's exorcism'), a lyrical thematic closer, and self-conscious meta-framing — whereas Kattni writes plainly and sequentially, reporting what she did in short declarative sentences with practical detail and unadorned endings.

---

The bug that took me three days to find wasn't actually hard. That's the part that still bothers me. I want to tell you it was some gnarly race condition buried in a distributed system, a heisenbug that vanished under a debugger's gaze, something worthy of the time it cost. It wasn't. It was a `.filter()` that ran before a `.sort()` instead of after, and once I saw it, I saw it in about four seconds.

The first day, I didn't even believe the bug was real. A user reported that a specific list — sorted, they said, by date — sometimes showed an item out of order. I couldn't reproduce it locally. I read the sorting function four or five times and it looked correct, because it was correct, in isolation. I moved on to other things, which in retrospect was the first mistake: I filed it under "probably a caching thing" and let a day and a half of instinct-trusting go by instead of instrumenting the code and just watching it.

The second day I actually got a repro, and this is where I want to be honest about the shape of the time, because the shape is the whole lesson. I didn't spend the second day staring at the sort function. I spent it staring at the network tab, then the database query, then a memoization hook three components upstream that I was sure was the culprit because it had "always been sketchy." I rewrote that hook. The bug persisted. I want to be clear that rewriting working code because it looks sketchy is not debugging, it's exorcism, and it rarely works for the same reason exorcism rarely works.

The third day I did the thing I should have done on day one: I stopped guessing and started asking the code what it believed was true at each step. Console.log, unglamorous and completely sufficient, at every stage of the pipeline. And there it was — the list got filtered for a "hidden" flag before it got sorted, but the filter ran on a copy that had already been sorted by a *different* comparator, upstream, for display grouping. Two sorts, two purposes, one array, and nobody had ever needed to think about their order relative to each other until this one edge case made it visible.

What I actually learned, and what I try to tell people who ask me about debugging, is that the first day and a half were not wasted because the bug was elsewhere — they were wasted because I skipped the boring step. Every time. The instinct to go hunt for the scary, interesting cause is exactly backwards; the scary, interesting cause is a story you tell yourself so you don't have to sit down and log every intermediate value like it's 2003. The fix, when I made it, was one line — moving the filter after the sort — and I've never been able to make that one line sound impressive at a standup. It isn't. But the three days weren't really about that line. They were about relearning, for what must be the fiftieth time, that "trust nothing, log everything" beats "trust your gut" in every single case that matters.

---

### Run 3 (interrupted), essay 1 · Aug 20, 1:01 AM

Style match 0.630 · Judge 3/10 · Essayist tells 2/10 · 528 words

> **Judge:** The candidate is a polished literary essay — dramatic pacing, self-deprecating wit, em-dash-heavy clauses, sentence fragments, and an aphoristic closing couplet — whereas Kattni writes plainly and sequentially with matter-of-fact reporting, explicit step-by-step detail, and unadorned endings.

---

The bug announced itself politely, the way the worst ones do. A test suite that had been green for months started failing intermittently — not always, not even often, maybe one run in twelve. My first instinct was the one every developer has and should be ashamed of: I re-ran it. It passed. I moved on with the specific, manufactured confidence of someone who wants a problem to not exist.

It came back two days later, in CI this time, blocking a release. Now it had my attention.

The first day was spent doing the thing I always tell people not to do, which is guessing. I suspected a race condition in our async queue handler, because it's always the async queue handler, and I spent six hours adding logging to a component that turned out to be completely innocent. I want to be honest about that hour count because I think we do a disservice to each other when we only publish the clean version of debugging — the version where you reason your way linearly to the answer. Real debugging looks like wandering into a room, turning on the lights, and finding nothing, over and over.

The second day I did what I should have done first: I made the bug reproducible on demand. Intermittent bugs aren't actually random, they're just triggered by a condition you haven't identified yet, and until you can summon it at will you're debugging blind. I wrote a script that ran the test in a loop, a thousand times, capturing full state on every failure. That took most of the morning to set up and felt like a detour. It wasn't. By afternoon I had eleven failures with eleven stack traces, and they weren't identical, which was its own clue — this wasn't one bug, it was one bug surfacing through two different symptoms.

The actual cause, when it finally showed up on day three, was almost insulting in its smallness: a timezone-naive datetime object being compared against a timezone-aware one, three layers down in a library we'd wrapped and mostly forgotten we'd wrapped. Python doesn't error on that comparison in every version, in every context, so the failure only appeared when a particular code path picked up a particular kind of timestamp — which happened to correlate, spuriously, with test order. Test order. That's the part that still gets me. I spent a day suspecting concurrency because the failure pattern looked like a race, and it was, technically, a race — just not the kind I was hunting for.

I fixed it in four lines. I want to tell you the fix felt triumphant, but mostly it felt like relief mixed with a faint, specific irritation at myself for not writing the reproducer on day one.

What I keep from this, and what I tell people I mentor, is that the instinct to guess at causes is strongest exactly when you're most under pressure, and it's exactly then that you most need to slow down and force reproducibility first. The bug doesn't care how long you've been staring at it. It only cares whether you can make it happen again.

---

### Run 3 (interrupted), essay 2 · Aug 20, 1:02 AM

Style match 0.613 · Judge 3/10 · Essayist tells 2/10 · 522 words

> **Judge:** The candidate is a polished literary essay — wry personification, one-line dramatic beats ("The tickets kept coming."), an epigrammatic pivot ("The fix was three lines. The finding was three days."), and a thematic closing reflection — where Kattni writes plainly and sequentially in the first person, explaining terms, using workmanlike connectives ("That said," "Therefore," "For example"), and ending on practical next steps rather than a crafted line.

---

The bug announced itself politely: a handful of support tickets, all describing the same thing. Users would upload a file, the progress bar would climb to ninety-eight percent, and then nothing. No error. No timeout. Just a spinner that had apparently decided to meditate.

I want to say I approached it with discipline from the start, but the first day was mostly me being smug. Ninety-eight percent means the upload finished and something after it broke — probably a callback, probably obvious. I added logging around the completion handler, redeployed, and waited for the next ticket to confirm my theory. The logs came back clean. The callback fired. Everything downstream reported success. The spinner just never got the memo.

Day two is when I stopped being smug and started being thorough, which in hindsight should have been the order from the beginning. I pulled every report that mentioned the stall and looked for what they had in common instead of what I assumed they had in common. Different browsers. Different file types. Different file sizes, though — and this is the detail I'd been skating past — always large enough to trigger our chunked upload path. Small files, uploaded in one request, never hung. That was the thread.

I spent the rest of day two inside the chunking logic, which was the kind of code that had clearly been written correctly once and then patched by three different people solving three different problems, none of whom left a note about what the others had done. I found a retry mechanism that reused a promise instead of creating a new one on failure, which meant that after a single dropped chunk, every subsequent retry was awaiting a promise that would never resolve again. It was a real bug. I fixed it, felt the specific relief of a diagnosis, and shipped it.

The tickets kept coming.

Day three started with the humiliating realization that the promise bug was real but not the bug — it explained some stalls, on some connections, some of the time, and I had mistaken a symptom for the disease because it was satisfying to find. I went back to the actual repro steps instead of my mental model of them, and this time I watched the network tab instead of the logs, because logs only tell you what the code thinks happened. What I saw was a chunk uploading twice, silently, because a browser resize event was re-triggering a visibility check that our upload hook treated as a fresh mount. The server deduped the chunk, said nothing, and the client's internal counter — which had incremented on send, not on acknowledgment — never matched the server's count again. Ninety-eight percent forever.

The fix was three lines. The finding was three days.

What I keep from that week isn't the fix, it's the reminder that my logs were lying to me the whole time — not maliciously, just narrowly, telling me exactly what I'd asked and nothing about what I hadn't thought to ask. The bug wasn't hiding. I just hadn't looked at it from outside my own assumptions yet.

---

### Run 3 (interrupted), essay 3 · Aug 20, 1:02 AM

Style match 0.647 · Judge 3/10 · Essayist tells 2/10 · 561 words

> **Judge:** The candidate is a polished literary essay full of aphoristic closers, fragment punchlines, rhetorical questions, and metaphor ('a strange kind of intimacy'), whereas Kattni writes plainly and procedurally in long, matter-of-fact first-person sentences that report steps and outcomes without stylistic flourish.

---

The bug didn't announce itself. It just sat there, quietly wrong, for three days.

It started as a support ticket: "sometimes exports come back empty." Sometimes. Not always, not never — the worst kind of qualifier a bug report can carry, because it means the reproduction steps are lying to you by omission. I pulled the logs, found nothing anomalous, and did what you do when the obvious places are clean: I assumed I'd misunderstood the report and moved on.

Day two, I actually reproduced it. Small win, except the fix I wrote for it didn't fix it. That's the moment a bug stops being a task and starts being a relationship. I added logging. I added more logging. I stared at timestamps until they stopped looking like numbers. The export was empty exactly often enough to feel meaningful and rare enough that I couldn't trust any single test run to tell me anything.

I want to say I had a flash of insight, but what actually happened is duller and truer: I got bored of guessing and started writing down what I actually knew, instead of what I assumed. Once it was on paper, the shape of it stopped being mysterious — a scheduled job and a user-triggered export both writing to the same temp path, sharing a strange kind of intimacy for two things that had never been introduced. Most of the time they didn't collide. Occasionally, they did, and the second write clobbered the first before it finished being read.

Three days for a race condition with a two-line fix. That ratio is not unusual, and it's the part people don't put in the postmortem — the fix is boring, the finding is the whole story.

What actually cost the time wasn't the bug's cleverness. It was mine — three days spent debugging as if the bug lived in the code I could see, when it lived in the assumption underneath the code: that two processes with different callers, different triggers, different owners, could never possibly overlap. Nobody wrote that assumption down. Nobody was wrong to not write it down, either — it's the kind of thing you don't think to question until it's the only thing left. I finally found it by refusing to believe the system was random. Systems don't do random. They do exactly what they're told, every time, and "sometimes" just means you haven't found the variable yet.

If I'm honest about what changed for me afterward, it's not that I got smarter about concurrency. It's that I stopped trusting my own certainty as evidence. "That can't be it" is not a debugging step, it's a resting point, and I'd been resting on it for two days without noticing. Now when I hear myself say a cause is impossible, I treat it as a flag rather than a conclusion — impossible according to what, exactly, and have I actually checked, or have I just been staring at it long enough that it started to feel checked?

The fix shipped in an afternoon. The three days before it weren't wasted, even though it felt that way in the middle — they were the actual work, the part where you build the model that makes the fix obvious in hindsight. Every real bug is obvious in hindsight. That's not a coincidence. That's what finding it means.

---

### Run 4, essay 1 · Aug 20, 5:34 PM

Style match 0.633 · Judge 3/10 · Essayist tells 2/10 · 515 words

> **Judge:** The candidate is a polished literary essay — opening hook, fragment punchlines, em-dash aphorisms, simile-laden reflection, and a thematic closing line — whereas Kattni writes plainly and procedurally in the first person, narrating steps and outcomes with straightforward sentences and no crafted flourishes.

---

The bug didn't announce itself. It just sat there, quietly wrong, for three days.

It started as a support ticket: a handful of users reporting that their exported reports occasionally had numbers that didn't add up. Not wildly wrong — off by a few cents, sometimes a few dollars, and never in a way that repeated. I opened the code expecting to find the culprit in an hour. I always expect that. I should know better by now.

Day one was denial. I read through the aggregation logic, convinced myself it was correct, and closed my laptop feeling smug. Day two was humility. I wrote a script to replay a week of production data through the export pipeline and diffed the output against what users had actually seen. About one export in four thousand disagreed with itself. Four thousand. That's not a bug you catch by staring at code — that's a bug you catch by staring at data, which is a different skill and one I'm always relearning under pressure.

The pattern, once I found it, was almost insulting in its simplicity: floating-point summation, done in a loop, with values accumulated in an order that depended on which database replica happened to answer the query first. Same numbers, different order, different rounding error. It wasn't nondeterministic in the spooky, unfalsifiable sense engineers invoke when they've given up — it was deterministic given the input order, and the input order was itself nondeterministic because of how we load-balanced reads. Two boring, individually reasonable decisions had combined into something that looked like ghosts.

I want to say I found it through elegant reasoning. I didn't. I found it because I got desperate enough on day three to log the raw values going into the sum, for every replica, for every request, and just read them. Hundreds of lines of nearly-identical numbers, and then one column that shouldn't have varied, did. The logs told me what the code couldn't, because the code was doing exactly what I'd written — the bug lived in the gap between what I'd written and what I'd assumed.

The fix took fifteen minutes: sort before summing, or better, use a summation method that doesn't care about order. Kahan summation, if you want to be thorough about it. Writing the postmortem took longer than writing the fix, which is usually a sign you found something worth writing down.

What stays with me isn't the floating-point trivia — I already knew that, in the abstract, the way you know smoking is bad for you. It's that the three days weren't wasted on the fix. They were spent building the instrumentation that let me see the problem at all. I didn't get faster at debugging by knowing more facts about IEEE 754. I got faster by getting more comfortable admitting, on day one, that I hadn't actually found it yet, and going to get better evidence instead of better guesses.

The bug is gone. The habit of distrusting my first hour of confidence is still here, and it's worth more than the fix ever was.

---

### Run 4, essay 2 · Aug 20, 5:35 PM

Style match 0.658 · Judge 3/10 · Essayist tells 2/10 · 496 words

> **Judge:** The candidate is a polished literary-essay performance — em-dash asides, ironic aphorisms, sentence fragments, a lyrical thematic closer about trusting code three layers down — where Kattni writes plainly and procedurally in short declaratives, with concrete steps, links, and matter-of-fact wrap-ups rather than crafted rhythm and punchlines.

---

The office was too warm, the coffee had gone cold twice, and I was on my third day of staring at the same forty lines of code, certain — certain — that the universe had it out for me.

The bug itself was almost insultingly small: a sensor reading that drifted, just slightly, every few hours. Not enough to crash anything. Not enough to trip an error. Just enough that if you graphed it over a weekend, the line would creep upward like it had somewhere better to be. My first instinct was the sensor itself — bad hardware, a loose connection, something I could blame on physics instead of myself. I swapped the board. Same drift. I swapped the cable. Same drift. I started to suspect the breadboard was cursed, which is the point in any debugging process where you should recognize you're no longer being rational and take a walk.

Day two was worse, because day two is always worse. That's the day you've ruled out the obvious answers and have to admit the bug is smarter than your assumptions. I rewrote the calibration routine from scratch, certain I'd missed an off-by-one somewhere in the averaging window. I hadn't. I added logging everywhere, the kind of logging that makes you feel productive because the terminal fills up with reassuring scrolling text, even though none of it is telling you anything you didn't already know. I went to bed that night doing the thing every engineer does and swears they won't do again: running the failure scenario over and over in my head instead of sleeping.

The fix, when it came on day three, wasn't in my code at all. It was in a library three layers down, in a function that quietly cast a float to an int during a unit conversion I'd never bothered to read closely because it wasn't mine and it wasn't supposed to matter. It mattered. Every conversion shaved off a sliver of precision, and over thousands of cycles, those slivers added up into a drift that looked, from the outside, exactly like a hardware problem. I found it not through cleverness but through the unglamorous work of reading someone else's source line by line, which is the debugging equivalent of admitting you should have done this on day one.

What stays with me isn't the fix — a one-line change, embarrassingly small for three days of effort — it's the reminder of where bugs actually like to hide. Not in the code you just wrote, which you've already scrutinized to death, but in the code you trust enough to stop looking at. The libraries. The abstractions. The parts of the stack you've silently agreed to believe in.

I write a lot about how things are supposed to work. This bug was a good reminder to spend more time writing about, and thinking about, what happens when the "supposed to" quietly stops being true, three layers down, where nobody's looking.

---

### Run 4, essay 3 · Aug 20, 5:35 PM

Style match 0.689 · Judge 3/10 · Essayist tells 2/10 · 566 words

> **Judge:** The candidate is a polished literary essay — em-dash-heavy dramatized narration, second-person aphorisms ("it's always a race condition"), emotional flourishes like "something close to grief," and a lyrical thematic closing — whereas Kattni writes plain, concrete, first-person practitioner reporting with short declaratives, parenthetical asides, and matter-of-fact endings.

---

No memory file yet, so nothing to draw on — I'll just write the essay.

The cursor blinked on line 340 of a file I'd read so many times I could recite it, and I still couldn't see the bug. That's the part nobody tells you about the hard ones: it's never that the code is complicated. It's that you've stared at it so long your eyes have stopped actually reading it and started pattern-matching against what you expect to be there.

It started as a support ticket. A handful of users reported that their saved preferences would randomly revert — not often, not predictably, just often enough to be infuriating and rare enough to be nearly impossible to reproduce. I spent the first day doing the thing you do first: reading the code path top to bottom, convinced I'd spot the off-by-one or the missing await within the hour. I didn't. The logic was clean. Too clean, in retrospect — clean code is exactly where you stop suspecting yourself, and that's a mistake.

Day two was reproduction. I wrote a script to hammer the preferences endpoint with concurrent requests, certain this was a race condition, because it's always a race condition when you can't explain it any other way. I got nothing. Hours of load testing, hundreds of thousands of requests, not a single flake. I started doubting the bug existed at all, which is its own special kind of demoralizing — you can't fix what you can't see, and you start wondering if you're chasing a ghost the users only imagined.

The break came almost by accident, the way it usually does. I was reading through an unrelated caching layer for a completely different task when I noticed a TTL value that didn't match the one in the config file. Not wildly off — just stale, left over from a refactor eight months earlier that had changed the config default but never touched this one hardcoded fallback buried three layers deep in a rarely-hit code path. Under normal load, the cache always got a fresh write before that fallback mattered. But under a very specific combination of timing and traffic — the exact combination my load test hadn't accidentally produced — the cache would expire early, fall back to a stale read, and silently overwrite a user's real preference with whatever had been cached before it.

Once I saw it, the whole three days collapsed into obviousness, which is the cruelest part of debugging. The fix was one line. I stared at that line for a long time before committing it, partly to make sure I actually understood why it worked, and partly out of something close to grief for the seventy-two hours it had taken to get there.

What I keep from that bug isn't the fix — I don't even remember the exact TTL number anymore. It's the reminder that the bug is rarely where you're looking; it's usually one layer over, in the code you've stopped suspecting because it isn't the code you're debugging. I've started treating "this looks fine" as a prompt to look harder, not a reason to move on. Three days is a long time to spend on one line. But it's also three days that recalibrated how carefully I read code I think I already understand — and that's worth more than the fix itself ever was.

---

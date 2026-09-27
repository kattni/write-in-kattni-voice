# Writing your first test with pytest

Register: tutorial. 30 essays, grouped by condition, oldest first within each.

Scores: **style match** is the eval's stylometric similarity to your six samples (0–1, higher is closer), recomputed with `style.py`; it matches the recorded value exactly wherever one was recorded. **Judge** is the LLM judge's overall voice-match score out of 10, and **essayist tells** is its score for avoiding polished-essayist habits (higher is better; only runs 1 onward). Both come from the judge's own transcript. See [README.md](README.md) for what each run was.

Mean style match / mean judge score, per run:

| Run | Skill | Baseline with samples | Naive baseline |
|---|---|---|---|
| Run 1 | 0.735 / 5.0 | 0.705 / 4.0 | 0.597 / 3.0 |
| Run 2 | 0.752 / 4.0 | 0.775 / 6.0 | 0.676 / 3.0 |
| Smoke test | 0.688 / 4.5 (×2) | 0.718 / 5.0 (×2) | 0.649 / 3.0 (×2) |
| Run 3 (interrupted) | 0.724 / 4.0 (×3) | 0.707 / 5.3 (×3) | 0.604 / 3.0 (×3) |
| Run 4 | 0.735 / 4.0 (×3) | 0.709 / 4.3 (×3) | 0.669 / 3.3 (×3) |

## Skill

`/write-in-kattni-voice` plus the task. Skill on.

### Run 1 · Aug 19, 6:52 PM

Style match 0.735 · Judge 5/10 · Essayist tells 4/10 · 484 words

> **Judge:** The candidate shares Kattni's first-person practitioner framing and plain technical vocabulary, but it reads as a polished personal essay — reflective memoir framing, parenthetical asides used for effect, fragment punchlines ("That's it. That's the whole test."), and a thematic closing line — where Kattni's tutorials are structurally scaffolded (kBits lists, headings, "you would include:" / "Which ends up rendered as:" refrains) and her personal posts are longer-winded, comma-spliced narrative without epigrammatic polish.

---

I put off writing tests for longer than I'd like to admit. Every project I started, I told myself I'd add tests once the code settled down, and the code never settled down, so the tests never showed up. That's a pretty common trap, and pytest is the tool I finally used to climb out of it.

pytest is a testing framework for Python. It runs a file full of functions, checks each one against the rules you wrote, and tells you which ones held up and which ones didn't. Nothing fancier than that.

Start with a project. Say you have a function that adds two numbers, sitting in a file called calculator.py:

```python
def add(a, b):
    return a + b
```

To test it, create a new file. pytest looks for files that start with test_ or end with _test.py, so call it test_calculator.py:

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

This tells pytest to import the add function, run it with 2 and 3, and check that the result is 5. The assert keyword is doing the actual work here (it's Python's built-in way of saying "this had better be true, or stop and tell me"). If the condition after assert is false, the test fails. If it's true, pytest just moves on.

Run it from your terminal:

```
pytest
```

If everything's set up right, you'll see a single green dot and a line that says something like "1 passed." That's it. That's the whole test.

I remember being surprised the first time by how little ceremony this takes. No setup class, no boilerplate, just a function whose name starts with test_ and an assert statement inside it. pytest finds it, runs it, reports back.

Try breaking it on purpose. Change the assert to expect 6 instead of 5, and run pytest again. You'll get a red F instead of a dot, along with the actual value it got and the value it expected. That output is worth reading closely, since it's the same output you'll be staring at months from now when a real bug shows up, and it helps to already know what it looks like when you're not under pressure.

One thing worth naming honestly: a single passing test doesn't mean your code is correct. It means this one input behaves the way you expected. Try adding a second test for negative numbers, or zero, or whatever edge case worries you. Each one is small, and each one is a fact about your code you no longer have to hold in your head.

I didn't start writing tests because I loved testing. I started because I got tired of re-checking the same thing by hand every time I changed a line of code. pytest just gave me a way to make that checking automatic, and cheap enough that I'd actually do it.

---

### Run 2 · Aug 19, 10:46 PM

Style match 0.752 · Judge 4/10 · Essayist tells 3/10 · 499 words

> **Judge:** The candidate adopts a polished, writerly voice — scene-setting hook, fragment punchlines, italic-style emphasis on "easy" vs "obvious", an aphoristic closer about red F's teaching more than ten green ones — where Kattni writes flatly procedural, first-person tutorial prose with literal step lists, code fences, and matter-of-fact wrap-ups.

---

The first time I opened a file named test_something.py, I stared at it for a solid five minutes before typing anything. I knew pytest was supposed to be the easy testing library, the one people recommend to beginners, but "easy" and "obvious" aren't the same thing when the file is empty and you don't know what a test is even supposed to look like.

Here's what finally got me unstuck: a test in pytest is just a function. Not a class, not a special file format, not some ceremony you have to learn before you're allowed to write one. It's a function whose name starts with test_, and inside it, you assert that something is true.

For example, if you had a function that adds two numbers, you'd write:

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

That's the whole test. The assert line is the entire point of the exercise: it says "run this, and if the result isn't 5, something is wrong." Save that in a file called test_math.py, then in your terminal, run:

pytest

pytest finds any file that starts with test_ or ends with _test.py, and inside those files it finds any function that starts with test_, and it runs each one. If the assertion holds, you get a quiet green dot, and that first green dot is more satisfying than it has any right to be. If it doesn't hold, pytest shows you exactly which line failed and what the values were on either side of the ==. No configuration file needed for any of that. No boilerplate, which wasn't what I expected, given how much setup other testing tools ask for upfront.

That's most of what you need to get a first test running, but a couple of things trip people up early on. One is naming. **If your function doesn't start with test_, pytest will not find it, it'll sit there silently and never run**, and you'll wonder why your suite says "1 passed" when you wrote two tests. The other is scope. A test doesn't need to check your whole program at once, and honestly it shouldn't. One assertion, or a small handful of closely related ones, checking a single thing your code is supposed to do. If you're testing five behaviors, write five small tests instead of one function trying to do all five at once.

Once you've got the basic pattern down, try breaking it on purpose. Change the assert to expect 6 instead of 5, and run pytest again. You'll get a red F instead of a dot, along with a readout showing 5 != 6. Reading that output, and learning to trust it, teaches you more about how tests actually work than ten passing ones ever will.

From there, the natural next step is writing tests for code you actually care about, not a toy add() function. Start with the behavior in your own project that you're most nervous about breaking.

---

### Smoke test, essay 1 · Aug 20, 12:40 AM

Style match 0.735 · Judge 4/10 · Essayist tells 3/10 · 502 words

> **Judge:** The candidate opens with a stray meta-commentary line no reference sample would contain, and while its plain instructional middle is passable, it drifts into a polished-essayist register with epigrammatic asides ('which is most of what debugging is anyway'), fragment punchlines ('That's the whole thing.', 'That's it, that's the confirmation.'), and a thematic closing zinger, whereas Kattni ends with flat practical wrap-ups, uses heavier comma-spliced qualification, code-formats filenames in backticks, and never addresses the reader with rhetorical flourish.

---

I wrote the first draft directly to the target register (personal opening, then instructional scaffold), then checked it against the calibration rules before finalizing.

---

I put off writing my first test for months. I kept telling myself the code worked, I'd tested it by running it and looking at the output, and that was good enough. It wasn't, not really. Looking at output by eye doesn't scale, and it doesn't catch the thing that breaks six months from now when you've forgotten how the function is supposed to behave in the first place. A test does that job for you. It's like leaving yourself a note that says exactly what "working" means, so you don't have to remember or re-check by hand every time.

pytest is one of the more approachable ways into testing in Python, mostly because it doesn't ask much of you up front. No boilerplate class, no special setup. You write a function, you write a test function that checks it, and pytest finds and runs it for you.

Say you have a function that adds tax to a price:

```python
# pricing.py
def add_tax(price, rate):
    return price + (price * rate)
```

To test it, you'd create a new file, usually named test_pricing.py, and write a function whose name starts with test_:

```python
# test_pricing.py
from pricing import add_tax

def test_add_tax():
    assert add_tax(100, 0.1) == 110
```

That's the whole thing. The assert statement is doing the actual checking. It's saying: run add_tax with these inputs, and if the result isn't 110, something is wrong. pytest doesn't need you to tell it this is a test, or to register it anywhere. It looks for files named test_*.py and functions named test_*, and it runs whatever it finds.

From the command line, in the same directory as your files, you run:

```
pytest
```

If everything passes, you'll see a single green dot and a summary line telling you one test passed. That's it, that's the confirmation. If you want more detail while you're getting used to reading the output, add -v for verbose mode, and it'll print the name of each test as it runs.

It's worth breaking something on purpose the first time, just to see what a failure looks like. Change the expected value in your test to 999 and run pytest again. You'll get a red F instead of a dot, along with the actual value pytest calculated versus what you told it to expect. That output is more useful than it looks at first. It's telling you exactly where reality and your assumption diverged, which is most of what debugging is anyway.

Try adding a second test function to the same file, maybe one that checks add_tax with a rate of 0. Or write a test for a function you already have lying around in an old project. You don't need a big test suite to get value out of this. One test that runs automatically is already more than most code has.

---

### Smoke test, essay 2 · Aug 20, 12:40 AM

Style match 0.640 · Judge 5/10 · Essayist tells 4/10 · 492 words

> **Judge:** The candidate shares the author's first-person practitioner stance and plain technical vocabulary, but its polished narrative hook, short punchy fragments, and aphoristic closing line ("a function, an assert, and a file named right is enough to call it a test suite") read as essayist craft rather than Kattni's flatter, step-listing, explicitly enumerated tutorial voice with its "For example, ... you would include:" cadence and kBits-style structure.

---

I wrote code for years before I wrote a test for any of it. I'd change a function, run the whole program by hand, poke at it until it looked right, and move on. That worked, mostly, until the day it didn't: a change I was sure was harmless quietly broke something three files away, and I didn't find out until a user did. That's the moment testing stops being an abstract good idea and starts being something you actually want.

pytest is the tool I'd point anyone toward for a first test, because it gets out of your way. Some testing frameworks want you to learn a class hierarchy and a vocabulary of assertion methods before you write a single check. pytest wants a function and the word `assert`.

Say you've got a function that adds tax to a price.

```python
def add_tax(price, rate):
    return price + (price * rate)
```

To test it, you write a second function, in a file named something like `test_pricing.py`, that calls `add_tax` and checks the result.

```python
from pricing import add_tax

def test_add_tax():
    assert add_tax(100, 0.05) == 105
```

That's the whole test. `assert` is just Python's plain-language way of saying "this had better be true." If `add_tax(100, 0.05)` really does equal 105, the assertion passes silently. If it doesn't, Python raises an error, and pytest catches that error and reports it as a failed test instead of crashing your program.

The naming matters here, and it trips people up the first time. pytest finds your tests by convention, not by you registering them anywhere. It looks for files that start with `test_`, and inside those files, functions that start with `test_`. Name the file or the function anything else and pytest will simply never see it. This is normal to forget once.

Run it from the command line with `pytest`, and for a passing test you'll see a single dot and a summary line, something like `1 passed in 0.01s`. It's not much to look at, which is exactly what you want from a test that's just confirming things are fine.

The more useful moment is watching it fail. Change the assertion to `== 999` and run it again. pytest shows you the actual value it got, the value you expected, and the exact line where they diverged, so you're not stuck guessing which of five changes broke things.

I'd suggest starting with a function you already have, something small and self-contained, and writing one assertion for the case you're most confident about. Then write a second test for an edge case, an empty input or a negative number, something you're less sure of. That second test is usually the one that teaches you something.

None of this requires understanding fixtures, mocking, or test classes. Those matter later, once your code gets more tangled. For now, a function, an assert, and a file named right is enough to call it a test suite.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:45 AM

Style match 0.759 · Judge 4/10 · Essayist tells 3/10 · 512 words

> **Judge:** The candidate is a polished reflective-essayist take on a tutorial — framing narrative, fragment punchlines ("It worked."), quotable lines about what tests are "really for," and a lyrical closing — whereas Kattni writes flat, procedural, first-person reporting with plain "For example, you would include:" scaffolding, parenthetical asides, and unsentimental wrap-ups.

---

The first time I wrote a test, I didn't really understand what I was testing for. I had a function that converted temperatures from Celsius to Fahrenheit, and I'd been checking it worked by running it in the Python REPL and eyeballing the output. That's fine for a few minutes of poking around, but it doesn't scale, and it doesn't stick. Close the terminal and that verification is gone. You're back to trusting the code and hoping nobody breaks it later.

pytest fixes that by turning "I checked this once" into "this gets checked every time." The install is one line:

```
pip install pytest
```

A test in pytest is just a function whose name starts with `test_`, sitting in a file whose name starts with `test_` or ends with `_test.py`. That's most of the magic right there. No special class to inherit from, no boilerplate setup. pytest goes looking for that naming pattern and runs whatever it finds.

Say the function I'm testing lives in `convert.py`:

```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

The test file, `test_convert.py`, would look like this:

```python
from convert import celsius_to_fahrenheit

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32
```

That's the whole test. The `assert` line is the actual check: it says "I expect this expression to be true," and if it isn't, pytest fails the test and tells you why. This tells Python to call the function with 0, compare the result to 32, and complain loudly if those two numbers don't match.

Run it from the terminal with:

```
pytest
```

pytest finds the file, finds the function, runs it, and reports back. A dot for a pass, an F for a failure, and a summary line at the end. The first time you see that dot, it's a little anticlimactic. It worked. Nothing exploded, nothing printed, just quiet confirmation that the thing you expected to be true is true.

The more interesting moment is watching it fail. Change the `32` in the test to `33` and run it again. pytest doesn't just say "failed." It shows you the assertion, the actual value, and the expected value, side by side. That output is doing real work: it's the difference between "something's wrong" and "here's exactly what's wrong and where."

One test isn't much on its own. Try adding a second one for a different input, maybe body temperature or boiling point, and run pytest again. You'll see both results in the same summary. This is where it starts to feel less like a chore and more like a safety net: every test you add is one more thing you don't have to manually re-check by hand next time you touch that file.

I still think about that Celsius function sometimes, mostly because it was the first time a test caught something I would have missed on my own (I'd flipped the multiplication and division at one point without noticing). That's really what the test is for. Not proving the code works once, but catching it the moment it stops.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:45 AM

Style match 0.738 · Judge 4/10 · Essayist tells 3/10 · 481 words

> **Judge:** The candidate is a reflective, literary essay-with-code — narrative openers, second-person musings, and a chiastic aphoristic close ("The coverage comes later, once the habit is already there") — where Kattni's tutorials are flat, bulleted, step-by-step procedure ("kBits", "you would include:", "Which ends up rendered as:") and her personal posts are plainly reported first-person experience rather than crafted reflection.

---

The first time I wrote a test, I didn't understand what I was protecting myself from. I'd finished a function, it worked when I ran it by hand, and someone told me to "write a test for that." So I did, mostly by copying a pattern I didn't fully understand, and I moved on. It wasn't until months later, when I changed that function and the test caught what I'd broken, that the whole point clicked.

pytest is one of the easier places to start, because it doesn't ask much of you up front. You don't need a class, you don't need to import a testing framework and inherit from it. You just write a function and use the word `assert`.

Say you have a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

To test it, you write another function, in a file that starts with `test_`, and inside it you check that the output is what you expect:

```python
def test_add():
    assert add(2, 3) == 5
```

That's the whole thing. pytest finds any file named `test_*.py`, looks inside for functions named `test_*`, runs them, and checks whether the `assert` statements are true. If `add(2, 3)` really does equal `5`, the test passes. If it doesn't, pytest tells you exactly which assertion failed and what the actual value was, so you're not left guessing.

Run it from the command line with:

```
pytest
```

and you'll see a single dot for a passing test, or a full traceback for a failing one. (If you have more than one test file, pytest will find all of them on its own. You don't have to tell it where to look.)

I think the instinct, early on, is to treat a test like a formality, something you write because you're supposed to, not because you'll ever look at it again. But a test isn't really about the moment you write it. It's about six months from now, when you've forgotten exactly how that function works and you change something nearby without realizing it touches this code too. The test runs, it fails, and you find out immediately instead of finding out from a user.

Try changing the test to check something false, like `assert add(2, 3) == 6`, and run pytest again. You'll get a failure, with the exact line and the exact values pytest compared. That failure message is doing a lot of the work here. It's the reason people reach for pytest over writing their own `if` statements and print debugging by hand.

Your first test doesn't need to cover every edge case. Mine didn't. It just needs to exist, and to check something true about the code you just wrote. The habit of writing it matters more than the coverage, at least at first. The coverage comes later, once the habit is already there.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:46 AM

Style match 0.676 · Judge 4/10 · Essayist tells 3/10 · 517 words

> **Judge:** The candidate is a polished narrative-essay take on a tutorial — evocative similes, a rhetorical question to the reader, fragmenty punchlines, and a reflective closing image — where Kattni writes plainer, more procedural first-person prose with heavy bullet-list scaffolding, "For example, to X, you would include:" constructions, italic/bold file names, and matter-of-fact wrap-ups rather than lyrical ones.

---

The first time I opened a file called `test_something.py`, I had no idea what I was doing. I'd written code before, plenty of it, but I'd never written code whose entire job was to check my other code. It felt backwards, like writing a letter to someone who was about to grade my handwriting.

Here's what actually happened when I sat down with pytest for the first time.

I had a small function, something like this:

```python
def add(a, b):
    return a + b
```

Nothing fancy. To test it, pytest doesn't want a class, a special decorator, or any ceremony at all. It wants a function whose name starts with `test_`, sitting in a file whose name also starts with `test_`. That's the whole contract.

```python
def test_add():
    assert add(2, 3) == 5
```

That's it. `assert` is the whole mechanism. You're telling Python: this thing on the right should be true, and if it isn't, stop and complain. Running `pytest` in the terminal, from the directory containing the file, finds every function that matches that naming pattern and runs it. No configuration file, no registration step, no importing a test runner class. It just looks.

The first time I ran it, I got a single green dot and a line that said `1 passed`. It worked. I remember being almost let down by how anticlimactic it was. I think I'd expected testing to feel like a bigger deal than a dot on a terminal line.

Where it got interesting was watching it fail. I changed the function to return `a - b` on purpose, just to see what pytest would tell me, and instead of a vague error, I got the actual values: it showed me `5 != -1`, with the exact line where the assertion broke. That's the part that changed how I thought about tests. A test isn't just a pass or fail flag, it's a report that tells you exactly where reality diverged from what you expected.

If you're wondering whether you need to test every single function in a project before it counts as "real" testing, you don't. I started with one function and one assertion, and that was enough to understand the shape of the tool. You can add more test functions in the same file as you go, each one checking a different case: `test_add_negative_numbers`, `test_add_with_zero`, whatever scenario is bugging you. Pytest will collect and run all of them together.

One thing worth trying once you have that first test passing: change the assertion to something you know is false, on purpose, and run pytest again. Get comfortable reading a failure before you need to read one for real, at 11pm, because a deploy broke. It's a lot less stressful to learn what a traceback looks like when nothing is actually on fire.

I still remember how small that first test felt, one function, one assert, four lines of code. It didn't feel like enough to matter. But it was the same shape I'd use for every test I wrote after it, just with more cases stacked on top.

---

### Run 4, essay 1 · Aug 20, 5:19 PM

Style match 0.735 · Judge 4/10 · Essayist tells 4/10 · 504 words

---

There's a specific kind of dread that comes from changing one line of code and having no idea what else it touched. You save the file, and now you're just hoping. That's the problem tests solve, and pytest is one of the easiest ways into that habit if you're writing Python.

At its simplest, pytest lets you write a function that checks whether something is true, and it tells you when it isn't. That's really the whole idea. No special syntax to memorize, no class to inherit from, just a function with `assert` in it.

Say you've got a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

To test it, you write a second function, in a separate file, whose name starts with `test_`:

```python
def test_add():
    assert add(2, 3) == 5
```

This tells Python to call `add` with 2 and 3, and to fail loudly if the result isn't 5. That's it. Save this as `test_add.py` (pytest looks for files matching that pattern, so the name matters), and from the same directory run:

```
pytest
```

You'll get a single green dot and a line saying one test passed. If you want more detail, `pytest -v` gives you the test name alongside the result instead of just a dot.

Now break it on purpose. Change the assertion to `assert add(2, 3) == 6` and run it again. Instead of a dot, you'll get a full traceback showing you exactly what pytest expected, what it got, and which line the assertion lives on. This is the part that sold me on pytest specifically, over Python's built-in unittest module. The failure output is readable. You don't have to squint at it.

I'd suggest writing your first real test against something you already have working, not something new. Pick a function you trust, write one assertion for it, and run pytest just to watch it pass. There's very little to learn from a first test failing for the wrong reason, like a typo in the file name.

One thing worth naming honestly: a single passing test doesn't mean your code is correct, it means this one case behaves the way you expected. Tests are only as good as the cases you think to write, and it took me a while to stop treating a green pytest run as proof of anything more than "the things I checked are fine." That's still useful. It's just not the same as complete confidence.

Once you're comfortable with one assertion per test, you can add more test functions to the same file, each checking a different case, like `add(-1, 1) == 0` or `add(0, 0) == 0`. pytest will run all of them and report each one separately, so a single failure doesn't hide the rest.

Once you've got a handful of tests written this way, running `pytest` before you commit anything takes about two seconds, and it catches the kind of mistake that's easy to miss just by reading the code over.

---

### Run 4, essay 2 · Aug 20, 5:21 PM

Style match 0.722 · Judge 4/10 · Essayist tells 3/10 · 470 words

> **Judge:** The candidate shares the author's plain first-person tutorial register and code-plus-explanation structure, but it leans on writerly moves she avoids — fragment punchlines ("It isn't."), wry asides ("the correct amount of drama"), and a two-beat imperative kicker ending — where Kattni writes longer, hedged, comma-heavy sentences with explicit numbered steps and a matter-of-fact wrap-up section.

---

I wrote my first pytest test because I broke the same function twice in one afternoon and didn't notice until a coworker filed a bug. That's usually how it goes. You fix something, feel good about it, and three days later it turns out you fixed it in a way that quietly broke something else. A test is the thing that tells you immediately, instead of a coworker telling you two days later.

pytest is a testing framework for Python. Not the only one, but it's the one I reach for first, because it doesn't ask much of you to get started. No boilerplate classes, no `assertTrue` and `assertEqual`, just Python.

Say I have a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

To test it, I create a file next to it named `test_add.py`. The name matters. pytest finds tests by looking for files that start with `test_` or end with `_test.py`, and inside them, functions that start with `test_`. That's the whole discovery mechanism.

```python
def test_add():
    assert add(2, 3) == 5
```

This tells pytest to call `add` with 2 and 3, and check that the result is 5. If it is, nothing happens, which is the correct amount of drama for a passing test. If it isn't, pytest shows you exactly what it expected versus what it got, without you writing any extra code to make that happen. `assert` is just the plain Python keyword; pytest rewrites it under the hood to give you a readable failure message.

To run it, from the terminal:

```
pytest
```

pytest scans the current directory, finds `test_add.py`, runs `test_add`, and prints a single green dot, or an F. One test, one character. It feels almost too small to matter. It isn't.

Run it once with a function that fails, on purpose, so you see what a failure looks like before you need to interpret a real one. Change the assert to expect 6 instead of 5, run pytest again, and read the output. You'll see the line that failed, the values on both sides of `==`, and a short traceback. That's the real reason to use pytest instead of writing your own if-statements and print calls. It's already done the work of explaining itself.

This example is deliberately small. Most of what you'll test later is messier: functions that touch a database, code that depends on the current time, things that can fail in more than one way. All of that builds on this same shape, though. Name the file `test_something.py`, name the function `test_something`, assert what should be true, run pytest, read what it tells you.

Start with one function you already trust and write a test that proves it. Then break the function on purpose and watch the test catch you.

---

### Run 4, essay 3 · Aug 20, 5:21 PM

Style match 0.747 · Judge 4/10 · Essayist tells 4/10 · 460 words

> **Judge:** The candidate is a polished literary memoir-essay — atmospheric scene-setting, withheld-detail pacing, and a reflective callback ending — where Kattni writes plain, blunt, step-listed practitioner prose with markdown headings, bulleted kBits, explicit "For example, you would include:" scaffolding, and flat closers, so despite shared first-person technical subject matter the voices read as different authors.

---

I didn't write my first test until years after I'd started writing code other people used. The reasoning that kept me away from it was simple enough: my code worked when I ran it myself, and that felt like proof enough. Then I changed a few lines in a function three weeks after I'd written it, and something else, somewhere else in the same project, quietly broke. I didn't notice for a week. That's when testing stopped being optional in my head.

Pytest is the tool I reached for, mostly because everyone I knew was already using it and because it doesn't ask much of you to get started. You don't inherit from a class or memorize a list of methods. You write a function, name it starting with test_, and inside it make a claim about what should be true using the word assert. If the claim holds, pytest moves on quietly. If it doesn't, pytest tells you exactly what it expected and what it got instead.

Say I have a function that adds tax to a price:

```python
def add_tax(price, rate):
    return price + (price * rate)
```

A first test for it might look like this:

```python
def test_add_tax():
    assert add_tax(100, 0.1) == 110
```

This calls add_tax with a price of 100 and a rate of 0.1, and fails loudly if the result isn't 110. That's the whole test. I saved it in a file named test_something.py (the test_ prefix matters, it's how pytest finds the file at all) and ran pytest from the terminal.

One dot appeared, for the one test that passed. It worked. I remember expecting the moment to feel more significant than it did. A passing test doesn't announce itself. Mine was a single character next to a line saying one test ran in a fraction of a second.

The more useful moment came next, when I broke it on purpose. I changed the 110 in the test to 111 and ran pytest again. Instead of a dot, I got an F, and underneath it, the exact line, the value pytest expected, and the value it actually got. That failure message did more for me than the passing test had. It's the thing that would have told me, three weeks earlier, exactly which function I'd broken instead of leaving me to find it by hand a week later.

If you're starting out, I'd pick one function you already trust and write a single assert against it, nothing more elaborate. You don't need a full test suite on day one; you need one test that fails honestly when the code is wrong. These days that's still how I start most new projects, one function, one assert, before I let myself write anything else.

---

## Baseline with samples

A standalone prompt carrying the same six writing samples, asking the model to match their style. Skill off.

### Run 1 · Aug 19, 6:53 PM

Style match 0.705 · Judge 4/10 · Essayist tells 3/10 · 523 words

> **Judge:** The candidate is warmer, more literary, and more reader-addressing than Kattni's plain step-by-step practitioner voice, leaning on essayist moves she never uses — rhetorical asides ("Ask me how I know."), reflective flourishes ("worth sitting with for a second," "debugging at 11pm"), and an exhortative closing line — instead of her flat "Here is what I found / Done." reporting and structured tutorial scaffolding.

---

I wrote my first pytest test at a point where I already understood, conceptually, what tests were for. I just hadn't sat down and done it. There's a particular kind of resistance that builds up around testing, I think, because it feels like it should be complicated. It isn't. That was the biggest surprise.

pytest asks very little of you to get started. You don't need to inherit from a class, you don't need to register anything, you don't need a special runner configuration to make a simple test work. You write a function whose name starts with `test_`, and inside it, you assert something is true. That's genuinely most of it.

Say you have a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

A test for it might look like this:

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

Save that in a file named `test_add.py`, run `pytest` from the command line in that directory, and it finds the test, runs it, and tells you whether it passed. No imports of a testing framework class, no boilerplate. Just a plain `assert`.

That word, `assert`, is doing all the work, and it's worth sitting with for a second. You're not calling a special `assertEqual` method or anything like that, the way some other testing frameworks require. You're writing a regular Python expression that evaluates to `True` or `False`, and pytest is smart enough to introspect it when it fails and tell you exactly what values didn't match. If `add(2, 3)` had returned `6`, pytest wouldn't just say "assertion failed." It would show you both sides of the comparison, which turns out to be enormously more useful than it sounds when you're debugging at 11pm.

Naming matters here too, in a way I didn't appreciate until I'd written a handful of these. Test files need to start with `test_` (or end in `_test.py`), and test functions need to start with `test_`, because that's how pytest's discovery mechanism finds them. Skip the prefix, and pytest will run right past your test without a word of complaint, and you'll be very confused later about why a bug you know you're testing for isn't getting caught. Ask me how I know.

Once you've written one test, the second one is easy, and the third is easier still, because you're not learning a framework anymore, you're just writing more functions. That's really the appeal of pytest as a starting point: it gets out of your way. You can add fixtures and parametrization and all sorts of more advanced features later, and there's plenty to learn if you want to go deeper. But none of that is required to get real value out of testing on day one.

If you've been putting off writing your first test the way I put off my own, for no better reason than a vague sense that it would be a whole thing, it isn't. Write the function, write the assert, run `pytest`, and see what happens. That's the whole barrier to entry, and it's lower than you think.

---

### Run 2 · Aug 19, 10:48 PM

Style match 0.775 · Judge 6/10 · Essayist tells 5/10 · 496 words

> **Judge:** The candidate borrows real Kattni markers (the kBits list, "90% of what I use day-to-day", plain first-person tutorial voice) but layers on a writerly opener with metaphor ("the vegetables next to the code"), fragment punchlines ("That's the whole test. No setup, no class, no boilerplate."), and a reflective closing line, where the author's own tutorials open flatly with context and close with practical wrap-ups.

---

Title: Writing Your First Test with Pytest

I put off writing tests for embarrassingly long. It always felt like homework tacked onto the actual work, the vegetables next to the code I actually wanted to write. Then I broke something in a script I hadn't touched in months, spent an evening tracking it down by hand, and decided that evening was never happening again. Pytest is where I landed. It's simple enough that you can write something useful in the first five minutes, and that's exactly what got me to stick with it.

##### The kBits

* Install pytest with `pip install pytest`.
* Write a function you want to test, and a separate function, prefixed with `test_`, that checks its behavior using a plain `assert`.
* Save the test file with a name that starts with `test_`, e.g. `test_math.py`.
* Run `pytest` from your terminal in the project directory.

That's genuinely most of it. There's a lot more pytest can do, but this is enough to get you started and to get you comfortable with the shape of things.

##### A First Test

Say you have a function that adds two numbers, sitting in a file called `math_utils.py`:

```python
def add(a, b):
    return a + b
```

To test it, you create a new file, `test_math_utils.py`, in the same directory. The filename matters here; pytest goes looking for files that start with `test_` (or end with `_test`), so if you name it something else, it won't get picked up. Inside, you import the function, and write a second function that starts with `test_`, containing an `assert` statement describing what you expect to be true.

```python
from math_utils import add

def test_add():
    assert add(2, 3) == 5
```

That's the whole test. No setup, no class, no boilerplate. You run it from the command line:

```console
$ pytest
```

And pytest goes off, finds every file and function matching its naming convention, runs them, and reports back. If everything checks out, you'll see a single green dot and a passed count. If something's wrong, pytest shows you exactly which assertion failed, and what the actual value was versus what you expected, without you needing to write any of that reporting yourself.

You can write as many `test_` functions as you like in the file, each checking a different case:

```python
def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5
```

Run `pytest` again, and it picks up all three, no extra configuration needed.

This is easily 90% of what I use day-to-day for smaller projects. Pytest does far more than this once you get into fixtures, parametrization, and plugins, but none of that is necessary to get real value out of it immediately. Start with a function, an assert, and a file name pytest recognizes. Once you've got that rhythm down, the rest starts making a lot more sense, and you'll wonder why you waited so long, same as I did.

---

### Smoke test, essay 1 · Aug 20, 12:42 AM

Style match 0.750 · Judge 4/10 · Essayist tells 3/10 · 504 words

> **Judge:** The candidate is a polished second-person essay with a wry opening hook, fragment punchlines, and a lyrical closing image ("that first green dot... a few lines of code willing to check"), whereas Kattni's tutorials are plainly first-person and procedural, with a kBits bullet summary, "For example, to X, you would include:" scaffolding, and a matter-of-fact wrap-up.

---

Writing pytest for the first time makes some people install five plugins and read a hundred pages of documentation before touching a keyboard. You don't need any of that. Here's enough to get you started.

pytest is a testing framework for Python. A "test" is just a small piece of code that checks whether another piece of code does what you expect it to. You write a function, you write another function that calls the first one and checks the result, and pytest runs the second function for you and tells you whether it passed or failed. That's the whole idea. Everything else is refinement.

Say you have a function called `add` that takes two numbers and returns their sum. It lives in a file called `calculator.py`. To test it, you create a second file, in the same directory, called `test_calculator.py`. The `test_` prefix matters; it's how pytest finds your tests without you having to tell it where to look.

Inside that file, you write:

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

The function name also needs the `test_` prefix, for the same reason the file does. The `assert` keyword is doing the actual checking. If the expression after it evaluates to `True`, nothing happens, and the test passes. If it evaluates to `False`, pytest stops, and shows you exactly what it expected versus what it got.

To run it, you install pytest (`pip install pytest`, or add it to your project's dependencies, however you're managing those), and from your terminal, in the directory containing both files, you run:

```console
$ pytest
```

pytest goes looking through your project for anything matching that `test_` naming convention, runs it, and reports back. One test, one pass, and a small green dot to show for it. Not particularly dramatic, but genuinely satisfying the first time you see it.

The real value shows up later, once you have more than one test. You write a test for what a function should do with normal input, and then you write another for what happens at the edges: zero, negative numbers, an empty string, whatever your function might reasonably be handed. Each one is its own `test_` function, sitting in the same file. Run pytest again, and it runs all of them, one after another, and tells you which ones failed and why.

You don't need to memorize the whole ecosystem of fixtures, parametrization, and plugins to get real use out of this. A file, a function, an `assert`, and a terminal command are enough to start catching mistakes before they become someone else's problem, including future you.

Once you've written a handful of these and gotten comfortable with the rhythm, the rest of pytest's features start making a lot more sense, because you'll actually have a reason to reach for them. But that first green dot doesn't need any of that. It just needs a function that returns what you think it does, and a few lines of code willing to check.

---

### Smoke test, essay 2 · Aug 20, 12:42 AM

Style match 0.686 · Judge 6/10 · Essayist tells 4/10 · 580 words

> **Judge:** The tutorial scaffolding (kBits section, front matter, step headings, "Done.") reads convincingly like Kattni, but the candidate is tighter and punchier than her sprawling, qualifier-heavy prose, and it closes with an imperative slogan-style kicker ("Go write it.") plus several epigrammatic one-liners she wouldn't write.

---

Title: Writing Your First Test with Pytest
Date: 2026-8-20 12:00
Author: Kattni
Tags: Python, Programming, Tutorials, Getting Started
Slug: writing-your-first-test-with-pytest
Summary: An introduction to testing your Python code with pytest
HideTOC: Yes
Status: published

Testing was one of those things I knew I was supposed to be doing, and put off for far longer than I'd like to admit. Writing code that works is one thing. Proving to yourself, and anyone else who touches your project, that it still works after you change something, is another thing entirely. Pytest is a Python testing framework, and it happens to be one of the more approachable ways into the habit. My intent here isn't to cover everything pytest can do, it's to get you to the point where you've written and run one real test.

##### The kBits
Here's what's covered in this tutorial.

* Installing pytest.
* Writing a function to test.
* Writing a test for that function.
* Running the test, and reading the results.

##### Installing Pytest
Pytest isn't part of the Python standard library, so you'll need to install it. In your terminal, with your virtual environment activated, run the following:

```console
$ pip install pytest
```

That's it. You're ready to write a test.

##### Writing a Function to Test
Before you can test something, you need something to test. Create a file called `calculator.py`, and include the following:

```python
def add(a, b):
    return a + b
```

This is deliberately simple. The point of this tutorial isn't the code being tested, it's the testing itself.

##### Writing a Test
Pytest looks for files that start with `test_`, or end with `_test.py`. It looks inside those files for functions that start with `test_`. That's the whole convention, and once it clicks, it makes everything else about pytest make sense.

Create a file called `test_calculator.py`, in the same directory as `calculator.py`, and include the following:

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

There are three things happening here. First, you import the function you're testing. Second, you write a function whose name starts with `test_`, so pytest knows to pick it up. Third, inside that function, you make an assertion, a statement that you expect to be true. If it's true, the test passes. If it's not, pytest will tell you exactly what it expected, and what it got instead.

##### Running the Test
From the directory containing both files, run:

```console
$ pytest
```

You should see something along the lines of the following:

```
collected 1 item

test_calculator.py .                                                   [100%]

1 passed in 0.01s
```

That single dot represents your test passing. Done.

Now, to see what a failure looks like, so you recognize it later, change the assertion in `test_add` to `assert add(2, 3) == 6`, and run pytest again. You'll get a detailed breakdown showing the assertion that failed, and the actual value it received. This is, genuinely, one of pytest's best features. You don't have to write your own error messages, it figures out what went wrong and shows you.

##### Wrap Up
That's a complete, working test. It's small, but it's real, and it's the same fundamental pattern you'll use for far more complicated code: import the thing, call the thing, assert what you expect. From here, you'll want to look into fixtures, parametrization, and organizing tests across multiple files, but none of that matters if you haven't written this first one. Go write it.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:47 AM

Style match 0.722 · Judge 6/10 · Essayist tells 5/10 · 505 words

> **Judge:** The tutorial scaffolding (kBits list, "My intent here is to give you a tour", "Wrap Up", "For example... you would include") lands close to the author's documented voice, but the candidate drifts into a more polished essayist register with fragment punchlines ("A file named right, a function named right, and an `assert`."), an aphoristic closer ("let the rest come to you as you need it"), and evaluative flourishes ("genuinely one of its nicest qualities") that the reference's plainer, step-reporting prose avoids.

---

I wrote my first pytest test this week, and it turns out the whole thing is far less intimidating than the ecosystem around it suggests. There's a lot of noise out there about fixtures, parametrization, plugins, conftest.py hierarchies, and mocking strategies. My intent here is to give you a tour of the actual minimum needed to get a test running, not the whole landscape of what pytest can do.

##### The kBits

* Install pytest into your project's environment.
* Create a file whose name begins with `test_` or ends with `_test.py`.
* Write a function whose name begins with `test_`.
* Use a plain `assert` statement to check the behaviour you expect.
* Run `pytest` from the command line.

##### Installing pytest

pytest is a package like any other. If you're using a `requirements.txt` or a `pyproject.toml` with dependency groups, add it to your `dev` or `test` group. Otherwise, `pip install pytest` into your virtual environment will do it.

##### Naming Your File

pytest discovers tests by convention rather than by configuration, which is genuinely one of its nicest qualities. Name your file `test_something.py`, and pytest will find it automatically when you run the `pytest` command from anywhere in the project. You don't need to register it anywhere.

##### Writing a Function

Inside that file, write a function whose name also begins with `test_`. This is what pytest actually collects and runs; a function named `check_addition` will be silently ignored, no matter how well-written it is.

For example, suppose you have a function elsewhere in your project:

```python
def add(a, b):
    return a + b
```

Your test file would contain:

```python
from mymodule import add

def test_add():
    assert add(2, 3) == 5
```

##### The `assert` Statement

This is the part that surprised me most. There's no special assertion class to import, no `self.assertEqual` ceremony. You write a plain Python `assert`, and pytest rewrites it under the hood to give you a genuinely useful failure message, showing you both sides of the comparison when it fails.

For example, if you had written the test above as:

```python
def test_add():
    assert add(2, 3) == 6
```

Running it would tell you, plainly, that `7 == 6` is false, and show you the actual value produced. No digging required.

##### Running It

From your project root, run:

```console
$ pytest
```

pytest will collect every `test_*.py` file it finds, run every `test_*` function inside them, and give you a summary: how many passed, how many failed, and where.

##### Wrap Up

That's genuinely enough to get you started. A file named right, a function named right, and an `assert`. There is a great deal more available to you once you outgrow this: fixtures for shared setup, parametrize for running the same test against multiple inputs, and a substantial plugin ecosystem for things like coverage reporting. But none of that is required to get real value out of your first test. Start here, get comfortable, and let the rest come to you as you need it.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:47 AM

Style match 0.679 · Judge 4/10 · Essayist tells 3/10 · 510 words

> **Judge:** It borrows surface markers of the author (the kBits list, "you would run the following" tutorial framing, first-person practitioner opening), but drifts into polished-essayist register with a lyrical "Why This Matters" section, fragment punchlines ("That's it. That's the whole test."), an aphoristic closing about the future version of you, and an imperative "Start there" — none of which appear in the reference samples, which end plainly and stay procedural.

---

##### Writing Your First Test with Pytest

I've been putting off learning pytest for embarrassingly long. Every time I ran into someone else's test suite, I'd nod along, quietly hoping I wouldn't be asked to add a test of my own. Recently, working on some BeeWare related code, that hope ran out. So, I sat down and actually learned it. Turns out, the barrier to entry is much lower than I'd built it up to be in my head.

Pytest is a testing framework for Python. What that means, practically, is that it's a tool that runs functions you write, checks whether the things you claimed would be true are actually true, and tells you clearly when they aren't. You don't need to inherit from a class or memorize a bunch of ceremony to get started. You write a function, you name it right, and pytest finds it.

##### The kBits
* Install pytest with `pip install pytest`.
* Create a file whose name starts with `test_`, e.g. `test_math.py`.
* Inside it, write a function whose name also starts with `test_`.
* Use a plain `assert` statement to check the thing you expect.
* Run `pytest` from your terminal in that directory.

##### Writing the Test
Say you have a function that adds two numbers together, in a file called `mymath.py`:

```python
def add(a, b):
    return a + b
```

To test it, you create a new file, `test_mymath.py`, in the same directory. Note the `test_` prefix; pytest uses this to find your tests automatically, so naming matters here more than it might seem like it should.

```python
from mymath import add

def test_add():
    assert add(2, 3) == 5
```

That's it. That's the whole test. You import the function you want to test, you write a function whose name starts with `test_`, and inside it, you assert that the thing you expect to be true, is true.

##### Running the Test
From the directory containing both files, you run the following:

```console
$ pytest
```

Pytest will find `test_mymath.py`, find `test_add` inside it, run it, and report back. If the assertion holds, you'll see a single green dot and a summary telling you one test passed. If it doesn't, pytest doesn't just tell you it failed, it shows you the actual and expected values, right there in the output, so you can see exactly what went wrong without adding a single print statement.

##### Why This Matters
The thing that finally got me to sit down and do this wasn't a deadline, it was watching pytest catch something I'd broken without meaning to, in code I hadn't touched in weeks. That's really the whole point. A test isn't there for the moment you write it, it's there for the version of you six weeks from now who forgot the edge case entirely.

You don't need a plan to test everything in your codebase today. You need one function, one assertion, and a file named correctly. Start there. Everything else, fixtures, parametrization, mocking, can wait until you actually need it.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:48 AM

Style match 0.721 · Judge 6/10 · Essayist tells 5/10 · 551 words

> **Judge:** The tutorial scaffolding (front matter, kBits section, Wrap Up, code blocks) and plain first-person practitioner voice match well, but the candidate leans warmer and more reflective than the reference's procedural directness, with a lyrical thematic closing line, a listy em-dash-free aphorism, and small emotive flourishes ("the mystery mostly evaporated," "a small victory," repeated "genuinely") that the author's own tutorials don't use.

---

Title: Writing Your First Test With Pytest
Date: 2026-8-20 11:04
Author: Kattni
Tags: Python, Programming, Tutorials, Getting Started
Slug: writing-your-first-test-with-pytest
Summary: A gentle introduction to testing your Python code with pytest
HideTOC: Yes
Status: published

For a long time, "testing" was a word that made me a little nervous. It sounded like something only serious, professional developers did, with elaborate frameworks and coverage reports I didn't understand. It turns out, at its most basic, a test is just a small piece of code that checks whether another piece of code does what you expect. Pytest is a Python tool that makes writing and running these checks about as painless as it can be. Once I wrote my first one, the mystery mostly evaporated.

##### The kBits
* Install pytest with `pip install pytest`.
* Write a function to test, in a file, e.g. `add.py`.
* Write a test file, prefixed `test_`, containing functions also prefixed `test_`.
* Use `assert` to check that your function returns what you expect.
* Run `pytest` from the command line.

##### A Function to Test
Say you have a simple function that adds two numbers, saved in a file called `add.py`:

```python
def add(a, b):
    return a + b
```

##### Writing the Test
Pytest works by looking for files and functions that follow a naming convention. Any file beginning with `test_`, and any function within it also beginning with `test_`, will be treated as a test. This is how pytest knows what to run without you having to tell it explicitly.

Create a file called `test_add.py` in the same directory, containing the following:

```python
from add import add

def test_add():
    assert add(2, 3) == 5
```

The `assert` keyword is doing the actual work here. It's a plain Python statement that checks whether the thing after it is true. If it is, nothing happens, and the test passes silently. If it isn't, Python raises an error, and pytest reports it as a failure, along with the values involved. You don't need any special syntax beyond `assert` to write a basic test; this is one of the things that makes pytest so approachable.

##### Running the Test
From the same directory, run:

```console
$ pytest
```

Pytest will find `test_add.py`, run `test_add()`, and report back. A passing test shows up as a single green dot and a summary line telling you one test passed. Genuinely, the first time I saw that, it felt like a small victory.

##### When It Fails
It's worth deliberately breaking your function once, just to see what a failure looks like. Change the `return` line to `a - b`, and run `pytest` again. Instead of a quiet dot, you'll get a readout showing exactly which assertion failed, and what value it got instead of the one it expected. This is, genuinely, the most useful part of the whole exercise: a good failure message tells you precisely where to look, instead of leaving you to go hunting through the rest of your code.

##### Wrap Up
This barely scratches the surface of what pytest can do, but it's the entire foundation. Everything else, fixtures, parametrization, mocking, is built on this same basic idea: write a function, make a claim about it with `assert`, and let pytest tell you whether you were right.

---

### Run 4, essay 1 · Aug 20, 5:23 PM

Style match 0.704 · Judge 4/10 · Essayist tells 3/10 · 488 words

> **Judge:** The candidate captures the author's first-person, practitioner-tutorial subject matter and some habits (code blocks, `$ pytest` console lines, "For example, ... you would" framing), but it reads as a polished personal essay — scene-setting opener, mid-sentence dramatic asides, a reflective emotional arc, and a lyrical encouraging closing line — where Kattni's actual style is flatter, more procedural, and closes with plain wrap-up statements rather than warm sign-off flourishes.

---

I wrote my first pytest test on a Tuesday night, mostly out of guilt. I'd been adding functions to a little project for weeks, and every time I changed something, I'd manually run the script and squint at the output to make sure I hadn't broken anything. That works, right up until it doesn't. I finally sat down to figure out testing properly, and pytest turned out to be far less intimidating than I expected.

Here's the thing nobody tells you up front: a test is just a function. That's it. Pytest doesn't need you to inherit from some special class or register anything in a config file. You write a function whose name starts with `test_`, put it in a file whose name starts with `test_` or ends with `_test.py`, and pytest will find it on its own.

For example, if I had a function called `add` that added two numbers, I might write:

```python
from my_module import add

def test_add():
    assert add(2, 3) == 5
```

That's the whole test. The `assert` keyword is doing the actual work here; if the condition after it is true, nothing happens and the test passes. If it's false, pytest raises an error, and, this is the part that won me over, it tells you exactly what it expected versus what it got, without you having to write a single error message yourself.

To run it, you install pytest, and from your project's directory, you type:

```console
$ pytest
```

Pytest goes looking through your files for anything matching its naming conventions, runs every test it finds, and gives you a nice, short summary: how many passed, how many failed, and, for anything that failed, precisely where and why.

I remember being surprised at how little ceremony was involved. I had assumed, going in, that testing was going to require learning an entirely separate way of thinking about my code. It didn't, really. It required learning to think about my code in terms of "what should this do", and then writing that expectation down as a sentence pytest could check for me. Once I had a handful of these written, I started noticing something: I trusted my own code more. Making a change stopped being a moment of quiet dread and started being something I could verify in a few seconds.

I won't pretend I write comprehensive test suites for everything I touch. I'm still learning what's worth testing and what isn't, and that's a much longer conversation than one blog post can hold. But that first test, the one where I confirmed that two plus three still equals five, was the moment testing stopped being an abstract good idea and became a tool I actually reached for. If you've been putting it off the way I did, I'd encourage you to just write the one function. You'll have a working test suite, however small, before you've finished your coffee.

---

### Run 4, essay 2 · Aug 20, 5:23 PM

Style match 0.713 · Judge 6/10 · Essayist tells 4/10 · 514 words

> **Judge:** The tutorial scaffolding (kBits list, console blocks, step headings, "Wrap Up") and plain first-person practitioner voice match well, but the candidate leans into polished-essayist moves the reference avoids — a narrative hook, fragment punchlines ("Nothing fancy. That's the point." / "Done."), and a thematic callback ending — and lacks Kattni's denser hedged asides, em-dash-free comma stacking, and repetitive procedural cadence.

---

#### Writing Your First Test With Pytest

I put off testing for a long time. It felt like one of those things that other, more disciplined developers did, and that I would get to eventually, once I had more time. Then I broke the same function three times in a row without noticing, and decided that "eventually" needed to become "now." Pytest turned out to be the friendliest way in. Here's what got me from zero to a passing test.

##### The kBits

* Install pytest with `pip install pytest`.
* Create a file whose name starts with `test_` or ends with `_test.py`.
* Write a function whose name starts with `test_`.
* Inside that function, use `assert` to check that something is true.
* Run `pytest` from your terminal.

##### Install Pytest

There's not much to this step. In your project's virtual environment, run:

```console
$ pip install pytest
```

Done.

##### Write a Function to Test

Pytest needs something to test, so let's say you have a small function, saved in `calculator.py`:

```python
def add(a, b):
    return a + b
```

Nothing fancy. That's the point.

##### Write the Test

Pytest finds tests by looking for files and functions with specific names. This is a convention, not a suggestion, so it's worth following exactly.

Create a file called `test_calculator.py` in the same directory. Inside it, import the function you want to test, and write a function whose name begins with `test_`:

```python
from calculator import add

def test_add():
    assert add(2, 2) == 4
```

That `assert` line is the whole test. You're telling pytest, "run this, and if the statement isn't true, something is wrong." No special assertion methods, no setup ceremony. Just a sentence in Python that's either true or it isn't.

##### Run It

From the directory containing both files, run:

```console
$ pytest
```

You should see a single dot, and a line telling you one test passed. If you want more detail about what ran, add `-v`:

```console
$ pytest -v
```

This will list `test_calculator.py::test_add PASSED`, which is a satisfying thing to see the first time.

##### Make It Fail, On Purpose

I'd suggest doing this once, just so you know what it looks like. Change the assertion to something false:

```python
def test_add():
    assert add(2, 2) == 5
```

Run pytest again, and you'll get a full breakdown of what was expected versus what was returned. This readout is, genuinely, one of pytest's best features. You don't have to guess why a test failed; it tells you.

##### Wrap Up

That's really all it takes to get started: a function, an assertion, and a command. Pytest is capable of a lot more than this covers, fixtures, parametrization, plugins for nearly anything you can think of, but none of that matters until you've written the first one. Once you have, adding a second test is just repeating the pattern. And a third. Before long, breaking the same function three times in a row becomes something pytest catches for you, instead of something you find out about later.

---

### Run 4, essay 3 · Aug 20, 5:24 PM

Style match 0.711 · Judge 3/10 · Essayist tells 2/10 · 500 words

> **Judge:** The candidate adopts a warm, polished blog-essayist voice with fragment punchlines ('That's it. That's a test.'), an aphoristic closing couplet, and reader-directed reassurance, where Kattni writes flatter, denser procedural prose with explicit step lists, kBits sections, and matter-of-fact 'Done.' reporting.

---

Writing your first test with pytest is one of those programming milestones that feels bigger in your head than it turns out to be in practice. I remember opening a terminal, typing `pip install pytest`, and then staring at a blank file for a solid five minutes, genuinely unsure where to begin. If you're in that same spot right now, here's what I wish someone had told me.

A test, at its most basic, is simply a function that checks whether your code does what you expect it to do. Pytest, specifically, is a testing framework for Python that makes writing and running those checks about as painless as it gets. You don't need to import a special class or inherit from anything. You just write a function whose name starts with `test_`, and inside it, you make an assertion.

For example, if you had a function called `add` that added two numbers together, your first test might look like this:

```python
def test_add():
    assert add(2, 3) == 5
```

That's it. That's a test. The `assert` keyword is doing all the work here; it simply confirms that whatever follows it evaluates to `True`. If it doesn't, pytest will fail the test and, helpfully, show you exactly what it expected versus what it got.

To run it, you save the function in a file with a name that starts with `test_` (pytest looks for this pattern to know what to collect), and then run `pytest` from your terminal in that directory. You'll get a summary: a green dot or a red F, a pass count, a fail count, and if something went wrong, a readable breakdown of why.

The part that trips people up, myself included, is the instinct to overthink it. You don't need a grand plan for "testing strategy" to write your first one. You need one function, one known input, and one expected output. Test that your `add` function actually adds. Test that your `is_even` function correctly identifies four as even and five as not. Small, obvious things. The confidence you build from watching that first dot turn green is worth more than any elaborate test suite you could design on day one.

Once you're comfortable with that basic shape, pytest opens up a lot more: fixtures for reusable setup, parametrize for running the same test with multiple inputs, and plenty more that I won't get into here, because none of it matters if you haven't written the first one yet.

What I've found, both in learning this myself and in watching others learn it, is that tests stop feeling like an obligation once you've experienced the moment they catch something. You change a line of code, run your tests, and one fails, exactly the one that should have. That's the whole point. It's not about proving your code is perfect; it's about giving yourself a quiet, reliable way to know when it isn't.

Start with one function. Start with one assert. The rest follows from there.

---

## Naive baseline

A standalone prompt asking for "the writing voice of Kattni (a developer and technical writer)", with no samples. Skill off.

### Run 1 · Aug 19, 6:53 PM

Style match 0.597 · Judge 3/10 · Essayist tells 2/10 · 526 words

> **Judge:** The candidate writes as a polished second-person essayist with aphoristic lines, fragment punchlines, em-dash asides, and a lyrical closing image, whereas Kattni writes plainly in first person, reporting concrete steps she took and what happened, with literal transitions and no rhetorical flourish.

---

The first time you write a test, you're not testing code. You're testing a belief — the belief that your function does what you think it does. pytest is a good tool for this because it gets out of your way faster than almost anything else in the Python ecosystem.

Here's the whole ceremony. You have a function:

```python
def add(a, b):
    return a + b
```

You write a file called `test_add.py`, next to it or in a `tests/` folder, and you put this inside:

```python
from mymodule import add

def test_add():
    assert add(2, 3) == 5
```

That's it. No class to inherit from, no `setUp` boilerplate, no decorator you have to remember the name of. A function whose name starts with `test_`, containing a plain `assert`. Run `pytest` from your terminal, and it finds the file, finds the function, runs it, and tells you whether the world matches your expectations.

The part that tends to surprise people coming from other testing frameworks — including, if you've touched Python's built-in `unittest`, your past self — is the assert. You don't call `self.assertEqual(add(2, 3), 5)`. You just write the condition you believe is true, the way you'd say it out loud. If it's false, pytest doesn't just say "AssertionError." It rewrites the assertion at import time so the failure output shows you the actual values on both sides of that `==`, the line of code, the whole picture. You get a debugging session in the output of a failed test, for free, without instrumenting anything yourself.

That matters more than it sounds like it should. The gap between "I wrote a test" and "I write tests" is almost entirely about friction. If checking your work costs you fifteen minutes of framework ceremony, you'll do it once, feel virtuous, and quietly stop. If it costs you four lines and a command you already have muscle memory for, you'll do it every time you touch the function, without having to talk yourself into it.

Start small on purpose. Test one function, one input, one obvious expected output. Don't reach for fixtures, don't reach for parametrize, don't try to cover every edge case in your first file. The goal of your first test isn't coverage — it's building the reflex. Write the function, write the test, watch it pass, then break the function on purpose and watch the test catch you. That last step is the one people skip, and it's the one that actually proves the test is doing anything. A test you've never seen fail is a test you don't actually trust yet.

Once that reflex is in place, the rest of pytest — fixtures for shared setup, `parametrize` for running one test against many inputs, plugins for coverage and mocking and async — stops being a wall of features to learn and starts being a toolbox you reach into exactly when you feel the friction that each piece was built to remove. But none of that is where you start. You start with one function, one assert, and the small, real satisfaction of watching a single green dot appear where you weren't sure one would.

---

### Run 2 · Aug 19, 10:48 PM

Style match 0.676 · Judge 3/10 · Essayist tells 2/10 · 537 words

> **Judge:** The candidate is a polished personal-essay performance — em-dash asides, fragment punchlines ('That was it. That was the whole ceremony.'), reflective callbacks, and a lyrical closing aphorism — whereas Kattni writes flat, procedural, plainly sequenced first-person reporting with explicit step lists, parenthetical definitions, and unshowy wrap-ups.

---

I still remember the first test I wrote with pytest. Not because it was elegant — it wasn't — but because of how anticlimactic it felt. I'd built up this idea that testing was a separate discipline, something senior engineers did in a different mental gear than the one I used to write actual features. Then I typed `def test_add():`, wrote an assertion, ran `pytest`, and watched a single green dot appear in my terminal. That was it. That was the whole ceremony.

That's the first thing worth knowing about pytest: it gets out of your way almost aggressively. You don't need a class. You don't need to inherit from anything. You don't need boilerplate setup just to prove a function returns what you expect. A test is a function whose name starts with `test_`, living in a file whose name starts with `test_`, and inside it you write plain `assert` statements. No `assertEqual`, no `assertTrue` — just `assert result == 4`, the same comparison you'd write anywhere else in Python. That plainness is a design decision, not a lack of features, and it's the reason pytest feels less like learning a framework and more like writing code you already know how to write.

The second thing worth knowing is that failure output is where pytest actually earns its reputation. When your assertion fails, pytest doesn't just tell you `False`. It rewrites the assertion at runtime to show you both sides — the value you got, the value you expected, sitting right next to each other in the terminal. The first time I saw that, I understood why people don't reach for `unittest` by default anymore. Debugging a failing test shouldn't require adding print statements to figure out what actually happened; the test runner should just tell you.

If you're writing your first one, resist the urge to test something trivial just to see the mechanism work, and then stop there. Pick a function in your own code that does something you'd be annoyed to have silently break — a date parser, a discount calculator, whatever handles an edge case you already got bitten by once. Write the test around the behavior you actually care about preserving. That's the difference between a test that proves pytest works and a test that proves your code works, and only one of those is worth keeping around.

Don't reach for fixtures or parametrize or mocking on day one. Those are real and you'll want them soon — fixtures especially, once you're tired of repeating setup code across tests — but they're layer two. Layer one is just: function, assert, run `pytest`, read what it tells you. Get comfortable with that loop first. Everything pytest adds on top is in service of making that same loop scale, not replacing it.

What surprised me most, looking back, is how much writing tests changed how I wrote the code being tested. Functions got smaller. Side effects got easier to spot because they got harder to test around. That wasn't the goal when I wrote that first `test_add` — I just wanted the green dot. But the habit sneaks up on you, which might be the actual argument for starting today instead of someday.

---

### Smoke test, essay 1 · Aug 20, 12:43 AM

Style match 0.630 · Judge 3/10 · Essayist tells 2/10 · 502 words

> **Judge:** The candidate is a polished second-person essay full of em-dash asides, fragment punchlines, imperative hooks, and a lyrical aphoristic closer, whereas Kattni writes plain, orderly first-person practitioner prose with explicit step lists, literal "Done." beats, and matter-of-fact wrap-ups.

---

I've never forgotten the first time a test actually failed the way it was supposed to. Not crashed, not thrown some cryptic traceback about a missing import — failed, cleanly, with a message that told me exactly what I'd broken. That's the moment pytest clicks for you, and it usually happens faster than you expect.

Start small. Don't open a tutorial that walks you through fixtures, parametrization, and conftest.py before you've written a single assert. Pick one function in your codebase — something with a clear input and output, nothing that touches a database or the network — and write the dumbest possible test for it.

```python
def test_add():
    assert add(2, 3) == 5
```

That's it. That's a real test. Save it as `test_add.py`, run `pytest` from your terminal, and watch it go green. There's a particular satisfaction in that first passing run, partly because pytest doesn't make you work for it. No test classes to inherit from, no boilerplate `self.assertEqual` — just a function name starting with `test_` and a plain `assert`. The framework gets out of your way, which is exactly what you want when you're still building the habit.

Now break something on purpose. Change the assertion to `assert add(2, 3) == 6` and run it again. Read the failure output closely — this is the part people skip, and it's the part that actually teaches you something. Pytest doesn't just tell you the assertion failed; it shows you both values, side by side, so you can see the gap between what you expected and what you got. That diff is doing real work for you. Get comfortable reading it now, before your tests get complicated, so it's second nature later when you're staring at a failure in CI at 5pm on a Friday.

A word on what to test first: resist the urge to test everything. Pick the function that scares you a little — the one with an edge case you're not fully sure you handled, or the one you keep manually checking by hand every time you touch it. That's the test that pays for itself immediately. Testing `add(2, 3)` is a fine warm-up, but the real value shows up when you write `test_add_handles_negative_numbers` and it catches a bug before a user does.

One more thing worth saying plainly: your first test doesn't need to be good. It doesn't need a fixture, it doesn't need to be parametrized, it doesn't need to follow whatever structure your team's more experienced testers use. It needs to run, and it needs to tell you something true about your code. Everything else — the `@pytest.fixture` decorators, the `tmp_path` argument, the marks and plugins — is stuff you'll reach for naturally once you hit a problem it solves. Let the pain point introduce you to the feature, not the other way around.

Write the test. Run `pytest`. Watch it pass, then watch it fail. That loop, repeated a thousand times over a career, is most of what testing actually is.

---

### Smoke test, essay 2 · Aug 20, 12:43 AM

Style match 0.668 · Judge 3/10 · Essayist tells 2/10 · 480 words

> **Judge:** The candidate reads as a polished essayist — em-dash-heavy cadence, second-person directives ("Resist it."), an aphoristic aside ("The syntax is five minutes of documentation."), and a lyrical closing about trusting the tool — where Kattni writes plainly and procedurally in first person, reporting what she did with literal step lists, "For example, to X, you would include:" scaffolding, and flat wrap-up sections rather than rhetorical flourish.

---

The first time I wrote a test with pytest, I remember being surprised by how little ceremony it demanded. No boilerplate class to inherit from, no `setUp` and `tearDown` rituual, no import of some heavyweight assertion library. Just a function, prefixed with `test_`, and a plain `assert` statement. That simplicity is the whole point, and it's worth sitting with before you write a single line.

Say you have a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

Your test file — call it `test_add.py`, because pytest discovers files by that naming convention — looks like this:

```python
from add import add

def test_add():
    assert add(2, 3) == 5
```

Run `pytest` from your terminal, and it finds the file, finds the function, runs it, and reports pass or fail. There's no configuration required to get here. That's deliberate, and it's one of the reasons pytest won out over more ceremonious frameworks: it gets out of your way until you need it to do something more.

The instinct when you're new to this is to reach for `self.assertEqual` or some equivalent, because that's what testing "looks like" in other languages and frameworks you've encountered. Resist it. Pytest's plain `assert` is not a simplification for beginners — it's the actual design. Under the hood, pytest rewrites your assert statements so that when one fails, you get a real, useful diff: what was expected, what you got, and where they diverged. You don't lose diagnostic power by writing plain Python; you gain it, because you're not memorizing a vocabulary of `assertEqual`, `assertIn`, `assertIsInstance` — you just write the boolean expression that describes what should be true, and let pytest do the explaining when it isn't.

The other thing I'd tell someone writing their first test: pick something real, not something trivial you invented to satisfy an exercise. Test a function you actually wrote for actual work, ideally one with a bug you already suspect or a behavior you're not fully sure of. First tests written against toy examples teach you the syntax but not the reflex — the habit of asking "what should this return, and does it?" before you trust your own code. That reflex is the actual skill. The syntax is five minutes of documentation.

Once you've written one test, the natural next question is what happens when your function needs different inputs to prove it's correct — and that's where `@pytest.mark.parametrize` earns its keep, letting you run the same assertion against a table of cases instead of copy-pasting `test_add_negative`, `test_add_zero`, and so on. But that's a lesson for your second test, not your first.

Write the one function. Write the one assert. Run it, watch it fail on purpose by breaking your code temporarily, then watch it pass again. That failure-then-pass cycle, more than the syntax, is what teaches you to trust the tool.

---

### Run 3 (interrupted), essay 1 · Aug 20, 12:49 AM

Style match 0.545 · Judge 3/10 · Essayist tells 2/10 · 523 words

> **Judge:** The candidate is a polished second-person motivational essay full of em-dash aphorisms, sentence fragments, and a lyrical closing slogan, whereas Kattni writes plainly in first person, reporting concrete steps she took and what happened with methodical, unadorned prose.

---

Writing your first test with pytest feels like a small thing right up until it isn't. You install pytest, you write a function that starts with `test_`, you type `assert` followed by something you already believe to be true, and you run `pytest` from the command line. Green dot. Done. It's almost anticlimactic — which is exactly the point.

Here's what nobody tells you clearly enough when you're starting out: a test is not a ceremony. It's not a hoop you jump through because someone on your team said "we need coverage." A test is a question you're asking your code, phrased in a way the code can answer back. `assert add(2, 2) == 4` isn't decoration. It's you, in writing, saying "I believe this is true," and pytest saying "let's find out."

That's why pytest, specifically, is such a good place to start. You don't need a class. You don't need to inherit from `unittest.TestCase` and remember six `self.assertEqual` variants. You write a function, you use the plain `assert` keyword you already know from every other Python program you've written, and pytest does the introspection for you — when something fails, it shows you the actual values, side by side, without you having to ask for them. That's not a small convenience. That's the difference between a tool that fights you and one that gets out of your way.

Start absurdly small. Test a function that adds two numbers. Test that an empty list returns zero. Test the boring, obvious case first, because the first thing you're learning isn't really about your code — it's about the rhythm. Write function, run pytest, watch it pass, then deliberately break something and watch it fail. That failure is the more important run. If you've never seen your test fail on purpose, you don't actually know it's testing anything. A test that has never failed is a test you haven't earned trust in yet.

Then let the real value show up: the moment you write a test for a bug you just fixed. That's when pytest stops being an exercise and becomes a colleague. You had a bug, you understood why it happened, and now you've written down that understanding in a form the computer can check forever, automatically, without you having to remember it exists. Six months from now, when you've forgotten the details entirely, that test will remember for you.

You don't need fixtures yet. You don't need parametrize, or mocking, or conftest.py, or any of the machinery that makes pytest genuinely powerful for large codebases. All of that is real and worth learning, but it's not where you start, and it's not what makes testing valuable. What makes testing valuable is the habit of stating your assumptions out loud and letting something other than your own belief check them.

So write the small one. `def test_something(): assert something == what_you_expect`. Run it. Break it on purpose. Watch it fail loudly and clearly. That loop — belief, check, break, fix — is the entire discipline in miniature. Everything else pytest offers is just more elegant ways to do that same thing at scale.

---

### Run 3 (interrupted), essay 2 · Aug 20, 12:49 AM

Style match 0.623 · Judge 3/10 · Essayist tells 2/10 · 504 words

> **Judge:** The candidate adopts a polished second-person essayist voice with em-dash asides, imperative staccato fragments, a rhetorical question, and a lyrical closing beat, whereas Kattni writes plainly first-person, narrating what she did and enumerating steps with flat declaratives and 'For example, ... you would include:' scaffolding.

---

I remember the first time someone told me to "just write a test for it" and I nodded like that meant something to me. It didn't. I'd been writing Python for a while, shipping things that mostly worked, and testing felt like a chore reserved for people more disciplined than me. Then I actually sat down with pytest, and it turned out to be one of the least intimidating things I'd learned that year.

Here's the thing nobody tells you up front: pytest doesn't want you to learn a framework. It wants you to write a function. That's it. No boilerplate class inheriting from `TestCase`, no `setUp` and `tearDown` ceremony unless you ask for it. You write a function whose name starts with `test_`, you put an `assert` in it, and you run `pytest`. If the assertion is true, you get a green dot. If it's false, pytest tells you exactly what went wrong, values and all, without you writing a single custom error message.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 2) == 4
```

That's a real test. It's not a toy example you'll throw away — it's the actual shape of testing you'll do for years, just applied to more interesting functions later. I think this is what trips people up when they come from other languages or other frameworks: they expect testing to require a bigger mental model before they're allowed to start. pytest lets you start before you understand it, and the understanding catches up.

The part I'd tell my past self to pay attention to is the failure output. Run that test with a bug — say `add` returns `a - b` — and pytest doesn't just say "assertion failed." It shows you the expression, the actual values, the whole comparison, right there in the terminal. That readable failure output is doing more to teach you how your code behaves than most documentation will. Read it. Don't skim past it to fix the bug and move on — actually read what pytest is telling you happened.

Once you've written that one test, resist the urge to immediately reach for fixtures, parametrize, mocking, plugins — the whole ecosystem that makes pytest genuinely powerful for large codebases. It's tempting because the docs are right there and it all looks useful. But your first test's job isn't to be impressive. Its job is to get you into the habit of asking "what do I expect this code to do?" before you ask "does it do that?" Everything else — fixtures for shared setup, parametrize for testing many inputs at once, `pytest.raises` for exceptions — is just vocabulary you'll pick up naturally once that question becomes automatic.

Write the function. Name it `test_something`. Assert something true about your code. Run `pytest`. Watch it pass, then break it on purpose and watch it fail, so you know what failure looks like before you're debugging something real at 11pm. That's the whole first lesson, and it's enough to start.

---

### Run 3 (interrupted), essay 3 · Aug 20, 12:50 AM

Style match 0.642 · Judge 3/10 · Essayist tells 2/10 · 539 words

> **Judge:** The candidate reads as a polished tech-essayist — em-dash-heavy reflective asides, second-person coaching, an embedded rhetorical question, and a lyrical thematic closer about testing "feeling like a conversation with your own code" — rather than Kattni's plain, procedural first-person reporting with short declaratives, explicit step lists, and matter-of-fact wrap-ups.

---

The first time I wrote a pytest test, I didn't feel like I was writing a test at all. I was writing a function that happened to start with `test_`, and that was, somewhat suspiciously, the whole trick.

I'd come from environments where "writing a test" meant importing a framework, subclassing something, and calling `self.assertEqual` inside a method that lived inside a class that lived inside a file with its own ceremony. Pytest doesn't ask for any of that. You write a plain function. You use the plain `assert` keyword you already know. That's it.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Save that as `test_add.py`, run `pytest`, and you get a green dot. No boilerplate, no inheritance, no framework-specific assertion vocabulary to memorize. The bar to writing your first test drops to almost nothing, and that's not a minor convenience — it's the whole point. A testing tool that's annoying to start using is a testing tool that gets skipped when you're in a hurry, which is exactly when bugs like to sneak in.

What surprised me most, once I got past that first green dot, was how much pytest does with plain assert statements when something fails. Run `add(2, 2)` against an expectation of `5` and pytest doesn't just tell you the assertion failed — it shows you both sides of the comparison, rewritten and laid out so you can see exactly what went wrong. No `assertEqual(a, b, msg)` required, no custom message to write yourself. The failure output does the explaining. That's a small thing that compounds into a real shift in how much friction there is between "something broke" and "I understand why."

The other thing I'd tell someone writing their first test: don't overthink what deserves one. Your first test doesn't need to cover an edge case or a tricky bit of business logic. Test the function you just wrote, the one you're least sure about, or the one that bit you last week. The goal at the start isn't coverage — it's building the habit of asking "how would I know if this broke?" before you move on to the next thing.

Once you've got a handful of `test_*` functions in a `test_*.py` file, pytest will find them on its own — no registry, no explicit test suite to assemble. Just run `pytest` from your project root and it goes looking. That auto-discovery is easy to take for granted, but it's what makes tests feel like a natural extension of the code instead of a separate system you have to maintain in parallel.

Eventually you'll want fixtures, parametrization, marks for skipping or grouping tests — pytest has real depth once you need it. But none of that is required to get value on day one. The first test you write should be small, a little boring, and mostly there to prove to yourself that the loop works: write code, write an assertion, watch it pass, then watch it fail on purpose just to make sure it's actually checking something. That loop, once it clicks, is the whole reason testing stops feeling like a chore and starts feeling like a conversation with your own code.

---

### Run 4, essay 1 · Aug 20, 5:24 PM

Style match 0.673 · Judge 3/10 · Essayist tells 2/10 · 494 words

> **Judge:** The candidate is a polished personal-essay voice—em-dash asides, reflective anecdote framing, rhetorical questions to the reader, fragment punchlines, and a lyrical aphoristic close ("Everything else is scaffolding")—whereas Kattni writes plain, stepwise practitioner prose with literal explanations, bulleted kBits, and matter-of-fact wrap-ups.

---

I remember the first time someone told me testing would "just click" once I wrote one. It didn't, not immediately. What clicked was smaller and less dramatic: I stopped treating tests as a chore bolted onto the end of writing code and started treating them as a second, more honest way of describing what my code was supposed to do.

pytest makes that first step unusually painless, which is part of why I recommend it to anyone writing Python. You don't need a class. You don't need to inherit from anything. You don't need to memorize a vocabulary of `assertEqual` and `assertTrue` and `assertIsInstance`. You write a function, you use the word `assert`, and pytest figures out the rest.

Here's the whole thing:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run `pytest` in that directory and it finds the function — because it starts with `test_` — runs it, and tells you whether the assertion held. That's it. No boilerplate, no setup ceremony. If it fails, pytest doesn't just say "assertion failed," it shows you the actual values on both sides of that `==`, which sounds like a small thing until you've spent an afternoon squinting at a traceback trying to figure out what a bare `AssertionError` actually meant.

The temptation, once you've written that first test, is to feel like you've done the job and move on. I'd push back on that a little. The value of a first test isn't the test itself — it's the habit it starts. Write the test next to the function you just wrote, while the intent is still fresh in your head. Not after, when you've moved on to the next thing and have to reconstruct what "correct" was even supposed to mean. That reconstruction is where most bad tests come from: ones that test whatever the code happens to do rather than what it should do.

A few things I wish someone had told me early: name your test functions like sentences, not labels. `test_add` is fine for a five-minute example, but `test_add_returns_sum_of_two_positive_integers` tells you, months later, exactly what broke and why it mattered. Test the edge first, not just the happy path — what does `add` do with negative numbers, with floats, with nothing at all? And don't reach for mocks or fixtures on day one. pytest has powerful tools for both, but if you bring in `conftest.py` and dependency injection before you've internalized the basic rhythm of "arrange, act, assert," you'll spend your first week fighting the framework instead of learning it.

The real payoff isn't the first green checkmark, satisfying as that is. It's six months from now, when you change that `add` function to handle a new case, run `pytest`, and get an immediate, specific answer to the question that actually matters: did I just break something that used to work? That question is why the test exists. Everything else is scaffolding.

---

### Run 4, essay 2 · Aug 20, 5:25 PM

Style match 0.664 · Judge 4/10 · Essayist tells 3/10 · 512 words

> **Judge:** The candidate is competent instructional writing but reads as a polished essayist — em-dash asides, fragment punchlines ("Just a function:", "That's it."), colon-driven rhythm, and a thematic closing line — where Kattni writes plainer, more literal step-by-step prose with "For example, to X, you would include:" scaffolding, bulleted kBits, explicit parenthetical definitions, and flat wrap-ups.

---

Here's your first test with `pytest`. Let's say I'm testing a simple `add` function:

```python
def add(a, b):
    return a + b
```

I'll create a file, `test_add.py`. That naming matters — pytest goes looking for files that start with `test_` (or end in `_test.py`), and inside those, functions that start with `test_`. No decorators, no boilerplate class, no `import unittest` ceremony. Just a function:

```python
from mymodule import add

def test_add():
    assert add(2, 3) == 5
```

That's it. Run `pytest` from your terminal, and it finds the file, finds the function, runs it, and tells you whether it passed. No test runner to configure, no suite to register. This is the part that got me when I first tried it — I'd come from a background where "writing a test" meant a fair amount of setup before you got to write anything resembling the actual check. pytest strips that down to: write a function, assert something, done.

The `assert` keyword is doing more work here than it looks like. In plain Python, `assert` just raises an `AssertionError` if the condition is false. pytest hooks into that and, when a test fails, shows you exactly what values were on each side of the comparison — not just "AssertionError," but `assert 4 == 5`, with the actual and expected values spelled out. You don't need special assertion methods like `assertEqual` or `assertTrue`. You write the condition the way you'd write it in any other Python code, and pytest does the introspection for you.

A few things I'd tell someone writing their very first test:

Name it for what it verifies, not for the function it calls. `test_add` is fine for a single trivial case, but once you're testing edge cases, `test_add_handles_negative_numbers` or `test_add_returns_zero_for_empty_inputs` will save you time later, when a test fails in CI and you want to know what broke without opening the file.

Test one thing per test. It's tempting to cram several assertions into one function to "save time," but when one of them fails, you want the test name and the traceback to tell you immediately what's wrong — not force you to scroll through five assertions to find the one that didn't hold.

Don't reach for fixtures or `conftest.py` on day one. They're genuinely great once you have shared setup across many tests, but for your first test, a plain function with a plain `assert` is not a simplified version of "real" pytest — it's how a huge amount of production test code actually looks. Complexity should show up because your code demands it, not because you assume you'll need it eventually.

And run it often. That's the actual habit worth building — not "know pytest," but reflexively run your tests after every small change, so failures show up while the change is still fresh in your head rather than three commits later.

That's the whole loop: write a function, assert something true, run `pytest`, read what it tells you. Everything else you'll learn — fixtures, parametrize, markers — is built on top of that same loop.

---

### Run 4, essay 3 · Aug 20, 5:25 PM

Style match 0.671 · Judge 3/10 · Essayist tells 2/10 · 548 words

> **Judge:** The candidate is a polished reflective essay — em-dash asides, aphoristic reframings ("a second, more honest description of what your code does"), a call-to-action closing, and a "That's the whole thing" fragment punchline — where Kattni writes plain, procedural, first-person "here is what I did, here are the steps" prose with kBits lists, literal transitions, and unsentimental endings.

---

No existing memory to draw on. Here's the essay.

---

The first time I wrote a test, I didn't think of it as writing a test. I thought of it as proving to myself that a function did what I claimed it did in the docstring above it. That distinction turned out to matter more than any of the syntax I learned that week.

pytest makes this an easy habit to start, because it asks almost nothing of you up front. No boilerplate class inheriting from some TestCase, no setUp and tearDown ceremony unless you want it. You write a function whose name starts with `test_`, you put an `assert` statement inside it, and that's a test. Run `pytest` from the command line, and it finds that function on its own.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

That's the whole thing. No imports beyond what your code already needs, no special assertion methods to memorize — just `assert`, the keyword you already know from a hundred debugging sessions. That's the detail that made pytest click for me: it didn't ask me to learn a new vocabulary for a concept I already understood. I already knew how to state a fact about my code and check whether it was true. pytest just gave that habit a place to live and a command to run it.

The other thing that won me over was the failure output. Run that test with a bug in `add` — say it returns `a - b` — and pytest doesn't just tell you `AssertionError`. It shows you the actual values on both sides of the comparison, right there in the terminal, no print statements required. The first time I saw that, I remember thinking: oh, this is going to save me a lot of debugging later. And it has.

If you're writing your first test, resist the urge to reach for anything advanced right away. Skip fixtures, skip parametrize, skip mocking. Write one function, write one assert, and run it. Watch it pass. Then break your code on purpose and watch it fail, so you know what failure looks like before you're relying on it to catch something real. That single loop — write, pass, break, fail, fix — is the whole discipline in miniature, and everything pytest adds later (fixtures for shared setup, parametrize for testing many inputs at once, marks for organizing suites) is in service of that same loop, just at scale.

What I'd tell anyone starting out is this: a test isn't a chore you do after the real work. It's a second, more honest description of what your code does — one that can't drift out of sync with reality the way a comment can, because if it does, it turns red and tells you. That's the whole value proposition. Not perfection, not full coverage on day one, just a small, running record of what you already believe to be true about your code, that checks itself.

Write one test today. Not a suite, not a strategy — one function, one assert. The rest of pytest will still be there tomorrow, and you'll have a much easier time learning it once you've felt that first green pass for yourself.

---

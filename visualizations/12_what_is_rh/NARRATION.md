# Narration script: "What is the Riemann Hypothesis?"

Spoken-narration script for the explainer in `what_is_rh.py`. The video already
shows this narration as on-screen subtitles, so it plays as a self-contained
silent video. This document is for recording a voiceover, or for reading along.

How to read this script:
- Each beat has the SHORT on-screen text (what appears as the headline / labels),
  a [VISUAL] cue (what is on screen), and the NARRATION (the words to speak).
- Durations are approximate. The video paces each subtitle to its length, so the
  real timing tracks the narration closely.
- Pronunciation note: "Euler" is said "Oiler", not "Yoo-ler".
- Total run time is about 7 to 8 minutes across the four parts.

Render the four parts and concatenate (low quality for a quick look, `-qh` for final):

```powershell
manim -qm visualizations/12_what_is_rh/what_is_rh.py Part1_Primes
manim -qm visualizations/12_what_is_rh/what_is_rh.py Part2_Machine
manim -qm visualizations/12_what_is_rh/what_is_rh.py Part3_MapAndZeros
manim -qm visualizations/12_what_is_rh/what_is_rh.py Part4_Hypothesis
```

---

## Part 1 - The Primes and Their Mystery

### Beat 1. The Building Blocks (approx 28 s)
On screen: "The atoms of numbers" / `2 3 5 7 11 13 ...` / `12 = 2 x 2 x 3`
[VISUAL] The primes glow in a row. 12 splits into little atom-like balls labeled 2, 2, 3.

> Let's start with a special kind of number. A whole number is a counting number like 1, 2, 3, with no fractions or pieces. Some whole numbers can't be made by multiplying smaller whole numbers together. Two, three, five, seven, eleven. The only way to reach them by multiplying is one times the number itself. Every other number is built by multiplying these together. Twelve is two times two times three. Just like every object is built from a small set of atoms, every number is built from these. Mathematicians call them prime numbers.

### Beat 2. They Look Random (approx 24 s)
On screen: "Where is the next one?"
[VISUAL] A number line. Prime dots light up one at a time at uneven gaps, a question mark past the last one.

> Now look at where the primes actually fall. Two, three, a gap, five, seven, a bigger gap, eleven. They seem scattered, like raindrops landing on pavement with no steady beat. The higher you count, the rarer they get, but never in a neat way you can predict ahead of time. For a long time, finding a simple rule for the next prime looked hopeless.

### Beat 3. The Counting Staircase (approx 30 s)
On screen: "A ragged staircase"
[VISUAL] A staircase builds left to right: one step up at each prime. Clearly irregular.

> So instead of asking where each prime lands, let's just count them. Walk along the numbers from left to right, and every time you pass a prime, take one step up. Two, step. Three, step. Five, step. What you draw is a staircase that keeps climbing. The steps come at uneven moments, so it climbs in a ragged, jumpy way. The whole mystery of the primes is really a question about the shape of this one staircase.

### Beat 4. A Smooth Shadow (approx 26 s)
On screen: "The mystery is the wiggle"
[VISUAL] A smooth curve fades in over the staircase; the steps stay close to it.

> Here is the first piece of magic. Zoom out, and that jagged staircase closely follows a smooth, graceful curve. A curve is just a gently bending line. The individual steps are unpredictable, but their overall shape is not. On average, we know roughly how fast the primes thin out, so the average is tame and well behaved. The real mystery is the wiggle: how far the true staircase is allowed to wander above and below that smooth curve.

---

## Part 2 - The Machine

### Beat 5. A Number Machine (approx 26 s)
On screen: "A number machine" / IN / OUT
[VISUAL] A friendly box with an in-slot, an out-slot, and a knob. A 3 drops in the top, a number comes out the bottom.

> To tame the wiggle, mathematicians built a special tool. Picture a box with a knob on the front. You feed a number in one side, and the box does some arithmetic and hands you a number back out the other side. That's the whole idea. Mathematicians have a fancy word for a machine like this. They call it a function. But really, it's just a box that turns one number into another.

### Beat 6. Inside the Machine (approx 32 s)
On screen: "The pieces settle on a total" / `1/2 + 1/4 + 1/8 + ...`
[VISUAL] The fractions stack, and a dot on a 0-to-1 line creeps toward 1 and stops.

> Here is what is inside our machine. It adds up a never-ending list of fractions. A fraction is just a piece of a whole, like a half or a quarter. The knob controls how fast those fractions shrink as you go along the list. Turn it the right way, and the pieces get tiny so quickly that the whole endless sum settles on a single finite total instead of growing forever. A half plus a quarter plus an eighth, halving forever, creeps up toward one and stops there. That settled total is the number that comes out. Mathematicians call this machine the zeta function.

### Beat 7. The Secret Recipe (approx 32 s)
On screen: "Same machine, two recipes" / "two recipes, the same cake"
[VISUAL] The endless-sum recipe on the left, a primes-only recipe on the right, an equals sign between them.

> Now the surprise that started everything. Long ago, a mathematician named Euler, whose name sounds like Oiler, discovered that this exact same machine can be rebuilt a completely different way, using only the prime numbers, combined in a special pattern. Two recipes, the endless sum and a recipe made purely of primes, always give the identical answer. Like two different recipes that bake the exact same cake. So this quiet adding machine secretly carries all the primes inside it. That is why studying the machine means studying the primes.

---

## Part 3 - The Map and the Zeros

### Beat 8. Inputs Become Map Points (approx 28 s)
On screen: "Inputs as points on a map" / "how far right" / "how far up"
[VISUAL] A flat grid. A dot is placed by an arrow right, then an arrow up, landing on a labeled spot.

> To get the real power out of the machine, we feed it a richer kind of input. Instead of a single number on a line, picture a spot on a flat map. You go a little to the right, then a little up, and that pair of moves names a place, the way a square on a board game is named by how far across and how far up it sits. A two-part input like that is called a complex number. You don't need the details. Just picture the knob roaming a flat map, and for every spot, the machine still hands back one answer.

### Beat 9. What Is a Zero? (approx 26 s)
On screen: "A zero: the machine goes silent" / answer: 0
[VISUAL] A probe dot glides up the map. At special spots the answer flashes 0 and a bright marker drops.

> Now we go hunting. At most spots on the map, the machine hands back some ordinary number. But at certain rare spots, the answer comes out as exactly zero. The machine goes completely silent. These silent spots are the heart of the whole mystery. Mathematicians call them the zeros of the machine. And it turns out these zeros are exactly what control the wiggle in our ragged prime staircase.

### Beat 10. The Zeros Live in a Strip (approx 26 s)
On screen: "They all hide in one strip" / "one fenced lane"
[VISUAL] A highlighted up-and-down band on the map; the zero-dots appear only inside it.

> When mathematicians marked these zero spots on the map, the interesting ones didn't scatter everywhere. They all fell inside one narrow up-and-down strip, like footprints found only within a single fenced-off lane. So the search shrinks. We no longer scan the whole map, just this one tall, thin band. And that already feels suspiciously orderly for something tied to the wild, random-looking primes.

### Beat 11. The Line Down the Middle (approx 28 s)
On screen: "They sit on the center line" / "the critical line" / "exactly halfway across"
[VISUAL] A straight up-and-down line through the middle of the band; the zero-dots snap onto it like beads on a wire.

> Here is the jaw-dropping part. Draw one perfectly straight up-and-down line right down the middle of that strip, exactly halfway between its two edges. Every single zero anyone has ever found, and we have checked many billions, sits balanced right on that line, like beads threaded on one perfectly straight wire. Not near it. On it. Mathematicians call this the critical line.

---

## Part 4 - The Hypothesis, and Why It Matters

### Beat 12. The Riemann Hypothesis (approx 32 s)
On screen: "The Riemann Hypothesis" / "EVERY zero is on the line" / "still unproven"
[VISUAL] A wire of beads extends upward. One bead drifts off, gets a red X and a question mark, then snaps back.

> And that is the Riemann Hypothesis. A hypothesis is just an educated guess that has not yet been proven. It is one bold claim: that every last one of these zeros, not just the billions we have checked but all of them, going on forever, sits exactly on that center line. No stragglers, no exceptions, ever. We have tested billions and they all obey. But checking a lot is not the same as proving it for every single one. Nobody has found an exception, and nobody has proven there couldn't be one. That gap is the whole problem.

### Beat 13. The Zeros Are Waves (approx 28 s)
On screen: "The zeros are like sheet music" / "each zero = one wave" / "the prime staircase"
[VISUAL] A few gentle waves on the left, an arrow, the jagged prime staircase on the right.

> So why does anyone care? Remember the wiggle in our staircase. Each of those zeros acts like a single gentle wave on water. And when you add all those waves together, they reproduce the ragged prime staircase exactly, step for step. The zeros are like the sheet music, and the primes are like the song it plays. So where the zeros sit isn't a curiosity. It sets the deepest rhythm of the primes.

### Beat 14. On the Line Means No Wobble (approx 30 s)
On screen: "On the line means no wobble"
[VISUAL] Split screen. Top: zeros on the line, primes ticking a steady even beat. Bottom: one zero off the line, the prime ticks bunching unevenly.

> Now the stakes are clear. If every zero sits dead on the center line, the waves stay perfectly balanced, and the primes are spread out as smoothly and evenly as they could ever possibly be, like a steady, well-tuned drumbeat. But if even one zero slipped off the line, it would mean a hidden wobble in that rhythm, a secret clump or gap in the primes. So the Riemann Hypothesis is really a promise that the primes hold their beat with no wobble.

### Beat 15. Still Open, Still Chased (approx 32 s)
On screen: "Open for over 160 years" / "written down in 1859" / "we are here"
[VISUAL] A mountain with a cloud at the peak; a small flag planted partway up. The view settles, then the title returns.

> Riemann wrote this down back in 1859, and more than a hundred and sixty years later, no one has proven it, and no one has found a single zero off the line either. It is one of the most famous unsolved problems in all of mathematics. But it isn't a locked door. It's a summit, and people are still climbing toward it, one careful step at a time. And now you know what they are reaching for, and why a few quiet dots on a map could hold the deepest secret of the numbers themselves.

---

## Glossary (plain definitions)

- **Whole number**: a plain counting number like 1, 2, 3, with no fractions or pieces.
- **Prime number**: a whole number bigger than 1 that can't be made by multiplying smaller whole numbers together (2, 3, 5, 7, 11...). The building blocks of all numbers, like atoms.
- **Prime-counting staircase**: a picture made by stepping up by one each time you pass a prime. Its height tells you how many primes you have passed so far.
- **Function**: a machine with a knob: put a number in, and exactly one number comes out.
- **Zeta function**: the machine of this story. One recipe adds an endless list of shrinking fractions; a second recipe builds the same answer using only primes, so it secretly contains the primes.
- **Settles on a total (converges)**: when an endless sum of ever-shrinking pieces stops growing and lands on a single finite total, the way a half plus a quarter plus an eighth, on forever, creeps up to one.
- **Complex number**: a two-part input pictured as a spot on a flat map: go some distance right, then some distance up.
- **Zero (of the function)**: a spot on the map where the machine's answer comes out as exactly 0, where it goes silent. These zeros control the spacing of the primes.
- **Critical line**: the exact center line of the strip, halfway between its two edges. Every zero found so far sits on it.
- **Hypothesis**: an educated guess that has not yet been proven true.
- **Riemann Hypothesis**: the unproven claim that every zero of the zeta function lies exactly on the center line, with no exception ever, which would mean the primes are spread as evenly as possible.

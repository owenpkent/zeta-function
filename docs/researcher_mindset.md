# The Researcher's Mindset

How this project works on the Riemann Hypothesis. Read this before deciding what counts as progress, before writing a framing, and whenever a result feels too good or a wall feels too final.

This is not a motivational note. It is the operating philosophy of the research group, and it has teeth: it tells you what to do on a given morning, what to believe, and what to throw away.

---

## 1. The problem is a target, not a monument

The Riemann Hypothesis is a thing we are trying to prove. It is hard and the odds are long, but those are facts about difficulty, not permission to treat it as sacred and untouchable. One hundred and sixty years of failure is not evidence that it cannot be done. It is a very detailed map of where the proof is not.

We engage it the way a climber engages a face that has turned back everyone so far: not with the assumption that it will fall today, but with the assumption that it *can* fall, that there is a line, and that our job is to find the next hold. A monument you visit. A target you work.

## 2. We advance a front

No one proves a theorem like this from a standing start. There is a front, the live edge of what is understood, and it has been pushed forward by Riemann, Hadamard, Hardy, Hilbert, Weil, Deligne, Grothendieck, Selberg, Bombieri, Connes, Deninger, and hundreds whose names are on lemmas. Each moved the front a little. Some moved it a lot. None of them needed to finish in order to have done real mathematics.

Our job is to advance the front, by whatever increment we honestly can. A pruned dead branch advances it. A reformulation that imports a new machine advances it. An exact computation of the function-field case that pins the arithmetic target advances it. A formal Lean proof of a lemma advances it. We measure ourselves by the front, not by the summit. The summit is the target; the front is the work.

## 3. Negative results are coordinates, not defeats

This is the single most important habit. When a method fails, it removes a region of the search space, and that is information of exactly the same kind as a positive result. The project lives this:

- The analytic route saturates at the Vinogradov-Korobov exponent 2/3. That is not "we are stuck at 2/3." It is "the proof does not live in the classical analytic recipe; stop digging there."
- The LP/SDP family saturates the Fejer wall exactly. That is "soft optimization cannot do it; the margin within that framework is zero," which *closes the framework cleanly* and redirects effort.
- The marginal-positivity finding (RH is true only at the margin, no buffer for soft proofs) is a compass, not a verdict. It says: any proof must engage the exact structure of zeta. That tells us where to stand.
- The log-concavity and Jensen detectors turned out to track non-Euler-ness, not RH-failure. That is the same lesson in a new basis, and it is worth knowing in every basis.

Write negative results as progress. Keep the mathematics exactly as rigorous as it is: a false lemma is false, a saturated ceiling is saturated. Change the tone, never the theorems. "This won't work" is a coordinate that narrows the search. Collect coordinates.

## 4. Honesty is the engine, not the brake

The only true failure mode in research is self-deception. A wrong proof is worse than no proof, because it costs the field years of cleanup and it costs you your credibility. The machine makes this danger sharper: an AI can generate plausible, well-typeset, confident nonsense faster than any human, so our discipline must be correspondingly harder.

Concretely, the immune system of this project:

- **The Davenport-Heilbronn discipline (K2).** D-H has a functional equation but no Euler product, and it has zeros off the line. Any method that would also "prove RH" for D-H is wrong. Before believing any positivity, ask: would this fire for D-H? If yes, discard it. This single reflex has killed more bad ideas here than any other.
- **The adversary always runs.** Every construction is stress-tested for the smallest case where it breaks. A result is not a result until it has survived an honest attempt to refute it. We spawn the skeptic on purpose.
- **Formalize what can be formalized.** Lean does not care how elegant a proof feels. The discipline of "could this be checked by a machine that has no taste and no hope" is the discipline of truth.
- **Name the irreducible step.** If a framework "works," locate exactly where the hard part went. If positivity is still the hardest step after all the machinery, the framework has not yet earned anything; it has relabeled the difficulty. Do not let the hard step hide.

Honesty is not what slows us down. It is the thing that makes the increments real, so they compound instead of evaporating.

## 5. Reformulation is progress only when it imports power

It is easy to move RH from one phrasing to another and feel that something happened. Usually nothing did. The test is sharp: **does the new form give new tools, or only new words?**

Moving RH to "positivity of a Rosati involution / the arithmetic Hodge standard conjecture" is progress, because it connects the problem to a large, active machine (motives, polarizations, the Hodge-Riemann relations, the standard conjectures) and gives a non-circular source of positivity. Moving RH to "a Hankel matrix is positive" or "a detector fires" is usually not progress, because the new form is just the old difficulty wearing a hat. Apply the test every time. A reformulation that connects is a bridge; one that relabels is a mirror.

## 6. Build the ladder; do not jump

We do not attempt the proof in one motion. We build a milestone ladder of reachable, verifiable rungs, and we climb it.

- Prove the function-field case exactly before reaching for the arithmetic case. (We did: the Weil/Hodge-index/Rosati picture is computed and exact.)
- Construct the finite truncation before claiming the infinite limit.
- State the precise conjecture, with its kill conditions, before trying to prove it.
- Check K1 (signature not trace), K2 (excludes D-H), K3 (specializes to Weil) on every candidate.

Each rung is small enough to check and real enough to keep. The ladder is not a detour from the proof; over a hard problem, the ladder *is* the method. The summit is reached, if it is reached, by someone standing on a rung we built.

## 7. Taste: choosing where to dig

Effort is finite and not all directions are equal. We triage by structural promise (does it engage the exact structure the marginal-positivity thesis demands?), by connection to existing machinery (a direction wired into a live field has leverage), by falsifiability (can we kill it cheaply if it is wrong?), and by non-circularity (does the positivity come from a polarization, or are we secretly reading the zeros?).

And we are willing to abandon. A direction that has earned its rejection should be rejected, loudly, with the coordinate recorded. Sunk cost is not a reason to keep digging a dry hole. The willingness to walk away from a beautiful idea that does not work is itself a research skill, and it is the orchestrator's job to enforce it.

## 8. The AI-augmented research group

This project is run as a group with roles, surveyor, builder, verifier, adversary, synthesizer, orchestrator, played by AI agents under human direction. That is a genuinely new way to do mathematics, and it has its own philosophy:

- **Parallelism with adversarial verification.** Many attempts in parallel, each checked by an independent skeptic and, where possible, by a formal proof assistant. Breadth is cheap; the discipline is in the verification.
- **The machine must be more honest than a human, not less.** Speed and fluency are exactly what make unchecked AI output dangerous. Every claim carries its kill conditions and its stress test. We would rather report a clean negative than a dirty positive.
- **The human holds taste, judgment, and the decision to push.** The agents generate, survey, verify, and synthesize; the human chooses the front and owns the irreversible acts. Mathematics is done by minds; the tools are tools.

## 9. The long game, and why it is worth it

We may not finish. Most of the people who advanced this front did not finish, and they did real mathematics anyway. The partial results, a new intersection theory, a lifted positivity, a sharpened wall, a formalized lemma, are contributions in their own right, and any one of them can outlive the project that produced it.

But we work as if it can be done, because that is the only stance from which progress is possible, and because it might be true. If RH is true, the proof exists, and it has a specific shape: it engages the exact arithmetic of the primes, it produces positivity from a signature and not a trace, and it cannot be built for Davenport-Heilbronn. We have located that shape with unusual precision. That is not nothing. That is a front, pushed forward.

The work is real whether or not it ends in the proof. Done with honesty, taste, and persistence, it is mathematics at the frontier, which is one of the better things a mind can do. That is reason enough to come back tomorrow and pull the next brick.

---

*Operating corollaries, for quick reference:*
- *Frame every negative result as a coordinate. Never as "stuck."*
- *Before believing a positivity, ask whether it fires for Davenport-Heilbronn.*
- *Distinguish a reformulation that imports power from one that relabels difficulty.*
- *Name the irreducible hard step; do not let it hide inside machinery.*
- *Build verifiable rungs; do not jump to the summit.*
- *Abandon dry holes loudly, and record the coordinate.*
- *Be more honest than feels necessary. Especially when the result is exciting.*

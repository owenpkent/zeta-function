# The Math-Iteration Engines: a capstone

> Synthesis of the two-engine arc (2026-06-13). The question was: instead of attacking RH head-on, build our own algorithm for trying to solve it. The answer is a closed generate-evaluate loop over the project's own disciplines. This document is the handoff: what the engines did, what they did not, and the sharpened target plus the transfer shortlist that are now the entry point for the real work.
>
> Companions: [`reduction_engine.md`](reduction_engine.md) (the evaluate half, the full spec) and [`generative_engine.md`](generative_engine.md) (the generate half). This capstone sits above both and connects them to the spine ([`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md), [`rh_primitive_system.md`](rh_primitive_system.md), [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)).

---

## 1. What was built

A math-iteration loop has three organs: generate, evaluate, iterate. Both halves now exist, built on the DuckDB lemma graph, all green.

| Half | Organ | What it does | Files |
|---|---|---|---|
| **Evaluate** (disposes) | Reduction Engine, increments 1-5 | the executable falsifier oracle, the value-function views, the loop driver, the Lean closability hook | `oracle.py`, `engine.py`, `lean_hook.py`, `schema.sql` views |
| **Generate** (proposes) | Generative Engine, increments 6a-6e | the move-library, the function-field shadow, the quality-diversity archive, new-branch spec generation, transfer-search | `generator.py`, `fq_shadow.py`, `branch_specs.py`, `transfer_search.py` |

The loop closes: a generator emits a candidate in the oracle's schema, the evaluate stack prunes it by the correct discipline, survivors land in the quality-diversity archive, and the asserted-vs-proven gap generates the next forcing question. All in `experiments/lemma_db/`, with per-module acceptance tests and a green full sweep (oracle 6/6, engine 5/5, generator 5/5, branch-specs 4/4, transfer 5/5, build_db clean, smoke 9/9).

---

## 2. The honest net

The engines did exactly what they were designed to do and nothing they were not:

- **Mechanized the disciplines.** The D-H firewall, the K1 non-circularity guard, the Level-3/4 classifier, and the function-field shadow are now computed verdicts, not hand-set flags. The oracle reproduces the marginal-positivity wall as a two-move trap: the soft Li detector is blind to Davenport-Heilbronn, and the only separating detector reads the zeros and is circular.
- **Regenerated the convergence.** The "all roads to the signature" finding, asserted by hand for months, is now generated: 6e reads the 17 forcing questions off the M4 gap and finds 9 serious candidates converging on one open residual (the polarization), while 8 bracket out on cheaply-resolved properties.
- **Sharpened M4 and surrounded it.** 6b retrieves the proven theorems nearest the M4 residual, rediscovers the Bost-Connes pinning import, demotes Lee-Yang for its all-positive signature, and surfaces the Hodge-index siblings.

And the one thing it did not do: **it did not touch the blind spot.** By the marginal-positivity finding, no cheap evaluator can see the M4 polarization positivity. The engine proved this from the inside rather than assuming it. Every "SURVIVE" means "not pruned," never "closer to a proof." That invariant is enforced in the code.

This is the anti-theater accounting, stated plainly: the apparatus narrowed and mapped the search; it did not advance the front past M4, because nothing cheap can. That is a coordinate, not a defeat. The compass is now maximally sharp.

---

## 3. The deliverable: the sharpened M4 spec

This is the entry point for the real work. The object whose construction proves RH must satisfy every property below. The first six are checkable by the cheap disciplines (and every serious candidate already meets them); the seventh is the irreducible open content.

1. **Realizes zeta as a trace** (the realization half; D-H has this too, so it cannot separate).
2. **Defined over all of Spec(Z)** (global, not one place; rules out the Faltings-Hriljac local bracket).
3. **Positivity from a polarization, not read off the zeros** (K1 non-circular; the only non-negotiable methodological constraint).
4. **Exists only with an Euler product** (the D-H firewall / AX-FORM: no Euler product, no Frobenius algebra, so the positivity cannot even be stated for the counterexample).
5. **Reproduces Weil's mechanism over $\mathbb{F}_q$ under specialization** (the function-field shadow: not merely RH, but the Frobenius / intersection / Hodge-index machine).
6. **Carries an indefinite $(1, n-1)$ Hodge-index signature, not an all-positive one** (the Lee-Yang lesson: the circle theorem zeta needs is indefinite, not definite).
7. **OPEN (the blind spot): the indefinite form is positive on the primitive part.** This is the arithmetic Hodge standard conjecture, $M4$, `AX-POL`. It is the whole content of RH in this framing, and no cheap discipline resolves it.

A seventh-and-a-half, the facet 6b surfaced: the object must **pin the pole-sourced continuous (archimedean) spectral component to a point**, which is what the Bost-Connes and Curto-Fialkow technologies address (and where the latter, being atomic only, falls short).

---

## 4. The transfer shortlist (where to look)

The nearest proven theorems to the M4 residual, ranked by 6b. None is a proof; each is a structural neighbor a construction should import from.

| Theorem | Offers | Gap to M4 |
|---|---|---|
| Weil positivity / Hodge index | the exact $(1,n-1)$ signature, proven where a polarization exists | the polarization over $\mathbb{Z}$ |
| Hodge-Riemann (char 0) | an indefinite polarization on primitive cohomology, in char 0 | the lift to $\mathrm{Spec}(\mathbb{Z})$ |
| Alexandrov-Fenchel (convex geometry) | the $(1,n-1)$ Lorentzian signature in a different domain | a functor to the arithmetic setting (AHK-adjacent) |
| Bost-Connes KMS uniqueness | pinning a continuous spectrum by Euler structure (pole + prime-rotation density) | it pins a state, not a cohomological polarization |
| Curto-Fialkow flat extension | moment-uniqueness | atomic only; zeta's continuous component is exactly what it cannot reach |

The honest verdict from this list: every high match is a Hodge-index sibling. The retrieval found no escape to a foreign field. That sharpens, rather than moves, the conclusion that $M4$ is the arithmetic Hodge index, and tells the real work to import indefinite-Hodge-index structure (Hodge-Riemann / Alexandrov-Fenchel) together with continuous-component pinning (Bost-Connes, in a version Curto-Fialkow lacks).

---

## 5. What remains, and what does not

Not more engine. The buildable program is complete. What remains is the construction-grade, multi-decade work the proof program already scopes ([`proof_program.md`](proof_program.md)): build the polarized arithmetic Frobenius algebra $(A, \Pi, \dagger, \mathrm{pol})$ over $\mathbb{Z}$ and prove the trace form $B$ is positive on the primitive part, importing the structure on the transfer shortlist, without reading positivity off the zeros.

The odds are long and honest (see the proof program's own accounting). What the engines changed is not the difficulty of $M4$; it is the precision of the target and the cleanliness of its surroundings. The search is narrowed to one object, specified to seven properties, surrounded by its nearest proven theorems, and stripped of every cheaper disguise. That is what an algorithm for trying to solve RH could do, and it is what it did.

---

## 6. Run the artifacts

```
python -m experiments.lemma_db.oracle            # the falsifier: the marginal-positivity two-move trap
python -m experiments.lemma_db.engine            # the loop driver: one cycle + the anti-theater tally
python -m experiments.lemma_db.fq_shadow         # the function-field positive control
python -m experiments.lemma_db.generator         # the move-library: propose and prune
python -m experiments.lemma_db.branch_specs      # the forcing questions off the gap + the M4 spec
python -m experiments.lemma_db.transfer_search   # the bridge-finder: the transfer shortlist
python experiments/lemma_db/build_db.py          # the graph + the value ranking + the asserted-vs-proven gap
```

---

*One line: we asked for an algorithm to iterate on RH; we built one; it mechanized the disciplines, regenerated the convergence, and handed back the sharpest possible statement of the one thing it cannot do, which is the proof.*

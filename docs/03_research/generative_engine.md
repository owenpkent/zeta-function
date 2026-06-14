# The Generative Engine: a design for iterating on mathematics

> Speculative design for the **generate** half of a math-iteration loop. The [Reduction Engine](reduction_engine.md) is the **evaluate** half: it kills, ranks, and audits proposals. It proposes nothing. This document specs the organ that proposes, so that "iterate on mathematics" becomes an actual loop rather than a human typing candidates into an evaluator.
>
> Mostly design, with the first generators now built. It is written in the honest register of [`proof_program_ai_only.md`](proof_program_ai_only.md): the odds are long, most of it will not work, and the value is in the parts that fail cheaply and the one bridge that might not. Nothing here claims a shortcut to RH.

Status: 2026-06-13. The governing obstruction (section 1) is the project's own marginal-positivity finding, and it dictates the entire shape of what follows. As of this date the function-field shadow (6d), the move-library generator (6a), the quality-diversity archive (6c), and new-branch spec generation (6e) are built and green ([`fq_shadow.py`](../../experiments/lemma_db/fq_shadow.py), [`generator.py`](../../experiments/lemma_db/generator.py), [`branch_specs.py`](../../experiments/lemma_db/branch_specs.py); `test_generator.py` 5/5, `test_branch_specs.py` 4/4). Only transfer-search (6b) remains design.

---

## 0. Three organs, and which one exists

Any algorithm that iterates on mathematics has three organs:

- **Generate**: propose new definitions, reformulations, bridges, strategies.
- **Evaluate**: decide whether a proposal is correct and whether it is promising.
- **Iterate**: feed the evaluation back to steer the next generation.

The Reduction Engine is a strong **evaluate** organ and nothing else. The D-H oracle, the Lean floor, the numerics, the value-function views are all "is this right, is this promising," run cheaply. There is essentially zero **generate**. That asymmetry is not laziness: evaluation is the part that can be made rigorous and cheap; generation is the part where "an approach humans have not thought of" would have to come from, and it is unsolved.

This document specs the generate organ and the iterate organ that closes the loop around it.

---

## 1. The governing obstruction: the value-signal blind spot

A generate-evaluate loop is only as good as its **cheap value signal**. You generate many candidates, the evaluator scores them, you keep the good ones and repeat. That works (FunSearch found genuinely new cap-set constructions this way) exactly when there is a cheap, automatic score whose optimum is the answer.

RH does not have that, and the project has it in code. The marginal-positivity wall ([`soft_detector_wall.md`](soft_detector_wall.md), and the [oracle](../../experiments/lemma_db/oracle.py)'s flip test) is precisely a theorem that *no cheap evaluator can see the answer*: the Li detector is blind to Davenport-Heilbronn below $N \sim 10^{37}$, and every soft signal saturates at the wall. A loop pointed at "prove M4" is therefore blind exactly at the goal. It would iterate forever on the plateau.

The consequence dictates the whole design:

> **The loop must iterate on reformulations and bridges, not on proofs.** The search space is not "candidate proofs of M4" (no cheap signal, hopeless). It is "candidate restatements of M4, and candidate bridges from M4 to already-proven mathematics" (cheap signal: equivalence-checking and structural matching). The engine does not search for the proof. It searches for the position from which the proof becomes a known theorem.

### The one positive gradient the problem does offer: the function-field shadow

The blind spot is specifically about the *arithmetic* positivity over $\mathbb{Z}$. The *function-field shadow* of any candidate is cheaply checkable, and it is the rare positive signal the design leans on. RH is a theorem over $\mathbb{F}_q$ (Weil), and the project has the machinery to test it ([2F Hodge-index sweep, the e2ll wind tunnel](../../experiments/arithmetic_geometric/)). So a generated reformulation can be specialized to $\mathbb{F}_q[t]$ and checked: does it reproduce the known proof there? This is the mirror image of the D-H discipline. D-H is the negative filter ("must NOT work for the counterexample"); the function-field shadow is the positive filter ("must reproduce the theorem where the theorem is known"). Together they are a cheap two-sided gradient that points up to, but not across, the final arithmetic step.

The evaluation stack for a generated candidate, cheapest first:

1. **Oracle cheap falsifiers** (level, D-H, K1): negative filter, kills most garbage instantly.
2. **Function-field specialization**: does it reduce to the proven $\mathbb{F}_q$ theorem? The positive gradient.
3. **Numerical separation** of $\zeta$ from D-H where reachable.
4. **Lean equivalence-check** of the reformulation (not of the proof).

Step 4 is the only one that confers truth, and it confers it about *equivalence*, never about the open arithmetic content. That boundary is the soundness floor, inherited verbatim from the Reduction Engine.

---

## 2. The integration contract: generators emit Candidates

The generate organ plugs into the existing evaluate organ through one contract: **a generator emits objects in the oracle's `Candidate` schema** ([`oracle.py`](../../experiments/lemma_db/oracle.py)). A `Candidate` already carries `claim_type`, `claims_rh_equivalent`, `inputs`, a `construction(L)`, and a `detector(L)`. So a generated proposal flows straight into `run_oracle` and `run_cycle` ([`engine.py`](../../experiments/lemma_db/engine.py)): falsify, score, log, with no new evaluation code. The generator's whole job is to produce well-formed Candidates; the engine already knows how to dispose of them.

This makes the generative engine a true extension of what is built, not a parallel system. Increment 6 is "the first organ that proposes," feeding increments 1 through 5.

---

## 3. Generator I: the move-library (increment 6a)

A library of structure-preserving rewrites, each a function `move: Formulation -> [Formulation]`. A `Formulation` is a structured object, not free text and not a full proof: roughly `(base/setting, object, pairing, claimed-positivity, invariants-it-must-reproduce)`. The moves act on that structure. This is a typed term-rewriting system over mathematical *settings*, which captures the reformulation layer (the tractable target) without pretending to capture all of mathematics.

The moves are the standard mathematician's repertoire, and the project's own history is made of them:

| Move | Example in this project |
|---|---|
| base change / specialize | $\mathrm{Spec}(\mathbb{Z}) \leftrightarrow \mathbb{F}_q[t] \leftrightarrow$ a curve (the whole Weil-template strategy) |
| dualize | Poincare / Serre duality, the cup pairing (2K, Tang prismatic duality) |
| deform | add a nilpotent / monodromy (2LL the Euler-Sen $N$-block) |
| complete / localize / glue | p-adic + archimedean adelic assembly (Silverman local heights 2I/2L/2P) |
| categorify / decategorify | numbers $\leftrightarrow$ objects $\leftrightarrow$ traces |
| degenerate | $q \to 1$, $\mathbb{F}_1$ (Deitmar, Lorscheid, Connes-Consani) |
| twist | Tate twist, the place-dependent $(1,p)$ bidegree (2Q) |

A move applied to a formulation yields variants; each variant becomes a Candidate; the oracle prunes; survivors recurse. The honest deliverable of 6a is not a proof. It is a measurement: **how fast does the oracle prune the move-generated tree, and does any branch reach a failure cell (section 6) no human branch has occupied.** It is the first organ that proposes, and it is cheap to build because it reuses the entire evaluate stack.

The limit of 6a is real: a rewrite system explores the *deductive neighborhood* of existing formulations. It recombines; it does not invent a new field. The genuinely-new is more likely to come from generator II.

---

## 4. Generator II: transfer-search, bridges not atoms (increment 6b)

The strongest claim of this design. **The approach humans have not thought of is most likely a bridge, not an atom.** Humans are domain-siloed; the cross-domain transfer that would crack RH needs simultaneous deep fluency in two fields that almost no individual holds together. A machine's genuine edge is not depth, it is breadth held simultaneously: it can hold all of proven mathematics at once and search the product space

$$\big(\text{proven theorem in field } A\big) \times \big(\text{open target in field } B\big)$$

for structural isomorphisms. The project has done this by hand, one transfer at a time, limited by who knew both sides: "all roads to the signature" ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)) and the Bost-Connes import ([`lateral_imports_2026_06.md`](lateral_imports_2026_06.md), where the KMS$_\beta$ simplex being a single point was recognized as the exact shape of the composite-pinching target). Generator II automates that recognition.

The mechanism:

1. Take the open residual (M4: an RH-equivalent polarization of signature $(1, n{-}1)$ on primitive cohomology of $\mathrm{Spec}(\mathbb{Z})$).
2. Compute a **structural signature** richer than the four bits that killed the Reduction Engine's collision engine: features capturing the *kind* of positivity (definite vs indefinite), the *carrier* (cohomology / trace / measure / operator), the *source* of positivity (polarization / Hodge / spectral / ergodic / moment-uniqueness), and the invariants it must reproduce.
3. Embed every *proven* positivity / polarization / rigidity theorem in a corpus the same way (Hodge-Riemann, Hodge index, Weil, Alexandrov-Fenchel, Lee-Yang, Bost-Connes KMS uniqueness, Curto-Fialkow flat extension, de Branges, ...).
4. Nearest neighbors are candidate transfers. Each becomes a `Candidate`: claim = the transfer; `construction` = the proposed functor $S \to \mathrm{Spec}(\mathbb{Z})$; `detector` = does it separate D-H. The oracle and the function-field shadow then prune.

The hard part, and the honest one: a structural signature faithful enough to certify "these two residuals are the same object" *is* research-grade mathematics, the same no-free-lunch that killed the four-bit collision engine. So 6b does not pretend the embedding decides isomorphism. The embedding only *retrieves candidates* (nearest neighbors, cheap, fallible); an LLM judge then proposes the actual functor and the oracle checks it against D-H and the $\mathbb{F}_q$ shadow. The embedding is a retrieval prior, never a verdict. That keeps 6b on the right side of the soundness boundary.

---

## 5. Generator III: new-branch generation (increment 6e)

The deepest mode, and the most honest about its ceiling. A new branch of mathematics is not conjured from nothing; historically it is one of a small set of **meta-level moves** applied to existing material, plus a forcing question, plus the nerve to posit. The same architecture as 6a and 6b runs here one level up: the moves create theories instead of rewriting formulations.

| Meta-move | Born this way | In this project |
|---|---|---|
| posit the forced object | $\mathbb{C}$ ($x^2=-1$), ideals (restore unique factorization), schemes | $\mathbb{F}_1$ (to make $\mathrm{Spec}(\mathbb{Z})$ a curve) |
| identify two languages | Cartesian geometry, Langlands (Galois = automorphic) | cohomology-of-$\mathrm{Spec}(\mathbb{Z})$ $=$ a KMS / operator / measure structure |
| invent the invariant | cohomology, K-theory, the fundamental group | Deninger's cohomology with the right Lefschetz / weight structure |
| drop or change an axiom | non-Euclidean geometry, condensed mathematics | $\mathbb{F}_1$ as $\mathbb{Z}$ minus additive structure |
| reify a process | deformation theory, ergodic theory | Connes making the adele-class flow into geometry |

Generating new-branch *ideas* is not the bottleneck. The project overflows with them: $\mathbb{F}_1$, Deninger, Connes-Consani, prismatic-over-$\mathbb{Z}$ are all new-branch attempts, catalogued in [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md). The bottleneck is the value-signal problem in its purest form, one level up: no cheap test says which new branch is *right*, because "right" means "carries the RH-equivalent polarization," which is M4, which is the blind spot.

### The real product: a falsifiable spec of the missing object, and the gaps are the prompts

The move that makes this concrete rather than philosophical:

> **The engine's new-branch contribution is to write a tight, falsifiable SPECIFICATION of the object a new branch would need, read off from what the proof requires; and the Reduction Engine's gaps are the forcing questions that prompt it.**

M4's asserted-vs-proven gap of 16 (section 1; computed by the [`asserted_vs_proven`](../../experiments/lemma_db/schema.sql) view) is sixteen forcing questions. Every annotation edge that is not a load-bearing reduction marks a place where the current language is missing the object that would make the assertion a reduction. "What object would make Deninger-foliated actually reduce to the signature?" *is* a spec: a cohomology carrying a Frobenius whose eigenvalues are the zeros and a cup product that is a polarization of signature $(1, n{-}1)$. That spec is a real, checkable object even when the object satisfying it cannot be built. The project already writes such specs by hand (the acoustic thread's "missing object $=$ the bound-halving energy form $=$ Poincare-duality middle weight $=$ Deninger's weight filtration"). Systematizing it is this generator: read the spec off the deepest gaps, posit objects against it, filter.

A spec is filterable by the same cheap disciplines, which is what keeps new-branch generation signal rather than the infinite noise of vacuous axiom systems:

- **consistency / inhabitation** (Lean: do the posited axioms have a model, or are they vacuous? the repo already proves "no D-H instance, by type" in `FrobeniusAlgebra.lean`),
- **realization** (does the posited object realize $\zeta$ as a trace? cheap, positive),
- **the D-H firewall** (does the object structurally fail to exist for Davenport-Heilbronn, i.e. require the Euler product? if D-H can build it, it is the wrong branch),
- **function-field reproduction** (specialized to $\mathbb{F}_q$, does the new branch reproduce Weil's actual *mechanism*, not merely RH?).

Same verifier-is-enabler principle (section 7): you may posit aggressively precisely because these filters kill the vacuous and the D-H-buildable cheaply. The branch-specs that survive land in the quality-diversity archive (section 6) as their own failure cells.

### Two regimes, and the honest ceiling

There are two kinds of new-branch move, and the engine is strong at one and weak at the other.

- **Spec-and-fill**: the hole is named, and you hunt or posit an object meeting the spec. Falsifiable, filterable, tractable. The project lives here, and this generator systematizes it.
- **Reframe-so-the-hole-disappears**: you do not fill the gap, you find a language in which there is no gap, because RH stops being about cohomology (or about positivity, or about whatever the current frame assumes) at all. There is no spec to check against, because you are changing what counts as a solution. This is where genuine novelty and genuine intractability both live.

The approach humans have not thought of may well be a regime-two move, which is the hardest to mechanize. A language model can *propose* reframings ("what if this is not about $X$ but about $Y$"), but nothing cheaply tells you which reframing is the real one, because that judgment is the proof. So the honest division of labor: the engine generates forcing questions from the gaps, posits objects, writes specs, and filters by consistency and the $\mathbb{F}_q$ / D-H disciplines, compressing the space of possible new branches to the few that survive. It cannot decide which survivor is right (the blind spot, section 1), and it cannot yet *build* the posited branch, the creative research the [AI-only proof program](proof_program_ai_only.md) concedes is beyond current depth. The machine narrows; the human (or a future system with a stronger verifier) chooses and builds.

---

## 6. The iterate organ: quality-diversity, not optimization

For an open problem, run **quality-diversity, not optimization.** Optimization (maximize the positivity margin) climbs one hill and saturates at the wall. Quality-diversity maintains an archive (a MAP-Elites grid) of *structurally distinct* near-misses, each tagged by *how* it fails, and always steers generation toward an empty cell. It maps the boundary of the possible instead of re-climbing a known hill.

This is the project's epistemology made into a search. Every kill is a coordinate; every "this won't work" narrows the space ([`researcher_mindset.md`](../researcher_mindset.md)). The archive axes are the failure-mode features the evaluate stack already produces:

- which D-H separation level the candidate reaches (Level-3 / comb / beyond-comb),
- definite vs indefinite signature,
- where positivity is sourced,
- the resolution floor at which its detector goes blind,
- whether it reproduces the $\mathbb{F}_q$ shadow.

A generated Candidate lands in the cell its oracle verdict plus numerics define. Keep the best per cell. The objective is **fill an empty cell**, i.e. find a near-miss that fails in a way nothing has failed before, because that is the only kind of candidate that can move the frontier (the same novelty argument the Reduction Engine's residual layer settled on, now driving generation instead of only flagging it). The asserted-vs-proven gap and the kill-tally from the Reduction Engine feed the archive directly.

---

## 7. Three principles that govern the whole loop

1. **The verifier is the enabler.** Generation novelty can be cranked exactly as high as the verifier catches the hallucinations. Novelty without a catch-net is noise; novelty behind Lean + the D-H oracle + the $\mathbb{F}_q$ shadow is search. Investing in cheap verifiers is investing in how novel you can afford to be. The unglamorous evaluation infrastructure is what *permits* aggressive generation.

2. **Taste inversion.** Human search is pruned by taste, and taste is trained on past success, so it is biased against the genuinely new. The untried approach may be untried precisely because it looked ugly or unmotivated. The generator should deliberately bias toward branches human heuristics discard, and pay for the resulting garbage with the cheap verifier. This is affordable only because principle 1 holds.

3. **The blind-spot invariant.** The engine NEVER scores "progress toward the proof of M4." No cheap signal exists there, by the marginal-positivity finding, so any such score is theater. It scores only: survival of cheap falsifiers, function-field shadow reproduction, numerical D-H separation where reachable, Lean-checkable equivalence, and structural match to a proven theorem. Progress is "reached a new failure cell" or "surfaced a new bridge candidate," never "closer to the proof."

---

## 8. The honest limits

- **It maps to the doorway; it probably does not walk through.** The deepest signal, the actual M4 polarization, sits in the blind spot no cheap evaluator reaches. The best achievable target is the reformulation or bridge from which a human (or a future system with a stronger verifier) recognizes the proof. The engine is a cartographer of the doorway, not a key.
- **RH might be FLT-shaped.** Wiles needed modularity, a whole field, invented first. If RH requires inventing new theory rather than transferring existing theory, reformulation-and-bridge search cannot reach it. The design bets that the missing piece is a *connection* between existing bodies of math, not a new body. That bet may be wrong.
- **The corpus and embedding are themselves hard.** A structural signature good enough to retrieve the right neighbors is most of the difficulty, and it inherits the no-free-lunch the collision engine hit. 6b mitigates by using the embedding only for retrieval and an LLM judge plus the oracle for the verdict, but a bad embedding means bad retrieval, and there is no cheap way to know the embedding is good except by whether its transfers survive.
- **Meta-learning "good approach" is data-poor.** There are few RH-scale problems with known winning approaches to learn taste from. The bet is that taste learned on the millions of *small* solved theorems transfers up in scale, which is an open empirical question.

None of these is fatal; all are coordinates. They say the realistic deliverable is "tirelessly map the reformulation-and-bridge space until a cross-domain connection surfaces that no siloed human would spot," which is a believable machine edge, not a fantasy.

---

## 9. Implementation increments

Each lands on the existing `Candidate` schema and the evaluate stack, so each is a true extension of the built engine.

- **6a: the move-library (built 2026-06-13).** [`generator.py`](../../experiments/lemma_db/generator.py): a `Formulation` and eight structure-preserving moves (`base_change`, `raise_q`, `dualize`, `perturb_offline`, `drop_euler`, `degenerate_q1`, `read_zeros`, `go_statistical`). It proposes variants from a Weil/$\mathbb{F}_q$ seed and prunes them with the evaluate stack, reproducing every discipline: `drop_euler` is vacuous (no Euler, no positivity to state), `perturb_offline` breaks the $\mathbb{F}_q$ theorem, `read_zeros` is circular, `go_statistical` is Level-3. Reuses the committed oracle's `level_classifier` and `k1_noncircular`. SURVIVE means "not pruned," never "closer to M4."
- **6b: transfer-search.** Curate a small corpus of proven positivity theorems with hand-tagged structural features; embed M4's residual; retrieve nearest neighbors; LLM judge proposes the functor; oracle + $\mathbb{F}_q$ shadow prune. Deliverable: a ranked list of bridge candidates, the Bost-Connes import automated. The high-value, high-difficulty piece, still design.
- **6c: the quality-diversity archive (built 2026-06-13).** A MAP-Elites archive in `generator.py` binning every variant by its failure cell `(base, has_euler, outcome)`; only survivors spawn the next round. The demo fills six distinct cells from one seed. Fed by 6a now, by 6b and 6e later.
- **6d: the $\mathbb{F}_q$-shadow filter (built 2026-06-13).** [`fq_shadow.py`](../../experiments/lemma_db/fq_shadow.py): genuine $\mathbb{F}_q$ controls (real elliptic curves, Frobenius eigenvalues on the $\sqrt q$ circle, RH = Hasse holds) plus an off-line forgery (the function-field analogue of D-H). The check passes where RH is proven and kills the forgery. The positive mirror of the D-H discipline; the generator composes it.
- **6e: new-branch spec generation (built 2026-06-13).** [`branch_specs.py`](../../experiments/lemma_db/branch_specs.py): reads the forcing question off the top asserted-vs-proven gap (`TGT-m4-hodge-standard`, 17 asserted / 1 proven), writes the M4 spec as a required-property checklist with one blind-spot property (the indefinite polarization), and computes each candidate's residual from the graph + the cheap disciplines. Result, generated mechanically: 9 candidates converge on the one OPEN residual (the polarization, the blind spot); 8 bracket out on a RESOLVED property (global / carries-trace / circular / pre-realization, plus de Branges' refuted too-strong polarization). It generates the all-roads convergence rather than asserting it, and bottoms out at the doorway it cannot open. `test_branch_specs.py` 4/4. The construction of any surviving object stays human (or future-AI).

Built order: 6d, 6a, 6c, 6e (all 2026-06-13). Remaining: 6b (the prize).

---

## 10. The anti-theater guard

Inherited from the Reduction Engine and binding here too: **every generated candidate must either be killed cheaply (pruning the space, a coordinate) or reach a new failure cell or a new bridge candidate (a sharpening).** A generator that only emits oracle-killed restatements of known dead branches is overhead and gets cut. The measured numbers: new cells filled per $N$ candidates, and bridge candidates surfaced per $N$. If both stay zero across many runs, the generator is theater and the honest move is to stop running it and do the mathematics directly. The engine reports those numbers so the call is made on evidence, not mood.

What this engine buys, when it works, is the one thing a machine can do that a siloed human cannot: hold all of proven mathematics at once, search the product space of theorem-against-target tirelessly and without taste-prejudice, and surface the bridge that needed two careers in two fields to see. It will not hand you the proof. It might hand you the doorway.

---

## Revision log

- **2026-06-13, first draft.** The generate half of the math-iteration loop, designed around the marginal-positivity blind spot: iterate on reformulations and bridges, not proofs; use the function-field shadow as the positive gradient and D-H as the negative one; generate by move-library (6a) and transfer-search (6b); steer by quality-diversity over failure cells (6c); never score progress-to-proof. Companion to [`reduction_engine.md`](reduction_engine.md) (the evaluate half).
- **2026-06-13, new-branch generation (section 5, increment 6e).** Generating whole new branches is the same architecture one level up: a meta-move library (posit the forced object, identify two languages, invent the invariant, drop an axiom, reify a process), prompted by forcing questions read off the deepest asserted-vs-proven gaps. The engine's real product is a falsifiable spec of the missing object, filtered by consistency / realization / the D-H firewall / $\mathbb{F}_q$ reproduction. Honest ceiling: strong at spec-and-fill, weak at reframe-so-the-hole-disappears, which is where the truly new and the truly intractable both live.
- **2026-06-13, first generators built.** 6d ([`fq_shadow.py`](../../experiments/lemma_db/fq_shadow.py)): the function-field shadow, genuine $\mathbb{F}_q$ curves pass, the off-line forgery is killed. 6a + 6c ([`generator.py`](../../experiments/lemma_db/generator.py)): the move-library proposes variants from a Weil/$\mathbb{F}_q$ seed, the evaluate stack prunes them reproducing every discipline (`drop_euler` vacuous, `perturb_offline` breaks $\mathbb{F}_q$, `read_zeros` circular, `go_statistical` Level-3), and the quality-diversity archive fills six distinct cells. `test_generator.py` 5/5; the committed oracle is reused untouched (6/6 still green). The first organ that proposes.
- **2026-06-13, new-branch spec generation built (6e).** [`branch_specs.py`](../../experiments/lemma_db/branch_specs.py): reads the forcing question off the top gap, writes the M4 required-property spec with one blind-spot property, and generates the all-roads convergence mechanically: 9 candidates converge on the open polarization residual (the blind spot), 8 bracket out on resolved properties. `test_branch_specs.py` 4/4. Only transfer-search (6b) now remains design.

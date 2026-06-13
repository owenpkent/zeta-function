# The Reduction Engine: a problem-compression algorithm for the Riemann Hypothesis

> Spec for the project's own bespoke solver. Not a numerical RH solver and not a theorem prover. It is a **problem-compression procedure**: a designed loop that takes the whole tangle of proof approaches and squeezes it down to its irreducible open kernel, then tries to connect that kernel to known math.
>
> This document makes explicit the meta-search the project has been running implicitly across the Davenport-Heilbronn discipline, the K1-K4 kill criteria, the scorecards, the convergence finding ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)), and the DuckDB lemma graph ([`experiments/lemma_db/`](../../experiments/lemma_db/)). Most of the state object already exists. The engine is what closes the loop around it.
>
> **Relation to siblings.** [`proof_program.md`](proof_program.md) says *what to build* (Architecture 2, the Hodge index slot) on a multi-decade timeline. This document says *how to search*: the procedure that decides, at each step, which candidate to ingest, which to kill, and where the kernel currently sits. The proof program is the destination; the engine is the navigation.

Status: 2026-06-13. First spec. Sections 7 and 8 are the honest accounting of what is built versus what is missing.

---

## 0. The reframe, and the one criterion that keeps this honest

The head-on attack tries to leap from RH to a proof. The engine instead grows a structure that makes the leap shorter and shorter, until it is either trivial or precisely localized. The output at any moment is never "a proof or nothing." It is **the current minimal open kernel, plus the coordinates that rule out its neighbors.**

The bet is that making the meta-search explicit and partly mechanical pays off in two measurable ways: it **kills wrong candidates faster** (cheap disqualifiers run automatically, before any human reads a dossier), and it **localizes the kernel sharper** (when many approaches reduce to the same missing object, the engine recognizes the collision instead of leaving it to the eye).

That gives the single design rule, the anti-theater criterion, which every component must pass:

> **Every component must either kill candidates cheaply or sharpen the open kernel.** A component that does neither is overhead and gets cut. Each one is measured: edges killed per cycle, or frontier shrinkage per cycle.

This rule is the guard against the obvious failure mode of "build a meta-algorithm to solve RH," which is polishing the search machine forever instead of doing the math. The machine earns its keep or it goes.

---

## 1. The core object: the reduction graph

Picture one graph.

- **Nodes** are statements: primitives, axioms, lemmas, theorems, targets, obstructions.
- **Load-bearing edges** are reductions. An edge $A \xrightarrow{\text{depends\_on}} B$ means "$A$'s truth logically requires $B$'s truth." A `specializes` edge is the arithmetic lift of a proven function-field face.
- **The top** is `TGT-rh`, the unique sink.
- **The floor** is the set of nodes with status `proven_lean` / `proven_ff` / `proven_char0`: machine-checkable or model-proven facts.

**Every proof approach is a partial path** from `TGT-rh` downward. The proof exists exactly when a load-bearing path connects `TGT-rh` to the floor with no open node remaining on it.

The **frontier** is the set of open nodes all of whose load-bearing dependencies are already proven. It is the live edge of the search: the places where work can start now because nothing below them is still open. The deepest frontier node is the current minimal open kernel. Today that is `AX-polarization` / `AX-hodge-riemann` (the M4 arithmetic Hodge standard conjecture).

**This object already exists.** It is the lemma graph in [`experiments/lemma_db/schema.sql`](../../experiments/lemma_db/schema.sql): the `node` and `edge` tables, the `load_edge` / `frontier` / `rh_transitive_deps` views, the acyclicity and single-sink validation in `build_db.py`. The reduction graph is not something the engine has to build. It is something the engine has to *drive*.

---

## 2. The falsifier oracle

The oracle's job is narrow and decisive: **reject invalid edges before any downstream work.** Most candidate edges are wrong, and the entire efficiency of the search comes from killing them at low cost. The oracle is the cheap-first scheduler of disqualifiers.

The disqualifiers, in increasing cost:

1. **Level classifier.** Does the candidate live at Level 3 (spectral / statistical: Selberg CLT, GUE, log-correlated structure) or Level 4 (positivity)? A Level-3-only edge into `TGT-rh` is invalid by construction: those statements are compatible with a world where some zero has $\beta = 0.51$. Cheapest kill.
2. **D-H edge-validity (the firewall).** Any claimed edge "$A \implies \text{RH}$" is invalid if $A$ also yields "RH for Davenport-Heilbronn," because that is known false (off-line zeros near $\rho \approx 0.8085 + 85.699\,i$). This is the `dh_audit` view: a `dh_buildable='true'` content node on a load-bearing path is a violation.
3. **The off-line-zero flip test.** Run the candidate detector against the known D-H off-line zero. If it does not fire there, it cannot be detecting what RH needs. (The reusable filter from the crazy-idea screen, [`crazy_idea_convergence_meta`](#).)
4. **K1 non-circularity.** Positivity must come from a polarization, never read off the zeros. An edge into the kernel from a `numerical_only` node that already assumes the conclusion is invalid.
5. **K2-K4.** The heavier structural attacks, run only after the cheap disqualifiers pass.

### The flag-versus-computation upgrade

The lemma DB today encodes the D-H discipline as a **hand-set flag** (`dh_buildable`, entered by judgment) and audits it with `dh_audit`. That is a real discipline, but it trusts a human bit. The engine's upgrade is to make the oracle **executable wherever the object is evaluable**:

- If a candidate object can be evaluated, *run it on D-H*. If a finite number comes out, set `dh_buildable='true'` automatically. No judgment call.
- Run the flip test as a function in `experiments/_shared/` against the stored off-line zero. A candidate that fails it gets a `contradicts` edge and is parked.
- Run the level classifier as a checklist the candidate must answer in structured form.

This is the difference between an *audited* discipline and an *executable* oracle. The audit catches a human who mislabels a node. The oracle catches a candidate the human has not even thought to label.

**A candidate that passes every disqualifier is not validated. It is only "not yet killed."** The sole source of positive validation is the Lean floor (section 5).

---

## 3. The residual layer (what an adversarial pass killed, and the honest residue)

The first draft named this section "the residual and collision engine" and called it the prize: characterize each candidate by a four-bit *failing-conjunct signature* against `PROP-global` / `PROP-carries-trace` / `PROP-rh-equivalent` / `PROP-noncircular`, declare two candidates with the same signature to *collide* onto one frontier node, and call that the mechanization of [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md). An independent adversarial review on 2026-06-13 killed that design. The kill is recorded here as a coordinate, not erased, because it narrows sharply what the engine can honestly do.

### What was killed, with the graph evidence

1. **The signatures are not in the machine.** The convergence the engine claims to recompute lives as prose in node `notes`, not as machine-readable edges. The 12 collapse-cohort candidates (`CAND-deninger-foliated`, the Connes-Consani nodes, `CAND-bhatt-lurie-wcart`, `CAND-hesselholt-tp-tc`, the $\mathbb{F}_1$ pre-realization nodes, ...) carry **no** `contradicts -> PROP` edge at all: their mechanical failing-signature is *empty*. Only 7 nodes in the whole graph carry such an edge, and 6 are curated no-go brackets. So the detector is not vacuous (a constant), it is *inert*: over the cohort it computes "empty," which collides everything onto everything.

2. **The convergence carries no proof obligation.** 16 of 17 `CAND-*` nodes connect outward by `instantiates` (an annotation edge); the 17th uses `specializes` but into a side bracket. **Zero** `CAND` nodes reach `TGT-rh` along load-bearing edges, and **zero** appear in `rh_transitive_deps`. By the schema's own load-versus-annotation split, the entire "all roads to the signature" wiring is 17 assertions the proof obligation cannot see. The engine was specced to *build more* such annotation edges and then count them as convergence. That is asserting, not reducing.

3. **A bit-signature cannot be cheaper than the math it hashes.** The four PROP statements are full research conjectures (`PROP-carries-trace` is the AHK trace-injection step; `PROP-rh-equivalent` is the de Branges / Conrey-Li calibration). Deciding that two candidates "have the same residual" is deciding their open steps are the same theorem. A four-bit hash either collides them without earning it, or, to be faithful, becomes the M4-adjacent mathematics itself. There is no cheap middle.

4. **The bits are blind to the axis that does the work.** The project's single most important verdict, *honest near-miss versus K1-circular dead end*, is encoded in the graph not as a PROP signature but as a **target choice**: `CAND-deninger-foliated` instantiates `TGT-m4-hodge-standard` (honest), `CAND-connes-1999-adele-trace` instantiates `OBS-k1-circularity` (dead). Both have empty PROP signatures. So the smallest concrete pair you can feed the detector, Deninger versus Connes-1999, the two best-built candidates, gets *merged* by the engine while the project has already, correctly, separated them. The four-bit basis is structurally blind to the K1 axis, which is exactly the axis the project's real discrimination runs on.

### The honest residue

Strip the killed parts and one true sentence remains: **the engine's discriminating power lives entirely in the executable oracle of increment 1, not in any signature algebra.** Of the four conjuncts, only `PROP-rh-equivalent` is objectively testable, and its test is the off-line-zero flip test, already a disqualifier in the oracle. `PROP-carries-trace` hits the same resolution-floor wall that killed the soft detectors (the von Mangoldt signal is invisible below $N \gtrsim e^{85.7} \approx 10^{37}$). `PROP-global` and `PROP-noncircular` are predicates about a proof that does not exist yet; calling them "objective tests" relabels a judgment.

So the residual layer keeps exactly two honest jobs, both thin:

- **Route every new candidate through increment 1's oracle.** The oracle's flip-test and K1-provenance verdicts are the only mechanical discrimination available, and they are checked against Davenport-Heilbronn, not against a PROP lookup. A candidate is "interesting" (worth a human's time) when its objective verdict differs from the curated brackets. This is a flag for adjudication, never a claim of collision.
- **Report the asserted-versus-proven gap per frontier node.** For each frontier node, surface (annotation in-degree) minus (load-bearing in-degree). For M4 that is $17 - 1$: a large, honest number that says the convergence is believed and almost entirely unreduced. It points at exactly which annotation edges to go prove. Two caveats travel with it (section 4): the gap is direction-insensitive (a large gap fits both a rich real convergence and a pile of wishful annotations), and naive minimization is gameable by *not surveying* (every new candidate widens it). It is a diagnostic to read, never a loss to minimize.

Everything beyond those two jobs was four-bit judgment laundered through a hash, and it is cut under the anti-theater guard (section 5). The collision engine is not the prize. It was a re-description of a conviction the graph has not yet earned, and the useful move it leaves behind is the gap number that says so out loud.

---

## 4. The value function and the orchestrator policy

The frontier is usually more than one node. The engine ranks them by a value function and spends on the top.

A frontier node's value rises with:

- **Depth in the load-bearing graph**: how deep the open node sits in `rh_transitive_deps`. M4 dominates the frontier by *depth*, not by support. Its load-bearing in-degree is 1, and that one edge is its consumer above it (`TGT-rh -> TGT-m4`), not support from below. Any ranking that calls M4 a "high-breadth convergence node" is silently counting the 17 annotation edges, which is the circular version (section 3). Rank by depth and *proven* support, never by asserted support.
- **Distance to the floor**: how few reductions separate it from known math. A node one lift away from a Mathlib theorem is cheaper than one many lifts away.
- **Formalizability**: is its discharge a known, Lean-adjacent theorem (a function-field face to lift, a char-0 Hodge result), or genuinely novel mathematics?
- **Cost to attack**, inversely.

Alongside the ranking, the value layer reports the **asserted-versus-proven gap** of section 3 for each frontier node: annotation in-degree minus load-bearing in-degree. This is a diagnostic, not a score to optimize. Read it as "how much of this node's support is conviction we have not reduced." For M4 it reads $17 - 1$.

The policy:

- Spend on the highest-value frontier node.
- Abandon a branch the moment its cheapest disqualifier fires.
- Treat a large asserted-versus-proven gap as a to-do list (go prove those reductions), never as evidence the node is right, and never minimize it by declining to survey.
- When the top frontier node is the same kernel as last cycle and nothing cheap shrinks it, stop spending on the search and report the kernel (section 6, useful-stall).

The ranking is a DB view over `frontier` plus a depth and load-bearing-in-degree count from `rh_transitive_deps`. The asserted-versus-proven gap is a second view counting annotation in-degree. The policy is the [`OPERATIONS.md`](../../OPERATIONS.md) orchestrator's judgment, made into a ranking it can defend.

---

## 5. The invariants

These are non-negotiable properties of the engine. They are what separate a search that compresses the problem from one that fools itself.

1. **Soundness over completeness.** The engine must never assert a false edge. Stalling is acceptable; lying is not. The backstops are the Lean floor (an edge claimed `proven_lean` must type-check) and the D-H oracle (an edge that survives for the counterexample is rejected). Better to report a fat open kernel than a thin false one.
2. **Monotone memory.** Every kill is a permanent coordinate. A killed branch is never re-explored. The search space only shrinks. This is [`experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md) and the memory files, enforced.
3. **The honesty invariant.** The output is always "here is the current open kernel and what surrounds it." Never "stuck," never "almost there." Directional, per [`docs/researcher_mindset.md`](../researcher_mindset.md): a kill is a coordinate that narrows the search, not a verdict on the problem.
4. **The anti-theater guard.** Every component is measured by edges killed or frontier shrinkage per cycle. A component that does neither is cut. The engine reports its own kill/shrink counts each cycle, so its usefulness is auditable rather than assumed.

---

## 6. The loop (the algorithm proper)

```
state: the reduction graph G (lemma DB), the learnings memory L

repeat:
  1. INGEST     take a candidate approach; parse to a node + its claimed edges.
  2. FALSIFY    run the oracle on each new edge, cheapest disqualifier first
                (level -> D-H -> flip test -> K1 -> K2-K4).
                reject invalid edges; park parked ones with a contradicts edge.
  3. ROUTE      report the candidate's asserted-vs-proven position; flag for
                human/Lean adjudication ONLY if its objective oracle verdict
                (flip-test / K1) differs from the curated brackets.
                NEVER auto-wire a collision (section 3 killed that).
  4. SCORE      recompute the value function over the frontier.
  5. REPORT     emit: the current minimal open kernel (top frontier node),
                the coordinates ruling out its neighbors, and the next
                highest-value move.
  6. VERIFY     for any edge now claimable as closed, attempt the Lean lift;
                promote to proven_lean only on type-check.
  7. PERSIST    write kills and the new frontier to L (monotone).

until SUCCESS or USEFUL-STALL
```

**Termination.**

- **SUCCESS**: a load-bearing path connects `TGT-rh` to the floor with no open node on it, and the path type-checks in Lean. RH is proved.
- **USEFUL-STALL**: the frontier reduces to a single named kernel that is either already known / Mathlib-adjacent (in which case the proof is a formalization exercise) or genuinely novel mathematics that no cheap move shrinks. The engine outputs the kernel, the full map of coordinates ruling out its neighbors, and the highest-value attack. This is the realistic terminal state today: the kernel is `AX-polarization` (M4), and the output is exactly the spine.

The engine does not lower the difficulty of M4. It localizes it, protects effort from being spent on already-dead branches, and guarantees that when the hard theorem does arrive, it lands on a frontier node that has been proven to be the *only* thing left.

---

## 7. What exists versus what is missing

| Component | Status | Where |
|---|---|---|
| Reduction graph (state object) | **Built** | `lemma_db/schema.sql`, `seed_lemmas.json` (60 nodes, 96 edges) |
| Frontier query | **Built** | `frontier` view |
| Proof-obligation closure | **Built** | `rh_transitive_deps` view |
| D-H discipline as audit (flag) | **Built** | `dh_audit` view |
| K1 non-circularity guard | **Built** | query Q9 |
| Acyclicity + single-sink validation | **Built** | `build_db.py` |
| Monotone memory | **Partial** | `LEARNINGS.md` + memory files, not yet wired to the loop |
| Convergence record (manual) | **Built** | `all_roads_to_the_signature.md`, 17 `CAND-*` annotation edges |
| **Executable D-H oracle (compute, not flag)** | **Missing, specced** | section 2 increment 1; build-ready spec in [`experiments/lemma_db/oracle_spec.md`](../../experiments/lemma_db/oracle_spec.md) |
| **Flip-test as a callable falsifier** | **Missing, specced** | part of the oracle (disqualifier D2) |
| Residual + four-bit collision engine | **Killed** (2026-06-13 adversary) | section 3; mechanically inert, discrimination lives in the oracle |
| **Asserted-vs-proven gap reporter** | **New, scoped** | section 3 honest residue, increment 2' |
| **Value function (ranked by depth + proven support)** | **Missing** | section 4 increment 3 |
| **The loop driver** | **Missing** | section 6 increment 4 |
| **Lean closability hook** | **Missing** | section 5 increment 5 |

The state object is roughly two-thirds built. The engine's missing third is the executable oracle (specced), the value ranking, the asserted-vs-proven reporter, and the driver. The original "collision engine" is not in that list: the adversary showed the discrimination it promised already lives, honestly, in the oracle.

---

## 8. Implementation increments

Each increment is small and lands on existing infrastructure. None requires new mathematics; they operationalize what is already done by hand.

**Increment 1: the executable oracle.** A module `experiments/lemma_db/oracle.py` that, given a candidate in the structured schema, runs four cheap-first disqualifiers (level classifier; computed `dh_buildable` by instantiating the construction on D-H; the off-line-zero flip test; the K1 input tripwire), each returning kill / park / pass / untestable. It kills or parks, never validates. Wires into `build_db.py` as a gate, so `dh_audit` runs against a *computed* flag. Full build-ready spec, including the candidate schema, the disqualifier bodies, and a five-case acceptance suite (T2 = "the flip test must kill D-H" is the load-bearing test), in [`experiments/lemma_db/oracle_spec.md`](../../experiments/lemma_db/oracle_spec.md).

**Increment 2' (the rescoped residual layer).** *The four-bit collision engine is killed (section 3).* What replaces it is thin and honest: (a) route every new candidate through increment 1's oracle and flag it for human/Lean adjudication only when its objective verdict differs from the curated brackets; (b) a DB view reporting the asserted-versus-proven gap (annotation in-degree minus load-bearing in-degree) per frontier node, $17 - 1$ for M4. No signature hashing, no auto-wired collisions. The discrimination the original increment 2 promised lives in the oracle of increment 1, where it is checked against D-H rather than asserted.

**Increment 3: the value function.** A DB view `frontier_ranked` joining `frontier` to a depth and load-bearing-in-degree count from `rh_transitive_deps`, plus a distance-to-floor measure. Ranks by depth and *proven* support, never asserted support. The asserted-versus-proven gap rides alongside as a separate column (increment 2').

**Increment 4: the loop driver.** A script `experiments/lemma_db/engine.py` that runs ingest -> falsify -> route -> score -> report for one candidate, prints the kill/shrink counts (the anti-theater metric), and appends the cycle to a monotone log. This is the engine made runnable; the orchestrator drives candidates through it.

**Increment 5: the Lean closability hook.** When a frontier node's discharge is claimed, the driver checks whether the lift exists in the Lean substrate ([`lean/`](../../lean/)) and promotes to `proven_lean` only on a clean `lake build`. This is the soundness floor wired into the loop.

Ordering: 1, then 3, then 4 give a runnable engine over the existing graph quickly. 2' is cheap (two DB views plus a call into the oracle) and lands alongside 3; the four-bit collision engine that used to sit here was killed before it cost any code, which is the system working as intended. 5 closes the soundness loop and can land anytime.

---

## 9. The honest risk

Three things this engine is not.

- **It is not a shortcut.** It does not make M4 easier. The arithmetic Hodge standard conjecture is exactly as hard after the engine as before. What changes is that effort is provably spent on the only open node, never on a re-derivation of a dead branch.
- **Its oracle is only as good as its falsifiers.** A candidate that passes every cheap disqualifier is "not yet killed," not "correct." The single source of positive truth is the Lean floor. The engine's soundness rests on never confusing those two.
- **It can become the theater it is built to prevent.** The mitigation is the anti-theater guard, measured every cycle. If the kill count and the frontier-shrink count are both zero across many cycles, the engine is overhead and the honest move is to stop running it and go do the mathematics directly. The engine reports those numbers precisely so that call can be made on evidence, not mood.

What the engine buys, when it works, is the thing this project values most: it turns an ad-hoc research habit into a designed search whose every step is either a kill or a sharpening, whose memory is monotone, and whose output is always an honest map of where the real problem now lives.

---

## Revision log

- **2026-06-13, first draft.** Sections 0-9 as the reduction-graph + falsifier-oracle design.
- **2026-06-13, adversarial review of increment 2.** An independent ADVERSARY pass against the graph (`seed_lemmas.json`, `schema.sql`) killed the four-bit collision engine before any code: the candidate signatures are not machine-readable (12 collapse candidates have empty `contradicts -> PROP` sets), the convergence is 17 annotation edges with 0 load-bearing reach into `TGT-rh`, M4's load-bearing in-degree is 1 (its consumer above it), and the four-bit basis is blind to the K1 axis that does the real discrimination (Deninger-foliated vs Connes-1999 both hash to empty yet split to `TGT-m4` vs `OBS-k1-circularity`). Section 3 rewritten to the honest residue: route candidates through increment 1's oracle, report the asserted-versus-proven gap. Section 4 corrected (M4 dominates by depth, not breadth). Increment 2 demoted to 2' (two DB views). The kill is a coordinate: the engine's discrimination lives in the executable falsifier, not in a signature algebra.

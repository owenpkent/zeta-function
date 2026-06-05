# The RH Primitive System: a bespoke axiomatic system engineered around the signature

A purpose-built mathematical system for the Riemann Hypothesis, designed so that the SIGNATURE (the polarization / positivity) is the core primitive and the REALIZATION (the trace / explicit formula) is demoted to a supporting functional. The system reduces RH to exactly one open axiom, makes every other axiom a theorem to be cited, and makes the Davenport-Heilbronn unbuildability a property of the primitives rather than a manual check. The whole graph is tracked in a DuckDB lemma database that enforces the D-H discipline as a build gate.

Status as of 2026-06-05. Layer vocabulary, status vocabulary, and the M1-M5 milestone ladder follow [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) and [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md). The Lean formation interface this system mirrors is [`lean/ZetaRH/FrobeniusAlgebra.lean`](../../lean/ZetaRH/FrobeniusAlgebra.lean). The database lives in [`experiments/lemma_db/`](../../experiments/lemma_db/).

---

## 1. Why a bespoke system, and the one design rule that makes it worth building

Every general framework that touches $\zeta$ (Connes spectral / NCG, Deninger and Weil cohomology, Li and Weil positivity, Hesselholt THH/TC, prismatic, $\mathbb{F}_1$) produces the same easy thing: a REALIZATION of $\zeta$ as a trace, a determinant, a Dirichlet-series identity, or an explicit formula. That half is comparatively buildable, and several frameworks already build it. RH is the OTHER half: a SIGNATURE, a positive-definite pairing (a polarization) on a primitive subspace of some cohomology of $\mathrm{Spec}(\mathbb{Z})$. The convergence thesis of this project (see [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) and the 15-candidate scorecard in [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md)) is that this second half is the same object in every framework, and it is unsolved over $\mathbb{Z}$.

A bespoke system is worth building only if it respects one rule, and the rule is sharp enough to discard most designs immediately:

> **A bespoke system that only captures the realization half is worthless.** It is buildable for Davenport-Heilbronn (D-H), and D-H is a counterexample to its own RH-analogue (a functional equation, no Euler product, known off-line zeros near $\rho \approx 0.8085 + 85.699\,i$). Any system whose central primitive D-H can also instantiate cannot separate $\zeta$ from the counterexample, so it cannot be proving RH.

The naive design fails this rule. The obvious central object is the trace functional $\mathrm{Tr}$, because $\mathrm{Tr}(\Pi^k)$ recovers the Dirichlet coefficients and the explicit formula, and that is genuinely easy to set up. But D-H has a functional equation and an explicit formula, hence a trace, so a trace-centered system is D-H-buildable by construction. It is the wrong core.

The correct design makes the SIGNATURE the primitive. The central object is the Rosati trace form $B(x,y) = \mathrm{Tr}(x\, y^\dagger)$, together with the involution $\dagger$ and a polarization witness $\mathrm{pol}$ from which the positivity of $B$ is meant to FOLLOW. $\mathrm{Tr}$ is kept, but demoted: it is realization-side data that the system supports and does not lean on for the separation. The signature primitives ($\dagger$, $B$, $\mathrm{pol}$) and the single open axiom (the positivity of $B$) all sit on top of an algebra $A$ that exists only when an Euler product supplies a Frobenius element. That formation rule is exactly the D-H firewall: no Euler product means no $A$, means no $B$, means the one positivity statement that is RH cannot even be STATED for the counterexample.

This is the recommended system. Section 2 presents it. Section 3 states which single axiom is open and which are dischargeable. Section 4 gives the RH derivation chain. Section 5 gives the first-steps lemma ladder. Section 6 presents the synthetic alternative and explains honestly why it converges back to the same wall. Section 7 records the $\Pi^0_1$ / reverse-math reading and what it does and does not buy. Section 8 documents the DuckDB tracking substrate. Section 9 lists the first five lemmas to actually prove.

---

## 2. The recommended system: the Polarization-Interface System

**One line.** A small axiomatic system whose core primitive is the Rosati trace form $B(x,y) = \mathrm{Tr}(x\, y^\dagger)$ on an arithmetic Frobenius algebra $A$ of $\mathrm{Spec}(\mathbb{Z})$, where RH reduces to a single open axiom (no negative spectrum of $B$, the arithmetic Hodge standard conjecture), and the whole tower is uninhabited for Davenport-Heilbronn by formation, because no Euler product means no Frobenius element exists.

### 2.1 Primitives

The deliberate choice is to put the signature, not the realization, at the core. The chosen primitives are $(A, \Pi, \dagger, \mathrm{Tr}, B, \mathrm{pol})$, not $(\text{operator}, \text{eigenvalues}, \text{determinant})$. The latter set realizes $\zeta$ and is D-H-buildable. The former set is engineered so the one object whose positivity is RH ($B$ read through $\mathrm{pol}$) is the one object that cannot be instantiated for D-H.

| Symbol | Kind | Description |
|--------|------|-------------|
| $A$ | object | The arithmetic Frobenius algebra of $\mathrm{Spec}(\mathbb{Z})$: a finite-dimensional, place-graded $\mathbb{R}$-algebra, the arithmetic analogue of $\mathrm{End}^0(\mathrm{Jac}\,C) \otimes \mathbb{R}$, generated by the Deninger Frobenius correspondence. EXISTS ONLY when an Euler product supplies the Frobenius element. This is where D-H non-instantiation lives at the primitive level: no Euler product, so $A$ is uninhabited. |
| $\Pi$ | object | The Frobenius element of $A$ (analogue of the $q$-Frobenius $\pi$ on $H^1$). Its existence is conditioned on the Euler product via the Frobenius correspondence. $\Pi\,\Pi^\dagger = c\cdot 1$ with $c$ the scaling scalar (analogue of $q$). RH constrains the eigenvalues of $\Pi$ to $|\alpha| = \sqrt{c}$. |
| $\dagger$ | operation | A Rosati-type involution on $A$: an $\mathbb{R}$-linear anti-automorphism with $x^{\dagger\dagger} = x$ and $\Pi^\dagger \Pi = c\cdot 1$. The analogue of the Rosati adjoint with respect to the canonical polarization. A signature-side primitive: $\dagger$ is what makes $B$ symmetric and what couples $B$ to the polarization. |
| $\mathrm{Tr}$ | functional | An $\mathbb{R}$-linear trace $A \to \mathbb{R}$ with $\mathrm{Tr}(uv) = \mathrm{Tr}(vu)$. Realization-side data: $\mathrm{Tr}(\Pi^k) = t_k$ recovers the Dirichlet / explicit-formula coefficients. D-H-BUILDABLE and deliberately NOT the core. |
| $B$ | functional | **THE CORE PRIMITIVE.** The Rosati trace form $B(x,y) = \mathrm{Tr}(x\, y^\dagger)$, a symmetric bilinear form on $A \otimes \mathbb{R}$. The presence or absence of negative spectrum of $B$ is the entire content of RH. |
| $\mathrm{pol}$ | relation | The polarization witness: a distinguished positive class $h \in A$ (the canonical polarization) from which $B$'s positivity is meant to FOLLOW, so positivity comes from geometry, not from the zeros. K1-non-circularity lives here: $\mathrm{pol}$ is the source, the spectrum of $B$ is the consequence. Over $\mathbb{F}_q$, $\mathrm{pol}$ exists (canonical polarization on $\mathrm{Jac}\,C$); over $\mathbb{Z}$, constructing $\mathrm{pol}$ is the open work. |

### 2.2 Axioms

Seven axioms. Six are inputs and one (`AX-POL`) carries all the open content. The `dh_satisfiable` column is the firewall in one bit: it is false for everything except the realization dictionary `AX-ZERO`.

| id | layer | status | dh_satisfiable | statement (abridged) |
|----|-------|--------|----------------|----------------------|
| `AX-FORM` | foundation | proven_lean | false | Formation rule: $A$ (hence $\Pi, \dagger, B, \mathrm{pol}$) is defined only on top of `EulerProductData(L)`; without an Euler product $A$ is uninhabited. Mirrors the Lean `cupTarget_requires_eulerProduct`. |
| `AX-INV` | bridge | proven_ff | false | $\dagger$ is an involution ($\mathbb{R}$-linear, anti-multiplicative, $x^{\dagger\dagger}=x$) and $\Pi^\dagger \Pi = \Pi\,\Pi^\dagger = c\cdot 1$ for a positive scalar $c$. |
| `AX-SYM` | bridge | proven_ff | false | $B(x,y) = \mathrm{Tr}(x\,y^\dagger)$ is symmetric: $B(x,y) = B(y,x)$. Follows from $\mathrm{Tr}(uv)=\mathrm{Tr}(vu)$ and `AX-INV`. |
| `AX-GRAM` | bridge | proven_ff | false | On the cyclic basis $\{1,\Pi,\dots,\Pi^{n-1}\}$ the Gram of $B$ is $G[a][b] = c^{\min(a,b)}\, t_{\lvert a-b\rvert}$, $t_k = \mathrm{Tr}(\Pi^k)$. Exactly the experiment 2T formula. |
| `AX-SPEC` | bridge | proven_ff | false | $B$ positive on $\mathbb{R}[\Pi]$ implies every eigenvalue $\alpha$ of $\Pi$ has $\lvert\alpha\rvert=\sqrt{c}$, and conversely. Weil's specialization, finite linear algebra. |
| `AX-ZERO` | realization | proven_ff | **true** | Realization identity: zeros of $L(s)$ biject with eigenvalues of $\Pi$, with $\lvert\alpha\rvert=\sqrt{c} \iff \mathrm{Re}(s)=1/2$. The ONLY D-H-satisfiable axiom: D-H has a functional equation and explicit formula, so it too has a zero-spectrum dictionary. This is exactly why the realization half cannot separate. |
| `AX-POL` | **signature** | **open** | false | **THE single open arithmetic content.** Polarization positivity over $\mathbb{Z}$ (arithmetic Hodge standard conjecture): $B$ on $A \otimes \mathbb{R}$, read through $\mathrm{pol}$, has NO negative spectrum. Proven over $\mathbb{F}_q$ (Weil) and char 0 (Hodge-Riemann); OPEN over $\mathbb{Z}$. UNBUILDABLE for D-H because $A$ does not exist (`AX-FORM`). |

### 2.3 Where D-H unbuildability lives (a property of the primitives, not of a certificate)

D-H unbuildability is structural at the primitive level. $A$ is defined by `AX-FORM` to exist only on top of `EulerProductData(L)`. D-H has a functional equation but no Euler product, so `EulerProductData(davenport_heilbronn)` is uninhabited. In Lean its `has_euler_product` field has type `False` ([`FrobeniusAlgebra.lean:36,59-61`](../../lean/ZetaRH/FrobeniusAlgebra.lean)), and therefore $A, \Pi, \dagger, B, \mathrm{pol}$ do not exist for D-H. Since `AX-POL` is a statement about the spectrum of $B$, and $B$ does not exist for D-H, `AX-POL` is VACUOUS for D-H. The system cannot even state the positivity it would need to "prove D-H-RH."

This is the lemma `L-DH-NONINST` (`proven_lean`), a direct port of `no_dh_cupTarget` ([`FrobeniusAlgebra.lean:141-144`](../../lean/ZetaRH/FrobeniusAlgebra.lean)). It is the K2 guard expressed by TYPE, not by string-matching. The only D-H-satisfiable axiom is `AX-ZERO` (on `layer = realization`), because D-H does have an explicit formula and thus a trace.

---

## 3. The single open axiom, and the five dischargeable ones

### 3.1 The open arithmetic content: AX-POL

`AX-POL` is the polarization positivity over $\mathbb{Z}$, identical to the arithmetic Hodge standard conjecture for the Deninger Frobenius correspondence, equivalent to negative-definiteness of the primitive intersection / cup form. It is the M4 milestone of [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md). It is the SINGLE non-dischargeable axiom (database invariant INV2).

It must be supplied by CONSTRUCTING $\mathrm{pol}$ over $\mathbb{Z}$ (Arakelov / Green pairing glued to finite places) and proving positivity FOLLOWS from $\mathrm{pol}$, never by reading positivity off the zeros (K1). The only non-circular form anyone can currently compute, $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ from the $\Gamma$-factor and von Mangoldt primes with no zeros, reads $\min\mathrm{eig}(M) = +0.035$ for $\zeta$ but ALSO $+0.094$ for D-H (the stealth window). That is the proof that `AX-POL` cannot be closed by a soft certificate.

### 3.2 The five dischargeable axioms (cite, do not assume)

`AX-FORM` is `proven_lean` (formation by type). `AX-INV`, `AX-GRAM`, `AX-SPEC`, `AX-SYM` are `proven_ff`; `AX-SYM`/`AX-GRAM`/`AX-SPEC` are also char-0 theorems and Lean-formalizable as linear algebra of $\mathbb{R}[\Pi]$. `AX-ZERO` is `proven_ff`, the easy D-H-buildable half. The two discharges of `AX-POL` itself (`L-POL-FF` over $\mathbb{F}_q$, `L-POL-CHAR0` via Hodge-Riemann) confirm it is TRUE wherever a polarization or Hodge structure exists, localizing the open content to "no arithmetic Hodge structure over $\mathbb{Z}$."

### 3.3 An honesty correction: over $\mathbb{Z}$ the open core is fatter than one axiom

Over $\mathbb{Z}$ the involution $\dagger$ is DEFINED by $\mathrm{pol}$ (a Rosati adjoint exists only with respect to a polarization). So `AX-INV` over $\mathbb{Z}$, the scaling $c$, $\mathrm{pol}$, and `AX-POL` co-depend on constructing the polarized algebra. The honest accounting splits the flag: `dischargeable_FF` true for `AX-INV`/`AX-GRAM`/`AX-SPEC`; `dischargeable_Z` true only for `AX-FORM`/`AX-SYM`/`AX-ZERO`. The corrected open core is "the polarized arithmetic Frobenius algebra $(A,\Pi,\dagger,\mathrm{pol})$ exists and $B$ is positive," of which `AX-POL` is the positivity half. The phrase "definitional requirement on the constructed $A$" is retired.

---

## 4. The RH derivation: a four-link chain

1. **Reduction (`L-RH-EQUIV`, theorem).** `AX-ZERO` plus the spectral equivalence give: RH for $\zeta$ $\iff$ "$B$ has no negative spectrum on $A$." No open content.
2. **Spectral equivalence (`L-SPEC-EQUIV`, `proven_ff`).** From `L-GRAM-ENTRY` and `L-G1-PD` ($4c-t^2>0$): no-negative-spectrum on the Toeplitz-Hankel Gram $\iff |\alpha|=\sqrt{c}$. Finite linear algebra.
3. **The positivity (`AX-POL`).** The ONLY non-dischargeable input, sourced from $\mathrm{pol}$ (K1-non-circular). Equals the open M4 step.
4. **The K2 safety check (`L-DH-NONINST`, `proven_lean`).** The chain is vacuous for D-H, so the system structurally cannot prove the false D-H-RH.

Net: RH $\Leftarrow$ (`L-RH-EQUIV`: theorem) $+$ (`AX-POL`: the one open axiom). Invariant INV5 (RH transitively depends on `AX-POL`) passes.

A firewall honesty note: the type guard certifies D-H is EXCLUDED, but $\zeta$'s `has_euler_product` is a placeholder `True` ([`FrobeniusAlgebra.lean:48,52`](../../lean/ZetaRH/FrobeniusAlgebra.lean)). Until VERIFIER target EP-1 replaces it and constructs $\Pi$, the firewall is one-sided. This is a coordinate, not a wall: it names EP-1 as the precise next Lean obligation.

---

## 5. The small-lemma ladder

| id | status | depends on | statement (abridged) |
|----|--------|------------|----------------------|
| `L-SYM` | proven_ff | `AX-INV` | $B(x,y)=B(y,x)$ via $\mathrm{Tr}(x y^\dagger)=\mathrm{Tr}(y x^\dagger)$. |
| `L-GRAM-ENTRY` | proven_ff | `AX-INV` | $B(\Pi^a,\Pi^b)=c^{\min(a,b)}t_{\lvert a-b\rvert}$, from $\Pi^\dagger=c\,\Pi^{-1}$. |
| `L-G1-PD` | proven_ff | `L-GRAM-ENTRY` | $g=1$: PD iff $4c-t^2>0$ iff $\lvert t\rvert<2\sqrt{c}$. |
| `L-SIGNFLIP` | proven_ff | `L-GRAM-ENTRY` | Primitive intersection form $=-B$: $B$ positive $\iff$ intersection negative definite. |
| `L-DH-NONINST` | proven_lean | `AX-FORM` | No inhabitant of $A$ for D-H. Port of `no_dh_cupTarget`. |
| `L-SPEC-EQUIV` | proven_ff | `L-GRAM-ENTRY`, `L-G1-PD` | $B$ positive $\iff \lvert\alpha\rvert=\sqrt{c}$. |
| `L-RH-EQUIV` | proven_ff | `L-SPEC-EQUIV`, `AX-ZERO` | $B$ positive $\iff$ zeros on $\mathrm{Re}(s)=1/2 =$ RH. |
| `L-POL-Z` | **open** | `L-POL-FF`, `L-POL-CHAR0`, `L-ARITH-GRAM` | **THE OPEN STEP.** Construct $\mathrm{pol}$ over $\mathbb{Z}$, prove `AX-POL` on $A_P$, control $P\to\infty$. |

Everything up to `L-RH-EQUIV` is a theorem and Lean-formalizable now. The hard content is isolated in `L-POL-Z`.

---

## 6. The synthetic alternative, and why it converges back (the honesty point)

The Polarized Flow Site (PFS) is a maximally synthetic contrast: a site $X_{\mathrm{flow}}$ with a one-parameter flow, an orbit-trace, a six-functor duality, and an ABSTRACT polarization functor $\mathrm{Pol}$ giving $Q_L(x,y)=\mathrm{Tr}(x\cdot D(L\cdot y))$ on $\mathrm{Prim}\subset H^1$. It never names a Frobenius endomorphism algebra. Its realization axioms (site, determinant, duality, hard Lefschetz) are D-H-satisfiable and dischargeable.

**The collapse lemma `L8-COLLAPSE`.** The moment you require the orbit trace to produce the $\{\log p\}$ spectrum and a definite pairing on $\mathrm{Prim}$, the function-field anchor plus the collapse lemma show $Q_L$ on $\mathrm{Prim}$ is naturally isomorphic to the Rosati trace form of Section 2. So $\mathrm{PFS}$-`A6` equals arithmetic Rosati positivity equals the arithmetic Hodge standard conjecture. The Frobenius primitives are NOT forced, but the signature they carry IS forced. The contrast did not produce a new handle; it proved the hard content is invariant across framings. That is why Section 2 is recommended: it states the forced object in the most direct vocabulary, with the firewall already in Lean.

**Two corrections the contrast forced (sharpening the discipline for both systems):**
- D-H has a trace; it just does not factor. The D-H von Mangoldt object does not vanish, it DELOCALIZES (mass roughly $37.4$ off prime-powers vs $36.9$ on, first leak at $n=6$). The correct guard is "the polarization is DEFINABLE for D-H and its positivity correctly FAILS at $\gamma\approx 85.7$," upgrading the discipline from D-H-EXCLUDED to D-H-AWARE. Section 2 inherits the caution: the type firewall is clean, but a concrete $A_P$ lets D-H through (the stealth window).
- The Euler / $\{\log p\}$ content is signature-relevant, not pure realization (the prime-block ablation in e3p carries the discriminating sign). The honest headline is two open ingredients, not one.

---

## 7. The $\Pi^0_1$ / reverse-math reading

RH is $\Pi^0_1$ (Lagarias/Robin/DPRM), statable at EFA (Parikh); see [`rh_logical_status.md`](rh_logical_status.md) and [`lean/ZetaRH/RHEquivalences.lean`](../../lean/ZetaRH/RHEquivalences.lean). A bespoke object theory does NOT lower the bar: `AX-POL` as $v^\top Q_L^{(P)} v \ge -\varepsilon(P)$ is itself $\Pi^0_1$-shaped. The custom theory RELABELS the analytic content into matrix positivity; it does not discharge it.

What it buys: independence implies truth (a proof of independence proves RH true; undecidability is a back door), and a refutability asymmetry (one off-line witness refutes; only a uniform statement proves). What it does NOT buy: lower logical strength (the $N(T)$ / argument-principle step has no established reverse-math home; Friedman's grand-conjecture expectation is speculation). Treat `FND-rh-pi01` as a constraint on the target, not a load-bearing premise.

---

## 8. The DuckDB lemma graph

Tracked in [`experiments/lemma_db/`](../../experiments/lemma_db/): [`schema.sql`](../../experiments/lemma_db/schema.sql), [`seed_lemmas.json`](../../experiments/lemma_db/seed_lemmas.json) (60 nodes, 96 edges: the 36-node proof skeleton plus the 2026-06-05 import of the four gap-property conjuncts and the 17 Spec(Z) cohomology candidates), [`build_db.py`](../../experiments/lemma_db/build_db.py), [`queries.sql`](../../experiments/lemma_db/queries.sql).

**Model.** Three tables (`node`, `edge`, `obstruction_link`), six views. Controlled vocabularies are `CHECK`-enforced on `kind`, `status`, `layer`, `dh_buildable`.

**The central decision: the load-bearing / annotation split.** Edge kinds partition into load-bearing (`depends_on`, `specializes`) and annotation (`instantiates`, `contradicts`, `bridges`, `motivates`, `informs`, `constrains`, `contextualizes`). The `load_edge` view exposes only the former; every reachability view and the acyclicity check traverse it alone. An edge that merely records "this negative result informs that target" cannot smuggle a D-H-buildable node onto the proof obligation.

**Key queries.** `frontier` (open nodes with all load-deps proven, surfaces `AX-POL`), `rh_transitive_deps` (the 23-node, 9-open RH obligation), `dh_audit` (the firewall test: `dh_buildable='true'` content nodes on the load path, zero rows after fixes), `open_signature_nodes`, `dischargeable_axioms` (the `specializes` self-join encoding the M1-to-M4 lift).

**Discipline enforcement.** `build_db.py` exits non-zero if `dh_audit` is non-empty (the D-H detector as a CI gate). K1 is a query (no `numerical_only` node load-feeds `AX-hodge-riemann` / `LEM-pole-eigenvalue-bridge`). The M1-M5 ladder is the `milestone`/`status`/`layer` join. Defense in depth: duplicate-id / dangling / self-loop guards, Kahn acyclicity, single-sink check, transactional rollback, idempotent rebuild.

**Audited corrections already in the graph:** `LEM-m3` flipped to `dh_buildable='true'` with its edge to M4 downgraded to `motivates`; `OBS-marginal-positivity` to `true`; `TGT-rh`'s three non-logical premises downgraded to `constrains`/`contextualizes`; `AX-noncircular-source` retagged to `foundation`; the four placeholder-Euler nodes annotated formation-only (EP-1 open).

---

## 9. The first five lemmas to actually prove

1. **`L-SYM`** (`proven_ff`, Lean now). Dep: `AX-INV`. Symmetry of $B$, pure $\mathbb{R}[\Pi]$ linear algebra. The smallest brick.
2. **`L-GRAM-ENTRY`** (`proven_ff`). Dep: `AX-INV`. The Gram formula from $\Pi^\dagger=c\,\Pi^{-1}$. Unlocks the next three.
3. **`L-G1-PD`** (`proven_ff`, by hand). Dep: `L-GRAM-ENTRY`. $4c-t^2>0$; also the smallest place to SEE that over $\mathbb{Z}$ you cannot fill in $c$ or $\dagger$ without $\mathrm{pol}$.
4. **`L-DH-NONINST`** (`proven_lean`, a port). Dep: `AX-FORM`. Port `no_dh_cupTarget` to the abstract $A$; puts the firewall in the primitive layer.
5. **`L-POL-FF`** (`proven_ff`, cite Weil). Dep: `L-GRAM-ENTRY` + Weil's Rosati-positivity. The first beachhead on the open axiom, with the Gram from POINT COUNTS not zeros. The right place to start the K1 provenance audit.

Honest closing coordinate: lemmas 1-5 do not advance the difficulty of RH (`AX-POL` over $\mathbb{Z}$ is equivalent to RH, so this is a reduction in CONFUSION, not difficulty). What they buy: all scaffolding is shown to be theorems, the D-H exclusion is structural and machine-checked, and the single remaining object ($\mathrm{pol}$ over $\mathbb{Z}$) is named with maximal precision. That object is M4. Constructing it, or proving it cannot exist in any candidate cohomology, is the whole game. The system says exactly where to stand to play it.

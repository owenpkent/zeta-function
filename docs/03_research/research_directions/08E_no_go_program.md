# Direction 8E: The conditional no-go program. A ledger of which construction classes provably cannot source the RH polarization, and where the live boundary sits.

> A SYNTHESIZER/INFRA assembly written 2026-06-05, consolidating the DISPROVE thread. It does not propose a new construction. It assembles the program's accumulated no-go results into a single ledger, states the kill criterion (K5) that keeps the program on the safe side of a logical landmine, and names the one open boundary (class E) honestly as open.
>
> Companion: the no-go nodes in [`../../experiments/lemma_db/`](../../experiments/lemma_db/) (one obstruction/theorem node per class A-E, wired by annotation edges only). Cross-links: [`08D_sen_nonsemisimplicity_obstruction.md`](08D_sen_nonsemisimplicity_obstruction.md) (the model no-go, class A), [`08A_rosati_standard_conjecture.md`](08A_rosati_standard_conjecture.md) (RH = arithmetic Hodge standard conjecture, M4), [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md) (the universal gap and its four-property decomposition).

## 0. What this program is, in one paragraph

The universal gap (08A M4, the arithmetic Hodge standard conjecture) is a single object: a signed intersection pairing on the global $H^1$ of the product $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$, with Frobenius correspondence $\Gamma_S$ of bidegree $(1,p)$, whose negative-definiteness on the primitive part is proven WITHOUT RH input. A graph diagnostic decomposed it into a four-property conjunction (PROP-global, PROP-carries-trace, PROP-rh-equivalent, PROP-noncircular). The DISPROVE program does not try to build the object. It tries to prove, for each candidate CLASS of construction, a CONDITIONAL no-go: no construction of that class realizes all four properties. Each valid no-go prunes a branch and sharpens where the proof must live. The program is bounded by a strict kill criterion (K5) that keeps every no-go a proper-subclass statement, never a universal one, because a universal no-go would disprove RH.

## 1. The logical landmine (the spine; do not violate it)

Define $J$ := "there exists a construction realizing PROP-global AND PROP-carries-trace AND PROP-rh-equivalent AND PROP-noncircular" (joint realizability of the universal gap object).

Three implications fix what we may target.

- (a) $J \Rightarrow \mathrm{RH}$. THEOREM, by construction. Any joint realizer is a polarization on the primitive global $H^1$ whose negative-definiteness is RH-equivalent and proven without RH input; its positivity forces the zeros onto $\mathrm{Re}(s)=1/2$. This is the function-field Weil/Rosati template (verified end-to-end in the record: e2t/2G, 08A M1) transported to $\mathbb{Z}$. Building the object proves RH.
- (b) $\mathrm{RH} \Rightarrow J$. OPEN. This is exactly "does RH admit a motivic/cohomological proof." Over $\mathbb{F}_q$ it holds (Weil supplied the polarization from the canonical theta-divisor; the Rosati form $\mathrm{Tr}(x\,x^\dagger)$ is provably positive). Over $\mathbb{Z}$ it is unknown.
- (c) Contrapositive of (a): $\lnot\mathrm{RH} \Rightarrow \lnot J$. Hence an UNCONDITIONAL theorem "the four are not jointly realizable by ANY construction" would yield $\lnot\mathrm{RH}$.

RH is almost certainly true ($10^{13}+$ zeros verified, the $\Pi^0_1$ status in [`../rh_logical_status.md`](../rh_logical_status.md)). So any purported unconditional no-go is almost certainly an ERROR with a hidden circular or class-overreaching step. We NEVER target the unconditional no-go. The only sound deliverable is the CONDITIONAL no-go: "no construction of class $C$ realizes all four," with $C$ provably a PROPER subclass. This is safe because $\lnot J|_C$ does not imply $\lnot J$ (the class is strictly smaller), so it never trips (c).

## 2. The K5 kill criterion (the validity gate)

NEW KILL CRITERION K5: a proposed no-go "class $C$ cannot realize all four properties" is VALID only if its class $C$ is provably strictly smaller than "all constructions." Operationally, three checks.

- CHECK 1 (smallness witness): exhibit a named structure $S$ that is a construction in the ambient sense but does NOT belong to $C$, so the no-go's hypotheses do not apply to $S$. If no such $S$ can even be named, $C$ is secretly "all" and the no-go is malformed.
- CHECK 2 (disproof test, contrapositive of the landmine): ask "if this no-go were a theorem, would it, combined with $J \Rightarrow \mathrm{RH}$, yield $\lnot\mathrm{RH}$?" If yes, the class is secretly "all"; REJECT or narrow. The argument must use a property SPECIFIC to $C$ (e.g. "sources positivity from the archimedean Sen module $\Theta$"), never a property shared by every conceivable construction.
- CHECK 3 (relocation clause): a valid conditional no-go must NAME where the demand relocates: the strictly-smaller complement where the polarization could still live. 08D is the model: it kills "source from $\Theta$" (class A) and relocates to "source from the Frobenius/F-half ample class" (class E, untouched by the theorem).

The class A no-go (08D / #72) passes all three and is the program's template.

## 3. The class table (per-class status)

Each class tries to SOURCE the polarization from a different structure. The table is the no-go ledger.

| Class | Source of positivity | Property it fails | Status | K5 | Node |
|---|---|---|:--:|:--:|---|
| **A** | archimedean Sen module $\Theta$ (Hodge-Tate-weight operator) | PROP-noncircular (imports $Q$); arithmetic-blind by type | **THEOREM (proven_char0)** for its subclass | PASS | `OBS-classA-sen-compact-group` |
| **B** | truncated determinant/trace functional (band-limited to height $\le \log N$) | PROP-carries-trace in its D-H-discriminating reading, at finite $N$ | **STRONG EVIDENCE (numerical_only)** | PASS (finite-$N$ only) | `OBS-classB-resolution-floor` |
| **C** | combinatorial/matroid (AHK) Chow-ring Hodge-Riemann form | PROP-carries-trace (no continuous slot for $t$) | **THEOREM for fixed type; strong evidence for full class** | PASS | `OBS-classC-ahk-signature-rigidity` |
| **D** | archimedean de Branges reproducing-kernel | PROP-rh-equivalent (overshoots, REFUTED) | **REFUTED (a fact, not a conditional)** | N/A | `OBS-classD-debranges-refuted` |
| **E** | Frobenius/F-half arithmetic ample class (the Euler-pole $H^2$) = the universal gap | none for full E; a K2 tension for E-local | **OPEN (the live boundary)** | landmine: full E malformed, E-local PASS | `OBS-classE-pincer-live-boundary` |

### 3.1 Class A: closed (consolidate, do not redo)

The compact-group theorem (08D, #72): the Tate-equivariant cup duality $\Theta^{\mathsf T} B + B\,\Theta = -w B$ rewrites as $\Theta + (w/2)I \in \mathfrak{so}(B)$. If $B$ is positive-definite then $O(B) = O(n)$ is compact, so $\mathfrak{so}(B)$ consists of $B$-skew (semisimple) operators, forcing $\Theta$ semisimple, $\nu = 0$. Contrapositive: Petrov's non-semisimple Sen operator ($\nu \ne 0$, arXiv:2302.11389, Annals) admits no positive-definite invariant cup form. The only surviving fallback (the CKS form $Q_\ell(x,y) = Q(x, \nu^\ell y)$ on $\nu$-primitive pieces) imports its positive factor $Q$ from a polarized VHS that does not exist over $\mathrm{Spec}(\mathbb{Z})$; supplying $Q$ = RH (the transport theorem, #68). K5-PASS: witness outside $C$ = the F-half ample class; conditional on $\nu \ne 0$; relocates to E. This is a clean Lean-formalizable linear-algebra theorem (see section 5). Honest residual: the non-CKS manufacture of $Q$ from $\Theta$ is the hairline where A touches E, correctly left open.

### 3.2 Class B: strong evidence, strictly resolution-bounded

The soft-detector wall (#18-20, #34, #47, #63; soft_detector_wall.md, a FROZEN thread). A truncated trace functional reads $+0.035$ for zeta and $+0.094$ for D-H (M2.6 four-way FAIL): no separation. The discriminating signal of an off-line zero at height $\gamma$ enters at order $\epsilon^2 \exp(-(\pi/4) d\gamma)$, which is $O(1)$ only once $N \ge e^\gamma$ (resolving height $\gamma$ needs primes to $e^\gamma$). For D-H's first off-line zero $\gamma \approx 85.7$ this demands $N \ge e^{85.7} \approx 10^{37}$, unreachable. The SOUND no-go is strictly finite-$N$: the EXACT ($N=\infty$) functional IS D-H-aware (#63, defect spike $0.617$ at $\gamma\approx 85.7$). The unbounded version ("no trace functional EVER separates") is MALFORMED (it contradicts #63 and edges toward "all," tripping the landmine) and is explicitly REJECTED. Promotion to a theorem (a quantitative uncertainty / Beurling-Malliavin resolution floor) is open and valuable, and must stay finite-$N$.

### 3.3 Class C: theorem for fixed type, the cheapest clean conditional no-go still available

Signature-rigidity (#40, #48). The AHK form $Q_l^q$ and its inertia are invariants of the combinatorial isomorphism type of the matroid alone (the degree map is normalized to $1$ on every complete flag; the $(-1)^q$ sign is parity; AHK definiteness is UNCONDITIONAL for every matroid, realizable or not). There is no continuous real slot for an external scalar. The RH-equivalent FF Gram $G_{\mathrm{prim}}(g,q,t) = \begin{pmatrix}-2g & -t \\ -t & -2gq\end{pmatrix}$ flips negative-definiteness exactly at $|t| = 2g\sqrt q$ (Lean `negDef_iff_hasseWeil`: $t^2 < 4 g^2 q$), so its verdict depends continuously on $t$. A constant-in-$t$ object (any AHK form, reading the same $(1,3)$ for $t=2$ and $t=100$) cannot equal a $t$-flipping predicate. Hence no fixed combinatorial form carries the trace. The honest residual escape (a $t$-indexed matroid family $M_t$ with an HR phase transition at the Hasse-Weil bound) is exactly where C touches E and is open; such a family would BE the arithmetic ample class. K5-PASS (witness outside $C$ = the FF Rosati form, which sees $t$). The fixed-type lemma is a one-line Lean theorem (section 5).

### 3.4 Class D: refuted (a fact, fully closed)

The de Branges space of $\xi$ realizes the continuation as a signed reproducing-kernel inner product that DOES reach the global zeros, but its positivity is strictly stronger than RH (it implies GRH for all Dirichlet $L$ simultaneously). Conrey-Li PROVED it FAILS for zeta: the per-zero cross-term is negative at POSITIVE DENSITY ($\sim 6\%$ at $K=500$, drifting UPWARD to $\sim 8\text{-}13\%$ at $K=1000$; the anchor reproduced to 12 sig figs, #43). So the kernel positivity is FALSE for zeta even though RH is (conjecturally) true: the wrong target. K2-blind (built on the shared archimedean kernel). This is a REFUTATION, not a conditional no-go; K5 does not apply (there is no class to validate); the bracket is the one dead bracket, fully closed. (Note: the record is stronger than "the 34th zero"; cite the positive-density version.)

### 3.5 Class E: the open boundary (do NOT claim closed)

Class E IS the universal gap. A full-E no-go would disprove RH (the K5 landmine: obstructing all of E denies joint realizability) and is never targeted. Only the strictly-smaller E-LOCAL no-go is sound (section 4). The live front is unchanged: construct the F-half ample class on the Euler-pole $H^2$ and prove its Hodge-index positivity without RH input. That remains genuinely open, and that is where the proof must live.

## 4. The K2 pincer (the live mechanism)

The deepest structural tension and the program's sharpest compass. Two requirements pull opposite ways.

- PULL 1 (separate from D-H): by kill criterion K2, ONLY the Euler/Frobenius half $F$ (the $\{\log p\}$ / von Mangoldt trace, the $(1,p)$ bidegree) separates zeta from Davenport-Heilbronn. The archimedean/continuation half ($\Gamma$-factor, Sen $\Theta$, Sonin space, de Branges kernel) is SHARED by D-H (verified at $\ge 40$ digits: FE residual $\sim 1.8\times 10^{-43}$ zeta, $\sim 1.1\times 10^{-40}$ D-H, identical-by-type; only $-\zeta'/\zeta$ = von Mangoldt on prime powers vs D-H's non-multiplicative $a(n)$, $a(6)=+1$ but $a(2)a(3)=-0.0807$, separates them). So the discriminating positivity must ride $F$.
- PULL 2 (reach the zeros): the actual zeros live in the analytic continuation $\mathrm{Re}(s) < 1$. The local Euler/orbit data converges only for $\mathrm{Re}(s) > 1$ and cannot reach the off-line strip on its own. Reaching the continued zeros requires the continuation, carried by the ARCHIMEDEAN place.

The pincer (candidate no-go MECHANISM, sound ONLY as an E-LOCAL conditional under hypotheses H1-H3): no construction that (H1) sources its sign from local Frobenius data $\{\log p, a_k\}$ alone, (H2) continues to $\mathrm{Re}(s)<1$ solely by the D-H-shared archimedean block, and (H3) does NOT already contain the global product $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ with $\Gamma_S$, can reach the off-line zeros. EVIDENCE this is real, not yet a theorem: the M2.6 four-way FAIL is the pincer biting numerically ($M = +0.035$ zeta, $+0.094$ D-H; D-H's off-line obstruction, $\sim 2.6\%$ of the spectrum at $\gamma \approx 85.7$, sits below the reconstruction-residual floor at every reachable truncation).

CRUCIAL: the pincer is NOT a wall around the prize. The target object STRADDLES by construction, exactly as the function-field template does. On $C \times C$ over $\mathbb{F}_q$, the Frobenius correspondence $\Gamma$ is a global product object whose self-intersection sees the trace $t$ AND whose Rosati positivity controls all eigenvalues at once (the analogue of reaching $\mathrm{Re}(s)<1$). A straddler provably EXISTS over $\mathbb{F}_q$. Supplying the global product $+\,\Gamma_S$ (negating H3) makes $t$ a GLOBAL datum (the Frobenius point count, #70/2LO), fuses PROP-global with PROP-carries-trace into one bundled datum, and breaks the pincer's local-times-archimedean factorization. So the pincer correctly explains why class B and E-local cannot work and correctly points AT the global product as the escape; it does not, and by K5 must not, close class E.

## 5. The meta-theorem shape (how the union of no-gos approaches "RH needs new structure" without disproving RH)

Index the classes $C_1, C_2, \dots$ (A, B, C, D, E, ...). Each valid conditional no-go is $\lnot J|_{C_i}$, with $C_i$ a proper subclass. The program accumulates the union $U = \lnot J|_{C_1} \wedge \lnot J|_{C_2} \wedge \cdots$ = "no construction in $C_1 \cup C_2 \cup \cdots$ realizes all four." As classes broaden and fall, the covered union grows. In the limit where it exhausts every CURRENTLY-BUILDABLE class, $U$ becomes the meta-statement: "RH needs structure outside every currently-buildable class" = "the polarization requires not-yet-invented structure." This is a statement about the STATE OF MATHEMATICS, not the truth-value of RH.

Why it never disproves RH: the union is, at every finite stage and in the as-far-as-we-can-build limit, STRICTLY SMALLER than "all constructions," because "all constructions" includes not-yet-invented ones. The open converse $\mathrm{RH} \Rightarrow J$ is precisely that SOME construction (possibly not-yet-invented) realizes the four. $U$ leaves that escape hatch permanently open and asymptotes to "all" from strictly inside; the landmine ($\lnot J \Rightarrow \lnot\mathrm{RH}$) is never tripped.

Two honest closing outcomes, neither a disproof: (1) RH proved by inventing the structure outside every then-current class (the accumulated no-gos retroactively become a map of where the proof could NOT have come from); (2) the boundary characterized positively (a theorem that the realizer must have a specific new feature, turning the union of negatives into a named requirement). Outcome (2) in its terminal form is equivalent to settling whether RH has a motivic proof (the arithmetic Hodge standard conjecture, 08A M4), itself a famous open problem of RH-depth. So the program can rigorously map where the proof cannot come from; it cannot reach "the proof must have feature X, which is unconstructible" without proving RH or a standard-conjecture-strength statement.

## 6. The honest verdict

This is the directional reading the project mandates. Each no-go is a COORDINATE narrowing the search, never a verdict that the proof cannot exist.

- THEOREMS (conditional, K5-clean): Class A (08D / #72), a genuine compact-group + transport theorem for its subclass; consolidate, do not redo. Class C, theorem-grade for the fixed-combinatorial-type subclass (Lean #C-1), the cheapest clean conditional no-go still available.
- REFUTATION (a fact): Class D, de Branges fails for zeta at positive density. Fully closed.
- STRONG EVIDENCE (not a theorem): Class B, the soft-detector wall, sound only as the finite-$N$ resolution floor; the unbounded version is malformed and rejected.
- THE OPEN BOUNDARY: Class E, the universal gap. Not closed, and correctly so. Only E-local (under H3) is a sound conditional. The single most valuable next no-go is to promote Class C's fixed-type lemma to Lean and then attack the $t$-indexed-matroid escape as an explicit open hypothesis; the deepest candidate theorem (the K2 pincer) is the live boundary and must stay conditional on H3.

The two disciplines to enforce going forward: keep Class B finite-$N$, and keep Class C's status honest (subclass-theorem, not full-class). The live front is unchanged and now sharper: build the F-half ample class on the Euler-pole $H^2$, a global product object that fuses the trace $t$ (F-side) and the zero-reach (archimedean continuation) in ONE Frobenius correspondence, polarized by an arithmetic Hodge index proven without RH input. Building it is RH.

## 7. Cross-links

- [`08D_sen_nonsemisimplicity_obstruction.md`](08D_sen_nonsemisimplicity_obstruction.md): the model no-go (class A), the compact-group theorem in full.
- [`08A_rosati_standard_conjecture.md`](08A_rosati_standard_conjecture.md): RH = arithmetic Rosati positivity = arithmetic Hodge standard conjecture; the M1-M5 ladder; M4 = class E = the universal gap.
- [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md): the universal gap, the three proven bracket signatures (Faltings-Hriljac too-local, AHK too-blind, de Branges too-strong), the four-property decomposition, the K2 cut.
- [`../../experiments/lemma_db/`](../../experiments/lemma_db/): the no-go nodes (`OBS-classA-sen-compact-group`, `OBS-classB-resolution-floor`, `OBS-classC-ahk-signature-rigidity`, `OBS-classD-debranges-refuted`, `OBS-classE-pincer-live-boundary`) wired by annotation edges to the PROP conjuncts and `TGT-m4-hodge-standard`.

# The sourcing gap (R1): a weight-1 $\sqrt q$ carrier is variety-gated

> Written 2026-06-27, after the AHK route to P3 closed into R1 ([`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md) Section 6D; [`../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md`](../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md), LEARNINGS #129). It answers a single sharp question and records the literature verification (a SURVEYOR pass over Sarnak, Fontaine-Mazur, Lafforgue, Deligne, Drinfeld-module RH, Scholze torsion). The question is the cleanest statement of the program's universal gap, so it earns its own note.

## The question

> Can a **non-Tate weight-1 object with modulus-$\sqrt q$ Frobenius** ($H^1$ with all eigenvalues $|\alpha|=\sqrt q$) be **sourced without a variety**?

This is the residual R1 the AHK arc reduced to. RH-for-a-curve runs on $H^1(C)$, whose Frobenius eigenvalues satisfy $|\alpha|=\sqrt q$ (purity) and whose primitive cup form is a polarization. To get RH for $\zeta$ over $\mathrm{Spec}(\mathbb{Z})$ from a combinatorial / non-geometric source (no surface), one must first manufacture that $\sqrt q$-weight-1 carrier from the prime data directly. The AHK route ([09A](research_directions/09A_ahk_arithmetic_lattice.md)) showed combinatorics cannot: a matroid Chow ring is purely even / Tate, with no $H^1$ at all (e2yy/#124), and no super-AHK induction runs on a hand-grafted odd piece (e2zb/#129).

## Shape versus purity

Split R1 into two genuinely different asks:

1. **Source the shape**: a non-Tate, weight-1 object with *some* Frobenius/Galois action. Comparatively easy and genuinely doable without a variety: 2-dimensional Galois representations, automorphic (Maass) forms, the Bost-Connes / KMS modular structure, even artificial representations.
2. **Source it with provable $|\alpha|=\sqrt q$ (purity)**: the hard part, and on all available evidence equivalent to having a motive (a variety).

The combinatorial routes (AHK, tropical) fail at **(1)** already: they are Tate (no weight-1 shape) or, in the tropical case, Frobenius-free (over $(\mathbb{R},\max,+)$: no $q$, no $\sqrt q$, no Galois). The automorphic / Galois routes have the shape but not provable purity. Nobody has **(2)** without a variety.

## The verified answer: conjecturally NO, operationally OPEN

A SURVEYOR pass hard-checked four claims (HOLDS / WEAKENED / REFUTED, with reading-depth flagged); all hold.

| # | Claim | Ruling | Key citation |
|---|---|---|---|
| 1 | Weight-1 $|\alpha|=\sqrt q$ purity is PROVEN only via varieties/stacks | HOLDS | Deligne, Weil II; even Lafforgue's function-field GRC realizes the rep in the $\ell$-adic cohomology of the **moduli stack of Drinfeld shtukas**, then invokes Deligne purity |
| 2 | Fontaine-Mazur $\Rightarrow$ a pure geometric weight-1 $\sqrt q$ Galois rep is motivic | HOLDS as direction / WEAKENED as a lever (CONJECTURE; proven GL2/$\mathbb{Q}$ cases route motivicity through a Kuga-Sato variety; and it presupposes a Galois action a combinatorial object lacks) | Kisin (JAMS 2009), Emerton |
| 3 | Ramanujan for **Maass** forms is OPEN precisely because there is no variety; for holomorphic forms it is a Deligne theorem via the modular curve | HOLDS (verbatim in Sarnak) | Sarnak, Clay 2005, pp. 660, 663-664 |
| 4 | No genuinely variety-free pure weight-1 $\sqrt q$ object is known | HOLDS | composite; each near-counterexample fails one clause of {variety-free, $\sqrt q$-bearing, proven-pure} |

### The cleanest dramatization: holomorphic versus Maass (Sarnak)

For **holomorphic** modular forms, Ramanujan $|a_p|\le 2\sqrt p$ is **Deligne's theorem** *because* $\Gamma_0(N)\backslash\mathbb{H}$ is a moduli space of elliptic curves (a variety): the bound is the purity of Frobenius on the $\ell$-adic cohomology of a Kuga-Sato variety. For **Maass** forms, the symmetric space $SL_n(\mathbb{C})/SU(n)$ is non-Hermitian, so (Sarnak, p. 664) "there is no apparent algebro-geometric moduli interpretation," and Ramanujan is **open**, with only partial bounds (Kim-Sarnak $7/64$), never $\theta=0$. The instant the variety is removed, purity becomes open. The variety *is* the purity.

### Why each candidate variety-free source fails

- **Drinfeld modules / Anderson $t$-motives** (incl. the RH preprint arXiv:2512.12374): purity is proven, but the $t$-motive *is* a geometric-arithmetic object (a Tate module with a genuine Frobenius), and it lives only over function fields of characteristic $p$, not $\mathrm{Spec}(\mathbb{Z})$. Fails variety-free + wrong base.
- **Nori / Voevodsky / pure motives**: defined starting from smooth (projective) varieties; they reorganize variety-cohomology, they do not source purity ex nihilo. Fails variety-free by construction.
- **Scholze torsion classes / Calegari-Geraghty**: the closest to "automorphic but not yet motivic," but the Galois reps are extracted from the cohomology of locally symmetric / Shimura varieties, and purity for the genuinely non-self-dual (Maass-type) objects is open. Fails variety-free + proven-pure.
- **Amini-Piquerez non-Tate tropical Kähler / Babaee-Huh / tropical Jacobians**: genuinely combinatorial and genuinely non-Tate (so they refute the naive "combinatorial $\Rightarrow$ Tate"), but **Frobenius-free** (no $q$) with a positive-definite (wrong) signature. Fails $\sqrt q$-bearing entirely.

## The structural framing: the universal gap has two variety-gated facets

The [spec_z cohomology landscape](spec_z_cohomology_landscape.md) records that every candidate **realizes** $\zeta$ as a trace and **none** carries the **polarization** (the universal gap $=$ M4). R1 sharpens this. The universal gap has two facets, both variety-gated, distinct theorems in general, coincident in the genus-1 shadow:

- **(A) Sourcing / purity (R1).** Produce a weight-1 carrier with $|\alpha|=\sqrt q$. Over $\mathbb{F}_q$ this is **Deligne's purity theorem**, which holds for any variety; the verified R1 finding is that no *non-geometric* source for it is known.
- **(B) Polarization / signature (M4).** The arithmetic Hodge standard conjecture: the primitive cup form is definite with the indefinite $(1,n-1)$ signature. Over $\mathbb{F}_q$ this is **Weil's / the Rosati positivity** (a theorem for abelian varieties).

For a curve (genus 1) the two collapse to one inequality: $|\alpha|=\sqrt q \iff$ the primitive form is negative-definite $\iff t^2<4q$ (e2g). In general they are distinct (Deligne purity is a *weight* statement; the Hodge standard conjecture is *positivity*), and both are theorems over the function field precisely because there is a variety. Over $\mathrm{Spec}(\mathbb{Z})$ neither has a known non-geometric source. R1 is therefore not a softer residual we reduced to: it is the **sourcing facet of the same universal gap**, and it is exactly the residual lever B reaches (the scheme-theoretic existence of the rank-2 Frobenius/Tate-module datum, [`research_directions/lever_b_function_field_plan.md`](research_directions/lever_b_function_field_plan.md), #108).

## Gap, not obstruction

There is no impossibility theorem. "Variety-free $\Rightarrow$ no $\sqrt q$-purity" is a strong empirical regularity and the negative shadow of Fontaine-Mazur plus the open Maass-form status, but it has **not** been proven. So R1 cannot be closed by citation; it can only be closed by

- (a) **supplying** the geometric / motivic source (the FLT-adjacent existence problem the Arakelov face inherits), or
- (b) genuinely **refuting** the regularity with a variety-free pure-$\sqrt q$ construction, which would itself be a major theorem (a non-geometric proof of purity).

This is why every construction route in the project walls identically: each supplies **realization** (the shape) and none supplies **purity without a variety** (facet A) or **the polarization** (facet B). The Deninger program is precisely the attempt to be such a variety-free source; so R1 is the Deninger / arithmetic-cohomology-of-$\mathrm{Spec}(\mathbb{Z})$ question, stated at the sharpest level.

## References

- Peter Sarnak, *Notes on the Generalized Ramanujan Conjectures*, Clay Math. Proc. 4 (2005), pp. 659-666 (the decisive reference: proven purity = geometric; the holomorphic-vs-Maass split; "no algebro-geometric moduli interpretation" for the non-Hermitian case).
- P. Deligne, *La conjecture de Weil II* (purity from Frobenius on étale cohomology of varieties).
- J.-M. Fontaine, B. Mazur, *Geometric Galois representations* (the conjecture); M. Kisin, *The Fontaine-Mazur conjecture for $GL_2$*, JAMS 22 (2009); M. Emerton (completed cohomology).
- L. Lafforgue (function-field GRC via moduli of shtukas); cf. arXiv:2204.06053; Rapoport, *The work of Laurent Lafforgue*.
- *On the Riemann Hypothesis for Drinfeld Modules*, arXiv:2512.12374 (purity for $t$-motives, function-field only).
- P. Scholze, *On torsion in the cohomology of locally symmetric varieties*.

## Cross-references

- [09A Section 6D](research_directions/09A_ahk_arithmetic_lattice.md) (where R1 was named), [`../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md`](../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md) (R2 closes into R1), [`../../experiments/arithmetic_geometric/e2za_ahk_p3_super_graft.md`](../../experiments/arithmetic_geometric/e2za_ahk_p3_super_graft.md).
- [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) (the universal gap; R1 is its sourcing facet), [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the thesis R1 refines), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (M4, facet B).
- LEARNINGS #129 (AHK route closed into R1), #130 (this verification).

# The Spec(Z) cohomology landscape: who realizes zeta, and where the polarization is missing

> A consolidating reference map for Direction 8, written 2026-06-02. It answers a direct
> question: **"do we need to do Spec(Z) cohomology work, and is it unsolved?"** Short answer:
> yes, and it is unsolved at one precise point. Every serious candidate **realizes** $\zeta$ as a
> trace/determinant; **none** carries a **polarization** (a signed pairing whose positivity is RH).
> The polarization is the universal gap, and supplying it is not a shortcut to RH: it **is** RH
> (the arithmetic Hodge standard conjecture, [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) M4).
>
> Built from a survey/synthesis workflow grounded in the project findings #26-#44 and the
> reference-library reading notes; the three most load-bearing 2024-2026 literature items were
> verified against the originals (arXiv:1807.06400, 2302.11389, 2602.15941). Cross-checked against
> the project's own experiments. Distinguishes PROVEN from CONJECTURAL throughout.

## 1. The requirement (why "realizing zeta" is the easy half)

Weil's proof of RH for a curve $C/\mathbb{F}_q$ runs on a cohomology $H^1(C)$ that carries three things:

- **(i) Trace.** Frobenius acts with eigenvalues $\alpha_i$ = the "zeros," and $\zeta_C$ is a ratio of
  characteristic determinants $\det(1 - \mathrm{Frob}\, q^{-s} \mid H^i)$. (A realization of $\zeta$ as a determinant/trace.)
- **(ii) Duality.** Poincare duality $H^1 \otimes H^1 \to H^2$ **is** the functional equation $\xi(s)=\xi(1-s)$.
- **(iii) Polarization.** A positive-definite Rosati/Hodge-index form on the primitive part. Its
  positivity forces $|\alpha_i| = \sqrt q$, which **is** RH-for-$C$.

The project verified this entire template in the function-field case (2G/2T, four equivalent faces).
The thesis "all roads to the signature" (#30) is the empirical finding that **over Spec(Z) every
candidate delivers (i), most deliver a partial (ii), and none delivers (iii).** (iii) is the
irreducible content, and it equals RH.

**The universal gap has two variety-gated facets (2026-06-27, #130, [`sourcing_gap_r1.md`](sourcing_gap_r1.md)).**
Pushing the AHK route to its end ([09A](research_directions/09A_ahk_arithmetic_lattice.md) Section 6D) plus a
literature verification (Sarnak, Fontaine-Mazur, Lafforgue, Deligne) sharpens "(iii) is the gap" into two
distinct-but-linked facets, both variety-gated:

- **(A) Sourcing / purity (R1):** produce a weight-1 carrier with $|\alpha|=\sqrt q$ in the first place.
  Over $\mathbb{F}_q$ this is **Deligne's purity theorem** (free for any variety); the verified finding is
  that **no non-geometric source for it is known** (every proof of weight-1 purity routes through a
  variety/stack; the holomorphic-vs-Maass split dramatizes it: the moment you remove the variety, Ramanujan
  becomes open). The combinatorial candidates fail HERE, before (iii): a matroid Chow ring is purely Tate
  with no $H^1$, and the tropical objects are Frobenius-free.
- **(B) Polarization / signature (M4):** the cup form is definite with the indefinite $(1,n-1)$ signature.
  Over $\mathbb{F}_q$ this is **Weil / Rosati positivity**.

For a curve (genus 1) the two collapse to one inequality ($|\alpha|=\sqrt q \iff$ negative-definite $\iff
t^2<4q$, 2G); in general they are distinct theorems (a weight statement vs a positivity statement), both
holding over the function field exactly because there is a variety. So the scorecard's "(i) free, (iii)
missing" is more precisely: realization gives the *shape*, while both the *purity* of the carrier (A) and the
*polarization* (B) are the variety-gated content. It is a **gap, not an obstruction** (no impossibility
theorem); it closes only by supplying a geometric source (the FLT-adjacent problem the Arakelov face
inherits) or by a variety-free proof of purity (itself a major theorem).

## 2. The scorecard

Legend: ✓ = present/proven, ◑ = partial or proven-only-in-a-restricted-sense, ✗ = absent.
"Trace (i)", "FE (ii)", "Polariz. (iii)" are the three Weil ingredients; "K2" is the
Davenport-Heilbronn discipline (does the structure distinguish $\zeta$ from the no-Euler-product
counterexample); "Open step" is the single sharpest missing object.

| Candidate | (i) | (ii) | (iii) | K2 | Single sharpest open step |
|---|:--:|:--:|:--:|:--:|---|
| **Deninger** foliated dynamical system / R-flow | ◑ | ◑ | ✗ | ✓ (on $F$) | intersection form on $X\times X$ + Hodge-index signature, no RH input |
| **Connes** 1999 adele-class trace formula | ✓ | ◑ | ✗ (K1 wall) | ✓ (on $F$) | global (all-places) Weil positivity; spectral identification as a theorem |
| **Connes** $\eta_x$ / Weil-form CF (2602.04022) | ✓ (Thm 6.1) | ◑ | ✗ (K1 wall) | ✓ (only via unproven limit) | convergence $k_\lambda \to \theta_x$ ($\Leftrightarrow$ global Weil positivity $=$ RH) |
| **Connes-Consani** arithmetic site + square | ✓ (diag.) | ◑ | ✗ (#40) | ✓ | the arithmetic $q$-lift restoring the trace $t$ at the $(1,p)$ bidegree |
| **Connes-Consani** Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$ (2026) | ◑→✓ | ◑ | ✗ | ✓ (on $F$) | turn the Picard/realization structure into a signed pairing (not de Branges) |
| **Bhatt-Lurie** absolute prismatic / WCart | ✓ (both halves) | ◑ (duality proven, no positivity) | ✗ | ✓ (on $F$) | a positive cup-product / Rosati form on the global prismatic $H^1$ |
| **Bhatt-Scholze** per-prime prismatic | ◑ (local) | ◑ (local) | ✗ | ✓ | assembly over all $p$ + the polarization |
| **Hesselholt** TP/TC ($\zeta=\det_\infty(s-\Theta\mid TP_{odd}/TP_{ev})$) | ✓ (proven /$\mathbb{F}_q$) | ◑ (proven /$\mathbb{F}_q$) | ✗ over $\mathbb{Z}$ | ✓ | define TP over $\mathbb{Z}$ with a periodic flow + negative-definite cup form on $TP_{odd}$ |
| **Kucharczyk-Scholze** topological Galois realization | ✗ | ✗ | ✗ | n/a | an archimedean cohomology compatible with the cyclotomic/Witt substrate |
| **Faltings-Hriljac** single-surface arithmetic Hodge index | ✗ (no $\zeta$) | ◑ (wrong dim) | ◑ **PROVEN, but single surface** | vacuous | the **product** $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ + Frobenius $\Gamma_S$ |
| **Gillet-Soule** arithmetic Riemann-Roch | ✗ | ◑ (wrong dim) | ◑ (inherits single-surface) | vacuous | cycle-class for $\Gamma_S$ on the product + arithmetic standard conjecture |
| **Deitmar** monoid schemes | ✗ | ✗ | ✗ | vacuous | a non-collapsing 2-dim self-product + a cohomology |
| **Lorscheid** blueprints | ✗/◑ | open | ✗ | ✓ | intersection theory + cycle class on the (2-dim) blueprint surface |
| **Borger** $\Lambda$-rings / $\mathrm{Spec}(W(\mathbb{Z}))$ | ◑ (Frobenius built in) | open | ✗ | ✓ | a finite 2-dim $\Lambda$-cohomology of $\mathrm{Spec}(W(\mathbb{Z}))$ with an intersection form |
| **Soule / Kurokawa** $q\to1$ absolute zeta | ◑ (formal) | ◑ (by hand) | ✗ | weak/untested | a genuine cohomology behind the $q\to1$ bookkeeping |
| **Adiprasito-Huh-Katz** matroid Hodge theory | ✗ | ✗ | ◑ **PROVEN signature, no variety, but arithmetic-blind** | structure only | the sharpened AHK lattice ([09A](research_directions/09A_ahk_arithmetic_lattice.md)): a $t$-carrying submodular Lefschetz element + an indefinite $(1,n-1)$ primitive form |
| **Boucksom-Jonsson** NA Monge-Ampere / K-stability | ✗ | ✗ | ✗ (convex one-sided, not indefinite) | structure only | **killed (#97):** valuative at a single Berkovich place, archimedean-blind, no $t$-slot (the AHK too-blind bracket in new vocabulary) |
| **Clausen-Scholze** condensed/analytic six functors + norm-stack $\mathcal{N}/\mathbb{R}_{>0}$ | ✗ (no $\zeta$) | ✓ (Poincare-Verdier, perfect, **no sign**) | ✗ (perfectness, not polarization) | structure only | **WATCH as substrate (#119):** the best archimedean-inclusive base ($\infty$ a first-class Berkovich branch), but a native polarization needs an "archimedean Deligne-Illusie" (conjectural); the perfect-duality-over-unified-base upgrade of the #71 trio |

**2P+ sharpening (2026-06-05, LEARNINGS #71, [memo](../../experiments/arithmetic_geometric/2P_recent_global_signed_trace_pairing_probe.md)).** A targeted audit of the three strongest recent constructions against the (iii)-polarization column (a signed pairing on the global $H^1$ whose value sees the trace $t$, not just the $(1,p)$ bidegree), after 2LO (#70) named $t$ as the single missing datum. **None supplies it; they stop at three different adjacent inputs that are three two-thirds of the SAME construction:** Tang's prismatic Poincare duality ([arXiv:2210.14279](https://arxiv.org/abs/2210.14279), Compositio; F-gauge perfect duality $R\Gamma(X)^\vee\simeq R\Gamma(X)\{d\}[2d]$ + trace maps) gives **perfectness, not the Hodge-Riemann/Rosati sign**; Gurney's *Prismatization over $\mathbf{Z}$* ([arXiv:2301.12392](https://arxiv.org/abs/2301.12392)) gives the **global substrate, not the cup/sign/$t$**; Connes-Consani's 2026 Jacobian ([arXiv:2602.15941](https://arxiv.org/abs/2602.15941)) gives the **trace/realization, not a signed product pairing**. So the post-2LO gap is unchanged and identical for all three: construct $\Gamma_S$, form the primitive cup into the Euler-pole $H^2$, and prove the sign without RH input. Perfectness is free (even for D-H, 2HH/#61); the polarization carrying $t$ is the whole gap.

**QM/spectral currency (2026-06-24, dossier [`quantum_mechanics_signature_dossier.md`](../../experiments/spectral/quantum_mechanics_signature_dossier.md); LEARNINGS #111).** The Connes-Consani prolate/semilocal program confirms this scorecard from the operator-algebra side. Connes-Consani PROVED a Weil-positivity fragment (arXiv:2006.13771, Selecta Math. 2021) but ONLY at the archimedean place (the $\Gamma$-factor half D-H shares), so the literature now confirms the K2 firewall's prediction with a **published theorem** that the one provable positivity is RH-agnostic. The 2024 semilocal prolate operator (Connes-Consani-Moscovici, arXiv:2310.18423) is the one QM object that injects Euler content on the Frobenius side (measure $|\prod_v L_v(\tfrac12-is)|^2$, $S$-dependent Jacobi matrix, structurally unbuildable for D-H) with an explicit positivity **strategy** (realize the Weil form as an automatically-positive self-adjoint trace, then condition by the radical): strategy-not-theorem, standing K1 risk, door **ajar** (R3.5 leaves intersection-theoretic positivity open by construction). Same gap as (iii) above, in operator-algebra clothing. Bender-Brody-Müller (2017) is the canonical K1 wall (quasi-Hermiticity $\iff$ real spectrum $\iff$ RH; Bellissard operator-existence kill).

## 3. The two proven signatures that bracket the gap

The single most useful structural fact in the landscape: there exist exactly **two proven
Hodge-index-type signatures** anywhere near the problem, and **both miss in a precisely diagnosable
way**. A third, the de Branges pairing, overshoots; a fourth, the Rankin-Selberg / Deligne-Weil-II
positivity, is a different-type bracket (a proven *analytic* positivity, non-circular and Euler-essential,
that is too shallow to reach the line). Together they bracket the missing object from four sides.

- **Faltings-Hriljac (too local).** The arithmetic intersection form on a **single** arithmetic
  surface is negative semi-definite on the primitive part; equivalently the Neron-Tate height
  pairing is positive-definite. This is a **real, proven polarization** (the project reproduced it
  end-to-end, 2H-2P, ranks 1-4). It fails to give RH only because it lives on one surface of
  relative dimension $\ge 1$, **not** on the product $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$,
  and carries no Frobenius correspondence reaching the zeta zeros. *Too local.* The whole
  generalized-arithmetic-Hodge-index family shares this bracket: Moriwaki's higher-dimensional
  arithmetic Hodge index and Yuan-Zhang's adelic-line-bundle index theorem prove the same
  negative-definiteness on a *fixed* arithmetic variety (a Dirichlet-unit / non-archimedean-Calabi
  statement), and Cantat-Gao-Habegger-Xie *use* the single-variety index for the geometric Bogomolov
  conjecture rather than extending it to a product (2026 Arakelov-face probe,
  [2L](../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md) §4). Bost's theta-invariant /
  pro-Hermitian infinite-dimensional Arakelov geometry is genuinely over the arithmetic curve but is a
  *different* miss: it produces a Diophantine $h^0_\theta$ (a non-negative scalar), the wrong signature
  class, not an indefinite $(1,n-1)$ form.
- **Adiprasito-Huh-Katz (too blind).** The Kahler package (including Hodge-Riemann positivity) holds
  on the Chow ring of **any** matroid, even non-realizable ones: a **signature with no underlying
  variety**, exactly the shape Weil's proof wants. It fails because it is **arithmetic-blind**: it
  takes no Frobenius trace $t$ (the project's #40 mixed-volume probe reads the same $(1,3)$ signature
  for $t=2$ and $t=100$), and its log-concavity defect tracks non-Euler-ness, not RH-failure (e3n:
  the non-Euler RH-true Epstein control has the *most* violations). *Too blind.* **But it is the one
  retained positive coordinate of the 2026-06-14 breadth-over-proof-engines sweep (#97):** alone among
  the five from-below engines it is K1-clean (the signature comes from a submodular flip, not the
  zeros), so the response is not to drop it but to repair the blindness. The sharpened BUILDER target
  [`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md)
  asks for a finite graded prime-lattice whose degree map carries $t$ ($= q+1-t$ on the function-field
  shadow) and whose primitive form is born indefinite $(1,n-1)$, leaving only the positivity (= M4)
  open. The same sweep killed the Lorentzian / tropical / non-archimedean-Monge-Ampere (Boucksom-Jonsson)
  family as the AHK too-blind bracket in new vocabulary, and killed CKS limit-MHS as a transport (it
  imports the polarization $Q$ that $\mathrm{Spec}(\mathbb{Z})$ lacks). *Too blind, but the one face
  worth grafting arithmetic onto.*
- **de Branges (too strong).** The de Branges space of $\xi$ realizes the continuation as a signed
  reproducing-kernel inner product that **does** reach the global zeros, but its positivity is
  **strictly stronger than RH** (it implies GRH for all Dirichlet $L$ at once) and Conrey-Li proved
  it **fails for $\zeta$** at the 34th zero (the project reproduced this to 12 sig figs, #43/2DB.1).
  *Too strong.*
- **Rankin-Selberg / Deligne-Weil-II (too shallow).** Deligne's 1974 Weil-II proof reaches
  $|\alpha|=\sqrt q$ **without** the Hodge index theorem, via global monodromy of a Lefschetz pencil
  plus the Rankin-Selberg even-tensor-power positivity (the pole structure of $L(s,\mathrm{Sym}^{2k})$).
  Its one variety-free number-field shadow is the classical Rankin-Selberg / de la Vallee-Poussin
  positivity (the $3+4\cos\theta+\cos 2\theta\ge 0$ engine behind the zero-free region). That positivity
  is **proven, non-circular** (K1-clean: it comes from the pole of $L(s,\pi\times\tilde\pi)$ at $s=1$ and
  from non-negative convolution coefficients, *not* from reading the zeros) and **Euler-essential** (it
  correctly does NOT fire for D-H, which has no Rankin-Selberg square), but it lives at the
  $\mathrm{Re}=1$ edge and provably **saturates the Vinogradov-Korobov $2/3$ ceiling**: it cannot be
  pushed to $\mathrm{Re}=1/2$. *Too shallow.* Walked to its wall over a number field the monodromy engine
  SPLITS into exactly the two facets already on this map: the geometric core needs the purity/monodromy
  group that only a variety supplies (the R1 facet, [`sourcing_gap_r1.md`](sourcing_gap_r1.md)), and the
  variety-free shadow is Architecture 4 (the analytic ceiling). It is the 13th independent confirmation of
  the convergence, now from the weights/monodromy direction (2026-06-28 first-principles audit). Unlike
  Weil-I Hodge-index/Rosati positivity, it is genuinely a *different engine*, which is why it is worth a
  distinct bracket; it is no more tractable.

So the missing object is pinned by four sides: a polarization that is **global** (unlike
Faltings-Hriljac), **carries the arithmetic trace $t$** (unlike AHK), is **RH-equivalent, not
strictly stronger** (unlike de Branges), and is **deep enough to reach $\mathrm{Re}=1/2$** (unlike
Rankin-Selberg, which is a real, non-circular, Euler-essential positivity but is $2/3$-capped at the
$\mathrm{Re}=1$ edge).

## 4. The universal gap, stated precisely

Every candidate is missing the same object:

> A **signed intersection pairing on the global $H^1$ of the product** $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$
> (with its Frobenius correspondence $\Gamma_S$ of place-dependent bidegree $(1,p)$, #25/2Q, and
> regularized self-intersection $\Gamma_S^2 = $ the von Mangoldt sum, #26/2R), whose
> negative-definiteness on the primitive part is proven **without RH input**. This is the arithmetic
> Hodge standard conjecture / Rosati positivity (08A M4).

Why it is hard, localized by the project's recent coordinates:

- The zeros live in the **analytic continuation** $\mathrm{Re}(s) < 1$, where the local Euler/orbit
  data cannot reach (it converges only for $\mathrm{Re}(s) > 1$). The pairing must realize the
  continuation, carried by the **archimedean place** (#42/2CC.3).
- The free convex-geometry signatures (mixed volume / AHK) are **arithmetic-blind**: they have no
  slot for $t$ (#40/2CC).
- The trace lives on the diagonal ($\mathrm{Id}_\epsilon$ = von Mangoldt, #41/2CC.2; the prismatic
  Frobenius $F$ + Sen $\Theta$, #44/2PR.1), but the **signature** of the off-diagonal global $H^1$
  is exactly what no determinant supplies.
- A new structural obstruction: the prismatic Sen operator is **not semisimple** in general (Petrov,
  Annals), so the polarization cannot be built eigenspace-by-eigenspace; it must be intrinsic.

A passive-network reading ([`acoustic_passive_lossless.md`](acoustic_passive_lossless.md), LEARNINGS #90-94) gives the (i)/(ii)/(iii) template a physical name: (i) trace $=$ a **passive** medium ($Z=-\zeta'/\zeta$ has a positive von Mangoldt comb $\Leftrightarrow$ Euler product, unconditional); (ii) FE-duality $=$ **reciprocity**; (iii) polarization $=$ **losslessness**, the signature that **halves** the free passive bound $\mathrm{Re}\le 1 \to \mathrm{Re}\le\tfrac12$. The halving is Poincaré duality placing the self-dual middle weight at the geometric mean of the extremes ($q^{1/2}=\sqrt{q^0\cdot q^1}$), so (iii) is precisely "supply the weight filtration whose self-dual middle is $\mathrm{Re}=\tfrac12$." This confirms the universal gap from the acoustic side and explains why (i) is free while (iii) is RH: passivity is the Euler product, losslessness is the missing signature. It is a clarifying language, not a new construction (the network synthesis route lands on Suzuki's canonical system, RH-equivalent).

## 5. Closest candidates and what each would need

- **Faltings-Hriljac / Gillet-Soule + a constructed product.** The positivity is already a theorem on
  a single surface; the missing piece is the **product surface and a Frobenius cycle class**. This is
  the most direct route: graft the proven arithmetic Hodge index onto $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$
  once that object and $\Gamma_S$ exist. (Lorscheid gives a 2-dim blueprint self-product; Borger gives
  $\mathrm{Spec}(W(\mathbb{Z}))$; neither has an intersection theory yet.)
- **Bhatt-Lurie / Hesselholt prismatic-TP.** The trace is realized most explicitly here (both halves
  of completed $\zeta$ as determinants, #44; Hesselholt's $\mathbb{F}_q$ theorem proven). It needs a
  **positive cup-product on the global prismatic/TP $H^1$**, now known to resist the naive
  eigenspace construction (Petrov). The realization machinery has gone fully global over Spec(Z)
  (Gurney, *Prismatization over $\mathbf{Z}$*, arXiv:2301.12392; the Drinfeld and Bhatt-Lurie
  prismatizations are p-adic/local), so the substrate exists; the polarization does not.
- **Connes-Consani.** The 2026 Jacobian paper builds a Picard/polarization **structure** on the
  absolute curve and the spectral-realization apparatus (prolate/zeta-spectral-triples), but defers
  the RH-positivity. By the project's R3.5 no-shortcut theorem, any trace-formula positivity in this
  framework is K1-equivalent to RH (no independent reduction), so the route must escape into an
  honest intersection signature, not a trace identity. The one genuinely proven positivity here is at
  the **archimedean place only** (the Sonin space), which is RH-agnostic (shared by D-H).

## 6. The K2 caveat that organizes everything

The Davenport-Heilbronn discipline cuts the problem cleanly in two. The **archimedean / continuation
half** (the $\Gamma$-factor, the Sonin space, the Sen $\Theta$ divisor, the de Branges kernel
positivity) is **shared by D-H** and is therefore RH-agnostic: D-H has the same functional equation
and $\Gamma$-factor by construction. **All K2 discrimination lives on the Euler-product / Frobenius
half** (orbit lengths $\{\log p\}$, the $(1,p)$ bidegree, the prismatic $F$, THH). So the
polarization that proves RH must be carried by the **Frobenius direction**, the one object that is
structurally unbuildable for D-H (no Euler product $\Rightarrow$ no Frobenius correspondence $\Rightarrow$
no surface). Any proposed positivity built only from the continuation/archimedean side is
automatically K2-blind (#38/#43/#44).

## 7. Recent frontier (2024-2026)

The realization side is moving fast; the polarization has not moved. Verified items:

- **Deninger's foliated space is now constructed.** Via sheafified rational Witt vectors $W_{rat}(X)$,
  for normal schemes of finite type over $\mathrm{Spec}(\mathbb{Z})$, with an $\mathbb{R}$-flow whose
  periodic orbits biject with closed points ([arXiv:1807.06400](https://arxiv.org/abs/1807.06400),
  2018). The regularized-determinant Lefschetz formula is proven for genuine 3-dimensional Riemannian
  foliated dynamical systems (Deninger, 2024). **This corrects the project's earlier "X has never
  been constructed" caveat: X is now constructed; its cohomology, duality, and polarization remain
  open.** Morishita 2025 ([arXiv:2508.15971](https://arxiv.org/abs/2508.15971)) builds an
  $\mathbb{R}_+$-anti-equivariant bridge (a duality dictionary) between Deninger's systems and the
  Connes-Consani adelic spaces for abelian number fields; no polarization is transferred.
- **A new obstruction on the prismatic side.** Petrov proved the Bhatt-Lurie Sen operator is **not
  semisimple** in general (a liftable smooth projective variety of dimension $p+1$ with
  non-degenerate Hodge-to-de-Rham spectral sequence), [arXiv:2302.11389](https://arxiv.org/abs/2302.11389),
  Annals. This blocks any eigenspace-based Hodge-Riemann polarization on the prismatic substrate.
- **Connes-Consani, "On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$"**
  ([arXiv:2602.15941](https://arxiv.org/abs/2602.15941), Feb 2026): interprets the adele class space
  as the Picard monoid of the absolute curve, "incorporating the singular strata required for the
  spectral realization of L-functions." It builds the realization/Picard structure; it states **no**
  positivity or RH result. This lands exactly on the pattern: structure on the realization side, the
  polarization deferred.
- **Connes, "Letter to Riemann"** ([arXiv:2602.04022](https://arxiv.org/abs/2602.04022), Feb 2026):
  a survey with a research kernel. **Theorem 6.1 (Connes-van Suijlekom)** proves that the minimal
  eigenvector $\eta_x$ of the truncated Weil form $QW_\lambda$ has a Fourier transform with all zeros
  on the critical line, **unconditionally for each finite cutoff** (primes $\le 13$ recover the first
  50 zeros to $2.6\times10^{-55}$..$10^{-3}$). This **sharpens the realization half** (an on-line-
  zeros theorem, not a trace identity), but supplies **no** polarization: Theorem 6.1 manufactures
  on-line zeros for *any* admissible even-kernel form, so it is zeta-blind, and the entire RH content
  sits in the unproven convergence $\eta_x \to E(h)$ (sec 6.6), which is global Weil positivity, i.e.
  RH. The project verified the zeta-blindness directly: the identical construction reproduces
  Davenport-Heilbronn's on-line zeros and (Caratheodory-Fejer) gives all-roots-on-circle for zeta-,
  D-H-, and random-derived symbols alike, while structurally missing D-H's off-line zero at
  $0.8085+85.699i$ (e3s/e3t,
  [`connes_2602_letter_to_riemann.md`](connes_2602_letter_to_riemann.md), LEARNINGS #50). The proven
  fragments (Sonin-space archimedean positivity, prolate $\hat k_\lambda\to\Xi$, Moscovici UV model)
  are the D-H-shared, RH-agnostic half. Same pattern: a sharper realization, polarization deferred.

Other 2024-2026 developments reported by the survey (to verify against originals before formal
citation): prismatic Poincare duality of perfect complexes (Tang, Compositio 2024) supplies
ingredient (ii) at the complex level with no positivity; Gurney's *Prismatization over $\mathbf{Z}$*
(arXiv:2301.12392) extends the p-adic Drinfeld / Bhatt-Lurie prismatizations to a global object over
Spec(Z), and Bhatt-Lurie F-gauges/syntomification assemble the realization apparatus; the
Connes-Consani-Moscovici prolate / "zeta spectral triples" program matches the lowest zeros to high
numerical accuracy and states explicitly that proving the convergence would establish RH (i.e. the
convergence/positivity is the unproven content). Yuan-Zhang (Math. Ann. 367, 2017) extended the
arithmetic Hodge index to adelic line bundles in higher dimension, still on a fixed scheme, never on
the product; Moriwaki's higher-dimensional arithmetic Hodge index (arXiv:1010.1599) and
Cantat-Gao-Habegger-Xie (Duke 170(2), 2021, which *uses* the single-variety index for the geometric
Bogomolov conjecture) sit on the same `NODE-fh-too-local` bracket, and Bost's theta-invariant /
pro-Hermitian infinite-dimensional Arakelov geometry (Prog. Math. 334, 2020; arXiv:1512.08946) is over
the arithmetic curve but produces a Diophantine $h^0_\theta$ scalar, the wrong signature class (a
positive scalar, not an indefinite $(1,n-1)$ form). The 2026 Arakelov-face probe
([2L](../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md)) confirms the verdict is
unmoved: no generalized arithmetic Hodge index theorem reaches zeta's zeros without the product surface,
and the e2ae artifact computes the one specified-but-uncomputed Arakelov entry
($\overline\omega^2 = 12\,h_{\mathrm{Fal}}$).

## 8. Honest caveats (proven vs conjectural)

- **PROVEN:** the function-field template (Weil, 2G/2T); the single-surface arithmetic Hodge index
  (Faltings-Hriljac, 2H-2P); the AHK Kahler package (no variety, arithmetic-blind); Hesselholt's
  determinant formula over $\mathbb{F}_q$; the archimedean Weil positivity (Connes-Consani Sonin
  space, RH-agnostic); prismatic Poincare duality (complex-level, no positivity); the Sen-spectrum
  $\to$ $\Gamma$-divisor identity (#44, a class function of the spectrum, real-but-only-heuristic);
  Deninger's foliated space construction.
- **CONJECTURAL:** the global determinant over $\mathbb{Z}$; the spectral identification
  $\mathrm{spec}(H) = \{\gamma_n\}$; the product surface $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$
  and its Frobenius cycle class; **every** product/global polarization. The arithmetic standard
  conjectures (the would-be source of RH-positivity) are themselves open.
- Do **not** read any candidate's realization (i) or duality (ii) as progress toward RH. RH is (iii),
  and (iii) is open in every framework. "Spec(Z) cohomology" is RH in cohomological clothing.

## 9. The sharpest next probe (for this project)

Given #40-#44, the live frontier is **the product surface + $\Gamma_S$** (08A M4). Two ways in,
both research-grade:

1. **Construction:** build the intersection theory on a constructed self-product (Lorscheid's
   2-dim blueprint surface, or Borger's $\mathrm{Spec}(W(\mathbb{Z}))$, or the Connes-Consani square),
   with a cycle class for $\Gamma_S$ carrying the $(1,p)$ bidegree, then attempt the
   Faltings-Hriljac-type negative-definiteness on the primitive part.
2. **Obstruction-first (recommended near-term):** the arithmetic $q$-lift that re-injects the
   Frobenius trace $t$ into the (arithmetic-blind) mixed-volume / AHK signature at the $(1,p)$
   bidegree, or a sharp no-go showing why the local-to-global continuation pairing cannot be a
   determinant. This is cheaper to probe and continues the #40-#44 sequence; the open question is
   whether the TP/flow or prismatic language gives any new leverage on the positivity (Petrov's
   non-semisimplicity says the obvious eigenspace route is blocked).

## Graph diagnostic: do the 17 candidate cohomologies collapse onto one gap node, or bracket it?

Recorded 2026-06-05 (SYNTHESIZER/INFRA import into `experiments/lemma_db`). This section pins the answer to the fork the scorecard was built to resolve: is the universal gap (the missing RH-equivalent polarization) a single irreducible node that every realization candidate lacks, or do some candidates sit off to the side as distinct near-misses that could be attacked directly?

### The graph diagnostic

Every candidate framework was entered as a new `kind=candidate` node and wired to the existing graph by ANNOTATION edges only (never `depends_on`/`specializes`, per the load-bearing-edge rule: a candidate substrate NEEDS the gap, it does not PROVE it). Each candidate's single sharpest open step resolves to exactly one target:

- COLLAPSE (`instantiates TGT-m4-hodge-standard`): 9 realization candidates. Deninger foliated R-flow, Connes-Consani arithmetic site, Connes-Consani Jacobian, Bhatt-Lurie WCart, Bhatt-Scholze per-prime, Hesselholt TP/TC, Lorscheid blueprints, Borger Lambda-rings, Soule-Kurokawa absolute zeta. They differ only in substrate, never in the positivity they lack (#71/2P+: the three strongest recent ones are three two-thirds of the same construction).
- OFF-TO-SIDE (`instantiates`/`specializes` a distinct `NODE-*`): 4 candidate frameworks over 3 distinct proven-signature bracket nodes. Faltings-Hriljac and its inheritor Gillet-Soule on `NODE-fh-too-local`; Adiprasito-Huh-Katz on `NODE-ahk-too-blind`; de Branges on `NODE-debranges-too-strong`.
- K1 WALL (`instantiates OBS-k1-circularity`): 2 candidates (Connes 1999 adele-class trace formula, Connes eta_x / Weil-form CF). A degenerate fourth direction: a trap to escape, not a near-miss to extend.
- PRE-REALIZATION (`instantiates PRIM-euler-product`): 2 candidates (Kucharczyk-Scholze, Deitmar). Upstream of the gap; no realized zeta whose polarization could be missing.

A DuckDB query (added to `queries.sql`) counts candidates by resolve-target and joins each off-to-side bracket to the one `PROP-*` node it violates. Result: `TGT-m4-hodge-standard` collapses 9 candidates (missing property = the conjunction itself, no single drop); the three `NODE-*` brackets each carry a distinct single missing property.

### The property decomposition

The gap node `TGT-m4-hodge-standard` is the LOGICAL CONJUNCTION of four independently-named properties, each a new signature-layer node that `TGT-m4-hodge-standard --depends_on-->` (load-bearing, all `dh_buildable=false`):

1. `PROP-global`: lives on the global H^1 of the PRODUCT (reaches the actual zeros via the Frobenius correspondence Gamma_S), not a single surface, not place-by-place.
2. `PROP-carries-trace`: the pairing's value sees the arithmetic Frobenius trace t (von Mangoldt); not arithmetic-blind.
3. `PROP-rh-equivalent`: positivity is EQUIVALENT to RH for zeta, not strictly stronger (no GRH overshoot).
4. `PROP-noncircular` (K1): positivity DERIVED from a polarization, never read off the zeros (R3.5 no-shortcut).

GAP = PROP-global AND PROP-carries-trace AND PROP-rh-equivalent AND PROP-noncircular. Each conjunct is proven-droppable by a distinct object, which is what makes the conjunction irreducible (no property is redundant): Faltings-Hriljac proves {carries-trace, rh-equivalent, noncircular} (drops global); AHK proves {global, rh-equivalent, noncircular} (drops carries-trace); de Branges realizes {global, carries-trace, noncircular} (drops rh-equivalent, and is REFUTED on it for zeta at the 34th zero, Conrey-Li, #43); the Connes trace-formula family drops noncircular (the K1 wall).

Two adversary calibrations are recorded as load-bearing-correct. (a) Independence is two-level: at the BRACKET level (proven char-0/F_q witnesses) the four are pairwise dissociable (the AHK-vs-FH dissociation, AHK global-but-blind vs FH trace-but-local), but for the LITERAL target object `PROP-global` and carries-the-zeta-trace are CO-DEPENDENT, one bundled datum (the product surface + Gamma_S = the global Frobenius point count t, per #70/2LO and #56). carries-trace dissociates from global only under the weaker reading 'arithmetic-sensitive in general' (how AHK fails it). So the true joint-realizability question is effectively 3-axis, not 4-free. (b) Asymmetry: `PROP-noncircular` is the only conjunct with no positive realization-candidate witness; it is witnessed-as-droppable only negatively (by the Connes family). There is no noncircular near-miss to extend, only a wall to escape.

### The collapse count

Of the 17 candidate frameworks: 9 COLLAPSE onto `TGT-m4-hodge-standard`; 4 sit OFF TO THE SIDE over 3 distinct bracket nodes; 2 are on the K1 wall; 2 are pre-realization. The collapse cohort (9) dominates. The K2 cut (section 6) splits the four properties cleanly: NEUTRAL / archimedean side (shared by Davenport-Heilbronn, RH-agnostic) carries `PROP-global` and `PROP-rh-equivalent`; the EULER / Frobenius side (the K2 discriminators, unbuildable for D-H) carries `PROP-carries-trace` and `PROP-noncircular`. Every load-bearing PROP node is `dh_buildable=false`, so the D-H audit stays clean (the firewall holds by type on the gap conjunction).

### Verdict

The gap is IRREDUCIBLE. The missing-positivity of the realization candidates collapses onto the single node `TGT-m4-hodge-standard`; the three proven signatures (Faltings-Hriljac, AHK, de Branges) are the genuine off-to-side nodes, each missing exactly ONE structural property, and together they bracket the gap from three sides. The no-go (the four-property conjunction) IS the target, and there is no soft shortcut: any proof must supply all four at once. The two LIVE attack near-misses are AHK (supply `PROP-carries-trace`: inject t into the Hodge-Riemann form, intrinsically, since Petrov non-semisimplicity forbids the eigenspace route) and FH (supply `PROP-global`: build the product + Gamma_S). Because global and carries-the-zeta-trace are one datum for the literal object, these two near-misses are two faces of the same construction, which is exactly why the diagnosis is collapse rather than dissolution. de Branges is a dead bracket (refuted, K2-blind); the Connes/K1 direction is a wall, not a target.

---

## 10. References

Classical / verifiable: Weil (1948); Deninger, *Some analogies...* (ICM 1998), *Dynamical systems
for arithmetic schemes* ([arXiv:1807.06400](https://arxiv.org/abs/1807.06400), 2018); Connes,
*Trace formula in NCG and the zeros of zeta* (Selecta 1999); Connes-Consani, *Geometry of the
arithmetic site* ([arXiv:1502.05580](https://arxiv.org/abs/1502.05580), 2014), *Weil positivity and
the archimedean place* (Sonin space, [arXiv:2006.13771](https://arxiv.org/abs/2006.13771), 2021),
*On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$* ([arXiv:2602.15941](https://arxiv.org/abs/2602.15941),
2026); Bhatt-Lurie, *Absolute prismatic cohomology* ([arXiv:2201.06120](https://arxiv.org/abs/2201.06120));
Bhatt-Scholze, *Prisms and prismatic cohomology* (Annals 2022); Bhatt-Morrow-Scholze, *THH and
integral p-adic Hodge theory* (Publ. IHES 2019); Hesselholt, *THH and the Hasse-Weil zeta function*
(2018); Petrov, *Non-decomposability of the de Rham complex and non-semisimplicity of the Sen
operator* ([arXiv:2302.11389](https://arxiv.org/abs/2302.11389), Annals); Kucharczyk-Scholze,
*Topological realisations of absolute Galois groups* ([arXiv:1609.04717](https://arxiv.org/abs/1609.04717));
Arakelov (1974); Faltings, *Calculus on arithmetic surfaces* (Ann. Math. 1984); Hriljac (1985);
Gillet-Soule, *An arithmetic Riemann-Roch theorem* (Invent. Math. 1992); Yuan-Zhang, *The arithmetic
Hodge index theorem for adelic line bundles* (Math. Ann. 2017); Deitmar (2005); Lorscheid, *The
geometry of blueprints* (Adv. Math. 2012); Borger, *$\Lambda$-rings and the field with one element*
([arXiv:0906.3146](https://arxiv.org/abs/0906.3146)); Soule (2004); Kurokawa (absolute zeta);
Adiprasito-Huh-Katz, *Hodge theory for combinatorial geometries* (Ann. Math. 2018); Conrey-Li, *A
note on some positivity conditions...* ([arXiv:math/9812166](https://arxiv.org/abs/math/9812166));
Morishita ([arXiv:2508.15971](https://arxiv.org/abs/2508.15971), 2025); Moriwaki, *Arithmetic Hodge
index theorem* (alg-geom/9403011; *Toward a Dirichlet unit theorem on arithmetic varieties*,
[arXiv:1010.1599](https://arxiv.org/abs/1010.1599)); Cantat-Gao-Habegger-Xie, *The geometric Bogomolov
conjecture* (Duke Math. J. 170(2), 2021); Bost, *Theta invariants of euclidean lattices and
infinite-dimensional Hermitian vector bundles over arithmetic curves* (Prog. Math. 334, 2020;
[arXiv:1512.08946](https://arxiv.org/abs/1512.08946)); Gurney, *Prismatization over
$\mathbf{Z}$* ([arXiv:2301.12392](https://arxiv.org/abs/2301.12392)); Drinfeld, *Prismatization*
([arXiv:2005.04746](https://arxiv.org/abs/2005.04746)); Bhatt-Lurie, *Absolute prismatic cohomology*
([arXiv:2201.06120](https://arxiv.org/abs/2201.06120)).

Project internal: [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md)
(the M1-M5 ladder, RH = arithmetic Hodge standard conjecture); [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)
(#30); [`experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md) #25/#26/#40/#41/#42/#43/#44;
the reading notes in [`reading_notes/`](reading_notes/); the 2A candidate scorecards and
`f1_arakelov_survey` in [`experiments/arithmetic_geometric/`](../../experiments/arithmetic_geometric/).

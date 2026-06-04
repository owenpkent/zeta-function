# Foundational-object adversarial brief: the dimension-or-trace dichotomy

> An ADVERSARIAL stress-test of the program's spine, written 2026-06-04. The spine is:
> **RH = arithmetic Rosati positivity = the arithmetic Hodge standard conjecture**, requiring a
> polarization (a signed intersection pairing) on a $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$-type
> surface ([`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md),
> [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md)).
>
> **The question this brief attacks.** Does the spine target a *real geometric object*, or is it an
> *unfalsifiable description* of RH in cohomological clothing? If no such object exists, RH would
> hold for some non-Hodge-index reason and the spine is the wrong bet. This is the honest risk, and
> it deserves a genuine adversary, not a cheerleader.
>
> **Posture.** This is a SURVEYOR brief: it maps and scores, it does not decide. Every load-bearing
> external fact was verified by web search against the arXiv original (see §7); items that could not
> be verified are flagged. One repo discrepancy was found and is logged in §6.

## 0. The verdict up front (so downstream agents can route)

The spine **survives** this stress-test, but only to its own honest thesis, not beyond it:

> **The foundational object EXISTS but its polarization is OPEN.**

This is not a refutation: "the object exists, the polarization is open" is *literally the spine's own
claim* (08A M4 is the polarization; M1-M3 are the object). The adversary cannot upgrade this to
"the surface provably cannot exist," because Deninger's foliated dynamical system is **constructed**
(arXiv:1807.06400, verified §7a), with the closed-orbit length spectrum $\{\log p\}$ = the trace $t$
intact. So the strong-negative ("no object") is **off the table**.

What the adversary **can** establish, and what this brief is really for, is a sharper and more
dangerous claim than "no object":

> **The real risk is the transfer, not the existence.** The polarization is *proven over* $\mathbb{F}_q$
> (the Weil/Rosati positivity, finite buffer $O(\sqrt q)$). The bet is that it transfers to
> $\mathbb{Z}$. The repo's own experiments show **the buffer collapses on transfer**: over $\mathbb{Z}$
> the off-line margin is the doubly-exponential $e^{-4\pi x}$ marginal wall (the stealth window,
> #18/#19/#27/#34/#38). The spine is risky precisely at the $\mathbb{F}_q \to \mathbb{Z}$ step, and
> the risk is quantitative (the buffer), not existential (the object).

The rest of this brief earns that verdict.

## 1. The dichotomy, stated as a forced choice

The program's own experiments force a **dimension-or-trace dichotomy** on every candidate foundational
object for $\mathrm{Spec}(\mathbb{Z})$. To prove RH the Weil way you need *one* object carrying *all
three* of: a Krull-dimension-2-or-3 self-product (the surface), the Frobenius/scaling trace $t$ (the
$\{\log p\}$ / von Mangoldt / point-count spectrum), and a polarization (the signed pairing). The
finding, replicated across five frameworks, is that **the existing constructions buy the dimension by
losing the trace, or restore the trace by losing the global object.** Concretely, three horns:

- **Horn (i), characteristic 1: you get the 2-dim object but LOSE $t$.** The Connes-Consani square
  $\widehat{\mathbb{N}^{\times 2}}$ is a genuine 2-dimensional product object (structure sheaf =
  Newton polygons, verified §7c). Its natural mixed-volume / Minkowski form is **Lorentzian for free**
  by Alexandrov-Fenchel: a Hodge-index $(1,k)$ signature with no arithmetic input. But it is the
  **characteristic-1 shadow**: idempotent operations, no subtraction, no place for the Frobenius
  trace $t$. The form reads the identical signature for $t=2$ and $t=100$ (RH-violating). It is
  arithmetic-blind, hence RH-agnostic. (Repo: [`e2cc_tropical_shadow.md`](../../experiments/arithmetic_geometric/e2cc_tropical_shadow.md),
  LEARNINGS #40.)
- **Horn (ii), the q-lift: restore $t$ and you cannot reach $\mathrm{Re}(s)<1$.** Un-idempotent-ize
  the characteristic-1 operations (soft-max, finite $\beta$) and a signed pairing becomes formally
  possible; per place the lift *is* the finite-$q$ function-field Hodge index (carries $t$). But the
  **global assembly** is the gap: the zeros live in the analytic continuation $\mathrm{Re}(s)<1$,
  where the local Euler/orbit data cannot reach ($\prod_p(1-p^{-s})^{-1}$ converges only for
  $\mathrm{Re}(s)>1$; on the critical line the partial products do not converge). Realizing the
  continuation as a signed pairing IS the missing Weil cohomology. (Repo:
  [`e2cc3_q_lift_attempt.md`](../../experiments/arithmetic_geometric/e2cc3_q_lift_attempt.md),
  LEARNINGS #42.)
- **Horn (iii), the place-spread diverges: no finite-type single-scale surface.** On $C \times C$
  the Frobenius is a $(1,q)$ correspondence with *one* scale $q$. Over $\mathrm{Spec}(\mathbb{Z})$ the
  fibre over $p$ is $\mathrm{Spec}(\mathbb{F}_p)$ of cardinality $p$, so $\Gamma_S$ has a
  *place-dependent* bidegree $(1,p)$: no single $q$. The required-scale spread $\max(p)/\min(p)$ over
  the first 40 primes is already $86.5$ and **diverges**. Consequence: no finite-type, single-scale
  scheme can carry $\Gamma_S$; the object must be infinite-genus, and the $\mathbb{Z}$-action must
  become an $\mathbb{R}$-flow. (Repo: [`e2q_frobenius_bidegree.md`](../../experiments/arithmetic_geometric/e2q_frobenius_bidegree.md),
  LEARNINGS #25.)

The dichotomy is the conjunction of the three horns: **characteristic-1 gives dimension-without-trace
(i); the $q$-lift gives local-trace-without-global-reach (ii); and the divergent place-spread (iii)
forbids the finite-type single-scale surface that would let you have both at once cheaply.** This is
not a wall: it is a precise specification of the object that does the job (infinite-dimensional /
$\mathbb{R}$-flow, trace $\{\log p\}$ intact, a signed pairing realizing the continuation). And such an
object has been **constructed** (Deninger, §2). So the dichotomy routes to "polarization open," not
"object impossible."

## 2. The survey: five candidate objects, scored on dimension and trace

For each framework the adversarial questions are exactly two: **(D) does it deliver the
Krull-dimension-2-or-3 self-product object?** and **(T) does it keep the Frobenius/scaling trace $t$
(the $\{\log p\}$ / von Mangoldt / point-count spectrum), or only a $t$-blind shadow?** A third column
records whether the **polarization** (signature) is present (it never is over $\mathbb{Z}$; that is the
spine's thesis).

Legend: ✓ present/constructed, ◑ partial or only-in-a-restricted-sense, ✗ absent.

| Object | (D) dim-2-or-3 product? | (T) trace $t$ intact? | Polarization | Verified |
|---|:--:|:--:|:--:|:--:|
| **Deninger** foliated dynamical system ($W_{rat}(X)$, $\mathbb{R}$-flow) | ✓ (constructed; see §2 caveat on dim) | ✓ closed-orbit lengths $= \{\log p\}$ | ✗ | §7a |
| **Borger** big-Witt $W(\mathbb{Z})$ / $\Lambda$-rings | ◑ ($\mathrm{Spec}\,W(\mathbb{Z})$ is the substrate; no constructed self-product cohomology) | ◑ (Frobenius $\psi_p$ built in, but bare $\psi_p$ has no zeta-zero spectrum) | ✗ | repo §7e |
| **Lorscheid** blueprints | ◑ (2-dim blueprint self-product exists; no intersection theory) | ◑ ($\mathbb{F}_1$-degrees, but the trace is not realized) | ✗ | repo |
| **Connes-Consani** square $\widehat{\mathbb{N}^{\times 2}}$ | ✓ (2-dim topos, Newton-polygon sheaf) | ✗ char-1 shadow loses $t$ (Horn i) | ✗ (Lorentzian-but-blind) | §7c |
| **Drinfeld / Bhatt-Lurie / Gurney** prismatization (WCart) | ◑ (substrate global over $\mathbb{Z}$; no constructed self-product surface) | ✓ Frobenius $F$ $\to$ $\{\log p\}$; Sen $\Theta$ $\to$ archimedean divisor | ✗ (Sen not semisimple, Petrov) | §7b |

Reading of the table. Two frameworks deliver the object *and* keep the trace (Deninger fully; the
prismatic substrate keeps both operators, but has no constructed self-product *surface*, only a
substrate). The Connes-Consani square delivers the cleanest 2-dim *product* object but loses $t$ to
characteristic 1. Borger and Lorscheid deliver the right *kind* of substrate (Frobenius built in)
but no constructed self-product cohomology with an intersection theory. **No framework delivers all
of (D), (T), and the polarization**, and the polarization being the one universal absence is exactly
the spine's claim, not a refutation of it.

### 2a. Deninger: the object that defeats the strong-negative

This is the decisive entry, because it forecloses "the surface provably cannot exist."

- **Constructed, not conjectured.** Deninger, *Dynamical systems for arithmetic schemes*
  (arXiv:1807.06400, last revised Feb 2024), constructs (via sheafified rational Witt vectors
  $W_{rat}(X)$) for every normal scheme $X$ of finite type over $\mathrm{Spec}(\mathbb{Z})$, an
  $\mathbb{R}$-dynamical system whose periodic orbits relate to the closed points of $X$. The closed
  orbits correspond to maximal ideals; in the complete-arithmetic-curve picture they are knots in a
  3-manifold corresponding to primes (verified §7a).
- **Trace $t$ intact.** The closed-orbit length spectrum is $\{\log p\}$ (the place weights of #25/2Q,
  the von Mangoldt diagonal of #26/2R). The regularized-determinant formula
  $\zeta = \det_\infty(s - \Theta \mid \text{leafwise cohomology})$ that Deninger conjectured is now
  **proven** for 3-dimensional Riemannian foliated dynamical systems (Alvarez Lopez-Kim-Morishita,
  arXiv:2410.20758, Oct 2024, "the formula conjectured by Deninger," verified §7d). So the trace is
  not a hope; it is a theorem in the model setting.
- **Dimension caveat (honest, flagged).** There are *two* dimensions in play and they must not be
  conflated. The $W_{rat}(X)$ construction of 1807.06400 produces **infinite-dimensional**
  $\mathbb{R}$-dynamical systems (verified quote: "we construct infinite dimensional
  $\mathbb{R}$-dynamical systems"). The **3-dimensional** object is the *target analogy* (a complete
  arithmetic curve over $\mathrm{Spec}(\mathcal{O}_k)$ as the analogue of a 3-manifold with a
  codimension-1 foliation and transverse flow), and it is in that 3-dim Riemannian foliated setting
  that the determinant/Lefschetz formula is proven (2410.20758). So the precise, defensible statement
  is: **the object is constructed and the trace is realized; the "dimension 3" is the foliated-space
  model where the trace formula is a theorem, while the $W_{rat}$ construction over a general
  arithmetic scheme is infinite-dimensional.** The brief's task framing ("a dimension-3 dynamical
  system whose closed-orbit length spectrum is $\{\log p\}$") is correct *for the foliated-space model*
  carrying the proven trace formula; it would be an overclaim to say the general $W_{rat}$ system is
  finite-dimensional.
- **Polarization open.** None of 1807.06400 / 2410.20758 / Morishita 2508.15971 proves a cohomological
  Hodge-index / positivity / RH statement. The abstracts make no mention of positivity or polarization
  (verified §7a, §7d). This is the universal gap, and it is exactly where the spine says it is.

**Conclusion of 2a:** the strong-negative is refuted. A foundational object with the trace $t$ intact
exists. The spine's bet (M1-M3 the object, M4 the polarization) is therefore betting on a *real*
object, not an imaginary one.

### 2b. Prismatization (WCart): both operators, no self-product surface, a new obstruction

- **Substrate, not surface.** Bhatt-Lurie's absolute prismatic cohomology recasts prismatic crystals
  as quasicoherent sheaves on the Cartier-Witt stack WCart (arXiv:2201.06120, verified §7b). The
  substrate carries **two** operators: the Frobenius $F$ (whose spectrum feeds the finite Euler
  factors / $\{\log p\}$, #26/#41) and the Sen operator $\Theta$ (Hodge-Tate weights $\{-n\}$, feeding
  the archimedean / trivial-zero divisor via Lerch, #44/2PR.1). So prismatic cohomology supplies both
  trace-halves of completed zeta as regularized determinants. The trace $t$ is **intact** on the $F$
  side.
- **Global-over-$\mathbb{Z}$ status, VERIFIED, with an attribution correction.** Drinfeld
  (arXiv:2005.04746, "Prismatization") and Bhatt-Lurie (2201.06120) are **$p$-adic / per-prime**
  (verified §7b: Drinfeld "define and study the three versions of the prismatization of the formal
  spectrum of the ring of $p$-adic integers"). The genuinely **global-over-$\mathrm{Spec}(\mathbb{Z})$**
  extension is **Gurney, *Prismatization over $\mathbf{Z}$* (arXiv:2301.12392)**, which extends the
  prismatization functor "to all schemes over $\mathrm{Spec}(\mathbf{Z})$," with algebraicity,
  flatness for syntomic morphisms, perfectness of cohomology, recovering the filtered de Rham stack
  over $\mathbb{Q}$ (verified §7b). **This corrects a repo attribution: the landscape doc credits
  2301.12392 to Drinfeld; it is Gurney (see §6 discrepancy log).** Net: the realization substrate *has*
  gone global over $\mathbb{Z}$, so "the substrate does not exist globally" is also off the table.
- **No constructed self-product surface, and a new polarization obstruction.** WCart is a substrate,
  not a $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ self-product with an intersection
  theory. Worse for the naive route: Petrov proved the Sen operator is **not semisimple** in general
  (arXiv:2302.11389, Annals), so an eigenspace-by-eigenspace Hodge-Riemann polarization is blocked; a
  polarization here must be intrinsic. Trace intact, polarization open *and* the obvious construction
  obstructed.

### 2c. Borger and Lorscheid: right substrate, no constructed self-product cohomology

- **Borger big-Witt $W(\mathbb{Z})$ / $\Lambda$-rings.** $\mathrm{Spec}\,W(\mathbb{Z})$ is Borger's
  $\mathbb{F}_1$-descent substrate, and the Adams/Frobenius operators $\psi_p$ are *built in* (the
  $\Lambda$-ring structure is exactly the $\{\psi_p\}$ datum). So the **trace direction is native**:
  this is the framework where the Frobenius is least artificial. But the repo's own probe found that
  **bare $\psi_p$ on concrete $\Lambda$-rings has no zeta-zero-like spectrum** (the Adams-spectrum
  result, memory `arch_2e_adams_spectrum_result.md`): the operator is present, the *cohomology that
  would carry the zeros as eigenvalues* is not constructed. No 2-dimensional $\Lambda$-cohomology of
  $\mathrm{Spec}\,W(\mathbb{Z})$ with an intersection form exists yet. Dimension ◑, trace ◑ (operator
  present, spectrum not realized), polarization ✗.
- **Lorscheid blueprints.** Blueprints do give a 2-dimensional self-product object (a blueprint
  surface), which is more than monoid schemes (Deitmar) achieve, since the self-product does not
  collapse. But there is **no intersection theory and no cycle class** on it: the dimension is there,
  the trace is not realized as a point-count, the polarization is absent. Dimension ◑ (self-product
  exists, no intersection theory), trace ◑, polarization ✗.

These two are the "right kind of substrate, construction not done" entries: they keep the Frobenius
(so they are not characteristic-1-blind like the bare C-C square), but they have not produced the
constructed self-product cohomology with a trace realization, let alone a polarization.

## 3. The trace is the hinge, and D-H proves it

The Davenport-Heilbronn discipline cuts the dichotomy cleanly and explains *why* the trace is the
load-bearing column. D-H has a functional equation and a $\Gamma$-factor but **no Euler product**,
hence:

> no Euler product $\Rightarrow$ no local $(1,p)$ bidegrees $\Rightarrow$ no $\Gamma_S$ $\Rightarrow$
> no surface. (2Q/#25.)

The trace $t$ (the $\{\log p\}$ closed-orbit spectrum, the von Mangoldt diagonal, the $(1,p)$ bidegree)
is **exactly the structure D-H lacks**. Every $t$-blind object in the survey (the C-C mixed-volume
shadow, the AHK Kahler package, the archimedean / Sen / de Branges half) is *automatically*
RH-agnostic, because D-H shares it: D-H has the same $\Gamma$-factor, the same functional equation,
the same archimedean continuation. So the dichotomy's Horn (i), "you get the object but lose $t$", is
*precisely the D-H failure mode*: a $t$-blind object fires identically for D-H, which has off-line
zeros. This is the structural reason the spine insists the polarization must be carried by the
Frobenius / Euler direction, the one column D-H cannot build. **The trace is not a nice-to-have; it is
the only K2-discriminating column, and it is the column the characteristic-1 object drops.**

## 4. Where the bet is actually risky: the $\mathbb{F}_q \to \mathbb{Z}$ buffer collapse

Having foreclosed the strong-negative, the adversary's real product is locating the risk precisely.
It is **not** "the object does not exist" (it does, §2a) and **not** "the substrate is not global" (it
is, §2b). The risk is the **transfer of the polarization from $\mathbb{F}_q$ to $\mathbb{Z}$**, and the
repo's experiments show the *buffer* (the slack in the positivity inequality) collapses on transfer.

- **Over $\mathbb{F}_q$ the buffer is finite, $O(\sqrt q)$.** RH-for-$C$ is the algebraic inequality
  $|t| < 2g\sqrt q$ in two *integers* (2G/2Q). The Rosati positivity has a genuine open margin: the
  off-line configurations are bounded away from the on-line ones by an amount of order $\sqrt q$. The
  positivity is proven (Weil) and the slack is real. (Repo: 2G, 2T, M1.)
- **Over $\mathbb{Z}$ the buffer collapses to the doubly-exponential marginal wall.** The program's
  marginal-positivity thesis (memory `marginal_positivity_thesis.md`) is the repeated finding, in five
  independent bases, that over $\mathbb{Z}$ the off-line obstruction sits at the **stealth-window
  floor**: the D-H off-line zero at $\gamma \approx 85.7$ contributes an obstruction
  $\sim 2.6\%$ of the raw spectrum that drops *below the reconstruction-residual floor* of every finite
  truncation (M2.6/#34); the heat-kernel detector suppresses the off-line zero to
  $\exp(-(\pi/4)\,d\gamma)$, i.e. $|\Xi(85.7)| \approx 1.5 \times 10^{-29}$ (#38); the de Branges
  cross-term double-suppresses it to $|Q| \sim 10^{-56}$ (#43). In the archimedean kernel the wall is
  the $e^{-4\pi x}$-type doubly-exponential decay: the margin that was $O(\sqrt q)$ over $\mathbb{F}_q$
  is, over $\mathbb{Z}$, **a vanishing sliver no soft (truncation / determinant / convex) method can
  see**. (Repo: M2.6/#34, #18/#19/#27/#38/#43.)
- **Why this is the precise risk.** The function-field polarization works because the buffer is a fixed
  positive number ($O(\sqrt q)$). The bet is that the *same* polarization survives the $q \to 1$ /
  $\mathbb{F}_q \to \mathbb{Z}$ limit. The experiments say the limit is **singular for the buffer**: as
  you assemble the place-blocks (Horn iii, the divergent place-spread), the protective margin shrinks
  to the marginal wall. So the polarization could in principle still hold over $\mathbb{Z}$ (the spine
  is not refuted), but it must be an **exact** positivity with *zero slack to spare*, which is exactly
  why M3/M4 must be analytic (engaging the precise off-line structure), not a finer numerical
  truncation (08A "CONSEQUENCE: M3 must be ANALYTIC"). **The spine's vulnerability is here: it bets the
  $O(\sqrt q)$ buffer survives a limit in which every measurable proxy for it goes to the
  doubly-exponential floor.**

This is a falsifiable, located risk, and it is *more useful* to the program than the strong-negative
would have been: it says the proof cannot be soft, must be exact, and lives in the
$\mathbb{F}_q \to \mathbb{Z}$ transfer of the polarization, not in the construction of the object.

## 5. The unfalsifiability question, answered

Is the spine an *unfalsifiable description* of RH? The honest answer is: **it is falsifiable in
principle, and it has already survived two of its own falsification triggers, but it is not yet
falsifiable in the strong sense the adversary would prefer.**

- **It is not vacuous.** "RH = arithmetic Rosati positivity" makes contentful, *tested* predictions:
  (a) a $t$-blind object must be RH-agnostic (confirmed: C-C shadow #40, AHK #48, all soft detectors);
  (b) the discriminating column must be the Frobenius/Euler direction (confirmed: prime-block ablation
  #46, zeroing the prime block makes zeta fail exactly as D-H does); (c) the convex-Hodge signature
  has the *wrong polarity* and can never flag an off-line zero (confirmed: #48, unconditionally
  $(1,n-1)$). These are real, refutable claims and they held.
- **It has a standing falsification trigger.** 08A and the proof-program spec set an explicit trigger:
  *Phase 4 fails after 5 calendar years of parallel Hodge-index attempts* (PHASE_STATE.md
  falsifiability triggers). And de Branges is a *near-miss falsification of a neighboring spine*: a
  signed pairing that DOES see the zeros but whose positivity is strictly-stronger-than-RH and FAILS
  for zeta at the 34th zero (Conrey-Li, #43). That is the adversary's proof that "build a signed
  pairing that sees the zeros" can genuinely fail, so the spine's specific pairing is not guaranteed
  to exist, and the program is not assuming its conclusion.
- **The residual unfalsifiability.** What the adversary cannot yet do is exhibit a *finite* test that
  would refute the spine. Because the object exists (so "no object" is closed) and the polarization is
  the open arithmetic standard conjecture (so "no polarization" is not provable without doing the
  mathematics), the spine currently sits in the same epistemic box as the standard conjectures
  themselves: contentful, K1/K2-disciplined, with confirmed predictions, but with its central claim
  (the polarization) neither proven nor refutable by a cheap experiment. **That is a feature of the
  target (the arithmetic Hodge standard conjecture is genuinely open), not a defect of the framing.**
  The spine is the *correct professional home* for RH (Grothendieck's standard-conjecture circle),
  and the price of being in the right home is that the open step is a hard open conjecture.

So: not unfalsifiable in the bad sense (it makes and passes refutable predictions, and a neighboring
version already failed visibly via de Branges), but not cheaply falsifiable either (the open step is a
standard conjecture). The spine is the right bet *conditional on RH being a Hodge-index phenomenon at
all*, and the one scenario this brief cannot rule out is precisely the task's named honest risk:
**RH might hold for a non-Hodge-index reason, in which case the object exists but is the wrong object,
and the polarization the spine wants is not the mechanism.** Nothing in the repo refutes that scenario;
it is the irreducible bet.

## 6. Discrepancy log

| # | Where | Repo says | Verified fact | Action |
|---|---|---|---|---|
| 1 | [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) §7 and §10 references | attributes arXiv:2301.12392 ("Prismatization over Z") and "Drinfeld prismatization" as the global-over-$\mathbb{Z}$ machinery | arXiv:2301.12392 is by **Lance Gurney**, not Drinfeld. Drinfeld's prismatization is arXiv:2005.04746 and is **$p$-adic/local only**; Bhatt-Lurie 2201.06120 is also $p$-adic. The genuinely global-over-$\mathbb{Z}$ extension is **Gurney 2301.12392**. (Verified §7b.) | Flag for SYNTHESIZER: correct the attribution in the landscape doc. The *substance* (a global-over-$\mathbb{Z}$ prismatization exists) is correct; only the author credit is wrong. |
| 2 | task framing + landscape doc | "Deninger's foliated space, a dimension-3 dynamical system" | The $W_{rat}(X)$ construction (1807.06400) is **infinite-dimensional**; the **3-dimensional** object is the foliated-space *model* (complete arithmetic curve $\sim$ 3-manifold) where the determinant/Lefschetz formula is proven (2410.20758). Both are correct statements about *different* objects; conflating them would overclaim. (Verified §7a, §7d.) | Not an error, but a precision the brief makes explicit (§2a dimension caveat). The trace $\{\log p\}$ is intact in the foliated model; that is the load-bearing fact, and it holds. |

No mathematical discrepancy was found with the spine's central claims; the two items are an
attribution fix and a dimension precision, neither of which changes the verdict.

## 7. Verification record (external facts checked against arXiv originals)

Every load-bearing external fact below was checked by web search / fetch against the arXiv abstract or
page on 2026-06-04. Items the search could not confirm are marked UNVERIFIED.

- **(a) Deninger foliated space (arXiv:1807.06400).** VERIFIED. Abstract: "For normal schemes $X$ of
  finite type over $\mathrm{spec}\,\mathbb{Z}$, using $W_{rat}(X)(\mathbb{C})$ we construct infinite
  dimensional $\mathbb{R}$-dynamical systems whose periodic orbits are related to the closed points of
  $X$." Constructed (not conjectured); infinite-dimensional in general; 3-dim is the foliated-space
  analogy; abstract makes no positivity/polarization claim. Last revised Feb 2024.
- **(b) Prismatization global over $\mathbb{Z}$.** VERIFIED with attribution correction.
  arXiv:2005.04746 (Drinfeld, "Prismatization") = $p$-adic/local ("the prismatization of the formal
  spectrum of the ring of $p$-adic integers"). arXiv:2201.06120 (Bhatt-Lurie, "Absolute prismatic
  cohomology") = $p$-adic formal schemes, WCart = Cartier-Witt stack. arXiv:2301.12392 (**Gurney**,
  "Prismatization over $\mathbf{Z}$") = the global extension "to all schemes over
  $\mathrm{Spec}(\mathbf{Z})$," with algebraicity / flatness / perfectness, recovering filtered de Rham
  over $\mathbb{Q}$. **The repo's Drinfeld attribution of 2301.12392 is incorrect (it is Gurney).**
- **(c) Connes-Consani square (arXiv:1502.05580).** VERIFIED. Structure sheaf of the arithmetic site is
  $\mathbb{Z}_{\max} = (\mathbb{Z} \cup \{-\infty\}, \max, +)$, characteristic 1, $\mathbb{N}^\times$
  acting by Frobenius endomorphisms. The site admits a one-parameter semigroup of Frobenius
  correspondences as sub-varieties of the **square**, a semi-ringed topos whose structure sheaf
  involves **Newton polygons**; composition $\Psi(\lambda) \circ \Psi(\lambda') = \Psi(\lambda\lambda')$.
  This is the 2-dim product object of Horn (i).
- **(d) Deninger determinant/Lefschetz formula proven (arXiv:2410.20758).** VERIFIED. Alvarez
  Lopez-Kim-Morishita, Oct 2024: "We prove a regularized determinant formula for the zeta functions of
  certain 3-dimensional Riemannian foliated dynamical systems," explicitly "the formula conjectured by
  Deninger," via the distributional dynamical Lefschetz trace formula. **No** RH/positivity/polarization
  claim in the abstract. (Note: the 1712.04181 fiber-bundle special case and Morishita's
  arXiv:2508.15971 Deninger$\leftrightarrow$Connes-Consani bridge corroborate the trace-side picture;
  the bridge transfers no polarization.)
- **(e) Borger / Lorscheid.** PARTIALLY VERIFIED from repo (Adams-spectrum result memory; 2A
  scorecards). The external claim "bare $\psi_p$ on concrete $\Lambda$-rings has no zeta-zero spectrum"
  is the repo's own experimental result, not an external citation; the $\mathbb{F}_1$-descent /
  big-Witt framing is standard (Borger arXiv:0906.3146). UNVERIFIED externally beyond the repo: that
  no $\Lambda$-cohomology of $\mathrm{Spec}\,W(\mathbb{Z})$ with an intersection form exists (this is a
  literature-absence claim; treat as "not found," not "proven absent").
- **(f) Petrov Sen-operator non-semisimplicity (arXiv:2302.11389, Annals).** Cited from the repo
  landscape doc, which states it was verified against the original in the 2026-06-02 session; this
  brief did not re-verify it. Treat as repo-verified, not independently re-checked here.

## 8. What this enables / what remains open

**What this brief enables (for downstream agents):**

- **For BUILDER.** The object to build is now specified by the dichotomy: it must (D) be the
  infinite-dimensional / $\mathbb{R}$-flow object (the finite-type single-scale surface is *forbidden*
  by Horn iii), (T) carry the $\{\log p\}$ trace (Deninger's foliated model does; build *on* it, or on
  the Gurney global prismatization substrate, not on the characteristic-1 C-C square which drops $t$),
  and supply (the open step) a signed pairing realizing the continuation $\mathrm{Re}(s)<1$. Do **not**
  invest in the bare Connes-Consani mixed-volume form (arithmetic-blind, Horn i) or the convex-Hodge /
  AHK signature (wrong polarity, #48) as the polarization; they are confirmed dead for the signature.
  The live substrate candidates carrying the trace are **Deninger's foliated space** (proven trace
  formula, 2410.20758) and the **Gurney global prismatization** (both operators $F$, $\Theta$ intact),
  with the Petrov obstruction (no eigenspace polarization) noted.
- **For ADVERSARY.** The strong-negative ("no object") is closed. Do not spend cycles trying to prove
  the surface cannot exist; Deninger built it. The productive attack is on the **buffer collapse** (§4):
  find a sharp statement of *why* the $O(\sqrt q)$ margin must (or need not) survive the
  $\mathbb{F}_q \to \mathbb{Z}$ limit, or a D-H-style object that has the trace $\{\log p\}$ on a
  *finite* set of primes yet off-line zeros (a partial-Euler counterexample) to probe whether the
  trace column alone suffices. The de Branges failure (#43) is the template: a pairing that sees the
  zeros but is too strong is a real falsification mode.
- **For SYNTHESIZER.** Two concrete doc actions: (1) correct the arXiv:2301.12392 attribution
  (Gurney, not Drinfeld) in [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md); (2)
  add the dimension precision (infinite-dim $W_{rat}$ vs 3-dim foliated model) to the Deninger row of
  that scorecard.

**What remains open (unchanged by this brief, but now sharply located):**

- The **polarization** on the global object: the arithmetic Hodge standard conjecture (08A M4). This is
  the single universal gap; every framework reaches it and stops. It is open as a hard conjecture, not
  as a missing construction.
- The **$\mathbb{F}_q \to \mathbb{Z}$ transfer of the buffer** (§4): whether the $O(\sqrt q)$ Rosati
  margin survives to the marginal $e^{-4\pi x}$ wall over $\mathbb{Z}$. This is the spine's precise
  point of risk.
- The **irreducible bet** (§5): that RH is a Hodge-index phenomenon at all. If it is not (if RH holds
  for a non-Hodge-index reason), the object exists but is the wrong object, and the spine, while not
  refuted by anything here, would be the wrong target. This brief cannot close that scenario; naming it
  precisely is the most an adversary can honestly do.

**Bottom line.** The spine targets a *real* object (constructed, trace intact), so it is not an
unfalsifiable fiction; its open step is the polarization, which is the spine's own thesis, so the
spine is *not refuted*; and its genuine risk is the quantitative $\mathbb{F}_q \to \mathbb{Z}$ buffer
collapse plus the irreducible bet that RH is Hodge-index in nature. Survivable conclusion confirmed:
**the object exists, the polarization is open.**

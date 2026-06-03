# RH solved by accident: the accident-vector landscape

> A synthesis dossier written 2026-06-03, integrating an adversarially-verified
> sweep of 28 candidate "accident channels" by which RH for $\zeta$ could fall as a
> byproduct of a program built for another purpose. It answers a sharp question:
> **which currently-moving mathematics, none of it aiming at RH, could incidentally
> supply the one missing object (the polarization / signed pairing whose
> definiteness is RH)?** Short answer: a small handful are the right KIND of tool
> (they pass the Davenport-Heilbronn filter), none yet delivers, and a no-free-lunch
> theorem holds across all 28: in every case the program's own success yields only
> the **realization** of $\zeta$, and the residual step is itself RH-equivalent.
>
> Companion to [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md)
> (who realizes $\zeta$, where the polarization is missing) and
> [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the
> realization-vs-signature ledger, the marginal-positivity thesis). Distinguishes
> PROVEN from CONJECTURAL throughout. A channel ruled out is a coordinate that
> narrows the search.

## 1. The reframing: accident = byproduct that fills a target slot

Hard problems tend to fall as byproducts, not frontal assaults. Fermat fell to
modularity (built for Langlands), Poincare to Ricci flow (built as a geometric
heat equation), the Weil conjectures to etale cohomology (built for structural
reasons). In each case a foreign tool supplied the exact missing object: the
**signature / positivity** step, after the realization had already been built
elsewhere.

The Spec($\mathbb{Z}$) landscape is in precisely this configuration. Every framework
**realizes** $\zeta$ as a determinant or trace (the easy half). None carries the
**polarization** (the hard half), and supplying that polarization is not a shortcut
to RH: it **is** RH (the arithmetic Hodge standard conjecture, 08A M4). So an
"accident" here means a concrete event:

> A program built for functoriality, or p-adic Hodge theory, or Diophantine
> heights, or inverse spectral theory, incidentally produces a signed pairing whose
> negative-definiteness on a primitive subspace is logically equivalent to RH for
> $\zeta$, carried by the Frobenius/Euler direction, established without RH input.

The target slots (from the spec) are four:

- **Polarization slot** (Arch 2 / Direction 8 / 08A M4): a positive Rosati
  involution on the arithmetic Frobenius algebra $\mathcal{A}$, equivalently a
  negative-definite intersection form on primitive global $H^1$ of
  $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ carrying $\Gamma_S$.
- **Self-adjoint / spectral slot** (Hilbert-Polya, Arch 1): a self-adjoint operator
  $H$ with $\mathrm{spec}(H)=\{\gamma_n\}$, self-adjointness proven independently of
  zero locations. Dual to the polarization slot (positivity of the same quadratic
  form).
- **Archimedean-Frobenius unification slot**: one object fusing the
  archimedean/continuation data (RH-agnostic, shared with D-H) and the
  Frobenius/Euler data (RH-discriminating). Highest risk of silent K2-blindness.
- **Unforeseen exact identity / numerical stumble slot**: an exact identity (not a
  signature argument) that pins the zeros, surfacing first as a numerical
  coincidence. Strictest bar: must be proven exact AND RH-equivalent AND
  D-H-discriminating.

## 2. The filter that classifies tools: Davenport-Heilbronn (K2)

The D-H L-function has the same functional equation and $\Gamma$-factor as a
degree-2 L-function but **no Euler product**, and has known off-line zeros
($\rho \approx 0.8085 + 85.699\,i$). It cleaves the problem in two:

- The **archimedean / continuation half** ($\Gamma$-factor, Sonin space, Sen
  $\Theta$ divisor, de Branges kernel, the explicit-formula trace as a bare
  identity) is **shared by D-H** and is therefore **RH-agnostic**. Any positivity
  built only from this half either "proves" the false D-H analogue (so it is wrong)
  or is silently blind to the off-line obstruction.
- All K2 **discrimination lives on the Euler-product / Frobenius half** (orbit
  lengths $\{\log p\}$, the $(1,p)$ bidegree, the prismatic Frobenius $F$, THH,
  Satake parameters, excursion operators, Euler systems). This half is structurally
  unbuildable for D-H.

This is the early-warning classifier: **a tool is RH-relevant precisely when it
cannot be built for D-H.** Every illusory candidate below fails because its
mechanism is D-H-shared; every credible one passes because its discriminating
content rides the Frobenius half.

## 3. Scorecard

D-H verdict: **passes** = mechanism structurally unavailable to D-H
(RH-discriminating); **fails** = uses an object D-H also has (RH-agnostic);
**agnostic** = mechanism is a verifier/realization engine, not a sign.

| Vector | Built for | Accidental lemma (what would fill the slot) | Target slot | D-H | Tier |
|---|---|---|---|:--:|:--:|
| Beilinson-Bloch height (Gao / Chao Li) | Beilinson-Bloch conj. / BSD for higher cycles | Height positivity on $\Gamma_S$-as-higher-cycle on the self-product | Polarization | passes | **B** |
| Chen-Moriwaki / Yuan-Zhang adelic Hodge index | equidistribution, Bogomolov, Diophantine | proven adelic neg-definiteness applies to a Frobenius adelic cycle | Polarization (globality proven) | passes | **B** |
| Prismatization-over-$\mathbb{Z}$ F-gauge cup form | p-adic Hodge theory, geometrization | intrinsic neg-definite cup form on global prismatic $H^1$ | Polarization / unification | passes | **B** |
| Deninger foliated-Lefschetz (Alvarez-Lopez/Kim/Morishita) | foliated dynamics, leafwise cohomology | leafwise Hodge-index on the flow's primitive $H^1$ | Polarization / spectral | passes | **B** |
| Geometric Langlands -> arithmetic Hecke (Gaitsgory-Raskin; Fargues-Scholze) | the categorical GLC equivalence, functoriality | duality upgraded to definite hermitian form on tempered block | Polarization / spectral | passes | **B** |
| Euler-truncated zeta spectral triples (CCM) | spectral realization of zeros, metaplectic | limit operator essentially self-adjoint (primes inside $H$) | Spectral | passes | **C** |
| Connes-Consani infinite-genus Jacobian (2026) | genus paradox of $\mathrm{Spec}\,\mathbb{Z}$ | Riemann form / principal polarization on the Jacobian | Polarization | fails | **C** |
| Clausen-Scholze analytic stacks | foundations of analytic geometry | the self-product arena + an arithmetic intersection sign | Polarization / unification | fails | **C** |
| Weighted tropical Kahler package (Amini-Piquerez) | Hodge theory for tropical fans, log-concavity | HR signature that moves with $w_p=\log p$ and can fail | Polarization | agnostic | **C** |
| Arithmetic Newton-Okounkov bodies (Ballay/Wilms) | arithmetic ampleness, mixed volumes | Alexandrov-Fenchel neg-definiteness on $\Gamma_S$'s body | Polarization / unification | agnostic | **C** |
| Iwasawa MC / Euler-system char-ideal (Kato/Skinner-Urban) | Main Conjecture, BSD, special values | module-length non-negativity glued to complex zeros | Polarization | passes | **C** |
| All-order Turan / Laguerre-Polya (GORZ; Dimitrov-Lucas) | real-rootedness of arithmetic sequences | $\xi\in$ LP via uniform all-order Turan defects | Exact identity / spectral | fails | **C** |
| Beyond Endoscopy (Altug/Sarnak) | Langlands functoriality via trace formula | orbital-integral positivity excludes off-line excursion | Polarization / spectral | passes | **C** |
| Temperedness / Selberg eigenvalue (Kim-Sarnak) | $\lambda_1\ge 1/4$, Ramanujan-Petersson | temperedness $|\alpha_p|=1$ for the rep attached to $\zeta$ | Spectral | passes | **C** |
| Liouville/Mobius correlation collapse (Tao et al.) | Sarnak disjointness, Chowla | $\sqrt{\,}$-cancellation cascade in log Liouville $L^2$ | Spectral / exact identity | passes | **C** |
| Spectral form factor off-diagonal (Bogomolny-Keating) | universality of quantum chaos | $K(\tau)\ge 0$ from periodic-orbit (prime-pair) combinatorics | Spectral | passes | **D** |
| Riemann-Hilbert / DIK Euler-twisted symbol | Toeplitz/Hankel asymptotics in RMT | $I+K$ sign-definite from $\{\log p\}$ Fisher-Hartwig data | Polarization | agnostic | **D** |
| Makarov-Poltoratski canonical system | inverse spectral problem | positive Hamiltonian $H$ realizing the $\xi$-measure | Spectral | fails | **D** |
| $\xi$ as KP tau-function (Direction 13) | integrable hierarchies, Sato Grassmannian | second Riemann bilinear relation $\mathrm{Im}\,\Omega>0$ | Polarization / exact identity | fails | **D** |
| Free-probability operator-valued positivity | free entropy, RMT spectral distributions | Rosati form = B-valued Nevanlinna positivity | Polarization | fails | **D** |
| Arithmetic QUE (Lindenstrauss-Sarnak) | quantum unique ergodicity | entropy positivity transported to the scattering spectrum | Unification | fails | **D** |
| CUE moment arithmetic (divisor leakage $a_k$) | moments of $\zeta$, GMC universality | $a_k$ carries a Hankel signature pinning the line | Polarization / spectral | fails | **D** |
| Moment / CFKRS freezing transition | value distribution of $\zeta$, RMT model | moment sequence's measure supported on $\mathrm{Re}(s)=1/2$ | Spectral | fails | **D** |
| Lorentzian deformation of $\xi$ Jensen polys | Lorentzian polynomials, log-concavity | $\{\log p\}$-weighted Lorentzian gadget realizing $\xi$ | Exact identity / polarization | fails | **D** |
| de Bruijn-Newman backward heat ($\Lambda\le 0$) | dynamics of zeros under heat flow | log-gas Hessian positivity forcing $\Lambda\le 0$ | Spectral | fails | **D** |
| Guth-Maynard large-values cascade | primes in short intervals, density hyp. | $N(\sigma,T)=0$ for $\sigma>1/2$ | (analytic barrier) | fails | **D** |
| Formalization-driven equivalence (Lean/Mathlib) | verified analytic NT, autoformalization | dependency graph exposes a finite-data RH-equivalence | Exact identity | agnostic | **D** |
| Automated integer-relation discovery (PSLQ) | closed forms among constants | exact identity pinning an RH-equivalent quantity | Exact identity | fails | **D** |

## 4. Tiered analysis

### No A-live tier, and why that is honest

No candidate is currently both moving AND passing D-H AND delivering more than a
realization. That is not pessimism; it is the no-free-lunch theorem in measured
form. The A tier is reserved for a tool whose own success supplies the signature
for non-RH reasons, and the adversarial pass found none. The B tier is the live
frontier: right kind of tool, right slot, substrate moving, residual step is the
RH-equivalent polarization.

### B-credible (the right kind of tool, substrate moving)

- **Beilinson-Bloch height positivity (Gao / Chao Li).** The most honest version of
  the right idea. The height pairing is a **genuine signature** (negative-definite
  primitive, Neron-Tate-type), **global** (archimedean Green-current plus finite
  local indices), **arithmetically loaded** (local indices read point counts), and
  D-H-unbuildable. PROVEN: Gao's **generic** positivity for Gross-Schoen / Ceresa
  cycles (2024), in the $>1$-codimension product regime Faltings-Hriljac cannot
  reach. CONJECTURAL / missing: the self-product $\mathrm{Spec}(\mathbb{Z})\times
  \mathrm{Spec}(\mathbb{Z})$, $\Gamma_S$ as a homologically-trivial higher cycle on
  it, and **sharp** (not generic) positivity. Residual step is RH-equivalent.

- **Chen-Moriwaki / Yuan-Zhang adelic Hodge index.** The rare case where the SIGN
  is a **theorem** and **global over all places at once** (the adelic curve = all
  absolute values), cleanly meeting the globality criterion. PROVEN: negative-
  definiteness on the primitive part of an adelic-line-bundle group. Missing: a
  Frobenius correspondence $\Gamma_S$ as an adelic cycle on a true self-product,
  which is the arithmetic standard conjecture. A correct sign on the wrong (Frobenius-
  free) objects until the cycle is built.

- **Prismatization-over-$\mathbb{Z}$ F-gauge cup product (Drinfeld / Bhatt-Lurie).**
  D-H-discriminating ($F$ has no D-H analogue) and the realization apparatus is now
  fully **global over Spec($\mathbb{Z}$)** (Drinfeld prismatization accepted 2024;
  prismatization over $\mathbb{Z}$ 2025). PROVEN: prismatic Poincare duality (Tang,
  Compositio 2024), but **sign-blind**. Missing: an intrinsic negative-definite cup
  form on global prismatic $H^1$. OBSTRUCTION (PROVEN): the Sen operator is **not
  semisimple** (Petrov, Annals), killing the eigenspace route; the polarization must
  be intrinsic to the filtration.

- **Deninger foliated-Lefschetz (Alvarez-Lopez / Kim / Morishita).** Frobenius-
  loaded (orbit lengths $\{\log p\}$ ARE the Euler product) and concretely moving.
  PROVEN: the regularized-determinant Lefschetz formula for genuine 3-dim Riemannian
  foliated systems (2024); the Spec($\mathbb{Z}$) foliated space is constructed
  (rational Witt vectors); Morishita 2025 builds an $\mathbb{R}_+$-anti-equivariant
  bridge to Connes-Consani (a **duality** dictionary, no polarization transferred).
  Missing: a leafwise Hodge-index theorem on the singular arithmetic $X$. The trace
  is done; the SIGN is the M4 target.

- **Geometric Langlands -> arithmetic Hecke category.** Highest-activity item. PROVEN:
  the categorical GLC equivalence (2024) and Fargues-Scholze geometrization; excursion
  operators carry the Satake trace $t$, so it reaches the Frobenius half. But a
  **proven duality is not a polarization**: Serre/Verdier self-duality is sign-neutral.
  Missing: definiteness on the tempered block, which over Spec($\mathbb{Z}$) is
  weight-purity = $|\alpha|=\sqrt q$-analogue = RH. The arithmetic descent (an
  archimedean Fargues-Fontaine-type base) is not built.

### C-longshot (a real virtue, but a structural defect)

Each carries one genuine asset and one disqualifying defect.

- **Euler-truncated zeta spectral triples (CCM, 2511.22755).** Hottest spectral
  candidate; the 2025 Euler-product version is genuinely D-H-discriminating. Defect:
  finite-operator self-adjointness (Caratheodory-Fejer) does NOT transfer to the
  limit; the missing "limit is essentially self-adjoint" step is itself
  Hilbert-Polya.
- **Connes-Consani Jacobian (2026).** Fresh; a true Jacobian polarization would be
  neither too strong nor too local. Defect: the 2026 paper builds the Picard monoid
  (realization) and defers the polarization, which IS the missing object; the only
  proven C-C positivity (Sonin) is archimedean and D-H-shared.
- **Clausen-Scholze analytic stacks.** Could supply the missing ARENA (non-collapsing
  self-product, Kunneth, Poincare duality over all places). Defect: duality + Kunneth
  are the easy half, sign-free and D-H-available; the discriminating $\Gamma_S$
  content is not produced by the machinery.
- **Weighted tropical Kahler package (Amini-Piquerez).** Genuinely defeats AHK
  arithmetic-blindness: the HR signature now MOVES with weights. Defect: the proven
  package is **unconditionally definite**, so it can never fail when a zero leaves
  the line (wrong polarity for a detector); loading $\log p$ into a balancing
  condition that encodes multiplicativity is the standard conjecture.
- **Arithmetic Newton-Okounkov bodies.** A genuine globality upgrade over
  Faltings-Hriljac. Defect: the mixed-volume engine is arithmetic-blind; the
  discriminating input is the M4 polarization itself; regularizing $\Gamma_S^2$ is
  the open problem.
- **Iwasawa Main Conjecture / Euler systems.** Cleanly D-H-discriminating (the Euler
  system IS the Euler product). Defect: the non-negativity is a **p-adic** module
  length tied to $L_p$'s p-adic divisor, in the wrong completion; no theorem links
  p-adic to complex zeros, and the bridge is RH-equivalent.
- **All-order Turan / Laguerre-Polya (GORZ).** A genuine, tight, exactly-on-zeta
  RH-equivalence ($\xi\in$ LP $\Leftrightarrow$ RH), escaping the de Branges
  over-strength trap. Defect: built only from the Taylor coefficients of $\xi$
  (D-H-shared); $\xi_{DH}$ has the identical equivalence to its false RH, so an
  agnostic closure would prove a falsehood. Carries no $\{\log p\}$.
- **Beyond Endoscopy (Altug/Sarnak).** D-H-discriminating (no Satake data for D-H).
  Defect: orbital-integral positivity is positivity of a pole-detecting MEASURE, not
  a signature; the geometric=spectral identity makes it K1-circular.
- **Temperedness / Selberg eigenvalue (Kim-Sarnak).** The sharpest right-SHAPE object
  in the spectral slot ($|\alpha_p|=1$ is the analogue of $|\alpha_i|=\sqrt q$), with
  a K2-clean Rankin-Selberg sum-of-squares positivity. Defect: right shape on the
  WRONG axis: $\zeta$ is the trivial GL(1) rep where temperedness is automatic; RH is
  about zeros in the strip, not Satake unitarity. Dissolves at transport.
- **Liouville/Mobius correlation collapse (Tao et al.).** Cleanly D-H-discriminating
  (no D-H-Liouville exists). Defect: the toolkit removes MAIN TERMS (Level-3
  cancellation, compatible with a $\beta=0.51$ zero); the upgrade to pointwise
  $\sqrt{\,}$-cancellation is RH-equivalent.

### D-illusory (ruled out; each is a coordinate)

These are not failures so much as removed branches. The cluster is diagnostic:
nearly all fail for one of three reasons, and naming the reason narrows the search.

- **Trace-side / K1-circular** ($K(\tau)\ge 0$ form factor; the bare explicit-formula
  positivity): the positivity IS the Weil distribution restated, derivable from the
  zeros, not an independent polarization.
- **Archimedean / D-H-shared** (Makarov-Poltoratski; de Bruijn-Newman backward heat;
  Lorentzian Jensen; KP tau-function; PSLQ; arithmetic QUE on the scattering side):
  the carrier is the continuation half D-H also has, so it is RH-agnostic. de Branges
  is the canonical instance (too strong, false at the 34th zero).
- **Level-3 statistical / arithmetic-blind** (CUE moments $a_k$; CFKRS freezing;
  Guth-Maynard density; free-probability universal positivity; DIK generic Gram
  positivity): the object is compatible with a world containing an off-line zero,
  because it constrains averages/signatures generically, not the real part of any
  individual zero.

Formalization (Lean/Mathlib) is D-illusory **as a generator** but is the single most
valuable item in the entire dossier **as a verifier**: it cannot manufacture the
polarization, but it is the catch-net that turns an accident into a captured proof
and the mechanical guard against the de Branges and M2.6 stealth-window traps.

## 5. Watchlist (published-result signals that mean a channel just got hot)

1. **A Hodge-Riemann theorem for an arithmetic-AWARE object whose signature MOVES
   with a Frobenius trace $t$ AND which can FAIL** (the #40 $t=2$ vs $t=100$ probe
   finally separates, and the form is not unconditionally definite). Highest value:
   defeats AHK blindness and the tropical wrong-polarity problem at once. Promotes the
   tropical/Okounkov/AHK family from C to A.
2. **A constructed self-product $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$
   with an intersection theory and a cycle class for $\Gamma_S$** (bidegree $(1,p)$,
   $\Gamma_S^2$ = von Mangoldt sum). Makes the proven Chen-Moriwaki / Beilinson-Bloch
   / Gillet-Soule signatures APPLICABLE; both jump to A.
3. **A positive cup-product on global prismatic / syntomic / TP $H^1$ over
   $\mathbb{Z}$, derived intrinsically from the Nygaard/weight filtration** (no
   eigenspace decomposition, circumventing Petrov). Closes the Bhatt-Lurie /
   Hesselholt / Direction-10 route.
4. **An archimedean Fargues-Fontaine-type curve (or analytic-stack "compactified
   Spec($\mathbb{Z}$)") with a weight-purity / temperedness statement on its rank-1
   LocSys.** The arithmetic descent of GLC; weight-purity over this base IS the
   missing definiteness.
5. **Essential self-adjointness of the CCM zeta-spectral-triple limit operator**
   (uniform Caratheodory-Fejer persistence to the limit, no zero input). Fills the
   spectral slot; the Euler block already makes it D-H-discriminating.
6. **A leafwise Hodge-index theorem on Deninger's rational-Witt foliated space**
   (cup product against the flow-invariant transverse measure, negative-definite on
   non-polar eigenspaces). D-H-unbuildable; closes the Deninger channel.
7. **Beilinson-Bloch positivity upgraded from GENERIC to SHARP/UNCONDITIONAL on
   arithmetic self-products** (or an arithmetic inner product formula on a
   Spec($\mathbb{Z}$)-like base). Removes the second RH-hard step.
8. **NEGATIVE early-warning: any positivity claim that also holds for D-H, or any RH
   sketch that does not explicitly fail on D-H.** Flags the approach as K2-blind and
   retires it cheaply.

## 6. Cheap probes (runnable in this repo now)

The repo has the shared `LFunction` interface with controls for $\zeta$, D-H, a
Dirichlet L (Euler product), and a non-Euler RH-true **Epstein** control, plus the
M2.6 non-circular Weil/Rosati form, the Schur detector, and a Lean/Mathlib substrate.

1. **Four-way K2/Epstein guard (hours).** Loop the built non-circular Weil form
   ($M=A_{\mathrm{arch}}+P_{\mathrm{fin}}+B_{\mathrm{pole}}$, `e3c_weil_form` /
   `e3j_schur_complement`) over $\zeta$, D-H, Epstein, and a Dirichlet L. Demand every
   new accident-channel certificate reproduce the published M2.6 pattern ($\zeta\,
   {+}0.035$ RIGHT, D-H ${+}0.094$ WRONG-SIGN, Epstein no false fire) before any
   further work. This mechanically catches the de Branges trap.
2. **Prime-block ablation (hours).** Extend `e3m_place_type_balance` / `e3f` / `e3g`
   with a flag that zeroes the Euler/$\{\log p\}$ contribution and checks whether
   $\zeta$-vs-D-H discrimination DISAPPEARS. Operationalizes the spec's mandatory K2
   test: if discrimination survives prime-zeroing, the certificate is K2-blind
   (archimedean, shared with D-H) and is rejected.
   **DONE (2026-06-03, `experiments/positivity/e3p_prime_block_ablation.py`, LEARNINGS #46).**
   Result: the $M_{\mathrm{euler}}$ certificate is K2-GENUINE. Scaling the prime-power
   block by $\alpha\in[0,1]$: at $\alpha=1$ it sign-separates ($\zeta\,{+}0.035$ passes,
   D-H ${-}0.929$ fails); at $\alpha=0$ both are negative ($\zeta\,{-}2.34$, D-H ${-}4.63$)
   so the discrimination DISAPPEARS. The discriminating sign is carried by the Euler /
   $\{\log p\}$ block, not the archimedean block D-H shares. The positive counterpart to
   probe 3 (#45): there the PSLQ-accessible surface was the shared archimedean half;
   here the certificate's sign is verified to live on the unshared Euler half.
3. **Stumble-yield PSLQ sweep behind the D-H guard (a day).** PSLQ at $\ge 50$ digits
   over $\{\lambda_n, \gamma_k, C_\mu, \text{the THH/von-Mangoldt "one-Mobius-away"
   assembly}\}$, then immediately recompute every flagged relation for D-H and
   Epstein. Keep only relations that hold for $\zeta$ AND break for D-H. The
   numerical-stumble slot with the strictest bar baked in.
   **DONE (2026-06-03, `experiments/positivity/e3o_pslq_stumble.py`, LEARNINGS #45).**
   Result: the PSLQ-accessible surface (closed-form archimedean constants) is exactly
   the half D-H shares, and the discriminating Li data is precision-limited (~1 digit,
   large-n effect per #2), so the two surfaces are disjoint. PSLQ re-discovered the 3
   known archimedean identities (validation) and found no new one; the de Branges trap
   was reproduced (a spurious 8-digit-coefficient relation, residual $2.26\times10^{-61}$
   that does NOT vanish at higher precision) and defeated by a precision-stability test.
   Conclusion: the numerical-stumble accident is K2-blind by computability. A
   PSLQ-discoverable coincidence cannot distinguish $\zeta$ from its counterexample.
4. **Sharp-margin recovery test (hours-day).** Extend `e3k_hypothetical_offline` to
   inject a zero at $\rho\approx 0.8085+85.699\,i$ into a candidate's spectral input
   and measure where its margin crosses zero. Compare the required resolution to the
   Platt-Trudgian rigorous bound ($\epsilon<10^{-7}$) versus the float64 stealth
   window ($\epsilon<10^{-5}$). Tests "RECOVERS THE MARGIN, NOT JUST THE SIGN".
   **DONE (2026-06-03, `experiments/positivity/e3q_margin_recovery.py`, LEARNINGS #47).**
   Result: the off-line margin is a clean $-3.1\,\varepsilon^2$ law at the D-H height (real
   D-H zero $\varepsilon=0.3085$ gives $-0.77$, trivially detected). The float64 stealth is a
   REMOVABLE eigensolver-cancellation artifact, NOT structural: the signal source
   $\|\mathrm{Im}\,\phi\|^2$ is clean $\varepsilon^2$ with float64 $=$ mpmath to $\varepsilon=10^{-12}$.
   But removability is moot for certification: detecting an off-line zero at distance
   $\varepsilon$ requires injecting its location to precision $<\varepsilon$, exactly what rigorous
   verification supplies, so the certificate is downstream with no independent disproof
   leverage. The margin must be recovered analytically. Sharpens #3K/#19.
5. **Lean de-smuggling audit of the $C_\mu$ Weil form (days).** State
   $\min\mathrm{eig}(M)>0$ as a Lean proposition and trace its dependency graph
   against the Mathlib analytic-NT port to confirm no lemma silently assumes RH, GRH,
   or a zero-free region beyond Vinogradov-Korobov $2/3$. Formalization as the K1/
   non-circularity verifier.
6. **Wrong-polarity check for the convex-Hodge family (a day).** Build a small
   weighted matroid Chow ring / tropical fan with $w_p=\log p$ (Amini-Piquerez
   general-weight setting) and test computationally whether its HR form is
   UNCONDITIONALLY definite (cannot detect an off-line perturbation) or whether any
   weighting makes it fail. Reuses the `e3c2_weil_gram` cvxpy/CLARABEL machinery. A
   found violation is the watchlist-1 signal.
   **DONE (2026-06-03, `experiments/positivity/e3r_convex_hodge_polarity.py`, LEARNINGS #48).**
   Result: the convex-Hodge (mixed-area / Lorentzian) signature is UNCONDITIONALLY
   $(1, n-1)$ for every weighting (uniform, $w_p=\log p$, steep, adversarial; 2000/2000
   random cases have pos $=1$), so it cannot flip to flag an off-line zero: WRONG polarity.
   The Weil form, by contrast, flips PSD $\to$ indefinite when an off-line pair is injected
   (min-eig $0 \to -0.104$): RIGHT polarity. So the channel is blocked by TWO obstructions,
   #40 (arithmetic-blind, signature does not move with $t$) AND #48 (even if it did, the
   Kahler package cannot fail). The watchlist-1 signal needs a genuinely new theorem, not
   weight injection. No violation found (none expected).

## 7. Epistemics: why hard problems fall by accident, and the catch-net

Tao's claim, stated carefully, is not that hard problems are solved by luck. It is
that the deepest problems are usually solved as **byproducts**: a tool built for a
different, often more tractable, purpose turns out to fill the exact slot the hard
problem needs. Fermat fell because modularity (built for Langlands) supplied the
missing object; Poincare fell because Ricci flow plus Perelman's entropy
monotonicity supplied a polarization-like functional; the Weil conjectures fell
because etale cohomology (built structurally) plus the weight-monodromy argument
supplied the positivity. In every case the **realization** side was constructed
elsewhere, and the hard problem was the **signature/positivity** step the foreign
tool happened to carry.

That is exactly the present configuration. The adversarial pass establishes a
**no-free-lunch theorem** across all 28 candidates: full success of each program for
its own reasons delivers only the realization, and the residual step is itself
RH-equivalent. There is no channel where RH falls out as a strictly-cheaper
corollary. This is a targeting instruction, not a verdict: stop building
realizations (the repo has many), and instead (a) watch the few foreign programs
whose tool is the **right kind**, and (b) build the **catch-net** that converts an
accident into a captured proof.

The catch-net has three components, all of which this project has or can cheaply
build:

- **Formalization (Lean/Mathlib).** When a foreign tool produces a candidate
  positivity, a machine-checkable de-smuggling audit confirms it is non-circular (no
  hidden RH / GRH / zero-free-region assumption) and lands on the zeros, not on a
  surplus. Formalization cannot discover the polarization, but it catches the de
  Branges failure mode (positivity that overshoots to GRH and is false at the 34th
  zero) and turns a plausible byproduct into a captured theorem.
- **Cross-field translation dictionaries** like Morishita 2025 (the
  $\mathbb{R}_+$-anti-equivariant bridge between Deninger and Connes-Consani spaces).
  These are the wires along which a polarization built in one framework could be
  transported. Morishita currently transports only a **duality** dictionary; the day
  a dictionary carries a **signature** rather than a duality, an accident has
  happened.
- **The Davenport-Heilbronn filter as a real-time classifier.** A tool is
  RH-relevant precisely when it CANNOT be built for D-H. Every D-illusory candidate
  fails because its mechanism is D-H-shared; every B-credible one passes because its
  discriminating content lives on the Frobenius half. When a 2026 paper appears whose
  central object is unbuildable for D-H (a Frobenius correspondence, a prismatic $F$,
  an excursion operator, an Euler system, a periodic-orbit flow), the filter says:
  this is the right kind, watch it.

The decisive irony is that the repo's OWN finding sharpens which accidents are even
possible. The **marginal-positivity thesis** (RH is just barely true: D-H fails Weil
positivity by 78.7% per off-line direction, yet $\zeta$'s non-circular certificate
sits at $\min\mathrm{eig} = +0.035$ with the off-line obstruction below the
$10^{-7}$ stealth window) is a constraint on the accident space. A zero-slack gap
cannot be closed by a soft or lucky realization, because a soft certificate reads
spuriously positive for D-H too (M2.6: $\zeta\,{+}0.035$ right, D-H $\,{+}0.094$
wrong-sign). Therefore the accident, in whatever slot, **cannot be a fortunate
determinant or a statistical coincidence**: it must be a genuine **signature
theorem** that engages the exact off-line structure on the Frobenius/Euler half.
This is exactly what rules out the entire D-illusory tier (the Level-3 statistical,
the trace-side-circular, the archimedean-shared, the arithmetic-blind), not on
grounds of taste but on grounds of the zero-slack measurement.

So the marginal-positivity thesis is not a wall but a compass. It says the only real
accidents are the ones that supply a definite, $t$-carrying, D-H-unbuildable
polarization, which is precisely the B-credible tier. Every channel ruled out is a
coordinate, and the coordinates all point at the same place the function-field proof
already lives: the Hodge-index signature on a primitive subspace, carried by
Frobenius.

## 8. References

Project-internal: [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md);
[`all_roads_to_the_signature.md`](all_roads_to_the_signature.md);
[`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md)
(M1-M5 ladder, the M2.6 four-way discrimination, K1/R3.5 non-circularity);
[`experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md) #18-21, #25-27, #29,
#40-44; the positivity experiment suite (`e3c_weil_form`, `e3j_schur_complement`,
`e3k_hypothetical_offline`, `e3l_epstein_control`, `e3m_place_type_balance`);
the shared controls (`davenport_heilbronn.py`, `epstein_zeta.py`, `dirichlet_l.py`).

External (selected, 2024-2026, to verify against originals before formal citation):
Gaitsgory-Raskin et al. GLC (arXiv:2405.03599, 2409.09856); Fargues-Scholze
(arXiv:2102.13459); Drinfeld Prismatization (arXiv:2301.12392) and prismatization
over $\mathbb{Z}$ (arXiv:2504.07005); Bhatt-Lurie (arXiv:2201.06120); Petrov, Annals
(arXiv:2302.11389); Tang, prismatic Poincare duality (Compositio 2024); Hesselholt,
THH and the Hasse-Weil zeta function (2018); Connes-Consani, On the Jacobian of
$\overline{\mathrm{Spec}\,\mathbb{Z}}$ (arXiv:2602.15941, 2026); Connes-Consani-
Moscovici, Zeta Spectral Triples (arXiv:2511.22755, 2025); Alvarez-Lopez/Kim/
Morishita (arXiv:2410.20758); Deninger (arXiv:1807.06400); Morishita
(arXiv:2508.15971, 2025); Clausen-Scholze, Six-Functor Formalisms (arXiv:2510.26269)
and Condensed Mathematics and Complex Geometry; Chen-Moriwaki, Positivity in
Arakelov Geometry over Adelic Curves (Progress in Math 355, 2024); Yuan-Zhang (Math.
Ann. 367, 2017); Ballay (J. Algebraic Geom. 33, 2024); Wilms (arXiv:2502.18441,
2025); Gao, generic positivity of Beilinson-Bloch heights (2024); Amini-Piquerez
(arXiv:2310.15367); Branden-Huh, Lorentzian polynomials (Ann. Math. 2020); Griffin-
Ono-Rolen-Zagier (PNAS 2019); Dimitrov-Lucas; Rodgers-Tao (Forum Math. Pi 2020);
Guth-Maynard (arXiv:2405.20552, Annals 2025); Pilatte (arXiv:2310.19357); Altug,
Beyond Endoscopy III (arXiv:1512.09249); Kim-Sarnak; Conrey-Li (arXiv:math/9812166).
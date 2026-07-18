# Reading notes: Connes-Consani, *On the Absolute Geometry of Spec Z and the Fargues-Fontaine curve* (arXiv:2606.06604v1, 4 Jun 2026)

> SURVEYOR reading note, 2026-07-10. Target: the single most important of the four "closest live-M4"
> papers flagged in [`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md:57) and
> [`PHASE_STATE.md`](../../../PHASE_STATE.md) (#155) as lacking a reading note, because Connes-Consani are
> the primary authors of the arithmetic-site / scaling-site program that is the repo's current frontier
> (the CCM Section-7 uniform limit = M4). Companion to the two existing CCM notes:
> [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md) (the Feb-2026 survey
> 2602.04022, the prolate / Weil-form / Letter-to-Riemann analytic thread) and
> [`../ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) (the semilocal prolate operator; the
> #153/#154 Section-7 = M4 addenda). This paper is on the ORTHOGONAL (geometric substrate) axis of the
> same program: it builds the F_1 / Fargues-Fontaine carrier, not the positivity.
>
> **Fidelity:** the bibliographic header, section structure, abstract, theorem statements, and the
> decisive ABSENCE of any RH / Weil-positivity / Xi / prolate / uniform-limit / determinant content are
> VERIFIED-BY-FETCH against two independent renders (ar5iv HTML + arxiv.org/html), which agree. The
> internal proofs were NOT read (no proof-level verification). Theorem wordings are high-confidence
> fast-model reads of the HTML, not a line-by-line LaTeX read (same caveat class as
> `ccm_semilocal_prolate.md`); the absence claims are the robust part and are what the verdict hinges on.

## Verified bibliographic header (VERIFIED-BY-FETCH)

- **Title.** *On the Absolute Geometry of Spec Z and the Fargues-Fontaine curve.* (The arXiv abstract-page
  metadata truncates this to "On the Absolute Geometry of Spec Z"; the HTML running head and the search
  index carry the full title including the Fargues-Fontaine clause.)
- **Authors.** Alain Connes, Caterina Consani.
- **arXiv.** 2606.06604v1, submitted 4 June 2026. 30 pages. License CC-BY 4.0.
- **Subjects.** Primary math.AG (Algebraic Geometry); secondary math.NT (Number Theory).
- **MSC 2020.** 14G40, 14G45, 06F05, 11R42, 11M55. (Note: 11M55 is "relations with noncommutative
  geometry"; 11R42 is "zeta functions and L-functions of number fields." So the number-theory tag is the
  Spec Z / arithmetic-site lineage, NOT an RH claim; see the absence finding below.)
- **Sections (verbatim order):** Abstract; 1 Introduction (with a "Heuristic Idea (P. Scholze)"
  paragraph); 2 Lift of the Abel-Jacobi Map to Pic* (2.1 lift; 2.2 pullback of the absolute structure
  sheaf; 2.3 morphisms from stalks to F_1-algebras); 3 Spec Z and the Fargues-Fontaine Curve (3.1-3.10:
  dense embeddings in local fields, places, local morphisms, points over a field and the tilt, points in
  a perfectoid field, char-p perfectoid points, cyclotomic embeddings, symmetries and the FF curve,
  Scholze's heuristic, universal tilting functor and geometric sieve); 4 Points of (Spec Z)_{F_1} over C
  (4.1 geometric C-points local at infinity; 4.4 geometric C-points local at p); 5 Outlook; References.
  **There is NO Section 6 and NO Section 7.**

## What it does (VERIFIED-BY-FETCH at abstract + theorem-statement level)

A purely **geometric / foundational** construction. There is no analysis, no positivity, no zeta
function evaluated. The paper builds an absolute (F_1-level) arithmetic curve over Spec Z and shows that
evaluating its points over perfectoid and complex fields reproduces, on the nose, three previously
separate objects: the tilting formalism of p-adic Hodge theory, the Fargues-Fontaine curve, and
(complex-analytically) the Tate curve with the CCM scaling-site periodic orbits.

Structural claims, in order:

1. **The F_1-arithmetic curve (Section 2).** Define the F_1-arithmetic site Pic* = (N-hat-x_0, O_{F_1}),
   O_{F_1} = F_1[T] (the spherical algebra of the free monoid on one variable), over the presheaf topos of
   sets with an action of the multiplicative monoid N. There is a geometric morphism Theta: Spec Z ->
   N-hat-x_0 (from [CC1, Thm 5.3]) sending a prime p to the ordered group [(Z[1/p], Z[1/p]_+)] and the
   generic point to the trivial group. Define the F_1-curve (Spec Z)_{F_1} := (Spec Z, F) with
   F := Theta^{-1}(O_{F_1}) the pullback sheaf. **Prop 2.2:** the stalks are F_eta = F_1 at the generic
   point and F_p = F_1[T^{Z[1/p]_+}] at prime p (the "perfect at p" stalk: exponents in the additive
   group Z[1/p]).

2. **Realization of Scholze's heuristic (Section 3, Theorems 1 / 3.16 / 3.17).** For F an algebraically
   closed perfectoid field of characteristic p, the moduli of local F-points of (Spec Z)_{F_1}, modulo the
   canonical stalk symmetries, decomposes over the closed points of Spec Z as: at every prime ℓ ≠ p the
   fiber rigidly collapses to a single orbit; at the prime p the fiber is canonically in bijection with
   the untilts of F modulo Frobenius. Theorem 3.17 phrases this as a "strict geometric sieve": the F_1
   stalk at p acts as a **universal tilting functor** (Prop 3.7: evaluation extracts the tilt F-flat), and
   the ultrametric mismatch at ℓ ≠ p forces discreteness.

3. **The Fargues-Fontaine curve as a quotient (Cor 3.14 / 3.15).** Quotient the non-trivial local
   morphisms by Z_p^x -> untilts of C-flat containing all p-power roots of unity; quotient by the full
   Q_p^x -> the closed points of the Fargues-Fontaine curve X_{F,Q_p}. So FF appears intrinsically as a
   symmetry quotient of the F_1-curve's fiber at p.

4. **Complex points and the Tate curve (Section 4, Theorems 3 / 4).** Over C at each prime p, the
   non-trivial points canonically form **two principal homogeneous spaces (torsors) over the Weil groups**
   W_p = Q_p^x and W_infty = C^x (Thm 3: single Weil-group orbit each). Quotienting the archimedean orbit
   by the discrete Frobenius p^Z yields the **complex Tate curve** E_p = C^x / p^Z with modulus q = p^{-1}
   (Thm 4), which decomposes canonically as E_p ≅ C_p x X-tilde_infty (periodic orbit of length log p
   times a p-independent phase factor of length 2 pi), with holomorphic 1-form omega = d lambda / lambda +
   i d theta. The archimedean analogue X_infty := M_p^infty / W_infty^sigma ≅ P^1(R) is offered as "an
   archimedean analogue of the Fargues-Fontaine curve."

5. **Outlook (Section 5).** The characteristic-1 geometry of the CCM scaling site S [CC3] is "intrinsically
   encoded in the analytic structure underlying the Fargues-Fontaine curve, and appears as the intrinsic
   idempotent skeleton underlying p-adic Hodge geometry." This is the paper's ONLY explicit bridge back to
   the zeta-carrying half of the CCM program, and it is a substrate-identification remark, not a theorem
   about positivity or convergence.

**The decisive absence (VERIFIED-BY-FETCH, both renders independently).** The words *Riemann Hypothesis*,
*Weil positivity*, *Xi / xi function*, *prolate*, *Sonin*, *uniform limit*, *regularized determinant*,
*convergence xi_lambda -> Xi*, and *zeta zeros* **do not appear**. The scaling site is named exactly once,
in the Outlook, as a substrate identification. There is no Section 7. This paper is the geometric-carrier
half of the program, deliberately upstream of the analytic positivity thread where the M4 wall lives.

## Central object

The load-bearing object is the pullback sheaf **F = Theta^{-1}(O_{F_1})** on Spec Z and its fiber over
perfectoid / complex fields. Structurally this is a **candidate variety-free carrier** on the Frobenius
side of Spec Z: it equips Spec Z with (i) a per-prime local geometry (the FF curve at p, the Tate curve
over C), (ii) a Frobenius / Weil-group action (W_p, W_infty) intrinsic to the stalk, and (iii) the
scaling-site periodic orbits C_p of length log p (the "knots = primes" data of the CCM survey, here
DERIVED from the absolute F_1 geometry rather than posited). It is a substrate with a Frobenius datum. It
carries no cohomological grading, no Lefschetz operator, no pairing of Hodge-Riemann type, and no
positivity.

## Scorecard: 2606.06604's central object vs the repo M4 skeleton (S1-S7) + R1 + K1

The S1-S7 skeleton is the field-agnostic M4 statement from [`../breadth_program.md`](../breadth_program.md)
(lines 59-72); S6 (right-polarity / contingency) is the master discriminator, S7 non-circularity. R1 is the
sourcing facet from [`../sourcing_gap_r1.md`](../sourcing_gap_r1.md); K1 the circularity constraint; the
#156 clause from [`../model_theoretic_frobenius.md`](../model_theoretic_frobenius.md).

| Constraint | Status for 2606.06604 | Evidence / note |
|---|---|---|
| **S1** Lefschetz operator L on a graded V | **ABSENT** | No cohomology, no graded space, no L. The object is a moduli-of-points / sheaf construction, not a Weil cohomology. (Verified: no such structure in the section list or theorems.) |
| **S2** primitive decomposition | **ABSENT** | Nothing to decompose; no graded V. |
| **S3** perfect (-1)-symmetric pairing Q (the functional equation) | **SUBSTRATE ONLY** | There is geometric duality data (the Tate-curve 1-form omega = dlambda/lambda + i dtheta; the real-locus vs phase-space split E_p ≅ C_p x X-tilde_infty; the two Weil-group torsors). But no perfect Hodge-Riemann pairing is constructed. Symmetry present; polarizable pairing not built. |
| **S4** distinguished trace datum t (the Frobenius eigenvalue / spectral parameter) | **PRESENT (substrate), genuinely new** | The Weil-group action W_p = Q_p^x, W_infty = C^x and the Frobenius quotient p^Z; the periodic orbit C_p of length log p. This is the paper's strongest S-contribution: a Frobenius-side datum DERIVED from absolute geometry. But it is a carrier datum, not a computed trace/pole budget. |
| **S5** polarization (definite of fixed sign on primitives) | **ABSENT** | No positivity anywhere in the paper. |
| **S6** right polarity: (S5) is CONTINGENT on t and FLIPS off-locus (the master discriminator) | **ABSENT / AUTO-BLIND** | Decisive column. There is no signature, so nothing can flip. The construction is identical in shape whether or not RH holds; it never sees the critical line. Cannot discriminate zeta from Davenport-Heilbronn because it carries no sign to discriminate WITH. |
| **S7** non-circularity | **N/A for positivity; construction is zero-free** | No positivity is claimed, so there is nothing to prove non-circularly. The construction itself never inputs zeta zeros (it is pure F_1 / perfectoid geometry). Vacuously clean, but only because it produces no sign. |
| **R1** variety-free Frobenius source WITH a computable pole/trace budget | **PARTIAL: supplies substrate, NAMES no mechanism** | This is where the paper actually lands (not M4). It DOES supply a genuinely new candidate variety-free carrier on the Frobenius side of Spec Z (the F_1-curve with an intrinsic Weil-group action, FF at each p). It does NOT supply (a) an independently computable pole/trace budget, (b) the #153 additive-lattice GLUE (its Theta pullback and Z[1/p]_+ lattice are topos-geometric, not the metric/archimedean-aware trace glue #153 requires; no explicit formula, no trace is written), or (c) a uniform determinant-class limit (#148/#154). It builds the carrier and names the substrate; it supplies no trace mechanism = the repo's standing "realization/carrier is free in framework after framework" pattern. |
| **K1** circularity (does positivity smuggle in the zeros) | **CLEAN (vacuously)** | No zeros are input anywhere; the construction is K1-clean. But K1 does not bite either way because no positivity is derived. |
| **#156 WATCH clause** (index-set-preserving AND non-endomorphism-shaped) | **CONSISTENT (passes the consistency check)** | Both conjuncts hold, as expected for CCM's own program. Index-set-preserving: F is a SHEAF over ALL of Spec Z; the ℓ ≠ p "collapse" is per-untilt-field, not a global quotient of the prime index set (every prime remains a distinct fiber, Thm 3.16). Non-endomorphism-shaped: Theta is a geometric morphism of topoi and the arithmetic action is the Weil-group action W_v (a group action / correspondence flavor), not a single ring endomorphism. So the object sits in the #156 survivor class (Borger, Deninger, CCM E-map, Connes). This is a consistency check, and it passes: the paper does not trip the model-theoretic no-go, consistent with #156's own list. |

**One-line scorecard reading.** The paper is strong on S4 (a new Frobenius-side substrate datum) and R1's
carrier facet, empty on S5-S6 (the polarization and its contingency = M4), and vacuously clean on
S7 / K1 because it produces no sign. It is a carrier, not a polarization.

## Verdict: ADJACENT-WATCH (new object, substrate axis, not load-bearing for M4/CCM)

Using the [`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md) taxonomy
(KNOWN-TO-REPO / ADJACENT-WATCH / NEW-LOAD-BEARING):

- **Not NEW-LOAD-BEARING.** It supplies no positivity mechanism, no computable trace/pole budget, and does
  not touch the M4 / CCM Section-7 residual. It fails the move-criterion for R1 (carrier without a trace
  budget) and does not engage S5-S6 at all.
- **Not merely KNOWN-TO-REPO.** Unlike the corpus's KNOWN-TO-REPO restatements, the OBJECT here is
  genuinely new: the F_1-curve as a pullback sheaf, the realization of Scholze's heuristic, and the
  intrinsic appearance of the Fargues-Fontaine curve and the scaling-site periodic orbits from absolute
  geometry are new geometric content, not a repackaging of something the repo already holds.
- **Therefore ADJACENT-WATCH.** A genuine substrate development on the authors' own frontier program,
  landing on the R1 / carrier axis. Its live value is as a potentially better geometric SUBSTRATE (an
  archimedean-inclusive, FF-based home for the scaling site), the P3 "better component" role from
  [`../breadth_program.md`](../breadth_program.md) (line 45), not as a supplier of the missing sign.

## CRITICAL: does it move the CCM Section-7 = M4 wall? NO.

Direct answer: **No. This paper does not move the Section-7 uniform-limit = M4 wall at all, in either
direction.** Three independent reasons, in decreasing order of how conclusive:

1. **It is on the other thread of the program.** The "Section-7 uniform limit = M4" wall is the
   convergence xi_lambda -> Xi (equivalently global Weil positivity) that lives in the CCM ANALYTIC thread:
   the Feb-2026 survey 2602.04022 Section 7 (the prolate / Sonin / Weil-form machinery), the D_log family
   2511.22755 / 2511.23257, and the prolate operator 2112.05500. See
   [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md) (Section 6.6, "the gap")
   and [`../ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) addenda #153/#154. The present paper is
   the GEOMETRIC-CARRIER thread. It has no Section 7 (only 5 sections), and it contains none of the objects
   the wall is stated in (no Xi, no prolate operator, no Weil form, no uniform limit, no determinant). It is
   structurally upstream of the wall.

2. **It builds the carrier half, which was never the bottleneck.** The repo's standing finding (S1-S4
   "realization" is free in framework after framework; S5-S6-S7 is M4; see
   [`../sourcing_gap_r1.md`](../sourcing_gap_r1.md) line 58 and
   [`../ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) section D) is that supplying a better
   substrate does not move the positivity wall. This paper supplies a genuinely better substrate (S4 + R1's
   carrier facet) and, exactly as the pattern predicts, does not touch S5-S6. The FF / scaling-site
   unification is a cleaner GEOMETRIC ORIGIN for the objects the CCM analytic thread already uses; it does
   not provide the convergence estimate or the sign that thread is missing.

3. **It names the substrate without a mechanism, the expected outcome.** Per the honesty brief (#155: the
   whole 2021-2026 corpus had 0 survivors; the nearest crossing named the M4 residual and supplied no
   mechanism), the expected outcome for a CCM substrate paper is exactly this: it deepens the geometric
   picture (here, genuinely, by DERIVING the scaling-site periodic orbits and the Tate curve from absolute
   F_1 geometry) but supplies no positivity mechanism. It confirms the #131 read of the sibling Feb-2026
   paper 2602.15941 ("On the Jacobian of Spec Z-bar") as **trace-side / substrate-side only**; 2606.06604
   is the same program's substrate thread one step further, and the read is unchanged.

**Skeptical re-read (where a load-bearing claim would hide, and why it is not here).** The one place a
skeptic looks for hidden M4 content is the Fargues-Fontaine connection: the FF curve carries a
Harder-Narasimhan / slope (semistability) formalism, which is a positivity-flavored structure, and the
paper explicitly identifies the scaling site as "the intrinsic idempotent skeleton underlying p-adic Hodge
geometry." If the paper had constructed a polarization (a definite pairing contingent on the critical line)
out of the FF slope structure, that would be NEW-LOAD-BEARING and would have to be reported loudly. It does
not. The FF appearance is a bijection of point-sets (Cor 3.15: FF closed points = a symmetry quotient of
the fiber), an identification of carriers, with no pairing, no signature, and no contingency on any
spectral parameter. So the skeptical re-read confirms substrate-only. The honest WATCH trigger this paper
sets is: *if a follow-up derives a Hodge-Riemann-type polarization on this FF / scaling-site substrate
whose sign is contingent on the critical line, that would be the mechanism.* This paper is the substrate
for that hypothetical, not the hypothetical.

## Discrepancy log (against existing repo analyses)

- **No contradiction found.** The paper is consistent with every existing repo analysis of the CCM program.
- **One refinement of the title-based triage.** The arch2-supplement and
  [`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md:57) listed 2606.06604 among the
  "four closest live-M4 papers." The deep read RELOCATES it from the M4 (polarization) axis to the R1 /
  substrate (carrier) axis: it is close to the CCM program, but its content is carrier, not polarization.
  This is a sharpening consistent with the supplement's own honest verdict ("none supplies the missing
  object"), not a disagreement. Recommend the M4-adjacency label on this paper be read as "CCM-program
  adjacency, substrate face," not "M4 mechanism candidate."
- **Confirms, does not contradict, #131.** #131 read the sibling 2602.15941 (CC Jacobian of Spec Z-bar) as
  "trace-side only." 2606.06604 is the same substrate lineage; the trace-side / substrate-only read holds.

## References to chase (paper-internal, mostly bibliographic-only in this repo)

Self-citations (the CCM absolute-geometry lineage; verify which already have repo homes):
- **[CC1]** the arithmetic site N-hat-x_0 and the geometric morphism Theta (Thm 5.3). Repo home:
  [`../../../experiments/arithmetic_geometric/2A_R3_6_arithmetic_site.md`](../../../experiments/arithmetic_geometric/2A_R3_6_arithmetic_site.md).
- **[CC3]** the scaling site S and the characteristic-1 periodic orbit C_p (the object this paper derives
  geometrically). The zeta-carrying half of the program.
- **[CC6]** Pic(Spec Z) and the Abel-Jacobi map; sibling to the Feb-2026 "Jacobian of Spec Z-bar"
  (arXiv:2602.15941, already noted #131 as trace-side only).
- **[CC2], [CC4]** spherical algebras F_1[T] and base-change for F_1-algebras.

External:
- **[FF]** Fargues-Fontaine (the curve realized as the quotient at p).
- **[Scholze], [Lurie]** the perfectoid / untilt heuristic being realized (Scholze's lectures via Lurie).
- **[Weil], [Xu]** Ostrowski's theorem; spherical-algebra details.

Not yet in the repo and worth a WATCH (per the #155 CCM-axis alert): any FOLLOW-UP that puts a pairing or a
Harder-Narasimhan-sourced positivity on this FF / scaling-site substrate. That, not this paper, would be the
mechanism.

## What this enables / what remains open

**Enables (for BUILDER / SYNTHESIZER).**
- A cleaner, archimedean-inclusive geometric SUBSTRATE for the scaling site: the CCM periodic orbits C_p
  (length log p) and the archimedean phase factor now have a DERIVED geometric origin (absolute F_1
  geometry -> Tate curve E_p ≅ C_p x X-tilde_infty), rather than being posited. If a BUILDER later attempts
  an M4 polarization on the CCM side, this is the better substrate to attempt it on (the P3 role), because
  it packages the Frobenius/Weil-group datum (S4) and the FF slope formalism in one place.
- A consistency datum for #156: CCM's absolute-geometry construction is index-set-preserving AND
  non-endomorphism-shaped, confirming the survivor class is stable across their newest paper.

**Remains open (unchanged frontier).**
- The M4 / CCM Section-7 wall (uniform xi_lambda -> Xi = global Weil positivity) is UNTOUCHED by this paper.
  It stays exactly where [`../ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) (#153/#154) and
  [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md) (§6.6) left it: the
  authors' own "main remaining obstacle," met-not-escaped at the Section-7 step, in the analytic thread.
- The load-bearing question this paper does NOT answer: is there a polarization (a definite,
  critical-line-contingent pairing) on the FF / scaling-site substrate? WATCH the CCM axis for it.

**For ADVERSARY.** No positivity claim is made, so there is no positivity to break here; the D-H discipline
is not triggered (the object carries no sign, so it is trivially D-H-blind by type, which is fine because it
claims nothing about zeta). The only adversarial action is to confirm the absence: if a future revision adds
a positivity theorem sourced from the FF slope structure, re-run S6 (does the signature flip, and on what)
and K1 (does the FF-side construction input the zeros) at that point.

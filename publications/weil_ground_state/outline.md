# P12 outline: "The ground state of the localized Weil form: certified numerics for the Connes-Consani-Moscovici-Suzuki limit"

Working outline (2026-08-20). Registry: PUBLICATIONS.md P12. Sources: LEARNINGS #180-#187 and the
e2an/e2ao/e2aq/e2ar/e2as/e2at/e2au dossiers. Status: awaiting the e2au turnaround verdict, then the
law-novelty pass, then drafting.

## Framing (one paragraph, stated early)

This note claims no progress toward RH. It measures, with explicit certificates, the finite-window
behavior of the object at the center of a live spectral-theoretic program (Yoshida 1992; Bombieri
2000; Connes-Consani-Moscovici, "Zeta spectral triples"; Suzuki, arXiv:2606.09096 v2): the ground
state of Weil's quadratic form localized to $L^2(-a,a)$, whose Fourier transform is conjectured
((1.2) in Suzuki's account) to converge to $\xi(1/2+iz)$. Every claim carries its precision, its
convergence gate, and its certificate; three of the paper's own pre-registered hypotheses were
refuted by its runs, and the refutations are reported as the results they produced.

## Section plan

1. **Setup and conventions.** The Weil form, the window localization, the additive picture; the
   zero-side instrument; the exact-closed-form B-spline basis (hard support, 13 orders of endpoint
   flatness, sinc-power FTs, cardinal-spline Grams: no quadrature in the form); precision protocol
   (zeros AND arithmetic at matched digits; why float-accurate zeros cap resolvable bottoms at
   1e-50).
2. **The single-mode margin law.** margin$(\sigma) = 4\sqrt{\pi}\sigma e^{-\gamma_1^2\sigma^2}$:
   measurement (four figures, 38 orders), the refuted midgap prediction, the derivation (the pole is
   EF-cancelled; the central hole has radius $\gamma_1$), and the certification-cost corollary
   (prime-side assembly certifies only $\sigma^2 < \ln(c/\varepsilon)/\gamma_1^2$).
3. **The multi-mode bottom: exact locking and the graded frontier.** Nodes on every reachable zero
   to working precision; the annihilation frontier two-plus zeros past the ceiling; ~6 decades of
   node precision per zero; the fixed-grid $\sigma$-slope selecting the first unannihilatable
   zero's distance to 2 percent; the refuted nearest-gap law; the mode-count confound.
4. **The xi-shape transient.** Soft-window family degeneracy (typed: hole norm-stuffing) vs the
   hard window's rigidity; the $a = 1$ match to $\Xi$ (residual 0.051, refinement-stable 0.026);
   certified narrowing through $a = 2.5$ at 80 digits; per-quantity convergence (eigenvectors
   before eigenvalues).
5. **Placement and the object identification.** CCM's $QW_\lambda$ on the full window (weightless
   $\kappa$): the measured object IS (1.2)'s; the pole-constrained control (ratios explode;
   $\Xi(i/2) = 1/2$ violates the constraint; CCM's Lemma 7.3 is interior-only); why the
   finite-$\lambda$ kernel-groundstate proximity is compatible with common narrowing.
6. **The turnaround.** [e2au verdict slot: either $a^*$ located on $[2.5, 5]$, or monotone
   continuation with the proximity question posed]. Composition with CCM's proven kernel limit;
   what each outcome means for (1.2).
7. **Instrument appendix.** The certificate suite and what each caught (capacity scaling, precision
   starvation, cutoff exploitation, basis-convergence gates, the removable-pole evaluation);
   reproducibility pointers (all code and 50-110-digit zero caches in the repository).

## Figures (from the existing gallery machinery, restyled for print)

F1 margin law with the certification floor (gallery 6); F2 the frontier's graded node-precision
profile; F3 the a-ladder ratio curves with gates (the transient); F4 the turnaround readout (e2au).

## Blocking items

1. e2au verdict (in flight). 2. Law-novelty pass (Fourier-optimization school) on Sections 2-3's
closed forms. 3. Owen's author decisions (name, acknowledgments, arXiv categories: math.NT primary,
cross-list math.CA?).

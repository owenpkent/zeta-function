# E2BB: the eta-form second variation: the Hessian exists, its signature is forced, and what forces it is holomorphy, not positivity

**Date**: 2026-08-23. **Status**: BUILDER round, executed; 11/11 checks (~10 min, mp dps 20). **Code**: [`e2bb_eta_second_variation.py`](e2bb_eta_second_variation.py). **Data**: `e2bb_eta_second_variation.npz` (tracked). **Executes**: backlog C2 (#178's trigger-1 probe, given shape). **K1 posture**: zeros consumed by design (form-side diagnostic of the eta functional); Beurling refusal typed (the pencil needs the FE); the D-H discipline is INTERNAL (generic pencil members ARE the FE-no-Euler class, measured: off-line fraction 1.00 immediately off the character point).

## 0. The setting

Character space is archimedean-ly discrete (#177/#178), so the eta invariant's second variation needs a chosen continuous deformation space: the only FE-closed continuous family through a complex character $\chi$ is the pencil $\mathrm{span}\{L(s,\chi), L(s,\bar\chi)\}$. Directions: $d_1 = L(\bar\chi)$, $d_2 = iL(\bar\chi)$ (conjugate-mixing, reality-breaking: the eta-active plane) and $d_3, d_4$ (rescalings: exact null rows, measured $1.2\times10^{-26}$: the end-to-end pipeline validation). $\eta(g_u)$ from Newton-tracked zeros (completeness inherited; $u = 0$ sets complete against the density formula, on-line to $10^{-20}$), Abel weights on a $\tau$-ladder, Cesaro counting-window as the independent estimator, and the #178 C1 closed form $-(2/\pi)\arg_c L(\tfrac12,\chi)$ as the anchor (Cesaro-vs-C1: $0.034$ at $q = 5$, $0.064$ at $q = 7$). Secondary exact validations landed: $\eta$ at the real-coefficient point $u = (1,0)$ is $-4.9\times10^{-2} \approx 0$ (conjugation-symmetric spectrum, step-tracked through the D-H-class region with zero losses), and the conservation-law mini-cell below.

## 1. THE RESULT: a canonical Hessian with a FORCED signature, and the force is holomorphy

The $2\times2$ eta-Hessian on the conjugate-mixing plane exists canonically: step-halving dev $0.00$, $\tau$-ladder drift $8$ percent, $T$-window-cut dev $0.17$, and it is

$$H_{q=5} = \begin{pmatrix} -0.235 & -0.471 \\ -0.471 & +0.235 \end{pmatrix}, \qquad H_{q=7} = \begin{pmatrix} +0.276 & -0.291 \\ -0.291 & -0.295 \end{pmatrix}:$$

**traceless** ($|\mathrm{tr}|/\|H\|$: $0.000$ at $q=5$, $0.045$ at $q=7$) with signature $(1,1)$ at BOTH conductors: forced, exactly as the fork's [F-A] branch demanded: and the forcing mechanism is identifiable and elementary: the zeros move HOLOMORPHICALLY in the complex mixing parameter $w = u_1 + iu_2$ (implicit function theorem on $g(s,w) = L(s,\chi) + wB(s)$), so each $\mathrm{Im}\,\rho_j(w)$ is harmonic, and $\eta_\tau = \sum_j \mathrm{sign}_j e^{-|\mathrm{Im}\rho_j|\tau}$ has Hessian $= \sum F_j'\cdot\mathrm{Hess}(\mathrm{Im}\rho_j)$ (traceless) $+ O(\tau^2)$ gradient terms: traceless at leading Abel order, with the measured trace/norm ratios sitting exactly at the predicted $O(\tau)$ scale. The zero-side decomposition confirms the shape: per-zero $|$contribution$|$ correlates $0.90$ ($q{=}5$) / $0.84$ ($q{=}7$) with the $|B(\rho)/L'(\rho)|^2 e^{-\gamma\tau}$ profile: the APS-costume magnitude profile, carrying the harmonic sign structure.

## 2. The fork's verdict: the unlisted third branch

The backlog fork was "reproduces the Weil form (M4 in APS costume: coordinate #5) or fails forcing (trigger 1 hardens)." The measurement takes the branch neither wording anticipated: **forcing SUCCEEDS: and it forces the harmonic (traceless) structure, which is the structural OPPOSITE of a polarization.** A traceless form is maximally indefinite: it cannot be positive on any half of its domain, at any conductor, for the same reason at every conductor. Coordinate #5 is therefore minted as a no-go with a mechanism: **the eta route's second variation is conformally rigid: holomorphy of zero motion in every FE-closed deformation balances the signature exactly, so no positivity can be sourced from the eta-form's curvature.** This is the second-order extension of #178's parity kill (the odd sector is exactly solvable and exactly RH-blind): at first order eta's variation is prime-local with no bulk term; at second order its curvature is harmonic with no definite part. #177's trigger 1 hardens in the sharpened sense: a functorial eta-form EXISTS at finite conductor (canonical, stable, forced), and it is harmonic-class, not polarization-class.

## 3. The conservation-law mini-cell (a closed form for a banked number)

The mod-5 real pencil's Euler defect has the closed form $b_6(\kappa) = (\kappa^2 + 1)\log 6 \ge \log 6$, with conservation-Hessian $2\log 6 > 0$: and e2an's measured D-H value $b_6 = 1.936$ (LEARNINGS #179's Euler-leak witness) is its exact evaluation at $\kappa_{\rm DH}$: $(\kappa_{\rm DH}^2 + 1)\log 6 = 1.9364$. The real FE-pencil is bounded away from Euler by a positive-definite quadratic: the Euler points sit at $\kappa = \pm i$, off the real pencil entirely: which is WHY D-H exists.

## 4. Estimator lessons (typed, reusable)

- **Non-commuting limits**: at fixed truncation $T$, the Abel $\tau \to 0$ extrapolation is biased toward the integer $D(T)$ ($\tau \to 0$ and $T \to \infty$ do not commute); the eta VALUE should be anchored by C1/Cesaro, while the HESSIAN is immune (low-zero-dominated: the $\tau$/T-stability gates).
- **Cesaro granularity**: the counting-window estimator is integer-granular, so its second differences at small steps are noise ($H^{\rm Ces}_{11} = -3.7$ vs Abel $-0.235$): estimator granularity, not regularization failure: it remains the good eta-level estimator.
- **The Hurwitz-pole nan**: the $\arg$-continuation grid must avoid $\sigma = 1$ (per-term poles cancel analytically, not numerically).

## 5. Scope and caveats

Two conductors (5, 7), one complex character each, window $T = 30$ (21 and 24 zeros), $h = 0.03$ stencils at dps 20: the forced-signature claim is measured at two conductors with one shared mechanism proof-sketch (holomorphy), not a theorem for all $q$ (the mechanism argument is conductor-independent, which is the real content; a VERIFIER-shaped statement is named below). The pencil is the 2-complex-dimensional FE-closed family; richer deformation spaces (higher conductor blocks, several characters) would give larger harmonic Hessians, same mechanism. Frontier verdict: UNMOVED (a form-side diagnostic; the finding is a sharpened no-go coordinate).

## 6. Hand-off

(i) The VERIFIER nugget, clean and self-contained: "if $\rho(w)$ is holomorphic and nonreal, then $w \mapsto f(\mathrm{Im}\,\rho(w))$ has traceless Hessian up to $f''$-terms": one lemma; its corollary is the conductor-independence of the (1,1) forcing. (ii) The heavy tier's last item is C4 (the Lean `SPInterface` with e2ay's witnesses). (iii) The eta arc (#177 triggers) now has triggers 1 and 2 both typed (2 discharged by #178's build; 1 hardened-with-structure here); trigger 3 (the ACS "path integrals of L-function type") remains the only open one. (iv) The $b_6$ closed form belongs in e2an's margin notes if that dossier is ever revised.

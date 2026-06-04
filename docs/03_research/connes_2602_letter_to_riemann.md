# Connes' "Letter to Riemann" (arXiv:2602.04022): assessment against this project

> Dossier on Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*
> (arXiv:2602.04022v1, 3 Feb 2026, 42 pp). Written 2026-06-03. The paper is a commissioned RH
> survey with a research kernel ("a new perspective that emerged during its preparation"). This
> dossier records what the kernel is, what it proves versus the precise gap, and how it lands
> against the project's spine: the marginal-positivity thesis, the $(N_{\text{off}}, N_{\text{off}})$
> Weil-Gram signature, the Davenport-Heilbronn discipline, the Spec(Z) cohomology landscape, and
> the "RH solved by accident" framework. Two experiments instrument the conclusions:
> [`e3s_connes_eta.py`](../../experiments/positivity/e3s_connes_eta.py) and
> [`e3t_prolate_residual.py`](../../experiments/positivity/e3t_prolate_residual.py).

## 1. What the paper is, and the one new claim

The survey portion covers 165 years of RH approaches (analytic NT, entire-function theory, Weil
over function fields, Langlands, random-matrix/GUE, Connes' own NCG trace formula, p-adic/motivic
$L$-functions, and the equivalent formulations: Weil positivity, Beurling-Nyman, Li, Robin/Lagarias,
with a Godel/Chaitin digression on RH's logical status).

The research kernel is a **constructive reframing of Weil positivity**. The recipe (the "Letter to
Riemann"):

1. Restrict the Weil quadratic form $QW_\lambda$ to test functions $g$ supported on
   $[\lambda^{-1}, \lambda] \subset \mathbb{R}^*_+$, i.e. on $\log u \in [-\Lambda, \Lambda]$ with
   $\Lambda = \tfrac12 \log x$. Only prime powers $n = p^m \le x = \lambda^2$ enter, via the
   explicit-formula local terms $W_p$.
2. Take the minimal eigenvector $\eta_x$ of $QW_\lambda$ (Connes constructs it by extremizing the
   form, an analogue of Riemann's Dirichlet-principle proof of the conformal mapping theorem).
3. **Theorem 6.1 (Connes-van Suijlekom, "Quadratic Forms, Real Zeros and Echoes of the Spectral
   Action")**: for any even real distributional kernel $\tilde D(x-y)$ defining a lower-bounded
   self-adjoint operator whose spectral minimum is a **simple, isolated eigenvalue with even
   eigenfunction** $\eta$, every zero of the entire function $\hat\eta(z)$ lies on the real line.
   Applied to $QW_\lambda$ this gives, **unconditionally**, that the zeros of $\hat\eta_x$ lie
   exactly on the critical line for each finite cutoff.
4. **Conjecture (UNPROVEN)**: as $x \to \infty$, $\eta_x$ converges so that $\hat\eta_x \to$
   Riemann's $\Xi$; then Hurwitz's theorem (a uniform limit of functions with only real zeros has
   only real zeros) forces RH.

The advertised evidence: using only primes $\le 13$, the first 50 zeros are recovered with
accuracies from $2.6 \times 10^{-55}$ (first zero) to $\sim 10^{-3}$ (50th). The prolate spheroidal
wave operator $PW_\lambda = -\partial_x[(\lambda^2 - x^2)\partial_x] + (2\pi\lambda x)^2$ (Slepian-
Pollak-Landau, rooted in Shannon's band/time-limiting problem) plays a dual role: in the **infrared**
it supplies the eigenvector model $k_\lambda$ (sec 6.3-6.5), and in the **ultraviolet** a self-
adjoint extension on the Sonin space (with Moscovici, ref [27]) reproduces the large-zero
asymptotics. Sections 7.x rewrite the 1998 trace formula in Shannon/Slepian time-limiting $P_T$ /
band-limiting $\hat P_W$ projections and place the semilocal adele class space $Y_S$ as a sheaf over
$\mathrm{Spec}\,\mathbb{Z}$ (Theorem 7.2).

## 2. Proven versus the precise gap

**Proven and unconditional:** Theorem 6.1; its corollary (each finite-cutoff $\hat\eta_x$ has on-
line zeros); Fact 6.2 ($\Xi = $ FT of $E(h)$, $h$ the vanishing-integral combination of Hermite
$h_0, h_4$); Fact 6.3 (Slepian-Pollak prolate commutation); Fact 6.4 (the **prolate model**
$\hat k_\lambda \to \Xi$, with explicit rate); Theorem 7.1 (archimedean Weil positivity via the
Sonin space); the trace-formula reformulations; Theorem 7.2 (sheaf compatibility). The Moscovici
result is a genuine but **asymptotic** UV match (only at $\lambda = 1, \sqrt2$), with a Dirac-square-
root ambiguity tied to the differential Galois theory of the prolate equation. Theorem 7.3 (heat
expansion) is **conditional on RH**, a consequence not a step.

**The precise gap.** Theorem 6.1 **manufactures an on-line-zeros function for any admissible form.**
Its hypotheses (lower-bounded, simple isolated even ground state) are mild and generic; they require
no positivity and know nothing about the Euler product. Zeta enters only as the choice of input
distribution. So the entire RH content collapses into one unproven convergence: $\eta_x$ (recentered
$\theta_x$) must converge to $E(h)$ with control strong enough for Hurwitz. Connes states this
verbatim ("This is something which at this point is not proved") and localizes it in sec 6.6: the
proven convergence (Fact 6.4) is only for the **archimedean** prolate model $k_\lambda$; the genuine
missing micro-step is "$k_\lambda$ is a sufficiently good approximation of $\theta_x$," and that
implicitly requires controlling $QW_\lambda$, whose global positivity is Weil's criterion, i.e. RH.
Two further sub-gaps: the simple+even hypothesis of Theorem 6.1 is verified only for the prolate
analogue, not for $QW_\lambda$; and $QW_\lambda$ positivity is proved only for small $\lambda$
(Yoshida; Connes-Consani).

## 3. Against the project's marginal-positivity thesis and $(N_{\text{off}}, N_{\text{off}})$ signature

Connes **confirms the framing and, read through the project's instruments, sharpens it.** It does
not contradict anything.

- **Same object.** $QW_\lambda$ is the project's truncated Weil/Rosati form (e3c/e3c2 answer-side
  Gram; e3j Schur split; e3m M2-M3 non-circular form, $\min\mathrm{eig} = +0.035$ for zeta). The
  project's [`2A_R3_connes_positivity.md`](../../experiments/arithmetic_geometric/2A_R3_connes_positivity.md)
  (C1) already records that Connes' positivity conjecture *is* the Weil-Bombieri form with
  $\mathrm{PSD} \Leftrightarrow$ RH.
- **$\varepsilon(\lambda)$ is an independent measurement of the project's near-radical.** Connes'
  Figure 1 (the smallest eigenvalue $\varepsilon(\sqrt x)$ tracking $1 - \chi_2 \sim e^{-4\pi e^L}$,
  from the near-intersection of $P_\lambda$ and $\hat P_\lambda$) is the same "no buffer"
  phenomenon the marginal-positivity thesis pins at the $\sim 0.1\%$ boundary/prime cancellation
  (LEARNINGS #7). He calls it the "near radical of the Weil form"; the project calls it the stealth
  window. Two instruments, one wall.
- **The $(N_{\text{off}}, N_{\text{off}})$ finding is exactly why the convergence equals RH.**
  Connes' sec 6.4 ("RH implies $QW_\lambda$ is strictly positive and its radical is $\{0\}$") is the
  project's e3j result stated qualitatively: the Schur complement of the D-H Weil Gram has dimension
  $2 N_{\text{off}}$ and signature exactly $(N_{\text{off}}, N_{\text{off}})$, one rank-2 indefinite
  block per off-line $\gamma$, saturating at $-78.7\%$ (LEARNINGS #18). The project supplies the
  magnitude of the obstruction the convergence must overcome.
- **Sharpening back to the project.** Connes localizes the gap one notch finer than "bound the von
  Mangoldt sum to $0.1\%$": specifically "$k_\lambda$ approximates $\theta_x$," which separates the
  **archimedean** prolate model (proven to converge) from the **Euler-coupled** true eigenvector
  (unproven). This maps onto the project's M3 finding (LEARNINGS #46) that the discriminating sign
  rides the Euler/$\{\log p\}$ block.

## 4. Davenport-Heilbronn discipline: distinguishes only via the unproven step

**Verdict: distinguishes only via the unproven convergence, which is provably false for D-H and
circular for zeta.** This is the load-bearing result and it is instrumented in
[`e3s_connes_eta.py`](../../experiments/positivity/e3s_connes_eta.py).

Steps 1-3 of the machine are zeta-blind. D-H has a functional equation, hence its own explicit
formula and its own $QW_\lambda^{DH}$; as long as that form is lower-bounded with a simple even
ground state (a mild generic condition, **not** requiring RH), Theorem 6.1 fabricates an all-zeros-
on-line function for D-H exactly as for zeta. The experiment confirms this directly:

- With cutoff $x = 25$ and grid $N = 120$, the minimal eigenvector recovers the first eight **zeta**
  zeros to $\sim 10^{-2}$ (e.g. $14.0997$ vs $14.1347$, $21.0053$ vs $21.0220$), with $117/119$
  polynomial roots on the unit circle.
- The **identical** machine recovers D-H's **on-line** zeros even more accurately ($5.0946,\,
  8.9407,\, 12.1329,\, 14.4048,\dots$ vs true $5.0942,\, 8.9399,\, 12.1335,\, 14.4040$), also
  $117/119$ roots on the circle. The construction is zeta-blind.
- **Caratheodory-Fejer, input-agnostic.** The minimal eigenvector of a marginally PSD Toeplitz form
  has **all** roots on the unit circle regardless of input: a zeta-derived symbol, a D-H-derived
  symbol, and a pseudo-random symbol all give frac-on-circle $= 1.000$. "All zeros on the critical
  line" is a property of the construction, not of zeta.
- **The off-line obstruction.** D-H has off-line zeros at $0.8085 + 85.699i$ and $0.1915 + 85.699i$.
  Near height $85.7$ the machine produces only real frequencies ($83.5,\, 85.4,\, 87.7,\dots$).
  Theorem 6.1 forbids a complex zero of $\hat\eta$, so $\hat\eta_{DH}$ cannot represent the off-line
  zero; hence $\hat\eta_{DH} \not\to \Xi_{DH}$ (Hurwitz: a uniform limit of real-zero functions has
  no complex zero). The only place zeta and D-H differ is exactly the step Connes leaves unproven,
  and it is **false for D-H** and **RH-equivalent for zeta** (the project's R3.5 no-shortcut theorem).

## 5. The prolate ansatz: the work is archimedean (e3t)

[`e3t_prolate_residual.py`](../../experiments/positivity/e3t_prolate_residual.py) instruments the
prolate side of the gap.

- **Fact 6.4, reproduced.** $k_\lambda = E(h_\lambda)$, built from the prolate eigenfunctions of
  $PW_\lambda$ (the harmonic-oscillator/Gamma-factor family) with **zero primes**, has
  $\hat k_\lambda$ recovering the first zeta zero to $14.133$-$14.135$ (true $14.1347$) for
  $x = 13, 25, 49$.
- **It nearly achieves the infimum.** $Q(k_\lambda)/\|k_\lambda\|^2$ is comparable to the
  resolution-limited $\varepsilon_{\min}$ of $QW_\lambda$: the prolate "educated guess" is a good
  approximation of the minimizer in energy.
- **The energy is archimedean-dominated.** Decomposing $Q(k_\lambda) = A_{\text{arch}}(k_\lambda) -
  \mathrm{PrimeTerm}(k_\lambda)$, the prime coupling is $\sim 0.9$-$1.3\%$ of the archimedean block.
  The archimedean/prolate model alone does the work, and that model is **shared with D-H** (D-H has a
  $\Gamma$-factor). So the prolate approximation cannot be what distinguishes zeta from D-H; the
  Euler block is exactly the part $k_\lambda$ does **not** supply, and supplying it (proving
  $k_\lambda = \theta_x$ and that the infimum $\to 0$ globally) is the unproven, RH-equivalent step.
  This is the e3s off-line obstruction seen from the ansatz side, and it confirms the project's
  thesis (LEARNINGS #46, the spec_z K2 caveat) that all discrimination lives on the Euler/Frobenius
  half.

## 6. Placement in the landscape

- **Spec(Z) cohomology landscape** ([`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md)).
  The paper does not change the existing Connes-family rows; it adds a **sharper realization half**.
  Theorem 6.1 makes the finite-cutoff on-line property a **theorem** rather than a trace identity, so
  the realization/polarization asymmetry is more vivid, not less. Column (iii), the RH-equivalent
  polarization, is still absent; the residual positivity (the convergence) is K1-circular. A
  Connes-$\eta$ row is added to the scorecard.
- **RH solved by accident** ([`rh_solved_by_accident.md`](rh_solved_by_accident.md)). A commissioned
  survey whose RH perspective "emerged during preparation" is textbook Tao byproduct structure.
  Routed through the no-free-lunch theorem it lands **C-longshot, not A/B**: the proven fragments
  (Theorem 7.1 Sonin space; Fact 6.4 prolate convergence; the Moscovici UV model) are exactly the
  **archimedean, D-H-shared, RH-agnostic** half the theorem predicts a survey would deliver. The
  Moscovici "ultraviolet model" (the long-flagged gap that no fixed spectral operator matches the
  log-growing zero density) is genuinely new infrastructure on the realization/IR-UV axis, but still
  archimedean and polarization-free.

## 7. Bottom line

Connes' construction is a clean, unconditional theorem (6.1) that produces on-line zeros for every
finite cutoff, plus a proven **archimedean** convergence (Fact 6.4). The whole of RH is concentrated
in one unproven, RH-equivalent step ($k_\lambda \to \theta_x$, i.e. $QW_\lambda$ positive with
trivial radical in the limit). Because Theorem 6.1 fires identically for Davenport-Heilbronn, the
method distinguishes zeta from D-H only through that step, which is provably false for D-H and
circular for zeta. This **confirms and sharpens** the project's marginal-positivity thesis and the
$(N_{\text{off}}, N_{\text{off}})$ Weil-Gram signature: Connes' $\varepsilon(\lambda)$ / near-radical
is an independent measurement of the same zero-buffer the project pinned at $-78.7\%$ per off-line
direction. In the landscape it is another trace-without-polarization instance with a sharper
realization half, a C-longshot accident channel, and its only proven positivity (Sonin/archimedean,
prolate model) is the D-H-shared, RH-agnostic half exactly as the no-free-lunch theorem predicts.

## 8. References

- Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022v1 (2026).
- Connes-van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (ref [32] therein).
- Connes-Moscovici, prolate self-adjoint extension / UV spectral model (ref [27] therein).
- Connes-Consani, *Weil positivity and the archimedean place* (Sonin space), arXiv:2006.13771 (2021).
- Connes-Consani, *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$*, arXiv:2602.15941 (2026).
- Project internal: [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md);
  [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md);
  [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md);
  [`rh_solved_by_accident.md`](rh_solved_by_accident.md);
  [`2A_R3_connes_positivity.md`](../../experiments/arithmetic_geometric/2A_R3_connes_positivity.md);
  LEARNINGS #7/#18/#46/#49/#50; experiments
  [`e3s_connes_eta.py`](../../experiments/positivity/e3s_connes_eta.py),
  [`e3t_prolate_residual.py`](../../experiments/positivity/e3t_prolate_residual.py).

# E2AR: the faithful hard-window xi-test: at the converged window, the ground state IS the xi shape

**Date**: 2026-08-20. **Status**: BUILDER round, executed; 8/8 checks (97 s; 50-digit protocol). **Code**: [`e2ar_hard_window_xi.py`](e2ar_hard_window_xi.py). **Data**: `e2ar_hard_window_xi.npz` (tracked). **Executes**: backlog B2c-hard (the live half of the xi-convergence test after e2aq typed the soft family's failure). **Target**: Suzuki arXiv:2606.09096, conjecture (1.2): the localized Weil-form ground state's Fourier transform converges to $\xi(1/2+iz)$.

## 0. Headline

At the basis-converged window ($a = 1$), the hard-window Weil-form ground state's Fourier transform **is the xi function's shape**: $L^2$ residual $0.051$ against a fitted multiple of $\Xi$ on $[0, 10]$, pointwise agreement within 26 percent out to $z = 8$, refinement-stable to $0.026$ under a doubled basis. Against the soft-window family's residuals of 33-154 (e2aq), the hard support is worth a factor of about a thousand: the rigidity IS the window, exactly as the family-dependence diagnosis predicted. This is the repo's first direct numerical contact with the live conjecture, and it is positive at the window the instrument can certify.

## 1. The instrument

Even cardinal B-splines of degree 12 on a uniform knot grid strictly inside $[-a, a]$: hard support by construction, 13 orders of endpoint flatness, and EXACT 50-digit closed forms for both the Fourier transforms (sinc powers times cosines) and the $L^2$ Gram (the degree-25 cardinal spline at integer offsets, a finite rational sum): no quadrature anywhere in the form. Zero side on the 50-digit zeros to $T = 200$ (the e2aq cache); mp.eigsy for the bottom pair; knot spacing FIXED across the ladder ($h = 1/28$, so capacity scales with the window: the first run held $J$ fixed and its rising residual was a capacity artifact, corrected).

Three certificates guard the claims, and each caught something:
- **A-posteriori tail** (the minimizer's own above-cutoff mass): margins exceed $10\times$ the tail at every kept rung; the $a = 3$ rung FAILED it spectacularly (tail $10^{-15}$ vs margin at the dps floor: the type-3 family exploits the $T = 200$ cutoff) and is excluded, with the fix quantified (zeros to $T \approx 350$).
- **Eigenvector-mixing safety**: $\sqrt{\mathrm{tail}_0\,\mathrm{tail}_1}/(\lambda_1 - \lambda_0)$ at most $10^{-3}$: the omitted tail cannot rotate the ground state.
- **The basis-convergence gate** (the decisive one): double-knot-density controls. $a = 1$: pointwise ratios shift $0.026$ (converged; the shape claim stands) while $\lambda_0$ itself still falls under refinement (per-quantity gating: the eigenvector converges before the eigenvalue). $a = 2$: ratios shift by up to $20.9$, and the refined solve is genuinely degenerate (gap $0.9$, $\lambda_0$ at the 50-digit floor): everything at $a \ge 1.5$ is gated OUT of the claims.

## 2. What is claimed, what is recorded, what is excluded

- **CLAIMED (gated)**: rigidity restored at every rung (within-family gaps 849 to $8\times10^6$; the soft family's degeneracy is gone); the $a = 1$ xi-shape match as in the headline; node locking (a node within $10^{-18}$-$10^{-28}$ of $\gamma_1$ at every rung).
- **RECORDED, no claim**: across the raw ladder the $z = 6$ ratio falls monotonically ($1.28 \to 0.01$), i.e. the finite-basis lobe narrows through the xi shape near $a \approx 1$; since the $a \ge 1.5$ rungs are basis-unconverged, this narrowing is NOT evidence about the continuum ground state. Whether the true finite-$a$ state stays on $\Xi$ (as (1.2) wants) or genuinely narrows is exactly what the deeper instrument must decide.
- **EXCLUDED**: $a = 3$ (cutoff-exploited); $a \ge 1.5$ shape claims (unconverged).

## 3. The quantified exit (B2c-deep)

Testing (1.2) beyond $a \approx 1$ needs, jointly: 50-digit-or-better zeros to $T \gtrsim 350$ (the cutoff wall measured at $a = 3$), working precision comfortably above the continuum $\lambda_0$ at the target window (the $a = 2$ refined solve already sits at the dps-50 floor: dps 80+), and refinement until the pointwise gate passes per rung. Cost: one long zero-computation (cacheable) plus eigsy at dps 80: feasible on this box; queued as B2c-deep.

## 4. Verdict

Frontier UNMOVED (a diagnostic of the form, zeros consumed by design). Banked: the first positive numerical contact with Suzuki (1.2) at the certifiable window; the instrument-design lessons (capacity must scale with the window; within-family gaps do not imply continuum convergence; per-quantity convergence gating); the measured walls of the deeper test. The e2aq + e2ar pair now gives the corpus-facing statement: the soft-window family cannot see (1.2) for a typed mechanistic reason, the hard window sees it at $a = 1$, and the $a$-ladder's continuation is a precision-and-cutoff engineering problem with measured requirements, not an open-ended search.

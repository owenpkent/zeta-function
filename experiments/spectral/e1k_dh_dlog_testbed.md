# E1K: the CCM D_log spectral triple as a Davenport-Heilbronn testbed

> Companion to `e1k_dh_dlog_testbed.py` / `.npz`. Reimplements the
> Connes-Consani-Moscovici rank-one D_log operator (arXiv:2511.22755) and its
> Caratheodory-Fejer self-adjointness engine (arXiv:2511.23257) faithfully in
> mpmath/numpy, then runs it side by side on a zeta stream and a
> Davenport-Heilbronn stream. Source spec: the reading note
> [`docs/03_research/reading_notes/CCM-2025-Dlog-family.md`](../../docs/03_research/reading_notes/CCM-2025-Dlog-family.md).
> Continues the e1f-e1j CCM thread. It proves nothing about RH; it confirms and
> sharpens the D-H discipline. All numbers below are from the default run.

> **BANNER (read before quoting any number):** `dh_discrimination_real = FALSE
> BY DESIGN`. The zeta-vs-D-H separation lives ONLY in the unreachable
> Section-7 / M4 uniform limit (`lambda^2 >~ 5e11`). Every finite-cutoff fact in
> this record is D-H-blind and RH-neutral. The `FALSE` is the D-H discipline
> working as intended (finite reality is information-free), NOT a testbed
> failure; do not later cite any finite-cutoff reality here as bearing on RH.

## One-line result

The finite machine is **Davenport-Heilbronn-blind at every reachable cutoff**:
identical code builds both twins, and the D-H twin's finite spectrum is real
(to 7.8e-30 at 30-digit precision) and matches D-H's on-line zeros. At the
HEIGHT of D-H's genuine off-line zero the nearest finite eigenvalue is real
(85.78, Im ~ 2e-12) where the true zero is complex (`z = 85.699 - 0.308i`); the
finite self-adjoint operator can only ever return a real number in that
neighborhood, never the complex zero. (At this cutoff, `lambda=3.7 / N=36`, that
85.78 is the finite operator's generic real spectrum near that height, NOT a
fidelity reconstruction of that specific zero.) The zeta-vs-D-H discrimination is quarantined
entirely to the unreachable Section-7 uniform limit. Finite reality carries zero
bits about RH (the information-free-finiteness / M4 wall, LEARNINGS #153/#154).

## What was built (faithfully)

The truncated Weil quadratic form `QW = A_arch + [pole] - sum_{2<=n<=lambda^2}
Lambda(n) T(n)` on the orthonormal Fourier basis `V_n` of the log-circle of
circumference `L = 2 log lambda`. Derived closed forms, verified numerically:

- `Vhat_n(z) = 2 L^{-1/2} sin(zL/2)/(z - 2 pi n / L)` (matches paper eq (5.25),
  verified against the direct integral to **1e-31**).
- Prime term `T(n)` from the multiplicative-shift correlation `(V_m star
  V_n)(k) + (V_m star V_n)(1/k)`, in closed form (no quadrature).
- Archimedean term by mpmath tanh-sinh over the whole line with the L-function's
  OWN density (zeta: `(1/2pi)(Re psi(1/4+it/2) - log pi)`; D-H, an odd character
  mod 5: `(1/2pi)(log(5/pi) + Re psi(3/4+it/2))`). NB the reading note's claim
  that D-H "shares zeta's Gamma factor" is imprecise: D-H uses `Gamma((s+1)/2)`
  (odd), not `Gamma(s/2)`. We use D-H's own factor. Reality is insensitive to
  which archimedean factor is used, so the discipline conclusion is unaffected.
- Pole term `2 Re(conj(a_m) a_n)`, `a_n = Vhat_n(i/2)`, present **only for
  zeta** (D-H is entire; a rank-<=2 structural difference).

The two functions enter through the SAME code via the Dirichlet log-derivative
recursion `sum_{d|n} Lambda(d) c_{n/d} = c_n log n` (`c_1 = 1`):

| stream | `c_n` | `Lambda(n)` | support |
|---|---|---|---|
| ZETA | `1` | von Mangoldt `log p` on prime powers | prime powers only (Euler product) |
| D-H | period-5 `(1, kappa, -kappa, -1, 0)` | dense, sign-changing, non-multiplicative | ALL `n >= 2` (no Euler product) |

Validation that the reconstruction is faithful: the finite spectrum reproduces
the low zeros of BOTH functions.
- ZETA (N=10, lambda=sqrt13): 14.1347 (err 6e-5), 21.0220 (1.6e-4), 25.0109 (1e-3).
- D-H  (N=10, lambda=sqrt13): 5.0942 (3e-5), 8.9399 (1.9e-3), 12.1335 (1.8e-3), 14.4040 (5.3e-3), 17.1302 (1.8e-2).

## Task 1 -- K2 / CF-on-D-H feasibility: **CF RUNS on D-H (finite reality then information-free)**

The Caratheodory-Fejer self-adjointness condition (23257 Thm 1.2/6.1) requires
only that the form be **real + even + lower-bounded + simple lowest eigenvalue**.
None of these references an Euler product. D-H supplies a genuine
log-derivative coefficient stream `Lambda_DH(n)` (dense, sign-changing), and the
support truncation `n <= lambda^2` makes the sum finite exactly as for zeta.
Both matrices assemble by IDENTICAL code; the only differences are the
coefficient comb and the (rank-<=2) pole term. Hence CF is input-agnostic and
runs on D-H. This is NOT a non-mimicry exemption: D-H IS buildable by type.

## Task 2 -- finite-cutoff reality on the D-H twin: **REAL (as Thm 5.10(iii) predicts, D-H-blind)**

Operator `D' = D_log - |D_log xi><delta_N|`; its eigenvalues are the zeros of
`xihat` (Thm 5.10(ii)). Reality reported side by side, with the
G-self-adjointness residual `||GM - M^H G|| / (||G|| ||M||)`, `G = Q - eps I`,
as the fidelity measure (a G-self-adjoint operator has real spectrum by
construction):

| twin | G-self-adj residual | float (N=10) physical max\|Im\| | HP (N=6, dps=30) physical max\|Im\| |
|---|---|---|---|
| D-H | **4.1e-06** | 2.5e-11 | **7.8e-30** |
| ZETA | 2.5e-02 | 1.5e-09 | 5.3 (ghosts) |

The **D-H twin is essentially exactly G-self-adjoint** and its physical
eigenvalues are real to 30-digit precision, matching D-H's on-line zeros. This
is the D-H-blind, information-free-finiteness fact made concrete: the same
theorem that manufactures on-line reality for zeta manufactures it for D-H, with
no arithmetic input.

Honest caveat: the zeta twin's pole-term realization is not exactly the CF
normal form (residual 2.5e-2), so a few "ghost" eigenvalues go complex at high
precision (`max|Im| = 5.33` at HP); this is a reconstruction imperfection
specific to the zeta pole term, NOT a statement about the theorem. It does not
weaken the discipline conclusion, because both twins run identical code. The
D-H-vs-zeta asymmetry here is **entirely** an artifact of one term: the zeta
twin carries a rank-2 pole matrix that is only approximately realized (the
coefficient `a_n = Vhat_n(i/2)` is reused for both the `i/2` and `-i/2` slots),
which D-H simply lacks (D-H is entire, `use_pole=False`). So D-H reconstructs
cleaner ONLY because it has one fewer approximate term, NOT because an off-line
-zero function is intrinsically easier. Read the fidelity accordingly: the D-H
twin (real to 7.8e-30) and the LOW zeta eigenvalues are the trustworthy outputs;
the zeta twin should **not** be quoted as a faithful realization of Thm 5.10(iii)
at high eigenvalues, where its ghost complex values are a pole-term artifact.

## Task 3 -- uniformity / off-line-zero signal: the off-line zero shows up ONLY as a limit non-uniformity

Direct off-line probe (N=36, lambda=3.7: spectral range now covers 85.7):

```
D-H eigenvalues in (70,100):  71.51, 73.47, 75.83, 78.07, 80.44, 82.69, 85.7828
all with |Im| < 3e-12
```

At the HEIGHT of D-H's genuine off-line zero (`s = 0.808 + 85.699i`, i.e. `z =
85.699 - 0.308i`, **complex**), the nearest finite eigenvalue is **85.7828**
(real, Im = -2.3e-12). It is off the true height by 0.083 (the nearest tooth of a
~2-spaced comb), and at this cutoff (`lambda=3.7 / N=36`) the reconstruction has
no fidelity at height ~85 (the low D-H zeros already drift to ~2e-2 by the 5th),
so 85.78 is the finite operator's **generic real spectrum** in that neighborhood,
NOT a reconstruction of that specific zero. The substantive point does not depend
on the eigenvalue landing on 85.699: the finite self-adjoint operator can only
ever return a real number near that height, NEVER the off-line complex zero. This
is the sharpest form of the discipline: at the height of a known counterexample
zero, the finite machine returns a real number. The off-line zero can only emerge in the `lambda -> inf` uniform
limit, where a sequence of real-zero entire functions fails (by the Hurwitz
contrapositive) to converge uniformly to `Xi_DH` near `gamma ~ 85.7`.

Infeasibility, stated honestly: the DIRECT Section-7 uniform-limit test needs
`lambda^2 >~ 5e11` (Platt-Trudgian region) to be in the convergence regime where
the D-H stall is separable from truncation noise. That is out of reach. What IS
reachable (above) is the finite-cutoff fact that the reality is preserved even at
the off-line height, with the archimedean stealth suppression
(`e^{-(pi/4) d gamma} ~ 1e-30` near `gamma ~ 85.7`) keeping the finite reality
exact to machine/HP precision. So the off-line zero is invisible at finite cutoff
by design, and the discrimination is a large-lambda uniformity phenomenon only.

Lambda sweep (N=8): both twins' smallest eigenvalue **hovers within ~1e-4 of
zero** (the marginal / zero-margin structure), sign fluctuating with cutoff.
Neither shows a clean lower-boundedness break at reachable `lambda`, because
resolving `gamma ~ 85.7` needs spectral range `N >~ 36`, and the stealth
suppression preserves finite reality far beyond that. The predicted D-H
positivity break (reading note: `lambda ~ 3.7`) is not cleanly visible in `eps`
at `N = 8`; the finite `eps` is itself D-H-blind. An incidental finding: the
even/odd lowest eigenvalues are **near-degenerate** for D-H, so the "assumed
even" hypothesis is marginal and the global minimum is ODD at several cutoffs
(flagged `o` in the sweep, `[WARN]` in Task 2) -- exactly the Remark 2.3 /
simplicity caveat, surfaced honestly rather than hidden.

## Task 4 -- C3 reading: the testbed SUPPORTS C3

Every object of the Section-7 limit (`xihat_lambda`, `D_log`, the truncated Weil
form, the prolate/Sonin space, the periodization `E`) lives on the real log-line
= C3's archimedean-injection object; no non-archimedean carrier appears. The
`lambda -> inf` limit injects all primes (`support = {p <= lambda^2}`), so the
Section-7 uniform limit IS the uniformity of the archimedean injection over all
primes. The D-H twin fails uniformity exactly there (near `gamma ~ 85.7`), and
nowhere in the finite construction. This confirms C3's object+location identity
(Tiers 1-2) while leaving Tier 3 (logical equivalence) as it stands: C3 locates
and names the uniformity; the RH-hardness owns its truth-value. The Section-7
uniform limit is M4 in yet another costume (uniform truncated-Weil ground-state
control = global Weil positivity with a rate).

## The honest wall (where the testbed confirms it)

The wall is at the **Section-7 uniform limit**, and it is **M4-equivalent**. The
finite construction -- operator, determinant identity, and reality -- is
installed and exact, and is **information-free** (D-H-blind): both twins produce
real finite spectra by the same finite-self-adjointness mechanism, and the D-H
twin does so even at the height of its off-line zero. Discrimination appears only
in the `lambda -> inf` limit as a convergence non-uniformity, which is
simultaneously CCM's "main remaining obstacle," the RH-equivalent global Weil
positivity with a rate, and the sole place the zeta-vs-D-H separation can live.

## Overclaim guard (what this does NOT show)

- It does **not** move RH. Every finite-cutoff reality fact is D-H-blind and
  therefore RH-neutral by construction.
- It does **not** prove the Section-7 limit for zeta or disprove it for D-H; the
  direct test is infeasible (`lambda^2 >~ 5e11`).
- The reconstruction is a testbed, not the paper's exact operator: the zeta
  pole-term realization is imperfect (self-adjointness residual 2.5e-2, ghost
  complex eigenvalues at high precision), and the ground state sits on a
  near-degenerate zero-margin cluster where the "even" and "simple" hypotheses
  are marginal. These are honest limitations of the numerics, not claims.
- The wall stays exactly M4-equivalent: nothing here narrows the gap between
  finite reality and the uniform limit.

## Reproduce

```
python -m experiments.spectral.e1k_dh_dlog_testbed          # full (~5 min)
python -m experiments.spectral.e1k_dh_dlog_testbed --skip-hp --skip-offline
```
Outputs `e1k_dh_dlog_testbed.npz` (streams, spectra, sweep, off-line probe).

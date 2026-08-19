# E2AN: SP-object v0, the first assembled instance of the missing-object interface

**Date**: 2026-08-19. **Status**: BUILDER round, executed; 27/27 checks full (`--quick` skips the D-H zero-list check). **Code**: [`e2an_sp_object_v0.py`](e2an_sp_object_v0.py). **Data**: `e2an_sp_object_v0.npz` (tracked next to the script per the evidence rule). **Spec**: [`missing_object_interface.md`](../../docs/03_research/missing_object_interface.md) (the five components SP1-SP5, open joints C1/C2), CCM door shape from B1 rung 4.

## 0. What this is

Owen's directive: build the object, even if it is wrong. Every prior probe inhabited SP components one at a time; this round assembles ONE datum $X = (H, \mathrm{Fr}, (B,\Delta), \mathrm{TF}, \mathrm{pol})$ at finite scale and scores all five components on zeta and on both controls through identical code. The object is wrong exactly where the interface document said the two open joints are, and now the wrongness has numbers.

The engine is one identity (Muntz's formula). For $f$ smooth, compactly supported in $(0,\infty)$:

$$\int_{\mathbb{R}} \Big[\sum_{\nu} a_\nu f(\nu e^s) - R\, I_1 e^{-s}\Big] e^{(1/2+i\tau)s}\, ds \;=\; m(\tau)\,\tilde f(\tfrac12+i\tau),$$

with $m(\tau) = L(1/2+i\tau)$. Everything on the left is integer data (the coefficient lattice, its density $R$); $m$ is EXTRACTED, never evaluated: the construction consumes no L-value and no zero (K1 guard: an oracle-call counter asserts 0 through the whole build phase). The carrier is the circle $C_L = \mathbb{R}/L\mathbb{Z}$; its Fourier grid $\tau_k = 2\pi k/L$ is the Mellin grid $c_k = 1/2 + i\tau_k$ (critical sampling), and the descent of the lattice map $\mathcal{E}(f)(u) = u^{1/2}\sum a_n f(nu)$ to the circle is exactly the fold of the line engine (verified to 3.3e-10, the SP1-SP2 joint). The cokernel of the map (where $|m|$ dips) is literally an $H^1$; the scaling flow compressed to it has the zeros as spectrum. This realizes B1 rung 4's door shape numerically: one circle, the map $\mathcal{E}$ eating the surplus states, the whole budget on the circumference.

## 1. The scorecard (all cells measured by the one pipeline)

| Component | zeta | D-H (FE, no Euler) | Beurling (Euler, no lattice) |
|---|---|---|---|
| SP1 realization: $m(\tau)$ lattice-sourced | 2.5e-12 vs $\zeta(1/2+i\tau)$ | 7.7e-14 vs $DH(1/2+i\tau)$ | exists at every finite scale |
| SP1c duality: completed $m$ real on line | 2.4e-11 | 2.2e-11 (its OWN $\Gamma$: FE intact) | **0.665 defect** (borrowed $\Gamma$) |
| $H^0$ (pole): descent divergence $e^{S/2}$, residue | expo 0.5000, $R = 1.0005$ | $R = 2.7\text{e-}17$ (entire) | $R = 1.5856$ = its density $A = 1.5870$ |
| descent converges (a critical line exists) | drift 2.1e-12 | converges | **drift 0.505**: no line to converge to |
| SP2 emergent spectrum (cokernel dips) | 29/29 zeros to $T=100$, max err 1.25e-4, 0 spurious, stability 7e-15 | 100% of its ON-line zeros found | dips exist but scale-unstable |
| SP2 completeness | = RH, not provided (the point) | **off-line pair invisible**: $|m|$ at 85.7 stays 0.242 vs dip depth 4e-4 (600x) | n/a |
| SP3 diagonal knows primes ($b_n$ division) | $b_n = \Lambda(n)$ to 3.8e-15 | **$b_6 = 1.936$**, 1475 leaks off prime powers ($n\le5000$) | exact von Mangoldt identity, 2.7e-15 |
| SP4 trace formula two-sided | residual 2.5e-8 (true zeros), **1.0e-7 on the object's own spectrum** | not posable (prime side unbuildable) | not posable (no $\Gamma$ term) |
| SP5 polarization (prime-side Weil Gram) | = zero-side to 2.7e-5; window margin $-1.9\text{e-}16$: **zero at machine precision** | known indefinite (e3c2); sourcing fails at $b_n$ | form not well-posed (no FE) |

Reading the columns: D-H passes every lattice/FE-side cell and fails every Euler-side cell; Beurling exactly dually; zeta alone fills the column. The conservation law (trojan-horse ledger) now has a per-component witness table produced by one run.

## 2. The three wrongness coordinates (what v0 honestly lacks)

1. **SP2 completeness IS RH.** The object's spectrum is "zeros visible on the carrier"; the D-H run proves the mechanism can be blind (its off-line pair leaves $|m|$ bounded below on the line, so the cokernel never opens there). For zeta, "the emergent spectrum is all of the spectrum" is precisely the claim to be proved. Finite resolution: the circle at circumference $L$ sees the line at grid $2\pi/L$; the data meter needs $n \lesssim e^{|s_{\min}|+\mathrm{supp}}$ (the two-meter law, paid explicitly in the truncation certificates).
2. **SP4 is two-sided only up to a finite-scale residual** (1.0e-7 at this window; the window is finite). The infinite-scale statement, the global trace formula, is equivalent to RH for all Hecke L-functions (Connes 1998, Theorem 5 in positive characteristic, asserted analogue over $\mathbb{Q}$; the repo holds the paper at `references/04_ncg_connes/Connes-1998-Trace-Formula-in-NCG-and-Zeros-of-Riemann-Zeta.pdf` and the verified reading note [`Connes-1998-Trace-Formula-NCG-Zeros.md`](../../docs/03_research/reading_notes/Connes-1998-Trace-Formula-NCG-Zeros.md)). v0's SP4 cell is the finite shadow of exactly that equivalence: C1's open half.
3. **SP5's margin is zero at resolution.** Zero-side bottom eigenvalue $-1.9\text{e-}16$ on $\lambda_{\max} = 1.27$; prime-side $-3.1\text{e-}7$ within the assembly resolution 3.0e-5. The window Weil form is PSD with an almost-null vector: the marginal-positivity coordinate (e3v; the e1y near-null ground state) reproduced inside the assembled object. The uniform $L \to \infty$ positivity is M4 (C2) and is not touched.

## 3. What the assembly adds to the map

- **The satisfiability matrix gains its first built row**: SP1 yes (finite, lattice-sourced, duality-carrying), SP2 part (spectrum emerges from integers; completeness = RH), SP3 yes at the diagonal (integer-exact), SP4 finite-residual, SP5 empirical-marginal. One-word wall: the limit.
- **The pole is cohomology in the object**: the unregularized descent diverges at the exact rate $e^{S/2}$ with lattice-extracted residue equal to the counting density (1 / 0 / 1.586): a weight-one $H^0$ obstruction the carrier sees, and the constraint that removes it is the codimension the pole conditions cut (property 7.5's shadow).
- **The bracket is now componentwise.** Previous rounds established D-H and Beurling as detectors for whole methods; v0 shows which SP cell each detector kills, in one table. Any future candidate object can be dropped into this pipeline and scored cell by cell.

## 4. Honest scope

Finite linear algebra plus certified-truncation quadrature; nothing here proves anything about RH. The emergent-zero mechanism at finite scale is |L| dipping on the line, dressed as a cokernel; its value is the sourcing discipline (all data from integers) and the assembly identities, not detection power. The scorecard's zeta column is conditional on nothing, but its "all cells green" reading stops at exactly the two joints where green cannot be bought at finite scale: completeness (C1) and the uniform margin (C2). Frontier verdict: UNMOVED, by design; the deliverable is the first assembled instance and its measured failure coordinates.

## 5. Handed forward

1. **The scaling ladder**: run the object at $L = 8, 10, 12, 14$ (grid refinement $2\pi/L$) and measure how the SP4 residual and the SP5 window margin move with scale. The M4 statement is exactly "the margin survives the ladder uniformly"; measuring its finite-scale decay law would put a number on the C2 gap from the object side.
2. **The D-H completeness contrast as a detector spec**: $|m|$ bounded below on the line at an off-line height is a computable "invisibility certificate". Formalizing the certificate (a lower bound on $|m_{DH}|$ over the landmark window from its coefficient lattice) would make the completeness failure a theorem about the object rather than a measurement.
3. **B2 (Lean)**: the interface as a structure with the five components as fields, this object's finite-scale instance as the inhabitant of the four-of-five fragment; the function-field instance inhabits all five (ToyModel direction).

# E2BE: the certification-cost theorem (backlog B3)

**Date**: 2026-08-25. **Status**: BUILDER round, executed; 14/14 checks full and `--quick` (13 s). **Code**: [`e2be_certification_cost.py`](e2be_certification_cost.py). **Data**: `e2be_certification_cost.npz` (tracked; full-mode run). **Provenance**: hardens LEARNINGS #180 (e2ao's handed-forward item 1); backlog spec in [`construction_backlog.md`](../../docs/03_research/construction_backlog.md) Family B. **Joint**: C2 (SP5): the finite-scale price of the uniform-margin clause, from the instrument side.

## 0. What this is

#180 measured that the e2ao prime-side assembly certifies the window margin only down to a floor crossed at $\sigma \approx 0.3$, and read off the price "$e^{\gamma_1^2\sigma^2}$ in assembly precision". This build makes both the floor and the price theorems about the instrument, with every constant explicit and machine-evaluable. Full statements and derivations are in the module docstring; the shape:

**T1 (instrument bound).** $|A(g_\omega) - Q(g_\omega)| \le \varepsilon(\sigma)$ with $\varepsilon$ an explicit four-clause budget: linear-interpolation error at the $\log n$ nodes (the dominant clause, computed from the closed-form autocorrelation $c(y) = \tfrac{\sqrt{\pi}\sigma}{2}e^{-y^2/4\sigma^2}[\cos\omega y + e^{-\sigma^2\omega^2}]$), the prime-sum tail (Gaussian-tail closed form via $\Lambda(n) \le \ln n$ and Rosser-Schoenfeld $\psi(x) < 1.03883x$), the support cut, and a $2\times10^{-11}$ lump provably covering the aliasing/domain/float clauses (each gated: the two aliasing clauses are $10^{-84636}$ and $10^{-542}$; Poisson summation and strip-analyticity of $\psi(\tfrac14 + \tfrac{it}{2})$ respectively).

**T2 (margin lower bound; free).** $\mathrm{margin}(\sigma) \ge 4\sqrt{\pi}\sigma e^{-\gamma_1^2\sigma^2}$, since the zero-side sum has positive terms and this is its first one ($\gamma_1 \le 14.1347253$).

**T3 (threshold and price).** If $4\sqrt{\pi}\sigma e^{-\gamma_1^2\sigma^2} \ge 2\varepsilon_R(\sigma)$ the assembly provably certifies the margin's sign and value to a factor of 2; the largest such $\sigma^*$ solves $\sigma^{*2} = \ln(2\sqrt{\pi}\sigma^*/\varepsilon_R)/\gamma_1^2$. Corollary: certification at scale $\sigma$ requires $\mathrm{digits} \ge \gamma_1^2\sigma^2/\ln 10 + O(\ln N, \ln\sigma)$: **#180's $e^{\gamma_1^2\sigma^2}$ price as a theorem about the instrument.**

## 1. The numbers

| clause | pre-registered | measured |
|---|---|---|
| T1 majorization over the 11 e2ao rungs | holds, looseness $\le 10^4$ | holds, looseness **3.3x-5.1x** |
| T1 on live reruns ($\sigma = 0.25$; $dx = 2\text{e-}3, 1\text{e-}3, 5\text{e-}4$) | each within its bound | $8.4\text{e-}7 \le 1.5\text{e-}6$; $1.3\text{e-}7 \le 3.6\text{e-}7$; $4.5\text{e-}8 \le 9.0\text{e-}8$ |
| $E_P$ honesty ($\sigma = 0.6$, $N$ vs $4N$) | within bound | $4.9\text{e-}19 \le 4.1\text{e-}18$ |
| T2 remainder at every rung | $\|m/\text{first} - 1\| \le R$ | worst $6.22\text{e-}5$ vs bound $6.35\text{e-}5$ |
| $\sigma^*$ (T3, proven-certifiable) | $\in [0.21, 0.29]$, $\le$ measured crossing | $\sigma^* = 0.2367$; crossing $0.30$; rung 0.2 covered with factor 41.5 |
| price demo at $\sigma = 0.5$ | dps-50 certifies; float64 cannot | certified to $9.8\text{e-}30$ vs required $3.2\text{e-}22$; float64 err $2.1\text{e-}5$ is 16 orders above; digits 21.4 vs $\gamma_1^2\sigma^2/\ln 10 = 21.7$ |

The bracket $[\sigma^*, \sigma_{\rm cross}] = [0.237, 0.30]$ pins the true certification threshold; its width is exactly the bound's factor-5 looseness ($\ln$-scale $0.01$-$0.03$ in $\sigma^2$).

## 2. What the theorem says structurally

1. **The error budget of the assembly is closed-form-understood.** Looseness 3-5x, not orders of magnitude: the instrument's floor is the $(dx^2/8)\sup|c''|$ interpolation clause at the $\log 2$ node, plus a Gaussian prime tail: nothing mysterious remains in the #180 floor. The measured flat $10^{-5}$-scale error and its mild $\sigma$-growth are both reproduced by the formula.
2. **The price is polynomial-vs-exponential, now provably.** Every instrument clause scales polynomially in the controls ($dx^2$, $e^{-c\ln^2 N}$ effective in $N$, digits linearly in working precision), while the target scales as $e^{-\gamma_1^2\sigma^2}$. So the digits-price $\gamma_1^2\sigma^2/\ln 10$ is not an artifact of a bad algorithm: within this assembly family, ANY parameter schedule pays it. That is the C2 finite-scale statement (#180's reading) upgraded from measurement to theorem-about-the-instrument: the uniform ($\sigma \to \infty$) margin statement M4 needs is exactly the statement no finite precision schedule reaches for free.
3. **The demo is constructive in both directions.** The same closed forms that prove the bound let a 50-digit assembly certify $\sigma = 0.5$ (8 orders of headroom), and the tracked #180 row shows float64 failing 16 orders short at the same rung: sufficiency and necessity exhibited on the same object.
4. **Scope.** Sufficiency ($\sigma \le \sigma^*$) is proven; necessity is measured (the e2ao crossing), so "iff" holds up to the factor-5 bracket. The margin law's single-mode, first-zero-dominated scope is unchanged from #180 (upper-bound family; not a statement about all of Weil positivity). The bound covers the $\omega \in [0, 20]$ scan of the e2ao instrument as built.

## 3. Lean-able residue (VERIFIER nuggets)

Three finite statements with no analytic number theory beyond citations: (i) the Gaussian-tail lemma chain behind $E_P$ (elementary inequalities on $\int u e^{u/2 - u^2/4\sigma^2}$); (ii) $\sum_{n\le N}\Lambda(n)/\sqrt{n} \le 2.07766\sqrt{N}$ by partial summation from $\psi(x) < 1.03883x$ (Rosser-Schoenfeld as the one citation); (iii) the linear-interpolation error bound with the closed-form $c''$. Each is a candidate for the VerifierQueue pattern (#188): statement-level targets with the npz as witness.

## 4. Handed forward

1. **B2d and B1 remain** in the hardening tier. B1 (the coupled SP4 ladder) now has a costing tool: T1's budget says which meter (dx, N, precision) must grow to chase the residual's floor downward.
2. **The bracket-narrowing residue**: the factor-5 looseness lives almost entirely in the per-node sup of $|c''|$; a signed-error (rather than sup) treatment at the $\log 2$ node alone would close most of the $[0.237, 0.30]$ bracket. Cheap, optional.
3. **The cross-instrument reading**: e2bd (#199) certified the completeness face with the same ball-arithmetic idioms; together the two hardening builds make the #179/#180 scorecard cells "theorem about the control" and "theorem about the instrument" respectively. The remaining measured-only cell of that bank is the SP4 residual floor, which is B1's target.

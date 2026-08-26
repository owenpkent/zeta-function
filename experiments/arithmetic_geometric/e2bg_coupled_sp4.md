# E2BG: the coupled SP4 ladder (backlog B1): the bank's closing build

**Date**: 2026-08-25. **Status**: BUILDER round, executed; 10/10 full (89 s) and 10/10 `--quick`; all three pre-registrations FIRED. **Code**: [`e2bg_coupled_sp4.py`](e2bg_coupled_sp4.py). **Data**: `e2bg_coupled_sp4.npz` (tracked; full run). **Provenance**: backlog B1, reclassified BANK MAINTENANCE by the #201 frame audit and run as the bank's closing build, with the audit's falsifier 2 as its P1, verbatim stakes.

## 0. The verdict first

**C1 does not bind inside the costed meters, and the bank closes FULLY PRICED.** Across the fully coupled ladder (test-function support, data depth, measured spectral ceiling all grown together: $(x_0, X) = (4, 7\times10^4), (6, 3\times10^5), (7, 10^6)$, each at its measured ceiling $T^*$), the object's two-sidedness residual is predicted by a purely internal instrument budget to factors of **2.66, 2.78, 1.32**: no unexplained defect remains. The #180 flat floor is now a THEOREM-GRADE budget line: the residual is the zero-displacement functional of the finite object, internally measurable, and nothing beyond it.

| rung $(x_0, X)$ | $T^*$ | resid_true | budget_true | resid_obj | budget_obj | ratio |
|---|---|---|---|---|---|---|
| $(4, 70000)$ | 197.3 | $4.6\times10^{-13}$ | $2.9\times10^{-12}$ | $2.2\times10^{-8}$ | $8.2\times10^{-9}$ | 2.66 |
| $(6, 300000)$ | 197.3 | (in budget) | | $3.3\times10^{-9}$ | $1.2\times10^{-9}$ | 2.78 |
| $(7, 10^6)$ | 197.3 | $1.2\times10^{-12}$ | (worst ratio 0.16) | $1.4\times10^{-10}$ | $1.1\times10^{-10}$ | 1.32 |

(Ratios are resid/budget; the budget carries NO oracle input: every clause is computed from the instrument's own data.)

## 1. The instrument (what it took to make the budget clean)

Exact-evaluation prime side (closed-form $\hat h(\log n)$, no interpolation), direct cosine transforms at the zeros, trapezoid archimedean integral INCLUDING $t = 0$, Richardson clauses on both quadrature axes (FFT padding and the $x$-grid), the density-tail Stieltjes fluctuation clause with a generous Backlund-grade zero-count constant, and, decisive for the object side, the **internal displacement meter**: each emergent zero's error is predicted by data-halving Richardson ($X$ vs $X/2$ positions, K1-clean) plus the polish's final-move self-estimate. Counts match the certified list 78/78 at every rung.

## 2. Four pilot catches, banked (the harness working as designed)

1. **The archimedean $t = 0$ bin.** The first pilot's P3 fired at ratio $3\times10^{10}$: a rect sum excluding $t = 0$ costs $\sim h(0)\mathrm{kern}(0)\,dt/2\pi \approx 2\times10^{-3}$ relative, with the measured signature ($x_0$-sensitive, $T$-insensitive). Fixed by trapezoid.
2. **The ceiling is real.** Fixed-$T$ rungs produced 86 detected vs 79 certified at $T = 200$ and 134 vs 202 at 400: the emergent spectrum's usable range is bounded, so the ladder couples to the measured $T^*(X)$.
3. **The pole's grid clause.** The second pilot's residual excess (16.6x at $x_0 = 7$) was the $x$-grid rect error on the pole integral ($5.2\times10^{-11}$, measured by grid halving): now a budget clause.
4. **Duplicate dips, and displacement is data-drift.** The detector doubles/quadruples dips at some zeros (broke the order-pairing at 195); deduping recovered the ceiling to 197. The pairing dev (0.010 at $\gamma_{77}$) against the polish self-estimate ($8\times10^{-6}$) proved the zero DISPLACEMENT at height is the finite object's data-drift, not polish error: hence the internal Richardson meter.

## 3. Findings beyond the verdict

- **The ceiling is DETECTOR-limited at these depths.** $T^*(X) = 197$ flat across $X = 7\times10^4 \to 10^6$ (14x), and the mismatch panel's data-axis sensitivity is exactly 0.0: at these depths the binding meter is the dip detector (threshold and median-window in `detect_zeros`), not the data. The #198 knee is deeper than $X = 10^6$ at this probe; growing $T^*$ is a detector-design problem before it is a data problem. (Recorded; not pursued: the bank is closed.)
- **The exchange rate along the ladder**: resid_obj $2.2\times10^{-8} \to 3.3\times10^{-9} \to 1.4\times10^{-10}$ (step ratios 0.15, 0.04): the widening test function pays fewer displaced-zero weights ($|h'|$ mass concentrates below the displacement region); the displacement clause tracks it, which is exactly why the budget stays predictive.
- **P2 FIRED**: the displacement clause dominates budget_obj at every rung (vs fluct/quad/rounding): the #180 floor's reading confirmed: the spectral meter is the binding axis of the glue at finite scale.

## 4. Honest scope

The verdict is about the costed meters: $x_0 \le 7$, $X \le 10^6$, $T^* \approx 197$, this detector, this probe. "C1 does not bind" means: within this instrument family, the object's trace-formula two-sidedness is fully accounted by internally-predictable finite-scale error, with nothing left over: the audit's falsifier 2 resolves to "the last measured-only cell becomes another priced ceiling," and the bank has no cells left that are not theorem-about-instrument or RH-equivalent. It does NOT mean C1 is closed: the infinite-scale two-sided trace formula remains the C1 joint (Connes's equivalence), untouched, exactly as the interface doc states. Frontier UNMOVED.

## 5. Handed forward (recorded, not queued: the bank is closed)

The detector-ceiling question (a dip detector whose range grows with data: prerequisite for any future deep-spectrum glue work); the displacement functional $D_h$ as a standing internal meter for any counting-side build; the four catches as budget clauses any sibling instrument should carry.

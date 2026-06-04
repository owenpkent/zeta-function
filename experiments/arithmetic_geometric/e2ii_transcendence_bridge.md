# 2II: the candidate-F bridge is weaker than hoped (brick 2)

> Companion for [`e2ii_transcendence_bridge.py`](e2ii_transcendence_bridge.py). Executes brick 2 of [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md): does Weil positivity carry a transcendence/independence condition on $\{\log p\}$ (candidate F), or is the available independence elementary / positivity insensitive to it? Run: `python -m experiments.arithmetic_geometric.e2ii_transcendence_bridge`.

## The question and the deflating fact

2FF (#45) bridged organ (b) (the two-clock period) to candidate F: the period cannot be a single number *because* $\{\log p\}$ is rationally independent. The synthesis flagged brick 2 as the highest-leverage move: if Weil positivity genuinely requires an *effective* (Baker-type) independence of $\{\log p\}$, the program connects to Diophantine approximation as a live field.

The deflating fact to confront first: the Q-linear independence of $\{\log p\}$ is **elementary**. $\sum a_i\log p_i = 0$ with $a_i\in\mathbb{Q}$ $\iff$ $\prod p_i^{a_i}=1$ $\iff$ all $a_i=0$, by unique factorization. So the qualitative incommensurability 2FF used is **free**, not a deep transcendence statement. Candidate F's deep version would need something stronger: an effective lower bound on $|\sum a_i\log p_i|$ (Baker), or independence together with the archimedean periods.

## Results

- **Part 1 (independence is elementary).** The smallest short integer combination $|\sum a_i\log p_i|$ (primes $\le 11$) shrinks with the coefficient bound — $0.0465$ ($|a_i|\le 1$), $0.0101$ ($\le 2$), $0.0019$ ($\le 3$) — but stays $> 0$, with a one-line proof (unique factorization). The qualitative independence (organ (b), "no single period") is free and **cannot** be candidate F's deep content.
- **Part 2 (effective gap vs the Weil margin).** Effective gaps reach $\approx 0.0013$ (6 primes, $|a_i|\le 2$). The Weil positivity margin for $\zeta$ (#34) is $0.035$, a factor $\sim 25$ **above** the gap scale. Positivity does not obviously live at the transcendence (Baker) scale.
- **Part 3 (controlled sensitivity).** Rebuilding the prime block with the sampling positions $\{\log n\}$ snapped to a commensurable grid degrades $\min\mathrm{eig}(M)$ ($+0.026 \to -0.39$ at grid $0.10$), **but no more than** an equal-RMS *incommensurable* random perturbation ($-0.33 \pm 0.34$, $n=12$): the commensurability z-score is $-0.20$ (and $-0.67$ at grid $0.20$), nowhere near the $-2$ that would signal resonance-sensitivity. The large control variance shows it is the displacement *magnitude*, not commensurability, that moves positivity. **Positivity is not specifically resonance-sensitive at reachable truncation.**

## Verdict

**Candidate F is a weaker bridge than hoped.** (1) The independence it can supply is elementary; (2) the Weil margin sits above the effective-gap scale; (3) forcing commensurability does not degrade positivity beyond an equal-magnitude incommensurable perturbation. So the 2FF organ-(b)$\leftrightarrow$F bridge connects organ (b) to a *free* fact and does **not** import the Baker/Diophantine machinery candidate F promised. The genuine discriminator remains the **Euler-product $H^2$** (2GG/#46), not the transcendence of $\{\log p\}$.

This refines, not contradicts, #45: the obstruction to a single period *is* the independence of $\{\log p\}$ (true), but that independence is elementary, so the bridge is real and shallow rather than deep. The net effect on the program is a consolidation: **the deep content concentrates on the H² / Euler-product side (organ (a)), away from the transcendence side.** A clean negative coordinate — it prunes a hoped-for import and sharpens where the work is.

## Honest scope

Part 1 is elementary/rigorous. Part 2 is a scale comparison (real effective gaps vs the #34 margin). Part 3 is a controlled numerical sensitivity test at reachable truncation, not a theorem. The verdict locates where candidate F lives; it is not a statement about RH. (Caveat on Part 2: the effective gaps shrink as more primes and larger coefficients are allowed, so "above the gap scale" is a statement about the reachable regime, not an asymptotic claim; but the margin being $O(1)$ while short-combo gaps are $O(10^{-3})$ is the honest reading that positivity is not poised at the resonance scale.)

## Pointers

- Parent: [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md) (brick 2), [`backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (candidate F).
- Refines: [`e2ff_two_clock_period.py`](e2ff_two_clock_period.py) (2FF / #45, the organ-(b)$\leftrightarrow$F bridge).
- The discriminator it points back to: [`e2gg_fundamental_class.py`](e2gg_fundamental_class.py) (2GG / #46, the Euler-product $H^2$).
- Findings leaned on: #34 (the Weil margin, stealth window), #45 (the bridge), #46 (the H² discriminator).

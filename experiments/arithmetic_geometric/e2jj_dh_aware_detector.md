# 2JJ: the D-H-aware detector — the stealth window is a target, not a wall (brick 3)

> Companion for [`e2jj_dh_aware_detector.py`](e2jj_dh_aware_detector.py). Executes brick 3 (the capstone) of [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md), closing the brainstorm's mistake (iii) loop ([`backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) §4). Run: `python -m experiments.arithmetic_geometric.e2jj_dh_aware_detector`.

## The reframe

The D-H discipline as usually stated ("if a method fires for D-H, discard it") is a sufficient safety filter but too blunt to *characterize* correctness. The brainstorm's mistake (iii): the correct object should *apply* to D-H and correctly output its **off-line** zeros, while outputting ζ's **on-line** zeros, from one mechanism. 2HH (#47) gave the exact handle: the duality-vs-polarization defect $D(\rho) = |(1-\rho)-\bar\rho| = |1-2\beta|$ is a fixed structural quantity that vanishes on the critical line and is nonzero exactly at off-line zeros. As a function of height, $D(\gamma)$ is the **D-H-aware detector**.

## Results

- **Part 1 (the detector locates the off-line zero).** On the actual zeros: ζ has $D(\gamma) \equiv 0$ (25 zeros to $T=90$, max $0$, all on the line). D-H has $D(\gamma)=0$ on its 35 on-line zeros (to $T=60$) and **spikes to $0.617$** at the off-line zero $\gamma\approx 85.7$ ($\beta\approx 0.8085$). The detector is D-H-aware: it does not fail to see D-H — it *locates* D-H's off-line obstruction and is flat for ζ.
- **Part 2 (the stealth window is a resolution cost).** Resolving a zero at height $\gamma$ via the non-circular prime-side reconstruction needs test functions of frequency $\sim\gamma$, hence primes up to $\sim e^{\gamma}$. For $\gamma=85.7$ that is $e^{85.7}\approx 1.6\times 10^{37}$ primes — unreachable. The reachable truncation $b\le 6$ resolves heights only up to $\log(b^2)\approx 3.58$, below even the first ζ zero at $14.13$. So the **exact** form (from zeros) sees the off-line zero for free, while the reachable reconstruction provably cannot. The #34 stealth window is this $e^{\gamma}$ resolution cost, **not** an intrinsic blindness of the Weil form to D-H.
- **Part 3 (the reframed discipline).** Old: "is the object silent on D-H?" New: "does it give each $L$ its **true** zero locus?" The exact Weil form / the defect $D(\gamma)$ passes the stronger test — D-H-aware (spikes at D-H's off-line zeros, flat for ζ). The cohomological reason ζ's $D(\gamma)\equiv 0$ is 2HH/2GG: on the line the FE-partner equals the conjugate (the cup product is a polarization); D-H's off-line zero is exactly where that fails.

## Verdict

The stealth window is a **target reframed, not a wall**. The exact Weil form is D-H-aware: the detector $D(\gamma)$ locates D-H's off-line zero at $85.7$ and is flat for ζ, and the non-circular reconstruction's blindness is a resolution cost ($e^{85.7}\approx 10^{37}$ primes), not an intrinsic failure to distinguish. So the D-H discipline upgrades from **D-H-excluded** to **D-H-aware**: the right object gives D-H its off-line zeros and ζ its on-line zeros from one mechanism (the cup-product-is-a-polarization criterion, 2HH). This closes the brainstorm's mistake (iii) loop.

## Honest scope

$D(\gamma)$ is computed from the actual zeros: a characterization / localization demonstration (like the FF anchors and 2HH), circular as an RH proof. The value is the reframe — it shows the exact object is D-H-aware and that the stealth window is a resolution cost (a quantitative, non-circular argument), **not** that the non-circular reconstruction can be pushed to see $\gamma=85.7$ (it provably cannot, at $e^{85.7}$ primes). Nothing here proves RH; it upgrades the discipline and dissolves the "wall" reading of the stealth window.

## Pointers

- Parent: [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md) (brick 3), [`backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) §4 mistake (iii).
- Builds on: [`e2hh_cup_is_polarization.py`](e2hh_cup_is_polarization.py) (2HH / #47, the defect handle), [`e2gg_fundamental_class.py`](e2gg_fundamental_class.py) (2GG / #46).
- Findings leaned on: #34 (the stealth window, now reframed), #47 (the defect), the D-H discipline (now upgraded).

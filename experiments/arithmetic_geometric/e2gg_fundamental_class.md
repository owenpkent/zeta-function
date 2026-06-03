# 2GG: organ (a), the H² fundamental class and the Poincaré-duality trace map

> Companion for [`e2gg_fundamental_class.py`](e2gg_fundamental_class.py). Attacks organ (a) of milestone M4, named by probe B (2EE / #44): the fundamental class $H^2$ and the trace map $H^1\otimes H^1\to H^2 = \text{unit}$. Run: `python -m experiments.arithmetic_geometric.e2gg_fundamental_class`.

## The decisive structural point

The functional equation $\xi(s)=\xi(1-s)$, with $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, **is** the Poincaré duality $H^1\times H^1\to H^2$: it pairs a zero $\rho$ with its partner $1-\rho$, and the factor $s(s-1)$ carries the Deninger grading: $s=0$ is $H^0$ (weight 0), $s=1$ is $H^2$ (the pole, weight 2 = Tate twist, the **fundamental class**), and the nontrivial zeros are $H^1$ (weight 1, where RH lives). The duality $s\leftrightarrow 1-s$ swaps $H^0\leftrightarrow H^2$ and preserves $H^1$.

But **Davenport-Heilbronn also has a functional equation** (that is the defining property of the wrong-approach detector: "functional equation, no Euler product"). So the duality pairing itself is buildable for D-H. What D-H lacks is the **nonzero fundamental class**: $\zeta$ has a pole at $s=1$ (residue 1, an avatar of the Euler-product divergence $\prod_p(1-1/p)^{-1}\to\infty$), while D-H is entire (residue 0). A Poincaré duality whose trace lands in a zero fundamental class is not a polarization. So organ (a) splits, and only the second half is the obstruction:

- the duality pairing (the FE): **buildable for D-H** — not the gap;
- the fundamental class $H^2$ (the Euler-product pole): **absent for D-H** — this is organ (a), and the K2 face.

## Results

### Part 1: function-field anchor (real)

For curves $C/\mathbb{F}_q$, the cup product on $H^1$ (dim $2g$) into $H^2 = \mathbb{Q}(-1)$ is verified to be a **perfect** (nondegenerate, alternating) Poincaré pairing for every curve in the family; Frobenius is a **similitude of scale $q$** ($\Phi^{\top}J\Phi = qJ$, the polarization compatibility); and the induced Riemann polarization is definite exactly when $|\alpha_i|=\sqrt q$ (RH). So over $\mathbb{F}_q$ **both** organ-(a) ingredients are present: a perfect duality and a nonzero 1-dim fundamental class, and the polarization is definite at RH.

| | cup perfect | similitude $q$ | polariz $\Leftrightarrow$ RH |
|---|---|---|---|
| all curves (genus 1, 2) | yes | yes | yes |

### Part 2: the arithmetic separation (the decisive contrast)

- (i) $\zeta$ functional equation $\xi(s)=\xi(1-s)$ (the **duality**): holds to $\max|\xi(s)-\xi(1-s)| = 5\times 10^{-36}$.
- (ii) $\zeta$ residue at $s=1$ (the **fundamental class** $H^2$): $= 1.000000$ (nonzero, the Euler-product pole).
- (iii) D-H residue at $s=1$: $= 9.2\times 10^{-11} \approx 0$ (D-H is entire, **no fundamental class**) — yet D-H **has its own functional equation** (the duality is buildable for it).

**Decisive contrast: the fundamental class is 1 for $\zeta$ and 0 for D-H.** The duality (FE) does not distinguish them; the fundamental class (the Euler-product pole) does. Organ (a)'s obstruction is the nonzero unit, not the pairing. In cohomological language: D-H has $H^1\times H^1\to H^2$ but $H^2 = 0$, so its duality is not a polarization. This is the cleanest cohomological statement of the D-H discipline the project has produced.

### Part 3: the named gap

Present over $\mathrm{Spec}(\mathbb{Z})$: the FE-symmetry (the duality, present even for D-H) and the rank-1 Euler-pole fundamental class (2EE, nonzero only for Euler $L$). Missing: a genuine **geometric** Poincaré duality realizing $H^1\otimes H^1\to H^2$ as a **perfect cup product** into that 1-dim Euler-pole fundamental class, on the **infinite-dimensional** arithmetic $H^1$ (the prismatic Poincaré duality, candidate A's dependency (i)). Its induced polarization positivity is RH. So organ (a) is: *make the FE a geometric cup product into the Euler-pole $H^2$, perfectly, on the infinite-dim $H^1$* — with the Deninger $H^0/H^1/H^2$ grading ($s=0$ / zeros / $s=1$ pole) as the target shape.

## Why this is a coordinate

It separates the two things "Poincaré duality" was bundling: the **pairing** (the FE, which even the counterexample has) and the **fundamental class** (the Euler-product pole, which only an Euler product supplies). This both sharpens organ (a) (the obstruction is the unit, not the pairing) and gives the D-H discipline its cleanest cohomological form: D-H fails not for lack of a duality but for lack of a nonzero $H^2$. It also confirms and grades probe B's rank-1 ample direction: that direction is the $H^2$ at $s=1$ in the Deninger grading.

## Honest scope

Part 1 (FF cup-product perfectness, similitude, polarization $\Leftrightarrow$ RH) is rigorous (the crystalline/Weil picture, reproducing 2T/2G/2DD in duality language). The residue contrast (Part 2) is a clean decisive computation. The $H^0/H^1/H^2$ grading and the "FE = Poincaré duality, pole = fundamental class" reading are the Deninger structural picture, not a constructed arithmetic cohomology; this proves nothing about RH. No new theorem; a sharpening coordinate.

## Pointers

- Parent: [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (organ (a); candidate A).
- Builds on: [`e2ee_archimedean_gluing.py`](e2ee_archimedean_gluing.py) (2EE / #44, the rank-1 $H^2$ shadow), [`e2dd_prismatic_cup_room.py`](e2dd_prismatic_cup_room.py) (2DD / #43, the cup product), [`e2t_rosati_positivity.py`](e2t_rosati_positivity.py) (2T).
- Findings leaned on: #44 (the two organs), #21 (the Hodge-index signature), the D-H discipline.

# 2HH: organ (a) made exact — RH ⟺ the cup product is a polarization (brick 1)

> Companion for [`e2hh_cup_is_polarization.py`](e2hh_cup_is_polarization.py). Executes brick 1 of [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md): organ (a)'s prismatic Poincaré duality, and the question "is perfectness or positivity the gap?" Run: `python -m experiments.arithmetic_geometric.e2hh_cup_is_polarization`.

## The characterization

A polarization is a duality compatible with a positive Hermitian structure (Hodge-Riemann). On the arithmetic $H^1$ the two pairings are:

- the **cup product / Poincaré duality** (from the functional equation): pairs a zero $\rho$ with its FE-partner $1-\rho$;
- the **Hermitian polarization** (the Hodge star / complex conjugation): pairs $\rho$ with its conjugate $\bar\rho$.

These coincide for every zero iff $1-\rho = \bar\rho$ iff $\mathrm{Re}(\rho)=1/2$. Hence

$$\text{RH} \iff \text{the cup product (Poincaré duality) is a polarization} \iff 1-\rho = \bar\rho \text{ for every zero}.$$

The cup product (the FE-pairing) is a **perfect** (nondegenerate) duality for any $L$ with a functional equation, **including D-H**. What fails for D-H is not perfectness but **positivity**: at an off-line zero the FE-partner and the conjugate are different points, displaced by $|1-2\beta| > 0$.

## Results

- **(1) ζ:** the first 10 zeros all have $\beta = 1/2$ exactly, so the duality-vs-polarization defect $|1-2\beta| = 0$. The cup product **is** the polarization (perfect and positive).
- **(2) D-H:** (a) its functional-equation residual is $6\times 10^{-30}$ — D-H **has** the duality, so the cup product is a **perfect** pairing for D-H too; perfectness is not the discriminator. (b) Its off-line zero $\rho \approx 0.8085 + 85.699\,i$ (verified, $|L(\rho)| = 1.1\times 10^{-5}$) has FE-partner $1-\rho \approx 0.1915 - 85.699\,i$, **different** from the conjugate $\bar\rho \approx 0.8085 - 85.699\,i$, displaced by $|1-2\beta| \approx 0.617$. The cup product is **not** a polarization for D-H: positivity fails while perfectness holds.
- **(3) Truncation reading.** The defect $0.617$ is a **fixed structural** quantity, not a reconstruction-floor quantity: unlike the stealth window (#34) it does not shrink with truncation. It is visible at any resolution that includes the off-line zero. The honest catch: evaluating it needs the zero location (circular w.r.t. RH) or the non-circular reconstruction (back under the stealth floor). So the **characterization** is exact and stealth-free; its **non-circular evaluation** is still the analytic gap.

## Verdict (brick 1's question answered)

**Positivity, not perfectness, is the gap.** The FE gives a perfect cup-product duality for both ζ and D-H; the cup product is a *polarization* (FE-partner = conjugate) for ζ and not for D-H. So organ (a)'s open content is precisely "the FE-duality is Hodge-Riemann positive," i.e. RH, on the infinite-dim $H^1$. This imports the standard-conjecture frame (a polarization = a positive duality), the same power-importing move 08A endorsed, now on the $H^2$/duality face.

**Combined with 2GG (#46):** D-H fails twice over, both saying its duality is not a polarization — from the unit side (no nonzero $H^2$; D-H is entire) and from the positivity side (FE-partner ≠ conjugate at off-line zeros). Organ (a) = a perfect cup product into the *nonzero* Euler-pole $H^2$ that is *also* a polarization. Perfectness and the duality are free (the FE); the unit (Euler pole) and the positivity (Re = 1/2) are the content.

## Lean target

[`lean/ZetaRH/PrismaticCohomology.lean`](../../lean/ZetaRH/PrismaticCohomology.lean) gained typed placeholder targets in the existing Phase-1 idiom: `cup_product`, `fundamental_class`, `Q3a_fundamental_class_nonzero` (the unit/K2 face), `Q3b_cup_is_polarization_iff_RH` (the positivity face). **Not compiled in this session** (no elan/lake toolchain available here); they mirror the known-green `Unit`/`True := by sorry` pattern of Q1-Q5 and are to be verified on the owner's build.

## Honest scope

The characterization (RH ⟺ cup is a polarization ⟺ $1-\rho=\bar\rho$) is an exact, elementary restatement; its value is importing the Hodge-Riemann / standard-conjecture frame on the $H^2$/duality face. The demonstration uses actual zeros (a characterization, like the FF anchors, not a non-circular certificate) and proves nothing new about RH. A sharpening coordinate that answers brick 1 (positivity is the gap) and delimits the stealth-window-free content.

## Pointers

- Parent: [`docs/03_research/state_of_candidate_ABF.md`](../../docs/03_research/state_of_candidate_ABF.md) (brick 1), [`backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (candidate A, organ (a)).
- Builds on: [`e2gg_fundamental_class.py`](e2gg_fundamental_class.py) (2GG / #46, the duality vs the unit), [`e2ee_archimedean_gluing.py`](e2ee_archimedean_gluing.py) (2EE / #44, the rank-1 $H^2$).
- Findings leaned on: #34 (stealth window), #46 (the fundamental class), the D-H discipline.

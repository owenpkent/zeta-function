# Euler-product control on the D-H gap-collapse attribution (#169 adversarial follow-up)

> **VERDICT: THE EULER-PRODUCT ATTRIBUTION IS FALSIFIED.** `chi3_L` and
> `chi4_L` (real primitive Dirichlet L-functions with a genuine Euler product
> AND the same functional-equation template as zeta and D-H) collapse by the
> **same 4-6 orders of magnitude** as D-H, at the same `lambda` cells, in the
> IDENTICAL construction. At several cells chi3/chi4 collapse *more* than
> D-H. Section 5 of `_e1s_dh_undercount.md` names "Euler-product-sourced" as
> the driving structural cause of D-H's `gap_even` collapse; this control
> shows the collapse also happens to functions that possess an Euler product,
> so "has an Euler product" is not the discriminator. The gap-collapse
> phenomenon itself survives (it is real, reproducible, N-robust: confirmed
> at `N=8` and `N=12`), but it discriminates **zeta from everything else
> tested** (D-H, chi3, chi4 alike), not "Euler-product functions from
> non-Euler-product functions." This downgrades `source_classification` in
> the parent dossier's Verdict table and weakens, but does not eliminate,
> the discriminating value claimed there.

## 0. Pre-registered prediction (written before any control number was computed)

- **If the Euler-product attribution is CORRECT**: chi3/chi4 `gap_even`
  should track Zoff (order 1-10, growing with `lambda`) and NOT collapse.
- **If chi3/chi4 ALSO collapse**: the Euler attribution is FALSIFIED, and the
  collapse is driven by something else -- candidates named in advance: the
  sign-changing coefficient comb, the (small) conductor, the specific
  archimedean-density/coefficient-stream MATCH, or a general non-zeta
  property unrelated to the Euler product.

Result below matches the second branch. Falsified as pre-registered.

## 1. Reproduction check

Reused `build_float` / `operator_spectrum` / `make_streams` / `ZETA_CFG` /
`DH_CFG` from `experiments/spectral/e1k_dh_dlog_testbed.py` exactly, at
`N = 8`, `mp.mp.dps = 25` (matching the parent dossier's stated precision
exactly -- an initial run without setting `dps` gave DH values 2-30x off at
the smallest-gap cells, which is itself consistent with the parent dossier's
own conditioning-fragility finding at those cells; setting `dps = 25`
resolved this to a clean match). "Zoff" is `ZETA_CFG` dens with
`use_pole=False` per `e1s_rank_one_interlacing.py:cell()`, not
`ZETA_CFG["use_pole"]=True`; matching this was required.

| lam | Zoff gap_even (this run) | dossier Zoff | DH gap_even (this run) | dossier DH |
|---|---|---|---|---|
| 2.0 | 2.832 | 2.83 | 1.621 | 1.62 |
| 2.5 | 3.900 | 3.90 | 1.298 | 1.30 |
| 3.0 | 4.822 | 4.82 | 9.17e-2 | 9.17e-2 |
| 3.3 | 5.335 | 5.33 | 7.42e-3 | 7.42e-3 |
| 3.6 | 5.836 | 5.84 | 3.08e-4 | 3.08e-4 |
| 4.0 | 6.486 | 6.49 | 1.19e-5 | 1.19e-5 |
| 4.5 | 7.255 | 7.25 | 1.07e-5 | 1.07e-5 |
| 5.0 | 7.985 | 7.98 | 1.38e-4 | 1.38e-4 |
| 5.5 | 8.682 | 8.68 | 5.37e-5 | 5.37e-5 |

**Reproduction confirmed to 3-4 significant figures across every cell.**
Measuring the same quantity as the parent dossier.

## 2. Control construction

`chi3_L` (conductor 3, odd) and `chi4_L` (conductor 4, odd) from
`experiments/_shared/dirichlet_l.py`. Both are real primitive Dirichlet
characters: genuine Euler product, genuine functional equation, GRH believed
(not known false, unlike D-H).

**Archimedean density.** Derived directly from the same completed-L-function
template already used for both existing twins, `Lambda(s,chi) = (q/pi)^{(s+a)/2}
Gamma((s+a)/2) L(s,chi)` (this is literally
`DirichletL.functional_equation_residual`'s own formula): `dens_a = (2a+1)/4`,
`dens_b = log(q/pi)`. This is a two-point-verified, non-cherry-picked formula:
it exactly reproduces `ZETA_CFG` (`q=1, a=0` -> `dens_a=0.25, dens_b=-log(pi)`)
and `DH_CFG` (`q=5, a=1` -> `dens_a=0.75, dens_b=log(5/pi)`) before being
applied to chi3 (`q=3, a=1` -> `dens_a=0.75, dens_b=log(3/pi)`) and chi4
(`q=4, a=1` -> `dens_a=0.75, dens_b=log(4/pi)`).

**Coefficient stream.** Identical Dirichlet log-derivative recursion
(`sum_{d|n} Lambda(d) c_{n/d} = c_n log n`) already used for zeta and D-H, with
`c_n = chi(n)` taken directly from `DirichletL.dirichlet_coefficient`. Verified
structurally: the resulting `Lambda` is supported ONLY on prime powers for
both chi3 and chi4 (checked up to `n <= 40`, zero non-prime-power entries in
either support), confirming these are genuinely sparse, Euler-product-typical
streams, unlike D-H's dense, all-`n` stream.

**Construction sanity check.** `build_float` + `operator_spectrum` at
`N=10, lam=2.8` recovers chi3's and chi4's own known low zeros
(`chi3_L.zeros`, `chi4_L.zeros`) to `1e-4` to `1e-2`: chi3 `8.0397 -> 8.0396`,
`11.2492 -> 11.2492`; chi4 `6.0209 -> 6.0207`, `10.2438 -> 10.2417`,
`12.9881 -> 12.9788`. The construction is genuinely realizing chi3/chi4, not
producing garbage.

## 3. Control results: gap_even across identical cells (N=8, dps=25)

| lam | Zoff gap | DH gap | chi3 gap | chi4 gap | Zoff/DH | Zoff/chi3 | Zoff/chi4 |
|---|---|---|---|---|---|---|---|
| 2.0 | 2.832e+00 | 1.621e+00 | 6.420e-01 | 1.473e+00 | 1.75e+00 | 4.41e+00 | 1.92e+00 |
| 2.5 | 3.900e+00 | 1.298e+00 | 6.595e-03 | 3.255e-01 | 3.00e+00 | 5.91e+02 | 1.20e+01 |
| 3.0 | 4.822e+00 | 9.170e-02 | 9.824e-05 | 3.429e-03 | 5.26e+01 | 4.91e+04 | 1.41e+03 |
| 3.3 | 5.335e+00 | 7.423e-03 | 6.525e-05 | 2.496e-04 | 7.19e+02 | 8.18e+04 | 2.14e+04 |
| 3.6 | 5.836e+00 | 3.080e-04 | 1.806e-05 | 5.466e-05 | 1.89e+04 | 3.23e+05 | 1.07e+05 |
| 4.0 | 6.486e+00 | 1.188e-05 | 7.918e-07 | 2.389e-06 | 5.46e+05 | 8.19e+06 | 2.71e+06 |
| 4.5 | 7.255e+00 | 1.075e-05 | 1.983e-06 | 5.372e-06 | 6.75e+05 | 3.66e+06 | 1.35e+06 |
| 5.0 | 7.985e+00 | 1.380e-04 | 1.667e-04 | 1.216e-04 | 5.79e+04 | 4.79e+04 | 6.57e+04 |
| 5.5 | 8.682e+00 | 5.366e-05 | 1.373e-05 | 3.123e-05 | 1.62e+05 | 6.32e+05 | 2.78e+05 |

**chi3 and chi4 collapse by the same 4-6 orders of magnitude as D-H, at the
same cells, and at `lam in {3.0, 3.3, 4.0, 4.5}` collapse MORE severely than
D-H** (e.g. `lam=4.0`: DH ratio `5.46e5`, chi3 ratio `8.19e6`, chi4 ratio
`2.71e6`). Only Zoff stays smooth and monotone-growing (`2.83 -> 8.68`)
across the entire range; D-H, chi3, and chi4 all show the same qualitative
signature -- near-degenerate collapse with non-monotone wobble -- despite two
of the three having a genuine Euler product.

**N-robustness check.** Repeated at `N=12` for `lam in {3.3, 4.0}`:
`lam=3.3`: Zoff=5.338, DH=4.637e-3, chi3=6.277e-5, chi4=2.445e-4.
`lam=4.0`: Zoff=6.488, DH=5.004e-6, chi3=7.660e-7, chi4=2.174e-6.
Same qualitative pattern; not an `N=8` accident.

## 4. Honest split: gap collapse vs. undercount integer vs. attribution

Three separate claims need to be separated, since the parent dossier's own
concession (the `lam=4.5, N=20` cell resolves to the exact target count once
`dps` is pushed to `40`) only speaks to one of them:

1. **The raw numerical fact that D-H's `gap_even` collapses relative to
   Zoff's**: real, hp-confirmed (`mpmath` dps=30 dense linear algebra),
   N-robust. This part of the dossier's finding is not touched by this
   control and stands.
2. **The exact undercount integer at `dps=25`**: conceded by the dossier
   itself to be precision-fragile at the most extreme cell tested
   (`lam=4.5`). This control did not re-test that specific claim but has no
   reason to doubt the dossier's own concession.
3. **"Euler-product-sourced" as the causal attribution of (1)**: FALSIFIED by
   this control. The collapse is not specific to functions lacking an Euler
   product; it happens (as badly or worse) to functions that have one. The
   correct read is closer to "zeta-specific" than "Euler-product-specific":
   something about this particular truncated-Weil-form construction is
   uniquely well-behaved for zeta (`q=1`, its own archimedean normalization)
   and not for any of the three non-zeta functions tested, GRH-believed or
   not.

**The MECHANISM headline overclaims on exactly this axis.** The dossier's
`source_classification: Euler-product-sourced` and its framing of
`discriminating_value` as a "D-H-vs-zeta discriminator" both need
correction: the observed discriminator is zeta-vs-everything-else, which is a
weaker and more concerning reading, since it means the gap-collapse signal
does not correlate with whether the function's own RH-analogue is TRUE
(chi3/chi4, GRH-believed) or FALSE (D-H, RH-analogue known false) -- it fires
identically for both. A signal that cannot distinguish "believed-true"
Selberg-class members from a "known-false" counterexample is not carrying
verified RH-relevant information regardless of what it "measures" internally.

## 5. Scope

- Correct split (revised from the task's suggested framing): gap collapse
  as a raw phenomenon = real and construction-robust; undercount integer =
  conditioning-fragile per the dossier's own concession; Euler-product
  CAUSAL ATTRIBUTION = false, replaced by "zeta-specific, mechanism
  unidentified."
- Does not prove or disprove anything about RH; this is a discipline check
  on one dossier's causal claim, per the D-H/adversarial protocol.
- All numbers freshly computed in this session; reproduction against the
  parent dossier's own table matches to 3-4 significant figures (Section 1),
  which is the confirmation that this control is measuring the same
  quantity, not a different one that happens to also collapse.

## Reproduce

`experiments/spectral/_evidence/e1s_euler_control.py` (standalone, imports
`build_float` / `make_streams` / `ZETA_CFG` / `DH_CFG` / `operator_spectrum`
from `e1k_dh_dlog_testbed.py` and `chi3_L` / `chi4_L` from
`experiments/_shared/dirichlet_l.py` read-only; no tracked `.npz` touched):

```
python -m experiments.spectral._evidence.e1s_euler_control
```

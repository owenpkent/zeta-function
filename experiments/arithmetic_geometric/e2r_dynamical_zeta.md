# 2R: the Ruelle dynamical-zeta realization of `Gamma_S^2`

> Experiment [e2r_dynamical_zeta.py](e2r_dynamical_zeta.py). Direction 8 / the
> product surface; continues [2Q](e2q_frobenius_bidegree.md). 2Q pinned the missing
> arithmetic Frobenius correspondence `Gamma_S` to a place-dependent bidegree
> `(1, p)` and pinned its regularized self-intersection `Gamma_S^2` to the von
> Mangoldt prime side (the Direction 4.6 determinant). That was an abstract
> specification. 2R makes it CONCRETE on the dynamical side, and confirms the
> Davenport-Heilbronn control has no such object.

## The dynamical picture

In Deninger's program (and the Morishita bridge [arXiv:2508.15971], which matches
closed orbits to primes), the arithmetic flow `Phi_t` has primitive closed orbits
`gamma_p`, one per prime, of LENGTH `l(gamma_p) = log p`. These lengths are exactly
2Q's place-weights `{log p}`. The Ruelle dynamical zeta of such a flow is

```
zeta_Ruelle(s) = prod_p (1 - e^{-s l(gamma_p)})^{-1} = prod_p (1 - p^{-s})^{-1}
               = zeta(s)        (Re s > 1, the Euler product),
```

and its logarithmic derivative is the flow's regularized self-pairing -- the
Lefschetz / `Gamma_S^2` object:

```
-zeta'/zeta(s) = sum_p sum_{k>=1} (log p) p^{-ks} = sum_n Lambda(n) n^{-s}.
```

So 2Q's abstract `Gamma_S^2 = reg-sum_p (log p)(...)` IS `-zeta'/zeta`, realized as
the log-derivative of a dynamical zeta whose primitive-orbit-length spectrum is
`{log p}`. The local factor at `p` (orbit length `log p`) is the Euler factor
`(1 - p^{-s})^{-1}` -- the geometric content of 2Q's `(1, p)` bidegree.

## Results (all at `s = 2`, prec 30)

| verification | outcome |
|---|---|
| dynamical-zeta product `prod_{p<=P}(1-p^{-s})^{-1}` → `zeta(s)` | `|err|` 5.0e-2 → 3.5e-5 as `P: 10 → 5000` (orbit lengths `{log p}` reproduce zeta) |
| `sum_{n<=N} Lambda(n) n^{-s}` → `-zeta'/zeta(s) = 0.56996099` | `|err|` 1.0e-1 → 2.0e-4 as `N: 10 → 5000` (the `Gamma_S^2` realization) |
| D-H `Lambda_DH` support (`n <= 60`) | ON prime powers `Σ|Λ_DH| = 36.94`; **OFF prime powers `37.42`**, first nonzero off-pp at `n = 6` |

The first two confirm the dynamical-zeta object's data is exactly `Gamma_S^2`. The
third is the control: for D-H the log-derivative coefficients `Lambda_DH` (from
`-L_DH'/L_DH = sum_n Lambda_DH(n) n^{-s}`) carry as much mass OFF prime powers as on
them, first leaking at `n = 6` -- matching the 3M delocalization fingerprint (#20).
So D-H has NO primitive-orbit-length spectrum `{log p}`: the dynamical flow /
dynamical-zeta representation does not exist for it. This is the dynamical-language
form of 2Q's sharper K2 (a `(1, p)` local bidegree is the Euler factor; no Euler
product ⇒ no local bidegrees ⇒ no flow).

## What this is, and is not

- **It is** the concrete realization of 2Q's pinned `Gamma_S^2`: the orbit-length
  spectrum `= {log p} =` 2Q's place-weights, and the dynamical-zeta log-derivative
  `= -zeta'/zeta =` the prime side `= Gamma_S^2`. This makes concrete the half of
  the Morishita Deninger ↔ Connes-Consani bridge that Deninger supplies (the flow
  with closed orbits ↔ primes).
- **It is not** a new route to RH. The Euler-product / `-zeta'/zeta` identities are
  classical; the value is the structural identification and the D-H non-existence,
  not a positivity or a proof. It does NOT build the product surface, the leafwise
  prismatic cohomology `H^*_{F,pr}`, finiteness/trace-class, or the index theorem
  (Directions 4 and 8 remain open). The dynamical zeta gives the SPECTRUM and the
  self-pairing of `Gamma_S`, not the SIGNATURE that RH needs.

## The gap this sharpens

2R supplies the orbit-length data of the flow `Phi_t`; what is still missing is the
COHOMOLOGY the flow acts on, on which `det_zeta(s - Phi_t)` would be a genuine
regularized determinant and on which a Hodge-index SIGNATURE could be proved. The
next computable rung is Direction 4.6 proper: a leafwise prismatic `H^*_{F,pr}` with
a trace formula whose regularized determinant equals this dynamical zeta. 2R fixes
its target (orbit lengths `{log p}`, self-pairing `-zeta'/zeta`); D-H fixes the
control (no such spectrum).

## Connections

- 2Q ([e2q](e2q_frobenius_bidegree.md)): pins `Gamma_S^2` abstractly; 2R realizes it dynamically.
- 3M ([e3m](../positivity/e3m_place_type_balance.md), #20): the von Mangoldt delocalization that 2R reads as "no closed-orbit spectrum."
- 2K ([2K](2K_spec_z_squared_dictionary.md)): the dictionary; `Gamma_S^2` is the prime block `P_fin`.
- Direction 4 ([04_prismatic_foliation.md](../../docs/03_research/research_directions/04_prismatic_foliation.md)): 4.6 is the cohomological home for this dynamical zeta.
- Morishita bridge (arXiv:2508.15971): closed orbits ↔ primes, the Deninger half made concrete here.

## Outputs

- `e2r_dynamical_zeta.npz`: Euler-product + `-z'/z` convergence data; zeta/D-H von Mangoldt supports.
- `e2r_dynamical_zeta.png`: both realizations converging; zeta (clean `{log p}`) vs D-H (delocalized) support.

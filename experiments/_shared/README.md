# Shared experiment infrastructure

Phase 0 of the [proof-architectures plan](../PROOF_ARCHITECTURES_PLAN.md). Provides a uniform `LFunction` interface so every architecture (positivity, spectral, zero-free, arithmetic-geometric) can be run against $\zeta$ and against the Davenport-Heilbronn control with identical code paths.

## Modules

| File | Purpose |
|---|---|
| [`lfunction.py`](lfunction.py) | Abstract `LFunction` base class. Defines `evaluate(s)`, `zeros(T_max, prec)`, optional `dirichlet_coefficient(n)`. Also exports `li_coefficients(L, n_max)` which works on any `LFunction`. |
| [`zeta.py`](zeta.py) | `ZetaLFunction`: Riemann zeta wrapping `mp.zeta` and `mp.zetazero`, with disk caching of high-precision zero lists. |
| [`davenport_heilbronn.py`](davenport_heilbronn.py) | `DavenportHeilbronn`: 1936 construction with period-5 Dirichlet coefficients $(1, \kappa, -\kappa, -1, 0)$ where $\kappa = (\sqrt{10 - 2\sqrt 5} - 2)/(\sqrt 5 - 1) \approx 0.2841$. Functional equation but no Euler product. Off-line zeros known. |
| [`smoke_test.py`](smoke_test.py) | Phase 0 regression suite: 5 tests covering zeta evaluation/zeros, D-H Dirichlet/Hurwitz agreement, D-H functional equation, and D-H off-line zero discovery. |

## The Davenport-Heilbronn discipline

The Davenport-Heilbronn L-function is the **wrong-approach detector** for the entire project. It has the analytic structure of an L-function (Dirichlet series, functional equation) but is known to have zeros off the critical line. The first off-line zero pair is at $\rho \approx 0.8085 + 85.699\,i$ (and its conjugate).

Any RH-style method in Architectures 1, 3, or 4 must distinguish $\zeta$ from D-H:

- An operator (Arch 1) whose spectrum would "give" D-H zeros on the line is structurally insufficient.
- A positivity method (Arch 3) that finds $Q(f) \geq 0$ or $\lambda_n \geq 0$ for D-H is wrong, because D-H violates these.
- A zero-free-region method (Arch 4) that extends the D-H zero-free region to the critical line is wrong.

Architecture 2 sits outside this discipline because the arithmetic-geometric construction is intended to be specific to the Euler-product / functional-equation structure that D-H lacks.

## Smoke test

Run it from the repo root:

```
python -m experiments._shared.smoke_test
```

All 5 tests should pass. The first run computes and caches zeros (a few seconds for zeta to $T = 30$, about a minute for D-H to $T = 100$ at $\geq 0.5$ scan step). Subsequent runs use the cache in `_cache/`.

## Cache invalidation

If you change zero-finding logic in `zeta.py` or `davenport_heilbronn.py`, delete `_cache/` to force recomputation. The cache key includes `(T_max, prec, scan_step)` so different parameters produce different cache files automatically.

# THH(Z) and the von Mangoldt sum: Direction 10A.ii, first pass

Companion writeup to [`e_thh_vonmangoldt.py`](e_thh_vonmangoldt.py). This is the THH-side mirror of LEARNINGS #26 and the first concrete attempt at the Direction 10A checkpoint (docs/03_research/research_directions/[10A_thh_vonmangoldt_checkpoint.md](../../docs/03_research/research_directions/10A_thh_vonmangoldt_checkpoint.md)).

## The question

Direction 10 claims that $\mathrm{THH}(\mathbb{Z})$, with its $S^1$-action and cyclotomic Frobenii $\{\varphi_p\}$, is the single object carrying all the commensurable scales $\{\log p\}$ at once (the thing LEARNINGS #25 proved a single mod-$p$ Frobenius cannot do). The decisive checkpoint: does an $S^1$-equivariant invariant of $\mathrm{THH}(\mathbb{Z})$ reproduce the von Mangoldt sum $-\zeta'/\zeta(s) = \sum_n \Lambda(n) n^{-s}$, which #26 identified with the regularized self-intersection $\Gamma_S^2$?

## The substrate (Bökstedt's theorem)

$$\pi_*(\mathrm{THH}(\mathbb{Z})) = \mathbb{Z}\ (\deg 0),\quad \mathbb{Z}/i\ (\deg 2i-1,\ i\ge 1),\quad 0\ (\text{even}>0).$$

So the torsion in degree $2i-1$ has order $i$, and its $p$-primary part is $\mathbb{Z}/p^{v_p(i)}$: the prime $p$ enters degree $2i-1$ exactly when $p \mid i$.

## The result: a sharp conditional, not a yes/no

Assign degree $2i-1$ the spectral weight $i^{-s}$ and value $\log|\mathrm{THH}_{2i-1}(\mathbb{Z})| = \log i$. The assembled series is

$$Z_{\mathrm{THH}}(s) := \sum_{i\ge 1} \log|\mathrm{THH}_{2i-1}(\mathbb{Z})|\, i^{-s} = \sum_{i\ge 1} (\log i)\, i^{-s}.$$

**Link 1 (exact, term by term).** $\zeta'(s) = -\sum_i (\log i) i^{-s}$, so $Z_{\mathrm{THH}}(s) = -\zeta'(s)$. Verified to $5\times 10^{-16}$ (partial sum, $s=4$). This is the **imprimitive** log-sum, NOT the von Mangoldt sum.

**Link 2 (the Möbius gap).** The two differ by exactly a factor of $\zeta$:
$$-\zeta'(s) = \zeta(s)\cdot\big(\!-\zeta'/\zeta\big)(s), \qquad \text{equivalently} \qquad \Lambda = \mu * \log,$$
the classical identity $\Lambda(n) = \sum_{d\mid n}\mu(n/d)\log d$ (verified to $6\times 10^{-31}$). So the von Mangoldt sum is recovered by **Möbius convolution** (multiplication by $1/\zeta$) of the THH log-orders.

**Link 3 (per-prime structure, exact by regrouping).** $\sum_i v_p(i)\, i^{-s} = \sum_{k\ge 1}\sum_{p^k\mid i} i^{-s} = \zeta(s)\sum_k p^{-ks} = \zeta(s)\,p^{-s}/(1-p^{-s})$. Times $\log p$ this is $\zeta(s)$ times the $p$-Euler factor of $-\zeta'/\zeta$. Verified to $\sim 10^{-12}$ for $p=2,3,5$. The cross-check $\sum_p v_p(i)\log p = \log i$ (prime factorization) holds exactly and recovers Link 1.

## Interpretation

The primes enter $\mathrm{THH}(\mathbb{Z})$ exactly through $v_p(i)$ in the torsion of degree $2i-1$, with the correct $\log p$ weights, and assemble **rigorously** (given the $i^{-s}$ weight) into $-\zeta'(s)$. The von Mangoldt sum = #26 dynamical zeta = $\Gamma_S^2$ is **one Möbius factor** $1/\zeta$ away. On the spectral side $1/\zeta = \mu$ is the **primitive reduction**: morally the passage from $\mathrm{THH}$ to $\mathrm{TC}$ (the cyclotomic-Frobenius equalizer of Nikolaus-Scholze divides out the redundancy that the bare $\mathrm{THH}$ carries).

So checkpoint 10A.ii is **PASSED in its imprimitive form** and the whole direction is reduced to a single, sharp, falsifiable target:

> **Does the THH $\to$ TC cyclotomic equalizer implement Möbius inversion (multiplication by $1/\zeta$)?**

If yes, the $S^1$-equivariant invariant of $\mathrm{TC}(\mathbb{Z})$ is the von Mangoldt sum and the Deninger flow is incarnated as the circle action. If no, the analogy stops at $-\zeta'$ and Direction 10 is downgraded.

## Two explicit caveats (adversary discipline)

- **Caveat A (the weight).** The weight $i^{-s}$ on degree $2i-1$ is an assumption. With weight $(2i-1)^{-s}$ one gets an odd-zeta-like object instead. Justifying $i^{-s}$ from the $S^1$-equivariant / regularized-determinant formalism is part of milestone 10A.ii proper. This experiment establishes only the conditional identity.
- **Caveat B (the reduction).** "$1/\zeta$ = the TC reduction" is a conjectural mapping, stated as the target, not a theorem.

## K2 firewall (Davenport-Heilbronn)

D-H is a $\mathbb{C}$-linear combination of L-functions, not a ring, so no ring spectrum's $\mathrm{THH}$ produces it. Concretely its von Mangoldt coefficients $\Lambda_{DH}$ **delocalize onto composite $n$** (first leak at $n=6$, then $12,14,18,21,24,\dots$; matches #20/#26). Hence $\Lambda_{DH}$ is NOT $\mu * (\text{log of any order-}i\text{ sequence})$: the THH $\to$ von-Mangoldt route has no D-H analogue. The firewall holds at the most structural level yet: there is no THH to begin with.

## Status

First pass of milestone 10A.ii complete. Rigorous parts: Bökstedt's groups (theorem), the three Dirichlet-series identities (theorems / verified numerically). Conjectural part isolated to one statement (TC = Möbius reduction). Recorded as LEARNINGS #28. Next: Route A proper (justify the $i^{-s}$ weight via the $S^1$-Tate spectral sequence; test whether the equalizer realizes $1/\zeta$), or a SURVEYOR pass on whether the von Mangoldt sum already appears as a TC Euler characteristic in the Hesselholt / Nikolaus-Scholze literature.

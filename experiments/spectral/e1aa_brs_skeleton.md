# E1AA: the BRS skeleton. Does the functional equation buy any economy at $\{k\log p\}$?

> Companion to `e1aa_brs_skeleton.py` / `.npz`. Executes the probe LEARNINGS
> #173's T1 sweep handed forward, built to
> [`../../docs/03_research/brs_skeleton_build_spec.md`](../../docs/03_research/brs_skeleton_build_spec.md)
> (spec written before the build, per the `theta_s4_build_spec.md`
> precedent). K1 guards on `mp.zetazero` and the D-H scanner, never tripped:
> the zero side is symbolic throughout. It proves nothing about RH.

## The question

Bondarenko-Radchenko-Seip (arXiv:2005.02996) Theorem 1.1 is the Viazovska
corpus's own log-node object: it pairs the nodes $\{\log n/(4\pi)\}$ with the
zeta zero multiset, exactly critically, recovering Riemann-Weil as a
consequence. #173's T1 argued on paper that transferring it to $\{k\log p\}$
costs the Euler product for the node restriction and M4 for the one-sided use.
This measures the half of that argument that can be measured:

> Does the FE buy any conditioned economy at the prime sublattice beyond what
> the all-$n$ comb already gives, without evaluating the zero side?

**What the FE is here.** BRS's functional equation is $s \mapsto 1-s$, which
on the log-circle acts as $u \mapsto -u$, so the FE-respecting subspace is the
even (cosine) half of e1o's decimated space $V_K$. That is the entire FE
content available without the zero side. The other half of BRS's mechanism,
the pairing of the node comb against its dual, is exactly what K1 forbids, and
a probe that could see it would be a probe that had already solved the
problem.

## One-line result

**The FE buys nothing.** At generic $\lambda$ the cost ratio at $\{k\log p\}$
is $1.0$ in the full space and still $1.0$ in the FE-even subspace, and the
same is true at the all-$n$ comb, at an equally spaced non-arithmetic comb,
and at the Beurling twin. Where a ratio below 1 does appear, it appears **equally in the all-$n$ comb**
and is an exact rational coincidence forced by the choice of $\lambda$ (a
power of a comb prime, or a ratio of two of them), absent from every comb
without such relations. The economy the S4 spec needs is not on the FE side of BRS; it is on
the zero side, and using the zero side one-sidedly is M4.

## The measurement

The instrument is e1o's `cheapness` (rank of the evaluation matrix of $V_K$ at
the comb, over the number of conditions), with one addition that turned out to
matter more than the rank itself: an exact, **threshold-free predictor**.

> $V_K = \mathrm{span}\{e^{2\pi i K m u/L}\}$ cannot separate $u$ from $u'$
> unless $u - u' \notin (L/K)\mathbb{Z}$. The even (FE-respecting) subspace
> additionally cannot separate $u$ from $-u$, so it also identifies $u$ with
> $u'$ when $u + u' \in (L/K)\mathbb{Z}$. Hence
> $$\mathrm{rank} = \min(\#\text{equivalence classes},\ \dim),$$
> with no tolerance in it. **Verified in 96/96 cells** across every
> $(\lambda, K, \text{comb}, \text{parity})$ combination tested.

So every ratio below 1 in this probe is a *countable coincidence* in the comb,
identifiable in advance, rather than something the rank tolerance decided.
That is what makes the answer clean.

| comb | full $V_K$ | even $V_K$ | even/full |
|---|---|---|---|
| $\{k\log p\}$ | 1.0 except at coincident $\lambda$ | same | **0.90 to 1.00** |
| all-$n$, $\{\log m\}_{m \le \lambda^2}$ | same | same | **0.90 to 1.00** |
| equally spaced (non-arithmetic) | 1.0 | 1.0 | 1.00 |
| Beurling twin | 1.0 | 1.0 | 1.00 |

**The answer to the question is the first two rows being identical.** The FE
identifies exactly as much of the prime comb as of the all-$n$ comb, worst
difference $+0.0000$. Whatever the even subspace buys, the Euler restriction
does not make it buy more.

## Where the dips come from, and why they are not the answer

Every dip is an exact rational relation among the comb points, forced by the
choice of $\lambda$:

- $\lambda = 4$: the circle is $L = 2\log 4 = 4\log 2$, so the 2-orbit
  $\{\log 2, 2\log 2, 3\log 2, 4\log 2\}$ has spacing exactly $L/4$ and wraps
  onto itself. Under $K = 2$ two pairs are identified (ratio $0.8$); in the
  even space $\log 2$ and $3\log 2$ are reflections about $L/2$, giving one
  free condition (ratio $0.9$).
- $\lambda = 6.5$: here $6.5 = 13/2$ and $\log 13 - \log 2 = \log 6.5 = L/2$
  exactly, so two prime powers collide under $K = 2$ decimation. Not $\lambda$
  being a prime power at all, but $\lambda$ being a **ratio** of two primes in
  the comb.

Both appear identically in the all-$n$ comb, which contains the same points
($\log 8 = 3\log 2$). Neither appears in the equally spaced comb or the
Beurling twin, which contain no exact rational relations by construction. So
the dips need exact coincidences, arise in Euler-restricted and unrestricted
combs alike, and are absent from a comb that has an Euler product but no
lattice. They are a measure-zero property of the free parameter $\lambda$, not
a mechanism.

## Two design errors the probe made and caught

Recorded because both are the kind that would have produced a false positive.

1. **The first version used $\lambda \in \{3, 4, 5\}$ throughout**, every one a
   power of a small prime, read the resulting $0.9$ as the FE helping more at
   the primes than at the all-$n$ comb, and that is precisely the shape the
   spec's own exit condition calls an S4-class finding. The conditioning was
   sound ($\sigma_{\min} = 0.14$), so the spec's first screen would not have
   caught it. What caught it was asking *which* $\lambda$, and noticing.
2. **The all-$n$ comb was mis-normalized.** BRS write their nodes as
   $\{\log n/(4\pi)\}$, but that $4\pi$ belongs to their Fourier
   normalization, not to e1o's log-circle geometry. Carried across, it
   compressed the entire comb onto the arc $[0.055, 0.24]$ of a circle of
   circumference $3.74$ and made the evaluation matrix ill-conditioned for
   reasons unrelated to the question. The fair baseline is
   $\{\log m\}_{m \le \lambda^2}$: the same generating structure minus the
   Euler restriction, on the same arc.

## The pre-registration was wrong, in an instructive direction

The spec predicted the FE would buy the trivial parity factor:
"$B3/B1 = B4/B2 \approx 1/2$". **It buys nothing**, on 5 of 6 quick cells and
the large majority of the full grid. Halving the *dimension budget* only
reduces the *rank* when the budget binds, and here the condition count $J$
sits well below even the halved dimension, so the rank is set by $J$ and the
parity restriction costs and buys nothing. The measured answer is stronger
than the predicted one. Recorded because a spec that predicts an effect and
measures none should say so.

## Verdict fields

| field | value |
|---|---|
| `fe_buys_prime_economy` | **NO.** At generic $\lambda$ the even-subspace ratio at $\{k\log p\}$ is 1.0, identical to the full space |
| `fe_buys_parity` | NO, contrary to the spec's own prediction: the dimension halves but the rank does not, because the condition count is not budget-bound |
| `exact_law` | rank = min(#equivalence classes, dim), verified 96/96 cells, threshold-free |
| `full_space_baseline` | 1.0 at generic $\lambda$, reproducing e1o T4c |
| `where_a_drop_appears` | only where $\lambda$ is a rational combination of the comb's own primes ($4 = 2^2$; $6.5 = 13/2$). Identical in the all-$n$ comb, absent from both non-arithmetic controls |
| `controls` | equally spaced comb and the Beurling twin (Euler product, no lattice, no FE) both at 1.0, so nothing is creditable to the FE |
| `k1_clean` | YES, zero side symbolic throughout |
| `consequence` | the S4 economy is not on the FE side of BRS. It is on the zero side, and one-sided use of the zero side is M4: **this corpus's wall is #171's chain wall** |
| `frontier_delta` | ZERO. One more route priced, not opened |

## Caveats

- This cannot prove BRS's mechanism does not transfer. It measures whether the
  FE-available part buys anything at the prime sublattice on a finite
  skeleton. The zero side is symbolic by construction, so the probe is blind
  to exactly the half BRS actually uses, which is the point.
- The rank instrument is inherited from e1o and so are its caveats; in
  particular "cost ratio" is a rank statement about a finite decimated space,
  not a statement about any extremal problem.
- D-H does not apply to the comb geometry (no Euler product means no prime
  sublattice), and is noted rather than faked.

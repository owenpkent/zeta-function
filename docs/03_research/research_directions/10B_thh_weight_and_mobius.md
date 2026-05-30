# Direction 10B (BUILDER note): the i^{-s} weight and the Mobius reduction

> Companion to [`10A_thh_vonmangoldt_checkpoint.md`](10A_thh_vonmangoldt_checkpoint.md) and the experiment [`e_thh_vonmangoldt`](../../../experiments/homotopy/e_thh_vonmangoldt.md). The first pass (LEARNINGS #28) reduced Direction 10 to two flagged gaps. This note attacks both with concrete homotopy-theoretic candidates and, per BUILDER discipline, separates what is established from what is conjectural.
>
> **The two gaps.** (A) Why does degree $2i-1$ carry the spectral weight $i^{-s}$? (B) Why should the $\mathrm{THH}\to\mathrm{TC}$ reduction supply the factor $1/\zeta = \mu$ (Mobius)?

## Gap A: the weight $i^{-s}$ from $S^1$-Tate periodicity and a scaling action

**Established (theorems).**
- $\mathrm{THH}(\mathbb{Z})$ carries an $S^1$-action. Its Tate construction $\mathrm{TP}(\mathbb{Z}) = \mathrm{THH}(\mathbb{Z})^{tS^1}$ is **2-periodic**: there is an invertible periodicity (Bott) class of cohomological degree $2$, and $\mathrm{TP}_*$ is a module over $\mathbb{Z}[\sigma^{\pm 1}]$ with $|\sigma| = 2$. (Nikolaus-Scholze; this is the homotopy-theoretic source of the "even/odd" $2$-step structure that already appears in Bokstedt's $\deg 2i-1$ indexing.)
- The cyclotomic structure provides Frobenii $\varphi_p$ and, through the $C_n$-fixed points and the restriction/Verschiebung maps, an action of the multiplicative monoid $\mathbb{N}^\times$ (the Witt-vector Frobenius/Verschiebung calculus: $F_n V_n = n$).

**The BUILDER claim (the candidate).** Grade $\mathrm{TP}(\mathbb{Z})$ by powers of the degree-2 periodicity class $\sigma$, so the "level $i$" piece sits in degree $2i$ (and the Bokstedt torsion of degree $2i-1$ is its boundary). Let $N$ be the generator of the $\mathbb{N}^\times$ scaling action (assembled from $F_n V_n = n$). The claim is:

> $N$ acts on the level-$i$ ($\sigma^i$) graded piece with eigenvalue $i$.

If so, the zeta-regularized trace $\mathrm{Tr}(N^{-s})$ attaches weight $i^{-s}$ to level $i$, and combined with the Bokstedt torsion log-order $\log i$ gives the assembled $\sum_i (\log i)\, i^{-s} = -\zeta'(s)$ of the first pass.

**Why the eigenvalue should be $i$ (heuristic).** The relation $F_n V_n = n$ is the multiplicative shadow of the periodicity: applying the level-raising operator $n$ times multiplies by $n$. The $\sigma$-grading is exactly the eigenspace decomposition of the scaling generator, with $\sigma^i$ scaled by $i$. This is the same mechanism by which the Connes-Consani scaling site produces $n^{-s}$ from the $\mathbb{R}_+^\times$ (or $\mathbb{N}^\times$) action: the scaling eigenvalue on the $i$-th mode is $i$.

**The honest gap.** Identifying $N$ precisely (is it the Connes $B$-operator composed with periodicity? the de Rham-Witt $d$? the Bost-Connes scaling?) and PROVING its eigenvalue on $\sigma^i$ is $i$ is the real content of milestone 10A.ii. This note gives the candidate operator ($F_n V_n = n$ scaling) and the expected eigenvalue; it does not yet prove it. Alternative outcome to rule out: if the natural grading weight is $(2i-1)^{-s}$ or $(2i)^{-s}$ rather than $i^{-s}$, the assembled series is an odd/even-zeta variant, not $-\zeta'$, and Gap A fails.

## Gap B: the Mobius factor from the cyclotomic necklace decomposition

This is the more promising gap, because the cyclotomic structure has a *known* Mobius mechanism.

**Established (theorems).**
- The cyclic bar construction underlying $\mathrm{THH}$ has $C_n$-fixed points whose components are indexed by the combinatorics of **necklaces** (aperiodic cyclic words). The number of aperiodic necklaces of length $n$ on $q$ letters is the **necklace polynomial**
$$M(q,n) = \frac{1}{n}\sum_{d\mid n} \mu(n/d)\, q^{d},$$
which is *literally Mobius inversion* of $q^n = \sum_{d \mid n} d\, M(q,d)$.
- $\mathrm{TC}$ is the equalizer of $(\mathrm{can}, \varphi)$ assembling the Frobenii over all $p$ (Nikolaus-Scholze). Passing from $\mathrm{THH}$/$\mathrm{TP}$ to $\mathrm{TC}$ extracts the Frobenius-invariant / "primitive" part.

**The BUILDER claim (the candidate).** The redundancy that $\mathrm{TP}$ carries and $\mathrm{TC}$ removes is exactly the over-counting of prime-power levels: the imprimitive sum $-\zeta' = \sum_i (\log i) i^{-s}$ runs over *all* $i$, while the primitive von Mangoldt sum $-\zeta'/\zeta = \sum_n \Lambda(n) n^{-s}$ runs only over prime powers with the necklace/Mobius weights. Concretely, $\Lambda = \mu * \log$ is the same Mobius inversion as the necklace identity $q^n = \sum_{d\mid n} d\,M(q,d)$ read multiplicatively. The conjecture:

> The $\mathrm{THH}\to\mathrm{TC}$ cyclotomic equalizer realizes the Mobius inversion that turns the level-counting Dirichlet series $-\zeta'$ into the primitive (Euler-product) series $-\zeta'/\zeta$.

**Why this is more than a coincidence.** Both sides are governed by the *same* arithmetic function $\mu$ for a structural reason: the cyclotomic $C_n$-fixed-point decomposition (necklaces) and the Dirichlet identity $\Lambda = \mu*\log$ are two faces of Mobius inversion over the divisor lattice. The Frobenius $\varphi_p$ on $\mathrm{THH}$ is, at the level of $\pi_*$, the operation whose iterated fixed points produce the necklace/$\mu$ counting. So the equalizer (Frobenius-invariants) is the natural home for the $\mu$ factor.

**The honest gap.** "Governed by the same $\mu$" is strong heuristic, not a derivation that the $\mathrm{TC}$ Euler characteristic is exactly $-\zeta'/\zeta$. The missing step: track the necklace/Mobius weights through the equalizer at the level of the regularized trace, and verify the resulting Dirichlet series is $1/\zeta$ times the $\mathrm{TP}$ series, not merely "Mobius-flavored." This is checkable on low levels by hand (compute the $C_n$-fixed-point contributions for $n \le 12$ and compare to $\mu$).

## What this note establishes and what it leaves open

- **Establishes:** both gaps have *specific* homotopy-theoretic candidates, not vague hopes. Gap A: the $F_n V_n = n$ scaling action on the $\sigma$-graded $\mathrm{TP}$. Gap B: the necklace/$\mu$ combinatorics of the cyclotomic $C_n$-fixed points, which is literally Mobius inversion.
- **Leaves open (the real milestone):** proving the scaling eigenvalue on $\sigma^i$ is $i$ (Gap A), and tracking the necklace weights through the $\mathrm{TC}$ equalizer to get exactly $1/\zeta$ (Gap B). Both are concrete, both are checkable on low degrees/levels first.

## Next concrete steps (in priority order)

1. **Low-level necklace check (Gap B, cheapest). DONE 2026-05-30, passed.** See [`experiments/homotopy/e_necklace_mobius.py`](../../../experiments/homotopy/e_necklace_mobius.py). Verified exactly (exact rational arithmetic): (a) the necklace polynomials $M(q,n)$ are non-negative integers; (b) $\sum_{d\mid n} d\,M(q,d) = q^n$ (the Mobius-inverse pair); (c) the Metropolis-Rota cyclotomic identity $1/(1-qt) = \prod_n (1-t^n)^{-M(q,n)}$ holds mod $t^{25}$; (d) the same Mobius inversion gives $\Lambda = \mu * \log$ = von Mangoldt. Conclusion: the $\mu$ factor Gap B needs is **intrinsic to the cyclotomic $C_n$-fixed-point combinatorics**, not imported. This is structural support, not yet a proof that $\mathrm{TC}$'s Euler characteristic equals $-\zeta'/\zeta$ (that still needs the necklace weights tracked through the regularized trace).
2. **Identify the scaling operator $N$ (Gap A).** Pin down whether the eigenvalue-$i$-on-$\sigma^i$ claim holds for the de Rham-Witt $d$ / Connes $B$ / Bost-Connes scaling, using the known $\pi_*\mathrm{TP}(\mathbb{Z})$.
3. **The K1 crux (form 10A.iii) remains untouched:** even if Gaps A and B close, producing a *signature* (not a trace) is the actual RH content, and is where R3.5 must be escaped.

## References

- Nikolaus, T.; Scholze, P. (2018). *On topological cyclic homology*. Acta Math. 221(2). (Cyclotomic structure, $\mathrm{TC}$ as equalizer, $\mathrm{TP}$ 2-periodicity.)
- Bokstedt, M. (1985). THH of $\mathbb{Z}$ and $\mathbb{F}_p$. (The torsion orders.)
- Hesselholt, L. (2005, 2015). *The big de Rham-Witt complex*; lectures on $\mathrm{TC}$. (Frobenius/Verschiebung, $F_nV_n = n$.)
- Metropolis, N.; Rota, G.-C. (1983). *Witt vectors and the algebra of necklaces*. Adv. Math. 50. (Necklace polynomials = Mobius inversion; the combinatorial heart of Gap B.)
- Connes, A.; Consani, C. (2016+). *The scaling site*. (The $n^{-s}$ from a scaling action.)

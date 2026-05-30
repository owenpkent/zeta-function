# Direction 10A: The decisive checkpoint for the THH route (does S^1-equivariant THH(Z) reproduce the von Mangoldt sum?)

> **Companion to [`10_thh_cyclotomic_frobenius.md`](10_thh_cyclotomic_frobenius.md).** Direction 10 is broad; this note isolates the ONE checkpoint that should be reached first, because it either lights up the whole direction or kills it cheaply. It is the analogue, on the THH side, of LEARNINGS #26's dynamical-zeta computation.
>
> **The checkpoint, in one line.** Compute the $S^1$-equivariant Euler characteristic / regularized determinant attached to $\mathrm{THH}(\mathbb{Z})$ and ask whether it reproduces $-\zeta'/\zeta(s) = \sum_{n\ge 1}\Lambda(n)\,n^{-s}$ (equivalently the Euler product $\prod_p (1-p^{-s})^{-1}$). If yes, the cyclotomic Frobenius is the carrier of the Deninger flow and Direction 3 should re-point from prismatic-over-$\mathbb{Z}_p$ to $\mathrm{TC}$-over-$\mathbb{S}$. If no, the analogy is decorative and Direction 10 is dropped.

## 1. Why this checkpoint and not another

LEARNINGS #25 isolates the obstruction with unusual precision: over $\mathrm{Spec}(\mathbb{Z})$ the Frobenius correspondence must carry a place-dependent bidegree $(1,p)$, no single scale, and from that one fact the Deninger flow (a continuous $\mathbb{R}$-action, not a $\mathbb{Z}$-action) and the infinite-dimensionality of $H^i$ follow as consequences. LEARNINGS #26 then realizes the regularized self-intersection $\Gamma_S^2$ concretely as the log-derivative of a Ruelle dynamical zeta whose closed-orbit lengths are exactly $\{\log p\}$, giving $\sum_n \Lambda(n) n^{-s}$, and shows Davenport-Heilbronn has no such closed-orbit spectrum.

Direction 10's whole claim is that $\mathrm{THH}(\mathbb{Z})$, with its $S^1$-action and cyclotomic Frobenii $\{\varphi_p\}_{p}$, is the single object that carries all the scales $\{\log p\}$ at once, with the flow being the circle action. If that claim is true, then the $S^1$-equivariant invariant of $\mathrm{THH}(\mathbb{Z})$ must know the primes the same way the dynamical zeta does. So the checkpoint is forced: it is the THH-side mirror of #26. Passing it is necessary (not sufficient) for the direction; failing it is decisive.

## 2. What is rigorously known (the substrate to build on)

These are theorems, not conjectures, and they are the ground the checkpoint stands on.

- **Bökstedt.** $\pi_* \mathrm{THH}(\mathbb{Z})$ is $\mathbb{Z}$ in degree $0$, $\mathbb{Z}/i$ in degree $2i-1$ for $i \ge 1$, and $0$ in positive even degrees. The torsion groups $\mathbb{Z}/i$ are where the arithmetic enters: the prime $p$ appears in degree $2i-1$ exactly when $p \mid i$. This is already a "spread the primes across degrees" phenomenon, organized by a single graded object.
- **Nikolaus-Scholze.** The cyclotomic structure on $\mathrm{THH}(\mathbb{Z})$ is a collection of $S^1$-equivariant Frobenius maps $\varphi_p : \mathrm{THH}(\mathbb{Z}) \to \mathrm{THH}(\mathbb{Z})^{tC_p}$ for every prime $p$, and $\mathrm{TC}(\mathbb{Z})$ is the equalizer assembling all of them. This is the precise sense in which one object carries a Frobenius for every prime at once.
- **Bhatt-Morrow-Scholze.** After $p$-completion, $\mathrm{THH}(\mathbb{Z};\mathbb{Z}_p)$ and its cyclotomic Frobenius recover the prismatic / $q$-de Rham picture over $\mathbb{Z}_p$. So Direction 3's per-prime prismatic outputs are literally the $p$-completed pieces of the global THH object; the directions assemble rather than compete.
- **Hesselholt-Madsen; Hesselholt.** $\mathrm{TC}$ and the de Rham-Witt complex compute $p$-adic $K$-theory of local fields and relate to $p$-adic special values; the technology for turning equivariant THH into number-theoretic output exists.

## 3. The checkpoint stated precisely (three increasingly demanding forms)

Let $\mathbb{T} = S^1$ act on $X = \mathrm{THH}(\mathbb{Z})$ with universal cover $\mathbb{R} \to \mathbb{T}$, giving the candidate Deninger flow $\Phi_t$.

- **10A.i (Euler-factor form).** Show that the local contribution at the prime $p$, extracted from the $C_p$-fixed/Tate piece $X^{tC_p}$ via $\varphi_p$, is the Euler factor $(1-p^{-s})^{-1}$ (equivalently, the local orbit of length $\log p$ of #26). This is the bidegree $(1,p)$ of #25 read off the cyclotomic Frobenius at $p$.
- **10A.ii (assembled-determinant form).** Show that the regularized $\zeta$-determinant of the flow generator, $\mathrm{det}_\infty\!\big(\tfrac{s-\Phi}{2\pi}\big)$ on the appropriate equivariant cohomology of $X$, assembles the local factors into $\xi(s)$ (the completed zeta), so that its logarithmic derivative is $\sum_n \Lambda(n) n^{-s} + (\text{archimedean})$. This is the THH-side mirror of #26 and is the actual checkpoint.
- **10A.iii (signature form, the K1 crux).** Show that the Hermitian/real structure on $\pi_* \mathrm{TC}(\mathbb{Z})$ (with the archimedean place entering as in LEARNINGS #22-24) carries a definite **signature** on a primitive piece, and that RH is that definiteness. This is what separates Direction 10 from Connes' trace formula: if the only output is a trace identity, R3.5 kills it. The direction succeeds only if 10A.iii produces a signature, not a trace.

The checkpoint to reach FIRST is **10A.ii**. It is concrete, it mirrors a computation you have already done on the dynamical side (#26), and it does not yet require resolving the K1 question.

## 4. How to actually attempt 10A.ii

Two routes, run in parallel.

**Route A (computational-structural, the cheaper one).** Work with the known $\pi_* \mathrm{THH}(\mathbb{Z})$ (Bökstedt) and the homotopy-fixed-point / Tate spectral sequences for the $S^1$- and $C_p$-actions. Assemble the candidate Lefschetz/Euler series $\sum_i (-1)^i \mathrm{tr}(\Phi_t \mid H^i_{S^1})$ as a regularized product over the cyclotomic Frobenii, and check term-by-term against the Euler product. The prime $p$ enters through the $\mathbb{Z}/i$ torsion ($p \mid i$) and through $\varphi_p$; the question is whether the bookkeeping reproduces $(1-p^{-s})^{-1}$ at each $p$ with the correct $\log p$ weight. This is paper-and-spectral-sequence work, checkable on the first few primes, in the spirit of your 2K/2Q/2R dictionary entries (#24-26).

**Route B (literature-anchored).** Read the existing attempts to attach zeta values to $\mathrm{TC}/K$-theory (Hesselholt's "topological cyclic homology and the Fontaine-Messing / de Rham-Witt" program; the absolute-geometry heuristics of Connes-Consani on $\mathbb{S}$ as $\mathbb{F}_1$; any work relating the $S^1$-Tate construction to the Riemann gas) and locate whether the von Mangoldt sum has already appeared as an equivariant Euler characteristic, even implicitly. A SURVEYOR pass with a tight scorecard (does the source produce $\sum_n \Lambda(n) n^{-s}$ from an $S^1$-equivariant invariant of THH? yes/no/partial) is the right instrument.

## 5. Kill conditions (be specific, so the checkpoint is honest)

The checkpoint FAILS (and Direction 10 is dropped or heavily downgraded) if any of:

- The assembled equivariant Euler series cannot reproduce the Euler product even on the first three primes (Route A returns a structural mismatch, not just a hard computation).
- The only invariant that *does* reproduce $\sum_n \Lambda(n) n^{-s}$ is manifestly a trace (so 10A.iii can never be a signature, and R3.5 applies).
- The construction reproduces the von Mangoldt sum for an object built from a non-ring spectrum, i.e. the K2 firewall leaks (this should be impossible, since THH needs the multiplication, but it must be checked: a $\mathbb{C}$-linear combination like D-H has no ring whose THH gives it, so there should be no THH-side D-H at all).

## 6. What success buys, even short of RH

Independent of RH, reaching 10A.ii would give:

- A clean homotopy-theoretic identity "the von Mangoldt sum is the $S^1$-equivariant Euler characteristic of $\mathrm{THH}(\mathbb{Z})$," which would be a genuinely new statement connecting Bökstedt's computation to the prime counting function.
- A rigorous incarnation of the Deninger flow as the circle action on THH, removing the "infinite-dimensional $H^i$, mysterious $\mathbb{R}$-flow" hand-waving by replacing it with the cyclotomic formalism.
- A re-pointing of Direction 3: the prismatic-over-$\mathbb{Z}_p$ work becomes the $p$-completed shadow of the global TC object, which is a cleaner organizing principle for Phase 2.

## 7. Estimated effort to the checkpoint

Route A: 2-6 person-months for someone fluent in cyclotomic spectra and the THH/TC spectral sequences, to either exhibit the first-primes match or find the structural mismatch. Route B: 2-4 person-weeks of SURVEYOR-grade literature work. This is the cheapest decisive milestone in the entire Directions 1-13 portfolio relative to its potential payoff, which is exactly why it should be attempted before the heavier Direction 8 / Direction 10A.iii machinery.

## 8. References

- Bökstedt, M. (1985, unpublished). *Topological Hochschild homology of $\mathbb{Z}$ and $\mathbb{Z}/p$*.
- Nikolaus, T.; Scholze, P. (2018). *On topological cyclic homology*. Acta Math. 221(2).
- Bhatt, B.; Morrow, M.; Scholze, P. (2019). *Topological Hochschild homology and integral $p$-adic Hodge theory*. Publ. Math. IHES 129.
- Hesselholt, L. (1996, 2006). *On the $p$-typical curves in Quillen's $K$-theory*; *The de Rham-Witt complex and $p$-adic Hodge theory*.
- Deninger, C. (1998, 2002). The foliated-dynamical-systems program (the flow this checkpoint aims to incarnate).
- LEARNINGS #25 (bidegree obstruction), #26 (dynamical zeta = von Mangoldt sum), #22-24 (the archimedean place in the signature).

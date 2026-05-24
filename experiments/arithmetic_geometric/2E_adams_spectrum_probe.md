# 2E — Adams-Operation Spectrum vs Zeta-Zero Ordinates

> A direct numerical probe of the hypothesis underlying [2A_R5_prismatic_cohomology.md](2A_R5_prismatic_cohomology.md): on any concrete Λ-ring substrate, do the Adams operations $\psi_p$ have a spectrum that resembles the imaginary parts $\{\gamma_n\}$ of zeta zeros?
>
> **Headline**: no, and the negative result is the right answer. Bare $\psi_p$-spectra in computable settings are roots of unity, the single point $\{0\}$, or pure powers of $p$. None of these match $\{\gamma_n\} \approx \{14.13, 21.02, 25.01, 30.42, \ldots\}$ in any structural way. The one apparent near-coincidence ($5^2 = 25 \approx \gamma_3 = 25.01$) is pigeonhole, confirmed by a randomization control.
>
> **Why this matters**: confirms that R5 is the correct framing. The Λ-structure itself is too small (or too symmetric) to carry zeta-zero information. A cohomology theory built on top of $\mathrm{Spec}(W(\mathbb{Z}))$ is what would lift the small Λ-action to a Hilbert-space-like object large enough to host the zeta spectrum. Prismatic cohomology is R5's leading candidate for that theory.

## 1. The hypothesis under test

In Borger's framework ([2A_borger_dossier.md §2-3](2A_borger_dossier.md)), the Adams operations $\psi_p$ are the Frobenius substitute for $\mathrm{Spec}(\mathbb{Z})$. By analogy with curves over $\mathbb{F}_q$, one might hope: "the eigenvalues of $\psi_p$ on some natural Λ-ring give the imaginary parts of zeta zeros." The Weil-proof template ([2A_weil_proof_diff.md](2A_weil_proof_diff.md)) puts Frobenius eigenvalues on $H^1(C, \mathbb{Q}_\ell)$ at the zeros of $Z(C, T)$; the corresponding aspiration for $\mathrm{Spec}(\mathbb{Z})$ is: $\psi_p$-eigenvalues on some H-something give the zeros of $\zeta$.

R5 articulates the structural reason this can't work directly on the Λ-ring: the bare Λ-ring is the wrong size of object. The cohomology theory is what does the lifting.

This experiment makes "bare Λ-ring is too small" concrete by computing $\psi_p$-spectra on four concrete Λ-ring substrates and demonstrating the gap.

## 2. The four probes

### Probe 1: $\psi_p$ on representation rings $R(\mathbb{Z}/n)$

$R(\mathbb{Z}/n)$ has basis given by characters $\chi_j$, $j \in \mathbb{Z}/n$. The Adams operations act by

$$\psi_p(\chi_j)(g) = \chi_j(g^p) = \chi_{pj \bmod n}(g).$$

So $\psi_p$ is the permutation matrix corresponding to multiplication by $p$ on $\mathbb{Z}/n$. Its spectrum is a union of root-of-unity sets: a cycle of length $L$ in the permutation contributes the $L$-th roots of unity.

**Computed for** $(p, n) \in \{(2, 7), (3, 7), (3, 100), (2, 105), (5, 1001)\}$. All eigenvalues lie exactly on the unit circle, as predicted. Cycle structure observed e.g. for $(p, n) = (3, 100)$: 11 cycles, lengths up to 20.

### Probe 2: Frobenius on $\mathbb{F}_q$ for $q = p^k$

Frobenius $F: x \mapsto x^p$ on $\mathbb{F}_q$ has order $k$, so its eigenvalues (over $\overline{\mathbb{F}_p}$, or under any lift to characteristic 0) are the $k$-th roots of unity. Computed mod $p$ as the matrix of $F$ in a basis $\{1, \alpha, \alpha^2, \ldots, \alpha^{k-1}\}$ where $\alpha$ is a root of an irreducible polynomial of degree $k$ over $\mathbb{F}_p$. Sanity check: $F^k \equiv I \pmod p$ for all four test cases.

**Computed for** $(p, k) \in \{(2, 3), (2, 5), (3, 4), (5, 3)\}$. Eigenvalues are exactly $\{e^{2\pi i j/k}\}$.

### Probe 3: $\psi_p$ on truncated ghost ring of $W$

In ghost coordinates, the Adams operations on big Witt vectors $W(R)$ satisfy

$$\psi_p \circ w_n = w_{pn}$$

where $w_n: W(R) \to R$ is the $n$-th ghost component. If we truncate to ghost components $\{w_1, w_2, \ldots, w_N\}$, then $\psi_p$ sends $w_n$ to $w_{pn}$ for $pn \le N$ and to $0$ otherwise. Since $p > 1$ implies $pn \ne n$ for all $n > 0$, the diagonal is zero, the matrix is strictly upper-shift in $n$, hence **nilpotent**. Spectrum: $\{0\}$.

**Computed for** $(p, N) \in \{(2, 16), (3, 27), (5, 25), (2, 64)\}$. Numerical eigenvalue computation returns $\max|\lambda| < 10^{-15}$ in all cases, confirming nilpotency.

### Probe 4 (reference): $\psi_p$ on rational K-theory $K_*(\mathrm{Spec}\,\mathbb{Z}) \otimes \mathbb{Q}$

Computed theoretically (not from matrix), as a reference point. By the Beilinson decomposition of rational K-theory, $\psi_p$ acts as multiplication by $p^d$ on $K_{2d-1}(\mathbb{Z}) \otimes \mathbb{Q}$. So the spectrum is $\{p^d : d \ge 0\}$.

Computed for $p \in \{2, 3, 5, 7\}$, $d \in \{0, \ldots, 7\}$.

## 3. Quantitative comparison to zeta ordinates

For each probe we report $\min_n \min_{\lambda \in \mathrm{spec}} |\gamma_n - \lambda|$, where $\gamma_n$ ranges over the first 10 zeta zero ordinates and $\lambda$ is taken over the relevant real-valued projection of the spectrum (real part, imaginary part, modulus — whichever is smallest).

| Probe | Spectrum | min $|\gamma_n - \lambda|$ |
|---|---|---|
| $R(\mathbb{Z}/7)$, $\psi_2$ | 7-th roots of unity union | 13.13 |
| $R(\mathbb{Z}/100)$, $\psi_3$ | unit circle, 11 cycles | 13.13 |
| $R(\mathbb{Z}/1001)$, $\psi_5$ | unit circle, 33 cycles | 13.13 |
| $F$ on $\mathbb{F}_{2^3}$ | $\{1, \omega_3, \omega_3^2\}$ | 13.13 |
| $F$ on $\mathbb{F}_{3^4}$ | $\{1, i, -1, -i\}$ | 13.13 |
| $\psi_2$ on $W$-ghost, $N=64$ | $\{0\}$ | 14.13 |
| $K$-theory, $\psi_2$ | $\{1, 2, 4, 8, 16, 32, 64, 128\}$ | 0.94 |
| $K$-theory, $\psi_5$ | $\{1, 5, 25, 125, \ldots\}$ | **0.01** |
| $K$-theory, $\psi_7$ | $\{1, 7, 49, 343, \ldots\}$ | 0.77 |

For reference: the mean consecutive zeta-ordinate spacing at this height is about 3.96.

**Probes 1, 2, 3**: clearly no match. Spectra live on the unit circle or at $\{0\}$, while $\gamma_n$ starts at 14.13. Min-distances are exactly $\gamma_1 - 1$ or $\gamma_1 - 0$. There is no parameter choice that would shrink these.

**Probe 4 (K-theory)**: pure powers of $p$. Several entries are accidentally close to $\gamma_n$:
- $5^2 = 25.00$ vs $\gamma_3 = 25.01$, distance $0.01$ (the closest hit).
- $2^4 = 16$ vs $\gamma_1 = 14.13$, distance $1.87$ (or $2^5 = 32$ vs $\gamma_5 = 32.94$, distance $0.94$).
- $7^2 = 49$ vs $\gamma_9 = 48.01$, distance $0.99$ (or vs $\gamma_{10} = 49.77$, distance $0.77$).

## 4. Randomization control on probe 4

To check whether the K-theory near-coincidences indicate signal or just pigeonhole, we use a structural null: replace $\{2, 3, 5, 7\}$ with 4 randomly chosen primes from $[2, 200]$, form the same family $\{q^d : d = 0, \ldots, 7\}$, and recompute min-distance to the first 10 $\gamma_n$.

Over 5000 trials:
- **Observed min-distance** (the actual $\{2, 3, 5, 7\}$ data): $0.0109$
- **Null median**: $0.97$
- **Quantile of observed in null**: $0.086$

So the closeness is in the lower tail (~9th percentile) but not extreme. About 1 in 12 random 4-prime configurations produces a similar or closer collision. Verdict: **lucky pigeonhole, not signal**.

This is the right outcome for two structural reasons:
1. Powers of small primes pack densely in $[1, 50]$ on the log scale; with 4 primes and 8 powers we get 13 values in $[1, 50]$ vs 10 zeta ordinates there. A $\le 0.01$ collision under such density is expected at the few-percent level.
2. There is no theory that would predict $\psi_5$-eigenvalue 25 should equal $\gamma_3$. The Beilinson eigenvalues $p^d$ are integer powers; the $\gamma_n$ are transcendentals (conjecturally irrational, almost certainly transcendental). Their distributions are unrelated.

## 5. What this shows

**The bare $\psi_p$-spectrum on any computable Λ-ring substrate carries no zeta-zero information.** The four probes cover the main concrete families one can think of:

| Substrate | Where it sits | Why it can't carry $\gamma_n$ |
|---|---|---|
| $R(\mathbb{Z}/n)$ | Finite-dim representation theory of small cyclic groups | Spectrum is on unit circle (permutation) |
| $\mathbb{F}_q$ | Finite-dim $\mathbb{F}_p$-vector space | Spectrum is $k$-th roots of unity ($F$ has order $k$) |
| Truncated ghost $W_N$ | Finite-dim shifts | $\psi_p$ is nilpotent (no diagonal) |
| $K$-theory of $\mathbb{Z}$ | Infinite-dim graded $\mathbb{Q}$-vector space | $\psi_p = p^d$ on Beilinson eigenspace; integer-spaced |

In all four, the spectrum is dictated by the small-finite or shift-graded structure of the substrate, not by anything connected to $\zeta$.

## 6. Why this confirms R5's framing

R5 ([2A_R5_prismatic_cohomology.md](2A_R5_prismatic_cohomology.md)) argues that the Adams operations on Borger's $W(\mathbb{Z})$ would carry zeta-zero spectral information only after lifting to a cohomology theory built on $\mathrm{Spec}(W(\mathbb{Z}))$. The bare $\psi_p$ would not.

This experiment confirms R5's structural reasoning by exhausting the natural finite-dim Λ-ring substrates and showing that none of them has spectrum compatible with zeta. To get a zeta-like spectrum out of Borger's framework, the missing ingredients are:

1. A cohomology theory $H^*_?(\mathrm{Spec}\,W(\mathbb{Z}))$ that is **infinite-dim** in the right way (capable of hosting infinitely many distinct eigenvalues).
2. A $\psi_p$-action on that cohomology that is **trace-class or summable** (so the spectrum is discrete and countable, like $\{\gamma_n\}$).
3. The spectrum must **come from arithmetic, not from the bare Λ-structure**.

Prismatic cohomology of $\mathrm{Spec}(W(\mathbb{Z}))$ (R5's proposal) is the strongest current candidate for (1)-(3), via the $\delta$-ring structure that pairs with $\psi_p$. Whether the prismatic-cohomology $\psi_p$-spectrum actually equals $\{\gamma_n\}$ is the central open question — R5 Q2.

## 7. The complementary "Weil-curve" baseline

For comparison, recall what Weil's proof of RH for curves $C / \mathbb{F}_q$ delivers ([2B](e2b_elliptic_curve_fp.py)): Frobenius on $H^1(C, \mathbb{Q}_\ell)$ has eigenvalues $\alpha_i$ with $|\alpha_i| = \sqrt q$ (the Weil bound). Crucially:

- $H^1$ has dimension $2g$ (the genus): **infinite-dim only as $g \to \infty$**, but in any case has the right finite-dim structure to host $\zeta_C$'s zeros.
- The action of $\mathrm{Frob}_q$ on $H^1$ is given by the **geometric Frobenius endomorphism of $C$**, not by an Adams operation on the algebraic substrate (the ring $H^0(C, \mathcal{O}_C)$, for instance).

Both points have direct $\mathrm{Spec}(\mathbb{Z})$ analogues that are open:
- The right "cohomology" of $\mathrm{Spec}(W(\mathbb{Z}))$ (or its compactification) is the R5 question.
- The right "geometric Frobenius substitute" is the constraint (viii) question in [2A_candidate_evaluation.md](2A_candidate_evaluation.md).

Both 2B and 2E point in the same direction: **the cohomology theory carries the spectral information; the bare algebraic substrate does not.** This is the structural lesson.

## 8. Limitations

- We tested four concrete Λ-ring substrates. There are exotic Λ-rings (e.g., the universal $\Lambda$-ring on infinitely many generators, the de Rham-Witt complex of a smooth scheme, the Frobenius-equivariant K-theory of moduli stacks) that we did not probe. The point is structural — bare $\psi_p$-actions on finite/discrete substrates have spectra constrained by the substrate's structure, not by external arithmetic — but a counterexample would be valuable.
- We compared spectra to the **first 10 $\gamma_n$**. A larger comparison (say first 1000) would not change the structural conclusion but might surface additional pigeonhole near-coincidences in probe 4.
- We did not test the rotated comparison: "are zeta ordinates $\gamma_n$ themselves approximately roots of unity in some natural way?" The answer is no (zeta ordinates are conjecturally irrational, with no rational multiples of $\pi$ structure), but this is a separate non-trivial statement.

## 9. Outputs

- **Code**: [e2e_adams_spectrum.py](e2e_adams_spectrum.py)
- **Figure**: [e2e_adams_spectrum.png](e2e_adams_spectrum.png) — four-panel plot of probe spectra in $\mathbb{C}$, with zeta-ordinate overlay on the K-theory panel.
- **Data**: `e2e_adams_spectrum.npz` — all probe eigenvalues, min-distance rows, randomization-control distribution.

## 10. Connections to the broader Arch 2A program

- **R3.5** ([2A_R3_5_K1_universality.md](2A_R3_5_K1_universality.md)): the no-shortcut theorem rules out direct $\psi_p$-based positivity arguments. 2E is the spectral analogue: bare $\psi_p$-spectra are also too constrained to hit zeta zeros.
- **R5** ([2A_R5_prismatic_cohomology.md](2A_R5_prismatic_cohomology.md)): articulates that the cohomology lifts is where the zeta-spectrum should live. 2E exhausts the "non-cohomology" route and confirms the gap is structural.
- **R5 Q2**: the question "does $\psi_p$ on $H^*_{\mathrm{prism}}(W(\mathbb{Z}))$ have zeta-zero-like spectrum?" remains open. 2E is consistent with that question being the right one (per R5), but does not advance it: the cohomology computation is beyond the project scope per [2A_path_forward.md](2A_path_forward.md).

## 11. Verdict

The bare Adams operations $\psi_p$ on concrete Λ-ring substrates do **not** have zeta-zero-like spectra. This is structurally expected: the substrate is too small or too symmetric. R5's prediction that the cohomology theory must do the lifting is consistent with the data.

2E does not refute Arch 2 (or even Borger). It refutes a naive version of Borger that would skip the cohomology step. The actual Borger candidate (with prismatic cohomology on top, per R5) remains the strongest 𝔽₁ candidate — and remains blocked at K1 (positivity) per R3.5, not at the spectrum question.

**Status:** Arch 2E complete. The Adams-spectrum question is closed: the bare $\psi_p$ does not carry zeta information, the cohomology theory must. This is the predicted negative result.

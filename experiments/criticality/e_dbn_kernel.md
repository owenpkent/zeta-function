# E_DBN1 — de Bruijn-Newman kernel positivity is orthogonal to RH (heat-side face of the D-H discipline)

> Direction 12 (de Bruijn-Newman criticality), first computational experiment.
> Closes the gap left by [`3e_li_de_bruijn_newman.md`](../positivity/3e_li_de_bruijn_newman.md),
> which deferred the heat side as "computationally heavy" and never ran it.
> Code: [`e_dbn_kernel.py`](e_dbn_kernel.py). Run `python -m experiments.criticality.e_dbn_kernel`.
>
> **Status after adversarial verification + literature survey (2026-06-02).** The mathematics
> is verified correct (independent re-implementation reproduced every number; see "Verification").
> The central conclusion is **TRUE and confirms the project's marginal-positivity thesis**, but
> it is **substantially pre-empted** by the de Bruijn-Newman literature (Dobner 2020;
> Newman-Wu 2019; Michalowski 2026). This is therefore a **confirmed coordinate** (and an import
> of three serious references that independently corroborate the thesis), not new mathematics.
> The project's own durable contributions are the D-H-discipline packaging, the quantitative
> suppression law, and the explicit D-H numerics. Framed honestly below.

## The question

The project's **marginal-positivity thesis** ("RH is just barely true, no buffer for soft
proofs") is *verbatim* Newman's 1976 slogan: introducing the constant $\Lambda$, Newman called
$\Lambda \ge 0$ "a quantitative version of the dictum that the Riemann hypothesis, if true, is
only barely so." Its precise avatar: $\mathrm{RH} \Leftrightarrow \Lambda = 0$, with
$\Lambda \ge 0$ a **theorem** (Rodgers-Tao 2018). So half of the marginal-positivity thesis is
already proven.

de Bruijn's half ($\Lambda \le 1/2$) rests on the positivity of the **Pólya kernel** $\Phi$,

$$\Xi_f(z) := (\text{completed } f)\!\left(\tfrac12 + iz\right) = \int_0^\infty \Phi_f(u)\cos(zu)\,du ,$$

which for $\zeta$ is Pólya's 1926 theorem $\Phi_\zeta > 0$, a **theta / modularity** fact, *not*
the Euler product. The project question: **is $\Phi \ge 0$ a face of the Davenport-Heilbronn
discipline?** Does the wrong-approach detector fail kernel positivity where $\zeta$ passes it?

## The test (Bochner, in the project's idiom)

$\Xi_f$ is real, even, exponentially decaying on the line, so by **Bochner**:
$\Phi_f \ge 0 \iff \Xi_f$ positive-definite $\iff$ every Toeplitz $[\Xi_f((j{-}k)\delta)]\succeq 0$.
Two **rigorous one-sided FAIL witnesses** (no truncation caveat) that $\Phi_f \not\ge 0$:

1. **Toeplitz min eigenvalue $< 0$** ($M=\int\Phi\,w w^* du$ is a nonnegative combination of
   rank-1 PSD matrices when $\Phi\ge 0$, so $M\succeq 0$ exactly).
2. **$\max_z|\Xi(z)| > |\Xi(0)|$** (a positive-definite function attains its max modulus at $0$).

Passing both is *necessary, not sufficient* for $\Phi\ge 0$ — the code labels it "$\Phi\ge 0$
consistent / no resolvable witness," never "proof." Method **validated on $\zeta$**: reconstructed
$\Phi_\zeta \ge 0$, matches Pólya's closed form to **shape error $4.4\times10^{-16}$**.

## The result

Canonical entire completion per function (the object whose real-rootedness $\Leftrightarrow$ its
RH). $\zeta$ and Epstein have a pole, so carry the $\tfrac12 s(s{-}1)$ factor; D-H and Dirichlet
are entire (no factor) — the **clean, unconfounded** comparison.

| function | Euler | RH ($\le T$) | deg $d$ | $\max|\Xi|/\Xi(0)$ | Toeplitz min eig | resolvable $\Phi\!<\!0$? |
|---|---|---|---|---|---|---|
| $\zeta$ | yes | yes | 1 | 1.000 | $-7\times10^{-31}$ | none (Pólya: $\Phi>0$) |
| $\chi_3$ (mod 3) | yes | yes | 1 | 1.000 | $-1\times10^{-31}$ | none |
| $\chi_4$ (mod 4) | yes | yes | 1 | 1.000 | $-2\times10^{-32}$ | none |
| **Davenport-Heilbronn** | **no** | **NO** | 1 | **1.000** | $-1\times10^{-30}$ | **none (to floor)** |
| Epstein d47 principal ($\times s(s{-}1)$) | no | yes | 2 | **1.853** | $-8.1$ | **YES** (factor-induced) |
| Epstein d47 principal (bare) | no | yes | 2 | 1.000 | $+0.41$ | none |
| Epstein d47 non-principal | no | NO | 2 | 1.000 | $-3\times10^{-15}$ | none (to floor) |

**Headline (clean degree-1 comparison).** $\zeta$, $\chi_3$, $\chi_4$ (Euler) **and
Davenport-Heilbronn (non-Euler, RH FALSE)** show **no resolvable failure of $\Phi\ge 0$**
($\max|\Xi|/\Xi(0)=1.000$, Toeplitz PSD to the floor). The canonical RH-violator is
indistinguishable from $\zeta$ on kernel positivity. So $\Phi\ge 0$ is **not** a face of the
D-H discipline and **does not discriminate RH**.

> **Precise wording (verifier catch).** For $\zeta$, $\Phi>0$ is Pólya's *theorem*. For D-H there
> is no modularity reason for $\Phi_{DH}\ge 0$ and its coefficients $(1,\kappa,-\kappa,-1,0)$ have
> mixed signs; the experiment establishes only that **no failure is resolvable** — any violation
> is below the suppression floor $\exp(-\tfrac{\pi}{4}d\gamma)\sim10^{-29}$. That is exactly the
> point: the kernel test *cannot see* whether D-H truly passes. (Indeed de Bruijn's strip-width
> theorem gives D-H a finite $\Lambda_{DH}>0$, so its $H_t$ is *not* real-rooted at $t=0$, yet its
> $t=0$ kernel is blind to this.)

**$\Phi \ge 0$ is orthogonal to RH (degree-2).** With the canonical $\tfrac12 s(s{-}1)$ factor,
the **RH-true** Epstein-principal **breaks** positive-definiteness ($\max|\Xi|/\Xi(0)=1.85$ at
$z=2$, *not at any zero*); the **RH-false** Epstein-non-principal passes; without the factor both
pass. So positive-definiteness is a property of the function's archimedean / pole shape, **not**
its zero locations. (Honestly flagged: the principal failure is *factor-induced* — decomposes as
$|\tfrac12 s(s{-}1)|=2.125 \times$ bare $0.109 = 1.853$ — not a zero effect.)

## Why: the exact suppression law

An off-line zero at height $\gamma$ enters $\Phi$ only at the **archimedean-suppressed level**
$\sim\exp(-\tfrac{\pi}{4}d\,\gamma)$, because $|\Xi_f(\tfrac12+iz)|\sim\exp(-\tfrac{\pi}{4}d|z|)$
(the $\Gamma$-factor; Dobner's Lemma 1). Measured (decay-rate fit at elevated precision):

| function | $d$ | measured rate | predict $\tfrac{\pi}{4}d$ | $|\Xi(\gamma_{\mathrm{off}})|$ |
|---|---|---|---|---|
| Davenport-Heilbronn | 1 | 0.73 ($\to\pi/4$; residual = sub-exp. polynomial) | 0.785 | $|\Xi(85.7)| = 1.5\times10^{-29}$ |
| Epstein d47 non-principal | 2 | **1.589** | 1.571 | $|\Xi(32.0)| = 3\times10^{-20}$ |

So D-H's RH violation is buried **~29 orders of magnitude down** in the function whose transform
is $\Phi$. This is the **stealth window** (LEARNINGS #18/#19/#34) in the heat basis, the **softest
detector in the project**: the raw Weil Gram sees the off-line obstruction at $\sim2.6\%$ of its
spectrum (#18); the de Bruijn kernel sees it at $\sim10^{-29}$.

## Consequence

de Bruijn's theorem extracts only $\Lambda \le 1/2$ — and that bound uses $\Phi\ge 0$ **together
with the kernel's super-exponential decay** (the $e^{2u}$ in the theta kernel; $\Phi\ge 0$ alone
gives merely *some* finite bound). All RH content lives in the gap $(0,1/2]$: the **flow**
(the sign of $\Lambda$), not the $t=0$ kernel. This **vindicates Direction 12's flow focus** and
**explains its difficulty** (the cheap $t=0$ object is K2-failing and orthogonal to RH, so the
Polymath15-style flow is forced).

### Kill-criteria read
- **K2 (D-H discipline): FAIL.** A candidate RH route on $\Phi\ge 0$ cannot distinguish $\zeta$
  from D-H — the most extreme stealth window in the project.
- **K1 (signature not trace):** the flow positivity that *would* reach $\Lambda\le 0$ is governed
  by $\Xi$ (hence the primes via the explicit formula), funneling back to the same signature
  ("all roads to the signature").

## Where this sits in the literature (the honest framing)

The central conclusion is **established**, at three levels:

- **Dobner (2020), *A proof of Newman's conjecture for the extended Selberg class*** (arXiv:2005.05142,
  Acta Arith. 2021). Proves $\Lambda_F \ge 0$ for **every** $F$ in the extended Selberg class $S^\#$
  (Kaczorowski-Perelli) — which **drops the Euler-product axiom and therefore includes
  Davenport-Heilbronn**. The kernel $\Phi_F$ is the critical-line Fourier transform of the
  completed $L$ and is *never assumed nonnegative*; the proof is "completely analytic rather than
  arithmetic" and notes that "mock $\xi$" functions (arbitrary Dirichlet series $\times$ arbitrary
  $\Gamma$ factors) have deformations with off-line zeros for all $t<0$. **This pre-empts the
  orthogonality claim and covers D-H directly.** (Lemma 1 is the $\Gamma$-factor decay that *is*
  our suppression law.)
- **Newman-Wu (2019), *Constants of de Bruijn-Newman type...*** (arXiv:1901.06596). The 3-fact
  decomposition isolating $\Phi\ge 0$ as powering only de Bruijn's $\Lambda\le 1/2$; and explicit
  nonnegative even kernels whose deformation has **empty** real-zero set (Case 9 / Prop 19) — the
  cleanest abstract statement of "$\Phi\ge 0$ is independent of real-rootedness." Thm 10: only a
  narrow Laguerre-Pólya product form gives $\Lambda=-\infty$, which $\Phi_\zeta$ provably violates
  — the structural form of "barely true."
- **Michalowski (2026), *On the Pólya Frequency Order of the de Bruijn-Newman Kernel*** (arXiv:2602.20313,
  Feb 2026). **Convergent independent work using the same Toeplitz-minor method (mpmath interval
  arithmetic):** proves the kernel $K(u)=\Phi(|u|)$ is not PF$_5$ and states explicitly that this
  "should not be confused with the de Bruijn-Newman constant $\Lambda$, which concerns the reality
  of zeros... orthogonal to, and not subsumed by" the zero-reality results.
- Generalized $\Lambda$ for sub-families predates this: **Stopple (2013)** ($\Lambda_{Kr}$ for
  quadratic Dirichlet $L$, arXiv:1301.3158); **Andrade-Chang-Miller (2013)** (function-field /
  automorphic, arXiv:1310.3477). Necessary-not-sufficient precedent: **Csordas-Norfolk-Varga
  (1986)** Turán inequalities for $\xi$.

**What is genuinely the project's own** (not found verbatim in the surveyed literature):
1. The framing of $\Phi\ge 0$ as a **face of the Davenport-Heilbronn discipline** and the **K2-FAIL**
   verdict (wrong-approach-detector vocabulary applied to kernel positivity).
2. The **quantitative stealth law** $\exp(-\tfrac{\pi}{4}d\gamma)$ as a *detector-resolution* law,
   tied to the Weil-Gram $2.6\%$ figure (#18) — a cross-architecture quantification.
3. The **explicit D-H numerics** (D-H is *outside* the named dBN literature — it is in $S^\#$ in
   principle via Dobner, but nobody computed $\Phi_{DH}$ / $|\Xi_{DH}(85.7)|$ explicitly).
4. The **synthesis** linking $\Lambda=0$ to the marginal-positivity thesis and "all roads to the
   signature."

## Verification (workflow `wf_2e7d7b30`, 4 agents)

- **Independent re-implementation (PASS).** Rebuilt $\Xi$ from scratch (dps=40, no reuse of code
  paths beyond the shared $L$-evaluators) and reproduced every number: D-H even/real and FE
  $\Lambda(s)=\Lambda(1-s)$ to $10^{-41}$ ($\varepsilon=+1$); $\max|\Xi_{DH}|/\Xi(0)=1.000000$
  verified by a fine scan to $z=90$ (past the off-line height); Toeplitz min eig $-3.2\times10^{-16}$
  (PSD), wide grids reaching $z=90$ give strictly positive min eig; decay rate $0.7985$;
  $|\Xi_{DH}(85.699)|=1.51\times10^{-29}$; off-line zero independently refined to
  $0.80852+85.6993i$ ($\mathrm{Re}-\tfrac12=0.31$, genuine violation); Epstein factor break
  decomposed as $2.125\times0.109$.
- **Adversarial math/logic (PASS, sound-with-caveats).** Bochner + max-modulus witnesses correct
  and honestly used; D-H completion correct; $s(s{-}1)$ confounder handled fairly (verified $\zeta$
  *without* the factor still passes, so the factor is not doing the degree-1 work); citations
  standard. Caveats fixed here: the degree-2 decay rate is $\approx1.5$ (not $1.25$ — that was a
  precision-floor artifact; the suppression law holds *better* than first reported); "D-H satisfies
  $\Phi\ge 0$" softened to "no resolvable failure"; "$\Lambda\le1/2$ from $\Phi\ge 0$ **and** the
  kernel decay."

## What this opens (next target)

Rodgers-Tao prove $\Lambda\ge 0$ via a **monotone Lyapunov functional** on the zero dynamics. The
sharp follow-up this experiment isolates: **can that proven functional be identified with a
fragment of the Weil / Hodge positivity**, so that $\Lambda\ge 0$ becomes a proven piece of the
signature and the missing half ($\Lambda\le 0$) the exact remaining fragment? That would turn the
squeeze $0\le\Lambda\le1/2$ into a statement about which part of the signature is already a
theorem — a Level-4 target, unlike the (Level-3) kernel test this experiment retired.

## Honest scope

A **confirmed negative coordinate**: it retires the cheap $t=0$ kernel as an RH test, explains why
(archimedean suppression $\exp(-\tfrac{\pi}{4}d\gamma)$), and imports three references that
corroborate the marginal-positivity thesis. It does **not** advance the signature construction, and
its core conclusion is pre-empted (Dobner 2020 / Newman-Wu 2019 / Michalowski 2026). Numerically
rigorous *given* the $L$-evaluations (D-H FE to $10^{-41}$; $\zeta$ Pólya-validated to $4\times10^{-16}$);
not a formal proof.

## Pointers
- Direction doc: [`../../docs/03_research/research_directions/12_debruijn_newman_criticality.md`](../../docs/03_research/research_directions/12_debruijn_newman_criticality.md)
- Literature note: [`../positivity/3e_li_de_bruijn_newman.md`](../positivity/3e_li_de_bruijn_newman.md)
- Anchors: LEARNINGS #18 (Weil-form 78.7% / 2.6% stealth), #19 (stealth window), #34 (Rosati stealth window), #27 (Jensen/Turán stealth).
- References: Newman 1976; de Bruijn 1950; Rodgers-Tao, *Forum Math Pi* 8 (2020); **Dobner, arXiv:2005.05142 (2020)**; **Newman-Wu, arXiv:1901.06596 (2019)**; **Michalowski, arXiv:2602.20313 (2026)**; Stopple, arXiv:1301.3158 (2013); Andrade-Chang-Miller, arXiv:1310.3477 (2013); Polymath15 (2019).

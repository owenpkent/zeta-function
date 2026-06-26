# 3S: the moment-MATRIX framing of M4 dissolves over Z (the Li-Hankel is non-PSD for zeta)

> Experiment [`e3s_li_hankel_dissolves.py`](e3s_li_hankel_dissolves.py). A verified structural
> no-go from the 2026-06-26 M4 construction attempt (front 2, `scratchpad/m4_attempt/02_moment_gram.md`).
> Recorded as LEARNINGS #128. Not a proof of anything; a coordinate that narrows where M4 can live.

## The finding

e2xx (#123): for a curve $C/\mathbb{F}_q$, RH-for-the-curve $\iff$ the trigonometric **moment
matrix** $[c_{|j-k|}]$ is PSD (Carathéodory–Toeplitz). The natural lift to $\zeta$ would be a moment
matrix of the zeros, and the cleanest arithmetic moment data are the **Li coefficients** $\lambda_n$
(Li 1997: $\lambda_n\ge0\ \forall n\iff$ RH). Does the **Li-Hankel** $[\lambda_{i+j}]$ carry RH the
way e2xx's Toeplitz matrix does over $\mathbb{F}_q$?

**No — and the reason is structural, not numerical.** A Hankel matrix $[m_{i+j}]$ is PSD iff
$\{m_n\}$ is a Hamburger moment sequence $m_n=\int x^n\,d\mu$, $\mu\ge0$; any such sequence is
**log-convex** ($m_n^2\le m_{n-1}m_{n+1}$, Cauchy–Schwarz). But $\zeta$'s Li sequence is strictly
**log-concave**: $\lambda_n\sim(n/2)\log n+cn$ (Bombieri–Lagarias), and $(n/2)\log n$ is log-concave,
so $\lambda_n^2\ge\lambda_{n-1}\lambda_{n+1}$ for all large $n$. Log-concave and log-convex are
incompatible, so $\{\lambda_n\}$ is **not** a moment sequence, and the Li-Hankel is **non-PSD even
for $\zeta$**.

Verified (16 Li coefficients from 200+ zeta zeros): termwise $\lambda_n>0$ (RH); **log-concave
14/14, log-convex 0/14**; Li-Hankel min eigenvalue negative at every size ($-0.014,-0.055,-0.137,
-0.275,-0.480$ at $2\times2$ ... $6\times6$).

## What it means

The e2xx moment-**matrix** object is **genus-faithful** — a finite Frobenius spectrum over
$\mathbb{F}_q$ gives a genuine (finite, PSD-iff-RH) moment matrix. Over $\mathbb{Z}$ the **infinite**
zeta zero-spectrum, accumulating at the archimedean point, makes the matrix **dissolve** (the
moment $C_n=\sum w_\rho^n$ diverges; the Hankel is indefinite regardless of RH). Only the
**termwise** $\lambda_n\ge0$ (the Weil form, the Level-4 object, #18/#19) survives as the M4 object
over $\mathbb{Z}$. This is the **#122 genus-1-faithfulness caveat one level up**, and it sharpens #27
from "Li log-concavity is a non-Euler detector" to the exact structural fact "the Li sequence is
log-concave, hence not a moment sequence."

**RH is unaffected:** RH is the termwise positivity $\lambda_n\ge0$, *not* the Hankel PSD. M4
untouched.

## Cross-refs

LEARNINGS #128 (the M4 attempt this is front 2's verified residue of), #123/e2xx (the moment object
that dissolves), #122 (genus-1-faithfulness), #27 (Li log-concavity = non-Euler detector, sharpened),
#18/#19 (the surviving termwise Weil form), #2 (large-$n$ Li negativity for D-H), #42/#25 (the
local-to-global gap = why the spectrum is infinite/accumulating). Built on
[`e3a_zeta_li.py`](e3a_zeta_li.py). Report: `scratchpad/m4_attempt/02_moment_gram.md`.

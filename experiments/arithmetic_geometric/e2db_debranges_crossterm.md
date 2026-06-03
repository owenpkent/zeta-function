# 2DB.1 — The de Branges / Conrey-Li per-zero cross-term Q(ρ): a NEGATIVE coordinate

> Direction 8 / the live frontier, the exact CONVERSE of [2CC.3](e2cc3_q_lift_attempt.md) #42.
> Code: [`e2db_debranges_crossterm.py`](e2db_debranges_crossterm.py).
> A confirmed negative coordinate: every primary number below was independently reproduced in
> this repo (the Conrey-Li anchor matches to 12 significant figures), not transcribed.

## The setup

The recent probe sequence localized the Direction-8 gap to "realize zeta's analytic
**continuation** as a signed pairing on the global H¹" (2CC #40, 2CC.2 #41, 2CC.3 #42).
2CC.3 showed the Connes-Consani **local** Euler/orbit data is **blind** to the zeros: it
converges only for Re(s) > 1, while the zeros live in the continuation (Re(s) = ½). This
experiment looks at the **exact converse** — a global object that *does* reach the zeros.

de Branges built exactly such an object: the Hilbert space `H(E)` of entire functions with
structure function `E(z) = ξ(1 − iz)`, whose Hermite-Biehler symmetry **is** the functional
equation `ξ(s) = ξ(1−s)` (the would-be Poincaré duality), and whose reproducing kernel pairs
the **global** zeros directly. Conrey-Li (IMRN 2000 No. 18; arXiv:math/9812166) proved the de
Branges positivity condition (3.1) implies RH — but it is **strictly stronger than RH** (it
implies GRH for all Dirichlet L simultaneously), and they showed it **fails for zeta**. The
pointwise necessary consequence of (3.1) at each zero is

$$Q(\rho) := -\mathrm{Re}\big\{\xi'(\rho)\,\xi(1+\rho)\big\} \;\ge\; 0 \quad(\text{for every zero }\rho,\text{ if (3.1) held}).$$

Conrey-Li's decisive computation: at the **34th** zeta zero `ρ₃₄ = ½ + 111.0295…i` (on the
critical line, RH-true), `Q(ρ₃₄) < 0`. The signed pairing that *does* see the zeros has the
**wrong** positivity, and it fails even where RH holds.

## Results (independently reproduced)

| # | What | Result |
|---|---|---|
| 1 | **Anchor** | With `ξ(s) = s(s−1)π^(−s/2)Γ(s/2)ζ(s)` (Conrey-Li's normalization, **no ½**), `Q(ρ₃₄) = −5.38910050718e−69`, matching Conrey-Li's published `−5.389100507182945e−69` to **12 sig figs (ratio 1.000)**. Riemann's ½-normalized ξ gives exactly **¼** of this (Q is bilinear in ξ). |
| 2 | **Sign sequence** | Among the first 50 zeta zeros, `Q(ρ_k) < 0` for **exactly one** index, **k = 34**. A global pairing that sees the zeros fails even under RH. **(Density revision, [2DB.2](e2db2_debranges_k500.py): extended to K=500, the failure is at POSITIVE DENSITY ~6% (32 of 500), not sporadic; the single-k=34 reading here was a small-sample artifact. See LEARNINGS #43.)** |
| 3 | **Suppression law** | `log₁₀|Q|` vs γ has finite-size slope **−0.655** (k=1..50; tail −0.665), converging to **−(π/2)/ln10 = −0.6822**: **twice** as steep as #38's single-Gamma `−(π/4)/ln10 = −0.3411`. Mechanism: `Q = ξ'(ρ)·ξ(1+ρ)` carries **two** completed-ξ factors; the measured sub-slopes are −0.328 and −0.326, each ≈ −(π/4)/ln10, summing to the double-Gamma law. |
| 4a | **Euler controls (RH true)** | `χ₃` (odd, cond 3): **0** negatives of 46 zeros to T=100. `χ₄` (odd, cond 4): **1** negative (k=30) to T=100. So sporadic `Q<0` occurs for *some* Euler L-functions under RH, but the **density is L-function-dependent**, not generic. |
| 4b | **D-H control (RH FALSE)** | Completed self-dual `Λ_DH` verified (`|Λ(s)−Λ(1−s)| ~ 1e−62`). Its **on-line** zeros also show sporadic `Q<0` (**1 of 28**, at γ≈40.16) — identical to RH-true zeta/χ₄, so `Q<0` is **not** an RH-violation signal. The actual off-line obstruction (pair at γ≈85.7) is double-suppressed to **|Q| ~ 1e−56**, far below #38's `1e−29` detection floor. |

The off-line D-H sign split (0.8085 → `Q<0`, partner 0.1915 → `Q>0`) is a **shift artifact** of
the non-conjugate-symmetric off-line choice; the K2 reading rests on the **magnitude** only.

## The finding (honest)

This is a **negative coordinate** and the exact **converse of #42**:

- **#42:** the *local* Euler/orbit data **cannot see** the zeros (it converges only Re(s) > 1).
- **2DB.1:** the *global* de Branges pairing **does see** the zeros — but its positivity is the
  **wrong** one (pointwise, strictly-stronger-than-RH), and it fails sporadically even when RH
  holds.

So the obstruction has moved from "cannot reach the zeros" to "reaches them with the wrong
positivity." It is the **third soft detector** after #38 (heat kernel) and #39 (Rodgers-Tao
log-gas): RH-agnostic in the buildable direction, and the actual RH violation (D-H's off-line
pair) is archimedean-suppressed below detectability — now by the **double**-Gamma law `−(π/2)`,
sharper than #38's single-Gamma `−(π/4)`.

**Implication for Direction 8 / M3.** The signed pairing that realizes the continuation must be
**RH-equivalent** — a global *sum*, like the Li coefficients `λ_n` which the project verified
positive for zeta in 3A (and negative for D-H/Epstein at large n in 3B/3B.4) — **not** the
pointwise Hermite-Biehler cross-term. A naive cup-product whose positivity is the de Branges /
Hermite-Biehler condition is doomed for the same reason Conrey-Li found: the archimedean
derivative cross-term `−Re{ξ'(ρ)ξ(1+ρ)}` already has the wrong sign at a single on-line zero.
This narrows the search for the M3 polarization.

## Honest scope

Status of each claim:
- **(i)** `Q(ρ₃₄) < 0` reproducing Conrey-Li = **numerical fact** (ratio to published 1.000 at no-½
  normalization; the ¼ at the Riemann ½ normalization is a clean bilinearity convention, not noise).
- **(ii)** "only k=34 negative among the first 50 for zeta" = **numerical observation** (new artifact,
  dps=80).
- **(iii)** the double-archimedean slope = **numerical fit**. The finite-size value is −0.655; it
  converges to −(π/2)/ln10 = −0.6822 only asymptotically. Reported as a finite-size measurement
  with the two-factor decomposition as the structural reading, not as a proved identity.
- **(iv)** "de Branges positivity is the wrong (strictly-stronger-than-RH) positivity, doomed as a
  naive Arch-2 cup-product/Hermite-Biehler signature" = **structural reading** built on Conrey-Li's
  *proved* theorems ((3.1) ⇒ GRH; the pointwise necessary condition), not a new theorem.
- **(v)** "off-line D-H buried at `exp(−(π/2)γ)`" = **numerical observation** (`log₁₀|Q| ≈ −56`) plus
  the suppression-law reading.

It does **NOT**: construct the Arch-2 signed pairing / Weil cohomology (the Direction-8 / M3 gap is
**unchanged**); prove RH or any new theorem; yield an RH test (the condition *fails* for the RH-true
case, so it cannot certify RH); or discriminate zeta from D-H in the buildable direction (sporadic
`Q<0` for both). The negativity density is L-function-dependent (χ₃ uniformly positive to T=100), so
this is **not** "generic to all Euler L-functions under RH." The one genuinely circular fragment —
Hermite-Biehler **admissibility** (monotonicity of `|E(x+iy)|` in y), which is RH repackaged and which
D-H fails — is flagged and deliberately **not** computed as a test.

**Durable content:** (a) the per-zero sign sequence (new to the project), (b) the double-archimedean
law `−(π/2)` confirmed asymptotically (new, sharper than #38), (c) the converse-of-#42 connection,
which tells Arch 2 the correct M3 signature must be RH-equivalent (a sum like `λ_n`), not the
pointwise cross-term.

## K1–K4

- **K1 (circularity):** clean. `Q` is computed from `ξ'/ξ` at the zeros and is *never* used to certify
  RH (its sporadic failure under RH is the whole point — there is no positivity-read-off-the-zeros
  loop). The one circular fragment (HB admissibility = RH) is flagged and not computed.
- **K2 (D-H discipline):** RH-agnostic NEGATIVE. D-H on-line zeros give the same sporadic `Q<0` as
  zeta/χ₄; the off-line obstruction is suppressed below the floor. A valid negative coordinate, the
  third soft detector after #38/#39.
- **K3 (function-field):** N/A by construction — the de Branges `H(E)` is the archimedean/analytic
  realization of the continuation; there is no Γ-factor over `F_q`. Consistent with #42's
  archimedean-continuation reading; contributes nothing new there.
- **K4 (other):** anchor reproduced to 12 sig figs; chi4 reported as **k=30 only to T=100** (the
  survey's additional k=68/77 lie beyond T=100 and were **not** claimed); off-line sign split flagged
  as a shift artifact; not a reinvention of 3A (3A/3N are *global* RH-equivalent sums `λ_n`, positive
  for zeta; `Q` is *per-zero*, strictly-stronger-than-RH, and *fails* for zeta).

## Pointers

- LEARNINGS #43 (this), #42 (2CC.3, the converse), #41 (2CC.2), #40 (2CC), #39 (Rodgers-Tao,
  de Branges fails for zeta), #38 (heat-kernel suppression law), 3A/3B (Li coefficients).
- 08A (the M1–M5 Rosati ladder); 2CC / 2CC.2 / 2CC.3.
- References: Conrey, J. B. & Li, X.-J., *A note on some positivity conditions related to zeta and
  L-functions*, IMRN 2000 No. 18, 929–940 (arXiv:math/9812166) — read for the precise condition,
  the structure function `E(z)=ξ(1−iz)`, and the k=34 / height-282 failure computations. de Branges,
  *Hilbert Spaces of Entire Functions* (1968) and the 1986 Bull. AMS announcement (cited, not
  independently read).

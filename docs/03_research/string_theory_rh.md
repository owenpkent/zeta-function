# The string-theory / high-energy-physics angle on RH

> Survey + adversarial verification, 2026-06-24 (SURVEYOR -> ADVERSARY). Scope: every serious
> string-theory / QFT connection to $\zeta$ and the Riemann Hypothesis, scored against the project's
> realization-vs-signature framework and cross-referenced to the existing repo kills, so we do not
> re-derive dead branches. Raw artifacts: `scratchpad/string_theory/{01_surveyor,02_adversary}.md`.

## Bottom line (read this first)

**Every string-theory / QFT structure that touches $\zeta$ realizes it on the Euler/Frobenius side and
supplies realization + functional-equation duality for free; none carries the signature** (the
indefinite $(1, n{-}1)$ polarization = M4). Every thread reduces to an existing repo kill. No new
foothold.

Two honest qualifications, both from adversary review:

1. **This is NOT a clean "seventh independent all-roads confirmation."** The positivity-bearing threads
   that actually reach the zeros (reflection positivity, the metaplectic/CCM row) are **re-citations**
   of existing kills (`#43`, `#111`), not a new basis. Only the **string-native** subset (adelic
   amplitudes, SYK/$xp$, topological string) is an independent confirmation, and it lands on existing
   kills (`#42`/`#76`, `#96`, out-of-scope). The honest framing: **the string/HEP corpus closes onto
   the existing kills**; it is corpus-completing, with one genuinely new datum (an inert metaplectic
   coincidence) and one genuinely new near-miss correctly identified (Kudla).
2. **The one bankable new discriminator** (worth more than the survey itself): *any
   arithmetic-intersection route whose native output is a central **L-value or L-derivative** is in the
   BSD / Gross-Zagier / Beilinson-Bloch (order-of-vanishing) regime, **not** the RH regime. RH needs
   the **signature of the pairing across all heights**, not the rank/derivative at the center.* This
   cleanly separates the Gross-Zagier family from the RH target and is the correct kill for the Kudla
   thread below.

## The scorecard

Legend: (R) realizes $\zeta$/an L-function; (S) signature/positivity (Level 4) or only
realization/Level 3; (K2) injects Euler/Frobenius arithmetic discriminating $\zeta$ from D-H.

| Thread | (R) | (S) | Reduces to (existing kill) |
|---|:--:|:--:|---|
| Freund-Witten adelic Veneziano (product formula $\prod_v A_v = $ const) | yes | no (= FE) | `#42`/`#76`: Tate functional equation, K2-blind duality (the "perfectness" half) |
| $p$-adic string field theory (Volovich, Sen rolling tachyon) | yes | no | `#76`: Euler-side realization |
| $p$-adic AdS/CFT (Bruhat-Tits tree; Gubser et al., Heydeman-Marcolli-Saberi-Stoica) | yes | no | `#76`: the geometric face, closest, still definite |
| He-Jejjala-Minic "Veneziano $\to$ Riemann" | yes | no | Arch-3 Li criterion (archimedean, not a new positivity) |
| SYK / Schwarzian / Berry-Keating $xp$ / near-AdS$_2$ | yes | **no, Level 3** | `1C` + `#96`: spectral statistics, robust to one off-line zero |
| Topological string Gopakumar-Vafa / MacMahon constant maps | values | no | zeta **values** ($\zeta(-1)$, $-1/12$), not zeros: numerology, out of scope |
| Metaplectic / Weil rep $\to$ CCM semilocal prolate | yes | strategy | **= QM `#111`** (the same M4 object, door ajar) |
| Modular bootstrap / 2d-CFT unitarity; matrix models; no-ghost (Goddard-Thorn) | yes | **no, definite** | `#43`/`#95`/`#111`: the easy (unitarity) half |
| Worldsheet OS reflection positivity (FE-reflected) | yes | reaches zeros | **`#43` de Branges / Conrey-Li** (already built as Mechanism 4, strictly stronger than RH, fails for $\zeta$) |
| Arithmetic Kudla / Borcherds-Howe theta lift (indefinite $O(n,2)$) | yes | **proven, but wrong invariant** | Arakelov / Faltings-Hriljac face (B-tier); see below |

## The threads, grouped by failure mode

**Euler-side realization (reduces to `#42`/`#76`).** The adelic / $p$-adic string is the structurally
interesting subset: the Freund-Witten product formula $\prod_v A_v(s) = 1$ for Veneziano amplitudes is
literally the Tate functional equation / the adelic product, and $p$-adic string field theory and
$p$-adic AdS/CFT live on the Bruhat-Tits tree at a single prime. This is exactly the Euler/Frobenius
side where the K2 firewall says the polarization must live, but the string-amplitude framing supplies
**realization + duality**, the same easy two-thirds as Connes / Bost-Connes / the Euler Crystal (ECC),
not the signature. The "adelic ferromagnet" version of this is already killed (`#76`) as a
continuation-wall (`#42`) restatement.

**Level 3 (reduces to `1C` + `#96`).** The SYK / Schwarzian / near-AdS$_2$ / $xp$ line (Garcia-Garcia-
Verbaarschot; the Berry-Keating-to-black-hole dictionary) produces zeta-like spectral **statistics**
(GUE / random-matrix), which is Level 3 in the four-level framing: compatible with a $\beta = 0.51$
world, hence unable to close RH. It is the same wall as the closed spectral experiments `1A`-`1C`, in
holographic clothing.

**Reflection positivity = de Branges (`#43`).** This is the one string/QFT positivity that genuinely
*reaches the zeros*, so it is the most important reduction to get right. Bare worldsheet / 2d-CFT
Osterwalder-Schrader positivity is **unitarity** = a definite cone = the easy half. To make it see the
zeros you must reflect across the FE involution $s \to 1-s$ with the $\Gamma$-factor inserted (an
FE-isometry); the completed object is exactly de Branges $\mathcal{H}(E)$ / Hermite-Biehler positivity,
which Conrey-Li (2000) proved is **strictly stronger than RH and fails for $\zeta$** (at the 34th zero,
on the line, with RH true). This is already built and killed in-repo as Mechanism 4 of
`building_the_missing_positivity.md` (`#43`). No string-specific reflection hyperplane escapes: any
hyperplane other than $\mathrm{Re}=1/2$ is not an FE-isometry and yields the bare definite cone; the
modular ($\tau \to -1/\tau$) reflection is the modular-bootstrap unitarity, definite, the same easy
half.

**The metaplectic coincidence: real but inert (= `#111`).** The 2024 CCM semilocal prolate operator
(`#111`, arXiv:2310.18423) is built on the metaplectic representation of $\widetilde{SL(2,\mathbb{R})}$,
which is *also* the string worldsheet / Weil-representation structure (theta functions, Siegel-Narain
lattice sums transform under $\mathrm{Mp}(2,\mathbb{Z})$). The coincidence is genuine but **inert**: the
shared metaplectic rep is the **realization / duality vehicle** in both, while the CCM positivity comes
from the separate **Sonin-space radical-conditioning of the indefinite Weil form**, which has no
worldsheet counterpart. The natural worldsheet positivity (the no-ghost / Goddard-Thorn theorem) is
**definite** (unitarity, no negative-norm states) -- the opposite signature-type from the Sonin
conditioning of an *indefinite* form -- so it cannot transfer. Definite positivity (the easy half)
never feeds the indefinite signature (the hard half). This row is the same M4 object as `#111`, not an
independent confirmation of it.

**The Kudla theta lift: the serious near-miss (reduces to the Arakelov face, but $t$-LOADED).** The
indefinite Siegel-Narain / Borcherds-Howe theta lift is the one string object that natively carries an
indefinite $(p,q)$ signature -- exactly the shape of the M4 target -- so it earned a full steelman. The
naive dismissal ("free Narain moduli, $t$-blind") is **wrong**: the *arithmetic* Kudla theta lift is
$t$-**loaded**. Its special cycles $Z(T)$ on an orthogonal/unitary Shimura variety lift to arithmetic
Chow groups $\widehat{CH}^*(\mathcal{X})$ over $\mathrm{Spec}(\mathbb{Z})$, and the Kudla-Millson
generating series $\sum_T \hat Z(T) q^T$ is a modular form whose Gillet-Soulé / Faltings-Hriljac heights
provably equal **derivatives of L-functions** (Kudla's central conjecture; proven in cases by
Kudla-Rapoport-Yang, Bruinier-Yang, Yuan-Zhang-Zhang). This is the most arithmetically loaded theta
lift in mathematics. It still reduces to the existing Arakelov / Faltings-Hriljac M4 face (B-tier), for
three sharper reasons:
- **(R-a, decisive) Wrong invariant.** The Kudla height is a **central L-derivative** (Gross-Zagier /
  Beilinson-Bloch / order-of-vanishing regime): it detects the order of vanishing of $L$ at the central
  point $s=1/2$, BSD-type information, **completely orthogonal** to RH's content (the *location* of all
  zeros). The Faltings-Hriljac positivity here is positive-*definiteness* of a height pairing on a
  Mordell-Weil-type group, not the $(1, N_{\text{off}})$ signature on a primitive $H^1$.
- **(R-b) Codimension-1 / single Shimura variety.** Where the heights are proven (Bruinier-Yang,
  Yuan-Zhang-Zhang, arXiv:1304.3538), they are codim-1 special divisors on one Shimura variety -- the
  repo's already-pinned "too local + codim-1" wall. The RH-relevant instance is a higher-codimension
  Frobenius correspondence $\Gamma_S$ (bidegree $(1,p)$) on a self-product, where the Kudla-Rapoport
  height conjectures are **open**.
- **(R-c) No self-product, no $\Gamma_S$.** No $\mathrm{Spec}(\mathbb{Z}) \times
  \mathrm{Spec}(\mathbb{Z})$, no Frobenius correspondence carrying the von Mangoldt self-intersection.

It enters the B-tier list (Gross-Schoen/Ceresa, adelic Hodge index) as a fourth costume for the **same**
residual, with the handicap that its native invariant is the wrong one. No new-foothold flag.

## Crank filter

Serious mathematical physics kept and scored: Freund-Witten, He-Jejjala-Minic, Gubser et al.,
Heydeman-Marcolli-Saberi-Stoica, Connes-Consani / CCM, the arithmetic Kudla program (Kudla,
Kudla-Millson, Kudla-Rapoport, Bruinier-Yang, Yuan-Zhang-Zhang, Gross-Zagier). Discounted as numerology
/ no-venue: El Naschie, "RH emerges in dynamical quantum phase transitions", Tamburini-Licata (correctly
self-marked heuristic), and topological-string zeta-**value** appearances (zeta-regularization $\neq$
RH). The Kudla program was the one serious result the survey first under-weighted (dismissed under a
string-side strawman); it is named, scored, and killed above so a future surveyor does not re-discover
it as a fresh foothold.

## What this contributes

A negative coordinate plus one reusable tool. The string/HEP shelf is now closed onto the existing
kills, with the genuine positivity candidate (reflection positivity) confirmed as the already-killed de
Branges object, the holographic line confirmed Level-3, and the adelic/$p$-adic string confirmed an
Euler-side realization. The durable takeaway is the **L-value/L-derivative discriminator**: it retires
the entire Gross-Zagier / BSD-flavored family (including the deepest arithmetic theta lift) from the RH
search in one line, by regime rather than case-by-case. Cross-refs: `#43` (de Branges), `#76`/`#42`
(adelic ferromagnet / continuation wall), `#95` (Lee-Yang), `#96`/`#97`/`#98` (the crazy-idea / engine
/ frame-audit screens), `#111` (the QM run / CCM metaplectic), `#71` and `spec_z_cohomology_landscape.md`
(the Faltings-Hriljac / Arakelov B-tier face), `all_roads_to_the_signature.md` (the convergence).

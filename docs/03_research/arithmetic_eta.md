# The arithmetic eta invariant: constructed, closed-formed, and typed

**Status:** BUILDER round, 2026-08-19. Discharges reopen trigger 2 of
[`arithmetic_chern_simons_door.md`](arithmetic_chern_simons_door.md) section 6.
**Probe:** [`experiments/spectral/e1ac_arithmetic_eta.py`](../../experiments/spectral/e1ac_arithmetic_eta.py) (18/18, npz saved).
**Data:** the repo's Oliveira e Silva Dirichlet zeros ([`DATASETS.md` §5](../../experiments/primes/DATASETS.md)), 10,000 zeros per character at 20 decimals.
**Parent thread:** [LEARNINGS #176 → #177 → #178](../../experiments/LEARNINGS.md).

#177 closed the arithmetic Chern-Simons door with three reopen triggers, the
sharpest being "an arithmetic eta invariant": a real-valued spectral-asymmetry
invariant whose mod-Z reduction is the torsion (root-number) layer, the way the
Atiyah-Patodi-Singer eta invariant lifts the Chern-Simons invariant of a flat
connection. This round **builds it**. The result is a complete object: it
exists, it has a closed form, its torsion shadow is exactly the #177 layer, its
variation is prime-local with no archimedean bulk term, and it is **provably
RH-blind**, for a structural reason that is itself the round's most useful
product. The trigger is discharged: the arithmetic eta exists and is not the
missing object.

---

## 1. The construction

The abelian flat connections of $\operatorname{Spec}(\mathbb{Z})$ (minus a
conductor) are the primitive Dirichlet characters $\chi$. The **signed
spectrum** of $\chi$ is the zero multiset of the completed
$\Lambda(s,\chi)$ read as $\{\gamma : \Lambda(\tfrac12 + i\gamma, \chi) = 0\}$.
Conjugation gives $Z(\bar\chi) = -Z(\chi)$, so:

- for **real** $\chi$, and for $\zeta$ itself (the trivial connection), the
  spectrum is symmetric and every spectral asymmetry vanishes;
- the invariant lives on the **complex** characters, exactly as the APS rho
  invariant lives on the nontrivial flat connections.

Define, APS-style,

$$\eta(\chi) := \lim_{t \to 0^+} \sum_{\gamma \in Z(\chi)} \operatorname{sign}(\gamma)\, e^{-|\gamma| t}.$$

Data note that makes this measurable at all: the negative-$\gamma$ zeros of
$\chi$ are the positive-$\gamma$ zeros of $\bar\chi$, so the repo's conjugate
file pairs give the full signed spectrum. Six conjugate pairs used
($q = 5, 7, 7, 11, 11, 11$; characters built from the files' exact rational
$\theta$-tables, multiplicativity and the functional equation re-verified at
25 dps, completeness tracked against Riemann-von Mangoldt).

## 2. The three measured laws

**Existence (T3).** Abel regularization (heat-kernel sums extrapolated
$t \to 0$) and Cesàro regularization (window means of the counting asymmetry
$D(T) = N^+(T) - N^-(T)$) agree to $\lesssim 7 \times 10^{-4}$ on every pair.
The invariant is real and well-defined.

**C1, the closed form (T4).** Derived by the argument principle (the
$\Gamma$/conductor factors cancel between $\chi$ and $\bar\chi$; the mean of
$S(T,\chi)$ vanishes because $\int_{1/2}^\infty \log|L|\,d\sigma$ converges),
then measured:

$$\boxed{\ \eta(\chi) = -\frac{2}{\pi}\, \arg L(\tfrac12, \chi)\ }$$

with the branch continued **along the real axis from $\sigma = +\infty$**.
Match: $2 \times 10^{-4}$ absolute on every pair, regression slope $1.0002$
across a family whose $\eta$ values span $-0.093$ to $-0.722$. The winding
integer (continued minus principal argument, in units of $2\pi$) is $0$ for
all six small-conductor characters and is reported by the probe as the
invariant's integer-ambiguity bookkeeping.

| $q$ | character pair | $\eta$ measured | $\eta = -\frac{2}{\pi}\arg_c L(\frac12)$ |
|---|---|---|---|
| 5 | quartic (001/003) | $-0.1764$ | $-0.1762$ |
| 7 | (002/005) | $-0.3738$ | $-0.3737$ |
| 7 | (003/004) | $-0.1466$ | $-0.1465$ |
| 11 | (001/009) | $-0.0932$ | $-0.0930$ |
| 11 | (002/008) | $-0.2078$ | $-0.2076$ |
| 11 | (003/007) | $-0.7224$ | $-0.7221$ |

**C2, the torsion shadow (T4).** Since
$\arg_c \Lambda(\tfrac12,\chi) = \tfrac12 \arg \varepsilon(\chi) \bmod \pi$,

$$\eta(\chi) \equiv -\tfrac{1}{\pi} \arg \varepsilon(\chi) \pmod 2,$$

verified exactly. **The mod-2 reduction of the R-valued lift is the
root-number phase**, i.e. precisely the torsion layer #177 measured as the
entire signature content of the arithmetic Chern-Simons boundary. This is the
APS pattern (rho mod Z = CS of the flat connection) realized in arithmetic, and
it says where the lift's extra content sits: in the winding of $L(\sigma,\chi)$
along the real segment, which is zero-counting data.

**C3, the variation formula (T2).** For **odd** test functions $h$ the Weil
explicit formula loses its archimedean term identically (the $\Gamma$-density
is even in $r$), leaving

$$\sum_\rho h(\gamma_\rho) = -2 \sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt n}\, \operatorname{Im}\chi(n)\, G(\log n), \qquad G(x) = \frac{1}{2\pi}\int h(r)\sin(rx)\,dr,$$

(sign pinned by measurement, consistent to $3 \times 10^{-15}$ across cells).
Verified to $5 \times 10^{-16}$ on 12 (character, width) cells. **The variation
of eta across the character direction is prime-local with no bulk term**: the
APS locality property, exactly. Control: for even $h$ the archimedean integral
is required, and dropping it misses by exactly the measured integral
($0.1149$ at the tested cell). The bulk term exists, is exactly the archimedean
place, and decouples from the odd sector.

## 3. The kill: solvable exactly where blind

Pre-registered, and both halves landed.

**The invariant is exactly RH-blind.** $\operatorname{sign}(\gamma)$ never
references $\beta$: an off-line pair $(\beta, \gamma), (1-\beta, \gamma)$
counts as two zeros at height $\gamma$ regardless of $\beta$. Moving zeros off
the line changes $\eta$ by nothing at all, not by something small.

**The variation is exactly RH-blind in the D-H direction.** A
Davenport-Heilbronn off-line quadruple (real coefficients + FE force
$\gamma$-symmetry) enters every odd test function in an exactly cancelling
configuration: measured $|{\sum}| = 0.0$ against per-term scale $8.6$ at the
repo's landmark zero $0.8085 + 85.699i$. Algebraic zero, not exponential
smallness. The even-$h$ control sees the same quadruple at $O(\delta^2)$
(measured $1.1 \times 10^{-4}$), which is the familiar #158-class weak
sensitivity.

**Beurling: unposable.** The variation identity's two sides consume the
lattice half (the completed $\Lambda$, the zero side) and the Euler half
(the $\Lambda(n)$ prime side) respectively. No FE, no identity. So the eta
construction **pays the full conservation-law tariff, and what it buys is an
odd-sector observable.**

The structural summary, and the round's reusable coordinate:

> **The odd sector of the explicit-formula observable algebra is exactly
> solvable, and exactly RH-blind. RH is purely even-sector.**

The parity decomposition unifies three banked facts. The even-sector
statistics (GUE, pair correlation) are RH-blind because they see only the
multiset $\{\gamma\}$ ([`PRIME_PATTERNS.md`](../../experiments/primes/PRIME_PATTERNS.md), #174).
The odd sector is RH-blind because off-line motion is $\gamma$-symmetric
(this round, exact). What remains RH-sensitive in the EF layer is the
exponentially suppressed $\operatorname{Im}\gamma$ corrections, the #158 blind
class. And the solvable/blind coincidence is the #170 pattern ("free exactly
where information-free") appearing as a parity decomposition: the half of the
observable algebra that admits a closed form is the half that carries no RH
bits.

## 4. Honest placement

- **Novelty is in the assembly, not the counting constant.** Zero-counting
  formulas for complex characters, including argument terms, are classical
  territory (the Riemann-von Mangoldt / Selberg line). What this round adds is
  the eta-typed assembly: the APS dictionary verified end to end (existence,
  closed form, torsion shadow = CS layer, prime-local variation, vanishing
  bulk term), plus the exact-blindness theorem-shape and its measurement.
- **The archimedean path remark.** In topology the R-valued lift of eta comes
  from a path of connections through the bulk of connection space. Arithmetic
  connection space (characters) is archimedean-ly discrete; the path that
  exists and was used here is the **real-axis path in the $s$-plane**
  ($\sigma: \infty \to 1/2$), and $p$-adic paths exist in weight space (the
  Iwasawa direction, matching the corpus's one $\mathbb{Z}_p$-valued limit and
  ACS II's "related to $p$-adic L-functions" aside). The unique archimedean
  path available produces exactly central-argument data: special-value regime
  by the #113 discriminator.
- **What an eta would have to be to matter for M4.** A single number per
  connection cannot be a polarization. The M4-shaped object would be an
  eta-FORM: a second variation on a growing space with forced indefinite
  signature, and that is the Weil-positivity statement itself. The trigger
  list of [`arithmetic_chern_simons_door.md`](arithmetic_chern_simons_door.md)
  section 6 shrinks: trigger 2 is discharged (built, measured, typed:
  not the missing object); triggers 1 and 3 stand.

## 5. Artifacts

[`e1ac_arithmetic_eta.py`](../../experiments/spectral/e1ac_arithmetic_eta.py)
(18/18; T0 characters-from-headers, T1 completeness, T2 variation formula +
even control, T3 two-regularization existence, T4 closed form + shadow +
winding, T5 the kill), `e1ac_arithmetic_eta.npz` (eta table + zero prefixes).
Background: Atiyah-Patodi-Singer I-III; Atiyah, *The logarithm of the Dedekind
$\eta$-function* (1987: eta invariant = signature defect = Rademacher function
= Shimizu L-value for mapping tori, the proven topological instance of
"eta of an arithmetic-like 3-manifold is an L-value"); Atiyah-Donnelly-Singer
1983 (per #177).

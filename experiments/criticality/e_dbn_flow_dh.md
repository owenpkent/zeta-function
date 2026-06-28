# E_DBN-FLOW: the de Bruijn-Newman FLOW's prime block is a MIRROR (D-H-blind)

> Sub-target 12.4' (Direction 12, de Bruijn-Newman criticality). Experiment
> [`e_dbn_flow_dh.py`](e_dbn_flow_dh.py). Run `python -m experiments.criticality.e_dbn_flow_dh`.
> The LAST untested non-polarization Level-4 route in the first-principles audit (LEARNINGS #133):
> the program SPECIFIED 12.4' with a prediction but never RAN it. We ran it. Nothing here is
> evidence for or against RH. Sibling experiments: [`e_dbn_kernel.md`](e_dbn_kernel.md) (the killed
> $t=0$ kernel, #38), [`e_nb_baez_duarte_dh.md`](e_nb_baez_duarte_dh.md) (the NB-BD mirror, same audit).

## The question

RH $\iff \Lambda \le 0$ for the de Bruijn-Newman constant; Rodgers-Tao (2018) proved $\Lambda \ge 0$,
so RH $\iff \Lambda = 0$: $\zeta$ sits exactly on a phase boundary (the marginal-positivity thesis
made rigorous). E_DBN1 (#38) already **KILLED** the $t=0$ **kernel** positivity $\Phi \ge 0$ as
K2-failing: an off-line zero at height $\gamma$ enters the completed-$\Xi$ kernel only at the
archimedean-suppressed level $\exp(-\tfrac{\pi}{4}d\gamma)\sim10^{-29}$ (the stealth window in the
heat basis). The **only non-pre-empted** route left in Direction 12 is the **FLOW**: does the
**PRIME block** of the heat-flow-smoothed explicit formula discriminate D-H in a way that ESCAPES
that archimedean suppression? Verdict to test: **BRIDGE** (a genuine non-polarization Level-4 D-H
discriminator, which would REOPEN the route) or **MIRROR** (the stealth window again, which CLOSES it
and confirms #38/#39 + the audit prediction).

## The flow object (the faithful 12.4', NOT the killed kernel)

The de Bruijn-Newman heat-flow family is (de Bruijn 1950; Polymath15 2019; Tao 2018-01-19)

$$H_t(z) = \int_0^\infty e^{t u^2}\,\Phi(u)\,\cos(zu)\,du,\qquad H_0(z) = \Xi(z) = \xi(\tfrac12 + iz),$$

a Gaussian $e^{tu^2}$ on the **Fourier variable** $u$. In the Polymath15 parameterization $x=e^u$ the
weight is $e^{t\log^2 x}$, so in the Weil/Guinand explicit formula, where the prime side lives on
$u=\log n$ (primes enter as $\cos(\gamma\log p)=\cos(\gamma u)$), the flow at time $t$ multiplies the
$n$-th prime-side term by the Gaussian

$$w_t(n) = \exp\!\big(t\,(\log n)^2\big)$$

(the same $b_n^t$ that appears in the Polymath15 effective approximation $A_t+B_t$). This is the
faithful 12.4' object: the heat-flow re-weighting of the **prime block** of Bombieri's explicit
formula, **not** the $t=0$ kernel positivity (killed, #38).

We start from the repo's validated decomposition (`positivity/e3f`, `e3g`, `e3h`)
$$W(f_b) = \mathrm{ARCH}(f_b) + \mathrm{PRIME}(f_b) + \mathrm{POLE}(f_b),\qquad
\mathrm{PRIME}(f_b) = -2\!\!\sum_{n<b^2}\!\frac{a_n}{\sqrt n}\,(2\log b - \log n),$$
with $a_n=\Lambda(n)$ ($\zeta$), $a_n=\Lambda(n)\chi(n)$ (Dirichlet-$L$), $a_n=b_n^{DH}$ (D-H, all
$n$, the $-f'/f$ recursion). The **flowed** prime block is
$$\mathrm{PRIME}_t(f_b) = -2\!\!\sum_{n<b^2}\!\frac{a_n\,e^{t(\log n)^2}}{\sqrt n}\,(2\log b - \log n).$$
The three L-functions: **$\zeta$** (Euler, RH-true, has pole), **$\chi_5$** = the real primitive
character mod 5 = $(1,-1,-1,1,0)$ (Euler, RH-true, entire, the closest control: same conductor 5 as
D-H), and **D-H** (no Euler, RH-FALSE, off-line zero at $0.8085+85.699i$).

**Honest scope (sign / convergence).** de Bruijn-Newman $e^{+tu^2}$ **grows**, so the full prime sum
diverges for $t>0$. The boxcar test function $f_b$ has compact Fourier support (half-width $2\log b$),
so the prime sum is already truncated to $n<b^2$; on that finite support $e^{t(\log n)^2}$ is a bounded
re-weighting and the object is well-defined. We study the flow at fixed truncation $b=20$ and report
the truncation as the controlling scope (exactly as the NB-BD sibling reported finite $T$). The
discriminator is the **trend** in $t$ and whether the D-H signal **rises above** the stealth floor.

## Validation (the experiment is WRONG if these fail)

| check | result | numbers |
|---|---|---|
| **V1** $\mathrm{PRIME}_0$ reproduces e3f $-$prime ($\zeta$, $b{=}20$) | **PASS** | $-120.3133$ vs e3f $-120.31$ |
| **V1** $W(f_0)=\mathrm{ARCH}+\mathrm{PRIME}_0+\mathrm{POLE}$ vs e3f $W_{\text{prime}}$ | **PASS** | $0.095099$ vs e3f $0.095099$ (boundary $144.40$, $-$const $-18.62$, $-\gamma_{\text{int}}\,-5.369$) |
| D-H $\mathrm{PRIME}_0(b{=}20)$ vs e3g $-$Dirichlet sum | matches | $2.830086$ |
| **V2** D-H off-line zero present (smoke test) | **PASS** | $\beta=0.8085,\ \gamma=85.6993$ (2 off-line zeros found) |
| **V3** flow normalization stated | yes | $e^{t(\log n)^2}$ prime re-weighting, NOT the $t=0$ kernel |

The $t=0$ column of $\mathrm{PRIME}_t$ **is** the repo's W(f) prime block, cross-checked to 6 digits
against e3f. The decomposition is the validated one; only the Gaussian flow factor is new.

## The flow table ($b=20$, truncation $n<400$, dps $=30$)

$\mathrm{PRIME}_t(f_{20})$:

| $t$ | $\zeta$ | $\chi_5$ (Euler) | D-H |
|---|---|---|---|
| 0.00 | $-120.3133$ | $14.7774$ | $2.8301$ |
| 0.05 | $-252.3273$ | $18.3840$ | $2.9093$ |
| 0.10 | $-656.3557$ | $28.4279$ | $1.5422$ |
| 0.20 | $-7483.94$ | $278.015$ | $-75.108$ |
| 0.40 | $-2.703\times10^{6}$ | $2.419\times10^{5}$ | $-6.190\times10^{4}$ |

$\tfrac{d}{dt}\mathrm{PRIME}_t(f_{20})$ (the flow linear response):

| $t$ | $\zeta$ | $\chi_5$ | D-H |
|---|---|---|---|
| 0.00 | $-1528.98$ | $49.098$ | $4.377$ |
| 0.10 | $-13889.5$ | $356.40$ | $-70.244$ |
| 0.40 | $-8.420\times10^{7}$ | $8.297\times10^{6}$ | $-2.011\times10^{6}$ |

All three L-functions respond to the flow with a generic blow-up driven by their **own low-$n$
coefficients** ($e^{t(\log n)^2}$ is $\approx1$ for small $n$ and the truncated sum is dominated by
them). The D-H value differs from the Euler controls by an $O(1)$ amount set by the **signs of
$b_n^{DH}$**, exactly the t=0 discrimination mechanism, not by anything the flow injects.

## Mechanism diagnosis (the scientific payload)

**1. The off-line zero is not in the prime block at all.** $\mathrm{PRIME}_t$ sums over $n<b^2=400$;
the off-line zero sits at height $\gamma=85.699$ in the **archimedean tail** and enters the completed
kernel only at $\exp(-\tfrac{\pi}{4}\cdot85.699)=5.87\times10^{-30}$ (the E_DBN1 stealth floor). The
flow re-weights the **same low-$n$ coefficients** the $t=0$ block already used; it adds **no**
off-line-zero information. The flow-induced change $\Delta(t)=\mathrm{PRIME}_t-\mathrm{PRIME}_0$ for
the Euler control $\chi_5$ (no off-line zero) and for D-H is a generic low-$n$ re-weighting of each
function's own coefficients, not a structural D-H signal.

**2. The skeptic's dual probe (zero side), answered.** A reader could object: $e^{tu^2}$ on the
Fourier side is $e^{t\gamma^2}$ on the **zero** side, which is huge at $\gamma=85.7$, so does the flow
drag the off-line zero out of the stealth window? Two facts close the door.

- **(a)** For the **boxcar** $f_b$, the off-line zero is **not** at the $10^{-29}$ kernel floor on the
  zero side: $|\Phi_b(\rho)|$ decays only **polynomially** in $\gamma$, so the off-line zero already
  contributes $8.60\times10^{-4}$ at $t=0$ (vs max on-line contribution $9.95\times10^{-2}$). **This is
  the e3c raw Weil-Gram detector** (the $\sim2.6\%$-of-spectrum signal). So the **$t=0$** Weil form
  ALREADY discriminates D-H; the flow has nothing to add to it.
- **(b)** Weighting each zero by $e^{t\gamma^2}$ does make the off-line **share** grow ($0.6\%\to41\%$
  by $t=0.001$), but the totals **DIVERGE** ($3\times10^{-1}\to1.4\times10^{14}$ by $t=0.005$). This is
  the de Bruijn-Newman $e^{+tu^2}$ divergence: the "amplification" is dominated by the largest $\gamma$
  in the (arbitrary) truncation, has no $t\to0^{+}$ limit, and is **not** a convergent positivity
  functional. The actual flow **moves** the zeros (backward heat equation $\partial_t H=-\partial_{zz}H$);
  it does not hand you a convergent re-weighted Weil form.

| zero-side $e^{t\gamma^2}$ weighting (D-H, $b{=}20$) | $t=0$ | $t=0.001$ | $t=0.002$ | $t=0.005$ |
|---|---|---|---|---|
| off-line share | $5.6\times10^{-3}$ | $4.17\times10^{-1}$ | $3.95\times10^{-1}$ | $9.5\times10^{-2}$ |
| on-line total | $3.03\times10^{-1}$ | $3.72$ | $6.30\times10^{3}$ | $1.45\times10^{14}$ |

Net: on the **prime** side the off-line zero is absent; on the **zero** side it is the **existing**
$t=0$ e3c detector, and the only flow "amplification" diverges. The flow adds no new discriminator.

## Verdict: MIRROR (and the stealth window again)

| kill-criterion read | |
|---|---|
| **K2 (D-H discipline): the flow's prime block is BLIND, not discriminating.** | $\mathrm{PRIME}_t$ never reaches the off-line zero; it re-weights low-$n$ coefficients, so it separates D-H from $\zeta$ no better than the $t=0$ block, and via the same mechanism (coefficient signs $b_n^{DH}$), not the off-line zero. |
| **K1 (signature, not trace).** | The only object the flow yields is a finite re-weighting of the explicit-formula prime coefficients (prime side) or a divergent zero-sum (zero side). No new positivity organ; it funnels back to the same critical-line data as every Level-3 / stealth-window object. |

The audit **predicted FALSE** (E_DBN1 suppression). Confirmed: the de Bruijn-Newman flow, in the
faithful prime-block representation, is a **MIRROR**. It does not supply a non-polarization Level-4
D-H discriminator. This **CLOSES sub-target 12.4'** and the last non-polarization Level-4 route in the
audit. Direction 12's RH content is exactly where #38/#39 located it: in the **flow LOCATING $\Lambda$**
(a criticality statement, Level-3-proven by Rodgers-Tao for $\Lambda\ge0$ and Level-4-open for
$\Lambda\le0=$ RH), **not** in any prime-block positivity object. The squeeze $0\le\Lambda\le\tfrac12$
straddles the Level-3/Level-4 boundary; no prime-side functional crosses it.

## What is PROVEN vs CONJECTURAL/numerical

- **PROVEN (theorem, imported):** RH $\iff\Lambda=0$ (Rodgers-Tao $\Lambda\ge0$, 2018; de Bruijn
  $\Lambda\le\tfrac12$). $H_t(z)=\int e^{tu^2}\Phi(u)\cos(zu)du$ and the $e^{t\log^2 n}$ prime
  re-weighting (Polymath15 effective approximation). Bombieri's explicit formula and its
  ARCH/PRIME/POLE decomposition (validated against e3f to 6 digits). The off-line zero off the
  critical line (D-H 1936, smoke test).
- **NUMERICAL (this experiment, rigorous given the truncation):** the validation triple (V1/V2/V3);
  the $\mathrm{PRIME}_t$ and $\tfrac{d}{dt}\mathrm{PRIME}_t$ tables; the zero-side dual probe (off-line
  contribution $8.6\times10^{-4}$ at $t=0$; the $e^{t\gamma^2}$ divergence). Fixed truncation $b=20$,
  $n<400$: the flow object is well-defined only on compact Fourier support, stated as such; the
  discriminator is the trend, not an absolute.
- **CONJECTURAL / scope caveat:** the prime-side $e^{t(\log n)^2}$ re-weighting is the faithful
  explicit-formula image of the de Bruijn-Newman flow on compact support; the full $t>0$ flow on
  $\Xi$ is a backward-heat deformation of the zeros, which no finite prime-block object captures
  convergently (that is the point). The MIRROR verdict is about the convergent prime-block object,
  which is the one sub-target 12.4' asked for.

## Cross-refs

[`e_dbn_kernel.md`](e_dbn_kernel.md) (the killed $t=0$ kernel, #38; same stealth law
$\exp(-\tfrac{\pi}{4}d\gamma)$ in the heat basis; this is its **flow** sibling), 
[`e_nb_baez_duarte_dh.md`](e_nb_baez_duarte_dh.md) (the NB-BD mirror; same audit, same
BRIDGE-vs-MIRROR structure, same stealth-window mechanism), the Weil-form prime-side builders
([`../positivity/e3f_weil_prime_side.py`](../positivity/e3f_weil_prime_side.py),
[`e3g_dh_prime_side.py`](../positivity/e3g_dh_prime_side.py),
[`e3h_chi3_prime_side.py`](../positivity/e3h_chi3_prime_side.py)), the raw Weil-Gram detector
([`e3c_weil_form.py`](../positivity/e3c_weil_form.py), the $\sim2.6\%$ off-line signal), the D-H
discipline (`experiments/_shared/davenport_heilbronn.py`), Direction 12
([`../../docs/03_research/research_directions/12_debruijn_newman_criticality.md`](../../docs/03_research/research_directions/12_debruijn_newman_criticality.md),
sub-target 12.4'). References: de Bruijn 1950; Newman 1976; Rodgers-Tao, *Forum Math Pi* 8 (2020),
arXiv:1801.05914; Polymath15, *Res. Math. Sci.* (2019), arXiv:1904.12438; Balanzario-Cárdenas-Chacón,
*A smooth version of Landau's explicit formula*, arXiv:2311.04347 (2023); Dobner, arXiv:2005.05142;
Newman-Wu, arXiv:1901.06596.

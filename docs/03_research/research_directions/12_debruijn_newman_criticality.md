# Direction 12: RH as exact criticality (a variational proof that the de Bruijn-Newman constant is zero)

> **Status: speculative, proposed 2026-05-30.** Turns the project's marginal-positivity thesis from a mood into a theorem target.
>
> **Headline.** Rodgers-Tao (2020) proved the de Bruijn-Newman constant $\Lambda \ge 0$, and $\mathrm{RH} \Leftrightarrow \Lambda \le 0$, so $\mathrm{RH} \Leftrightarrow \Lambda = 0$. That is *literal criticality*: $\zeta$ sits exactly on a phase boundary. Prove RH as a **statistical-mechanics criticality theorem** by exhibiting a free-energy functional whose unique critical point is $\zeta$ with no symmetry breaking. Promotes the project's Level-3 multifractal thread to a Level-4 tool.

## 1. The idea in one paragraph

The marginal-positivity thesis ("RH is just barely true, no buffer for soft proofs," the project's central structural finding) has an *exact* mathematical avatar: $\Lambda = 0$. The de Bruijn-Newman flow $H_t$ is a heat flow on the zeros; $\Lambda$ is the time at which all zeros become real. RH $\Leftrightarrow \Lambda = 0$ says $\zeta$ is exactly critical. Direction 12 proposes to build a **free-energy functional** $F[\cdot]$ on the (log-correlated) zero field such that the de Bruijn-Newman flow is its gradient flow, $\partial_t(\text{config}) = -\,\mathrm{grad}\,F$, and to prove $\Lambda = 0$ as "no spontaneous symmetry breaking": the order parameter (off-line displacement) stays zero along the flow. The Euler product enters as the **interaction term** that pins the field to be exactly log-correlated (critical), rather than super- or sub-critical.

## 2. Formal kernel

- **Order parameter.** $m = $ mean-square off-line displacement of zeros, $m = 0 \Leftrightarrow$ RH.
- **Free energy.** $F[\mu] = $ a rate functional on the zero point process $\mu$, built from the explicit formula read as an energy: a logarithmic (Coulomb / log-correlated) pair interaction plus an arithmetic potential from the prime side $\sum_p (\log p)\,\hat\phi(\log p^k)$.
- **Flow.** Identify $H_t$ (de Bruijn-Newman) with $-\mathrm{grad}\,F$ under the right metric (Wasserstein / Dirichlet form on the field).
- **Criticality theorem.** Show $\zeta$ is the unique stationary point with $m=0$, and that the arithmetic interaction forbids a symmetry-broken ($m>0$) phase. $\Lambda = 0$ follows.

The link to the project's existing work: the multifractal experiments (E0-E3) already model the log-correlated structure of $\log|\zeta|$. Direction 12 supplies the missing Level-4 ingredient: the arithmetic interaction that makes criticality (Level 4) rather than mere log-correlation (Level 3).

## 3. Why it could break Davenport-Heilbronn (K2)

D-H has off-line zeros, hence its analogue $\Lambda_{DH} > 0$: it is **not** critical, it has already symmetry-broken ($m_{DH} > 0$). The functional $F$ must be built from the Euler product so that "criticality at $\Lambda=0$" is an *arithmetic* statement. A generic log-correlated field (Level 3) is compatible with a broken phase (some zero at $\beta = 0.51$); only the arithmetic interaction forces $m=0$. This is the project's Level-4-not-Level-3 commitment made into the engine of the proof: D-H realizes the broken phase the generic field permits.

## 4. Kill-criteria status

- **K1 (signature not trace):** borderline. The positivity here is *variational* (a free energy is minimized / a Hessian is positive), not a trace identity and not literally a Hodge signature. Whether this counts as escaping R3.5 depends on the Hessian being a genuine new positivity input rather than the explicit formula in disguise. This is the direction's main risk and must be checked early.
- **K2:** clean ($\Lambda_{DH} > 0$, D-H is supercritical).
- **K3:** for a curve over $\mathbb{F}_q$, "criticality" should be the statement that Frobenius eigenvalues sit exactly on $|{\cdot}| = \sqrt q$, i.e. Weil's bound as a marginal condition. Milestone 12.3.

## 5. First step (reuses E0-E3 multifractal thread)

Construct the candidate $F$ numerically from the explicit formula (log-correlated interaction + prime potential) and measure whether $\zeta$'s zero configuration is a **critical point** ($\mathrm{grad}\,F \approx 0$) while D-H's is not ($\mathrm{grad}\,F$ points off-line). If running the de Bruijn-Newman flow on the D-H zeros reveals a nonzero order parameter that the same functional assigns to $\zeta$ as exactly zero, Direction 12 has a variational D-H discriminator and earns further work. The numerics reuse the multifractal field machinery already in `experiments/multifractal/`.

## 6. Honest assessment

Probability of closing RH: medium-low, and gated on the K1 question (is the variational positivity genuinely new input?). The appeal is that it gives the marginal-positivity thesis a precise theorem to aim at ($\Lambda = 0$ as criticality) and recruits the project's existing Level-3 multifractal work toward a Level-4 goal, which no other direction does. Even a partial result (a rigorous free-energy whose gradient flow is the de Bruijn-Newman flow) would be a notable contribution to the spectral/statistical-mechanics view of RH.

## 7. References

- Rodgers, B.; Tao, T. (2020). *The de Bruijn-Newman constant is non-negative*. Forum Math. Pi 8.
- Newman, C. (1976). *Fourier transforms with only real zeros*. Proc. AMS 61.
- de Bruijn, N. G. (1950). *The roots of trigonometric integrals*. Duke Math. J. 17.
- Polymath15 (2019). *Effective approximation of heat flow evolution of the Riemann xi function*. Res. Math. Sci.
- Project: `docs/02_graduate/log_correlated_fields_intro.md` (four-level framing), `experiments/multifractal/` (E0-E3).

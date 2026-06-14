# 2OO: the P3-P4 von Neumann probe (the live frame-audit edge)

> Experiment [`e2oo_vonneumann_rosati_probe.py`](e2oo_vonneumann_rosati_probe.py). Follow-up to the regime-two frame-audit (LEARNINGS #98, [`optimizing_rh_for_ai.md`](../../docs/03_research/optimizing_rh_for_ai.md)). Result recorded as LEARNINGS #99. Sits in the 08A Rosati ladder.

## The question

The frame-audit found the M4 property graph has exactly one live edge, **P3-P4**, graded CORRELATED (not GENUINE) in the polarized-Frobenius / Rosati frame:

- **P3 = noncircular**: the positivity comes from an intrinsic polarization, never read off the zeros.
- **P4 = euler-gated**: the algebra exists only with an Euler product (the Davenport-Heilbronn firewall).

The audit's sharpest next probe: does **requiring the arithmetic Frobenius algebra $\mathcal{A}$ to be a finite von Neumann algebra with a faithful normal tracial state** upgrade the edge from CORRELATED to GENUINE? That is, does "$\mathcal{A}$ exists and is euler-gated" become co-extensive with "$\mathcal{A}$ carries an intrinsic positive Rosati involution"?

A finite von Neumann algebra with a faithful normal trace $\tau$ carries a canonical intrinsic positive form for free, the GNS / trace inner product $\langle a,b\rangle = \tau(b^* a)$, positive-definite by faithfulness. So naively the upgrade succeeds: existence of the traced algebra forces intrinsic positivity. The probe asks whether that is the **right** positivity, the one that reaches P5 (the indefinite $(1,n-1)$ Hodge index that IS RH).

## The result: CORRELATED, not GENUINE (three obstructions, on small models)

Running the experiment establishes four structural facts, each a concrete computation:

1. **A faithful trace gives an intrinsic positive form.** On $M_2(\mathbb{C})$ with the normalized trace, the GNS Gram matrix has minimum eigenvalue $0.5 > 0$: positive-definite. So P3-intrinsic-positivity is genuinely free once you have the traced algebra. The upgrade's premise holds.

2. **But that form is positive-DEFINITE, never the M4 Hodge polarization.** The trace-form signature is $(4,0,0)$, positive-definite by construction ($\tau(xx^*)\ge 0$, $=0$ iff $x=0$). M4's polarization is not positive-definite: the full Hodge index is indefinite $(1,n-1)$, equivalently the 2G primitive form $G_{\mathrm{prim}}=\begin{psmallmatrix}-2g&-t\\-t&-2gq\end{psmallmatrix}$ is negative-definite under Hasse-Weil (eigenvalues $\approx(-10.12,-1.88)$ at $g{=}1,q{=}5,t{=}1$). Either way it is not the positive-definite trace form. **The very property that makes the upgrade work (faithfulness $\Rightarrow$ PD) is what makes it the wrong signature.**

3. **The natural arithmetic state is a KMS state, not a trace.** A Gibbs/KMS state $\omega(x)=\mathrm{Tr}(\rho x)$ with $\rho=e^{-\beta H}/Z$ for a non-scalar Hamiltonian $H$ (the modular generator = the scaling / Frobenius flow) is not tracial: at $\beta=1$, $\omega(E_{12}E_{21})=0.731 \neq 0.269=\omega(E_{21}E_{12})$. The modular flow makes the arithmetic algebra type III (Bost-Connes is type III$_1$, LEARNINGS #81), which has no faithful normal trace at all. So the upgrade's hypothesis is not even satisfied by the natural algebra.

4. **The trace form is D-H-blind (not euler-gated).** The GNS/trace form is defined for any $\ast$-algebra with no reference to primes or an Euler product (zeta has an Euler product, Davenport-Heilbronn does not, but the trace form exists for both). A soft positivity, not the euler-gated M4 form.

## Reading

The upgrade yields P3 from P4 only as a **definite, D-H-blind positivity on a type II$_1$ algebra the arithmetic does not provide** (it is type III$_1$). It reaches the wrong positivity three different ways, so the edge stays CORRELATED, not GENUINE, for the RH-relevant (indefinite, euler-gated) positivity. **P5 stays isolated**, confirming the frame-audit's prediction (NONE-or-CORRELATED).

The value is a named residual. M4 is exactly the gap between the **free definite trace form** and the needed **indefinite $(1,n-1)$ euler-gated Hodge form**. This is the 2MM transport result (LEARNINGS #68) restated in operator-algebra language: a faithful trace fixes the form to be positive-definite, while M4 needs it indefinite, so the trace supplies no progress toward the Hodge signature. A negative coordinate, and a sharp one: it closes the "make P3-P4 an iff via a trace" route and tells the construction work that the polarization on $\mathcal{A}$ must be the indefinite modular/Hodge form, not the tracial one. The modular structure ($\sigma_t$ = the Frobenius/scaling flow, type III), not a trace, is where the arithmetic lives.

## Cross-refs

- LEARNINGS #98 (the frame-audit that surfaced this edge), #99 (this result), #81 (Bost-Connes type III$_1$ / the KMS machinery), #68 (2MM: the form is transport, signature$(Q)$ = signature of whatever $B$ you supply), #43 (de Branges: another wrong-positivity, too strong).
- [`optimizing_rh_for_ai.md`](../../docs/03_research/optimizing_rh_for_ai.md) (the value-signal program), [`research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md) (the Rosati ladder this lives in).

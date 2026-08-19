# Local quantum gravity and how the primes exist

**Status:** survey + two measured results, 2026-08-19.
**Probe:** [`experiments/spectral/e1ab_automorphic_spectrum.py`](../../experiments/spectral/e1ab_automorphic_spectrum.py) (30/30).
**Papers:** `references/09_quantum_gravity/` (13 arXiv PDFs, gitignored per the references tier; index in [`references/README.md`](../../references/README.md), table in [§8](#8-sources-pulled)).
**Dataset:** 2202 level-1 Maass cusp forms, [`DATASETS.md` §17](../../experiments/primes/DATASETS.md).

This is a deep dive into the interface between quantum gravity and the existence of
the primes, aimed at one question this project actually cares about: does anything
on that interface supply the polarization that RH needs, or is it one more way of
realizing $\zeta$ as a trace without a signature?

The answer is the second one, and the interesting part is *how sharply* it is the
second one. Two things got measured rather than argued, and one of them kills a whole
family of arguments at once.

---

## 1. Why the primes exist: "local" is not a metaphor

The word "local" in "local quantum gravity" has two readings, and for this project
they are the same reading.

**Ostrowski's theorem.** Every nontrivial absolute value on $\mathbb{Q}$ is
equivalent to either the usual $|\cdot|_\infty$ or the $p$-adic $|\cdot|_p$ for
exactly one prime $p$. That is the whole list. So a prime is not primarily a number
that fails to factor. A prime **is a way for $\mathbb{Q}$ to be local**: a completion,
a place, a local field $\mathbb{Q}_p$. The primes exist because $\mathbb{Q}$ has
exactly these completions and no others, and the integers' multiplicative structure
is the shadow of that classification, not its cause.

This is the cleanest available answer to "how do the primes exist," and it is
already a physics statement. A theory over $\mathbb{Q}$ is a theory with one local
sector per place. The archimedean place $\mathbb{R}$ is one sector among infinitely
many, distinguished only by being the one we can see.

**The product formula is a conservation law.** For $x \in \mathbb{Q}^\times$,

$$\prod_v |x|_v = 1,$$

the product running over all places including $\infty$. Every local theory can be
deformed, but the total is pinned. This is the adelic Gauss law, and it is the
structural reason a local-to-global principle exists at all.

**Tate's thesis is the partition function.** Fourier analysis on
$\mathbb{A}_\mathbb{Q}/\mathbb{Q}$ produces $\zeta$ as a product of local integrals,
one per place, with $\Gamma$-factor at $\infty$ and Euler factor $(1-p^{-s})^{-1}$ at
$p$. The functional equation is Poisson summation on the adeles. So $\zeta$ *is* an
adelic partition function, and it already has the shape a physicist wants: local
factors multiplying, one global constraint.

**The Volovich hypothesis** (1987) takes this literally: below the Planck length the
archimedean description fails and spacetime is non-archimedean, so physics should be
written $p$-adically or adelically. Thirty years of $p$-adic mathematical physics
follow (`arxiv_1705.04758.pdf` in `references/09_quantum_gravity/`). It is a real program and it is the honest sense in
which "local quantum gravity" and "the primes" are the same subject.

**Where this repo already stands on it.** The Beurling discipline
([`experiments/_shared/beurling.py`](../../experiments/_shared/beurling.py),
LEARNINGS #152) is exactly the statement that the adelic package has two independent
halves. Davenport-Heilbronn has the functional equation without the Euler product.
A Beurling generalized prime system has the Euler product without the additive
lattice, so no Poisson summation and no theta functional equation. $\zeta$ is the
intersection, and Tate's thesis is the assembly. Everything in §5 below is an
application of that bracket.

---

## 2. Five mechanisms by which primes enter a gravitational theory

The literature has more unity than it looks. There are essentially five ways a prime
can show up in a physical model, and knowing which one a paper is using predicts what
it can and cannot prove.

| # | Primes appear as | Produces | Canonical example | Eats Euler product? | Eats lattice/FE? |
|---|---|---|---|---|---|
| 1 | **Places** of $\mathbb{Q}$ | $\zeta$ as adelic partition function | Tate's thesis; Connes' adele class space | yes | yes |
| 2 | **Knots** in a 3-manifold | linking numbers = Legendre symbols | arithmetic topology; Kim's arithmetic Chern-Simons | no | no |
| 3 | **Closed orbits** of length $\log p$ | dynamical $\zeta$, $-\zeta'/\zeta$ | Deninger's foliated flow; Gutzwiller/Selberg | passively | no |
| 4 | **Energy levels** $E_p = \log p$ | $Z = \zeta(\beta)$, Hagedorn pole at $\beta=1$ | primon gas (Julia); Bost-Connes | yes | no |
| 5 | **Primitivity** of a lattice vector | $1/\zeta$, via $\mu(m)$ | Godet's no-boundary condition | no | yes |

Mechanisms 1 through 4 are already in this repo's ledgers. Mechanism 3 is
[`experiments/chaos/`](../../experiments/chaos/) C4 and the Deninger dossiers;
mechanism 4 is `building_the_missing_positivity.md` Mechanism 2, killed because the
modular operator is strictly positive definite and so cannot carry an indefinite
Hodge signature.

**Mechanism 5 is new to the repo and is the genuinely interesting import.** In
Godet's quantum cosmology the Hartle-Hawking state is a Poincaré sum over no-boundary
geometries, and the no-boundary condition forbids contracting cycles that wrap a
non-primitive lattice vector. Restricting to $\gcd(n_1,\dots,n_d)=1$ and Möbius-inverting
gives $1/\zeta(s) = \sum_m \mu(m) m^{-s}$, and the state becomes a **Möbius average of
CFT partition functions**,

$$\psi_{HH} = \sum_{m \ge 1} \mu(m)\, m^{d/2 - 1} Z_{\mathrm{CFT}}[C m^d].$$

This is worth naming because it is the only entry in the table where the primes arrive
from a *geometric* condition rather than from multiplicativity, and the only one whose
native output is $1/\zeta$ rather than $\zeta$. RH then reads as square-root
cancellation in the Mertens function, which is to say as the *randomness* of $\mu$
rather than as a positivity. That is a different-shaped door. It is still not a
polarization (see §5), but it is not a re-dressing of mechanism 4 either.

---

## 3. The live constructions, 2020 to 2026

Four programs, stated at the precision needed to judge them.

### 3.1 Godet: quantum cosmology as automorphic dynamics
`arxiv_2405.09833.pdf`, `arxiv_2505.03068.pdf`

Pure Einstein gravity in $d+1$ dimensions with $\Lambda > 0$, spatial slices $T^d$.
In minisuperspace the Wheeler-DeWitt equation becomes a Klein-Gordon equation on
$GL(d,\mathbb{R})/O(d)$ with time equal to spatial volume, and the Hilbert space is
$\mathcal{H} = L^2(SL(d,\mathbb{Z}) \backslash \mathfrak{h}_d)$, square-integrable
automorphic forms for $GL(d)$. The spatial part of the WDW operator is literally the
Casimir, that is, the Laplacian on the modular moduli space. For $d=2$ the
no-boundary trajectories are geodesics in **Artin's billiard** on
$\mathbb{H}/PSL(2,\mathbb{Z})$.

The zeros enter through the Langlands spectral decomposition: the completed Eisenstein
series $\bar E_s = \Lambda(\tfrac{d}{2}s) E_s$ has $\zeta$ in the denominator, and
the Hartle-Hawking state comes out as an explicit sum over the nontrivial zeros $\rho$.
Godet then writes: *"the Hilbert-Pólya Hamiltonian, defined to have the imaginary parts
as eigenvalues, is the time evolution operator for the Hartle-Hawking state near the
singularity."*

Two things to be exact about, because they are what §4 tests.

1. That is a **definition**, not a construction. No self-adjoint operator is built and
   no spectrum is computed. Elsewhere in the same paper the same zeros are described
   correctly as *"poles of the scattering phase $\varphi(s)$, so they are purely ingoing
   or outgoing waves corresponding to resonances."* Resonances and eigenvalues are
   different objects, and the paper uses both framings.
2. RH is an **input**, used descriptively: RH is quoted as the statement that the
   near-singularity fluctuations are $O(G^{1/3})$ in $d=3$. Nothing in the construction
   is claimed to constrain zero location, and Godet does not claim otherwise. The
   adelic generalization $\psi \in L^2(GL(d,\mathbb{Q})\backslash GL(d,\mathbb{A}))$ is
   proposed but not developed.

### 3.2 LeClair: spectral flow and a unitary S-matrix
`arxiv_2406.01828.pdf`

A scattering problem whose S-matrix is built directly from the Euler product, so that
the quantized levels $E_n(\sigma)$ equal the zeros as $\sigma \to 1/2$. Because the
S-matrix is unitary by construction, the Hamiltonian "must be" hermitian and the
eigenvalues real. Spectral flow in $\sigma$ then gives a criterion for RH.

This paper is unusually disciplined for the genre and deserves credit for two things.

**It runs the D-H test itself, and passes.** Section IV takes Davenport-Heilbronn
explicitly as *"a well-known such example"* with a functional equation, on-line and
off-line zeros, and no Euler product, and shows the analogue of its Proposition 2
fails there. The stated reason is exactly this repo's reason: *"Without the Euler
product, one cannot even define the quantum scattering problem."*

**Its conclusion is this repo's conservation law, arrived at independently:**

> *"This work provides ample evidence that for the RH to be true, one needs both the
> functional equation and the Euler product."*

That is `trojan_horse_m4.md`'s tariff (consume the Euler product plus the additive
lattice at the same joint) stated from the S-matrix side by someone who was not
looking for it. Worth recording as external corroboration.

**Where it stops.** The author is explicit: *"the validity of the RH comes down to
Proposition 1, namely that the hamiltonian for the LM model and its generalizations has
real eigenvalues... We thus cannot see any obstructions to Proposition 1 at present."*
And earlier: *"Although we didn't present a formula for the implicit underlying
hamiltonian... Henceforth we assume the theory is well-defined by its dispersion
relation and its unitary S-matrix."* So the Hamiltonian is never constructed,
essential self-adjointness is never proved, and the unitarity is inherited from an
Euler product that converges only for $\sigma > 1$, which is precisely the region
where there are no zeros to worry about. This is the self-adjointness costume from
`trojan_horse_m4.md`, and it pays at the identification joint.

### 3.3 Betzios, Gaddam, Papadoulaki: gauging CPT
`arxiv_2004.09523.pdf` (SciPost Phys. Core 4, 032)

Gauging CPT as a phase-space boundary condition discretizes the continuous spectrum of
an operator related to the dilation generator, and the discretization matches zeros of
$\zeta$ and of the Dirichlet beta function. Proposed as near-horizon dynamics of the
Schwarzschild S-matrix. The authors claim a spectral realization only, saying it *"may
help the pursuit"* of RH. This is Berry-Keating with a black-hole reading, and the
repo's existing verdict on Berry-Keating (`quantum_chaos_and_the_zeros.md`, spectral
README 1A/1B/1C: density mismatch, no D-H discrimination) applies unchanged.

### 3.4 Kim: arithmetic Chern-Simons
`arxiv_1510.05818.pdf`, `arxiv_1609.03012.pdf`

The one genuine gap in this repo's coverage. Arithmetic topology says $\operatorname{Spec}(\mathcal{O}_K)$
behaves like a 3-manifold and primes behave like knots (the repo has this via the
Morishita and Li-Sia reading notes). Kim goes further and puts a **quantum field theory**
on it: an arithmetic analogue of the Chern-Simons functional on a space of Galois
representations, with Dijkgraaf-Witten invariants, decomposition formulas, and explicit
computations. Since 3d gravity *is* Chern-Simons, this is the most literal existing
sense of "quantum gravity on $\operatorname{Spec}(\mathbb{Z})$."

Honest scoping: nothing in this program currently touches $\zeta$'s zeros. It is
mechanism 2 in the table, which eats neither the Euler product nor the lattice, so by
§5 it cannot as it stands see RH. It is listed here because it is unexplored, because
it is the only candidate whose *carrier* is a genuine 3-manifold-like object with a
TQFT on it, and because Direction 8's Hodge-index target would need exactly such a
carrier. See §7.

### 3.5 Excluded

Search on these terms surfaces a large amount of material that does not survive
inspection: an "E8 holographic resolution of the cosmological constant problem," a
"spectral proof of RH employing the Forcing Lemma," and an adelic framework claiming to
resolve the Hubble tension via "adelic dimensional reduction" validated against LIGO O4
and JWST. These are on academia.edu and similar venues, are not peer reviewed, and read
as machine-generated. None is used here. Recording the exclusion because anyone
repeating this literature search will hit them in the first page of results.

---

## 4. What got measured

Two claims in §3 are checkable rather than arguable, so
[`e1ab_automorphic_spectrum.py`](../../experiments/spectral/e1ab_automorphic_spectrum.py)
checks them. 30/30.

### 4.1 The zeros are not the discrete spectrum of the modular Laplacian

If Godet's Hilbert-Pólya identification were constructive, the zeros would be
eigenvalues of the operator he actually has, the Laplacian on
$L^2(SL(d,\mathbb{Z})\backslash \mathfrak{h}_d)$. For $d=2$ that operator's discrete
spectrum is the Maass cusp forms, and the data now exist: **2202 level-1 Maass forms
pulled from LMFDB** (contributor Holger Then), $\lambda = 1/4 + R^2$.

Method, with the trap handled first. The list is **not complete over its whole range**,
and that matters more than anything else in the probe, because randomly deleting levels
from any spectrum drives its spacing statistics toward Poisson, which is the direction
of the expected answer. So the completeness horizon is measured first against Weyl's law
with the scattering correction, $N(R) \sim R^2/12 - (2R/\pi)\log(R/e\sqrt{\pi/2})$:
the staircase tracks Weyl to better than 0.5% up to $R = 100$ (617 forms) and breaks to
0.94 immediately above it. On the complete range the fitted leading coefficient is
$a = 0.083149$ against $\mathrm{Area}/4\pi = 1/12 = 0.083333$, a 0.22% confirmation of
the modular surface's area. Each parity class is then unfolded separately, since mixing
two independent spectra manufactures Poisson by itself.

Result, through one identical pipeline at matched sample size $N = 255$:

| spectrum | KS to Poisson | KS to GOE | KS to GUE |
|---|---|---|---|
| zeta zeros | 0.3440 | 0.1295 | **0.0625** |
| Maass, odd | 0.1406 | 0.1325 | 0.1822 |
| Maass, even | 0.1129 | 0.1241 | 0.1919 |

KS 5% critical value at that $N$ is 0.0852. So **GUE is accepted for the zeta zeros
and rejected for the Maass spectrum at 2.1x and 2.3x critical**, same code path, same
unfolding, same $N$. The zeros are not eigenvalues of the modular Laplacian.

The probe deliberately claims only that. It does **not** claim to resolve which class
the Maass spectrum is in: below the horizon Poisson and GOE are not separated at
$n \sim 300$, and the strong Poisson signal on the full list is confounded by the
missing levels. The argument needs only the rejection of GUE, so the ambiguity is
reported rather than papered over.

Where the zeros actually live is then unambiguous: they are **resonances**, poles of
the Eisenstein constant term $\varphi(s) = \xi(2s-1)/\xi(2s)$ in
$E(z,s) = y^s + \varphi(s) y^{1-s}$, sitting at $s = \rho/2$. Verified at 30 digits,
along with $\varphi(s)\varphi(1-s) = 1$. RH is the statement that those poles lie on
$\operatorname{Re}(s) = 1/4$.

### 4.2 Unitarity of the automorphic scattering matrix is RH-blind

This is the result that generalizes, and it is the one worth carrying forward.

Every construction in this family inherits a unitary or self-adjoint structure for
free and treats it as leverage: the Hilbert space is $L^2$, the Laplacian is
self-adjoint, the S-matrix is unitary, therefore (the argument goes) something is
forced to be real. Run the D-H discipline on that step directly.

Build the same scattering phase for Davenport-Heilbronn,
$\varphi_{DH}(s) = \Lambda_{DH}(2s-1)/\Lambda_{DH}(2s)$, from the completed D-H
function with the odd-character-mod-5 $\Gamma$-factor already in
[`_shared/davenport_heilbronn.py`](../../experiments/_shared/davenport_heilbronn.py).
Measured at 30 digits:

- $|\varphi(1/2+it)| = 1$ for zeta, max deviation $3.9 \times 10^{-31}$.
- $|\varphi_{DH}(1/2+it)| = 1$ for D-H, max deviation $2.2 \times 10^{-30}$.
- D-H's known off-line zero $\rho \approx 0.8085 + 85.699i$ puts a resonance at
  $s \approx 0.40425 + 42.8495i$, which is $0.154$ away from $\operatorname{Re}(s)=1/4$.

Both scattering matrices are unitary on the critical line to thirty digits. One of them
belongs to a function that violates its own Riemann hypothesis.

The reason is structural, not numerical. Unimodularity on the line follows from real
Dirichlet coefficients plus a self-dual completion and **nothing else**: real
coefficients give $\Lambda(\bar s) = \overline{\Lambda(s)}$, so on
$\operatorname{Re}(s)=1/2$ the phase is $\overline{\Lambda}/\Lambda$, which has modulus 1
wherever the zeros happen to be. It is a consequence of the functional equation alone.

**So unitarity of the automorphic scattering matrix carries zero bits about zero
location.** No construction can extract RH from it, and any argument of the form
"the theory is unitary, therefore the spectrum is real, therefore RH" is passing
through a step that a known counterexample satisfies identically. This is the same
shape as LEARNINGS #170: the free structure is free exactly where it is
information-free.

---

## 5. The verdict, against this repo's own disciplines

The conservation law from `trojan_horse_m4.md` says a construction must consume the
Euler product **and** the additive lattice at the same joint. D-H detects failure to
pay the first; Beurling detects failure to pay the second. Apply it:

| construction | eats Euler product | eats lattice/FE | predicted | observed |
|---|---|---|---|---|
| Godet quantum cosmology | **no** ($\mu$ from primitivity, not multiplicativity) | yes ($T^d$, $SL(d,\mathbb{Z})$, Poisson) | cannot see RH | RH used as input, not output |
| LeClair spectral flow | yes | yes ($\vartheta$ from the FE, in the counting) | reaches an RH-equivalent restatement | Proposition 1 asserted, Hamiltonian never built |
| Betzios et al. CPT | partially | via the dilation operator | Berry-Keating class | spectral realization only |
| Kim arithmetic CS | no | no | outside the RH question | no contact with the zeros |

Both live candidates fail, and they fail in **complementary** ways, which is the most
useful thing this sweep produced. Godet has a real Hilbert space, a real self-adjoint
operator and a real appearance of the zeros, and no Euler product anywhere, so his
"Hilbert-Pólya Hamiltonian" can only ever be a name. LeClair has the Euler product and
the functional equation, and no Hilbert space or operator, so his unitarity can only
ever be an assumption. Between them they have all the pieces and no joint.

This is exactly the pattern LEARNINGS #113 recorded for string theory and
`spec_z_cohomology_landscape.md` recorded for every candidate cohomology of
$\operatorname{Spec}(\mathbb{Z})$: **every candidate realizes $\zeta$ as a trace; none
carries the polarization.** Quantum gravity does not break the pattern. It is now the
fourth independent field to reproduce it, and §4.2 explains why: the structure quantum
gravity hands you for free (unitarity) is provably the wrong kind of structure, because
it is a consequence of the functional equation and the functional equation is the half
of the package that D-H already has.

Stated as a coordinate rather than a wall: the search space just lost the entire
"unitarity implies reality" family, including the versions not yet written down, and it
lost them for a reason that can be checked in thirty digits rather than argued. What
remains is what remained before, sharpened: an *indefinite* form with a sign, not a
positive-definite or unitary structure.

---

## 6. What is genuinely new here

1. **Mechanism 5** (§2): primes entering through primitivity of a lattice vector, giving
   $1/\zeta$ and a Möbius average, with RH as randomness of $\mu$ rather than as
   positivity. New to the repo, and structurally different from the other four.
2. **The unitarity kill** (§4.2): a 30-digit D-H demonstration that unimodularity of the
   automorphic scattering phase is a consequence of the functional equation alone and
   therefore RH-blind. This is reusable as a disqualifier and belongs in the
   `breadth_program.md` battery.
3. **The Maass/GUE separation** (§4.1): the zeta zeros and the modular Laplacian's
   discrete spectrum are different universality classes at matched $N$, so the
   identification in the gravity literature is definitional. Also the first use of the
   Maass dataset in this repo.
4. **External corroboration of the conservation law** (§3.2): LeClair reaches "one needs
   both the functional equation and the Euler product" independently, from the S-matrix
   side.
5. **Arithmetic Chern-Simons** (§3.4): a real gap in the repo's coverage, now named.

---

## 7. What would move the needle

Not a plan, a shortlist, in decreasing order of how much it would change.

- **Arithmetic Chern-Simons with an indefinite pairing.** The Chern-Simons/Dijkgraaf-Witten
  setup on $\operatorname{Spec}(\mathcal{O}_K)$ has a carrier of the right *shape* for
  Direction 8: a 3-manifold-like object with a TQFT, hence a natural pairing on a middle
  cohomology. The question worth asking is whether the arithmetic linking form can be
  made **indefinite with a sign**, since the Legendre-symbol linking pairing is
  symmetric and its signature is exactly the kind of object M4 wants. If it is definite
  or degenerate for a structural reason, that is a clean negative and closes the door.
- **The Beurling test on LeClair.** He notes his model works with arbitrary real
  impurities, not just $\log p$. A Beurling system has an Euler product with real
  $\log p_j$, so his S-matrix construction goes through verbatim, and Diamond-Montgomery-Vorhauer
  built Beurling systems whose zeta has zeros arbitrarily close to $\sigma = 1$. Either
  the functional equation is doing more work in his counting condition than he credits,
  or Proposition 1 is false as stated. Both outcomes are informative and the test is cheap.
- **Godet's adelic lift.** $L^2(GL(d,\mathbb{Q})\backslash GL(d,\mathbb{A}))$ is proposed
  and not developed. That is the one move in his program that would introduce the Euler
  product (via the finite places) into a construction that currently has none. Whether
  it introduces a *signature* along with it is the only question that matters, and by
  the §5 table it is the only way that program could ever reach RH.

---

## 8. Sources pulled

All in `references/09_quantum_gravity/`, fetched 2026-08-19 from arXiv. Per the references-tier
policy the PDFs and their text extractions are gitignored; this table and the
[`references/README.md`](../../references/README.md) entry are the tracked record.

| file | paper |
|---|---|
| `arxiv_2505.03068.pdf` | Godet, *Möbius randomness in the Hartle-Hawking state* |
| `arxiv_2405.09833.pdf` | Godet, *Quantum cosmology as automorphic dynamics* |
| `arxiv_2406.01828.pdf` | LeClair, *Spectral Flow for the Riemann zeros* |
| `arxiv_2004.09523.pdf` | Betzios, Gaddam, Papadoulaki, *Black holes, quantum chaos, and the Riemann hypothesis* |
| `arxiv_1510.05818.pdf` | Kim, *Arithmetic Chern-Simons Theory I* |
| `arxiv_1609.03012.pdf` | Kim et al., *Arithmetic Chern-Simons Theory II* |
| `arxiv_1705.04758.pdf` | Dragovich et al., *p-Adic Mathematical Physics: The First 30 Years* |
| `arxiv_1101.3116.pdf` | Schumayer, Hutchinson, *Physics of the Riemann Hypothesis* |
| `arxiv_0712.0155.pdf` | Maloney, Witten, *Quantum Gravity Partition Functions in Three Dimensions* |
| `arxiv_0802.4077.pdf` | Agullo et al., *Black hole state counting in LQG: a number theoretical approach* |
| `arxiv_1507.05818.pdf` | Connes, Consani, *The Scaling Site* |
| `arxiv_2205.01391.pdf` | Connes, Consani, *Riemann-Roch for $\overline{\operatorname{Spec}\mathbb{Z}}$* |
| `arxiv_1509.05576.pdf` | Connes, *An essay on the Riemann Hypothesis* |

Text extractions (`.txt`) exist alongside the PDFs for the four papers read closely.

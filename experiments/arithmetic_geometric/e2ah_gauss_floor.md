# e2ah: the Gauss-lemma height floor in the vF disc model

> Probe of the "smallest checkable sub-question" surfaced by the van Frankenhuijsen deep-read
> ([`docs/03_research/reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md`](../../docs/03_research/reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md), Section 8).
> Code: [`e2ah_gauss_floor.py`](e2ah_gauss_floor.py). Lean companion: [`lean/ZetaRH/GaussFloor.lean`](../../lean/ZetaRH/GaussFloor.lean) (#GF-1..#GF-5, sorry-free, axiom-clean).

## The lemma

**Gauss-lemma floor.** Let $f \in \mathbb{Z}[z]$, $f \ne 0$, and let $P$ be a finite set of primes
such that $f$ vanishes at $z = 1/p$ with multiplicity at least $m_p$ for each $p \in P$. Then
$(pz-1)^{m_p} \mid f$ in $\mathbb{Z}[z]$ (each $pz - 1$ is primitive, so Gauss's lemma descends
the $\mathbb{Q}[z]$-divisibility), the factors for distinct primes are non-associated irreducibles
of the UFD $\mathbb{Z}[z]$, and since the leading coefficient is multiplicative,

$$|\mathrm{lead}(f)| \;\ge\; \prod_{p \in P} p^{m_p}, \qquad \text{i.e.} \qquad \log|\mathrm{lead}(f)| \;\ge\; \sum_{p \in P} m_p \log p.$$

(The Lean proof routes each prime separately through leading coefficients: $(pz-1)^{m_p} \mid f$
gives $p^{m_p} \mid \mathrm{lead}(f)$, and the prime powers are pairwise coprime integers, so no
polynomial-coprimality argument is needed at all.)

## The equality case

With van Frankenhuijsen's multiplicities $m_p = \lfloor \log_p x \rfloor$ the floor is exactly
Chebyshev: $\sum_{p \le x} m_p \log p = \psi(x)$, integer-exactly $\prod_p p^{m_p} = \mathrm{lcm}(1,\dots,x) = e^{\psi(x)}$.
The canonical product $f_x(z) = \prod_{p \le x} (pz-1)^{m_p}$ **attains** the floor:
$|\mathrm{lead}(f_x)| = e^{\psi(x)}$ exactly. So the minimal height of a prime-forced vanisher in
the model IS $\psi(x)$, with zero slack.

## What the probe verified (all PASS, integer-exact)

- **A (equality case)**: for $x \in \{2,3,5,10,20,30,50,100\}$, $|\mathrm{lead}(f_x)|$ (sympy
  expansion) $= \prod p^{m_p}$ (integer arithmetic) $= \mathrm{lcm}(1..x)$; so
  $\log|\mathrm{lead}| = \psi(x)$ exactly.
- **B (cofactor stress)**: 300 random $f = g \cdot \prod (pz-1)^{m_p}$; vanishing re-verified by
  exact division; floor never violated; equality holds iff $|\mathrm{lead}(g)| = 1$ (34 cases).
- **C (naive interpolation, the adversarial half)**: vanishers built from the rational nullspace
  of the derivative conditions, not as cofactor times product. At the minimal degree
  $D = \sum m_p$ the kernel is 1-dimensional and its primitive integer generator equals
  $\pm f$-canonical for all six configurations tested: a **complete** no-cheaper-vanisher
  certificate at degree $D$. At degrees $D+1..D+3$, 449 random lattice vanishers all obey the floor.

## The no-go interpretation

In the vF disc model there is **no Siegel-lemma slot**: any auxiliary function with the required
vanishing at $\{1/p\}$ already has log-height at least $\psi(x)$, which is precisely the quantity
the Stepanov-Bombieri engine is supposed to bound ($\psi(x) \le x + O(x^{1/2+\varepsilon})$ is
the target; PNT is the statement that the floor is $\sim x$). The pigeonhole (S3) can never
construct below the floor, so the model's only open slot is the S4/R1 cheap-multiplicity
operator: the missing Frobenius / arithmetic derivative (see
[`docs/03_research/stepanov_engine_audit.md`](../../docs/03_research/stepanov_engine_audit.md)).
The negative is a coordinate: the model's open slot is provably the only slot.

## Status

Registered as [P10](../../PUBLICATIONS.md#p10) (gate run 2026-07-02, tier DEVELOPING). Novelty
split: the assembled statement is apparently novel (vF 2008 Section 4 gives the setting with no
bound); the mechanism is folklore (the rational root theorem with multiplicity; the m = 1 case is
Mathlib's `den_dvd_of_is_root`), so the row is carried by the formal axis (Mathlib PR: generalized
multiplicity rational-root floor, absent from Mathlib). Scope note: the uniqueness-at-minimal-degree
clause is Python-certified only, not in `GaussFloor.lean` (#GF-6 candidate); machine-checked claims
are floor + equality until it lands.

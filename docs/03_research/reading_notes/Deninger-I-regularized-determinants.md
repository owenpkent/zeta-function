# Reading notes: Deninger, *Motivic L-functions and regularized determinants* (I)

> Third entry in the read-through ([`references/README.md`](../../../references/README.md)).
> This is the foundational paper of Deninger's program: it makes the regularized-
> determinant formalism rigorous and constructs the local (per-prime) infinite-
> dimensional cohomologies via the Riemann-Hilbert correspondence. It is the
> machinery 2R, the Lean `ExplicitFormula` archimedean kernel, and Direction 4.6 all
> rest on. Pages refer to the PDF in `references/02_deninger_program/`. Read: pp.1-9
> (§0 intro, §1 regularized determinants, §2 Riemann-Hilbert on `𝔾_m`).

## One-line takeaway

Deninger I gives the rigorous definition of `det_∞(Θ|V)` (zeta-regularized
determinant on a countable-dimensional space), the local cohomology `F_p(M)` via the
Riemann-Hilbert correspondence (eigenvalues of `Θ` ↔ eigenvalues of monodromy/
Frobenius), and identifies the SIGN in the functional equation with a **regularized
superdimension = the Atiyah-Patodi-Singer η-invariant**. The archimedean Γ-factor
falls out as a regularized product. This is the formal substrate under 2R (the
determinant) and under the Lean `archKernel`/`digamma` work (the Γ-factor).

## The points that matter, mapped to the project

1. **The program's four promises, stated (§0, p.1).** Deninger lists exactly the
   objects the project is chasing: (a) "What form should a **Lefschetz fixed point
   formula** take? ... the relation with explicit formulas in analytic number theory"
   = **Direction 4.6 / 2R**; (b) "a short 'proof' ... of the Riemann hypotheses
   assuming that a **Hodge ∗-operator** with standard properties exists on the
   prospected cohomologies" = **Direction 8 (the signature)**; (c) functional equation
   ↔ **Poincaré duality**; (d) "Künneth formula and **Kurokawa's multiple zeta
   functions**" = the **product/× structure**, i.e. the 2K product-surface theme. The
   whole program's milestone list is Deninger's §0.

2. **Rigorous regularized determinant (§1, (1.1)).** For `Θ` on a countable-dim `V`
   with eigenvalue Dirichlet series `ζ_Θ(s) = Σ_{α≠0} α^{-s}` continuing holomorphically
   past `s=0`: `dim_∞(Θ) = dim V₀ + ζ_Θ(0)` and `det_∞(Θ|V) = exp(-ζ'_Θ(0))` (or `0` if
   `0 ∈ Sp Θ`). Exact triangles multiply determinants and add dimensions (1.2).
   → This is the **precise meaning of the `det_ζ(s-Θ)` in Direction 4.6 and the object
   2R computed numerically**. 2R verified `-ζ'/ζ = Σ Λ(n)n^{-s}` (the log-derivative of
   exactly this regularized determinant over `H¹`). Deninger I is the definition that
   makes 2R's "regularized determinant" rigorous rather than formal.

3. **The sign in the functional equation = a regularized SIGNATURE = the η-invariant
   (§1, (1.3)-(1.6)).** Deninger defines the regularized superdimension
   `sdim_∞ Θ = (dim V₀⁺ + H⁺(0)) - (dim V₀⁻ + H⁻(0))` for a `Θ`-invariant splitting
   `V = V⁺ ⊕ V⁻`, and proves `det_∞(-Θ) = e^{iπ·sdim_∞ Θ} · det_∞ Θ` (1.6). Remark:
   "if `dim_∞ Θ^±` exist, `sdim_∞ Θ` can be viewed as the **η-invariant of `Θ` in the
   sense of Atiyah-Patodi-Singer**."
   → **Important bridge.** A *signature-like* quantity (the superdimension / η-invariant,
   a regularized `dim V⁺ - dim V⁻`) appears on the **regularized-determinant (trace)
   side** itself, governing the functional-equation sign. This is the closest the
   trace side comes to the Direction-8 signature, and it is exactly where 2R stops
   (2R gives the spectrum/`det`; the sign/`sdim` is the next structural layer). Worth
   flagging as a candidate link between 2R (trace) and Direction 8 (Hodge-∗ signature):
   the Hodge-∗ operator's job is to make this `sdim`/η controllable.

4. **Local cohomology `F_p(M)` via Riemann-Hilbert (§2).** On `𝔾_m/ℂ`, regular-singular
   differential equations `(M,∇)` ↔ finite-dim representations of `π₁(ℂ*) = ℤ`
   (D.E.R.S.(`𝔾_m`)), with `Θ = z d/dz`. The functor `ℍ(D) = (D ⊗ 𝒪(ℂ))^{Θ=0}` and
   `(2.6) Sp(Θ) = e^{-1} Sp(F)` where `F` is (inverse) monodromy = the local Frobenius;
   `e(α) = exp(2πiα)`. This is the "improved construction ... using an elementary case
   of the Riemann-Hilbert correspondence" that drops the semisimplicity assumption
   (noted independently by S. Bloch).
   → This is the concrete **construction of the local (per-prime) infinite-dim
   cohomology** the program's `H^*` is glued from. The relation `Sp(Θ) = e^{-1}Sp(F)`
   (additive eigenvalues of the generator ↔ multiplicative eigenvalues of Frobenius)
   is the **local form of 2Q's `(1,p)` bidegree / 2R's `{log p}` orbit lengths**:
   `log`(Frobenius eigenvalue) = generator eigenvalue, the same `log p` ↔ `p` passage.

5. **The archimedean Γ-factor as a regularized product (§2, (2.7) + p.9).** The
   regularized product `∏_{ν∈ℤ} γ(z+ν) = 1 - e^{±2πiz}` (the local Euler-factor shape),
   and over `ℕ` the Hurwitz-zeta values `ζ(0,z) = ½ - z`, `∂_s ζ(0,z) = log Γ(z) - ½log 2π`
   give `exp(-∂_s ζ̄(0,z)) = (Γ(z)/√(2π))^{-1}` — the **Γ-factor as a regularized
   determinant**.
   → Directly validates the Lean `ExplicitFormula` choice: our `archKernel` is the
   log-derivative of the Γ-factor `π^{-s/2}Γ(s/2)`, and `digamma = (log Γ)'`. Deninger
   derives the Γ-factor itself as the regularized product whose log-derivative our
   kernel is. The archimedean `A_arch` block (2I) is this regularized Γ-factor; the
   finite places are the `1 - e^{±2πiz}` Euler factors. Same `det_∞` formalism, all
   places uniform — the `new_mathematics.md §4.2` "cohomology that knows about
   archimedean primes" made concrete at the local level.

## What this changes for the program

- **2R is now grounded.** Deninger I §1 is the rigorous definition of the regularized
  determinant whose log-derivative 2R computed; the program can cite it for "what
  `det_ζ(s-Θ)` means."
- **A trace-side signature exists: the η-invariant / superdimension.** This is the
  most novel takeaway. The functional-equation sign is governed by `sdim_∞ Θ` (an APS
  η-invariant), a regularized `dim⁺ - dim⁻`. It sits on the trace side yet is
  signature-flavoured — a possible conceptual bridge from 2R (spectrum) toward the
  Direction-8 Hodge-∗ signature, and worth keeping in view when thinking about how the
  signature could ever emerge from the flow.
- **The local `log p ↔ p` passage is the Riemann-Hilbert `Sp(Θ)=e^{-1}Sp(F)`.** 2Q's
  bidegree and 2R's orbit lengths are the global assembly of this local fact. Good
  to have the local statement pinned to a theorem.
- **The Lean archimedean kernel is on solid ground.** Deninger I derives the Γ-factor
  as a regularized product; our `archKernel = -(1/2)log π + (1/2)ψ(1/4 + ir/2)` is its
  log-derivative. No change needed, but the foundation is now explicit.

## Actionable

- The `sdim_∞`/η-invariant ↔ Hodge-∗ signature link (§1 here + Deninger II §6) is the
  thread most worth pulling for the trace↔signature question. No new computation yet,
  but it sharpens "what would make the signature emerge."
- Next read: **Álvarez-López–Kordyukov–Leichtnam 2017** (the general foliated-flow
  trace formula / Hodge decomposition machinery that Leichtnam 2006 cites as [A-K00]),
  then the **prismatic stack** (Bhatt-Scholze; the p-adic transversal's cohomology).

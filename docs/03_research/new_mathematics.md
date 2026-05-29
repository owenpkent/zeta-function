# The Shape of New Mathematics

> What would a mathematical framework capable of proving the Riemann Hypothesis
> actually look like? What properties must it have, what should it unify, and
> how does it differ from everything that exists today?

---

## 1. Why New Mathematics Is Needed

Every serious approach to RH has hit a wall: not a wall of insufficient effort,
but a wall where the available tools provably cannot go further. These walls are
not independent failures. They are symptoms of the same missing structure. This
is the normal prelude to new mathematics, not the end of the road. Section 9
gives the historical pattern (the quintic, the parallel postulate, the
three-body problem, the finite-field Riemann Hypothesis), where the same kind of
wall was the signal that a new structure had to be built.

```
                    ┌─────────────────────────────────────────┐
                    │         THE RIEMANN HYPOTHESIS          │
                    │   "All non-trivial zeros have Re = 1/2" │
                    └──────────────────┬──────────────────────┘
                                       │
                          ┌────────────┼────────────┐
                          │            │            │
                          ▼            ▼            ▼
                    ┌──────────┐ ┌──────────┐ ┌──────────┐
                    │ SPECTRAL │ │ GEOMETRIC│ │ ANALYTIC │
                    │ approach │ │ approach │ │ approach │
                    └─────┬────┘ └─────┬────┘ └────┬─────┘
                          │            │            │
                          ▼            ▼            ▼
                    ┌──────────┐ ┌──────────┐ ┌──────────┐
                    │Positivity│ │ Geometry │ │ Analytic │
                    │   gap    │ │   gap    │ │ ceiling  │
                    └──────────┘ └──────────┘ └──────────┘
                          │            │            │
                          └────────────┼────────────┘
                                       │
                                       ▼
                          ┌────────────────────────┐
                          │   SAME MISSING THING   │
                          │                        │
                          │  A framework that sees │
                          │  arithmetic, geometry, │
                          │  and analysis as ONE   │
                          │  unified structure     │
                          └────────────────────────┘
```

Each single approach stalls at a specific, identifiable place. The spectral
approach stalls at proving positivity. The geometric approach stalls at building
the right space. The analytic approach stalls because its tools are provably at
their ceiling. That precision is the opening, not the obituary: the spectral
approach *needs geometry* for positivity, the geometric approach *needs analysis*
for the trace formula, and the analytic approach *needs algebra* for deeper
structure. Each approach reaches its limit precisely where it needs to become one
of the other approaches. The place each one stalls is a map of what to build next.

**The new mathematics is not a better version of any one approach. It is the
thing that makes them all the same approach.**

---

## 2. Five Properties the New Framework Must Have

### 2.1 It Must See Arithmetic and Geometry Simultaneously

**The problem:** In the [function field](https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety) world (where RH is proved), there is a
literal geometric object — a curve over a [finite field](https://en.wikipedia.org/wiki/Finite_field) — whose shape *is* the
number theory. The zeros of its zeta function are topological features of this
curve. You can "see" the hypothesis.

For the integers, there is no such object. $\operatorname{Spec}(\mathbb{Z})$
is a one-dimensional [scheme](https://en.wikipedia.org/wiki/Scheme_(mathematics)), but it is **non-compact, has no [Frobenius](https://en.wikipedia.org/wiki/Frobenius_endomorphism), and
lacks the geometric richness** that makes the function field proof work.

```
FUNCTION FIELD (RH is proved here)
═══════════════════════════════════

    Curve C over F_q
    ┌──────────────────────────────────────┐
    │  • A smooth compact geometric object │
    │  • Has étale cohomology H^i(C)       │
    │  • Frobenius acts on cohomology      │
    │  • Weil pairing gives duality        │
    │  • Hodge index theorem → POSITIVITY  │
    │  • Zeros = eigenvalues of Frobenius  │
    └──────────────────────────────────────┘
         │
         │   All of this exists and works.
         │   The proof follows almost inevitably.
         │
         ▼
    ζ_C(s) satisfies RH  ✓


NUMBER FIELD (RH is unproved here)
══════════════════════════════════

    Spec(Z) — "the integers as a space"
    ┌──────────────────────────────────────┐
    │  • Not compact (no archimedean end)  │
    │  • No étale cohomology that works    │
    │  • No Frobenius endomorphism         │
    │  • No Weil pairing                   │
    │  • No source of positivity           │
    │  • Zeros = ??? eigenvalues of ???    │
    └──────────────────────────────────────┘
         │
         │   Every line here is a missing piece:
         │   a concrete thing the new framework has to build.
         │
         ▼
    ζ(s) satisfies RH  ???
```

**What the new framework must do:** Provide a way to treat
$\operatorname{Spec}(\mathbb{Z})$ — or some compactification of it — as a
geometric object rich enough to carry cohomology, a Frobenius-like symmetry,
and the duality/positivity that makes the proof work.

This is not about finding a clever analogy. It is about discovering that
arithmetic *already is* geometry, in some deep sense we don't yet understand,
and building the mathematical language that makes this visible.

---

### 2.2 It Must Contain a Natural Source of Positivity

**The problem:** The word "positivity" appears everywhere in RH research.

- **Weil positivity:** RH ⟺ a quadratic form on test functions is positive
  semi-definite
- **[Li's criterion](https://en.wikipedia.org/wiki/Li%27s_criterion):** RH ⟺ an infinite sequence of real numbers $\lambda_n$
  are all positive
- **[Robin's inequality](https://en.wikipedia.org/wiki/Robin%27s_inequality):** RH ⟺ $\sigma(n) < e^\gamma n \ln\ln n$ for $n > 5040$
  (a positivity of "headroom" in the divisor function)
- **Self-adjointness:** RH ⟺ a spectral operator has only real eigenvalues
  (i.e., the imaginary part is "positively" zero)

All of these are different faces of the same underlying positivity. In the
function field proof, positivity comes from **[intersection theory](https://en.wikipedia.org/wiki/Intersection_theory) on algebraic
surfaces** — ultimately from the [Hodge index theorem](https://en.wikipedia.org/wiki/Hodge_index_theorem), which says that the
intersection pairing on a surface has a specific signature.

```
THE POSITIVITY LANDSCAPE
════════════════════════

                         ┌──────────────┐
                         │   THE PROOF  │
                         │   OF RH      │
                         └──────┬───────┘
                                │
                        requires positivity
                                │
           ┌────────────────────┼────────────────────┐
           │                    │                     │
           ▼                    ▼                     ▼
    ┌──────────────┐   ┌───────────────┐    ┌────────────────┐
    │ Weil's       │   │ Spectral      │    │ Arithmetic     │
    │ quadratic    │   │ self-         │    │ inequalities   │
    │ form ≥ 0    │   │ adjointness   │    │ (Robin, Li)    │
    └──────┬───────┘   └───────┬───────┘    └────────┬───────┘
           │                   │                      │
           └───────────────────┼──────────────────────┘
                               │
                         ALL EQUIVALENT
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SOURCE: ???       │
                    │                     │
                    │   Function fields:  │
                    │   Hodge index thm   │
                    │                     │
                    │   Number fields:    │
                    │   ??? UNKNOWN ???   │
                    └─────────────────────┘
```

**What the new framework must do:** Not merely *prove* positivity, but make
positivity *obvious*. In the function field case, positivity is not hard to
establish — it falls out naturally from the geometry. A correct framework for
$\mathbb{Q}$ should make positivity similarly inevitable.

If proving positivity still feels like the hardest step in the new framework,
the framework is not the right one. The right framework is the one where
positivity is a structural feature, not a theorem.

---

### 2.3 It Must Bridge the Spectral and Arithmetic Worlds

**The problem:** There are extraordinary parallels between the eigenvalues of
large random matrices and the zeros of the zeta function. The zeros "know
about" quantum mechanics. But nobody can explain *why*, rigorously.

```
TWO WORLDS, ONE MYSTERY
════════════════════════

    ARITHMETIC WORLD                    SPECTRAL WORLD
    ┌──────────────────────┐            ┌──────────────────────┐
    │                      │            │                      │
    │  Primes: 2,3,5,7,11 │            │  Eigenvalues of      │
    │                      │            │  random matrices     │
    │  Divisors, sums,     │            │                      │
    │  multiplicative      │            │  Operators on        │
    │  functions           │            │  Hilbert spaces      │
    │                      │            │                      │
    │  Euler product       │            │  Spectral            │
    │  ∏(1-p^{-s})^{-1}   │            │  decomposition       │
    │                      │            │                      │
    │  Primes → zeros      │            │  Quantum chaos →     │
    │  (explicit formula)  │            │  energy levels       │
    │                      │            │                      │
    └──────────┬───────────┘            └──────────┬───────────┘
               │                                   │
               │         DEEP CONNECTION           │
               │◄─────── but no rigorous ─────────►│
               │         bridge exists             │
               │                                   │
               └──────────────┬────────────────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  Montgomery (1973):  │
                   │  pair correlation of │
                   │  zeros matches GUE   │
                   │                      │
                   │  Odlyzko (1987):     │
                   │  zeros at height     │
                   │  10^20 still match   │
                   │                      │
                   │  Berry-Keating:      │
                   │  H = xp should work  │
                   │  ... but can't prove │
                   │  self-adjointness    │
                   └──────────────────────┘
```

**What the new framework must do:** Provide a natural, rigorous mathematical
object that is *simultaneously* arithmetic and spectral. Not an analogy, not
a dictionary between the two worlds, but a single object that *is* both.

The closest existing idea: [Connes](https://en.wikipedia.org/wiki/Alain_Connes)' [noncommutative geometry](https://en.wikipedia.org/wiki/Noncommutative_geometry) of the [adèle](https://en.wikipedia.org/wiki/Ad%C3%A8le_ring) class
space, where the space itself is arithmetic (built from primes) and carries a
natural spectral theory (operators on $L^2$ spaces). But the positivity proof
within Connes' framework remains missing — the framework reveals the connection
but doesn't yet close it.

---

### 2.4 It Must Convert "Almost All" into "All"

**The problem:** We know a staggering amount about zeta zeros *statistically*:

- Their spacing matches GUE to extraordinary precision
- 100% of zeros (in density) lie on the critical line
- Over $10^{13}$ individual zeros have been verified on the critical line
- The [de Bruijn–Newman constant](https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant) is within $10^{-11}$ of zero

None of this proves RH, because RH is about *every single zero*, including
hypothetical ones at height $10^{10^{100}}$ that we could never compute.

```
THE EXACTNESS PROBLEM
═════════════════════

What we know:                          What RH requires:

  "Almost all zeros are          →      "ALL zeros are
   on the critical line"                 on the critical line"

  "The density of zeros          →      "There are EXACTLY ZERO
   off the line is 0"                    zeros off the line"

  "Statistics match GUE"         →      "Every individual zero
                                         has Re = 1/2"

  "First 10^13 zeros: ✓"        →      "The 10^(10^100)-th
                                         zero: also ✓"

                    ┌────────────────────────┐
                    │  No known mathematical │
                    │  tool can make this    │
                    │  jump in general.      │
                    │                        │
                    │  But algebra can.      │
                    │  If you know the       │
                    │  structure, you know   │
                    │  ALL the instances.    │
                    └────────────────────────┘
```

**What the new framework must do:** Reveal *algebraic structure* beneath the
statistical regularities. When you prove that $x^2 + 1 = 0$ has no real
solutions, you don't check every real number — you use the algebraic structure
($x^2 \geq 0$ for real $x$). Similarly, the right framework would show that
zeros *must* be on the critical line as a structural necessity, not something
requiring case-by-case or statistical verification.

The jump from "almost all" to "all" always requires finding the hidden
algebraic/geometric reason behind the statistical pattern. The new mathematics
must provide this reason.

---

### 2.5 It Must Be Self-Evidently Natural

**The problem:** There is an aesthetic criterion in mathematics that the "right"
proof of a theorem feels inevitable — it reveals *why* the theorem is true,
not just *that* it's true. [Wiles' proof of Fermat's Last Theorem](https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem), while
incredibly deep, ultimately made people feel that the [modularity of elliptic
curves](https://en.wikipedia.org/wiki/Modularity_theorem) was the "real reason" behind $a^n + b^n = c^n$ having no solutions.

A correct framework for RH should similarly reveal *why* the zeros are on the
critical line.

Consider what we know about the functional equation:

$$\xi(s) = \xi(1-s)$$

This equation says the zeta function has a **perfect mirror symmetry** about
the line $\operatorname{Re}(s) = 1/2$. The zeros either lie on this mirror
or come in symmetric pairs reflected across it. RH says they all lie on the
mirror — there are no off-mirror pairs.

```
THE FUNCTIONAL EQUATION'S MIRROR
═════════════════════════════════

                  Re(s) = 0          Re(s) = 1/2         Re(s) = 1
                     │                    │                   │
  Critical strip     │    If a zero       │                   │
  ◄─────────────────►│    is HERE    ●    │                   │
                     │                    │                   │
                     │    then one        │                   │
                     │    must be HERE    │    ●              │
                     │                    │                   │
                     │         ●          │                   │
                     │                    │                   │
                     │                    │          ●        │
                     │                    │                   │
                     │                    │                   │
                     │                    ● ← on the mirror  │
                     │                    ●   = satisfies RH │
                     │                    ●                   │
                     │                    │                   │

  RH says: all zeros are ON the mirror, never off it.
  The mirror exists because of the functional equation.
  But WHY do zeros prefer the mirror to off-mirror pairs?
```

**What the new framework must do:** Make the answer to "why do zeros prefer
the mirror?" feel as obvious as "why do eigenvalues of a real symmetric matrix
prefer the real line?" (answer: because real symmetric matrices are
self-adjoint, and self-adjoint operators have real spectra — it's structural,
not coincidental).

---

## 3. How It Differs from Existing Mathematics

### 3.1 Existing Tools and Why They Fall Short

```
TOOL                     WHAT IT CAN DO              WHERE IT BREAKS FOR RH
──────────────────────── ─────────────────────────── ────────────────────────
Complex analysis         Locate zeros approximately;  Cannot push zero-free
                         functional equation;         region past 2/3 exponent
                         Hadamard product             (provable barrier)

Algebraic geometry       Prove RH for function        Cannot "lift" to Q;
(étale cohomology)       fields completely             Spec(Z) lacks needed
                                                      geometric structure

Spectral theory          Formulate RH as spectral     Cannot prove self-
(operators, Hilbert      problem; identify candidate  adjointness of any
spaces)                  operators                    candidate operator

Random matrix theory     Predict zero statistics      Statistical → exact
                         with stunning accuracy       gap is unbridgeable

Analytic number theory   Zero-free regions;           Vinogradov-Korobov
(exponential sums)       prime-counting estimates     ceiling at 2/3

Noncommutative geometry  Reformulate via adèle        Positivity remains
(Connes)                 class space                  unproved

Arakelov geometry        Partial compactification     Does not give full
                         of Spec(Z)                   cohomology needed
```

Each tool captures *part* of the truth but is provably insufficient alone.
The new mathematics must either:

**(a)** Extend one of these tools so dramatically that the extension deserves
to be called new mathematics, or

**(b)** Provide a unifying framework in which all of these tools are special
cases, and the RH-proof arises from properties of the unified framework that
aren't visible in any special case.

History favors (b). Weil's proof for function fields unified geometry and
number theory; Wiles' proof of FLT unified modular forms and elliptic curves.
Major problems fall when previously separate theories merge.

---

### 3.2 The Missing Unification

```
CURRENT STATE: Islands of Mathematics
══════════════════════════════════════

    ╔═══════════╗    ╔══════════════╗    ╔════════════╗
    ║  Complex  ║    ║   Algebraic  ║    ║  Spectral  ║
    ║  Analysis ║    ║   Geometry   ║    ║   Theory   ║
    ║           ║    ║              ║    ║            ║
    ║ ζ(s),     ║    ║ Curves/F_q,  ║    ║ Operators, ║
    ║ zeros,    ║    ║ cohomology,  ║    ║ eigenvalues║
    ║ estimates ║    ║ Frobenius    ║    ║ Hilbert sp.║
    ╚═════╤═════╝    ╚══════╤═══════╝    ╚═════╤══════╝
          │                 │                   │
          │   Occasional    │    Occasional     │
          │◄──analogies ───►│◄───parallels ────►│
          │   (Weil, Li)    │    (Berry-Keating) │
          │                 │                   │
          ▼                 ▼                   ▼
      each approach      each approach      each approach
      hits its own       hits its own       hits its own
      wall               wall               wall


NEEDED STATE: Unified Continent
═══════════════════════════════

    ╔═════════════════════════════════════════════════╗
    ║                                                 ║
    ║          UNIFIED ARITHMETIC GEOMETRY            ║
    ║                                                 ║
    ║   Analysis ←→ Geometry ←→ Spectral theory      ║
    ║                                                 ║
    ║   • A space that IS both arithmetic and         ║
    ║     geometric                                   ║
    ║   • An operator that IS both analytic and       ║
    ║     algebraic                                   ║
    ║   • Positivity that IS both topological and     ║
    ║     spectral                                    ║
    ║                                                 ║
    ║   RH falls out as a structural consequence      ║
    ║   of the unified framework                      ║
    ║                                                 ║
    ╚═════════════════════════════════════════════════╝
```

---

### 3.3 What "New" Really Means

The history of mathematics suggests the new framework won't come from nowhere.
It will likely:

1. **Extend an existing theory past its current limits.** [Étale cohomology](https://en.wikipedia.org/wiki/%C3%89tale_cohomology) was
   an extension of classical [cohomology](https://en.wikipedia.org/wiki/Cohomology). [Arakelov geometry](https://en.wikipedia.org/wiki/Arakelov_theory) extends algebraic
   geometry. The breakthrough extends something we already have in a direction
   nobody expected to be possible.

2. **Reveal that two known things are secretly the same.** [Galois theory](https://en.wikipedia.org/wiki/Galois_theory)
   revealed that field extensions and symmetry groups are the same. The
   [Langlands program](https://en.wikipedia.org/wiki/Langlands_program) is revealing that [automorphic forms](https://en.wikipedia.org/wiki/Automorphic_form) and [Galois
   representations](https://en.wikipedia.org/wiki/Galois_representation) are the same. The breakthrough reveals that some pair of
   mathematical structures are secretly identical.

3. **Take a physical intuition and make it rigorous.** Berry-Keating's
   $H = xp$ is a physical intuition. The GUE connection is a physical
   intuition. The breakthrough takes one of these seriously and builds
   rigorous mathematics around it.

```
HISTORICAL PATTERN: How Breakthroughs Happen
════════════════════════════════════════════

   Fermat's Last Theorem (1994)
   ────────────────────────────
   Known:   Elliptic curves over Q
   Known:   Modular forms
   Missing: They are the same thing (modularity)
   Proof:   Wiles proved modularity → FLT follows

   RH for Function Fields (1948/1974)
   ──────────────────────────────────
   Known:   Curves over finite fields
   Known:   Cohomology theories
   Missing: The right cohomology (étale) + Frobenius action
   Proof:   Weil/Deligne built the tools → RH follows

   Classification of Finite Simple Groups (1981)
   ──────────────────────────────────────────────
   Known:   Many families of simple groups
   Known:   Representation theory
   Missing: Systematic framework (plus monstrous moonshine)
   Proof:   Decades of case analysis + structural theory

   RH for Q (???)
   ────────────
   Known:   Zeta zeros behave like eigenvalues
   Known:   Function field proof works
   Missing: ??? The connection between these two facts ???
   Proof:   ???
```

---

## 4. Concrete Characteristics of the New Framework

Based on the five properties above and the landscape of failures, we can
describe the new mathematics with surprising specificity:

### 4.1 An "Arithmetic Frobenius"

In the function field proof, the Frobenius endomorphism $\text{Fr}: x \mapsto x^q$
is the engine of the entire proof. Its eigenvalues on cohomology are the
zeros of the zeta function, and its algebraic properties force those
eigenvalues to have the right absolute value.

The new framework needs an arithmetic analogue — an operator or symmetry
of $\operatorname{Spec}(\mathbb{Z})$ that plays the role of Frobenius.

```
FROBENIUS: What It Does in the Function Field Proof
════════════════════════════════════════════════════

    Curve C over F_q
          │
          │  Frobenius: x ↦ x^q
          │  (raises coordinates to q-th power)
          │
          ▼
    Acts on cohomology H^1(C)
          │
          │  Eigenvalues: α_1, ..., α_{2g}
          │
          ▼
    Zeta function: ζ_C(s) = ∏(1 - α_i q^{-s}) / (...)
          │
          │  RH ⟺ |α_i| = √q
          │
          ▼
    Proof: Hodge index theorem + Frobenius compatibility
           forces |α_i| = √q.  Done. ✓


FOR Q: What We Need
════════════════════

    Spec(Z) or compactification
          │
          │  "Arithmetic Frobenius": ???
          │  (what operation plays this role?)
          │
          ▼
    Acts on "arithmetic cohomology" H^1(Spec(Z))
          │
          │  Eigenvalues: ρ_1, ρ_2, ...
          │
          ▼
    ζ(s) expressed in terms of these eigenvalues
          │
          │  RH ⟺ eigenvalues have Re = 1/2
          │
          ▼
    Proof: ??? positivity + compatibility ???

    CANDIDATES FOR "ARITHMETIC FROBENIUS":
    ──────────────────────────────────────
    • Scaling on idèles: x ↦ λx on A_Q^×/Q^×  (Connes)
    • "Absolute Frobenius" in F_1-geometry     (Borger, Connes-Consani)
    • Time evolution in quantum statistical
      mechanics of number-theoretic systems    (Bost-Connes)
```

**Deninger's insight:** The Frobenius in the function field case generates a
$\mathbb{Z}$-action (iterate it). For $\mathbb{Q}$, Deninger suggested we
need an $\mathbb{R}$-action (a flow). This flow should be the "time evolution"
of some dynamical system on an arithmetic space, and the zeta zeros should be
the "frequencies" of this flow — just as the eigenvalues of the Laplacian are
frequencies of vibration on a surface.

---

### 4.2 A Cohomology That Knows About Archimedean Primes

Classical algebraic geometry over $\mathbb{Q}$ treats the "prime at infinity"
(the archimedean absolute value) differently from finite primes. But the
zeta function treats them uniformly — the completed zeta function
$\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ includes the gamma factor
(the archimedean contribution) on equal footing with the Euler product
(the finite-prime contribution).

```
THE PRIME DECOMPOSITION OF ζ
════════════════════════════

    ξ(s) = ½s(s-1) · π^{-s/2} · Γ(s/2) · ζ(s)

                        ▲                    ▲
                        │                    │
                   archimedean          finite primes
                   "prime at ∞"         p = 2,3,5,...
                        │                    │
                   Gamma factor         Euler product
                   π^{-s/2}Γ(s/2)      ∏(1-p^{-s})^{-1}
                        │                    │
                        └────────┬───────────┘
                                 │
                            The completed
                            zeta function
                            treats BOTH
                            uniformly

    Current mathematics:
    ┌────────────────────────────────────────────────┐
    │ Finite primes → étale cohomology (works great) │
    │ Archimedean   → ??? (Hodge theory? analysis?)  │
    │                                                │
    │ No single cohomology handles both uniformly.   │
    └────────────────────────────────────────────────┘

    Needed mathematics:
    ┌────────────────────────────────────────────────┐
    │ ALL primes (finite + archimedean) treated by   │
    │ a single cohomology theory with:               │
    │   • Poincaré duality                           │
    │   • Künneth formula                            │
    │   • Lefschetz trace formula                    │
    │   • Hodge-type positivity                      │
    └────────────────────────────────────────────────┘
```

This is essentially Deninger's program. The cohomology groups $H^i$ should be
infinite-dimensional (unlike the function field case), with a flow (the
arithmetic Frobenius) whose "regularized determinant" gives the zeta function.

---

### 4.3 A Notion of "Shape" for the Prime Numbers

The primes are distributed irregularly along the number line, but their
distribution has deep structure. The new framework should give us a way to
talk about the **geometry** of this distribution — literally, the "shape" that
the primes trace out.

```
PRIMES AS GEOMETRY
══════════════════

Current understanding:
    Primes on the number line:
    2  3     5     7          11    13          17    19          23
    │  │     │     │          │     │           │     │           │
    ●──●─────●─────●──────────●─────●───────────●─────●───────────●──────►
    Irregular spacing, but governed by ζ(s)

What we'd LIKE to see:
    The primes as a geometric object in some higher space,
    where their structure becomes visible as SHAPE:

         ●
        ╱ ╲
       ●   ●
      ╱ ╲ ╱ ╲           A surface, manifold, or space
     ●   ●   ●          whose topology encodes prime
      ╲ ╱ ╲ ╱           distribution — where
       ●   ●            "the zeros are on the line"
        ╲ ╱             becomes "the shape has
         ●              positive curvature"
          ╲
           ●

    Then RH becomes a statement about curvature,
    intersection numbers, or topological invariants —
    the kind of thing geometry CAN prove.
```

This is what we mean by "seeing arithmetic as geometry." The function field
proof literally uses the curvature properties of a surface (the curve × the
curve, where intersection theory lives) to establish positivity. We need an
analogous "surface" for $\operatorname{Spec}(\mathbb{Z})$.

---

### 4.4 A Bridge Between Discrete and Continuous

The integers are discrete. Operators live in continuous (Hilbert) spaces.
Zeta zeros are complex numbers (continuous) but encode information about
primes (discrete). The new mathematics must be natively fluent in both.

```
THE DISCRETE ↔ CONTINUOUS BRIDGE
═════════════════════════════════

    DISCRETE                               CONTINUOUS
    ┌──────────────────┐                   ┌──────────────────┐
    │                  │                   │                  │
    │  Z (integers)    │                   │  R (reals)       │
    │  Primes          │                   │  Operators       │
    │  Arithmetic      │   The new math    │  Analysis        │
    │  functions       │   must live HERE   │  Spectral        │
    │  (μ, φ, σ, Λ)   │◄─────────────────►│  theory          │
    │                  │   naturally        │                  │
    │  Galois groups   │   fluent in both  │  Hilbert spaces  │
    │  (finite,        │                   │  (infinite-      │
    │   discrete)      │                   │   dimensional)   │
    │                  │                   │                  │
    └──────────────────┘                   └──────────────────┘

    EXISTING BRIDGES (partial):
    ─────────────────────────
    • Explicit formula: ψ(x) = x - Σ_ρ x^ρ/ρ + ...
      (primes ↔ zeros, but the connection is one-way and fragile)

    • Adèles: A_Q = R × ∏'Q_p
      (all completions at once — treats all primes uniformly)

    • p-adic analysis: Q_p gives continuous methods for discrete primes
      (but one prime at a time, not globally)

    THE NEW BRIDGE MUST:
    ────────────────────
    • Treat primes not as indexed discrete objects but as
      structural features of a continuous space
    • Make the explicit formula a CONSEQUENCE of geometry,
      not a computational identity
    • Allow spectral methods and arithmetic methods to be
      applied to the same object
```

---

### 4.5 Computability and Falsifiability

A crucial practical characteristic: the new framework must produce
**computable predictions** beyond RH itself. A framework that only says
"RH is true" and nothing else would be unfalsifiable and therefore
untrustworthy. The right framework should:

- Predict new relationships between zeros, primes, and L-functions
- Give sharper bounds than currently known (e.g., better error terms in the
  prime counting function)
- Apply to the Generalized Riemann Hypothesis (GRH) for other L-functions
- Suggest connections to physics that can be tested

```
A GOOD FRAMEWORK PREDICTS MORE THAN RH
═══════════════════════════════════════

    The framework
         │
         ├──► RH for ζ(s)                    (the main target)
         │
         ├──► GRH for all L-functions         (should follow naturally)
         │
         ├──► New bounds on π(x) - Li(x)      (sharper than current)
         │
         ├──► Predictions about zero spacing   (beyond GUE?)
         │
         ├──► Connections to physics            (testable)
         │
         └──► New theorems we didn't expect     (the real payoff)

    Historical example: Weil's proof for function fields
    gave not just RH but the entire Weil conjectures —
    rationality, functional equation, Betti numbers, AND RH.
    The framework was richer than the question that motivated it.
```

---

## 5. What Has Been Tried Before (and Why It Didn't Work)

### 5.1 Summary of Attempted Frameworks

```
TIMELINE OF ATTEMPTED NEW MATHEMATICS FOR RH
═════════════════════════════════════════════

1914    Hilbert-Pólya conjecture proposed
        "Find a self-adjoint operator whose eigenvalues are the zeros"
        Status: OPEN. No suitable operator found in 110+ years.

1945    Weil begins function field program
1948    Weil proves RH for curves/F_q
        "Lift these techniques to Q"
        Status: PARTIAL. The geometry of Spec(Z) is insufficient.

1973    Montgomery pair correlation → GUE discovery
        "Use random matrix theory to understand zeros"
        Status: STATISTICAL ONLY. Cannot bridge to exact results.

1976    Newman conjecture (Λ ≥ 0)
        "Squeeze the de Bruijn-Newman constant to determine RH"
        Status: Λ ∈ [-10^{-11}, 0]. Cannot determine sign.

1992    Deninger's cohomological program
        "Build the right cohomology for Spec(Z)"
        Status: OPEN. Requirements identified but no construction.

1996    Connes' noncommutative geometry approach
        "Use the adèle class space as the geometric object"
        Status: PARTIAL. Reformulates RH but positivity unproved.

1999    Berry-Keating quantization program
        "Rigorously quantize H = xp"
        Status: OPEN. Multiple quantizations tried; none proven.

2005    Connes-Consani F_1-geometry
        "Build algebraic geometry over the field with one element"
        Status: PARTIAL. Multiple definitions of F_1; none sufficient.

2011    Sierra-Townsend Landau levels
        "Use quantum mechanics in hyperbolic plane"
        Status: PARTIAL. Matches statistics but not individual zeros.

2020    Rodgers-Tao (Polymath15)
        "Prove Newman's conjecture"
        Status: PROVED Λ ≥ 0. But doesn't prove RH (needs Λ ≤ 0).
```

### 5.2 Patterns in Failure

Every attempt falls into one of these categories:

```
FAILURE MODE 1: "Right space, wrong tools"
──────────────────────────────────────────
Example:  Connes' adèle class space approach
What:     The space A_Q/Q* is arguably the right arena
Why fail: Cannot prove positivity within noncommutative geometry
Lesson:   Having the right object is necessary but not sufficient;
          you also need the right TECHNIQUES for that object

FAILURE MODE 2: "Right tools, wrong space"
──────────────────────────────────────────
Example:  Trying to extend étale cohomology to Spec(Z)
What:     Étale cohomology works perfectly for function fields
Why fail: Spec(Z) is not compact; no Frobenius; wrong dimension
Lesson:   The tool that works in the analogous setting doesn't
          directly transfer; the arithmetic case is fundamentally
          different, not just technically harder

FAILURE MODE 3: "Right answer, wrong precision"
───────────────────────────────────────────────
Example:  Random matrix theory
What:     Gives the RIGHT statistics for zeros, to arbitrary precision
Why fail: Statistics ≠ individual certainty
Lesson:   Matching predictions to 15 decimal places is not a proof;
          the framework must access structural truth, not numerical

FAILURE MODE 4: "Right idea, incomplete execution"
─────────────────────────────────────────────────
Example:  Deninger's program
What:     Identified ALL the properties the cohomology must have
Why fail: Nobody has constructed a theory with all those properties
Lesson:   The specification is clear; the construction is the hard part

FAILURE MODE 5: "Right reformulation, same difficulty"
────────────────────────────────────────────────────
Example:  Any of the 300+ equivalent reformulations of RH
What:     Translates RH into a different mathematical language
Why fail: The translated problem is exactly as hard
Lesson:   Reformulation ≠ progress unless the new language comes
          with new tools that the old language didn't have
```

---

### 5.3 The Most Instructive Failure: The Analytic Ceiling

The zero-free region approach deserves special attention because its failure
is the most precisely understood.

```
THE 2/3 WALL
═════════════

Best known zero-free region (since 1958):
    σ ≥ 1 - c / (log|t|)^{2/3} (log log|t|)^{1/3}

    This means: as you go up the critical strip, the region
    where we KNOW there are no zeros looks like this:

                Re(s) = 1/2         Re(s) = 1
                     │                  │
     ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─   t = large
                     │       ██████████│
                     │      ███████████│   ← zero-free region
                     │     ████████████│      (known to contain
                     │    █████████████│       no zeros)
                     │   ██████████████│
                     │  ███████████████│
                     │ ████████████████│
     ─ ─ ─ ─ ─ ─ ─ ─│█████████████████│─ ─ ─ ─   t = 0
                     │                  │
                 CRITICAL LINE      Re(s) = 1

    RH says: the zero-free region extends ALL the way
    to the critical line (the entire shaded region above).

    We can prove it extends to the 2/3-power boundary.
    NOTHING in the last 67 years has budged this.

    Why? Because the proof uses inequalities like:
        3 + 4cos(θ) + cos(2θ) ≥ 0
    These are OPTIMAL — no better trigonometric inequality
    exists. The method is squeezed dry. Any improvement
    requires a fundamentally different technique.
```

This is the clearest signal that new mathematics is needed: not a failure
of imagination, but a **provable ceiling** on what existing methods can achieve.

---

## 6. Speculative Directions: Where Might the New Mathematics Come From?

These are informed speculations based on the patterns above.

### 6.1 From Physics: Quantum Gravity and Arithmetic

The zeta zeros behave exactly like energy levels of a quantum system with
chaotic classical dynamics. This is not metaphor — the statistical match is
precise to many decimal places. If we could identify *which* physical system,
the mathematics of that system might contain the proof.

Candidates:
- A quantum system on the adèle class space (Connes)
- A particular quantization of the geodesic flow on the modular surface
  $\text{SL}_2(\mathbb{Z}) \backslash \mathbb{H}$ (Selberg connection)
- Some version of string theory on an arithmetic space (speculative)

### 6.2 From Category Theory: Higher Structures

Modern mathematics increasingly works with higher categories, derived
categories, and homotopy-theoretic structures. Perhaps the cohomology of
$\operatorname{Spec}(\mathbb{Z})$ lives naturally in such a world — it
might require ∞-categorical or derived algebraic geometry tools that didn't
exist when Deninger formulated his program.

Potential connection: **[Condensed mathematics](https://en.wikipedia.org/wiki/Condensed_mathematics)** ([Clausen](https://en.wikipedia.org/wiki/Dustin_Clausen)–[Scholze](https://en.wikipedia.org/wiki/Peter_Scholze)) provides
new ways to do analysis using algebraic structures, potentially bridging the
discrete-continuous divide.

### 6.3 From Machine Learning: Conjecture Generation

ML is unlikely to *prove* RH, but it might:
- Discover the right operator by fitting spectral data
- Find the right test functions that reveal positivity structure
- Identify unexpected patterns in zero data that suggest new conjectures
- Guide formal proof search in Lean/Mathlib

The new mathematics might be *suggested* by ML and then developed by humans.

### 6.4 From Number Theory Itself: Langlands and Beyond

The Langlands program is the most ambitious current program in number theory,
connecting automorphic forms to Galois representations. The [geometric Langlands](https://en.wikipedia.org/wiki/Geometric_Langlands_correspondence) variant was recently resolved. A full Langlands
correspondence would prove GRH for automorphic L-functions. While the
full program is far from complete, advances in it (especially geometric
Langlands, recently resolved by Gaitsgory et al.) might provide unexpected
tools.

---

## 7. A Thought Experiment: What Would the Textbook Look Like?

Imagine the year is 2050 (or 2150) and RH has been proved. A graduate textbook
teaches the proof. What does the table of contents look like?

```
HYPOTHETICAL TEXTBOOK: "Arithmetic Geometry of Spec(Z) and the Riemann Hypothesis"
═══════════════════════════════════════════════════════════════════════════════════

Part I: Foundations
  Ch 1.  The Zeta Function and Its Zeros
  Ch 2.  The Function Field Analogy (Weil, Deligne)
  Ch 3.  Why Classical Methods Have Ceilings

Part II: The New Framework
  Ch 4.  [THE NEW SPACE] — A compactification of Spec(Z) with the
         right geometric properties
  Ch 5.  [THE NEW COHOMOLOGY] — Cohomology groups H^i that are
         infinite-dimensional but well-behaved
  Ch 6.  [THE ARITHMETIC FROBENIUS] — A canonical flow on the
         new space, whose regularized trace gives ζ(s)
  Ch 7.  [THE POSITIVITY THEOREM] — Why the analogue of the Hodge
         index theorem holds in this setting

Part III: The Proof
  Ch 8.  The Trace Formula (connecting zeros to the flow)
  Ch 9.  The Positivity Argument (forcing zeros onto the critical line)
  Ch 10. The Riemann Hypothesis (putting it together)

Part IV: Consequences and Generalizations
  Ch 11. Generalized RH for L-functions
  Ch 12. New Prime Distribution Estimates
  Ch 13. Connections to Physics and Random Matrix Theory
  Ch 14. Open Problems in the New Framework
```

Chapters 4-7 are "the new mathematics." They don't exist today. The book
implies that once those chapters are written — once the space, cohomology,
Frobenius, and positivity theorem are established — the proof of RH
(Chapters 8-10) is relatively straightforward, much as the Weil conjectures
become straightforward once étale cohomology is developed.

This is the nature of problems that require new mathematics: the proof itself
is short, but the foundations it rests on are deep.

---

## 8. Summary: The Shape of What's Missing

```
THE NEW MATHEMATICS FOR RH
══════════════════════════

    Must be:                             Must not be:
    ────────                             ────────────
    ✓ Simultaneously arithmetic          ✗ Just analysis
      and geometric                      ✗ Just algebra
                                         ✗ Just geometry
    ✓ Naturally positive (positivity
      is structural, not a theorem)      ✗ A framework where positivity
                                           is the hard step

    ✓ Natively spectral (operators       ✗ A translation between
      and eigenvalues are built in)        separate theories

    ✓ Able to make exact statements      ✗ Statistical or approximate
      from structural properties

    ✓ Self-evidently natural (the        ✗ An ad hoc construction
      "right" framework that makes         designed solely to prove RH
      RH obvious)

    ✓ Rich enough to prove more          ✗ A narrow tool that proves
      than just RH (GRH, new bounds,       exactly one thing
      connections to physics)

    ✓ Computationally accessible         ✗ Pure existence results
      (makes predictions we can test)      with no computable content

    ✓ Historically grounded (extends     ✗ Mathematics from scratch
      or unifies existing theories)        with no connection to known work
```

The ultimate test of the new mathematics is not whether it can be made to
prove RH through clever argument, but whether, once understood, RH becomes
*obviously true*: as obvious as "self-adjoint operators have real eigenvalues"
or "compact curves over finite fields satisfy the Weil conjectures."

When someone discovers the right framework, the reaction will not be
"what an incredible proof" but rather "of course, how could it be
otherwise?"

---

## 9. Historical Precedent: New Mathematics Is Invented to Order

The claim "RH probably needs new mathematics" can read as an excuse. It is not.
It is the single most common pattern in the history of hard problems. Almost
every era's central problem was eventually settled not by a clever argument
inside the existing tools, but by the invention of a new *kind* of mathematics,
and the invention almost always looked absurd or illegitimate at first. The
purpose of this section is to make that pattern explicit, because it is the
honest frame for this project: ruling out the soft routes (the rest of this
document) is what tells us a new structure is required, exactly as it was
required in each case below.

The recurring shape is: **a specific problem cannot be touched by the available
tools, someone builds a new world to make it touchable, and the new world turns
out to be far larger than the problem that forced it.**

### 9.1 Problems that forced new mathematics into existence

| New mathematics | Forced by | The "impossible" step | Later reach |
|---|---|---|---|
| Complex numbers (Cardano, Bombelli, 1500s) | Solving the cubic | $\sqrt{-1}$ appears *en route* to real answers (casus irreducibilis) | All of analysis, physics, engineering |
| Group theory (Galois, ~1830) | Is the quintic solvable by radicals? | Attach a symmetry group to an equation; solvability becomes a group property | Modern algebra, symmetry everywhere |
| Non-Euclidean geometry (Gauss, Bolyai, Lobachevsky, 1820s) | Proving Euclid's parallel postulate | *Deny* the postulate and get a consistent geometry | General relativity (Einstein, 1915) |
| Set theory, transfinite numbers (Cantor, 1870s) | Uniqueness of trigonometric (Fourier) series | Infinities come in different sizes | Foundations of all mathematics |
| Topology (Poincaré, 1890s) | The three-body problem | Abandon exact solutions for qualitative shape (homology, $\pi_1$) | Geometry, data, physics |
| Computability (Turing, Church, Gödel, 1930s) | Hilbert's Entscheidungsproblem | First define "algorithm" precisely, to prove no algorithm exists | All of computer science |

Other clear instances of the same move: calculus (Newton, Leibniz) to handle
motion and tangents; measure theory and the Lebesgue integral, because the
Riemann integral was too weak to survive limits; distribution theory (Schwartz,
1940s) to make the physicists' Dirac delta legal; quaternions (Hamilton, 1843)
to do three-dimensional rotation, at the cost of giving up commutativity;
Kolmogorov's measure-theoretic axioms (1933) to turn probability into
mathematics.

The lesson is uniform. In each case the established mathematicians of the day
often considered the new object illegitimate (Kronecker against Cantor's
infinities, generations of geometers certain the parallel postulate *must* be
provable, "imaginary" and "sophistic" numbers). The new mathematics was not a
trick to evade the problem. It was the structure in which the problem became a
theorem.

### 9.2 The precedent that this project is directly chasing

The most important precedent for the Riemann Hypothesis is the one that already
happened, for the same statement in a different world: the **Weil conjectures**,
including the Riemann Hypothesis for varieties over finite fields.

```
1949   Weil conjectures the RH-analogue over finite fields, and SEES that a
       proof would need a tool that does not yet exist: a cohomology theory
       for algebraic varieties over F_q, with a Lefschetz fixed-point formula
       turning "count solutions" into "count eigenvalues of Frobenius," and a
       Hodge-index-type positivity forcing |eigenvalue| = sqrt(q).

1960s  Grothendieck builds that tool from the foundations up: schemes, topos
       theory, etale cohomology. An entire new geometry, created largely to
       make the missing cohomology exist.

1974   Deligne completes the proof. The finite-field Riemann Hypothesis is now
       a THEOREM, because the new mathematics was built.
```

This is exactly the bet of Architecture 2 (Direction 8). Experiment
[2F](../../experiments/arithmetic_geometric/e2f_hodge_index_sweep.py) in this
project exhibits the payoff concretely: over finite fields the bound
$|\alpha_i| = \sqrt{q}$ holds *exactly* across a whole family of curves, because
the machinery (the Hodge index theorem on $C \times C$) exists there. The gap
for the real RH is precisely that the analogous machinery over
$\mathrm{Spec}(\mathbb{Z})$ has never been built: there is no Frobenius, no
surface $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, no index
theorem. The function-field case is not an analogy that might help. It is a
completed instance of the exact pattern, where the new mathematics arrived and
turned the hypothesis into a theorem.

### 9.3 Why this is the honest frame, not pessimism

This project's experimental thread keeps finding the same thing from the inside:
the soft tools provably cannot reach (the marginal-positivity results, the
Level-3 ceiling, the $2/3$ analytic ceiling, the K1 wall). In the historical
record, that is not the sound of a dead end. It is the sound that immediately
precedes new mathematics: the quintic, the parallel postulate, the three-body
problem, and the finite-field RH all looked exactly this way until the new
structure was built. Ruling out what cannot work is how the field learns what
the new structure has to be.

So "RH needs new mathematics" is a statement of where to dig, with a long track
record of digging there successfully. The marginal-positivity finding points at
the exact structure of $\zeta$; the function-field precedent points at
intersection-theoretic positivity over $\mathrm{Spec}(\mathbb{Z})$ as the shape
of the missing tool. Both are coordinates, not walls.

---

## Further Reading

- **Deninger, C.** (1992–) — The cohomological program for Spec(Z)
- **Connes, A.** (1999) — Noncommutative geometry and the zeros of ζ
- **Berry, M.V. & Keating, J.P.** (1999) — The spectral interpretation
- **Manin, Y.I.** (1995) — Lectures on zeta functions and motives
- **Connes, A. & Consani, C.** (2011) — Geometry over F_1
- **Clausen, D. & Scholze, P.** (2019–) — Condensed mathematics (potential new foundations)
- **Gaitsgory, D. et al.** (2024) — Proof of geometric Langlands (new tools)

See also: [Research Atlas](../research_atlas/README.md) §4 for the concise
version of what new mathematics is needed, and
[Solutions](../solutions/README.md) for detailed analysis of each approach
and its obstacles.

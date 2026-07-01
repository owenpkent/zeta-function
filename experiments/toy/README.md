# The RH toy sandbox

A checkable training ground for the M4 move. Curves over a finite field $\mathbb{F}_q$ are
the toy world where RH is a **theorem** (Weil 1948, Deligne 1974) with the identical
skeleton to the real problem: an Euler product, a functional equation, and a positivity
that is secretly a Hodge-index / Rosati polarization (the project's M4). Because the answer
is known here, this sandbox does the one thing that is impossible over $\mathbb{Z}$: it
**grades a proposed M4 construction as right or wrong**, and catches a soft, circular, or
Davenport-Heilbronn-blind argument on contact.

```powershell
python -m experiments.toy.play          # the full demo (battery + grading + spectral toy)
python -m experiments.toy.selberg       # just the abstract Selberg / Hilbert-Polya spectral toy
python -m experiments.toy.ihara         # the Ihara / graph proven world (graph-RH <=> Ramanujan)
python -m experiments.toy.ihara_grader  # the spectral grader on the graph world
python -m experiments.toy.interlacing   # the MSS non-variety sqrt(q) source and why it does not transfer
python -m experiments.toy.alon_boppana  # marginal positivity as a theorem (Alon-Boppana = extremality)
python -m experiments.toy.archimedean_place  # the archimedean place = atomic-flat vs continuous-never-flat
python -m experiments.toy.test_toy      # the smoke test (12/12)
```

## Why it helps

The project's binding constraint, per [`../../docs/03_research/optimizing_rh_for_ai.md`](../../docs/03_research/optimizing_rh_for_ai.md),
is the **value-signal blind spot**: at M4 there is no cheap gradient, because numerics
provably cannot separate $\zeta$ from a near-counterexample (the #34 stealth window). The
toy is the one place the gradient exists. It lets you:

1. **Manufacture the missing gradient.** Right vs wrong is decidable here, so a proposed
   *move* is scored instantly.
2. **Practice the M4 move in a checkable setting.** If a "proof" of positivity secretly read
   off the zeros (K1), or also "worked" for the fake-zeta (D-H-blind), the grader catches it.
3. **Localize the real obstruction.** When a move works in the toy and fails to lift to
   $\mathbb{Z}$, the precise delta is the most exact statement of what is missing.

## The battery (`instances.py`)

Each instance is a finite Frobenius spectrum in normalized coordinates $u = \alpha/\sqrt q$,
closed under $u \mapsto 1/u$ (Rosati) and conjugation, so the moment sequence
$c_n = \sum_u u^n$ is real with $c_0 = 2g$. Under RH every $|u| = 1$ (Weil), so
$c_n = \sum 2\cos(n\phi)$; off RH some $|u| \neq 1$. The point-count reading is
$c_n = (q^n + 1 - \#C(\mathbb{F}_{q^n}))/q^{n/2}$.

- **Positive battery (RH true):** real elliptic curves (genus 1) plus synthetic on-circle
  genus 2 and 3 Weil spectra.
- **Negative battery (RH false):** the canonical integer fake-zeta from e2xx
  ($P(T) = T^4 - 4T^3 + 15T^2 - 20T + 25$ over $q=5$, roots off the circle), a complex
  off-circle quad, a real off-circle pair (the discriminant real-root half that the #119
  screen retires), and Davenport-Heilbronn (a functional equation but no Euler product, so
  no finite spectrum and no moments).

The eigenvalue multiset is the **answer key**. A candidate never sees it: it receives only
`ToyData` (`q`, `genus`, the moments $c_0..c_K$, the Euler-product flag), which is exactly
the K1-clean information a real M4 construction is allowed to use.

## Writing a candidate (`grader.py`)

A candidate is a function

```python
def my_candidate(data: ToyData) -> np.ndarray | None:
    # build a real symmetric matrix M from data.q, data.genus, data.moments (c_0..c_K)
    # M is your claim: PSD <=> RH. Return None when uninstantiable (no Euler product).
    ...

from experiments.toy import grade
print(grade(my_candidate, "my candidate").report())
```

The grader scores four things:

| check | meaning |
|---|---|
| `reproduces_weil` | $M$ is PSD on every RH-true instance (matches the proven theorem) |
| `rejects_fakes` | $M$ is indefinite on every RH-false instance (catches the off-line zero) |
| `k1_clean` | structural: the candidate only ever saw point counts, never $\lvert u\rvert$ or the on-circle assumption, so it cannot have read the answer off the zeros |
| `dh_immune` | on the no-Euler-product instance the construction is uninstantiable, so it cannot spuriously certify D-H |

The **reference candidate** (`moment_matrix_candidate`) is the e2xx Toeplitz moment matrix
$G = [c_{|j-k|}]$; by Caratheodory-Toeplitz it is PSD at every order iff all $|u| = 1$ iff RH
for the curve. It scores all green. Two demonstration "bad" candidates (`identity_candidate`,
`diag_moment_candidate`) fail `rejects_fakes`, showing a soft / wrong-polarity form has no RH
content.

## The spectral toy (`selberg.py`)

The Architecture-1 (Hilbert-Polya) training ground. For a compact hyperbolic surface the
Selberg zeta zeros sit at $s = \tfrac12 \pm i\,r_n$ with $\tfrac14 + r_n^2 = \lambda_n$, the
Laplacian eigenvalues. The Laplacian is self-adjoint and $\geq 0$, so $r_n$ is real and the
zeros lie on $\mathrm{Re}(s) = \tfrac12$: the RH-analogue is a theorem *because* the operator
is self-adjoint and bounded below. The toy shows that removing self-adjointness pushes the
zeros off the line, and that for $\zeta$ the zeros are **resonances, not eigenvalues**, which
is exactly why the move does not transfer (LEARNINGS #128 Front 3).

## The second proven world (`ihara.py`, `ihara_grader.py`)

The abstract `selberg.py` models the Laplacian by a random symmetric matrix. `ihara.py`
replaces that stand-in with a **genuine, finite, fully computable dynamical zeta** whose
RH-analogue is a theorem, giving a second checkable world alongside the function-field one.

For a connected $(q+1)$-regular graph $G$ the Ihara zeta is a product over the **primitive
closed cycles** of $G$ (literally the periodic orbits, cycle length playing the role of
$\log p$), and the Ihara-Bass determinant formula collapses it onto the adjacency spectrum:

$$Z_G(u)^{-1} = (1-u^2)^{r-1}\det(I - Au + qu^2).$$

The substitution $u = q^{-s}$ sends $|u| = 1/\sqrt q$ to $\mathrm{Re}(s) = \tfrac12$, and

$$\text{graph RH} \iff \text{Ramanujan} \iff |\lambda_{\text{nontrivial}}| \le 2\sqrt q,$$

a theorem (Ihara, Bass; the Ramanujan equivalence is standard, Terras 2011). This is the
spectral cousin of the function-field Weil bound $|\alpha| = \sqrt q$, same $\sqrt q$.

**A native Davenport-Heilbronn.** A non-Ramanujan regular graph has the *same* Ihara
functional equation yet poles off $|u| = 1/\sqrt q$: a genuine off-line "zero." So the graph
world carries its own wrong-approach detector, native rather than imported. `two_clique_bridge`
(two barely-coupled cliques, $d \ge 5$) and `cycle_power` ($C_n^k$, $k \ge 3$) are guaranteed
non-Ramanujan and serve as the negative battery.

The grader (`ihara_grader.py`) mirrors the four axes, with the D-H axis specialized:

| check | meaning |
|---|---|
| `reproduces_ramanujan` | $M$ PSD on every Ramanujan (RH-true) graph |
| `rejects_nonramanujan` | $M$ indefinite on every non-Ramanujan graph (the native D-H) |
| `k1_clean` | the candidate saw only closed-walk counts $N_k = \mathrm{tr}(A^k)$ and public structure, never the spectrum |
| `gap_is_the_content` | structural: self-adjointness (real spectrum) is free, so the discriminating part is the $2\sqrt q$ gap |

The reference candidate is the $[-1,1]$ moment form: with $\nu = \lambda/(2\sqrt q)$, Ramanujan
means every $\nu \in [-1,1]$, which by the Hausdorff moment theorem holds iff both the Hamburger
Hankel $H_0 = [m_{i+j}]$ and the localizing $H_1 = [m_{i+j} - m_{i+j+2}]$ are PSD. It scores all
green. The instructive failure is `hamburger_only_candidate`: $H_0$ alone is PSD for **every**
symmetric $A$, so certifying self-adjointness reproduces the curves but **fails to reject** the
native D-H. That is the exact lesson for $\zeta$: the operator (real ordinates) is free; the
polarization (the localizing block, the spectral gap) is the whole content, which is M4.

## The R1 sourcing probe (`interlacing.py`)

The Ihara world raises a sharp question. The graph-RH bound is the same $\sqrt q$ as the
function-field Weil bound, and in arithmetic that bound (the purity $|\alpha| = \sqrt q$) is
**variety-gated**: it is Deligne's theorem, sourced from a variety (the project's R1 sourcing
gap, [LEARNINGS #130](../../docs/03_research/sourcing_gap_r1.md)). But in the graph world the
same bound has a second source that uses **no variety at all**: Marcus-Spielman-Srivastava
(Interlacing Families I, Annals 2015) prove bipartite Ramanujan graphs of every degree exist
by the method of expected characteristic polynomials. So the graph world **crosses** R1 by a
combinatorial route.

`interlacing.py` exhibits the engine and then asks whether it transfers. Part 1 confirms the
non-variety $\sqrt q$ source on small graphs, three checkable facts:

- **Godsil-Gutman**: the average over edge-signings of $\det(xI - A_s)$ equals the matching polynomial $\mu(G)$ (verified to $10^{-15}$).
- **Heilmann-Lieb**: $\mu(G)$ is real-rooted with all roots in $[-2\sqrt{d-1}, 2\sqrt{d-1}]$, the Ramanujan window.
- **Interlacing**: a good signing exists (best top eigenvalue $2.00$ for $K_{3,3}$, $1.73$ for $Q_3$, both under the bound), so a Ramanujan 2-lift is sourced with no variety.

Part 2 shows why it does not reach Spec($\mathbb{Z}$). The engine's fuel is **real-rootedness**
(Heilmann-Lieb, and the interlacing family needs real-rooted polynomials), which holds because
the signed adjacency $A_s$ is symmetric (self-adjoint). The arithmetic L-polynomial (the
characteristic polynomial of Frobenius on $H^1$) is **not** real-rooted: its roots are the
Frobenius eigenvalues on the circle $|\alpha| = \sqrt q$, genuinely complex (measured
$\max|\mathrm{Im}\ \text{root}| \approx 0.8$ to $1.0$ across the curve battery). There is no
self-adjoint operator behind Frobenius, which is Hilbert-Polya, the open problem.

**Net.** The non-variety $\sqrt q$ source is paid for with self-adjointness, exactly the
ingredient the Ihara grader showed is free in the graph world and absent over $\mathbb{Z}$. R1
(the sourcing gap) and M4 (the polarization gap) are two faces of the one missing self-adjoint
operator, and #130 sharpens from "variety-gated" to "self-adjointness-gated." MSS is added to
the transfer-search corpus ([`../lemma_db/transfer_search.py`](../lemma_db/transfer_search.py))
as a killed R1 source, sibling to the Lorentzian / real-stable kill.

## Marginal positivity as a theorem (`alon_boppana.py`)

The project's central empirical finding is **marginal positivity**: RH is true only at the
margin, with no buffer for soft proofs, and the session-019 program read this as **extremality**
(an extreme point cannot be marginally true by accident). Both are findings over $\mathbb{Z}$,
not theorems. The graph world makes them theorems.

The graph-RH bound $|\lambda_{\text{nontrivial}}| \le 2\sqrt q$ is bracketed by two theorems.
**Alon-Boppana**: any growing family of $(q+1)$-regular graphs has $\liminf$ nontrivial spectral
radius $\ge 2\sqrt q - o(1)$ (you cannot asymptotically beat Ramanujan). **Friedman**: a random
regular graph meets it up to $o(1)$. So every family's nontrivial spectral radius **converges to
$2\sqrt q$**: the bound is universal and saturated, beatable by none, and a Ramanujan graph
(which meets it) is **extremal**. That is marginal positivity, proven, and the extremality
reading, proven.

`alon_boppana.py` exhibits this. Cycles give the deterministic version: the margin $2 - \lambda_2(C_n)$
falls $0.59 \to 0.15 \to 0.038 \to \ldots \to 0.0006$, no fixed buffer. Random $d$-regular graphs
have their nontrivial radius concentrate at $2\sqrt{d-1}$ (within $\pm 0.05$ by $n = 600$), while
the native Davenport-Heilbronn graphs sit strictly above. The mechanism is the **universal cover**:
$2\sqrt q$ is the spectral radius of the $(q+1)$-regular infinite tree (the edge of the Kesten-McKay
measure, verified empirically at $2.819$ vs $2.828$ for $d=3$), which covers every finite regular
graph. A finite graph cannot beat its own universal cover, so there is no buffer.

**Honest caveat** (the same as the interlacing probe): this proof of "marginal = extremal" runs on
the self-adjoint adjacency spectrum (the tree's real spectral radius), exactly the ingredient
$\zeta$ lacks. So it validates the **frame** (extremality is the right reading of marginal
positivity) without transferring the **proof**; the self-adjointness gap of #139 and #140 is
unchanged.

## The archimedean place, localized (`archimedean_place.py`)

The function-field world has no archimedean place, a finite atomic Frobenius spectrum, and RH
as a theorem. Over $\mathbb{Q}$ there is exactly one extra place, the archimedean one, carried
by the $\Gamma$-factor in $\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$. The whole difficulty of RH
localizes at that one place, so the question is what adding it changes.

The answer uses the flat-extension mechanism (LEARNINGS #79, #80): a measure is finitely atomic
iff its moment (Hankel) matrix goes **flat** (a machine-zero eigenvalue at a fixed order), and
Curto-Fialkow then pins it, which is why the function-field RH is decidable; a **continuous**
measure never flattens. The new content is the identification of the archimedean continuous
spectrum with the **universal cover**: by #141 the $(q+1)$-regular tree has a continuous
Kesten-McKay spectrum. So:

$$\text{adding the archimedean place} = \text{passing to the continuous spectrum of the universal cover} = \text{flat becomes never-flat}.$$

`archimedean_place.py` verifies three parts. Part 1: finite graphs are atomic and go flat at
their atom count ($K_6$ at order 1, Petersen at order 2). Part 2: the Kesten-McKay measure is
continuous, its Hankel never flat (min eigenvalue stays positive, $m_2 = d$). Part 3: growing
finite graphs' normalized moments converge to the Kesten-McKay moments (distance $0.078 \to
0.0018$), so the atomic measures approach the continuous limit. The one archimedean place is
that infinite-volume passage from atomic-flat (RH-provable) to continuous-never-flat (RH-hard),
unifying #141 (the tree as the marginal continuous limit), #79/#80 (flat vs never-flat), and
`../chaos/c4_prime_orbit_spectrum.py` (the $\Gamma$-factor as the continuous mean). Same honest
caveat: a structural model of the obstruction shape on the self-adjoint spectrum, not $\zeta$'s
arithmetic archimedean content.

## The honest caveat

The toy trains the **move**, it cannot contain the **obstruction**. The function-field
spectrum is finite and sits on one circle; $\zeta$'s is infinite and accumulates (the $(1,p)$
bidegree). The moment-matrix move that is all green here provably **dissolves** over
$\mathbb{Z}$: $\zeta$'s Li sequence is strictly log-concave, hence not a moment sequence
(LEARNINGS #128 Front 2, [`../positivity/e3s_li_hankel_dissolves.py`](../positivity/e3s_li_hankel_dissolves.py)).
So a green scorecard means "the move is K1-clean and correct in the toy," **not** "it lifts to
RH." The delta between toy-success and $\mathbb{Z}$-failure is the compass.

## Provenance and related work

- Reuses [`../lemma_db/fq_shadow.py`](../lemma_db/fq_shadow.py) (genus-1 eigenvalues, the
  function-field shadow as the positive control) and the moment-matrix positivity of
  [`../arithmetic_geometric/e2xx_higher_rank_rosati.py`](../arithmetic_geometric/e2xx_higher_rank_rosati.py).
- The D-H firewall: [`../_shared/davenport_heilbronn.py`](../_shared/davenport_heilbronn.py).
- The strategic frame: [`../../docs/03_research/all_roads_to_the_signature.md`](../../docs/03_research/all_roads_to_the_signature.md),
  [`../../docs/03_research/m4_construction_attempt.md`](../../docs/03_research/m4_construction_attempt.md).

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
python -m experiments.toy.selberg       # just the Selberg / Hilbert-Polya spectral toy
python -m experiments.toy.test_toy      # the smoke test
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

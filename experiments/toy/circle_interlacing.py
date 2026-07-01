"""Can the interlacing-families engine run CIRCLE-ROOTED? The averaging step is the gate.

The question (LEARNINGS #140). The Marcus-Spielman-Srivastava engine sources the
sqrt(q) purity bound for graphs with no variety (interlacing.py), and its fuel is
REAL-ROOTEDNESS, which the graph world gets free from self-adjointness of the signed
adjacency. The arithmetic L-polynomial is CIRCLE-rooted (Frobenius eigenvalues on
|alpha| = sqrt(q)), not real-rooted, so the engine stalls over Z. The follow-up this
module pins by computation: is the obstruction merely the root LOCUS (circle vs
line), so the engine could be rebuilt to run on the circle-rooted side?

The answer the battery supports: NO, and the gate sits one step deeper than #140
stated. Neither the locus nor the interlacing order is the missing piece; the
engine's motor, the EXPECTED-CHARACTERISTIC-POLYNOMIAL (averaging) step, is what
dies without operator-class (self-adjoint/unitary) structure, in every ensemble
tested here.

  Part 1 (Tests 1-4). The locus is a coordinate, not an obstruction. For a genus-g
      curve over F_q the L-polynomial is q-self-inversive, and the trace substitution
      x = T + q/T turns circle-rootedness (all Frobenius roots on |T| = sqrt(q)) into
      REAL-rootedness of the degree-g real Weil polynomial h with roots in
      [-2 sqrt(q), 2 sqrt(q)]. Verified on genuine brute-force-counted curves (genus
      1 and 2). The failure modes then split: the arithmetic fake (the #123 genus-2
      Davenport-Heilbronn analogue) loses real-rootedness of h ITSELF (roots 2 +/- i),
      while the graph fake keeps real-rootedness for free (symmetric adjacency) and
      can only exit the window. With a self-adjoint carrier the sole failure mode is
      exit-the-window; without one, real-rootedness itself CAN also be lost (both
      modes stay open in the no-carrier world: FE-true real-rooted-but-out-of-window
      quartics exist too, e.g. (T^2 - 5T + 5)(T^2 + 5T + 5) from t^2 > 4q factors).
      That possible-failure-modes dichotomy is the finding of Part 1.

  Part 2 (Tests 5-6). The interlacing ORDER exists on the circle. Para-orthogonal
      polynomials on the unit circle (POPUC, Szego recursion on Verblunsky
      coefficients; Simon, OPUC vol. 1; Cantero-Moral-Velazquez) are circle-rooted,
      and two distinct boundary parameters beta give strictly interlacing zeros. So
      the order is not the missing fuel. But both facts are sourced by the truncated
      CMV matrix with unitary boundary condition (rank-one unitary perturbations):
      the circle-rooted order exists exactly because a NORMAL operator sits behind
      it, the same operator-class ingredient.

  Part 3 (Tests 7-10). The sharp mechanism. The engine that works (Godsil-Gutman:
      the +-1 edge-signing average of char(A_s) equals the real-rooted matching
      polynomial) survives averaging because 2-cycles contribute |s|^2 = 1 under the
      SYMMETRIC pairing. The holomorphic analogue collapses: for a fixed unitary U
      and iid uniform phases D = diag(e^(i theta_j)), E[det(zI - DU)] = z^n EXACTLY
      (every nonempty principal minor carries a product of independent mean-zero
      phases), verified both exactly (discrete mean-zero phase groups) and by Monte
      Carlo at the M^(-1/2) rate. Hermitian phase-signing survives (average = the
      matching polynomial again: 2-cycles pair e^(i theta) with its conjugate). The
      CUE anchor: E_Haar[det(zI - U)] = z^N (first moment trivial) while the
      sesquilinear second moment E[|det(I - U)|^2] = N + 1 (Keating-Snaith) is where
      the content lives. In every family tested here, content survives averaging
      only through CONJUGATE PAIRING; the independent-phase and Haar holomorphic
      first moments are structurally trivial. (Ensemble-specific, not circle-
      universal: structured non-Haar ensembles carry rich holomorphic first
      moments, e.g. unitary Brownian motion's unitary Hermite law, Kabluchko
      2025, and the conjugate-paired phase subtorus, whose first moment is
      nontrivial and empirically circle-rooted; each such survivor presupposes
      the unitary carrier plus conjugate pairing.) The averaging step is powered
      by self-adjointness on both sides (the operator AND the pairing).

  Part 4 (Test 11). The Z-side landing of the dictionary: RH is exactly the
      statement that Xi(t) = xi(1/2 + it) is real-rooted, the classical
      Laguerre-Polya / de Bruijn-Newman face the project has already mapped
      (LEARNINGS #38/#39). Wired numerically at 30 digits: Xi is real on the real
      axis and changes sign across the first three zeta zeros.

Net. Circle-rootedness IS real-rootedness in the trace coordinate, and interlacing
IS available on the circle, yet the engine still cannot run: in every tested
family, expectation preserves root-locus structure only through conjugate
(sesquilinear) pairing inside a unitary carrier, and the circle locus has no
native one-sided order for the extremal-selection step. This sharpens #140: the
R1/M4 gate is operator-class structure (self-adjoint/unitary) at the AVERAGING
step, presupposed rather than manufactured, so MSS-on-the-circle is not a route
around Hilbert-Polya.

Run from the repo root:  python -m experiments.toy.circle_interlacing
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
from mpmath import mp

from experiments.toy.ihara import cycle_power, graph_rh_verdict, two_clique_bridge
from experiments.toy.interlacing import (
    cube_edges,
    degree,
    expected_char_poly,
    matching_polynomial,
)


# ---------------------------------------------------------------------------
# Finite-field helpers. Prime fields use plain ints; F_25 and F_125 use
# polynomial arithmetic modulo an irreducible modulus that is VERIFIED
# irreducible at construction (a reducible modulus would silently corrupt
# every point count downstream, so it fails loudly instead).
# ---------------------------------------------------------------------------
class ExtField:
    """F_{p^k} for k in {2, 3}: elements are length-k tuples of ascending
    coefficients mod p; the modulus is monic ascending of length k + 1. For
    degree 2 or 3, having no root in F_p is exactly irreducibility."""

    def __init__(self, p: int, modulus: tuple) -> None:
        self.p = p
        self.k = len(modulus) - 1
        if self.k not in (2, 3):
            raise ValueError("only F_{p^2} and F_{p^3} are needed here")
        if modulus[-1] % p != 1:
            raise ValueError("modulus must be monic")
        self.modulus = tuple(c % p for c in modulus)
        for x in range(p):
            if sum(c * x ** i for i, c in enumerate(self.modulus)) % p == 0:
                raise ValueError(f"modulus {modulus} has a root mod {p}: reducible")
        self.q = p ** self.k

    def elements(self):
        return itertools.product(range(self.p), repeat=self.k)

    def one(self) -> tuple:
        return (1,) + (0,) * (self.k - 1)

    def lift(self, c: int) -> tuple:
        return (c % self.p,) + (0,) * (self.k - 1)

    def add(self, a: tuple, b: tuple) -> tuple:
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def mul(self, a: tuple, b: tuple) -> tuple:
        p, k = self.p, self.k
        conv = [0] * (2 * k - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    conv[i + j] = (conv[i + j] + x * y) % p
        for i in range(2 * k - 2, k - 1, -1):        # kill degrees >= k, top down
            c = conv[i]
            if c:
                for j in range(k):
                    conv[i - k + j] = (conv[i - k + j] - c * self.modulus[j]) % p
                conv[i] = 0
        return tuple(conv[:k])

    def pow(self, a: tuple, e: int) -> tuple:
        result, base = self.one(), a
        while e:
            if e & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            e >>= 1
        return result

    def is_zero(self, a: tuple) -> bool:
        return all(c == 0 for c in a)

    def sqrt_count(self, v: tuple) -> int:
        """Number of y in F_q with y^2 = v (q odd): 1 + chi(v) with chi(0) = 0,
        by Euler's criterion chi(v) = v^((q-1)/2)."""
        if self.is_zero(v):
            return 1
        return 2 if self.pow(v, (self.q - 1) // 2) == self.one() else 0


def sqrt_count_prime(p: int, v: int) -> int:
    v %= p
    if v == 0:
        return 1
    return 2 if pow(v, (p - 1) // 2, p) == 1 else 0


def eval_poly_ext(F: ExtField, coeffs_ascending, x: tuple) -> tuple:
    """Horner evaluation of an integer polynomial at x in F_{p^k}."""
    acc = (0,) * F.k
    for c in reversed(coeffs_ascending):
        acc = F.add(F.mul(acc, x), F.lift(c))
    return acc


def count_elliptic_points(p: int, a: int, b: int) -> int:
    """#E(F_p) for y^2 = x^3 + ax + b, brute force, point at infinity included."""
    if (4 * a ** 3 + 27 * b ** 2) % p == 0:
        raise ValueError(f"singular cubic over F_{p}: (a,b)=({a},{b}) is not elliptic")
    return 1 + sum(sqrt_count_prime(p, x ** 3 + a * x + b) for x in range(p))


def weil_fe_ok(coeffs_ascending, q: int, g: int, roots_are: str) -> bool:
    """Exact functional-equation test for a degree-2g Weil polynomial over F_q.

    roots_are = "alpha":   chi(T) = prod (T - alpha), ascending coeffs d,
                           FE  <=>  d[m] * q^m == d[2g-m] * q^g  for all m.
    roots_are = "1/alpha": P(T) = prod (1 - alpha T) (spec form
                           P(T) = q^g T^{2g} P(1/(qT))), ascending coeffs c,
                           FE  <=>  c[m] * q^g == c[2g-m] * q^m  for all m.
    Integer-exact, no floats."""
    c = list(coeffs_ascending)
    if len(c) != 2 * g + 1:
        return False
    for m in range(2 * g + 1):
        if roots_are == "alpha":
            lhs, rhs = c[m] * q ** m, c[2 * g - m] * q ** g
        elif roots_are == "1/alpha":
            lhs, rhs = c[m] * q ** g, c[2 * g - m] * q ** m
        else:
            raise ValueError("roots_are must be 'alpha' or '1/alpha'")
        if lhs != rhs:
            return False
    return True


# ---------------------------------------------------------------------------
# Szego recursion / para-orthogonal polynomials on the unit circle (POPUC).
# Polynomials are ascending complex coefficient arrays.
# ---------------------------------------------------------------------------
def szego_step(phi: np.ndarray, a: complex) -> np.ndarray:
    """One Szego step: Phi_{k+1}(z) = z Phi_k(z) - conj(a) Phi_k^*(z), where
    Phi_k^*(z) = z^k conj(Phi_k(1/conj(z))) = reversed conjugated coefficients."""
    z_phi = np.concatenate(([0.0 + 0.0j], phi))
    star = np.concatenate((np.conj(phi[::-1]), [0.0 + 0.0j]))
    return z_phi - np.conj(a) * star


def szego_phi(alphas) -> np.ndarray:
    """Phi_n from Verblunsky coefficients alpha_0..alpha_{n-1} (all in the open disk)."""
    phi = np.array([1.0 + 0.0j])
    for a in alphas:
        phi = szego_step(phi, a)
    return phi


def para_orthogonal(alphas, beta: complex) -> np.ndarray:
    """B_n(z; beta) = z Phi_{n-1}(z) - conj(beta) Phi_{n-1}^*(z), |beta| = 1.
    All n zeros lie on the unit circle (Simon, OPUC vol. 1, Thm 2.2.12)."""
    return szego_step(szego_phi(alphas), beta)


def poly_zeros_ascending(coeffs: np.ndarray) -> np.ndarray:
    return np.roots(coeffs[::-1])


# ---------------------------------------------------------------------------
# Small-graph and unitary helpers for Part 3.
# ---------------------------------------------------------------------------
def k4_edges() -> tuple:
    """K_4: 3-regular, 6 edges. Small enough for EXACT enumeration of the
    quartic-phase Hermitian signing average (4^6 = 4096 terms)."""
    return tuple((i, j) for i in range(4) for j in range(i + 1, 4)), 4


def hermitian_phased_adjacency(edges, n: int, phases) -> np.ndarray:
    """(A_theta)_uv = phase on the edge, (A_theta)_vu = its conjugate: Hermitian."""
    A = np.zeros((n, n), dtype=complex)
    for (u, v), ph in zip(edges, phases):
        A[u, v] = ph
        A[v, u] = np.conj(ph)
    return A


def cycle_dft_unitary(n: int) -> np.ndarray:
    """U = P @ F: the n-cycle permutation composed with the unitary DFT, a fixed
    deterministic unitary with generically nonzero principal minors."""
    P = np.zeros((n, n), dtype=complex)
    for i in range(n):
        P[(i + 1) % n, i] = 1.0
    j, k = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    F = np.exp(-2.0j * np.pi * j * k / n) / np.sqrt(n)
    return P @ F


def haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    """Haar CUE sample: QR of a complex Ginibre matrix with the Mezzadri phase
    correction (columns rescaled by R_jj / |R_jj|)."""
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R)
    return Q * (d / np.abs(d))


# ---------------------------------------------------------------------------
# PART 1  The substitution dictionary.
# ---------------------------------------------------------------------------
ELLIPTIC_BATTERY = [
    (5, 1, 1), (5, 2, 1),
    (7, 1, 3), (7, 3, 2),
    (11, 3, 5), (11, 1, 1),
    (13, 1, 1), (13, 6, 2),
]


def test_1_elliptic_dictionary() -> bool:
    """Genuine elliptic curves: brute-force counts give t with the circle and
    window statements holding SIMULTANEOUSLY (the genus-1 dictionary)."""
    print("Test 1  Genus-1 dictionary on brute-force-counted elliptic curves")
    print("        chi(T) = T^2 - tT + p on |T| = sqrt(p)  <=>  h(x) = x - t,"
          " |t| <= 2 sqrt(p)")
    ok = True
    for p, a, b in ELLIPTIC_BATTERY:
        N = count_elliptic_points(p, a, b)
        t = p + 1 - N
        # descending convention: chi(T) = T^2 - tT + p, roots = Frobenius alphas.
        alphas = np.roots([1.0, -float(t), float(p)])
        circle_defect = float(np.max(np.abs(np.abs(alphas) - np.sqrt(p))))
        # ascending convention: P(T) = 1 - tT + pT^2, roots 1/alpha on |T| = 1/sqrt(p).
        proots = np.roots([float(p), -float(t), 1.0])
        inv_defect = float(np.max(np.abs(np.abs(proots) - 1.0 / np.sqrt(p))))
        fe = (weil_fe_ok([1, -t, p], p, 1, "1/alpha")
              and weil_fe_ok([p, -t, 1], p, 1, "alpha"))
        in_window = abs(t) <= 2.0 * np.sqrt(p)
        on_circle = circle_defect < 1e-9 and inv_defect < 1e-9
        # the dictionary is a biconditional: both sides computed independently
        # must AGREE (and, for a genuine curve, both must be True by Hasse/Weil).
        row = fe and on_circle and in_window and (on_circle == in_window)
        ok = ok and row
        print(f"    E/F_{p}: y^2=x^3+{a}x+{b}  N={N:3d}  t={t:+3d}"
              f"  |t|<=2sqrt(p)={in_window}  circle defect={circle_defect:.1e}"
              f"  FE={fe}  {'ok' if row else 'BAD'}")
    print(f"    {len(ELLIPTIC_BATTERY)} genuine curves: circle-rooted and"
          " window-real-rooted, simultaneously.")
    return ok


def test_2_genus2_dictionary() -> bool:
    """A genuine genus-2 curve over F_5, counted over F_5 and F_25, with the
    recovered quartic validated by an INDEPENDENT count over F_125 (any sign
    convention error in a1/a2 fails this loudly)."""
    p, g = 5, 2
    f = [1, 0, 0, 1, 0, 1]                     # f(x) = x^5 + x^3 + 1
    print("Test 2  Genus-2 dictionary: C: y^2 = x^5 + x^3 + 1 over F_5")
    # smoothness: f' = 3x^2 in char 5, gcd(f, f') = 1 since f(0) = 1 != 0.
    N1 = 1 + sum(sqrt_count_prime(p, (x ** 5 + x ** 3 + 1)) for x in range(p))
    F25 = ExtField(p, (3, 0, 1))               # w^2 = 2, a nonresidue mod 5
    N2 = 1 + sum(F25.sqrt_count(eval_poly_ext(F25, f, x)) for x in F25.elements())
    # zeta log-expansion: N_n = q^n + 1 - sum_i alpha_i^n, so with power sums
    # s1 = q + 1 - N1 and s2 = q^2 + 1 - N2, Newton gives e1 = s1, e2 = (s1^2 - s2)/2.
    e1 = p + 1 - N1
    s2 = p ** 2 + 1 - N2
    parity_ok = (e1 * e1 - s2) % 2 == 0
    if not parity_ok:
        print("    FAIL: (e1^2 - s2) is odd, sign conventions are wrong")
        return False
    e2 = (e1 * e1 - s2) // 2
    a1, a2 = -e1, e2                           # P(T) = 1 + a1 T + a2 T^2 + 5 a1 T^3 + 25 T^4
    print(f"    N_1 = {N1}, N_2 = {N2}  ->  e1 = {e1}, e2 = {e2}"
          f"  (a1 = {a1}, a2 = {a2})")
    fe = (weil_fe_ok([1, a1, a2, p * a1, p * p], p, g, "1/alpha")
          and weil_fe_ok([p * p, -p * e1, e2, -e1, 1], p, g, "alpha"))
    # blind cross-check: predict N_3 via Newton (p3 = e1 p2 - e2 p1 + 3 e3, e3 = q e1)
    # and compare with a brute-force count over F_125.
    p1 = e1
    p2 = e1 * p1 - 2 * e2
    p3 = e1 * p2 - e2 * p1 + 3 * (p * e1)
    N3_pred = p ** 3 + 1 - p3
    F125 = ExtField(p, (1, 1, 0, 1))           # u^3 + u + 1, no root mod 5
    N3 = 1 + sum(F125.sqrt_count(eval_poly_ext(F125, f, x)) for x in F125.elements())
    n3_ok = N3 == N3_pred
    print(f"    functional equation (both conventions): {fe}")
    print(f"    N_3 predicted from (N_1, N_2) = {N3_pred},"
          f" brute-force #C(F_125) = {N3}  match = {n3_ok}")
    # the dictionary: chi roots on |T| = sqrt(5) AND h real-rooted in the window.
    chi = [1.0, -float(e1), float(e2), -float(p * e1), float(p * p)]
    alphas = np.roots(chi)
    circle_defect = float(np.max(np.abs(np.abs(alphas) - np.sqrt(p))))
    h = np.array([1.0, -float(e1), float(e2 - 2 * p)])   # h(x) = x^2 - e1 x + (e2 - 2q)
    hroots = np.roots(h)
    h_real = float(np.max(np.abs(hroots.imag))) < 1e-9
    h_window = h_real and bool(np.all(np.abs(hroots.real) <= 2.0 * np.sqrt(p) + 1e-9))
    # the substitution x = T + q/T maps the four alphas 2-to-1 onto the h-roots.
    xs = alphas + p / alphas
    map_defect = float(np.max([np.min(np.abs(xs - r)) for r in hroots]))
    map_ok = map_defect < 1e-6
    print(f"    roots of chi: circle defect = {circle_defect:.1e}  (all on |T| = sqrt(5))")
    print(f"    h(x) = x^2 - ({e1}) x + ({e2 - 2 * p}): roots"
          f" {np.sort(hroots.real).round(4)}  real = {h_real}, in"
          f" [-2 sqrt(5), 2 sqrt(5)] = {h_window}")
    print(f"    substitution x = T + q/T maps chi-roots onto h-roots:"
          f" defect = {map_defect:.1e}")
    return fe and n3_ok and circle_defect < 1e-8 and h_window and map_ok


def test_3_arithmetic_fake() -> bool:
    """The arithmetic D-H control (#123): the RH-false Weil-shaped quartic keeps
    the functional equation, leaves the circle, and its real Weil polynomial has
    COMPLEX roots: loss of real-rootedness is an arithmetic failure mode the
    self-adjoint graph world cannot access (exit-the-window stays possible too)."""
    q, g = 5, 2
    chi_desc = [1, -4, 15, -20, 25]            # descending: chi(T) = prod(T - alpha)
    print("Test 3  The arithmetic fake: P(T) = T^4 - 4T^3 + 15T^2 - 20T + 25, q = 5")
    fe = weil_fe_ok(chi_desc[::-1], q, g, "alpha")
    alphas = np.roots([float(c) for c in chi_desc])
    moduli = np.sort(np.abs(alphas))
    off_circle = float(np.min(np.abs(moduli - np.sqrt(q))))
    # e1 = 4, e2 = 15 from the coefficients; h(x) = x^2 - e1 x + (e2 - 2q).
    e1, e2 = 4, 15
    h = np.array([1.0, -float(e1), float(e2 - 2 * q)])
    hroots = np.sort_complex(np.roots(h))
    h_complex = float(np.min(np.abs(hroots.imag))) > 0.5
    h_matches_spec = np.allclose(np.sort_complex(hroots), np.sort_complex(
        np.array([2.0 - 1.0j, 2.0 + 1.0j])), atol=1e-9)
    print(f"    functional equation holds: {fe}")
    print(f"    root moduli {moduli.round(4)} vs sqrt(5) = {np.sqrt(5):.4f}:"
          f" min distance to circle = {off_circle:.3f} (OFF the circle)")
    print(f"    h(x) = x^2 - 4x + 5: roots {hroots.round(4)} = 2 +/- i, COMPLEX")
    print("    -> the arithmetic fake loses REAL-ROOTEDNESS itself, not just the window.")
    return fe and off_circle > 0.3 and h_complex and h_matches_spec


def test_4_graph_fake() -> bool:
    """The graph D-H control: a non-Ramanujan graph's spectrum is REAL for free
    (symmetric adjacency) and fails only by EXITING the window [-2 sqrt(q), 2 sqrt(q)].
    The failure-mode dichotomy against Test 3 is the finding."""
    print("Test 4  The graph fake: real-rootedness is free, failure = exit-the-window")
    ok = True
    for name, A in [("two_clique_bridge(5)  (5-regular, q=4)", two_clique_bridge(5)),
                    ("cycle_power(30, 3)    (6-regular, q=5)", cycle_power(30, 3))]:
        # real-rootedness check with the GENERAL (non-symmetric) eigensolver, so it
        # is a computation, not an assumption.
        eigs = np.linalg.eigvals(A.astype(float))
        max_imag = float(np.max(np.abs(eigs.imag)))
        v = graph_rh_verdict(A)
        exits = v.max_nontrivial_abs_lambda > v.ramanujan_bound + 1e-9
        row = max_imag < 1e-9 and exits and not v.is_ramanujan
        ok = ok and row
        print(f"    {name}: max|Im lambda| = {max_imag:.1e} (real spectrum),"
              f" max|lambda_nontriv| = {v.max_nontrivial_abs_lambda:.3f}"
              f" > 2 sqrt(q) = {v.ramanujan_bound:.3f}: exits window = {exits}")
    print("    Dichotomy: graph world (self-adjoint carrier) can ONLY fail by exiting")
    print("    the window; arithmetic without a self-adjoint carrier can ALSO fail by")
    print("    losing real-rootedness itself (Test 3). Note cycle_power(30,3) has q = 5, the")
    print("    same q as the arithmetic fake: same window, different failure axis.")
    return ok


# ---------------------------------------------------------------------------
# PART 2  Circle interlacing exists (POPUC).
# ---------------------------------------------------------------------------
def _verblunsky(n: int, seed: int = 20260701):
    rng = np.random.default_rng(seed)
    r = 0.85 * np.sqrt(rng.uniform(size=n - 1))
    th = rng.uniform(0.0, 2.0 * np.pi, size=n - 1)
    return r * np.exp(1j * th)


def test_5_popuc_circle_rooted() -> bool:
    """Para-orthogonal polynomials are circle-rooted: the Szego recursion with
    |beta| = 1 boundary puts all n zeros on |z| = 1 (while the orthogonal Phi_n
    itself, |alpha| < 1 throughout, has all zeros strictly INSIDE the disk)."""
    n = 8
    alphas = _verblunsky(n)
    print("Test 5  POPUC circle-rootedness (Szego recursion, n = 8, seeded Verblunsky)")
    phi = szego_phi(alphas)
    phi_zeros = poly_zeros_ascending(phi)
    max_inside = float(np.max(np.abs(phi_zeros)))
    inside_margin = 1.0 - max_inside
    beta = np.exp(0.9j)
    B = para_orthogonal(alphas, beta)
    zeros = poly_zeros_ascending(B)
    circle_defect = float(np.max(np.abs(np.abs(zeros) - 1.0)))
    print(f"    orthogonal Phi_7 zeros: max|z| = {max_inside:.6f}, margin to the circle"
          f" = {inside_margin:.1e}")
    print("    (strictly inside, the OPUC baseline; an on-circle zero would show a")
    print("    margin at root-finder noise, ~1e-15, not ~1e-3)")
    print(f"    para-orthogonal B_8(z; beta), |beta| = 1: deg = {len(B) - 1},"
          f" max| |z| - 1 | = {circle_defect:.1e}")
    print("    -> setting the boundary parameter unimodular lands ALL zeros on the circle.")
    return inside_margin > 1e-6 and len(B) - 1 == n and circle_defect < 1e-8


def test_6_popuc_interlacing() -> bool:
    """Two distinct unimodular boundary parameters give STRICTLY interlacing
    zeros on the circle: the interlacing ORDER exists circle-rooted. Its source
    is the truncated CMV matrix under rank-one unitary perturbation, i.e. the
    normal-operator structure."""
    n = 8
    alphas = _verblunsky(n)
    beta1, beta2 = np.exp(0.9j), np.exp(2.7j)
    z1 = poly_zeros_ascending(para_orthogonal(alphas, beta1))
    z2 = poly_zeros_ascending(para_orthogonal(alphas, beta2))
    print("Test 6  POPUC interlacing on the circle (beta_1 != beta_2)")
    args = [(float(np.angle(z)) % (2.0 * np.pi), 0) for z in z1]
    args += [(float(np.angle(z)) % (2.0 * np.pi), 1) for z in z2]
    args.sort()
    labels = [lab for _, lab in args]
    alternates = all(labels[i] != labels[(i + 1) % len(labels)]
                     for i in range(len(labels)))
    gaps = [(args[(i + 1) % len(args)][0] - args[i][0]) % (2.0 * np.pi)
            for i in range(len(args))]
    min_gap = float(min(gaps))
    print(f"    2n = {len(args)} zero arguments sorted around the circle:"
          f" strict label alternation = {alternates}, min angular gap = {min_gap:.4f}")
    print("    -> an interlacing ORDER exists on the circle (POPUC). But the")
    print("    circle-rootedness and the interlacing are sourced by the UNITARY CMV")
    print("    truncation (rank-one unitary perturbations): the operator-class")
    print("    ingredient again. The order is not the missing fuel.")
    return alternates and min_gap > 1e-6


# ---------------------------------------------------------------------------
# PART 3  The averaging step collapses without self-adjointness.
# ---------------------------------------------------------------------------
def test_7_signing_average_baseline() -> bool:
    """The engine that works: the exact +-1 edge-signing average of char(A_s)
    equals the matching polynomial (Godsil-Gutman), real-rooted in the Ramanujan
    window (Heilmann-Lieb). Exact enumeration, no sampling."""
    print("Test 7  Baseline: E_signings[char(A_s)] = matching polynomial (exact)")
    ok = True
    for name, (edges, n) in [("K_4", k4_edges()), ("Q_3 cube", cube_edges())]:
        d = degree(edges, n)
        bound = 2.0 * np.sqrt(d - 1)
        mu = matching_polynomial(edges, n)
        avg = expected_char_poly(edges, n)          # all 2^{|E|} signings
        err = float(np.max(np.abs(avg - mu)))
        roots = np.roots(mu)
        max_imag = float(np.max(np.abs(roots.imag)))
        max_root = float(np.max(np.abs(roots.real)))
        row = err < 1e-9 and max_imag < 1e-7 and max_root <= bound + 1e-9
        ok = ok and row
        print(f"    {name}: |avg - mu| = {err:.1e},  max|Im root| = {max_imag:.1e}"
              f" (real-rooted),  max|root| = {max_root:.3f} <= 2 sqrt(d-1)"
              f" = {bound:.3f}")
    print("    The symmetric signing average KEEPS full content: it lands exactly on")
    print("    the real-rooted matching polynomial. This is the motor MSS runs on.")
    return ok


def test_8_holomorphic_average_collapses() -> bool:
    """The holomorphic phase average is trivial: E[det(zI - DU)] = z^n exactly.

    The one-line argument: det(zI - DU) = sum over subsets S of
    (-1)^{|S|} det((DU)[S,S]) z^{n-|S|}, and det((DU)[S,S]) =
    (prod_{j in S} e^{i theta_j}) det(U[S,S]); for S nonempty the phase product
    has independent factors each of mean zero, so every coefficient except z^n
    averages to zero. Verified (a) EXACTLY with the discrete mean-zero phase
    group {+-1}^n (each theta_j appears to power exactly 1, so the sign average
    kills it identically), and (b) by Monte Carlo at the M^(-1/2) rate."""
    n = 6
    U = cycle_dft_unitary(n)
    unit_err = float(np.max(np.abs(U @ U.conj().T - np.eye(n))))
    target = np.zeros(n + 1, dtype=complex)
    target[0] = 1.0                                   # z^n, descending coefficients
    print("Test 8  Holomorphic collapse: E[det(zI - DU)] = z^n for U = P_cycle @ DFT_6")
    print(f"    U unitary: max|U U* - I| = {unit_err:.1e}")
    # (a) exact: average over the 2^n diagonal sign matrices.
    acc = np.zeros(n + 1, dtype=complex)
    for signs in itertools.product((1.0, -1.0), repeat=n):
        acc += np.poly(np.diag(signs) @ U)
    exact_err = float(np.max(np.abs(acc / 2 ** n - target)))
    print(f"    exact discrete-phase average (2^6 sign matrices): max|avg - z^6|"
          f" = {exact_err:.1e}")

    # (b) Monte Carlo with continuous uniform phases: error should fall like M^(-1/2).
    def mc_err(M: int, seed: int) -> float:
        rng = np.random.default_rng(seed)
        acc = np.zeros(n + 1, dtype=complex)
        for _ in range(M):
            D = np.diag(np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, n)))
            acc += np.poly(D @ U)
        return float(np.linalg.norm(acc / M - target))

    err_1k = float(np.mean([mc_err(1000, s) for s in (1, 2, 3)]))
    err_4k = float(np.mean([mc_err(4000, s) for s in (11, 12, 13)]))
    ratio = err_1k / err_4k
    print(f"    Monte Carlo: err(M=1000) = {err_1k:.4f}, err(M=4000) = {err_4k:.4f},"
          f" ratio = {ratio:.2f} (theory sqrt(4) = 2.00)")
    print("    -> the holomorphic average retains NOTHING: every principal minor")
    print("    carries a nonempty product of independent mean-zero phases.")
    return (unit_err < 1e-10 and exact_err < 1e-12
            and err_4k < err_1k and err_4k < 0.15 and 1.2 < ratio < 3.4)


def test_9_hermitian_average_survives() -> bool:
    """Hermitian phase-signing survives: E[char(A_theta)] with theta_ji = -theta_ij
    is again the matching polynomial. In the permutation expansion each edge
    appears with net phase exponent in {-1, 0, +1}: 2-cycles pair e^(i theta)
    with its conjugate (|e^(i theta)|^2 = 1, exponent 0) and survive; longer
    cycles carry a net uniform phase and vanish. So averaging over Z_4 phases
    {1, i, -1, -i} per edge is EXACT (it kills exponents +-1 identically), and
    the continuous-phase Monte Carlo agrees."""
    print("Test 9  Hermitian phase-signing survives: E[char(A_theta)] = matching poly")
    # (a) exact on K_4: enumerate all 4^6 quartic-phase Hermitian signings.
    edges4, n4 = k4_edges()
    mu4 = matching_polynomial(edges4, n4)
    acc = np.zeros(n4 + 1, dtype=complex)
    for ks in itertools.product(range(4), repeat=len(edges4)):
        acc += np.poly(hermitian_phased_adjacency(edges4, n4, [1j ** k for k in ks]))
    avg4 = acc / 4 ** len(edges4)
    imag4 = float(np.max(np.abs(avg4.imag)))
    err4 = float(np.max(np.abs(avg4.real - mu4)))
    print(f"    K_4 exact (4^6 Hermitian phasings): max|avg - mu| = {err4:.1e},"
          f" max|Im| = {imag4:.1e}")
    # (b) Monte Carlo on Q_3 with continuous phases, against Test 7's polynomial.
    edges8, n8 = cube_edges()
    mu8 = matching_polynomial(edges8, n8)
    rng = np.random.default_rng(42)
    M = 3000
    acc = np.zeros(n8 + 1, dtype=complex)
    for _ in range(M):
        phases = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, len(edges8)))
        acc += np.poly(hermitian_phased_adjacency(edges8, n8, phases))
    avg8 = acc / M
    rel_err = float(np.linalg.norm(avg8.real - mu8) / np.linalg.norm(mu8))
    print(f"    Q_3 Monte Carlo (M = {M}, continuous phases):"
          f" ||avg - mu|| / ||mu|| = {rel_err:.4f}")
    print("    -> the CONJUGATE-PAIRED average keeps the full matching-polynomial")
    print("    content; only the paired (2-cycle) terms survive, exactly as in the")
    print("    real signing. Hermitian structure is what feeds the averaging step.")
    return err4 < 1e-10 and imag4 < 1e-10 and rel_err < 0.08


def test_10_cue_anchor() -> bool:
    """The CUE anchor: E_Haar[det(zI - U)] = z^N (the holomorphic first moment is
    trivial: U -> e^(i phi) U rotates the k-th secular coefficient by e^(i k phi),
    so its Haar mean is 0), while the sesquilinear second moment
    E[|det(I - U)|^2] = N + 1 (Keating-Snaith) carries the content."""
    print("Test 10  CUE: first moment trivial, content only in |.|^2 (N + 1 law)")
    ok = True
    M = 4000
    for N in (4, 6, 8):
        rng = np.random.default_rng(100 + N)
        first = np.zeros(N + 1, dtype=complex)
        second = 0.0
        for _ in range(M):
            c = np.poly(haar_unitary(N, rng))
            first += c
            second += abs(np.polyval(c, 1.0)) ** 2
        first /= M
        second /= M
        target = np.zeros(N + 1, dtype=complex)
        target[0] = 1.0
        dev1 = float(np.max(np.abs(first - target)))
        rel2 = abs(second / (N + 1) - 1.0)
        row = dev1 < 0.10 and rel2 < 0.15
        ok = ok and row
        print(f"    N = {N}: max|E[coeffs] - z^N| = {dev1:.3f} (-> 0),"
              f"  E[|det(I-U)|^2] = {second:.3f} vs N + 1 = {N + 1}"
              f" (rel err {rel2:.3f})")
    print("    -> in the tested ensembles, content survives averaging only through")
    print("    CONJUGATE PAIRING (the sesquilinear second moment); the Haar holomorphic")
    print("    first moment is trivial (Haar-exact, not circle-universal). The averaging")
    print("    step is powered by self-adjointness on BOTH sides (operator and pairing).")
    return ok


# ---------------------------------------------------------------------------
# PART 4  The Z-side landing.
# ---------------------------------------------------------------------------
def test_11_xi_real_rooted_face() -> bool:
    """The same substitution over Z: RH says Xi(t) = xi(1/2 + it) is REAL-ROOTED.
    Wired numerically at 30 digits: Xi is real on the real axis and changes sign
    across each of the first three zeta zeros."""
    mp.dps = 30
    print("Test 11  Z-side landing: Xi(t) = xi(1/2 + it) real on R, sign changes at zeros")

    def xi(s):
        return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

    def Xi(t):
        return xi(mp.mpf("0.5") + mp.mpc(0, 1) * mp.mpf(t))

    max_imag = max(abs(mp.im(Xi(t))) for t in ("1", "5", "10", "20"))
    real_ok = max_imag < mp.mpf("1e-25")
    print(f"    reality: max|Im Xi(t)| over t in {{1, 5, 10, 20}} = {mp.nstr(max_imag, 3)}")
    # midpoints bracketing the first three zeros 14.1347, 21.0220, 25.0109.
    mids = ("7.0", "17.5", "23.0", "27.5")
    vals = [mp.re(Xi(t)) for t in mids]
    signs = [1 if v > 0 else -1 for v in vals]
    pattern_ok = signs == [1, -1, 1, -1]
    changes = all(vals[i] * vals[i + 1] < 0 for i in range(3))
    for t, v in zip(mids, vals):
        print(f"    Xi({t:>4}) = {mp.nstr(v, 6):>14}   sign {'+' if v > 0 else '-'}")
    print(f"    three sign changes across gamma = 14.1347, 21.0220, 25.0109: {changes}")
    print("    -> the circle-to-line dictionary lands on the classical Laguerre-Polya /")
    print("    de Bruijn-Newman face (RH = Xi real-rooted, LEARNINGS #38/#39): the")
    print("    real-rootedness zeta needs is exactly what no known operator supplies.")
    return real_ok and pattern_ok and changes


# ---------------------------------------------------------------------------
# The battery.
# ---------------------------------------------------------------------------
PARTS = [
    ("PART 1  The substitution dictionary: circle-rooted IS real-rooted in x = T + q/T",
     [test_1_elliptic_dictionary, test_2_genus2_dictionary,
      test_3_arithmetic_fake, test_4_graph_fake]),
    ("PART 2  Circle interlacing exists (POPUC): the order is not the missing fuel",
     [test_5_popuc_circle_rooted, test_6_popuc_interlacing]),
    ("PART 3  The averaging step collapses without self-adjointness",
     [test_7_signing_average_baseline, test_8_holomorphic_average_collapses,
      test_9_hermitian_average_survives, test_10_cue_anchor]),
    ("PART 4  The Z-side landing",
     [test_11_xi_real_rooted_face]),
]


def main() -> None:
    print("Can the interlacing engine run circle-rooted? (the #140 follow-up)\n")
    passed, total = 0, 0
    for banner, tests in PARTS:
        print(banner)
        print("-" * 78)
        for t in tests:
            total += 1
            ok = t()
            passed += int(ok)
            print(f"  -> {'PASS' if ok else 'FAIL'}\n")
    print("=" * 78)
    print("Verdict: the engine cannot run circle-rooted, and the gate is now localized")
    print("at the AVERAGING step. Part 1: the root locus is a coordinate (circle-rooted")
    print("= real-rooted under x = T + q/T; the arithmetic fake loses real-rootedness,")
    print("the graph fake merely exits the window). Part 2: the interlacing ORDER exists")
    print("on the circle (POPUC), sourced by the unitary CMV truncation. Part 3: the")
    print("expected-char-poly motor keeps content only under conjugate pairing (matching")
    print("polynomial, Keating-Snaith N + 1); the independent-phase/Haar holomorphic")
    print("average is exactly z^n (ensemble-specific, not circle-universal). Part 4:")
    print("over Z the dictionary is the Laguerre-Polya / dBN face. This sharpens #140:")
    print("R1/M4 is operator-class-gated AT THE EXPECTATION STEP (the unitary carrier is")
    print("presupposed, not manufactured; the circle also lacks a native one-sided order")
    print("for the extremal-selection step), so an MSS-on-the-circle rebuild is not a")
    print("route around Hilbert-Polya.")
    print(f"\n{passed}/{total} circle_interlacing tests passed.")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()

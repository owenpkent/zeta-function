"""The HIGHER-RANK AHK/Rosati object: NS(C x C)'s primitive form on Frobenius POWERS,
where genus 1 stops being elementary. This is the construction the #122 faithfulness
caveat said was missing -- and it is buildable, computable, and rigorous over F_q.

WHY THIS, AND WHY NOW (the #122 caveat, made concrete)
------------------------------------------------------
The 09A AHK program (e2uu/#105, e2ww/#122) localized the construction gap to P3 on the
genus-1 function-field shadow, where the primitive intersection form is the 2x2 binary
Gram  Q = [[-2g, -t], [-t, -2gq]],  negative-definite iff |t| < 2 sqrt q (the Weil bound).
The ADVERSARY's load-bearing correction (scratchpad/ahk_tslot/03_adversary.md, LEARNINGS
#122): genus 1 is the EASIEST Weil case. A 2x2 binary quadratic form is definite iff its
determinant is positive -- Hasse proved exactly this bound in 1933 from norm-form positivity,
BEFORE Weil, with NO Hodge index theorem. So in the genus-1 shadow the M4 positivity (P6)
looks automatic the instant P3 is supplied, which is an ARTIFACT. The genuine M4 difficulty
is HIGHER-RANK Rosati positivity (Hodge-Riemann on a >2-dimensional primitive part). That
is precisely what the 2x2 throws away, and it is what nobody in this repo had built: even
e2g's "genus-2" check uses the SAME 2x2 trace-bound form [[-2g,-t],[-t,-2gq]] -- it bounds
only the trace t = Tr(Frob | H^1), never the higher Frobenius moments.

THE OBJECT (the honest higher-rank generalization of e2uu, derived from first principles)
-----------------------------------------------------------------------------------------
On S = C x C take the Frobenius-power correspondences  c_k = Gamma_{q^k} = graph(Frob^k),
k = 0, 1, ..., m  (c_0 = the diagonal Delta).  These are genuine divisor classes; on H^1
they act as pi^k where pi is Frobenius (pi pi^dagger = q, the Rosati involution sending
pi -> q pi^{-1}).  Their PRIMITIVE intersection Gram (project out the hyperbolic plane
<e, f> exactly as in e2g) is

      G^prim_{jk}  =  - M_{jk},      M_{jk} = q^k t_{j-k},   t_n = Tr(pi^n) = sum_i (alpha_i^n + (q/alpha_i)^n)

and the Hodge index theorem says G^prim is NEGATIVE-definite, i.e. M is POSITIVE-definite.
Writing alpha_i = sqrt(q) u_i and normalizing the basis by q^{k/2}, M is congruent to the
real symmetric TOEPLITZ MOMENT MATRIX

      G_m = [ c_{|j-k|} ]_{0<=j,k<=m},    c_n = sum_{i=1}^g (u_i^n + u_i^{-n}) = (q^n + 1 - #C(F_{q^n})) / q^{n/2}.

  * m = 1 is EXACTLY the e2uu/e2g 2x2 form (G_1 = [[2g, c_1],[c_1, 2g]], det = 4g^2 - c_1^2,
    PD iff |c_1| < 2g iff |t| < 2g sqrt q): the trace bound, Hasse's binary form. Genus 1 has
    NOTHING ELSE -- one Frobenius pair gives only c_0, c_1, so the form is 2x2 and that is the
    whole story (the artifact).
  * m >= 2 is a GENUINE (m+1)x(m+1) moment problem. By the Caratheodory-Toeplitz theorem,
    { G_m PSD for all m }  <=>  { c_n are the Fourier coefficients of a POSITIVE measure on
    the unit circle }  <=>  { every u_i lies on |u| = 1 }  <=>  RH for the curve.

So the higher-rank primitive Hodge form is the trigonometric moment matrix of the
symmetrized Frobenius spectrum, and its definiteness is RH for the curve, NOT as a single
determinant but as a positive-definite (Hamburger/Toeplitz) moment sequence. THIS is the
">2-dimensional primitive part" the caveat named, now explicit and computable.

WHAT THIS FILE DEMONSTRATES (and what it does NOT)
--------------------------------------------------
  [1] Genus-1 reduction: m=1 reproduces e2uu's [[-2g,-t],[-t,-2gq]] EXACTLY (the new object
      contains the old one as its degenerate rank-2 corner).
  [2] The higher-rank polarization: on RH-respecting genus-2/3 spectra (all |u_i|=1), G_m is
      PSD at every order -- the primitive form is the polarization.
  [3] THE HEADLINE (adversary-corrected): the integer genus-2 Davenport-Heilbronn analogue
      P(T) = T^4 - 4T^3 + 15T^2 - 20T + 25 over q=5 (RH false). Its rank-3 joint form G_2 (from
      N_1, N_2) is INDEFINITE while EVERY 2x2 principal sub-minor of G_2 is PD -- the smallest
      genuine higher-rank Hodge-Riemann structure (indefinite, all 2x2 restrictions definite),
      invisible to the genus-1 binary form. NOTE (honesty): this does NOT mean 'higher rank is
      needed to SEE a violation' -- the 2x2 trace-bound FAMILY {|c_n|<=2g : all n} is also
      equivalent to RH and catches THIS violation at n=3; the joint form is the data-EFFICIENT
      detector, and the genuine M4 difficulty is PROVING positivity (untouched, hard already at
      g=2, n=1).
  [4] Real genus-2 curves (point-counted over F_q and F_{q^2}): Weil's theorem holds, G_m is
      PSD = the polarization, |alpha_i| = sqrt q exactly.
  [5] The higher-rank off-line flip: push one Frobenius pair off the circle. The flip RANK is
      FLAT at the kernel size 2g+1 (not climbing); what vanishes as r->1 is the MARGIN (the
      marginal-positivity wall #18/#19, now in a (2g+1)x(2g+1)). The joint form detects at this
      fixed small rank, sooner in point-count data than the 2x2 family (n ~ 1/log r).
  [6] D-H control + the honest reading: what is classical (on-circle => PSD), what is the
      content (the GEOMETRIC/combinatorial proof of PSD = Weil = M4/P6, still open over Z),
      and the sharpening it forces on 09A's P3.

This file does NOT prove M4. It BUILDS and IDENTIFIES the higher-rank object the caveat named
(the primitive form on the Frobenius powers = the trig moment matrix, RH <=> all G_m PSD), and
sharpens P3: the AHK-lattice degree map must carry the curve's zeta numerator P(T) (= t_1..t_g,
the first g point counts), not just t_1, and the higher-rank Hodge index is the joint
moment-positivity of that 2g-dim form. The Frobenius powers saturate at rank 2g (Cayley-
Hamilton), so 'higher rank' means up to 2g. P6/M4 (proving positivity) is where M4 lives and is
left open. (ADVERSARY-corrected: scratchpad/higher_rank_rosati/01_adversary.md.)

Run:
  python -m experiments.arithmetic_geometric.e2xx_higher_rank_rosati
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path

import numpy as np


# ===========================================================================
# The higher-rank primitive form, three equivalent presentations.
# ===========================================================================
def moment_sequence(us, nmax: int) -> np.ndarray:
    """c_n = sum_i (u_i^n + u_i^{-n}) for g Frobenius pairs (u_i, 1/u_i), n = 0..nmax.
    c_n is real for any q-symmetric spectrum (the multiset {u_i} is closed under u -> 1/u).
    Under RH every |u_i| = 1 and c_n = sum_i 2 cos(n phi_i)."""
    out = []
    for n in range(nmax + 1):
        s = 0j
        for u in us:
            s += u ** n + u ** (-n)
        out.append(s.real)
    return np.array(out, dtype=float)


def rosati_gram(us, q: float, m: int) -> np.ndarray:
    """The UN-normalized primitive intersection Gram on the Frobenius powers {pi^0..pi^m}:
    G^prim = -M, M_{jk} = q^k t_{j-k}, t_n = sum_i(alpha_i^n + (q/alpha_i)^n), alpha_i = sqrt(q) u_i.
    For m=1 this is e2uu's [[-2g, -t], [-t, -2gq]] exactly (verified in Part 1)."""
    sq = math.sqrt(q)
    alphas = [sq * u for u in us]

    def t(n: int) -> float:
        s = 0j
        for a in alphas:
            s += a ** n + (q / a) ** n
        return s.real

    M = np.zeros((m + 1, m + 1), dtype=float)
    for j in range(m + 1):
        for k in range(m + 1):
            M[j, k] = (q ** k) * t(j - k)
    return -M                                   # the primitive INTERSECTION form (neg-def under RH)


def toeplitz_moment(c, m: int) -> np.ndarray:
    """The normalized higher-rank Hodge form: G_m = [c_{|j-k|}], the trigonometric moment
    matrix. Congruent to the un-normalized Rosati Gram M; PSD iff M PD iff RH (Caratheodory-
    Toeplitz). This is the clean classical face of the primitive intersection form."""
    M = np.zeros((m + 1, m + 1), dtype=float)
    for j in range(m + 1):
        for k in range(m + 1):
            M[j, k] = c[abs(j - k)]
    return M


# Tolerance note: an RH moment matrix is positive SEMI-definite -- the symmetrized Frobenius
# spectrum is a measure on 2g points, so [c_{j-k}] has rank 2g and becomes SINGULAR (a genuine
# zero eigenvalue) at size 2g+1. "PSD" must allow that boundary zero; a "flip" is a GENUINELY
# negative eigenvalue (below -tol*scale). 1e-7 relative cleanly separates the float64 noise at
# the RH boundary (~1e-15) from real off-line flips (>=1e-6 here).
_TOL = 1e-7


def signature(M: np.ndarray, tol: float = _TOL) -> tuple:
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    scale = max(1.0, float(np.max(np.abs(ev))))
    return (int(np.sum(ev > tol * scale)), int(np.sum(ev < -tol * scale)))


def is_psd(M: np.ndarray, tol: float = _TOL) -> bool:
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    scale = max(1.0, float(np.max(np.abs(ev))))
    return bool(np.all(ev > -tol * scale))


# ===========================================================================
# Genus-2 curves: real point counts over F_q and F_{q^2} -> the Frobenius spectrum.
# ===========================================================================
def _nonresidue(p: int) -> int:
    sq = {(x * x) % p for x in range(p)}
    for n in range(2, p):
        if n % p not in sq:
            return n
    raise ValueError(f"no non-residue found mod {p}")


class _F2:
    """F_{p^2} = F_p[t]/(t^2 - ns), elements (a, b) = a + b t. Enough for point counting."""

    def __init__(self, p: int):
        self.p = p
        self.ns = _nonresidue(p)

    def mul(self, A, B):
        a, b = A
        c, d = B
        p = self.p
        return ((a * c + b * d * self.ns) % p, (a * d + b * c) % p)

    def squares(self) -> set:
        return {self.mul((a, b), (a, b)) for a in range(self.p) for b in range(self.p)}


def _squarefree_mod(coeffs, p: int) -> bool:
    """gcd(f, f') = const in F_p[x]  <=>  f squarefree mod p  <=>  the curve is smooth there."""
    f = [c % p for c in coeffs]
    fp = [((i) * f[i]) % p for i in range(1, len(f))]

    def deg(a):
        a = [x % p for x in a]
        while a and a[-1] % p == 0:
            a = a[:-1]
        return len(a) - 1, a

    def polymod(a, b):
        da, a = deg(a)
        db, b = deg(b)
        if db < 0:
            return a
        inv = pow(b[-1], p - 2, p)
        a = a[:]
        while True:
            da, a = deg(a)
            if da < db:
                return a
            coef = (a[-1] * inv) % p
            shift = da - db
            for i in range(db + 1):
                a[shift + i] = (a[shift + i] - coef * b[i]) % p

    a, b = f, fp
    while True:
        db, b = deg(b)
        if db < 0:
            da, a = deg(a)
            return da <= 0
        a, b = b, polymod(a, b)


def count_genus2(p: int, coeffs) -> tuple:
    """Brute-force #C(F_p), #C(F_{p^2}) for the genus-2 hyperelliptic curve y^2 = f(x),
    f given by `coeffs` (low->high), deg f = 5, monic, squarefree (=> 1 point at infinity)."""
    assert len(coeffs) == 6 and coeffs[-1] == 1, "need a monic degree-5 f (genus 2)"
    assert _squarefree_mod(coeffs, p), "f must be squarefree mod p (smooth curve)"

    def fp(x):
        v = 0
        for c in reversed(coeffs):
            v = (v * x + c) % p
        return v

    sq_p = {(x * x) % p for x in range(p)}
    N1 = 1                                         # the single point at infinity (deg-5 model)
    for x in range(p):
        v = fp(x) % p
        N1 += 1 if v == 0 else (2 if v in sq_p else 0)

    F = _F2(p)
    Sq2 = F.squares()

    def fpp(X):
        v = (0, 0)
        for c in reversed(coeffs):
            v = F.mul(v, X)
            v = ((v[0] + c) % p, v[1] % p)
        return v

    N2 = 1
    for a in range(p):
        for b in range(p):
            v = fpp((a, b))
            if v == (0, 0):
                N2 += 1
            elif v in Sq2:
                N2 += 2
    return N1, N2


def eigs_from_counts(q: int, N1: int, N2: int):
    """Frobenius eigenvalues of a genus-2 curve from its first two point counts, via the
    functional equation P(T) = T^4 - e1 T^3 + e2 T^2 - q e1 T + q^2 (e3 = q e1, e4 = q^2)."""
    p1 = q + 1 - N1                                # sum alpha_i
    p2 = q * q + 1 - N2                            # sum alpha_i^2
    e1 = p1
    e2 = (p1 * p1 - p2) / 2
    return np.roots([1.0, -e1, e2, -q * e1, q * q])


def weil_poly_spectrum(q: int, e1: int, e2: int):
    """A genus-2 FUNCTIONAL-EQUATION-respecting candidate zeta numerator
    P(T) = T^4 - e1 T^3 + e2 T^2 - q e1 T + q^2 (integer e1, e2). Its roots are q-symmetric
    (closed under alpha -> q/alpha) and conjugate-closed (real coefficients), but are NOT
    forced onto |alpha| = sqrt q unless the trace polynomial s^2 - e1 s + (e2 - 2q) has both
    roots real in [-2 sqrt q, 2 sqrt q]. When it does not, P is a genus-2 Davenport-Heilbronn
    analogue: an integer 'fake zeta' with the right functional equation but RH false, hence
    NOT the zeta of any curve. Returns (roots, moments c_n for n=0..8, RH-bool).
    c_n = (sum over the 2g roots alpha^n)/q^{n/2} = sum_i(u_i^n + u_i^{-n}), u_i = alpha_i/sqrt q.
    c_1, c_2 are the data from (N_1, N_2); higher c_n would need (N_3, N_4, ...)."""
    roots = np.roots([1.0, float(-e1), float(e2), float(-q * e1), float(q * q)])
    c = [float(np.sum(roots ** n).real) / (q ** (n / 2.0)) for n in range(9)]
    rh = bool(np.allclose(sorted(abs(r) for r in roots), [math.sqrt(q)] * 4, atol=1e-6))
    return roots, c, rh


def us_from_eigs(q: int, roots) -> list:
    """The g normalized representatives u_i = alpha_i / sqrt(q), one per conjugate pair."""
    sq = math.sqrt(q)
    us, used = [], [False] * len(roots)
    for i, a in enumerate(roots):
        if used[i]:
            continue
        # pair a with its functional-equation partner q/a (= conj(a) under RH)
        j = min((k for k in range(len(roots)) if not used[k] and k != i),
                key=lambda k: abs(roots[k] - q / a))
        used[i] = used[j] = True
        us.append(a / sq)
    return us


# ===========================================================================
# Parts.
# ===========================================================================
def part1_genus1_reduction() -> dict:
    """m=1 reproduces e2uu/e2g exactly: the new higher-rank object contains the old 2x2
    trace-bound form as its degenerate rank-2 corner."""
    q, t = 25.0, 6.0                              # genus 1, |t| < 2 sqrt q = 10 (RH ok)
    disc = t * t - 4 * q
    a1 = (t + cmath.sqrt(disc)) / 2
    u1 = a1 / math.sqrt(q)
    G = rosati_gram([u1], q, 1)
    e2uu = np.array([[-2.0, -t], [-t, -2.0 * q]])
    return {"q": q, "t": t, "G_prim": G, "e2uu_form": e2uu,
            "matches_e2uu": bool(np.allclose(G, e2uu)),
            "neg_def": is_psd(-G)}


def part2_higher_rank_polarization() -> list:
    """RH-respecting genus-2 and genus-3 spectra (all |u_i| = 1): the higher-rank moment
    form G_m is PSD at EVERY order -- it is the polarization."""
    configs = [
        ("genus 2 (phi=0.5, 2.1)", [cmath.exp(0.5j), cmath.exp(2.1j)]),
        ("genus 3 (phi=0.3,1.2,2.7)", [cmath.exp(0.3j), cmath.exp(1.2j), cmath.exp(2.7j)]),
    ]
    rows = []
    for label, us in configs:
        c = moment_sequence(us, 2 * len(us) + 2)
        psd_all = all(is_psd(toeplitz_moment(c, m)) for m in range(1, len(c)))
        rows.append({"label": label, "g": len(us), "c": c,
                     "psd_all_orders": psd_all})
    return rows


def part3_trace_blind_witness() -> dict:
    """THE HEADLINE (ADVERSARY-corrected, scratchpad/higher_rank_rosati/01_adversary.md): the
    genus-2 Davenport-Heilbronn analogue  P(T) = T^4 - 4 T^3 + 15 T^2 - 20 T + 25  over q = 5,
    an integer 'fake zeta' with the exact curve functional equation but RH FALSE (trace poly
    s^2 - 4s + 5 has complex roots 2 +- i, eigenvalues off the circle, not the zeta of any
    curve). From its first two point-count moments (c_1, c_2 = data from N_1, N_2), the JOINT
    rank-3 moment form G_2 (built from exactly {c_0, c_1, c_2}) has signature (2,1) --
    INDEFINITE -- while EVERY 2x2 PRINCIPAL sub-minor of G_2 is positive-definite (both the n=1
    bound |c_1|<=2g and the n=2 bound |c_2|<=2g hold). So the indefiniteness is caught ONLY by
    the full 3x3 determinant, not by any 2x2 restriction: G_2 is the smallest matrix exhibiting
    the genuine higher-rank (joint) Hodge-Riemann structure -- indefinite with all 2x2 minors
    PD. That structure is invisible to the genus-1 binary form, and its POSITIVITY over Z is M4.

    THREE honest caveats the adversary forced (do not over-read this):
    * It does NOT show 'higher rank is needed to SEE a violation.' The 2x2 trace-bound FAMILY
      {|c_n| <= 2g : all n} is equivalent to RH at every genus (an off-circle pair makes c_n ~
      r^n unbounded), so this same violation IS seen by a 2x2 sub-minor -- at n = 3 (|c_3|>2g),
      i.e. needing the further point count N_3. The joint form is the DATA-EFFICIENT detector
      (catches at rank 3 from (N_1,N_2) what the 2x2 family needs N_3 to see), not the only one.
    * The genuine higher-rank DIFFICULTY is PROVING positivity (= the Hodge index theorem = M4),
      which is UNTOUCHED and bites already at (g=2, n=1): even the trace bound |t| < 2g sqrt q is
      no longer Hasse's elementary binary norm form once g >= 2.
    * Contrast: the genuine Weil polynomial T^4 - 5T^3 + 20T^2 - 35T + 49 over q=7 (RH true) is
      PSD. The object is correct; the discriminator is the JOINT positivity, left open."""
    q, e1, e2 = 5, 4, 15
    g = 2
    roots, c, rh = weil_poly_spectrum(q, e1, e2)
    per_order = []
    for m in range(1, 4):
        G = toeplitz_moment(c, m)
        per_order.append({"size": m + 1, "signature": signature(G), "psd": is_psd(G)})
    # every 2x2 PRINCIPAL sub-minor of G_2 is PD (so no 2x2 restriction catches the violation):
    G2 = toeplitz_moment(c, 2)
    two_by_two_all_pd = all(is_psd(G2[np.ix_([i, j], [i, j])]) for (i, j) in ((0, 1), (0, 2), (1, 2)))
    caught_at = next((r_["size"] for r_ in per_order if not r_["psd"]), None)
    # the 2x2 FAMILY (across all n) first catches it at this n (needs point count N_n):
    family_first_n = next((n for n in range(1, len(c)) if abs(c[n]) > 2 * g), None)
    # the RH control: a genuine Weil polynomial passes the joint form
    rc, cc, rh_ctrl = weil_poly_spectrum(7, 5, 20)
    ctrl_psd = all(is_psd(toeplitz_moment(cc, m)) for m in (1, 2))
    return {"poly": f"T^4-{e1}T^3+{e2}T^2-{q*e1}T+{q*q}", "q": q, "g": g,
            "roots_abs": sorted(round(float(abs(r)), 4) for r in roots),
            "sqrt_q": round(math.sqrt(q), 4), "c": c, "rh_holds": rh,
            "integer_fe_respecting": True, "per_order": per_order,
            "G2_indefinite": not is_psd(G2), "all_2x2_principal_minors_pd": two_by_two_all_pd,
            "first_caught_at_size": caught_at, "family_2x2_first_n": family_first_n,
            "control_weil_poly": "T^4-5T^3+20T^2-35T+49 (q=7)", "control_rh": rh_ctrl,
            "control_joint_psd": ctrl_psd,
            "joint_rank3_beats_its_2x2_minors": (not is_psd(G2)) and two_by_two_all_pd
            and (not rh)}


def part4_real_genus2_curves() -> list:
    """Real genus-2 hyperelliptic curves y^2 = f(x), point-counted over F_p and F_{p^2}.
    Weil's theorem: the higher-rank moment form is PSD = the polarization, |alpha_i| = sqrt p.
    Also CROSS-CHECKS the two presentations are one object: the un-normalized primitive
    intersection Gram (rosati_gram) is NEGATIVE-definite (the polarization) and CONGRUENT to
    the normalized Toeplitz moment form (same signature), confirming computationally what the
    adversary verified via Weil's intersection formula."""
    curves = [
        (5, [2, 0, 1, 0, 0, 1]),                   # y^2 = x^5 + x^2 + 2 over F_5
        (7, [1, 1, 0, 1, 0, 1]),                   # y^2 = x^5 + x^3 + x + 1 over F_7
        (7, [3, 1, 0, 0, 0, 1]),                   # y^2 = x^5 + x + 3      over F_7
        (11, [4, 0, 2, 0, 1, 1]),                  # y^2 = x^5 + x^4 + 2x^2 + 4 over F_11
    ]
    rows = []
    for p, coeffs in curves:
        N1, N2 = count_genus2(p, coeffs)
        roots = eigs_from_counts(p, N1, N2)
        us = us_from_eigs(p, roots)
        c = moment_sequence(us, 6)
        psd_all = all(is_psd(toeplitz_moment(c, m)) for m in range(1, len(c)))
        on_circle = bool(np.allclose(sorted(abs(r) for r in roots),
                                     [math.sqrt(p)] * 4, atol=1e-6))
        # congruence cross-check at rank 4 (= 2g, the full Frobenius-power span): the
        # intersection Gram -M is neg-def and has the same signature as the moment form.
        Gint = rosati_gram(us, p, 3)               # un-normalized primitive INTERSECTION form
        Gmom = toeplitz_moment(c, 3)               # normalized moment form
        congruent = signature(Gint) == (signature(Gmom)[1], signature(Gmom)[0])  # sign-flipped
        rows.append({"p": p, "coeffs": coeffs, "N1": N1, "N2": N2,
                     "intersection_neg_def": is_psd(-Gint), "congruent_to_moment": congruent,
                     "abs_alpha": sorted(round(float(abs(r)), 4) for r in roots),
                     "sqrt_p": round(math.sqrt(p), 4),
                     "weil_on_circle": on_circle, "psd_all_orders": psd_all,
                     "trace_bound": abs(c[1]) < 4})
    return rows


def part5_higher_rank_offline_flip(q: float = 25.0) -> dict:
    """The higher-rank off-line flip (#96 generalized), ADVERSARY-corrected. Start from a
    genus-3 RH spectrum; push ONE pair off the circle (u = e^{i phi} -> r e^{i phi}, r > 1).

    Mechanism (the honest reading): an RH moment matrix is PSD and becomes SINGULAR at size
    2g+1 (= 7 here, g=3) -- the spectrum is a measure on 2g points, so the form sits at the
    PSD boundary with a kernel, never going negative. An off-line pair pushes that borderline
    zero eigenvalue NEGATIVE. What the corrected experiment reports:

    * The flip RANK is essentially FLAT at the kernel size 2g+1 for the whole near-circle range
      (NOT a 'rank climbs as r->1' law -- the earlier framing was withdrawn). It drops below
      2g+1 only when the pair is far off (r=2.5 -> size 5).
    * What vanishes as r->1 is the MARGIN: the flipping min-eigenvalue -> 0 (r=1.001 gives
      ~ -1e-5 at size 7). That is the ordinary marginal-positivity wall (#18/#19/#3J), now
      living in a (2g+1) x (2g+1) instead of a 2x2 -- a MAGNITUDE stealth, not a rank stealth.
    * The point in favour of the joint form: it detects a barely-off pair at the FIXED small
      size 2g+1, exponentially sooner (in point-count data) than the 2x2 trace-bound family,
      which needs c_n past 2g at n ~ 1/log(r) (hundreds of point counts for r near 1)."""
    phis = [0.4, 1.3, 2.6]
    g = len(phis)
    rows = []
    for r in [1.0, 1.001, 1.01, 1.05, 1.2, 1.6, 2.5]:
        us = [r * cmath.exp(1j * phis[0])] + [cmath.exp(1j * ph) for ph in phis[1:]]
        c = moment_sequence(us, 16)                     # small: enough for the Toeplitz flip
        flip_size, flip_margin = None, None
        for m in range(1, len(c)):
            ev = np.linalg.eigvalsh(toeplitz_moment(c, m))
            if not is_psd(toeplitz_moment(c, m)):
                flip_size, flip_margin = m + 1, float(ev.min())
                break
        # the 2x2 trace-bound family first catches it when |c_n| > 2g (off-circle => c_n ~ r^n);
        # a near-circle pair needs LARGE n, a far pair small n -- search lazily, break early:
        family_first_n = None
        for n in range(1, 5000):
            cn = sum((u ** n + u ** (-n)) for u in us).real
            if abs(cn) > 2 * g:
                family_first_n = n
                break
            if abs(cn) > 1e12:                          # far-off pair: stop before overflow
                family_first_n = n
                break
        rows.append({"r": r, "rh": abs(r - 1.0) < 1e-9,
                     "flip_first_at_size": flip_size, "flip_margin": flip_margin,
                     "family_2x2_first_n": family_first_n})
    # the corrected facts: (a) RH never flips; (b) off-line flip rank is ~flat at 2g+1, NOT
    # climbing; (c) the margin vanishes as r->1; (d) the joint form beats the 2x2 family in data.
    offline = [r_ for r_ in rows if not r_["rh"]]
    near = [r_ for r_ in offline if r_["r"] <= 1.2]
    flip_rank_flat_near_circle = len({r_["flip_first_at_size"] for r_ in near}) == 1
    margin_vanishes = (near[0]["flip_margin"] is not None
                       and abs(near[0]["flip_margin"]) < 1e-4)        # r=1.001 margin ~ -1e-5
    joint_beats_family = all((r_["flip_first_at_size"] or 99) < (r_["family_2x2_first_n"] or 0) + 1
                             for r_ in near)
    return {"phis": phis, "g": g, "rows": rows,
            "kernel_rank_2g_plus_1": 2 * g + 1,
            "flip_rank_flat_near_circle": flip_rank_flat_near_circle,
            "margin_vanishes_near_circle": margin_vanishes,
            "joint_beats_2x2_family_in_data": joint_beats_family}


def part6_dh_control_and_reading() -> dict:
    """K2 / D-H and the honest reading."""
    return {
        "dh_builds_object": False,
        "dh_note": ("Davenport-Heilbronn has no Euler product => no Frobenius pi => no q-Weil "
                    "spectrum {alpha_i, q/alpha_i} => no Frobenius-power correspondences and no "
                    "NS(C x C): D-H instantiates NONE of the moment matrix (09A's K2, structural)."),
        "classical_direction": ("on-circle (RH) => PSD at all orders is the EASY half "
                                "(Caratheodory-Toeplitz: a positive measure on the circle has a "
                                "PSD moment matrix). It is a restatement, not a proof."),
        "the_content_M4": ("the proof that the moment matrix IS PSD without assuming the "
                           "spectrum is on the circle = the Hodge index theorem on C x C = Weil "
                           "= M4/P6. Over F_q it is a theorem; over Z (the AHK lattice) it is open."),
        "p3_sharpened": ("the genus-1 P3 'the degree map carries t' (= t_1) is too weak: the "
                         "higher-rank Hodge index needs the curve's zeta numerator P(T), i.e. "
                         "t_1..t_g (the first g point counts #C(F_{q^n}), n=1..g; the rest are "
                         "determined by the functional equation), and P6 becomes the joint "
                         "moment-positivity of that 2g-dim form -- NOT one determinant. (For g=1 "
                         "it reduces to #105.)"),
        "rank_caveat": ("the Frobenius powers saturate at rank 2g (Cayley-Hamilton: pi satisfies "
                        "its degree-2g char poly), so 'higher rank' here means up to 2g; the object "
                        "does NOT reach the full rank rho-2 of the primitive part of NS(C x C)."),
    }


# ===========================================================================
# Demo.
# ===========================================================================
def demo() -> int:
    print("=" * 88)
    print("e2xx: the HIGHER-RANK AHK/Rosati object -- where genus 1 stops being elementary")
    print("=" * 88)

    print("\n[1] Genus-1 reduction (m=1 reproduces e2uu/e2g EXACTLY):")
    p1 = part1_genus1_reduction()
    print(f"    q={p1['q']:.0f} t={p1['t']:.0f}: G_prim =\n{np.array2string(p1['G_prim'], prefix='        ')}")
    print(f"    e2uu [[-2g,-t],[-t,-2gq]] match = {p1['matches_e2uu']}; neg-def = {p1['neg_def']}")
    print("    => the higher-rank object CONTAINS the old 2x2 trace-bound form as its rank-2 corner.")

    print("\n[2] The higher-rank polarization (RH spectra: PSD at EVERY order):")
    for r in part2_higher_rank_polarization():
        print(f"    {r['label']:28} (g={r['g']}): c={np.round(r['c'][:5], 3)}...  "
              f"PSD all orders = {r['psd_all_orders']}")

    print("\n[3] *** HEADLINE (adversary-corrected): an INTEGER genus-2 Davenport-Heilbronn")
    print("    analogue whose rank-3 joint form is indefinite while every 2x2 minor is PD ***")
    p3 = part3_trace_blind_witness()
    print(f"    fake zeta P = {p3['poly']}  (q={p3['q']}): integer coeffs, curve functional eqn,")
    print(f"    roots |alpha| = {p3['roots_abs']} (NOT all sqrt q = {p3['sqrt_q']}) => RH={p3['rh_holds']}")
    print(f"    moments from (N_1, N_2): c = [{', '.join(f'{x:.4f}' for x in p3['c'][:3])}, ...]  "
          f"(c_0 = 2g = {2*p3['g']})")
    for r in p3["per_order"]:
        print(f"        joint moment form size {r['size']}: signature {r['signature']}  PSD={r['psd']}")
    print(f"    => G_2 (rank 3) is INDEFINITE ({p3['G2_indefinite']}) yet ALL its 2x2 principal")
    print(f"       sub-minors are PD ({p3['all_2x2_principal_minors_pd']}): the smallest genuine")
    print(f"       higher-rank Hodge-Riemann structure, caught only by the 3x3 det = "
          f"{p3['joint_rank3_beats_its_2x2_minors']}")
    print(f"    HONEST CAVEATS (adversary): the 2x2 trace-bound FAMILY does catch this violation, "
          f"but only at n={p3['family_2x2_first_n']} (needs N_{p3['family_2x2_first_n']}); the joint")
    print(f"       form is the DATA-EFFICIENT detector, not the only one. PROVING positivity (=M4)")
    print(f"       is the real difficulty, untouched, and bites already at g=2,n=1.")
    print(f"    CONTROL (genuine Weil poly {p3['control_weil_poly']}): RH={p3['control_rh']}, "
          f"joint form PSD={p3['control_joint_psd']}")

    print("\n[4] Real genus-2 curves (point-counted over F_p and F_{p^2}); Weil + the polarization:")
    for r in part4_real_genus2_curves():
        print(f"    F_{r['p']:<2} f={r['coeffs']}: N1={r['N1']:>3} N2={r['N2']:>4}  "
              f"|alpha|={r['abs_alpha']} (sqrt p={r['sqrt_p']})  on-circle={r['weil_on_circle']}  "
              f"PSD={r['psd_all_orders']}  intersection-form neg-def={r['intersection_neg_def']} "
              f"& congruent-to-moment={r['congruent_to_moment']}")

    print("\n[5] The higher-rank off-line flip (push one pair off; report flip RANK + MARGIN):")
    p5 = part5_higher_rank_offline_flip()
    for r in p5["rows"]:
        tag = "RH" if r["rh"] else "off-line"
        margin = "n/a" if r["flip_margin"] is None else f"{r['flip_margin']:+.2e}"
        print(f"    r={r['r']:.3f} ({tag:8}): flip first at size = {str(r['flip_first_at_size']):>4} "
              f"(margin {margin:>9});  2x2 family first catches at n = {r['family_2x2_first_n']}")
    print(f"    => CORRECTED (adversary): the flip RANK is FLAT at the kernel size 2g+1 = "
          f"{p5['kernel_rank_2g_plus_1']} near the circle ({p5['flip_rank_flat_near_circle']}), NOT")
    print(f"       climbing. What vanishes as r->1 is the MARGIN ({p5['margin_vanishes_near_circle']}): "
          f"the ordinary #18/#19 marginal-positivity wall, now in a (2g+1)x(2g+1).")
    print(f"       The joint form still beats the 2x2 family in DATA (detects at fixed small rank, "
          f"sooner than n~1/log r): {p5['joint_beats_2x2_family_in_data']}")

    print("\n[6] D-H control + the honest reading:")
    p6 = part6_dh_control_and_reading()
    print(f"    K2/D-H: {p6['dh_note']}")
    print(f"    CLASSICAL (easy half): {p6['classical_direction']}")
    print(f"    THE CONTENT (= M4): {p6['the_content_M4']}")
    print(f"    P3 SHARPENED: {p6['p3_sharpened']}")
    print(f"    RANK CAVEAT: {p6['rank_caveat']}")

    print("\n" + "=" * 88)
    print("VERDICT (a CONSTRUCTION, honestly scoped -- adversary-corrected):")
    print("  - BUILT and IDENTIFIED the higher-rank object the #122 caveat named: NS(C x C)'s")
    print("    primitive form on Frobenius POWERS = the trigonometric moment matrix of the")
    print("    symmetrized Frobenius spectrum, and RH-for-the-curve <=> all G_m PSD (Caratheodory-")
    print("    Toeplitz). Genus 1 is its degenerate rank-2 corner (e2uu); object verified via")
    print("    Weil's intersection formula, not just the genus-1 match.")
    print("  - The genuine higher-rank Hodge-Riemann structure is real (G_2 indefinite with all")
    print("    2x2 minors PD, Part 3), but SEEING an off-line violation does NOT need higher rank")
    print("    (the 2x2 trace-bound FAMILY = RH too); the difficulty is PROVING positivity = M4.")
    print("  - The higher-rank P6 is the joint moment-POSITIVITY of a 2g-dim form (NOT a single")
    print("    determinant), non-elementary already at g=2; THAT is where M4's difficulty lives,")
    print("    and it is UNTOUCHED.")
    print("  - SHARPENED 09A's P3: the degree map must carry the curve's zeta P(T) = t_1..t_g,")
    print("    not just t_1. The Frobenius powers cap at rank 2g (Cayley-Hamilton).")
    print("=" * 88)

    # ---- structural assertions ----
    assert p1["matches_e2uu"] and p1["neg_def"], "Part 1: m=1 must reproduce e2uu and be neg-def"
    assert all(r["psd_all_orders"] for r in part2_higher_rank_polarization()), \
        "Part 2: RH spectra must give PSD at all orders"
    assert p3["joint_rank3_beats_its_2x2_minors"], \
        "Part 3: G_2 must be indefinite while all its 2x2 principal minors are PD"
    assert p3["per_order"][0]["psd"] and not p3["per_order"][1]["psd"], \
        "Part 3: the 2x2 must be PSD and the 3x3 indefinite"
    assert p3["family_2x2_first_n"] is not None and p3["family_2x2_first_n"] > 2, \
        "Part 3: the 2x2 family must (honestly) also catch it, at some n>2"
    assert p3["control_joint_psd"] and p3["control_rh"], \
        "Part 3: the genuine Weil-polynomial control must be RH and give a PSD joint form"
    p4 = part4_real_genus2_curves()
    assert all(r["weil_on_circle"] and r["psd_all_orders"] for r in p4), \
        "Part 4: real curves must satisfy Weil (on circle) and give the PSD polarization"
    assert all(r["intersection_neg_def"] and r["congruent_to_moment"] for r in p4), \
        "Part 4: the intersection form must be neg-def and congruent (sign-flipped) to the moment form"
    p5a = part5_higher_rank_offline_flip()
    assert p5a["rows"][0]["flip_first_at_size"] is None, "Part 5: the RH (r=1) spectrum must not flip"
    assert any(r["flip_first_at_size"] is not None for r in p5a["rows"][1:]), \
        "Part 5: off-line spectra must flip the form at some finite rank"
    assert p5a["flip_rank_flat_near_circle"] and p5a["margin_vanishes_near_circle"], \
        "Part 5: flip rank must be flat near the circle and the margin must vanish (corrected)"
    print("\n(all structural assertions hold)")

    out = Path(__file__).resolve().parent / "e2xx_higher_rank_rosati.npz"
    np.savez_compressed(
        out,
        genus1_Gprim=p1["G_prim"], genus1_matches_e2uu=p1["matches_e2uu"],
        headline_c=p3["c"], headline_first_caught_size=p3["first_caught_at_size"] or -1,
        real_curve_p=np.array([r["p"] for r in p4]),
        real_curve_N1=np.array([r["N1"] for r in p4]),
        real_curve_N2=np.array([r["N2"] for r in p4]),
        flip_rates=np.array([r["r"] for r in p5a["rows"]]),
        flip_sizes=np.array([(r["flip_first_at_size"] or -1) for r in p5a["rows"]]),
        flip_margins=np.array([(r["flip_margin"] if r["flip_margin"] is not None else 0.0)
                               for r in p5a["rows"]]),
    )
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())

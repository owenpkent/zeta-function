"""R2 (super-AHK machinability): is there a recursion for an AHK induction to run on?

THE QUESTION (R2, from e2za's adversary-corrected residual). AHK 2018 proves the Kähler
package for a matroid Chow ring via a DELETION-CONTRACTION / semismall induction over the
matroid's minors. The arithmetic target needs a t-carrying (1,1) form (the Frobenius trace,
living on the odd H^1 (x) H^1). e2yy/#124 showed the FORM is t-blind (purely Tate). R2 asks
the deeper question: even granting an odd H^1, does AHK's INDUCTION ENGINE run on it?

THIS PROBE elevates e2yy from the form to the ENGINE. The AHK induction's only input is the
matroid M and its minors M\e (deletion), M/e (contraction), glued by the characteristic-
polynomial deletion-contraction relation chi_M = chi_{M\e} - chi_{M/e} (the even recursion,
whose log-concavity AHK proves). The claim tested here:

    The ENTIRE AHK induction input (M and all its minors) is t-BLIND: two arithmetic
    decorations of the SAME matroid with different Frobenius trace t have IDENTICAL even
    data (same chi, same minors, same deletion-contraction tree), while the t-carrying
    moment form they must certify DIFFERS (one RH-true/PSD, one RH-false/indefinite).

If true, no matroid-deletion-contraction induction -- however 'super' -- can carry t,
because the thing it recurses on does not move with t while the thing RH needs does. So R2
reduces to R1 (sourcing) UNLESS the recursion is run on a t-SEEING combinatorial structure
(a symplectic / delta-matroid / Lagrangian-matroid recursion, the open lead -> SURVEYOR).

This is more than e2yy: e2yy killed the form; this scopes the ENGINE, and names exactly what
a viable super-AHK must have (a t-seeing recursion, not a matroid one). It does NOT prove no
such structure exists (that is R1 + the delta-matroid literature). P6/M4 untouched.

Run: python -m experiments.arithmetic_geometric.e2zb_super_ahk_recursion
"""

from __future__ import annotations

import cmath
import math
from math import comb

import numpy as np


# ===========================================================================
# The EVEN recursion: characteristic polynomials of uniform matroids + minors.
# ===========================================================================
def chi_uniform(r: int, n: int):
    """Characteristic polynomial coefficients of U_{r,n} (rank r, n elements), high->low
    degree. Flats are all subsets of size < r (Boolean intervals, mu=(-1)^k) plus E.
    chi(lambda) = sum_{k<r} C(n,k)(-1)^k lambda^{r-k} + mu(0,E),
    mu(0,E) = -sum_{k<r} C(n,k)(-1)^k."""
    coeffs = [comb(n, k) * (-1) ** k for k in range(r)]      # coeff of lambda^{r-k}
    top = -sum(coeffs)                                        # mu(0, E), the constant term
    return coeffs + [top]


def poly_sub(a, b):
    """Subtract two coeff lists (high->low), aligning by degree."""
    la, lb = len(a), len(b)
    L = max(la, lb)
    a = [0] * (L - la) + list(a)
    b = [0] * (L - lb) + list(b)
    return [x - y for x, y in zip(a, b)]


# ===========================================================================
# The arithmetic decoration: an odd H^1 Frobenius on top of the even matroid.
# ===========================================================================
def elliptic_alphas(q, t):
    """Eigenvalues of X^2 - tX + q (the H^1 Frobenius of a genus-1 decoration)."""
    r = cmath.sqrt(complex(t * t - 4 * q))
    return [(t + r) / 2, (t - r) / 2]


def moment_matrix(alphas, q, m):
    """The t-carrying primitive form (e2xx): Toeplitz [c_{|j-k|}], c_n = sum (u^n+u^-n),
    u = alpha/sqrt q. PSD iff |u|=1 iff RH-for-the-decoration."""
    sq = math.sqrt(q)
    us = [a / sq for a in alphas]
    c = [sum((u ** n + u ** (-n)) for u in us).real for n in range(m + 1)]
    return np.array([[c[abs(j - k)] for k in range(m + 1)] for j in range(m + 1)], float)


def min_eig(M):
    return float(np.linalg.eigvalsh((M + M.T) / 2).min())


def banner(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main():
    print("R2 PROBE: is the AHK induction ENGINE (deletion-contraction) able to carry t?")

    # -----------------------------------------------------------------------
    banner("1. The EVEN recursion exists: chi_M = chi_{M\\e} - chi_{M/e} (AHK's induction)")
    print("  For a uniform matroid, M\\e = U_{r,n-1} (deletion), M/e = U_{r-1,n-1} (contraction).")
    print(f"  {'matroid':>10} {'chi (coeffs)':>22} {'|coeffs| log-concave?':>22}")
    for (r, n) in [(2, 3), (3, 4), (3, 5)]:
        chi = chi_uniform(r, n)
        cm = chi_uniform(r, n - 1)
        cc = chi_uniform(r - 1, n - 1)
        recursion_ok = poly_sub(cm, cc) == chi
        absc = [abs(x) for x in chi]
        logc = all(absc[i] ** 2 >= absc[i - 1] * absc[i + 1] for i in range(1, len(absc) - 1))
        print(f"  U_({r},{n})    {str(chi):>22} {str(logc):>22}  "
              f"deletion-contraction: {recursion_ok}")
    print("  => the even recursion is real and is what AHK's induction runs on. It is purely")
    print("     combinatorial: chi depends on (r,n) only -- no arithmetic, no q, no t.")

    # -----------------------------------------------------------------------
    banner("2. The ENGINE is t-BLIND: same matroid + minors, different t, different RH-truth")
    q = 25
    decs = [("decoration A (t=2)", 2, True), ("decoration B (t=100)", 100, False)]
    print(f"  Same even object for both: the matroid U_(2,3) (chi = {chi_uniform(2,3)}),")
    print(f"  same Tate scale q={q}. Only the odd H^1 Frobenius trace t differs.\n")
    print(f"  {'decoration':22} {'t':>5} {'|alpha|':>10} {'RH-true':>8} "
          f"{'moment minEig':>14} {'PSD':>6}")
    for name, t, rh in decs:
        al = elliptic_alphas(q, t)
        mod = abs(al[0])
        G = moment_matrix(al, q, m=3)
        me = min_eig(G)
        print(f"  {name:22} {t:>5} {mod:>10.4f} {str(rh):>8} {me:>14.4e} {str(me > -1e-9):>6}")
    print("\n  The even AHK induction input (the matroid, its minors, chi, the whole")
    print("  deletion-contraction tree) is IDENTICAL for A and B. The t-carrying moment form")
    print("  is PSD for A (RH-true) and INDEFINITE for B (RH-false). So the engine cannot")
    print("  distinguish A from B, but RH does.")

    # -----------------------------------------------------------------------
    banner("3. VERDICT (to be adversary-checked): R2 reduces to R1 for any MATROID recursion")
    print("""  WHAT THIS SHOWS (a structural sharpening of e2yy, at the ENGINE level):
   - AHK's induction recurses on the matroid + minors via chi_M = chi_{M\\e} - chi_{M/e}.
     That input is purely combinatorial and t-blind (Section 1: chi = chi(r,n) only).
   - Two decorations with the SAME matroid/minors but different t have different RH-truth
     (Section 2: A is PSD/RH-true, B is indefinite/RH-false). The form RH needs MOVES with
     t; the induction input does NOT.
   - Therefore NO deletion-contraction induction over a matroid -- however 'super' the
     algebra on top -- can carry t: it would propagate the IDENTICAL conclusion for A and
     B. A super-AHK that proves the t-carrying Hodge-Riemann must recurse on a structure
     that SEES t.

   WHAT THIS DOES NOT SHOW (honest scope):
   - It does NOT prove no such t-seeing combinatorial recursion exists. The candidate is a
     SYMPLECTIC / delta-matroid / Lagrangian-matroid structure whose deletion-contraction
     could move with the Frobenius. Whether any of those has a proven Kähler package AND a
     non-Tate (t-carrying) Frobenius is the open lead (SURVEYOR, in progress).
   - It is NOT progress on P6/M4. It SCOPES R2: a viable super-AHK needs a t-seeing
     recursion, reducing R2 to 'does a t-seeing combinatorial Hodge theory exist?' (= R1
     restated as a recursion question).

   NET: R2, for the only induction AHK actually has (matroid deletion-contraction), reduces
   to R1. The escape, if any, is a t-seeing (symplectic/delta-matroid/tropical) recursion.

   RESOLUTION (verified: literature survey + 2 adversarial refutation probes, 2026-06-27).
   R2 is a DEAD BRANCH, but NOT for the naive reason. CORRECTIONS the adversaries forced:
     - "combinatorial => Tate" is FALSE as a theorem (a GAP, not an obstruction). Amini-
       Piquerez prove a genuinely non-Tate combinatorial Kähler package with NO ambient
       variety (off-diagonal tropical h^{p,q}); Belkale-Brosnan + Mnev universality make
       matroid/Kirchhoff schemes arbitrarily non-Tate; Brown-Schnetz give a modular K3 in
       phi^4. Do NOT close R2 on 'combinatorial => Tate'.
     - The tropical Jacobian polarization is INTRINSIC to the metric graph (Mikhalkin-
       Zharkov), not imported -- so the survey's 'imported' reason was also wrong.
   WHAT ACTUALLY CLOSES R2 (the corrected, true statement): no known object is at once
   (i) bare-combinatorial, (ii) carrying a modulus-sqrt(q) Frobenius on a non-Tate piece,
   and (iii) AHK-machinable. The split is on the FROBENIUS clause: the non-Tate combinatorial
   objects (Amini-Piquerez, Babaee-Huh, tropical Jacobians) are FROBENIUS-FREE (over
   (R,max,+): no q, no sqrt(q), no Galois); the sqrt(q)-carriers (Belkale-Brosnan,
   Brown-Schnetz) IMPORT the polarization from an ambient variety (= #97). The tropical lead
   is DOUBLY dead: no arithmetic weight (no t) AND wrong signature (positive-definite, never
   flips off-line; the e3r/#97 polarity objection). So R2 reduces to R1 AND even granting t
   the AHK polarity is the wrong (definite) signature for P6/M4. RECOMMENDATION: record-and-
   stop on R2; pivot to the ARAKELOV face (09A Section 5/7), which natively carries both a
   genuine arithmetic weight (Faltings-Hriljac) and the indefinite Hodge-index signature.""")


if __name__ == "__main__":
    main()

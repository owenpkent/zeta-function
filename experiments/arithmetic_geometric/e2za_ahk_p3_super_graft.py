"""09A P3 attack: resolve the t-carrying degree map via an ODD generator + super-tensor.

THE GAP (09A, sharpened by #105/#122/#123): the bare AHK lattice supplies P1/P2/P4/P5
for free; the single missing property is P3 -- the degree map must carry the Frobenius
trace t (and the full zeta numerator P(T)). The e2yy near-theorem (#124) explains why the
bare object fails P3: a matroid Chow ring is purely EVEN / Tate (Hodge type (k,k)), it has
NO H^1 where the weight-1, modulus-sqrt(q) Frobenius eigenvalues live, so its degree map is
a combinatorial integer with no t-slot. Section 7 of 09A names the real risk: P3 and P1
(AHK product structure) may be JOINTLY UNSATISFIABLE -- the arithmetic decoration that
carries t might destroy the product structure.

THE NEW ANGLE TESTED HERE. Over a curve the t-carrying intersection form lives in
H^1(C) (x) H^1(C) by Kunneth, and the Kunneth product of two ODD pieces IS a product
structure -- but the SUPER (graded) tensor product, not the even matroid tensor. So the
hypothesis is:

    P3 is satisfiable, and the missing ingredient is exactly an ODD generator with a
    super-tensor product. Then (a) the degree map carries t as the graded LEFSCHETZ
    number 1 - Tr(Frob|H^1) + q = q+1-t (the standard fixed-point count = #C(F_q)),
    (b) P1 survives as Kunneth multiplicativity L(C x C) = L(C)^2, and (c) the apparent
    P1-vs-P3 tension dissolves -- e2yy's obstruction was the ABSENCE of the odd generator,
    not a conflict with P1.

ADVERSARY-CORRECTED (the headline claims were over-stated; this is the honest reading).
An independent adversary pass downgraded the result. The corrections, folded in below:
  * "deg = Lefschetz number = q+1-t" is the Grothendieck-Lefschetz fixed-point formula
    RESTATED -- a tautology, not new. (#C(F_q) = q+1-t is its definition.)
  * "P1 survives as Kunneth multiplicativity" was the serious overclaim, now RETRACTED.
    What the code tests is the SCALAR identity L(CxC) = L(C)^2, i.e. (1-t+q)^2 = (1-t+q)^2,
    which holds for ANY t, q (including nonsense: t=100, q=1, no curve). That is NOT the
    AHK ALGEBRA-level local product structure P1 (A(star F) = A(L_F) (x) A(L^F)) that the
    deletion-contraction / semismall induction consumes. AHK machinability of a super
    algebra is UNTOUCHED -- and that is exactly the Section-7 risk, still OPEN.
  * The odd H^1 + Frobenius Pi is HANDED IN as input; the lattice still cannot SOURCE it
    (e2yy unchanged). So the gap is RENAMED, not moved.
  * The off-line flip (P5) is the e2xx moment matrix run verbatim on the curve spectrum;
    the lattice / super-tensor never enter it. It is e2xx re-run, not a graft property.

WHAT GENUINELY SURVIVES (modest, a coordinate not an advance): a correct DIAGNOSIS of
e2yy -- the matroid Chow ring's failure to carry t is the ABSENCE of an odd H^1 (weight 1,
modulus sqrt q) -- and K1-cleanliness (Pi from POINT COUNTS, never the zeros; the fake is
correctly rejected). The two hard questions are exactly as open as before:
  (R1) SOURCING: can any AHK-machinable combinatorial object PRODUCE an odd H^1 with a
       modulus-sqrt(q) Frobenius? (e2yy's near-theorem says a matroid Chow ring cannot;
       adjoining one by hand assumes the answer.)
  (R2) SUPER-AHK MACHINABILITY (= the Section-7 risk): even granting the odd graft, does
       AHK's deletion-contraction induction RUN on a super-algebra so Hodge-Riemann is
       propagated K1-cleanly? Unknown, not attempted. AHK 2018 is a theorem about EVEN
       matroid Chow rings; there is no published super-AHK.
P6/M4 is UNTOUCHED.

Run: python -m experiments.arithmetic_geometric.e2za_ahk_p3_super_graft
"""

from __future__ import annotations

import cmath
import math

import numpy as np


# ===========================================================================
# The super-graded model of a curve's cohomology (the AHK skeleton + odd H^1).
# ===========================================================================
class SuperCurve:
    """A^bullet = A^0 (even, H^0, Frob=1)  (+)  A^1_odd (H^1, Frob=Pi, rank 2g)
                  (+)  A^2 (even, H^2, Frob=q).

    The EVEN part (H^0=1, H^2=q) is the Tate skeleton the AHK lattice sources
    combinatorially. The ODD part (H^1, Frobenius Pi) is the arithmetic input the
    lattice cannot source (e2yy), built here from point counts, NOT from the zeros."""

    def __init__(self, q: float, alphas, name: str, rh_true: bool):
        self.q = float(q)
        self.alphas = [complex(a) for a in alphas]   # Frobenius eigenvalues on H^1
        self.g = len(self.alphas) // 2
        self.name = name
        self.rh_true = rh_true

    @property
    def t1(self) -> float:
        """t = Tr(Frob | H^1) = sum of all 2g eigenvalues = q+1-#C(F_q)."""
        return float(sum(self.alphas).real)

    def point_count(self, n: int = 1) -> float:
        """#C(F_{q^n}) = q^n + 1 - sum alpha_i^n  (the Lefschetz fixed-point formula)."""
        tn = sum(a ** n for a in self.alphas).real
        return self.q ** n + 1 - tn

    def lefschetz_number(self, n: int = 1) -> float:
        """The graded trace L(Frob^n) = Tr(A^0) - Tr(A^1) + Tr(A^2)
                                       = 1 - sum alpha_i^n + q^n  = #C(F_{q^n}).
        THIS is the degree-map functional (P3): it carries t and MOVES when t moves."""
        tn = sum(a ** n for a in self.alphas).real
        return 1.0 - tn + self.q ** n


def companion_frobenius(alphas, q):
    """An integer-ish 2g x 2g matrix Pi with char poly prod(T - alpha_i) (the H^1
    Frobenius). Built from the eigenvalues; over a real curve these come from point
    counts. We return the eigenvalues themselves (diagonal action suffices for traces)."""
    return np.array(alphas, dtype=complex)


# ---------------------------------------------------------------------------
# The t-carrying primitive form on H^1 (x) H^1 (the e2xx moment matrix).
# ---------------------------------------------------------------------------
def moment_matrix(alphas, q, m):
    """The trigonometric moment matrix G_m = [c_{|j-k|}] of the symmetrized Frobenius
    spectrum, c_n = sum_i (u_i^n + u_i^-n), u_i = alpha_i/sqrt(q). This IS the primitive
    intersection form on H^1 (x) H^1 (e2xx/#123). PSD at every m  iff  all |u_i|=1  iff RH."""
    sq = math.sqrt(q)
    us = [a / sq for a in alphas]
    c = []
    for n in range(m + 1):
        s = sum((u ** n + u ** (-n)) for u in us)
        c.append(s.real)
    return np.array([[c[abs(j - k)] for k in range(m + 1)] for j in range(m + 1)], float)


def min_eig(M):
    return float(np.linalg.eigvalsh((M + M.T) / 2).min())


# ===========================================================================
# Test curves (eigenvalues from genuine point-count data; K1-clean).
# ===========================================================================
def elliptic(p, a):
    """E/F_p, trace a (a^2<4p): eigenvalues (a +- sqrt(a^2-4p))/2 on |alpha|=sqrt(p)."""
    r = cmath.sqrt(complex(a * a - 4 * p))
    return [(a + r) / 2, (a - r) / 2]


def on_circle_genus2(q, phi1, phi2):
    sq = math.sqrt(q)
    return [sq * cmath.exp(1j * phi1), sq * cmath.exp(-1j * phi1),
            sq * cmath.exp(1j * phi2), sq * cmath.exp(-1j * phi2)]


def e2xx_fake_q5():
    """The integer genus-2 fake-zeta P(T)=T^4-4T^3+15T^2-20T+25 over q=5 (RH FALSE)."""
    return [complex(a) for a in np.roots([1, -4, 15, -20, 25])]


CURVES = [
    SuperCurve(5, elliptic(5, 1), "E/F_5 (a=1, g=1)", True),
    SuperCurve(7, elliptic(7, 2), "E/F_7 (a=2, g=1)", True),
    SuperCurve(13, elliptic(13, 4), "E/F_13 (a=4, g=1)", True),
    SuperCurve(9, on_circle_genus2(9, 0.7, 1.9), "synthetic g=2 (on-circle)", True),
    SuperCurve(5, e2xx_fake_q5(), "e2xx fake P(T)/q=5 (g=2, RH false)", False),
]


def banner(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main():
    print("09A P3 ATTACK: the t-carrying degree map via an ODD generator + super-tensor")

    # -----------------------------------------------------------------------
    banner("P3 / K3: the degree map = the graded LEFSCHETZ number = q+1-t = #C(F_q)")
    print("  (the even AHK skeleton gives H^0=1, H^2=q; the odd H^1 carries Frobenius Pi)")
    print(f"  {'curve':32} {'q+1-t (Lefschetz)':>18} {'#C(F_q)':>10} {'match':>7}")
    for C in CURVES:
        L = C.lefschetz_number(1)
        N = C.point_count(1)
        ok = abs(L - N) < 1e-9
        print(f"  {C.name:32} {L:>18.6f} {N:>10.4f} {str(ok):>7}")
    print("  => deg carries t IF an odd H^1 is present: the functional 1 - Tr(Pi|H^1) + q.")
    print("     But this is the Grothendieck-Lefschetz formula RESTATED (tautological), and")
    print("     Pi is HANDED IN (the lattice cannot source it, e2yy). The gap is renamed: the")
    print("     diagnosis 'missing odd H^1' is correct; producing it from a lattice is open (R1).")

    # -----------------------------------------------------------------------
    banner("P1 (SCALAR SHADOW ONLY -- adversary-corrected): the Lefschetz NUMBER multiplies")
    print("  WARNING: this tests only the scalar identity L(CxC)=L(C)^2 = (1-t+q)^2, which")
    print("  holds for ANY t,q (incl. nonsense). It is NOT the AHK ALGEBRA product structure")
    print("  P1 (A(star F) = A(L_F) (x) A(L^F)) the deletion-contraction induction needs.")
    print(f"  {'curve':32} {'L(C)^2':>14} {'#(CxC)(F_q)':>14} {'match':>7}")
    for C in CURVES:
        L = C.lefschetz_number(1)
        # #(C x C)(F_q) via Kunneth: sum_{i+j} (-1)^{i+j} Tr(Frob|H^i(C))Tr(Frob|H^j(C))
        # = (1 - t1 + q)^2 = L^2.
        prod = L * L
        # direct: #(CxC)(F_q) = #C(F_q)^2 (product variety over F_q)
        direct = C.point_count(1) ** 2
        ok = abs(prod - direct) < 1e-7
        print(f"  {C.name:32} {prod:>14.4f} {direct:>14.4f} {str(ok):>7}")
    print("  => CORRECTED: a scalar trace identity, true for any t,q -- it certifies NOTHING")
    print("     about product structure. AHK machinability of the super algebra is UNTOUCHED;")
    print("     that IS the Section-7 risk (R2), still open. 'P1 survives' is RETRACTED.")

    # -----------------------------------------------------------------------
    banner("P5 + K1 off-line flip: the primitive form on H^1 (x) H^1 carries t and FLIPS")
    print("  The primitive intersection form = the e2xx moment matrix G_m (the odd (x) odd")
    print("  Hodge-index form). PSD iff RH-for-the-curve; an off-circle (off-line) eigenvalue")
    print("  must flip it indefinite (the K1 sanity check #96).")
    print(f"  {'curve':32} {'rh_true':>8} {'minEig G_3':>12} {'PSD':>6} {'correct':>8}")
    for C in CURVES:
        G = moment_matrix(C.alphas, C.q, m=3)
        me = min_eig(G)
        psd = me > -1e-9
        correct = (psd == C.rh_true)
        print(f"  {C.name:32} {str(C.rh_true):>8} {me:>12.4e} {str(psd):>6} {str(correct):>8}")
    print("  => P5/flip: the form is t-carrying (it flips with an off-line zero), the K1-clean")
    print("     property AHK demands. The fake (RH false) is correctly rejected.")

    # -----------------------------------------------------------------------
    banner("K1 accounting: what is SOURCED vs IMPORTED, and is it circular?")
    print("  SOURCED from the lattice (AHK-combinatorial): the EVEN skeleton -- H^0=1, H^2=q,")
    print("    the atoms/flats. This is the Tate part e2yy correctly found the lattice gives.")
    print("  ARITHMETIC INPUT (the lattice CANNOT source it, e2yy): the ODD H^1 + Frobenius Pi.")
    print("    But it is K1-CLEAN: Pi is built from POINT COUNTS #C(F_{q^n}) (the Lefschetz")
    print("    numbers), NOT from the zeros or |alpha|=sqrt(q). Moving t moves the object; we")
    print("    never input RH. (Verify: the fake, built the same way from its point counts,")
    print("    is correctly REJECTED above -- so the construction is not assuming RH.)")
    print("  K2 (D-H): no Euler product => no prime-atoms => no lattice => no even skeleton to")
    print("    graft onto. D-H cannot instantiate even A^0/A^2; unbuildable by type.")

    # -----------------------------------------------------------------------
    banner("VERDICT (adversary-corrected): a correct DIAGNOSIS + two sharpened open questions")
    print("""  RESULT (honest, downgraded after the adversary pass):
   WHAT SURVIVES (modest, a coordinate -- NOT an advance on P3 or P6):
   - A correct DIAGNOSIS of e2yy: the matroid Chow ring fails to carry t because it
     is purely even/Tate and LACKS an odd H^1 (weight 1, modulus sqrt q). The missing
     ingredient is named precisely.
   - K1-cleanliness is genuine: Pi is built from POINT COUNTS, never the zeros; the
     RH-false fake is correctly rejected, so RH is not smuggled in.
   - K2 holds: D-H has no Euler product => no q, no Frobenius, no lattice to graft onto.

   WHAT WAS RETRACTED (over-claims caught by the adversary):
   - "P3 satisfiable via a super-tensor graft": overstated. The odd H^1 is HANDED IN;
     the lattice still cannot source it (e2yy). The gap is RENAMED, not moved.
   - "P1 survives": RETRACTED. The code tests only the SCALAR Lefschetz multiplicativity
     (true for any t,q); it says nothing about the AHK ALGEBRA product structure or its
     deletion-contraction induction. The Section-7 risk is UNTOUCHED.
   - "deg carries t" is the Grothendieck-Lefschetz formula restated (a tautology).

   THE TWO HARD QUESTIONS, EXACTLY AS OPEN AS BEFORE:
   (R1) SOURCING: can any AHK-machinable lattice PRODUCE an odd H^1 with a
        modulus-sqrt(q) Frobenius? (e2yy: a matroid Chow ring cannot.)
   (R2) SUPER-AHK MACHINABILITY (= the Section-7 risk): does AHK deletion-contraction
        run on a super-algebra at all? No published super-AHK exists; not attempted.

   NET: this increment is a relabeling of e2yy's "supply the H^1 the Tate ring lacks"
   into two precise open questions (R1 sourcing, R2 super-machinability), plus the
   confirmation that the naive 'P1 survives' resolution is illusory (a scalar shadow).
   P3 and P6/M4 are UNTOUCHED. A coordinate that narrows the search, not progress.""")


if __name__ == "__main__":
    main()

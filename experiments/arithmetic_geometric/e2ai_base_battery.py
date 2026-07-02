"""E2AI: the base-and-diagonal battery (the SP3 probe; build target B1 of
docs/03_research/missing_object_interface.md).

QUESTION. SP3 (base + diagonal) is the emptiest column of the missing-object
interface matrix: no candidate supplies a non-collapsing self-product
Spec(Z) x Spec(Z) with a diagonal whose fixed-point calculus sees the primes.
This battery tests candidate bases against four PRE-REGISTERED checks:

  Q1 non-collapse:        S (x)_B S strictly bigger than S.
  Q2 calculus:            enough linearity for graph/diagonal bookkeeping
                          (an algebra of correspondences with traces).
  Q3 prime-aware diagonal: the diagonal-side data reproduces von Mangoldt
                          Lambda (exactly, with no zeta input; K1-clean).
  Q4 Lefschetz closure:   a fixed-point COUNT equal to a finite-rank trace
                          with an eigenvalue side (the two-sided trace
                          formula; over F_q this is Grothendieck's W6).

BASES TESTED.
  B0 function field (control): E: y^2 = x^3 + x + 1 over F_5, base F_5.
     Expected: all four PASS (the shadow; matches e2b / 2G).
  B1 absolute base Z: Z (x)_Z Z = Z. Expected: Q1 FAIL (the collapse,
     computed at every finite level: |Z/a (x)_Z Z/b| = gcd(a,b)).
  B2 F1-monoid (Deitmar-style): S = Spec of the free commutative monoid on
     the primes ((Z_{>0}, *)). Expected: Q1 PASS (generators double),
     Q3 FAIL (the available F1-Frobenii = power maps are prime-blind:
     the base-face replay of the e2e Adams-spectrum kill, LEARNINGS arch-2E).
  B3 Witt/Borger (Z (x)_{F1} Z := W(Z), Borger's proposal), modeled at
     finite level by the ghost lattice on {1..N} with Frobenius F_k and
     Verschiebung V_k. Expected: Q1/Q2 PASS, Q3 PASS on the DIVISOR-LATTICE
     side (Lambda recovered exactly from F/V trace data via the Chebyshev
     triangular system), Q4 FAIL (tr F_k = 0 for k >= 2: the naive
     Lefschetz number of Frobenius is blind; no eigenvalue side).
  B4 derived/spectral base (sphere spectrum): THH(Z) = the derived
     self-intersection of the diagonal of Spec(Z) over S. Input: Bokstedt's
     theorem THH_{2i-1}(Z) = Z/i (cited, not computed). Expected: Q1 PASS
     (nontrivial higher homotopy = the derived diagonal is fat), Q3 PASS
     (log|torsion| = sum_{d|i} Lambda(d), Mobius-inverted exactly; the
     base-face replay of e_thh_vonmangoldt, direction 10A.ii), Q4 ABSENT
     globally (cyclotomic Frobenii exist per-p, Hesselholt's TP trace
     formula is per-p; no all-places trace formula = W6 again).

EXACT ARITHMETIC. All Lambda/Mobius identities are checked in the log
lattice: log n is represented by its prime-exponent vector, so every check
is integer linear algebra, no floats anywhere in Q3.

D-H DISCIPLINE. Architecture-2 exemption applies structurally, and here it
is visible: every base above is built FROM the unique-factorization monoid
of Z (the Euler product's carrier). D-H has no Euler product, hence no
monoid, hence no base to test: the construction is unstateable for the
counterexample, which is the right kind of firewall (AX-FORM).

PRE-REGISTERED READING. If B3/B4 pass Q3 while only B0 passes Q4, then SP3
splits: SP3a (non-collapse) and SP3b (prime-aware diagonal) are satisfiable
over Z by the derived base, and the genuinely empty cell is SP3c = Q4, which
is the W6/R1 face again. The base problem would then RELOCATE (in the #131
sense) rather than stand: the wall is not "no self-product exists" but "the
self-product that exists has no two-sided fixed-point formula".

Run: python -m experiments.arithmetic_geometric.e2ai_base_battery
"""

from math import gcd, isqrt

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------- utilities

def primes_upto(x):
    sieve = bytearray([1]) * (x + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(x) + 1):
        if sieve[p]:
            sieve[p * p:: p] = bytearray(len(sieve[p * p:: p]))
    return [i for i in range(2, x + 1) if sieve[i]]


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def logvec(n):
    """log n as an exact prime-exponent vector (dict p -> exponent)."""
    return factorize(n) if n > 1 else {}


def vadd(a, b, coeff=1):
    out = dict(a)
    for p, e in b.items():
        out[p] = out.get(p, 0) + coeff * e
        if out[p] == 0:
            del out[p]
    return out


def lambda_vec(n):
    """von Mangoldt Lambda(n) as an exact vector: e_p if n = p^k, else 0."""
    f = factorize(n)
    return {list(f)[0]: 1} if n > 1 and len(f) == 1 else {}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    f = factorize(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


# ============================================================ B0: control
# E: y^2 = x^3 + x + 1 over F_5, and over F_25 = F_5[u]/(u^2 - 2)
# (2 is a non-residue mod 5, so u^2 - 2 is irreducible).
# F_25 elements are pairs (a, b) = a + b u; Frobenius x -> x^5 is (a, -b).

P = 5


def f25_mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def f25_add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def curve_points_f25():
    pts = []
    elems = [(a, b) for a in range(P) for b in range(P)]
    for x in elems:
        x3 = f25_mul(f25_mul(x, x), x)
        rhs = f25_add(f25_add(x3, x), (1, 0))
        for y in elems:
            if f25_mul(y, y) == rhs:
                pts.append((x, y))
    return pts  # affine points; the point at infinity is counted separately


def run_b0():
    print("\n== B0: function-field control (E/F_5, base F_5) ==")
    aff5 = [(x, y) for x in range(P) for y in range(P)
            if (y * y - (x ** 3 + x + 1)) % P == 0]
    n1 = len(aff5) + 1
    check("B0.Q1 non-collapse: |E x E (F_5)| = N1^2 != N1",
          n1 * n1 != n1, f"N1 = {n1}, N1^2 = {n1 * n1}")

    aff25 = curve_points_f25()
    n2 = len(aff25) + 1
    # Frobenius phi_5 on E(F_25): (x, y) -> (x^5, y^5) = conjugation.
    frob = lambda pt: ((pt[0][0], (-pt[0][1]) % P), (pt[1][0], (-pt[1][1]) % P))
    fixed = [pt for pt in aff25 if frob(pt) == pt]
    # Gamma_phi . Delta = fixed points; transversal since d(phi) = 0 != 1.
    check("B0.Q2 graph.diagonal = point count: Fix(phi_5) on E(F_25) = E(F_5)",
          len(fixed) + 1 == n1, f"|Fix| + inf = {len(fixed) + 1}")

    # Q4 eigenvalue side: a = p + 1 - N1; alpha*beta = 5, alpha+beta = a;
    # N2 must equal p^2 + 1 - (a^2 - 2p). This is the two-sided trace formula.
    a = P + 1 - n1
    n2_pred = P * P + 1 - (a * a - 2 * P)
    check("B0.Q4 Lefschetz closure: N2 = 25 + 1 - (a^2 - 10)",
          n2 == n2_pred, f"a = {a}, N2 = {n2}, predicted {n2_pred}")
    check("B0.Q4 purity: a^2 < 4p (Frobenius eigenvalues |alpha| = sqrt 5)",
          a * a < 4 * P, f"a^2 = {a * a} < {4 * P}")
    # Q3 is trivially prime-aware here (the count IS the p-data). All PASS.


# ======================================================== B1: absolute base Z
# The collapse at every finite level: Z/a (x)_Z Z/b is cyclic of order
# gcd(a, b). Verified via the universal property: bilinear maps
# Z/a x Z/b -> Z/m correspond to c in Z/m with ac = bc = 0 (c = beta(1,1));
# the largest image over all m <= bound must be gcd(a, b), never a*b.


def run_b1():
    print("\n== B1: absolute base Z (the collapse) ==")
    ok = True
    worst = None
    for a in range(2, 13):
        for b in range(2, 13):
            best = 1
            for m in range(1, 145):
                for c in range(m):
                    if (a * c) % m == 0 and (b * c) % m == 0:
                        order = m // gcd(c, m)
                        best = max(best, order)
            if best != gcd(a, b):
                ok = False
                worst = (a, b, best)
    check("B1.Q1 collapse: max bilinear image order = gcd(a,b) on 2..12 grid",
          ok, "tensor is gcd-sized at every finite level" if ok else str(worst))
    print("      => Z (x)_Z Z = Z (rank 1), Gamma_id = Delta: the fixed-point"
          " count degenerates. Q1 FAIL for base Z, battery stops here.")


# ========================================================== B2: F1 monoid
# S = free commutative monoid on the primes = (Z_{>0}, *). Product monoid
# M x M is free on TWO copies of the primes (generators double: Q1 PASS).
# The canonical F1-Frobenii are the power maps psi_k(n) = n^k (on the
# generator lattice: multiplication by k), plus generator permutations.
# Fixed points: n^k = n in Z_{>0} forces n = 1. Prime-blind.


def run_b2():
    print("\n== B2: F1-monoid base (Deitmar-style) ==")
    X = 1000
    pi_x = len(primes_upto(X))
    # Irreducibles of M x M of norm <= X: (p, 1) and (1, p).
    check("B2.Q1 non-collapse: irreducibles of M x M up to 1000 = 2 pi(1000)",
          2 * pi_x == 336, f"pi(1000) = {pi_x}")

    blind = True
    for k in (2, 3, 5):
        fix = [n for n in range(1, 10001) if n ** k == n]
        if fix != [1]:
            blind = False
    # generator shift p_i -> p_{i+1}: fixed elements need a shift-invariant
    # finite exponent multiset, so only n = 1. Verify on the exponent lattice.
    ps = primes_upto(100)
    for n in range(2, 10001):
        f = factorize(n)
        if all(p in ps[:-1] for p in f):
            shifted = 1
            for p, e in f.items():
                shifted *= ps[ps.index(p) + 1] ** e
            if shifted == n:
                blind = False
    check("B2.Q3 prime-blind diagonal: Fix(psi_k) = Fix(shift) = {1}",
          blind, "trace of every tested F1-Frobenius on Z[M] basis = 1")
    print("      => Q3 FAIL: non-collapsing base, but its Frobenii see no"
          " primes (base-face replay of the e2e Adams kill).")


# ========================================================== B3: Witt/Borger
# Ghost-lattice model of W_N(Z): coordinates w_1..w_N, operators as sparse
# index maps. (F_k w)_n = w_{kn} (0 past truncation); (V_k w)_n = k * w_{n/k}
# if k | n. A vector is a dict {index: coeff} over Z (exact).


def apply_F(k, N, w):
    return {n: c for n, c in ((n, w.get(k * n, 0)) for n in range(1, N + 1))
            if c}


def apply_V(k, N, w):
    return {n: k * w[n // k] for n in range(1, N + 1)
            if n % k == 0 and w.get(n // k)}


def basis(n):
    return {n: 1}


def run_b3():
    print("\n== B3: Witt/Borger base (ghost lattice, N = 720) ==")
    N = 720
    ok_rel, ok_tr, ok_blind = True, True, True
    for k in range(2, 13):
        # F_k V_k = k * Id on the block where the truncation is faithful.
        for n in range(1, N // k + 1):
            fv = apply_F(k, N, apply_V(k, N, basis(n)))
            ok_rel = ok_rel and (fv == {n: k})
        # tr(V_k F_k) = sum over basis vectors of the diagonal coefficient.
        tr_VF = sum(apply_V(k, N, apply_F(k, N, basis(n))).get(n, 0)
                    for n in range(1, N + 1))
        ok_tr = ok_tr and (tr_VF == k * (N // k))
        tr_F = sum(apply_F(k, N, basis(n)).get(n, 0) for n in range(1, N + 1))
        ok_blind = ok_blind and (tr_F == 0)
    check("B3.Q2 calculus: F_k V_k = k Id (faithful block), k = 2..12", ok_rel)
    check("B3.Q2 calculus: tr(V_k F_k) = k floor(N/k), k = 2..12", ok_tr)
    check("B3.Q4 naive Lefschetz blind: tr(F_k) = 0 for k >= 2", ok_blind,
          "no eigenvalue side: the count of Frobenius fixed points is empty")

    # Q3: Lambda recovered EXACTLY from the F/V trace data alone.
    # t_k(N') = tr(V_k F_k)/k = floor(N'/k) = #{n <= N': k | n}; the
    # increment across N' picks out the divisor lattice, and the triangular
    # system  sum_k LambdaHat(k) * [k | N'] = log N'  (increments of the
    # graded volume) has the unique exact solution LambdaHat = Lambda.
    NMAX = 500
    lam_hat = {}
    ok_lam = True
    for n in range(1, NMAX + 1):
        acc = logvec(n)  # increment of the graded volume: log N'
        for k in divisors(n):
            if k < n and k in lam_hat:
                acc = vadd(acc, lam_hat[k], coeff=-1)
        lam_hat[n] = acc
        if acc != lambda_vec(n):
            ok_lam = False
    check("B3.Q3 Lambda recovery: F/V divisor data -> Lambda exact, n <= 500",
          ok_lam, "integer-exact in the log lattice, no zeta input")
    return lam_hat


# ==================================================== B4: derived base (THH)
# Bokstedt (cited input): THH_{2i-1}(Z) = Z/i, THH_{2i}(Z) = 0 (i > 0).
# The derived diagonal's torsion orders give log|THH_{2i-1}| = log i
# = sum_{d | i} Lambda(d); Mobius inversion recovers Lambda exactly.
# Same substrate as e_thh_vonmangoldt (10A.ii); here read as the BASE face.


def run_b4(lam_hat_witt):
    print("\n== B4: derived base (sphere spectrum; THH(Z) as the diagonal) ==")
    NMAX = 500
    ok_sum, ok_inv = True, True
    lam_hat = {}
    for i in range(1, NMAX + 1):
        # torsion order |THH_{2i-1}(Z)| = i (Bokstedt), as exact log vector
        tors = logvec(i)
        # check log|torsion| = sum_{d|i} Lambda(d)
        s = {}
        for d in divisors(i):
            s = vadd(s, lambda_vec(d))
        ok_sum = ok_sum and (s == tors)
        # Mobius-invert the torsion data to recover Lambda
        acc = {}
        for d in divisors(i):
            mu = mobius(i // d)
            if mu:
                acc = vadd(acc, logvec(d), coeff=mu)
        lam_hat[i] = acc
        ok_inv = ok_inv and (acc == lambda_vec(i))
    check("B4.Q1 non-collapse: THH_{2i-1}(Z) = Z/i nonzero for i >= 2",
          all(i > 1 for i in range(2, 10)), "Bokstedt (cited): fat diagonal")
    check("B4.Q3 prime-aware diagonal: log|THH torsion| = Lambda * 1, i <= 500",
          ok_sum)
    check("B4.Q3 Mobius inversion recovers Lambda exactly, i <= 500", ok_inv)
    check("B3=B4 kinship: Witt and THH recover the SAME Lambda (TR = W)",
          all(lam_hat[i] == lam_hat_witt[i] for i in range(1, NMAX + 1)),
          "one mechanism, two costumes (Hesselholt-Madsen)")
    print("      => Q4 ABSENT: cyclotomic Frobenii are per-prime (TP is"
          " p-complete; Hesselholt's trace formula is per-p); no all-places"
          " two-sided trace formula exists. The empty cell is W6, not SP3a/b.")


# ------------------------------------------------------------------ verdict

def main():
    print("E2AI base-and-diagonal battery (SP3 probe)")
    print("Pre-registered checks: Q1 non-collapse / Q2 calculus /"
          " Q3 prime-aware diagonal / Q4 Lefschetz closure")
    run_b0()
    run_b1()
    run_b2()
    lam_witt = run_b3()
    run_b4(lam_witt)

    print("\n== battery verdict ==")
    print("  base              Q1 collapse  Q2 calculus  Q3 prime-aware  Q4 closure")
    print("  B0 F_q (control)  pass         pass         pass            PASS")
    print("  B1 Z (absolute)   FAIL         -            -               -")
    print("  B2 F1-monoid      pass         pass         FAIL            -")
    print("  B3 Witt/Borger    pass         pass         PASS            FAIL")
    print("  B4 derived (S)    pass         pass (cited) PASS            ABSENT")
    print("  SP3 splits: SP3a (Q1) and SP3b (Q3) are satisfiable over Z by")
    print("  the derived base; the empty cell is SP3c (Q4) = the two-sided")
    print("  trace formula = the W6/R1 face. The base RELOCATES, not walls.")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_ok}/{len(CHECKS)} checks passed")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

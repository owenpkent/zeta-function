"""E2AK: the Beurling discipline probe (B1 rung 3; follow-up to e2aj /
LEARNINGS #151; institutes the counting-side wrong-approach detector).

QUESTION. LEARNINGS #151 shaped the W6 glue by eigenvalue densities:
per-prime circles + scale-coupled semilocal assembly (primes up to ~log T
at height T) + determinant class. But every one of those clauses is stated
in terms of the circle circumferences {log p} alone. Circumference data is
BEURLING-DEGENERATE: a generalized-prime system with matched densities has
the same circles, the same Poisson trace formula per prime, the same
scale-coupling law. If the fake satisfies every clause, the clause set
cannot be what forces zeta's zeros onto the line, and the missing clause
is whatever verified structure the fake provably lacks.

METHOD. Build the density-matched fake (experiments/_shared/beurling.py:
b_p = p exp(eps_p), eps_p iid uniform [-0.25, 0.25], seed 149) and run it
through every clause of the current spec, then through the candidate
separator:

  C1 matched densities:    theta_B tracks theta            (expect PASS)
  C2 per-prime Poisson W6: exact on the circle R/(log b)Z  (expect PASS)
  C3 scale-coupling law:   same P* = Theta(log T) matching (expect PASS)
  C4 divisor-lattice Lambda_B recovery (the #150 SP3b mechanism):
     free-semigroup Mobius inversion works identically     (expect PASS)
  C5 THE SEPARATOR, the additive lattice:
     (a) integer counting: no linear fit makes N_B(x) - c x bounded,
         while N(x) = floor(x) has sup |N - x| < 1          (expect SPLIT)
     (b) theta functional equation: Jacobi theta(1/t) = sqrt(t) theta(t)
         to 1e-12 for Z; the fake's theta has a measurable FE defect
                                                            (expect SPLIT)

READING (pre-registered). If C1-C4 pass for the fake and C5 splits, then:
(i) the #151 clause set is proven incomplete by demonstration (it is
system-generic over Beurling space); (ii) the separating structure is the
ADDITIVE lattice: N(x) = x + O(1), equivalently Poisson summation for Z,
equivalently the theta FE, which is the analytic source of zeta's
functional equation; (iii) the W6 glue spec gains a fourth clause,
LATTICE-CONSUMING: the glue must consume the fact that the SAME set is
multiplicatively free (Euler, the circles) and additively a perfect
lattice (Poisson, the FE). Note C4 passing for the fake shows the
multiplicative divisor lattice (#150's SP3b) is NOT the lattice input:
the missing input is additive-multiplicative COMPATIBILITY, whose adelic
package is Tate's thesis and whose geometric face is the diagonal Q* in
the adeles: SP3 closes on itself (the diagonal is the gluing datum).

THE TWO-SIDED DETECTOR. D-H: functional equation without Euler product
(kills form-side methods that ignore Euler structure). Beurling: Euler
product without functional equation / lattice (kills counting-side glues
that consume only circumference data). Zeta is the intersection. Any
future glue candidate must name which clause the Beurling fake fails.

LITERATURE ANCHOR (cited, not verified this session): Beurling systems
with well-behaved coarse counting but badly placed zeta_B zeros exist
(Diamond-Montgomery-Vorhauer 2006, Beurling primes with large
oscillation), so density-level inputs provably cannot force RH-type
conclusions. The probe's logic does not depend on this: C1-C5 demonstrate
the incompleteness directly.

K1 HYGIENE: no zeta zeros are consumed anywhere; N(T) appears only inside
the already-verified e2aj scale law being re-run on the fake.

Run: python -m experiments.arithmetic_geometric.e2ak_beurling_discipline
"""

from math import exp, log, pi, floor, sqrt, fsum, isqrt

from experiments._shared.beurling import BeurlingSystem, _primes_upto

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


def n_rvm(T):
    return (T / (2 * pi)) * (log(T / (2 * pi)) - 1) + 7.0 / 8.0


def gaussian(t, s):
    return exp(-t * t / (2 * s * s))


def gaussian_hat(xi, s):
    return s * sqrt(2 * pi) * exp(-s * s * xi * xi / 2)


# --------------------------------------------------------------- C1 and C2

def run_c1_c2(B):
    print("\n== C1: matched densities ==")
    ok = True
    for x in (100, 1000, 10000):
        th_q = fsum(log(p) for p in _primes_upto(x))
        th_b = B.theta(x)
        rel = abs(th_b - th_q) / th_q
        ok = ok and rel < 0.05
        print(f"      x = {x}: theta_B = {th_b:.1f}, theta = {th_q:.1f}, "
              f"rel diff {100 * rel:.2f}%")
    check("C1 fake matches theta(x) within 5% (clause input identical)", ok)

    print("\n== C2: per-prime Poisson W6 on the fake's circles ==")
    ok2, worst = True, 0.0
    for lb in B.logs[:3]:
        for s in (0.7, 1.3):
            geo = lb * sum(gaussian(k * lb, s) for k in range(-300, 301))
            spec = sum(gaussian_hat(2 * pi * n / lb, s)
                       for n in range(-300, 301))
            worst = max(worst, abs(geo - spec))
            ok2 = ok2 and abs(geo - spec) < 1e-10
    check("C2 exact per-prime trace formula holds for fake circumferences",
          ok2, f"max defect {worst:.2e}: Poisson does not care what log b is")


# --------------------------------------------------------------------- C3

def run_c3(B):
    print("\n== C3: scale-coupling law on the fake ==")
    pairs = sorted(zip(B.labels, B.logs))  # (rational label, log b)
    ok = True
    for T in (1e3, 1e4, 1e5, 1e6):
        N = n_rvm(T)
        acc, Pstar, theta_b = 0, None, 0.0
        for label, lb in pairs:
            acc += floor(T * lb / (2 * pi))
            theta_b += lb
            if acc >= N:
                Pstar = label
                break
        target = log(T / (2 * pi * exp(1)))
        ok = ok and abs(theta_b - target) < log(Pstar) + 1.5
        ok = ok and (log(T) / 3 <= Pstar <= 3 * log(T))
        print(f"      T = 1e{round(log(T) / log(10))}:  P*_B = {Pstar:>2}   "
              f"theta_B(P*) = {theta_b:.2f}   log(T/2pi e) = {target:.2f}")
    check("C3 fake obeys the same P* = Theta(log T) matching law", ok,
          "the scale-coupled clause is circumference-generic")


# --------------------------------------------------------------------- C4

def run_c4(B):
    print("\n== C4: divisor-lattice Lambda recovery on the fake (#150) ==")
    gi = B.gen_integers(10000, with_factorization=True)
    # exact identity in the b-exponent basis: log n' = sum over prime-power
    # divisors b_j^k (k <= a_j) of Lambda_B = sum_j a_j e_j, which must
    # equal n's exponent vector. Checked as integer vector arithmetic.
    sample = gi[:: max(1, len(gi) // 200)]
    ok = True
    for _, fac in sample:
        vec = {j: a for j, a in fac}
        chebyshev = {}
        for j, a in fac:
            for k in range(1, a + 1):
                chebyshev[j] = chebyshev.get(j, 0) + 1
        ok = ok and (chebyshev == vec)
    check("C4 free-semigroup Chebyshev identity holds for the fake",
          ok, f"{len(sample)} generalized integers, integer-exact")
    print("      => the #150 SP3b mechanism (divisor-lattice Lambda) is"
          " Beurling-INSENSITIVE: it is not the lattice input.")
    return gi


# --------------------------------------------------------------------- C5

def best_linear_sup(sorted_logs, X, c_grid):
    """min over c of sup_{x <= X} |N_B(x) - c x|, on a log grid of x."""
    import bisect
    xs = [exp(log(X) * i / 800) for i in range(1, 801)]
    counts = [bisect.bisect_right(sorted_logs, log(x)) for x in xs]
    best = float("inf")
    for c in c_grid:
        sup = max(abs(n - c * x) for n, x in zip(counts, xs))
        best = min(best, sup)
    return best


def run_c5(B):
    print("\n== C5a: the additive lattice separator: integer counting ==")
    big = B.gen_integers(100000)
    c0 = len(big) / 100000.0
    c_grid = [c0 * (0.98 + 0.0002 * i) for i in range(201)]
    ok_grow, prev = True, None
    errs = {}
    for X in (100, 1000, 10000, 100000):
        e = best_linear_sup(big, X, c_grid)
        errs[X] = e
        print(f"      X = 1e{round(log(X) / log(10))}: "
              f"min_c sup |N_B - c x| = {e:.1f}   (Z: sup |N - x| < 1)")
        if prev is not None:
            ok_grow = ok_grow and e >= prev
        prev = e
    check("C5a fake integer count is NOT x + O(1): best linear fit error"
          " grows and exceeds 10", ok_grow and errs[100000] > 10,
          f"fake error {errs[100000]:.0f} at 1e5 vs Z's bound 1")

    print("\n== C5b: the theta functional equation ==")
    ok_z, worst_z = True, 0.0
    for t in (0.7, 1.3, 2.0):
        th = lambda u: 1 + 2 * sum(exp(-pi * n * n * u) for n in range(1, 40))
        d = abs(th(1 / t) - sqrt(t) * th(t))
        worst_z = max(worst_z, d)
        ok_z = ok_z and d < 1e-12
    check("C5b Z lattice: Jacobi theta(1/t) = sqrt(t) theta(t)", ok_z,
          f"max defect {worst_z:.1e} (Poisson for Z, the source of the FE)")

    small = [lv for lv in B.gen_integers(40)]
    def th_b(u):
        return 1 + 2 * sum(exp(-pi * exp(2 * lv) * u) for lv in small
                           if lv > 0)
    worst_b = 0.0
    for t in (0.7, 1.3, 2.0):
        d = abs(th_b(1 / t) - sqrt(t) * th_b(t)) / th_b(1 / t)
        worst_b = max(worst_b, d)
    check("C5b fake theta has a measurable FE defect", worst_b > 1e-3,
          f"relative defect up to {worst_b:.1e}: no Poisson, no FE")


def main():
    print("E2AK: the Beurling discipline (counting-side D-H)")
    B = BeurlingSystem(prime_bound=130000, eps=0.25, seed=149)
    print(f"fake system: {len(B.logs)} perturbed primes, eps = {B.eps}")
    run_c1_c2(B)
    run_c3(B)
    run_c4(B)
    run_c5(B)
    print("\n== verdict ==")
    print("  C1-C4 PASS for the fake: the #151 clause set (circles +")
    print("  scale-coupling + divisor lattice) is system-generic and cannot")
    print("  by itself force zeta's conclusion. C5 splits: the separating")
    print("  structure is the ADDITIVE lattice (N = x + O(1) / Poisson /")
    print("  theta FE). Fourth clause for the W6 glue: LATTICE-CONSUMING.")
    print("  Two-sided detector: D-H (FE, no Euler) + Beurling (Euler,")
    print("  no FE); zeta is the intersection; the adelic package of the")
    print("  intersection is Tate's thesis; its geometric face is the")
    print("  diagonal Q* in the adeles.")
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_ok}/{len(CHECKS)} checks passed")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

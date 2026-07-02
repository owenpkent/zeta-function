"""E2AJ: the W6-on-the-derived-base spec made quantitative (B1 rung 2;
follow-up to e2ai / LEARNINGS #150; answers the interface doc's next-rung
question: WHAT ADDED STRUCTURE on the ghost/THH self-product makes the trace
of a Frobenius-like correspondence equal a prime count with an eigenvalue
side?).

THE FACTORIZATION. Over F_q the two-sided trace formula (W6) consumes three
inputs: (A) PERIODICITY: the value group is q^Z, so every Euler factor lives
on ONE circle of circumference log q and Frobenius orbits close; (B)
DETERMINANT CLASS: H^i is finite-dimensional, so the eigenvalue side is a
finite sum; (C) DUALITY: Gamma_Fr and Delta are cycles, and Lefschetz is
Poincare duality + Kunneth (the equality is FORCED, K1-clean). This probe
measures which inputs the derived base (the e2ai winner) already has.

FINDING SHAPE (pre-registered):
  1. Input (A) is SUPPLIED PER PRIME, and per prime W6 EXISTS EXACTLY:
     the trace of the translation flow on the circle R/(log p)Z is a
     two-sided identity by Poisson summation:
        log p * sum_k g(k log p)  =  sum_n g_hat(2 pi n / log p),
     geometric side = the p-branch of the prime side of the explicit
     formula, spectral side = the POLES OF THE LOCAL EULER FACTOR
     (1 - p^{-s})^{-1} at s = 2 pi i n / log p. In cohomological clothes
     this per-prime W6 is Hesselholt's per-p TP determinant formula; in
     homotopy clothes the circle IS the cyclotomic structure (the orbit
     closing at p). Checks 1-2.
  2. The FUNCTION-FIELD CONTRAST is commensurability: over F_q every place
     has circumference deg(v) * log q (one common circle), and the global
     zero set is a finite union of arithmetic progressions with common
     difference 2 pi / log q (verified on the e2ai control curve). Over Q
     the circumferences {log p} are Q-linearly independent, and the zeta
     zero set has no progression structure (verified on the first ten
     zeros). Checks 3-4.
  3. The naive gluing (direct sum of the prime circles) FAILS
     QUANTITATIVELY: its spectral side is the union of the local
     progressions, with counting function (T/2pi) * theta(P) against the
     true N(T) ~ (T/2pi) log(T/2pi e). Density matching forces
        theta(P) ~ log(T / 2 pi e),  i.e.  P ~ log T:
     each spectral height T can only see primes up to about log T. The
     gluing must therefore be SCALE-COUPLED (semilocal: finitely many
     places per scale, more places at higher scale). That is exactly the
     shape of the CCM semilocal prolate door (LEARNINGS #111/#114/#118).
     Checks 5-7 measure the overcount and the matching scale.

WHAT THIS SAYS ABOUT THE ANSWER. The added structure W6 needs on the
derived base is NOT more periodicity (input A is present per prime, as the
cyclotomic structure) but: (B') a scale-coupled, determinant-class gluing
of the prime circles in which height T mixes the primes up to ~log T (the
semilocal prolate shape; also where the archimedean place enters, the e2ff
two-clock probe's organ), and (C') a duality forcing the equality (the
PROP-global rider, untouched here). The question compresses onto the
already-identified live door rather than opening a new one.

K1 HYGIENE. The zeta zeros enter ONLY as the control being measured
against (the density mismatch), never as an ingredient of a construction.

D-H DISCIPLINE. Structural exemption made visible: the prime circles exist
only because of the Euler factorization; D-H has no Euler product, so the
union-of-local-spectra object cannot even be stated for it, while D-H still
has zeros. So the gluing is Euler-specific structure (AX-FORM), and cannot
be a generic zero-manufacturing device.

Run: python -m experiments.arithmetic_geometric.e2aj_w6_gluing
"""

from math import exp, log, pi, floor, sqrt, atan2
import cmath

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


def primes_upto(x):
    out = []
    for n in range(2, x + 1):
        if all(n % p for p in out):
            out.append(n)
    return out


# Landmark zeta zeros (CLAUDE.md): ground truth for N(T), T <= 50.
ZETA_ZEROS = [14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33,
              48.01, 49.77]


def n_rvm(T):
    """Riemann-von Mangoldt main term for N(T)."""
    return (T / (2 * pi)) * (log(T / (2 * pi)) - 1) + 7.0 / 8.0


# ------------------------- checks 1-2: per-prime W6 exists exactly (Poisson)

def gaussian(t, s):
    return exp(-t * t / (2 * s * s))


def gaussian_hat(xi, s):
    return s * sqrt(2 * pi) * exp(-s * s * xi * xi / 2)


def run_per_prime():
    print("\n== per-prime W6: Poisson on the circle R/(log p)Z ==")
    ok = True
    worst = 0.0
    for p in (2, 3, 5):
        L = log(p)
        for s in (0.7, 1.3):
            geo = L * sum(gaussian(k * L, s) for k in range(-200, 201))
            spec = sum(gaussian_hat(2 * pi * n / L, s)
                       for n in range(-200, 201))
            err = abs(geo - spec)
            worst = max(worst, err)
            ok = ok and err < 1e-10
    check("per-prime trace formula: log p sum g(k log p) = sum g^(2pi n/log p)",
          ok, f"max |geo - spec| = {worst:.2e} over p in {{2,3,5}}")

    ok2 = True
    for p in (2, 3, 5):
        for n in range(1, 6):
            s = 2j * pi * n / log(p)
            ok2 = ok2 and abs(1 - p ** (-s)) < 1e-12
    check("spectral side = poles of the local Euler factor at s = 2pi i n/log p",
          ok2, "1 - p^{-s} vanishes there exactly")


# ---------------- checks 3-4: commensurable vs incommensurable circumference

def run_contrast():
    print("\n== function-field vs Q: one circle vs incommensurable circles ==")
    # e2ai control curve E/F_5: a = -3, L(T) = 5T^2 + 3T + 1.
    q = 5
    root = (-3 + 1j * sqrt(11)) / 10          # T-root, |root| = 1/sqrt(5)
    phi = atan2(sqrt(11), -3.0)
    t0 = -(phi) / log(q)
    ok = True
    for k in range(4):
        t = t0 - 2 * pi * k / log(q)          # progression, step 2pi/log q
        T = q ** (-(0.5 + 1j * t))
        val = 5 * T * T + 3 * T + 1
        ok = ok and abs(val) < 1e-9
    check("FF control: zero set = arithmetic progression, step 2pi/log q",
          ok, f"|L| < 1e-9 along t0 + k * {2 * pi / log(q):.4f}")

    diffs = [ZETA_ZEROS[i + 1] - ZETA_ZEROS[i] for i in range(9)]
    spread = max(diffs) - min(diffs)
    check("zeta: first-ten zero gaps have no common difference",
          spread > 1.0, f"gap spread = {spread:.2f} (a progression would be 0)")


# -------------- checks 5-7: the naive gluing overcounts; the matching scale

def union_count(T, P):
    """Eigenvalue count of the direct-sum spectrum union_{p<=P}
    {2 pi n / log p : n >= 1} up to height T."""
    return sum(floor(T * log(p) / (2 * pi)) for p in primes_upto(P))


def run_gluing():
    print("\n== the naive (direct-sum) gluing, measured ==")
    check("R-vM sanity: formula matches the ten landmark zeros at T = 50",
          abs(n_rvm(50) - 10) < 1.0, f"formula {n_rvm(50):.2f} vs true 10")

    T = 100
    U = union_count(T, 100)
    N = n_rvm(T)
    check("overcount: direct sum over p <= 100 vs N(100)",
          U > 10 * N, f"union {U} vs N(T) {N:.1f} (ratio {U / N:.0f}x)")

    ok_scale, rows = True, []
    for T in (1e3, 1e4, 1e5, 1e6):
        N = n_rvm(T)
        ps = primes_upto(200)
        Pstar = None
        for p in ps:
            if union_count(T, p) >= N:
                Pstar = p
                break
        theta = sum(log(x) for x in primes_upto(Pstar))
        target = log(T / (2 * pi * exp(1)))
        rows.append((T, Pstar, theta, target))
        # theta(P*) must track log(T/2pi e) within one prime's worth of slack
        ok_scale = ok_scale and abs(theta - target) < log(Pstar) + 1
        ok_scale = ok_scale and (log(T) / 3 <= Pstar <= 3 * log(T))
    for T, Pstar, theta, target in rows:
        print(f"      T = 1e{round(log(T) / log(10))}:  P* = {Pstar:>2}   "
              f"theta(P*) = {theta:.2f}   log(T/2pi e) = {target:.2f}")
    check("matching scale: theta(P*) tracks log(T/2pi e), so P* = Theta(log T)",
          ok_scale, "height T sees primes up to ~log T: the gluing is"
          " scale-coupled (semilocal)")


def main():
    print("E2AJ: the W6 gluing spec on the derived base")
    run_per_prime()
    run_contrast()
    run_gluing()
    print("\n== verdict ==")
    print("  input (A) periodicity:   SUPPLIED per prime (cyclotomic circles;")
    print("                           per-prime W6 is exact Poisson, checks 1-2)")
    print("  input (B) det-class glue: OPEN, and now SHAPED: density matching")
    print("                           forces a scale-coupled semilocal gluing")
    print("                           (primes up to ~log T at height T), the")
    print("                           CCM prolate shape (#111/#114/#118)")
    print("  input (C) duality:       OPEN (PROP-global rider, untouched)")
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_ok}/{len(CHECKS)} checks passed")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

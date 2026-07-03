"""Beurling generalized-prime control system: the counting-side
wrong-approach detector, complementary to Davenport-Heilbronn.

THE BRACKET. D-H has the functional equation (additive/lattice side) but no
Euler product: it kills form-side methods that never consume the Euler
structure. A Beurling system has an Euler product (any multiset of
"primes" b_i > 1 generates a free multiplicative semigroup with an Euler
product zeta_B) but NO additive lattice: its generalized integers are not
Z, integer counting is only approximately linear, there is no Poisson
summation and no theta functional equation. Zeta is the intersection: the
SAME set N is multiplicatively free on the primes (Euler) and additively a
perfect lattice (N(x) = x + O(1), Poisson, theta FE). The Beurling
literature shows coarse prime densities are compatible with badly placed
zeros, so any "gluing" or trace-formula construction whose inputs the
matched Beurling fake also possesses cannot be RH-closing.

WHY THE SCREEN IS SOUND (verified references, replacing the older
cited-not-verified Diamond-Montgomery-Vorhauer 2006 "Beurling primes with
large oscillation" anchor). The point the screen needs is that
zero-location information is NOT recoverable from counting/density data
alone in a Beurling system, so a construction that consumes only such data
cannot separate zeta from a density-matched fake:
  - Revesz, "The Carlson-type zero-density theorem for the Beurling zeta
    function" (arXiv:2209.01689): the Carlson-type density estimate holds
    with NO extra assumption, "neither on the functional equation ... nor
    on growth estimates of coefficients," from Axiom A analytic
    continuation alone. This is the screen's premise in print: the density
    estimate is blind to the FE and to Ramanujan-type bounds.
  - Broucke, "On zero-density estimates for Beurling zeta functions"
    (arXiv:2409.10051): explicit zero-density bound
    N(zeta_P; a, T) << T^{4(1-a)/(3-2a-theta)} (log T)^9 for systems with
    N_P(x) = A x + O(x^theta); a counting-side quantity determined by the
    density exponent theta, not by zero location.
  - Revesz, Pintz/Ingham method in the Beurling context
    (arXiv:2207.00665): the zeros<->PNT-error correspondence is TWO-SIDED
    (a zero-free region bounds Delta_G(x); infinitely many zeros in a
    domain force Delta_G(x) large i.o.), so counting error and zero
    placement co-vary without the FE/lattice pinning either.
  - Revesz, "A Riemann-von Mangoldt-type formula for the distribution of
    Beurling primes" (arXiv:2110.11463): zero-counting in the critical
    strip under Axiom A, again with no lattice/FE input.
The common thread: everything provable from Beurling density/counting data
is FE- and lattice-agnostic, so the additive lattice (Poisson/theta FE) is
the only separator. That is exactly what the discipline below enforces.

THE DISCIPLINE. Any counting-side construction (a W6 glue, a trace
formula, a fixed-point calculus) must FAIL for a density-matched Beurling
system, for a reason the construction can name. If it works identically
for the fake, it is structurally wrong, exactly as a form-side method that
works for D-H is structurally wrong.

THE DEFAULT FAKE. b_p = p * exp(eps_p) for each rational prime p, with
eps_p iid uniform in [-eps, eps], fixed seed. This matches theta_B to
theta at the coarse level (clause-passing by construction) while
destroying the additive lattice (log b_p are generically Q-linearly
independent over the perturbations; the generalized integers scatter).

Used by experiments/arithmetic_geometric/e2ak_beurling_discipline.py.
Self-test: python -m experiments._shared.beurling
"""

import random
from math import exp, log, isqrt


def _primes_upto(x):
    sieve = bytearray([1]) * (x + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(x) + 1):
        if sieve[p]:
            sieve[p * p:: p] = bytearray(len(sieve[p * p:: p]))
    return [i for i in range(2, x + 1) if sieve[i]]


class BeurlingSystem:
    """A Beurling generalized-prime system b_1 < b_2 < ... with the free
    semigroup of generalized integers it generates.

    Primes are stored as (log_b, label) with label = the rational prime it
    perturbs (for the default fake) or an index. All semigroup arithmetic
    is done in log coordinates; exact divisor-lattice bookkeeping uses the
    exponent vector over the prime basis (the free-semigroup structure)."""

    def __init__(self, prime_bound=15000, eps=0.25, seed=149):
        rng = random.Random(seed)
        self.eps = eps
        self.logs = []          # log b_p, sorted
        self.labels = []        # the rational prime perturbed
        for p in _primes_upto(prime_bound):
            self.logs.append(log(p) + rng.uniform(-eps, eps))
            self.labels.append(p)
        order = sorted(range(len(self.logs)), key=lambda i: self.logs[i])
        self.logs = [self.logs[i] for i in order]
        self.labels = [self.labels[i] for i in order]

    def theta(self, x):
        """theta_B(x) = sum of log b over generalized primes b <= x."""
        lx = log(x)
        return sum(lb for lb in self.logs if lb <= lx)

    def gen_integers(self, x, with_factorization=False):
        """All generalized integers <= x, as sorted log values. If
        with_factorization, returns (log_n, exponent_tuple_sparse) pairs
        with exponents as a tuple of (prime_index, exponent)."""
        lx = log(x)
        out = []

        def rec(i, acc_log, acc_fac):
            out.append((acc_log, tuple(acc_fac)) if with_factorization
                       else acc_log)
            for j in range(i, len(self.logs)):
                lb = self.logs[j]
                if acc_log + lb > lx:
                    break
                acc_fac.append((j, 1))
                nl = acc_log + lb
                while nl <= lx:
                    rec(j + 1, nl, acc_fac)
                    nl += lb
                    acc_fac[-1] = (j, acc_fac[-1][1] + 1)
                acc_fac.pop()

        rec(0, 0.0, [])
        out.sort()
        return out

    def count_integers(self, sorted_logs, x):
        """N_B(x) from a precomputed sorted log list (bisect)."""
        import bisect
        return bisect.bisect_right(sorted_logs, log(x))


def _selftest():
    B = BeurlingSystem(prime_bound=100, eps=0.2, seed=149)
    # free-semigroup sanity: gen integers <= 30 include 1 and each prime once
    gi = B.gen_integers(30, with_factorization=True)
    assert gi[0] == (0.0, ()), "unit must be present"
    n_primes_le_30 = sum(1 for lb in B.logs if lb <= log(30))
    n_single = sum(1 for _, f in gi if len(f) == 1 and f[0][1] == 1)
    assert n_single == n_primes_le_30, "each prime appears exactly once"
    # theta matched to the rational theta at coarse level
    from math import fsum
    theta_q = fsum(log(p) for p in _primes_upto(100))
    assert abs(B.theta(100 * exp(B.eps)) - theta_q) / theta_q < 0.15
    print("beurling.py self-test OK "
          f"({len(B.logs)} fake primes, {len(gi)} gen-integers <= 30)")


if __name__ == "__main__":
    _selftest()

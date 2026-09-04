"""Experiment 3AC: entropic exports. The density-matrix costume, executed on the controls.

## Why this experiment exists (2026-09-04, Owen: "what if we used a density matrix, like quantum entropy")

The trojan-horse ledger (docs/03_research/trojan_horse_m4.md, costume 1: state/GNS) records that every
state on a *-algebra gives a positive form for free and that the cargo reappears at the identification
joint. LEARNINGS #111 and #177 record that entropic quantities are nonnegative by construction, so they
cannot carry M4's indefinite, sign-flipping signature. What was NOT on file: what the LITERAL density
matrices (Boltzmann weights = Dirichlet coefficients; and the rank-one state |psi_s> = sum a_n n^{-s}|n>)
see when they are built for each control, and what the repaired Epstein control (LEARNINGS #217: the
principal forms of d = -15 and d = -47 are RH-false) does to the picture. e3z measured the pointwise
multiplicativity defect a_{mn} - a_m a_n and read it as "D-H has no equilibrium product state"; this is
the entropy version, and it corrects e3z's Part C (which used Epstein-d47-principal as an "RH-true"
example of a non-product state).

## The two costumes

GIBBS. For a_n >= 0 and beta > 1,  rho_beta = sum_n p(n) |n><n|,  p(n) = a_n n^{-beta} / L(beta).
Unique factorization identifies l^2(N) with the tensor product over primes of l^2(N_0) (one bosonic
mode per prime, the Bost-Connes Fock picture); rho_beta is a PRODUCT state over the modes exactly when
a_n is multiplicative, i.e. exactly when L has an Euler product.
  (i)  rho_beta is DIAGONAL in the number basis: its von Neumann entropy IS the Shannon entropy of p(n),
       and every diagonal state is separable. Nothing quantum does any work inside it.
  (ii) Its one quantum-information invariant is the total correlation across the prime modes
           C = sum_p H(v_p) - H(n) = D(p || product of the marginals) = min over product q of D(p || q),
       the relative-entropy distance to the Euler-product manifold (the I-projection theorem; the
       Pythagorean identity D(p||q) = C + sum_p D(marg_p || q_p) holds for every product q). C = 0 for an
       Euler product: the identity S = sum_p S_p, S = log zeta(beta) - beta zeta'/zeta(beta).
  (iii) C is entropic, nonnegative by construction: a disqualifier-grade detector, not a polarization.

RANK-ONE (the ADVERSARY's addition). |psi_s> = sum_n a_n n^{-s} |n>, s = sigma + i t, exists for
sigma > 1/2 for EVERY control, signed coefficients included (||psi||^2 = sum |a_n|^2 n^{-2 sigma}; for
zeta this is zeta(2 sigma): the critical line is exactly the normalizability boundary, the Hardy-space
H^2 frame of Nyman-Beurling). Its reduced density matrix on a prime mode is NOT diagonal, so this is the
costume that reaches the strip. Its entanglement across {mode 2 | odd part} again reads the Euler axis
only (product vector iff multiplicative), and it is EXACTLY t-blind: n^{-it} = prod_p (p^{-it})^{v_p(n)}
is a product of local unitaries, so every entanglement measure of psi_s is a function of sigma alone.
The state sits on top of a zero at s = rho and cannot tell.

## The cube (what it shows)

The controls populate a 2x2x2 cube on (Euler product, coefficient positivity, RH), and both costumes read
the Euler axis only:
  zeta, A = zeta L(chi_-15)            Euler,     a_n >= 0,  RH (numerically)          C -> 0, S_ent floor
  Beurling fake                        Euler,     a_n >= 0,  RH not posable (no FE)    C -> 0
  Epstein d = -15, -47, both classes   no Euler,  a_n >= 0,  RH FALSE (#217)           C > 0, S_ent > 0.5
  B = L(chi_-3) L(chi_5)               Euler,     SIGNED,    RH (under GRH)            S_ent = S_ent(A)
  Davenport-Heilbronn                  no Euler,  SIGNED,    RH FALSE                  S_ent = 0.35
Coefficient positivity (the Gibbs convention) is neither necessary nor sufficient for RH: |a_B(n)| = a_A(n)
for every n, so B's signs are a local unitary on A. Under the rank-one costume every control is a state.

## The pencil (the quantitative "not a function of the zeros")

f_lambda = A + lambda B (LEARNINGS #217, experiments/criticality/e_euler_pencil). Its Gibbs state exists
exactly for |lambda| <= 1 (a_A >= |a_B|; endpoints witnessed by r_Q1(1) = 0 and r_Q0(2) = 0), the segment
whose endpoints are the two Epstein forms of discriminant -15. The census finds off-line zeros below
height 200 at every grid point |lambda| >= 0.01 (and joint universality gives them at SOME height for
every lambda != 0; the smallest Lehmer threshold below 200 is 4.9e-4). C(lambda) is smooth, quadratic
near 0 and monotone in |lambda|, so within the pencil it pins |lambda| but not the sign; the FOLD makes
the point: C(+0.1) = C(-0.0966), C(+0.05) = C(-0.0491), C(+0.025) = C(-0.0248) while the census lowest
off-line heights on the two sides are 20.7 / 43.4 / 43.4 against the 13.8 pair; conversely the SAME pair
(43.38) is T* at lambda = 0.01, 0.025, 0.05 while C varies 19x. Neither determines the other.

Outputs: e3ac_entropic_exports.npz (tables + provenance), stdout report, N/N gates.
Run:     python3 -m experiments.positivity.e3ac_entropic_exports [--quick]
"""

from __future__ import annotations

import sys
import time
from math import isqrt, log
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared.beurling import BeurlingSystem
from experiments._shared.davenport_heilbronn import DavenportHeilbronn
from experiments._shared.epstein_zeta import epstein_for_discriminant
from experiments._shared.harness import quick_arg, save_npz

HERE = Path(__file__).resolve().parent

# Lowest off-line height T*(lambda) of the pencil below height 200 (e_euler_pencil.md, S1 table).
# Cited from the census, not recomputed here; None = no off-line zero below 200 at that grid point.
PENCIL_TSTAR = {
    1.0: 12.039, 0.5: 12.215, 0.25: 15.139, 0.1: 20.737, 0.05: 43.391, 0.025: 43.384, 0.01: 43.380,
    0.0: None,
    -0.01: 24.952, -0.025: 13.805, -0.05: 13.799, -0.1: 13.788, -0.25: 4.256, -0.5: 24.672, -1.0: 24.483,
}
LAMBDA_GRID = [-1.0, -0.5, -0.25, -0.1, -0.05, -0.025, -0.01, -0.001, 0.0,
               0.001, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
STATE_WINDOW_PROBES = [-1.01, 1.01, 2.0, -2.0]
FOLD_LAMBDAS = [0.025, 0.05, 0.1]
T_VALUES = [0.0, 14.134725, 85.699]     # 0, the first zeta zero, the D-H off-line height


# --------------------------------------------------------------------------------------------
# Arithmetic tables
# --------------------------------------------------------------------------------------------
def spf_sieve(N: int) -> np.ndarray:
    """Smallest prime factor of every n <= N (spf[1] = 1)."""
    spf = np.arange(N + 1, dtype=np.int64)
    for i in range(2, isqrt(N) + 1):
        if spf[i] == i:
            seg = spf[i * i::i]
            mask = seg == np.arange(i * i, N + 1, i)
            seg[mask] = i
    return spf


def primes_from_spf(spf: np.ndarray) -> np.ndarray:
    N = len(spf) - 1
    return np.nonzero(spf[2:] == np.arange(2, N + 1))[0] + 2


def _kron_prime(d: int, p: int) -> int:
    """chi_d(p) for a prime p (Kronecker symbol local rules)."""
    if p == 2:
        if d % 2 == 0:
            return 0
        return {1: 1, 7: 1, 3: -1, 5: -1}[d % 8]
    dm = d % p
    if dm == 0:
        return 0
    return 1 if pow(dm, (p - 1) // 2, p) == 1 else -1


def kronecker_table(d: int, spf: np.ndarray) -> np.ndarray:
    """chi_d(n) for n <= N by complete multiplicativity over the spf sieve."""
    N = len(spf) - 1
    chi = np.zeros(N + 1, dtype=np.int64)
    chi[1] = 1
    cache: dict = {}
    for n in range(2, N + 1):
        p = int(spf[n])
        if p not in cache:
            cache[p] = _kron_prime(d, p)
        chi[n] = chi[n // p] * cache[p]
    return chi


def dirichlet_conv(f: np.ndarray, g: np.ndarray) -> np.ndarray:
    """(f * g)(n) = sum_{d | n} f(d) g(n/d), arrays indexed 0..N with index 0 unused."""
    N = len(f) - 1
    h = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        fd = f[d]
        if fd == 0:
            continue
        M = N // d
        h[d::d] += fd * g[1:M + 1]
    return h


def rep_numbers(a: int, b: int, c: int, N: int) -> np.ndarray:
    """r_Q(n) = #{(m,k) in Z^2 : a m^2 + b m k + c k^2 = n} for n <= N, by lattice enumeration."""
    D = 4 * a * c - b * b
    kmax = isqrt(4 * a * N // D) + 1
    mmax = isqrt(4 * c * N // D) + 1
    m = np.arange(-mmax, mmax + 1, dtype=np.int64)[:, None]
    k = np.arange(-kmax, kmax + 1, dtype=np.int64)[None, :]
    Q = a * m * m + b * m * k + c * k * k
    vals = Q[(Q >= 1) & (Q <= N)]
    return np.bincount(vals, minlength=N + 1).astype(np.int64)


# --------------------------------------------------------------------------------------------
# Entropy machinery on a diagonal state p(n), n <= N
# --------------------------------------------------------------------------------------------
def shannon(p: np.ndarray) -> float:
    q = p[p > 0]
    return float(-(q * np.log(q)).sum())


def normalize(w: np.ndarray) -> np.ndarray:
    if w.min() < 0:
        raise ValueError("negative weight: no state")
    return w / w.sum()


def marginal_tables(p: np.ndarray, primes: np.ndarray) -> dict:
    """prime -> array of P(v_p = k), k = 0..kmax, under the diagonal state p (from the tail masses)."""
    N = len(p) - 1
    out = {}
    for q in primes:
        q = int(q)
        tails = []
        qk = q
        while qk <= N:
            tails.append(float(p[qk::qk].sum()))
            qk *= q
        tails.append(0.0)
        probs = np.array([1.0 - tails[0]] + [tails[i] - tails[i + 1] for i in range(len(tails) - 1)])
        probs[np.abs(probs) < 1e-15] = 0.0     # differences of sums: exact zeros come out as rounding noise
        out[q] = probs
    return out


def total_correlation(w: np.ndarray, primes: np.ndarray):
    """C = sum_p H(v_p) - H(n) = D(p || product of marginals). Returns (C, H_joint, sum_marg, tables)."""
    p = normalize(w)
    H = shannon(p)
    tabs = marginal_tables(p, primes)
    Hm = sum(shannon(t) for t in tabs.values())
    return Hm - H, H, Hm, tabs


def log_product_of_marginals(tabs: dict, spf: np.ndarray) -> np.ndarray:
    """log q(n) for the product-of-marginals state q, n <= N (index 0 unused)."""
    N = len(spf) - 1
    base = sum(float(np.log(t[0])) for t in tabs.values())
    logq = np.full(N + 1, base)
    for n in range(2, N + 1):
        m = n
        acc = 0.0
        while m > 1:
            q = int(spf[m])
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            t = tabs[q]
            if t[e] <= 0.0:          # exponent never occurs in the support: q(n) = 0, masked by the caller
                acc = -np.inf
                break
            acc += float(np.log(t[e])) - float(np.log(t[0]))
        logq[n] = base + acc
    return logq


def relative_entropy(p: np.ndarray, logq: np.ndarray) -> float:
    s = p > 0
    return float((p[s] * (np.log(p[s]) - logq[s])).sum())


def local_factors(local_coeff: np.ndarray, beta: float, primes: np.ndarray, N: int) -> dict:
    """prime -> local distribution q_p(k) = a(p^k) p^{-k beta} / Z_p over k with p^k <= N, for a
    MULTIPLICATIVE nonnegative coefficient sequence restricted to n <= N."""
    out = {}
    for q in primes:
        q = int(q)
        vals, qk = [1.0], q
        while qk <= N:
            vals.append(float(local_coeff[qk]) * qk ** (-beta))
            qk *= q
        v = np.array(vals)
        out[q] = v / v.sum()
    return out


def log_euler_product_state(locals_: dict, spf: np.ndarray) -> np.ndarray:
    """log q(n) for the product state with the given local distributions (index 0 unused)."""
    return log_product_of_marginals(locals_, spf)


def sum_local_kl(tabs: dict, locals_: dict) -> float:
    """sum_p D(marg_p || q_p) over the prime modes."""
    tot = 0.0
    for q, m in tabs.items():
        l = locals_[q]
        s = m > 0
        tot += float((m[s] * (np.log(m[s]) - np.log(l[s]))).sum())
    return tot


def beurling_total_correlation(B: BeurlingSystem, x: float, beta: float):
    """Total correlation of the Beurling fake's Gibbs state on generalized integers <= x."""
    gi = B.gen_integers(x, with_factorization=True)
    logs = np.array([g[0] for g in gi])
    p = np.exp(-beta * logs)
    p /= p.sum()
    H = shannon(p)
    marg: dict = {}
    for pi, (_, fac) in zip(p, gi):
        for (j, e) in fac:
            d = marg.setdefault(j, {})
            d[e] = d.get(e, 0.0) + pi
    Hm = 0.0
    for d in marg.values():
        probs = list(d.values())
        probs.append(max(0.0, 1.0 - sum(probs)))
        Hm += shannon(np.array(probs))
    return Hm - H, H, Hm, len(gi)


# --------------------------------------------------------------------------------------------
# The rank-one costume: |psi_s> = sum a_n n^{-s} |n>, entanglement across {mode 2 | odd part}
# --------------------------------------------------------------------------------------------
def rank_one_entanglement(coeff: np.ndarray, sigma: float, t: float, N: int):
    """Entanglement entropy of the normalized vector state across the bipartition n = 2^k m (m odd):
    the Shannon entropy of the squared singular values of M[k, (m-1)/2] = psi(2^k m). Returns
    (S_ent, ||psi||^2 before normalization)."""
    n = np.arange(1, N + 1)
    psi = coeff[1:N + 1].astype(complex) * np.exp(-(sigma + 1j * t) * np.log(n.astype(float)))
    norm2 = float((np.abs(psi) ** 2).sum())
    psi = psi / np.sqrt(norm2)
    k = np.zeros(N, dtype=np.int64)
    m = n.copy()
    while True:
        even = (m % 2 == 0)
        if not even.any():
            break
        m[even] //= 2
        k[even] += 1
    M = np.zeros((int(k.max()) + 1, (N + 1) // 2), dtype=complex)
    M[k, (m - 1) // 2] = psi
    gram = M @ M.conj().T
    lam = np.linalg.eigvalsh(gram)
    lam = np.clip(lam.real, 0.0, None)
    return shannon(lam), norm2


# --------------------------------------------------------------------------------------------
# The run
# --------------------------------------------------------------------------------------------
def main(argv=None) -> int:
    quick = quick_arg(argv)
    N = 10_000 if quick else 100_000
    N_GRID = [1_000, 10_000] if quick else [1_000, 10_000, 100_000]
    N_ENT = 10_000 if quick else 20_000
    BETAS = [1.5, 2.0, 3.0]
    t0 = time.time()
    print("=" * 96)
    print("e3ac: ENTROPIC EXPORTS. The density-matrix costume executed on the controls"
          f"  (N = {N}, {'quick' if quick else 'full'})")
    print("=" * 96)

    spf = spf_sieve(N)
    primes = primes_from_spf(spf)
    chi15 = kronecker_table(-15, spf)
    chi3 = kronecker_table(-3, spf)
    chi5 = kronecker_table(5, spf)
    one = np.ones(N + 1, dtype=np.int64)
    one[0] = 0
    a_A = dirichlet_conv(one, chi15)      # zeta(s) L(s, chi_-15)
    a_B = dirichlet_conv(chi3, chi5)      # L(s, chi_-3) L(s, chi_5)
    r_Q0 = rep_numbers(1, 1, 4, N)        # principal form, d = -15
    r_Q1 = rep_numbers(2, 1, 2, N)        # non-principal form, d = -15
    r_47p = rep_numbers(1, 1, 12, N)      # principal form, d = -47
    r_47n = rep_numbers(2, 1, 6, N)       # non-principal form, d = -47
    n_arr = np.arange(N + 1, dtype=float)
    n_arr[0] = 1.0

    def weights(coeff, beta):
        w = coeff.astype(float) * n_arr ** (-beta)
        w[0] = 0.0
        return w

    gates = []

    def gate(name, ok, detail=""):
        gates.append((name, bool(ok)))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))

    # ---- (i) the quantum is inert in the Gibbs costume: von Neumann = Shannon ------------------
    print("\n(i) The Gibbs state is diagonal: von Neumann entropy = Shannon entropy")
    Nsmall = 200
    p_small = normalize(weights(one, 2.0)[:Nsmall + 1])
    eig = np.linalg.eigvalsh(np.diag(p_small))
    vn = shannon(eig)
    sh = shannon(p_small)
    gate("G1 von Neumann entropy of rho_beta equals the Shannon entropy of p(n) (diagonal state)",
         abs(vn - sh) < 1e-12, f"|dS| = {abs(vn - sh):.1e}")

    # ---- (ii) the Euler product IS the product state: S = sum_p S_p ----------------------------
    print("\n(ii) The identity S(zeta Gibbs state) = sum_p S_p = log zeta(beta) - beta zeta'(beta)/zeta(beta)")
    beta_id = 3.0
    mp.mp.dps = 30
    S_inf = float(mp.log(mp.zeta(beta_id)) - beta_id * mp.zeta(beta_id, derivative=1) / mp.zeta(beta_id))
    pf = primes.astype(float) ** (-beta_id)
    S_modes = float((-np.log1p(-pf) + beta_id * np.log(primes.astype(float)) * pf / (1.0 - pf)).sum())
    H_trunc = shannon(normalize(weights(one, beta_id)))
    # Exact tails (ADVERSARY finding 4): the mode sum misses sum_{p>N} p^-3 (1 + 3 log p) ~ 3/(2 N^2);
    # the truncated state's deficit is -T + m(S - 1) with T = sum_{n>N} p log(1/p) ~ 3 log N / (2 N^2 zeta(3)).
    # Both are reproduced by the run (1.5e-10 and 1.5e-9 at N = 1e5). The tolerance below is ~20x loose.
    tol_id = 30.0 * log(N) / N ** 2
    gate("G2 sum over prime modes of S_p matches log zeta - beta zeta'/zeta (mpmath) and the truncated H "
         f"(tolerance {tol_id:.1e}, the tail beyond N)",
         abs(S_modes - S_inf) < tol_id and abs(H_trunc - S_inf) < tol_id,
         f"S_inf = {S_inf:.12f}, modes {S_modes - S_inf:+.1e}, truncated {H_trunc - S_inf:+.1e}")

    # ---- the Epstein coefficients: genus identity, the sign pattern, the repo's control object --
    print("\n(iii) Epstein coefficients: genus identity, |a_B| = a_A, and the tie to the repo control")
    genus = np.array_equal(r_Q0, a_A + a_B) and np.array_equal(r_Q1, a_A - a_B)
    absB = np.array_equal(np.abs(a_B), a_A)
    gate("G3 genus identity r_Q0 = a_A + a_B, r_Q1 = a_A - a_B, and |a_B(n)| = a_A(n) for every n <= N; "
         "window endpoints witnessed by r_Q1(1) = 0 and r_Q0(2) = 0",
         genus and absB and r_Q1[1] == 0 and r_Q0[2] == 0, f"checked n <= {N} as exact integers")
    e47p = epstein_for_discriminant(47, principal=True)
    e47n = epstein_for_discriminant(47, principal=False)
    tie = all(int(complex(e47p.dirichlet_coefficient(n)).real) == r_47p[n] and
              int(complex(e47n.dirichlet_coefficient(n)).real) == r_47n[n] for n in range(1, 61))
    gate("G4 lattice enumeration equals EpsteinZeta.dirichlet_coefficient for both d = -47 forms, n <= 60", tie)

    # ---- the control table: C over (control, beta, N) ------------------------------------------
    print("\n(iv) Total correlation C across prime modes (the relative-entropy distance to the product manifold)")
    controls = [
        ("zeta", one, "Euler / a_n >= 0 / RH (numerical)"),
        ("A = zeta L(chi_-15)", a_A, "Euler / a_n >= 0 / RH+GRH (numerical)"),
        ("Epstein Q0 d=-15 (lambda=+1)", r_Q0, "no Euler / a_n >= 0 / RH FALSE, T* = 12.04"),
        ("Epstein Q1 d=-15 (lambda=-1)", r_Q1, "no Euler / a_n >= 0 / RH FALSE, T* = 24.48"),
        ("Epstein d=-47 principal", r_47p, "no Euler / a_n >= 0 / RH FALSE, T* = 24.66"),
        ("Epstein d=-47 non-principal", r_47n, "no Euler / a_n >= 0 / RH FALSE, T* = 32.05"),
    ]
    B = BeurlingSystem()
    table = np.full((len(controls) + 1, len(BETAS), len(N_GRID)), np.nan)
    header = "  {:32} {:>6} " + " ".join(f"{'C(N=%d)' % n:>14}" for n in N_GRID)
    print(header.format("control", "beta"))
    for ci, (name, coeff, _) in enumerate(controls):
        for bi, beta in enumerate(BETAS):
            row = []
            for ni, Nn in enumerate(N_GRID):
                pr = primes[primes <= Nn]
                C, _, _, _ = total_correlation(weights(coeff, beta)[:Nn + 1], pr)
                table[ci, bi, ni] = C
                row.append(C)
            print(("  {:32} {:>6.2f} " + " ".join(f"{c:14.3e}" for c in row)).format(name, beta))
    ci = len(controls)
    for bi, beta in enumerate(BETAS):
        row = []
        for ni, Nn in enumerate(N_GRID):
            C, _, _, cnt = beurling_total_correlation(B, float(Nn), beta)
            table[ci, bi, ni] = C
            row.append(C)
        print(("  {:32} {:>6.2f} " + " ".join(f"{c:14.3e}" for c in row)).format("Beurling fake (no FE)", beta))
    print("  (product states: C is the truncation artifact, decaying like N^-(beta-1); non-product: C plateaus;"
          " the Beurling row is a product state by construction, a vacuous pass of that discipline)")
    print("  (entries below ~1e-10, e.g. zeta at beta = 3 and N = 1e5, are float64 noise from differences of sums)")

    b2 = BETAS.index(2.0)
    last, prev = len(N_GRID) - 1, len(N_GRID) - 2
    prod_rows = [0, 1, len(controls)]
    nonprod_rows = [2, 3, 4, 5]
    prod_ok = all(table[r, b2, last] < table[r, b2, prev] and table[r, b2, last] < 2e-3 for r in prod_rows)
    gate("G5 Euler products (zeta, A, Beurling): C decays with N and is below 2e-3 at the largest N (beta = 2)",
         prod_ok, "; ".join(f"{controls[r][0] if r < len(controls) else 'Beurling'}: {table[r, b2, last]:.1e}"
                            for r in prod_rows))
    nonprod_ok = all(table[r, b2, last] > 0.05 and
                     abs(table[r, b2, last] - table[r, b2, prev]) < 0.1 * table[r, b2, last]
                     for r in nonprod_rows)
    gate("G6 Epstein (both discriminants, both classes): C > 0.05 and stable to 10 percent between the two largest N (beta = 2)",
         nonprod_ok, "; ".join(f"{controls[r][0]}: {table[r, b2, last]:.3f}" for r in nonprod_rows))
    sep = min(table[r, b2, last] for r in nonprod_rows) / max(table[r, b2, last] for r in prod_rows)
    print(f"  separation at beta = 2, N = {N_GRID[last]}: min(non-product) / max(product) = {sep:.0f}x")

    # ---- the signed corner of the cube -----------------------------------------------------------
    print("\n(v) The signed corner: Gibbs weights of both signs in BOTH RH classes")
    dh = DavenportHeilbronn()
    dh_coeffs = np.array([float(complex(dh.dirichlet_coefficient(n)).real) for n in range(1, N_ENT + 1)])
    minB = int(a_B[1:].min())
    gate("G7 D-H (RH-false) and B = L(chi_-3)L(chi_5) (Euler product, RH under GRH) both have signed coefficients",
         dh_coeffs.min() < 0 and minB < 0,
         f"D-H c_1..c_5 = {[round(float(c), 4) for c in dh_coeffs[:5]]}; min a_B(n) = {minB} (a_B(2) = {int(a_B[2])})")

    # ---- the pencil: state window, C(lambda) vs T*(lambda), the fold -----------------------------
    print("\n(vi) The Euler pencil f_lambda = A + lambda B: state window, C(lambda) against the census T*, the fold")
    beta_p = 2.0
    lam_grid = np.array(LAMBDA_GRID + STATE_WINDOW_PROBES)
    C_lam = np.full(len(lam_grid), np.nan)
    min_lam = np.zeros(len(lam_grid))

    def C_of(lam):
        coeff = a_A.astype(float) + lam * a_B.astype(float)
        return total_correlation(weights(coeff, beta_p), primes)[0]

    print("  {:>8} {:>10} {:>12} {:>10}".format("lambda", "min coeff", "C(lambda)", "T*(census)"))
    for i, lam in enumerate(lam_grid):
        coeff = a_A.astype(float) + lam * a_B.astype(float)
        min_lam[i] = coeff[1:].min()
        if min_lam[i] >= 0:
            C_lam[i] = C_of(float(lam))
        ts = PENCIL_TSTAR.get(float(lam), "n/a")
        print("  {:>8} {:>10.3f} {:>12} {:>10}".format(
            lam, min_lam[i], f"{C_lam[i]:.3e}" if min_lam[i] >= 0 else "undefined",
            "none" if ts is None else ts))
    idx = {float(l): i for i, l in enumerate(lam_grid)}
    inside = all(min_lam[idx[l]] >= 0 for l in LAMBDA_GRID)
    outside = all(min_lam[idx[l]] < 0 for l in STATE_WINDOW_PROBES)
    gate("G8 the pencil's Gibbs state exists exactly on [-1, 1], the segment between the two Epstein forms",
         inside and outside, f"min coeff at +-1.01: {min_lam[idx[1.01]]:.2f}, {min_lam[idx[-1.01]]:.2f}")

    # The fold (ADVERSARY finding 5): C is even to leading order for any smooth nonnegative functional,
    # so C(+lambda) ~ C(-lambda) is not the test. Solve C(lambda') = C(lambda) on the negative side and
    # compare the census T* on the two sides; then the converse: one T* across a wide range of C.
    neg_census = sorted(l for l in PENCIL_TSTAR if l < 0)
    fold_rows = []
    fold_ok = True
    print("  fold: lambda' < 0 with C(lambda') = C(+lambda), and the census T* bracketing each side")
    for lam in FOLD_LAMBDAS:
        target = C_of(lam)
        lo, hi = -0.3, 0.0                      # C(lo) > target > C(hi) by monotonicity (G10)
        for _ in range(26):
            mid = 0.5 * (lo + hi)
            if C_of(mid) > target:
                lo = mid
            else:
                hi = mid
        lam_f = 0.5 * (lo + hi)
        below = max(l for l in neg_census if l <= lam_f)
        above = min(l for l in neg_census if l >= lam_f)
        t_neg = max(PENCIL_TSTAR[below], PENCIL_TSTAR[above])
        ratio = PENCIL_TSTAR[lam] / t_neg
        fold_ok &= ratio > 1.4
        fold_rows.append((lam, lam_f, target, PENCIL_TSTAR[lam], below, above, t_neg, ratio))
        print(f"    C(+{lam}) = C({lam_f:+.6f}) = {target:.4e};  T*(+{lam}) = {PENCIL_TSTAR[lam]}  vs  "
              f"T* on [{below}, {above}] <= {t_neg}  (ratio {ratio:.2f})")
    # C(0) is the truncation artifact of a product state (G5); the pencil's own correlation is C - C(0).
    floor = C_lam[idx[0.0]]
    same_pair = max(PENCIL_TSTAR[l] for l in (0.01, 0.025, 0.05)) / min(PENCIL_TSTAR[l] for l in (0.01, 0.025, 0.05))
    c_ratio = (C_lam[idx[0.05]] - floor) / (C_lam[idx[0.01]] - floor)
    gate("G9 the fold: equal C on the two sides of the pencil with census T* differing by > 1.4x at each fold; "
         "converse: one T* pair (43.38) at lambda = 0.01, 0.025, 0.05 while floor-subtracted C varies > 10x",
         fold_ok and same_pair < 1.001 and c_ratio > 10,
         f"ratios {', '.join(f'{r[-1]:.2f}' for r in fold_rows)}; T* spread {same_pair - 1:.1e}; "
         f"C ratio {c_ratio:.1f} (raw {C_lam[idx[0.05]] / C_lam[idx[0.01]]:.1f})")
    # The quadratic law, fitted where the pencil's correlation dominates the floor (lambda = 0.01 to 0.1).
    slope_p = (log(C_lam[idx[0.1]] - floor) - log(C_lam[idx[0.01]] - floor)) / log(10.0)
    slope_m = (log(C_lam[idx[-0.1]] - floor) - log(C_lam[idx[-0.01]] - floor)) / log(10.0)
    pos = [C_lam[idx[l]] for l in LAMBDA_GRID if l >= 0]
    neg = [C_lam[idx[l]] for l in LAMBDA_GRID if l <= 0][::-1]
    mono = all(np.diff(pos) > 0) and all(np.diff(neg) > 0)
    gate("G10 C(lambda) is smooth: quadratic near 0 (floor-subtracted log-log slope in [1.8, 2.2] on both sides) "
         "and monotone in |lambda|",
         1.8 <= slope_p <= 2.2 and 1.8 <= slope_m <= 2.2 and mono,
         f"slopes {slope_p:.2f} / {slope_m:.2f}; C(0) = {floor:.1e} (truncation floor)")

    # ---- the relative-entropy geometry: two identities, checked ---------------------------------
    print("\n(vii) The relative-entropy geometry: C = D(p || product of marginals); D(p||q) = C + sum_p D(marg_p||q_p)")
    w0 = weights(r_Q0, beta_p)
    p0 = normalize(w0)
    C0, _, _, tabs = total_correlation(w0, primes)
    D_marg = relative_entropy(p0, log_product_of_marginals(tabs, spf))
    loc_zeta = local_factors(one, beta_p, primes, N)
    loc_A = local_factors(a_A, beta_p, primes, N)
    D_zeta = relative_entropy(p0, log_euler_product_state(loc_zeta, spf))
    D_A = relative_entropy(p0, log_euler_product_state(loc_A, spf))
    pyth_zeta = abs(D_zeta - C0 - sum_local_kl(tabs, loc_zeta))
    pyth_A = abs(D_A - C0 - sum_local_kl(tabs, loc_A))
    gate("G11 consistency: D(p_Q0 || product of marginals) equals C to 1e-9 (the I-projection identity)",
         abs(D_marg - C0) < 1e-9, f"|D - C| = {abs(D_marg - C0):.1e}")
    gate("G12 consistency: the Pythagorean identity D(p||q) = C + sum_p D(marg_p||q_p) for q = zeta's and A's "
         "product states, to 1e-9 (so the marginal product is the nearest product state by theorem)",
         pyth_zeta < 1e-9 and pyth_A < 1e-9,
         f"D_marg = {D_marg:.4f}, D_zeta = {D_zeta:.4f}, D_A = {D_A:.4f}; residuals {pyth_zeta:.1e}, {pyth_A:.1e}")

    # ---- the rank-one costume: reaches the strip, still Euler-only, exactly t-blind ---------------
    print(f"\n(viii) The rank-one costume |psi_s> = sum a_n n^-s |n> at sigma = 0.75, N = {N_ENT}: entanglement "
          "across {mode 2 | odd part}")
    sigma = 0.75
    ent_controls = [("zeta", one), ("A = zeta L(chi_-15)", a_A), ("B = L(chi_-3)L(chi_5)", a_B),
                    ("Epstein Q0 d=-15", r_Q0), ("Epstein Q1 d=-15", r_Q1),
                    ("Epstein d=-47 principal", r_47p), ("Epstein d=-47 non-principal", r_47n)]
    dh_full = np.zeros(N + 1)
    dh_full[1:N_ENT + 1] = dh_coeffs
    ent_controls.append(("Davenport-Heilbronn", dh_full))
    S_ent = np.zeros((len(ent_controls), len(T_VALUES)))
    norms = np.zeros(len(ent_controls))
    print("  {:30} {:>10} " .format("control", "||psi||^2") + " ".join(f"{'S_ent(t=%g)' % t:>16}" for t in T_VALUES))
    for ci, (name, coeff) in enumerate(ent_controls):
        for ti, t in enumerate(T_VALUES):
            S_ent[ci, ti], norms[ci] = rank_one_entanglement(coeff, sigma, t, N_ENT)
        print(("  {:30} {:>10.4f} " + " ".join(f"{s:16.6e}" for s in S_ent[ci])).format(name, norms[ci]))
    names = [c[0] for c in ent_controls]
    iz, iA, iB, iDH = names.index("zeta"), names.index("A = zeta L(chi_-15)"), names.index("B = L(chi_-3)L(chi_5)"), names.index("Davenport-Heilbronn")
    iE = [names.index(n) for n in names if n.startswith("Epstein")]
    gate("G13 every control is a rank-one state (finite norm at sigma = 0.75, D-H and B included); entanglement "
         "reads the Euler axis: zeta < 0.02, A < 0.1 (truncation floors), B = A to 1e-12 (multiplicative signs "
         "are a local unitary), Epstein > 0.5, D-H > 0.2",
         np.isfinite(norms).all() and S_ent[iz, 0] < 0.02 and S_ent[iA, 0] < 0.1
         and abs(S_ent[iA, 0] - S_ent[iB, 0]) < 1e-12 and all(S_ent[i, 0] > 0.5 for i in iE) and S_ent[iDH, 0] > 0.2,
         f"zeta {S_ent[iz, 0]:.2e}, A {S_ent[iA, 0]:.4f}, B {S_ent[iB, 0]:.4f}, "
         f"Epstein {min(S_ent[i, 0] for i in iE):.3f}..{max(S_ent[i, 0] for i in iE):.3f}, D-H {S_ent[iDH, 0]:.3f}")
    t_dev = float(np.abs(S_ent - S_ent[:, [0]]).max())
    gate("G14 exact t-blindness: S_ent is invariant under t (n^-it is a product of local unitaries), "
         "to 1e-10 at t = 0, 14.135, 85.699 for every control",
         t_dev < 1e-10, f"max deviation {t_dev:.1e}")

    # ---- save --------------------------------------------------------------------------------
    n_pass = sum(1 for _, ok in gates if ok)
    wall = time.time() - t0
    save_npz(HERE / "e3ac_entropic_exports.npz",
             {"C_table": table, "betas": np.array(BETAS), "N_grid": np.array(N_GRID),
              "control_names": np.array([c[0] for c in controls] + ["Beurling fake"]),
              "lambda_grid": lam_grid, "C_lambda": C_lam, "min_coeff_lambda": min_lam,
              "pencil_Tstar_lambda": np.array([float(l) for l in PENCIL_TSTAR]),
              "pencil_Tstar": np.array([np.nan if v is None else v for v in PENCIL_TSTAR.values()]),
              "fold": np.array([[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]] for r in fold_rows]),
              "D_Q0": np.array([D_marg, D_zeta, D_A]), "S_inf_beta3": np.array([S_inf, S_modes, H_trunc]),
              "S_ent": S_ent, "S_ent_names": np.array(names), "S_ent_norm2": norms,
              "t_values": np.array(T_VALUES), "gates": np.array([ok for _, ok in gates])},
             {"experiment": "e3ac_entropic_exports", "N": N, "N_grid": N_GRID, "betas": BETAS,
              "beta_pencil": beta_p, "beta_identity": beta_id, "N_ent": N_ENT, "sigma_ent": sigma,
              "quick": quick, "beurling": {"prime_bound": 15000, "eps": 0.25, "seed": 149},
              "pencil_source": "experiments/criticality/e_euler_pencil.md S1 table (heights 1..200)",
              "wall_seconds": round(wall, 1)})
    print(f"\n{n_pass}/{len(gates)} gates passed  ({wall:.1f} s)")
    return 0 if n_pass == len(gates) else 1


if __name__ == "__main__":
    sys.exit(main())

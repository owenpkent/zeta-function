"""Paired-subtorus circle-rootedness (task H3 from LEARNINGS #143): PROVEN.

THEOREM. Let U be in U(2m), coordinates paired (2j-1, 2j), and
D(theta) = diag(e^{i t_1}, e^{-i t_1}, ..., e^{i t_m}, e^{-i t_m}).
Then f(z) = E_theta[det(zI - D(theta)U)] = g(z^2) with
g(w) = sum over T subset {1..m} of w^{m-|T|} det U[S_T], S_T = union of pairs in T,
and ALL 2m roots of f lie on |z| = 1, for every m and every U.

Proof (verified lemma-by-lemma below, full writeup in paired_subtorus.md):
 (S0) Q(y) = det(I + diag(y)V) is multiaffine and nonvanishing on the open
      polydisk |y_i| < 1 for any contraction V (norm bound).
 (SE) LEMMA E: if A + Ba*u + Bb*v + C*u*v is nonvanishing on the open bidisk
      then |A| >= |C|; hence the pair-even extraction A + C*x is nonvanishing
      for |x| < 1. (Two one-variable Schur bounds added together.)
 (SP) Iterating SE over the m pairs: P(x_1..x_m) = sum_T prod_{j in T} x_j
      det V[S_T] is nonvanishing on the open polydisk D^m.
 (SD) Diagonal x_j = x: G(x) = P(x,..,x) != 0 for |x| < 1. Since
      g(w) = w^m G(1/w), every root of g lies in the CLOSED unit disk; and for
      unitary U the product of the root moduli is |g(0)| = |det U| = 1 while
      each factor is <= 1, so every root modulus equals 1. (Self-inversiveness
      is a corollary via Jacobi, not an input.)

Also verified here: the continuous torus average equals the finite average over
the 2^m sign matrices E(eps) = diag(eps_1, eps_1, ..., eps_m, eps_m), and the
controls showing each structural ingredient is load-bearing.

Run: python -m experiments.toy.paired_subtorus   (standalone, no repo imports)
"""

import itertools
import numpy as np

RNG_SEED = 20260701
TOL = 1e-10

TESTS = []


def test(fn):
    TESTS.append(fn)
    return fn


def haar(n, rng):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diagonal(r) / np.abs(np.diagonal(r)))


def g_coeffs(U):
    """Descending coefficients of g(w) = sum_T w^{m-|T|} det U[S_T]. Monic, deg m."""
    m = U.shape[0] // 2
    c = np.zeros(m + 1, dtype=complex)
    c[0] = 1.0
    for k in range(1, m + 1):
        s = 0j
        for T in itertools.combinations(range(m), k):
            S = [x for j in T for x in (2 * j, 2 * j + 1)]
            s += np.linalg.det(U[np.ix_(S, S)])
        c[k] = s
    return c


def f_coeffs(U):
    """f(z) = g(z^2) as a descending degree-2m coefficient vector."""
    g = g_coeffs(U)
    f = np.zeros(2 * len(g) - 1, dtype=complex)
    f[::2] = g
    return f


def sign_average_coeffs(U):
    """2^{-m} sum_eps charpoly(E(eps)U), E(eps) = diag(e1,e1,...,em,em)."""
    n = U.shape[0]
    m = n // 2
    acc = np.zeros(n + 1, dtype=complex)
    for eps in itertools.product((1.0, -1.0), repeat=m):
        d = np.repeat(eps, 2)
        acc += np.poly(d[:, None] * U)
    return acc / 2 ** m


def g_defect(U):
    """Max | |w| - 1 | over roots of g (z-defect is about half of this)."""
    return float(np.max(np.abs(np.abs(np.roots(g_coeffs(U))) - 1.0)))


@test
def test_01_r2_formula_and_sign_average_identity():
    """R2 + key identity: minor formula = 2^m sign average = continuous average."""
    rng = np.random.default_rng(RNG_SEED)
    worst_sign = 0.0
    for m in (2, 3, 4):
        U = haar(2 * m, rng)
        worst_sign = max(worst_sign, float(np.max(np.abs(f_coeffs(U) - sign_average_coeffs(U)))))
    # Monte Carlo continuous torus average at m = 2 (statistical check)
    m, N = 2, 20000
    U = haar(2 * m, rng)
    acc = np.zeros(2 * m + 1, dtype=complex)
    for _ in range(N):
        t = rng.uniform(0, 2 * np.pi, m)
        d = np.empty(2 * m, dtype=complex)
        d[::2] = np.exp(1j * t)
        d[1::2] = np.exp(-1j * t)
        acc += np.poly(d[:, None] * U)
    mc_err = float(np.max(np.abs(acc / N - f_coeffs(U))))
    print(f"    exact sign-average identity max err = {worst_sign:.2e}; MC (N={N}) err = {mc_err:.3f}")
    assert worst_sign < 1e-12 and mc_err < 0.06
    return True


@test
def test_02_r1_realizations_circle_rooted():
    """R1: every realization det(zI - D(theta)U) is a unitary char poly."""
    rng = np.random.default_rng(RNG_SEED + 1)
    worst = 0.0
    for m in (2, 3):
        U = haar(2 * m, rng)
        for _ in range(200):
            t = rng.uniform(0, 2 * np.pi, m)
            d = np.empty(2 * m, dtype=complex)
            d[::2] = np.exp(1j * t)
            d[1::2] = np.exp(-1j * t)
            r = np.roots(np.poly(d[:, None] * U))
            worst = max(worst, float(np.max(np.abs(np.abs(r) - 1.0))))
    print(f"    max circle defect over 400 realizations = {worst:.2e}")
    assert worst < 1e-12
    return True


@test
def test_03_r3_jacobi_self_inversive():
    """R3: Jacobi gives c_{m-k} = det(U) * conj(c_k) for the g coefficients."""
    rng = np.random.default_rng(RNG_SEED + 2)
    worst = 0.0
    for m in (2, 3, 4, 5):
        U = haar(2 * m, rng)
        c = g_coeffs(U)
        delta = np.linalg.det(U)
        for k in range(m + 1):
            worst = max(worst, float(abs(c[m - k] - delta * np.conj(c[k]))))
    print(f"    max |c_(m-k) - det(U) conj(c_k)| over m = 2..5 = {worst:.2e}")
    assert worst < 1e-11
    return True


def Q_eval(V, y):
    return complex(np.linalg.det(np.eye(V.shape[0]) + np.diag(y) @ V))


def P_eval(V, x):
    """P(x_1..x_m) = sum_T prod_{j in T} x_j det V[S_T] (multiaffine, step SP)."""
    m = V.shape[0] // 2
    s = 1.0 + 0j
    for k in range(1, m + 1):
        for T in itertools.combinations(range(m), k):
            S = [i for j in T for i in (2 * j, 2 * j + 1)]
            s += np.prod([x[j] for j in T]) * np.linalg.det(V[np.ix_(S, S)])
    return s


@test
def test_04_s0_polydisk_nonvanishing():
    """S0: Q(y) = det(I + diag(y)V) has no zero in the open polydisk (norm bound)."""
    rng = np.random.default_rng(RNG_SEED + 3)
    minmod, worst_pred = np.inf, 0.0
    for _ in range(400):
        n = int(rng.integers(2, 9))
        V = haar(n, rng)
        y = rng.uniform(0, 0.999, n) * np.exp(1j * rng.uniform(0, 2 * np.pi, n))
        q = abs(Q_eval(V, y))
        minmod = min(minmod, q)
        # eigenvalues of diag(y)V lie in |.| <= max|y_i| < 1, so |Q| >= prod(1-|lam|) > 0
        lam = np.linalg.eigvals(np.diag(y) @ V)
        worst_pred = max(worst_pred, float(np.max(np.abs(lam)) - np.max(np.abs(y))))
    print(f"    min |Q| over 400 polydisk samples = {minmod:.2e}; max (rho - max|y|) = {worst_pred:.2e}")
    assert minmod > 1e-12 and worst_pred < 1e-12
    return True


@test
def test_05_lemma_e():
    """LEMMA E: bidisk-nonvanishing multiaffine => |A| >= |C| (chain (*),(**),(**'))."""
    rng = np.random.default_rng(RNG_SEED + 4)
    worst = -np.inf  # max over samples of |C| - |A| (should stay <= 0)
    worst_chain = -np.inf
    for _ in range(600):
        m = int(rng.integers(2, 5))
        V = haar(2 * m, rng)
        j = int(rng.integers(0, m))
        y = rng.uniform(0, 0.98, 2 * m) * np.exp(1j * rng.uniform(0, 2 * np.pi, 2 * m))
        a, b = 2 * j, 2 * j + 1

        def q(u, v):
            yy = y.copy()
            yy[a], yy[b] = u, v
            return Q_eval(V, yy)

        A = q(0, 0)
        Ba = q(1, 0) - A
        Bb = q(0, 1) - A
        C = q(1, 1) - A - Ba - Bb
        worst = max(worst, abs(C) - abs(A))
        # the two Schur bounds (**) and (**') from the proof
        chain = max((abs(Ba) + abs(C)) - (abs(A) + abs(Bb)),
                    (abs(Bb) + abs(C)) - (abs(A) + abs(Ba)))
        worst_chain = max(worst_chain, chain)
        # (*): |A|^2 + |Bb|^2 - |Ba|^2 - |C|^2 >= 2|conj(A)Bb - conj(Ba)C|
        star = (abs(A) ** 2 + abs(Bb) ** 2 - abs(Ba) ** 2 - abs(C) ** 2
                - 2 * abs(np.conj(A) * Bb - np.conj(Ba) * C))
        assert star > -1e-9
    # negative control: |C| > |A| really forces a bidisk zero (content of the lemma)
    # Q(u,v) = 0.5 + uv vanishes at u = 0.9, v = -0.5/0.9, both inside the disk
    u0, v0 = 0.9, -0.5 / 0.9
    zero_val = abs(0.5 + u0 * v0)
    print(f"    max |C|-|A| = {worst:.2e}; max chain violation = {worst_chain:.2e}; "
          f"control zero |Q| = {zero_val:.1e} at |v| = {abs(v0):.3f} < 1")
    assert worst < 1e-11 and worst_chain < 1e-11 and zero_val < 1e-15
    return True


@test
def test_06_master_claim_P_nonvanishing():
    """SP: P(x) = sum_T prod_{j in T} x_j det V[S_T] != 0 on the open polydisk."""
    rng = np.random.default_rng(RNG_SEED + 5)
    minmod = np.inf
    for m in (2, 3, 4):
        for _ in range(500):
            V = haar(2 * m, rng)
            x = rng.uniform(0, 0.999, m) * np.exp(1j * rng.uniform(0, 2 * np.pi, m))
            minmod = min(minmod, abs(P_eval(V, x)))
    # adversarial: push x toward the known boundary contact (block-diagonal case)
    m = 3
    blocks = [haar(2, rng) for _ in range(m)]
    V = np.zeros((2 * m, 2 * m), dtype=complex)
    for j, B in enumerate(blocks):
        V[2 * j:2 * j + 2, 2 * j:2 * j + 2] = B
    xb = np.array([-0.999 / np.linalg.det(B) for B in blocks])  # x_j -> -1/det B_j
    near = abs(P_eval(V, xb))
    pred = abs(np.prod(1 + xb * np.array([np.linalg.det(B) for B in blocks])))
    print(f"    min |P| over 1500 samples = {minmod:.2e}; near-boundary |P| = {near:.2e}"
          f" (exact block formula {pred:.2e})")
    assert minmod > 1e-12 and abs(near - pred) < 1e-12
    return True


@test
def test_07_theorem_regression_haar():
    """THEOREM: g is circle-rooted; Haar regression m = 1..6."""
    rng = np.random.default_rng(RNG_SEED + 6)
    report = []
    for m in range(1, 7):
        worst = max(g_defect(haar(2 * m, rng)) for _ in range(300))
        report.append(f"m={m}: {worst:.1e}")
    print("    max g-root circle defect, 300 Haar samples each: " + "; ".join(report))
    assert all(float(r.split(": ")[1]) < 1e-10 for r in report)
    return True


@test
def test_08_search_m5_m6_m7():
    """STEP-1 search verdict: random + Nelder-Mead maximization finds no counterexample."""
    from scipy.linalg import expm
    from scipy.optimize import minimize
    rng = np.random.default_rng(RNG_SEED + 7)
    report = []
    overall = 0.0
    for m, nrand, nmev in ((5, 1500, 2000), (6, 1000, 1500), (7, 600, 0)):
        n = 2 * m
        worst = max(g_defect(haar(n, rng)) for _ in range(nrand))
        if nmev:
            def neg(xflat):
                H = xflat[:n * n].reshape(n, n) + 1j * xflat[n * n:].reshape(n, n)
                H = (H + H.conj().T) / 2
                return -g_defect(expm(1j * H))
            for _ in range(2):
                res = minimize(neg, rng.standard_normal(2 * n * n),
                               method="Nelder-Mead", options={"maxfev": nmev})
                worst = max(worst, -res.fun)
        # structured adversarial start: block-diagonal at the boundary det pattern + noise
        blocks = []
        for j, ph in enumerate((1.0, -1.0, -1.0) + (1.0,) * (m - 3)):
            B = haar(2, rng)
            B = B / np.sqrt(np.linalg.det(B)) * np.sqrt(complex(ph))
            blocks.append(B)
        V = np.zeros((n, n), dtype=complex)
        for j, B in enumerate(blocks):
            V[2 * j:2 * j + 2, 2 * j:2 * j + 2] = B
        K = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        worst = max(worst, g_defect(V @ expm((K - K.conj().T) * 0.05)))
        overall = max(overall, worst)
        report.append(f"m={m}: {worst:.1e}")
    print("    max defect (random + polish + boundary-perturbed): " + "; ".join(report))
    assert overall < 1e-8
    return True


@test
def test_09_boundary_case_block_diagonal():
    """Boundary contact: block-diagonal U gives g(w) = prod_j (w + det V_j) exactly."""
    rng = np.random.default_rng(RNG_SEED + 8)
    m = 3
    phases = (1.0, -1.0, -1.0)  # the deltoid-boundary det pattern from the analysis
    V = np.zeros((2 * m, 2 * m), dtype=complex)
    dets = []
    for j, ph in enumerate(phases):
        B = haar(2, rng)
        B = B / np.sqrt(np.linalg.det(B)) * np.sqrt(complex(ph))
        V[2 * j:2 * j + 2, 2 * j:2 * j + 2] = B
        dets.append(np.linalg.det(B))
    g = g_coeffs(V)
    expect = np.poly(np.array([-d for d in dets]))
    err = float(np.max(np.abs(g - expect)))
    # (w+1)(w-1)^2: a double root ON the circle (multiple roots allowed, still on |w|=1)
    r = np.sort(np.roots(g))
    print(f"    |g - prod(w + det V_j)| = {err:.2e}; roots = {np.round(r, 6)}")
    assert err < 1e-12 and float(np.max(np.abs(np.abs(r) - 1))) < 1e-8
    return True


@test
def test_10_controls_each_ingredient_load_bearing():
    """Controls: same-sign pairing collapses; equal-det averaging fails; self-inversive alone fails."""
    rng = np.random.default_rng(RNG_SEED + 9)
    m = 3
    U = haar(2 * m, rng)
    # (a) same-sign pairing diag(e^{it_j}, e^{+it_j}): E[e^{2it}] = 0 kills all content
    acc = np.zeros(2 * m + 1, dtype=complex)
    for k in range(4 ** m):  # exact via Z_4 phases per pair (degree <= 2 per phase)
        t = 2 * np.pi * np.array([(k // 4 ** j) % 4 for j in range(m)]) / 4
        d = np.repeat(np.exp(1j * t), 2)
        acc += np.poly(d[:, None] * U)
    acc /= 4 ** m
    collapse = float(np.max(np.abs(acc - np.eye(2 * m + 1)[0])))
    # (b) average of two SAME-DET unitary char polys, off-circle: (z-e^{i pi/3})^3 & conj
    p = np.poly([np.exp(1j * np.pi / 3)] * 3)
    q = np.poly([np.exp(-1j * np.pi / 3)] * 3)
    r = np.roots((p + q) / 2)
    maxmod_b = float(np.max(np.abs(r)))
    # (c) self-inversive cubic not from the construction: w^3 - 1.5w^2 - 1.5w + 1
    rc = np.sort_complex(np.roots([1, -1.5, -1.5, 1]))
    offc = float(np.max(np.abs(np.abs(rc) - 1)))
    print(f"    same-sign collapse to z^n err = {collapse:.2e}; equal-det avg max|root| = "
          f"{maxmod_b:.4f} (off-circle); self-inversive control defect = {offc:.3f}")
    assert collapse < 1e-12 and maxmod_b > 1.9 and offc > 0.9
    return True


@test
def test_11_contraction_corollary():
    """Corollary: ||V|| <= 1 => ALL g-roots in the closed disk (Schur stable); strict => inside."""
    rng = np.random.default_rng(RNG_SEED + 10)
    maxmod, minmod = 0.0, np.inf
    for m in (2, 3):
        for _ in range(300):
            V = 0.8 * haar(2 * m, rng)
            r = np.abs(np.roots(g_coeffs(V)))
            maxmod = max(maxmod, float(np.max(r)))
            minmod = min(minmod, float(np.min(r)))
    # 0.8*U scales every pair minor by 0.8^2 and det U[S_T] by 0.8^{2|T|}:
    # g_{0.8U}(w) = 0.8^{2m} g_U(w/0.64), so roots sit exactly at modulus 0.64.
    print(f"    contraction 0.8*U: max |g-root| = {maxmod:.4f} (<= 1), min = {minmod:.4f}"
          f" (= 0.8^2, strictly inside)")
    assert maxmod < 1 + 1e-9 and abs(minmod - 0.64) < 1e-9
    return True


@test
def test_12_mpmath_high_precision():
    """Exactness at 50 digits: exact-unitary Cayley U, g-roots on the circle to ~1e-45."""
    from mpmath import mp
    mp.dps = 50
    m = 3
    n = 2 * m
    rng = np.random.default_rng(RNG_SEED + 11)
    A = rng.integers(-9, 10, (n, n))
    B = rng.integers(-9, 10, (n, n))
    H = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            H[i, j] = (mp.mpf(int(A[i, j] + A[j, i])) + 1j * mp.mpf(int(B[i, j] - B[j, i]))) / 10
    I = mp.eye(n)
    U = (I + 1j * H) * (I - 1j * H) ** -1  # Cayley: exactly unitary
    uerr = max(abs((U * U.transpose_conj())[i, j] - (1 if i == j else 0))
               for i in range(n) for j in range(n))
    coeffs = [mp.mpc(1)]
    for k in range(1, m + 1):
        s = mp.mpc(0)
        for T in itertools.combinations(range(m), k):
            S = [x for j in T for x in (2 * j, 2 * j + 1)]
            sub = mp.matrix([[U[a, b] for b in S] for a in S])
            s += mp.det(sub)
        coeffs.append(s)
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=100)
    defect = max(abs(abs(r) - 1) for r in roots)
    print(f"    unitarity residual = {mp.nstr(uerr, 3)}; g-root circle defect = {mp.nstr(defect, 3)}")
    assert uerr < mp.mpf('1e-45') and defect < mp.mpf('1e-40')
    return True


if __name__ == "__main__":
    print(__doc__.splitlines()[0])
    npass = 0
    for i, fn in enumerate(TESTS, 1):
        print(f"Test {i:2d}: {fn.__name__}")
        print(f"    {fn.__doc__.strip().splitlines()[0]}")
        ok = fn()
        npass += bool(ok)
        print(f"    -> {'PASS' if ok else 'FAIL'}")
    print(f"\npaired_subtorus: {npass}/{len(TESTS)} tests passed")

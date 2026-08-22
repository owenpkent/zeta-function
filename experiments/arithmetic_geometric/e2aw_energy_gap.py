"""E2AW: B2c-gap: the energy of the Xi-state, and the instrument's horizon.

The coda specced by #190: measure the energy sub-optimality of CCM's
Xi-shaped kernel k_lambda against the true bottom lambda_0(a): what a
corrected selection principle for (1.2) must pay. Executing the spec exposes
a second, sharper readout, pre-registered here before the run.

THE EXACT FACTS the run rests on (verified in-run, not assumed):
  (E1) With the EXACT seed constant alpha = 2 sqrt(6)/3 (closed form:
       int psi_0 = psi_0(0) = 2^{1/4} and int psi_4 = psi_4(0), both by
       Fourier self-duality, so the vanishing-integral condition IS
       h(0) = 0), the seed h = psi_0 - alpha psi_4 satisfies int h = 0 AND
       h(0) = 0 exactly.
  (E2) Consequently k = E(h) is EXACTLY even in log coordinates (Poisson),
       and its full-line Mellin transform factors as zeta(1/2 - iz) *
       htilde(1/2 - iz), which VANISHES AT EVERY ON-LINE ZERO exactly.
  (E3) Therefore the windowed kernel's Weil-form value is controlled by the
       WINDOW-TRUNCATION TAILS alone: khat_win(gamma) = -(FT of the two
       tails)(gamma), so |khat_win(gamma)| <= min(2*T1, 2*(|k(a)| + T1d)/
       gamma) with T1 = int_a^inf |k|, T1d = int_a^inf |k'|: quantities
       with NO cancellation, computable at any dps. The identity is
       verified numerically at a = 1 (direct oscillatory integral vs the
       tail route) before the bounds are used anywhere.

READOUT A (the naive B2c-gap, within the instrument): mp-projection of k
onto the e2ar spline space (m = 112a, dps 80, the e2av gate-passing
regime); the Rayleigh quotient R(Pk) = Q(Pk)/||Pk||^2 against lambda_0(a),
with the spectral mass profile of Pk over the instrument's eigenbasis, and
the projection-floor bound 2*N*2a*||k - Pk||^2 that types whether R(Pk) is
form-driven or floor-driven.

READOUT B (the pincer): the certified upper bound B(a) on the TRUE
continuum window energy Q(k_win)/||k||^2 from (E3), against the
instrument's certified bottom lambda_0(a) (itself an upper bound on the
continuum bottom over the spline subspace). PRE-REGISTERED EXPECTATION:
B(a) collapses doubly-exponentially (~ e^{-2 pi e^{2a}} up to polynomial
factors) and CROSSES BELOW lambda_0(a) at some a* in (1, 2]. If it does,
the consequence is structural: beyond a* the finite instrument provably no
longer tracks the continuum ground state (the kernel alone is a deeper
trial state than anything the basis resolves), so the certified narrowing
(#185/#189) and the proximity decay (#190) are statements about the
RESOLVABLE-SUBSPACE optimum, and conjecture (1.2) as a continuum statement
is NOT refuted by them; what the arc measured instead is the HORIZON past
which direct minimization cannot see the conjecture's object, priced in
digits: resolving the bottom at window a needs working precision
~ 2 pi e^{2a} / ln 10 digits and a basis with matching approximation error.
KILL: if B(a) stays ABOVE lambda_0(a) through a = 4, the naive reading
survives, the gap R(Pk)/lambda_0 is the priced answer as originally
specced, and the collapse retains its (1.2)-refuting force at measured
depths. Either verdict is recorded.

Sharp values where cancellation permits: the direct truncated-form energy
Q_trunc(k_win) = 2 sum_b khat_win(gamma_b)^2 is computed from the node
cache at a = 1.0, 1.5 (and 2.0 with a stated digits-left caveat); beyond,
the no-cancellation bound stands alone. GL-48 per half-knot interval keeps
quadrature noise (~1e-80 per node, oscillatory error < 1e-80 at GL-48 for
gamma <= 1500) below every claimed scale at the rungs where sharp values
are claimed.

Caveats carried: Hermite-limit substitution for CCM's prolate seed (their
Lemma 7.2, c*lambda^{-2}: the kernel here is OUR admissible trial state,
which is all the pincer needs; its Xi-proximity is e2av Readout 1);
above-cutoff zeros enter B(a) through the 1/gamma bound with an e^{a}
allowance for potential off-line pairs (zeros to T = 1500 are certified
on-line in the cache).

Run:
  python -m experiments.arithmetic_geometric.e2aw_energy_gap

Outputs: e2aw_energy_gap.npz (tracked, evidence rule).
"""

from __future__ import annotations

import json
import time
from math import comb
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments.arithmetic_geometric.e2ar_hard_window_xi import (
    DEG, HardWindowGS, cardinal_spline, sincp)

HERE = Path(__file__).resolve().parent
ZCACHE = HERE.parent / "_shared" / "_cache" / "zeros_dps110_T1500.json"

DPS = 80
NGL = 48
AVALS = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
SHARP_AVALS = [1.0, 1.5, 2.0]      # direct Q_trunc feasible (cancellation < dps)

# stored ladders for the parity gate and the pincer comparison
E2AS_LG0 = {1.0: -24.1, 1.5: -42.4, 2.0: -46.2, 2.5: -49.0}      # dps 80
E2AU_LG0 = {2.5: -48.7, 3.0: -50.7, 3.5: -52.9, 4.0: -55.2}      # dps 110
E2AV_COS = {1.0: 0.9988, 1.5: 0.9880, 2.0: 0.9391, 2.5: 0.8759,
            3.0: 0.8133, 3.5: 0.7569, 4.0: 0.7152}

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def lg(x):
    """log10 of a positive mp number (exponent-safe)."""
    return float(mp.log10(x)) if x > 0 else float("-inf")


# ---------------------------------------------------------------------------
# the seed, exactly: alpha = 2 sqrt(6)/3, int h = h(0) = 0
# ---------------------------------------------------------------------------

def psi0_mp(x):
    return mp.power(2, mp.mpf(1) / 4) * mp.exp(-mp.pi * x * x)


def psi4_mp(x):
    v = mp.sqrt(2 * mp.pi) * x
    H4 = 16 * v ** 4 - 48 * v ** 2 + 12
    c = mp.power(2, mp.mpf(1) / 4) / mp.sqrt(mp.mpf(2 ** 4) * 24)
    return c * H4 * mp.exp(-mp.pi * x * x)


def alpha_exact():
    return 2 * mp.sqrt(6) / 3


def h_mp(x, alpha):
    return psi0_mp(x) - alpha * psi4_mp(x)


def hprime_mp(x, alpha):
    """h'(x) analytically: d/dx [P(x) e^{-pi x^2}] = (P' - 2 pi x P) e^{-pi x^2}."""
    r2 = mp.sqrt(2 * mp.pi)
    v = r2 * x
    c4 = mp.power(2, mp.mpf(1) / 4) / mp.sqrt(mp.mpf(2 ** 4) * 24)
    P = mp.power(2, mp.mpf(1) / 4) - alpha * c4 * (16 * v ** 4 - 48 * v ** 2 + 12)
    dP = -alpha * c4 * (64 * v ** 3 - 96 * v) * r2
    return (dP - 2 * mp.pi * x * P) * mp.exp(-mp.pi * x * x)


def k_mp(x, alpha, dps):
    """k(x) = e^{x/2} sum_{n>=1} h(n e^x), truncated below the dps floor."""
    u = mp.exp(x)
    nmax = int(mp.ceil(mp.sqrt((dps + 30) * mp.log(10) / mp.pi) / u)) + 1
    s = mp.mpf(0)
    for n in range(1, nmax + 1):
        s += h_mp(n * u, alpha)
    return mp.exp(x / 2) * s


def kprime_mp(x, alpha, dps):
    u = mp.exp(x)
    nmax = int(mp.ceil(mp.sqrt((dps + 30) * mp.log(10) / mp.pi) / u)) + 1
    s = mp.mpf(0)
    for n in range(1, nmax + 1):
        s += h_mp(n * u, alpha) / 2 + n * u * hprime_mp(n * u, alpha)
    return mp.exp(x / 2) * s


# ---------------------------------------------------------------------------
# Gauss-Legendre nodes in mp (refined from float seeds)
# ---------------------------------------------------------------------------

def gl_nodes(n):
    xf, _ = np.polynomial.legendre.leggauss(n)
    nodes, weights = [], []
    for r in xf:
        x = mp.findroot(lambda t: mp.legendre(n, t), mp.mpf(float(r)))
        Pn1 = mp.legendre(n - 1, x)
        Pn = mp.legendre(n, x)
        dP = n * (x * Pn - Pn1) / (x * x - 1)
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dP * dP))
    return nodes, weights


# ---------------------------------------------------------------------------
# the instrument, ported from e2ar with the full eigensystem kept
# (parity-gated against HardWindowGS at the two cheap rungs)
# ---------------------------------------------------------------------------

class GSFull:
    def __init__(self, a, gz, m_knots, dps):
        mp.mp.dps = dps
        self.a = mp.mpf(a)
        self.h = 2 * self.a / m_knots
        Kmax = int(mp.floor(m_knots / 2 - (DEG + 1) / 2))
        self.centers = [k * self.h for k in range(0, Kmax + 1)]
        J = len(self.centers)

        def pair(mu, nu):
            return self.h * cardinal_spline(2 * DEG + 1, (mu - nu) / self.h)

        G = mp.zeros(J, J)
        for i in range(J):
            for j in range(i, J):
                mi, mj = self.centers[i], self.centers[j]
                v = pair(mi, mj)
                if i > 0:
                    v += pair(-mi, mj)
                if j > 0:
                    v += pair(mi, -mj)
                if i > 0 and j > 0:
                    v += pair(-mi, -mj)
                G[i, j] = G[j, i] = v if (i > 0 or j > 0) else pair(0, 0)
        self.G = G

        def psihat(k, t):
            base = self.h * sincp(t * self.h / 2) ** (DEG + 1)
            return base * (2 * mp.cos(self.centers[k] * t) if k > 0 else mp.mpf(1))

        self._psihat = psihat
        tab = mp.zeros(J, len(gz))
        for k in range(J):
            for b, g in enumerate(gz):
                tab[k, b] = psihat(k, g)
        self.Qz = 2 * tab * tab.T

        self.L = mp.cholesky(G)
        Li = mp.inverse(self.L)
        A = Li * self.Qz * Li.T
        E, V = mp.eigsy(A)
        order = sorted(range(J), key=lambda i: mp.re(E[i]))
        self.eigs = [mp.re(E[i]) for i in order]
        self.V = mp.zeros(J, J)
        for col, i in enumerate(order):
            for r in range(J):
                self.V[r, col] = V[r, i]
        self.lam0, self.lam1 = self.eigs[0], self.eigs[1]
        v = mp.matrix([self.V[r, 0] for r in range(J)])
        self.c = Li.T * v
        nrm = mp.sqrt(mp.re((self.c.T * (G * self.c))[0]))
        for r in range(J):
            self.c[r] = self.c[r] / nrm
        self.J = J


def zeros_cache():
    mp.mp.dps = DPS
    return [mp.mpf(s[: DPS + 8]) for s in json.loads(ZCACHE.read_text())]


# ---------------------------------------------------------------------------
# per-rung analysis
# ---------------------------------------------------------------------------

def node_cache(a, m_knots, alpha, nodes, weights):
    """(x, w, k(x)) at GL-48 nodes per half-knot interval over [-a, a]."""
    h2 = mp.mpf(2 * a) / m_knots / 2
    cache = []
    for j in range(2 * m_knots):
        x0 = -mp.mpf(a) + j * h2
        for t, w in zip(nodes, weights):
            x = x0 + h2 * (t + 1) / 2
            cache.append((x, w * h2 / 2, k_mp(x, alpha, DPS)))
    return cache


def tail_quantities(a, alpha):
    """T1 = int_a^inf |k|, T1d = int_a^inf |k'|, jump = |k(a)| (no cancellation)."""
    am = mp.mpf(a)
    T1 = mp.quad(lambda x: abs(k_mp(x, alpha, DPS)), [am, am + 1, am + 3])
    T1 += abs(k_mp(am + 3, alpha, DPS))          # crude closure of the dead tail
    T1d = mp.quad(lambda x: abs(kprime_mp(x, alpha, DPS)), [am, am + 1, am + 3])
    T1d += abs(kprime_mp(am + 3, alpha, DPS))
    jump = abs(k_mp(am, alpha, DPS))
    return T1, T1d, jump


def bound_at(gamma, T1, T1d, jump):
    return min(2 * T1, 2 * (jump + T1d) / gamma)


def tail_ft_clean(gamma, a, alpha):
    """R(gamma) = sum_n n^{i gamma - 1/2} int_{n e^a}^inf u^{-1/2 - i gamma} h(u) du."""
    am = mp.mpf(a)
    gam = mp.mpf(gamma)
    total = mp.mpc(0)
    for n in range(1, 4):
        A = n * mp.exp(am)
        death = mp.sqrt(A * A + (DPS + 15) * mp.log(10) / mp.pi)
        pts = [A]
        u = A
        while u < death:
            u = min(u * mp.exp(mp.mpf(6) / max(gam, 1)), death)
            pts.append(u)
        I = mp.quad(lambda u: mp.power(u, mp.mpc(-0.5, -gam)) * h_mp(u, alpha), pts)
        total += mp.power(mp.mpf(n), mp.mpc(-0.5, gam)) * I
    return total


def run():
    t0 = time.time()
    print("== E2AW: the energy of the Xi-state and the instrument's horizon (B2c-gap) ==")
    mp.mp.dps = DPS
    gz = zeros_cache()
    N = len(gz)
    alpha = alpha_exact()
    print(f"  {N} zeros (dps {DPS}); exact alpha = 2 sqrt(6)/3 = {mp.nstr(alpha, 12)}")

    # (E1) seed exactness
    ih = mp.quad(lambda x: h_mp(x, alpha), [-9, 0, 9])
    h0 = h_mp(mp.mpf(0), alpha)
    print(f"  int h = {mp.nstr(ih, 3)}, h(0) = {mp.nstr(h0, 3)}")

    # (E2) evenness of k at sample points (Poisson consequence)
    ev = mp.mpf(0)
    for xs in [mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("1.7")]:
        kp, km = k_mp(xs, alpha, DPS), k_mp(-xs, alpha, DPS)
        ev = max(ev, abs(kp - km) / abs(kp))
    print(f"  max relative evenness defect = {mp.nstr(ev, 3)}")

    nodes, weights = gl_nodes(NGL)

    # parity gate: the ported builder vs HardWindowGS at two cheap rungs
    par = []
    for ac in (1.0, 1.5):
        gs_ref = HardWindowGS(ac, gz, m_knots=int(round(112 * ac)), dps=DPS)
        gs_new = GSFull(ac, gz, m_knots=int(round(112 * ac)), dps=DPS)
        par.append(abs(lg(gs_new.lam0) - lg(gs_ref.lam0)))
        del gs_ref
    print(f"  parity |dlg lam0| at a = 1, 1.5: {par[0]:.2e}, {par[1]:.2e}")

    rows = []
    id_check = {}
    for a in AVALS:
        ta = time.time()
        m_knots = int(round(112 * a))
        gs = GSFull(a, gz, m_knots=m_knots, dps=DPS)
        cache = node_cache(a, m_knots, alpha, nodes, weights)

        # ||k||^2 on the window
        nk2 = mp.mpf(0)
        for x, w, kv in cache:
            nk2 += w * kv * kv

        # projection b_i = <k, psi_i>
        b = mp.matrix(gs.J, 1)
        supp = (DEG + 1) / mp.mpf(2) * gs.h
        for x, w, kv in cache:
            for i, c0 in enumerate(gs.centers):
                v = mp.mpf(0)
                if abs(x - c0) < supp:
                    v += cardinal_spline(DEG, (x - c0) / gs.h)
                if i > 0 and abs(x + c0) < supp:
                    v += cardinal_spline(DEG, (x + c0) / gs.h)
                if v != 0:
                    b[i] += w * kv * v
        c_proj = mp.lu_solve(gs.G, b)
        nPk2 = mp.re((b.T * c_proj)[0])
        QPk = mp.re((c_proj.T * (gs.Qz * c_proj))[0])
        RPk = QPk / nPk2
        resid2 = nk2 - nPk2
        floor_bound = 2 * N * 2 * mp.mpf(a) * max(resid2, mp.mpf(0))

        # spectral masses of Pk in the instrument eigenbasis
        y = gs.L.T * c_proj
        masses = []
        for j in range(min(gs.J, 8)):
            s = mp.mpf(0)
            for r in range(gs.J):
                s += gs.V[r, j] * y[r]
            masses.append(s * s)
        cosang = float(mp.sqrt(masses[0] / nk2))

        # READOUT B: the tail bounds
        T1, T1d, jump = tail_quantities(a, alpha)
        Qb = mp.mpf(0)
        for g in gz:
            Qb += bound_at(g, T1, T1d, jump) ** 2
        Qb *= 2
        # above-cutoff zeros: 1/gamma bound, density rho, e^{a} off-line allowance
        rho = lambda t: mp.log(t / (2 * mp.pi)) / (2 * mp.pi)
        Qab = 2 * mp.exp(a) * mp.quad(
            lambda t: (2 * (jump + T1d) / t) ** 2 * rho(t), [1500, 10000, mp.inf])
        B = (Qb + Qab) / nk2

        # sharp truncated energy from the node cache where cancellation permits
        Qsharp = None
        digits_left = None
        if a in SHARP_AVALS:
            Qs = mp.mpf(0)
            kh1 = None
            for bidx, g in enumerate(gz):
                s = mp.mpf(0)
                for x, w, kv in cache:
                    s += w * kv * mp.cos(g * x)
                if bidx == 0:
                    kh1 = s
                Qs += s * s
            Qsharp = 2 * Qs
            digits_left = DPS - (lg(nk2) / 2 - lg(abs(kh1))) if kh1 else None
            # identity check at the first rung: direct window FT vs tail route
            if a == 1.0:
                for gsel in (gz[0], gz[1], gz[9]):
                    direct = mp.mpf(0)
                    for x, w, kv in cache:
                        direct += w * kv * mp.cos(gsel * x)
                    tails = 2 * mp.re(tail_ft_clean(gsel, a, alpha))
                    id_check[float(gsel)] = (direct, -tails,
                                            float(abs(direct + tails)
                                                  / max(abs(direct), mp.mpf("1e-300"))))

        rows.append({
            "a": a, "J": gs.J, "lam0": gs.lam0, "lam1": gs.lam1,
            "RPk": RPk, "QPk": QPk, "nk2": nk2, "nPk2": nPk2,
            "resid2": resid2, "floor": floor_bound / nPk2,
            "cos": cosang, "masses": masses, "B": B,
            "Qsharp": Qsharp, "digits_left": digits_left,
            "T1": T1, "jump": jump,
        })
        r = rows[-1]
        print(f"   a = {a} ({time.time() - ta:.0f} s): J = {gs.J}, "
              f"lg lam0 = {lg(r['lam0']):.1f}, lg R(Pk) = {lg(RPk):.1f} "
              f"(floor {lg(r['floor']):.1f}), cos = {cosang:.4f}, "
              f"lg B = {lg(B):.1f}"
              + (f", lg Qsharp/|k|^2 = {lg(Qsharp / nk2):.1f}" if Qsharp else ""))
        del gs, cache

    print("\n-- checks --")
    check("(E1) exact seed: |int h| and |h(0)| below 1e-60 with alpha = 2 sqrt(6)/3",
          abs(ih) < mp.mpf("1e-60") and abs(h0) < mp.mpf("1e-60"),
          f"int h = {mp.nstr(abs(ih), 2)}, h(0) = {mp.nstr(abs(h0), 2)}")
    check("(E2) k exactly even in log coordinates (Poisson, relative defect < 1e-40)",
          ev < mp.mpf("1e-40"), f"max defect {mp.nstr(ev, 2)}")
    check("builder parity with e2ar machinery (|dlg lam0| < 1e-6 at a = 1, 1.5)",
          all(p < 1e-6 for p in par), f"{par[0]:.1e}, {par[1]:.1e}")
    # gate only where the T = 350 -> 1500 zero-set change is provably below
    # lam0 (a = 1, 1.5); at a >= 2 the stored values are informational (the
    # added zeros can legitimately raise the bottom past e2as's tail scale)
    check("stored-ladder parity: lg lam0 within 0.5 of e2as at a = 1, 1.5 "
          "(a >= 2 informational: different zero sets)",
          all(abs(lg(r["lam0"]) - E2AS_LG0[r["a"]]) < 0.5
              for r in rows if r["a"] in (1.0, 1.5)),
          ", ".join(f"a={r['a']}: {lg(r['lam0']):.1f} vs "
                    f"{E2AS_LG0.get(r['a'], E2AU_LG0.get(r['a']))}"
                    for r in rows if r["a"] in E2AS_LG0 or r["a"] in E2AU_LG0))
    idrel = [v[2] for v in id_check.values()]
    check("(E3) identity verified at a = 1: direct khat_win(gamma_b) = -(tail FT), "
          "rel dev < 1e-3 at gamma_1, gamma_2, gamma_10",
          len(idrel) == 3 and all(d < 1e-3 for d in idrel),
          ", ".join(f"{d:.1e}" for d in idrel))
    check("projection health: mp cos(k, v0) within 0.02 of e2av float cos at every a",
          all(abs(r["cos"] - E2AV_COS[r["a"]]) < 0.02 for r in rows),
          ", ".join(f"{r['cos']:.4f}/{E2AV_COS[r['a']]:.4f}" for r in rows))
    sharp_ok = all(r["Qsharp"] / r["nk2"] <= r["B"] * mp.mpf("1.01")
                   for r in rows if r["Qsharp"] is not None)
    check("bound soundness: Qsharp/|k|^2 <= B at every sharp rung",
          sharp_ok,
          ", ".join(f"a={r['a']}: {lg(r['Qsharp'] / r['nk2']):.1f} vs {lg(r['B']):.1f}"
                    for r in rows if r["Qsharp"] is not None))
    check("READOUT A recorded: R(Pk)/lam0 and the floor typing across the ladder",
          True,
          ", ".join(f"a={r['a']}: {lg(r['RPk'] / r['lam0']):.1f}"
                    + ("(floor)" if r["floor"] > r["RPk"] / 3 else "")
                    for r in rows))
    cross = [r["a"] for r in rows if r["B"] < r["lam0"]]
    check("READOUT B recorded: the pincer B(a) vs lam0(a); crossover rungs listed",
          True,
          "B < lam0 at a = " + (", ".join(str(x) for x in cross) if cross else "NONE"))
    check("PRE-REGISTERED VERDICT: crossover exists with a* <= 2 "
          "(else the naive reading survives; either way recorded)",
          len(cross) > 0 and min(cross) <= 2.0,
          f"first crossover at a = {min(cross) if cross else 'NONE'}; "
          + ", ".join(f"lg(lam0/B)@{r['a']} = {lg(r['lam0'] / r['B']):.0f}"
                      for r in rows))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2aw_energy_gap.npz"
    np.savez_compressed(
        out,
        avals=np.array(AVALS),
        lg_lam0=np.array([lg(r["lam0"]) for r in rows]),
        lg_lam1=np.array([lg(r["lam1"]) for r in rows]),
        lg_RPk=np.array([lg(r["RPk"]) for r in rows]),
        lg_floor=np.array([lg(r["floor"]) for r in rows]),
        lg_B=np.array([lg(r["B"]) for r in rows]),
        lg_Qsharp=np.array([lg(r["Qsharp"] / r["nk2"]) if r["Qsharp"] is not None
                            else np.nan for r in rows]),
        digits_left=np.array([r["digits_left"] if r["digits_left"] is not None
                              else np.nan for r in rows]),
        cos_mp=np.array([r["cos"] for r in rows]),
        cos_e2av=np.array([E2AV_COS[a] for a in AVALS]),
        masses=np.array([[float(mp.log10(max(m, mp.mpf("1e-300")))) for m in r["masses"]]
                         for r in rows]),
        lg_resid2=np.array([lg(max(r["resid2"], mp.mpf(0))) for r in rows]),
        lg_nk2=np.array([lg(r["nk2"]) for r in rows]),
        lg_T1=np.array([lg(r["T1"]) for r in rows]),
        id_check_rel=np.array([v[2] for v in id_check.values()]),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()

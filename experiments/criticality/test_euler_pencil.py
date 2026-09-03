"""Fast gates for the Euler pencil experiment (e_euler_pencil.py).

Standalone module (not pytest): main() prints "N/N passed" per the repo
convention. Target: under 90 s total.
"""

from __future__ import annotations

import time

import mpmath as mp

from experiments._shared.harness import Gates
from experiments._shared.epstein_zeta import epstein_for_discriminant
from experiments.criticality.e_euler_pencil import (
    kronecker, EulerPencil, count_rect, count_line, offline_zeros,
    lehmer_prediction, track_pair, _get_char, _dirichlet_L_mpmath,
    _precise_evaluate,
)


def main():
    t0 = time.time()
    gates = Gates()
    mp.mp.dps = 30

    # ---- G1: Kronecker tables ----
    ok = (
        [kronecker(-3, n) for n in range(1, 4)] == [1, -1, 0]
        and [kronecker(-4, n) for n in range(1, 5)] == [1, 0, -1, 0]
        and [kronecker(5, n) for n in range(1, 6)] == [1, -1, -1, 1, 0]
        and [kronecker(8, n) for n in range(1, 9)] == [1, 0, -1, 0, -1, 0, 1, 0]
    )
    gates.gate("G1a: hard-coded Kronecker periods (d=-3,-4,5,8)", ok)
    prod_ok = all(
        kronecker(-15, n) == kronecker(-3, n) * kronecker(5, n) for n in range(1, 31)
    )
    gates.gate("G1b: chi_-15 = chi_-3 * chi_5 pointwise on 1..30", prod_ok)

    # ---- G2: backend vs mpmath Hurwitz agreement ----
    backend = "flint"
    try:
        import flint  # noqa: F401
        s = mp.mpc(mp.mpf("0.7"), mp.mpf("30"))
        chi = _get_char(-15)
        prev = flint.ctx.dps
        flint.ctx.dps = 25
        try:
            a_s = flint.acb(float(s.real), float(s.imag))
            from experiments.criticality.e_euler_pencil import _acb_to_mpc
            L_flint = _acb_to_mpc(chi.l(a_s))
        finally:
            flint.ctx.dps = prev
        L_mp = _dirichlet_L_mpmath(-15, s)
        rel = abs(L_flint - L_mp) / abs(L_mp)
        gates.gate("G2: flint vs mpmath L(0.7+30i, chi_-15) agree to 1e-12",
                   rel < 1e-12, f"rel={float(rel):.2e}")
    except ImportError:
        gates.skip("G2: flint vs mpmath agreement", "python-flint not installed")

    # ---- G3: f_{+1}, f_{-1} vs the Chowla-Selberg Epstein module ----
    eps_p = epstein_for_discriminant(15, principal=True)    # (1,1,4)
    eps_np = epstein_for_discriminant(15, principal=False)  # (2,1,2)
    p1 = EulerPencil(d=-15, lam=1.0, backend="mpmath")
    pm1 = EulerPencil(d=-15, lam=-1.0, backend="mpmath")
    g3_ok = True
    g3_detail = []
    for s in (mp.mpc(mp.mpf("0.75"), mp.mpf("20")), mp.mpc(mp.mpf("0.6"), mp.mpf("45"))):
        rel_p = abs(p1.evaluate(s) - eps_p.evaluate(s)) / abs(eps_p.evaluate(s))
        rel_np = abs(pm1.evaluate(s) - eps_np.evaluate(s)) / abs(eps_np.evaluate(s))
        g3_detail.append(f"s={complex(s)}: rel_p={float(rel_p):.2e} rel_np={float(rel_np):.2e}")
        if rel_p >= 1e-9 or rel_np >= 1e-9:
            g3_ok = False
    gates.gate(
        "G3: lam=+1 <-> Epstein(1,1,4) [principal, sum A+B]; "
        "lam=-1 <-> Epstein(2,1,2) [non-principal, diff A-B]; agree to 1e-9",
        g3_ok, "; ".join(g3_detail),
    )

    # ---- G4: functional equation residual ----
    s4 = mp.mpc(mp.mpf("0.8"), mp.mpf("37"))
    g4_ok = True
    g4_detail = []
    for lam in (0.0, 0.3, 1.0, -0.5):
        p = EulerPencil(d=-15, lam=lam, backend="mpmath")
        L_s = p.completed(s4)
        L_1ms = p.completed(1 - s4)
        rel = abs(L_s - L_1ms) / abs(L_s)
        g4_detail.append(f"lam={lam}: rel={float(rel):.2e}")
        if rel >= 1e-12:
            g4_ok = False
    gates.gate("G4: |Lambda(s) - Lambda(1-s)| / |Lambda(s)| < 1e-12 at s=0.8+37i",
               g4_ok, "; ".join(g4_detail))

    # ---- G5: Z_lam(t) real ----
    g5_ok = True
    g5_detail = []
    for t in (20.5, 61.3):
        for lam in (0.3, 1.0):
            p = EulerPencil(d=-15, lam=lam, backend="mpmath")
            val = p.completed(mp.mpc(mp.mpf(1) / 2, t))
            rel = abs(val.imag) / abs(val.real) if val.real != 0 else abs(val.imag)
            g5_detail.append(f"t={t},lam={lam}: rel_im={float(rel):.2e}")
            if rel >= 1e-12:
                g5_ok = False
    gates.gate("G5: Z_lam(t) real to 1e-12 relative", g5_ok, "; ".join(g5_detail))

    # ---- G6: lam=0 on [10,60] ----
    p0 = EulerPencil(d=-15, lam=0.0, backend="flint")
    n_line0, _ = count_line(p0, 10.0, 60.0, step=0.02)
    n_rect0 = count_rect(p0, 10.0, 60.0)
    zeta_n = int(mp.nzeros(60) - mp.nzeros(10))

    class _LOnly:
        """Z(t) for L(s, chi_-15) ALONE, completed with chi_-15's OWN
        functional equation -- NOT the pencil's shared Gamma(s) factor.

        chi_-15 is odd (d < 0), so its natural completion is the standard
        one for an odd real primitive character (dirichlet_l.py's
        convention): Lambda_L(s) = (q/pi)^{(s+1)/2} Gamma((s+1)/2) L(s,chi).
        Using the PENCIL's Gamma(s) factor here instead (an earlier version
        of this gate did) silently computes something else: Re(pref * L)
        picks up spurious zero-crossings wherever pref*L is merely
        imaginary, not only at genuine zeros of L, which is why that
        version gave L_n == n_line0 exactly (not a coincidence worth
        trusting -- a symptom of counting the wrong function).
        """
        def Z(self, t):
            import flint
            s = mp.mpc(mp.mpf(1) / 2, t)
            q, a = 15, 1  # conductor 15, ODD parity
            pref = mp.power(q / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2)
            flint.ctx.dps = 25
            L_val = _get_char(-15).l(flint.acb(0.5, t))
            L_mp = mp.mpc(float(L_val.real.mid()), float(L_val.imag.mid()))
            return float((pref * L_mp).real)

    L_n, _ = count_line(_LOnly(), 10.0, 60.0, step=0.02)
    gates.gate("G6a: lam=0 count_rect == count_line on [10,60]",
               n_rect0 == n_line0, f"rect={n_rect0} line={n_line0}")
    gates.gate("G6b: count_line == zeta zeros + L(chi_-15)-alone zeros on [10,60]",
               n_line0 == zeta_n + L_n,
               f"line={n_line0} zeta_n={zeta_n} L_n={L_n}")

    # ---- G7: lam=1 window containing the lowest off-line pair ----
    p1f = EulerPencil(d=-15, lam=1.0, backend="flint")
    n_line7, _ = count_line(p1f, 11.0, 21.0, step=0.02)
    n_rect7 = count_rect(p1f, 11.0, 21.0)
    off7 = offline_zeros(p1f, 11.0, 21.0)
    diff7 = n_rect7 - n_line7
    gates.gate("G7: lam=1, window [11,21]: rect-line even and equals 2*located off-line zeros",
               diff7 % 2 == 0 and diff7 == 2 * len(off7),
               f"rect={n_rect7} line={n_line7} diff={diff7} located={len(off7)}")

    # ---- G8: regression, lowest off-line zero of f_{+1}, d=-15 ----
    # Located by the full offline_zeros scan of window [11,21] (2026 run):
    # beta = 0.80001099, gamma = 12.03859863 (8 significant digits).
    seed = mp.mpc(mp.mpf("0.80001099"), mp.mpf("12.03859863"))
    root8 = mp.findroot(lambda z: _precise_evaluate(-15, 1.0, z), seed,
                         tol=mp.mpf(10) ** -40, maxsteps=100)
    resid8 = abs(_precise_evaluate(-15, 1.0, root8))
    beta8 = float(root8.real)
    gates.gate("G8: regression -- lowest off-line zero of f_{+1} (d=-15) refines to |f|<1e-18",
               resid8 < 1e-18 and (beta8 - 0.5) > 1e-3,
               f"beta={beta8:.8f} gamma={float(root8.imag):.8f} resid={float(resid8):.2e}")

    # ---- G9: tracked/forward-tested pair vs the Lehmer-pair prediction ----
    # A close on-line pair of Z_0 near t~75.7 (delta ~ 0.01), located by the
    # full run's S3 sweep (ratio 1.002 there). NOT the even-closer pair at
    # t~48.004 (delta ~ 0.002): that one is a genuine, separately-reported
    # finding (S3's own model-check flags it) that the model's finite-
    # difference curvature estimate (h = 1e-3 in lehmer_prediction) becomes
    # unreliable once delta approaches h itself, giving a ~200x-off lam_pred
    # there. This pair's delta is safely above that regime, so the gate
    # tests the model in the domain it is meant to hold, not its known edge
    # case.
    t1_g9, t2_g9 = 75.695, 75.705
    pencil0_g9 = EulerPencil(d=-15, lam=0.0, backend="flint")
    pencilB_g9 = EulerPencil(d=-15, lam=1.0, backend="flint")
    t_m9, delta9, lam_pred9 = lehmer_prediction(pencil0_g9, pencilB_g9, t1_g9, t2_g9)

    def _n_on(lam_val):
        p = EulerPencil(d=-15, lam=lam_val, backend="flint")
        cnt, _ = count_line(p, max(1e-3, t_m9 - delta9), t_m9 + delta9, step=0.0005)
        return cnt

    n_base9 = _n_on(0.0)
    lo9, hi9 = 0.0, lam_pred9
    tries = 0
    while _n_on(hi9) == n_base9 and tries < 10:
        hi9 *= 2
        tries += 1
    for _ in range(40):
        mid9 = (lo9 + hi9) / 2
        if _n_on(mid9) == n_base9:
            lo9 = mid9
        else:
            hi9 = mid9
        if abs(hi9 - lo9) < 1e-4 * max(abs(hi9), 1e-12):
            break
    lam_c9 = (lo9 + hi9) / 2
    ratio9 = lam_c9 / lam_pred9 if lam_pred9 != 0 else float("nan")
    sign_ok9 = (lam_pred9 != 0) and ((lam_c9 > 0) == (lam_pred9 > 0))
    gates.gate("G9: bisected lam_c agrees with lam_pred within a factor of 3, same sign",
               sign_ok9 and (1 / 3.0 <= ratio9 <= 3.0),
               f"t1={t1_g9} t2={t2_g9} lam_pred={lam_pred9:.4e} lam_c={lam_c9:.4e} ratio={ratio9:.3f}")

    elapsed = time.time() - t0
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())

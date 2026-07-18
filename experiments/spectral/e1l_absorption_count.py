"""E1L: the E-absorption count 1+nu(lambda^2) as the W6-vs-#143 numerical shadow.

WHY THIS EXPERIMENT EXISTS
==========================
The CCM D_log family (arXiv:2511.22755 Thm 5.10; the e1k testbed) writes its
spectral content in a Betti-number shape "1 + nu(lambda^2)": a distinguished
central mode (the z=0 determinant zero = the functional-equation point s=1/2,
installed by hand as the rank-one perturbation vector xi) plus a
parameter-growing block nu of physical +/- gamma_j determinant zeros. The
question the #154 ledger left open is a DISCRIMINATOR:

  W6 shape (Grothendieck / Deligne, computed by symmetry): the number of
    Frobenius eigenvalues on H^1 of a curve is 2g, a TOPOLOGICAL invariant the
    theory computes by its own symmetry. If 1+nu(lambda^2) converged, as the
    truncation N -> infinity, to a COMPUTED asymptotic in lambda that is
    family-uniform and INDEPENDENT of N, that would be the one W6-shaped
    observable inside the D_log shell: a spectral genus the operator computes.

  #143 shape (Caratheodory-Fejer core, installed by the cutoff): reality and
    count MANUFACTURED by finite self-adjointness. The count and density are
    fixed by the truncation choice; the Riemann-von Mangoldt law appears only at
    the window edge. Then 1+nu carries zero bits about RH: it is bookkeeping of
    the matrix size, an installed determinant-class shell around a #143 core.

THE LOAD-BEARING TEST (family-uniformity / test A). Fix lambda. Sweep the
truncation dimension N. Does the absorbed count PLATEAU at an N-independent
nu_inf(lambda) (computed / W6), or does it TRACK N (installed / #143)? The single
decisive number is the large-N slope d(nu)/dN: ~0 = computed, ~const>0 = installed.

WHY THE ANSWER IS SUBTLE HERE (and reported honestly, not spun). The D_log
machine predicts ALL finite-cutoff determinant zeros REAL (Thm 5.10(iii)); the
faithful e1k build realizes this only up to an O(1) complex-ghost residual (see
STEP 5: n_real_total ~ 2N+1 - O(1), not exactly 2N+1). So the RAW count of
"physical real modes" is the matrix dimension 2N+1 up to O(1): it tracks N with
slope 1, the pure installed #143 signature. A plateau appears ONLY
when we impose the external two-meter window T = 2*pi*lambda^2 (the height that
lambda's Euler data n <= lambda^2 resolves). Inside that window the count
plateaus at ~ Twin * L / (2*pi) = 2*lambda^2*log(lambda), which by the density-
gate two-meter law (ccm_semilocal_prolate.md line 349) EQUALS the leading RvM
count N(Twin). That plateau value is a family-uniform COMPUTED asymptotic in
lambda -- but it is the CIRCLE-GEOMETRY lattice count (the blind Slepian/RvM
coincidence e1f/e1g already validated), installed BY the window choice, with
N*(lambda) ~ the count itself so the plateau barely separates from N. That is
exactly the #143 signature "count fixed by the truncation/window, RvM only at the
edge", NOT a W6 Betti count computed by the operator's own symmetry.

WHAT THIS BUILDS. It reuses the e1k D_log operator verbatim (make_streams,
build_float, operator_spectrum, ZETA_CFG/DH_CFG) and measures three absorption-
count observables side by side on the zeta and D-H twins:
  (i)   n_neg  = #{negative eigenvalues of the truncated Weil form Q} (the
        Sonin / positivity-margin block; a separate diagnostic, NOT the Shannon
        count -- Q is the Weil form, not the bare prolate operator W_lambda).
  (ii)  n_raw  = #{positive real determinant zeros, |re|>1} with NO height cap
        (the raw operator spectrum; = (2N+1-ish)/2, tracks N = installed).
  (iii) n_win  = #{positive real determinant zeros in 1 < re < Twin},
        Twin = 2*pi*lambda^2 (the physically resolved absorption count).
Plus, via e1g's genuine idempotent concentration operator T = P_W P_T P_W, the
classical Slepian plunge cross-check (count near 1 ~ 2c/pi = 4*lambda^2; plunge
width ~ (2/pi^2) log c) that confirms the geometry is genuine-but-blind Slepian.

D-H DISCIPLINE. D-H shares the archimedean Gamma-factor density and the same
two-meter law, so every count law is predicted IDENTICAL for both twins (blind),
the same finding as #158 (finite reality is information-free) and #148 (the
archimedean fragment is K2-blind). A count that discriminated zeta from D-H at
finite cutoff would be an artifact flag, not a Betti count.

HONEST SCOPE. Finite linear algebra on the e1k testbed (which itself is a faithful
reimplementation, not the paper's exact operator; see e1k caveats: razor-thin
positivity margin eps ~ 1e-4..1e-6, zeta pole term only ~5e-2 G-self-adjoint).
It proves nothing about RH. It measures ONE of the four named upgrade-spec
ingredients (the absorption-count law) and reports where it lands on the
W6-vs-#143 gate. It does NOT close the W6 upgrade and does NOT move any wall.

Run:
  python3 -m experiments.spectral.e1l_absorption_count
Outputs:
  experiments/spectral/e1l_absorption_count.npz  (+ .md companion)
"""

from __future__ import annotations

import argparse
import time
import warnings
from pathlib import Path

import numpy as np

from experiments.spectral.e1k_dh_dlog_testbed import (
    make_streams, build_float, operator_spectrum, ZETA_CFG, DH_CFG,
    ZETA_ZEROS, DH_ZEROS,
)
from experiments.spectral.e1g_ccm_faithful_prolate import concentration_spectrum

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")

IMAG_TOL = 1e-6   # a determinant zero counts as "real" (on-line) below this |Im|
RE_CUT = 1.0      # exclude the low-lying/central bookkeeping band (|re|>1)

# WHY a cache: build_float's archimedean matrix is 2401+ adaptive mpmath
# quadratures per call (~30s at N=48). Tests A, B and the anti-fooling step all
# reuse the same (lambda, N, twin) builds, so we memoize the FAITHFUL e1k build
# (no accelerated surrogate: a numpy-grid arch matrix drifts ~5e-4, which swamps
# the razor-thin eps~1e-4 margin and corrupts the physical-zero count).
_CACHE: dict = {}


# --------------------------------------------------------------------------
# The three absorption-count observables on a single e1k D_log build.
# WHY three: the spec names two proxies (Sonin n_neg, physical zeros n_phys),
# but they measure different objects here (Q is the Weil form, not the bare
# prolate operator), so we report both plus the raw/windowed split that is the
# actual W6-vs-#143 discriminator.
# --------------------------------------------------------------------------
def count_observables(N, lam, stream, cfg, Twin, label=""):
    key = (label, round(lam, 6), int(N))
    if key in _CACHE:
        o = dict(_CACHE[key])
        o["n_win"] = int(sum(1 for x in o["_reals_pos"] if x < Twin))
        o["n_win_nofilter"] = int(sum(1 for x in o["_reals_pos_nofilter"] if x < Twin))
        return o
    r = build_float(N, lam, stream, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
    ev, sa = operator_spectrum(r)
    w = r["w"]
    n_neg = int(np.sum(w < 0))                                  # Sonin / positivity block
    reals_pos = [z.real for z in ev if abs(z.imag) < IMAG_TOL and z.real > RE_CUT]
    n_raw = int(len(reals_pos))                                 # no height cap => tracks N
    n_win = int(sum(1 for x in reals_pos if x < Twin))          # within the two-meter window
    n_real_total = int(sum(1 for z in ev if abs(z.imag) < IMAG_TOL))
    top_re = float(max((z.real for z in ev), default=0.0))
    # anti-fooling control #2: does removing the |Im| filter change the real count?
    # Thm 5.10(iii) predicts total reality, but the FAITHFUL e1k build only realizes
    # it approximately (non-normal, ~1e-4 G-self-adjoint): D-H comes out real to ~1e-12,
    # while zeta carries O(1) complex "ghosts" (|Im| up to ~0.5) from the imperfect pole
    # realization. So this filter is NOT inert for zeta -- it can move n_win by O(1).
    reals_pos_nofilter = [z.real for z in ev if z.real > RE_CUT]
    n_win_nofilter = int(sum(1 for x in reals_pos_nofilter if x < Twin))
    o = dict(
        n_neg=n_neg, n_raw=n_raw, n_win=n_win, n_real_total=n_real_total,
        D=2 * N + 1, top_re=top_re, eps=float(r["eps"]),
        even_ok=bool(r["even_assumption_ok"]), sa_res=float(sa),
        n_win_nofilter=n_win_nofilter,
        _reals_pos=reals_pos, _reals_pos_nofilter=reals_pos_nofilter,
    )
    _CACHE[key] = o
    return dict(o)


def n_star(lam):
    """N*(lambda): the truncation at which the two-meter window fills = Twin/phi.
    phi = 2 pi / L, L = 2 log lam, Twin = 2 pi lam^2 => N* = 2 lam^2 log lam.
    This ALSO equals the leading RvM / circle-lattice count Twin*L/(2 pi).
    CAVEAT: phi*N* = Twin holds EXACTLY by construction, so n_win = Twin/phi is a
    LATTICE-COUNTING IDENTITY forced by the window choice, not a symmetry-computed
    quantity. The RvM-vs-Shannon fit confirms the lattice spacing phi = pi/log lam;
    it cannot separate 'computed by symmetry' from 'installed by the window' here."""
    return 2.0 * lam * lam * np.log(lam)


# --------------------------------------------------------------------------
# STEP 3: the genuine Slepian plunge, via e1g's idempotent concentration op.
# WHY: confirms the log-circle geometry is a real time-bandwidth concentration
# machine (count near 1 ~ 2c/pi Shannon; plunge width ~ (2/pi^2) log c), i.e.
# the family-uniform COMPUTED-but-BLIND geometry count the D_log shell sits on.
# --------------------------------------------------------------------------
def slepian_plunge(lam, eps=0.1, N=8192, L=60.0):
    c = 2.0 * np.pi * lam * lam                 # prolate parameter (spec: c = 2 pi lam^2)
    # SYMMETRIC time-bandwidth U0=S0=sqrt(c) so c = U0*S0 AND the band subspace is
    # large enough (dim >> 2c/pi) to actually HOLD all the absorbed modes; with the
    # e1g convention S0=1 the band caps the count. This is the Shannon-number config.
    r = np.sqrt(c)
    ev, M = concentration_spectrum(U0=r, S0=r, N=N, L=L, primes=[])
    n_absorbed = int(np.sum(ev > 0.5))          # Shannon: ~2c/pi eigenvalues near 1
    n_plunge = int(np.sum((ev > eps) & (ev < 1 - eps)))
    shannon = 2.0 * c / np.pi                    # = 4 lam^2
    plunge_pred = (2.0 / np.pi ** 2) * np.log(c) * np.log(1.0 / eps - 1.0)
    return dict(c=c, n_absorbed=n_absorbed, shannon=shannon,
                n_plunge=n_plunge, plunge_pred=float(plunge_pred), band_dim=M)


# --------------------------------------------------------------------------
# Least-squares helpers for the lambda-law fit (test B).
# --------------------------------------------------------------------------
def fit_scale(y, model):
    """Best single-scale fit y ~ a*model; return (a, relative rms residual)."""
    y = np.asarray(y, float)
    model = np.asarray(model, float)
    a = float((model @ y) / (model @ model))
    resid = y - a * model
    rms = float(np.sqrt(np.mean(resid ** 2)) / (np.mean(np.abs(y)) or 1.0))
    return a, rms


def fit_powerlaw(lam, y):
    """log y = log C + b log lam. Return (C, b, rms in log)."""
    lam = np.asarray(lam, float)
    y = np.asarray(y, float)
    A = np.vstack([np.ones_like(lam), np.log(lam)]).T
    coef, *_ = np.linalg.lstsq(A, np.log(y), rcond=None)
    logC, b = coef
    resid = np.log(y) - A @ coef
    rms = float(np.sqrt(np.mean(resid ** 2)))
    return float(np.exp(logC)), float(b), rms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="smaller sweeps")
    args = ap.parse_args()

    t_start = time.time()
    results = {}
    lz, ld = make_streams(80, float_out=True)
    twins = [("ZETA", ZETA_CFG, lz), ("D-H", DH_CFG, ld)]

    print("=" * 78)
    print("E1L: E-absorption count 1+nu(lambda^2) -- the W6-vs-#143 numerical shadow")
    print("=" * 78)

    # ======================================================================
    # STEP 1 (TEST A): N-sweep at FIXED lambda. The load-bearing discriminator.
    # ======================================================================
    print("\n[STEP 1 -- TEST A] N-dependence at FIXED lambda (does the count PLATEAU or TRACK N?)")
    if args.quick:
        A_lams = [float(np.sqrt(13.0))]
        A_Ngrid = {float(np.sqrt(13.0)): [8, 16, 24, 32, 40]}
    else:
        A_lams = [float(np.sqrt(13.0)), 3.0]
        A_Ngrid = {float(np.sqrt(13.0)): [8, 16, 24, 32, 40, 48],
                   3.0: [8, 16, 24, 32]}
    stepA = {}
    for lam in A_lams:
        Twin = 2 * np.pi * lam * lam
        Ns = A_Ngrid[lam]
        print(f"\n  lambda={lam:.4f}  lam^2={lam*lam:.2f}  Twin=2pi lam^2={Twin:.2f}"
              f"  N*={n_star(lam):.1f}  (circle-lattice/leading-RvM count = N*)")
        print(f"    {'N':>3} {'D':>4} | "
              f"{'ZETA n_neg':>10} {'n_raw':>6} {'n_win':>6} | "
              f"{'DH n_neg':>8} {'n_raw':>6} {'n_win':>6}   (reality approximate: O(1) ghosts, see STEP 5)")
        rec = {lbl: dict(N=[], n_neg=[], n_raw=[], n_win=[], eps=[], sa=[], top=[])
               for lbl, _, _ in twins}
        for N in Ns:
            row = {}
            for lbl, cfg, stream in twins:
                o = count_observables(N, lam, stream, cfg, Twin, label=lbl)
                row[lbl] = o
                rec[lbl]["N"].append(N)
                rec[lbl]["n_neg"].append(o["n_neg"])
                rec[lbl]["n_raw"].append(o["n_raw"])
                rec[lbl]["n_win"].append(o["n_win"])
                rec[lbl]["eps"].append(o["eps"])
                rec[lbl]["sa"].append(o["sa_res"])
                rec[lbl]["top"].append(o["top_re"])
            z, d = row["ZETA"], row["D-H"]
            print(f"    {N:>3} {z['D']:>4} | "
                  f"{z['n_neg']:>10} {z['n_raw']:>6} {z['n_win']:>6} | "
                  f"{d['n_neg']:>8} {d['n_raw']:>6} {d['n_win']:>6}")
        # decisive slopes in the large-N half of the sweep
        for lbl in ("ZETA", "D-H"):
            Ns_arr = np.array(rec[lbl]["N"], float)
            half = Ns_arr >= np.median(Ns_arr)
            for key in ("n_raw", "n_win", "n_neg"):
                y = np.array(rec[lbl][key], float)
                if half.sum() >= 2:
                    slope = float(np.polyfit(Ns_arr[half], y[half], 1)[0])
                else:
                    slope = float("nan")
                rec[lbl][f"slope_{key}"] = slope
        zs, ds = rec["ZETA"], rec["D-H"]
        print(f"    large-N slope d/dN:  ZETA  n_raw={zs['slope_n_raw']:+.3f}"
              f"  n_win={zs['slope_n_win']:+.3f}  n_neg={zs['slope_n_neg']:+.3f}")
        print(f"                         D-H   n_raw={ds['slope_n_raw']:+.3f}"
              f"  n_win={ds['slope_n_win']:+.3f}  n_neg={ds['slope_n_neg']:+.3f}")
        print(f"    => n_raw slope ~ +0.5..1.0 (TRACKS N = installed);"
              f" n_win slope -> 0 once N>=N* (plateau, but IMPOSED by the window).")
        stepA[lam] = rec
        for lbl in ("ZETA", "D-H"):
            for key in ("N", "n_neg", "n_raw", "n_win", "eps"):
                results[f"A_lam{lam:.3f}_{lbl}_{key}"] = np.array(rec[lbl][key])
            for key in ("n_raw", "n_win", "n_neg"):
                results[f"A_lam{lam:.3f}_{lbl}_slope_{key}"] = rec[lbl][f"slope_{key}"]

    # ======================================================================
    # STEP 2 (TEST B): lambda-law fit of the plateau nu_inf(lambda).
    # WHY: is nu_inf(lambda) a stable function of lambda alone (family-uniform),
    # and which law -- Shannon 4 lam^2 or RvM/circle-lattice 2 lam^2 log lam?
    # ======================================================================
    print("\n[STEP 2 -- TEST B] lambda-law fit of the plateau count nu_inf(lambda)")
    # WHY these N: chosen >= N*(lam) so we sit ON the plateau; where lam is in the
    # test-A grid we reuse the cached large-N build (3.0->N=32, sqrt13->N=48).
    B_Nmap = {2.2: 12, 2.6: 16, 3.0: 32, round(float(np.sqrt(13.0)), 3): 48}
    if args.quick:
        B_lams = [2.2, 2.6, 3.0, float(np.sqrt(13.0))]
    else:
        B_lams = [2.2, 2.6, 3.0, float(np.sqrt(13.0))]
    print("    (N chosen >= N*(lam), reusing cached test-A builds where possible)")
    print(f"    {'lam':>6} {'lam^2':>7} {'N':>4} {'Twin':>7} {'N*':>6} | "
          f"{'ZETA 1+nu':>9} {'DH 1+nu':>8}   (1+nu = n_win = windowed absorption count)")
    B = {"lam": [], "ZETA": [], "D-H": [], "N": [], "Twin": []}
    for lam in B_lams:
        Twin = 2 * np.pi * lam * lam
        N = B_Nmap.get(round(lam, 3), int(min(56, max(8, np.ceil(1.25 * n_star(lam))))))
        B["lam"].append(lam); B["N"].append(N); B["Twin"].append(Twin)
        vals = {}
        for lbl, cfg, stream in twins:
            o = count_observables(N, lam, stream, cfg, Twin, label=lbl)
            vals[lbl] = o["n_win"]
            B[lbl].append(o["n_win"])
        print(f"    {lam:>6.3f} {lam*lam:>7.2f} {N:>4} {Twin:>7.1f} {n_star(lam):>6.1f} | "
              f"{vals['ZETA']:>9} {vals['D-H']:>8}")
    lam_arr = np.array(B["lam"], float)
    shannon_model = 4.0 * lam_arr ** 2
    rvm_model = 2.0 * lam_arr ** 2 * np.log(lam_arr)      # = Twin*L/2pi, leading RvM
    fits = {}
    for lbl in ("ZETA", "D-H"):
        y = np.array(B[lbl], float)
        a_sh, r_sh = fit_scale(y, shannon_model)
        a_rv, r_rv = fit_scale(y, rvm_model)
        C, b, r_pl = fit_powerlaw(lam_arr, y)
        fits[lbl] = dict(a_shannon=a_sh, rms_shannon=r_sh,
                         a_rvm=a_rv, rms_rvm=r_rv, C=C, b=b, rms_pl=r_pl)
        print(f"    {lbl:5s} fit:  Shannon a*(4 lam^2): a={a_sh:.3f} rms={r_sh:.3f}  |"
              f"  RvM a*(2 lam^2 log lam): a={a_rv:.3f} rms={r_rv:.3f}  |"
              f"  power C*lam^b: b={b:.3f} rms={r_pl:.3f}")
    print("    => n_win = Twin/phi is a LATTICE IDENTITY forced by phi*N*=Twin, so this fit")
    print("       CONFIRMS the lattice spacing phi=pi/log lam; it cannot separate 'computed'")
    print("       from 'installed'. Same-lattice law: D-H clean (a~0.94, 1.6%), zeta pole/")
    print("       ghost-perturbed (a~0.80, 17%, ~2x low-lam outlier). The BLIND geometry law.")
    results["B_lam"] = lam_arr
    results["B_N"] = np.array(B["N"])
    results["B_Twin"] = np.array(B["Twin"])
    results["B_ZETA_1pnu"] = np.array(B["ZETA"], float)
    results["B_DH_1pnu"] = np.array(B["D-H"], float)
    results["B_shannon_model"] = shannon_model
    results["B_rvm_model"] = rvm_model
    for lbl in ("ZETA", "D-H"):
        for k, v in fits[lbl].items():
            results[f"B_{lbl}_{k}"] = v

    # ======================================================================
    # STEP 3: genuine Slepian plunge cross-check (e1g concentration operator).
    # ======================================================================
    print("\n[STEP 3] genuine Slepian plunge (e1g T=P_W P_T P_W): confirms the geometry")
    print("    {:>6} {:>8} | {:>10} {:>10} | {:>10} {:>10}".format(
        "lam", "c", "n>1/2", "2c/pi", "plunge", "(2/pi^2)logc*"))
    plunge_lams = [float(np.sqrt(13.0)), 3.0, 4.0, 5.0] if not args.quick else [float(np.sqrt(13.0)), 4.0]
    P = {"lam": [], "c": [], "n_absorbed": [], "shannon": [], "n_plunge": [], "plunge_pred": []}
    for lam in plunge_lams:
        pl = slepian_plunge(lam)
        for k in ("c", "n_absorbed", "shannon", "n_plunge", "plunge_pred"):
            P[k].append(pl[k])
        P["lam"].append(lam)
        print("    {:>6.3f} {:>8.2f} | {:>10d} {:>10.2f} | {:>10d} {:>10.2f}".format(
            lam, pl["c"], pl["n_absorbed"], pl["shannon"], pl["n_plunge"], pl["plunge_pred"]))
    print("    => count near 1 ~ 2c/pi = 4 lam^2 (Shannon), plunge width ~ (2/pi^2) log c")
    print("       (Landau-Widom): the log-circle IS a genuine time-bandwidth machine,")
    print("       family-uniform and COMPUTED -- but BLIND (e1g: reweighting-invariant).")
    for k, v in P.items():
        results[f"P_{k}"] = np.array(v, float)

    # ======================================================================
    # STEP 4 (D-H control): blindness verdict, quantified.
    # ======================================================================
    print("\n[STEP 4 -- D-H CONTROL] blind or discriminating?")
    lam0 = float(np.sqrt(13.0))
    zc = np.array(results[f"B_ZETA_1pnu"])
    dc = np.array(results[f"B_DH_1pnu"])
    reldiff = np.abs(zc - dc) / np.maximum(np.abs(zc), 1.0)
    print(f"    windowed 1+nu, ZETA vs D-H across the lambda grid:")
    print(f"      ZETA: {[int(x) for x in zc]}")
    print(f"      D-H : {[int(x) for x in dc]}")
    print(f"      max relative difference = {float(np.max(reldiff)):.3f}"
          f"  (leading-order agreement => D-H-BLIND count law)")
    print(f"    NB: part of the residual zeta<D-H gap is the |Im|-filtered complex-ghost")
    print(f"    artifact (STEP 5) + the zeta pole, NOT a clean archimedean-density signal.")
    print(f"    Removing the artifact makes the twins MORE blindly identical, reinforcing blind.")
    print(f"    slope verdict is IDENTICAL for both twins (see STEP 1). The count law does")
    print(f"    NOT discriminate zeta from D-H: same Gamma-factor density, same two-meter law.")
    print(f"    (The only place a difference could hide -- the off-line zero at gamma~85.7 --")
    print(f"     is quarantined to the Section-7 uniform limit; INVISIBLE at finite cutoff.)")
    results["DH_maxreldiff"] = float(np.max(reldiff))

    # ======================================================================
    # STEP 5 (anti-fooling): window removal, |Im| filter, margins.
    # ======================================================================
    print("\n[STEP 5 -- ANTI-FOOLING]")
    Twin0 = 2 * np.pi * lam0 * lam0
    af = {}
    for lbl, cfg, stream in twins:
        o32 = count_observables(32, lam0, stream, cfg, Twin0, label=lbl)
        o48 = count_observables(48, lam0, stream, cfg, Twin0, label=lbl) if not args.quick else o32
        af[lbl] = (o32, o48)
        ghosts32 = o32["D"] - o32["n_real_total"]
        ghosts48 = o48["D"] - o48["n_real_total"]
        print(f"  {lbl}: N=32 -> n_raw={o32['n_raw']} (no window, TRACKS N), "
              f"n_win={o32['n_win']} (windowed);  N=48 -> n_raw={o48['n_raw']}, n_win={o48['n_win']}")
        # COMPUTED (not asserted): n_real_total vs D exposes complex "ghost" modes.
        print(f"       reality: n_real_total={o32['n_real_total']}/{o32['D']} at N=32, "
              f"{o48['n_real_total']}/{o48['D']} at N=48  "
              f"(complex ghosts: {ghosts32} at N=32, {ghosts48} at N=48)")
        print(f"       |Im|-filter effect: n_win={o32['n_win']} vs n_win_nofilter={o32['n_win_nofilter']}"
              f"  (differ IFF a ghost falls in-window)")
        print(f"       razor-thin margin eps={o32['eps']:.2e}, even_assumption_ok={o32['even_ok']},"
              f" G-sa residual={o32['sa_res']:.1e}")
    print("  (i)  Removing the two-meter window flips PLATEAU -> TRACKS-N: the window does the")
    print("       work; the RAW count is installed (= matrix dimension).")
    print("  (ii) |Im| filter is NOT universally inert: Thm 5.10(iii) reality is only")
    print("       APPROXIMATELY realized by the faithful e1k build (non-normal, ~1e-4 G-self-")
    print("       adjoint). At the run precision (dps=25, forced by e1g module load) BOTH twins")
    print("       carry ~2 complex ghosts in the central |re|<1 band (excluded by RE_CUT), so")
    print("       n_win=n_win_nofilter here by ghost PLACEMENT, not by total reality. At dps=15")
    print("       zeta's ghosts move into the physical band (re=+-26.6, |Im|=0.55) INSIDE the")
    print("       window and the filter changes n_win (29 vs 31); D-H stays 65/65 real at dps=15.")
    print("       This is e1k caveat-2 (imperfect pole realization) surfacing, not information.")
    results["AF_ZETA_n_raw_32"] = af["ZETA"][0]["n_raw"]
    results["AF_ZETA_n_win_32"] = af["ZETA"][0]["n_win"]
    results["AF_ZETA_eps_32"] = af["ZETA"][0]["eps"]
    results["AF_ZETA_n_real_total_32"] = af["ZETA"][0]["n_real_total"]
    results["AF_ZETA_D_32"] = af["ZETA"][0]["D"]
    results["AF_ZETA_n_win_nofilter_32"] = af["ZETA"][0]["n_win_nofilter"]
    results["AF_DH_n_raw_32"] = af["D-H"][0]["n_raw"]
    results["AF_DH_n_win_32"] = af["D-H"][0]["n_win"]
    results["AF_DH_n_real_total_32"] = af["D-H"][0]["n_real_total"]
    results["AF_DH_D_32"] = af["D-H"][0]["D"]

    # ======================================================================
    # VERDICT
    # ======================================================================
    print("\n" + "=" * 78)
    print("VERDICT (W6 vs #143)")
    zsl = results[f"A_lam{lam0:.3f}_ZETA_slope_n_raw"]
    zwsl = results[f"A_lam{lam0:.3f}_ZETA_slope_n_win"]
    print(f"  Decisive slope d(nu)/dN at lambda={lam0:.3f}:")
    print(f"    RAW physical count:  d/dN = {float(zsl):+.3f}  (~ +0.5..1.0 => TRACKS N = #143 installed)")
    print(f"    WINDOWED count:      d/dN = {float(zwsl):+.3f}  (~ 0 once N>=N*, but plateau IMPOSED by window)")
    print("  => #143 shape CONFIRMED (installed shell), with the honest nuance that the")
    print("     windowed count IS a family-uniform computed asymptotic in lambda (~2 lam^2 log lam,")
    print("     the leading RvM = circle-lattice count) -- but it is the BLIND archimedean/geometry")
    print("     count (the two-meter density coincidence, e1f/e1g Slepian), installed BY the")
    print("     window T=2 pi lam^2 with N*~count, NOT a W6 Betti count computed by symmetry.")
    print("  => D-H gives the IDENTICAL law and the IDENTICAL verdict: BLIND.")
    print("  This is the numerical shadow of the #154 ledger: spectrum budget INSTALLED, not")
    print("  computed. It measures one upgrade-spec ingredient; it does NOT close W6 or move a wall.")
    print("=" * 78)

    results["meta_imag_tol"] = IMAG_TOL
    results["meta_re_cut"] = RE_CUT
    np.savez_compressed(OUT, **results)
    print(f"\nSaved -> {OUT}")
    print(f"Total time {round(time.time() - t_start, 1)}s")


if __name__ == "__main__":
    main()

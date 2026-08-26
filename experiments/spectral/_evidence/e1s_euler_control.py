"""ADVERSARY control (#169 follow-up): sharp falsification test of the
Euler-product attribution in experiments/spectral/_e1s_dh_undercount.md
section 5.

The dossier attributes D-H's ground-state gap collapse (gap_even shrinking
4-6 orders of magnitude relative to zeta-off) to "Euler-product-sourced"
structure, established BY ELIMINATION (a hybrid archimedean/coefficient-
stream swap that showed neither ingredient alone reproduces the collapse)
and flags a genuine non-zeta Euler-product control as the sharp test.

This script runs chi3_L (mod 3, odd) and chi4_L (mod 4, odd) -- both real
primitive Dirichlet characters with a genuine Euler product AND a functional
equation, i.e. on zeta's side of the Euler-product axis while differing from
zeta in conductor/character -- through the IDENTICAL truncated-Weil-form
construction (build_float / operator_spectrum) at the SAME (N, lambda) cells
used for the zeta-off vs D-H gap_even table in _e1s_dh_undercount.md section 4.

PRE-REGISTERED PREDICTION (written before any control number below was
computed or looked at):
  - EULER ATTRIBUTION CORRECT  => chi3/chi4 gap_even tracks zeta-off:
    order 1-10, GROWING with lambda, NOT collapsing by orders of magnitude.
  - EULER ATTRIBUTION FALSIFIED => chi3/chi4 gap_even ALSO collapses like
    D-H. If so, candidate alternative drivers to consider: the specific
    small conductor (q=3,4 vs zeta's q=1), the specific archimedean-density/
    coefficient-stream MATCH being a general "any non-zeta Selberg-class
    member" effect rather than an Euler-product-specific one, or some other
    shared structural feature.

Archimedean density (dens_a, dens_b) is derived directly from the SAME
functional-equation template already used (and confirmed self-consistent)
for both twins in e1k_dh_dlog_testbed.py:
    Lambda(s, chi) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s, chi)
  => dens_a = (2a+1)/4, dens_b = log(q/pi)
  Zeta:  q=1, a=0  -> dens_a=0.25, dens_b=-log(pi)      (matches ZETA_CFG)
  D-H:   q=5, a=1  -> dens_a=0.75, dens_b=log(5/pi)     (matches DH_CFG)
  chi3:  q=3, a=1  -> dens_a=0.75, dens_b=log(3/pi)
  chi4:  q=4, a=1  -> dens_a=0.75, dens_b=log(4/pi)
This is not a fudge: it is forced by the same completed-L-function template
DirichletL.functional_equation_residual already implements, and it exactly
reproduces both pre-existing CFGs (a non-cherry-picked, two-point-verified
formula).

The coefficient stream Lambda(n) uses the IDENTICAL Dirichlet log-derivative
recursion (sum_{d|n} Lambda(d) c_{n/d} = c_n log n) already used for zeta and
D-H, with c_n = chi(n) taken directly from DirichletL.dirichlet_coefficient.
Since chi is completely multiplicative (a genuine Euler product), this
recursion is EXPECTED to produce a Lambda supported on prime powers only
(sparse, like zeta, unlike D-H's dense period-5 stream) -- verified below as
a structural sanity check, not assumed.

No tracked .npz is touched. This script is standalone/disposable evidence,
kept under _evidence/ per the repo's evidence rule so the numbers in the
report are reproducible from a tracked file.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from experiments.spectral.e1k_dh_dlog_testbed import (  # noqa: E402
    build_float, make_streams, ZETA_CFG, DH_CFG, ZETA_ZEROS, DH_ZEROS,
    match_known, operator_spectrum,
)
from experiments._shared.dirichlet_l import chi3_L, chi4_L  # noqa: E402


def make_stream_from_chi(kmax, L_obj, float_out=True):
    """Same recursion as e1k's make_streams, but c_n = chi(n) from L_obj."""
    q = L_obj.modulus
    c = [mp.mpf(0)] + [L_obj.dirichlet_coefficient(n).real for n in range(1, kmax + 1)]
    Lam = [mp.mpf(0)] * (kmax + 1)
    for n in range(2, kmax + 1):
        s = c[n] * mp.log(n)
        for d in range(2, n):
            if n % d == 0:
                s -= Lam[d] * c[n // d]
        Lam[n] = s
    if float_out:
        return [float(x) for x in Lam]
    return Lam


def is_prime_power(n):
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return True


def cfg_for(L_obj):
    a = L_obj.parity
    q = L_obj.modulus
    dens_a = (2 * a + 1) / 4.0
    dens_b = float(mp.log(mp.mpf(q) / mp.pi))
    return dict(dens_a=dens_a, dens_b=dens_b, use_pole=False)


def main():
    mp.mp.dps = 25  # match the dossier's stated "N=8, dps=25" archimedean-quadrature precision exactly
    print("=" * 78)
    print("STEP 0: pre-registered prediction (see module docstring above)")
    print("=" * 78)
    print("  CORRECT attribution -> chi3/chi4 gap_even robust, grows with lambda")
    print("  FALSIFIED attribution -> chi3/chi4 gap_even also collapses like D-H")

    # ---- STEP 1: reproduce the dossier's zeta-off vs D-H gap_even table ----
    print("\n" + "=" * 78)
    print("STEP 1: reproduction of _e1s_dh_undercount.md section 4 (N=8, dps default float64)")
    print("=" * 78)
    lam_grid = [2.0, 2.5, 3.0, 3.3, 3.6, 4.0, 4.5, 5.0, 5.5]
    N = 8
    kmax_needed = int(np.floor(max(lam_grid) ** 2)) + 1
    lz, ld = make_streams(max(kmax_needed, 40), float_out=True)

    repro = {}
    for lam in lam_grid:
        # "Zoff" per e1s_rank_one_interlacing.py:cell() = ZETA_CFG dens with
        # use_pole=False (pole-off), NOT ZETA_CFG["use_pole"]=True. Matching
        # this exactly is required to reproduce the dossier's table.
        rz = build_float(N, lam, lz, ZETA_CFG["dens_a"], ZETA_CFG["dens_b"], False)
        rd = build_float(N, lam, ld, DH_CFG["dens_a"], DH_CFG["dens_b"], DH_CFG["use_pole"])
        repro[lam] = (rz["gap_even"], rd["gap_even"])
        print(f"  lam={lam:4.2f}  Zoff gap_even={rz['gap_even']:.4e}   DH gap_even={rd['gap_even']:.4e}"
              f"   ratio(Zoff/DH)={rz['gap_even']/rd['gap_even']:.3e}")

    # ---- STEP 2: build chi3 / chi4 CFGs and streams -------------------------
    print("\n" + "=" * 78)
    print("STEP 2: chi3/chi4 CFG + stream construction + structural sanity check")
    print("=" * 78)
    kmax = max(kmax_needed, 40)
    streams = {}
    cfgs = {}
    for name, Lobj in [("chi3", chi3_L), ("chi4", chi4_L)]:
        cfgs[name] = cfg_for(Lobj)
        streams[name] = make_stream_from_chi(kmax, Lobj, float_out=True)
        support = [n for n in range(2, kmax + 1) if abs(streams[name][n]) > 1e-9]
        non_pp = [n for n in support if not is_prime_power(n)]
        print(f"  {name}: modulus={Lobj.modulus} parity={Lobj.parity} "
              f"dens_a={cfgs[name]['dens_a']:.3f} dens_b={cfgs[name]['dens_b']:.4f}")
        print(f"       support n<=30: {[n for n in support if n <= 30]}")
        print(f"       non-prime-power entries in support (should be EMPTY if genuinely "
              f"Euler-product / completely multiplicative): {non_pp}")

    # ---- STEP 2b: quick zero-match sanity check on the construction --------
    print("\n  quick zero-match sanity (N=10, lam~2.8, low-height known zeros):")
    for name, Lobj in [("chi3", chi3_L), ("chi4", chi4_L)]:
        known = sorted(z.imag for z in Lobj.zeros(15.0, prec=20))
        r = build_float(10, 2.8, streams[name], cfgs[name]["dens_a"], cfgs[name]["dens_b"], False)
        ev, sa = operator_spectrum(r)
        m = match_known(ev, known[:3])
        print(f"    {name}: known zeros (T<=15) = {[round(float(x),4) for x in known[:3]]}")
        for g, got, err in m:
            print(f"       {float(g):8.4f} -> {float(got):8.4f}  (err {float(err):.2e})")

    # ---- STEP 3: gap_even sweep, identical cells ----------------------------
    print("\n" + "=" * 78)
    print("STEP 3: gap_even sweep across lam, N=8, IDENTICAL construction/code path")
    print("=" * 78)
    header = f"{'lam':>5} {'Zoff':>12} {'DH':>12} {'chi3':>12} {'chi4':>12} {'chi3/Zoff':>10} {'chi4/Zoff':>10}"
    print(header)
    rows = []
    for lam in lam_grid:
        rz_gap = repro[lam][0]
        rd_gap = repro[lam][1]
        r3 = build_float(N, lam, streams["chi3"], cfgs["chi3"]["dens_a"], cfgs["chi3"]["dens_b"], False)
        r4 = build_float(N, lam, streams["chi4"], cfgs["chi4"]["dens_a"], cfgs["chi4"]["dens_b"], False)
        g3, g4 = r3["gap_even"], r4["gap_even"]
        rows.append((lam, rz_gap, rd_gap, g3, g4))
        print(f"{lam:5.2f} {rz_gap:12.4e} {rd_gap:12.4e} {g3:12.4e} {g4:12.4e} "
              f"{g3/rz_gap:10.3e} {g4/rz_gap:10.3e}")

    print("\n" + "=" * 78)
    print("SUMMARY TABLE (for report)")
    print("=" * 78)
    print("| lam | Zoff gap | DH gap | chi3 gap | chi4 gap | Zoff/DH | Zoff/chi3 | Zoff/chi4 |")
    print("|---|---|---|---|---|---|---|---|")
    for lam, zg, dg, g3, g4 in rows:
        print(f"| {lam} | {zg:.3e} | {dg:.3e} | {g3:.3e} | {g4:.3e} | "
              f"{zg/dg:.2e} | {zg/g3:.2e} | {zg/g4:.2e} |")


if __name__ == "__main__":
    main()

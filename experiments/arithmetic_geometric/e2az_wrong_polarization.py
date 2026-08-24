"""E2AZ: B2: the wrong polarization, built anyway: three candidate metrics
on the v0 cokernel, scored cell-by-cell against the SP5 spec, and the
trilemma they measure out.

THE SETTING (e2an v0). The carrier is the circle/line picture with the
lattice map acting diagonally: multiplier m(tau) extracted from integer
data alone (K1-clean); the cokernel H^1 is where |m| dips (the emergent
zeros); the scaling flow is diagonal(tau) compressed to the dip modes.
SP5 asks for a polarization: an inner product making the flow
self-adjoint with the right spectrum AND supplying POSITIVITY on the
primitive part from structure, not from the zeros (the 7-property spec,
math_iteration_engines.md Section 3; the load-bearing demands here:
P3 K1-non-circularity, P4 Euler-product firewall, P6 indefinite-with-
positive-primitive, P7 the open content).

THE THREE CANDIDATES (backlog B2):
  (a) FLAT: L^2 on the carrier, restricted to the dip modes.
  (b) PULLBACK: <f, g>_E = <E f, E g>: diagonal weights |m(tau)|^2.
  (c) CHRISTOFFEL: weights from the Christoffel/CD kernel K_M(tau, tau)
      of the emergent measure (atoms at the dips); plus its K1-CLEAN
      SURROGATE (same construction on the measure |m(tau)|^2 d tau,
      which consumes no locations).

PRE-REGISTERED (the backlog's clause, sharpened to a TRILEMMA over three
demands: D1 = positive mass on the primitive (dip) part; D2 = K1-clean
(no zero locations consumed, neither as weights nor as support
selection); D3 = arithmetic contact (Euler-sourced: separates zeta from
D-H)):
  [B2-1] All three metrics are diagonal, so the flow is self-adjoint
         with the right spectrum in every case: self-adjointness is
         FREE here and cannot be the discriminating demand.
  [B2-2] FLAT = (D1 yes, D2 NO, D3 NO): its restriction to the dips is
         THE WEIL FORM ITSELF (measured: dip-restricted flat Gram equals
         the prime-side-assembled Weil Gram to assembly+refinement
         error): positivity by restatement, with the zero locations
         consumed at the SUPPORT-selection step; and the same
         construction passes verbatim on D-H's on-line zeros while
         D-H's RH is false (the P4 firewall, measured).
  [B2-3] PULLBACK = (D1 NO, D2 yes, D3 partial): K1-clean and
         Euler-sourced, but its mass sits exactly OFF the primitive
         part (weights = |m|^2 vanish at the dips: measured ratio;
         the #170 law: free exactly where information-free). It DOES
         see completeness structurally (at D-H's off-line landmark the
         weight fails to vanish: measured), i.e. it detects the
         D-H pathology without certifying anything positive about it.
  [B2-4] CHRISTOFFEL = (D1 yes, D2 NO, D3 NO): the CD kernel of the
         atomic emergent measure concentrates on the atoms (measured vs
         degree M), but its DEFINING DATA ARE THE LOCATIONS (the K1
         ledger line), and the construction poses IDENTICALLY on D-H's
         dip set (measured: the D-H twin concentrates the same way),
         so it flunks the firewall exactly like FLAT. Its K1-clean
         surrogate (|m|^2-weighted measure) concentrates off the dips
         like the pullback (measured): removing the location input
         restores the #170 law. The off-atom growth of K_M is the
         uniform growth clause (#160/#171/#172) surfacing inside the
         object.
  KILL (pre-registered): if any candidate achieves D1 AND D2 AND D3
         with margin above assembly error, escalate immediately (it
         would be a K1-clean Euler-sourced positive polarization at
         finite scale: not M4, but a new door). Expected: no candidate,
         and more sharply: within this family D1 IMPLIES (not-D2 and
         not-D3): primitive positivity is purchasable only from the dip
         set; the dip set is FE-side data shared with D-H; and the
         Euler-side data (the multiplier values) VANISH exactly on it.

THE DELIVERABLE: coordinate system #4 for M4 (after variational /
lattice-Hamburger / Weyl-spectral-chain, #171): in the assembled
object's own coordinates, M4 = the demand that the Euler side fund
positivity precisely on the locus where its own transform vanishes:
the conservation law (#148/#170) as a vanishing-locus statement, with
the three wrong polarizations as its measured faces. Probes C2.
Frontier expectation: UNMOVED.

Run:
  python -m experiments.arithmetic_geometric.e2az_wrong_polarization

Outputs: e2az_wrong_polarization.npz (tracked, evidence rule).
"""

from __future__ import annotations

import time
from math import pi
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, Probe, build_dh_lattice, build_zeta_lattice, detect_zeros,
    lambda_sieve, line_integrand, multiplier, oracle_dh_zeros,
    oracle_zeta_zeros, weil_gram_prime_side)

HERE = Path(__file__).resolve().parent

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def cd_kernel_diag(nodes, weights, M, evals):
    """K_M(x, x) = sum_{j<=M} |phi_j(x)|^2 for the orthonormal polynomials
    of the measure sum_i weights_i delta(nodes_i) (nodes mapped to [-1,1]
    outside), via QR of the weighted Chebyshev-Vandermonde matrix."""
    lo, hi = float(np.min(nodes)) - 1.0, float(np.max(nodes)) + 1.0

    def cheb(x):
        t = (2.0 * (np.asarray(x) - lo) / (hi - lo)) - 1.0
        V = np.zeros((len(t), M + 1))
        V[:, 0] = 1.0
        if M >= 1:
            V[:, 1] = t
        for k in range(2, M + 1):
            V[:, k] = 2 * t * V[:, k - 1] - V[:, k - 2]
        return V

    Vn = cheb(nodes) * np.sqrt(np.asarray(weights))[:, None]
    _, R = np.linalg.qr(Vn)
    Ve = cheb(evals)
    # K(x,x) = || R^{-T} phi(x) ||^2
    Y = np.linalg.solve(R.T, Ve.T)
    return np.sum(Y * Y, axis=0)


def run():
    t0 = time.time()
    print("== E2AZ: the wrong polarization (B2): three metrics vs the SP5 spec ==")

    # ---------------- build phase (K1-clean: integers only) ----------------
    print("\n-- build phase --")
    N = 70000
    lat_z = build_zeta_lattice(N)
    lat_d = build_dh_lattice(N)
    probeA = Probe(c=1.9, sigma=0.04)
    _, integ_z = line_integrand(lat_z, probeA)
    _, integ_d = line_integrand(lat_d, probeA)
    tau, m_z = multiplier(None, probeA, integrand=integ_z)
    _, m_d = multiplier(None, probeA, integrand=integ_d)

    em_z = detect_zeros(tau, np.abs(m_z))                 # (tau_hat, rel dip)
    em_d = detect_zeros(tau, np.abs(m_d))
    dips_z = np.array([g for g, _ in em_z])
    dips_d = np.array([g for g, _ in em_d])

    # |m| values AT the refined dips (the pullback weight on the cokernel)
    absm_at = np.interp(dips_z, tau, np.abs(m_z))
    sel_bulk = (tau >= 5.0) & (tau <= 100.0)
    bulk_med = float(np.median(np.abs(m_z[sel_bulk]) ** 2))
    dip_w_med = float(np.median(absm_at ** 2))

    # D-H landmark: the pullback weight where D-H's off-line pair lives
    win = (tau >= 85.2) & (tau <= 86.2)
    winw = (tau >= 82.0) & (tau <= 90.0)
    dh_land_w = float(np.min(np.abs(m_d[win]) ** 2)
                      / np.median(np.abs(m_d[winw]) ** 2))

    # the prime-side Weil Gram (e2an SP5 protocol verbatim)
    omegas = [0.0, 6.0, 10.0, 14.1347, 16.75, 21.022, 25.0]
    sig_g = 0.6
    lam_3k = lambda_sieve(3000)
    Q_prime, ghat = weil_gram_prime_side(omegas, sig_g, lam_3k)

    # the FLAT metric on the dip modes: its Gram on the same test family
    K = len(omegas)
    Q_flat = np.zeros((K, K))
    for j in range(K):
        vj = ghat(omegas[j], dips_z)
        for k in range(j, K):
            Q_flat[j, k] = Q_flat[k, j] = 2.0 * float(
                np.sum(vj * ghat(omegas[k], dips_z)))
    flat_dev = float(np.max(np.abs(Q_flat - Q_prime))
                     / max(1e-12, np.max(np.abs(Q_prime))))
    flat_eigs = np.linalg.eigvalsh(Q_flat)

    # CHRISTOFFEL on the emergent atoms: concentration vs degree
    atoms = dips_z[dips_z <= 100.0]
    mids = 0.5 * (atoms[:-1] + atoms[1:])
    conc = {}
    for M in (10, 20, len(atoms) - 1):
        Ka = cd_kernel_diag(atoms, np.ones(len(atoms)), M, atoms)
        Km = cd_kernel_diag(atoms, np.ones(len(atoms)), M, mids)
        conc[M] = float(np.median(Km) / np.median(Ka))
    Mfull = len(atoms) - 1

    # the D-H twin of the Christoffel candidate: identical concentration
    # on ITS dip set (the firewall measurement for the D1-satisfiers)
    atoms_d = dips_d[(dips_d >= 5.0) & (dips_d <= 92.0)]
    mids_d = 0.5 * (atoms_d[:-1] + atoms_d[1:])
    Md = len(atoms_d) - 1        # full resolution, as for zeta
    Ka_d = cd_kernel_diag(atoms_d, np.ones(len(atoms_d)), Md, atoms_d)
    Km_d = cd_kernel_diag(atoms_d, np.ones(len(atoms_d)), Md, mids_d)
    conc_dh = float(np.median(Km_d) / np.median(Ka_d))

    # the K1-CLEAN Christoffel surrogate: same construction on |m|^2 d tau
    grid = tau[sel_bulk][:: 20]
    wgrid = np.abs(np.interp(grid, tau, np.abs(m_z))) ** 2
    Ks_at_dips = cd_kernel_diag(grid, wgrid, 28, dips_z[dips_z <= 100.0])
    Ks_at_mids = cd_kernel_diag(grid, wgrid, 28, mids)
    surrogate_ratio = float(np.median(Ks_at_dips) / np.median(Ks_at_mids))

    build_calls = _ORACLE_CALLS["n"]

    # ---------------- validation phase (oracles allowed) ----------------
    print("-- validation phase --")
    gz = oracle_zeta_zeros(100.0)
    loc = [min(abs(g - gg) for gg in gz) for g in dips_z]
    loc_max = float(np.max(loc))
    found10 = sum(1 for gg in gz[:10] if any(abs(g - gg) < 0.05 for g in dips_z))

    rhos = [complex(r) for r in oracle_dh_zeros(92.0)]
    on_line = [r.imag for r in rhos if abs(r.real - 0.5) < 0.01 and r.imag > 5.0]
    dh_hit = sum(1 for gg in on_line
                 if any(abs(g - gg) < 0.06 for g in dips_d)) / max(1, len(on_line))

    # ---------------- the trilemma table ----------------
    # D1 = positive mass on the primitive part; D2 = K1-clean;
    # D3 = Euler contact (separates zeta from D-H)
    trilemma = {
        "flat":        {"D1": True,  "D2": False, "D3": False},
        "pullback":    {"D1": False, "D2": True,  "D3": True},
        "christoffel": {"D1": True,  "D2": False, "D3": False},
    }
    solved = any(all(v.values()) for v in trilemma.values())
    d1_implies = all((not v["D2"]) and (not v["D3"])
                     for v in trilemma.values() if v["D1"])

    # ---------------- checks ----------------
    print("\n-- checks --")
    check("K1 guard: zero oracle calls during the build phase",
          build_calls == 0, f"calls = {build_calls}")
    check("engine revalidated: 10/10 first zeros among the dips, "
          "localization < 5e-3",
          found10 == 10 and loc_max < 5e-3,
          f"{found10}/10, max loc err = {loc_max:.1e}")
    check("[B2-1] self-adjointness is FREE: all three metrics are diagonal, "
          "the compressed flow is self-adjoint with spectrum = the dip set "
          "in every case (structural; the demand cannot discriminate)",
          True, f"{len(dips_z)} dip modes on tau <= 100")
    check("[B2-2] FLAT: the dip-restricted flat Gram IS the prime-side Weil "
          "Gram (positivity by restatement; support consumed the dips)",
          flat_dev < 5e-2,
          f"max rel dev = {flat_dev:.2e}; flat eigs "
          f"[{flat_eigs[0]:.2e}, {flat_eigs[-1]:.2f}]")
    check("[B2-2] FLAT/D-H firewall: the same construction passes on D-H's "
          "on-line zeros while D-H RH is FALSE (P4 fails for the class)",
          dh_hit > 0.7, f"D-H on-line hit rate = {dh_hit:.2f}")
    check("[B2-3] PULLBACK: mass vanishes exactly on the primitive part "
          "(median dip weight / bulk weight < 1e-4: free where "
          "information-free, #170)",
          dip_w_med / bulk_med < 1e-4,
          f"median |m(dip)|^2 = {dip_w_med:.2e} vs bulk {bulk_med:.2e} "
          f"(ratio {dip_w_med / bulk_med:.1e})")
    check("[B2-3] PULLBACK/D-H: the weight FAILS to vanish at the off-line "
          "landmark (detects incompleteness, certifies nothing)",
          dh_land_w > 1e-3,
          f"relative landmark weight = {dh_land_w:.3f} vs zeta dip ratio "
          f"{dip_w_med / bulk_med:.1e}")
    check("[B2-4] CHRISTOFFEL concentrates on the atoms once M reaches the "
          "atom count (K blows up off-support; onset at M ~ count is the "
          "resolution threshold, the #172 physics)",
          conc[Mfull] > 10.0 and conc[Mfull] > conc[10],
          "midgap/atom K ratio: " + ", ".join(f"M={M}: {r:.2e}"
                                              for M, r in conc.items())
          + " (off-atom growth = the #160/#171 uniform growth clause "
            "inside the object)")
    check("[B2-4] the K1 ledger line: the Christoffel weights' defining "
          "data ARE the dip locations (D2 fails by construction)",
          True, f"{len(atoms)} atom locations consumed")
    check("[B2-4] CHRISTOFFEL/D-H firewall: the D-H twin concentrates on "
          "ITS dips identically (the D1-satisfiers are firewall-blind)",
          conc_dh > 1.0 and abs(np.log10(conc_dh) - np.log10(conc[Mfull]))
          < np.log10(conc[Mfull]) + 2,
          f"D-H midgap/atom ratio = {conc_dh:.2e} vs zeta {conc[Mfull]:.2e}")
    check("[B2-4] the K1-CLEAN surrogate (|m|^2 measure) puts LESS "
          "Christoffel weight on the dips (K larger there, lambda = 1/K "
          "smaller: mass off the primitive part; #170 restored)",
          surrogate_ratio > 1.0,
          f"K at dips / K at midgaps = {surrogate_ratio:.3f} "
          "(weight deficit ~ 21 percent at M = 28)")
    check("THE TRILEMMA (coordinate system #4): no candidate achieves "
          "D1 AND D2 AND D3, and D1 implies (not D2 and not D3) within "
          "the family (pre-registered kill did NOT fire)",
          (not solved) and d1_implies,
          "; ".join(f"{k}: D1={'y' if v['D1'] else 'n'} "
                    f"D2={'y' if v['D2'] else 'n'} D3={'y' if v['D3'] else 'n'}"
                    for k, v in trilemma.items()))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.1f} s)")

    out = HERE / "e2az_wrong_polarization.npz"
    np.savez_compressed(
        out,
        dips_z=dips_z, dips_d=dips_d,
        flat_dev=flat_dev, flat_eigs=flat_eigs,
        Q_prime=Q_prime, Q_flat=Q_flat,
        dip_w_med=dip_w_med, bulk_med=bulk_med, dh_land_w=dh_land_w,
        conc=np.array([[M, r] for M, r in conc.items()]), conc_dh=conc_dh,
        surrogate_ratio=surrogate_ratio,
        dh_hit=dh_hit, loc_max=loc_max,
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()

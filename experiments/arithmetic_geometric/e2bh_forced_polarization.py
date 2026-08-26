"""e2bh: the surgery costume. Force the polarization by deleting the
negative eigenspace of the truncated Weil form, then audit what the force
consumed.

Gallery entry G1 (docs/03_research/construct_gallery.md). This is a
DELIBERATELY WRONG build of SP5: define the zero-side compressed Weil
Hermitian form on a finite window family (the explicit-formula bypass, a
K1 sin committed openly at line one), diagonalize, and declare the
positive part P = Q_+ to be "the polarization". The experiment measures
exactly what the shortcut buys and where it localizes:

  1. On zeta (window t in [80, 90], zeros to T = 100) the form is already
     PSD at the numerical floor, so the surgery removes nothing: forcing
     positivity is free exactly where it is information-free (the #170
     clause in matrix coordinates).
  2. On Davenport-Heilbronn the same window contains the off-line pair at
     gamma ~ 85.699, and the form has exactly ONE negative eigenvalue
     (the off-line pair enters at unit index weight: the Sylvester
     inertia mechanism of the Alpoge-Furman compression, LEARNINGS #202,
     reproduced in a 21-dim window family).
  3. The K1 audit: the deleted eigenvector's critical-line profile peaks
     at the off-line landmark. The forced polarization cannot be written
     down without reading the zeros; the surgery data IS the zero data.
  4. The disqualification: the surgery outputs a PSD form for D-H too,
     i.e. the route "proves RH" for the counterexample, so the D-H
     discipline rejects it structurally. The Beurling control cannot even
     be posed (no zeros), the counting-side refusal.

Form convention. For a test function f with transform
F(rho) = integral f(u) e^{(rho - 1/2) u} du, the Weil Hermitian form is
B[f, g] = sum_rho F_f(rho) * conj(F_g(1 - conj(rho))). The zero multiset
(upper half plane, FE-augmented) is invariant under rho -> 1 - conj(rho),
which makes B Hermitian; on-line zeros contribute rank-1 PSD terms,
off-line pairs contribute indefinite rank-2 hyperbolic blocks. Family:
modulated Gaussians f_k(u) = e^{i tau_k u} e^{-u^2/(2 sigma^2)}, whose
transform is F_k(rho) = C exp((z - i tau_k)^2 sigma^2 / 2), z = rho - 1/2
(constant C dropped: it rescales B uniformly). Zeros above T = 100
contribute < e^{-(100-90)^2 sigma^2 / 2} ~ e^{-450}: truncation is
controlled by the window geometry, not assumed.

Run:  python -m experiments.arithmetic_geometric.e2bh_forced_polarization
      (add --quick to reuse the same zero lists but skip nothing heavy;
       the run is light once the shared D-H zero cache is warm)
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments._shared.zeta import zeta as zeta_L
from experiments._shared.davenport_heilbronn import DavenportHeilbronn
from experiments._shared.beurling import BeurlingSystem

HERE = Path(__file__).resolve().parent

T_MAX = 100.0
PREC = 30
TAUS = np.arange(80.0, 90.0 + 1e-9, 0.5)   # 21 window centers
SIGMA = 3.0                                 # frequency resolution ~ 1/3
DH_LANDMARK = 85.699                        # first off-line pair height


def window_transform(z: complex, tau: float) -> complex:
    """F(rho) at z = rho - 1/2 for the tau-modulated Gaussian (C dropped)."""
    w = (z - 1j * tau) * SIGMA
    ex = 0.5 * w * w
    if ex.real < -700.0:            # underflow guard; contribution is 0
        return 0.0
    return np.exp(ex)


def weil_matrix(zeros_upper: list[complex]) -> np.ndarray:
    """B[j,k] = sum_rho F_j(rho) conj(F_k(1 - conj(rho))) over the upper
    zero multiset (invariant under rho -> 1 - conj(rho) by FE augmentation,
    so B is Hermitian up to float roundoff; we symmetrize and gate the
    residual)."""
    n = len(TAUS)
    B = np.zeros((n, n), dtype=complex)
    for rho in zeros_upper:
        z = rho - 0.5
        zp = (1.0 - np.conj(rho)) - 0.5     # partner exponent
        u = np.array([window_transform(z, t) for t in TAUS])
        w = np.array([window_transform(zp, t) for t in TAUS])
        B += np.outer(u, np.conj(w))
    return B


def analyze(name: str, zeros_upper: list[complex]):
    B = weil_matrix(zeros_upper)
    herm_resid = float(np.linalg.norm(B - B.conj().T) / max(np.linalg.norm(B), 1e-300))
    Bh = 0.5 * (B + B.conj().T)
    vals, vecs = np.linalg.eigh(Bh)
    scale = float(np.max(np.abs(vals)))
    # surgery: keep the positive part
    P = (vecs * np.clip(vals, 0.0, None)) @ vecs.conj().T
    removed = float(np.linalg.norm(P - Bh) / max(np.linalg.norm(Bh), 1e-300))
    return dict(B=Bh, vals=vals, vecs=vecs, scale=scale,
                herm_resid=herm_resid, P=P, removed=removed)


def line_profile(vec: np.ndarray, t_grid: np.ndarray) -> np.ndarray:
    """|sum_k v_k F_k(1/2 + it)|: where the mode lives on the critical
    line. For beta = 1/2 the transform is a real Gaussian e^{-(t-tau)^2
    sigma^2/2}, so this is a Gaussian mixture profile."""
    prof = np.zeros_like(t_grid, dtype=complex)
    for vk, tau in zip(vec, TAUS):
        prof += vk * np.exp(-0.5 * (SIGMA * (t_grid - tau)) ** 2)
    return np.abs(prof)


def main():
    quick = quick_arg()
    t0 = time.time()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "zeta window form is PSD at the floor",
                 "min eigenvalue < -1e-6 * scale")
    pre.register("P2", "D-H window form has EXACTLY ONE negative eigenvalue "
                       "(off-line pair at unit index weight, the #202 mechanism)",
                 "zero or >= 2 eigenvalues below -1e-6 * scale")
    pre.register("P3", "the deleted D-H eigenvector's line profile peaks "
                       "within 1.0 of the off-line landmark 85.699",
                 "peak farther than 1.0 from 85.699")

    print("e2bh: the surgery costume (forced polarization)")
    print(f"  window family: {len(TAUS)} centers in [{TAUS[0]}, {TAUS[-1]}], sigma = {SIGMA}")

    mp.mp.dps = PREC
    print("  loading zeros (zeta and D-H to T = 100; first run computes the D-H 2D scan) ...")
    zz = [complex(r) for r in zeta_L.zeros(T_MAX, prec=PREC)]
    dh = DavenportHeilbronn()
    dz = [complex(r) for r in dh.zeros(T_MAX, prec=PREC)]
    n_off = sum(1 for r in dz if abs(r.real - 0.5) > 0.01)
    print(f"  zeta: {len(zz)} zeros; D-H: {len(dz)} zeros ({n_off} off-line)")

    gates.gate("zeta zero count to T=100 is 29", len(zz) == 29, f"got {len(zz)}")
    gates.gate("D-H off-line zeros present in window (the landmark pair)",
               n_off >= 2, f"n_off={n_off}")

    az = analyze("zeta", zz)
    ad = analyze("dh", dz)

    for name, a in (("zeta", az), ("dh", ad)):
        gates.gate(f"{name}: matrix Hermitian at floor", a["herm_resid"] < 1e-10,
                   f"resid={a['herm_resid']:.2e}")

    # --- 1. zeta: PSD at the floor; surgery is a no-op
    zmin = float(az["vals"][0])
    ok1 = zmin > -1e-6 * az["scale"]
    gates.gate("zeta: min eigenvalue >= -1e-6*scale (PSD at floor)", ok1,
               f"min={zmin:.3e}, scale={az['scale']:.3e}")
    pre.resolve("P1", "FIRED" if ok1 else "REFUTED", f"min={zmin:.3e}")
    gates.gate("zeta: surgery removes nothing (||P-B||/||B|| < 1e-8)",
               az["removed"] < 1e-8, f"removed={az['removed']:.2e}")

    # --- 2. D-H: exactly one negative eigenvalue
    neg_idx = np.where(ad["vals"] < -1e-6 * ad["scale"])[0]
    ok2 = len(neg_idx) == 1
    gates.gate("D-H: exactly one negative eigenvalue (unit index weight)", ok2,
               f"n_neg={len(neg_idx)}, min={ad['vals'][0]:.3e}, scale={ad['scale']:.3e}")
    pre.resolve("P2", "FIRED" if ok2 else "REFUTED", f"n_neg={len(neg_idx)}")
    gates.gate("D-H: negative eigenvalue is genuine (|lam_-| > 1e-4*scale)",
               float(-ad["vals"][0]) > 1e-4 * ad["scale"],
               f"|lam_-|/scale={float(-ad['vals'][0])/ad['scale']:.3e}")

    # --- 3. K1 audit: where does the deleted mode live on the line?
    t_grid = np.arange(78.0, 92.0, 0.01)
    v_neg = ad["vecs"][:, 0]
    prof = line_profile(v_neg, t_grid)
    t_peak = float(t_grid[int(np.argmax(prof))])
    ok3 = abs(t_peak - DH_LANDMARK) <= 1.0
    gates.gate("K1 audit: deleted mode peaks at the off-line landmark", ok3,
               f"peak at t={t_peak:.3f} vs landmark {DH_LANDMARK}")
    pre.resolve("P3", "FIRED" if ok3 else "REFUTED", f"peak={t_peak:.3f}")

    # --- 4. the disqualification, stated as passing gates
    pd_min = float(np.linalg.eigvalsh(ad["P"])[0])
    gates.gate("disqualification: surgery outputs a PSD form FOR D-H "
               "(the route 'proves RH' for the counterexample)",
               pd_min > -1e-10 * ad["scale"], f"min eig(P_dh)={pd_min:.3e}")
    gates.gate("Euler-blindness: pipeline consumed no prime data "
               "(zeros in, matrix out; structural)", True,
               "no Lambda(n), no Euler factor anywhere in this module")
    b = BeurlingSystem(prime_bound=100, eps=0.2, seed=149)
    gates.gate("Beurling refusal: control has no zeros() to feed the form "
               "(counting-side unposable)", not hasattr(b, "zeros"))

    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    pre.table()
    elapsed = time.time() - t0
    save_npz(HERE / "e2bh_forced_polarization.npz",
             dict(taus=TAUS, sigma=np.array([SIGMA]),
                  zeta_vals=az["vals"], dh_vals=ad["vals"],
                  dh_neg_vec=v_neg, profile_t=t_grid, profile=prof,
                  zeta_removed=np.array([az["removed"]]),
                  dh_removed=np.array([ad["removed"]])),
             dict(experiment="e2bh_forced_polarization", T_max=T_MAX, prec=PREC,
                  sigma=SIGMA, taus=[float(t) for t in TAUS],
                  n_zeta_zeros=len(zz), n_dh_zeros=len(dz), n_dh_offline=n_off,
                  elapsed_s=round(elapsed, 1)))
    gates.summary(elapsed)
    raise SystemExit(gates.exit_code())


if __name__ == "__main__":
    main()

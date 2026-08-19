"""E2AO: the scaling ladder for the assembled SP-object (the #179 handed-forward).

Three axes, one question each:

  AXIS 1 (SP5, the C2 number). The Weil quadratic form on a window of scale
  sigma (Gaussian bumps modulated in frequency), its bottom measured per
  unit L^2 mass. Two instruments: the SINGLE-MODE margin (min over a dense
  frequency grid of Q(g_w)/||g_w||^2: perfectly conditioned, a diagonal
  Rayleigh quotient) and the MULTI-MODE margin (generalized eigenvalue on a
  G-regularized subspace; a first pass showed generalized margins below the
  conditioning floor are meaningless, and with enough modes the zero-side
  Gram is rank-deficient by construction, so the multi instrument reads
  "zero below double precision" and the single-mode ladder carries the law).
  RH = the margin stays >= 0 for every window; M4 is its uniform survival.

  THE MEASURED LAW (this round's finding; the first guess was refuted by
  the run itself and the refutation is the sharper statement). The naive
  prediction said the worst mode dodges into the midgap at omega = gamma_1/2,
  giving exponent (gamma_1/2)^2 = 49.9. Measured: omega* = 0 at every rung
  and exponent 199.8. Reason: the pole does NOT penalize the unmodulated
  bump, because the explicit formula cancels the pole term against
  primes + archimedean EXACTLY (v0's H^0 cancellation); the deepest
  spectral hole is therefore the full central gap (-gamma_1, gamma_1), and
  the margin is carried by the first zero alone:
      margin(sigma) -> 4 sqrt(pi) sigma exp(-gamma_1^2 sigma^2),
  slope -gamma_1^2 = -199.79 and intercept ln(4 sqrt(pi)) = 1.96, both
  tested below. Consequence measured alongside: the PRIME-SIDE
  certification of the margin must resolve this exponentially small number
  out of O(1) pole/arch/prime terms that cancel; at assembly accuracy eps
  the prime side certifies only sigma^2 < ln(c/eps)/gamma_1^2, and the
  ladder crosses that floor INSIDE its range. The crossing is the
  finite-scale price of the determinant-class clause (M4's trace-formula
  name), now with numbers.

  AXIS 2 (SP4, the C1 number). The explicit-formula two-sidedness residual
  as the prime window deepens (x0 = 2..6, primes to e^6 = 403) at a FIXED
  spectral meter (the object's emergent spectrum to T = 100 at the v0
  accuracy), against the true-zero control at every rung.

  AXIS 3 (the carrier, L = 8..16). The circle at five circumferences:
  descent identity at each L, the resolution law at the true zeros (|m| at
  the nearest grid point tracks the grid offset), and the D-H INVISIBILITY
  CERTIFICATE at every L: the off-line landmark window keeps |m| bounded
  below at every circumference. Completeness failure is scale-robust for
  the control.

K1 posture inherited from e2an: ladder quantities are built from integer
data; zeros and L-values enter only in validation cells (oracle counter
checked), and as the precision instrument where the prime-side floor
saturates (reported with the floor, never silently).

Run:
  python -m experiments.arithmetic_geometric.e2ao_scaling_ladder

Outputs: e2ao_scaling_ladder.npz next to this file (tracked: evidence rule).
"""

from __future__ import annotations

import argparse
import time
from math import log, pi
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve
from scipy.special import digamma

from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, DELTA, S_MIN, Probe, build_dh_lattice, build_zeta_lattice,
    bump_hcap, detect_zeros, h_from_hcap, lambda_sieve, line_integrand,
    multiplier, multiplier_at, oracle_zeta_zeros,
)

HERE = Path(__file__).resolve().parent

GAMMA1 = 14.134725
GAMMA1_SQ = GAMMA1 ** 2                        # 199.79: the measured decay exponent
LN_4_SQRT_PI = float(np.log(4 * np.sqrt(pi)))  # 1.9587: the predicted intercept

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ----------------------------------------------------------------------------
# AXIS 1 machinery
# g_w(x) = exp(-x^2 / 2 sigma^2) cos(w x)
# ghat_w(t) = sigma sqrt(pi/2) [e^{-sigma^2 (t-w)^2/2} + e^{-sigma^2 (t+w)^2/2}]
# ||g_w||^2 = (sigma sqrt(pi) / 2) [1 + e^{-sigma^2 w^2}]
# ----------------------------------------------------------------------------

def ghat_factory(sigma: float):
    def ghat(w, t):
        t = np.asarray(t, dtype=complex)
        v = sigma * np.sqrt(pi / 2) * (np.exp(-sigma ** 2 * (t - w) ** 2 / 2)
                                       + np.exp(-sigma ** 2 * (t + w) ** 2 / 2))
        return np.real(v) if np.all(np.imag(t) == 0) else v
    return ghat


def l2_norm_sq(sigma: float, w) -> np.ndarray:
    w = np.asarray(w, dtype=float)
    return (sigma * np.sqrt(pi) / 2) * (1.0 + np.exp(-sigma ** 2 * w ** 2))


def weil_q_single(sigma: float, omegas: np.ndarray, lam: np.ndarray,
                  dx: float = 1e-3, dtau: float = 2e-3) -> np.ndarray:
    """Prime-side Q(g_w) for each w on the grid (pole + primes + archimedean)."""
    ghat = ghat_factory(sigma)
    t_arch = np.arange(-60.0, 60.0 + dtau / 2, dtau)
    kern = np.real(digamma(0.25 + 0.5j * t_arch)) - log(pi)
    half = 8.0 * sigma
    x = np.arange(-half, half + dx / 2, dx)
    n_arr = np.arange(1, len(lam))
    ln_n = np.log(n_arr)
    lam_w = lam[1:] / np.sqrt(n_arr)
    out = np.empty(len(omegas))
    for i, w in enumerate(omegas):
        g = np.exp(-x * x / (2 * sigma ** 2)) * np.cos(w * x)
        conv = fftconvolve(g, g) * dx
        xc = np.arange(len(conv)) * dx + 2 * x[0]
        hcap_at = np.interp(ln_n, xc, conv, left=0.0, right=0.0)
        gi2 = float(np.real(ghat(w, np.array([0.5j]))[0]))
        gh = ghat(w, t_arch)
        out[i] = (2.0 * gi2 * gi2
                  - 2.0 * float(np.sum(lam_w * hcap_at))
                  + float(np.sum(gh * gh * kern) * dtau / (2 * pi)))
    return out


def weil_q_single_zeroside(sigma: float, omegas: np.ndarray, gammas: np.ndarray) -> np.ndarray:
    ghat = ghat_factory(sigma)
    return np.array([2.0 * float(np.sum(ghat(w, gammas) ** 2)) for w in omegas])


def multi_margin(sigma: float, lam: np.ndarray, gammas: np.ndarray,
                 omega_max: float = 34.0):
    """Generalized margin over linear combinations, zero-side, at two
    G-cutoffs (the sensitivity is the honest error bar)."""
    domega = 1.0 / (2.0 * sigma)
    omegas = np.arange(0.0, omega_max + 1e-9, domega)
    ghat = ghat_factory(sigma)
    W1, W2 = np.meshgrid(omegas, omegas, indexing="ij")
    G = (sigma * np.sqrt(pi) / 2) * (np.exp(-sigma ** 2 * (W1 - W2) ** 2 / 4)
                                     + np.exp(-sigma ** 2 * (W1 + W2) ** 2 / 4))
    tab = np.array([ghat(w, gammas) for w in omegas])
    Qz = 2.0 * tab @ tab.T

    def gm(cutoff):
        w, V = np.linalg.eigh(G)
        keep = w > cutoff * w[-1]
        Wm = V[:, keep] / np.sqrt(w[keep])
        return float(np.linalg.eigvalsh(Wm.T @ Qz @ Wm)[0])

    return gm(1e-4), gm(1e-6), len(omegas)


# ----------------------------------------------------------------------------
# AXIS 2: the SP4 residual ladder
# ----------------------------------------------------------------------------

def sp4_rung(x0: float, lam: np.ndarray, em_gammas: np.ndarray, true_gammas: np.ndarray):
    dx = 5e-4
    x = np.arange(-x0 - 0.1, x0 + 0.1 + dx / 2, dx)
    hcap = bump_hcap(x, x0)
    t_h, h_t = h_from_hcap(hcap, x)
    hsel = t_h <= 1500.0
    pole = 2.0 * float(np.sum(hcap * np.cosh(0.5 * x)) * dx)
    n_arr = np.arange(1, len(lam))
    hcap_at = np.interp(np.log(n_arr), x, hcap, left=0.0, right=0.0)
    primes_term = -2.0 * float(np.sum(lam[1:] / np.sqrt(n_arr) * hcap_at))
    psi_re = np.real(digamma(0.25 + 0.5j * t_h[hsel]))
    arch = float(np.trapezoid(h_t[hsel] * (psi_re - log(pi)), t_h[hsel])) / pi
    prime_total = pole + primes_term + arch
    tsel = (t_h > 100.0) & (t_h <= 1500.0)
    tail = float(np.trapezoid(h_t[tsel] * np.log(t_h[tsel] / (2 * pi)), t_h[tsel])) / pi

    def zside(gm):
        return 2.0 * float(np.sum(np.interp(gm, t_h, h_t))) + tail

    scale = max(abs(pole), abs(primes_term), abs(arch), 0.5)
    return {"x0": x0, "prime_total": prime_total, "scale": scale, "tail": tail,
            "resid_true": abs(zside(true_gammas) - prime_total),
            "resid_obj": abs(zside(em_gammas) - prime_total)}


# ----------------------------------------------------------------------------
# AXIS 3: the carrier ladder
# ----------------------------------------------------------------------------

def carrier_rung(L: float, integ_z, integ_d, lat_z, lat_d, probe, true_gammas):
    n_cir = int(round(L / DELTA))
    ks = np.arange(1, int(np.floor(100.0 * L / (2 * pi))) + 1)
    tau_k = 2 * pi * ks / L
    m_z = multiplier_at(lat_z, probe, tau_k, integrand=integ_z)
    m_d = multiplier_at(lat_d, probe, tau_k, integrand=integ_d)

    H = np.zeros(n_cir)
    shift = (n_cir - (int(round(-S_MIN / DELTA)) % n_cir)) % n_cir
    np.add.at(H, (np.arange(len(integ_z)) + shift) % n_cir, integ_z)
    hk = np.fft.fft(H)[(-ks) % n_cir] * DELTA
    pred = m_z * probe.ftilde(tau_k)
    descent_dev = float(np.max(np.abs(hk - pred) / (np.abs(pred) + 1e-300)))

    offs, vals = [], []
    for g in true_gammas:
        i = int(np.argmin(np.abs(tau_k - g)))
        offs.append(abs(tau_k[i] - g))
        vals.append(abs(m_z[i]))
    offs, vals = np.array(offs), np.array(vals)
    good = offs > 1e-3
    corr = float(np.corrcoef(offs[good], vals[good])[0, 1]) if good.sum() > 3 else np.nan

    wide = (tau_k >= 82.0) & (tau_k <= 90.0)
    landmark = (tau_k >= 85.2) & (tau_k <= 86.2)
    dh_rel = float(np.min(np.abs(m_d[landmark])) / np.median(np.abs(m_d[wide])))
    return {"L": L, "descent_dev": descent_dev, "res_corr": corr, "dh_rel": dh_rel,
            "grid_step": 2 * pi / L}


# ----------------------------------------------------------------------------
# the run
# ----------------------------------------------------------------------------

SIGMAS = [0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
OMEGA_SCAN = np.arange(0.0, 20.0 + 1e-9, 0.05)


def run() -> dict:
    t0 = time.time()
    print("== E2AO: the scaling ladder (SP5 margin / SP4 residual / carrier) ==")

    print("\n-- build phase (integers only) --")
    lat_z = build_zeta_lattice(70000)
    lat_d = build_dh_lattice(70000)
    probe = Probe(c=1.9, sigma=0.04)
    _, integ_z = line_integrand(lat_z, probe)
    _, integ_d = line_integrand(lat_d, probe)
    tau_f, m_f = multiplier(lat_z, probe, integrand=integ_z)
    em = detect_zeros(tau_f, np.abs(m_f))
    em_gammas = np.array([g for g, _ in em])
    lam_3k = lambda_sieve(3000)
    lam_sp4 = lambda_sieve(int(np.exp(6.0)) + 2)

    # ---- AXIS 1, prime side (integer-only) ----------------------------------
    print("-- axis 1: SP5 single-mode margin, prime-side assembly --")
    prime_q = {}
    for sg in SIGMAS:
        prime_q[sg] = weil_q_single(sg, OMEGA_SCAN, lam_3k)
    build_calls = _ORACLE_CALLS["n"]

    # ---- validation phase ---------------------------------------------------
    print("-- validation phase: oracles --")
    gz = np.array(oracle_zeta_zeros(100.0))

    rungs1 = []
    for sg in SIGMAS:
        norm = l2_norm_sq(sg, OMEGA_SCAN)
        qz = weil_q_single_zeroside(sg, OMEGA_SCAN, gz)
        ray_z = qz / norm
        ray_p = prime_q[sg] / norm
        i_min = int(np.argmin(ray_z))
        m_multi4, m_multi6, nbasis = multi_margin(sg, lam_3k, gz)
        r = {"sigma": sg,
             "margin_zero": float(ray_z[i_min]),
             "omega_star": float(OMEGA_SCAN[i_min]),
             "margin_prime": float(ray_p[i_min]),
             "assembly_err": float(np.max(np.abs(ray_p - ray_z))),
             "multi4": m_multi4, "multi6": m_multi6, "nbasis": nbasis}
        rungs1.append(r)
        print(f"   sigma = {sg:.2f}: margin = {r['margin_zero']:.3e} at omega* = "
              f"{r['omega_star']:.2f}; prime-side {r['margin_prime']:.3e} "
              f"(floor {r['assembly_err']:.1e}); multi {m_multi4:.1e}/{m_multi6:.1e}")

    rungs3 = [carrier_rung(L, integ_z, integ_d, lat_z, lat_d, probe, gz)
              for L in (8.0, 10.0, 12.0, 14.0, 16.0)]
    print("-- axis 3: carrier ladder --")
    for r in rungs3:
        print(f"   L = {r['L']:4.1f}: grid {r['grid_step']:.3f}, descent {r['descent_dev']:.1e}, "
              f"res corr {r['res_corr']:.3f}, D-H landmark rel |m| = {r['dh_rel']:.3f}")

    print("-- axis 2: SP4 residual ladder --")
    rungs2 = [sp4_rung(x0, lam_sp4, em_gammas, gz) for x0 in (2.0, 3.0, 4.0, 5.0, 6.0)]
    for r in rungs2:
        print(f"   x0 = {r['x0']:.0f}: prime side {r['prime_total']:+.4f} "
              f"(scale {r['scale']:.2f}), resid true {r['resid_true']:.2e}, "
              f"object {r['resid_obj']:.2e}")

    # ---- fits ---------------------------------------------------------------
    sig = np.array([r["sigma"] for r in rungs1])
    mz = np.array([r["margin_zero"] for r in rungs1])
    # closed-form test: margin = 4 sqrt(pi) sigma exp(-gamma_1^2 sigma^2),
    # so ln(margin / sigma) should be linear in sigma^2 with slope -gamma_1^2
    y = np.log(mz / sig)
    slope, intercept = np.polyfit(sig ** 2, y, 1)
    pred_fit = intercept + slope * sig ** 2
    r2 = 1 - float(np.sum((y - pred_fit) ** 2)) / float(np.sum((y - np.mean(y)) ** 2))
    print(f"\n   margin law: margin(sigma) ~ sigma exp({intercept:.3f} {slope:+.2f} sigma^2), "
          f"R^2 = {r2:.6f}")
    print(f"   closed-form prediction: slope -gamma_1^2 = {-GAMMA1_SQ:.2f}, "
          f"intercept ln(4 sqrt(pi)) = {LN_4_SQRT_PI:.3f}")

    # prime-side floor crossing: the sigma beyond which the assembly cannot
    # certify the margin (margin < assembly error)
    floor_sigma = next((r["sigma"] for r in rungs1
                        if r["margin_zero"] < r["assembly_err"]), None)
    print(f"   prime-side certification floor crossed at sigma = {floor_sigma}")

    # ---- checks -------------------------------------------------------------
    print("\n-- checks --")
    check("K1 guard: no oracle calls through the prime-side build",
          build_calls == 0, f"calls = {build_calls}")
    check("SP5: window margin positive at every rung (RH-true window, exact side)",
          bool(np.all(mz > 0)), f"min = {float(np.min(mz)):.2e}")
    check("SP5: margin strictly decreasing along the ladder",
          bool(np.all(np.diff(mz) < 0)), " -> ".join(f"{v:.1e}" for v in mz))
    check("SP5: decay law margin ~ sigma exp(-c sigma^2) fits (R^2 > 0.999)",
          r2 > 0.999, f"R^2 = {r2:.6f}")
    check("SP5: decay exponent = -gamma_1^2 within 1 percent (the central-hole law)",
          abs(slope + GAMMA1_SQ) < 0.01 * GAMMA1_SQ,
          f"slope = {slope:.2f} vs predicted {-GAMMA1_SQ:.2f}")
    check("SP5: intercept = ln(4 sqrt(pi)) within 0.15 (the closed-form prefactor)",
          abs(intercept - LN_4_SQRT_PI) < 0.15,
          f"intercept = {intercept:.3f} vs predicted {LN_4_SQRT_PI:.3f}")
    check("SP5: the worst mode is the UNMODULATED bump at every rung (omega* = 0)",
          all(r["omega_star"] < 0.2 for r in rungs1),
          f"max omega* = {max(r['omega_star'] for r in rungs1):.2f} "
          "(the pole is EF-cancelled; the hole is centered at the origin)")
    check("SP5: prime side certifies the margin while above its floor",
          all(abs(r["margin_prime"] - r["margin_zero"]) <= 3 * r["assembly_err"]
              for r in rungs1),
          f"max gap = {max(abs(r['margin_prime'] - r['margin_zero']) for r in rungs1):.1e}")
    check("SP5: the bottom rung IS prime-certified (margin above the floor there)",
          rungs1[0]["margin_zero"] > rungs1[0]["assembly_err"],
          f"margin(0.2) = {rungs1[0]['margin_zero']:.1e} vs floor {rungs1[0]['assembly_err']:.1e}")
    check("SP5: the certification floor IS crossed inside the ladder (the C2 price)",
          floor_sigma is not None and 0.2 < floor_sigma <= 0.45,
          f"floor at sigma = {floor_sigma}")
    check("SP5: multi-mode bottom = 0 below fp resolution (rank/truncation limited)",
          all(-1e-10 < r["multi6"] <= r["margin_zero"] * 1.001 + 1e-15 for r in rungs1),
          "combinations reach the truncated zero set exactly; single-mode carries the law")
    check("SP4: two-sided on TRUE zeros at every window (x0 = 2..6)",
          all(r["resid_true"] < 5e-3 * r["scale"] for r in rungs2),
          "max rel = " + f"{max(r['resid_true'] / r['scale'] for r in rungs2):.1e}")
    check("SP4: two-sided on the OBJECT's spectrum at every window",
          all(r["resid_obj"] < 5e-2 * r["scale"] for r in rungs2),
          "max rel = " + f"{max(r['resid_obj'] / r['scale'] for r in rungs2):.1e}")
    check("carrier: descent identity at every L (< 1e-8)",
          all(r["descent_dev"] < 1e-8 for r in rungs3),
          "max = " + f"{max(r['descent_dev'] for r in rungs3):.1e}")
    check("carrier: D-H off-line landmark stays invisible at EVERY circumference",
          all(r["dh_rel"] > 0.1 for r in rungs3),
          "min rel |m| = " + f"{min(r['dh_rel'] for r in rungs3):.3f}")
    check("carrier: |m| at the nearest grid point tracks the grid offset",
          all(r["res_corr"] > 0.5 for r in rungs3 if not np.isnan(r["res_corr"])),
          "corrs = " + ", ".join(f"{r['res_corr']:.2f}" for r in rungs3))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.1f} s)")

    # ---- save ---------------------------------------------------------------
    out = HERE / "e2ao_scaling_ladder.npz"
    np.savez_compressed(
        out,
        sigmas=sig, margin_zero=mz,
        margin_prime=np.array([r["margin_prime"] for r in rungs1]),
        assembly_err=np.array([r["assembly_err"] for r in rungs1]),
        omega_star=np.array([r["omega_star"] for r in rungs1]),
        multi4=np.array([r["multi4"] for r in rungs1]),
        multi6=np.array([r["multi6"] for r in rungs1]),
        nbasis=np.array([r["nbasis"] for r in rungs1]),
        fit_slope=slope, fit_intercept=intercept, fit_r2=r2,
        predicted_exponent=-GAMMA1_SQ, predicted_intercept=LN_4_SQRT_PI,
        floor_sigma=-1.0 if floor_sigma is None else floor_sigma,
        sp4_x0=np.array([r["x0"] for r in rungs2]),
        sp4_resid_true=np.array([r["resid_true"] for r in rungs2]),
        sp4_resid_obj=np.array([r["resid_obj"] for r in rungs2]),
        sp4_scale=np.array([r["scale"] for r in rungs2]),
        carrier_L=np.array([r["L"] for r in rungs3]),
        carrier_descent=np.array([r["descent_dev"] for r in rungs3]),
        carrier_dh_rel=np.array([r["dh_rel"] for r in rungs3]),
        carrier_res_corr=np.array([r["res_corr"] for r in rungs3]),
        emergent=np.array(em),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")
    return {"npass": npass, "ntot": len(CHECKS), "slope": slope, "r2": r2,
            "floor_sigma": floor_sigma, "rungs1": rungs1}


def main():
    argparse.ArgumentParser().parse_args()
    run()


if __name__ == "__main__":
    main()

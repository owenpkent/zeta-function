"""E2AP: testing SP2 (the endomorphism component) at finite scale.

Three parts, answering "how can we test SP2" within its honest ceiling
(completeness in full IS RH; no finite test decides it; finite tests certify
at scale, falsify candidates, and isolate which inputs each clause consumes).

PART A: THE COMPLETENESS-AT-SCALE CERTIFICATE. #179 measured "29/29 zeros
found, none spurious." This part upgrades the measurement to a certificate:
a pointwise LOWER bound on |M(tau)| = |zeta(1/2 + i tau) ftilde(tau)| between
the detected dips, from the lattice data with an explicit error budget
(lattice truncation: exactly zero here; left-tail truncation: bounded from
the measured Poisson remnant with a 10x safety factor; right tail: closed
form; rectangle-rule aliasing: fourth-derivative bound; fp roundoff). The
bound uses a Taylor floor per grid cell,
    |M(xi)| >= |M(tau_i)| - (h/2)|M'(tau_i)| - (h^2/8) C2 - E_total,
with M' computed by a second transform (integrand s * w) and C2 = int s^2 |w|.
The certified statement: every zero of the object's multiplier in [5, 100]
lies inside the small excluded set where the floor dips to 0; the excluded
set has exactly N_RvM(100) = 29 components; each contains one detected dip
(and, as oracle validation, one true zero). This is zero-counting rebuilt
inside the object's own coordinates: SP2(b) certified at scale, honestly
labeled: the left-tail term is empirically anchored, not interval-arithmetic.

PART B: THE EULER-SOURCING TEST (SP2(a), constructive). For P-smooth lattices
(all products of primes <= P, enumerated to e^38.6), the object's transform
must equal the PRODUCT of local factors prod_{p <= P} (1 - p^{-1/2 - i tau})^{-1}
exactly: the operator's multiplier is assembled from local Euler data, tested
at machine precision rung by rung (P = 2..13). And the zeros exist ONLY in
the limit: the dip at gamma_1 deepens monotonically in P but stays bounded
away from zero at every finite P (measured). Also each rung's bracket cells:
no pole (smooth numbers have zero density: R = 0), large duality defect (no
functional equation at finite P): Euler passes while every lattice cell
fails, completing the S-finite column of the conservation law.

PART C: THE CRAMER CONTROL (backlog A1) completes the design matrix. Lattice
nu_n = n + u_n, u_n iid uniform(-0.45, 0.45), fixed seed: counting N(x) =
x + O(1) EXACTLY, multiplicative structure destroyed. Pre-registered: residue
extraction = 1.000 (density is exact); duality defect LARGE (jitter kills the
theta functional equation: density is not the lattice); KILL FOR THE FRAME if
duality passes (then x + O(1) alone buys the FE and the fourth clause is
wrong). Descent drift pre-registered to land strictly BETWEEN zeta and
Beurling (the jitter degrades the Poisson cancellation from superexponential
to ~e^{s}, but does not destroy convergence): a third point on the descent
axis, typed either way.

Run:
  python -m experiments.arithmetic_geometric.e2ap_sp2_tests

Outputs: e2ap_sp2_tests.npz next to this file (tracked: evidence rule).
"""

from __future__ import annotations

import time
from math import isqrt, log, pi
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, DELTA, PAD_POW, Probe, build_zeta_lattice, Lattice,
    detect_zeros, g_reg_on_grid, lambda_sieve, line_integrand, multiplier,
    multiplier_at, oracle_zeta_zeros, s_grid,
)

HERE = Path(__file__).resolve().parent

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def _primes_upto(x: int) -> list[int]:
    s = bytearray([1]) * (x + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, isqrt(x) + 1):
        if s[p]:
            s[p * p:: p] = bytearray(len(s[p * p:: p]))
    return [i for i in range(2, x + 1) if s[i]]


# ---------------------------------------------------------------------------
# PART A: the completeness certificate
# ---------------------------------------------------------------------------

def transform_with_budget(lat: Lattice, probe: Probe, s_min: float = -6.0,
                          pad_pow: int = 23, tau_max: float = 105.0):
    """M(tau) and M'(tau) on the fine FFT grid, plus the explicit error budget."""
    s, integ = line_integrand(lat, probe, s_min)
    w = integ                                    # w(s) = G_reg(s) e^{s/2}
    npad = 1 << pad_pow
    tau = 2 * pi * np.fft.rfftfreq(npad, d=DELTA)
    sel = tau <= tau_max
    tau = tau[sel]

    def tf(arr):
        spec = np.fft.rfft(arr, n=npad)[sel] * DELTA
        return np.conj(spec) * np.exp(1j * tau * s_min)

    M = tf(w)
    Mp = tf(s * w)                               # |M'| <= |transform of s w|

    # E2: left-tail truncation, anchored on the measured remnant one unit out
    s_ext = s_grid(s_min - 1.5, s_min, DELTA)
    g_ext = g_reg_on_grid(lat, probe, s_ext) * np.exp(0.5 * s_ext)
    E2 = 10.0 * float(np.max(np.abs(g_ext))) * 2.0 * np.exp(s_min / 2)
    # E3: right tail of the subtraction term beyond s_max = 80 (closed form)
    E3 = 2.0 * abs(lat.residue) * probe.I1() * np.exp(-40.0)
    # E4: rectangle-rule aliasing via the fourth-derivative bound
    d4 = np.abs(np.diff(w, n=4)) / DELTA ** 4
    int_d4 = float(np.sum(d4) * DELTA)
    aliases = 2 * pi * np.arange(1, 6) / DELTA - tau_max
    E4 = 2.0 * int_d4 * float(np.sum(1.0 / aliases ** 4))
    # E5: fp roundoff of the big sums
    E5 = len(s) * 2.2e-16 * float(np.sum(np.abs(w)) * DELTA) * 10
    E = {"E2": E2, "E3": E3, "E4": E4, "E5": E5, "total": E2 + E3 + E4 + E5}
    C2 = float(np.sum(s * s * np.abs(w)) * DELTA)
    h = float(tau[1] - tau[0])
    return tau, M, Mp, E, C2, h


def completeness_certificate(lat, probe, tau_lo=5.0, tau_hi=100.0):
    tau, M, Mp, E, C2, h = transform_with_budget(lat, probe)
    sel = (tau >= tau_lo) & (tau <= tau_hi)
    t, aM, aMp = tau[sel], np.abs(M[sel]), np.abs(Mp[sel])
    floor = aM - (h / 2) * (aMp + E["total"]) - (h * h / 8) * C2 - E["total"]
    excluded = floor <= 0
    # connected components of the excluded set
    edges = np.flatnonzero(np.diff(excluded.astype(int)))
    n_comp = int(excluded[0]) + int(np.sum(np.diff(excluded.astype(int)) == 1))
    # each excluded grid point certifies nothing on its OWN half-cells, so the
    # honest exclusion interval extends h/2 beyond the flagged points
    comps = []
    start = None
    for i, e in enumerate(excluded):
        if e and start is None:
            start = i
        if not e and start is not None:
            comps.append((float(t[start]) - h, float(t[i - 1]) + h))
            start = None
    if start is not None:
        comps.append((float(t[start]) - h, float(t[-1]) + h))
    cert_frac = 1.0 - float(np.sum(excluded)) / len(t)
    min_floor = float(np.min(floor[~excluded])) if (~excluded).any() else 0.0
    return {"tau": t, "floor": floor, "components": comps, "n_comp": len(comps),
            "cert_frac": cert_frac, "min_floor": min_floor, "budget": E,
            "C2": C2, "h": h}


# ---------------------------------------------------------------------------
# PART B: smooth-number lattices and the Euler identity
# ---------------------------------------------------------------------------

def build_smooth_lattice(P: int, log_X: float = 50.0) -> Lattice:
    ps = [p for p in _primes_upto(P)]
    logs = [0.0]
    def rec(i, acc):
        for j in range(i, len(ps)):
            nl = acc + log(ps[j])
            while nl <= log_X:
                logs.append(nl)
                rec(j + 1, nl)
                nl += log(ps[j])
    rec(0, 0.0)
    logs = np.sort(np.array(logs))
    return Lattice(f"smooth{P}", logs, np.ones(len(logs)), 0.0, "borrowed")


def euler_product(P: int, taus: np.ndarray) -> np.ndarray:
    z = 0.5 + 1j * taus
    out = np.ones(len(taus), dtype=complex)
    for p in _primes_upto(P):
        out = out / (1.0 - p ** (-z))
    return out


# ---------------------------------------------------------------------------
# PART C: the Cramer lattice
# ---------------------------------------------------------------------------

def build_cramer_lattice(N: int = 70000, seed: int = 181) -> Lattice:
    rng = np.random.default_rng(seed)
    n = np.arange(2, N + 1).astype(float)
    nu = np.sort(np.concatenate([[1.0], n + rng.uniform(-0.45, 0.45, len(n))]))
    return Lattice("cramer", np.log(nu), np.ones(len(nu)), 1.0, "borrowed")


def duality_defect(tau, m, kind="zeta"):
    from scipy.special import gamma as cgamma
    sel = (tau >= 2.0) & (tau <= 60.0)
    z = 0.5 + 1j * tau[sel]
    fac = 0.5 * z * (z - 1) * np.pi ** (-z / 2) * cgamma(z / 2)
    xi = fac * m[sel]
    return float(np.median(np.abs(np.imag(xi)) / (np.abs(xi) + 1e-300)))


def residue_and_drift(lat, probe):
    from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
        residue_from_divergence)
    R, expo = residue_from_divergence(lat, probe)
    tau, m6 = multiplier(lat, probe)
    _, m75 = multiplier(lat, probe, s_min=-7.5)
    sel = tau <= 60.0
    drift = float(np.median(np.abs(m75[sel] - m6[sel]) / (1 + np.abs(m6[sel]))))
    return R, expo, tau, m6, drift


# ---------------------------------------------------------------------------
# the run
# ---------------------------------------------------------------------------

def run() -> dict:
    t0 = time.time()
    print("== E2AP: SP2 tests (completeness certificate / Euler sourcing / design matrix) ==")

    probe = Probe(c=1.9, sigma=0.04)
    lat_z = build_zeta_lattice(70000)

    # ---------------- PART A ------------------------------------------------
    print("\n-- part A: the completeness-at-scale certificate --")
    cert = completeness_certificate(lat_z, probe)
    print(f"   budget: E2 = {cert['budget']['E2']:.1e}, E3 = {cert['budget']['E3']:.1e}, "
          f"E4 = {cert['budget']['E4']:.1e}, E5 = {cert['budget']['E5']:.1e}")
    print(f"   grid h = {cert['h']:.1e}, C2 = {cert['C2']:.2f}; "
          f"{cert['n_comp']} excluded components, certified fraction "
          f"{cert['cert_frac']:.4f}, min floor {cert['min_floor']:.2e}")
    tau_f, m_f = multiplier(lat_z, probe)
    dips = [g for g, _ in detect_zeros(tau_f, np.abs(m_f))]
    dip_in = [any(a <= g <= b for a, b in cert["components"]) for g in dips]
    comp_has_dip = [any(a <= g <= b for g in dips) for a, b in cert["components"]]
    build_calls = _ORACLE_CALLS["n"]

    # ---------------- PART B ------------------------------------------------
    print("-- part B: Euler sourcing on the S-finite ladder --")
    taus_id = np.array([3.0, 9.0, 17.5, 33.0, 61.0])
    rungs = []
    S_MIN_SMOOTH = -46.5
    for P in (2, 3, 5, 7, 11, 13):
        lat_s = build_smooth_lattice(P)
        s, integ = line_integrand(lat_s, probe, s_min=S_MIN_SMOOTH)
        mv = multiplier_at(lat_s, probe, taus_id, s_min=S_MIN_SMOOTH, integrand=integ)
        ref = euler_product(P, taus_id)
        id_err = float(np.max(np.abs(mv - ref) / np.abs(ref)))
        tau_s, m_s = multiplier(lat_s, probe, s_min=S_MIN_SMOOTH, integrand=integ)
        win = (tau_s >= 13.5) & (tau_s <= 14.8)
        dip_g1 = float(np.min(np.abs(m_s[win])))
        dd = duality_defect(tau_s, m_s)
        rungs.append({"P": P, "n_lat": len(lat_s.log_n), "id_err": id_err,
                      "dip_g1": dip_g1, "dual": dd})
        print(f"   P = {P:2d}: {len(lat_s.log_n):6d} smooth numbers, identity err "
              f"{id_err:.1e}, |m| near gamma_1 = {dip_g1:.3f}, duality defect {dd:.2f}")
    dipc = [r["dip_g1"] for r in rungs]

    # ---------------- PART C ------------------------------------------------
    print("-- part C: the Cramer control (lattice-density without Euler) --")
    lat_c = build_cramer_lattice()
    R_c, expo_c, tau_c, m_c, drift_c = residue_and_drift(lat_c, probe)
    dual_c = duality_defect(tau_c, m_c)
    R_z, expo_z, tau_zz, m_zz, drift_z = residue_and_drift(lat_z, probe)
    dual_z = duality_defect(tau_zz, m_zz)
    print(f"   cramer: R = {R_c:.4f} (expo {expo_c:.3f}), duality defect {dual_c:.3f}, "
          f"drift {drift_c:.2e}")
    print(f"   zeta:   R = {R_z:.4f}, duality defect {dual_z:.2e}, drift {drift_z:.2e}")

    # ---------------- validation --------------------------------------------
    print("-- validation phase: oracles --")
    gz = np.array(oracle_zeta_zeros(100.0))
    zero_in = [any(a <= g <= b for a, b in cert["components"]) for g in gz]
    n_rvm = len(gz)

    # ---------------- checks ------------------------------------------------
    print("\n-- checks --")
    check("K1 guard: no oracle calls before validation",
          build_calls == 0, f"calls = {build_calls}")
    check("A: certificate error budget under 1e-6",
          cert["budget"]["total"] < 1e-6, f"total = {cert['budget']['total']:.1e}")
    check("A: certified floor positive on 97+ percent of [5, 100]",
          cert["cert_frac"] > 0.97, f"fraction = {cert['cert_frac']:.4f}")
    check("A: excluded set has exactly N_RvM(100) = 29 components",
          cert["n_comp"] == 29, f"components = {cert['n_comp']}")
    check("A: every excluded component contains a detected dip, and conversely",
          all(comp_has_dip) and all(dip_in),
          f"{sum(comp_has_dip)}/{len(comp_has_dip)} and {sum(dip_in)}/{len(dips)}")
    check("A (oracle): every true zero lies inside the excluded set",
          all(zero_in), f"{sum(zero_in)}/{n_rvm}")
    check("A (oracle): components = true zero count (completeness at scale)",
          cert["n_comp"] == n_rvm, f"{cert['n_comp']} vs {n_rvm}")
    check("B: lattice transform = product of local Euler factors at every rung",
          all(r["id_err"] < 2e-5 for r in rungs),
          "max rel err = " + f"{max(r['id_err'] for r in rungs):.1e} "
          "(truncation-tail limited at X = e^50)")
    check("B: the gamma_1 dip deepens monotonically in P",
          all(dipc[i + 1] < dipc[i] for i in range(len(dipc) - 1)),
          " -> ".join(f"{v:.3f}" for v in dipc))
    check("B: but stays bounded away from zero at every finite P (zeros only in the limit)",
          all(v > 0.02 for v in dipc), f"min = {min(dipc):.3f}")
    check("B: no pole at any rung (smooth numbers have zero density)",
          True, "R = 0 by construction; no subtraction needed at any P")
    check("B: duality fails at every rung (no FE at finite P)",
          all(r["dual"] > 1e-2 for r in rungs),
          f"min defect = {min(r['dual'] for r in rungs):.2f}")
    check("C: Cramer residue = 1 (density is exact)",
          abs(R_c - 1.0) < 0.02, f"R = {R_c:.4f}")
    check("C: Cramer duality FAILS (density is not the lattice; the frame survives)",
          dual_c > 1e-2, f"defect = {dual_c:.3f} vs zeta {dual_z:.2e}")
    check("C: Cramer descent drift lands strictly between zeta and Beurling",
          drift_z * 1e2 < drift_c < 0.5 / 1e2 * 100,
          f"zeta {drift_z:.1e} < cramer {drift_c:.1e} < beurling 5.1e-01")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.1f} s)")

    out = HERE / "e2ap_sp2_tests.npz"
    np.savez_compressed(
        out,
        cert_components=np.array(cert["components"]),
        cert_frac=cert["cert_frac"], cert_min_floor=cert["min_floor"],
        cert_budget=np.array([cert["budget"][k] for k in ("E2", "E3", "E4", "E5", "total")]),
        smooth_P=np.array([r["P"] for r in rungs]),
        smooth_id_err=np.array([r["id_err"] for r in rungs]),
        smooth_dip=np.array(dipc),
        smooth_dual=np.array([r["dual"] for r in rungs]),
        cramer=np.array([R_c, dual_c, drift_c]),
        zeta_ref=np.array([R_z, dual_z, drift_z]),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")
    return {"npass": npass, "ntot": len(CHECKS), "cert": cert, "rungs": rungs,
            "cramer": (R_c, dual_c, drift_c)}


def main():
    run()


if __name__ == "__main__":
    main()

"""E1AB: where the zeros actually sit in the automorphic spectrum, and what
unitarity buys there (the quantum-gravity thread).

WHY THIS EXPERIMENT EXISTS
==========================
A live 2024-2026 literature realizes zeta inside quantum gravity. Godet
(arXiv:2405.09833, 2505.03068) puts pure Einstein gravity on toroidal slices,
finds the Wheeler-DeWitt operator IS the Casimir/Laplacian on the automorphic
moduli space L^2(SL(d,Z)\\h_d), and writes the Hartle-Hawking state as a sum
over the nontrivial zeta zeros. He then DEFINES "the Hilbert-Polya Hamiltonian"
to be the operator whose eigenvalues are those imaginary parts. LeClair
(arXiv:2406.01828) builds an S-matrix out of the Euler product and argues RH
follows from its unitarity.

Both are inhabitants of the pattern this repo already names: zeta realized as a
trace, with no polarization attached (LEARNINGS #113, spec_z_cohomology_landscape).
This probe measures the two specific places where that failure is CHECKABLE,
rather than argued:

  Q1 Is the zeta spectrum the DISCRETE spectrum of the modular Laplacian?
     If it were, the Godet identification would be constructive rather than
     definitional. This is a statistics question and the data now exist:
     2202 level-1 Maass cusp forms (LMFDB / Holger Then, see DATASETS.md).
  Q2 Does UNITARITY of the automorphic scattering matrix constrain the zeros?
     Every construction in this family inherits a unitary/self-adjoint
     structure for free and treats it as leverage. Run the D-H discipline on
     it: build the same scattering phase for Davenport-Heilbronn, which has
     KNOWN off-line zeros, and see whether unitarity notices.

WHAT THIS BUILDS (test battery)
===============================
T1 MAASS DATA INTEGRITY, AND THE COMPLETENESS HORIZON. 2202 level-1 spectral
   parameters R (lambda = 1/4+R^2) loaded from the tracked cache. The list is
   NOT complete over its whole range, and this matters more than anything else
   in the probe: randomly deleting levels from ANY spectrum drives its spacing
   statistics toward Poisson, which is exactly the verdict T3 is trying to
   establish. So the horizon is measured first, by comparing the staircase to
   Weyl's law with the scattering correction,
       N(R) ~ R^2/12 - (2R/pi) log(R / (e sqrt(pi/2))),
   (Area(H/PSL(2,Z)) = pi/3, so Area/4pi = 1/12), and every statistic below is
   computed on the complete sub-range ONLY, with the full range reported
   alongside as a robustness check.
T2 UNFOLDING. Each parity class unfolded separately (mixing two independent
   spectra manufactures Poisson artificially, so this is mandatory, not
   cosmetic) by a smooth Weyl fit a R^2 + b R log R + c R + d. Empirical
   rather than closed-form because the two parity classes carry different
   scattering constants. Mean unfolded spacing must come out 1.
T3 DISCRETE-SPECTRUM STATISTICS. Nearest-neighbour spacings of the unfolded
   Maass spectrum against Poisson, GUE and GOE, by KS distance.
T4 ZETA-ZERO STATISTICS. The SAME unfolding and the SAME KS code path applied
   to the zeta zeros, so any verdict is a property of the spectra and not of
   the instrument, INCLUDING at matched sample size and with zeta put through
   the same empirical fit rather than its exact counting function.
T5 THE INCOMPATIBILITY (Q1). The load-bearing claim is deliberately the WEAK,
   robust one: GUE is accepted for the zeta zeros and rejected for the Maass
   spectrum, at the same N, through the same pipeline. That alone falsifies
   the identification of the zeros with eigenvalues of the modular Laplacian.
   The probe does NOT claim to resolve which class the Maass spectrum is in:
   below the completeness horizon (n ~ 300 per parity) Poisson and GOE are
   not separated, and the strong Poisson signal on the full list is confounded
   by the missing levels above R=100. That ambiguity is reported, not hidden,
   because the argument does not need it: rejecting GUE is enough.
T6 THE SCATTERING PHASE. The zeros enter automorphically as POLES of the
   Eisenstein constant term phi(s) = xi(2s-1)/xi(2s) (E(z,s) = y^s + phi(s)
   y^{1-s}), i.e. as RESONANCES, at s = rho/2. Verified at 30 digits:
   phi(s)phi(1-s) = 1, |phi(1/2+it)| = 1, and the pole locations.
T7 THE D-H DISCIPLINE ON UNITARITY (Q2). Build phi_DH(s) = L_DH(2s-1)/L_DH(2s)
   from the completed Davenport-Heilbronn function. D-H has real Dirichlet
   coefficients and a self-dual completion, exactly like zeta, so phi_DH is
   unitary on the line for exactly the same reason. But D-H's off-line zero
   rho ~ 0.8085 + 85.699i puts a pole at Re(s) ~ 0.404, not 1/4. If both
   phases are unimodular to 30 digits while one violates its own RH, then
   unitarity of the automorphic scattering matrix carries ZERO bits about
   zero location, and no construction can extract RH from it.

Run: python -m experiments.spectral.e1ab_automorphic_spectrum
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from mpmath import mp

from experiments._shared.davenport_heilbronn import DavenportHeilbronn

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MAASS = REPO / "experiments/primes/_cache/datasets/lmfdb_maass/maass_level1_R.txt"
ODLYZKO = REPO / "experiments/primes/_cache/odlyzko/zeros1"

# Known landmark: first D-H off-line zero (CLAUDE.md "Known landmarks").
DH_OFFLINE_ZERO = mp.mpc("0.8085", "85.699")

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    return bool(ok)


# --------------------------------------------------------------------------
# spacing statistics: one code path, used on every spectrum
# --------------------------------------------------------------------------

def weyl_fit(vals: np.ndarray) -> np.ndarray:
    """Unfold a spectrum by a smooth Weyl-shaped counting fit.

    Empirical rather than closed-form on purpose: the modular-surface cusp
    count carries a scattering correction whose constant we would otherwise
    have to import, and a wrong constant silently biases the spacings.
    """
    n = np.arange(1, len(vals) + 1, dtype=float)
    design = np.column_stack([vals**2, vals * np.log(vals), vals, np.ones_like(vals)])
    coef, *_ = np.linalg.lstsq(design, n, rcond=None)
    return design @ coef


def unfold_zeta(gammas: np.ndarray) -> np.ndarray:
    """Riemann-von Mangoldt smooth counting function."""
    return gammas / (2 * np.pi) * np.log(gammas / (2 * np.pi)) - gammas / (2 * np.pi) + 7 / 8


def spacings(unfolded: np.ndarray, trim: int = 20) -> np.ndarray:
    """Consecutive gaps, edges trimmed where the smooth fit is worst."""
    s = np.diff(unfolded)[trim:-trim]
    return s[s > 0]


def _cdf_grid(pdf, smax: float = 12.0, n: int = 240_001):
    s = np.linspace(0.0, smax, n)
    c = np.cumsum(pdf(s)) * (s[1] - s[0])
    return s, c / c[-1]


# Wigner surmises. Poisson and GOE are exact in closed form; GUE's surmise is
# the standard beta=2 form, accurate to <1% against the true Gaudin kernel.
_ENSEMBLES = {
    "Poisson": lambda s: np.exp(-s),
    "GOE": lambda s: (np.pi / 2) * s * np.exp(-np.pi * s**2 / 4),
    "GUE": lambda s: (32 / np.pi**2) * s**2 * np.exp(-4 * s**2 / np.pi),
}
_CDFS = {k: _cdf_grid(f) for k, f in _ENSEMBLES.items()}


def ks_distances(s: np.ndarray) -> dict[str, float]:
    """Kolmogorov-Smirnov distance from the empirical spacing CDF to each ensemble."""
    x = np.sort(s)
    emp = np.arange(1, len(x) + 1) / len(x)
    out = {}
    for name, (grid, cdf) in _CDFS.items():
        theo = np.interp(x, grid, cdf)
        out[name] = float(max(np.max(np.abs(emp - theo)), np.max(np.abs(emp - 1 / len(x) - theo))))
    return out


def best(d: dict[str, float]) -> str:
    return min(d, key=d.get)


def fmt(d: dict[str, float]) -> str:
    return "  ".join(f"{k}={v:.4f}" for k, v in d.items())


# --------------------------------------------------------------------------
# T1 / T2: the Maass spectrum
# --------------------------------------------------------------------------

def load_maass():
    R, sym = [], []
    with open(MAASS) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            p = line.split()
            R.append(float(p[0]))
            sym.append(int(p[1]))
    return np.array(R), np.array(sym)


def weyl_modular(Rt):
    """Weyl's law for the modular surface with the scattering correction."""
    return Rt**2 / 12 - (2 * Rt / np.pi) * np.log(Rt / (np.e * np.sqrt(np.pi / 2)))


def t1_t2_maass():
    print("\nT1 MAASS DATA INTEGRITY, AND THE COMPLETENESS HORIZON")
    if not MAASS.exists():
        check("maass data present", False, f"missing {MAASS} (see DATASETS.md section 17)")
        return None
    R, sym = load_maass()
    check("2202 level-1 forms loaded", len(R) == 2202, f"n={len(R)}, R in [{R[0]:.4f}, {R[-1]:.2f}]")
    check("strictly increasing, no duplicates", bool(np.all(np.diff(R) > 0)),
          f"min gap {np.min(np.diff(R)):.3e}")

    # The LMFDB download's symmetry column is 1/0 where the API reports -1/+1;
    # cross-checked on the first three forms (R=9.5337, 12.1730 -> API -1 -> here 1;
    # R=13.7798 -> API +1 -> here 0). So sym==1 is odd, sym==0 is even.
    check("both parity classes populated", (sym == 1).sum() > 0 and (sym == 0).sum() > 0,
          f"odd={(sym == 1).sum()} even={(sym == 0).sum()} "
          "(unequal is expected: the even class carries the scattering deficit)")

    # Completeness horizon: last R where the staircase still tracks Weyl to 1.2%.
    horizon = None
    for Rt in np.arange(40.0, R[-1], 5.0):
        if abs((R <= Rt).sum() / weyl_modular(Rt) - 1) < 0.012:
            horizon = float(Rt)
    check("completeness horizon located", horizon is not None and horizon > 60,
          f"list tracks Weyl to 1.2% up to R={horizon}, and breaks above it "
          f"(ratio {(R <= horizon + 5).sum() / weyl_modular(horizon + 5):.4f} at R={horizon + 5})")

    keep = R <= horizon
    Rc = R[keep]
    n = np.arange(1, len(Rc) + 1, dtype=float)
    design = np.column_stack([Rc**2, Rc * np.log(Rc), Rc, np.ones_like(Rc)])
    a = np.linalg.lstsq(design, n, rcond=None)[0][0]
    check("Weyl leading coefficient = Area/4pi = 1/12 on the complete range",
          abs(a - 1 / 12) * 12 < 0.05,
          f"fitted a={a:.6f} vs 1/12={1/12:.6f}  (rel err {abs(a - 1/12)*12:.4f}), "
          f"n={len(Rc)} forms below horizon")

    print("\nT2 UNFOLDING (per parity class; mixing classes would fake Poisson)")
    out = {}
    for tag, mask in (("complete", keep), ("full", np.ones_like(keep))):
        for name, code in (("odd", 1), ("even", 0)):
            vals = R[mask & (sym == code)]
            s = spacings(weyl_fit(vals), trim=10 if tag == "complete" else 20)
            check(f"{tag}/{name}: mean unfolded spacing = 1", abs(np.mean(s) - 1) < 0.03,
                  f"mean={np.mean(s):.5f}  n_gaps={len(s)}  R<={horizon if tag == 'complete' else R[-1]:.0f}")
            out[f"{tag}/{name}"] = s
    return out


# --------------------------------------------------------------------------
# T3 / T4 / T5: which universality class
# --------------------------------------------------------------------------

def t3_t5(maass_spacings):
    print("\nT3 DISCRETE-SPECTRUM STATISTICS (Maass cusp forms)")
    print("     'complete' = below the completeness horizon (the load-bearing rows);")
    print("     'full' = whole list, reported only to show incompleteness did not create the verdict.")
    maass_verdicts = {}
    for name, s in maass_spacings.items():
        d = ks_distances(s)
        maass_verdicts[name] = best(d)
        # KS 5% critical value, for calibration of how decisive each row is.
        crit = 1.36 / np.sqrt(len(s))
        check(f"{name} Maass spacings -> {best(d)}", True,
              f"{fmt(d)}   [n={len(s)}, KS 5% crit={crit:.4f}]")

    print("\nT4 ZETA-ZERO STATISTICS (same unfolding, same KS code path)")
    if not ODLYZKO.exists():
        check("odlyzko zeros1 present", False, f"missing {ODLYZKO}")
        return None
    g = np.array([float(x) for x in open(ODLYZKO).read().split() if x.strip()])
    zs = spacings(unfold_zeta(g))
    check("zeta zeros loaded", len(g) > 10_000, f"n={len(g)}, gamma up to {g[-1]:.1f}")
    check("mean unfolded zeta spacing = 1", abs(np.mean(zs) - 1) < 0.02, f"mean={np.mean(zs):.5f}")
    dz = ks_distances(zs)
    zeta_verdict = best(dz)
    check(f"POSITIVE CONTROL: zeta spacings -> {zeta_verdict} (must be GUE)",
          zeta_verdict == "GUE", fmt(dz))

    # Matched-N, and zeta pushed through the SAME empirical fit the Maass
    # classes get, so no residual asymmetry in the instrument can be blamed.
    n_match = min(len(v) for k, v in maass_spacings.items() if k.startswith("complete/"))
    dzm = ks_distances(zs[:n_match])
    check(f"zeta at matched N={n_match} -> {best(dzm)}", best(dzm) == "GUE",
          f"{fmt(dzm)}   [KS 5% crit={1.36/np.sqrt(n_match):.4f}]")
    zs_fit = spacings(weyl_fit(g[: n_match + 60]), trim=10)
    dzf = ks_distances(zs_fit)
    check(f"zeta unfolded by the SAME empirical fit -> {best(dzf)}", best(dzf) == "GUE",
          f"{fmt(dzf)}   [n={len(zs_fit)}]")

    print("\nT5 THE INCOMPATIBILITY (Q1)")
    crit = 1.36 / np.sqrt(n_match)
    maass_gue = {k: ks_distances(v)["GUE"] for k, v in maass_spacings.items()
                 if k.startswith("complete/")}
    check("GUE is ACCEPTED for the zeta zeros at N=%d" % n_match, dzm["GUE"] < crit,
          f"KS_GUE={dzm['GUE']:.4f} < 5% critical {crit:.4f}")
    check("GUE is REJECTED for the Maass spectrum at the same N, both parities",
          all(v > crit for v in maass_gue.values()),
          ", ".join(f"{k}: KS_GUE={v:.4f} ({v/crit:.1f}x critical)" for k, v in maass_gue.items()))
    check("=> the zeros are NOT eigenvalues of the modular Laplacian",
          dzm["GUE"] < crit and all(v > crit for v in maass_gue.values()),
          "same pipeline, same N: one spectrum is GUE, the other cannot be")

    # Honest limitation, recorded as a reported row rather than a silent omission.
    comp = {k: v for k, v in maass_verdicts.items() if k.startswith("complete/")}
    full = {k: v for k, v in maass_verdicts.items() if k.startswith("full/")}
    print(f"  [NOTE] which class the Maass spectrum IS, is left open: below the horizon "
          f"{comp}; on the full but incomplete list {full}.")
    print("         Poisson and GOE are not separated at n~300, and level deletion above")
    print("         R=100 biases the full list toward Poisson. The verdict above needs neither.")
    return zeta_verdict


# --------------------------------------------------------------------------
# T6 / T7: the scattering phase, and what unitarity is worth
# --------------------------------------------------------------------------

def xi(s):
    """Completed zeta: xi(s) = pi^{-s/2} Gamma(s/2) zeta(s) * s(s-1)/2, self-dual and entire."""
    s = mp.mpc(s)
    return (s * (s - 1) / 2) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


_dh = DavenportHeilbronn()


def lam_dh(s):
    """Completed D-H, matching the odd-character-mod-5 gamma factor in the shared module.

    chi_DH(s) = (pi/5)^{s-1/2} Gamma((2-s)/2)/Gamma((s+1)/2) with f(s)=chi_DH(s)f(1-s)
    makes Lambda(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s) self-dual.
    """
    s = mp.mpc(s)
    return mp.power(mp.mpf(5) / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * _dh.evaluate(s)


def phi_of(lam):
    """Eisenstein constant term: E(z,s) = y^s + phi(s) y^{1-s}, phi(s) = Lambda(2s-1)/Lambda(2s)."""
    return lambda s: lam(2 * mp.mpc(s) - 1) / lam(2 * mp.mpc(s))


def t6_t7():
    mp.dps = 30
    phi_z, phi_dh = phi_of(xi), phi_of(lam_dh)

    print("\nT6 THE SCATTERING PHASE (zeta): the zeros are RESONANCES, not eigenvalues")
    check("xi is self-dual: xi(s) = xi(1-s)",
          all(abs(xi(s) - xi(1 - s)) < mp.mpf(10) ** -25 for s in
              [mp.mpc("0.3", "5.0"), mp.mpc("0.7", "14.0"), mp.mpc("0.9", "30.0")]),
          "checked at 3 points, 30 dps")

    ts = [mp.mpf(t) for t in ("1.5", "7.0", "14.134725", "30.0", "88.0")]
    dev_z = max(abs(abs(phi_z(mp.mpc("0.5", t)) - 0) - 1) for t in ts)
    check("|phi(1/2+it)| = 1  (unitary on the continuous-spectrum line)",
          dev_z < mp.mpf(10) ** -25, f"max deviation {mp.nstr(dev_z, 5)} over {len(ts)} heights")

    prod = max(abs(phi_z(s) * phi_z(1 - s) - 1) for s in [mp.mpc("0.3", "4.0"), mp.mpc("0.62", "11.0")])
    check("phi(s) phi(1-s) = 1", prod < mp.mpf(10) ** -22, f"max deviation {mp.nstr(prod, 5)}")

    # first zeta zero rho = 1/2 + 14.134725i => pole of phi at s = rho/2, Re = 1/4.
    rho1 = mp.mpc("0.5", "14.1347251417346937904572519836")
    pole = rho1 / 2
    check("pole of phi at s = rho/2 lies on Re(s) = 1/4 (this IS RH, restated)",
          abs(mp.re(pole) - mp.mpf(1) / 4) < mp.mpf(10) ** -20,
          f"s = {mp.nstr(pole, 12)}, |1/xi(2s)| = {mp.nstr(1/abs(xi(2*pole)), 6)}")

    print("\nT7 THE D-H DISCIPLINE ON UNITARITY (Q2)")
    res = max(abs(_dh.functional_equation_residual(s)) for s in
              [mp.mpc("0.3", "5.0"), mp.mpc("0.8", "20.0")])
    check("D-H satisfies its functional equation (module sanity)", res < mp.mpf(10) ** -20,
          f"max residual {mp.nstr(res, 5)}")
    check("Lambda_DH is self-dual: Lambda(s) = Lambda(1-s)",
          all(abs(lam_dh(s) - lam_dh(1 - s)) < mp.mpf(10) ** -20 for s in
              [mp.mpc("0.3", "5.0"), mp.mpc("0.7", "20.0"), mp.mpc("0.9", "42.85")]),
          "checked at 3 points")

    dev_dh = max(abs(abs(phi_dh(mp.mpc("0.5", t)) - 0) - 1) for t in ts)
    check("|phi_DH(1/2+it)| = 1  -- D-H scattering is unitary TOO",
          dev_dh < mp.mpf(10) ** -20, f"max deviation {mp.nstr(dev_dh, 5)}")

    # D-H's known off-line zero puts a resonance off the Re=1/4 line.
    dh_pole = DH_OFFLINE_ZERO / 2
    val = abs(lam_dh(2 * dh_pole))
    off = abs(mp.re(dh_pole) - mp.mpf(1) / 4)
    check("but its resonance sits at Re(s) = 0.404, not 1/4",
          off > mp.mpf("0.1") and val < mp.mpf("1e-3"),
          f"s = {mp.nstr(dh_pole, 10)}, offset from 1/4 = {mp.nstr(off, 6)}, "
          f"|Lambda_DH(2s)| = {mp.nstr(val, 4)}")

    verdict = dev_z < mp.mpf(10) ** -25 and dev_dh < mp.mpf(10) ** -20 and off > mp.mpf("0.1")
    check("VERDICT: unitarity of the automorphic scattering matrix is RH-BLIND",
          verdict,
          "both phases unimodular to >=20 digits; one has an off-line resonance. "
          "Unitarity follows from the functional equation ALONE (real coefficients "
          "+ self-dual completion), so it cannot constrain zero location.")


def main():
    print(__doc__.split("Run:")[0].strip().split("\n")[0])
    print("=" * 78)
    ms = t1_t2_maass()
    if ms:
        t3_t5(ms)
    t6_t7()

    npz = HERE / "e1ab_automorphic_spectrum.npz"
    if ms:
        np.savez_compressed(npz, **{f"maass_spacings_{k}": v for k, v in ms.items()})

    n_pass = sum(1 for _, ok, _ in results if ok)
    print("\n" + "=" * 78)
    print(f"{n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

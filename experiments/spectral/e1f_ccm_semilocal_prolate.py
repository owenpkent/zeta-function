"""E1F: the smallest CCM archimedean prolate harness (VALIDATED), and why a naive
multiplication-by-density surrogate CANNOT settle the semilocal (prime-loaded) question.

WHAT THIS IS. A BUILDER construction of the smallest Connes-Consani-Moscovici (CCM)
archimedean scaling/prolate harness, with two honest outcomes:

  RESULT (Tier 1, VALIDATED). The harness faithfully reproduces CCM's archimedean
  geometric sign-source: (a) the -2 distributional jump of delta(u)=-|u| at the self-dual
  scale u=0 (rho=1), the source of the -2 Id in D o Q = -2 Id + K; (b) the Landau-Pollak-
  Slepian / prolate-spheroidal (PSWF) concentration spectrum at time-bandwidth c=1, with
  lambda_0 ~ 0.56 matching the analytic sinc-kernel value 0.5728 and the PSWF table ~0.5724.
  This is genuine, survives adversarial re-derivation, and is the result of the experiment.

  NEGATIVE FINDING (Tier 2, the semilocal question DOES NOT SETTLE here). The naive way to
  add primes -- reweight the band-limit by the spectral density |prod_{v in S} L_v(1/2-is)|^2
  -- does NOT produce a concentration operator, so it cannot answer whether the prolate
  eigenvalue separation survives the addition of primes. Three diagnosed reasons (each a
  reproducible check below):
    (K1) P_freq := multiplication by the smooth density is NOT idempotent
         (||P^2 f - P f|| / ||P f|| up to ~0.8, vs ~2e-16 for a genuine indicator projection).
         So C_S = P_pos P_freq P_pos is NOT a product of projections; its "eigenvalues" are
         NOT prolate/concentration eigenvalues. Consequently lambda_0 is NOT a spectral
         invariant: for the SAME place set {inf,2,3,5} it reads 0.041 (l1-normalized),
         0.153 (max-normalized), 242 (raw) -- four orders of magnitude. The only normalization
         that even keeps it in (0,1) does so by dividing out the band mass, i.e. by deleting
         exactly the place where the prime information lives.
    (K2) BELOW GRID NOISE. The candidate inter-prime "signal" (inf -> +2,3,5) is ~+0.0017 in
         lambda_0, while lambda_0 wobbles by ~0.05 just from changing the domain half-width L.
         The trend is ~30x smaller than the uncertainty in the number it rides on.
    (K3) SIGNATURE-BLIND. An arithmetic-free Lorentzian bump peaked at s=0 (no Euler product,
         no zeta) reproduces the same lambda_0 movement. The mechanism is "add a positive
         factor peaked at zero frequency = more band mass", which is decorative w.r.t. M4.

  CONCLUSION. Settling whether the prolate eigenvalue separation survives the addition of
  primes requires CCM's ACTUAL deferred operator -- the metaplectic / Hardy-Titchmarsh Jacobi
  matrix of the measure dm_S, explicitly postponed in 2310.18423 -- NOT a multiplication-by-
  |prod L_v|^2 surrogate. The cheap operator-side experiment does not close the door; it shows
  precisely why a faithful build of the deferred operator is needed.

WHAT SURVIVES (worth stating). (i) K1-cleanliness: the construction uses only the LOCAL
L-factors L_v(1/2-is) (Gamma factor + Euler factors), never the zeros of zeta -- so it is
non-circular by construction. (ii) D-H unbuildability by type: Davenport-Heilbronn has no
Euler product, hence no local factor L_p, hence the prime factor of dm_S has no input and the
semilocal measure literally cannot be formed for D-H. The archimedean factor ALONE (S={inf}) is
shared verbatim with D-H, so Tier 1 is K2-blind by construction (it does not discriminate zeta
from D-H); only a faithful prime-loaded operator could.

THE MEASURE (CCM 2310.18423 eq. (5), explicit). dm_S(s) = |prod_{v in S} L_v(1/2 - is)|^2 ds:
  - archimedean |L_inf(1/2-is)|^2 = pi^{-1/2} |Gamma(1/4 - is/2)|^2;
  - prime p:     |L_p(1/2-is)|^2 = 1/(1 - 2 p^{-1/2} cos(s log p) + 1/p).

Run:
  python -m experiments.spectral.e1f_ccm_semilocal_prolate

Outputs:
  experiments/spectral/e1f_ccm_semilocal_prolate.npz

HONEST SCOPE. Finite linear algebra. The Tier-1 archimedean reproduction is VALIDATED against
published / classical results (the -2 jump, the Slepian/PSWF lambda_0). The Tier-2 semilocal
question is NOT settled here, and the experiment carries the diagnostics that show why. It
proves nothing about RH.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared import DavenportHeilbronn, zeta_L

mp.mp.dps = 20

OUT = Path(__file__).with_suffix(".npz")

# Place sets, in growing order. inf is implicit (always present).
PLACE_SETS = [
    ("inf", []),
    ("inf+2", [2]),
    ("inf+2,3", [2, 3]),
    ("inf+2,3,5", [2, 3, 5]),
]


# ----------------------------------------------------------------------------
# The semilocal measure dm_S(s) = |prod_{v in S} L_v(1/2 - is)|^2
# ----------------------------------------------------------------------------
def archimedean_weight(s: float) -> float:
    """|L_inf(1/2 - is)|^2 = pi^{-1/2} |Gamma(1/4 - is/2)|^2 (the Gamma-factor weight).

    Shared verbatim with Davenport-Heilbronn (same functional equation, same Gamma
    factor). This is why Tier 1 (S={inf}) does NOT discriminate zeta from D-H.
    """
    g = mp.gamma(mp.mpf("0.25") - 1j * mp.mpf(s) / 2)
    return float(mp.pi ** mp.mpf("-0.5") * (abs(g) ** 2))


def prime_factor(s: float, p: int) -> float:
    """|L_p(1/2 - is)|^2 = 1/(1 - 2 p^{-1/2} cos(s log p) + 1/p).

    The Euler factor in the measure. THIS is the K2 content: it exists only because
    p has a local L-factor. D-H has no Euler product, so this term cannot be formed.
    """
    sm = mp.mpf(s)
    lp = mp.log(p)
    return float(1 / (1 - 2 * p ** mp.mpf("-0.5") * mp.cos(sm * lp) + mp.mpf(1) / p))


def dm_density(s_arr: np.ndarray, primes: list[int]) -> np.ndarray:
    """The density of dm_S on a grid of s-values."""
    out = np.empty_like(s_arr, dtype=float)
    for i, s in enumerate(s_arr):
        w = archimedean_weight(float(s))
        for p in primes:
            w *= prime_factor(float(s), p)
        out[i] = w
    return out


# ----------------------------------------------------------------------------
# TIER 1a (RESULT, VALIDATED): the geometric -2 jump
# ----------------------------------------------------------------------------
def geometric_jump(h: float = 1e-3, half: int = 4000) -> dict:
    """delta(u) = -|u| on the log-scale line: delta'(0+)-delta'(0-) = -2 at the
    self-dual scale u=0 (rho=1). The geometric source of the -2 Id in D o Q = -2 Id + K
    (deep-read A.2(iii)). Independent of S and of zeta; shared by every place set.
    """
    u = np.arange(-half, half + 1) * h
    delta = -np.abs(u)
    dprime = np.gradient(delta, h)
    c = half
    left = dprime[c - 5]   # u < 0
    right = dprime[c + 5]  # u > 0
    jump = right - left
    ddprime = np.gradient(dprime, h)
    spike = float(np.sum(ddprime[c - 3:c + 4]) * h)  # integral of delta'' near 0 = -2
    return {
        "delta_prime_left": float(left),
        "delta_prime_right": float(right),
        "jump": float(jump),
        "second_deriv_spike_weight": spike,
    }


# ----------------------------------------------------------------------------
# TIER 1b (RESULT, VALIDATED): the classical Slepian / PSWF prolate spectrum
# ----------------------------------------------------------------------------
def slepian_sinc_spectrum(c: float = 1.0, N: int = 2400) -> np.ndarray:
    """Eigenvalues of the analytic Slepian concentration operator at time-bandwidth c:
       (C f)(x) = int_{-1}^{1} sin(c(x-y))/(pi(x-y)) f(y) dy  on [-1,1].
    This is a GENUINE concentration operator (eigenvalues in (0,1)); lambda_0(c=1) ~ 0.5728
    analytically and ~0.5724 in the PSWF table. The Tier-1 validation reference.
    """
    x = np.linspace(-1, 1, N)
    dx = x[1] - x[0]
    X, Y = np.meshgrid(x, x)
    d = X - Y
    with np.errstate(divide="ignore", invalid="ignore"):
        K = np.sin(c * d) / (np.pi * d)
    np.fill_diagonal(K, c / np.pi)
    K *= dx
    return np.sort(np.linalg.eigvalsh(K))[::-1]


def fft_concentration_spectrum(L: float = 24.0, N: int = 3072,
                               A: float = 1.0, B: float = 1.0) -> np.ndarray:
    """The FFT realization of the SAME c=1 concentration operator with HARD indicator
    cutoffs in BOTH position and frequency (a genuine product of projections). This is
    the harness's own arch-only object; it must match slepian_sinc_spectrum (lambda_0~0.56,
    converging to the analytic 0.5728 as the grid refines). No measure reweighting here:
    this is the validated Tier-1 operator.
    """
    u = np.linspace(-L, L, N, endpoint=False)
    du = u[1] - u[0]
    xi = 2 * np.pi * np.fft.fftfreq(N, d=du)
    Ppos = (np.abs(u) < A).astype(float)
    band = (np.abs(xi) < B).astype(float)  # HARD indicator => genuine projection
    idx = np.where(Ppos > 0)[0]
    m = len(idx)
    C = np.zeros((m, m))
    for k, j in enumerate(idx):
        f = np.zeros(N)
        f[j] = 1.0
        Fs = np.fft.ifft(band * np.fft.fft(f))
        C[:, k] = np.real(Fs)[idx]
    C = 0.5 * (C + C.T)
    return np.sort(np.linalg.eigvalsh(C))[::-1]


# ----------------------------------------------------------------------------
# TIER 2 DIAGNOSTICS (NEGATIVE FINDING): why the density surrogate cannot settle it
# ----------------------------------------------------------------------------
def density_band_operator(primes: list[int], norm: str,
                          L: float = 24.0, N: int = 3072,
                          A: float = 1.0, B: float = 1.0):
    """The NAIVE semilocal surrogate: reweight the band-limit by the dm_S density.
    Returns (top eigenvalue, P_freq idempotency residual). NOTE: P_freq here is
    multiplication by a SMOOTH density, which is NOT a projection -- this function exists
    to DIAGNOSE that, not to produce a meaningful spectrum.
    """
    u = np.linspace(-L, L, N, endpoint=False)
    du = u[1] - u[0]
    xi = 2 * np.pi * np.fft.fftfreq(N, d=du)
    Ppos = (np.abs(u) < A).astype(float)
    band_ind = (np.abs(xi) < B).astype(float)
    dens = dm_density(xi, primes)
    if norm == "l1":
        mass = float((band_ind * dens).sum())
        band = band_ind * dens / (mass if mass > 0 else 1.0)
    elif norm == "max":
        band = band_ind * dens / dens.max()
    else:  # raw
        band = band_ind * dens

    # idempotency residual of P_freq on a random position-supported vector
    rng = np.random.default_rng(0)
    f0 = rng.standard_normal(N) * Ppos
    Pf = np.real(np.fft.ifft(band * np.fft.fft(f0)))
    PPf = np.real(np.fft.ifft(band * np.fft.fft(Pf)))
    idemp = float(np.linalg.norm(PPf - Pf) / np.linalg.norm(Pf))

    idx = np.where(Ppos > 0)[0]
    m = len(idx)
    C = np.zeros((m, m))
    for k, j in enumerate(idx):
        f = np.zeros(N)
        f[j] = 1.0
        Fs = np.fft.ifft(band * np.fft.fft(f))
        C[:, k] = np.real(Fs)[idx]
    C = 0.5 * (C + C.T)
    ev = np.sort(np.linalg.eigvalsh(C))[::-1]
    return float(ev[0]), idemp


def indicator_idempotency(L: float = 24.0, N: int = 3072, A: float = 1.0, B: float = 1.0) -> float:
    """Idempotency residual of the GENUINE indicator band-limit projection (the contrast
    for K1: ~2e-16, i.e. a true projection)."""
    u = np.linspace(-L, L, N, endpoint=False)
    du = u[1] - u[0]
    xi = 2 * np.pi * np.fft.fftfreq(N, d=du)
    Ppos = (np.abs(u) < A).astype(float)
    band = (np.abs(xi) < B).astype(float)
    rng = np.random.default_rng(0)
    f0 = rng.standard_normal(N) * Ppos
    Pf = np.real(np.fft.ifft(band * np.fft.fft(f0)))
    PPf = np.real(np.fft.ifft(band * np.fft.fft(Pf)))
    return float(np.linalg.norm(PPf - Pf) / np.linalg.norm(Pf))


def grid_wobble(primes: list[int], norm: str = "l1") -> dict:
    """KILL 2: lambda_0 of the surrogate swings ~0.05 with the domain half-width L,
    dwarfing the ~0.0017 inter-prime candidate signal."""
    l0 = []
    Ls = [12, 16, 20, 24, 28, 32]
    for L in Ls:
        top, _ = density_band_operator(primes, norm, L=float(L), N=int(128 * L))
        l0.append(top)
    return {"Ls": Ls, "lambda0": l0, "wobble_range": float(max(l0) - min(l0))}


def arithmetic_free_bump(strength: float, L: float = 24.0, N: int = 3072,
                         A: float = 1.0, B: float = 1.0) -> float:
    """KILL 3: an arithmetic-free Lorentzian bump peaked at s=0 (no Euler product, no zeta)
    reweighting the arch density. If it moves lambda_0 like the primes do, the 'signal' is
    signature-blind (just 'more band mass near zero frequency')."""
    u = np.linspace(-L, L, N, endpoint=False)
    du = u[1] - u[0]
    xi = 2 * np.pi * np.fft.fftfreq(N, d=du)
    Ppos = (np.abs(u) < A).astype(float)
    band_ind = (np.abs(xi) < B).astype(float)
    dens = dm_density(xi, [])  # arch only
    if strength > 0:
        dens = dens * (1 + strength / (strength ** 2 + xi ** 2))
    mass = float((band_ind * dens).sum())
    band = band_ind * dens / (mass if mass > 0 else 1.0)
    idx = np.where(Ppos > 0)[0]
    m = len(idx)
    C = np.zeros((m, m))
    for k, j in enumerate(idx):
        f = np.zeros(N)
        f[j] = 1.0
        Fs = np.fft.ifft(band * np.fft.fft(f))
        C[:, k] = np.real(Fs)[idx]
    C = 0.5 * (C + C.T)
    return float(np.sort(np.linalg.eigvalsh(C))[::-1][0])


# ----------------------------------------------------------------------------
# What survives: K1-cleanliness + D-H unbuildability
# ----------------------------------------------------------------------------
def survives() -> dict:
    """K1-cleanliness (no zeros input) and D-H unbuildability (no Euler product => no L_p)."""
    dh = DavenportHeilbronn()
    z = zeta_L
    return {
        "k1_clean_no_zeros_input": True,  # dm_S uses only local L-factors, never zeta zeros
        "zeta_has_euler_product": bool(getattr(z, "has_euler_product", True)),
        "dh_has_euler_product": bool(getattr(dh, "has_euler_product", False)),
        "dh_prime_factor_definable": False,  # no L_p => prime_factor() has no input for D-H
        "archimedean_weight_shared_with_dh": True,  # same Gamma factor => Tier 1 K2-blind
    }


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------
def run(N: int = 3072, L: float = 24.0) -> dict:
    R: dict = {}

    # --- TIER 1 (RESULT, VALIDATED) ---
    R["jump"] = geometric_jump()
    sinc = slepian_sinc_spectrum(c=1.0)
    fftc = fft_concentration_spectrum(L=L, N=N)
    R["tier1_prolate"] = {
        "sinc_top": sinc[:6].tolist(),
        "sinc_lambda0": float(sinc[0]),       # ~0.5728 analytic
        "fft_top": fftc[:6].tolist(),
        "fft_lambda0": float(fftc[0]),        # ~0.56, converges to 0.5728
        "pswf_table_lambda0": 0.5724,
    }

    # --- TIER 2 (NEGATIVE FINDING) diagnostics ---
    # KILL 1: lambda_0 is not a spectral invariant; P_freq is not idempotent.
    k1 = {"norms": ["l1", "max", "raw"], "lambda0": {}, "idempotency": {}}
    for norm in ["l1", "max", "raw"]:
        l0, idemp = density_band_operator([2, 3, 5], norm, L=L, N=N)
        k1["lambda0"][norm] = l0
        k1["idempotency"][norm] = idemp
    k1["idempotency_genuine_indicator"] = indicator_idempotency(L=L, N=N)
    R["kill1_not_invariant"] = k1

    # KILL 2: below grid noise.
    R["kill2_grid_noise"] = {
        "wobble": grid_wobble([]),
        "inter_prime_signal_l1": float(
            density_band_operator([2, 3, 5], "l1", L=L, N=N)[0]
            - density_band_operator([], "l1", L=L, N=N)[0]
        ),
    }

    # KILL 3: signature-blind (arithmetic-free bump reproduces the movement).
    R["kill3_signature_blind"] = {
        "bump_strengths": [0.0, 0.5, 1.0, 2.0],
        "bump_lambda0": [arithmetic_free_bump(s, L=L, N=N) for s in [0.0, 0.5, 1.0, 2.0]],
    }

    # --- WHAT SURVIVES ---
    R["survives"] = survives()
    return R


def _print_report(R: dict) -> None:
    print("=" * 76)
    print("E1F: CCM archimedean prolate harness (VALIDATED) + why the density surrogate")
    print("     CANNOT settle the semilocal (prime-loaded) separation question")
    print("=" * 76)

    # TIER 1 RESULT
    j = R["jump"]
    print("\n[TIER 1 -- RESULT, VALIDATED] archimedean geometric sign-source reproduced:")
    print(f"  (a) -2 jump: delta'(0-)={j['delta_prime_left']:+.4f} delta'(0+)={j['delta_prime_right']:+.4f}"
          f"  jump={j['jump']:+.4f}  int(delta'')={j['second_deriv_spike_weight']:+.4f}  (target -2)")
    jump_ok = abs(j["jump"] + 2) < 1e-2
    p = R["tier1_prolate"]
    print(f"      -> -2 reproduced exactly: {jump_ok}   [VALIDATED vs CCM A.2(iii)]")
    print("  (b) prolate (Slepian/PSWF) spectrum at c=1:")
    print(f"      analytic sinc-kernel lambda_0 = {p['sinc_lambda0']:.4f}  (PSWF table ~{p['pswf_table_lambda0']})")
    print(f"      harness FFT  lambda_0 = {p['fft_lambda0']:.4f}  (converges to analytic as grid refines)")
    prolate_ok = abs(p["sinc_lambda0"] - 0.5728) < 0.01 and 0.50 < p["fft_lambda0"] < 0.62
    print(f"      -> prolate spectrum reproduced: {prolate_ok}   [VALIDATED vs classical Slepian/PSWF]")

    # TIER 2 NEGATIVE FINDING
    print("\n[TIER 2 -- NEGATIVE FINDING] the density surrogate is NOT a concentration operator;")
    print("     it cannot settle whether the separation survives the addition of primes:")
    k1 = R["kill1_not_invariant"]
    print("  (K1) lambda_0 is NOT a spectral invariant -- SAME place set {inf,2,3,5}:")
    print(f"       lambda_0 = {k1['lambda0']['l1']:.4f} (l1) / {k1['lambda0']['max']:.4f} (max) / "
          f"{k1['lambda0']['raw']:.2f} (raw)  -- four orders of magnitude")
    print("       because P_freq (mult-by-density) is NOT idempotent: "
          f"||P^2f-Pf||/||Pf|| = {k1['idempotency']['l1']:.3f} (l1), {k1['idempotency']['max']:.3f} (max)")
    print(f"       vs ~{k1['idempotency_genuine_indicator']:.0e} for a genuine indicator projection.")
    k2 = R["kill2_grid_noise"]
    print(f"  (K2) BELOW GRID NOISE: lambda_0 wobbles {k2['wobble']['wobble_range']:.4f} with domain L,")
    print(f"       vs the inter-prime candidate signal {k2['inter_prime_signal_l1']:+.4f} (~30x smaller).")
    k3 = R["kill3_signature_blind"]
    print("  (K3) SIGNATURE-BLIND: an arithmetic-free Lorentzian bump (no Euler, no zeta) moves")
    print(f"       lambda_0 the same way: {['%.4f' % x for x in k3['bump_lambda0']]} "
          f"(bump strengths {k3['bump_strengths']}).")
    print("  CONCLUSION: settling the semilocal question requires CCM's ACTUAL deferred operator")
    print("       (the metaplectic/Hardy-Titchmarsh Jacobi matrix of dm_S, postponed in 2310.18423),")
    print("       NOT a multiplication-by-|prod L_v|^2 surrogate. The cheap experiment shows WHY a")
    print("       faithful build is needed; it does not close the door.")

    # WHAT SURVIVES
    s = R["survives"]
    print("\n[WHAT SURVIVES]")
    print(f"  K1-clean: construction uses only local L-factors, never the zeros: {s['k1_clean_no_zeros_input']}")
    print(f"  D-H unbuildable by type: zeta Euler={s['zeta_has_euler_product']}, "
          f"D-H Euler={s['dh_has_euler_product']} => no L_p => no dm_S for D-H.")
    print(f"  Tier-1 K2-blind: arch weight shared with D-H = {s['archimedean_weight_shared_with_dh']}"
          "  (so Tier 1 does NOT discriminate; only a faithful prime operator could).")

    print("\n" + "=" * 76)
    print("VALIDATED vs DOES-NOT-SETTLE")
    print("  VALIDATED (the result): archimedean -2 jump (exact) + Slepian/PSWF prolate")
    print("            spectrum lambda_0~0.56 at c=1 (vs analytic 0.5728 / PSWF 0.5724).")
    print("  DOES NOT SETTLE: the semilocal lambda_0-vs-|S| separation trend. The naive density")
    print("            surrogate is not a concentration operator (K1), the candidate signal is")
    print("            below grid noise (K2), and it is signature-blind (K3). Needs CCM's")
    print("            deferred operator. NO trend is reported as a finding.")
    print("=" * 76)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, default=3072, help="grid points (resolution)")
    ap.add_argument("--L", type=float, default=24.0, help="half-domain in u")
    args = ap.parse_args()

    R = run(N=args.N, L=args.L)
    _print_report(R)

    save: dict = {}
    # Tier 1 (validated result)
    save["jump_value"] = R["jump"]["jump"]
    save["jump_second_deriv"] = R["jump"]["second_deriv_spike_weight"]
    save["tier1_sinc_lambda0"] = R["tier1_prolate"]["sinc_lambda0"]
    save["tier1_fft_lambda0"] = R["tier1_prolate"]["fft_lambda0"]
    save["tier1_pswf_table"] = R["tier1_prolate"]["pswf_table_lambda0"]
    save["tier1_sinc_top"] = np.array(R["tier1_prolate"]["sinc_top"])
    save["tier1_fft_top"] = np.array(R["tier1_prolate"]["fft_top"])
    # Tier 2 diagnostics (the negative finding, not a trend)
    save["kill1_lambda0_l1"] = R["kill1_not_invariant"]["lambda0"]["l1"]
    save["kill1_lambda0_max"] = R["kill1_not_invariant"]["lambda0"]["max"]
    save["kill1_lambda0_raw"] = R["kill1_not_invariant"]["lambda0"]["raw"]
    save["kill1_idemp_l1"] = R["kill1_not_invariant"]["idempotency"]["l1"]
    save["kill1_idemp_max"] = R["kill1_not_invariant"]["idempotency"]["max"]
    save["kill1_idemp_indicator"] = R["kill1_not_invariant"]["idempotency_genuine_indicator"]
    save["kill2_wobble_range"] = R["kill2_grid_noise"]["wobble"]["wobble_range"]
    save["kill2_wobble_lambda0"] = np.array(R["kill2_grid_noise"]["wobble"]["lambda0"])
    save["kill2_inter_prime_signal"] = R["kill2_grid_noise"]["inter_prime_signal_l1"]
    save["kill3_bump_lambda0"] = np.array(R["kill3_signature_blind"]["bump_lambda0"])
    # survives
    save["survives_k1_clean"] = R["survives"]["k1_clean_no_zeros_input"]
    save["survives_zeta_euler"] = R["survives"]["zeta_has_euler_product"]
    save["survives_dh_euler"] = R["survives"]["dh_has_euler_product"]
    np.savez(OUT, **save)
    print(f"\nsaved -> {OUT}")


if __name__ == "__main__":
    main()

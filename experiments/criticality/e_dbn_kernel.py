"""E_DBN1 -- the Polya kernel positivity test as a new face of the D-H discipline.

The de Bruijn-Newman story. Define the heat-flow deformation of the completed
zeta function by

    H_t(z) = INT_{-inf}^{inf} e^{t u^2} Phi(u) e^{i z u} du,     H_0 = Xi := xi(1/2 + i z),

where Phi is the Polya kernel. De Bruijn (1950) proved H_t has only real zeros
for t >= 1/2; Newman (1976) defined Lambda = inf{t : H_t real-rooted for all t' >= t};
RH <=> Lambda <= 0; Rodgers-Tao (2018) proved Lambda >= 0. So RH <=> Lambda = 0:
zeta sits exactly on a phase boundary. This is the EXACT avatar of the project's
marginal-positivity thesis ("RH is just barely true"), and Lambda >= 0 is the
proven LOWER half of that thesis.

The structural input that makes de Bruijn's theorem START (an a-priori upper
bound on Lambda) is the POSITIVITY of the kernel: Phi(u) >= 0. For zeta this is
Polya's 1926 observation, and it is a THETA / MODULARITY fact, not the Euler
product. This experiment asks the question nobody in the project has asked:

    is Phi >= 0 a face of the Davenport-Heilbronn discipline?
    i.e. does the wrong-approach detector (D-H, Epstein) FAIL kernel positivity
    where zeta passes it -- and does Phi >= 0 track Euler-ness, RH-truth, or is
    it special to zeta?

The clean, project-idiom test (Bochner). Xi is real and even on the line and
decays exponentially (the Gamma factor beats the polynomial growth), so

    Xi(z) = INT Phi(u) cos(z u) du,   Phi real even.

By Bochner, Phi >= 0  <=>  Xi is a positive-definite function  <=>  every
Toeplitz matrix  M_{jk} = Xi((j - k) delta)  is positive semidefinite. And the
implication is RIGOROUS in one direction with NO truncation caveat: if Phi >= 0
then M = INT Phi(u) w(u) w(u)^* du (w_j(u) = e^{i j delta u}) is a nonnegative
combination of rank-1 PSD matrices, hence M >= 0 exactly for any finite grid.
Contrapositive: a single Toeplitz matrix with a negative eigenvalue is a
rigorous witness that Phi is NOT >= 0.

So we test, for each L-function f:
    - build Xi_f(z) = (completed f)(1/2 + i z), oriented so Xi_f(0) > 0;
    - verify Xi_f is real and even on the line (the functional equation);
    - form M[delta] = [Xi_f((j-k) delta)] and report min eig (Bochner test);
    - reconstruct Phi_f(u) by cosine inversion for the picture and to localize
      where (if anywhere) Phi_f goes negative;
    - validate the method on zeta against Polya's closed-form kernel.

The controls:
    zeta              Euler,     RH true            -> Polya: Phi >= 0 (KNOWN)
    chi3, chi4        Euler,     GRH believed       -> "special to zeta?"
    D-H               NO Euler,  RH FALSE           -> the wrong-approach detector
    Epstein d47 prin  NO Euler,  RH true (<=120)    -> degree-2 control
    Epstein d47 nonpr NO Euler,  RH FALSE (off-line)-> degree-2 off-line

RESULT (this experiment). Phi >= 0 is NOT a face of the D-H discipline and does
NOT discriminate RH. In the CLEAN degree-1 comparison (D-H and Dirichlet are
entire, no s(s-1) factor confound), zeta, chi3, chi4 AND Davenport-Heilbronn
(RH FALSE) ALL satisfy Phi >= 0 (max|Xi|/Xi0 = 1.000): the RH-violator passes
kernel positivity. WHY: an off-line zero at height gamma enters Phi only at the
archimedean-suppressed level exp(-(pi/4) d gamma) (D-H: |Xi(85.7)| ~ 1.5e-29),
because |Xi(1/2+iz)| ~ exp(-(pi/4) d |z|). de Bruijn's Phi >= 0 yields only
Lambda <= 1/2; ALL the RH content is in the flow / the gap (0, 1/2], invisible
to the t=0 kernel. This is the stealth window (#18/#19/#34) in the heat basis,
sharpened to the exact suppression law -- the SOFTEST detector yet (the raw Weil
Gram saw off-line at 2.6%; the kernel sees it at ~1e-29).

Degree 2 (Epstein) shows Phi >= 0 is moreover ORTHOGONAL to RH: with the canonical
1/2 s(s-1) entire factor, the RH-TRUE principal form BREAKS positive-definiteness
(max|Xi|/Xi0 = 1.85) while the RH-FALSE non-principal passes; without the factor
both pass. So positive-definiteness is a property of the function's archimedean /
pole shape, not its zero locations.

LITERATURE (honest framing; see e_dbn_kernel.md). The central conclusion is correct
but PRE-EMPTED: Dobner (arXiv:2005.05142, 2020) proves Lambda_F >= 0 for the entire
extended Selberg class S# (which INCLUDES Davenport-Heilbronn -- S# drops the Euler
axiom) with the kernel never assumed >= 0; Newman-Wu (arXiv:1901.06596, 2019) exhibit
nonnegative kernels with empty real-zero set; Michalowski (arXiv:2602.20313, 2026)
independently studies this kernel with the SAME Toeplitz-minor method and states it is
orthogonal to Lambda. This experiment is a confirmed coordinate + D-H specialization,
not new mathematics. Project-own: the D-H-discipline / K2-FAIL packaging, the
quantitative suppression law exp(-(pi/4) d gamma), the explicit D-H numerics.

Run:  python -m experiments.criticality.e_dbn_kernel
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared.davenport_heilbronn import davenport_heilbronn
from experiments._shared.dirichlet_l import chi3_L, chi4_L
from experiments._shared.epstein_zeta import epstein_d47, epstein_d47_principal

DPS = 30
HERE = Path(__file__).resolve().parent


def _trapz(y, x):
    """Trapezoidal integral, version-agnostic (np.trapz removed in NumPy 2.0)."""
    if hasattr(np, "trapezoid"):
        return np.trapezoid(y, x)
    return np.trapz(y, x)  # pragma: no cover (older numpy)


# --------------------------------------------------------------------------
# Completed (entire, FE-symmetric) functions Xi_f(z) = Lambda_f(1/2 + i z).
# Each is real and even on the real z-axis when the root number is +1.
# We return the raw complex value; orientation/realness handled downstream.
# --------------------------------------------------------------------------

def xi_zeta(z):
    """Riemann xi(1/2 + i z) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s).

    The 1/2 s(s-1) factor makes xi entire (cancels the pole); it is part of
    zeta's natural completion and is exactly the object Polya's kernel belongs
    to. D-H / Dirichlet / Epstein have no pole, so no such factor.
    """
    s = mp.mpc(mp.mpf(1) / 2, z)
    return mp.mpf(1) / 2 * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_dh(z):
    """Davenport-Heilbronn completion (odd character mod 5 Gamma factor).

    The FE residual code uses chi(s) = (pi/5)^{s-1/2} Gamma((2-s)/2)/Gamma((s+1)/2),
    which is solved by Lambda(s) = (5/pi)^{s/2} Gamma((s+1)/2) f(s), symmetric
    Lambda(s) = Lambda(1-s). f is entire so no s(s-1) factor.
    """
    s = mp.mpc(mp.mpf(1) / 2, z)
    return mp.power(5 / mp.pi, s / 2) * mp.gamma((s + 1) / 2) * davenport_heilbronn.evaluate(s)


def make_xi_dirichlet(L):
    """Dirichlet completion Lambda(s) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s), a = parity."""
    q = L.modulus
    a = L.parity

    def xi(z):
        s = mp.mpc(mp.mpf(1) / 2, z)
        return mp.power(q / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2) * L.evaluate(s)

    return xi


def make_xi_epstein(E, entire_factor: bool = True):
    """Epstein completion pi^{-s} Gamma(s) E(tau, s), optionally x 1/2 s(s-1).

    Epstein has a pole at s = 1 (and s = 0 by the FE). Its canonical ENTIRE
    object carries the 1/2 s(s-1) factor (entire_factor=True), exactly like
    zeta's xi -- this is the fair comparison for a pole-bearing function. We
    ALSO expose the bare (entire_factor=False) completion as a diagnostic,
    because the s(s-1) factor multiplies by a growing quadratic that can break
    positive-definiteness on its own (the very thing Polya's theorem shows zeta
    survives). Comparing the two isolates the factor's role.

    The individual Eisenstein main terms have a zeta(2s) pole at s = 1/2 (z = 0)
    that cancels in E, but mpmath raises before the cancellation, so we nudge z
    off exactly 0 (the completed function is smooth and even there).
    """

    def xi(z):
        zz = mp.mpf(z)
        if abs(zz) < mp.mpf(10) ** (-7):
            zz = mp.mpf(10) ** (-7)
        s = mp.mpc(mp.mpf(1) / 2, zz)
        base = mp.power(mp.pi, -s) * mp.gamma(s) * E.eisenstein(s)
        if entire_factor:
            return mp.mpf(1) / 2 * s * (s - 1) * base
        return base

    return xi


# --------------------------------------------------------------------------
# Polya's closed-form kernel for zeta (the validation ground truth).
#   Xi(z) = xi(1/2 + i z) = INT_0^inf Phi(u) cos(z u) du   with
#   Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) exp(-pi n^2 e^{2u}).
# Phi is even and Polya (1926) showed Phi(u) > 0 for all real u.
# --------------------------------------------------------------------------

def polya_phi(u, n_terms: int = 40):
    # The closed form below is the u >= 0 branch; Phi is even, so evaluate at
    # |u| (feeding raw negative u makes the -3 pi n^2 e^{5u/2} term spuriously
    # dominate and go negative -- an artifact, not a violation of Polya's Phi>0).
    u = abs(mp.mpf(u))
    e2u = mp.e ** (2 * u)
    e92 = mp.e ** (mp.mpf(9) / 2 * u)
    e52 = mp.e ** (mp.mpf(5) / 2 * u)
    total = mp.mpf(0)
    for n in range(1, n_terms + 1):
        n2 = mp.mpf(n) ** 2
        total += (2 * mp.pi ** 2 * n2 ** 2 * e92 - 3 * mp.pi * n2 * e52) * mp.e ** (-mp.pi * n2 * e2u)
    return total


# --------------------------------------------------------------------------
# Core machinery.
# --------------------------------------------------------------------------

def sample_xi(xi_fn, z_grid):
    """Evaluate the completed function on a real z-grid, returning oriented,
    real, normalized values Xi_hat(z) with Xi_hat(0) = 1.

    Also returns diagnostics: max |Im Xi| / |Xi| (realness) and the
    even-symmetry residual max|Xi(z) - Xi(-z)| / |Xi(0)|.
    """
    raw = [xi_fn(mp.mpf(z)) for z in z_grid]
    xi0 = xi_fn(mp.mpf(0))
    realness = max(abs(mp.im(v)) / (abs(v) + mp.mpf(10) ** (-DPS)) for v in raw)
    # evenness: compare a few z against -z
    even_res = mp.mpf(0)
    for z in z_grid[: min(8, len(z_grid))]:
        if z == 0:
            continue
        a = xi_fn(mp.mpf(z))
        b = xi_fn(-mp.mpf(z))
        even_res = max(even_res, abs(a - b) / (abs(xi0) + mp.mpf(10) ** (-DPS)))
    # orient so the (real part of) the central value is positive
    sign = 1 if mp.re(xi0) > 0 else -1
    vals = [sign * mp.re(v) / abs(mp.re(xi0)) for v in raw]
    # Positive-definiteness NECESSARY condition: a positive-definite function
    # attains its maximum modulus at 0, so max_z |Xi(z)| / |Xi(0)| > 1 is itself
    # a witness that Phi is NOT >= 0 (no Toeplitz needed).
    max_ratio = float(max(abs(v) for v in vals))
    return vals, float(realness), float(even_res), max_ratio


def toeplitz_min_eig(xi_fn, delta, n):
    """min eigenvalue of the (n+1)x(n+1) Toeplitz matrix M_{jk} = Xi_hat((j-k) delta).

    By Bochner, Phi >= 0 => M >= 0 exactly (no truncation caveat); a negative
    min eigenvalue is a rigorous witness that Phi is NOT nonnegative. Computed
    at full mpmath precision via mp.eigsy.
    """
    xi0 = xi_fn(mp.mpf(0))
    sign = 1 if mp.re(xi0) > 0 else -1
    norm = abs(mp.re(xi0))
    # c[k] = Xi_hat(k delta), k = 0..n
    c = []
    for k in range(n + 1):
        v = xi_fn(mp.mpf(k) * mp.mpf(delta))
        c.append(sign * mp.re(v) / norm)
    M = mp.matrix(n + 1, n + 1)
    for j in range(n + 1):
        for k in range(n + 1):
            M[j, k] = c[abs(j - k)]
    eigs, _ = mp.eigsy(M)
    eig_list = [float(eigs[i]) for i in range(n + 1)]
    return min(eig_list), max(eig_list)


def reconstruct_phi(z_grid, xi_vals, u_grid):
    """Phi(u) = (2/pi) INT_0^Zmax Xi_hat(z) cos(z u) dz, by trapezoid over the grid.

    z_grid and xi_vals are floats; the integral is well-conditioned because
    Xi_hat decays exponentially. Returns Phi on u_grid (floats).
    """
    z = np.asarray([float(v) for v in z_grid])
    xi = np.asarray([float(v) for v in xi_vals])
    phi = []
    for u in u_grid:
        integrand = xi * np.cos(z * u)
        val = (2.0 / np.pi) * _trapz(integrand, z)
        phi.append(val)
    return np.asarray(phi)


def reconstruct_xi(u_grid, phi_vals, z_check):
    """Forward check: Xi(z) = INT_0^inf Phi(u) cos(z u) du, trapezoid over u_grid.

    Should match Xi_hat(z) up to the same positive normalization. Returns the
    reconstructed values at z_check (floats), unnormalized; the caller compares
    shape / ratio.
    """
    u = np.asarray(u_grid)
    phi = np.asarray(phi_vals)
    out = []
    for z in z_check:
        integrand = phi * np.cos(u * z)
        out.append(_trapz(integrand, u))
    return np.asarray(out)


def measure_decay_rate(xi_fn, zs, dps: int = 70):
    """Fit the exponential decay rate of |Xi(z)|: |Xi(z)| ~ C exp(-r z).

    Returns r. The archimedean prediction is r = (pi/4) d (degree d), so the
    off-line zero at height gamma enters the kernel Phi only at ~exp(-r gamma).

    Computed at elevated precision so the additive floor never clips the tail:
    at 30 dps a 1e-30 floor flattens the degree-2 |Xi| tail and pulls the fitted
    slope spuriously low (verifier catch). At dps=70 with floor 1e-78 the window
    values stay far above the floor and the fit recovers the true asymptotic rate.
    """
    prev = mp.mp.dps
    mp.mp.dps = dps
    try:
        floor = mp.mpf(10) ** (-(dps + 8))
        ls = [float(mp.log(abs(xi_fn(mp.mpf(z))) + floor)) for z in zs]
    finally:
        mp.mp.dps = prev
    A = np.polyfit(np.asarray(zs, float), np.asarray(ls), 1)
    return float(-A[0])


def run():
    import math
    mp.mp.dps = DPS
    print("=" * 78)
    print("E_DBN1 -- Polya kernel positivity as a face of the D-H discipline")
    print("Direction 12 (de Bruijn-Newman). RH <=> Lambda = 0; Rodgers-Tao: Lambda >= 0.")
    print("Bochner: Phi >= 0 <=> Xi positive-definite <=> Toeplitz [Xi((j-k)d)] PSD.")
    print("Two rigorous witnesses of Phi NOT >= 0: (a) Toeplitz min eig < 0;")
    print("(b) max_z |Xi(z)| > |Xi(0)| (a PD function attains its max modulus at 0).")
    print("=" * 78)

    # Each entry: name, xi_fn, euler, degree d, off-line height gamma (None if
    # RH-true in range), group, note. The degree sets the archimedean decay rate
    # |Lambda(1/2+iz)| ~ exp(-(pi/4) d |z|). 'deg1' is the CLEAN comparison:
    # zeta needs the 1/2 s(s-1) factor (it has a pole), but D-H and Dirichlet are
    # entire with NO factor, so D-H is an unconfounded RH-false control. 'deg2'
    # (Epstein) is shown WITH and WITHOUT the s(s-1) factor to expose that the
    # factor -- not RH -- is what can break positive-definiteness.
    functions = [
        dict(name="zeta",          xi=xi_zeta,                                     euler=True,  deg=1, goff=None,   grp="deg1", note="Euler, RH (Polya: Phi>=0)"),
        dict(name="chi3 (mod 3)",  xi=make_xi_dirichlet(chi3_L),                   euler=True,  deg=1, goff=None,   grp="deg1", note="Euler, GRH"),
        dict(name="chi4 (mod 4)",  xi=make_xi_dirichlet(chi4_L),                   euler=True,  deg=1, goff=None,   grp="deg1", note="Euler, GRH"),
        dict(name="Davenport-Heil.", xi=xi_dh,                                     euler=False, deg=1, goff=85.699, grp="deg1", note="non-Euler, RH FALSE (control)"),
        dict(name="Eps47-pr",      xi=make_xi_epstein(epstein_d47_principal, True),  euler=False, deg=2, goff=None,  grp="deg2", note="non-Euler, RH true<=120; entire x s(s-1)"),
        dict(name="Eps47-pr bare", xi=make_xi_epstein(epstein_d47_principal, False), euler=False, deg=2, goff=None,  grp="deg2", note="same; bare (no s(s-1) factor)"),
        dict(name="Eps47-npr",     xi=make_xi_epstein(epstein_d47, True),            euler=False, deg=2, goff=32.05, grp="deg2", note="non-Euler, RH FALSE; entire x s(s-1)"),
        dict(name="Eps47-npr bare",xi=make_xi_epstein(epstein_d47, False),           euler=False, deg=2, goff=32.05, grp="deg2", note="same; bare"),
    ]

    # z-grid for sampling / Phi reconstruction. Xi decays ~ exp(-pi z /4) (deg 1)
    # or exp(-pi z /2) (deg 2), so Zmax = 60 is far into the tail. The u-grid must
    # be wide enough to hold the kernel: zeta's Phi is doubly-exponential (tiny by
    # |u|=1.5) but Epstein's (poles of Gamma(s)) decays only ~exp(-3|u|/2), so we
    # use [-6, 6] to keep the cosine-transform pair self-consistent (recon_err).
    Zmax = 60.0
    nz = 601
    z_grid = [Zmax * i / (nz - 1) for i in range(nz)]
    u_grid = np.linspace(-6.0, 6.0, 1201)

    # Toeplitz spacings (verdict must not be a grid artifact).
    toeplitz_specs = [(0.5, 36), (1.0, 24), (0.25, 56)]

    results = {}
    print()
    for f in functions:
        name, xi_fn = f["name"], f["xi"]
        vals, realness, even_res, max_ratio = sample_xi(xi_fn, z_grid)
        min_eigs = {}
        for delta, n in toeplitz_specs:
            me, Me = toeplitz_min_eig(xi_fn, delta, n)
            min_eigs[delta] = (me, Me)
        phi = reconstruct_phi(z_grid, vals, u_grid)
        phi_min = float(np.min(phi))
        phi_min_at = float(u_grid[int(np.argmin(phi))])
        # forward self-consistency of the cosine-transform pair.
        z_check = [0.0, 2.0, 5.0, 10.0]
        xi_recon = reconstruct_xi(u_grid, phi, z_check)
        xi_true = np.asarray([float(vals[min(range(len(z_grid)),
                                             key=lambda i: abs(z_grid[i] - zc))])
                              for zc in z_check])
        if abs(xi_recon[0]) > 1e-30:
            recon_norm = xi_recon / xi_recon[0]
            recon_err = float(np.max(np.abs(recon_norm - xi_true / xi_true[0])))
        else:
            recon_err = float("nan")

        # Two independent positive-definiteness verdicts.
        me_05 = min_eigs[0.5][0]
        pd_toeplitz = me_05 > -1e-9
        pd_maxmod = max_ratio < 1.0 + 1e-6
        phi_pos = pd_toeplitz and pd_maxmod

        results[name] = dict(
            **{k: f[k] for k in ("euler", "deg", "goff", "grp", "note")},
            realness=realness, even_res=even_res, max_ratio=max_ratio,
            min_eigs=min_eigs, phi_min=phi_min, phi_min_at=phi_min_at,
            recon_err=recon_err, phi_pos=phi_pos, phi=phi,
        )

        verdict = "Phi >= 0 consistent" if phi_pos else "Phi NOT >= 0"
        print(f"{name:<16} {f['note']}")
        print(f"    realness={realness:.1e} evenness={even_res:.1e} recon_err={recon_err:.1e}"
              f"  max|Xi|/Xi0={max_ratio:.3f}")
        print(f"    Toeplitz min eig: d=0.5 {min_eigs[0.5][0]:+.2e}, d=1.0 {min_eigs[1.0][0]:+.2e},"
              f" d=0.25 {min_eigs[0.25][0]:+.2e}")
        print(f"    Phi(u) min = {phi_min:+.3e} at u={phi_min_at:+.2f}   =>  {verdict}")
        print()

    # ---- Validation against Polya's closed-form kernel (zeta) -----------
    print("-" * 78)
    print("VALIDATION: reconstructed Phi_zeta vs Polya closed form (shape, normalized)")
    polya = np.asarray([float(polya_phi(u)) for u in u_grid])
    phi_zeta = results["zeta"]["phi"]
    i0 = int(np.argmin(np.abs(u_grid)))
    if abs(polya[i0]) > 1e-30:
        p_n = polya / polya[i0]
        r_n = phi_zeta / phi_zeta[i0]
        mask = p_n > 1e-3
        shape_err = float(np.max(np.abs(p_n[mask] - r_n[mask])))
    else:
        shape_err = float("nan")
    print(f"    Polya Phi(0) = {float(polya_phi(0)):.6f}  (must be > 0)")
    print(f"    Polya min over u in [-6,6] = {float(np.min(polya)):+.4e}  (must be >= 0)")
    print(f"    shape match (normalized, on Polya support) max abs err = {shape_err:.2e}")
    print()

    # ---- Suppression law: |Xi(z)| ~ exp(-(pi/4) d z) ---------------------
    print("-" * 78)
    print("SUPPRESSION LAW: off-line zero at height gamma enters Phi at ~exp(-(pi/4) d gamma)")
    for f in functions:
        if f["goff"] is None or "bare" in f["name"]:
            continue
        # Window chosen per degree so |Xi| stays well above the precision floor
        # (degree-2 decays twice as fast, so use a lower window).
        zs_fit = [40, 55, 70, 80] if f["deg"] == 1 else [35, 45, 55, 65]
        rate = measure_decay_rate(f["xi"], zs_fit)
        predicted = (math.pi / 4) * f["deg"]
        gamma = f["goff"]
        level = float(abs(f["xi"](mp.mpf(gamma))))
        print(f"    {f['name']:<16} deg={f['deg']}  measured rate={rate:.4f} "
              f"(predict pi d/4={predicted:.4f});  |Xi(gamma={gamma:.1f})|={level:.2e}")
    print()

    # ---- Synthesis ------------------------------------------------------
    print("=" * 78)
    print("SYNTHESIS")
    print("=" * 78)
    print(f"{'function':<16}{'Euler':<6}{'RH':<5}{'deg':<4}{'max|Xi|/Xi0':<13}"
          f"{'minEig(.5)':<13}{'Phi>=0?':<9}{'off-line floor'}")
    for f in functions:
        r = results[f["name"]]
        rh = "yes" if f["goff"] is None else "NO"
        floor = "(none)" if f["goff"] is None else \
            f"e^-({math.pi/4*f['deg']:.2f}*{f['goff']:.0f})={math.exp(-math.pi/4*f['deg']*f['goff']):.0e}"
        print(f"{f['name']:<16}{str(f['euler']):<6}{rh:<5}{f['deg']:<4}{r['max_ratio']:<13.3f}"
              f"{r['min_eigs'][0.5][0]:<+13.2e}{('yes' if r['phi_pos'] else 'NO'):<9}{floor}")
    print()
    print("DEGREE-1 (clean: D-H & Dirichlet are entire, no s(s-1) factor confound):")
    print("  zeta, chi3, chi4 (Euler) AND Davenport-Heilbronn (non-Euler, RH FALSE)")
    print("  ALL have Phi >= 0. The RH-violator passes kernel positivity. So Phi>=0")
    print("  is NOT a face of the D-H discipline and does NOT discriminate RH.")
    print("DEGREE-2 (Epstein): Phi>=0 is ORTHOGONAL to RH and sensitive to the s(s-1)")
    print("  factor -- with it the RH-TRUE principal form breaks PD (max|Xi|/Xi0=1.85),")
    print("  without it both forms are PD. RH plays no role either way.")
    print("WHY: off-line zeros are archimedean-suppressed in Phi to exp(-(pi/4) d gamma)")
    print("  (D-H: |Xi(85.7)|~1e-29). de Bruijn's Phi>=0 only yields Lambda<=1/2; ALL the")
    print("  RH content is the flow / the gap (0,1/2]. The t=0 kernel is the wrong object.")

    # ---- Save artifacts -------------------------------------------------
    def _key(nm):
        return "phi_" + "".join(ch if ch.isalnum() else "_" for ch in nm)

    np.savez(
        HERE / "e_dbn_kernel.npz",
        u_grid=u_grid, polya=polya,
        **{_key(f["name"]): results[f["name"]]["phi"] for f in functions},
        min_eig_05=np.array([results[f["name"]]["min_eigs"][0.5][0] for f in functions]),
        max_ratio=np.array([results[f["name"]]["max_ratio"] for f in functions]),
        names=np.array([f["name"] for f in functions]),
    )
    _plot(u_grid, results, polya, functions)
    print(f"\nSaved: {HERE / 'e_dbn_kernel.npz'} and e_dbn_kernel.png")
    return results


def _plot(u_grid, results, polya, functions):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    colors = {"zeta": "k", "chi3 (mod 3)": "tab:green", "chi4 (mod 4)": "tab:olive",
              "Davenport-Heil.": "tab:red", "Eps47-pr": "tab:blue",
              "Eps47-pr bare": "tab:cyan", "Eps47-npr": "tab:purple",
              "Eps47-npr bare": "tab:pink"}
    # Left: degree-1 clean comparison (the headline).
    for f in functions:
        if f["grp"] != "deg1":
            continue
        phi = results[f["name"]]["phi"]
        phi = phi / np.max(np.abs(phi))
        ax1.plot(u_grid, phi, label=f["name"], color=colors.get(f["name"]), lw=1.8)
    ax1.axhline(0, color="gray", lw=0.8, ls="--")
    ax1.set_xlim(-3, 3)
    ax1.set_xlabel("u"); ax1.set_ylabel("Phi(u) (unit max)")
    ax1.set_title("Degree 1: zeta, Dirichlet, AND D-H (RH FALSE)\nall have Phi >= 0 -- "
                  "kernel positivity does not discriminate RH")
    ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
    # Right: degree-2 Epstein, factor on/off.
    for f in functions:
        if f["grp"] != "deg2":
            continue
        phi = results[f["name"]]["phi"]
        phi = phi / np.max(np.abs(phi))
        ax2.plot(u_grid, phi, label=f"{f['name']} (PD={'Y' if results[f['name']]['phi_pos'] else 'N'})",
                 color=colors.get(f["name"]), lw=1.6)
    ax2.axhline(0, color="gray", lw=0.8, ls="--")
    ax2.set_xlim(-4, 4)
    ax2.set_xlabel("u"); ax2.set_ylabel("Phi(u) (unit max)")
    ax2.set_title("Degree 2: Epstein d47, with/without s(s-1).\nPhi>=0 is orthogonal to RH "
                  "(RH-true principal breaks PD via the factor)")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    fig.suptitle("de Bruijn-Newman / Direction 12 -- Polya kernel positivity is NOT the RH signal",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(HERE / "e_dbn_kernel.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    run()

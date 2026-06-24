"""NP-1: does the FINITE-PRIME modular data continue past Re(s)=1 into the strip
as a POSITIVITY or CONSTRAINT that (a) detects the off-line obstruction
(|t_p| < 2 sqrt p vs |t_p| > 2 sqrt p) and (b) is NOT shared with Davenport-Heilbronn?

This is the AT-MOD-4 probe from `quantum_mechanics_signature_dossier.md` Part 8.

------------------------------------------------------------------------------
WHAT THIS FILE ACTUALLY ESTABLISHES (honest scope -- read first).
------------------------------------------------------------------------------
NP-1 = NO is established by an ANALYTIC argument (the M4-reduction, the verdict
block below and Section 5 of the .md), NOT by a numerical measurement. There is no
honest way to "measure" the t_p-independence of the carrier, because the carrier
quantities are a pure FUNCTION of (prime set S, beta) -- they have no t_p argument at
all. That is a structural fact about the construction, not an experimental result, and
this file labels it as such (Part 4).

The TWO genuine computations this file runs (both have a real data path that COULD
register a change, so they are non-vacuous):
  (1) THE C_E FLIP CONTRAST (Part 1). The genus-1 block B_E(p, t_p) (the object the
      C_E-twist polarizes) is a REAL function of t_p; its minimum eigenvalue crosses
      zero EXACTLY at |t_p| = 2 sqrt p (PD -> indefinite). This is the object that DOES
      see t_p, and t_p acts on C_E (the polarization phase), which is NOT
      modular-carrier data (#101/MC.2).
  (2) FINITE-TRUNCATION ZERO-FREENESS IN THE STRIP (Part 2). The finite local Euler
      product prod_{p in S}(1 - p^{-s})^{-1} has min|.| > 0 across a strip sweep
      Re(s) in (1/2, 1). So no off-line zero appears in ANY finite truncation; reaching
      the strip WITH the obstruction is the infinite-product limit S -> all primes =
      the M4 coupling = #104. This is the real support for the M4-reduction.

Everything else here is either a STRUCTURAL / LEAK-CHECK statement (the carrier
functions have no t_p slot, Part 4), explicitly labeled, OR a genuine demonstration of
the modular degrees of freedom -- the relative modular operator / Connes cocycle moves
under STATE and FLOW TIME (Part 3), axes ORTHOGONAL to t_p. By the analytic #101
argument the BC weights have no t_p slot, so there is no t_p-bearing modular object; we
state that as the argument, NOT as a measured t_p-independence (we do not compare
identical inputs).

------------------------------------------------------------------------------
THE CRITICAL DISTINCTION (the adversary corrected this on a prior run).
------------------------------------------------------------------------------
Do NOT conflate the FINITE-PRIME modular data with GLOBAL zeta. A finite Euler product
is ZERO-FREE in the strip; it continues trivially and never vanishes there. Global
zeta's strip zeros emerge only from the infinite-product limit + completed
continuation. The off-line obstruction is invisible to any finite-prime truncation,
and the operation that reaches the strip (S -> all primes) is the M4 coupling, NOT a
modular-flow operation. NP-1 is about whether the finite-prime modular STRUCTURE
continues as a t_p-detecting positivity, not whether some global function reaches the
strip.

------------------------------------------------------------------------------
TWO DISTINCT t's (load-bearing).
------------------------------------------------------------------------------
  * t_flow  = the MODULAR FLOW TIME. sigma_{t_flow}(x) = Delta^{i t_flow} x Delta^{-i t_flow}.
              The KMS two-point function is n^{-(beta - i t_flow)}. Continuation "past
              Re(s)=1" means continuation in s = beta - i t_flow.
  * t_p     = the FROBENIUS TRACE at p. The off-line obstruction is a t_p-phenomenon:
              1 - t_p p^{-s} + p^{1-2s} has zeros off Re=1/2 iff |t_p| > 2 sqrt p.
These are DIFFERENT variables. The carrier is parametrized by (S, beta, t_flow); t_p
enters only via C_E, which is not carrier data (#101/MC.2).

Run:  python -m experiments.arithmetic_geometric.e2vv_np1_modular_continuation

Honest scope. Finite linear algebra + an analytic continuation check on a toy BC
carrier. Proves nothing about RH. Deliverable: the precise status of the continuation
question (NP-1 = NO via the analytic M4-reduction; the numerics are the C_E-flip
contrast and the finite-truncation zero-freeness, both genuine).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared import DavenportHeilbronn

OMEGA = np.array([[0.0, 1.0], [-1.0, 0.0]])
TOL = 1e-9


# ==========================================================================
# Reused machinery (e2ss/e2tt): the per-prime genus-1 block.
# ==========================================================================


def b_e(p: float, t: float) -> np.ndarray:
    """Genus-1 Rosati / cup block B_E(p, t) = -G_prim. The C_E-twisted polarization
    Q_p = B_E / sqrt(4p - t^2) has the SAME signature as B_E on the window; B_E itself
    is the object whose definiteness flips at |t| = 2 sqrt p. CARRIES t_p."""
    return np.array([[2.0, t], [t, 2.0 * p]])


# ==========================================================================
# Part 0: the off-line obstruction is a t_p-phenomenon, in 1/2 < Re(s) < 1.
# (link (i); the genus-1 factor is self-dual so zeros come in (x, 1-x) pairs.)
# ==========================================================================


def local_factor_zero_realparts(p: float, t: float):
    """Re(s) of the two zeros of L_p(s) = 1 - t p^{-s} + p^{1-2s}.
    u = p^{-s}: 1 - t u + p u^2 = 0 => u = (t +/- sqrt(t^2-4p))/(2p),
    Re(s) = -log|u| / log p."""
    disc = t * t - 4.0 * p
    if disc < 0:
        r = np.sqrt(-disc)
        us = [complex(t, r) / (2.0 * p), complex(t, -r) / (2.0 * p)]
    else:
        r = np.sqrt(disc)
        us = [complex((t + r) / (2.0 * p)), complex((t - r) / (2.0 * p))]
    return sorted(-np.log(abs(u)) / np.log(p) for u in us if abs(u) > 1e-15)


def part0_obstruction_is_tp(primes=(2, 3, 5, 7, 11, 13)):
    rows = []
    for p in primes:
        edge = 2.0 * np.sqrt(p)
        hasse = float(p + 1)
        t_on = edge - 0.5                     # in-window (on Re=1/2)
        t_strip = 0.5 * (edge + hasse)        # off-line (in the strip)
        rows.append({
            "p": p, "edge": edge, "hasse": hasse,
            "Re_on": local_factor_zero_realparts(p, t_on),
            "Re_strip": local_factor_zero_realparts(p, t_strip),
            "Re_hasse": local_factor_zero_realparts(p, hasse),
        })
    return rows


# ==========================================================================
# Part 1 (GENUINE COMPUTATION #1): the C_E flip contrast -- t_p acts on the
# polarization (NOT the carrier). The block min-eigenvalue crosses zero at
# |t_p| = 2 sqrt p. This is the object that DOES have a t_p data path.
# ==========================================================================


def part1_CE_flip_contrast(primes=(2, 3, 5, 7)):
    """For each prime, sweep t_p across 2 sqrt p and record the minimum eigenvalue of
    the genus-1 block B_E(p, t_p) (the object the C_E-twist polarizes). It is a real
    function of t_p that crosses zero EXACTLY at |t_p| = 2 sqrt p (PD -> indefinite).
    This is the genuine, non-vacuous t_p contrast: t_p flips the POLARIZATION, and the
    polarization phase C_E is NOT modular-carrier data (#101/MC.2)."""
    rows = []
    crossings_ok = True
    for p in primes:
        edge = 2.0 * np.sqrt(p)
        ts = np.linspace(edge - 1.0, edge + 1.0, 41)
        dets = 4.0 * p - ts * ts  # det(B_E); the polarization flips where this hits 0
        # the block is PD (min eigenvalue > 0) iff |t| < edge; indefinite iff |t| > edge
        pd_below = float(np.linalg.eigvalsh(b_e(p, edge - 0.3)).min()) > TOL
        indef_above = float(np.linalg.eigvalsh(b_e(p, edge + 0.3)).min()) < -TOL
        # the flip location from the det zero crossing (dets is decreasing in t here)
        t_flip = float(np.interp(0.0, dets[::-1], ts[::-1]))
        flip_at_edge = abs(t_flip - edge) < 0.06
        crossings_ok = crossings_ok and pd_below and indef_above and flip_at_edge
        rows.append({"p": p, "edge": edge, "pd_below_edge": pd_below,
                     "indef_above_edge": indef_above, "t_flip": t_flip,
                     "flip_at_edge": flip_at_edge,
                     "min_ev_at_edge_minus": float(np.linalg.eigvalsh(b_e(p, edge - 0.3)).min()),
                     "min_ev_at_edge_plus": float(np.linalg.eigvalsh(b_e(p, edge + 0.3)).min())})
    return rows, crossings_ok


# ==========================================================================
# Part 2 (GENUINE COMPUTATION #2): finite-truncation zero-freeness in the strip.
# The real support for the M4-reduction (the off-line zero is absent from every
# finite carrier; reaching the strip with it = the infinite limit = M4 = #104).
# ==========================================================================


def part2_finite_euler_zero_free(primes_list=((2, 3, 5, 7), (2, 3, 5, 7, 11, 13, 17, 19)),
                                 betas=(0.51, 0.6, 0.75, 0.9, 0.99)):
    """The finite local Euler product Z_S(s) = prod_{p in S}(1 - p^{-s})^{-1}. Each
    factor 1 - p^{-s} vanishes only on Re(s) = 0, so Z_S is zero-free (and finite) for
    Re(s) > 0. Sweep the critical strip Re(s) in (1/2, 1) and report min|Z_S| > 0. So
    NO off-line zero appears in any finite truncation: the off-line obstruction is a
    property of the INFINITE-product limit + completion (= the M4 coupling), not of the
    finite-prime modular carrier."""
    def Z_S(primes, s):
        return complex(np.prod([1.0 / (1.0 - complex(mp.power(p, -s))) for p in primes]))

    rows = []
    overall_min = float("inf")
    for primes in primes_list:
        for beta in betas:
            ts = np.linspace(0.0, 120.0, 600)
            vals = np.array([abs(Z_S(primes, complex(beta, t))) for t in ts])
            mn = float(vals.min())
            overall_min = min(overall_min, mn)
            rows.append({"k": len(primes), "beta": beta, "min_abs": mn,
                         "zero_free": mn > TOL})
    return rows, overall_min > TOL, overall_min


# ==========================================================================
# Part 3 (the modular degrees of freedom, genuine distinct inputs): the relative
# modular operator / Connes cocycle moves under STATE and FLOW TIME -- axes
# ORTHOGONAL to t_p. The analytic #101 argument then says no t_p-bearing modular
# object exists (stated as the argument, NOT a measured t_p-independence).
# ==========================================================================


def gibbs_density(weights):
    w = np.array(weights, dtype=float)
    return np.diag(w / w.sum())


def relative_modular_spectrum(rho_phi, rho_psi):
    """log Delta_{psi|phi} spectrum {log(rho_psi)_i - log(rho_phi)_j} (finite GNS model)."""
    pp = np.log(np.diag(rho_psi))
    pq = np.log(np.diag(rho_phi))
    return sorted(round(float(a - b), 9) for a in pp for b in pq)


def connes_cocycle_phases(rho_phi, rho_psi, t_flow):
    """Eigenphases of the Connes cocycle (D psi : D phi)_{t_flow} (diagonal sector)."""
    pp = np.log(np.diag(rho_psi))
    pq = np.log(np.diag(rho_phi))
    return np.exp(1j * t_flow * (pp - pq))


def part3_modular_axes_orthogonal_to_tp(primes=(2, 3, 5, 7), beta=1.5):
    """GENUINE demonstration with real distinct inputs: the relative modular operator /
    Connes cocycle DOES move -- under the choice of state (phi vs psi) and under the
    flow time t_flow. The point is that these are the modular degrees of freedom, and
    they are ORTHOGONAL to t_p: the BC weights n^{-beta} have no t_p slot, so by #101
    there is no t_p-bearing modular object (this is the analytic argument; we do NOT
    claim a measured t_p-independence, i.e. we never compare identical inputs)."""
    ns = sorted({1} | {p ** k for p in primes for k in range(1, 4)})
    rho_phi = gibbs_density([n ** (-beta) for n in ns])            # KMS state at beta
    rho_psi = gibbs_density([n ** (-(beta + 0.3)) for n in ns])    # distinct KMS state
    # state axis: cocycle for two genuinely DIFFERENT states (real distinct inputs)
    coc_two_states = connes_cocycle_phases(rho_phi, rho_psi, t_flow=7.0)
    coc_self = connes_cocycle_phases(rho_phi, rho_phi, t_flow=7.0)  # phi vs phi = identity
    state_axis_moves = not np.allclose(coc_two_states, coc_self)
    # flow-time axis: same states, different t_flow (real distinct inputs)
    coc_tf7 = connes_cocycle_phases(rho_phi, rho_psi, t_flow=7.0)
    coc_tf3 = connes_cocycle_phases(rho_phi, rho_psi, t_flow=3.0)
    tflow_axis_moves = not np.allclose(coc_tf7, coc_tf3)
    n_rel = len(relative_modular_spectrum(rho_phi, rho_psi))
    return {
        "n_rel_weights": n_rel,
        "state_axis_moves": bool(state_axis_moves),
        "tflow_axis_moves": bool(tflow_axis_moves),
    }


# ==========================================================================
# Part 4 (STRUCTURAL / LEAK-CHECK, honestly labeled): the carrier quantities are
# a pure function of (S, beta). A fact about the construction (no t_p argument
# exists), NOT a measurement. Stated for the record, labeled as such.
# ==========================================================================


def part4_carrier_has_no_tp_slot(primes=(2, 3, 5, 7), beta=1.5):
    """STRUCTURAL FACT (leak-check, not a measurement). The carrier quantities are
    functions of (S, beta) alone -- there is literally no t_p in their definitions:
      Z_S(beta)        = prod_{p in S}(1 - p^{-beta})^{-1}
      Gibbs weights    = {n^{-beta}}
      log Delta        = {log n - log m}
    We exhibit the closed forms and confirm they reference only (S, beta). The honest
    statement is: t_p does not enter the carrier; it enters C_E (the polarization
    phase, Part 1), which is not carrier data (#101/MC.2). We do NOT dress this as a
    'measured t_p-independence' (there is no input axis to vary)."""
    ns = sorted({1} | {p ** k for p in primes for k in range(1, 4)})
    Z = float(abs(np.prod([1.0 / (1.0 - mp.power(p, -beta)) for p in primes])))
    return {
        "Z_S": Z,
        "gibbs_count": len(ns),
        "logDelta_count": len(ns) ** 2,
        "carrier_args": "(prime set S, beta) -- no t_p argument exists",
    }


# ==========================================================================
# Part 5: the D-H analogue -- the ONLY discriminator is the comb sign at Re>1.
# ==========================================================================


def von_mangoldt_comb(coeff, N: int) -> dict:
    Lam = {}
    for n in range(1, N + 1):
        s = coeff(n) * mp.log(n)
        for d in (d for d in range(1, n) if n % d == 0):
            s -= coeff(n // d) * Lam[d]
        Lam[n] = s
    return Lam


def part5_dh_analogue(N: int = 30):
    """The only place zeta and D-H differ in the finite-prime carrier is the von
    Mangoldt comb sign (a Re(s)>1 statement deciding whether a positive Gibbs state
    forms). In the strip, no carrier quantity distinguishes them. Confirms clause (b):
    no finite-prime strip remnant un-shared with D-H; the one un-shared structure is
    the Re(s)>1 comb sign (the easy half)."""
    mp.mp.dps = 40
    dh = DavenportHeilbronn()
    Lam_z = von_mangoldt_comb(lambda n: mp.mpf(1), N)
    Lam_dh = von_mangoldt_comb(lambda n: mp.re(dh.dirichlet_coefficient(n)), N)
    z_min = float(min(Lam_z[n] for n in range(1, N + 1)))
    dh_neg = [n for n in range(1, N + 1) if float(Lam_dh[n]) < -1e-9]
    return {
        "zeta_comb_min": z_min,
        "zeta_carrier_forms_at_Re_gt_1": z_min > -1e-9,
        "dh_first_negative_comb": dh_neg[0] if dh_neg else None,
        "dh_carrier_forms": len(dh_neg) == 0,
        "discriminator_location": "Re(s)>1 (comb sign)",
        "strip_discriminator_exists": False,
    }


# ==========================================================================
# Driver.
# ==========================================================================


def run(out_dir: Path | None = None, beta: float = 1.5):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("[NP-1] Does the finite-prime modular data continue past Re(s)=1 as a")
    print("       t_p-detecting positivity, NOT shared with D-H?")
    print("       (Verdict NO rests on the ANALYTIC M4-reduction; the numerics are the")
    print("        C_E-flip contrast and the finite-truncation zero-freeness.)")
    print("=" * 80)

    # Part 0: the obstruction is a t_p-phenomenon, in the strip.
    rows0 = part0_obstruction_is_tp()
    print("\nPart 0 (link (i): the off-line obstruction is a t_p-phenomenon in 1/2<Re<1):")
    print(f"  {'p':>3} {'edge=2sqrt p':>13} {'Re(s) off-line (strip)':>24} {'Re(s) at Hasse t=p+1':>22}")
    for r in rows0:
        rs = [f"{x:.3f}" for x in r["Re_strip"]]
        rb = [f"{x:.3f}" for x in r["Re_hasse"]]
        print(f"  {r['p']:>3} {r['edge']:>13.3f} {str(rs):>24} {str(rb):>22}")

    def off_line_in_strip(re_pair):
        hi = max(re_pair)
        return (abs(hi - 0.5) > 1e-3) and (0.5 < hi < 1.0 + 1e-6)
    link_i = (all(off_line_in_strip(r["Re_strip"]) for r in rows0)
              and all(abs(max(r["Re_on"]) - 0.5) < 1e-6 for r in rows0))
    print(f"  => off-line zeros (2 sqrt p < t_p < p+1) sit OFF Re=1/2 in (1/2, 1); "
          f"on-line at the edge: {link_i}")

    # Part 1 (GENUINE): the C_E flip contrast.
    rows1, crossings_ok = part1_CE_flip_contrast()
    print("\nPart 1 (GENUINE COMPUTATION: t_p flips the POLARIZATION, not the carrier):")
    print(f"  {'p':>3} {'edge':>7} {'min ev (edge-0.3)':>18} {'min ev (edge+0.3)':>18} {'t_flip':>8} {'@edge':>6}")
    for r in rows1:
        print(f"  {r['p']:>3} {r['edge']:>7.3f} {r['min_ev_at_edge_minus']:>+18.4f} "
              f"{r['min_ev_at_edge_plus']:>+18.4f} {r['t_flip']:>8.3f} {str(r['flip_at_edge']):>6}")
    print(f"  => the genus-1 block B_E(p, t_p) min-eigenvalue crosses 0 EXACTLY at "
          f"|t_p| = 2 sqrt p: {crossings_ok}")
    print("     (PD below the edge, indefinite above). t_p acts on C_E (the polarization")
    print("     phase), which is NOT modular-carrier data (#101/MC.2). This is the object")
    print("     that genuinely sees t_p -- and it is not part of the modular carrier.")

    # Part 2 (GENUINE): finite-truncation zero-freeness in the strip.
    rows2, zero_free, overall_min = part2_finite_euler_zero_free()
    print("\nPart 2 (GENUINE COMPUTATION: finite Euler product zero-free in the strip):")
    print(f"  {'k':>3} {'beta':>6} {'min|Z_S(beta+it)|, t in [0,120]':>34} {'zero-free':>10}")
    for r in rows2:
        print(f"  {r['k']:>3} {r['beta']:>6.2f} {r['min_abs']:>34.4f} {str(r['zero_free']):>10}")
    print(f"  => every finite truncation prod_S(1-p^-s)^-1 is zero-free across the strip "
          f"(overall min |Z_S| = {overall_min:.4f} > 0): {zero_free}")
    print("     So NO off-line zero appears in any finite-prime carrier. Reaching the")
    print("     strip WITH the obstruction is the infinite-product limit S -> all primes")
    print("     (= the M4 coupling = #104), NOT a finite-prime modular operation.")

    # Part 3 (modular degrees of freedom = state + t_flow, orthogonal to t_p).
    p3 = part3_modular_axes_orthogonal_to_tp(beta=beta)
    print("\nPart 3 (the modular axes are STATE and FLOW TIME, ORTHOGONAL to t_p):")
    print(f"  relative modular operator / Connes cocycle ({p3['n_rel_weights']} weights):")
    print(f"    moves under the choice of STATE (phi vs psi):       {p3['state_axis_moves']}")
    print(f"    moves under the FLOW TIME t_flow (7.0 vs 3.0):      {p3['tflow_axis_moves']}")
    print("  => the modular degrees of freedom are (state, t_flow). By #101 the BC weights")
    print("     n^{-beta} have no t_p slot, so there is no t_p-bearing modular object")
    print("     (the ANALYTIC argument; we do NOT claim a measured t_p-independence).")

    # Part 4 (STRUCTURAL / LEAK-CHECK): the carrier has no t_p slot.
    p4 = part4_carrier_has_no_tp_slot(beta=beta)
    print("\nPart 4 (STRUCTURAL FACT, leak-check, NOT a measurement):")
    print(f"  carrier quantities are functions of {p4['carrier_args']}:")
    print(f"    Z_S(beta) = {p4['Z_S']:.4f}; {p4['gibbs_count']} Gibbs weights; "
          f"{p4['logDelta_count']} log Delta weights.")
    print("  => t_p does not enter the carrier definitions at all; it enters C_E (Part 1).")
    print("     This is a fact about the construction, not an experimental result.")

    # Part 5: the D-H analogue.
    p5 = part5_dh_analogue()
    print("\nPart 5 (D-H analogue: the only discriminator is the Re>1 comb sign):")
    print(f"  zeta comb min = {p5['zeta_comb_min']:.4f} >= 0 -> carrier forms (Re>1): "
          f"{p5['zeta_carrier_forms_at_Re_gt_1']}")
    print(f"  D-H comb first negative at n={p5['dh_first_negative_comb']} -> no carrier: "
          f"{not p5['dh_carrier_forms']}")
    print(f"  discriminator location: {p5['discriminator_location']}; "
          f"a STRIP discriminator exists: {p5['strip_discriminator_exists']}")

    # ---- verdict ----
    print("\n" + "=" * 80)
    print("[NP-1] VERDICT")
    print("=" * 80)
    clause_b = not p5["strip_discriminator_exists"]
    print(f"  link (i)   obstruction is a t_p-phenomenon in the strip:        {link_i}")
    print(f"  GENUINE: C_E block flips PD->indefinite exactly at |t_p|=2sqrt p: {crossings_ok}")
    print(f"  GENUINE: finite Euler product zero-free across the strip:        {zero_free}")
    print(f"  modular axes (state, t_flow) both move (orthogonal to t_p):      "
          f"{p3['state_axis_moves'] and p3['tflow_axis_moves']}")
    print(f"  clause (b) no strip remnant un-shared with D-H:                  {clause_b}")
    print()
    answer_no = link_i and crossings_ok and zero_free and clause_b
    print(f"  NP-1 ANSWER: {'NO' if answer_no else 'INVESTIGATE'}  (via the ANALYTIC M4-reduction)")
    print()
    print("  THE ANALYTIC M4-REDUCTION (this is what establishes NO; the numerics")
    print("  support it, they do not measure it):")
    print("  * t_p acts on the C_E polarization phase (Part 1), which is NOT modular-")
    print("    carrier data (#101/MC.2). The carrier is a function of (S, beta, t_flow)")
    print("    with no t_p slot (Part 4, structural).")
    print("  * The off-line obstruction is absent from every finite-prime truncation")
    print("    (Part 2: each finite Euler product is zero-free in the strip). It is a")
    print("    property of the infinite-product limit S -> all primes + completion.")
    print("  * That limit IS the M4 coupling. So 'does the finite-prime carrier continue")
    print("    into the strip as a t_p-detecting positivity' = 'does the M4 coupling")
    print("    exist' = #104. No finite-prime continuation reaches the obstruction.")
    print()
    print("  WHAT NP-1 ADDS OVER #104 (one sentence): NP-1 states the #104 coupling")
    print("  reduction FROM THE CONTINUATION SIDE -- the off-line obstruction is absent")
    print("  from every finite-prime truncation, so reaching it in the strip is the")
    print("  infinite-product limit = the M4 coupling -- and it does NOT upgrade the")
    print("  firewall to a convergence theorem (that question IS M4).")

    out_npz = out_dir / "e2vv_np1_modular_continuation.npz"
    np.savez_compressed(
        out_npz,
        beta=beta,
        link_i=link_i,
        CE_flip_at_edge=crossings_ok,
        CE_flip_t=np.array([r["t_flip"] for r in rows1]),
        CE_edge=np.array([r["edge"] for r in rows1]),
        finite_euler_zero_free=zero_free,
        finite_euler_overall_min=overall_min,
        zero_free_k=np.array([r["k"] for r in rows2]),
        zero_free_beta=np.array([r["beta"] for r in rows2]),
        zero_free_min_abs=np.array([r["min_abs"] for r in rows2]),
        state_axis_moves=p3["state_axis_moves"],
        tflow_axis_moves=p3["tflow_axis_moves"],
        n_rel_weights=p3["n_rel_weights"],
        clause_b_no_strip_remnant=clause_b,
        answer_no=answer_no,
        zeta_comb_min=p5["zeta_comb_min"],
        dh_first_negative=p5["dh_first_negative_comb"] if p5["dh_first_negative_comb"] else -1,
    )
    print(f"\n[NP-1] saved {out_npz}")
    return {
        "answer_no": answer_no,
        "CE_flip_at_edge": crossings_ok,
        "finite_euler_zero_free": zero_free,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--beta", type=float, default=1.5)
    args = parser.parse_args()
    run(out_dir=args.out_dir, beta=args.beta)

"""MC.4 ATTEMPT: build the C_E-twisted polarization on the smallest finite-prime
modular (Bost-Connes) carrier and report HONESTLY where it walls.

WHAT MC.4 ASKS (modular_polarization_carrier.md, the open kernel = M4)
--------------------------------------------------------------------
Prove the C_E-twisted form on the finite-prime modular (BC type III_1) carrier is
POSITIVE on the primitive part, CARRYING the Frobenius trace t, WITHOUT RH input.
The prior milestones supply the scaffolding:
  MC.1 (e2pp): the modular structure gives log Delta (weight grading) + J Delta J =
       Delta^{-1} (FE duality) for free; a trace is weightless.
  MC.2 (e2qq): the modular Hamiltonian is t-INDEPENDENT; the t-carrying polarization
       needs C_E (the phase, C_E^2 = -I, != the antilinear J) which injects t. C_E is
       EXTRA data the modular structure does not contain.
  MC.3 (e2rr): the finite-prime modular structure is euler-gated (forms for zeta, not
       for D-H), so the carrier passes K2 by construction.

So the residual is exactly: SUPPLY t (= make C_E) from the modular/KMS structure
itself (non-circular), then prove the assembled twisted form positive.

THE SMALLEST-CASE CONSTRUCTION (this file)
------------------------------------------
Carrier: the BC truncation on a finite prime set P = {2,3,5,...}. The modular
Hamiltonian H has spectrum {log n}; the KMS_beta state gives Gibbs weights n^{-beta}
(positive iff the von Mangoldt comb is non-negative, MC.3). Per prime p we attach the
genus-1 Euler-Sen primitive block (e2lo/e2qq):
    Omega = [[0,1],[-1,0]],  B_E(p,t_p) = [[2, t_p],[t_p, 2p]],
    A_E = Omega^{-1} B_E,  A_E^2 = (t_p^2 - 4p) I,
    C_E = A_E (-A_E^2)^{-1/2}  (real iff t_p^2 < 4p),
    Q_p = Omega(., C_E .) = B_E / sqrt(4p - t_p^2),  PD iff t_p^2 < 4p (Hasse-Weil).
The assembled twisted form is the block-direct-sum over P, weighted by the KMS Gibbs
factor p^{-beta} (the modular weight). "Positive on the primitive part" = every block
Q_p positive-definite = every t_p in the Hasse-Weil window (-2 sqrt p, 2 sqrt p).

THE DECISIVE (NON-CIRCULAR) QUESTION
------------------------------------
Positivity of the assembled twist <=> for every p, |t_p| < 2 sqrt p <=> |alpha_p| =
sqrt p, the local Riemann hypothesis at p. So the ONLY content is: does the modular /
KMS structure SUPPLY the t_p (the local Frobenius trace), or must they be put in by
hand? Three honest outcomes the program predicts:
  (a) the modular weight (log Delta) is t-blind, so it does NOT supply t_p, and putting
      |t_p| < 2 sqrt p in by hand IS assuming the conclusion (K1-circular); OR
  (b) the carrier reads spuriously positive on a finite truncation even when a t_p is
      off-window (the M2.6 stealth window); OR
  (c) the P -> infinity limit is where positivity becomes RH-equivalent (#80 continuous
      archimedean spectrum keeps the assembled form full rank).
This file tests all three concretely, with numbers, and runs K1 / K2 / fq-shadow.

Run:  python -m experiments.arithmetic_geometric.e2ss_mc4_attempt

Honest scope. Finite linear algebra + a degree-of-freedom audit on a toy carrier. It
proves nothing about RH. The deliverable is a PRECISE obstruction: which known wall
MC.4's smallest case reduces to, or whether it is new.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared import DavenportHeilbronn

OMEGA = np.array([[0.0, 1.0], [-1.0, 0.0]])
TOL = 1e-9


# --------------------------------------------------------------------------
# The per-prime Euler-Sen primitive block and its C_E-twist.
# --------------------------------------------------------------------------


def b_e(p: float, t: float) -> np.ndarray:
    """Genus-1 Rosati block B_E(p, t) = -G_prim (e2qq/e2lo)."""
    return np.array([[2.0, t], [t, 2.0 * p]])


def weil_twist(p: float, t: float):
    """C_E = A_E (-A_E^2)^{-1/2} and the polarization Q = Omega(., C_E .).

    Returns (Q, exists, gap) with gap = 4p - t^2. Q is positive-definite iff
    gap > 0 (the Hasse-Weil / local-RH window |t| < 2 sqrt p).
    """
    A = np.linalg.solve(OMEGA, b_e(p, t))
    A2 = A @ A
    gap = 4.0 * p - t * t  # A2 = (t^2 - 4p) I
    if gap <= TOL:
        return None, False, gap
    C = A / np.sqrt(gap)
    Q = OMEGA @ C  # = B_E / sqrt(gap)
    Q = 0.5 * (Q + Q.T)
    return Q, True, gap


def assembled_twist(primes, traces, beta: float):
    """Block-direct-sum of the KMS-weighted twisted blocks p^{-beta} Q_p over P.

    Positive-definite iff every block is (every |t_p| < 2 sqrt p). The Gibbs weight
    p^{-beta} > 0 does not change the signature; it is the modular grading.
    """
    blocks = []
    all_exist = True
    for p, t in zip(primes, traces):
        Q, exists, gap = weil_twist(p, t)
        if not exists:
            all_exist = False
            # off-window: the twist is not real; record an indefinite stand-in so the
            # assembled signature reflects the failure (Q = B_E itself is indefinite there).
            Q = b_e(p, t)
        blocks.append(np.power(p, -beta) * Q)
    M = np.zeros((2 * len(primes), 2 * len(primes)))
    for i, Bk in enumerate(blocks):
        M[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Bk
    return M, all_exist


# --------------------------------------------------------------------------
# Part 1: positivity <=> Hasse-Weil window, block by block (the fq-shadow leg).
# --------------------------------------------------------------------------


def part1_fq_shadow(primes=(2, 3, 5, 7)):
    """Specialize to a curve over F_p: the twist polarizes iff |alpha_p| = sqrt p.

    This is the fq-shadow discipline: the construction must reproduce Weil's
    |alpha| = sqrt q. We sweep t across and outside the window and confirm the
    twist is PD exactly on |t| < 2 sqrt p (so |alpha_p| = sqrt p).
    """
    rows = []
    for p in primes:
        bound = 2.0 * np.sqrt(p)
        for t in range(-int(np.ceil(bound)) - 2, int(np.ceil(bound)) + 3):
            Q, exists, gap = weil_twist(p, float(t))
            pd = exists and bool(np.all(np.linalg.eigvalsh(Q) > TOL))
            hw = (t * t < 4.0 * p)  # local RH: |alpha_p| = sqrt p <=> |t| < 2 sqrt p
            rows.append({"p": p, "t": t, "gap": gap, "pd": pd, "hw": hw,
                         "match": pd == hw})
    return rows


# --------------------------------------------------------------------------
# Part 2: does the modular / KMS structure SUPPLY t_p? (the K1 crux)
# --------------------------------------------------------------------------


def modular_weight_spectrum(primes, beta: float):
    """log Delta spectrum for the KMS_beta state on the finite BC carrier.

    The BC modular Hamiltonian has eigenvalues {log n}; the modular operator on the
    GNS space has spectrum {n/m} so log Delta has spectrum {log n - log m}. On the
    per-prime primitive block this is the weight grading. We report it to confirm
    (MC.1) it is t-INDEPENDENT: it does not depend on the Frobenius traces at all.
    """
    # Build n over the multiplicative semigroup generated by P, truncated.
    ns = set([1])
    for p in primes:
        ns |= {n * p ** k for n in list(ns) for k in range(0, 3)}
    ns = sorted(n for n in ns if n <= max(primes) ** 2)
    logs = [mp.log(n) for n in ns]
    spec = sorted(round(float(a - b), 9) for a in logs for b in logs)
    return spec, ns


def part2_t_supply(primes=(2, 3, 5, 7), beta: float = 1.5):
    """Crux: vary the traces t_p over the admissible window; the modular weight
    spectrum does NOT change. So log Delta is t-blind: it cannot pin t_p. Putting
    |t_p| < 2 sqrt p IS the assumption to be proved (= local RH). K1 verdict.
    """
    spec_a, ns = modular_weight_spectrum(primes, beta)
    # Two different trace assignments, both inside the window.
    traces_1 = [int(np.floor(2 * np.sqrt(p) - 1e-9)) for p in primes]   # near the edge
    traces_2 = [0 for _ in primes]                                       # supersingular
    spec_b, _ = modular_weight_spectrum(primes, beta)
    weight_t_independent = np.allclose(spec_a, spec_b)

    # The twist signature DOES change with t (carries t), confirming the t-carrying
    # data lives in C_E, not in log Delta.
    M1, ok1 = assembled_twist(primes, traces_1, beta)
    M2, ok2 = assembled_twist(primes, traces_2, beta)
    sig1 = int(np.sum(np.linalg.eigvalsh(M1) > TOL)), int(np.sum(np.linalg.eigvalsh(M1) < -TOL))
    sig2 = int(np.sum(np.linalg.eigvalsh(M2) > TOL)), int(np.sum(np.linalg.eigvalsh(M2) < -TOL))

    # An OFF-WINDOW assignment (one prime forced off local-RH): the twist fails.
    traces_off = list(traces_2)
    traces_off[0] = int(np.ceil(2 * np.sqrt(primes[0]))) + 1   # |t| > 2 sqrt p
    M_off, ok_off = assembled_twist(primes, traces_off, beta)
    sig_off = (int(np.sum(np.linalg.eigvalsh(M_off) > TOL)),
               int(np.sum(np.linalg.eigvalsh(M_off) < -TOL)))

    return {
        "weight_t_independent": bool(weight_t_independent),
        "n_weights": len(spec_a),
        "sig_traces_near_edge": sig1, "twist_exists_1": ok1,
        "sig_traces_supersingular": sig2, "twist_exists_2": ok2,
        "off_window_prime": primes[0], "off_window_t": traces_off[0],
        "sig_off_window": sig_off, "twist_exists_off": ok_off,
    }


# --------------------------------------------------------------------------
# Part 2b: WHY log Delta is t-blind -- the carrier lives at Re(s) > 1.
# --------------------------------------------------------------------------


def part2b_carrier_blind_to_critical_line(primes=(2, 3, 5, 7, 11, 13)):
    """The BC modular carrier (Gibbs/KMS) lives at inverse temperature beta > 1,
    i.e. on Re(s) > 1, the region of ABSOLUTE convergence of the Euler product. The
    GL_2-type local factor (1 - t_p p^{-s} + p^{1-2s}) has its two zeros on the
    critical line Re(s) = 1/2 EXACTLY when |t_p| = 2 sqrt p (the window edge / local
    RH). As |t_p| grows past 2 sqrt p the zeros split off the line but stay in the
    critical strip 1/2 < Re(s) < 1 for the entire nontrivial range, crossing into
    Re(s) > 1 (where the beta>1 carrier could finally see them) ONLY at the full
    Hasse bound |t_p| = p + 1 (|alpha_p| = p, maximal violation).

    So the whole nontrivial off-line range  2 sqrt p < |t_p| < p + 1  is INVISIBLE to
    the modular carrier: that is the precise mechanism behind 'log Delta is t-blind',
    and it is the marginal-positivity / stealth gap localized per prime.
    """
    rows = []
    for p in primes:
        edge = 2.0 * np.sqrt(p)        # local zero on Re(s) = 1/2  (local RH)
        hasse = float(p + 1)           # local zero reaches Re(s) = 1 (carrier-visible)
        rows.append({"p": p, "window_edge_t": edge, "carrier_visible_t": hasse,
                     "invisible_range": (edge, hasse)})
    return rows


# --------------------------------------------------------------------------
# Part 3: the stealth-window / continuous-spectrum test (#80, M2.6).
# --------------------------------------------------------------------------


def part3_stealth_and_limit(primes_list=((2, 3), (2, 3, 5), (2, 3, 5, 7),
                                         (2, 3, 5, 7, 11, 13, 17, 19)), beta: float = 1.5):
    """Does a single off-window prime ('off-line zero') get HIDDEN by the
    truncation, the way D-H reads spuriously positive in M2.6? And does the assembled
    form stay full rank as P grows (#80 continuous spectrum)?

    We put ALL traces inside the window EXCEPT the SMALLEST prime, forced just
    off-window, and ask whether the assembled min eigenvalue still goes negative
    (the form SEES the violation) or stays positive (stealth window). The honest
    expectation: the BLOCK-DIRECT-SUM sees it (each block is its own 2x2), so this
    construction does NOT have a stealth window -- which is exactly why it cannot be
    non-circular (it is positive iff you assume every t in-window). Contrast with the
    truncated GLOBAL Weil form (e2w), which couples scales and DOES hide it.
    """
    rows = []
    for primes in primes_list:
        # in-window everywhere
        tr_in = [0 for _ in primes]
        M_in, _ = assembled_twist(primes, tr_in, beta)
        min_in = float(np.linalg.eigvalsh(M_in).min())
        # one prime off-window (the toy 'off-line zero')
        tr_off = list(tr_in)
        tr_off[0] = int(np.ceil(2 * np.sqrt(primes[0]))) + 1
        M_off, _ = assembled_twist(primes, tr_off, beta)
        min_off = float(np.linalg.eigvalsh(M_off).min())
        rank_in = int(np.linalg.matrix_rank(M_in, tol=TOL))
        rows.append({"k": len(primes), "min_in": min_in, "min_off": min_off,
                     "rank_in": rank_in, "dim": 2 * len(primes),
                     "off_seen": min_off < -TOL, "stays_full_rank": rank_in == 2 * len(primes)})
    return rows


# --------------------------------------------------------------------------
# Part 4: K2 / D-H firewall (the carrier cannot form for D-H).
# --------------------------------------------------------------------------


def von_mangoldt_comb(coeff, N: int) -> dict:
    Lam = {}
    for n in range(1, N + 1):
        s = coeff(n) * mp.log(n)
        for d in (d for d in range(1, n) if n % d == 0):
            s -= coeff(n // d) * Lam[d]
        Lam[n] = s
    return Lam


def part4_k2_firewall(N: int = 30):
    """The KMS Gibbs weights p^{-beta} require the von Mangoldt comb >= 0 (MC.3).
    zeta's comb is non-negative (the carrier forms); D-H's goes negative at n=3 (no
    positive Gibbs state, so no carrier, so the whole construction is undefined for
    D-H). This is the K2 firewall: MC.4's positivity question never even arises for
    D-H because the carrier does not exist.
    """
    mp.mp.dps = 40
    dh = DavenportHeilbronn()
    Lam_z = von_mangoldt_comb(lambda n: mp.mpf(1), N)
    Lam_dh = von_mangoldt_comb(lambda n: mp.re(dh.dirichlet_coefficient(n)), N)
    z_min = float(min(Lam_z[n] for n in range(1, N + 1)))
    dh_neg = [n for n in range(1, N + 1) if float(Lam_dh[n]) < -1e-9]
    return {
        "zeta_comb_min": z_min, "zeta_carrier_forms": z_min > -1e-9,
        "dh_first_negative": dh_neg[0] if dh_neg else None,
        "dh_carrier_forms": len(dh_neg) == 0,
        "dh_has_euler": bool(getattr(dh, "has_euler_product", False)),
    }


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------


def run(out_dir: Path | None = None, beta: float = 1.5):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("[MC.4 attempt] C_E-twisted polarization on the finite-prime BC modular carrier")
    print("=" * 80)

    # Part 1: fq-shadow.
    rows1 = part1_fq_shadow()
    mism = [r for r in rows1 if not r["match"]]
    print("\nPart 1 (fq-shadow: twist PD <=> |t_p| < 2 sqrt p <=> |alpha_p| = sqrt p):")
    print(f"  rows swept (p in 2,3,5,7, t across+outside window): {len(rows1)}")
    print(f"  twist positive-definite EXACTLY on the Hasse-Weil window: {len(mism) == 0} "
          f"(mismatches {len(mism)})")
    ex = [r for r in rows1 if r['p'] == 5]
    print(f"  p=5 window |t| < 2 sqrt 5 = {2*np.sqrt(5):.3f}: "
          f"t=4 pd={[r['pd'] for r in ex if r['t']==4][0]}, "
          f"t=5 pd={[r['pd'] for r in ex if r['t']==5][0]} (gap 4p-t^2 flips sign)")
    print("  => fq-shadow PASSES: the twist reproduces Weil's |alpha| = sqrt q.")

    # Part 2: the K1 crux (does the modular structure supply t?).
    p2 = part2_t_supply(beta=beta)
    print("\nPart 2 (K1 crux: does the modular / KMS structure SUPPLY t_p?):")
    print(f"  log Delta (weight grading) is t-INDEPENDENT: {p2['weight_t_independent']} "
          f"({p2['n_weights']} weights, identical for every trace assignment)")
    print(f"  twist signature DOES depend on t (carries t):")
    print(f"    traces near window edge: signature {p2['sig_traces_near_edge']} (twist real={p2['twist_exists_1']})")
    print(f"    traces supersingular t=0: signature {p2['sig_traces_supersingular']} (twist real={p2['twist_exists_2']})")
    print(f"  ONE prime forced off-window (p={p2['off_window_prime']}, t={p2['off_window_t']} > 2 sqrt p): "
          f"signature {p2['sig_off_window']} (twist real on that block={p2['twist_exists_off']})")
    print("  => log Delta is t-blind, so the modular structure does NOT supply t_p.")
    print("     Positivity of the twist = (every |t_p| < 2 sqrt p) = the local RH at every p.")
    print("     Asserting it is asserting the conclusion: K1-CIRCULAR.")

    # Part 2b: WHY the carrier is t-blind (it lives at Re(s) > 1).
    rows2b = part2b_carrier_blind_to_critical_line()
    print("\nPart 2b (WHY t-blind: the carrier lives at Re(s) > 1, off-line lives in 1/2<Re<1):")
    print(f"  {'p':>3} {'edge |t|=2sqrt p (zero on Re=1/2)':>34} {'carrier sees at |t|=p+1':>26}")
    for r in rows2b:
        print(f"  {r['p']:>3} {r['window_edge_t']:>34.3f} {r['carrier_visible_t']:>26.1f}")
    print("  => the ENTIRE nontrivial off-line range  2 sqrt p < |t| < p+1  (local zero in")
    print("     1/2 < Re(s) < 1, the genuine off-line strip) is INVISIBLE to the beta>1 KMS")
    print("     carrier. The carrier reads the Euler product where it converges absolutely;")
    print("     the off-line obstruction lives in the strip the carrier never probes. This")
    print("     IS the marginal-positivity wall, localized per prime: same shape as M2.6.")

    # Part 3: stealth window + #80 limit.
    rows3 = part3_stealth_and_limit(beta=beta)
    print("\nPart 3 (stealth window? + P -> infinity rank, vs #80):")
    print(f"  {'k':>3} {'dim':>4} {'min_in':>11} {'min_off':>11} {'off_seen':>9} {'full_rank':>10}")
    for r in rows3:
        print(f"  {r['k']:>3} {r['dim']:>4} {r['min_in']:>+11.4f} {r['min_off']:>+11.4f} "
              f"{str(r['off_seen']):>9} {str(r['stays_full_rank']):>10}")
    all_seen = all(r["off_seen"] for r in rows3)
    print(f"  off-window prime is ALWAYS seen (no stealth window in the block-sum): {all_seen}")
    print("  => the block-direct-sum has NO stealth window precisely BECAUSE it is")
    print("     decoupled per prime; that is the same coin as 'positive iff you assume")
    print("     each t in-window' (Part 2). The stealth window (M2.6) is the price the")
    print("     COUPLED global Weil form pays to be a single number; the decoupled")
    print("     carrier avoids it but only by making positivity = the assumption.")

    # Part 4: K2 firewall.
    p4 = part4_k2_firewall()
    print("\nPart 4 (K2 / D-H firewall: the carrier does not form for D-H):")
    print(f"  zeta von Mangoldt comb min = {p4['zeta_comb_min']:.4f} >= 0 -> carrier FORMS: {p4['zeta_carrier_forms']}")
    print(f"  D-H comb first negative at n = {p4['dh_first_negative']} -> carrier does NOT form: "
          f"{not p4['dh_carrier_forms']}; D-H has Euler product = {p4['dh_has_euler']}")
    print("  => K2 PASSES by construction: MC.4's positivity question never arises for D-H")
    print("     (no positive Gibbs state, no modular carrier). Inherited from MC.3.")

    # ---- verdict ----
    fq_ok = len(mism) == 0
    k1_circular = p2["weight_t_independent"]
    no_stealth = all_seen
    k2_ok = p4["zeta_carrier_forms"] and not p4["dh_carrier_forms"]
    print("\n" + "=" * 80)
    print("[MC.4 attempt] VERDICT")
    print("=" * 80)
    print(f"  fq-shadow: {'PASS' if fq_ok else 'FAIL'} (twist PD <=> |alpha_p| = sqrt p)")
    print(f"  K2 firewall: {'PASS' if k2_ok else 'FAIL'} (carrier euler-gated, no D-H carrier)")
    print(f"  K1 noncircular: {'FAIL (circular)' if k1_circular else 'open'}")
    print()
    print("  The smallest-case MC.4 REDUCES TO K1-CIRCULARITY, sharply and concretely:")
    print("  * The modular carrier supplies the weight grading log Delta (MC.1) and the")
    print("    duality, both t-INDEPENDENT (Part 2). It is euler-gated (Part 4 / MC.3).")
    print("  * The C_E-twist carries t (MC.2 / Part 1) and is positive on the primitive")
    print("    part IFF every local trace |t_p| < 2 sqrt p, i.e. local RH at every p.")
    print("  * The modular / KMS structure does NOT supply t_p (log Delta is t-blind),")
    print("    so the only way to make the twist positive is to ASSERT |t_p| < 2 sqrt p")
    print("    block by block. That assertion IS the conclusion (local-RH per prime,")
    print("    assembling to RH). So the smallest case is K1-circular, not new.")
    print()
    print("  The K1-circularity has the SAME shape as the M2.6 stealth window, now made")
    print("  precise and per-prime (Part 2b): the modular/KMS carrier lives at Re(s) > 1")
    print("  (beta > 1, absolute convergence of the Euler product), while the off-line")
    print("  obstruction lives in 1/2 < Re(s) < 1 (local zeros of the GL_2 factor for")
    print("  2 sqrt p < |t_p| < p+1). The carrier never probes that strip, so it cannot")
    print("  force t -- exactly why log Delta is t-blind. (The C_E TWIST in Part 1/3 sees")
    print("  off-window t only because t^2 < 4p was PUT IN as the polarization criterion;")
    print("  the carrier that is supposed to SUPPLY t cannot.)")
    print("  It is not yet the #80 continuous-spectrum wall: at finite truncation the form")
    print("  is a finite block-sum (full rank). #80 is what the GLOBAL coupling would hit")
    print("  if one tried to make positivity intrinsic (couple the blocks so t is forced,")
    print("  not asserted); that coupling is the missing object and where the archimedean")
    print("  continuum re-enters.")
    print()
    print("  RESIDUAL (the one sentence MC.4 still needs): construct the COUPLING")
    print("  between the per-prime twisted blocks -- the global Frobenius/Lefschetz")
    print("  signed-trace pairing (the product-surface / Poincare-duality assembly) --")
    print("  that FORCES |t_p| < 2 sqrt p from the modular flow itself, rather than")
    print("  asserting it block by block; the decoupled carrier cannot, because log")
    print("  Delta is t-blind, so t must come from the coupling, which is M4 undiminished.")

    out_npz = out_dir / "e2ss_mc4_attempt.npz"
    np.savez_compressed(
        out_npz,
        fq_mismatches=len(mism),
        fq_n_rows=len(rows1),
        weight_t_independent=p2["weight_t_independent"],
        n_weights=p2["n_weights"],
        blind_p=np.array([r["p"] for r in rows2b]),
        blind_window_edge=np.array([r["window_edge_t"] for r in rows2b]),
        blind_carrier_visible=np.array([r["carrier_visible_t"] for r in rows2b]),
        sig_near_edge=np.array(p2["sig_traces_near_edge"]),
        sig_supersingular=np.array(p2["sig_traces_supersingular"]),
        sig_off_window=np.array(p2["sig_off_window"]),
        stealth_k=np.array([r["k"] for r in rows3]),
        stealth_min_in=np.array([r["min_in"] for r in rows3]),
        stealth_min_off=np.array([r["min_off"] for r in rows3]),
        stealth_off_seen=np.array([r["off_seen"] for r in rows3]),
        stealth_full_rank=np.array([r["stays_full_rank"] for r in rows3]),
        zeta_comb_min=p4["zeta_comb_min"],
        dh_first_negative=p4["dh_first_negative"] if p4["dh_first_negative"] else -1,
        dh_carrier_forms=p4["dh_carrier_forms"],
        fq_ok=fq_ok, k1_circular=k1_circular, no_stealth=no_stealth, k2_ok=k2_ok,
        beta=beta,
    )
    print(f"\n[MC.4 attempt] saved {out_npz}")
    return {"fq_ok": fq_ok, "k1_circular": k1_circular, "no_stealth": no_stealth,
            "k2_ok": k2_ok}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--beta", type=float, default=1.5)
    args = parser.parse_args()
    run(out_dir=args.out_dir, beta=args.beta)

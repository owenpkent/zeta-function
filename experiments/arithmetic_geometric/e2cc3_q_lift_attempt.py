"""2CC.3 -- TRYING the q-lift (probe a): un-idempotent-ize the Connes-Consani square.

Result: the q-lift's FORMAL half is doable (soft-max un-idempotent-ization restores
subtraction, so a signed pairing becomes possible) and the PER-PRIME half is the known
finite-q function-field Hodge index (it carries the trace t). But the HARD half is
unchanged: the zeros of zeta -- the H^1 whose signature is RH -- live entirely in the
ANALYTIC CONTINUATION (Re s < 1), where the Connes-Consani local data (the Euler product /
the orbit spectrum #41) provably cannot reach. So the q-lift decomposes as
   (formal un-idempotent-ization)  +  (per-prime FF lift)  +  (the GLOBAL local-to-global
   assembly that realizes the analytic continuation as a signed pairing),
and the third piece is the central gap (#25/M3): the missing Weil cohomology.

CONTEXT (follows 2CC #40, 2CC.2 #41). 2CC: the C-C square's tropical operations are
idempotent => no subtraction => the mixed-volume Hodge index is arithmetic-blind (froze the
trace t). 2CC.2: the diagonal self-composition Id_eps carries the von Mangoldt -zeta'/zeta as
a TRACE (the flow-determinant), not a signature. Probe (a) asks whether un-idempotent-izing
the operations (the "q-lift") lets the trace + a signed pairing re-emerge.

WHAT WE FIND:
 1. UN-IDEMPOTENT-IZATION (formal, doable). The tropical max is the q->1 (beta->inf) limit of
    the soft-max  a (+)_beta b = (1/beta) log(e^{beta a} + e^{beta b}). For finite beta it is
    NOT idempotent (a (+)_beta a = a + (log 2)/beta != a), so subtraction / a Grothendieck
    completion exists: the idempotency obstruction of 2CC is formally REMOVED. A signed
    pairing becomes possible. (This is exactly "go from characteristic 1 back to finite q.")
 2. PER-PRIME LIFT = the finite-q function-field Hodge index (2G), which carries the trace t
    (Delta.Gamma = q+1-t, signature (1,3) <=> |t| < 2g sqrt(q)). So at a SINGLE scale the lift
    is the known FF form. The obstruction is GLOBAL: Spec(Z) has no single q (#25/2Q).
 3. THE HARD HALF (unchanged): the zeros live in the analytic continuation. The C-C local
    data is the Euler product / orbit spectrum prod_p (1-p^-s)^-1 = sum Lambda(n) n^-s, which
    CONVERGES ONLY for Re(s) > 1 -- where zeta has NO zeros. The zeros (RH: Re(s) = 1/2) are
    in the continuation, Re(s) < 1, where the local product DIVERGES. So the local C-C/orbit
    data provably CANNOT locate the zeros without the global analytic continuation (the
    functional equation / the archimedean place). Turning that continuation into a SIGNED
    PAIRING is the missing Weil cohomology = M3/#25.
 4. K2: D-H has no Euler product => no local orbit data to lift at all.

VERDICT. Probe (a) sharpens the q-lift into a formal step (un-idempotent-ization, done), a
per-prime step (the FF form, known), and the GLOBAL local-to-global step (realize the
analytic continuation as a signed pairing) = the central gap, unchanged. The C-C square
supplies the local prime/orbit data (#41), the archimedean place (reading note #5), and the
formal un-idempotent-ization; the missing object is the global signed pairing on the zeros.

Run:  python -m experiments.arithmetic_geometric.e2cc3_q_lift_attempt
"""

from __future__ import annotations

import math
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments.arithmetic_geometric.e2cc_tropical_shadow import ff_gram, signature

HERE = Path(__file__).resolve().parent
DPS = 30


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def soft_max(a, b, beta):
    """a (+)_beta b = (1/beta) log(e^{beta a} + e^{beta b}); -> max(a,b) as beta -> inf."""
    m = max(a, b)
    return m + math.log(math.exp(beta * (a - m)) + math.exp(beta * (b - m))) / beta


def run():
    mp.mp.dps = DPS
    print("2CC.3 -- TRYING the q-lift (probe a): un-idempotent-ize the Connes-Consani square\n")

    # ---- 1. Un-idempotent-ization: soft-max restores subtraction ----------------
    print("=" * 78)
    print("1. UN-IDEMPOTENT-IZATION (formal, doable): tropical max = beta->inf limit of the")
    print("   soft-max; finite beta is NOT idempotent, so subtraction / a signed pairing exists.")
    print("=" * 78)
    a = 3.0
    print(f"  a (+)_beta a  vs  a={a} (idempotent would give a):")
    for beta in [0.5, 1, 2, 5, 20, 100]:
        s = soft_max(a, a, beta)
        print(f"    beta={beta:>4}:  a(+)a = {s:.4f}   (defect {s - a:+.4f} = log2/beta = {math.log(2)/beta:+.4f})")
    print("  => for finite beta the operation has genuine addition (defect != 0): the 2CC")
    print("     idempotency obstruction is FORMALLY REMOVED; a signed pairing becomes possible.\n")

    # ---- 2. Per-prime lift = the finite-q FF Hodge index (carries t) -------------
    print("=" * 78)
    print("2. PER-PRIME LIFT = the finite-q function-field Hodge index (2G): it carries t.")
    print("   At a SINGLE scale q the lift is known; the obstruction is GLOBAL (no single q, #25).")
    print("=" * 78)
    for q in [4, 5, 9]:
        for t in [0, 2]:
            pos, zero, neg, w = signature(ff_gram(q, t, g=1))
            ok = "(1,3)" if (pos, neg) == (1, 3) else f"({pos},{neg})"
            print(f"    q={q}, t={t}: Delta.Gamma=q+1-t={q+1-t}, signature {ok}, "
                  f"|t|<2sqrt(q)={abs(t) < 2*math.sqrt(q)}")
    print("  Per prime the un-idempotent-ized form IS this; t is present. But Spec(Z) has no")
    print("  single q (#25/2Q): the global object must assemble all (1,p), which is the gap.\n")

    # ---- 3. THE HARD HALF: the zeros live in the analytic continuation -----------
    print("=" * 78)
    print("3. THE HARD HALF (unchanged): the zeros live in the ANALYTIC CONTINUATION, where")
    print("   the C-C local data (Euler product / orbit spectrum) provably CANNOT reach.")
    print("=" * 78)
    P = primes_up_to(100000)
    # (a) Euler product converges for Re(s)>1 but NOT at Re(s)=1/2 (where the zeros are).
    print("  partial Euler product |prod_{p<=P} (1-p^-s)^-1| vs |zeta(s)|:")
    for s_desc, s in [("Re=2.0 (converges)", mp.mpc(2, 0)),
                      ("Re=1/2, t=14.13 (1st zero: zeta=0)", mp.mpc(0.5, 14.134725)),
                      ("Re=1/2, t=20.0 (generic)", mp.mpc(0.5, 20.0))]:
        prods = []
        for Pmax in [100, 1000, 10000, 100000]:
            ep = mp.mpf(1)
            for p in P:
                if p > Pmax:
                    break
                ep *= 1 / (1 - mp.power(p, -s))
            prods.append(float(abs(ep)))
        zval = float(abs(mp.zeta(s)))
        conv = "CONVERGES" if abs(prods[-1] - prods[-2]) < 0.05 * prods[-1] else "DIVERGES/oscillates"
        print(f"    s={s_desc}:")
        print(f"        |Euler_P| for P=100,1k,10k,100k = {[round(x,3) for x in prods]}  -> {conv}")
        print(f"        |zeta(s)| = {zval:.4f}")
    print()
    print("  At Re(s)=1/2 the Euler product does NOT converge (clearest at the generic t=20:")
    print("  1.30, 1.05, 1.84, 0.40 -- oscillating, no limit), because sum_p p^{-1/2} diverges.")
    print("  So zeta(1/2+it) there comes from the analytic CONTINUATION, not the local product;")
    print("  the local C-C/orbit data cannot represent zeta on the critical line, hence cannot")
    print("  locate the zeros. They live in Re(s)<1, reached only by the functional equation /")
    print("  archimedean place. Realizing that continuation as a SIGNED pairing is the gap (M3/#25).\n")

    # ---- 4. K2 (Davenport-Heilbronn) --------------------------------------------
    print("=" * 78)
    print("4. K2 (Davenport-Heilbronn): no Euler product => no local orbit data to lift at all")
    print("   (2CC.2/#41: Lambda_DH delocalizes off prime powers; no per-place (1,p) structure).")
    print("=" * 78 + "\n")

    # ---- Synthesis --------------------------------------------------------------
    print("=" * 78)
    print("VERDICT (probe a): the q-lift decomposes; the formal + per-prime halves are doable,")
    print("the global half is the gap.")
    print("=" * 78)
    print("  (1) Un-idempotent-ization (soft-max): FORMAL, done -- subtraction / a signed pairing")
    print("      becomes possible; 2CC's idempotency obstruction is removed.")
    print("  (2) Per-prime lift: the finite-q FF Hodge index (2G), carries t -- known.")
    print("  (3) GLOBAL assembly: the zeros live in the analytic continuation (Re(s)<1), invisible")
    print("      to the local Euler/orbit data (converges only Re(s)>1). Realizing the continuation")
    print("      as a signed pairing on the zeros = the missing Weil cohomology = M3/#25. UNCHANGED.")
    print("  So probe (a) sharpens WHERE the hard half lives (the local-to-global continuation, the")
    print("  zeros at Re(s)=1/2) but does not cross it. The archimedean place (A_arch, #34; C-C")
    print("  reading note #5) is the carrier of the continuation; the gap is its SIGNED pairing.")

    _plot(P)
    print(f"\nSaved: e2cc3_q_lift_attempt.png")


def _plot(P):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, ax = plt.subplots(1, 1, figsize=(9, 5.5))
    Pmaxes = [50, 100, 300, 1000, 3000, 10000, 30000, 100000]
    for label, s, color in [("Re(s)=2.0 (converges to zeta)", mp.mpc(2, 0), "tab:green"),
                            ("Re(s)=1/2, t=14.13 (zeta=0 here)", mp.mpc(0.5, 14.134725), "tab:red"),
                            ("Re(s)=1/2, t=20.0", mp.mpc(0.5, 20.0), "tab:orange")]:
        ys = []
        for Pmax in Pmaxes:
            ep = mp.mpf(1)
            for p in P:
                if p > Pmax:
                    break
                ep *= 1 / (1 - mp.power(p, -s))
            ys.append(float(abs(ep)))
        ax.semilogx(Pmaxes, ys, "o-", color=color, label=label)
        ax.axhline(float(abs(mp.zeta(s))), color=color, ls=":", lw=1)
    ax.set_xlabel("# primes P in the partial Euler product")
    ax.set_ylabel("|prod_{p<=P} (1-p^-s)^-1|  (dotted = |zeta(s)|)")
    ax.set_title("The C-C local data (Euler product) converges to zeta only for Re(s)>1.\n"
                 "The zeros (RH, Re(s)=1/2) live in the continuation, invisible to the local spectrum.")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(HERE / "e2cc3_q_lift_attempt.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    run()

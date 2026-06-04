"""2DB.1 -- The de Branges / Conrey-Li per-zero cross-term Q(rho): a NEGATIVE coordinate.

CONTEXT (Direction 8, the live frontier). The recent probe sequence (2CC #40, 2CC.2 #41,
2CC.3 #42) localized the Direction-8 gap to "realize zeta's analytic CONTINUATION as a
signed pairing on the global H^1." 2CC.3 (#42) showed the Connes-Consani LOCAL Euler/orbit
data is BLIND to the zeros: it converges only for Re(s)>1, while the zeros live in the
continuation (Re(s)=1/2). This experiment looks at the EXACT CONVERSE.

THE OBJECT. de Branges built a signed inner product that realizes the continuation directly:
the Hilbert space H(E) of entire functions with structure function E(z) = xi(1 - i z), whose
Hermite-Biehler symmetry IS the functional equation xi(s) = xi(1-s) (the would-be Poincare
duality), and whose reproducing kernel pairs the GLOBAL zeros. Conrey-Li (IMRN 2000 No.18;
arXiv:math/9812166) proved the de Branges positivity condition (3.1) implies RH -- but it is
strictly stronger than RH (it implies GRH for all Dirichlet L at once), and they showed it
FAILS for zeta. The pointwise necessary consequence of (3.1) at each zero rho is

    Q(rho) := -Re{ xi'(rho) xi(1 + rho) }    (>= 0 for all zeros if (3.1) held).

Conrey-Li's decisive computation: at the 34th zeta zero rho_34 = 1/2 + 111.0295... i (ON the
critical line, RH-TRUE), Q(rho_34) = -5.389100507182945e-69 < 0. The signed pairing that DOES
see the zeros has the WRONG positivity, and it fails even where RH holds.

WHAT WE COMPUTE AND FIND (all numbers independently reproduced here, not transcribed):
 1. ANCHOR. With xi(s) = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s) (Conrey-Li's normalization, no
    1/2 factor), Q(rho_34) = -5.38910050718e-69, matching Conrey-Li to 12 significant figures
    (ratio 1.000). Riemann's 1/2-normalized xi gives exactly 1/4 of this (Q is bilinear in xi).
 2. SIGN SEQUENCE. Among the first 50 zeta zeros, Q(rho_k) < 0 for EXACTLY ONE index, k=34.
    So a global signed pairing that sees the zeros fails sporadically even under RH.
 3. SUPPRESSION LAW (sharper than #38). log10|Q| vs gamma has finite-size slope -0.655 over
    k=1..50, converging to -(pi/2)/ln10 = -0.6822: TWICE as steep as #38's single-Gamma
    -(pi/4)/ln10 = -0.3411, because Q = xi'(rho) * xi(1+rho) carries TWO completed-xi factors
    (each contributes one Gamma(s/2) super-exponential decay; the sub-slopes are ~ -0.33 each).
 4. CONTROLS / K2. The buildable direction is RH-AGNOSTIC -- it is the THIRD soft detector
    after #38 (heat kernel) and #39 (Rodgers-Tao log-gas):
      - chi3 (odd, RH true): 0 negatives among 46 zeros to T=100.
      - chi4 (odd, RH true): 1 negative (k=30) to T=100. So sporadic Q<0 occurs for SOME
        Euler L-functions under RH but the density is L-function-dependent, not generic.
      - Davenport-Heilbronn (RH FALSE): its ON-LINE zeros ALSO show sporadic Q<0 (1 of 28),
        identical behaviour to RH-true zeta/chi4 -- so Q<0 is NOT an RH-violation signal. The
        actual off-line obstruction (the pair at gamma~85.7) is double-suppressed to
        |Q| ~ 1e-56, far below #38's 1e-29 detection floor (the off-line sign split is a
        shift artifact of the non-conjugate-symmetric choice, not structural; K2 rests on the
        magnitude only).

THE COORDINATE (honest). This is a NEGATIVE coordinate and the exact CONVERSE of #42: #42
showed the LOCAL data cannot see the zeros; here the GLOBAL de Branges pairing DOES see them,
but its positivity is the wrong (pointwise, strictly-stronger-than-RH) one. The implication
for Direction 8 / M3: the signed pairing that realizes the continuation must be RH-EQUIVALENT
(a global SUM, like the Li coefficients lambda_n which the project verified positive for zeta
in 3A), NOT the pointwise Hermite-Biehler cross-term. It does NOT advance the Direction-8 gap
itself (no Weil cohomology is constructed; M3 is unchanged); it rules out a route.

Run: python -m experiments.arithmetic_geometric.e2db_debranges_crossterm
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

from experiments._shared.dirichlet_l import chi3_L, chi4_L
from experiments._shared.davenport_heilbronn import davenport_heilbronn as DH

HERE = Path(__file__).resolve().parent
DPS_ZETA = 80          # |Q| reaches ~1e-88 by k=50; 80 digits keeps the sign reliable
DPS_CTRL = 60          # controls live at lower height (T<=100)
PUBLISHED_34 = mp.mpf("-5.389100507182945e-69")   # Conrey-Li, arXiv:math/9812166


# ----------------------------------------------------------------------------- xi / Lambda
def xi(s):
    """Completed zeta in Conrey-Li's normalization (NO 1/2 factor): reproduces their Q."""
    s = mp.mpc(s)
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lambda_dirichlet(L):
    """Self-dual completed Dirichlet L: Lambda(s) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s)."""
    q, a = L.modulus, L.parity
    def Lam(s):
        s = mp.mpc(s)
        return mp.power(mp.mpf(q) / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2) * L.evaluate(s)
    return Lam


def lambda_DH(s):
    """Self-dual completed Davenport-Heilbronn (odd character mod 5, a=1, q=5).

    Lambda(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s); satisfies Lambda(s)=Lambda(1-s)
    given f(s) = (pi/5)^{s-1/2} Gamma((2-s)/2)/Gamma((s+1)/2) f(1-s) (the coded FE).
    """
    s = mp.mpc(s)
    return mp.power(mp.mpf(5) / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * DH.evaluate(s)


def Q(Lam, rho):
    """The Conrey-Li pointwise de Branges cross-term Q(rho) = -Re{Lam'(rho) Lam(1+rho)}."""
    return -mp.re(mp.diff(Lam, rho) * Lam(1 + rho))


def _slope(gammas, logabsQ):
    """OLS slope of log10|Q| vs gamma."""
    n = len(gammas)
    mx = sum(gammas) / n
    my = sum(logabsQ) / n
    sxx = sum((x - mx) ** 2 for x in gammas)
    return sum((x - mx) * (y - my) for x, y in zip(gammas, logabsQ)) / sxx


# ----------------------------------------------------------------------------- runners
def run_zeta(n_zeros=50):
    mp.mp.dps = DPS_ZETA
    print("=" * 78)
    print("1-3. ZETA: anchor, sign sequence, double-archimedean suppression law")
    print("=" * 78)
    gammas, logsQ, signs = [], [], []
    sub_xip, sub_x1 = [], []          # the two-factor decomposition of the slope
    neg = []
    q34 = None
    for k in range(1, n_zeros + 1):
        rho = mp.zetazero(k)
        xip = mp.diff(xi, rho)
        x1 = xi(1 + rho)
        qk = -mp.re(xip * x1)
        if k == 34:
            q34 = qk
        if qk < 0:
            neg.append(k)
        gammas.append(float(rho.imag))
        logsQ.append(float(mp.log10(abs(qk))))
        signs.append(int(mp.sign(qk)))
        sub_xip.append(float(mp.log10(abs(xip))))
        sub_x1.append(float(mp.log10(abs(x1))))

    ratio = q34 / PUBLISHED_34
    print(f"  ANCHOR  Q(rho_34) = {mp.nstr(q34, 13)}")
    print(f"          Conrey-Li = {mp.nstr(PUBLISHED_34, 13)}   ratio = {mp.nstr(ratio, 8)} (no-1/2 xi)")
    print(f"          (Riemann's 1/2-normalized xi would give 1/4 of this: Q bilinear in xi)")
    print(f"  SIGN SEQUENCE k=1..{n_zeros}: negative at k = {neg}  ({len(neg)} of {n_zeros})")
    s_all = _slope(gammas, logsQ)
    s_tail = _slope(gammas[20:], logsQ[20:])
    s_xip = _slope(gammas, sub_xip)
    s_x1 = _slope(gammas, sub_x1)
    pi2 = -float(mp.pi / 2 / mp.log(10))
    pi4 = -float(mp.pi / 4 / mp.log(10))
    print(f"  SLOPE log10|Q| vs gamma:  all k=1..{n_zeros} = {s_all:.4f}   tail k=21..{n_zeros} = {s_tail:.4f}")
    print(f"          target -(pi/2)/ln10 = {pi2:.4f}   (#38 single-Gamma -(pi/4)/ln10 = {pi4:.4f})")
    print(f"  TWO-FACTOR decomposition: slope[log|xi'(rho)|] = {s_xip:.4f}, slope[log|xi(1+rho)|] = {s_x1:.4f}")
    print(f"          (each ~ {pi4:.4f}; they sum to the {pi2:.4f} double-Gamma law)\n")
    return dict(gammas=gammas, logsQ=logsQ, signs=signs, neg=neg, q34=q34, ratio=ratio,
                slope_all=s_all, slope_tail=s_tail, sub_xip=sub_xip, sub_x1=sub_x1)


def run_dirichlet(L, T, label):
    mp.mp.dps = DPS_CTRL
    Lam = lambda_dirichlet(L)
    zs = L.zeros(T, prec=40)
    gammas, logsQ, signs, neg = [], [], [], []
    for k, rho in enumerate(zs, 1):
        qk = Q(Lam, rho)
        gammas.append(float(rho.imag))
        logsQ.append(float(mp.log10(abs(qk))))
        signs.append(int(mp.sign(qk)))
        if qk < 0:
            neg.append((k, float(rho.imag)))
    sl = _slope(gammas, logsQ) if len(gammas) >= 3 else float("nan")
    print(f"  {label}: {len(zs)} zeros to T={T}  ->  {len(neg)} negative {[n[0] for n in neg]}, slope {sl:.4f}")
    return dict(gammas=gammas, logsQ=logsQ, signs=signs, neg=neg, slope=sl, n=len(zs))


def run_DH(T=90):
    mp.mp.dps = DPS_CTRL
    print("=" * 78)
    print("4b. Davenport-Heilbronn (RH FALSE): on-line sporadic Q<0 (K2-null) + off-line floor")
    print("=" * 78)
    # self-dual completed function check
    res = max(float(abs(lambda_DH(s) - lambda_DH(1 - s)))
              for s in [mp.mpc(0.5, 10), mp.mpc(0.7, 30), mp.mpc(0.3, 5)])
    print(f"  completed Lambda_DH self-dual check: max|Lambda(s)-Lambda(1-s)| = {res:.2e}")
    zs = DH.zeros(T, prec=40)
    online = [z for z in zs if abs(float(z.real) - 0.5) <= 0.01]
    offline = [z for z in zs if abs(float(z.real) - 0.5) > 0.01]
    on_neg = []
    on_g, on_lq = [], []
    for k, rho in enumerate(online, 1):
        qk = Q(lambda_DH, rho)
        on_g.append(float(rho.imag)); on_lq.append(float(mp.log10(abs(qk))))
        if qk < 0:
            on_neg.append((k, float(rho.imag)))
    print(f"  ON-LINE: {len(online)} zeros to T={T}; Q<0 at {on_neg}  ({len(on_neg)} of {len(online)})")
    print(f"           -> RH-AGNOSTIC: same sporadic Q<0 as RH-true zeta/chi4")
    off = []
    print(f"  OFF-LINE pair (the actual RH violation), MAGNITUDE only (sign = shift artifact):")
    for rho in offline:
        qk = Q(lambda_DH, rho)
        lq = float(mp.log10(abs(qk)))
        off.append((float(rho.real), float(rho.imag), int(mp.sign(qk)), lq))
        print(f"     rho={mp.nstr(rho,8)}  signQ={int(mp.sign(qk)):+d}  log10|Q|={lq:.2f}")
    floor38 = -29.0
    print(f"           -> off-line |Q| ~ 1e{off[0][3]:.0f}, far below #38's detection floor 1e{floor38:.0f}\n")
    return dict(self_dual_residual=res, online_neg=on_neg, n_online=len(online),
                on_g=on_g, on_lq=on_lq, offline=off)


def run():
    print("\n2DB.1 -- de Branges / Conrey-Li per-zero cross-term Q(rho) = -Re{xi'(rho) xi(1+rho)}")
    print("A NEGATIVE coordinate: the global pairing sees the zeros, but its positivity is wrong.\n")

    z = run_zeta(50)

    print("=" * 78)
    print("4a. EULER CONTROLS (RH true): chi3, chi4 -- the buildable direction is RH-agnostic")
    print("=" * 78)
    c3 = run_dirichlet(chi3_L, 100, "chi3 (odd, cond 3)")
    c4 = run_dirichlet(chi4_L, 100, "chi4 (odd, cond 4)")
    print()
    dh = run_DH(90)

    # ---- assertions on the independently-verified numbers ----
    assert z["q34"] < 0, "Q(rho_34) must be negative (Conrey-Li)"
    assert 0.24 < float(z["ratio"]) < 0.26 or 0.99 < float(z["ratio"]) < 1.01, \
        f"Q(rho_34)/published = {z['ratio']} not at 1.0 (no-1/2) or 0.25 (1/2)"
    assert z["neg"] == [34], f"zeta first-50 negatives should be exactly [34], got {z['neg']}"
    assert -0.70 < z["slope_all"] < -0.62, f"zeta slope {z['slope_all']} off the double-Gamma law"
    assert len(c3["neg"]) == 0, f"chi3 should have 0 negatives to T=100, got {c3['neg']}"
    assert len(c4["neg"]) == 1 and c4["neg"][0][0] == 30, f"chi4 should be 1 negative (k=30), got {c4['neg']}"
    assert len(dh["online_neg"]) >= 1, "D-H on-line should also show sporadic Q<0 (K2-null)"
    assert dh["offline"][0][3] < -40, "D-H off-line |Q| should be deeply suppressed (<1e-40)"
    print("All assertions PASS (independently reproduced; not transcribed from the survey).")

    _save(z, c3, c4, dh)
    _plot(z, c3, c4, dh)


def _save(z, c3, c4, dh):
    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        print(f"(npz skipped: {exc})")
        return
    np.savez(
        HERE / "e2db_debranges_crossterm.npz",
        zeta_gamma=np.array(z["gammas"]), zeta_logQ=np.array(z["logsQ"]), zeta_sign=np.array(z["signs"]),
        chi3_gamma=np.array(c3["gammas"]), chi3_logQ=np.array(c3["logsQ"]), chi3_sign=np.array(c3["signs"]),
        chi4_gamma=np.array(c4["gammas"]), chi4_logQ=np.array(c4["logsQ"]), chi4_sign=np.array(c4["signs"]),
        dh_online_gamma=np.array(dh["on_g"]), dh_online_logQ=np.array(dh["on_lq"]),
        dh_offline=np.array(dh["offline"]),
        zeta_slope=z["slope_all"], zeta_slope_tail=z["slope_tail"],
    )
    print("Saved: e2db_debranges_crossterm.npz")


def _plot(z, c3, c4, dh):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: sign sequence (zeta, chi3, chi4)
    ax = axes[0]
    for name, d, color in [("zeta", z, "tab:blue"), ("chi3", c3, "tab:green"), ("chi4", c4, "tab:orange")]:
        ks = list(range(1, len(d["signs"]) + 1))
        ax.scatter(ks, d["signs"], s=18, color=color, label=name, alpha=0.8)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel("zero index k"); ax.set_ylabel("sign Q(rho_k)")
    ax.set_yticks([-1, 1]); ax.set_title("Sign of the de Branges cross-term Q(rho_k)\n(Q<0 = de Branges positivity fails at that zero)")
    ax.legend(); ax.grid(alpha=0.3)

    # Panel 2: log10|Q| vs gamma with both reference slopes
    ax = axes[1]
    g = np.array(z["gammas"]); lq = np.array(z["logsQ"])
    ax.scatter(g, lq, s=16, color="tab:blue", label="zeta")
    pi2 = -float(mp.pi / 2 / mp.log(10)); pi4 = -float(mp.pi / 4 / mp.log(10))
    g0 = g.min(); c = lq[0] - z["slope_all"] * g[0]
    ax.plot(g, pi2 * (g - g0) + (lq[0]), "--", color="tab:red",
            label=f"-(pi/2)/ln10 = {pi2:.3f} (double-Gamma)")
    ax.plot(g, pi4 * (g - g0) + (lq[0]), ":", color="gray",
            label=f"-(pi/4)/ln10 = {pi4:.3f} (#38 single-Gamma)")
    ax.set_xlabel("gamma = Im(rho)"); ax.set_ylabel("log10 |Q(rho)|")
    ax.set_title(f"Double-archimedean suppression (zeta)\nfit slope = {z['slope_all']:.3f}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: D-H on-line vs off-line against the exp(-(pi/2)gamma) floor
    ax = axes[2]
    ax.scatter(dh["on_g"], dh["on_lq"], s=18, color="tab:purple", label="D-H on-line")
    for (re, im, sg, lq_) in dh["offline"]:
        ax.scatter([im], [lq_], s=70, marker="x", color="tab:red")
    ax.scatter([], [], marker="x", color="tab:red", label="D-H off-line (gamma~85.7)")
    ax.axhline(-29, color="k", ls="--", lw=1, label="#38 detection floor 1e-29")
    ax.set_xlabel("gamma = Im(rho)"); ax.set_ylabel("log10 |Q(rho)|")
    ax.set_title("D-H: the actual off-line obstruction is\ndouble-suppressed below detectability")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.suptitle("2DB.1 -- de Branges/Conrey-Li cross-term Q(rho): a NEGATIVE coordinate (third soft detector)", fontsize=12)
    fig.tight_layout()
    fig.savefig(HERE / "e2db_debranges_crossterm.png", dpi=130)
    plt.close(fig)
    print("Saved: e2db_debranges_crossterm.png")


if __name__ == "__main__":
    run()

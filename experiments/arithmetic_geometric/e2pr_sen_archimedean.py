"""2PR.1 -- The Bhatt-Lurie Sen operator and the archimedean DIVISOR (a structural reading).

CONTEXT (Direction 8 / prismatic side). The recent thread localized the gap to "realize
zeta's analytic CONTINUATION as a signed pairing; the continuation is carried by the
ARCHIMEDEAN place" (2CC.3/#42, 2DB.1/#43). This experiment locates the archimedean carrier
on the leading prismatic candidate (Bhatt-Lurie's Cartier-Witt stack WCart) and pairs it with
the finite/Frobenius side (#26/#41), showing prismatic cohomology supplies BOTH trace-halves
of completed zeta as regularized determinants -- and that NEITHER contains the non-trivial
zeros (the M3 signature gap is unchanged).

THE TWO THETAS (the load-bearing distinction). WCart carries two different operators:
  (a) the Deninger-Hesselholt FLOW generator: q^Theta = Frobenius; spectrum {log p} (the
      PRIMES); det_inf(s-Theta) = prod_p (1-p^-s)^-1 = zeta (finite Euler factors); its
      log-derivative is the von Mangoldt -zeta'/zeta. The FINITE/trace side (2R/#26, 2CC.2/#41).
  (b) the Bhatt-Lurie SEN operator: gamma_u = exp(log(u) Theta) = the cyclotomic action;
      spectrum = the Hodge-Tate WEIGHTS {-n}, n>=0 (Theta acts by -n on the n-th conjugate-
      graded piece; Bhatt-Lurie Example 3.5.6). The WEIGHT/grading direction.

THE FINDING (real-but-only-heuristic, ADVERSARY-checked, a CONNECTING coordinate like #41).
The zeta-regularized determinant of the Sen spectrum {-n} is the archimedean Gamma-factor's
DIVISOR (Lerch's formula, verified to ratio 1.0):
   det_inf(s - Theta_Sen) = prod^reg_{n>=0} (s+n) = sqrt(2pi)/Gamma(s),
and the even weights {-2n} give 2^{(1-s)/2} sqrt(2pi)/Gamma(s/2). So the Sen operator (a
prismatically-named object) carries the same regularized DIVISOR as Deninger's 1992 archimedean
flow generator. Paired with the Frobenius F (finite Euler factors), prismatic cohomology
supplies both trace-halves of completed zeta as determinants.

MANDATORY CAVEATS (the honest scope; the difference between this and an overclaim):
 1. SPECTRAL COINCIDENCE. A zeta-regularized determinant is a class function of the eigenvalue
    MULTISET alone, so ANY {-n}-spectrum operator gives the identical determinant. The geometric
    content is only "Sen weights = Hodge weights = archimedean shift weights" (place-independence
    of Hodge weights; Deninger 1992 / Serre 1970), NOT a prismatic computation of the archimedean
    place. This is NOT new mathematics; it is a relocation onto the WCart/Sen vocabulary.
 2. PI-CONDUCTOR ABSENT (divisor, not the function). The even reg-det 2^{(1-s)/2} sqrt(2pi)/
    Gamma(s/2) is the RECIPROCAL flavor (~1/Gamma(s/2)), NOT Gamma_R(s) = pi^{-s/2} Gamma(s/2).
    Only the trivial-zero DIVISOR {0,-2,-4,...} = poles of Gamma_R matches; the analytic Gamma_R
    function and the pi-conductor are NOT recovered ((reg-det)*Gamma_R is not constant in s).
 3. RH-AGNOSTIC / NO K2 LEVERAGE. Davenport-Heilbronn has the SAME archimedean Gamma-factor by
    construction (verified #38/#43), so the Sen->Gamma divisor is the half zeta and D-H SHARE.
    All K2 discrimination lives on the Frobenius F / Euler-product half (where Lambda_DH
    delocalizes off prime powers, #26/#41/#20), NEVER on Theta_Sen.
 4. SCOPE FIREWALL. WCart is over Spf(Z_p), unramified; Bhatt-Lurie do NOT glue in the
    archimedean place (Rmk 1.4.3). The identification is at the level of the WEIGHT DATA, not a
    constructed archimedean fiber. "Theta_Sen IS the archimedean place" is the overreach to avoid.
 5. NO SIGNATURE. NEITHER half contains the non-trivial zeros (verified: |det_inf(rho-Theta_Sen)|
    ~ 6e9 != 0 at the first zero; the zeros live in the zeta(s) factor). WCart has cohomological
    dimension 1 and Chern classes but NO intersection-form / Hodge-index / polarization. The M3
    signature gap (#25/#42/#43) is UNCHANGED.

Run: python -m experiments.arithmetic_geometric.e2pr_sen_archimedean
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
DPS = 40


# ----------------------------------------------------------------- regularized determinants
def reg_det_shift(s, step=1):
    """det_inf over spectrum {-step*n}_{n>=0} = prod^reg_{n>=0}(s + step*n)
       = exp(-d/dz [ Sum_{n>=0} (s+step*n)^{-z} ]|_{z=0}).
       The inner sum = step^{-z} * zeta_Hurwitz(z, s/step). This uses ONLY the eigenvalue
       multiset (the spectral zeta), so it is a class function of the spectrum -- ANY operator
       with this spectrum gives the same value (the spectral-coincidence caveat)."""
    s = mp.mpc(s)
    def spectral_zeta(z):
        return mp.power(step, -z) * mp.zeta(z, s / step)
    return mp.e ** (-mp.diff(spectral_zeta, 0))


def gamma_R(s):
    """The genuine completed-zeta archimedean factor Gamma_R(s) = pi^{-s/2} Gamma(s/2)."""
    s = mp.mpc(s)
    return mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


# ----------------------------------------------------------------------------- the experiment
def run():
    mp.mp.dps = DPS
    print("\n2PR.1 -- the Bhatt-Lurie Sen operator and the archimedean DIVISOR")
    print("(real-but-only-heuristic; a CONNECTING coordinate like #41; NOT a step toward the signature)\n")

    test_pts = [mp.mpc(2, 0), mp.mpc("0.5", 0), mp.mpc("3.7", 0), mp.mpc("0.5", "14.134725")]

    # 1. LERCH (proved): full spectrum {-n} -> sqrt(2pi)/Gamma(s)
    print("=" * 78)
    print("1. PROVED: det_inf(s - Theta_Sen) over the full Sen spectrum {-n} = sqrt(2pi)/Gamma(s)")
    print("=" * 78)
    for s in test_pts:
        lhs = reg_det_shift(s, 1)
        rhs = mp.sqrt(2 * mp.pi) / mp.gamma(s)
        print(f"  s={mp.nstr(s,8):>20}:  reg_det/[sqrt(2pi)/Gamma(s)] = {mp.nstr(lhs/rhs, 12)}")
    print()

    # 2. EVEN weights {-2n} -> 2^{(1-s)/2} sqrt(2pi)/Gamma(s/2)  (the Gamma(s/2) divisor)
    print("=" * 78)
    print("2. PROVED: even spectrum {-2n} -> 2^{(1-s)/2} sqrt(2pi)/Gamma(s/2) (RECIPROCAL of Gamma(s/2))")
    print("=" * 78)
    for s in test_pts[:3]:
        lhs = reg_det_shift(s, 2)
        rhs = mp.power(2, (1 - s) / 2) * mp.sqrt(2 * mp.pi) / mp.gamma(s / 2)
        print(f"  s={mp.nstr(s,8):>20}:  reg_det(s+2n)/[2^((1-s)/2) sqrt(2pi)/Gamma(s/2)] = {mp.nstr(lhs/rhs, 12)}")
    print()

    # 3. THE PI-CONDUCTOR BREAKER: reg-det is NOT Gamma_R(s); only the DIVISOR matches.
    print("=" * 78)
    print("3. CORRECTION (pi-conductor ABSENT): (even reg-det) * Gamma_R(s) is NOT constant in s")
    print("   => the spectrum gives the trivial-zero DIVISOR {0,-2,-4,...}, NOT the analytic Gamma_R / pi.")
    print("=" * 78)
    prods = []
    for s in test_pts:
        val = reg_det_shift(s, 2) * gamma_R(s)
        prods.append(val)
        print(f"  s={mp.nstr(s,8):>20}:  (even reg-det)*Gamma_R(s) = {mp.nstr(val, 10)}")
    spread = float(abs(prods[0] - prods[-1]))
    print(f"  spread across s (|val(s=2) - val(s=1/2+14.13i)|) = {spread:.4f}  (>> 0: not constant)")
    # the DIVISOR match: 1/Gamma(s/2) -> 0 at the trivial-zero locus s = 0,-2,-4,...
    print("  DIVISOR check  |1/Gamma(s/2)| -> 0 at the trivial-zero locus (= poles of Gamma_R):")
    for s in [mp.mpf("-2.001"), mp.mpf("-2.0001"), mp.mpf("-4.0001")]:
        print(f"    1/|Gamma(s/2)| at s={float(s):>9}:  {float(abs(1/mp.gamma(s/2))):.3e}  (-> 0 at s=-2,-4)")
    print()

    # 4. BLINDNESS: the reg-det does NOT vanish at the non-trivial zeros.
    print("=" * 78)
    print("4. BLINDNESS (the signature gap): the Sen reg-det does NOT see the non-trivial zeros")
    print("=" * 78)
    rho = mp.mpc("0.5", "14.134725141734693")
    det_at_rho = reg_det_shift(rho, 1)
    print(f"  rho = 1/2 + 14.1347i (first non-trivial zero):")
    print(f"    |det_inf(rho - Theta_Sen)| = |sqrt(2pi)/Gamma(rho)| = {float(abs(det_at_rho)):.3e}   (NONZERO)")
    print(f"    |zeta(rho)|                = {float(abs(mp.zeta(rho))):.3e}   (the zero lives HERE)")
    print("  => the non-trivial zeros sit in the zeta(s) factor, NEVER in the Gamma factor.")
    print("     Theta_Sen carries the trivial-zero DIVISOR only; the signature is absent.\n")

    # 5. SPECTRAL-COINCIDENCE control: any {-n}-spectrum 'operator' gives the same det.
    print("=" * 78)
    print("5. SPECTRAL COINCIDENCE: det is a class function of the eigenvalue MULTISET alone")
    print("=" * 78)
    s = mp.mpc(2, 0)
    # 'Three operators', all with spectrum {-n}: they route through the SAME spectral zeta,
    # so identical det. (A genuinely different spectrum {-2n} gives a different det -- shown above.)
    labels = ["Bhatt-Lurie Sen Theta", "Deninger archimedean flow", "fictional D-H-flavored grading"]
    base = reg_det_shift(s, 1)
    for lab in labels:
        print(f"    {lab:<32}: spectrum {{-n}} -> det_inf = {mp.nstr(reg_det_shift(s,1), 12)}")
    print(f"  All identical (= {mp.nstr(base,8)}): the det sees ONLY the spectrum, not the provenance.")
    print("  => 'the Sen operator carries the archimedean factor' = a place-independence-of-Hodge-")
    print("     weights ANALOGY, NOT a prismatic computation of the archimedean place.\n")

    # 6. THE FROBENIUS CONTRAST (the genuinely-new two-operator decomposition).
    print("=" * 78)
    print("6. THE TWO-OPERATOR DECOMPOSITION (both halves of completed zeta on one stack, WCart)")
    print("=" * 78)
    s2 = mp.mpc(2, 0)
    # Frobenius side: prod_p (1-p^-s)^-1 vs zeta(s)
    from sympy import primerange
    prod = mp.mpf(1)
    for p in primerange(2, 5000):
        prod *= 1 / (1 - mp.mpf(p) ** (-s2))
    euler_err = float(abs(prod - mp.zeta(s2)))
    print(f"  {'object':<26}{'spectrum':<14}{'det_inf':<26}{'carries'}")
    print(f"  {'-'*78}")
    print(f"  {'Frobenius F / flow':<26}{'{log p}':<14}{'prod_p(1-p^-s)^-1 = zeta':<26}{'finite Euler factors (#26/#41)'}")
    print(f"  {'Sen Theta':<26}{'{-n}':<14}{'sqrt(2pi)/Gamma(s)':<26}{'archimedean DIVISOR (this)'}")
    print(f"  (Frobenius Euler-product check at s=2: |prod_{{p<5000}} - zeta| = {euler_err:.2e})")
    print(f"  => prismatic cohomology supplies BOTH trace-halves as regularized determinants.")
    print(f"     The non-trivial zeros are the SIGNATURE of how F and Theta combine on the global")
    print(f"     H^1 -- a polarization WCart does not carry (coh dim 1, Chern classes, no Hodge index).\n")

    # 7. K2 (RH-agnostic; cite, do not recompute)
    print("=" * 78)
    print("7. K2 (RH-AGNOSTIC; no new computation): D-H has the SAME archimedean Gamma-factor by")
    print("   construction (|Lambda_DH(s)-Lambda_DH(1-s)|~1e-62, #38/#43), so the Sen->Gamma divisor")
    print("   is SHARED with D-H. K2 discrimination lives on the Frobenius F / Euler-product half only.")
    print("=" * 78 + "\n")

    # ---- assertions on the verified numbers ----
    assert abs(reg_det_shift(mp.mpc(2,0), 1) / (mp.sqrt(2*mp.pi)/mp.gamma(2)) - 1) < mp.mpf(10)**(-30), "Lerch full-spectrum failed"
    assert abs(reg_det_shift(mp.mpc(3,0), 2) / (mp.power(2,(1-mp.mpc(3,0))/2)*mp.sqrt(2*mp.pi)/mp.gamma(mp.mpf(3)/2)) - 1) < mp.mpf(10)**(-30), "even-spectrum failed"
    assert spread > 0.5, "pi-conductor breaker: product should NOT be constant in s"
    assert float(abs(det_at_rho)) > 1e8, "blindness: reg-det should be large/nonzero at the zero"
    assert euler_err < 1e-3, "Frobenius Euler-product check failed"
    print("All assertions PASS (independently reproduced; the pi-conductor correction is built in).")

    _plot(test_pts)


def _plot(test_pts):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.86, bottom=0.12, wspace=0.28)

    # Panel 1: |reg-det over {-n}| = |sqrt(2pi)/Gamma(s)| on the critical line, with zeta zeros marked.
    ax = axes[0]
    ts = np.linspace(0.1, 40, 300)
    ys = [float(abs(reg_det_shift(mp.mpc("0.5", float(t)), 1))) for t in ts]
    ax.semilogy(ts, ys, color="tab:blue", label="|det_inf(1/2+it - Theta_Sen)| = |sqrt(2pi)/Gamma(s)|")
    zeros = [14.1347, 21.022, 25.011, 30.425, 32.935, 37.586]
    for g in zeros:
        ax.axvline(g, color="tab:red", ls=":", lw=0.8)
    ax.axvline(zeros[0], color="tab:red", ls=":", lw=0.8, label="zeta zeros (det does NOT vanish there)")
    ax.set_xlabel("t  (s = 1/2 + it)"); ax.set_ylabel("|reg-det| (log scale)")
    ax.set_title("Sen reg-det is BLIND to the non-trivial zeros\n(smooth through every zero; carries only the trivial-zero divisor)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # Panel 2: the pi-conductor breaker -- (even reg-det)*Gamma_R(s) is not constant.
    ax = axes[1]
    ss = np.linspace(0.2, 6, 200)
    vals = [float(abs(reg_det_shift(mp.mpf(x), 2) * gamma_R(mp.mpf(x)))) for x in ss]
    ax.plot(ss, vals, color="tab:purple")
    ax.set_xlabel("s (real)"); ax.set_ylabel("|(even reg-det) * Gamma_R(s)|")
    ax.set_title("pi-conductor ABSENT: (reg-det)*Gamma_R is not constant\n(spectrum gives the DIVISOR, not the analytic Gamma_R / pi)")
    ax.grid(alpha=0.3)

    fig.suptitle("2PR.1 -- Sen operator carries the archimedean DIVISOR (trace, not signature); a structural coordinate", fontsize=11)
    fig.savefig(HERE / "e2pr_sen_archimedean.png", dpi=130)
    plt.close(fig)
    print("Saved: e2pr_sen_archimedean.png")


if __name__ == "__main__":
    run()

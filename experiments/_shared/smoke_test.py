"""Phase 0 smoke test: do zeta and Davenport-Heilbronn work?

Validates:
  1. zeta evaluation matches mpmath's mp.zeta directly
  2. zeta first few zeros match known values (14.134..., 21.022..., ...)
  3. Davenport-Heilbronn evaluation gives known value at s=2
     (verify against direct Dirichlet series sum)
  4. Davenport-Heilbronn satisfies the functional equation numerically
  5. Davenport-Heilbronn finds at least one zero near the expected
     low-lying off-line position
"""

from __future__ import annotations

import mpmath as mp

from experiments._shared import zeta_L, DavenportHeilbronn, chi3_L, chi4_L


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_zeta_evaluation():
    print("Test 1: zeta evaluation")
    mp.mp.dps = 30
    val_ours = zeta_L.evaluate(mp.mpc(2))
    val_ref = mp.zeta(2)
    return check(
        "zeta(2) matches mpmath",
        abs(val_ours - val_ref) < mp.mpf(10) ** (-25),
        f"got {val_ours}",
    )


def test_zeta_zeros():
    print("Test 2: zeta first three zeros")
    mp.mp.dps = 30
    zeros = zeta_L.zeros(T_max=30, prec=30)
    if len(zeros) < 3:
        return check("at least 3 zeros below T=30", False, f"got {len(zeros)}")
    expected = [
        mp.mpf("14.134725141734693790457251983562"),
        mp.mpf("21.022039638771554992628479593897"),
        mp.mpf("25.010857580145688763213790992562"),
    ]
    ok_all = True
    for k, exp in enumerate(expected):
        diff = abs(zeros[k].imag - exp)
        ok = diff < mp.mpf(10) ** (-25)
        ok_all = ok_all and check(
            f"zero #{k+1} imag = {exp}", ok, f"got {zeros[k].imag}"
        )
    return ok_all


def test_dh_dirichlet():
    print("Test 3: Davenport-Heilbronn Dirichlet sum at s=2")
    mp.mp.dps = 30
    dh = DavenportHeilbronn()
    direct = mp.mpf(0)
    coeffs = dh._coeffs(30)
    for n in range(1, 5000):
        direct += coeffs[(n - 1) % 5] / mp.mpf(n) ** 2
    via_hurwitz = dh.evaluate(mp.mpc(2)).real
    diff = abs(direct - via_hurwitz)
    return check(
        "Hurwitz form agrees with direct Dirichlet sum",
        float(diff) < 1e-3,
        f"direct {direct}, Hurwitz {via_hurwitz}, diff {diff}",
    )


def test_dh_functional_equation():
    print("Test 4: Davenport-Heilbronn functional equation")
    mp.mp.dps = 50
    dh = DavenportHeilbronn()
    residuals = []
    for s in [mp.mpc("0.3", "5.0"), mp.mpc("0.5", "10.0"), mp.mpc("0.7", "20.0")]:
        res = abs(dh.functional_equation_residual(s))
        ratio = abs(dh.evaluate(s))
        relative = float(res) / max(float(ratio), 1e-20)
        residuals.append((s, float(res), float(ratio), relative))
        print(f"     s={s} |residual|={float(res):.2e} |f(s)|={float(ratio):.2e} rel={relative:.2e}")
    ok = all(r[3] < 1e-3 for r in residuals)
    return check("functional equation holds (rel < 1e-3) at sampled s", ok)


def test_dh_offline_zero():
    print("Test 5: Davenport-Heilbronn off-line zero in upper strip")
    mp.mp.dps = 30
    dh = DavenportHeilbronn()
    zeros_list = dh.zeros(T_max=100.0, prec=30, scan_step=0.5)
    print(f"     found {len(zeros_list)} zero(s) below T=100")
    for z in zeros_list[:10]:
        offline = abs(float(z.real) - 0.5) > 0.01
        marker = "  OFFLINE" if offline else ""
        print(f"     rho = {float(z.real):.6f} + {float(z.imag):.6f} i{marker}")
    has_offline = any(abs(float(z.real) - 0.5) > 0.01 for z in zeros_list)
    ok_any = check("at least one off-line zero found", has_offline)
    # Regression check: the known first off-line zero is near
    # rho ~ 0.808517 + 85.699 i (Davenport-Heilbronn 1936, numerical
    # value reproduced in many sources).
    offline = [z for z in zeros_list if abs(float(z.real) - 0.5) > 0.01]
    ok_loc = False
    for z in offline:
        if abs(float(z.real) - 0.8085) < 0.01 and abs(float(z.imag) - 85.70) < 0.05:
            ok_loc = True
            break
    ok_loc = check("first off-line zero at rho ~ 0.8085 + 85.70 i", ok_loc)
    return ok_any and ok_loc


def test_dirichlet_known_values():
    print("Test 6: Dirichlet L-functions at known special values")
    mp.mp.dps = 30
    # L(2, chi_4) = Catalan's constant G
    val4_2 = chi4_L.evaluate(mp.mpc(2)).real
    ok_g = check(
        "L(2, chi_4) = Catalan",
        float(abs(val4_2 - mp.catalan)) < 1e-25,
        f"got {val4_2}, expected {mp.catalan}",
    )
    # L(3, chi_4) = pi^3 / 32
    val4_3 = chi4_L.evaluate(mp.mpc(3)).real
    expected = mp.pi ** 3 / 32
    ok_pi3 = check(
        "L(3, chi_4) = pi^3/32",
        float(abs(val4_3 - expected)) < 1e-25,
        f"got {val4_3}, expected {expected}",
    )
    return ok_g and ok_pi3


def test_dirichlet_functional_equation():
    print("Test 7: Dirichlet L-functions satisfy functional equation with W = +1")
    mp.mp.dps = 30
    ok_all = True
    for L in (chi3_L, chi4_L):
        res_p, res_m = L.functional_equation_residual(mp.mpc("0.3", "5.0"))
        ok = float(abs(res_p)) < 1e-25 and float(abs(res_m)) > 1e-3
        ok_all = ok_all and check(
            f"{L.name}: |res(W=+1)| < 1e-25 << |res(W=-1)|",
            ok,
            f"W=+1: {float(abs(res_p)):.2e}, W=-1: {float(abs(res_m)):.2e}",
        )
    return ok_all


def test_dirichlet_first_zeros():
    print("Test 8: Dirichlet L-functions first zeros match LMFDB")
    mp.mp.dps = 30
    # LMFDB: chi_3 first zeros at gamma ~ 8.03974, 11.24921, 15.70462
    zs = chi3_L.zeros(T_max=20, prec=30, scan_step=0.25)
    expected_chi3 = [8.039737165225, 11.249206234526, 15.704619356106]
    ok_all = True
    for k, exp in enumerate(expected_chi3):
        if k >= len(zs):
            ok_all = ok_all and check(f"chi_3 zero #{k+1}", False, "not found")
            continue
        diff = float(abs(zs[k].imag - exp))
        ok = diff < 1e-6
        ok_all = ok_all and check(
            f"chi_3 zero #{k+1} = {exp:.10f}", ok, f"got {float(zs[k].imag):.10f}, diff {diff:.2e}"
        )
    return ok_all


def main():
    results = [
        test_zeta_evaluation(),
        test_zeta_zeros(),
        test_dh_dirichlet(),
        test_dh_functional_equation(),
        test_dh_offline_zero(),
        test_dirichlet_known_values(),
        test_dirichlet_functional_equation(),
        test_dirichlet_first_zeros(),
    ]
    print()
    n_pass = sum(results)
    print(f"Smoke test: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

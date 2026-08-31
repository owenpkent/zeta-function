"""E_SPEISER -- Speiser's criterion run against the Davenport-Heilbronn control.

Speiser (1935): RH is equivalent to zeta'(s) having no zeros in the open left
half-strip 0 < Re(s) < 1/2 (quantified by Levinson-Montgomery 1974: zeta and
zeta' have, up to O(log T), equally many zeros left of the line). This probe
asks the question filed by the 2026-08-31 gap sweep (Tier 1 item 4.4,
docs/03_research/reading_notes/wikipedia_rh_gap_sweep_2026-08-31.md): is the
Speiser equivalence FE-only?

The test is the house discipline. Davenport-Heilbronn satisfies a Riemann-style
functional equation, has no Euler product, and violates its own RH (first
off-line pair at beta = 0.8085 and 1 - 0.8085 = 0.1915, gamma = 85.699). If the
Speiser mechanism transplants (an off-line zero forcing a derivative zero left
of the line), the criterion consumes only the FE half of the adelic package and
files in the RH-blind bin next to scattering unimodularity. If it does NOT
transplant (D-H's derivative stays zero-free left of the line at the off-line
height), the equivalence genuinely uses more than the FE; the classical proof
routes through the pole at s = 1 and the sigma >= 1 zero-free region, which for
zeta are Euler-product facts, and D-H (which has zeros in sigma > 1) is exactly
the function that breaks them.

PRE-REGISTERED expectation (from the sweep note): left-of-line derivative zeros
appear for D-H near the off-line pair. The probe is built so that either outcome
is a determinate measurement: winding numbers (argument principle; f and f' are
entire) computed by adaptive phase continuation around rectangles, hard-checked
for integrality, refinement stability, and cross-checked against an independent
grid + findroot sweep, with a positive control proving the instrument counts a
known derivative zero.

Derivatives are analytic, not finite differences: through the Hurwitz
representation f(s) = 5^{-s} sum_a c_a zeta(s, a/5),

    f'(s) = 5^{-s} ( sum_a c_a zeta'(s, a/5) - log(5) sum_a c_a zeta(s, a/5) ),

with mpmath's Hurwitz derivative; zeta'(s) itself via mp.zeta(s, derivative=1).

Run:  python -m experiments.criticality.e_speiser_dh          (11 checks)
      python -m experiments.criticality.e_speiser_dh --quick  (9 checks)
"""
from __future__ import annotations

import sys

import mpmath as mp

from experiments._shared.davenport_heilbronn import davenport_heilbronn as dh

RHO_OFF = mp.mpc("0.8085", "85.699")   # landmark first off-line zero (approx)

# Rectangles [sigma_lo, sigma_hi] x [t_lo, t_hi]; boundaries chosen off zeros.
BOX_DH_MAIN = (0.06, 0.44, 80.2, 90.1)     # left strip, off-line height
BOX_DH_TIGHT = (0.06, 0.48, 83.0, 88.0)    # squeezed toward the line
BOX_DH_LONG = (0.06, 0.44, 10.1, 80.2)     # left strip below the off-line pair
BOX_Z_BAND = (0.06, 0.44, 80.2, 90.1)      # matched zeta' band
BOX_Z_LONG = (0.06, 0.44, 10.1, 100.2)     # zeta' full window


def f(s):
    return dh.evaluate(s)


def fprime(s):
    s = mp.mpc(s)
    c = dh._coeffs(mp.mp.dps)
    five = mp.power(5, -s)
    tot = mp.mpc(0)
    dtot = mp.mpc(0)
    for a in range(1, 6):
        tot += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5)
        dtot += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5, 1)
    return five * (dtot - mp.log(5) * tot)


def fprime2(s):
    s = mp.mpc(s)
    c = dh._coeffs(mp.mp.dps)
    five = mp.power(5, -s)
    l5 = mp.log(5)
    t0 = mp.mpc(0)
    t1 = mp.mpc(0)
    t2 = mp.mpc(0)
    for a in range(1, 6):
        t0 += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5)
        t1 += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5, 1)
        t2 += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5, 2)
    return five * (t2 - 2 * l5 * t1 + l5 * l5 * t0)


def polish_fp_root(x, steps=10):
    """Newton iteration on f' with the analytic f''. Deterministic; muller's
    error metric stalls near 3e-16 on f' roots, so root searches here polish
    with Newton instead and verify the residual directly."""
    for _ in range(steps):
        d = fprime2(x)
        if d == 0:
            break
        x = x - fprime(x) / d
    return x


def zprime(s):
    return mp.zeta(s, derivative=1)


def _winding_along(g, path_pts):
    """Total winding of g along a closed polyline, by adaptive phase tracking.

    Subdivides until every consecutive phase step is below 0.8 rad, so no step
    can alias a full turn. Returns (winding_float, nearest_int, integrality_err).
    """
    pts = [(s, g(s)) for s in path_pts]
    max_pts = 20000
    i = 0
    while i < len(pts) - 1:
        (s1, v1), (s2, v2) = pts[i], pts[i + 1]
        if v1 == 0 or v2 == 0:
            raise RuntimeError("zero of g on the contour; shift the box")
        if abs(mp.arg(v2 / v1)) > 0.8:
            if len(pts) >= max_pts or abs(s2 - s1) < mp.mpf("1e-9"):
                raise RuntimeError("contour refinement failed; zero too close to boundary")
            smid = (s1 + s2) / 2
            pts.insert(i + 1, (smid, g(smid)))
        else:
            i += 1
    total = mp.mpf(0)
    for k in range(len(pts) - 1):
        total += mp.arg(pts[k + 1][1] / pts[k][1])
    w = total / (2 * mp.pi)
    n = int(mp.nint(w))
    return float(w), n, abs(float(w - n))


def rect_winding(g, box, step=0.15):
    slo, shi, tlo, thi = [mp.mpf(str(v)) for v in box]
    corners = [
        mp.mpc(slo, tlo), mp.mpc(shi, tlo), mp.mpc(shi, thi), mp.mpc(slo, thi),
    ]
    path = []
    for k in range(4):
        a, b = corners[k], corners[(k + 1) % 4]
        n = max(8, int(abs(b - a) / step) + 1)
        for j in range(n):
            path.append(a + (b - a) * mp.mpf(j) / n)
    path.append(corners[0])
    return _winding_along(g, path)


def circle_winding(g, center, radius, n0=48):
    path = [center + radius * mp.exp(2j * mp.pi * mp.mpf(k) / n0) for k in range(n0)]
    path.append(path[0])
    return _winding_along(g, path)


def grid_roots(g, box, ns=10, nt=40, keep=10):
    """Independent zero sweep: coarse |g| grid, findroot from the smallest cells."""
    slo, shi, tlo, thi = box
    cells = []
    for i in range(ns + 1):
        sig = slo + (shi - slo) * i / ns
        for j in range(nt + 1):
            t = tlo + (thi - tlo) * j / nt
            s = mp.mpc(sig, t)
            cells.append((float(abs(g(s))), s))
    cells.sort(key=lambda c: c[0])
    roots = []
    for _, s0 in cells[:keep]:
        try:
            r = polish_fp_root(s0)
        except (ValueError, ZeroDivisionError):
            continue
        if abs(g(r)) > mp.mpf("1e-20"):
            continue
        if not (slo < r.real < shi and tlo < r.imag < thi):
            continue
        if all(abs(r - q) > mp.mpf("1e-6") for q in roots):
            roots.append(r)
    return roots


def main(quick: bool = False) -> int:
    mp.mp.dps = 30
    results = []

    def check(name, ok, detail=""):
        results.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    # 1. Right object: functional equation residual.
    r1 = abs(dh.functional_equation_residual(mp.mpc("0.3", "40.0")))
    r2 = abs(dh.functional_equation_residual(mp.mpc("0.7", "85.0")))
    check("FE residual ~ 0 at two points", r1 < mp.mpf("1e-25") and r2 < mp.mpf("1e-25"),
          f"|res| = {mp.nstr(r1, 3)}, {mp.nstr(r2, 3)}")

    # 2. Analytic derivative agrees with central finite difference.
    errs = []
    for s0 in (mp.mpc("0.3", "85.2"), mp.mpc("0.42", "12.7")):
        h = mp.mpf(10) ** -12
        fd = (f(s0 + h) - f(s0 - h)) / (2 * h)
        ap = fprime(s0)
        errs.append(abs(ap - fd) / abs(ap))
    check("analytic f' = finite difference (rel err < 1e-15)", all(e < mp.mpf("1e-15") for e in errs),
          f"rel errs = {mp.nstr(errs[0], 3)}, {mp.nstr(errs[1], 3)}")

    # 3. The off-line pair is where the landmark says, and both are simple zeros
    # of f. The partner is checked by direct evaluation at 1 - conj(rho): the FE
    # plus real Dirichlet coefficients make that point a zero exactly, so no
    # second root search is needed (a muller search from the left start can jump
    # back to rho itself, which is 0.617 away).
    rho = mp.findroot(f, RHO_OFF, solver="muller", tol=mp.mpf(10) ** -25)
    partner = 1 - mp.conj(rho)
    ok3 = (abs(rho - RHO_OFF) < mp.mpf("5e-3") and abs(f(rho)) < mp.mpf("1e-25")
           and abs(f(partner)) < mp.mpf("1e-25")
           and abs(fprime(rho)) > mp.mpf("0.1") and abs(fprime(partner)) > mp.mpf("0.1"))
    check("off-line pair rho, 1 - conj(rho) verified, both simple", ok3,
          f"rho = {mp.nstr(rho, 12)}, |f| = {mp.nstr(abs(f(rho)), 2)}, {mp.nstr(abs(f(partner)), 2)}")

    # 4. Positive control: the instrument counts a known f' zero (right of the
    # strip), located by Newton polish from a scan-derived start.
    s1 = polish_fp_root(mp.mpc("1.2417", "87.428"))
    assert abs(fprime(s1)) < mp.mpf("1e-24"), "positive-control root residual too large"
    assert abs(s1 - mp.mpc("1.2417", "87.428")) < mp.mpf("0.02"), "positive control drifted"
    wc, nc, ec = circle_winding(fprime, s1, mp.mpf("0.05"))
    wb, nb, eb = rect_winding(fprime, (float(s1.real) - 0.1, float(s1.real) + 0.1,
                                       float(s1.imag) - 0.1, float(s1.imag) + 0.1), step=0.05)
    check("instrument positive control: known f' zero counted once", nc == 1 and nb == 1
          and ec < 0.02 and eb < 0.02, f"s1 = {mp.nstr(s1, 12)}, circle {nc}, box {nb}")

    # 5. zeta' left strip, full window: Speiser holds where RH is verified.
    if not quick:
        wz, nz, ez = rect_winding(zprime, BOX_Z_LONG, step=0.08)
        check("zeta' zero count in left strip, t in [10.1, 100.2] == 0", nz == 0 and ez < 0.02,
              f"winding = {wz:+.4f}")

    # 6. zeta' matched band.
    wzb, nzb, ezb = rect_winding(zprime, BOX_Z_BAND, step=0.08)
    check("zeta' zero count in left strip, t in [80.2, 90.1] == 0", nzb == 0 and ezb < 0.02,
          f"winding = {wzb:+.4f}")

    # 7. THE MEASUREMENT: D-H f' zeros in the left strip at the off-line height.
    w1, n1, e1 = rect_winding(fprime, BOX_DH_MAIN, step=0.15)
    check("D-H f' winding integral over [0.06,0.44]x[80.2,90.1]", e1 < 0.02,
          f"count = {n1} (pre-registered expectation was >= 1)")

    # 8. Same, squeezed toward the line.
    w2, n2, e2 = rect_winding(fprime, BOX_DH_TIGHT, step=0.15)
    check("D-H f' winding integral over [0.06,0.48]x[83.0,88.0]", e2 < 0.02,
          f"count = {n2}")

    # 9. Cross-check: independent grid + findroot sweep agrees with the winding.
    roots = grid_roots(fprime, BOX_DH_MAIN)
    check("grid+findroot sweep count == winding count", len(roots) == n1,
          f"sweep found {len(roots)}, winding says {n1}")

    # 10. Refinement stability: main box at higher precision and finer sampling.
    prev = mp.mp.dps
    mp.mp.dps = 40
    try:
        w1r, n1r, e1r = rect_winding(fprime, BOX_DH_MAIN, step=0.07)
    finally:
        mp.mp.dps = prev
    check("main-box count stable under dps 30 -> 40 and 2x sampling", n1r == n1 and e1r < 0.02,
          f"count = {n1r}")

    # 11. D-H left strip below the off-line height.
    if not quick:
        w3, n3, e3 = rect_winding(fprime, BOX_DH_LONG, step=0.15)
        check("D-H f' winding integral over [0.06,0.44]x[10.1,80.2]", e3 < 0.02,
              f"count = {n3}")

    npass, ntot = sum(results), len(results)
    print()
    print("VERDICT INPUTS: D-H off-line pair present at t = 85.699; D-H f' left-strip")
    print(f"counts: main box = {n1}, tight box = {n2}" + ("" if quick else f", long box = {n3}")
          + f"; zeta' left-strip counts = 0.")
    for r in roots:
        print(f"left-strip f' zero: s* = {mp.nstr(r, 15)}  |f(s*)| = {mp.nstr(abs(f(r)), 3)}"
              f"  dist to 1 - conj(rho) = {mp.nstr(abs(r - partner), 4)}")
    if n1 == 0 and n2 == 0:
        print("FINDING: the Speiser mechanism does NOT transplant to D-H at its first")
        print("off-line pair: RH fails there with the left strip f'-zero-free. The")
        print("pre-registered FE-only expectation is REFUTED: Speiser's equivalence")
        print("consumes more than the functional equation.")
    elif n1 >= 1:
        print("FINDING: left-of-line derivative zero(s) present near the off-line pair:")
        print("the Speiser mechanism transplants to D-H, filing the criterion as FE-only")
        print("(RH-blind bin), as pre-registered.")
    print(f"{npass}/{ntot} passed")
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv[1:]))

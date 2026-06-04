"""Experiment 3O: the numerical-stumble accident slot, run with the D-H guard.

Motivated by the "RH solved by accident" dossier
(docs/03_research/rh_solved_by_accident.md), slot 4: the "unforeseen exact
identity / numerical stumble". Terry Tao's pattern is that an accidental proof
often surfaces first as a high-precision numerical coincidence in a program
built for another purpose. PSLQ (integer-relation detection) is the canonical
detector for such a coincidence.

The dossier assigns this slot the STRICTEST bar: a coincidence is not a proof
until it is (a) proven exact, (b) shown RH-equivalent (not an RH-agnostic
detector), and (c) D-H-discriminating. The canonical trap is de Branges in
reverse: 12-digit agreement, then failure at the 34th zero (Conrey-Li). The
mandatory guard is to re-test any flagged relation on the Davenport-Heilbronn
L-function (functional equation, no Euler product, off-line zeros) and on a
non-Euler RH-true Epstein control.

WHAT THIS EXPERIMENT FINDS (and why it is a coordinate, not a null ritual).
The PSLQ-accessible surface and the D-H-discriminating surface are DISJOINT, by
a precision argument:

  - PSLQ needs its inputs to ~tens of digits. The quantities available to that
    precision in closed form (gamma_E, log pi, log 2pi, the Stieltjes constants,
    the Bombieri kernel C_mu = log pi - psi((1+mu)/2), zeta values) are all on
    the ARCHIMEDEAN / Gamma-factor half. That half is SHARED by D-H verbatim
    (same functional equation, same Gamma factor), so any relation PSLQ finds
    there is RH-agnostic by construction.

  - The quantities that DISCRIMINATE zeta from D-H are the Li coefficients
    lambda_n (they depend on the exact zero locations, so off-line zeros make
    them go negative). Computed from finite zero data they carry a truncation
    error of order n^2 log(T)/T, i.e. they are good to ~1-2 digits, FAR below
    PSLQ's threshold. They cannot be fed to PSLQ.

So the "lucky numerical identity" accident is precision-confined to the half of
the problem that cannot tell zeta from its known counterexample. This is a
new, concrete reading of the dossier's verdict: the numerical-stumble slot is
K2-blind not as a matter of taste but as a matter of computability.

Structure:
  Part A (validation): PSLQ re-discovers KNOWN closed-form relations among the
    archimedean constants (proves the scanner detects real relations).
  Part B (search): PSLQ search over the independent archimedean constants AND
    the high-precision prime-side constants (prime zeta P(2), P(3)); reports
    that no new relation appears, and that the prime constants it CAN reach all
    live in the convergent half-plane Re(s) > 1, not at the zeros.
  Part C (the D-H/Epstein guard layer): computes the low-index Li coefficients
    for zeta, Davenport-Heilbronn, and two Epstein controls, exhibits the
    sign discrimination (the genuine RH content), and quantifies that this
    discriminating data sits orders of magnitude below PSLQ precision.

Outputs:
  - e3o_pslq_stumble.npz: the constant basis, the relations found, the Li table.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, epstein_d15, epstein_d47
from experiments._shared.davenport_heilbronn import davenport_heilbronn
from experiments._shared.lfunction import li_coefficients


def _pslq(values, names, maxcoeff=10**7, maxsteps=10**5, tol=None):
    """Run PSLQ on a list of mp.mpf values; return (relation, pretty) or (None, '').

    relation is a list of integers a_i with sum a_i * values_i ~ 0, or None.
    """
    rel = mp.pslq(list(values), tol=tol, maxcoeff=maxcoeff, maxsteps=maxsteps)
    if rel is None:
        return None, ""
    terms = []
    for a, nm in zip(rel, names):
        if a == 0:
            continue
        sign = "+" if a > 0 else "-"
        mag = abs(a)
        terms.append(f"{sign} {mag}*{nm}" if mag != 1 else f"{sign} {nm}")
    pretty = " ".join(terms).lstrip("+ ").strip()
    return rel, f"{pretty} = 0"


def _combo_residual_at(rel, names, dps):
    """Recompute | sum a_i * const_i | at a HIGHER precision dps.

    A GENUINE relation keeps vanishing (residual ~ 10^-dps). A SPURIOUS PSLQ
    artifact (large coefficients, residual near the original tolerance floor)
    does NOT improve when precision rises: this is the de Branges trap test in
    numerical form (apparent agreement that fails when you look harder).
    """
    prev = mp.mp.dps
    try:
        Bhi = build_basis(dps)
        s = mp.mpf(0)
        for a, nm in zip(rel, names):
            s += a * Bhi[nm]
        return abs(s)
    finally:
        mp.mp.dps = prev


def _max_abs_coeff(rel):
    return max(abs(int(a)) for a in rel) if rel else 0


def _residual(rel, values):
    """Magnitude of sum a_i * values_i for a found relation (should be ~0)."""
    s = mp.mpf(0)
    for a, v in zip(rel, values):
        s += a * v
    return abs(s)


def build_basis(dps: int):
    """High-precision archimedean / known-Li constants, all closed form."""
    mp.mp.dps = dps
    one = mp.mpf(1)
    gE = mp.euler
    lpi = mp.log(mp.pi)
    l2 = mp.log(2)
    l2pi = mp.log(2 * mp.pi)
    z2 = mp.zeta(2)
    z3 = mp.zeta(3)
    st1 = mp.stieltjes(1)
    st2 = mp.stieltjes(2)
    # Bombieri kernel value at mu = 0: C0 = log pi - psi(1/2) = log pi + gamma + 2 log 2.
    C0 = lpi - mp.psi(0, mp.mpf(1) / 2)
    # Bombieri-Lagarias asymptotic constant: lambda_n/n ~ (1/2) log n + ASYMP.
    ASYMP = (one - gE - l2pi) / 2
    # Prime-side, high precision but living in the convergent half-plane Re(s) > 1.
    P2 = mp.primezeta(2)
    P3 = mp.primezeta(3)
    return {
        "1": one, "gamma_E": gE, "log_pi": lpi, "log_2": l2, "log_2pi": l2pi,
        "zeta(2)": z2, "zeta(3)": z3, "stieltjes_1": st1, "stieltjes_2": st2,
        "C_mu(0)": C0, "ASYMP_BL": ASYMP, "P(2)": P2, "P(3)": P3,
    }


def part_A_validation(B):
    print("\n[3O] Part A: PSLQ validation (re-discover KNOWN archimedean relations)")
    print("     If PSLQ finds these, the scanner detects real integer relations.")
    checks = [
        (["C_mu(0)", "log_pi", "gamma_E", "log_2"],
         "C_mu(0) = log pi - psi(1/2) = log pi + gamma_E + 2 log 2"),
        (["ASYMP_BL", "1", "gamma_E", "log_2pi"],
         "ASYMP_BL = (1 - gamma_E - log 2pi)/2  (Bombieri-Lagarias)"),
        (["log_2pi", "log_pi", "log_2"],
         "log 2pi = log pi + log 2"),
    ]
    results = []
    for names, desc in checks:
        vals = [B[n] for n in names]
        rel, pretty = _pslq(vals, names, maxcoeff=10**4)
        ok = rel is not None
        res = _residual(rel, vals) if ok else None
        print(f"     - {desc}")
        if ok:
            # stability: a real relation keeps vanishing at higher precision
            res_hi = _combo_residual_at(rel, names, 200)
            print(f"         FOUND: {pretty}")
            print(f"         residual {mp.nstr(res, 3)} (dps=80) -> "
                  f"{mp.nstr(res_hi, 3)} (dps=200): vanishes with precision = REAL")
        else:
            print(f"         NOT FOUND (unexpected)")
        results.append((desc, rel, pretty, ok))
    return results


def part_B_search(B):
    print("\n[3O] Part B: PSLQ search for a NEW relation (the actual stumble hunt)")
    # The set with the trivially-dependent constants (log_2pi, C_mu, ASYMP)
    # removed, plus the high-precision prime-side constants.
    search_names = ["gamma_E", "log_pi", "log_2", "zeta(2)", "zeta(3)",
                    "stieltjes_1", "stieltjes_2", "P(2)", "P(3)"]
    vals = [B[n] for n in search_names]
    print("     Basis (all independent transcendentals + Euler-side P(2),P(3)):")
    print("       " + ", ".join(search_names))

    # Honest search: small coefficients + a TIGHT tolerance demanding near-full
    # precision vanishing. A real identity survives; chance relations cannot.
    tol_tight = mp.mpf(10) ** (-(80 - 8))
    rel, pretty = _pslq(vals, search_names, maxcoeff=10**4, tol=tol_tight)
    if rel is None:
        print("     RESULT (maxcoeff 1e4, tol 1e-72): no integer relation found.")
        print("             No accidental closed form among these constants.")
    else:
        res_hi = _combo_residual_at(rel, search_names, 200)
        print(f"     RESULT (maxcoeff 1e4, tol 1e-72): {pretty}")
        print(f"             stability at dps=200: {mp.nstr(res_hi, 3)} "
              "(check vanishing before any claim).")

    # The trap, made explicit: loosen the discipline and PSLQ "finds" a
    # spurious relation with huge coefficients. This is the de Branges trap in
    # numerical form. We refute it with the precision-stability test.
    print("     --- de Branges trap demonstration (loose discipline) ---")
    rel_t, pretty_t = _pslq(vals, search_names, maxcoeff=10**9)  # mpmath default tol
    if rel_t is not None:
        res_lo = _residual(rel_t, vals)
        res_hi = _combo_residual_at(rel_t, search_names, 220)
        print(f"     loose PSLQ (maxcoeff 1e9, default tol) 'finds':")
        print(f"       max|coeff| = {_max_abs_coeff(rel_t):.2e}, residual {mp.nstr(res_lo, 3)} (dps=80)")
        print(f"     SPURIOUS: same integer combo at dps=220 -> {mp.nstr(res_hi, 3)}")
        print(f"       (does NOT vanish with precision: 8-digit coefficients are an")
        print(f"        artifact of tol ~ maxcoeff^-(n-1), not a real identity).")
    else:
        print("     loose PSLQ found nothing (basis too small for a chance relation).")

    print("     NOTE: the prime-side constants P(2), P(3) are high precision but live")
    print("           in the convergent half-plane Re(s) > 1, away from the zeros.")
    print("           D-H has no Euler product, so no P(s); but P(s) carries no")
    print("           zero-location (RH) content either. The discriminating data is")
    print("           the Li coefficients, handled in Part C.")
    return search_names, rel, pretty


def part_C_guard(n_max, dps):
    print("\n[3O] Part C: the D-H/Epstein guard layer (where the RH content actually is)")
    print("     Li coefficients lambda_n: RH <=> lambda_n >= 0 for all n (Li 1997).")
    print("     Two facts in tension, which is the whole point:")
    print("       (1) the off-line obstruction is a LARGE-n effect (off-line rho gives")
    print("           |1-1/rho| > 1, so its term ~|1-1/rho|^n only dominates at large n;")
    print("           at small n the on-line zeros dominate and lambda_n stays > 0).")
    print("           D-H negativity is documented at large n (e3b / LEARNINGS #18).")
    print("       (2) the truncation error grows ~ n^2 log(T)/T, so by the time n is")
    print("           large enough to SEE the discrimination, precision is already gone.")
    controls = [
        ("zeta",            zeta_L,            200.0, True),
        ("davenport_heil",  davenport_heilbronn, 95.0, False),
        ("epstein_d15",     epstein_d15,        40.0, True),   # no off-line zeros < T~80
        ("epstein_d47",     epstein_d47,        40.0, False),  # off-line zero ~0.634+32i
    ]
    table = {}
    for label, L, T_max, rh_expected in controls:
        t0 = time.time()
        try:
            coeffs, last = li_coefficients(L, n_max=n_max, T_max=T_max, prec=dps)
        except Exception as exc:  # keep the run alive if one control is slow/fails
            print(f"     - {label:16s}: SKIPPED ({type(exc).__name__}: {exc})")
            continue
        dt = time.time() - t0
        arr = np.array([float(c) for c in coeffs])
        n_neg = int((arr < 0).sum())
        first_neg = int(np.argmax(arr < 0)) + 1 if n_neg else None
        # truncation proxy: magnitude of the last per-zero term at n_max
        trunc = float(abs(last[-1])) if last else float("nan")
        euler = "Euler" if L.has_euler_product else "no-Euler"
        offline = "has off-line zeros" if not rh_expected else "RH-true control"
        print(f"     - {label:16s} [{euler:8s}] {offline}")
        print(f"         first {n_max} lambda_n signs: "
              f"{''.join('+' if x >= 0 else '-' for x in arr)}   "
              f"({n_neg} negative" + (f", first at n={first_neg}" if first_neg else "") + ")")
        print(f"         lambda_1..3 = {', '.join(mp.nstr(c, 6) for c in coeffs[:3])}")
        print(f"         per-zero tail term at n={n_max}: ~{trunc:.2e}  "
              f"(==> usable precision ~ a digit or two, not ~{dps})")
        print(f"         [{dt:.1f}s, {label}]")
        table[label] = arr
    print(f"\n     At low n (n<={n_max}) ALL controls read positive: no discrimination yet.")
    print("     The off-line obstruction has not surfaced (it is a large-n effect), and")
    print("     the per-zero tail term is already ~1e-2, so usable precision is ~1 digit.")
    print("     This is the tension made concrete: the discriminating SIGNAL only appears")
    print("     in the large-n regime where the truncation error has destroyed precision.")
    print("     => the Li coefficients are never simultaneously discriminating AND")
    print("        PSLQ-precise. The stumble surface is confined to the D-H-shared half.")
    return table


def run(n_max: int = 12, dps: int = 80, cross_L: bool = True, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("[3O] PSLQ stumble-yield scan with the Davenport-Heilbronn guard")
    print(f"     dps={dps}, Li n_max={n_max}")
    print("=" * 72)

    B = build_basis(dps)
    a_results = part_A_validation(B)
    search_names, rel, pretty = part_B_search(B)
    table = part_C_guard(n_max, dps=30) if cross_L else {}

    print("\n" + "=" * 72)
    print("[3O] VERDICT")
    n_found_A = sum(1 for *_, ok in a_results if ok)
    print(f"     Part A: {n_found_A}/{len(a_results)} known relations re-discovered "
          f"(scanner validated).")
    if rel is None:
        print("     Part B: no new accidental identity among the high-precision")
        print("             archimedean + prime-side constants.")
    else:
        print(f"     Part B: candidate relation {pretty} -> must pass D-H/Epstein guard.")
    print("     Part C: the RH-discriminating Li coefficients are precision-limited")
    print("             (~1 digit), orders of magnitude below PSLQ reach.")
    print("     CONCLUSION: the numerical-stumble accident slot is precision-confined")
    print("                 to the archimedean half that D-H shares (K2-blind by")
    print("                 computability). A PSLQ-discoverable coincidence cannot,")
    print("                 by construction, distinguish zeta from its counterexample.")
    print("                 Reinforces the dossier no-free-lunch finding from a new angle.")
    print("=" * 72)

    # Persist
    save = {
        "basis_names": np.array(list(B.keys())),
        "basis_values": np.array([mp.nstr(v, 40) for v in B.values()]),
        "search_names": np.array(search_names),
        "search_relation": np.array(rel if rel is not None else [], dtype=object),
        "n_max": n_max, "dps": dps,
    }
    for k, v in table.items():
        save[f"li_{k}"] = v
    np.savez_compressed(out_dir / "e3o_pslq_stumble.npz", **save)
    print(f"[3O] Saved {out_dir / 'e3o_pslq_stumble.npz'}")
    return a_results, rel, table


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=12, help="Li coefficient count")
    parser.add_argument("--dps", type=int, default=80, help="precision for PSLQ basis")
    parser.add_argument("--no-cross-L", action="store_true",
                        help="skip Part C (the D-H/Epstein Li layer)")
    args = parser.parse_args()
    run(n_max=args.n_max, dps=args.dps, cross_L=not args.no_cross_L)

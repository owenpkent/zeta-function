"""Experiment 2F: Hodge-index positivity sweep across curves over finite fields.

This is experiment C in the Architecture-2 thread. It makes the function-field
Riemann hypothesis CONCRETE and QUANTITATIVE across a family of smooth
projective curves over finite fields, as a numerical model of the "target" that
an analogous Spec(Z) construction would have to hit.

## The architectural point

For a smooth projective curve C of genus g over F_q, RH is a THEOREM (Weil
1948, via the Hodge index theorem on the surface C x C). The zeta function is

    Z_C(T) = P(T) / ((1 - T)(1 - q T)),
    P(T) = prod_{i=1}^{2g} (1 - alpha_i T),

an integer polynomial of degree 2g, and the Weil RH states that every Frobenius
eigenvalue obeys |alpha_i| = sqrt(q) EXACTLY. The positivity that forces this is
the Hodge index theorem: the intersection form on the Neron-Severi space of
C x C is negative definite on the primitive part. That negative-definiteness is
the same structural object the project calls "Weil positivity," and it lives at
the project's Level 4.

The point of this experiment: in the function-field world the positivity is
AVAILABLE (the Hodge index theorem is a theorem), so the RH bound holds exactly
and we can exhibit it. This is the target the geometric route must reproduce
over Spec(Z). Here it is, exact and concrete, in the world where the Hodge
index theorem exists. The Spec(Z) lift (Architecture 2) is stuck precisely
because no analogue of that surface or that index theorem has been built.

## What is computed, per curve

  1. Point counts N_k = #C(F_{q^k}) for k = 1..2g, by brute force over the
     affine model plus the points at infinity. F_{q^k} is built as
     F_q[t] / (irreducible g_k), reusing the prime-field-plus-extension
     machinery validated in e2b.

  2. The zeta polynomial P(T). From log Z = sum_k N_k T^k / k and
     Z(T) (1 - T)(1 - q T) = P(T), we recover the 2g integer coefficients of
     P(T) by exact power-series arithmetic in sympy (no floating point).

  3. The Frobenius eigenvalues alpha_i = reciprocal roots of P(T), i.e. roots of
     the reversed polynomial T^{2g} P(1/T). We VERIFY |alpha_i| = sqrt(q) to
     root-finding precision and report max_i | |alpha_i| - sqrt(q) |. This is the
     function-field RH; it is a theorem and MUST hold up to numerical error.

  4. The positivity / pairing structure. The functional equation pairs
     eigenvalues as (alpha, q/alpha); on the Weil circle |alpha| = sqrt(q) this
     is exactly complex conjugation, so eigenvalues come in conjugate pairs on
     |z| = sqrt(q). We write alpha_i = sqrt(q) e^{i theta_i} and report the
     angles theta_i. Their distribution (over the whole family) is the
     computable shadow of the Sato-Tate / equidistribution content that the
     Hodge-index positivity underwrites.

## The sweep

Default (smoke) sweep: elliptic curves (g = 1) y^2 = x^3 + a x + b over a small
set of primes. The --full flag expands to more primes and to genus-2
hyperelliptic curves y^2 = f(x) with deg f in {5, 6}, which require counting up
to F_{q^4}; q is kept small (<= 13) so q^4 stays brute-forceable.

## Headline deliverable

Across the WHOLE family the bound |alpha_i| = sqrt(q) holds exactly. The
experiment tabulates the eigenvalue angles, exhibiting concretely the positivity
that a Spec(Z) lift would need to reproduce.

Outputs:
  - e2f_hodge_index_sweep.npz : per-curve P-coefficients, deviations, angles
  - e2f_hodge_index_sweep.png : 4-panel summary
  - stdout : per-curve table
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Finite-field arithmetic (F_{q^k} for q = p prime, built as F_p[t]/(g_k)).
#
# Reuses the validated prime-field point-count strategy from e2b: at k = 1 we
# count directly over F_p; for k > 1 we construct an irreducible polynomial of
# degree k over F_p and represent F_{p^k} elements as polynomials of degree < k.
# Curves are now general hyperelliptic y^2 = f(x), so the only change from e2b
# is that the right-hand side is an arbitrary polynomial f rather than the fixed
# cubic x^3 + a x + b.
# ---------------------------------------------------------------------------


def _poly_eval_int_Fp(f_coeffs, x: int, p: int) -> int:
    """Evaluate the integer-coefficient polynomial f (low-order first) at the
    F_p element x (a plain int), returning the result in F_p."""
    acc = 0
    for c in reversed(f_coeffs):
        acc = (acc * x + c) % p
    return acc


def count_points_Fp(f_coeffs, p: int) -> int:
    """#C(F_p) for the smooth model of y^2 = f(x), f given as integer
    coefficients low-order first.

    Counts affine points then adds the points at infinity. For deg f odd there
    is one point at infinity; for deg f even there are two if the leading
    coefficient is a square in F_p, else zero. (Standard smooth-model count for
    a hyperelliptic curve; for deg f = 3 this reduces to the elliptic-curve
    count of e2b.)
    """
    deg = len(f_coeffs) - 1
    count = 0
    for x in range(p):
        rhs = _poly_eval_int_Fp(f_coeffs, x, p)
        if rhs == 0:
            count += 1
        elif pow(rhs, (p - 1) // 2, p) == 1:
            count += 2
    count += _points_at_infinity(f_coeffs, p, k=1)
    return count


def count_points_Fpk(f_coeffs, p: int, k: int):
    """#C(F_{p^k}) for the smooth model of y^2 = f(x).

    For k = 1 delegates to count_points_Fp. For k > 1 builds F_{p^k} and
    enumerates all p^k values of x.
    """
    if k == 1:
        return count_points_Fp(f_coeffs, p)

    g = _find_irreducible_poly(p, k)
    order_field = p ** k
    half = (order_field - 1) // 2
    # Reduce the integer coefficients of f mod p once.
    f_mod = [c % p for c in f_coeffs]
    count = 0
    for x_int in range(order_field):
        x = _int_to_poly(x_int, p, k)
        rhs = _poly_eval_field(f_mod, x, g, p)
        if all(c == 0 for c in rhs):
            count += 1
        else:
            rhs_pow = _poly_pow_mod(rhs, half, g, p)
            if all(c == 0 for c in _poly_add_const(rhs_pow, -1, p)):
                count += 2
    count += _points_at_infinity(f_coeffs, p, k)
    return count


def _points_at_infinity(f_coeffs, p: int, k: int) -> int:
    """Number of points at infinity on the smooth model of y^2 = f(x) over
    F_{p^k}. deg odd -> 1; deg even -> 2 if leading coeff is a square in
    F_{p^k}, else 0."""
    deg = len(f_coeffs) - 1
    if deg % 2 == 1:
        return 1
    lead = f_coeffs[-1] % p
    order_field = p ** k
    # lead lives in the prime field F_p, but "square in F_{p^k}" is the right
    # test. An element of F_p is a square in F_{p^k} iff lead^{(p^k-1)/2} = 1,
    # which we evaluate via integer modular exponentiation lifted to F_{p^k}:
    # since lead is in the prime subfield, lead^{(p^k-1)/2} mod p equals the
    # constant term, and the result is +1 or -1 in F_p.
    if lead == 0:
        return 0
    res = pow(lead, (order_field - 1) // 2, p)
    return 2 if res == 1 else 0


# --- polynomial-over-F_p helpers (lists low-order first), as in e2b ---


def _find_irreducible_poly(p: int, k: int):
    from itertools import product
    for tail in product(range(p), repeat=k):
        f = list(tail) + [1]
        if _is_irreducible(f, p):
            return f
    raise RuntimeError(f"No irreducible polynomial of degree {k} over F_{p}?")


def _is_irreducible(f, p):
    k = len(f) - 1
    if k <= 0:
        return False
    from sympy import factorint
    for q in factorint(k).keys():
        d = k // q
        x_pd = _poly_pow_mod([0, 1], p ** d, f, p)
        diff = _poly_sub(x_pd, [0, 1], p)
        if _poly_gcd(diff, f, p) != [1]:
            return False
    x_pk = _poly_pow_mod([0, 1], p ** k, f, p)
    diff = _poly_sub(x_pk, [0, 1], p)
    return all(c == 0 for c in diff)


def _poly_eval_field(f_mod, x, g, p):
    """Evaluate the F_p-coefficient polynomial f_mod at the F_{p^k} element x
    (a poly mod g), by Horner in F_{p^k}."""
    acc = [0]
    for c in reversed(f_mod):
        acc = _poly_mul_mod(acc, x, g, p)
        acc = _poly_add_const(acc, c, p)
    return acc


def _poly_pow_mod(base, n, f, p):
    result = [1]
    cur = list(base)
    while n > 0:
        if n & 1:
            result = _poly_mul_mod(result, cur, f, p)
        cur = _poly_mul_mod(cur, cur, f, p)
        n >>= 1
    return result


def _poly_mul_mod(a, b, f, p):
    prod = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            prod[i + j] = (prod[i + j] + ai * bj) % p
    return _poly_reduce(prod, f, p)


def _poly_reduce(a, f, p):
    a = list(a)
    deg_f = len(f) - 1
    while len(a) - 1 >= deg_f:
        top_idx = len(a) - 1
        top = a[top_idx]
        if top == 0:
            a.pop()
            continue
        for i in range(deg_f + 1):
            idx = top_idx - deg_f + i
            a[idx] = (a[idx] - top * f[i]) % p
        a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a if a else [0]


def _poly_sub(a, b, p):
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out.append((ai - bi) % p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_add_const(a, c, p):
    out = list(a)
    out[0] = (out[0] + c) % p
    return out


def _poly_gcd(a, b, p):
    while any(c != 0 for c in b):
        a, b = b, _poly_mod(a, b, p)
    return _poly_make_monic(a, p)


def _poly_mod(a, b, p):
    a = list(a)
    deg_b = len(b) - 1
    while len(a) > deg_b:
        if a[-1] == 0:
            a.pop()
            continue
        lead_b_inv = pow(b[-1], -1, p)
        top = (a[-1] * lead_b_inv) % p
        deg_top = len(a)
        for i, bi in enumerate(b):
            idx = deg_top - 1 - deg_b + i
            a[idx] = (a[idx] - top * bi) % p
        a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a if a else [0]


def _poly_make_monic(a, p):
    if all(c == 0 for c in a):
        return [0]
    lead_inv = pow(a[-1], -1, p)
    return [(c * lead_inv) % p for c in a]


def _int_to_poly(x, p, k):
    out = []
    for _ in range(k):
        out.append(x % p)
        x //= p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out if out else [0]


# ---------------------------------------------------------------------------
# Zeta polynomial recovery and eigenvalue analysis.
# ---------------------------------------------------------------------------


def zeta_polynomial(N_k, p: int, g: int):
    """Recover P(T) (sympy Poly in T, integer coefficients, degree 2g) from
    the point counts N_k, k = 1..2g.

    Uses log Z = sum_{k>=1} N_k T^k / k, so
        Z(T) = exp(sum_{k=1}^{2g} N_k T^k / k)  mod T^{2g+1},
    and P(T) = Z(T) * (1 - T)(1 - q T)  truncated to degree 2g. Everything is
    done as exact rational power series in sympy; the resulting coefficients are
    integers (a theorem), which we verify.
    """
    T = sp.symbols("T")
    deg = 2 * g
    # log Z truncated to order deg.
    logZ = sum(sp.Rational(N_k[k - 1], k) * T ** k for k in range(1, deg + 1))
    # exp of the series, truncated to T^deg.
    Z = sp.series(sp.exp(logZ), T, 0, deg + 1).removeO()
    Z = sp.expand(Z)
    P_full = sp.expand(Z * (1 - T) * (1 - p * T))
    P_poly = sp.Poly(P_full, T)
    # Truncate to degree 2g (higher terms are series-truncation artifacts).
    coeffs_low_first = [P_poly.coeff_monomial(T ** j) for j in range(deg + 1)]
    # All should be integers; verify and coerce.
    int_coeffs = []
    for c in coeffs_low_first:
        c_simpl = sp.nsimplify(c)
        if not c_simpl.is_integer:
            raise ValueError(f"Non-integer P(T) coefficient {c_simpl}; "
                             f"check point counts N_k={N_k}, p={p}, g={g}")
        int_coeffs.append(int(c_simpl))
    P = sp.Poly(list(reversed(int_coeffs)), T)  # Poly wants high-order first
    return P, int_coeffs


def frobenius_eigenvalues(int_coeffs, prec: int = 40):
    """Frobenius eigenvalues = reciprocal roots of P(T) = roots of the reversed
    polynomial sum_j P_j T^{2g-j}. Computed with mpmath.polyroots at high
    precision."""
    mp.mp.dps = prec
    deg = len(int_coeffs) - 1
    # Reversed polynomial coefficients high-order first: reversed P has
    # coefficient P_j at T^{deg-j}, i.e. coeffs high-order first = int_coeffs.
    rev_high_first = [mp.mpf(c) for c in int_coeffs]
    roots = mp.polyroots(rev_high_first, maxsteps=200, extraprec=4 * prec)
    return [complex(r) for r in roots]


# ---------------------------------------------------------------------------
# Curve family.
# ---------------------------------------------------------------------------


def is_smooth_hyperelliptic(f_coeffs, p: int) -> bool:
    """f squarefree mod p (smooth affine model). Uses gcd(f, f') = 1 over F_p."""
    f = [c % p for c in f_coeffs]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    if len(f) <= 1:
        return False
    fp = [(j * f[j]) % p for j in range(1, len(f))]
    while len(fp) > 1 and fp[-1] == 0:
        fp.pop()
    if fp == [0]:
        return False
    return _poly_gcd(f, fp, p) == [1]


def elliptic_family(primes):
    """Elliptic curves y^2 = x^3 + a x + b over F_p, one nonsingular pick per
    prime (smallest (a, b) with nonzero discriminant)."""
    fam = []
    for p in primes:
        chosen = None
        for a in range(p):
            for b in range(p):
                # discriminant of x^3 + a x + b is -16(4a^3 + 27 b^2)
                if (4 * a ** 3 + 27 * b ** 2) % p != 0:
                    chosen = (a, b)
                    break
            if chosen:
                break
        a, b = chosen
        fam.append({
            "p": p, "g": 1,
            "f_coeffs": [b, a, 0, 1],  # b + a x + 0 x^2 + x^3
            "label": f"y^2=x^3+{a}x+{b} /F_{p}",
        })
    return fam


def genus2_family(primes):
    """Genus-2 hyperelliptic curves y^2 = f(x), deg f in {5, 6}, smooth model.
    One smooth pick per prime, searching a small set of candidate f."""
    fam = []
    # Candidate quintics/sextics (integer coeffs, low-order first).
    candidates = [
        [1, 0, 0, 0, 0, 1],        # x^5 + 1
        [1, 1, 0, 0, 0, 1],        # x^5 + x + 1
        [-1, 0, 0, 0, 0, 1],       # x^5 - 1
        [1, 0, 0, 0, 0, 0, 1],     # x^6 + 1
        [2, 0, 1, 0, 0, 1],        # x^5 + x^2 + 2
    ]
    for p in primes:
        chosen = None
        for f in candidates:
            if is_smooth_hyperelliptic(f, p):
                chosen = f
                break
        if chosen is None:
            continue
        deg = len(chosen) - 1
        fam.append({
            "p": p, "g": 2,
            "f_coeffs": chosen,
            "label": f"y^2=f(x) deg{deg} /F_{p}  f={chosen}",
        })
    return fam


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------


def analyze_curve(curve, prec: int = 40):
    """Full per-curve pipeline: count, recover P(T), eigenvalues, RH check."""
    p, g, f_coeffs = curve["p"], curve["g"], curve["f_coeffs"]
    deg = 2 * g
    N_k = [count_points_Fpk(f_coeffs, p, k) for k in range(1, deg + 1)]
    P, int_coeffs = zeta_polynomial(N_k, p, g)
    eigs = frobenius_eigenvalues(int_coeffs, prec=prec)
    sqrt_q = np.sqrt(p)
    moduli = np.array([abs(z) for z in eigs])
    max_dev = float(np.max(np.abs(moduli - sqrt_q)))
    angles = np.array([np.angle(z) for z in eigs])
    # Functional-equation sanity: constant term of P is q^g (P(0)=1, leading=q^g)
    fe_ok = (int_coeffs[-1] == p ** g)
    return {
        "p": p, "g": g, "label": curve["label"],
        "f_coeffs": f_coeffs,
        "N_k": N_k,
        "P_coeffs": int_coeffs,
        "eigs": eigs,
        "moduli": moduli,
        "angles": angles,
        "sqrt_q": float(sqrt_q),
        "max_dev": max_dev,
        "fe_ok": bool(fe_ok),
    }


def run(
    primes_elliptic=(5, 7),
    primes_genus2=(),
    full: bool = False,
    prec: int = 40,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    if full:
        primes_elliptic = (5, 7, 11, 13, 17, 19, 23)
        primes_genus2 = (5, 7, 11, 13)

    t_start = time.time()

    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))

    print("[2F] Hodge-index positivity sweep across curves over finite fields.")
    print("[2F] Function-field RH (a theorem via the Hodge index theorem on")
    print("     C x C): every Frobenius eigenvalue has |alpha_i| = sqrt(q).")
    print("     This is the target a Spec(Z) lift would need to reproduce.\n")
    print(f"[2F] {len(curves)} curves; prec = {prec} digits.\n")

    header = (f"{'curve':<34} {'g':>2} {'q':>3} {'P(T) coeffs (low->high)':<28} "
              f"{'max||a|-sqrt q|':>15} {'angles theta_i (rad)':<30}")
    print(header)
    print("-" * len(header))

    results = []
    rh_all = True
    worst_dev = 0.0
    for curve in curves:
        res = analyze_curve(curve, prec=prec)
        results.append(res)
        worst_dev = max(worst_dev, res["max_dev"])
        rh_ok = res["max_dev"] < 1e-9 and res["fe_ok"]
        rh_all = rh_all and rh_ok
        ang_str = ", ".join(f"{a:+.4f}" for a in sorted(res["angles"]))
        pc_str = str(res["P_coeffs"])
        print(f"{res['label']:<34} {res['g']:>2} {res['p']:>3} {pc_str:<28} "
              f"{res['max_dev']:>15.3e} [{ang_str}]")

    print("-" * len(header))
    print(f"\n[2F] Worst eigenvalue-modulus deviation across family: {worst_dev:.3e}")
    print(f"[2F] Function-field RH |alpha_i| = sqrt(q) holds for ALL curves "
          f"(tol 1e-9): {rh_all}")
    print(f"[2F] (This is a theorem; numerical agreement confirms the pipeline.)")
    print(f"[2F] Elapsed: {time.time() - t_start:.1f}s")

    _save_and_plot(results, out_dir)
    return results, rh_all, worst_dev


def _save_and_plot(results, out_dir: Path):
    # --- npz ---
    save = {
        "n_curves": len(results),
        "labels": np.array([r["label"] for r in results], dtype=object),
        "worst_dev": float(max(r["max_dev"] for r in results)),
    }
    for i, r in enumerate(results):
        save[f"c{i}_p"] = r["p"]
        save[f"c{i}_g"] = r["g"]
        save[f"c{i}_f_coeffs"] = np.array(r["f_coeffs"])
        save[f"c{i}_N_k"] = np.array(r["N_k"])
        save[f"c{i}_P_coeffs"] = np.array(r["P_coeffs"])
        save[f"c{i}_eigs"] = np.array(r["eigs"])
        save[f"c{i}_moduli"] = r["moduli"]
        save[f"c{i}_angles"] = r["angles"]
        save[f"c{i}_sqrt_q"] = r["sqrt_q"]
        save[f"c{i}_max_dev"] = r["max_dev"]
    np.savez_compressed(out_dir / "e2f_hodge_index_sweep.npz", **save)

    # --- plot: 4 panels ---
    fig, axs = plt.subplots(2, 2, figsize=(13, 10))

    # Panel 1: all eigenvalues in the complex plane, scaled by 1/sqrt(q) so the
    # Weil circle becomes the unit circle and every curve overlays.
    ax = axs[0, 0]
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), "k--", lw=1, label=r"$|z|=\sqrt{q}$ (unit after scaling)")
    cmap = plt.get_cmap("viridis")
    n = len(results)
    for i, r in enumerate(results):
        z = np.array(r["eigs"]) / r["sqrt_q"]
        ax.scatter(z.real, z.imag, s=40, color=cmap(i / max(n - 1, 1)),
                   alpha=0.8, edgecolors="k", linewidths=0.3)
    ax.axhline(0, color="gray", lw=0.4); ax.axvline(0, color="gray", lw=0.4)
    ax.set_aspect("equal")
    ax.set_xlabel(r"Re$(\alpha / \sqrt{q})$"); ax.set_ylabel(r"Im$(\alpha / \sqrt{q})$")
    ax.set_title("Frobenius eigenvalues, scaled by $1/\\sqrt{q}$\n(all on the unit circle: Weil RH)")
    ax.legend(loc="upper right", fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: max modulus deviation per curve (the RH-bound residual).
    ax = axs[0, 1]
    devs = [r["max_dev"] for r in results]
    idx = np.arange(len(results))
    ax.bar(idx, np.maximum(devs, 1e-18), color="tab:blue")
    ax.set_yscale("log")
    ax.axhline(1e-9, color="r", ls="--", label="tol 1e-9")
    ax.set_xlabel("curve index")
    ax.set_ylabel(r"$\max_i\,||\alpha_i|-\sqrt{q}|$")
    ax.set_title("RH-bound residual per curve\n(theorem: should be root-finding noise)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # Panel 3: distribution of eigenvalue angles theta_i over the whole family.
    ax = axs[1, 0]
    all_angles = np.concatenate([r["angles"] for r in results])
    ax.hist(all_angles, bins=24, range=(-np.pi, np.pi), color="tab:green",
            edgecolor="k", alpha=0.8)
    ax.set_xlabel(r"$\theta_i$ where $\alpha_i=\sqrt{q}\,e^{i\theta_i}$")
    ax.set_ylabel("count")
    ax.set_title("Angle distribution across the family\n(conjugate pairs; Sato-Tate shadow)")
    ax.grid(alpha=0.3)

    # Panel 4: point counts vs q^k + 1 baseline, per curve (Weil deviation).
    ax = axs[1, 1]
    for i, r in enumerate(results):
        ks = np.arange(1, len(r["N_k"]) + 1)
        baseline = np.array([r["p"] ** k + 1 for k in ks])
        dev = np.abs(baseline - np.array(r["N_k"]))
        bound = 2 * r["g"] * np.array([r["p"] ** (k / 2.0) for k in ks])
        ax.plot(ks, np.maximum(dev, 1e-9), "o-", color=cmap(i / max(n - 1, 1)), alpha=0.6)
        ax.plot(ks, bound, "--", color=cmap(i / max(n - 1, 1)), alpha=0.4)
    ax.set_yscale("log")
    ax.set_xlabel("k")
    ax.set_ylabel(r"$|q^k+1-N_k|$ (solid), Weil bound $2g\sqrt{q^k}$ (dashed)")
    ax.set_title("Point-count deviation vs Weil bound")
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e2f_hodge_index_sweep.png", dpi=140)
    plt.close()
    print(f"\n[2F] Saved {out_dir / 'e2f_hodge_index_sweep.png'}")
    print(f"[2F] Saved {out_dir / 'e2f_hodge_index_sweep.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hodge-index positivity sweep over curves /F_q.")
    parser.add_argument("--full", action="store_true",
                        help="Expand the sweep to more primes and genus-2 curves (heavy).")
    parser.add_argument("--primes-elliptic", type=int, nargs="+", default=[5, 7],
                        help="Primes for the genus-1 elliptic family (smoke default 5 7).")
    parser.add_argument("--primes-genus2", type=int, nargs="+", default=[],
                        help="Primes for the genus-2 hyperelliptic family (default none).")
    parser.add_argument("--prec", type=int, default=40, help="mpmath precision (digits).")
    args = parser.parse_args()
    run(
        primes_elliptic=tuple(args.primes_elliptic),
        primes_genus2=tuple(args.primes_genus2),
        full=args.full,
        prec=args.prec,
    )

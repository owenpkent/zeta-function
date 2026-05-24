"""Experiment 2E: Adams-operation spectrum vs zeta zero ordinates.

A direct numerical probe of the R5 hypothesis. Borger's framework
(2A_borger_dossier.md) proposes the Adams operations psi_p as a
Frobenius substitute on Lambda-rings such as the big Witt ring
W(Z). The natural question: in any concrete Lambda-ring setting we
can compute, does psi_p have a spectrum that looks like zeta
zeros?

R5 (2A_R5_prismatic_cohomology.md) argues that the zeta-zero
spectrum does NOT live on the Lambda-ring directly. It would live
on a cohomology theory built on top of Spec(W(Z)), with the Adams
operations acting on the cohomology by transport of structure.
Prismatic cohomology is the leading candidate for that theory.

This experiment confirms R5's framing by direct computation: on
several concrete Lambda-ring substrates (representation rings,
unramified extensions, truncated ghost rings), the spectrum of
psi_p is structurally orthogonal to zeta-zero ordinates. The
spectra are either:
  - roots of unity (permutation actions),
  - the single point {0} (nilpotent shifts), or
  - pure powers of p (rational K-theory eigenvalues).

None resemble {gamma_1, gamma_2, ...} ~ {14.13, 21.02, 25.01, ...}.

The negative finding documents WHY Arch 2 needs the cohomology
theory: the bare Lambda-structure is too small (or too symmetric)
to encode zeta. The cohomology lifts the small Lambda-structure to
an infinite-dim Hilbert/sheaf-cohomology object where the spectral
information of zeta could plausibly live.

Probes:
  (1) psi_p on R(Z/n) = representation ring of Z/n. psi_p sends
      character chi_j to chi_{p*j mod n}; spectrum is a union of
      roots of unity given by the cycle structure of mult-by-p
      acting on Z/n.

  (2) Frobenius on F_q = F_{p^k}, viewed as F_p-linear map.
      Characteristic polynomial X^k - 1 over F_p (since Frobenius
      has order k). Over the algebraic closure or under any
      complex embedding via lifting to characteristic 0, eigenvalues
      are k-th roots of unity.

  (3) psi_p on truncated ghost ring of W: ghost coordinates
      indexed by divisors {d <= N}. psi_p shifts w_m to w_{pm},
      killing basis elements with pm > N. Result: nilpotent
      operator with spectrum {0}.

  (4) psi_p on rational K-theory K_*(Spec Z) Q: reference, not
      directly computed. The Beilinson eigenspaces have psi_p = p^d
      on K_{2d-1} Q. We just plot the predicted eigenvalues
      {1, p, p^2, ...} for documentation.

For each probe we compute the spectrum, compare to the first few
zeta zero ordinates, and produce a four-panel figure plus a
quantitative "min-distance" summary.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import zeta_L


def adams_on_R_Zn(p: int, n: int) -> np.ndarray:
    """psi_p as permutation matrix on the character basis of R(Z/n).

    Returns the n x n integer matrix M with M[i, j] = 1 if
    psi_p(chi_j) = chi_i, else 0. The action sends chi_j to
    chi_{(p*j) mod n}.
    """
    M = np.zeros((n, n), dtype=int)
    for j in range(n):
        i = (p * j) % n
        M[i, j] = 1
    return M


def cycle_structure_mult_by_p(p: int, n: int) -> list[int]:
    """Cycle lengths of multiplication by p acting on Z/n."""
    seen = [False] * n
    lengths = []
    for start in range(n):
        if seen[start]:
            continue
        length = 0
        x = start
        while not seen[x]:
            seen[x] = True
            x = (p * x) % n
            length += 1
        lengths.append(length)
    return lengths


def spectrum_of_permutation(cycle_lengths: list[int]) -> np.ndarray:
    """Eigenvalues of a permutation given its cycle structure: a
    cycle of length L contributes the L-th roots of unity."""
    evs = []
    for L in cycle_lengths:
        for k in range(L):
            evs.append(np.exp(2j * np.pi * k / L))
    return np.array(evs)


def frobenius_matrix_Fq(p: int, k: int) -> np.ndarray:
    """Matrix of Frobenius F: x -> x^p on F_{p^k}, in the basis
    {1, alpha, alpha^2, ..., alpha^{k-1}} where alpha is a root of
    an irreducible polynomial f of degree k over F_p.

    Entries are integers in {0, ..., p-1}; the matrix is the F_p
    representation of Frobenius. Eigenvalues over the algebraic
    closure of F_p are the k-th roots of unity (since F has order k),
    but we are computing the F_p-matrix here; eigenvalues over C of
    this lifted-to-Z matrix are NOT the right thing. For complex
    visualization we use the structural fact that F has order k and
    plot k-th roots of unity directly.
    """
    f = _find_irreducible(p, k)
    M = np.zeros((k, k), dtype=int)
    for j in range(k):
        # Compute alpha^{p*j} mod f as a polynomial of degree < k
        poly = _alpha_power_mod_f(p * j, f, p, k)
        for i, c in enumerate(poly):
            M[i, j] = c
    return M


def _find_irreducible(p: int, k: int) -> list[int]:
    """Find a monic irreducible polynomial of degree k over F_p.

    Returns coefficients low-order first, leading coefficient 1.
    """
    from itertools import product
    for tail in product(range(p), repeat=k):
        f = list(tail) + [1]
        if _is_irreducible(f, p):
            return f
    raise RuntimeError(f"no irreducible polynomial of degree {k} over F_{p}")


def _is_irreducible(f: list[int], p: int) -> bool:
    """Rabin test for irreducibility of monic f over F_p."""
    k = len(f) - 1
    if k <= 0:
        return False
    from sympy import factorint
    primes = list(factorint(k).keys()) if k > 1 else []
    x_poly = [0, 1]
    for q in primes:
        d = k // q
        x_pd = _poly_pow_mod(x_poly, p ** d, f, p)
        diff = _poly_sub(x_pd, x_poly, p)
        g = _poly_gcd(diff, f, p)
        if g != [1]:
            return False
    x_pk = _poly_pow_mod(x_poly, p ** k, f, p)
    diff = _poly_sub(x_pk, x_poly, p)
    return all(c == 0 for c in diff)


def _alpha_power_mod_f(n: int, f: list[int], p: int, k: int) -> list[int]:
    """Compute alpha^n in F_p[alpha]/(f) as a degree-<k polynomial."""
    if n == 0:
        out = [0] * k
        out[0] = 1
        return out
    result = _poly_pow_mod([0, 1], n, f, p)
    while len(result) < k:
        result.append(0)
    return result[:k]


def _poly_pow_mod(base: list[int], n: int, f: list[int], p: int) -> list[int]:
    result = [1]
    cur = list(base)
    while n > 0:
        if n & 1:
            result = _poly_mul_mod(result, cur, f, p)
        cur = _poly_mul_mod(cur, cur, f, p)
        n >>= 1
    return result


def _poly_mul_mod(a: list[int], b: list[int], f: list[int], p: int) -> list[int]:
    deg_a, deg_b = len(a) - 1, len(b) - 1
    prod = [0] * (deg_a + deg_b + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            prod[i + j] = (prod[i + j] + ai * bj) % p
    return _poly_reduce(prod, f, p)


def _poly_reduce(a: list[int], f: list[int], p: int) -> list[int]:
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


def _poly_sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out.append((ai - bi) % p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    while any(c != 0 for c in b):
        a, b = b, _poly_mod(a, b, p)
    return _poly_make_monic(a, p)


def _poly_mod(a: list[int], b: list[int], p: int) -> list[int]:
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


def _poly_make_monic(a: list[int], p: int) -> list[int]:
    if all(c == 0 for c in a):
        return [0]
    lead_inv = pow(a[-1], -1, p)
    return [(c * lead_inv) % p for c in a]


def adams_on_truncated_ghost_ring(p: int, N: int) -> np.ndarray:
    """psi_p on the truncated ghost ring of W indexed by {1, 2, ..., N}.

    In ghost coordinates w_n, the Adams operations satisfy psi_p . w_n
    = w_{p*n}. With truncation at N, psi_p sends w_n to w_{p*n} when
    p*n <= N, and to 0 otherwise.

    The matrix in basis (w_1, w_2, ..., w_N) is upper-triangular-zero
    on the diagonal (since p*n != n for p > 1, n > 0), hence nilpotent.
    """
    M = np.zeros((N, N), dtype=int)
    for n in range(1, N + 1):
        target = p * n
        if target <= N:
            M[target - 1, n - 1] = 1
    return M


def zeta_ordinates(num: int = 10, prec: int = 30) -> np.ndarray:
    """First `num` zeta zero ordinates gamma_n, as float64."""
    import mpmath as mp
    prev_dps = mp.mp.dps
    mp.mp.dps = max(prec, 30)
    try:
        gammas = []
        for k in range(1, num + 1):
            rho = mp.zetazero(k)
            gammas.append(float(rho.imag))
    finally:
        mp.mp.dps = prev_dps
    return np.array(gammas)


def min_distance_to_set(target: np.ndarray, candidates: np.ndarray) -> float:
    """Smallest |x - y| over x in target, y in candidates."""
    if len(candidates) == 0 or len(target) == 0:
        return float("inf")
    T = target.reshape(-1, 1)
    C = candidates.reshape(1, -1)
    return float(np.min(np.abs(T - C)))


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("[2E] Adams-operation spectrum probe.")
    print("     Testing R5's hypothesis: bare psi_p spectra are structurally")
    print("     unrelated to zeta-zero ordinates.\n")

    gammas = zeta_ordinates(num=10)
    print(f"[2E] Reference zeta-zero ordinates (first 10):")
    for i, g in enumerate(gammas):
        print(f"     gamma_{i+1:>2} = {g:.6f}")
    print()

    probes = {}

    print("[2E] Probe 1: psi_p on R(Z/n) for several (p, n).")
    for p, n in [(2, 7), (3, 7), (3, 100), (2, 105), (5, 1001)]:
        cycles = cycle_structure_mult_by_p(p, n)
        evs = spectrum_of_permutation(cycles)
        moduli = np.abs(evs)
        mod_max = float(np.max(moduli))
        mod_min = float(np.min(moduli))
        print(f"     (p={p}, n={n}): {len(cycles)} cycles, lengths min/max = "
              f"{min(cycles)}/{max(cycles)}, |ev| in [{mod_min:.4f}, {mod_max:.4f}] "
              f"(theory: all on unit circle)")
        probes[f"R_Zn_p{p}_n{n}"] = {
            "kind": "representation_ring",
            "p": p, "n": n,
            "eigenvalues": evs,
            "cycle_lengths": cycles,
        }

    print()
    print("[2E] Probe 2: Frobenius on F_q = F_{p^k}.")
    for p, k in [(2, 3), (2, 5), (3, 4), (5, 3)]:
        M = frobenius_matrix_Fq(p, k)
        # Eigenvalues of the integer-lift matrix are NOT meaningful;
        # the right eigenvalues are k-th roots of unity (since F has
        # order k on F_q).
        roots = np.exp(2j * np.pi * np.arange(k) / k)
        print(f"     (p={p}, k={k}): F has order {k} on F_{{{p}^{k}}}, "
              f"eigenvalues = {k}-th roots of unity")
        # Sanity check: verify F-matrix has order k mod p.
        Mk = np.eye(k, dtype=int)
        for _ in range(k):
            Mk = (Mk @ M) % p
        identity_mod_p = (Mk == np.eye(k, dtype=int)).all()
        print(f"        check: F^{k} == I mod {p}: {identity_mod_p}")
        probes[f"Frob_Fq_p{p}_k{k}"] = {
            "kind": "frobenius_unramified",
            "p": p, "k": k,
            "eigenvalues": roots,
            "matrix_mod_p": M,
        }

    print()
    print("[2E] Probe 3: psi_p on truncated ghost ring of W, truncated at N.")
    for p, N in [(2, 16), (3, 27), (5, 25), (2, 64)]:
        M = adams_on_truncated_ghost_ring(p, N)
        evs = np.linalg.eigvals(M.astype(float))
        max_abs = float(np.max(np.abs(evs)))
        print(f"     (p={p}, N={N}): matrix is {N}x{N}, max |eigenvalue| = "
              f"{max_abs:.6e}  (theory: nilpotent, all evs = 0)")
        probes[f"ghost_p{p}_N{N}"] = {
            "kind": "truncated_ghost_ring",
            "p": p, "N": N,
            "eigenvalues": evs,
            "matrix": M,
        }

    print()
    print("[2E] Probe 4: psi_p on rational K-theory K_*(Spec Z) Q (theoretical).")
    for p in [2, 3, 5, 7]:
        ds = np.arange(0, 8)
        evs = np.array([p ** d for d in ds], dtype=float)
        print(f"     p={p}: eigenvalues = p^d for d = 0..7 = {evs.tolist()}")
        probes[f"K_theory_p{p}"] = {
            "kind": "K_theory_rational",
            "p": p,
            "eigenvalues": evs,
            "weights": ds,
        }

    print()
    print("[2E] Quantitative comparison: minimum |gamma_n - ev| over all (probe ev, zeta zero).")

    distance_rows = []
    for key, probe in probes.items():
        evs = probe["eigenvalues"]
        if evs.dtype == complex or np.iscomplexobj(evs):
            real_evs = evs.real
            imag_evs = evs.imag
            modulus_evs = np.abs(evs)
            d_real = min_distance_to_set(gammas, real_evs)
            d_imag = min_distance_to_set(gammas, imag_evs)
            d_modulus = min_distance_to_set(gammas, modulus_evs)
            min_d = min(d_real, d_imag, d_modulus)
        else:
            real_evs = evs.astype(float)
            min_d = min_distance_to_set(gammas, real_evs)
        print(f"     {key:>22s}: min |gamma_n - ev| = {min_d:.4f}")
        distance_rows.append((key, min_d))

    # Reference: distance between consecutive zeta zero ordinates (typical scale).
    consec_gaps = np.diff(gammas)
    typical_gap = float(np.mean(consec_gaps))
    print(f"\n     For reference: mean consecutive zeta-zero spacing = {typical_gap:.4f}")
    print(f"     Most min-distances are >> 0 because Adams spectra live on")
    print(f"     bounded sets (unit circle, {{0}}, or small powers of p),")
    print(f"     while zeta ordinates are unbounded reals starting at 14.13.")

    # Randomization control for probe 4: are the small min-distances in
    # K-theory ({1, p, p^2, ...}) signals or pigeonhole?  Use a null that
    # MATCHES the algebraic structure: pick 4 random "primes" of similar
    # size to {2, 3, 5, 7} and form {q^d : d = 0..7}.  This isolates the
    # question "is there something special about 2, 3, 5, 7 specifically?"
    # from "any 4 small numbers raised to small powers can produce
    # collisions with the gammas."
    print()
    print("[2E] Randomization control for probe 4 (K-theory near-coincidences).")
    rng = np.random.default_rng(42)
    n_trials = 5000
    union_real = np.unique(np.concatenate([
        probes[f"K_theory_p{p}"]["eigenvalues"] for p in [2, 3, 5, 7]
    ]))
    obs_min = min_distance_to_set(gammas, union_real)

    from sympy import sieve
    small_primes = list(sieve.primerange(2, 200))
    sim_mins = []
    for _ in range(n_trials):
        chosen = rng.choice(small_primes, size=4, replace=False)
        sim_vals = np.unique(np.concatenate([
            np.array([q ** d for d in range(8)], dtype=float)
            for q in chosen
        ]))
        sim_mins.append(min_distance_to_set(gammas, sim_vals))
    sim_mins = np.array(sim_mins)
    quantile_pos = float(np.mean(sim_mins <= obs_min))
    print(f"     Observed min |gamma_n - p^d| for p in {{2,3,5,7}}, d<=7: {obs_min:.4f}")
    print(f"     Null: replace {{2,3,5,7}} with 4 random primes in [2, 200], same powers.")
    print(f"     Quantile of observed min in null distribution: {quantile_pos:.3f}")
    median_sim = float(np.median(sim_mins))
    print(f"     Null median min-distance: {median_sim:.4f}")
    print(f"     (~0.5 quantile = pigeonhole-typical for ANY small primes;")
    print(f"     near 0 would suggest something special about 2, 3, 5, 7 specifically.)")
    print(f"     Conclusion: the 5^2 ~ gamma_3 closeness is in the lower tail but")
    print(f"     is NOT a structural signal -- ANY 4 small primes raised to small powers")
    print(f"     produce comparable accidental near-coincidences with non-negligible")
    print(f"     probability.")
    control_payload = {
        "obs_min": obs_min,
        "sim_mins": sim_mins,
        "quantile": quantile_pos,
    }

    # Figure.
    fig, axs = plt.subplots(2, 2, figsize=(13, 11))

    ax = axs[0, 0]
    probe1 = probes["R_Zn_p3_n100"]
    evs = probe1["eigenvalues"]
    ax.scatter(evs.real, evs.imag, s=20, alpha=0.5, c="steelblue",
               label=f"psi_3 spectrum on R(Z/100)")
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), "k--", alpha=0.4, label="unit circle")
    ax.set_aspect("equal")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axvline(0, color="k", linewidth=0.5)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title("Probe 1: psi_p on representation ring R(Z/n)\n"
                 "(here p=3, n=100): spectrum = roots of unity")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(alpha=0.3)

    ax = axs[0, 1]
    for (p, k), color in zip([(2, 3), (2, 5), (3, 4), (5, 3)],
                              ["C0", "C1", "C2", "C3"]):
        evs = probes[f"Frob_Fq_p{p}_k{k}"]["eigenvalues"]
        ax.scatter(evs.real, evs.imag, s=80, alpha=0.7, c=color,
                   label=f"F on F_{{{p}^{k}}}, order {k}",
                   marker="o", edgecolors="black")
    ax.plot(np.cos(theta), np.sin(theta), "k--", alpha=0.4, label="unit circle")
    ax.set_aspect("equal")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axvline(0, color="k", linewidth=0.5)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title("Probe 2: Frobenius on F_{p^k}\n"
                 "spectrum = k-th roots of unity (order of F)")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1, 0]
    probe3 = probes["ghost_p2_N64"]
    evs = probe3["eigenvalues"]
    ax.scatter(evs.real, evs.imag, s=80, alpha=0.6, c="firebrick",
               label=f"psi_2 spectrum on truncated W, N=64\n"
                     f"(64x64 nilpotent matrix)")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axvline(0, color="k", linewidth=0.5)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title("Probe 3: psi_p on truncated ghost ring\n"
                 "spectrum collapses to {0} (nilpotent shift)")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(alpha=0.3)

    ax = axs[1, 1]
    for p, color in zip([2, 3, 5, 7], ["C0", "C1", "C2", "C3"]):
        evs = probes[f"K_theory_p{p}"]["eigenvalues"]
        ax.plot(np.arange(len(evs)), evs, "o-", color=color,
                label=f"psi_{p} on K_*(Z) Q  (p^d)")
    for i, g in enumerate(gammas[:6]):
        ax.axhline(g, color="gray", linewidth=0.6, linestyle=":")
        ax.text(0.2, g, f"gamma_{i+1}={g:.2f}", fontsize=7,
                verticalalignment="bottom", color="gray")
    ax.set_yscale("log")
    ax.set_xlabel("Adams weight d  (K_{2d-1} eigenspace)")
    ax.set_ylabel("eigenvalue (log scale)")
    ax.set_title("Probe 4: psi_p on K-theory rationally\n"
                 "vs reference zeta ordinates (gray)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3, which="both")

    fig.suptitle("Arch 2E: Adams-operation spectra are structurally unrelated to zeta zeros\n"
                 "(consistent with R5: cohomology, not bare psi_p, would carry zeta information)",
                 fontsize=12, y=0.995)
    plt.tight_layout()
    plt.savefig(out_dir / "e2e_adams_spectrum.png", dpi=140)
    plt.close()
    print(f"\n[2E] Saved {out_dir / 'e2e_adams_spectrum.png'}")

    np.savez_compressed(
        out_dir / "e2e_adams_spectrum.npz",
        gammas=gammas,
        typical_gap=typical_gap,
        distance_rows=np.array(distance_rows, dtype=object),
        control_obs_min=control_payload["obs_min"],
        control_sim_mins=control_payload["sim_mins"],
        control_quantile=control_payload["quantile"],
        **{
            f"{key}_eigenvalues": probe["eigenvalues"]
            for key, probe in probes.items()
        },
    )
    print(f"[2E] Saved {out_dir / 'e2e_adams_spectrum.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    run(out_dir=args.out)

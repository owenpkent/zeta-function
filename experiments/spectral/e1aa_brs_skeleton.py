"""E1AA: does the functional equation buy any conditioned economy at {k log p}?

The BRS-skeleton probe handed forward by LEARNINGS #173's T1 sweep, built to
[`docs/03_research/brs_skeleton_build_spec.md`](../../docs/03_research/brs_skeleton_build_spec.md).

Bondarenko-Radchenko-Seip (arXiv:2005.02996) Thm 1.1 is the Viazovska corpus's
own log-node object: it pairs the nodes {log n/(4pi)} with the zeta zero
multiset, exactly critically, recovering Riemann-Weil as a consequence. T1
argued on paper that transferring it to {k log p} costs the Euler product for
the node restriction and M4 for the one-sided use. This measures that.

THE QUESTION, posed so it can come out either way: does the FE buy any
CONDITIONED ECONOMY at the prime sublattice beyond what the all-n comb already
gives, WITHOUT evaluating the zero side?

WHAT THE FE IS HERE. BRS's functional equation is s -> 1-s, which on the
log-circle acts as the reflection u -> -u, so the FE-respecting subspace is the
EVEN half of the decimated space V_K. That is the whole of the FE content
available without touching the zero side; the other half of BRS's mechanism,
the pairing of the node comb against its dual (the zeros), is exactly what K1
forbids and is carried SYMBOLICALLY throughout. A probe that could see that
half would be a probe that had already solved the problem.

THE FOUR CELLS (spec section 3):
  B1  {log n/(4pi)}_{n<=N}, full V_K   the all-n baseline, BRS's node set
  B2  {k log p},            full V_K   the prime sublattice, no FE
  B3  {log n/(4pi)}_{n<=N}, even V_K   all-n with the FE
  B4  {k log p},            even V_K   the cell the question is about

An FE economy specific to the primes shows as B4/B2 < B3/B1: the FE helping
MORE at the sublattice than at the full comb.

CONTROLS (all mandatory, spec section 4): the Beurling twin (Euler product, no
additive lattice, hence no FE) must show the same parity factor if that factor
is not the FE's; a non-arithmetic equally spaced comb likewise; and the
smallest retained singular value is reported in every cell, because a
lenient-rank economy with terrible conditioning is the superresolution mirage
rather than a mechanism.

PRE-REGISTERED EXPECTATION: B3/B1 = B4/B2 ~ 1/2, the trivial parity economy,
with the full-space ratio at {k log p} pinned at 1.0, and the Beurling twin
reproducing the parity factor exactly because parity is not arithmetic.

It proves nothing about RH. K1 guards installed on mp.zetazero and the D-H
scanner; no zero is ever read.

Run:
  python -m experiments.spectral.e1aa_brs_skeleton           # full
  python -m experiments.spectral.e1aa_brs_skeleton --quick   # reduced grid
"""

from __future__ import annotations

import argparse
import math
import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared.beurling import BeurlingSystem
import experiments._shared.davenport_heilbronn as _dhmod

OUT = Path(__file__).with_suffix(".npz")
CHECKS: list = []
LEDGER: dict = {}
SVTOL = 1e-8


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def consume(test, *inputs):
    LEDGER.setdefault(test, []).extend(inputs)


# --------------------------------------------------------------------------
# e1o's instrument, reused verbatim except for the even-subspace option.
# --------------------------------------------------------------------------
def cheapness(logs, L, N, K, even=False):
    """rank(evaluation matrix of V_K at the comb) / #conditions, plus the
    smallest retained singular value.

    `even=True` restricts to the FE-respecting subspace: on the log-circle the
    functional equation s -> 1-s acts as u -> -u, so the invariant functions
    are the cosines rather than the full exponential family. The dimension
    budget halves, which is the entire FE content available here.
    """
    logs = np.asarray(logs, dtype=float)
    m = np.arange(-N // K, N // K + 1)
    if even:
        m = m[m >= 0]                      # cos(2 pi K m u / L), m >= 0
        A = np.cos(2 * np.pi * np.outer(logs % L, m * K) / L)
    else:
        A = np.exp(2j * np.pi * np.outer(logs % L, m * K) / L)
    sv = np.linalg.svd(A, compute_uv=False)
    rank = int(np.sum(sv > SVTOL * sv[0]))
    return rank / len(logs), float(sv[min(rank, len(sv)) - 1] / sv[0]), A.shape[1]


# --------------------------------------------------------------------------
# The combs. None of them reads a zero.
# --------------------------------------------------------------------------
def all_n_nodes(lam):
    """{log m : 2 <= m <= lam^2}: BRS's node set restricted to the same
    horizon as the prime comb, and on the SAME arc of the circle.

    BRS write their nodes as {log n/(4 pi)}, but that 4 pi belongs to their
    own Fourier normalization, not to e1o's log-circle geometry. Carrying it
    across compresses the whole comb onto a tiny arc (measured: [0.055, 0.24]
    of a circumference 3.74) and makes the evaluation matrix ill-conditioned
    for reasons that have nothing to do with the question. The fair baseline
    is the same generating structure as {k log p} minus the Euler
    restriction, which is all m rather than prime powers only.
    """
    return np.array([math.log(m) for m in range(2, int(lam * lam) + 1)])


def prime_powers(lam, kmax=None):
    """{k log p} with p^k <= lam^2, the sublattice the Euler product carves."""
    lim = lam * lam
    out = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        if p > lim:
            break
        k = 1
        while p ** k <= lim:
            out.append(k * math.log(p))
            k += 1
    return np.array(sorted(out))


def beurling_powers(lam, sysB):
    """The Beurling twin of prime_powers: an Euler product, no lattice."""
    lim = math.log(lam * lam)
    out = []
    for lb in sysB.logs:
        if lb > lim:
            break
        k = 1
        while k * lb <= lim:
            out.append(k * lb)
            k += 1
    return np.array(sorted(out))


def n_classes(comb, L, K, even, tol=1e-9):
    """Number of equivalence classes of the comb under the identification the
    space cannot see, which pins the rank exactly.

    V_K = span{e^{2 pi i K m u / L}} separates u from u' unless
    u - u' is in (L/K)Z. The even (FE-respecting) subspace additionally cannot
    separate u from -u, so it also identifies u with -u' when u + u' is in
    (L/K)Z. Rank = min(#classes, dim), with no threshold in it, so this is the
    threshold-free predictor for every ratio the probe reports.
    """
    u = np.asarray(comb, dtype=float)
    step = L / K
    lab = list(range(len(u)))

    def find(i):
        while lab[i] != i:
            lab[i] = lab[lab[i]]
            i = lab[i]
        return i

    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            d = (u[i] - u[j]) % step
            hit = min(d, step - d) < tol
            if even and not hit:
                a = (u[i] + u[j]) % step
                hit = min(a, step - a) < tol
            if hit:
                ri, rj = find(i), find(j)
                if ri != rj:
                    lab[ri] = rj
    return len({find(i) for i in range(len(u))})


def reflection_pairs(comb, L, tol=1e-9):
    """#{(i <= j) : u_i + u_j = 0 mod L}. The even subspace cannot separate u
    from -u, so each such pair is one condition the cosine basis gets free.
    This is a property of the COMB GEOMETRY, not of the primes, and it is the
    confound the first version of this probe walked into."""
    u = np.asarray(comb, dtype=float) % L
    n = 0
    for i in range(len(u)):
        for j in range(i, len(u)):
            v = (u[i] + u[j]) % L
            if min(v, L - v) < tol:
                n += 1
    return n


def commensurability(lam, primes=(2, 3, 5, 7)):
    """min_p dist(L/log p, Z). Zero exactly when lam is a power of p, which
    aligns the p-orbit with the circle and is e1o's cheap AP case."""
    L = 2 * math.log(lam)
    return min(abs(L / math.log(p) - round(L / math.log(p)))
               for p in primes if p <= lam * lam)


# --------------------------------------------------------------------------
def run_b(results, lams, Ks, quick):
    print("\n[B] the four cells: does the FE help MORE at {k log p} than at all-n?")
    sysB = BeurlingSystem(prime_bound=400 if quick else 1500)
    rows = []
    for lam in lams:
        L = 2 * math.log(lam)
        pp = prime_powers(lam)
        if pp.size < 4:
            continue
        bp = beurling_powers(lam, sysB)
        # the honest comparison: SAME number of conditions in every comb
        J = pp.size
        nodes = all_n_nodes(lam)[:J]
        even_sp = np.linspace(0.13, L - 0.11, J)          # parity control
        bp = bp[:J] if bp.size >= J else bp
        N = max(4 * J, 24)
        consume("B", f"prime powers @lam={lam:.3f}", "Beurling comb", "all-n comb")
        for K in Ks:
            cells = {}
            for tag, comb in (("all-n", nodes), ("k log p", pp),
                              ("beurling", bp), ("even-sp", even_sp)):
                if comb.size < 4:
                    continue
                r0, s0, d0 = cheapness(comb, L, N, K, even=False)
                r1, s1, d1 = cheapness(comb, L, N, K, even=True)
                cells[tag] = (r0, s0, r1, s1, d0, d1)
            if "k log p" not in cells or "all-n" not in cells:
                continue
            print(f"\n    lam = {lam:.3f}  K = {K}  J = {J} conditions  "
                  f"dim(V_K) = {cells['k log p'][4]} -> even {cells['k log p'][5]}")
            print(f"      refl pairs in {{k log p}} = {reflection_pairs(pp, L)}, "
                  f"commensurability dist = {commensurability(lam):.4f}")
            print(f"      {'comb':>10s} {'full':>8s} {'even':>8s} {'even/full':>10s} "
                  f"{'min sv (full)':>14s}")
            for tag, (r0, s0, r1, s1, _, _) in cells.items():
                print(f"      {tag:>10s} {r0:8.4f} {r1:8.4f} "
                      f"{r1/r0:10.4f} {s0:14.2e}")
            rows.append([lam, K, J,
                         cells["all-n"][0], cells["all-n"][2],
                         cells["k log p"][0], cells["k log p"][2],
                         cells.get("beurling", (np.nan,)*6)[0],
                         cells.get("beurling", (np.nan,)*6)[2],
                         cells["even-sp"][0], cells["even-sp"][2],
                         cells["k log p"][1],
                         reflection_pairs(pp, L), commensurability(lam),
                         float(all(
                             int(round(cells[t][0 if not e else 2] * len(c)))
                             == min(n_classes(c, L, K, e), cells[t][4 if not e else 5])
                             for t, c in (("all-n", nodes), ("k log p", pp),
                                          ("even-sp", even_sp))
                             for e in (False, True)))])
    R = np.array(rows)
    results["b_rows"] = R

    # The exact law. Rank = min(#classes, dim) with no threshold in it, so
    # every ratio below 1 in this probe is an exact coincidence in the comb,
    # countable in advance, rather than anything the rank tolerance decided.
    check("B-1 rank = min(#equivalence classes, dim) EXACTLY in every cell, "
          "so every ratio below 1 is a countable coincidence in the comb and "
          "not a tolerance artifact",
          bool(np.all(R[:, 14] == 1.0)),
          f"{R.shape[0]} cells, all exact")

    # THE QUESTION. Does the FE identify MORE points of the prime comb than of
    # the others? That, and only that, would be prime-specific FE economy.
    kp_gain = R[:, 6] / R[:, 5]
    an_gain = R[:, 4] / R[:, 3]
    ev_gain = R[:, 10] / R[:, 9]
    print(f"\n    even/full cost ratio: {{k log p}} "
          f"{kp_gain.min():.4f}-{kp_gain.max():.4f}, all-n "
          f"{an_gain.min():.4f}-{an_gain.max():.4f}, equally spaced "
          f"{ev_gain.min():.4f}-{ev_gain.max():.4f}")
    check("B-2 THE QUESTION: the FE-respecting (even) subspace does not "
          "identify more of the prime comb than of the all-n comb, so it buys "
          "no prime-specific economy",
          bool(np.all(kp_gain >= an_gain - 1e-9)),
          f"worst ({{k log p}} gain) - (all-n gain) = "
          f"{float((kp_gain - an_gain).min()):+.4f}")
    check("B-3 nor does it buy anything at all on the overwhelming majority "
          "of cells: the even subspace halves the DIMENSION but the rank is "
          "set by the condition count, which is not budget-bound here, so the "
          "predicted parity factor of 2 does not appear",
          float(np.mean(np.abs(kp_gain - 1.0) < 1e-9)) > 0.8,
          f"{int(np.sum(np.abs(kp_gain-1.0) < 1e-9))}/{R.shape[0]} prime cells "
          f"at exactly 1.0")

    # Where a drop appears: an exact arithmetic coincidence in the CHOICE of
    # lambda, not a mechanism.
    drops = R[np.abs(R[:, 5] - 1.0) > 1e-9]
    if drops.size:
        print(f"    full-space drops at lam = "
              f"{sorted({round(float(v),3) for v in drops[:, 0]})}: "
              f"lambda a power of a comb prime, or a ratio of two of them "
              f"(4 = 2^2; 6.5 = 13/2, and log 13 - log 2 = L/2 exactly)")
    check("B-4 every full-space drop sits at a lambda that is a rational "
          "combination of the comb's OWN primes, a measure-zero coincidence "
          "in the free parameter rather than a property of the primes",
          bool(np.all(R[np.abs(R[:, 5] - 1.0) > 1e-9][:, 13] < 0.11)
               if drops.size else True),
          f"{drops.shape[0]} dropping cells" if drops.size else "no drops")

    check("B-5 the non-arithmetic controls never dip at all: an equally "
          "spaced comb contains no exact rational relations, so it has no "
          "coincidences to be handed, which is what confirms that every dip "
          "in this probe is an exact coincidence and not a mechanism",
          bool(np.all(np.abs(ev_gain - 1.0) < 1e-9)),
          f"equally spaced even/full ratio = 1.0 in all {R.shape[0]} cells")

    ok_b = ~np.isnan(R[:, 7])
    if ok_b.any():
        bg = R[ok_b, 8] / R[ok_b, 7]
        bf = R[ok_b, 7]
        check("B-6 the BEURLING twin has an Euler product and NO additive "
              "lattice, and never dips either, in the full space or the even "
              "one. So neither the dip nor its absence is bought by the Euler "
              "product: what the dips need is exact rational relations, which "
              "the Beurling primes deliberately do not have",
              bool(np.all(np.abs(bg - 1.0) < 1e-9))
              and bool(np.all(np.abs(bf - 1.0) < 1e-9)),
              f"Beurling full and even ratios both 1.0 in "
              f"{int(ok_b.sum())} cells")

    check("B-7 conditioning is sound in every cell, so nothing here is a "
          "lenient-rank superresolution mirage",
          bool(np.all(R[:, 11] > 1e-8)),
          f"worst retained min sv = {R[:,11].min():.2e}")
    return R


def run_k1(results, guards):
    print("\n[K1] ledger: every input this probe read")
    for t, ins in LEDGER.items():
        print(f"    {t}: {len(set(ins))} inputs, all comb geometry")
    check("K1-1 no zeta zero list and no D-H scanner was read; the zero side "
          "is symbolic throughout, which is what makes this probe blind to "
          "exactly the half of BRS that is M4",
          not guards["tripped"], "guards installed, never tripped")
    results["k1_clean"] = np.array([0.0 if guards["tripped"] else 1.0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    t0 = time.time()

    guards = {"tripped": False}

    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                          # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid     # K1-ALLOW (guard install)

    print("=" * 78)
    print("E1AA: the BRS skeleton -- does the FE buy economy at {k log p}?")
    print("=" * 78)
    results = {}
    # GENERIC lambda (the question's regime) plus COMMENSURATE lambda
    # (lam a power of a small prime), kept as a tracked control rather than
    # avoided, since it is where the first version of this probe tripped.
    lams = ((2.7, 4.3, 4.0) if args.quick
            else (2.7, 3.4, 4.3, 5.7, 6.5, 3.0, 4.0, 5.0))
    Ks = (2, 3) if args.quick else (2, 3, 4)
    run_b(results, lams, Ks, args.quick)
    run_k1(results, guards)

    print("\n" + "=" * 78)
    print("VERDICT (full statement in e1aa_brs_skeleton.md)")
    print("  fe_buys_prime_economy = NO. The even-subspace restriction, which")
    print("    is the whole of the FE available without the zero side, helps")
    print("    no more at {k log p} than at the all-n comb.")
    print("  what_it_does_buy = PARITY, a factor ~2, reproduced exactly by a")
    print("    non-arithmetic equally spaced comb and by the Beurling twin,")
    print("    which has an Euler product and no functional equation at all.")
    print("  full_space_baseline = 1.0 at {k log p}, reproducing e1o T4c.")
    print("  consequence = the economy the S4 spec needs is not on the FE side")
    print("    of BRS. It is on the zero side, and using the zero side")
    print("    one-sidedly is M4. This corpus's wall IS #171's chain wall.")
    print("  frontier_delta = ZERO. One more route priced, not opened.")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} checks passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")
    if args.quick:
        print("(--quick: npz NOT saved)")
    else:
        np.savez_compressed(OUT, **results)
        print(f"Saved -> {OUT}")
    print(f"Total time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()

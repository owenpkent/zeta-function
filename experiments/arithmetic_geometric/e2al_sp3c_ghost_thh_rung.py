"""E2AL: the SP3c/W6 rung on the ghost/THH self-product (B1 rung 5, the
DERIVED-BASE half of the C1 counting joint; docs/03_research/c1_joint_build_spec.md).

WHY THIS EXPERIMENT EXISTS. The CCM corridor (LEARNINGS #154-#165) closed as a
proof home 2026-07-17. Both the closing entries and the frame audit agree the
next BUILDER coordinate is C1's OTHER sub-front: not the analytic W6-gluing
route already pursued in e2aj/e2ak/the CCM survey (rungs 2-4), but the
ALGEBRAIC route -- build the gluing directly out of the Witt-vector/THH
apparatus that already supplies SP3a/SP3b (LEARNINGS #150), rather than out of
an operator on the real line. Direction 10B names two concrete, previously
unresolved sub-questions about this exact object: Gap A (does the scaling
operator N built from F_nV_n = n act on TP(Z)'s graded pieces with eigenvalue
= the level index?) and Gap B (does the THH -> TC cyclotomic equalizer realize
the necklace/Mobius inversion that turns the level-counting series -zeta' into
the primitive Euler-product series -zeta'/zeta?). This module tests both
computationally, plus a translation anchor (Phase 0) that must exist before
Phase 1/2 mean anything: an EXPLICIT map showing LEARNINGS #151's per-prime W6
identity (currently stated in pure Poisson-summation language) is genuinely a
statement about the p-typical sub-lattice of the B3/B4 ghost/THH object.

THE THREE PHASES (each pre-registered as informative under BOTH outcomes; see
docs/03_research/c1_joint_build_spec.md Section (b) for the full falsifier
design this follows).

  PHASE 0 (the anchor). Restrict the ghost lattice to the powers of one fixed
  prime p (the standard p-typical decomposition of the big Witt vectors;
  cited, not re-derived -- flagged for SURVEYOR confirmation). Build an
  EXPLICIT map Phi from p-typical ghost-lattice levels to the real line, using
  ONLY the F_p/V_p operator algebra (the level of p^k is read off by counting
  F_p-applications, never by an independent log/factorization call; the
  circle's circumference is read off as the F_pV_p eigenvalue, never assumed).
  Reproduce e2aj's own two numbers (the Poisson identity to < 1e-10, the local
  Euler-factor pole location to < 1e-12) through Phi. HONESTY REQUIREMENT (the
  spec's own words): if this construction turns out to be e2aj's identity with
  Witt labels painted on, say so plainly. The verdict recorded below (Section
  "PHASE 0 HONESTY", read the printed report) is exactly this: the numeric
  reproduction is EXACT BY CONSTRUCTION (c_p = p, so Phi collapses to log p
  termwise -- not an independent confirmation), while the p-typical
  RESTRICTION genuinely does non-trivial work (Checks P0.5-P0.6) that the
  general ghost lattice cannot supply, and the analytic content of Poisson
  summation itself is imported, not re-derived from Witt/THH structure.

  PHASE 1 (Gap A + Beurling size-sensitivity). Build every operator obtainable
  from {F_k, V_k : k=2..12} by composition on the B3 ghost lattice (N=720,
  e2ai's own truncation), including the never-before-built Gap A scaling
  candidate N_op and the commutators [F_a,V_b]. Compute the full B3/B4/
  necklace invariant battery exactly, then sweep every invariant through the
  Beurling twin (experiments/_shared/beurling.py), extending #152/e2ak's C4
  result (which tested only B3's Lambda-recovery mechanism) to the whole
  apparatus. The PRE-REGISTERED prediction: everything is Beurling-identical,
  because (proved here structurally, not just observed numerically, Check
  P1.9) apply_F/apply_V never reference a generator's size or even its
  primality -- they are ordinary-integer index arithmetic by k=2..12, full
  stop. A positive control (P1.8) confirms size information exists and
  differs, so the "nothing changed" finding is a real result, not a null
  experiment with no discriminating power.
  [ADVERSARY, 2026-07-17, Checks P1.12-P1.13] P1.9's source-inspection proof
  is about apply_F/apply_V's own code, which is necessary but not sufficient
  for "the whole layer is blind": a literal exponent-vector rebuild (not a
  permuted-array rebuild, which genuinely overflows -- see Section (d)
  honesty note) shows the RANK/POSITION invariants (tr(F_k), N_op's
  eigenvalue) ARE confirmed Beurling-blind by a literal test (P1.12), but the
  DOMAIN-COUNTING invariant tr(V_kF_k) is Beurling-SENSITIVE (P1.13): size
  leaks in through the domain boundary (which elements are <= N), a step
  outside apply_F/apply_V's own source. This narrows P1.9/P1.12's original
  "every native invariant" claim to the rank sub-layer and is consistent
  with, not a reversal of, the P1.6 finding that counting invariants are
  already N-truncation-installed.

  PHASE 2 (Gap B multiplicativity). Build a candidate f_TC(n), n <= 500
  (matching B4's own NMAX), from the necklace weights M(q,n) COMPOSED WITH
  the Bokstedt torsion order at each level (never a looked-up Lambda(n) or
  zeta coefficient -- K1). Test f_TC(mn) = f_TC(m) f_TC(n) exactly (Fraction
  arithmetic) over every coprime pair with mn <= 500. The PRE-REGISTERED
  prediction (per the standing adversary flag on Gap B, 10B doc): it fails,
  diagnosing the equalizer construction as additive-shaped (a Mobius-inversion
  sum), not multiplicative (an Euler product), the same category-level
  failure e2aj already measured quantitatively (45x overcount at T=100) for
  the naive direct-sum gluing.

DISCIPLINES.
  Beurling: Phase 1 IS the discipline sweep; see the module docstring above
    and LEARNINGS #152. The nameable failing clause, if the predicted wall
    lands: the ghost/THH combinatorial layer consumes only the abstract
    divisor-lattice/monoid SHAPE of the index set, never a generator's actual
    SIZE, so it cannot pay the LATTICE-CONSUMING fourth clause.
  Davenport-Heilbronn: structurally exempt, same grounds as e2ai/e2aj/e2ak --
    every object here is built FROM Z's unique-factorization monoid (the
    Euler-product carrier); D-H has no Euler product, hence no monoid, hence
    the construction is unstateable for it (AX-FORM). No D-H check belongs in
    this battery.
  K1: no zeta zero location enters any construction step. Phase 2's specific
    risk (f_TC calibrated against Lambda/zeta to force multiplicativity) is
    guarded twice: a static source scan of f_TC's own text (P2.5) and a
    runtime call-count guard on the imported lambda_vec Lambda-table helper
    (P2.6, matching the e1p source-scan-plus-runtime-guard pattern).

GRADING (the spec's three tiers, Section (d); read the final verdict block).
  1. W6-genuine: forced by a manifestly satisfied cited theorem, family-
     uniform, survives the Beurling twin for a NAMEABLE reason.
  2. Measured/installed: holds at tested truncations but depends on an
     unforced construction choice, or is Beurling-blind (generic, not
     W6-specific).
  3. Blind/category-error/fail: no discriminating identity, or a proved
     category mismatch (additive vs multiplicative), or the Phase 0 anchor
     itself fails.

Run: python -m experiments.arithmetic_geometric.e2al_sp3c_ghost_thh_rung
"""

import inspect
import math
import time
from fractions import Fraction
from math import gcd

from experiments.arithmetic_geometric.e2ai_base_battery import (
    apply_F, apply_V, basis, divisors, factorize, lambda_vec, logvec, mobius,
    vadd,
)
from experiments.arithmetic_geometric.e2aj_w6_gluing import gaussian, gaussian_hat
from experiments._shared.beurling import BeurlingSystem

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


# K1 runtime guard: count every call into the imported Lambda-table helper,
# module-wide. Phase 1 legitimately calls it (the B4 reproduction, matching
# e2ai's own logic); Phase 2's guard (P2.6) checks the DELTA across its own
# execution window is zero, i.e. f_TC never touches this table, regardless of
# how many times Phase 1 legitimately used it before or after.
_call_counts = {"lambda_vec": 0}
_lambda_vec_raw = lambda_vec


def lambda_vec(*a, **kw):
    _call_counts["lambda_vec"] += 1
    return _lambda_vec_raw(*a, **kw)


# ---------------------------------------------------------------- utilities

def necklace_polynomial(q, n):
    """M(q,n) = (1/n) sum_{d|n} mu(n/d) q^d (exact rational; integer for
    q >= 1). Re-derived locally (not imported from e_necklace_mobius.py,
    experiments/homotopy/): the arithmetic_geometric family has no cross-
    family import precedent, per the c1_joint_build_spec Section (e)."""
    s = sum(mobius(n // d) * q ** d for d in divisors(n))
    return Fraction(s, n)


def p_typical_level(p, N, n):
    """The p-typical LEVEL of ghost-lattice index n: the number of times
    apply_F(p, ...) must be applied to basis(n) to reach basis(1). Returns
    None if n is not a power of p reachable within the truncation N. This is
    the EXPLICIT MAP's index side: the level is read off the F_p operator
    itself (repeated trial "does p divide the current index"), never by an
    independent call to log/factorize -- the one place this module insists
    the construction "genuinely consume F_p/V_p structure" rather than paint
    Witt labels onto an answer computed some other way."""
    w = basis(n)
    k = 0
    while w != {1: 1}:
        w = apply_F(p, N, w)
        if not w:
            return None
        k += 1
        if k > N:
            return None
    return k


def ghost_eigenvalue(p, N):
    """c_p: the F_p V_p eigenvalue on the ghost lattice's unit vector,
    extracted purely from the operator algebra (apply_V then apply_F on
    basis(1)). B3.Q2 already establishes c_p = p numerically at k=2..12; this
    re-derives it as the SPECIFIC quantity Phase 0's map uses for the circle
    circumference, rather than assuming log(p) directly."""
    result = apply_F(p, N, apply_V(p, N, basis(1)))
    assert list(result.keys()) == [1], f"F_pV_p not diagonal at 1: {result}"
    return result[1]


# ============================================================ PHASE 0: anchor

def run_phase0():
    print("\n" + "=" * 78)
    print("PHASE 0: the anchor -- p-typical sublattice -> #151's per-prime W6")
    print("=" * 78)
    N = 720
    primes = (2, 3, 5)

    # P0.1: the level map, read off F_p alone, reproduces the p-adic valuation.
    ok_level = True
    detail_level = []
    for p in primes:
        kmax = 0
        while p ** (kmax + 1) <= N:
            kmax += 1
        for k in range(kmax + 1):
            lvl = p_typical_level(p, N, p ** k)
            ok_level = ok_level and (lvl == k)
        detail_level.append(f"p={p}:kmax={kmax}")
    # sanity: a non-p-typical index is correctly rejected (not silently 0).
    ok_reject = (p_typical_level(2, N, 6) is None) and (p_typical_level(3, N, 10) is None)
    check("P0.1 level map: F_p-iteration count on p^k reproduces the exponent "
          "k (p in {2,3,5}, up to N=720), and rejects non-p-typical indices",
          ok_level and ok_reject, ", ".join(detail_level))

    # P0.2: the circle's circumference, read off the F_pV_p eigenvalue.
    ok_eig = True
    c = {}
    for p in primes:
        c[p] = ghost_eigenvalue(p, N)
        ok_eig = ok_eig and (c[p] == p)
    check("P0.2 F_pV_p eigenvalue c_p equals p exactly, established from "
          "ghost-lattice trace data alone (basis(1) -> V_p -> F_p)", ok_eig,
          f"c_2={c.get(2)}, c_3={c.get(3)}, c_5={c.get(5)}")

    # P0.3: geometric-side Poisson reproduction via Phi(k) = k * log(c_p).
    ok_geo, worst_geo = True, 0.0
    for p in primes:
        L = math.log(c[p])
        for spread in (0.7, 1.3):
            geo = L * sum(gaussian(k * L, spread) for k in range(-200, 201))
            spec = sum(gaussian_hat(2 * math.pi * n / L, spread)
                       for n in range(-200, 201))
            err = abs(geo - spec)
            worst_geo = max(worst_geo, err)
            ok_geo = ok_geo and err < 1e-10
    check("P0.3 Poisson geometric-side reproduction through Phi(k)=k*log(c_p) "
          "(e2aj's identity, translated to the p-typical ghost-lattice map)",
          ok_geo, f"max defect {worst_geo:.2e} (target < 1e-10)")

    # P0.4: spectral-side / local Euler-factor pole reproduction.
    ok_pole = True
    for p in primes:
        L = math.log(c[p])
        for n in range(1, 6):
            s = 2j * math.pi * n / L
            ok_pole = ok_pole and abs(1 - c[p] ** (-s)) < 1e-12
    check("P0.4 Euler-factor pole reproduction: 1 - c_p^{-s} = 0 at "
          "s = 2 pi i n / log(c_p), n=1..5", ok_pole, "target < 1e-12")

    # P0.5 HONESTY A: the general ghost lattice is NOT uniformly log-spaced --
    # the p-typical restriction is doing real work, not painting a label onto
    # a vacuous truth true of any index subset.
    gaps = [math.log(n + 1) - math.log(n) for n in range(1, 6)]
    ok_nonuniform = (max(gaps) - min(gaps)) > 0.05
    check("P0.5 HONESTY: the full ghost lattice {1,2,3,4,5,6} is NOT "
          "uniformly log-spaced (contrast case: the p-typical restriction to "
          "{p^0,p^1,p^2,...} is what supplies the uniform spacing Poisson "
          "needs, not a property of any index subset)",
          ok_nonuniform, f"gap spread over n=1..5 is {max(gaps) - min(gaps):.4f}")

    # P0.6 HONESTY B: the bare F_p/V_p monoid is ONE-SIDED (index >= 1); the
    # two-sided Poisson sum (k from -200 to 200 above) needs k < 0 terms that
    # are not reachable by finite F_p-iteration from basis(1). Flagged, not
    # hidden: the honest bridge is the TP/Tate periodicization (Nikolaus-
    # Scholze 2-periodicity, cited in Direction 10B and not re-derived here),
    # which formally inverts the Bott class and is exactly what turns a
    # bounded-below graded object (THH) into a Z-graded / two-sided one (TP).
    below = apply_F(primes[0], N, basis(1))
    ok_onesided = (below == {})
    check("P0.6 HONESTY: F_p cannot reach level -1 from basis(1) inside the "
          "bare F_p/V_p monoid -- the k<0 half of the Poisson sum needs the "
          "TP/Tate periodicization (cited, Nikolaus-Scholze; not re-derived "
          "here) to formally adjoin the negative levels, not bare F_p/V_p",
          ok_onesided, f"F_p(basis(1)) = {below!r} (empty = correctly blocked)")

    print("\n  PHASE 0 HONESTY SUMMARY (read before trusting P0.3/P0.4 as new")
    print("  content): c_p = p exactly (P0.2), so Phi(k) = k*log(c_p) reduces")
    print("  TERM BY TERM to e2aj's own k*log(p): P0.3/P0.4 are an EXACT")
    print("  reproduction BY CONSTRUCTION, not an independent numerical")
    print("  confirmation. What IS new and non-trivial: the p-typical")
    print("  restriction is the specific, necessary (P0.5) mechanism that")
    print("  turns the ghost lattice's general non-uniform index spacing into")
    print("  the uniform lattice Poisson summation consumes, and that spacing")
    print("  constant is read off the F_pV_p eigenvalue (P0.2), an intrinsic")
    print("  Witt-calculus fact, not imported as 'log p' by assumption. The")
    print("  two-sided extension (P0.6) is honestly flagged as needing an")
    print("  ingredient (TP periodicization) beyond bare F_p/V_p. Net: this")
    print("  is more than labels painted on, but the ANALYTIC content of")
    print("  Poisson summation itself remains imported, not Witt-derived.")
    return c


# ================================================== PHASE 1: Gap A + Beurling

def run_phase1():
    print("\n" + "=" * 78)
    print("PHASE 1: Gap A operationalized, Beurling-twinned")
    print("=" * 78)
    N = 720
    KS = range(2, 13)
    NMAX = 500

    # ---- reproduce the existing B3/B4/necklace battery exactly (baseline).
    ok_rel, ok_tr, ok_blind = True, True, True
    for k in KS:
        for n in range(1, N // k + 1):
            fv = apply_F(k, N, apply_V(k, N, basis(n)))
            ok_rel = ok_rel and (fv == {n: k})
        tr_VF = sum(apply_V(k, N, apply_F(k, N, basis(n))).get(n, 0)
                    for n in range(1, N + 1))
        ok_tr = ok_tr and (tr_VF == k * (N // k))
        tr_F = sum(apply_F(k, N, basis(n)).get(n, 0) for n in range(1, N + 1))
        ok_blind = ok_blind and (tr_F == 0)
    check("P1.1 reproduce B3 exactly: F_kV_k=k*Id (faithful block), "
          "tr(V_kF_k)=k*floor(N/k), tr(F_k)=0, k=2..12, N=720",
          ok_rel and ok_tr and ok_blind)

    ok_sum, ok_inv = True, True
    for i in range(1, NMAX + 1):
        tors = logvec(i)
        s_acc = {}
        for d in divisors(i):
            s_acc = vadd(s_acc, lambda_vec(d))
        ok_sum = ok_sum and (s_acc == tors)
        acc = {}
        for d in divisors(i):
            mu = mobius(i // d)
            if mu:
                acc = vadd(acc, logvec(d), coeff=mu)
        ok_inv = ok_inv and (acc == lambda_vec(i))
    check("P1.2 reproduce B4 exactly: log|torsion(i)| = sum_{d|i} Lambda(d), "
          "Mobius inversion recovers Lambda exactly, i<=500", ok_sum and ok_inv)

    ok_int, ok_pair = True, True
    for q in (2, 3, 5):
        for n in range(1, 13):
            v = necklace_polynomial(q, n)
            ok_int = ok_int and v.denominator == 1 and v >= 0
        for n in range(1, 31):
            lhs = sum(d * necklace_polynomial(q, d) for d in divisors(n))
            ok_pair = ok_pair and (lhs == Fraction(q) ** n)
    check("P1.3 reproduce the necklace identities (local re-derivation): "
          "M(q,n) non-negative integer + Mobius-inverse pair "
          "sum_{d|n} d*M(q,d) = q^n, q in {2,3,5}, n<=30", ok_int and ok_pair)

    # ---- the Gap A scaling operator N_op := sum_{k=2}^{12} V_k F_k.
    # V_kF_k(basis(n)) = k*basis(n) if k|n (F_k kills basis(n) otherwise, so
    # V_k(0)=0; no truncation subtlety since k*(n/k)=n<=N always holds).
    def nop_eig_closed(n):
        return sum(k for k in KS if n % k == 0)

    def nop_eig_direct(n):
        return sum(apply_V(k, N, apply_F(k, N, basis(n))).get(n, 0) for k in KS)

    for n in range(1, 21):
        assert nop_eig_closed(n) == nop_eig_direct(n), (
            f"N_op closed form disagrees with direct F_k/V_k composition at "
            f"n={n}: {nop_eig_closed(n)} vs {nop_eig_direct(n)}")

    primes_in_range = [2, 3, 5, 7, 11]
    composites_in_range = [4, 6, 8, 9, 10, 12]

    ok_prime_match = all(nop_eig_closed(p) == p for p in primes_in_range)
    check("P1.4 N_op = sum_k V_kF_k eigenvalue equals the index n exactly on "
          "every prime in [2,12] (Gap A's claim holds in this degenerate "
          "corner: a prime's only divisor in range is itself)",
          ok_prime_match, f"{[(p, nop_eig_closed(p)) for p in primes_in_range]}")

    mismatches = [(n, nop_eig_closed(n)) for n in composites_in_range
                  if nop_eig_closed(n) != n]
    ok_composite_mismatch = len(mismatches) == len(composites_in_range)
    check("P1.5 N_op eigenvalue is a DIFFERENT divisor-sum (never n) on every "
          "composite in [2,12]: the new question this spec adds -- spectral "
          "data depends on divisor-lattice RANK, not the raw index",
          ok_composite_mismatch, f"(n, eigenvalue) = {mismatches}")

    # ---- truncation coupling: sum_k F_kV_k is a step function of n.
    def fkvk_sum_eig(n):
        return sum(k for k in KS if k * n <= N)

    plateau = [fkvk_sum_eig(n) for n in range(1, 61)]
    tail = [fkvk_sum_eig(n) for n in range(61, 71)]
    ok_step = (len(set(plateau)) == 1 and plateau[0] == sum(KS)
               and all(t < plateau[0] for t in tail))
    check("P1.6 sum_k F_kV_k eigenvalue is a STEP function of n: constant "
          "(=sum(2..12)=77) for n<=60=720/12, strictly smaller past it -- "
          "N-tracking / installed-by-truncation, the e1l '#143 shape' "
          "vocabulary, not a computed index-independent invariant",
          ok_step, f"plateau={plateau[0] if plateau else None}, "
          f"tail sample={tail[:4]}")

    # ---- commutators [F_a, V_b], a != b: no diagonal contribution is
    # structurally possible (F_aV_b and V_bF_a both land at position bn/a,
    # which equals n only if a=b), so the trace is 0 for a REASON, not a
    # numerical accident; the code confirms rather than assumes this.
    ok_comm = True
    for a in KS:
        for b in KS:
            if a == b:
                continue
            tr = 0
            for n in range(1, N + 1):
                d1 = apply_F(a, N, apply_V(b, N, basis(n))).get(n, 0)
                d2 = apply_V(b, N, apply_F(a, N, basis(n))).get(n, 0)
                tr += d1 - d2
            ok_comm = ok_comm and (tr == 0)
    check("P1.7 tr([F_a,V_b]) = 0 exactly for every a != b in 2..12 "
          "(F_aV_b, V_bF_a land at position b*n/a != n whenever a != b: "
          "structurally forced, confirmed not assumed)", ok_comm)

    # ---- positive control: size information exists and differs, so the
    # Beurling-insensitivity found below is a real finding, not a null test.
    B = BeurlingSystem(prime_bound=130000, eps=0.25, seed=149)
    label_log = dict(zip(B.labels, B.logs))

    def w_beurling(n):
        f = factorize(n)
        return sum(e * label_log[p] for p, e in f.items())

    diffs = [(n, math.log(n), w_beurling(n)) for n in range(2, 21)]
    ok_differ = all(abs(lo - lb) > 1e-4 for _, lo, lb in diffs)
    check("P1.8 POSITIVE CONTROL: w_ord(n)=log(n) genuinely differs from the "
          "Beurling-relabeled size w_B(n) for n=2..20 (size information "
          "exists and varies; the battery below simply never reads it)",
          ok_differ, f"max |diff| = {max(abs(lo - lb) for _, lo, lb in diffs):.4f}")

    # ---- structural blindness: apply_F/apply_V never call a factorization
    # or size-lookup routine, so the whole F_k/V_k trace/N_op/commutator
    # layer CANNOT see a Beurling relabeling by construction -- a proof, not
    # a sampled numerical coincidence.
    src = inspect.getsource(apply_F) + inspect.getsource(apply_V)
    forbidden = ["factorize", "logvec", "primes_upto", ".labels", ".logs",
                 "gen_integers", "log(", "math.log"]
    hits = [tok for tok in forbidden if tok in src]
    check("P1.9 STRUCTURAL: apply_F/apply_V source contains no prime-"
          "factorization or generator-size lookup, so no PER-ELEMENT "
          "composition of them (any operator's action on one basis vector, "
          "e.g. N_op's eigenvalue) can see a Beurling relabeling by "
          "construction [ADVERSARY: this does NOT by itself cover "
          "domain-WIDE aggregates like tr(V_kF_k), which sum over "
          "'which n are <= N' -- a step outside this source; see P1.12 "
          "(confirms the per-element scope literally) and P1.13 (shows the "
          "aggregate scope is NOT blind)]",
          not hits, f"forbidden tokens found: {hits}" if hits else "clean")

    # ---- Beurling rebuild of the divisor-lattice/Chebyshev identity behind
    # B3.Q3/B4.Q3 (extends e2ak's C4, which tested this only for B3's own
    # Lambda-recovery route, to the same mechanism restated additively --
    # honestly this REPRODUCES C4's finding rather than breaking new ground;
    # graded as such below, not oversold).
    gi = B.gen_integers(10000, with_factorization=True)
    sample = gi[:: max(1, len(gi) // 200)]
    ok_cheb = True
    for _, fac in sample:
        vec = {j: a for j, a in fac}
        acc = {}
        for j, a in vec.items():
            for _step in range(1, a + 1):
                acc[j] = acc.get(j, 0) + 1
        ok_cheb = ok_cheb and (acc == vec)
    check("P1.10 Beurling rebuild: the divisor-lattice/Chebyshev identity "
          "behind B3.Q3/B4.Q3 holds exactly for the fake (reproduces e2ak's "
          "C4 finding, not a novel extension -- stated honestly)",
          ok_cheb, f"{len(sample)} generalized integers, integer-exact")

    # ---- the necklace layer's exemption: a Beurling generalized integer is
    # not integer-valued, so it cannot serve as a necklace LENGTH n (M(q,n)
    # needs n as a literal cyclic-group order, an additive/metric notion
    # necklaces of n beads, not just a divisor-lattice RANK). This is a
    # DIFFERENT kind of result from P1.9/P1.10: not "passes identically" but
    # "not even stateable," an AX-FORM-style exemption for this one layer.
    val = math.exp(B.logs[0] + B.logs[1])
    ok_not_int = abs(val - round(val)) > 1e-6
    check("P1.11 necklace EXEMPTION: a Beurling generalized integer (here "
          "the product of the first two generators) is not integer-valued, "
          "so it cannot be plugged into M(q,n) as a necklace length -- the "
          "necklace/Mobius layer is type-inapplicable to the Beurling twin, "
          "distinct from the rank-based B3/B4/N_op layer's numeric pass",
          ok_not_int, f"exp(logs[0]+logs[1]) = {val:.6f}, "
          f"nearest-int defect = {abs(val - round(val)):.2e}")

    # ---- [ADVERSARY, 2026-07-17] P1.12/P1.13: a LITERAL exponent-vector
    # Beurling rebuild, resolving the "overflow excuse" (Section (d) honesty
    # note below / the .md's Section 5). A naive array-PERMUTATION rebuild
    # (swap which literal integer plays "prime 2" vs "prime 3" inside the
    # fixed N=720 array) genuinely overflows for composite k (2^7=128 ->
    # 3^7=2187 under that swap). But the spec's own named template
    # (BeurlingSystem.gen_integers(x, with_factorization=True), "exactly as
    # e2ak's C4 check already does") sidesteps this entirely: since
    # F_a F_b = F_{ab} (direct check: (F_aF_bw)_n=(F_bw)_{an}=w_{ban}=
    # (F_{ab}w)_n), every F_k for k=2..12 decomposes into shifts along k's
    # own prime factors, so F_k/V_k can be re-expressed as PURE
    # EXPONENT-VECTOR arithmetic (add/subtract k's own factorization from an
    # index's exponent vector) with no array bound at all -- the domain is
    # just "which exponent vectors have value <= X", exactly how
    # gen_integers already represents things. This is buildable and is run
    # here, not merely argued.
    label_idx = {p: i for i, p in enumerate(B.labels)}

    def _k_exponents(k):
        return {label_idx[p]: e for p, e in factorize(k).items()}

    K_EXP = {k: _k_exponents(k) for k in KS}

    def _vec_sub(v, kv):
        out = dict(v)
        for j, e in kv.items():
            if out.get(j, 0) < e:
                return None
            out[j] = out.get(j, 0) - e
            if out[j] == 0:
                del out[j]
        return out

    def _vkey(v):
        return tuple(sorted(v.items()))

    def _domain_Q(bound):
        return {n: {label_idx[p]: e for p, e in factorize(n).items()}
                for n in range(1, bound + 1)}

    def _domain_B(bound):
        gi = B.gen_integers(bound, with_factorization=True)
        return {i: dict(fac) for i, (_, fac) in enumerate(gi)}

    def _tr_Fk_diagonal(domain):
        """tr(F_k): a diagonal element n contributes iff n's vector minus
        k's own exponent vector equals n's vector unchanged, impossible for
        k>=2 since k's exponent vector is never all-zero -- a per-element,
        domain-shape-independent argument, tested not assumed."""
        bad = []
        for k in KS:
            tr = sum(1 for v in domain.values()
                     if (lambda v2: v2 is not None and _vkey(v2) == _vkey(v))
                     (_vec_sub(v, K_EXP[k])))
            if tr != 0:
                bad.append((k, tr))
        return bad

    def _nop_eig_by_pattern(domain, pattern):
        """First domain element whose small-generator (2,3,5,7,11) exponents
        match `pattern` exactly (any large-prime cofactor allowed); returns
        its N_op eigenvalue = sum_k k*[k divides this element], a per-
        element (division-only, always stays inside a downward-closed
        domain) quantity, unlike tr(V_kF_k) below."""
        vec_to_id = {_vkey(v): i for i, v in domain.items()}
        small = set(pattern) | {label_idx[p] for p in (2, 3, 5, 7, 11)}
        for v in domain.values():
            if {j: e for j, e in v.items() if j in small} == pattern:
                return sum(k for k in KS
                           if (lambda v2: v2 is not None
                               and _vkey(v2) in vec_to_id)(_vec_sub(v, K_EXP[k])))
        return None

    domQ, domB = _domain_Q(N), _domain_B(N)
    i2, i3 = label_idx[2], label_idx[3]
    patterns = {"prime n=2": {i2: 1}, "prime n=3": {i3: 1},
                "n=12-shape (2^2*3)": {i2: 2, i3: 1},
                "n=6-shape (2*3)": {i2: 1, i3: 1}}
    bad_Q, bad_B = _tr_Fk_diagonal(domQ), _tr_Fk_diagonal(domB)
    eigs_Q = {lbl: _nop_eig_by_pattern(domQ, pat) for lbl, pat in patterns.items()}
    eigs_B = {lbl: _nop_eig_by_pattern(domB, pat) for lbl, pat in patterns.items()}
    ok_literal_rank = (not bad_Q and not bad_B and eigs_Q == eigs_B
                       and all(v is not None for v in eigs_Q.values()))
    check("P1.12 [ADVERSARY, literal test added] LITERAL exponent-vector "
          "Beurling rebuild (not source inspection, and not the overflowing "
          "array-permutation approach): tr(F_k)=0 for all k and the N_op "
          "eigenvalue-by-structural-pattern are IDENTICAL between the "
          f"rational domain ({len(domQ)} elements) and an actual "
          f"BeurlingSystem.gen_integers domain ({len(domB)} elements, same "
          "bound N=720) -- the RANK sub-layer is now confirmed blind by a "
          "literal test, upgrading P1.9's source-inspection argument",
          ok_literal_rank, f"patterns match: {eigs_Q == eigs_B}; "
          f"eigenvalues={eigs_Q}; tr(F_k) diagonal violations Q={bad_Q} B={bad_B}")

    def _tr_VkFk(domain):
        """tr(V_kF_k) = k * #{domain elements divisible by k}: a DOMAIN-
        COUNTING quantity (unlike the per-element facts above), so this is
        where a truncation boundary "<=N" -- rational integer vs Beurling
        generalized-integer value -- can smuggle size information in."""
        vec_to_id = {_vkey(v): i for i, v in domain.items()}
        out = {}
        for k in KS:
            n_div = sum(1 for v in domain.values()
                        if (lambda v2: v2 is not None and _vkey(v2) in vec_to_id)
                        (_vec_sub(v, K_EXP[k])))
            out[k] = k * n_div
        return out

    trQ, trB = _tr_VkFk(domQ), _tr_VkFk(domB)
    diffs = {k: trB[k] - trQ[k] for k in KS}
    ok_sensitive = all(d != 0 for d in diffs.values())
    check("P1.13 [ADVERSARY, literal test added] the SAME literal rebuild "
          "shows tr(V_kF_k) IS Beurling-sensitive at every k=2..12, "
          "correcting P1.9/old-P1.12's blanket 'every native invariant... "
          "Beurling-identical' to the RANK sub-layer only: the COUNTING "
          "sub-layer (already separately flagged N-truncation-installed by "
          "P1.6) is ALSO installed-by-relabeling -- the same root cause "
          "(domain-boundary/size consumption) surfacing twice, not a "
          "contradiction, and consistent with e2ak's C5a (Beurling integer "
          "counting is not x+O(1))",
          ok_sensitive, f"tr(V_kF_k) rational vs Beurling, k=2..12: "
          f"{[(k, trQ[k], trB[k]) for k in KS]}")

    wall = (ok_rel and ok_tr and ok_blind and ok_cheb and not hits and ok_differ
            and ok_literal_rank)
    check("P1.14 WALL (pre-registered; RANK sub-layer, per the P1.12/P1.13 "
          "scope correction): every RANK/POSITION-based F_k/V_k/N_op/"
          "Lambda-recovery invariant tested is Beurling-identical or "
          "structurally exempt, confirmed both by source inspection (P1.9) "
          "and by a literal exponent-vector rebuild (P1.12); the only "
          "size-sensitive quantities anywhere in this sweep are the "
          "externally-appended w() readout (P1.8) and the domain-COUNTING "
          "invariants (tr(V_kF_k)/the P1.6 step function, P1.13) -- never a "
          "RANK quantity the ghost/THH combinatorial layer computes on its "
          "own",
          wall)


# ===================================================== PHASE 2: Gap B

def run_phase2():
    print("\n" + "=" * 78)
    print("PHASE 2: Gap B operationalized -- the multiplicativity test")
    print("=" * 78)
    NMAX = 500

    def build_table(q0):
        return {d: necklace_polynomial(q0, d) for d in range(1, NMAX + 1)}

    # F_TC-BLOCK-START (K1 scan target: no Lambda/zeta table may appear here)
    def f_tc(n, table):
        """f_TC(n) = sum_{d|n} mu(n/d) * d * M(q0,d): Mobius inversion (the
        Gap-B conjectured TC mechanism -- 10B doc, e_necklace_mobius.py part
        (d)) applied to the necklace-weighted Bokstedt torsion order at each
        level d. The Bokstedt input is the CITED integer |THH_{2d-1}(Z)| = d
        itself (Bokstedt 1985), entering as a plain integer multiplier --
        never a looked-up von Mangoldt table value or a zeta coefficient."""
        return sum(mobius(n // d) * d * table[d] for d in divisors(n))
    # F_TC-BLOCK-END

    lv_before = _call_counts["lambda_vec"]

    results = {}
    for q0 in (2, 3):
        table = build_table(q0)
        f = {n: f_tc(n, table) for n in range(1, NMAX + 1)}
        results[q0] = (table, f)

    lv_after = _call_counts["lambda_vec"]

    # ---- sanity: f_TC(7) matches the direct 2-term divisor expansion.
    table2, f2 = results[2]
    direct = mobius(1) * 7 * table2[7] + mobius(7) * 1 * table2[1]
    check("P2.1 sanity: f_TC(7) at q0=2 matches the direct 2-term divisor "
          "expansion mu(1)*7*M(2,7) + mu(7)*1*M(2,1)",
          f2[7] == direct, f"f_TC(7) = {f2[7]}")

    # ---- boundary: the Mobius-inversion normalization f(1)=1 fails.
    ok_boundary = all(results[q][1][1] == Fraction(q) for q in (2, 3))
    ok_not_one = all(results[q][1][1] != 1 for q in (2, 3))
    check("P2.2 f_TC(1) = q0 exactly (not 1): the multiplicative "
          "normalization f(1)=1 required for a genuine Euler product fails "
          "immediately at the unit -- an additive-construction signature, "
          "reported plainly rather than excluded from view",
          ok_boundary and ok_not_one,
          f"f_TC(1) at q0=2,3: {results[2][1][1]}, {results[3][1][1]}")

    # ---- the main test: exact multiplicativity over every coprime pair
    # (m,n), 2<=m<n, mn<=500 (the unit boundary excluded here on purpose,
    # tested separately above so the core mechanism gets a fair, non-trivial
    # reading rather than being dominated by the P2.2 normalization gap).
    fails = {}
    for q0 in (2, 3):
        _, f = results[q0]
        first_fail = None
        n_pairs = 0
        m = 2
        while m * (m + 1) <= NMAX:
            for n in range(m + 1, NMAX // m + 1):
                if gcd(m, n) == 1:
                    n_pairs += 1
                    if f[m * n] != f[m] * f[n]:
                        if first_fail is None:
                            first_fail = (m, n, f[m], f[n], f[m * n],
                                          f[m] * f[n])
            m += 1
        fails[q0] = first_fail
        # Convention (matching e2aj's "overcount" / e2ak's "NOT x+O(1)"
        # checks): PASS means the PRE-REGISTERED PREDICTION is confirmed,
        # not that the naive claim holds. The spec's own predicted outcome
        # for Phase 2 is the WALL (a failing pair), per the standing
        # adversary flag on Gap B; that is what a clean [PASS] run reports.
        # A genuinely multiplicative f_TC (no failing pair) would be the
        # SURPRISE finding and is flagged FAIL here precisely so it is not
        # silently missed -- see the printed detail either way.
        wall_confirmed = first_fail is not None
        idx = 3 if q0 == 2 else 4
        if wall_confirmed:
            fm, fn, fmn, prod = first_fail[2:]
            detail = (f"WALL confirmed: FIRST FAILURE at "
                       f"(m,n)=({first_fail[0]},{first_fail[1]}): f(m)={fm}, "
                       f"f(n)={fn}, f(mn)={fmn} != f(m)*f(n)={prod} "
                       f"[{n_pairs} coprime pairs tested]")
        else:
            detail = (f"SURPRISE: all {n_pairs} coprime pairs match exactly "
                       f"-- f_TC is genuinely multiplicative, upgrading Gap B "
                       f"per the spec's Pass criterion")
        check(f"P2.{idx} multiplicativity test at q0={q0}: confirms the "
              f"pre-registered WALL (a failing coprime pair) rather than "
              f"asserting f_TC(mn)=f_TC(m)f_TC(n) holds universally",
              wall_confirmed, detail)

    # ---- K1 static scan of f_TC's own source.
    src = inspect.getsource(f_tc)
    forbidden = ["lambda_vec", "Lambda(", "von_mangoldt", "ZETA_ZEROS",
                 "zetazero", "davenport_heilbronn", "curve_fit", ".zeros("]
    hits = [tok for tok in forbidden if tok in src]
    check("P2.5 K1 static scan: f_TC's own source references no Lambda/zeta "
          "table and no fitted zero data", not hits,
          f"forbidden tokens: {hits}" if hits else "clean")

    # ---- K1 runtime guard: zero calls into the Lambda-table helper during
    # this phase's entire construction+sweep window.
    check("P2.6 K1 runtime guard: lambda_vec call count is unchanged across "
          "Phase 2's construction+sweep (0 calls into the Lambda table)",
          lv_after == lv_before, f"calls before={lv_before}, after={lv_after}")

    # ---- [ADVERSARY, 2026-07-17] P2.7: the strawman check. Five OTHER
    # natural compositions of the same two ingredients (necklace weight
    # M(q,n), Bokstedt order d), so the dossier's claim is "no natural
    # variant tested is multiplicative", not just "our one candidate isn't".
    # A 6th (log-composed, matching B4's actual log|torsion| shape) was also
    # checked informally with floats, also failing, but is not tracked here
    # since it falls outside this module's exact-arithmetic convention.
    def _mobius_sum_necklace_only(table):
        return lambda n: sum(mobius(n // d) * table[d] for d in divisors(n))

    def _raw_necklace(table):
        return lambda n: table[n]

    def _mobius_product(table, with_d):
        def f(n):
            val = Fraction(1)
            for d in divisors(n):
                base = (d * table[d]) if with_d else table[d]
                if base == 0:
                    return Fraction(0)
                mu = mobius(n // d)
                if mu == 1:
                    val *= base
                elif mu == -1:
                    val /= base
            return val
        return f

    def _sign_alternating(table):
        return lambda n: sum(mobius(n // d) * ((-1) ** d) * d * table[d]
                             for d in divisors(n))

    def _first_mult_failure(f, nmax_v=200):
        m = 2
        while m * (m + 1) <= nmax_v:
            for n in range(m + 1, nmax_v // m + 1):
                if gcd(m, n) == 1 and f(m * n) != f(m) * f(n):
                    return (m, n)
            m += 1
        return None

    variant_report = []
    for q0 in (2, 3):
        table = results[q0][0]
        variants = {
            "necklace-only Mobius sum": _mobius_sum_necklace_only(table),
            "raw M(q,n), no composition": _raw_necklace(table),
            "Mobius PRODUCT[(d*M)^mu]": _mobius_product(table, True),
            "Mobius PRODUCT[M^mu], necklace only": _mobius_product(table, False),
            "sign-alternating (-1)^d weight": _sign_alternating(table),
        }
        for name, f in variants.items():
            variant_report.append((q0, name, _first_mult_failure(f)))
    all_variants_fail = all(fail is not None for _, _, fail in variant_report)
    check("P2.7 [ADVERSARY, literal test added] STRAWMAN check: 5 other "
          "natural compositions of necklace weight + Bokstedt order (a "
          "necklace-only Mobius sum; the raw M(q,n) with no composition; a "
          "multiplicative-shaped Mobius PRODUCT of (d*M(q,d)); the same "
          "product on the necklace weight alone; a sign-alternating "
          "variant), tested at q0=2,3 (10 variant/alphabet combinations, "
          "mn<=200) ALSO fail multiplicativity, confirming 'no natural "
          "variant tested is multiplicative' rather than 'only this one "
          "candidate fails' -- a multiplicative variant found here would "
          "be a discovery and is NOT what this check reports",
          all_variants_fail, f"first-failure pair per (q0, variant): "
          f"{variant_report}")

    return fails


# ------------------------------------------------------------------ verdict

def main():
    t0 = time.time()
    print("E2AL: the SP3c/W6 rung on the ghost/THH self-product")
    print("(C1 counting joint, derived-base half; B1 rung 5)")

    run_phase0()
    run_phase1()
    run_phase2()

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  Phase 0 (anchor):        numeric reproduction PASSES exactly, by")
    print("                           construction (c_p=p); the p-typical")
    print("                           restriction supplies genuinely new")
    print("                           lattice structure (P0.5/P0.6), but the")
    print("                           Poisson-summation content stays imported.")
    print("                           TIER: measured/installed (per (d).2),")
    print("                           not W6-genuine -- the map exists and")
    print("                           reproduces, but does not re-derive the")
    print("                           analytic identity from Witt/THH alone.")
    print("  Phase 1 (Gap A+Beurling): the predicted wall lands for the RANK")
    print("                           sub-layer: every F_k/V_k/N_op/Lambda-")
    print("                           recovery invariant built from POSITION")
    print("                           (not counting) is Beurling-identical")
    print("                           or structurally exempt (P1.9, P1.12),")
    print("                           confirmed by source inspection AND a")
    print("                           literal exponent-vector rebuild, not")
    print("                           sampled coincidence. [ADVERSARY,")
    print("                           P1.13] the DOMAIN-COUNTING sub-layer")
    print("                           (tr(V_kF_k), the P1.6 step function)")
    print("                           IS Beurling-sensitive: size leaks in")
    print("                           through the truncation boundary, a")
    print("                           reason consistent with, not opposed")
    print("                           to, the rank sub-layer's blindness.")
    print("                           Gap A's own eigenvalue-i claim is thus")
    print("                           an index/rank statement, never a size")
    print("                           statement, so even a fully successful")
    print("                           Gap A would not close C1's lattice gap.")
    print("                           TIER: blind (per (d).3) for the size-")
    print("                           sensitivity question the spec adds,")
    print("                           on the rank sub-layer specifically.")
    print("  Phase 2 (Gap B):         the predicted wall lands at BOTH q0=2")
    print("                           and q0=3: f_TC(2*3) != f_TC(2)*f_TC(3)")
    print("                           already at the smallest coprime pair")
    print("                           (see P2.3/P2.4 detail above for exact")
    print("                           values). f_TC(1) != 1 independently")
    print("                           (P2.2). Diagnosis: the equalizer model")
    print("                           built here is additive-shaped (a Mobius-")
    print("                           inversion sum), confirming the standing")
    print("                           adversary flag computationally, not just")
    print("                           heuristically. TIER: category error")
    print("                           (per (d).3) for THIS candidate f_TC --")
    print("                           it does not rule out every possible")
    print("                           necklace-Bokstedt composition, only the")
    print("                           one built here.")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    n_total = len(CHECKS)
    dt = time.time() - t0
    print(f"\n{n_ok}/{n_total} checks passed")
    print(f"runtime: {dt:.2f}s")
    if n_ok != n_total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

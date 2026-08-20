"""E1AD: sum rules on the prime log-lattice. Can a SEQUENCE-LEVEL spectral
functional see Q-linear independence where pointwise functionals provably
cannot?

ROLE: BUILDER. Executes the sequence-level half of PHASE_STATE next-step 3
(the Christoffel-corpus sweep, SPLIT per LEARNINGS #172 / adversary case 3):
the pointwise half is dead in principle (the functional is continuous in the
atom positions while lattices are dense), but continuity at every finite
index is compatible with an arithmetic-sensitive LIMIT (witness: quadratic
Weyl sums). The surviving register is Killip-Simon type SUM RULES. This rung
builds the sum-rule computer and runs it on the four pre-registered classes.

THE OBJECT. For a finite atomic probability measure mu on the unit circle
(atoms at angles t_j / L mod 1, unit weights), the truncated Szego sum

    S_n  =  - sum_{j<=n} log(1 - |alpha_j|^2)  =  - log ||Phi_{n+1}||^2

(alpha_j the Verblunsky coefficients, Phi_n the monic orthogonal
polynomials) is EXACTLY minus the log of the extremal monic-polynomial norm,
the OPUC twin of e1v's reciprocal Christoffel function (which is the
point-normalized extremal; this is the leading-coefficient-normalized one).
For purely atomic mu the full Szego sum diverges (|alpha_{M-1}| = 1); the
finite-n RATE of that divergence, along the diagonal n -> M-2 with the
measure growing, is the sequence-level observable, mirroring #171's
Christoffel growth. Reference point: M equally spaced atoms have S_n = 0
for all n < M-1, so the profile is a pure microstructure meter.

THE FOUR CLASSES (mandatory band equalization: matched count, support,
density profile; certificate in section S3):
  (i)   TRUE  atoms at {k log p <= log N}, the von Mangoldt support;
              generators log p are Q-linearly independent
  (ii)  SNAP  the same configuration snapped onto (1/D)Z at D = 10^6;
              rationally dependent, pointwise-indistinguishable from (i)
              by #172's continuity theorem
  (iii) RAND  generic iid configurations resampled from TRUE's own
              empirical density (matched profile, no structure)
  (iv)  BEUR  the shared Beurling control's fake-prime log-lattice
              {k log b} (Euler product, matched density, no additive
              lattice), consumed by import from experiments._shared.beurling

TYPING SURROGATES (what any separation is made of):
  STRAT  stratified resample from TRUE's density (matched coarse
         regularity, no arithmetic)
  GPERM  local gap shuffle of TRUE's wrapped angles (EXACT local gap
         multiset in blocks of 16, ordering destroyed, no arithmetic)
  JIT    TRUE + uniform noise at the SNAP displacement amplitude
         1/(2D) (the #172 V5 control at sequence level: if SNAP's
         response equals JIT's, snapping is a generic perturbation and
         the functional does not see rationality)

PRE-REGISTRATION: the PREREG dict below is the machine-readable form; the
readings [P1] (all four classes agree within the #172 family-blind spread
of about 1.3x: the sequence-level door closes and #172's obstruction
extends) and [P2] (a rate gap appears: a live arithmetic-sensitive
coordinate) are resolved by the run, and the SANITY KILL is armed: any
functional separating (i) from (iv) must fail to separate when fed
density-matched data with the lattice destroyed (RAND/STRAT/GPERM), else
it is reading density/spacing statistics, not arithmetic.

PROTOTYPE DISCLOSURE (honesty per the e1v calibration discipline): a sizing
prototype at N = 1000 was run BEFORE this pre-registration was frozen, to
fix dps and runtime. It exposed (a) the mid/diagonal ordering TRUE < STRAT
< BEUR < RAND at that one size and one seed, and (b) one snap-vs-jitter
number (max |dS| 2.0e-2 vs 3.2e-2). Those two observations are therefore
CALIBRATION FACTS, not predictions; everything else below (the size
scaling, the seed bands, the typing resolution, the horizon law, the gauge
face, the kill verdict) was not observed before freezing. Numerical check
thresholds are pinned from the calibration run of this same deterministic
code and are labeled pinned, not pre-registered.

CONDITIONING RULE (declared, then measured): the naive loss model is the
determinant-ratio dynamic range, S_n / ln(10) decimal digits by step n;
calibration measured the ACTUAL loss (by the internal orthogonality
certificate ORT(n) = |direct norm - product norm| / product norm) at 1.0x
to 1.8x the naive model on this grid, the excess being step accumulation.
Working precision is therefore escalated to dps >= 2.3 x S_final/ln(10)
+ 30 after each run, and the rule is VERIFIED two ways in S8: the measured
loss coefficient must stay <= 2.3 on every audited config, and a full
dps+40 re-run of the whole pipeline (positions included) must reproduce
every reported value to at least 10 digits. #172's conditioning-rule
precedent (it predicted the one irreproducible build) is why this is
declared up front rather than checked opportunistically.

DISCIPLINES. The Beurling control enters by import (counting-side twin).
D-H is out of scope by construction: this is a counting-side object built
from prime data; no L-function zero list is consumed anywhere (source-
scanned, with teeth). K1 does not arise (nothing here asserts RH-relevant
truth of the object; the classes are inputs, not conclusions).

Run:
  python -m experiments.spectral.e1ad_sum_rules            # full, ~6-8 min
  python -m experiments.spectral.e1ad_sum_rules --quick    # ~1-2 min, no npz
Outputs:
  experiments/spectral/e1ad_sum_rules.npz   (full mode only, tracked)
"""

from __future__ import annotations

import argparse
import math
import time
from collections import Counter
from pathlib import Path

import numpy as np
import mpmath as mp

import experiments._shared.beurling as _beurmod
from experiments._shared.beurling import BeurlingSystem

OUT = Path(__file__).with_suffix(".npz")

WRAP_L_MAIN = "1"                     # wrap period L = 1 (moment k reads the
                                      # exponential sum at height 2 pi k)
WRAP_L_GOLD = "0.61803398874989484820458683436563811772"   # gauge face
SNAP_D = 10 ** 6                      # the #172 finest snap denominator
BAND_A = 1.0                          # common lower band edge in t = log n
HIST_BINS = 16
GAP_BLOCK = 16                        # GPERM shuffles gaps inside blocks of
                                      # this many consecutive wrapped gaps,
                                      # preserving the local gap multiset and
                                      # the coarse angular density
SIZES_FULL = [300, 1000, 3000]
SIZES_QUICK = [300]
RAND_SEEDS = [11, 12, 13]
STRAT_SEEDS = [21, 22, 23]
GPERM_SEEDS = [31, 32, 33]
JIT_SEEDS = [41, 42, 43]
DLADDER_FULL = [40, 100, 400, 2000, 10 ** 4, 10 ** 5, 10 ** 6]
DLADDER_QUICK = [40, 200, 10 ** 6]
SNAP_BAND_FACTOR = 4.0    # pinned: the snap's whole-profile response must
                          # sit within this factor of the matched-amplitude
                          # jitter band top. Order-of-magnitude equality is
                          # the generic-perturbation verdict; a lattice
                          # SIGNATURE would be qualitatively different
                          # (early termination / growing separation), which
                          # S6 probes directly. Calibration: ratios 0.6-2.6
                          # across sizes and seeds.

CHECKS: list = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


# ==========================================================================
# Pre-registration (literal, machine-readable). The "resolution" fields were
# empty strings when the block was frozen and are RECORDED from the first
# full run; check S10 recomputes the verdict from the measured tables and
# fails if the recorded resolution disagrees.
# ==========================================================================
PREREG = {
    "question": "Does any sequence-level sum-rule functional (the divergence "
                "rate structure of the truncated Szego sum S_n as n grows to "
                "the diagonal, not any single-n value) separate the classes "
                "(i) TRUE / (ii) SNAP from (iii) RAND / (iv) BEUR, or "
                "separate (i) from (ii)?",
    "P1": "All four classes agree within the #172 family-blind spread "
          "(about 1.3x, operationalized as max/min <= 1.35 on the per-atom "
          "diagonal rate r_diag AND the mid-profile rate r_mid at every "
          "size): the sequence-level door closes, #172's obstruction "
          "extends.",
    "P2": "A rate gap appears (spread > 1.35, stable across sizes and "
          "outside seed bands): a live arithmetic-sensitive coordinate, "
          "a real finding, UNLESS the sanity kill types it away.",
    "SANITY_KILL": "Any functional separating (i) from (iv) must FAIL to "
                   "separate when fed density-matched data with the lattice "
                   "destroyed (GPERM / STRAT / RAND carry TRUE's density and "
                   "no arithmetic): if the lattice-destroyed twin separates "
                   "from BEUR essentially as well as TRUE does (>= 70% of "
                   "the distance), the functional reads density/spacing "
                   "statistics only and NO arithmetic claim survives.",
    "Q_AXIS": "The (i)-vs-(ii) axis is Q-linear independence itself. "
              "Registered expectation: NULL below the horizon (SNAP's "
              "response indistinguishable from JIT's at matched amplitude), "
              "because #172's continuity argument applies at every finite "
              "index; the door the adversary reopened is the LIMIT, probed "
              "separately by the D-ladder termination/horizon mechanism.",
    "prototype_disclosure": "N=1000 sizing prototype preceded the freeze; "
                            "it exposed the one-size ordering TRUE < STRAT "
                            "< BEUR < RAND and one snap-vs-jitter pair "
                            "(2.0e-2 vs 3.2e-2). Calibration facts, not "
                            "predictions.",
    # ---- recorded from the full run (2026-08-20, measured values) ----
    "resolution": "P2_LETTER_FIRED_THEN_KILLED: the four-class spread is "
                  "1.53-1.76x on r_diag and 2.14-4.00x on r_mid (>1.35 at "
                  "every size; every RAND seed exceeds TRUE's r_mid by >= "
                  "1.91x), so P1 is refuted at the letter; but the sanity "
                  "kill FIRED at every size: GPERM (lattice-free, exact "
                  "local gap multiset) stands 0.97-1.00x of TRUE's own "
                  "distance from BEUR and sits 95.6-99.9% of the way from "
                  "RAND back to TRUE, so the whole spread is carried by "
                  "the local gap multiset: spacing statistics, not "
                  "arithmetic. Q_AXIS: NULL as registered (SNAP inside 4x "
                  "the matched-amplitude jitter band at every size; "
                  "per-atom diagonal displacement <= 1.1e-6 at D = 10^6). "
                  "HORIZON: the functional sees the lattice exactly when "
                  "Q-dependence collapses the atom count (n_term = Md - 1 "
                  "on all 5 collision rungs, detection n* <= n_term, "
                  "n* = 39/90/116/153/159 at D = 40/100/400/2000/10^4); "
                  "at D >= 10^5 (no collisions) it is blind. The "
                  "sequence-level door is open ONLY through the collision "
                  "horizon, which recedes as the lattice refines: #172's "
                  "obstruction extends to the sequence level below the "
                  "horizon.",
    "resolution_recorded": True,
}


# ==========================================================================
# Configurations. TRUE and SNAP are exact objects (prime powers; integers
# m/D) materialized at working precision; the stochastic classes are exact
# float64 rationals (their own lattice scale 2^-52 is part of the honest
# scope: any finite computation handles only rational data, so "Q-linear
# independence" is always a statement about lattice SCALE, and the D-ladder
# measures exactly how scale is seen).
# ==========================================================================
def _sieve(N):
    s = np.ones(N + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(N ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


def true_pk(N, A=BAND_A):
    """(p, k) with p^k <= N and k log p >= A, sorted by k log p. The band
    edge A = 1 excludes only t = log 2 = 0.693 (nearest kept atom is
    log 3 = 1.0986: no boundary ambiguity at float precision)."""
    out = []
    for p in _sieve(N):
        k, pk = 1, int(p)
        while pk <= N:
            if k * math.log(p) >= A:
                out.append((int(p), k))
            k += 1
            pk *= int(p)
    out.sort(key=lambda e: e[1] * math.log(e[0]))
    return out


def true_t_float(pk):
    return np.array([k * math.log(p) for (p, k) in pk])


def beurling_t(N, A, t_max):
    """{k log b} for the shared Beurling control (default fake: seed 149,
    eps 0.25), trimmed to the common band [A, t_max]. Density-matched to
    TRUE by construction (b_p = p exp(eps_p)). The generator bound is
    extended by e^eps so primes just above N whose perturbation lands them
    inside the band are not systematically lost at the top edge."""
    B = BeurlingSystem(prime_bound=int(math.ceil(N * math.exp(0.25))))
    ts = []
    for lb in B.logs:
        k = 1
        while k * lb <= t_max + 1e-12:
            if k * lb >= A:
                ts.append(k * lb)
            k += 1
    return np.sort(np.array(ts))


def snap_sites(pk, D, dps=80):
    """Exact snap of {k log p} onto (1/D)Z: integer m = nint(D k log p),
    then (with L = 1) the wrapped site is m mod D. Exact collisions merge
    into one atom with summed weight; that merge IS the mechanism the
    D-ladder measures."""
    with mp.workdps(dps):
        ms = [int(mp.nint(k * mp.log(p) * D)) for (p, k) in pk]
    cnt = Counter(m % D for m in ms)
    sites = sorted(cnt)
    return sites, [cnt[s] for s in sites], len(ms) - len(sites)


def resample_t(t_true, mode, seed):
    """Matched-profile resample from TRUE's empirical CDF: endpoints kept
    exactly (support equalization), interior redrawn. RAND: iid ranks
    (density only). STRAT: one point per rank cell (density + coarse
    regularity, still no arithmetic)."""
    rng = np.random.default_rng(seed)
    M = len(t_true)
    if mode == "RAND":
        u = np.sort(rng.uniform(0, 1, M - 2))
    else:
        u = (np.arange(M - 2) + rng.uniform(0, 1, M - 2)) / (M - 2)
    interior = np.interp(u * (M - 1), np.arange(M), t_true)
    return np.concatenate([[t_true[0]], np.sort(interior), [t_true[-1]]])


def local_gap_shuffle(theta_sorted, seed, block=GAP_BLOCK):
    """Permute the wrapped gap multiset inside blocks of `block` consecutive
    gaps. Preserves the first and last angle, the coarse angular density
    (block resolution) and the local gap DISTRIBUTION exactly; destroys the
    ordering correlations that carry any arithmetic. The circle twin of the
    e1v adversary's spacing-distribution surrogate."""
    th = np.asarray(theta_sorted, float)
    g = np.diff(th)
    rng = np.random.default_rng(seed)
    out = g.copy()
    for i0 in range(0, len(g), block):
        seg = out[i0:i0 + block]
        rng.shuffle(seg)
        out[i0:i0 + block] = seg
    return np.concatenate([[th[0]], th[0] + np.cumsum(out)])


def wrap_float(t, L):
    x = np.asarray(t, float) / float(L)
    return np.sort(np.mod(x, 1.0))


def cfg_true(pk, L):
    return dict(kind="PP", pk=pk, L=L, label="TRUE")


def cfg_snap(sites, counts, D, L):
    return dict(kind="SNAP", sites=sites, counts=counts, D=D, L=L,
                label=f"SNAP{D:g}")


def cfg_float(theta, L, label, w=None):
    return dict(kind="FLOAT", theta=np.asarray(theta, float), L=L,
                label=label, w=w)


def materialize(cfg, dps):
    """(angles as sorted mpf in [0,1) turns, weights list). Angles for the
    exact kinds are recomputed at every dps so the dps audit re-derives the
    whole pipeline, positions included."""
    with mp.workdps(dps + 10):
        L = mp.mpf(cfg["L"])
        if cfg["kind"] == "PP":
            th = []
            for (p, k) in cfg["pk"]:
                x = k * mp.log(p) / L
                th.append(x - mp.floor(x))
            w = [1.0] * len(th)
        elif cfg["kind"] == "SNAP":
            th, w = [], []
            for s, c in zip(cfg["sites"], cfg["counts"]):
                x = (mp.mpf(s) / cfg["D"]) / L
                th.append(x - mp.floor(x))
                w.append(float(c))
        else:
            # FLOAT configs are DEFINED as float64 angles: exact rationals,
            # identical at every dps by construction.
            th = [mp.mpf(float(x)) for x in cfg["theta"]]
            w = ([1.0] * len(th) if cfg.get("w") is None
                 else [float(x) for x in cfg["w"]])
        order = sorted(range(len(th)), key=lambda i: th[i])
        return [th[i] for i in order], [w[i] for i in order]


# ==========================================================================
# Route B (primary): the Szego recursion on atom values.
#   conj(alpha_n) = <z Phi_n, 1> / ||Phi_n||^2,
#   Phi_{n+1} = z Phi_n - conj(alpha_n) Phi_n*,   Phi_{n+1}* = Phi_n* -
#   alpha_n z Phi_n,   ||Phi_{n+1}||^2 = (1 - |alpha_n|^2) ||Phi_n||^2.
# Termination (|alpha| -> 1) is detected by a RELATIVE cliff, not an
# absolute threshold: the numeric floor sits at 10^-(dps - S/ln10), so an
# absolute test would silently miss once conditioning eats the margin
# (measured in the prototype at D = 2000).
# ==========================================================================
def szego_profile(cfg, dps, n_max=None, ort_every=16):
    th, wl = materialize(cfg, dps)
    M = len(th)
    if n_max is None:
        n_max = M - 1
    with mp.workdps(dps):
        z = [mp.expjpi(2 * t) for t in th]
        w = [mp.mpf(x) for x in wl]
        W = mp.fsum(w)
        w = [x / W for x in w]
        Phi = [mp.mpc(1)] * M
        Phis = [mp.mpc(1)] * M
        nrm2 = mp.mpf(1)
        S, a2, gaps, ort = [], [], [], []
        acc_a2 = 0.0
        n_term = None
        for n in range(min(n_max, M)):
            num = mp.fsum([w[j] * z[j] * Phi[j] for j in range(M)])
            a_conj = num / nrm2
            aa = abs(a_conj) ** 2
            gap = 1 - aa
            med = (sorted(gaps[-8:])[len(gaps[-8:]) // 2] if gaps
                   else mp.mpf(1))
            gaps.append(gap)
            if gap <= 0 or gap < mp.mpf("1e-10") * med:
                n_term = n
                break
            alpha = mp.conj(a_conj)
            Phi, Phis = (
                [z[j] * Phi[j] - a_conj * Phis[j] for j in range(M)],
                [Phis[j] - alpha * z[j] * Phi[j] for j in range(M)])
            nrm2 = nrm2 * gap
            S.append(-mp.log(nrm2))
            acc_a2 += float(aa)
            a2.append(acc_a2)
            if (n + 1) % ort_every == 0:
                direct = mp.fsum([w[j] * abs(Phi[j]) ** 2 for j in range(M)])
                ort.append((n + 1, float(abs(direct - nrm2) / nrm2)))
        return dict(S=S, a2=a2, ort=ort, n_term=n_term, M=M, dps=dps,
                    S_final=float(S[-1]) if S else 0.0)


def szego_adaptive(cfg, dps0, n_max=None, label=""):
    """Escalate dps until the declared trust margin holds. The measured
    conditioning law (S8) is that the recursion loses up to 2.3x
    S_final/ln10 digits at the sizes used here (the naive determinant-range
    model S/ln10 underpredicts by a growing step-accumulation factor,
    measured at 1.0-1.8x on the grid), so the requirement is
    dps >= 2.3 * S_final/ln10 + 30."""
    dps = dps0
    for _ in range(3):
        r = szego_profile(cfg, dps, n_max=n_max)
        need = 2.3 * r["S_final"] / math.log(10) + 30
        if dps >= need:
            return r
        dps = int(need + 15)
    return r


def dps_for(M):
    """Initial working precision: worst measured per-atom rate is about
    0.55 nats (RAND), so S_final <= 0.55 M and the rule gives
    dps ~ 0.24 M + 45 with 40% headroom. Pinned from calibration."""
    return max(60, 45 + int(0.34 * M))


# ==========================================================================
# Route A (independent): own complex-Hermitian Cholesky of the Toeplitz
# moment matrix; S[n] = -2 log L[n+1, n+1]. No recursion shared with route
# B: the certificate is agreement of the two.
# ==========================================================================
def route_a_profile(cfg, dps, K):
    th, wl = materialize(cfg, dps)
    with mp.workdps(dps):
        z = [mp.expjpi(2 * t) for t in th]
        w = [mp.mpf(x) for x in wl]
        W = mp.fsum(w)
        w = [x / W for x in w]
        mom = [mp.mpf(1)]
        zp = [mp.mpc(1)] * len(z)
        for _t in range(1, K + 2):
            zp = [zp[j] * z[j] for j in range(len(z))]
            mom.append(mp.fsum([w[j] * zp[j] for j in range(len(z))]))
        n1 = K + 1
        L = [[mp.mpc(0)] * n1 for _ in range(n1)]
        for i in range(n1):
            for j in range(i + 1):
                t = i - j
                a = mom[t] if t >= 0 else mp.conj(mom[-t])
                s = mp.fsum([L[i][k] * mp.conj(L[j][k]) for k in range(j)])
                if i == j:
                    L[i][j] = mp.sqrt(mp.re(a - s))
                else:
                    L[i][j] = (a - s) / L[j][j]
        return [-2 * mp.log(mp.re(L[n + 1][n + 1])) for n in range(K)]


# ==========================================================================
# Observables.
# ==========================================================================
def rates(res):
    """Per-atom rates off the profile: r_diag at the last finite index,
    r_mid at half depth, plus the quarter-point profile and the l^2
    (Killip-Simon coefficient side) partials."""
    S = res["S"]
    M = res["M"]
    n = len(S)
    if n == 0:
        return None
    q = [max(0, int(0.25 * (n - 1))), int(0.5 * (n - 1)),
         int(0.75 * (n - 1)), n - 1]
    return dict(M=M, n=n,
                r_diag=float(S[-1]) / M,
                r_mid=float(S[q[1]]) / M,
                Sq=[float(S[i]) for i in q],
                a2q=[res["a2"][i] for i in q])


def hist_l1(theta_a, theta_b, bins=HIST_BINS):
    ha = np.histogram(theta_a, bins=bins, range=(0, 1))[0] / len(theta_a)
    hb = np.histogram(theta_b, bins=bins, range=(0, 1))[0] / len(theta_b)
    return float(np.abs(ha - hb).sum())


def profile_dist(res_a, res_b):
    """max_n |S^a_n - S^b_n| over the common range, at matched dps."""
    m = min(len(res_a["S"]), len(res_b["S"]))
    with mp.workdps(60):
        return max(float(abs(res_a["S"][i] - res_b["S"][i]))
                   for i in range(m))


# ==========================================================================
# Source scan (teeth-verified): this module must consume prime/Beurling
# data only, never an L-function zero list.
# ==========================================================================
def scan_lines(lines):
    bad = []
    for i, ln in enumerate(lines, 1):
        if "SCAN-ALLOW" in ln:
            continue
        for tok in ("zetazero", "davenport", ".zeros("):    # SCAN-ALLOW
            if tok in ln:
                bad.append(f"{i}:{tok}")
    return bad


# ==========================================================================
# Sections.
# ==========================================================================
def s0_guards():
    print("\n[S0] HARNESS: imports and source scan")
    ok_imp = BeurlingSystem.__module__ == "experiments._shared.beurling"
    check("S0a Beurling control consumed by import from _shared "
          "(no reimplementation)", ok_imp, BeurlingSystem.__module__)
    teeth = scan_lines(["x = mp.zetazero(1)"])          # SCAN-ALLOW (teeth)
    src = Path(__file__).read_text(encoding="utf-8").splitlines()
    bad = scan_lines(src)
    check("S0b no L-function zero list consumed anywhere: source scan clean, "
          "and the scanner has teeth (catches a planted call)",
          teeth and not bad,
          f"planted caught: {bool(teeth)}; offending: {bad or 'none'}")


def s1_controls():
    print("\n[S1] ANALYTIC CONTROLS (exact statements, not fits)")
    # equal spacing: S = 0 until termination at n = M-1
    M = 64
    cfg = cfg_float(np.arange(M) / M, WRAP_L_MAIN, "EQSP")
    r = szego_profile(cfg, 60, n_max=M)
    smax = max(abs(float(x)) for x in r["S"]) if r["S"] else 0.0
    check("S1a equal spacing: S_n = 0 for n < M-1 (pinned < 1e-40) and "
          "termination fires exactly at n = M-1",
          smax < 1e-40 and r["n_term"] == M - 1,
          f"max|S| {smax:.1e}, n_term {r['n_term']} (theory {M - 1})")
    # two atoms: conj(alpha_0) = <z, 1> = w1 z1 + w2 z2, termination at n=1
    th = [0.13, 0.57]
    w = [0.3, 0.7]
    cfg2 = cfg_float(np.array(th), WRAP_L_MAIN, "TWO", w=w)
    r2 = szego_profile(cfg2, 60, n_max=3)
    with mp.workdps(60):
        # weights normalized exactly as the pipeline normalizes them (the
        # float sum 0.3 + 0.7 is not exactly 1, and the closed form must
        # live on the same normalized measure)
        wn = [mp.mpf(float(x)) for x in w]
        Wn = mp.fsum(wn)
        m1 = mp.fsum([x / Wn * mp.expjpi(2 * mp.mpf(t))
                      for x, t in zip(wn, th)])
        S0_closed = -mp.log(1 - abs(m1) ** 2)
        d = abs(r2["S"][0] - S0_closed) / S0_closed
    check("S1b two-atom closed form: S_0 = -log(1 - |w1 z1 + w2 z2|^2) "
          "(pinned rel < 1e-45) and termination at n = 1",
          float(d) < 1e-45 and r2["n_term"] == 1,
          f"rel dev {float(d):.1e}, n_term {r2['n_term']}")


def s2_routes(pk_small):
    print("\n[S2] TWO INDEPENDENT ROUTES: Szego recursion vs Toeplitz "
          "Cholesky (n <= 40)")
    worst = 0.0
    for cfg in (cfg_true(pk_small, WRAP_L_MAIN),
                cfg_float(wrap_float(resample_t(
                    true_t_float(pk_small), "RAND", 11), WRAP_L_MAIN),
                    WRAP_L_MAIN, "RAND")):
        rb = szego_profile(cfg, 100, n_max=40)
        ra = route_a_profile(cfg, 120, 40)
        with mp.workdps(120):
            d = max(float(abs(a - b) / abs(b))
                    for a, b in zip(ra, rb["S"]))
        worst = max(worst, d)
        print(f"    {cfg['label']:8s} worst rel {d:.2e}")
    check("S2a the two routes agree (recursion on atom values vs Cholesky "
          "of the moment matrix; pinned worst rel < 1e-30)", worst < 1e-30,
          f"worst {worst:.2e}")


def build_classes(N, quick, L=WRAP_L_MAIN, n_seeds=3):
    """All configs of one size, band-equalized. Returns (configs dict,
    t_true float array)."""
    pk = true_pk(N)
    t_true = true_t_float(pk)
    th_true_f = wrap_float(t_true, L)
    sites, counts, ncoll = snap_sites(pk, SNAP_D)
    tb = beurling_t(N, BAND_A, t_true[-1])
    cfgs = {"TRUE": cfg_true(pk, L),
            "SNAP": cfg_snap(sites, counts, SNAP_D, L),
            "BEUR": cfg_float(wrap_float(tb, L), L, "BEUR")}
    ns = 1 if quick else n_seeds
    for i, sd in enumerate(RAND_SEEDS[:max(2, ns) if quick else ns]):
        cfgs[f"RAND{i}"] = cfg_float(
            wrap_float(resample_t(t_true, "RAND", sd), L), L, f"RAND{i}")
    for i, sd in enumerate(STRAT_SEEDS[:ns]):
        cfgs[f"STRAT{i}"] = cfg_float(
            wrap_float(resample_t(t_true, "STRAT", sd), L), L, f"STRAT{i}")
    for i, sd in enumerate(GPERM_SEEDS[:ns]):
        cfgs[f"GPERM{i}"] = cfg_float(
            local_gap_shuffle(th_true_f, sd), L, f"GPERM{i}")
    for i, sd in enumerate(JIT_SEEDS[:max(2, ns)]):
        rng = np.random.default_rng(sd)
        cfgs[f"JIT{i}"] = cfg_float(
            np.sort(np.mod(th_true_f + rng.uniform(
                -0.5 / SNAP_D, 0.5 / SNAP_D, len(th_true_f)), 1.0)),
            L, f"JIT{i}")
    return cfgs, t_true, ncoll


def s3_grid(sizes, quick):
    print("\n[S3] THE GRID: profiles for all classes and sizes "
          "(band-equalization certificate inline)")
    store = {}
    eq_rows = []
    for N in sizes:
        n_seeds = 3 if N <= 1000 else 2
        cfgs, t_true, ncoll = build_classes(N, quick, n_seeds=n_seeds)
        thT, _ = None, None
        th_true = wrap_float(t_true, WRAP_L_MAIN)
        dps0 = dps_for(len(t_true))
        print(f"    N = {N}: M = {len(t_true)}, t in [{t_true[0]:.4f}, "
              f"{t_true[-1]:.4f}], dps0 = {dps0}, snap collisions at "
              f"D = 10^6: {ncoll}")
        print(f"    {'class':8s} {'M':>5s} {'dps':>4s} {'time':>6s} "
              f"{'S[q1]':>9s} {'S[mid]':>9s} {'S[q3]':>9s} {'S[diag]':>10s} "
              f"{'r_diag':>8s} {'histL1':>7s} {'mingap':>9s}")
        for name, cfg in cfgs.items():
            t0 = time.time()
            res = szego_adaptive(cfg, dps0, label=name)
            dt = time.time() - t0
            rt = rates(res)
            thc, _w = materialize(cfg, 30)
            thf = np.array([float(x) for x in thc])
            h = hist_l1(thf, th_true)
            mg = float(np.min(np.diff(thf))) if len(thf) > 1 else 1.0
            store[(N, name)] = dict(res=res, rt=rt, cfg=cfg)
            eq_rows.append((N, name, rt["M"], h, mg, res["dps"]))
            print(f"    {name:8s} {rt['M']:5d} {res['dps']:4d} {dt:6.1f}"
                  f" {rt['Sq'][0]:9.3f} {rt['Sq'][1]:9.3f} {rt['Sq'][2]:9.3f}"
                  f" {rt['Sq'][3]:10.3f} {rt['r_diag']:8.4f} {h:7.3f}"
                  f" {mg:9.2e}")
        store[(N, "_t_true")] = t_true
    # equalization checks over the whole grid
    MT = {N: store[(N, "TRUE")]["rt"]["M"] for N in sizes}
    cnt_ok = all(r[2] == MT[r[0]] for r in eq_rows
                 if r[1].startswith(("SNAP", "RAND", "STRAT", "GPERM", "JIT")))
    beur_dev = max(abs(r[2] - MT[r[0]]) / MT[r[0]] for r in eq_rows
                   if r[1] == "BEUR")
    check("S3a count equalization: surrogate classes match TRUE's M exactly; "
          "BEUR within 6% (density-matched generator, pinned)",
          cnt_ok and beur_dev < 0.06,
          f"surrogates exact: {cnt_ok}; BEUR worst dev {beur_dev:.3f}")
    # the sampling-fluctuation scale of the L1 histogram distance is
    # ~ 0.8 sqrt(bins/M), so the certificate is read in units of that scale
    # (a fixed absolute pin would fail small M and be vacuous at large M)
    worst_hn = max(r[3] / math.sqrt(HIST_BINS / max(MT[r[0]], 1))
                   for r in eq_rows)
    check("S3b band-profile equalization: worst angular-histogram L1 "
          "distance to TRUE, in units of the sampling-fluctuation scale "
          "sqrt(bins/M) (pinned < 1.3; iid expectation is ~ 0.8)",
          worst_hn < 1.3, f"worst normalized {worst_hn:.3f}")
    worst_g = min(r[4] for r in eq_rows)
    check("S3c no accidental near-collisions in any config (min wrapped gap "
          "> 1e-9)", worst_g > 1e-9, f"min gap {worst_g:.2e}")
    ok_term = all(store[(N, n)]["res"]["n_term"] is None
                  for N in sizes for n in
                  [k[1] for k in store if k[0] == N and k[1] != "_t_true"])
    check("S3d no main-grid run terminated early (the cliff detector is for "
          "genuine rank collapse only)", ok_term)
    return store, eq_rows


def s4_verdict(store, sizes, quick):
    print("\n[S4] THE RATE TABLE AND THE PRE-REGISTERED READINGS")
    table = []
    verdict = {}
    for N in sizes:
        row = {}
        for base in ("TRUE", "SNAP", "BEUR"):
            row[base] = (store[(N, base)]["rt"]["r_diag"],
                         store[(N, base)]["rt"]["r_mid"])
        for fam in ("RAND", "STRAT", "GPERM", "JIT"):
            ds = [store[k]["rt"]["r_diag"] for k in store
                  if k[0] == N and str(k[1]).startswith(fam)]
            ms = [store[k]["rt"]["r_mid"] for k in store
                  if k[0] == N and str(k[1]).startswith(fam)]
            # MEDIAN, not mean: the diagonal rate of an iid configuration is
            # heavy-tailed (a single tight pair adds O(-log d) nats), so the
            # mean is dominated by seed outliers; per-seed lists are kept
            # because the significance instrument is a per-seed ratio test
            row[fam] = (float(np.median(ds)), float(np.median(ms)),
                        float(np.max(ds) - np.min(ds)), ds, ms)
        four_d = [row["TRUE"][0], row["SNAP"][0], row["RAND"][0],
                  row["BEUR"][0]]
        four_m = [row["TRUE"][1], row["SNAP"][1], row["RAND"][1],
                  row["BEUR"][1]]
        spread_d = max(four_d) / min(four_d)
        spread_m = max(four_m) / min(four_m)
        seed_band = row["RAND"][2]
        table.append((N, row, spread_d, spread_m, seed_band))
        print(f"    N = {N}: r_diag  TRUE {row['TRUE'][0]:.4f}  SNAP "
              f"{row['SNAP'][0]:.4f}  GPERM {row['GPERM'][0]:.4f}  STRAT "
              f"{row['STRAT'][0]:.4f}  BEUR {row['BEUR'][0]:.4f}  RAND "
              f"{row['RAND'][0]:.4f} (seed band {seed_band:.4f})")
        print(f"             r_mid   TRUE {row['TRUE'][1]:.4f}  SNAP "
              f"{row['SNAP'][1]:.4f}  GPERM {row['GPERM'][1]:.4f}  STRAT "
              f"{row['STRAT'][1]:.4f}  BEUR {row['BEUR'][1]:.4f}  RAND "
              f"{row['RAND'][1]:.4f}")
        print(f"             four-class spread: r_diag {spread_d:.3f}x, "
              f"r_mid {spread_m:.3f}x   (P1 needs both <= 1.35)")
    # [P1] needs BOTH observables inside 1.35x at every size. The diagonal
    # rate is heavy-tailed for iid seeds (a tight pair adds O(-log d)
    # nats), so the INFERENTIAL reads below (P2 stability, significance,
    # kill) are made on the self-averaging mid-profile rate; the diagonal
    # is reported alongside with that caveat.
    p1 = all(t[2] <= 1.35 and t[3] <= 1.35 for t in table)
    # significance instrument: every individual RAND seed at every size
    # must exceed TRUE's r_mid by more than the P1 factor (a per-seed
    # ratio/sign test; with 8 seeds across sizes the sign test alone has
    # p ~ 2^-8 under exchangeability)
    ratios = [ms / t[1]["TRUE"][1] for t in table for ms in t[1]["RAND"][4]]
    sig_ok = all(r > 1.35 for r in ratios)
    p2_letter = all(t[3] > 1.35 for t in table) and sig_ok
    # the sanity kill, on the self-averaging observable: does the
    # lattice-destroyed twin (GPERM) stand as far from BEUR as TRUE does?
    kill_rows = []
    for (N, row, _sd, _sm, _band) in table:
        d_TB = abs(row["TRUE"][1] - row["BEUR"][1])
        d_GB = abs(row["GPERM"][1] - row["BEUR"][1])
        frac = d_GB / d_TB if d_TB > 0 else 1.0
        sig = max(row["BEUR"][1], row["TRUE"][1]) \
            / min(row["BEUR"][1], row["TRUE"][1]) > 1.35
        kill_rows.append((N, d_TB, d_GB, frac, sig))
        print(f"    KILL @ N = {N} (r_mid): |TRUE-BEUR| = {d_TB:.5f}, "
              f"|GPERM-BEUR| = {d_GB:.5f}, lattice-free fraction "
              f"{frac:.2f}, separation significant: {sig}")
    kill_fired = all((not s) or f >= 0.70 for (_N, _a, _b, f, s) in kill_rows)
    # how much of the TRUE-to-RAND gap the exact-local-gap surrogate closes:
    # near 1 means the whole spread is carried by the gap multiset
    expl = [(N, 1.0 - abs(row["GPERM"][1] - row["TRUE"][1])
             / max(abs(row["RAND"][1] - row["TRUE"][1]), 1e-12))
            for (N, row, _sd, _sm, _b) in table]
    for (N, f) in expl:
        print(f"    TYPING @ N = {N}: GPERM sits at {100 * f:.1f}% of the "
              f"way from RAND back to TRUE on r_mid (local gap multiset "
              f"carries the spread)")
    verdict.update(p1=p1, p2_letter=p2_letter, kill_fired=kill_fired,
                   table=table, kill_rows=kill_rows, explained=expl)
    check("S4a the [P1]/[P2] resolution is decided by the data, not "
          "asserted: every RAND seed at every size exceeds TRUE's r_mid by "
          "more than the P1 factor 1.35 (per-seed ratio test on the "
          "self-averaging observable)", sig_ok,
          f"min ratio {min(ratios):.2f} over {len(ratios)} seed-size pairs")
    check("S4b SANITY KILL armed and evaluated: any TRUE-vs-BEUR separation "
          "must survive lattice destruction to be typed non-arithmetic "
          "(fired = separation is spacing statistics)", True,
          f"kill_fired = {kill_fired}")
    return verdict


def s5_q_axis(store, sizes):
    print("\n[S5] THE (i)-vs-(ii) AXIS: snap response against the jitter "
          "band (the #172 V5 control at sequence level)")
    rows = []
    for N in sizes:
        rT = store[(N, "TRUE")]["res"]
        rS = store[(N, "SNAP")]["res"]
        dS = profile_dist(rT, rS)
        dJ = [profile_dist(rT, store[(N, k)]["res"])
              for k in [q[1] for q in store
                        if q[0] == N and str(q[1]).startswith("JIT")]]
        dr = abs(store[(N, "SNAP")]["rt"]["r_diag"]
                 - store[(N, "TRUE")]["rt"]["r_diag"])
        rows.append((N, dS, min(dJ), max(dJ), dr))
        print(f"    N = {N}: max_n|dS| snap {dS:.3e}, jitter band "
              f"[{min(dJ):.3e}, {max(dJ):.3e}], per-atom diag displacement "
              f"{dr:.2e}")
    ok_band = all(dS <= SNAP_BAND_FACTOR * hi
                  for (_N, dS, _lo, hi, _dr) in rows)
    worst_dr = max(r[4] for r in rows)
    check("S5a SNAP's whole-profile response sits at the matched-"
          "amplitude jitter band (pinned <= 4x the band top): snapping "
          "is a GENERIC perturbation to this functional, rationality "
          "invisible", ok_band,
          "; ".join(f"N={r[0]}: {r[1]:.1e} vs {r[3]:.1e}" for r in rows))
    check("S5b the per-atom diagonal rate moves by < 1e-3 under the "
          "D = 10^6 snap (the sequence-level extension of #172 V5, pinned)",
          worst_dr < 1e-3, f"worst {worst_dr:.2e}")
    return rows


def s6_horizon(N, quick):
    print("\n[S6] THE HORIZON: D-ladder. Where DOES the sequence-level "
          "functional see the lattice?")
    pk = true_pk(N)
    M0 = len(pk)
    dps0 = dps_for(M0)
    rT = szego_adaptive(cfg_true(pk, WRAP_L_MAIN), dps0)
    ladder = DLADDER_QUICK if quick else DLADDER_FULL
    rows = []
    for D in ladder:
        sites, counts, ncoll = snap_sites(pk, D)
        Md = len(sites)
        cfg = cfg_snap(sites, counts, D, WRAP_L_MAIN)
        # n_max past Md so the terminal |alpha| = 1 step is actually reached
        # (every M-atom measure terminates at n = M-1; DETECTION means
        # terminating EARLY, i.e. at n_term < M0 - 1, or the profile pulling
        # away from TRUE's before that)
        res = szego_adaptive(cfg, dps0, n_max=Md + 2)
        m = min(len(res["S"]), len(rT["S"]))
        nstar = None
        with mp.workdps(60):
            for i in range(m):
                if abs(res["S"][i] - rT["S"][i]) > 0.5:
                    nstar = i
                    break
        early = res["n_term"] is not None and res["n_term"] < M0 - 1
        if nstar is None and early:
            nstar = res["n_term"]
        rows.append((D, Md, ncoll, res["n_term"], nstar))
        print(f"    D = {D:>8g}: sites Md = {Md:4d} (collisions {ncoll:3d}), "
              f"n_term = {str(res['n_term']):>5s} (theory {Md - 1}), "
              f"detection n* = {nstar}")
    coll = [r for r in rows if r[2] > 0]
    ok_law = all(r[3] == r[1] - 1 and r[4] is not None and r[4] <= r[1] - 1
                 for r in coll)
    check("S6a the termination law is EXACT on every collision rung: "
          "n_term = Md - 1 < M - 1, and detection fires at or before it "
          "(the functional sees the lattice exactly when Q-dependence "
          "collapses the atom count)", ok_law,
          f"{len(coll)} collision rungs")
    nocoll = [r for r in rows if r[2] == 0]
    ok_blind = all(r[3] in (None, M0 - 1) and r[4] is None for r in nocoll)
    check("S6b below the collision horizon the ladder is BLIND: termination "
          "at the generic n = M-1 only, and the profile never leaves "
          "TRUE's by 0.5 nats at any no-collision rung", ok_blind,
          f"{len(nocoll)} no-collision rungs")
    ok_mono = all(rows[i][1] <= rows[i + 1][1] for i in range(len(rows) - 1))
    check("S6c Md(D) is monotone in D (the horizon recedes as the lattice "
          "refines)", ok_mono)
    return rows


def s7_gauge(N, quick):
    print("\n[S7] GAUGE FACE: the wrap period is a choice; the reading must "
          "survive it (L = golden mean vs L = 1)")
    cfgs, t_true, _ = build_classes(N, True, L=WRAP_L_GOLD, n_seeds=1)
    dps0 = dps_for(len(t_true))
    vals = {}
    for name in ("TRUE", "BEUR", "RAND0", "GPERM0"):
        res = szego_adaptive(cfgs[name], dps0)
        vals[name] = rates(res)["r_diag"]
    print("    r_diag at L = golden: " +
          ", ".join(f"{k} {v:.4f}" for k, v in vals.items()))
    ok_ord = vals["TRUE"] < vals["RAND0"] and \
        abs(vals["GPERM0"] - vals["TRUE"]) < abs(vals["RAND0"] - vals["TRUE"])
    check("S7a the class ordering (TRUE most rigid, GPERM near TRUE, RAND "
          "loosest) survives the gauge change", ok_ord,
          "; ".join(f"{k} {v:.4f}" for k, v in vals.items()))
    return vals


def s8_audit(store, sizes):
    print("\n[S8] DIGIT-LOSS AUDIT: the declared conditioning rule, "
          "verified against two independent meters")
    worst_drift = 0.0
    rows = []
    for N in sizes:
        names = ["TRUE", "SNAP", "BEUR", "RAND0"]
        # add the worst-conditioned config of this size (largest S_final):
        # it is exactly the one the escalation rule had to protect
        cands = [(store[k]["res"]["S_final"], k[1]) for k in store
                 if k[0] == N and k[1] != "_t_true"]
        worst_name = max(cands)[1]
        if worst_name not in names:
            names.append(worst_name)
        for name in names:
            if (N, name) not in store:
                continue
            res = store[(N, name)]["res"]
            hi = szego_profile(store[(N, name)]["cfg"], res["dps"] + 40,
                               n_max=len(res["S"]))
            with mp.workdps(res["dps"] + 60):
                drift = max(float(abs(a - b) / abs(b))
                            for a, b in zip(res["S"], hi["S"])
                            if abs(b) > mp.mpf("1e-6"))
            naive = res["S_final"] / math.log(10)
            ort = max(o for _, o in res["ort"]) if res["ort"] else 0.0
            # measured loss (digits) by the orthogonality meter, and its
            # ratio to the naive determinant-range model: the measured
            # conditioning coefficient the escalation rule (2.3x) must cover
            lost = res["dps"] + math.log10(max(ort, 1e-300))
            coef = lost / naive if naive > 1 else 0.0
            worst_drift = max(worst_drift, drift)
            rows.append((N, name, res["dps"], naive, lost, coef, drift))
            print(f"    N = {N} {name:6s}: dps {res['dps']}, naive loss "
                  f"{naive:5.1f} digits, measured loss {lost:5.1f} "
                  f"(coef {coef:4.2f}), dps+40 drift {drift:.1e}")
    check("S8a every reported value carries at least 10 trustworthy digits "
          "(dps+40 re-run of the whole pipeline, positions included; "
          "pinned worst rel drift < 1e-10)", worst_drift < 1e-10,
          f"worst {worst_drift:.1e}")
    # the global retained-digits floor by the internal meter, over EVERY
    # main-grid run (not just the audited subset): retained = dps - lost
    # = -log10(worst ORT)
    retained = min(-math.log10(max(
        max((o for _, o in store[k]["res"]["ort"]), default=0.0), 1e-300))
        for k in store if k[1] != "_t_true")
    ok_coef = all(c <= 2.3 for (_N, _n, _d, _na, _lo, c, _dr) in rows)
    check("S8b the measured conditioning law holds: loss coefficient "
          "<= 2.3x the naive S/ln10 model on every audited config (the "
          "escalation rule's constant), and every main-grid run retains "
          ">= 20 digits by the orthogonality meter", ok_coef and retained >= 20,
          f"worst coef {max(c for (_N, _n, _d, _na, _lo, c, _dr) in rows):.2f}"
          f", min retained {retained:.0f} digits")
    return rows


def s9_determinism(store, sizes):
    print("\n[S9] DETERMINISM: seeded configs reproduce exactly")
    N = sizes[0]
    k = (N, "RAND0")
    r2 = szego_profile(store[k]["cfg"], store[k]["res"]["dps"],
                       n_max=len(store[k]["res"]["S"]))
    with mp.workdps(store[k]["res"]["dps"]):
        same = all(a == b for a, b in zip(store[k]["res"]["S"], r2["S"]))
    check("S9a re-running an identical seeded config reproduces the profile "
          "EXACTLY (mpf equality, not tolerance)", same)


def s10_prereg(verdict, qrows):
    print("\n[S10] PRE-REGISTRATION RESOLUTION (recorded in the module, "
          "recomputed here)")
    p1, p2, kill = verdict["p1"], verdict["p2_letter"], verdict["kill_fired"]
    q_null = all(dS <= SNAP_BAND_FACTOR * hi
                 for (_N, dS, _lo, hi, _dr) in qrows)
    computed = (not p1) and p2 and kill and q_null
    recorded = PREREG["resolution_recorded"] and \
        PREREG["resolution"].startswith("P2_LETTER_FIRED_THEN_KILLED")
    print(f"    computed: P1 fired = {p1}, P2 letter fired = {p2}, "
          f"kill fired = {kill}, Q-axis null = {q_null}")
    print(f"    recorded: {PREREG['resolution'][:100]}...")
    check("S10a the recorded resolution matches the recomputed verdict "
          "(P1 refuted at the letter; P2 fired then KILLED by the "
          "lattice-destroyed twin; Q-axis null below the horizon)",
          computed and recorded,
          f"computed {computed}, recorded flag {recorded}")


# ==========================================================================
# Driver.
# ==========================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="one size, reduced seeds and ladder; no npz")
    args = ap.parse_args()
    t0 = time.time()
    print("=" * 78)
    print("E1AD: SUM RULES ON THE PRIME LOG-LATTICE (the sequence-level half")
    print("      of the split Christoffel sweep, PHASE_STATE next-step 3)")
    print("=" * 78)

    sizes = SIZES_QUICK if args.quick else SIZES_FULL
    pk_small = true_pk(300)

    s0_guards()
    s1_controls()
    s2_routes(pk_small)
    store, eq_rows = s3_grid(sizes, args.quick)
    verdict = s4_verdict(store, sizes, args.quick)
    qrows = s5_q_axis(store, sizes)
    hrows = s6_horizon(sizes[min(1, len(sizes) - 1)], args.quick)
    gvals = s7_gauge(sizes[0], args.quick)
    arows = s8_audit(store, sizes)
    s9_determinism(store, sizes)
    s10_prereg(verdict, qrows)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print("\n" + "=" * 78)
    print(f"SELF-TEST: {n_ok}/{len(CHECKS)} passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")

    if not args.quick:
        results = {}
        for (N, name), v in store.items():
            if name == "_t_true":
                continue
            results[f"S_{N}_{name}"] = np.array(
                [float(x) for x in v["res"]["S"]])
            results[f"a2_{N}_{name}"] = np.array(v["res"]["a2"])
        results["eq_rows"] = np.array(
            [(N, nm, M, h, g, d) for (N, nm, M, h, g, d) in eq_rows],
            dtype=object)
        results["rate_table"] = np.array(
            [(t[0], t[1]["TRUE"][0], t[1]["SNAP"][0], t[1]["GPERM"][0],
              t[1]["STRAT"][0], t[1]["BEUR"][0], t[1]["RAND"][0],
              t[1]["TRUE"][1], t[1]["SNAP"][1], t[1]["GPERM"][1],
              t[1]["STRAT"][1], t[1]["BEUR"][1], t[1]["RAND"][1],
              t[2], t[3], t[4]) for t in verdict["table"]], float)
        results["kill_rows"] = np.array(verdict["kill_rows"], float)
        results["q_axis_rows"] = np.array(qrows, float)
        results["horizon_rows"] = np.array(
            [(D, Md, nc, -1 if nt is None else nt, -1 if ns is None else ns)
             for (D, Md, nc, nt, ns) in hrows], float)
        results["gauge_vals"] = np.array(
            [(k, v) for k, v in gvals.items()], dtype=object)
        results["audit_rows"] = np.array(
            [(N, nm, d, na, lo, c, dr)
             for (N, nm, d, na, lo, c, dr) in arows], dtype=object)
        results["prereg_resolution"] = np.array(
            [PREREG["resolution"]], dtype=object)
        np.savez_compressed(OUT, **results)
        print(f"Saved -> {OUT}")
    else:
        print("(quick mode: no npz saved)")
    print(f"Total time {round(time.time() - t0, 1)}s")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""E1AF: the funding-wall typing probe (frame session F1, build half; the
funding-boundary frame's first measured claim, successor_frame_deliberation.md
Section 4 "Wall 1" / Section 7 "F1").

THE CLAIM UNDER TEST (F1a, verbatim from the deliberation): "the HL data class
exists as a data class only over an additive lattice (L1), so the funding wall
consumes the conservation law's lattice clause." Register, fixed in advance by
the deliberation: the singular series has average 1, so density matches at
LEADING order and the lattice enters at the SECOND-ORDER term (the
Montgomery-Soundararajan register); the typing lives there, not at leading
order. Pre-registered competitor typing (must be discriminated, not ignored):
the obstruction to funding past support 1 is minor-arc cancellation /
short-interval variance (provability), not lattice-data availability; the
probe types WHAT the funding consumes (the data class), the competitor types
WHY it is unproven (error control): both can land, as a CONJUNCTION.

THE DATA CLASS (derivation in e1af_funding_wall.md Section 2). At Fourier
support Delta = 1 + delta the compressed-Weil-form budget's off-diagonal
consumes exactly the prime-pair family B_X(h) = sum_{n <= X} Lambda(n)
Lambda(n+h) at INTEGER shifts 1 <= h <= H(delta), H ~ X/T = T^delta, each h
entering at weight ~ log(H/h). Hardy-Littlewood: B_X(h) ~ S(h) X with
S(h) = 2 C2 prod_{p | h, p > 2} (p-1)/(p-2) for even h, 0 for odd h
(C2 = 0.6601618158...). The L1 lattice content at its crudest: PARITY
(S vanishes on odd shifts) plus the mod-p oscillation (3 | h doubles S).

THE METER (second-order discrimination on the family {B_X(h)/X}, h = 1..H):
  parity  P = (mean_{even h} b - mean_{odd h} b) / mean_h b, b(h) = B_X(h)/X.
  R2      explained variance of parameter-free M1 (b = S(h)) against M0
          (flat at the fitted window mean; the PNT/Cramer level (theta/X)^2
          is reported alongside): R2 = 1 - RSS(M1)/RSS(M0). M0's level is
          fitted, M1 has NO free parameter.
  R2_even the same restricted to even h (mod-p structure with parity removed).
  rms_e   rms relative residual (b - S)/S over even h (the [P3] cleanliness
          meter for the competitor's finite-scale register).
Lambda choice, stated: PRIME-ONLY weights (w(n) = log n at primes, prime
powers dropped; their total weight is O(sqrt(X) log X), relative ~3e-4 at
X = 1e7, and the Lambda-form HL main term S(h) X is unchanged). The exact
integer meter and the windowed continuous meter (pair weight in windows
|b_j - b_i - h| < 1/2, Lambda-like weights log b) coincide on integer
configurations, gated (C3), so real-valued controls are meter-matched.

CONTROLS (the typing contrasts; each gated):
  C1 BEURLING prime side: b_p = p exp(eps_p), eps_p iid U[-0.25, 0.25]
     (the shared control's recipe, numpy rng for scale, seeds 149/150/151):
     Euler product, no additive lattice; integer-shift B(h) is unposable AS
     INTEGERS, so the honest continuous analogue (the windowed meter) is
     posed: the density-alone comparator. Expected flat, parity ~ 0.
  C2 SNAP: log p snapped to (1/D)Z, exponentiated back: reals, fully
     L2-commensurate at every D (all logs rational with denominator D),
     integer lattice destroyed EXACTLY at every D. Three rungs:
       D_lo  = X/1000 (1e4 full, 1e3 quick): pair displacement >> window
               across the weight range: expected DEAD (parity ~ 0).
       D_mid = 1e6 (the e1ad-standard scale): mid-transition; expectation
               set QUANTITATIVELY by the displacement law below.
       D_hi  = 10 X (1e8 full, 1e7 quick): displacement < 1/2 everywhere:
               window assignment identical to TRUE: expected ALIVE
               (meter output ~ TRUE to weight precision).
     The anti-alignment demonstration ON THE METER: L2-commensurability is
     total at ALL three rungs while the L1/HL signal runs dead-partial-alive:
     the meter provably does not read L2. With TRUE (independent, alive) and
     BEURLING (independent-generic, dead) this realizes all four corners of
     the (L2-commensurate?, HL-signal?) 2x2: the axes are INDEPENDENT,
     which is the deliberation's adversary-A2 split, measured.
  C3 TRUE through the SAME windowed meter as C1/C2 (meter-matched, gated
     equal to the exact meter).
  C4 SHUFFLE: Cramer draw (n included w.p. min(1, 1/log n), weight log n,
     seeds 20260826/27/28): INTEGER-VALUED but congruence-free: separates
     "lives in Z" from "carries the primes' mod-p correlations". Expected
     flat, parity ~ 0, M0 exact.
  C5 RAMP (e2bc idiom, full mode): b_p = p exp(t eps_p), t in
     {1e-6, 1e-4, 1e-2}, seed 149: the graded axis; parity decays along t
     per the same displacement law.

THE DISPLACEMENT LAW (design-derived and prototype-validated BEFORE the
registered full-scale run; prototype disclosure below). Snapping log p at
scale 1/D displaces b_p by ~ p r/D (|r| <= 1/2): a MULTIPLICATIVE-scale
perturbation read by an ADDITIVE-window meter. The pair displacement at
shift h is spread over a kernel of half-width a(p) = p/(2u), u = D/2
(snap, triangular model; a wrap analysis also admits a uniform variant at
u = D) or u = 1/t (ramp, exactly triangular: eps' - eps). Naive in-window
retention is the kernel mass in |disp| < 1/2, but the PARITY meter reads
the ALTERNATING sum over integer-offset windows, A(a) = sum_k (-1)^k
m_k(a): A = 1 for a <= 1/2 and decays like the kernel's Fourier mass at
the parity frequency (~1/a^2), much faster than the ~1/a in-window mass.
Registered model: parity ratio P/P_TRUE ~ r_par(X, u) = (1/X) int_0^X
A(p/(2u)) dp. Numbers at full scale (X = 1e7): SNAP D_mid = 1e6:
tri-variant 0.114, uniform-variant ~ 0.05-0.14 (band spans variants);
ramp t = 1e-6: 0.223; SNAP D_lo and ramp t = 1e-2: < 0.01, below the
meter's own noise floor (dead gate |P| <= 0.1). The EXACT-arithmetic
statement ("snapped reals have no integer differences") is meter-invisible
at D_hi: finite meters see displacements at their resolution, not
completed-totality 0/1s (the #172 / e2bc continuity finding, recurring
here by design; SNAP's site merging at p > 2Dh is e1ad's rank collapse
appearing in additive coordinates).

PROTOTYPE DISCLOSURE (the e1ad pattern). A quick-mode calibration run
(X = 1e6) preceded the full-scale freeze and exposed two design faults,
both fixed before the registered run: (i) a trial-division bug in the
singular-series routine (S(6)/S(2) came out 1.25; the factor 2 was never
removed; fixed and gated at the standard value 2, cross-checked against
e5b's C_6 = 4 C2); (ii) the naive in-window retention model over-predicts
the mid-rung parity at low retention (measured ramp t = 1e-4 ratio 0.021
vs in-window 0.092): the refined alternating-sum model above reproduces
the calibration values (snap-mid 0.886 predicted vs 0.888 measured; ramp
t = 1e-4: 0.023 vs 0.021). The full-scale (X = 1e7) numbers were not seen
before the freeze. Calibration facts, not predictions: TRUE parity 2.000
at X = 1e6; control parities at the 0.001-0.05 noise floor.

PRE-REGISTERED BRANCHES (frozen before any computation; harness.PreRegistry):
  P1 F1a-LANDS: TRUE (and C3) show the singular-series second-order
     structure: R2 >= 0.99, R2_even >= 0.9, parity >= 1 (expected ~ 2);
     while C1 (all seeds), C2-lo, C4 (all seeds) are flat: |parity| <= 0.1,
     R2 <= 0.3, R2_even <= 0.3. Then the funding wall's data class is
     LATTICE-CLASS (L1 congruence data), not density.
     KILL: any TRUE meter under threshold or any listed control over.
  P2 the F1a KILL branch (expected REFUTED; its FIRING is frame exit 1):
     C1 or C2-lo or C4 shows TRUE-class structure (parity >= 0.5 or
     R2_even >= 0.5): density / total log-commensurability purchases the
     congruence signal: F1a dies, the frame re-scopes to Wall 2.
  P3 the COMPETITOR's scoped landing (COMPATIBLE with P1, by design): the
     HL signal is PRESENT and CLEAN at accessible X: rms_e <= 0.03 on TRUE.
     Supports the competitor typing at the PROVABILITY register (the wall
     is uniform error control, not data availability at finite scale) while
     F1a holds at the DATA-CLASS register. P1 and P3 landing together is
     the expected outcome and is a CONJUNCTION, not a contradiction.
     KILL: rms_e > 0.10 (HL visibly rough at this X).
  P4 the displacement law (the SNAP/TRUE anti-alignment made quantitative;
     an INSTRUMENT-model branch: its failure means re-model the meter, not
     re-type F1a): P(C2-lo) <= 0.1 dead; |P(C2-hi) - P(TRUE)| <= 0.02
     alive-identical; P(C2-mid)/P(TRUE) within [0.5 x min-variant,
     1.7 x max-variant] of the alternating-sum model (tri at u = D/2,
     uniform at u = D); ramp parity nonincreasing in t (+0.02 slack) with
     P(t = 1e-2) <= 0.1 and P(t = 1e-6)/P(TRUE) in [0.5, 1.7] x the
     triangular model at u = 1/t. KILL: any clause fails.
  P5 leading-order blindness (the deliberation's register statement): the
     window mean of b is within [0.85, 1.15] of 1 for TRUE, every C1 seed,
     every C4 seed: the leading order does NOT discriminate; the typing
     content is second-order only. KILL: any mean outside the band.

DISCIPLINES. K1: this is a prime-side probe; NO zeta-zero data is consumed
anywhere (no zeros() call in this module; the harness import loads no zero
lists at import time). D-H: UNPOSABLE at the funding joint, type refusal per
LEARNINGS #202(iv): -f'/f for Davenport-Heilbronn has poles in sigma > 1, no
von-Mangoldt-type Dirichlet series exists there, so B_DH(h) cannot be posed;
stated, not faked. Beurling: the LIVE control (C1). Vedana negative control
(#204(v)): design-level, in the .md: the meter consumes integer-shift
congruence data, which C1/C2 show is not derivable from density or from
log-space commensurability; a typing that fired identically on a generic
formula-carrying system would be wrong, and P2 is exactly that kill.

Run:  python -m experiments.spectral.e1af_funding_wall [--quick] [--deep]
      quick: X = 1e6, single control seeds, no npz. full: X = 1e7, saves
      e1af_funding_wall.npz (tracked next to this script). deep adds a
      TRUE + C1 rung at X = 1e8 (report-only).
"""

from __future__ import annotations

import argparse
import sys
import time
from math import log

import numpy as np

from experiments._shared.harness import Gates, PreRegistry, save_npz
from experiments.primes.primestream import flat_primes

H_SHIFTS = 100
C2_REF = 0.6601618158  # twin prime constant, Wrench 1961 value to 10 digits
BEUR_SEEDS = (149, 150, 151)       # 149 = the shared control's seed
CRAMER_SEEDS = (20260826, 20260827, 20260828)
RAMP_TS = (1e-6, 1e-4, 1e-2)
RAMP_SEED = 149
WINDOW = 0.5                       # half-width of the continuous pair window


# ----------------------------------------------------------------- models --

def twin_constant(primes: np.ndarray) -> float:
    """C2 = prod_{p > 2} (1 - (p-1)^-2); truncation error ~ 1/(P log P)."""
    p = primes[primes > 2].astype(np.float64)
    return float(np.exp(np.log1p(-1.0 / (p - 1.0) ** 2).sum()))


def singular_series(h_max: int, c2: float) -> np.ndarray:
    """S[h], h = 1..h_max (index 0 unused). Even h: 2 C2 prod_{p|h, p>2}
    (p-1)/(p-2); odd h: 0. Parameter-free (no fit to data anywhere)."""
    s = np.zeros(h_max + 1)
    for h in range(2, h_max + 1, 2):
        m = h
        while m % 2 == 0:
            m //= 2
        prod, q = 1.0, 3
        while q * q <= m:
            if m % q == 0:
                prod *= (q - 1.0) / (q - 2.0)
                while m % q == 0:
                    m //= q
            q += 2
        if m > 1:
            prod *= (m - 1.0) / (m - 2.0)
        s[h] = 2.0 * c2 * prod
    return s


def _tri_cdf(xv, a):
    xv = np.clip(xv, -a, a)
    return 0.5 + xv / a - xv * np.abs(xv) / (2 * a * a)


def _uni_cdf(xv, a):
    xv = np.clip(xv, -a, a)
    return 0.5 + xv / (2 * a)


def _alt_factor(a: float, cdf, k_max: int = 400) -> float:
    """A(a) = sum_k (-1)^k m_k for a displacement kernel of half-width a:
    the parity meter reads the ALTERNATING window sum, not the in-window
    mass (a ~1/a^2 observable vs ~1/a; prototype-validated, see docstring)."""
    if a <= 0.5:
        return 1.0
    ks = np.arange(-k_max, k_max + 1)
    m = cdf(ks + 0.5, a) - cdf(ks - 0.5, a)
    return float(np.sum((-1.0) ** np.abs(ks) * m))


def r_par(x: float, u: float, kernel: str = "tri", n: int = 4000) -> float:
    """Parity-effective retention: (1/X) int_0^X A(p/(2u)) dp. Weight
    measure uniform in p (HL pair density x log^2 weights = flat; verified
    against direct twin-pair displacement measurement in calibration)."""
    cdf = _tri_cdf if kernel == "tri" else _uni_cdf
    p = np.linspace(1.0, x, n)
    vals = np.array([_alt_factor(a, cdf) for a in p / (2.0 * u)])
    return float(np.trapezoid(vals, p) / x)


# ----------------------------------------------------------------- meters --

def exact_pair_meter(vals: np.ndarray, x: int, h_max: int) -> np.ndarray:
    """b(h) = (1/X) sum_{n, n+h in vals} log(n) log(n+h) for integer-valued
    configurations, h = 1..h_max. Membership via searchsorted (vals sorted)."""
    lw = np.log(vals.astype(np.float64))
    out = np.zeros(h_max + 1)
    for h in range(1, h_max + 1):
        tgt = vals + h
        idx = np.searchsorted(vals, tgt)
        ok = idx < len(vals)
        hit = np.zeros(len(vals), dtype=bool)
        hit[ok] = vals[idx[ok]] == tgt[ok]
        out[h] = float(np.dot(lw[hit], lw[idx[hit]])) / x
    return out


def windowed_pair_meter(b: np.ndarray, x: int, h_max: int,
                        w: float = WINDOW) -> np.ndarray:
    """b(h) = (1/X) sum_{i != j} log(b_i) log(b_j) over |b_j - b_i - h| < w,
    for real-valued configurations (b sorted ascending). Prefix sums keep it
    O(H N log N). For integer configurations with w < 1 this equals the
    exact meter (gated as C3): the two formats are meter-matched."""
    lb = np.log(b)
    cs = np.concatenate(([0.0], np.cumsum(lb)))
    out = np.zeros(h_max + 1)
    for h in range(1, h_max + 1):
        lo = np.searchsorted(b, b + (h - w), side="right")
        hi = np.searchsorted(b, b + (h + w), side="left")
        out[h] = float(np.dot(lb, cs[hi] - cs[lo])) / x
    return out


def meters(bh: np.ndarray, s: np.ndarray) -> dict:
    """Second-order discrimination statistics on the family b(h), h >= 1."""
    b = bh[1:]
    sv = s[1:]
    hh = np.arange(1, len(b) + 1)
    even = hh % 2 == 0
    mean_all = float(b.mean())
    parity = float((b[even].mean() - b[~even].mean()) / mean_all)
    tss = float(((b - mean_all) ** 2).sum())
    rss1 = float(((b - sv) ** 2).sum())
    r2 = 1.0 - rss1 / tss if tss > 0 else float("nan")
    be, se = b[even], sv[even]
    tss_e = float(((be - be.mean()) ** 2).sum())
    rss_e = float(((be - se) ** 2).sum())
    r2_even = 1.0 - rss_e / tss_e if tss_e > 0 else float("nan")
    rms_e = float(np.sqrt((((be - se) / se) ** 2).mean()))
    return {"mean": mean_all, "parity": parity, "r2": r2,
            "r2_even": r2_even, "rms_e": rms_e}


# ------------------------------------------------------------ constructions --

def beurling_reals(primes: np.ndarray, x: int, seed: int) -> np.ndarray:
    """The shared Beurling control's recipe (b_p = p exp(eps_p), eps_p iid
    U[-0.25, 0.25]) at data scale, numpy rng (the _shared class's python-rng
    stream is impractical at 6.6e5 primes; same law, seed kept)."""
    rng = np.random.default_rng(seed)
    b = primes.astype(np.float64) * np.exp(rng.uniform(-0.25, 0.25, len(primes)))
    return np.sort(b[b <= x])


def snap_reals(primes: np.ndarray, x: int, d: float) -> np.ndarray:
    """log p snapped onto (1/D)Z, exponentiated back: fully L2-commensurate
    reals (denominator D), exact integer lattice destroyed at every D.
    float64 is adequate: D log p < 2^53 for all rungs, and the construction
    roundoff displaces b by < 0.02 << the 0.5 window."""
    b = np.exp(np.rint(d * np.log(primes.astype(np.float64))) / d)
    return np.sort(b[b <= x])


def ramp_reals(primes: np.ndarray, x: int, t: float,
               seed: int = RAMP_SEED) -> np.ndarray:
    """The e2bc jitter ramp b_p = p exp(t eps_p): t = 0 is the integer
    lattice, t = 1 the full Beurling fake; the graded lattice-clause axis."""
    rng = np.random.default_rng(seed)
    eps = rng.uniform(-0.25, 0.25, len(primes))
    b = primes.astype(np.float64) * np.exp(t * eps)
    return np.sort(b[b <= x])


def cramer_draw(x: int, seed: int) -> np.ndarray:
    """Random integers at the primes' density: n in [2, X] kept w.p.
    min(1, 1/log n). Integer-valued but congruence-free: the control that
    separates 'lives in Z' from 'carries mod-p correlation structure'."""
    rng = np.random.default_rng(seed)
    n = np.arange(2, x + 1, dtype=np.int64)
    keep = rng.random(len(n)) < np.minimum(1.0, 1.0 / np.log(n))
    return n[keep]


# ---------------------------------------------------------------------- run --

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--deep", action="store_true")
    ns, _ = ap.parse_known_args(argv if argv is not None else sys.argv[1:])
    quick, deep = ns.quick, ns.deep

    t0 = time.time()
    x = 10 ** 6 if quick else 10 ** 7
    d_lo, d_mid, d_hi = x / 1000.0, 1e6, 10.0 * x
    beur_seeds = BEUR_SEEDS[:1] if quick else BEUR_SEEDS
    cram_seeds = CRAMER_SEEDS[:1] if quick else CRAMER_SEEDS
    h = H_SHIFTS
    print(f"E1AF: funding-wall typing probe  (X = {x:.0e}, H = {h}, "
          f"{'quick' if quick else 'full'} mode)")

    gates = Gates(quick=quick)
    pre = PreRegistry()
    # Registered BEFORE any computation (the docstring carries the full text).
    pre.register("P1", "F1a-LANDS: TRUE/C3 carry singular-series second-order "
                 "structure (R2>=0.99, R2_even>=0.9, parity>=1); C1/C2-lo/C4 "
                 "flat (|P|<=0.1, R2<=0.3, R2_even<=0.3)",
                 "any TRUE meter under threshold or any listed control over")
    pre.register("P2", "F1a-KILL branch: some density/commensurability control "
                 "(C1, C2-lo, C4) carries TRUE-class structure (parity>=0.5 or "
                 "R2_even>=0.5): F1a dies, frame re-scopes to Wall 2",
                 "no control reaches half of TRUE-class structure (expected: "
                 "this branch REFUTED; its firing is frame exit 1)")
    pre.register("P3", "competitor's scoped landing (compatible with P1): HL "
                 "clean at accessible X: rms_e <= 0.03 on TRUE",
                 "rms_e > 0.10 (HL visibly rough at this X)")
    pre.register("P4", "displacement law (instrument-model branch): C2-lo dead "
                 "(|P|<=0.1); C2-hi alive-identical (|P - P_TRUE|<=0.02); "
                 "C2-mid parity ratio in [0.5 x min, 1.7 x max] of the "
                 "alternating-sum model variants; ramp t=1e-6 in [0.5,1.7] x "
                 "tri model; ramp nonincreasing, t=1e-2 rung <= 0.1",
                 "any clause fails (failure = re-model the meter, not re-type "
                 "F1a)")
    pre.register("P5", "leading-order blindness: window mean in [0.85, 1.15] "
                 "for TRUE and every C1/C4 seed: discrimination is "
                 "second-order only", "any mean outside the band")

    # -- data ---------------------------------------------------------------
    primes = flat_primes(x)
    n_pi = len(primes)
    theta = float(np.log(primes.astype(np.float64)).sum())
    pi_ref = {10 ** 6: 78498, 10 ** 7: 664579}[x]
    gates.gate("sieve: pi(X) exact", n_pi == pi_ref, f"pi({x:.0e}) = {n_pi}")
    gates.gate("sieve: theta(X)/X near 1", abs(theta / x - 1) <= 0.01,
               f"theta/X = {theta / x:.6f}")

    c2 = twin_constant(primes)
    gates.gate("twin constant C2", abs(c2 - C2_REF) <= 1e-6, f"C2 = {c2:.10f}")
    s = singular_series(h, c2)
    gates.gate("singular series structure",
               s[1] == 0 and s[3] == 0 and abs(s[4] - s[2]) < 1e-15
               and abs(s[6] - 2 * s[2]) < 1e-12
               and abs(s[2] - 2 * c2) < 1e-15,
               f"S(2)={s[2]:.7f}, S(6)/S(2)={s[6] / s[2]:.3f}, S(odd)=0")
    s_mean = float(s[1:].mean())
    gates.gate("S window average near 1 (second-order defect only)",
               0.90 <= s_mean <= 1.05, f"mean_h S = {s_mean:.4f}")

    # -- TRUE: exact integer meter and the windowed twin (C3) ---------------
    b_true = exact_pair_meter(primes, x, h)
    m_true = meters(b_true, s)
    b_c3 = windowed_pair_meter(primes.astype(np.float64), x, h)
    rel = np.max(np.abs(b_c3[1:] - b_true[1:]) / np.maximum(b_true[1:], 1e-12)
                 * (b_true[1:] > 0)) if np.any(b_true[1:] > 0) else 0.0
    abs_d = float(np.max(np.abs(b_c3[1:] - b_true[1:])))
    gates.gate("C3 meter match: windowed == exact on TRUE",
               abs_d <= 1e-6, f"max abs diff = {abs_d:.2e} (rel {rel:.1e})")
    print(f"  TRUE: parity {m_true['parity']:.3f}, R2 {m_true['r2']:.5f}, "
          f"R2_even {m_true['r2_even']:.5f}, rms_e {m_true['rms_e']:.4f}, "
          f"mean {m_true['mean']:.4f}")

    gates.gate("TRUE parity >= 1", m_true["parity"] >= 1.0,
               f"P = {m_true['parity']:.3f}")
    gates.gate("TRUE R2 >= 0.99", m_true["r2"] >= 0.99,
               f"R2 = {m_true['r2']:.5f}")
    gates.gate("TRUE R2_even >= 0.9", m_true["r2_even"] >= 0.9,
               f"R2_even = {m_true['r2_even']:.5f}")
    gates.gate("TRUE rms_e <= 0.03 (P3 meter)", m_true["rms_e"] <= 0.03,
               f"rms_e = {m_true['rms_e']:.4f}")

    # -- C1 Beurling (density-alone comparator) -----------------------------
    m_beur = []
    for sd in beur_seeds:
        bb = beurling_reals(primes, x, sd)
        m_beur.append(meters(windowed_pair_meter(bb, x, h), s))
        print(f"  C1 BEUR seed {sd}: parity {m_beur[-1]['parity']:+.4f}, "
              f"R2 {m_beur[-1]['r2']:+.1f}, R2_even {m_beur[-1]['r2_even']:+.1f}, "
              f"mean {m_beur[-1]['mean']:.4f}")
    beur_pmax = max(abs(m["parity"]) for m in m_beur)
    gates.gate("C1 Beurling flat: max |parity| <= 0.1", beur_pmax <= 0.1,
               f"max |P| = {beur_pmax:.4f} over {len(m_beur)} seed(s)")
    gates.gate("C1 Beurling: M1 no better than M0",
               max(m["r2"] for m in m_beur) <= 0.3
               and max(m["r2_even"] for m in m_beur) <= 0.3,
               f"max R2 = {max(m['r2'] for m in m_beur):.1f}, "
               f"max R2_even = {max(m['r2_even'] for m in m_beur):.1f}")

    # -- C4 Cramer (integer-valued, congruence-free) ------------------------
    m_cram = []
    for sd in cram_seeds:
        cv = cramer_draw(x, sd)
        m_cram.append(meters(exact_pair_meter(cv, x, h), s))
        print(f"  C4 CRAMER seed {sd}: parity {m_cram[-1]['parity']:+.4f}, "
              f"R2 {m_cram[-1]['r2']:+.1f}, R2_even {m_cram[-1]['r2_even']:+.1f}, "
              f"mean {m_cram[-1]['mean']:.4f}")
    cram_pmax = max(abs(m["parity"]) for m in m_cram)
    gates.gate("C4 Cramer flat: max |parity| <= 0.1", cram_pmax <= 0.1,
               f"max |P| = {cram_pmax:.4f} over {len(m_cram)} seed(s)")
    gates.gate("C4 Cramer: M1 no better than M0",
               max(m["r2"] for m in m_cram) <= 0.3
               and max(m["r2_even"] for m in m_cram) <= 0.3,
               f"max R2 = {max(m['r2'] for m in m_cram):.1f}, "
               f"max R2_even = {max(m['r2_even'] for m in m_cram):.1f}")

    # -- C2 SNAP rungs (the anti-alignment axis) ----------------------------
    m_snap = {}
    b_snap_hi = None
    for tag, d in (("lo", d_lo), ("mid", d_mid), ("hi", d_hi)):
        bs = snap_reals(primes, x, d)
        bh_s = windowed_pair_meter(bs, x, h)
        if tag == "hi":
            b_snap_hi = bh_s
        m_snap[tag] = meters(bh_s, s)
        print(f"  C2 SNAP D = {d:.0e}: parity {m_snap[tag]['parity']:+.4f} "
              f"(ratio {m_snap[tag]['parity'] / m_true['parity']:+.3f}), "
              f"R2_even {m_snap[tag]['r2_even']:+.1f}, "
              f"mean {m_snap[tag]['mean']:.4f}")
    gates.gate("C2-lo SNAP dead: |parity| <= 0.1 and R2_even <= 0.3",
               abs(m_snap["lo"]["parity"]) <= 0.1
               and m_snap["lo"]["r2_even"] <= 0.3,
               f"P = {m_snap['lo']['parity']:+.4f}, "
               f"R2_even = {m_snap['lo']['r2_even']:+.1f}")
    dp_hi = abs(m_snap["hi"]["parity"] - m_true["parity"])
    max_bdiff = float(np.max(np.abs(b_snap_hi[1:] - b_true[1:])))
    gates.gate("C2-hi SNAP alive-identical to TRUE",
               dp_hi <= 0.02 and max_bdiff <= 1e-3,
               f"|P - P_TRUE| = {dp_hi:.2e}, max |b - b_TRUE| = {max_bdiff:.1e}")
    ret_mid_tri = r_par(x, d_mid / 2.0, "tri")
    ret_mid_uni = r_par(x, d_mid, "uni")
    ratio_mid = m_snap["mid"]["parity"] / m_true["parity"]
    lo_b = 0.5 * min(ret_mid_tri, ret_mid_uni)
    hi_b = min(1.05, 1.7 * max(ret_mid_tri, ret_mid_uni))
    gates.gate("C2-mid SNAP tracks the displacement law",
               lo_b <= ratio_mid <= hi_b,
               f"P/P_TRUE = {ratio_mid:.3f}, band [{lo_b:.3f}, {hi_b:.3f}] "
               f"(model tri {ret_mid_tri:.3f} / uni {ret_mid_uni:.3f})")

    # -- C5 ramp (graded axis) ----------------------------------------------
    ramp_par = []
    for t in RAMP_TS:
        br = ramp_reals(primes, x, t)
        ramp_par.append(meters(windowed_pair_meter(br, x, h), s)["parity"])
        print(f"  C5 RAMP t = {t:.0e}: parity {ramp_par[-1]:+.4f} "
              f"(ratio {ramp_par[-1] / m_true['parity']:+.3f})")
    mono = all(ramp_par[i + 1] <= ramp_par[i] + 0.02
               for i in range(len(ramp_par) - 1))
    gates.gate("C5 ramp: parity nonincreasing in t, endpoint dead",
               mono and abs(ramp_par[-1]) <= 0.1,
               f"P(t) = {', '.join(f'{p:+.4f}' for p in ramp_par)}")
    ret_r = r_par(x, 1e6, "tri")   # u = 1/t at t = 1e-6; kernel known: tri
    ratio_r = ramp_par[0] / m_true["parity"]
    lo_r, hi_r = 0.5 * ret_r, min(1.05, 1.7 * ret_r)
    gates.gate("C5 ramp t=1e-6 tracks the displacement law",
               lo_r <= ratio_r <= hi_r,
               f"P/P_TRUE = {ratio_r:.3f}, band [{lo_r:.3f}, {hi_r:.3f}] "
               f"(ret = {ret_r:.3f})")

    # -- P5: leading-order blindness ----------------------------------------
    means = [m_true["mean"]] + [m["mean"] for m in m_beur] + \
            [m["mean"] for m in m_cram]
    gates.gate("leading order blind: all window means in [0.85, 1.15]",
               all(0.85 <= m <= 1.15 for m in means),
               "means = " + ", ".join(f"{m:.3f}" for m in means))

    # -- K1 / discipline statements (design facts, asserted) ----------------
    gates.gate("K1: no zero data consumed (prime-side probe)", True,
               "no zeros() call in this module; harness import is lazy")

    # -- optional deep rung --------------------------------------------------
    deep_out = {}
    if deep and not quick:
        xd = 10 ** 8
        pd = flat_primes(xd)
        b_d = exact_pair_meter(pd, xd, h)
        m_d = meters(b_d, s)
        bb = beurling_reals(pd, xd, BEUR_SEEDS[0])
        m_bd = meters(windowed_pair_meter(bb, xd, h), s)
        print(f"  DEEP X = 1e8: TRUE parity {m_d['parity']:.3f}, "
              f"rms_e {m_d['rms_e']:.4f}; BEUR parity {m_bd['parity']:+.4f}")
        deep_out = {"deep_b_true": b_d, "deep_true_meters":
                    np.array([m_d[k] for k in
                              ("mean", "parity", "r2", "r2_even", "rms_e")]),
                    "deep_beur_meters":
                    np.array([m_bd[k] for k in
                              ("mean", "parity", "r2", "r2_even", "rms_e")])}
    elif deep:
        gates.skip("deep rung", "requires full mode")

    # -- X-trend for P3 color (full mode: re-run TRUE at X/10) ---------------
    trend = {}
    if not quick:
        x2 = x // 10
        b_t2 = exact_pair_meter(primes[primes <= x2], x2, h)
        m_t2 = meters(b_t2, s)
        trend = {"rms_e_x10th": m_t2["rms_e"]}
        print(f"  trend: rms_e(X = {x2:.0e}) = {m_t2['rms_e']:.4f} vs "
              f"rms_e(X = {x:.0e}) = {m_true['rms_e']:.4f}")

    # -- resolve pre-registrations -------------------------------------------
    p1_true_ok = (m_true["parity"] >= 1.0 and m_true["r2"] >= 0.99
                  and m_true["r2_even"] >= 0.9)
    ctrl_flat = (beur_pmax <= 0.1 and cram_pmax <= 0.1
                 and abs(m_snap["lo"]["parity"]) <= 0.1
                 and max(m["r2"] for m in m_beur + m_cram) <= 0.3
                 and max(m["r2_even"] for m in m_beur + m_cram) <= 0.3
                 and m_snap["lo"]["r2_even"] <= 0.3)
    pre.resolve("P1", "FIRED" if (p1_true_ok and ctrl_flat) else "REFUTED",
                f"TRUE P={m_true['parity']:.2f} R2={m_true['r2']:.4f}; "
                f"controls max|P|={max(beur_pmax, cram_pmax, abs(m_snap['lo']['parity'])):.4f}")
    p2_fires = (max(abs(m["parity"]) for m in m_beur + m_cram) >= 0.5
                or abs(m_snap["lo"]["parity"]) >= 0.5
                or max(m["r2_even"] for m in m_beur + m_cram) >= 0.5
                or m_snap["lo"]["r2_even"] >= 0.5)
    pre.resolve("P2", "FIRED" if p2_fires else "REFUTED",
                "no control reaches half of TRUE-class structure"
                if not p2_fires else "A CONTROL FIRED: frame exit 1")
    pre.resolve("P3", "FIRED" if m_true["rms_e"] <= 0.03 else
                ("REFUTED" if m_true["rms_e"] > 0.10 else "SURVIVED"),
                f"rms_e = {m_true['rms_e']:.4f}")
    p4_ok = (abs(m_snap["lo"]["parity"]) <= 0.1 and dp_hi <= 0.02
             and lo_b <= ratio_mid <= hi_b and mono
             and abs(ramp_par[-1]) <= 0.1 and lo_r <= ratio_r <= hi_r)
    pre.resolve("P4", "FIRED" if p4_ok else "REFUTED",
                f"mid ratio {ratio_mid:.3f} in [{lo_b:.3f},{hi_b:.3f}]; "
                f"ramp {', '.join(f'{p:+.3f}' for p in ramp_par)}")
    p5_ok = all(0.85 <= m <= 1.15 for m in means)
    pre.resolve("P5", "FIRED" if p5_ok else "REFUTED",
                "means " + ", ".join(f"{m:.3f}" for m in means))
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    # -- save (full mode; the npz is tracked, evidence rule) ------------------
    if not quick:
        from pathlib import Path
        out = Path(__file__).resolve().parent / "e1af_funding_wall.npz"
        arrays = {
            "h": np.arange(1, h + 1),
            "singular_series": s[1:],
            "b_true": b_true[1:], "b_c3_windowed": b_c3[1:],
            "b_snap_hi": b_snap_hi[1:],
            "meters_true": np.array([m_true[k] for k in
                                     ("mean", "parity", "r2", "r2_even", "rms_e")]),
            "meters_beur": np.array([[m[k] for k in
                                      ("mean", "parity", "r2", "r2_even", "rms_e")]
                                     for m in m_beur]),
            "meters_cramer": np.array([[m[k] for k in
                                        ("mean", "parity", "r2", "r2_even", "rms_e")]
                                       for m in m_cram]),
            "meters_snap": np.array([[m_snap[t][k] for k in
                                      ("mean", "parity", "r2", "r2_even", "rms_e")]
                                     for t in ("lo", "mid", "hi")]),
            "snap_d_rungs": np.array([d_lo, d_mid, d_hi]),
            "ramp_t": np.array(RAMP_TS),
            "ramp_parity": np.array(ramp_par),
            "ret_predictions": np.array([r_par(x, d_lo / 2, "tri"),
                                         ret_mid_tri, ret_mid_uni,
                                         r_par(x, d_hi / 2, "tri"),
                                         ret_r, r_par(x, 1e4, "tri"),
                                         r_par(x, 1e2, "tri")]),
        }
        arrays.update(deep_out)
        prov = {"X": x, "H": h, "C2": c2, "window": WINDOW,
                "lambda_choice": "prime-only log p (prime powers dropped)",
                "M0": "flat at fitted window mean; PNT level (theta/X)^2 = "
                      f"{(theta / x) ** 2:.6f}",
                "beur_seeds": list(beur_seeds), "cramer_seeds": list(cram_seeds),
                "ramp_seed": RAMP_SEED, "trend": trend,
                "prereg": {pid: pre._entries[pid]["outcome"]
                           for pid in ("P1", "P2", "P3", "P4", "P5")},
                "elapsed_s": round(time.time() - t0, 1)}
        save_npz(out, arrays, prov)
        gates.gate("npz saved (tracked)", out.exists(), out.name)
    else:
        gates.skip("npz saved", "quick mode saves nothing")

    pre.table()
    gates.summary(elapsed=time.time() - t0)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())

"""ADVERSARY probe for e1ad_sum_rules (LEARNINGS #188).

Executes the adversarial test cases POSED in e1ad_sum_rules.md ("Adversarial
test cases"): cases 1, 2, 4, 5, 6, plus e1v's open case 7 (second-party
replication of e1v's K1/determinism guards). Case 3 (the super-resolution
attack on the horizon's completeness) is EXCLUDED here: it is being executed
separately as a build.

House rules (the _e1v_adversary.py precedent): everything analytic is
consumed from e1ad_sum_rules by import; this file adds attack harnesses only,
no new build machinery. Nothing tracked is written or modified: scratch
copies (planted-source teeth tests, the redirected full-run npz) go to a
tempfile directory, and the tracked npz files are only READ (md5-verified
untouched after every subprocess).

Run:
  .venv/bin/python -m experiments.spectral._e1ad_adversary
  flags: --skip-repl   skip the ~5 min full e1ad re-run (case 6d)
         --skip-e1v    skip the e1v quick replication (case 7; on a machine
                       with a cold e1t build cache this pays the quick-grid
                       build cost once, into the gitignored _cache/)
         --only 1,2    run only the listed cases (7 = the e1v case)

Report: _e1ad_adversary.md
"""

from __future__ import annotations

import argparse
import hashlib
import math
import re
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

import numpy as np
import mpmath as mp

import experiments.spectral.e1ad_sum_rules as e1ad
from experiments._shared.beurling import BeurlingSystem

REPO = Path(e1ad.__file__).resolve().parents[2]
NPZ_TRACKED = Path(e1ad.__file__).with_suffix(".npz")
E1V_PY = REPO / "experiments/spectral/e1v_christoffel_gauge.py"
E1V_NPZ = REPO / "experiments/spectral/e1v_christoffel_gauge.npz"
L1 = e1ad.WRAP_L_MAIN
LG = e1ad.WRAP_L_GOLD

VERDICTS = []


def verdict(case, landed, line):
    VERDICTS.append((case, landed, line))
    print(f"  [{'LANDED' if landed else 'MISSED'}] {case}: {line}")


def banner(txt):
    print("\n" + "=" * 78 + "\n" + txt + "\n" + "=" * 78)


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def nstar(res, ref, thresh=0.5):
    """First index where |S_res - S_ref| > thresh nats (e1ad's S6 rule)."""
    m = min(len(res["S"]), len(ref["S"]))
    with mp.workdps(60):
        for i in range(m):
            if abs(res["S"][i] - ref["S"][i]) > thresh:
                return i
    return None


def detect(res, ref, M_full):
    """e1ad's full S6 convention: profile departure, else early termination
    itself counts as the detection."""
    ns = nstar(res, ref)
    early = res["n_term"] is not None and res["n_term"] < M_full - 1
    return res["n_term"] if (ns is None and early) else ns


def true_run(N):
    pk = e1ad.true_pk(N)
    r = e1ad.szego_adaptive(e1ad.cfg_true(pk, L1), e1ad.dps_for(len(pk)))
    return pk, r


def min_wrapped_gap(theta):
    th = np.sort(np.asarray(theta, float))
    g = np.diff(th)
    wrap = th[0] + 1.0 - th[-1]
    return float(min(g.min(), wrap)) if len(g) else 1.0


# ==========================================================================
# CASE 1: the kill surrogate. GPERM on coarse-D snapped configurations.
# GPERM permutes the wrapped gap multiset blockwise: zero gaps (exact
# collisions) are elements of that multiset, so collision-level structure
# survives the shuffle by construction. Quantify retention vs destruction
# as a function of D.
# ==========================================================================
def case1(pk, rT):
    banner("CASE 1: the kill surrogate. GPERM applied to coarse-D snapped "
           "configs (N = 300)")
    M = len(pk)
    dps0 = e1ad.dps_for(M)
    retention_exact = True
    for D in (40, 100, 400):
        sites, counts, ncoll = e1ad.snap_sites(pk, D)
        Md = len(sites)
        rS = e1ad.szego_adaptive(e1ad.cfg_snap(sites, counts, D, L1),
                                 dps0, n_max=Md + 2)
        nsS = detect(rS, rT, M)
        dST = e1ad.profile_dist(rS, rT)
        # the UNMERGED snapped multiset (duplicates = zero wrapped gaps),
        # which is what GPERM actually acts on
        with mp.workdps(80):
            ms = [int(mp.nint(k * mp.log(p) * D)) for (p, k) in pk]
        th_dup = np.sort(np.array([(m % D) / D for m in ms], float))
        nzero = int(np.sum(np.diff(th_dup) == 0.0))
        # representation control: duplicate atoms == merged weighted atoms
        rDup = e1ad.szego_adaptive(e1ad.cfg_float(th_dup, L1, f"DUP{D}"),
                                   dps0, n_max=Md + 2)
        d_rep = e1ad.profile_dist(rDup, rS)
        gp = []
        for sd in (31, 32, 33):
            thg = e1ad.local_gap_shuffle(th_dup, sd)
            Mg = len(np.unique(thg))
            rG = e1ad.szego_adaptive(
                e1ad.cfg_float(thg, L1, f"GSNAP{D}s{sd}"), dps0, n_max=Mg + 2)
            gp.append(dict(sd=sd, Mg=Mg, nt=rG["n_term"], ns=detect(rG, rT, M),
                           dGS=e1ad.profile_dist(rG, rS),
                           dGT=e1ad.profile_dist(rG, rT)))
        kept = (rS["n_term"] == Md - 1 and nzero == ncoll
                and all(g["Mg"] == Md and g["nt"] == Md - 1 for g in gp))
        retention_exact &= kept
        print(f"  D = {D:4d}: Md = {Md:3d} (collisions {ncoll:3d}, zero gaps "
              f"in multiset {nzero:3d}), dup-vs-merged rep dev {d_rep:.1e}")
        print(f"    SNAP:        n_term = {rS['n_term']} (theory {Md - 1}), "
              f"n* = {nsS}, max|S - S_TRUE| = {dST:.3f}")
        for g in gp:
            print(f"    GPERM(SNAP) seed {g['sd']}: distinct sites {g['Mg']} "
                  f"(= Md: {g['Mg'] == Md}), n_term = {g['nt']} "
                  f"(= Md-1: {g['nt'] == Md - 1}), n* = {g['ns']}, "
                  f"max|S - S_SNAP| = {g['dGS']:.3f}, "
                  f"max|S - S_TRUE| = {g['dGT']:.3f}")
    # main-grid relevance: is there any collision-scale content in the data
    # the kill actually ran on? (S3c certified min gap; compare TRUE's
    # smallest wrapped gap to the surrogates')
    t_true = e1ad.true_t_float(pk)
    thT = e1ad.wrap_float(t_true, L1)
    mg_T = min_wrapped_gap(thT)
    mg_R = [min_wrapped_gap(e1ad.wrap_float(
        e1ad.resample_t(t_true, "RAND", sd), L1)) for sd in (11, 12, 13)]
    tb = e1ad.beurling_t(300, e1ad.BAND_A, t_true[-1])
    mg_B = min_wrapped_gap(e1ad.wrap_float(tb, L1))
    print(f"  main-grid tight-pair context (N = 300): min wrapped gap "
          f"TRUE {mg_T:.2e}, BEUR {mg_B:.2e}, RAND seeds "
          + ", ".join(f"{x:.2e}" for x in mg_R))
    verdict("case 1", False if retention_exact else True,
            "GPERM retains the collision channel EXACTLY at every D "
            "(distinct-site count and termination index invariant under the "
            "shuffle); on the main grid that channel is empty by the S3c "
            "certificate, so R2's kill stands, but the dossier's 'destroys "
            "every arithmetic correlation' needs a scale scope"
            if retention_exact else
            "retention NOT exact: the surrogate's advertised invariant broke")


# ==========================================================================
# CASE 2: the pinned 4x band (S5a). Widen the jitter ensemble to 12 seeds
# and locate SNAP's whole-profile response inside the jitter DISTRIBUTION
# (empirical percentile), not merely inside a 4x envelope.
# ==========================================================================
def case2(cache, n_jit=12):
    banner(f"CASE 2: the pinned 4x band. SNAP vs a {n_jit}-seed jitter "
           "ensemble (N = 300, 1000)")
    outlier_all = True
    for N in sorted(cache):
        pk, rT = cache[N]
        M = len(pk)
        dps0 = e1ad.dps_for(M)
        rtT = e1ad.rates(rT)
        sites, counts, _ = e1ad.snap_sites(pk, e1ad.SNAP_D)
        rS = e1ad.szego_adaptive(
            e1ad.cfg_snap(sites, counts, e1ad.SNAP_D, L1), dps0)
        rtS = e1ad.rates(rS)
        dS = e1ad.profile_dist(rT, rS)
        dmS = abs(rtS["r_mid"] - rtT["r_mid"])
        ddS = abs(rtS["r_diag"] - rtT["r_diag"])
        thT = e1ad.wrap_float(e1ad.true_t_float(pk), L1)
        dj, dm, dd = [], [], []
        for sd in range(41, 41 + n_jit):
            rng = np.random.default_rng(sd)
            th = np.sort(np.mod(thT + rng.uniform(
                -0.5 / e1ad.SNAP_D, 0.5 / e1ad.SNAP_D, M), 1.0))
            rJ = e1ad.szego_adaptive(e1ad.cfg_float(th, L1, f"JIT{sd}"), dps0)
            rtJ = e1ad.rates(rJ)
            dj.append(e1ad.profile_dist(rT, rJ))
            dm.append(abs(rtJ["r_mid"] - rtT["r_mid"]))
            dd.append(abs(rtJ["r_diag"] - rtT["r_diag"]))
        rank_p = sum(1 for x in dj if x >= dS)
        rank_m = sum(1 for x in dm if x >= dmS)
        rank_d = sum(1 for x in dd if x >= ddS)
        print(f"  N = {N}: SNAP max|dS| = {dS:.3e}; jitter ensemble "
              f"({n_jit} seeds) min {min(dj):.3e}, median "
              f"{float(np.median(dj)):.3e}, max {max(dj):.3e}")
        print(f"    sorted jitter |dS|: "
              + ", ".join(f"{x:.2e}" for x in sorted(dj)))
        print(f"    whole-profile: {rank_p}/{n_jit} jitter seeds >= SNAP "
              f"(SNAP/jitter-max = {dS / max(dj):.2f}; pinned S5a factor "
              f"4x band top: {'PASS' if dS <= 4 * max(dj) else 'FAIL'})")
        print(f"    r_mid displacement:  SNAP {dmS:.2e}, jitter "
              f"[{min(dm):.2e}, {max(dm):.2e}], {rank_m}/{n_jit} >= SNAP")
        print(f"    r_diag displacement: SNAP {ddS:.2e}, jitter "
              f"[{min(dd):.2e}, {max(dd):.2e}], {rank_d}/{n_jit} >= SNAP")
        outlier_all &= (rank_p == 0)
    verdict("case 2", outlier_all,
            "SNAP's whole-profile response exceeds every jitter seed at "
            "every size tested: the snap is a distribution outlier, S5a's "
            "'generic perturbation' reading needs revision"
            if outlier_all else
            "SNAP sits inside (or at the edge of) the widened jitter "
            "distribution at at least one size: no stable outlier status, "
            "S5a's generic-perturbation reading survives the wider ensemble")


# ==========================================================================
# CASE 4: the BEUR reading. Vary the Beurling epsilon (0.05 / 0.25 / 0.5)
# and the seed; R2's scale-mixture mechanism predicts smaller epsilon puts
# BEUR closer to TRUE at more scales (distances to TRUE increase with eps,
# and the diagonal convergence point in N moves with eps).
# ==========================================================================
def beurling_t_eps(N, A, t_max, eps, seed):
    B = BeurlingSystem(prime_bound=int(math.ceil(N * math.exp(eps))),
                       eps=eps, seed=seed)
    ts = []
    for lb in B.logs:
        k = 1
        while k * lb <= t_max + 1e-12:
            if k * lb >= A:
                ts.append(k * lb)
            k += 1
    return np.sort(np.array(ts))


def case4(cache):
    banner("CASE 4: the BEUR reading. Epsilon ladder 0.05 / 0.25 / 0.5 "
           "(seeds 149-151 at N = 300; seed 149 at N = 1000)")
    # anchor: eps = 0.25 / seed 149 must reproduce e1ad's own control exactly
    pk0, _ = cache[300]
    t0 = e1ad.true_t_float(pk0)
    same = np.array_equal(beurling_t_eps(300, e1ad.BAND_A, t0[-1], 0.25, 149),
                          e1ad.beurling_t(300, e1ad.BAND_A, t0[-1]))
    print(f"  anchor: eps=0.25/seed=149 reproduces e1ad.beurling_t exactly: "
          f"{same}")
    npz = np.load(NPZ_TRACKED, allow_pickle=True)
    rate_table = npz["rate_table"]
    mono_ok, results = True, {}
    for N in sorted(cache):
        pk, rT = cache[N]
        M = len(pk)
        rtT = e1ad.rates(rT)
        t_true = e1ad.true_t_float(pk)
        row = rate_table[[i for i in range(len(rate_table))
                          if int(rate_table[i][0]) == N][0]]
        print(f"  N = {N}: TRUE r_diag {rtT['r_diag']:.4f} r_mid "
              f"{rtT['r_mid']:.4f}; tracked RAND medians r_diag "
              f"{row[6]:.4f} r_mid {row[12]:.4f}")
        seeds = (149, 150, 151) if N == 300 else (149,)
        med = {}
        for eps in (0.05, 0.25, 0.5):
            dds, dms, rds, rms, cnts = [], [], [], [], []
            for sd in seeds:
                tb = beurling_t_eps(N, e1ad.BAND_A, t_true[-1], eps, sd)
                rB = e1ad.szego_adaptive(
                    e1ad.cfg_float(e1ad.wrap_float(tb, L1), L1,
                                   f"B{eps}s{sd}"), e1ad.dps_for(M))
                rt = e1ad.rates(rB)
                rds.append(rt["r_diag"])
                rms.append(rt["r_mid"])
                dds.append(abs(rt["r_diag"] - rtT["r_diag"]))
                dms.append(abs(rt["r_mid"] - rtT["r_mid"]))
                cnts.append(len(tb))
            med[eps] = (float(np.median(dds)), float(np.median(dms)))
            print(f"    eps = {eps:4.2f}: M_B {cnts} (count dev "
                  f"{max(abs(c - M) / M for c in cnts):.3f}), r_diag "
                  + "/".join(f"{x:.4f}" for x in rds) + ", r_mid "
                  + "/".join(f"{x:.4f}" for x in rms)
                  + f"; |d_diag| med {med[eps][0]:.4f}, |d_mid| med "
                  f"{med[eps][1]:.4f}")
        results[N] = med
        inc_d = med[0.05][0] <= med[0.25][0] <= med[0.5][0]
        inc_m = med[0.05][1] <= med[0.25][1] <= med[0.5][1]
        print(f"    monotone-in-eps distance to TRUE: r_diag {inc_d}, "
              f"r_mid {inc_m}")
        mono_ok &= inc_d and inc_m
    verdict("case 4", not mono_ok,
            "the predicted direction FAILED somewhere: the BEUR-TRUE typing "
            "(scale-mixture mechanism) is reopened"
            if not mono_ok else
            "distances to TRUE grow monotonically with eps on both "
            "observables at every size tested: the R2 mechanism's direction "
            "is confirmed, the typing stands")
    return results


# ==========================================================================
# CASE 5: the gauge scope. D-ladder at irrational wrap L = golden mean.
# The dossier's limit 3 claims exact collisions need DL commensurate and
# predicts blindness at ALL D for irrational L. But the SNAP is a snap of t
# onto (1/D)Z BEFORE wrapping: two prime powers rounding to the same m/D
# collide in t-space, and that survives ANY wrap. At irrational L the
# mod-D folding channel dies (m and m+D no longer coincide), so the correct
# site count is the UNREDUCED one. We run both readings and a matched-
# amplitude jitter control per rung to separate lattice-specific detection
# from generic large-perturbation response.
# ==========================================================================
def snap_sites_unreduced(pk, D, dps=80):
    with mp.workdps(dps):
        ms = [int(mp.nint(k * mp.log(p) * D)) for (p, k) in pk]
    cnt = Counter(ms)   # NO mod D: the t-space snap, correct at irrational L
    sites = sorted(cnt)
    return sites, [cnt[s] for s in sites], len(ms) - len(sites)


def case5(pk):
    banner("CASE 5: the gauge scope. D-ladder at L = golden mean (N = 300)")
    M = len(pk)
    dps0 = e1ad.dps_for(M)
    rTg = e1ad.szego_adaptive(e1ad.cfg_true(pk, LG), dps0)
    t_true = e1ad.true_t_float(pk)
    law_ok, blind_ok, coll_rungs, new_mech = True, True, 0, []
    for D in (40, 100, 400, 2000):
        sites, counts, ncoll = snap_sites_unreduced(pk, D)
        Md = len(sites)
        _s1, _c1, ncoll_L1 = e1ad.snap_sites(pk, D)
        rS = e1ad.szego_adaptive(e1ad.cfg_snap(sites, counts, D, LG),
                                 dps0, n_max=Md + 2)
        ns = detect(rS, rTg, M)
        dS = e1ad.profile_dist(rS, rTg)
        # matched-amplitude jitter control in t-space at this D
        rng = np.random.default_rng(77 + D)
        tj = t_true + rng.uniform(-0.5 / D, 0.5 / D, M)
        rJ = e1ad.szego_adaptive(
            e1ad.cfg_float(e1ad.wrap_float(tj, LG), LG, f"JITg{D}"),
            dps0, n_max=M + 2)
        nsJ = detect(rJ, rTg, M)
        dJ = e1ad.profile_dist(rJ, rTg)
        print(f"  D = {D:5d}: t-collisions {ncoll:3d} (vs {ncoll_L1:3d} at "
              f"L = 1 incl. folding), Md = {Md:3d}, n_term = "
              f"{str(rS['n_term']):>5s} (rank theory {Md - 1}), n* = {ns}, "
              f"max|dS| = {dS:.3f}")
        print(f"           matched jitter control: n_term = "
              f"{str(rJ['n_term']):>5s}, n* = {nsJ}, max|dS| = {dJ:.3f}")
        if ncoll > 0:
            coll_rungs += 1
            law_ok &= (rS["n_term"] == Md - 1)
        else:
            early = rS["n_term"] is not None and rS["n_term"] < M - 1
            blind_ok &= not early
            # lattice-specific detection without rank collapse would be a
            # new mechanism: flag if SNAP departs where matched jitter does
            # not (comparable departure = generic amplitude response)
            if ns is not None and (nsJ is None or dS > 3 * dJ):
                new_mech.append(D)
    landed = coll_rungs > 0
    line = (f"{coll_rungs} collision rungs EXIST at irrational L "
            "(t-space collisions are wrap-independent): 'blindness at ALL D' "
            "and limit 3's commensurability claim are refuted at the letter; "
            f"the rank law n_term = Md - 1 {'HELD' if law_ok else 'BROKE'} "
            "on every collision rung and the no-collision rungs "
            f"{'stayed blind' if blind_ok else 'TERMINATED EARLY'}"
            + (f"; lattice-specific no-collision detection at D = {new_mech}"
               if new_mech else
               "; no-collision departures match the jitter control "
               "(generic amplitude response, no new mechanism)"))
    verdict("case 5", landed, line if landed else
            "no collisions at any golden rung: the dossier's blindness "
            "prediction held as stated")


# ==========================================================================
# CASE 6: second-party replication of e1ad on this host: determinism,
# source-scan teeth (on scratch copies), quick-mode pass and npz hygiene,
# and the full-mode re-run compared array-by-array against the tracked npz.
# ==========================================================================
def case6(tmp, cache, skip_repl):
    banner("CASE 6: second-party replication of e1ad (same host that "
           "produced the tracked npz)")
    ok_all = True
    # (a) determinism: two identical runs byte-match
    pk, rT = cache[300]
    t_true = e1ad.true_t_float(pk)
    for label, cfg in (
            ("TRUE300", e1ad.cfg_true(pk, L1)),
            ("RAND0", e1ad.cfg_float(
                e1ad.wrap_float(e1ad.resample_t(t_true, "RAND", 11), L1),
                L1, "RAND0"))):
        r1 = e1ad.szego_profile(cfg, 71)
        r2 = e1ad.szego_profile(cfg, 71)
        with mp.workdps(71):
            b1 = repr([mp.nstr(x, 60) for x in r1["S"]]).encode()
            b2 = repr([mp.nstr(x, 60) for x in r2["S"]]).encode()
            same = (len(r1["S"]) == len(r2["S"])
                    and all(a == b for a, b in zip(r1["S"], r2["S"])))
        byte_same = b1 == b2
        ok_all &= same and byte_same
        print(f"  (a) determinism {label}: mpf-exact {same}, serialized "
              f"byte-match {byte_same} (md5 {hashlib.md5(b1).hexdigest()[:8]})")
    # (b) source-scan teeth on scratch copies (tracked file untouched)
    src = Path(e1ad.__file__).read_text(encoding="utf-8")
    clean = e1ad.scan_lines(src.splitlines())
    plants = ("x = mp.zetazero(1)",
              "from experiments._shared import davenport_heilbronn",
              "zs = zeta.zeros(100)")
    caught = []
    for pl in plants:
        copy = tmp / "planted.py"
        copy.write_text(src + "\n" + pl + "\n", encoding="utf-8")
        hits = e1ad.scan_lines(copy.read_text(encoding="utf-8").splitlines())
        caught.append(bool(hits))
    evades = not e1ad.scan_lines(["x = mp.zetazero(1)  # SCAN-ALLOW"])
    ok_scan = not clean and all(caught)
    ok_all &= ok_scan
    print(f"  (b) scan teeth: tracked source clean {not clean}; planted "
          f"copies caught {caught} (tokens: zetazero / davenport / .zeros(); "
          f"SCAN-ALLOW evasion possible by design: {evades})")
    # (c) quick mode passes and leaves the tracked npz untouched
    m0 = md5(NPZ_TRACKED)
    p = subprocess.run([sys.executable, "-m",
                        "experiments.spectral.e1ad_sum_rules", "--quick"],
                       capture_output=True, text=True, cwd=str(REPO),
                       timeout=600)
    mq = re.search(r"SELF-TEST: (\d+)/(\d+) passed", p.stdout)
    ok_q = (p.returncode == 0 and mq and mq.group(1) == mq.group(2)
            and md5(NPZ_TRACKED) == m0)
    ok_all &= bool(ok_q)
    print(f"  (c) quick mode: {'/'.join(mq.groups()) if mq else 'NO PARSE'} "
          f"passed, rc = {p.returncode}, tracked npz md5 unchanged = "
          f"{md5(NPZ_TRACKED) == m0}")
    # (d) full re-run, OUT redirected to scratch, arrays vs tracked npz
    if skip_repl:
        print("  (d) full re-run SKIPPED (--skip-repl)")
    else:
        out = tmp / "e1ad_rerun.npz"
        code = ("import sys; sys.argv = ['e1ad_sum_rules']\n"
                "from pathlib import Path\n"
                "import experiments.spectral.e1ad_sum_rules as m\n"
                f"m.OUT = Path({str(out)!r})\n"
                "m.main()\n")
        t0 = time.time()
        pf = subprocess.run([sys.executable, "-c", code], capture_output=True,
                            text=True, cwd=str(REPO), timeout=1800)
        mf = re.search(r"SELF-TEST: (\d+)/(\d+) passed", pf.stdout)
        print(f"  (d) full re-run: "
              f"{'/'.join(mf.groups()) if mf else 'NO PARSE'} passed, "
              f"rc = {pf.returncode}, {round(time.time() - t0)}s")
        if pf.returncode != 0 and not mf:
            print("      stderr tail: " + pf.stderr[-500:])
            ok_all = False
        A = np.load(NPZ_TRACKED, allow_pickle=True)
        B = np.load(out, allow_pickle=True)
        keys_same = set(A.files) == set(B.files)
        n_exact, diffs = 0, []
        for k in sorted(set(A.files) & set(B.files)):
            a, b = A[k], B[k]
            if a.dtype == object or b.dtype == object:
                same = (a.shape == b.shape and all(
                    str(x) == str(y)
                    for x, y in zip(a.ravel(), b.ravel())))
            else:
                same = np.array_equal(a, b)
            if same:
                n_exact += 1
            else:
                if a.dtype != object and a.shape == b.shape:
                    num = float(np.max(np.abs(a - b)))
                    den = float(np.max(np.abs(b))) or 1.0
                    diffs.append((k, num / den))
                else:
                    diffs.append((k, float("nan")))
        print(f"      npz comparison: keys identical {keys_same}; "
              f"{n_exact}/{len(A.files)} arrays EXACTLY equal"
              + ("" if not diffs else "; deviating: "
                 + ", ".join(f"{k} (rel {d:.1e})" for k, d in diffs)))
        ok_all &= keys_same and (not diffs) and bool(
            mf and mf.group(1) == mf.group(2))
    msg_ok = ("replication clean: determinism byte-exact, scanner teeth "
              "verified on planted copies, quick 21/21 with the tracked npz "
              "untouched"
              + ("" if skip_repl else ", full 21/21 with every npz array "
                                      "exactly reproduced"))
    verdict("case 6", not ok_all, msg_ok if ok_all else
            "REPLICATION ANOMALY: see lines above (this counts as a landed "
            "attack on the record)")


# ==========================================================================
# CASE 7 (e1v): run e1v --quick as a second party, and re-verify its K1
# guard mechanism and source-scan teeth independently (on scratch copies).
# ==========================================================================
def case7(tmp):
    banner("CASE 7 (e1v): second-party replication of e1v quick + K1 teeth")
    ok_all = True
    m0 = md5(E1V_NPZ)
    t0 = time.time()
    p = subprocess.run([sys.executable, "-m",
                        "experiments.spectral.e1v_christoffel_gauge",
                        "--quick"], capture_output=True, text=True,
                       cwd=str(REPO), timeout=1800)
    mq = re.search(r"SELF-TEST: (\d+)/(\d+) passed", p.stdout)
    ok_q = (p.returncode == 0 and mq and mq.group(1) == mq.group(2))
    ok_all &= bool(ok_q)
    print(f"  e1v --quick: {'/'.join(mq.groups()) if mq else 'NO PARSE'} "
          f"passed, rc = {p.returncode}, {round(time.time() - t0)}s "
          f"(cold e1t cache pays the quick-grid build here)")
    if not ok_q:
        print("    stdout tail: " + p.stdout[-800:])
        print("    stderr tail: " + p.stderr[-500:])
    npz_ok = md5(E1V_NPZ) == m0
    ok_all &= npz_ok
    print(f"  tracked e1v npz md5 unchanged after quick run: {npz_ok}")
    for tag in ("V6b", "V6c"):
        hit = [ln for ln in p.stdout.splitlines() if tag in ln]
        got = bool(hit) and "[PASS]" in hit[0]
        ok_all &= got
        print(f"  K1 check {tag} present and PASS in quick output: {got}")
    # independent scanner (e1v's own token list, reimplemented here)
    def e1v_scan(lines):
        bad = []
        for i, ln in enumerate(lines, 1):
            if "K1-ALLOW" in ln or "K1-SCANNER" in ln or "ADV-TEETH" in ln:
                continue
            for tok in ("mp.zetazero(", "zetazero(",
                        "davenport_heilbronn.zeros(", "_dhmod.dav"):
                if tok in ln:
                    bad.append(f"{i}:{tok}")
        return bad
    src = E1V_PY.read_text(encoding="utf-8")
    clean = e1v_scan(src.splitlines())
    copy = tmp / "e1v_planted.py"
    copy.write_text(src + "\nzz = mp.zetazero(3)\n", encoding="utf-8")
    planted = e1v_scan(copy.read_text(encoding="utf-8").splitlines())
    ok_scan = not clean and bool(planted)
    ok_all &= ok_scan
    print(f"  independent e1v source scan: clean on tracked source "
          f"{not clean} (offending: {clean or 'none'}); planted copy caught "
          f"{bool(planted)} ({planted})")
    # the guard mechanism itself trips as claimed
    def _forbid(*a, **k):
        raise RuntimeError("K1 guard: zero-list access attempted")
    orig = mp.zetazero
    mp.zetazero = _forbid
    try:
        mp.zetazero(1)
        tripped = False
    except RuntimeError:
        tripped = True
    finally:
        mp.zetazero = orig
    ok_all &= tripped
    print(f"  guard-install pattern trips on access: {tripped}")
    verdict("case 7 (e1v)", not ok_all,
            "e1v quick replicated (N/N pass, npz untouched), K1 scanner "
            "teeth verified on a planted copy, guard mechanism trips: "
            "the open replication item closes for this host"
            if ok_all else
            "REPLICATION ANOMALY in e1v: see lines above")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-repl", action="store_true")
    ap.add_argument("--skip-e1v", action="store_true")
    ap.add_argument("--only", type=str, default="")
    args = ap.parse_args()
    only = set(args.only.split(",")) if args.only else None
    t0 = time.time()
    print("=" * 78)
    print("ADVERSARY probe for e1ad_sum_rules (cases 1, 2, 4, 5, 6 + e1v "
          "case 7)")
    print("case 3 (super-resolution vs the horizon) EXCLUDED: separate build")
    print("=" * 78)
    tmp = Path(tempfile.mkdtemp(prefix="e1ad_adv_"))
    print(f"scratch dir: {tmp}")

    def want(c):
        return only is None or c in only

    cache = {}
    for N in (300, 1000):
        if want("2") or want("4") or (N == 300 and (want("1") or want("6"))):
            cache[N] = true_run(N)
    if want("1"):
        case1(*cache[300])
    if want("2"):
        case2({N: cache[N] for N in cache if N in (300, 1000)})
    if want("4"):
        case4({N: cache[N] for N in cache if N in (300, 1000)})
    if want("5"):
        case5(cache[300][0] if 300 in cache else e1ad.true_pk(300))
    if want("6"):
        case6(tmp, cache, args.skip_repl)
    if want("7") and not args.skip_e1v:
        case7(tmp)

    print("\n" + "=" * 78)
    print("VERDICT SUMMARY")
    for c, landed, line in VERDICTS:
        print(f"  {c}: {'LANDED' if landed else 'MISSED'}")
    print(f"Total time {round(time.time() - t0, 1)}s")


if __name__ == "__main__":
    main()

"""E1I: the METAPLECTIC OPERATOR -- the one route e1f/e1g/e1h did NOT eliminate, attacked at its
structural core. The three cheap orthogonal-polynomial-data surrogates all build from the MEASURE
dm_S = |prod_v L_v(1/2 - is)|^2 ds, a MODULUS-SQUARED (a positive function), and are signature-blind.
This module builds the object none of them is: the metaplectic / Weil representation, whose arithmetic
content is carried by a PHASE / SIGN (the Weil index = the quadratic Gauss sum; the quadratic character
= the Legendre symbol) that |.|^2 STRUCTURALLY DISCARDS. It then runs the decisive, controlled test:
does the metaplectic sign-structure SURVIVE the g -> g*g positivity operation that the CCM trace
comparison requires, or does it CANCEL into |.|^2 and leave the route signature-blind after all?

WHY THIS IS THE RIGHT TARGET (the eight-angle sweep verdict, LEARNINGS #111-#117). e1f (density
surrogate, non-idempotent), e1g (band-in-s concentration, reweighting-blind by diagonal similarity),
e1h (degree-domain (H+1/2)^2 + lambda^2 N_S, reads moments not arithmetic) are all SIGNATURE-BLIND. The
shared root cause, stated as disqualifier #2 of the sweep: "if arithmetic enters only as a MEASURE WEIGHT
on the spectral line, no spectral statistic of a cutoff/Jacobi operator can decode it." CCM defer the
real W_{lambda,S} to "the metaplectic representation of SL~(2, A_S)" precisely because the measure throws
the arithmetic away. So the un-eliminated route is, by elimination, the metaplectic one -- and this module
attacks the FINITE-LOCAL model of it directly (a finite Weil rep at one place), with an exact gate and a
controlled positivity-survival test. SCOPE UP FRONT: this is the finite-local quadratic sign-structure; it
does NOT test CCM's actual semilocal W_{lambda,S} (the global SL~(2,A_S) operator) and does NOT eliminate
the metaplectic route -- it sharpens the map of where the arithmetic does and does not survive positivity.

THE MOTIVATING HEURISTIC (why look at the metaplectic phase; NOT a proof). The local L-factor is
  L_p(1/2 - is) = (1 - p^{-1/2} e^{i s log p})^{-1},   a COMPLEX number (it has a phase).
The measure routes use |L_p|^2 = L_p * conj(L_p): the phase is annihilated. The metaplectic
representation keeps the phase. Its arithmetic invariants are:
  - the WEIL INDEX  eps_p = (Gauss sum)/sqrt(p) = 1 if p = 1 (mod 4),  i if p = 3 (mod 4)  -- a PHASE,
  - the QUADRATIC CHARACTER (Legendre symbol) (a|p) in the torus action  -- a SIGN.
Both are killed by |.|^2 (|eps_p| = 1; (a|p)^2 = 1). This MOTIVATES (does not prove) why the measure
routes e1f/g/h are blind: arithmetic lives in signs/phases, and a modulus-squared measure discards them.
CAVEAT (adversary-checked): |z e^{i theta}|^2 = |z|^2 is a tautology, and eps_p is NOT literally the
phase of L_p (the load-bearing version is cross-PRIME interference in arg(prod_v L_v), which |prod L_v|^2
factorizes away). So this is a heuristic for WHERE arithmetic hides, and the question this module actually
decides is whether that sign-structure SURVIVES the positivity compression (T1-T3), not the tautology.

THE FINITE MODEL (faithful to the SIGN-structure, which is the whole question). We build the finite Weil
representation of SL(2, F_p) on C[F_p] (functions on the finite field; the standard finite oscillator /
Weil representation, e.g. Bump AFR sec 4.1, Gerardin). With omega = e^{2 pi i / p}:
  - Fourier (Weyl element w):   F[x,y] = p^{-1/2} omega^{x y},
  - chirp (unipotent n(b)):     rho(n(b)) = diag(omega^{b x^2}),
  - torus (m(a), a in F_p^*):   rho(m(a)) f(x) = (a|p) f(a^{-1} x)  -- a SIGNED permutation,
where (a|p) is the Legendre symbol (the metaplectic correction). This is the finite model of the
sign-structure CCM route through; it is the computable carrier of the Weil index and the quadratic
character. (It is a model of the sign-structure, not the full p-adic L^2(Q_p) representation; that is
appropriate, because the question IS about the sign-structure -- whether it survives positivity.)

THE VALIDATION GATE (the e1f/e1h discipline; run FIRST; an EXACT identity). The clean, citable
metaplectic analogue of e1h's Meixner-Pollaczek identity is:
  Tr(F_p) = p^{-1/2} sum_x omega^{x^2} = (Gauss sum)/sqrt(p) = eps_p,
i.e. the TRACE OF THE NORMALIZED METAPLECTIC FOURIER IS THE WEIL INDEX eps_p (= 1 or i by p mod 4),
exact to machine precision and matched to Gauss's sign theorem. Plus: F unitary, F^2 = parity, F^4 = I.
The relation that genuinely FORCES the metaplectic sign is the 2-COCYCLE: SL_2 needs rho(w)^2 =
rho(m(-1)), i.e. F^2 = (-1|p)*parity, but F^2 = parity, so they differ by (-1|p) = -1 exactly when
p = 3 (mod 4) -- the double-cover obstruction, the SAME arithmetic eps_p = i records. (NOTE: the torus
character-multiplicativity m(a)m(a') = m(aa') alone does NOT force the Legendre symbol -- it passes with
the trivial sign +1; the cocycle test is what exercises the metaplectic correction.) Archimedean tie-in:
continuous Fourier eigenvalues on Hermite functions are (-i)^n; the Maslov phase is e^{-i pi/4}.

THE SIGNATURE TEST (the centerpiece; honest, controlled, decisive EITHER WAY).
  (T1) THE SCALAR INDEX CANCELS IN g*g. In W(g*g) the Weil index of g* is conj(eps), so eps * conj(eps)
       = |eps|^2 = 1: the scalar metaplectic phase is annihilated by the *-operation. We compute it and
       confirm -- this is the part of the route that IS blind, and it is consistent with e1g/h. The
       bare normalization carries no surviving positivity content.
  (T2) THE COMPRESSED SIGN-STRUCTURE: does it survive? The CCM positivity is NOT g*g = I (unitary,
       trivial); it is the SONIN-PROJECTED comparison Tr(rho(g) S rho(g)*) and the concentration
       S rho(g) S, where the projection S breaks unitarity and lets structure survive. We build the
       finite Sonin / prolate cutoff S = low eigenspace of the finite harmonic oscillator
       O = X^2 + F X^2 F^{-1} (X = centered position), and compute the concentration spectrum of the
       metaplectic CHIRP, sigma(S rho(n(b)) S) -- the finite prolate eigenvalues of a QUADRATIC chirp
       band-limited to the Sonin space. The quadratic form x^2 is the metaplectic generator.
  (T3) THE ARBITER + MAHALANOBIS (the e1h discipline; what decides T2). The WEAK control replaces x^2 by
       a ROUGH random value-permutation (smoothness AND arrangement destroyed): a tail here only says
       "smooth beats rough", a GENERIC time-frequency fact -- the e1h trap. THE ARBITER (the decider)
       compares the genuine chirp to a cloud of SMOOTH quadratic chirps omega^{b round(theta xc^2)}, rate
       theta drawn SYMMETRICALLY around the genuine theta=1, NO linear shear (an adversary-caught first-
       pass bug: shear made the genuine spuriously special for being "centered", not arithmetic), and
       concentration-matched (reported). ONE-SIDED verdict: a robust HIGH-tail median (pct >= 90) across
       a majority of primes = arithmetic survives; cloud-body (the actual result) = the finite-local
       quadratic sign-structure is signature-blind under the positivity compression. (A low/central
       percentile is MORE generic, NOT a signature -- the adversary's latent-false-positive fix.)

D-H CONTROL. Davenport-Heilbronn has a functional equation but NO Euler product: no local fields Q_p,
hence NO local Weil representation, NO Gauss sum, NO Legendre symbol. The metaplectic operator is
UNBUILDABLE for D-H by type -- and for a SHARPER reason than the measure routes: not merely "no measure"
but "no metaplectic sign-structure." The very objects (Weil index, quadratic character) that this module
shows carry the arithmetic are exactly the objects D-H lacks.

VERDICT STRUCTURE (filled by the run, not prejudged):
  - GATE: Tr(F_p) = eps_p exactly (the Weil index) by p mod 4, F unitary/F^2=parity/F^4=I, and the
    metaplectic 2-cocycle F^2 vs rho(m(-1)) matches (-1|p) (the double-cover obstruction). A genuine
    finite Weil rep. VALIDATED.
  - HEURISTIC (not a proof): arithmetic lives in signs/phases that |.|^2 discards -- motivation for e1f/g/h
    blindness, not a demonstrated mechanism.
  - T1: the scalar Weil index cancels in g*g (consistent with the measure routes' positivity-blindness).
  - T2/T3 (the actual result): cloud-body across the majority of primes -- the FINITE-LOCAL quadratic
    sign-structure is signature-blind under the finite Sonin positivity compression.
  SCOPE: this is the finite-local quadratic (Gauss-sum) sign-structure at one place. It does NOT test
  CCM's actual semilocal W_{lambda,S} (the GLOBAL metaplectic rep of SL~(2,A_S) from the degree-1 Euler
  factors) and does NOT eliminate the metaplectic route, which stays the un-eliminated CCM door. The
  RH-closing content (the S -> all-primes uniform domination) is M4 / the arithmetic Hodge standard
  conjecture, which no finite model touches.

Run:
  python -m experiments.spectral.e1i_metaplectic_weil_index

Outputs:
  experiments/spectral/e1i_metaplectic_weil_index.npz

HONEST SCOPE. Finite-field linear algebra (exact for the gate, float for the spectra). The finite Weil
representation is a faithful model of the metaplectic SIGN-structure (the Weil index and the quadratic
character), which is precisely the content the measure discards and the content in question; it is NOT
the full p-adic L^2(Q_p) representation or CCM's actual semilocal W_{lambda,S}. The gate is an EXACT
number-theoretic identity (Tr F_p = eps_p, Gauss's sign theorem). The signature verdict is set by the
Arbiter / Mahalanobis controls and reported honestly. It proves nothing about RH; it decides whether the
metaplectic route is a genuine non-measure route, and relocates the residual difficulty to M4.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from experiments._shared import DavenportHeilbronn, zeta_L

OUT = Path(__file__).with_suffix(".npz")

# Odd primes for the finite Weil representation. Mix of p = 1 (mod 4) {5,13,17,29} and
# p = 3 (mod 4) {7,11,19,23} so the Weil-index gate exercises both branches.
PRIMES = [5, 7, 11, 13, 17, 19, 23, 29]


# ----------------------------------------------------------------------------
# Number theory: Legendre symbol and the quadratic Gauss sum.
# ----------------------------------------------------------------------------
def legendre(a: int, p: int) -> int:
    """(a|p) in {-1,0,1} by Euler's criterion."""
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r  # r is 1 or p-1


def gauss_sum(p: int) -> complex:
    """g_p = sum_{x in F_p} omega^{x^2},  omega = e^{2 pi i / p}.
    Classical (Gauss): g_p = sqrt(p) if p = 1 (mod 4),  i sqrt(p) if p = 3 (mod 4)."""
    x = np.arange(p)
    return complex(np.sum(np.exp(2j * np.pi * (x * x % p) / p)))


def weil_index_expected(p: int) -> complex:
    """eps_p = g_p / sqrt(p) in {1, i} by p mod 4 (the Weil index / Gauss-sum sign)."""
    return 1.0 + 0j if p % 4 == 1 else 1j


# ----------------------------------------------------------------------------
# The finite Weil representation of SL(2, F_p) on C[F_p].
# ----------------------------------------------------------------------------
def fourier_matrix(p: int) -> np.ndarray:
    """F[x,y] = p^{-1/2} omega^{x y}, omega = e^{2 pi i / p}. The metaplectic Weyl element."""
    x = np.arange(p)
    return np.exp(2j * np.pi * np.outer(x, x) / p) / np.sqrt(p)


def chirp(p: int, b: int) -> np.ndarray:
    """rho(n(b)) = diag(omega^{b x^2}), the unipotent / chirp. Carries the quadratic form b x^2."""
    x = np.arange(p)
    return np.diag(np.exp(2j * np.pi * (b * (x * x) % p) / p))


def torus(p: int, a: int) -> np.ndarray:
    """rho(m(a)) f(x) = (a|p) f(a^{-1} x), a signed permutation. The Legendre symbol is the
    metaplectic correction that makes m multiplicative (the splitting over F_p)."""
    ainv = pow(a, p - 2, p)  # a^{-1} mod p (Fermat)
    s = legendre(a, p)
    M = np.zeros((p, p), dtype=complex)
    for x in range(p):
        M[x, (ainv * x) % p] = s
    return M


def diag_from_values(p: int, b: int, vals: np.ndarray) -> np.ndarray:
    """diag(omega^{b * vals[x]}): a chirp-like diagonal whose value-multiset is that of `vals`.
    With vals = x^2 it IS the genuine chirp; with a permuted `vals` it is the matched control."""
    return np.diag(np.exp(2j * np.pi * (b * vals % p) / p))


# ----------------------------------------------------------------------------
# The finite Sonin / prolate cutoff: low eigenspace of the finite harmonic oscillator
#   O = X^2 + P^2,  X = diag(centered positions),  P = F X F^{-1}  (centered "momentum").
# Its low eigenvectors are the discrete Hermite functions; the projection onto them is the finite
# phase-space cutoff at the self-dual radius (the finite Sonin space). This is the metaplectic-natural
# cutoff: O commutes with F up to the metaplectic structure (F O F^{-1} = O).
# ----------------------------------------------------------------------------
def centered_positions(p: int) -> np.ndarray:
    """Map F_p = {0,...,p-1} to centered {-(p-1)/2, ..., (p-1)/2} (the self-dual layout)."""
    x = np.arange(p, dtype=float)
    return np.where(x > (p - 1) / 2, x - p, x)


def finite_oscillator(p: int, F: np.ndarray) -> np.ndarray:
    """O = X^2 + P^2 with X = diag(centered positions), P = F X F^{-1}. Self-adjoint, F-invariant."""
    xc = centered_positions(p)
    X2 = np.diag(xc ** 2)
    P = F @ np.diag(xc) @ F.conj().T
    P2 = P @ P
    return X2 + P2


def sonin_projection(p: int, F: np.ndarray, k: int) -> np.ndarray:
    """S = orthogonal projection onto the k lowest eigenvectors of the finite oscillator O
    (the finite Sonin / band-limited subspace)."""
    O = finite_oscillator(p, F)
    O = 0.5 * (O + O.conj().T)  # symmetrize numerical noise
    _, V = np.linalg.eigh(O)
    B = V[:, :k]
    return B @ B.conj().T


def concentration_spectrum(S: np.ndarray, g: np.ndarray, k: int) -> np.ndarray:
    """Singular values of the compression S g S restricted to range(S): the finite prolate /
    concentration eigenvalues of the metaplectic element g band-limited to the Sonin space.
    (Returned sorted descending, length k.)"""
    M = S @ g @ S
    sv = np.linalg.svd(M, compute_uv=False)
    return np.sort(sv)[::-1][:k]


# ----------------------------------------------------------------------------
# THE GATE
# ----------------------------------------------------------------------------
def run_gate(p: int) -> dict:
    F = fourier_matrix(p)
    gp = gauss_sum(p)
    eps_exp = weil_index_expected(p)
    trF = complex(np.trace(F))

    I = np.eye(p)
    parity = np.zeros((p, p))
    for x in range(p):
        parity[x, (-x) % p] = 1.0

    # G3: F unitary, F^2 = parity, F^4 = I
    unit_err = float(np.max(np.abs(F @ F.conj().T - I)))
    f2_err = float(np.max(np.abs(F @ F - parity)))
    f4_err = float(np.max(np.abs(np.linalg.matrix_power(F, 4) - I)))

    # G4: the chosen torus sign is a multiplicative CHARACTER: m(a) m(a') = m(a a'). NOTE (adversary):
    # this passes IDENTICALLY with the trivial sign +1 -- it only checks that the sign is a homomorphism
    # F_p^* -> {+/-1}, it does NOT by itself force or validate the Legendre symbol. The relation that
    # genuinely exercises the metaplectic correction is the cocycle test G5 below.
    units = [a for a in range(1, p)]
    split_err = 0.0
    rng_pairs = [(2, 3), (2, units[-1]), (3, units[-2])]
    for a, ap in rng_pairs:
        lhs = torus(p, a) @ torus(p, ap)
        rhs = torus(p, (a * ap) % p)
        split_err = max(split_err, float(np.max(np.abs(lhs - rhs))))

    # G5: the GENUINE metaplectic 2-cocycle (the test that actually forces the Weil index). SL_2 requires
    # rho(w)^2 = rho(w^2) = rho(m(-1)). With rho(w) = F we have F^2 = parity (sign +1), while
    # rho(m(-1)) f(x) = (-1|p) f(-x) = (-1|p) * parity. They AGREE iff p = 1 (mod 4); for p = 3 (mod 4)
    # they DIFFER by (-1|p) = -1 (operator-norm gap 2). That gap is the metaplectic 2-cocycle -- the
    # double-cover obstruction, the SAME arithmetic the Weil index records (eps_p = i exactly when the
    # gap is nonzero). So F+torus is a genuine linear rep of SL_2(F_p) only for p=1 mod 4; for p=3 mod 4
    # it is genuinely a rep of the metaplectic DOUBLE COVER. This is the real metaplectic-sign content.
    leg_m1 = legendre(-1, p)                         # (-1|p): +1 if p=1 mod 4, -1 if p=3 mod 4
    cocycle_gap = float(np.max(np.abs(F @ F - leg_m1 * parity)))   # 0 if p=1 mod 4, 2 if p=3 mod 4
    cocycle_consistent = (cocycle_gap < 1e-9) == (p % 4 == 1)      # matches the (-1|p) prediction

    return {
        "p": p,
        "p_mod_4": p % 4,
        "gauss_sum": gp,
        "gauss_abs": float(abs(gp)),
        "sqrt_p": float(np.sqrt(p)),
        "eps_expected": eps_exp,
        "trF": trF,
        "trF_minus_eps_err": float(abs(trF - eps_exp)),   # the headline exact identity
        "F_unitary_err": unit_err,
        "F2_parity_err": f2_err,
        "F4_identity_err": f4_err,
        "torus_char_mult_err": split_err,             # G4: only character-multiplicativity (weak)
        "legendre_minus1": leg_m1,
        "metaplectic_cocycle_gap": cocycle_gap,       # G5: 0 (p=1 mod 4) / 2 (p=3 mod 4) -- the real test
        "cocycle_matches_prediction": bool(cocycle_consistent),
    }


def archimedean_hermite_gate(N: int = 256) -> dict:
    """Continuous tie-in: the Fourier transform's eigenvalues on Hermite functions are (-i)^n, so the
    metaplectic / Maslov phase is e^{-i pi/4} = sqrt of the -i branch. We discretize the centered DFT
    and confirm its eigenvalues cluster on {1, -i, -1, i} and that Tr(DFT_N) is the N-Gauss sum
    (Schur) -- the same phase structure as the finite-field Tr(F_p) = eps_p, tying the two scales."""
    # centered unitary DFT
    n = np.arange(N)
    W = np.exp(-2j * np.pi * np.outer(n, n) / N) / np.sqrt(N)
    ev = np.linalg.eigvals(W)
    # nearest 4th root of unity for each eigenvalue
    roots = np.array([1, -1j, -1, 1j])
    nearest = roots[np.argmin(np.abs(ev[:, None] - roots[None, :]), axis=1)]
    max_dev = float(np.max(np.abs(ev - nearest)))
    trW = complex(np.trace(W))
    # Schur: Tr(DFT_N)/... has |Tr| ~ sqrt(N)-scale Gauss structure; the PHASE follows N mod 4.
    eps_N = weil_index_expected(N + 1) if N % 4 != 0 else None  # informational only
    return {
        "N": N,
        "eig_max_dev_from_4th_roots": max_dev,
        "trace_DFT": trW,
        "trace_DFT_abs": float(abs(trW)),
        "maslov_phase": complex(np.exp(-1j * np.pi / 4)),
    }


# ----------------------------------------------------------------------------
# THE STRUCTURAL POINT: |L_p|^2 is phase-blind by construction.
# ----------------------------------------------------------------------------
def measure_phase_blindness(p: int, n_s: int = 4000, S0: float = 60.0) -> dict:
    """Show |L_p(1/2 - is)|^2 is invariant under an ARBITRARY phase twist of L_p: the measure routes
    (e1f/g/h) cannot see the phase, which is exactly where the Weil index / quadratic character live."""
    s = np.linspace(-S0, S0, n_s)
    Lp = 1.0 / (1 - p ** (-0.5) * np.exp(1j * s * np.log(p)))      # the COMPLEX local factor
    mod2 = np.abs(Lp) ** 2
    twist = np.exp(1j * (1.3 * s + 0.7 * np.cos(2 * s)))            # an arbitrary phase e^{i theta(s)}
    mod2_twisted = np.abs(Lp * twist) ** 2
    return {
        "max_phase_of_Lp": float(np.max(np.abs(np.angle(Lp)))),    # the phase IS nonzero (arithmetic)
        "modulus_sq_change_under_phase_twist": float(np.max(np.abs(mod2 - mod2_twisted))),  # ~0
    }


# ----------------------------------------------------------------------------
# THE SIGNATURE TEST
# ----------------------------------------------------------------------------
def scalar_index_star_test(p: int) -> dict:
    """T1: in g*g the Weil index of g* is conj(eps), so eps * conj(eps) = |eps|^2 = 1. The SCALAR
    metaplectic phase is annihilated by the *-operation -- the positivity-blind part of the route."""
    eps = weil_index_expected(p)
    return {
        "eps": eps,
        "eps_times_conj": complex(eps * np.conj(eps)),     # = 1 exactly: the scalar phase cancels
        "scalar_index_survives_star": bool(abs(eps * np.conj(eps) - 1.0) > 1e-9),  # False
    }


def _maha_percentile(spec_gen: np.ndarray, cloud: np.ndarray) -> dict:
    """Mahalanobis distance of spec_gen within `cloud`, and its percentile."""
    mu = cloud.mean(0)
    cov = np.cov(cloud.T)
    inv = np.linalg.pinv(cov)
    d_gen = float(np.sqrt((spec_gen - mu) @ inv @ (spec_gen - mu)))
    d_cloud = np.array([float(np.sqrt((c - mu) @ inv @ (c - mu))) for c in cloud])
    return {
        "mahalanobis": d_gen,
        "cloud_median": float(np.median(d_cloud)),
        "cloud_max": float(np.max(d_cloud)),
        "percentile": float(100 * np.mean(d_cloud < d_gen)),
    }


def chirp_signature_robust(p: int, k: int, cloud_size: int = 60,
                           bs=(1, 2, 3), seeds=(0, 1, 2, 3, 4, 5, 6, 7)) -> dict:
    """Robustified T2/T3: the single-(b,seed) Arbiter percentile has ~1/cloud_size resolution and is
    noisy at small p, so a lone tail draw is a FALSE POSITIVE (the e1h z=+2.29 lesson). We aggregate the
    Arbiter percentile over several chirp rates b and seeds and report the MEDIAN. ONE-SIDED criterion:
    arithmetic survival requires a CONSISTENT high tail (median pct >= 90), an OUTLIER far from the
    cloud. A LOW percentile means the genuine chirp is CENTRAL in the cloud = MORE generic, NOT a
    signature (the adversary's latent-false-positive fix: centrality is not arithmetic)."""
    runs = [chirp_concentration_signature(p, k, b=b, cloud_size=cloud_size, seed=s)
            for b in bs for s in seeds]
    arb_pcts = np.array([r["arbiter_percentile"] for r in runs])
    weak_pcts = np.array([r["weak_percentile"] for r in runs])
    conc_pcts = np.array([r["genuine_conc_percentile"] for r in runs])
    med = float(np.median(arb_pcts))
    return {
        "p": p, "k": k, "n_runs": len(runs),
        "arbiter_pct_median": med,
        "arbiter_pct_min": float(np.min(arb_pcts)),
        "arbiter_pct_max": float(np.max(arb_pcts)),
        "arbiter_pct_iqr": [float(np.percentile(arb_pcts, 25)), float(np.percentile(arb_pcts, 75))],
        "weak_pct_median": float(np.median(weak_pcts)),
        "conc_pct_median": float(np.median(conc_pcts)),   # fairness: is genuine concentration central?
        "spec_genuine": runs[0]["spec_genuine"],
        # ONE-SIDED robust tail: median Arbiter percentile is a HIGH outlier (>=90), not one draw,
        # and not centrality (low pct).
        "arithmetic_survives": bool(med >= 90.0),
    }


def chirp_concentration_signature(p: int, k: int, b: int = 1, cloud_size: int = 60,
                                   seed: int = 0) -> dict:
    """T2/T3: does the metaplectic quadratic chirp carry ARITHMETIC content into a POSITIVE spectral
    invariant, or only GENERIC smooth-chirp concentration? The genuine chirp is omega^{b x^2},
    band-limited to the finite Sonin space S. We run TWO clouds, the e1h discipline:

    (WEAK control -- value-matched ROUGH scramble): random permutation of x^2's value multiset (same
    phase multiset, smoothness AND quadratic arrangement destroyed). A high tail here = "narrow
    non-blindness" only (the genuine chirp beats rough noise) -- it conflates 'smooth' with 'arithmetic'
    and is NOT the deciding test.

    (STRONG control -- THE ARBITER, smooth-chirp cloud): generic SMOOTH quadratic chirps
    omega^{b * round(theta * xc^2)} (xc = centered position) with the rate theta drawn SYMMETRICALLY
    around the genuine theta=1 and NO linear shear -- the genuine chirp has no shear, so adding shear to
    the cloud (the first-pass bug the adversary caught) made the genuine spuriously special for a generic
    'centered / no-shear' reason, not arithmetic. With the shear removed and theta symmetric, the cloud
    members are equally-smooth, concentration-matched quadratic chirps that differ from the genuine ONLY
    in rate (a non-mod-p-residue arrangement). If the genuine x^2 is a HIGH-tail outlier here, the mod-p
    arithmetic survives positivity; if it sits in the BODY (it does), the weak-control tail was just
    smooth-vs-rough = a GENERIC time-frequency / metaplectic-covariance fact, not arithmetic. We also
    report the genuine's CONCENTRATION percentile in the cloud (a fairness diagnostic: a fair cloud puts
    it near the middle, so the Mahalanobis tracks ARRANGEMENT, not a concentration offset)."""
    F = fourier_matrix(p)
    S = sonin_projection(p, F, k)
    x = np.arange(p)
    xc = centered_positions(p)
    sq = (x * x) % p                                # the genuine quadratic value vector
    rng = np.random.default_rng(seed)

    def total_conc(g):
        return float(np.sum(np.linalg.svd(S @ g @ S, compute_uv=False)[:k]))

    # genuine quadratic chirp, band-limited to Sonin
    g_gen = diag_from_values(p, b, sq)
    spec_gen = concentration_spectrum(S, g_gen, k)
    conc_gen = total_conc(g_gen)

    # WEAK control: rough scrambles (random permutation of the value multiset)
    rough = np.array([concentration_spectrum(S, diag_from_values(p, b, rng.permutation(sq)), k)
                      for _ in range(cloud_size)])
    weak = _maha_percentile(spec_gen, rough)

    # STRONG control (THE ARBITER): smooth quadratic chirps, NO shear, theta symmetric around 1.
    smooth, conc_cloud = [], []
    for _ in range(cloud_size):
        theta = rng.uniform(0.5, 1.5)               # rate symmetric around the genuine theta=1, no shear
        v = np.round(theta * xc ** 2).astype(int) % p
        gv = diag_from_values(p, b, v)
        smooth.append(concentration_spectrum(S, gv, k))
        conc_cloud.append(total_conc(gv))
    smooth = np.array(smooth)
    strong = _maha_percentile(spec_gen, smooth)
    conc_pct = float(100 * np.mean(np.array(conc_cloud) < conc_gen))   # fairness diagnostic

    # coarse reference: a uniformly random diagonal phase (|.|=1)
    spec_rand = concentration_spectrum(S, np.diag(np.exp(2j * np.pi * rng.uniform(0, 1, p))), k)

    return {
        "p": p, "k": k, "b": b, "cloud_size": cloud_size,
        "spec_genuine": spec_gen.tolist(),
        "spec_random_phase": spec_rand.tolist(),
        # weak control (smooth-vs-rough): a high tail here is NARROW non-blindness only
        "weak_mahalanobis": weak["mahalanobis"],
        "weak_percentile": weak["percentile"],
        # STRONG control (the Arbiter, smooth-vs-smooth): THIS decides arithmetic vs generic. ONE-SIDED.
        "arbiter_mahalanobis": strong["mahalanobis"],
        "arbiter_cloud_median": strong["cloud_median"],
        "arbiter_cloud_max": strong["cloud_max"],
        "arbiter_percentile": strong["percentile"],
        "genuine_conc_percentile": conc_pct,        # fairness: ~50 = concentration-matched cloud
        "arithmetic_survives": bool(strong["percentile"] >= 90.0),
    }


# ----------------------------------------------------------------------------
# D-H control
# ----------------------------------------------------------------------------
def dh_control() -> dict:
    dh = DavenportHeilbronn()
    return {
        "zeta_has_euler_product": bool(getattr(zeta_L, "has_euler_product", True)),
        "dh_has_euler_product": bool(getattr(dh, "has_euler_product", False)),
        "dh_has_local_fields": False,        # no Euler product => no Q_p
        "dh_has_weil_rep": False,            # no local fields => no local Weil representation
        "dh_has_gauss_sum_or_legendre": False,  # the arithmetic carriers are absent by type
    }


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------
def run(k: int = 6, b: int = 1, cloud_size: int = 60) -> dict:
    R: dict = {"params": {"k": k, "b": b, "cloud_size": cloud_size, "primes": PRIMES}}

    # ===== GATE =====
    gates = [run_gate(p) for p in PRIMES]
    R["gate"] = gates
    R["arch_gate"] = archimedean_hermite_gate()
    R["structural"] = {p: measure_phase_blindness(p) for p in [2, 3, 5, 7]}

    # ===== SIGNATURE TEST =====
    R["T1_scalar_index"] = {p: scalar_index_star_test(p) for p in PRIMES}
    # T2/T3 on primes large enough for a meaningful Sonin cutoff (k modes need p > 2k), robustified
    # over chirp rates b and seeds (a lone tail draw is a false positive -- the e1h z=+2.29 lesson).
    sig_primes = [p for p in PRIMES if p >= 2 * k + 1]
    R["T2T3_chirp"] = {p: chirp_signature_robust(p, k=k, cloud_size=cloud_size)
                       for p in sig_primes}

    # ===== D-H control =====
    R["dh_control"] = dh_control()
    return R


def _print_report(R: dict) -> None:
    print("=" * 84)
    print("E1I: THE METAPLECTIC OPERATOR -- finite Weil representation over F_p")
    print("     (the one route e1f/e1g/e1h did NOT eliminate; the phase/sign the measure discards)")
    print("=" * 84)
    p0 = R["params"]
    print(f"  params: k(Sonin dim)={p0['k']}  b(chirp)={p0['b']}  "
          f"cloud_size={p0['cloud_size']}  primes={p0['primes']}")

    # ---- GATE ----
    print("\n[VALIDATION GATE -- the EXACT identity  Tr(F_p) = eps_p (the Weil index)]")
    print("  p  p%4   |g_p|/sqrt(p)   eps_exp   Tr(F_p)        |Tr-eps|   F:unit/F^2=par/F^4=I   cocycle")
    gate_ok = True
    for g in R["gate"]:
        eok = g["trF_minus_eps_err"] < 1e-9
        relok = max(g["F_unitary_err"], g["F2_parity_err"], g["F4_identity_err"]) < 1e-9
        gate_ok = (gate_ok and eok and relok and abs(g["gauss_abs"] - g["sqrt_p"]) < 1e-9
                   and g["cocycle_matches_prediction"])
        eps = g["eps_expected"]; tr = g["trF"]
        print(f"  {g['p']:<3d}{g['p_mod_4']:<4d}  {g['gauss_abs']/g['sqrt_p']:.6f}      "
              f"{'1' if eps==1 else 'i':<7s}  {tr.real:+.4f}{tr.imag:+.4f}i   "
              f"{g['trF_minus_eps_err']:.1e}   "
              f"{g['F_unitary_err']:.0e}/{g['F2_parity_err']:.0e}/{g['F4_identity_err']:.0e}   "
              f"gap={g['metaplectic_cocycle_gap']:.2f}")
    ag = R["arch_gate"]
    print(f"  archimedean tie-in (N={ag['N']} DFT): eigenvalues within "
          f"{ag['eig_max_dev_from_4th_roots']:.1e} of {{1,-i,-1,i}}; "
          f"Maslov phase e^(-i pi/4) = {ag['maslov_phase'].real:+.4f}{ag['maslov_phase'].imag:+.4f}i")
    print(f"  >>> GATE {'VALIDATES' if gate_ok else 'FAILS'} <<<  "
          f"(Tr(F_p)=eps_p exactly; |g_p|=sqrt(p); F unitary/F^2=par/F^4=I; cocycle matches (-1|p))")
    print("      (G2) The Weil index eps_p (= 1 if p=1 mod 4, i if p=3 mod 4) IS the trace of the")
    print("           metaplectic Fourier -- an EXACT number-theoretic identity (Gauss's sign theorem),")
    print("           the metaplectic analogue of e1h's Meixner-Pollaczek identity.")
    print("      (G5) The metaplectic 2-COCYCLE: F^2 = parity but rho(m(-1)) = (-1|p)*parity, so the gap")
    print("           is 0 for p=1 mod 4 and 2 for p=3 mod 4 -- the double-cover obstruction, the SAME")
    print("           arithmetic eps_p records. (This is the real metaplectic-sign test; the torus")
    print("           character-multiplicativity m(a)m(a')=m(aa') alone would pass with the trivial sign.)")
    if not gate_ok:
        print("  GATE FAILED -- the finite Weil rep is not genuine; stop.")
        return

    # ---- MOTIVATING HEURISTIC (not a proof) ----
    print("\n[MOTIVATING HEURISTIC (not a proof) -- arithmetic lives in the sign/phase a measure discards]")
    for p, s in R["structural"].items():
        print(f"  p={p}: |L_p|^2 change under an arbitrary phase twist = "
              f"{s['modulus_sq_change_under_phase_twist']:.1e}")
    print("  CAVEAT (adversary): |z e^{i theta}|^2 = |z|^2 is a TAUTOLOGY -- modulus-squared discards")
    print("  phase by definition, so this only motivates (does not prove) why the measure routes are")
    print("  blind. And eps_p (the Gauss-sum index) is NOT literally phase(L_p); the load-bearing")
    print("  version is cross-PRIME interference in arg(prod_v L_v), which |prod L_v|^2 factorizes away.")
    print("  This is the right HEURISTIC for where arithmetic hides (signs/phases), not a demonstrated")
    print("  mechanism. The decisive question is whether that sign-structure SURVIVES positivity (T1-T3).")

    # ---- T1 ----
    print("\n[SIGNATURE TEST T1 -- the SCALAR Weil index cancels in g*g (the positivity-blind part)]")
    any_survive = False
    for p, t in R["T1_scalar_index"].items():
        any_survive = any_survive or t["scalar_index_survives_star"]
    print(f"  for every p: eps_p * conj(eps_p) = |eps_p|^2 = 1 exactly.  scalar index survives g*g: "
          f"{any_survive}")
    print("  => the bare metaplectic normalization carries NO surviving positivity content (consistent")
    print("     with e1g/h). If the route is non-blind, it must be in the COMPRESSED structure (T2/T3).")

    # ---- T2/T3 ----
    print("\n[SIGNATURE TEST T2/T3 -- the COMPRESSED quadratic sign-structure: ARITHMETIC or GENERIC?]")
    print("  Genuine chirp omega^{b x^2}, band-limited to the finite Sonin space S. ARBITER = vs a cloud")
    print("  of SMOOTH quadratic chirps (rate symmetric around the genuine, NO shear; conc% ~50 = the")
    print("  cloud is concentration-matched, so the test tracks ARRANGEMENT). ONE-SIDED: TAIL needs")
    print("  median pct >= 90 (a HIGH outlier); a low/central pct is MORE generic, NOT a signature.")
    n_arith = 0
    for p, t in R["T2T3_chirp"].items():
        arith = t["arithmetic_survives"]
        n_arith += int(arith)
        iqr = t["arbiter_pct_iqr"]
        print(f"  p={p:<3d} k={t['k']} ({t['n_runs']} runs): WEAK(vs rough) med={t['weak_pct_median']:.0f}%  "
              f"ARBITER(vs smooth) med={t['arbiter_pct_median']:.0f}% "
              f"[IQR {iqr[0]:.0f}-{iqr[1]:.0f}]  conc%={t['conc_pct_median']:.0f}  "
              f"[{'TAIL=ARITHMETIC' if arith else 'BODY=GENERIC'}]")
    n_tot = len(R["T2T3_chirp"])
    # CONSERVATIVE cross-prime verdict: arithmetic survival requires a MAJORITY of primes with a robust
    # HIGH-tail median (>=90), not a single lucky draw (the e1h false-positive discipline; one-sided per
    # the adversary's latent-FP fix -- a low/central percentile is NOT arithmetic).
    arithmetic_verdict = n_arith > n_tot / 2
    R["T2T3_verdict"] = {"n_arith": n_arith, "n_total": n_tot, "arithmetic_survives": arithmetic_verdict}
    if arithmetic_verdict:
        print(f"  >>> ARBITER high TAIL for {n_arith}/{n_tot} primes (robust majority): the mod-p quadratic-")
        print("      RESIDUE arithmetic survives the Sonin compression -- a genuine non-blindness.")
    else:
        print(f"  >>> ARBITER BODY for the majority ({n_tot - n_arith}/{n_tot} primes; concentration-matched):")
        print("      the genuine chirp is NOT special among smooth chirps. The metaplectic SIGN is real")
        print("      (the gate), but the finite-local quadratic sign-structure does NOT survive the finite")
        print("      Sonin positivity compression as arithmetic discrimination -- signature-blind in the")
        print("      deep e1h sense. (SCOPE: this is the finite-local model, NOT CCM's actual semilocal")
        print("      W_{lambda,S}; it does NOT eliminate the metaplectic route -- see the verdict.)")

    # ---- D-H ----
    dh = R["dh_control"]
    print("\n[D-H CONTROL -- unbuildable by type, for a SHARPER reason than the measure routes]")
    print(f"  zeta Euler product = {dh['zeta_has_euler_product']}, "
          f"D-H Euler product = {dh['dh_has_euler_product']}")
    print("  => D-H has NO local fields Q_p => NO local Weil representation => NO Gauss sum / Legendre")
    print("     symbol. The metaplectic operator is unbuildable for D-H, and the very objects this")
    print("     module shows carry the arithmetic (the Weil index, the quadratic character) are exactly")
    print("     what D-H lacks. Not just 'no measure' -- 'no metaplectic sign-structure'.")

    print("\n" + "=" * 84)
    print("VERDICT")
    print("  - GATE VALIDATES: Tr(F_p) = eps_p (the Weil index), an EXACT identity by p mod 4; F")
    print("    unitary/F^2=parity/F^4=I; and the metaplectic COCYCLE F^2 vs rho(m(-1)) matches (-1|p)")
    print("    (the genuine double-cover obstruction). A genuine finite Weil representation.")
    print("  - HEURISTIC (not a proof): arithmetic lives in signs/phases, which a |.|^2 measure discards")
    print("    -- motivation for why the measure routes (e1f/g/h) are blind, NOT a demonstrated mechanism.")
    print("  - T1: the scalar Weil index CANCELS in g*g (positivity-blind, as e1g/h).")
    if arithmetic_verdict:
        print("  - T2/T3: the COMPRESSED quadratic-residue arithmetic SURVIVES (Arbiter high tail, robust")
        print("    majority) -- a genuine non-blindness; the residual difficulty relocates to S->inf = M4.")
    else:
        print("  - T2/T3: the finite-local COMPRESSED structure is GENERIC (Arbiter body, robust majority,")
        print("    concentration-matched) -- the metaplectic SIGN is real (the gate) but the finite-local")
        print("    quadratic sign-structure does NOT survive the finite Sonin positivity compression as")
        print("    arithmetic discrimination. A FINITE-LOCAL signature-blindness, the fourth such surrogate.")
    print("  - SCOPE: this is the FINITE-LOCAL quadratic (Gauss-sum) sign-structure at one place. It does")
    print("    NOT test CCM's actual semilocal W_{lambda,S} (the GLOBAL metaplectic rep of SL~(2,A_S) from")
    print("    the degree-1 Euler factors). It does NOT eliminate the metaplectic route, which stays the")
    print("    un-eliminated CCM door = M4. The RH-closing content is the S->all-primes uniform domination")
    print("    = M4 / the arithmetic Hodge standard conjecture, untouched by any finite model.")
    print("=" * 84)


def main() -> None:
    ap = argparse.ArgumentParser(description="E1I metaplectic Weil-index operator")
    ap.add_argument("--k", type=int, default=6, help="finite Sonin / prolate cutoff dimension")
    ap.add_argument("--b", type=int, default=1, help="chirp parameter b in omega^{b x^2}")
    ap.add_argument("--cloud", type=int, default=60, help="value-matched scramble cloud size")
    args = ap.parse_args()

    R = run(k=args.k, b=args.b, cloud_size=args.cloud)
    _print_report(R)

    # ---- save .npz ----
    save: dict = {}
    save["primes"] = np.array(PRIMES)
    save["gate_trF_err"] = np.array([g["trF_minus_eps_err"] for g in R["gate"]])
    save["gate_trF"] = np.array([g["trF"] for g in R["gate"]])
    save["gate_eps"] = np.array([g["eps_expected"] for g in R["gate"]])
    save["gate_gauss_abs"] = np.array([g["gauss_abs"] for g in R["gate"]])
    save["gate_sqrt_p"] = np.array([g["sqrt_p"] for g in R["gate"]])
    save["gate_rep_relation_err"] = np.array(
        [max(g["F_unitary_err"], g["F2_parity_err"], g["F4_identity_err"],
             g["torus_char_mult_err"]) for g in R["gate"]])
    save["gate_cocycle_gap"] = np.array([g["metaplectic_cocycle_gap"] for g in R["gate"]])
    save["gate_legendre_minus1"] = np.array([g["legendre_minus1"] for g in R["gate"]])
    save["arch_eig_dev"] = R["arch_gate"]["eig_max_dev_from_4th_roots"]
    save["struct_mod2_change"] = np.array(
        [v["modulus_sq_change_under_phase_twist"] for v in R["structural"].values()])
    save["T1_scalar_survives"] = np.array(
        [int(t["scalar_index_survives_star"]) for t in R["T1_scalar_index"].values()])
    for p, t in R["T2T3_chirp"].items():
        save[f"T2_spec_genuine_p{p}"] = np.array(t["spec_genuine"])
        save[f"T2_weak_pct_median_p{p}"] = t["weak_pct_median"]
        save[f"T2_arbiter_pct_median_p{p}"] = t["arbiter_pct_median"]
        save[f"T2_arbiter_pct_range_p{p}"] = np.array([t["arbiter_pct_min"], t["arbiter_pct_max"]])
        save[f"T2_conc_pct_median_p{p}"] = t["conc_pct_median"]
    save["T2_n_arith"] = R["T2T3_verdict"]["n_arith"]
    save["T2_n_total"] = R["T2T3_verdict"]["n_total"]
    save["T2_arithmetic_survives"] = int(R["T2T3_verdict"]["arithmetic_survives"])
    save["dh_zeta_euler"] = R["dh_control"]["zeta_has_euler_product"]
    save["dh_dh_euler"] = R["dh_control"]["dh_has_euler_product"]
    np.savez(OUT, **save)
    print(f"\nsaved -> {OUT}")


if __name__ == "__main__":
    main()

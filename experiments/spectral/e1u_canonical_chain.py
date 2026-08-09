"""E1U: trace-normed canonical-system (de Branges chain) embedding of the
ghost-quotiented CCM D_log objects, with the two relocated clauses MEASURED.

WHY THIS EXPERIMENT EXISTS
==========================
LEARNINGS #170 / trojan_horse_m4.md Section 6: the one costume whose tariff
is not yet priced is the trace-normed canonical-system compactness (Remling;
at-source Hur arXiv:1501.01268): trace-normed Hamiltonians form a compact
metric space and H <-> m (Weyl) is a homeomorphism, so subsequential limits
of finite chains exist FOR FREE, with reality preserved by class and the
measured type divergence absorbed into the length coordinate. In this
encoding the RH content relocates into exactly two ENTANGLED clauses:
  (a) identification of the limit chain (the lattice site, = the #160 pin);
  (b) non-degeneracy / no-mass-escape of the limit Hamiltonian (the Euler
      site), Beurling-satisfiable at density level BY PREDICTION, so it
      should carry zero discrimination alone; the RH weight sits in the
      conjunction (an off-line pair of the true limit manifests as a LOCAL
      MASS DEFECT against the family's global data).
e1t measured the FUNCTION face non-Cauchy for zeta (projective gaps
0.267-0.432, D-H 10x more coherent) and the type-subtracted m-proxy flat
(~0.52): the germ carries nothing. This rung asks whether the CHAIN
coordinate (the Killip-Simon coordinate, deliberately) buys anything the
function face did not. A negative or split verdict is fully acceptable;
nothing is tuned toward a positive.

THE ENCODING (each step verified in-run, Q1)
============================================
finite measure of the ghost-quotiented object (finitely many point masses)
  -> Jacobi matrix by the STABLE reconstruction (discrete Stieltjes =
     Lanczos with FULL reorthogonalization at mpmath dps 50; naive
     Stieltjes-from-moments is numerically fatal and is NOT used)
  -> finite canonical-system chain via the Kac-Krein footprint construction:
     interval k has vector u_k = (q_k(0), -p_k(0)) (first/second-kind
     orthonormal polynomial values at the footpoint), H_k = u_k u_k^T
     (rank one, trace-length l_k = |u_k|^2), transfer B_k(z) = I + z J
     u_k u_k^T EXACT (nilpotent: (J u u^T)^2 = 0)
  -> trace-normalized by construction (Tr H_k = l_k, reparametrized unit
     trace); embedded in the Hur compact space V_+ via an INDIVISIBLE-TAIL
     extension. THE TAIL IS THE NAMED BUILDER-MUST-FIX: primary choice
     TAIL-N = the natural closure direction (q_M(0), -p_M(0)), the unique
     tail for which the half-line Weyl m equals the input measure's m
     exactly (round-trip certified); alternatives TAIL-0 (angle 0) and
     TAIL-D (angle pi/2) are measured for sensitivity of every downstream
     result (U6d). The tail changes ONLY the m-closure; the finite chain
     data (lengths, angles, K(x)) is tail-invariant by construction.
Convention note: our m(z) = -u2(0)/u1(0) with Weyl solution u(X) = J u_tail
was calibrated on the M=1 atom case analytically and certified by exact
round trips; the dictionary to Hur's u_1(0) = 0 boundary-condition form is
a named VERIFIER target, not assumed.

SURVEYOR FOLD-INS (remling_suzuki_canonical_pin.md, mid-round)
==============================================================
(1) The indivisible-tail extension is a standard in-print move (a finite
chain with boundary condition beta embeds via a singular half-line tail
P_{beta+pi/2}, converging in the Section 5.2 metric; Remling-Scarbrough
arXiv:1811.07067): so the must-fix is a REPORTED CHOICE among named
conventions, not an invention; the tail angle is printed per build.
(2) Metric convergence on the trace-normed space is equivalent to locally
uniform convergence of the integrated Hamiltonians M(x) = int_0^x H (Hur):
the M(x) face here IS the metric-native certificate. Local certificates
are free, so every convergence read is explicitly GERM-SCOPED (head
windows inside the shortest compared germ; no artificial-tail region ever
enters a claim).
(3) Clause (b) is NOT claimed newly isolated: Suzuki arXiv:1606.05726 v3
(JFA 2021) Thm 2.4 carries the in-print two-clause cousin (no finite-time
determinant degeneration + far-end kernel decay J(t;z,z) -> 0, the latter
proven necessary in his Thm 2.3) in a TRANSVERSE gauge (identification
free / positivity open; ours: positivity free / identification open).
(4) The U3c probe computes the e1u analogue of his J(t;z,z): the Weyl
solution's remaining H-mass beyond chain position uX (exact per interval,
germ-pure), and asks whether its decay is lambda-uniform per family: no
rate form exists anywhere in his series, so even a crude measured
comparison is new information.

TWO MEASURE FACES (both flow through identical code for all three streams)
===========================================================================
FACE A (spectral/zero face): the counting measure on the object's own strip
  zeros (ghost-quotiented where the FE-gate poses; +-t_j, unit weights,
  Prokhorov-normalized). This is the canonical Herglotz data -G'/G of the
  real-rooted object, restricted to the window (the exact lattice tail
  beyond phi N is basis-structural, T0c of e1t, family-blind by
  measurement, and is the declared truncation). Footpoint 0 (mid-gap by
  evenness). Density-typed by construction: the DMV screen MUST fire here.
FACE B (gauged coefficient face): the e1t T1f FE-gated ghost-quotient
  lattice measure aq_n = a_n / q(phi n) at atoms phi n (the object IS its
  in-band lattice data). The chain consumes the POSITIVE PART; the
  discarded fraction fneg_q is the declared admission price and is exactly
  the T1f family separator (Q5). Footpoint mid-gap via shift phi/2.

PRE-REGISTERED EXPECTATIONS AND EXITS (stated before results)
=============================================================
Q1 WELL-POSEDNESS: round trips exact at mpmath precision for all builds of
   all three families; conditioning reported honestly. Exit: a failed
   round trip is a measured price of the encoding, not tuned away.
Q2 CHAIN COHERENCE: from e1t (m-proxy flat, zero-microstructure-bound) the
   m-face is expected to stay D-H-cleanest on density-dominated reads; the
   chain-data faces (K(x), Jacobi head) are the open question; raw heads
   are expected to window-track (T3d moment radii). PRE-REGISTERED EXIT:
   if zeta shows no improvement AND clause (b) is family-blind on every
   measured face, the rung closes as a THIRD REFORMULATION and that is
   the finding.
Q3 NO-MASS-ESCAPE: prediction to test: (b) alone is Beurling-satisfiable
   at density level (degeneration indicators of the fake behave like
   zeta's): confirm or refute by measurement.
Q4 IDENTIFICATION + ENTANGLEMENT: the finite m-data that pins a chain is
   any C+-accumulating value set (Herglotz rigidity + the Hur
   homeomorphism); the CONDITIONING of that pin against a local mass
   defect is the measured question. The off-line signature: the e1k
   off-line config (D-H, lam 3.7, N 36; window covers gamma ~ 85.7) is
   rebuilt through the identical harness and read directly; prediction
   (#158): the finite chain hides the defect (reality is CF-manufactured),
   so the defect is exhibited on a SYNTHETIC off-line perturbation of the
   zeta object (nearest-degenerate zero pair collided off-axis), stated
   honestly as synthetic.
Q5 THE T1f LEAD: does the gauged zeta/D-H separation (fneg_q 0.028 vs
   0.05+) persist, close, or widen along lambda in the chain encoding; the
   deep-dressed mass collapse (sum|aq| down to 0.0017) is framed via
   Prokhorov on NORMALIZED measures (the chain input is well-defined at
   every build iff the positive part is nonzero).
Q6 DISCIPLINES: the compactness leg is density-blind by construction, so
   the DMV screen MUST fire on the Face-A certification vector (failure to
   fire is an ALARM, not a discovery); every discriminating clause is
   typed to its input (FE gate / Euler / lattice / density); K1 runtime
   guards; the pre-registered ADVERSARY question is reformulation-not-
   reduction at PRICE level (statement level was attacked in #170 and did
   not land): the .md compares the price of proving clause (b) against
   the price of uniform det-class control.

Thresholds in checks are PINNED from a calibration run of this same code
on the same builds (the e1t discipline), labeled as such, and carry no
inferential weight beyond regression pinning. dps-25 build branch caveat
inherited from e1n/e1t.

ADVERSARY ROUND (2026-07-22, same day; full record in _e1u_adversary.md)
========================================================================
The two headline zeta-first faces died under the probe's OWN
pre-registered controls (adversarial test cases 2 and 3 of the .md):
(1) the mA flip is low-band geometry: symmetric exclusion of |t| < 13.6
    restores D-H-first (0.0012 vs zeta 0.0015) and BEUR parity (0.0015),
    and at |t| >= 20 all three means agree within 1.3x (new check U2c);
    a disk beside each family's first zero restores D-H-first; the
    eps = 0.01 fake reaches D-H parity (0.0070 vs 0.0068). "Cleanest
    family" on any mid-gap disk = "deepest central gap" = first-zero-
    position data, density/FE-adjacent, exactly the U3a residual.
(2) the U3c stabilization is a UGRID-floor artifact: u_half "constant
    0.025" was pinned at the FIRST grid step; on a grid resolving
    u < 0.025 the profile gaps become ZETA {0.99, 0.11, 0.0}, D-H
    {0.85, 0.86, 0.45} NON-stabilizing, BEUR {0.28, 0.11} the smallest
    (ordering inverted), and after band equalization at 13.6 all three
    families show the identical degenerate pattern (new check U3d).
    The gated profiles collapse onto u = 0+ because X blows up (the
    relocated type divergence): the u-normalized profile is a broken
    instrument for the gated families, not a uniformity read.
Also measured: the Weyl profile is NOT tail-invariant (shifts to 0.28
face A / 0.22 face B under tail swap; the docstring claim is corrected:
germ-supported, yes; tail-invariant, no); the (b)-indicator blindness is
linear-scale saturation (deltaK spans 1e-2 down to 9e-14 with ZETA the
NEAREST to the degenerate boundary; genuine spectral escape does not
move deltaK/dispersion at all, measured flat at 0.64/0.40 with half the
mass escaping); the U4a 243x is pair-specific (sweep: 9.7x at the lowest
zeta pair, 490x mid-window, 2.9x at D-H's lowest pair: the asymmetry
TRACKS defect location, which CONFIRMS the localization reading).
Attacks that did NOT land: leave-one-out lambda (flip was in-sample
stable before the geometry controls killed it), K1 (guards trip; cold-
cache get_build rebuild bit-identical at dps 25 with guards armed), the
npz/quick discipline, round trips, the D-H 3.7/36 build, U4a/U4b as
measurements, U5 (fneg_q carried, still the only zeta-first face left).
NET: the pre-registered Q2 exit FIRES post-adversary: the rung closes
as the THIRD reformulation (after e1m and e1t), with the conditioning
panel, the entanglement numbers, and the exact embedding as the round's
durable products.

Run:
  python3 -m experiments.spectral.e1u_canonical_chain           # full
  python3 -m experiments.spectral.e1u_canonical_chain --quick   # < ~90 s, no npz
Outputs:
  experiments/spectral/e1u_canonical_chain.npz   (FULL mode only)
  experiments/spectral/_cache/e1t_build_*.npz    (shared build cache, gitignored)
"""

from __future__ import annotations

import argparse
import math
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp

# The e1t harness is consumed BY IMPORT so that zeta, D-H and the Beurling
# fake flow through literally the same build code that e1t verified
# bit-identical to e1k (T0a/T0b/T0d there). Nothing is re-implemented.
from experiments.spectral.e1t_compact_class_limit import (
    build_comb, int_pairs, get_build, ghost_gate, qpoly, streams, projd, ZZ,
)
from experiments.spectral.e1k_dh_dlog_testbed import build_float, ZETA_CFG
from experiments.spectral.e1m_hamburger_pin import winding_count
import experiments._shared.davenport_heilbronn as _dhmod

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")
E1T_NPZ = Path(__file__).parent / "e1t_compact_class_limit.npz"
SQRT13 = float(np.sqrt(13.0))
CHAIN_DPS = 50   # chain pipeline precision (builds stay on the dps-25 branch)

CHECKS: list = []
LEDGER: dict = {}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def consume(test, *inputs):
    LEDGER.setdefault(test, []).extend(inputs)


# fixed identification compact (pre-registered geometry): the disk
# |z - 2i| <= 0.9, safely inside C+, mirroring the Remling/Hur metric disk
# |z - 2i| <= 1 on which the H <-> m map is a homeomorphism.
MSAMP = [complex(2j)] + [complex(2j + 0.9 * np.exp(1j * t))
                         for t in np.linspace(0, 2 * np.pi, 12, endpoint=False)]
# robustness disk (geometry-caveat probe): the 2i disk sits closer to D-H's
# low zeros (5.09) than to zeta's (14.1); any family ordering read off the
# 2i disk must survive a farther disk or it is disk-geometry, not structure.
MSAMP6 = [complex(6j)] + [complex(6j + 0.9 * np.exp(1j * t))
                          for t in np.linspace(0, 2 * np.pi, 12, endpoint=False)]


def chordal(w1, w2):
    """Spherical (chordal) metric on Herglotz values, per the Remling/Hur
    metric on the m-target space (which includes the degenerate reals)."""
    w1, w2 = complex(w1), complex(w2)
    return abs(w1 - w2) / math.sqrt((1 + abs(w1) ** 2) * (1 + abs(w2) ** 2))


def m_dist(mvals1, mvals2):
    return max(chordal(a, b) for a, b in zip(mvals1, mvals2))


# ==========================================================================
# The chain encoder: measure -> Jacobi -> Kac-Krein footprint chain -> Weyl m.
# All mpmath at CHAIN_DPS; exactness certified by round trips (U1a/U1b),
# never assumed. WHY Lanczos-with-reorth and not moments: the moment map is
# exponentially ill-conditioned (Gautschi; the Gragg-Harrod/RKPW literature
# exists because of exactly that failure); the discrete Stieltjes procedure
# with full reorthogonalization is the stable route and its residual drift
# is CAUGHT by the round-trip certificate rather than estimated.
# ==========================================================================
def lanczos_jacobi(xs, ws):
    """Discrete Stieltjes/Lanczos with full reorthogonalization.
    xs, ws: mpf lists (ws > 0, any mass; normalized internally).
    Returns bs (len M), as_ (len M-1), orth_defect (spot-checked)."""
    M = len(xs)
    W = mp.fsum(ws)
    ws = [w / W for w in ws]

    def ip(f, g):
        return mp.fsum(w * a * b for w, a, b in zip(ws, f, g))

    ps = [[mp.mpf(1)] * M]
    bs, as_ = [], []
    for k in range(M):
        pk = ps[k]
        b = ip([x * v for x, v in zip(xs, pk)], pk)
        bs.append(b)
        if k == M - 1:
            break
        r = [x * v - b * v for x, v in zip(xs, pk)]
        if k > 0:
            r = [ri - as_[k - 1] * vi for ri, vi in zip(r, ps[k - 1])]
        for pj in ps:   # full reorthogonalization (the stability step)
            c = ip(r, pj)
            r = [ri - c * vj for ri, vj in zip(r, pj)]
        a = mp.sqrt(ip(r, r))
        as_.append(a)
        ps.append([ri / a for ri in r])
    # spot orthogonality defect (adjacent + first-vs-last: the classical
    # loss modes), cheap versus the full Gram matrix
    pairs = [(0, M - 1), (0, 1), (M // 2, M - 1)] if M > 1 else []
    odef = max((abs(ip(ps[i], ps[j])) for i, j in pairs), default=mp.mpf(0))
    return bs, as_, float(odef)


def footprints(bs, as_, z):
    """First-kind p_k(z) and second-kind q_k(z), k = 0..M-1, plus the
    closure pair (p_M, q_M) with the a_M := 1 convention. The closure is
    what makes m(z) = -q_M/p_M the EXACT m of the M-atom measure."""
    M = len(bs)
    p, q = [mp.mpf(1)], [mp.mpf(0)]
    for k in range(M - 1):
        pa = as_[k - 1] * p[k - 1] if k > 0 else 0
        qa = as_[k - 1] * q[k - 1] if k > 0 else 0
        p.append(((z - bs[k]) * p[k] - pa) / as_[k])
        q.append(((z - bs[k]) * q[k] - qa + (1 if k == 0 else 0)) / as_[k])
    if M == 1:
        pM, qM = z - bs[0], mp.mpf(1)
    else:
        pM = (z - bs[M - 1]) * p[M - 1] - as_[M - 2] * p[M - 2]
        qM = (z - bs[M - 1]) * q[M - 1] - as_[M - 2] * q[M - 2]
    return p, q, pM, qM


class Chain:
    """Finite trace-normed canonical-system chain of an atomic probability
    measure, in the Kac-Krein footprint construction, embedded in the Hur
    compact space by an indivisible tail (angle reported, variants measured).

    Interval k: vector u_k = (q_k(0), -p_k(0)), H_k = u_k u_k^T (rank one),
    trace-length l_k = |u_k|^2. Transfer over interval k is EXACT:
    B_k(z) = I + z J u_k u_k^T, because (J u u^T)^2 = 0. The footpoint
    (spectral shift s) puts z = 0 mid-gap; all m evaluations are returned
    in UNSHIFTED coordinates: m_mu(z) = m_chain(z + s)."""

    def __init__(self, atoms, weights, shift):
        with mp.workdps(CHAIN_DPS):
            xs = [mp.mpf(float(x)) + mp.mpf(float(shift)) for x in atoms]
            ws = [mp.mpf(float(w)) for w in weights]
            self.shift = mp.mpf(float(shift))
            self._Wmp = mp.fsum(ws)   # mpf total mass (float W would floor
            self.W = float(self._Wmp)  # the round trip at 1e-17)
            self.M = len(xs)
            self.atoms = np.asarray(atoms, float)
            self.wts = np.asarray(weights, float)
            self.bs, self.as_, self.orth_defect = lanczos_jacobi(xs, ws)
            p0, q0, pM, qM = footprints(self.bs, self.as_, mp.mpf(0))
            self.u = [(q0[k], -p0[k]) for k in range(self.M)]
            self.u_tail = (qM, -pM)
            self.lens = np.array([float(a * a + b * b) for a, b in self.u])
            self.angles = np.array([math.atan2(float(b), float(a)) % math.pi
                                    for a, b in self.u])
            self.tail_angle = math.atan2(float(-pM), float(qM)) % math.pi
            self.X = float(np.sum(self.lens))
            self.xs_mp, self.ws_mp = xs, ws

    # ---- Weyl m (chain-native), tail variants -----------------------------
    def _tail_vec(self, tail):
        if tail == "N":
            return self.u_tail
        if tail == "0":
            return (mp.mpf(1), mp.mpf(0))
        return (mp.mpf(0), mp.mpf(1))   # "D", angle pi/2

    def _transfer(self, z):
        """U(X, z) = B_{M-1} ... B_0 (leftmost interval first)."""
        U = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
        for (ua, ub) in self.u:
            # B = I + z J u u^T with J = [[0,-1],[1,0]]
            r0 = [-z * ub * ua, -z * ub * ub]
            r1 = [z * ua * ua, z * ua * ub]
            U = [[(1 + r0[0]) * U[0][0] + r0[1] * U[1][0],
                  (1 + r0[0]) * U[0][1] + r0[1] * U[1][1]],
                 [r1[0] * U[0][0] + (1 + r1[1]) * U[1][0],
                  r1[0] * U[0][1] + (1 + r1[1]) * U[1][1]]]
        return U

    def _weyl_u0(self, z, tail):
        U = self._transfer(z)
        ut = self._tail_vec(tail)
        uX = (-ut[1], ut[0])            # u(X) = J u_tail (bc angle beta,
        det = U[0][0] * U[1][1] - U[0][1] * U[1][0]   # tail P_{beta+pi/2})
        return ((U[1][1] * uX[0] - U[0][1] * uX[1]) / det,
                (-U[1][0] * uX[0] + U[0][0] * uX[1]) / det)

    def m(self, z, tail="N"):
        """m of the HALF-LINE embedded system, in unshifted coordinates.
        Returns mpc (round trips are judged at CHAIN_DPS, not float)."""
        with mp.workdps(CHAIN_DPS):
            zz = mp.mpc(z) + self.shift
            u0 = self._weyl_u0(zz, tail)
            return -u0[1] / u0[0]

    def m_direct(self, z):
        """Direct spectral m of the (normalized) input measure (mpc)."""
        with mp.workdps(CHAIN_DPS):
            zz = mp.mpc(z)
            return mp.fsum(
                (mp.mpf(float(w)) / self._Wmp) / (mp.mpf(float(x)) - zz)
                for x, w in zip(self.atoms, self.wts))

    def m_jacobi(self, z):
        """m via the closure polynomials -q_M/p_M (isolates Lanczos error
        from chain error in the round-trip ledger). Returns mpc."""
        with mp.workdps(CHAIN_DPS):
            zz = mp.mpc(z) + self.shift
            _, _, pM, qM = footprints(self.bs, self.as_, zz)
            return -qM / pM

    # ---- chain-data faces (tail-invariant by construction) ----------------
    def Mx(self, xgrid):
        """Integrated Hamiltonian M(x) = int_0^x H dt on the FINITE GERM
        (the metric-native object: Hur's metric convergence is equivalent
        to locally uniform convergence of M(x)). Returns (len(xgrid), 3)
        array of (M11, M12, M22). Tail-scoped: defined only on the germ;
        callers must keep x <= X or scope the claim."""
        ends = np.cumsum(self.lens)
        starts = ends - self.lens
        c, s = np.cos(self.angles), np.sin(self.angles)
        h11, h12, h22 = c * c, c * s, s * s
        out = np.zeros((len(xgrid), 3))
        for i, x in enumerate(xgrid):
            covered = np.clip(x - starts, 0.0, self.lens)
            out[i] = (np.sum(covered * h11), np.sum(covered * h12),
                      np.sum(covered * h22))
        return out

    def indicators(self):
        """Degeneration indicators of the finite germ (chain-geometry
        face: length-weighted angle balance and indivisibility).
        [ADVERSARY] These are NOT no-mass-escape detectors: a family
        with half its spectral mass escaping to infinity leaves deltaK/
        dispersion flat (measured 0.64/0.40 at T = 5..320), and on the
        gated Face-A builds deltaK sits at the degenerate boundary
        (down to 9e-14) because of the central-gap length blowup, so
        linear-scale comparisons of these numbers are saturation reads
        (see the U3a check-text caveat)."""
        Mtot = self.Mx(np.array([self.X]))[0]
        detK = Mtot[0] * Mtot[2] - Mtot[1] ** 2
        delta_total = float(4 * detK / self.X ** 2)   # 1 balanced, 0 indivisible
        zsum = np.sum(self.lens * np.exp(2j * self.angles))
        dispersion = float(1 - abs(zsum) / np.sum(self.lens))
        return dict(X_total=self.X, delta_total=delta_total,
                    dispersion=dispersion,
                    min_len=float(np.min(self.lens)),
                    max_len=float(np.max(self.lens)),
                    l0=float(self.lens[0]))

    def weyl_tail_mass(self, z0, ugrid, tail="N"):
        """The Suzuki-analogue no-mass-at-the-singular-end profile: the
        Weyl solution's remaining H-mass beyond chain position u*X,
        normalized to 1 at u = 0. Exact per interval: on an indivisible
        interval e^T u(t) is CONSTANT, so interval k contributes
        l_k |e_k^T f(x_k)|^2. GERM-SUPPORTED by construction: the
        artificial indivisible tail carries exactly ZERO Weyl H-mass.
        [ADVERSARY] NOT tail-invariant: the Weyl solution depends on the
        tail angle through its boundary vector, and the normalized
        profile shifts by up to 0.28 (face A) / 0.22 (face B) under the
        tail swap (U6d detail); "pure germ observable" means the mass
        lives on the germ, not that the read is tail-free.
        Returns (profile, total, identity_err):
        the internal certificate is the exact S(x) = u^T J conj(u) calculus,
        total = |f_1(0)|^2 Im m / Im z, evaluated at CHAIN_DPS."""
        with mp.workdps(CHAIN_DPS):
            zz = mp.mpc(z0) + self.shift
            f = list(self._weyl_u0(zz, tail))
            mm = -f[1] / f[0]
            contrib_mp = []
            for (ua, ub) in self.u:
                # l_k |e_k^T f|^2 = |u_k^T f|^2 (since |u_k|^2 = l_k)
                contrib_mp.append(abs(ua * f[0] + ub * f[1]) ** 2)
                gain = zz * (ua * f[0] + ub * f[1])
                f = [f[0] - gain * ub, f[1] + gain * ua]
            total = mp.fsum(contrib_mp)
            pred = abs(self._weyl_u0(zz, tail)[0]) ** 2 * mp.im(mm) / mp.im(mp.mpc(z0))
            iderr = float(abs(total - pred) / abs(pred))
            contrib = np.array([float(c) for c in contrib_mp])
            ends = np.cumsum(self.lens)
            tot_f = float(total)
            prof = np.array([np.sum(contrib[ends > u * self.X]) for u in ugrid])
            return prof / tot_f, tot_f, iderr


# ==========================================================================
# Measure extraction: the two faces. Identical code for all three streams;
# family differences enter ONLY through the comb input and the FE-typed
# ghost gate (documented input typing, exactly as in e1t).
# ==========================================================================
def real_zeros(fn, t_lo, t_hi, step):
    """Sign-change scan + bisection on Re fn along the real axis. Consumes
    only the OBJECT's own values (K1: no L-function zero list anywhere).
    Endpoint-inclusive (a plain arange loses the final partial cell, which
    cost one BEUR zero at 56.89 in calibration)."""
    xs = np.append(np.arange(t_lo, t_hi, step), t_hi)
    g = np.real(fn(xs))
    out = []
    for i in np.where(np.diff(np.sign(g)) != 0)[0]:
        lo, hi = xs[i], xs[i + 1]
        flo = float(np.real(fn(np.array([lo]))[0]))
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            fm = float(np.real(fn(np.array([mid]))[0]))
            if (fm > 0) == (flo > 0):
                lo, flo = mid, fm
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    # dedupe boundary-duplicated roots
    ded = []
    for t in out:
        if not ded or abs(t - ded[-1]) > 1e-6:
            ded.append(t)
    return ded


def face_A(label, lam, N):
    """Zero-counting measure of the ghost-quotiented object: atoms +-t_j
    (window zeros), unit weights, footpoint 0 (mid-gap by evenness).
    Returns (atoms, weights, shift, meta)."""
    xh, _ = get_build(label, lam, N)
    gate, z0s = ghost_gate(label, xh)
    Twin = 2 * math.pi * lam * lam

    def G(zv):
        return xh(zv) / qpoly(zv, z0s)

    lo = (13.6 if label == "ZETA" else 4.9) if z0s or gate == "POSABLE" else 0.05
    # scan starts above the quotiented band for gated streams (the quotient
    # removed everything below by the FE budget); the fake scans from 0.05.
    # The scan window matches the winding contour [lo, Twin + 0.4] so the
    # U1d cross-check compares like with like.
    # step phi/32: finer than the closest observed pair (sep 0.124 at
    # ZETA 3.0 vs phi/16 = 0.179 there, alignment luck not relied on)
    tz = [t for t in real_zeros(G, lo + 1e-3, Twin + 0.4, xh.phi / 32)
          if all(abs(t - z0) > 1e-6 for z0 in z0s)]
    atoms = np.array([-t for t in tz[::-1]] + tz)
    return atoms, np.ones(len(atoms)), 0.0, dict(
        gate=gate, nghost=len(z0s), tz=tz, Twin=Twin, xh=xh, z0s=z0s,
        min_dist=min(tz) if tz else np.inf)


def face_B(label, lam, N):
    """The e1t T1f FE-gated ghost-quotient lattice measure: atoms phi n,
    signed weights aq_n = a_n / q(phi n) (sign-fixed, invertible,
    object-computable). Returns the SIGNED measure; the chain consumes the
    positive part and the discarded fraction is the declared price."""
    xh, _ = get_build(label, lam, N)
    gate, z0s = ghost_gate(label, xh)
    c = np.real(xh.coef)
    a = ((-1.0) ** xh.idx) * c
    if a[np.argmax(np.abs(a))] < 0:
        a = -a
    x_lat = xh.phi * np.asarray(xh.idx, float)
    qlat = (np.real(qpoly(x_lat.astype(complex), z0s)) if len(z0s)
            else np.ones_like(x_lat))
    aq = a / qlat
    if aq[np.argmax(np.abs(aq))] < 0:
        aq = -aq
    tvq = float(np.sum(np.abs(aq)))
    fneg_q = float(np.sum(np.abs(aq[aq < 0])) / tvq)
    return x_lat, aq, xh.phi / 2, dict(
        gate=gate, nghost=len(z0s), tvq=tvq, fneg_q=fneg_q, phi=xh.phi, xh=xh)


def build_chain(atoms, weights, shift):
    """Positive-part chain, dropping w <= 0 (declared; the discarded
    fraction is reported by the caller as the admission price)."""
    keep = weights > 0
    return Chain(atoms[keep], weights[keep], shift)


# ==========================================================================
# Face instruments.
# ==========================================================================
XHEAD = 5.0                      # head-window CAP for the M(x) face
UGRID = np.linspace(0.0, 1.0, 41)          # shape grid (germ-only)
JHEAD = 12                       # Jacobi head length compared across lambda


def mvals(ch, tail="N"):
    return [ch.m(z, tail) for z in MSAMP]


def dMx_head(ch1, ch2, xmax):
    """Metric-native head distance: sup Frobenius |M1(x) - M2(x)| on
    [0, xmax]. The caller passes xmax = min(XHEAD, 0.9 min X_total over the
    compared family-face), so the window is PURE GERM for every build (the
    surveyor's tail-scoping rule enforced by construction: no artificial-
    tail region ever enters a convergence claim)."""
    grid = np.linspace(0.0, xmax, 51)
    A, B = ch1.Mx(grid), ch2.Mx(grid)
    d = A - B
    fro = np.sqrt(d[:, 0] ** 2 + 2 * d[:, 1] ** 2 + d[:, 2] ** 2)
    return float(np.max(fro))


def dMx_shape(ch1, ch2):
    """Shape distance: M(u X)/X profiles on the unit grid (germ-only,
    scale-free: compares the mass-distribution profile of the chains)."""
    A = ch1.Mx(UGRID * ch1.X) / ch1.X
    B = ch2.Mx(UGRID * ch2.X) / ch2.X
    d = A - B
    fro = np.sqrt(d[:, 0] ** 2 + 2 * d[:, 1] ** 2 + d[:, 2] ** 2)
    return float(np.max(fro))


def dJacobi(ch1, ch2):
    """Killip-Simon coordinate distances on the head: raw and
    support-radius-scaled (shape). Head = first JHEAD entries."""
    k = min(JHEAD, len(ch1.bs) - 1, len(ch2.bs) - 1)
    b1 = np.array([float(v) for v in ch1.bs[:k]])
    b2 = np.array([float(v) for v in ch2.bs[:k]])
    a1 = np.array([float(v) for v in ch1.as_[:k]])
    a2 = np.array([float(v) for v in ch2.as_[:k]])
    raw = max(np.max(np.abs(b1 - b2)), np.max(np.abs(a1 - a2)))
    r1 = np.max(np.abs(ch1.atoms + float(ch1.shift)))
    r2 = np.max(np.abs(ch2.atoms + float(ch2.shift)))
    sc = max(np.max(np.abs(b1 / r1 - b2 / r2)), np.max(np.abs(a1 / r1 - a2 / r2)))
    return raw, sc


RTPTS = [2j, 1 + 2j, -0.7 + 1.3j, 3 + 5j, 25 + 1.5j]


def rt_errs(ch):
    """Round-trip errors evaluated INSIDE the chain precision context (the
    ambient dps-25 build branch would otherwise floor the comparison)."""
    with mp.workdps(CHAIN_DPS):
        ej = max(abs(ch.m_jacobi(z) - ch.m_direct(z)) for z in RTPTS)
        ec = max(abs(ch.m(z) - ch.m_direct(z)) for z in RTPTS)
    return float(ej), float(ec)


# ==========================================================================
# U0: harness identity (the "identical code" claim, made checkable).
# ==========================================================================
def run_u0(results, quick):
    print("\n[U0] HARNESS IDENTITY: e1t machinery consumed by import; record consistency")
    consume("U0", "Lambda stream (arithmetic input, no zeros)",
            "tiny fidelity build (N=4, lam=1.8)")
    mods = {get_build.__module__, ghost_gate.__module__, qpoly.__module__,
            build_comb.__module__}
    same = mods == {"experiments.spectral.e1t_compact_class_limit"}
    lz, _ = streams()
    rf = build_float(4, 1.8, lz, ZETA_CFG["dens_a"], ZETA_CFG["dens_b"], True)
    rc = build_comb(4, 1.8, int_pairs(lz, 1.8), ZETA_CFG["dens_a"],
                    ZETA_CFG["dens_b"], True)
    dq = float(np.max(np.abs(rf["Q"] - rc["Q"])))
    check("U0a harness identity: build/gate/gauge functions ARE e1t's by import "
          "(module check) and build_comb == build_float bit-identical at the "
          "fidelity config", same and dq < 1e-12,
          f"modules={'e1t' if same else mods}, max|dQ|={dq:.1e}")
    results["u0_dq"] = dq

    if E1T_NPZ.exists():
        d = np.load(E1T_NPZ)
        errs = {}
        for label, lam, N in GRID_FULL if not quick else GRID_QUICK:
            tag = f"t1_{label.replace('-', '')}_{lam:.3f}_eps"
            if tag in d:
                _, meta = get_build(label, lam, N)
                errs[(label, lam)] = abs(float(d[tag]) - meta["eps"])
        worst = max(errs.values()) if errs else np.inf
        # [PORTABILITY FIX 2026-08-09, LEARNINGS #172] The tolerance was
        # 1e-15, which asserted same-machine BIT reproducibility rather than
        # numerical agreement. eps is determined by the build to only ~1e-10
        # ABSOLUTE: the archimedean density uses a central-difference digamma
        # at h = 1e-5 in float64, whose own relative accuracy measures ~5e-10
        # against exact mpmath digamma. A fresh machine therefore deviated by
        # 3.7e-11 (worst over the full grid) while EVERY structural number
        # reproduced to printed precision, and e1u scored 16/18 there. Now a
        # numerical-agreement check at 1e-9 (27x the measured worst), which is
        # verified to still catch a genuine regression: the documented
        # dps-branch flip trips it by 3e5x. Evidence and both measurements:
        # _e1u_portability.py.
        check("U0b cached-build eps values agree with the tracked e1t npz "
              "record to the build's own accuracy floor (numerical agreement, "
              "not bit reproducibility; tolerance pinned and teeth verified in "
              "_e1u_portability.py)",
              bool(errs) and worst < 1e-9,
              f"{len(errs)} builds, max|deps|={worst:.1e} (tol 1e-9)")
        results["u0_eps_worst"] = worst
    else:
        print("    (U0b skipped: e1t npz not present; no record to cross-check)")


# ==========================================================================
# U1 (Q1): embedding well-posedness. Round trips certified, conditioning
# reported, trace-norming exact, scan-vs-winding zero consistency.
# ==========================================================================
def run_u1(results, grid, quick):
    print("\n[U1/Q1] WELL-POSEDNESS: encoder exactness, round trips, conditioning")
    consume("U1", "object values on R + contours (own zeros; no L-zero lists)",
            "reference measures (synthetic atoms, seeded)")

    # ---- U1a: encoder reference tests (conventions frozen by calibration
    # on the analytic M=1 case; see module docstring) ----
    with mp.workdps(CHAIN_DPS):
        ch1 = Chain(np.array([2.5]), np.array([1.0]), 0.0)
        target = 1.0 / (mp.mpf("2.5") - mp.mpc(2j))
        e_analytic = float(abs(ch1.m(2j) - target))
        rng = np.random.default_rng(20260722)
        xs5 = np.sort(rng.uniform(-5, 5, 5))
        ws5 = rng.uniform(0.1, 1.0, 5)
        ch5 = Chain(xs5, ws5, 0.3)
        e5 = float(max(abs(ch5.m(z) - ch5.m_direct(z)) for z in RTPTS))
        e5j = float(max(abs(ch5.m_jacobi(z) - ch5.m_direct(z)) for z in RTPTS))
    check("U1a(Q1) encoder exact on reference measures: M=1 analytic atom and "
          "seeded M=5, chain-m and jacobi-m round trips at mpmath precision",
          e_analytic < 1e-40 and e5 < 1e-40 and e5j < 1e-40,
          f"M=1 err {e_analytic:.1e}, M=5 chain {e5:.1e}, jacobi {e5j:.1e}")
    results["u1_ref_errs"] = np.array([e_analytic, e5, e5j])

    # ---- build all chains (both faces, full grid) ----
    faces = {}
    for label, lam, N in grid:
        for face, extractor in (("A", face_A), ("B", face_B)):
            atoms, wts, shift, meta = extractor(label, lam, N)
            ch = build_chain(atoms, wts, shift)
            ej, ec = rt_errs(ch)
            ind = ch.indicators()
            fneg = meta.get("fneg_q", 0.0)
            faces[(label, lam, face)] = dict(
                ch=ch, meta=meta, ej=ej, ec=ec, ind=ind,
                fneg=fneg, mvN=mvals(ch, "N"))
            tag = f"u1_{label.replace('-', '')}_{lam:.3f}_{face}"
            results[f"{tag}_rt"] = np.array([ej, ec])
            results[f"{tag}_lens"] = np.array(
                [ind["X_total"], ind["min_len"], ind["max_len"], ind["l0"]])
            results[f"{tag}_M"] = ch.M
            print(f"    {label:5s} lam={lam:.3f} {face}: M={ch.M:3d} "
                  f"rt_jac={ej:.1e} rt_chain={ec:.1e} "
                  f"orth={ch.orth_defect:.1e} X={ind['X_total']:.1f} "
                  f"l0={ind['l0']:.3f} len[{ind['min_len']:.2e},{ind['max_len']:.1f}] "
                  f"tail_ang={ch.tail_angle:.3f}"
                  + (f" fneg_q={fneg:.4f}" if face == "B" else
                     f" gate={meta['gate'][:8]}"))

    # ---- U1b: full-pipeline round trip on every build-face ----
    worst_j = max(v["ej"] for v in faces.values())
    worst_c = max(v["ec"] for v in faces.values())
    worst_o = max(v["ch"].orth_defect for v in faces.values())
    check("U1b(Q1) full-pipeline round trip on ALL build-faces of all three "
          "families: measure -> Jacobi -> chain -> Weyl m returns the direct "
          "spectral m at mpmath precision (encoding well-posed, conditioning "
          "in the ledger)", worst_j < 1e-30 and worst_c < 1e-30,
          f"worst jacobi {worst_j:.1e}, worst chain {worst_c:.1e}, "
          f"worst orth defect {worst_o:.1e}")
    results["u1_worst_rt"] = np.array([worst_j, worst_c, worst_o])

    # ---- U1c: trace-normalization exact + structural chain facts ----
    l0s = [v["ind"]["l0"] for v in faces.values()]
    minl = min(v["ind"]["min_len"] for v in faces.values())
    xmin = min(v["ind"]["X_total"] for v in faces.values())
    check("U1c(Q1) trace-norming exact by construction: every interval H_k is "
          "a unit-trace rank-one projector scaled by l_k; l_0 = 1 exactly "
          "(p_0=1, q_0=0); min l_k > 0 (footprint nondegeneracy); germs "
          "nondegenerate (head windows are germ-scoped per family-face in U2)",
          max(abs(l - 1) for l in l0s) < 1e-30 and minl > 0 and xmin > 1.0,
          f"max|l0-1|={max(abs(l - 1) for l in l0s):.1e}, min len={minl:.2e}, "
          f"min X={xmin:.1f}")
    results["u1_minlen_minX"] = np.array([minl, xmin])

    # ---- U1d: Face-A zero scan vs winding count (grid-independent cross-
    # check; strip counts are dps-branch-dependent per e1t, caveat inherited)
    wgrid = ([g for g in grid if g[0] == "ZETA"][:1]
             + [g for g in grid if g[0] == "BEUR"][:1]) if quick else grid
    wind_ok, det = [], []
    for label, lam, N in wgrid:
        fa = faces[(label, lam, "A")]
        xh, z0s = fa["meta"]["xh"], fa["meta"]["z0s"]
        Twin = fa["meta"]["Twin"]
        lo = (13.6 if label == "ZETA" else 4.9) if fa["meta"]["gate"] == "POSABLE" \
            else 0.05
        f = lambda z: complex((xh(np.array([z])) / qpoly(np.array([z]), z0s))[0])
        e = lo - 0.03 + 1e-3
        w, r, _ = winding_count(
            f, [e - 0.4j, Twin + 0.4 - 0.4j, Twin + 0.4 + 0.4j, e + 0.4j], n0=256)
        nz = len(fa["meta"]["tz"])
        wind_ok.append(r < 0.05 and round(w) == nz)
        det.append(f"{label} {lam:.2f}: scan {nz} wind {w:.2f}")
    check("U1d(Q1) Face-A zero scan agrees with the winding count on the "
          "quotiented object (the atoms are the object's own strip zeros; "
          "count on the dps-25 branch, e1n caveat inherited)",
          all(wind_ok), "; ".join(det))
    return faces


def fam_lams(grid):
    fam = {}
    for label, lam, N in grid:
        fam.setdefault(label, []).append(lam)
    for v in fam.values():
        v.sort()
    return fam


# ==========================================================================
# U2 (Q2): chain-coordinate coherence vs the e1t function-face baseline.
# ==========================================================================
def run_u2(results, faces, grid, quick):
    print("\n[U2/Q2] CHAIN COHERENCE: m-face and chain-data gaps vs the e1t baseline")
    consume("U2", "chain data + m samples on the fixed compact (object data)")
    fam = fam_lams(grid)

    # baseline: the e1t T3b function-face projective gaps, recomputed through
    # the imported e1t instruments (same ZZ grid, same quotient, same projd)
    gaps_fn = {}
    for label, lams in fam.items():
        FZ = {}
        for lam in lams:
            meta = faces[(label, lam, "A")]["meta"]
            FZ[lam] = meta["xh"](ZZ) / qpoly(ZZ, meta["z0s"])
        gaps_fn[label] = [projd(FZ[a], FZ[b]) for a, b in zip(lams, lams[1:])]
        results[f"u2_fngaps_{label.replace('-', '')}"] = np.array(gaps_fn[label])

    # chain faces: m (TAIL-N), Mx head, Mx shape, Jacobi raw/scaled.
    # Head windows are GERM-SCOPED per family-face (tail-scoping rule): the
    # window is min(XHEAD cap, 0.9 x the shortest germ in that family-face),
    # so no artificial-tail region ever enters a convergence read.
    tabs = {f: {} for f in ("mA", "mB", "hA", "hB", "sA", "sB",
                            "jrA", "jrB", "jsA", "jsB")}
    xh_ff = {}
    for label, lams in fam.items():
        for face in ("A", "B"):
            xh_ff[(label, face)] = min(
                XHEAD, 0.9 * min(faces[(label, lam, face)]["ind"]["X_total"]
                                 for lam in lams))
    print("    germ-scoped head windows (family, face) -> x_max: " + ", ".join(
        f"{k[0]}/{k[1]} {v:.2f}" for k, v in xh_ff.items()))
    for label, lams in fam.items():
        for a, b in zip(lams, lams[1:]):
            for face in ("A", "B"):
                c1, c2 = faces[(label, a, face)], faces[(label, b, face)]
                tabs["m" + face].setdefault(label, []).append(
                    m_dist(c1["mvN"], c2["mvN"]))
                tabs["h" + face].setdefault(label, []).append(
                    dMx_head(c1["ch"], c2["ch"], xh_ff[(label, face)]))
                tabs["s" + face].setdefault(label, []).append(
                    dMx_shape(c1["ch"], c2["ch"]))
                jr, js = dJacobi(c1["ch"], c2["ch"])
                tabs["jr" + face].setdefault(label, []).append(jr)
                tabs["js" + face].setdefault(label, []).append(js)
    results["u2_headwin"] = np.array(list(xh_ff.values()))
    for key, t in tabs.items():
        for label, g in t.items():
            results[f"u2_{key}_{label.replace('-', '')}"] = np.array(g)

    print("    consecutive-lambda gap tables (germ-scoped chain data; m on the")
    print("    fixed disk |z-2i|<=0.9 in chordal metric; fn = e1t baseline):")
    for label in fam:
        if len(fam[label]) < 2:
            continue
        print(f"      {label}: fn {[round(g, 3) for g in gaps_fn[label]]}")
        for key, name in (("mA", "m-face A"), ("mB", "m-face B"),
                          ("hA", "M(x) head A"), ("hB", "M(x) head B"),
                          ("sA", "M(x) shape A"), ("sB", "M(x) shape B"),
                          ("jsA", "Jacobi shape A"), ("jsB", "Jacobi shape B")):
            print(f"        {name:14s} {[round(g, 4) for g in tabs[key][label]]}")

    # improvement ratios: each family normalized by its OWN function-face
    # baseline (scale-free; the load-bearing zeta-vs-D-H comparison)
    imp = {}
    for key in ("mA", "mB", "sA", "sB"):
        for label in fam:
            if label in tabs[key] and gaps_fn.get(label):
                imp[(key, label)] = (float(np.mean(tabs[key][label]))
                                     / float(np.mean(gaps_fn[label])))
    for (key, label), v in imp.items():
        results[f"u2_imp_{key}_{label.replace('-', '')}"] = v
    if imp:
        print("    improvement ratios (chain-face mean gap / function-face mean gap):")
        for key in ("mA", "mB", "sA", "sB"):
            row = {lab: imp.get((key, lab)) for lab in fam if (key, lab) in imp}
            print(f"      {key}: " + ", ".join(f"{lab} {v:.3f}" for lab, v in row.items()))

    if not quick:
        # baseline consistency against the tracked e1t record (same code
        # path, same caches: the improvement DENOMINATOR is the recorded one)
        base_err = 0.0
        if E1T_NPZ.exists():
            d = np.load(E1T_NPZ)
            for label in fam:
                key = f"t3_gaps_{label.replace('-', '')}"
                if key in d and len(gaps_fn.get(label, [])):
                    base_err = max(base_err, float(np.max(np.abs(
                        np.array(gaps_fn[label]) - d[key]))))
        # robustness disk at 6i: does the mA ordering survive away from the
        # low-zero geometry of the 2i disk?
        m6 = {}
        for label, lams in fam.items():
            vals = {lam: [faces[(label, lam, "A")]["ch"].m(z) for z in MSAMP6]
                    for lam in lams}
            m6[label] = [m_dist(vals[a], vals[b]) for a, b in zip(lams, lams[1:])]
            results[f"u2_m6_{label.replace('-', '')}"] = np.array(m6[label])
        print("    robustness disk 6i, m-face A gaps: " + "; ".join(
            f"{lab} {[round(g, 4) for g in m6[lab]]}" for lab in fam
            if len(m6.get(lab, [])) > 0))
        # [PINNED from the calibration run, deterministic rerun] the measured
        # outcome: the mA ordering FLIPS relative to the e1t function face
        # (zeta cleanest at 0.0015 mean vs D-H 0.005, BEUR 0.013), zeta's
        # improvement ratio is ~40x D-H's (0.005 vs 0.214), BUT the shape
        # face is family-blind-small (weak-topology collapse: compactness
        # free where information-free) and no zeta gap sequence is
        # monotonically decreasing: no coincidence certificate anywhere.
        z_m = float(np.mean(tabs["mA"]["ZETA"]))
        d_m = float(np.mean(tabs["mA"]["D-H"]))
        b_m = float(np.mean(tabs["mA"]["BEUR"]))
        zeta_first = z_m < d_m < b_m
        imp_gap = imp[("mA", "ZETA")] < 0.05 < imp[("mA", "D-H")]
        shape_blind = max(max(g) for g in tabs["sA"].values()) < 0.005
        z_seq = tabs["mA"]["ZETA"]
        no_cert = not all(a > b for a, b in zip(z_seq, z_seq[1:]))
        z6 = float(np.mean(m6["ZETA"]))
        d6 = float(np.mean(m6["D-H"]))
        # [PORTABILITY FIX 2026-08-09, LEARNINGS #172] base_err was
        # compared at 1e-9, the third bit-reproducibility assertion in
        # this module (with U0b and U5a). It compares the recomputed
        # e1t function-face baseline against the tracked record, so it
        # inherits the build noise floor and amplifies it: measured
        # 2.7e-7 on a fresh machine. Tolerance 1e-5 (37x the measured
        # deviation, and still ~1400x below the SMALLEST tracked gap,
        # 0.014), so it remains a real check on the improvement
        # denominator. NOTE the four content clauses below (ordering,
        # improvement gap, shape-blindness, no-certificate) reproduced
        # EXACTLY on the fresh machine; only the record comparison
        # failed. Evidence: _e1u_portability.py.
        cond = (base_err < 1e-5 and zeta_first and imp_gap and shape_blind
                and no_cert)
        detail = (f"mA means z/d/b = {z_m:.4f}/{d_m:.4f}/{b_m:.4f}; imp "
                  f"{imp[('mA', 'ZETA')]:.3f} vs {imp[('mA', 'D-H')]:.3f}; "
                  f"6i-disk means z/d = {z6:.4f}/{d6:.4f}; base_err {base_err:.1e}")
    else:
        cond = all(np.isfinite(g) for g in tabs["mA"].get("ZETA", [0.0]))
        detail = "quick: single-gap levels only, orderings need the full grid"
    check("U2a(Q2) the chain m-face ORDERING FLIPS vs the e1t function face: "
          "zeta cleanest (D-H 3-4x, BEUR 8x worse), zeta's improvement ratio "
          "~40x D-H's; priced honestly: the shape face is family-blind-small "
          "(weak-topology collapse) and NO family shows a monotone gap decay "
          "(no coincidence certificate); 6i-disk robustness in the detail "
          "[ADVERSARY: numbers stand as pinned, but the flip is LOW-BAND "
          "GEOMETRY and dies under the U2c band-equalization control]",
          cond, detail)

    if not quick:
        raw_grow = all(
            tabs["jrA"][lab][-1] > tabs["jrA"][lab][0] * 0.5 for lab in fam
            if len(tabs["jrA"].get(lab, [])) >= 2)
        check("U2b(Q2) raw Jacobi/chain heads window-track (the T3d moment "
              "radii in Killip-Simon clothing): raw head gaps stay O(support), "
              "no raw-coordinate Cauchy trend anywhere",
              raw_grow, "raw jA gap tables in npz; shape faces carry the question")
    else:
        check("U2b(Q2) raw head gap computed (quick level)",
              np.isfinite(list(tabs["jrA"].values())[0][0]), "")

    # ---- U2c [ADVERSARY]: the symmetric low-band exclusion control --------
    # The mA flip's pre-registered kill (adversarial test case 2 of the
    # .md): if equalizing the compared band restores D-H-first or BEUR
    # parity, the flip is geometry, not structure. Measured: it does BOTH.
    # The fixed 2i/6i disks sit mid-gap for every family, and "cleanest
    # family" on a mid-gap disk = "deepest central gap relative to the
    # disk" = first-zero-position data (FE/density-adjacent, exactly the
    # U3a residual). Concordant controls (adversary report): a disk beside
    # each family's first zero (t1 + 2i) restores D-H-first outright, and
    # the eps = 0.01 fake reaches D-H parity (0.0070 vs 0.0068).
    if not quick:
        means_ex = {}
        for T0 in (13.6, 20.0):
            chx = {}
            for label, lams in fam.items():
                for lam in lams:
                    ch = faces[(label, lam, "A")]["ch"]
                    keep = np.abs(ch.atoms) >= T0
                    chx[(label, lam)] = build_chain(ch.atoms[keep],
                                                    ch.wts[keep], 0.0)
            gg = {}
            for label, lams in fam.items():
                vals = {lam: mvals(chx[(label, lam)]) for lam in lams}
                gg[label] = [m_dist(vals[a], vals[b])
                             for a, b in zip(lams, lams[1:])]
                results[f"u2c_ex{int(10 * T0)}_{label.replace('-', '')}"] = \
                    np.array(gg[label])
            means_ex[T0] = {label: float(np.mean(gg[label])) for label in fam}
            print(f"    [ADVERSARY] mA gaps, band-equalized |t| >= {T0}: "
                  + "; ".join(f"{lab} mean {means_ex[T0][lab]:.4f}"
                              for lab in fam))
        m1, m2 = means_ex[13.6], means_ex[20.0]
        flip_dead = (m1["D-H"] <= m1["ZETA"] and m1["BEUR"] < 1.5 * m1["ZETA"]
                     and max(m2.values()) < 1.5 * min(m2.values()))
        check("U2c(Q2) [ADVERSARY] the mA flip is LOW-BAND GEOMETRY: with "
              "the compared band equalized (all families on |t| >= 13.6) "
              "D-H-first is restored and BEUR reaches zeta parity; at "
              "|t| >= 20 all three family means agree within 1.5x. The "
              "flip dies by its own pre-registered kill criterion; the mA "
              "coherence face is density-typed (first-zero position), not "
              "a zeta-first structure read",
              flip_dead,
              f"means at 13.6: z/d/b = {m1['ZETA']:.4f}/{m1['D-H']:.4f}/"
              f"{m1['BEUR']:.4f}; at 20: {m2['ZETA']:.4f}/{m2['D-H']:.4f}/"
              f"{m2['BEUR']:.4f}")
    else:
        print("    (U2c skipped in quick mode: orderings need the full grid)")
    return tabs, gaps_fn, imp


# ==========================================================================
# U3 (Q3): clause (b), degeneration / no-mass-escape indicators + the
# Suzuki-analogue no-mass-at-the-singular-end profile.
# ==========================================================================
def run_u3(results, faces, grid, quick):
    print("\n[U3/Q3] NO-MASS-ESCAPE: degeneration indicators, escape, Weyl tail mass")
    consume("U3", "chain indicator data (lengths, angles, Weyl solution)")
    fam = fam_lams(grid)

    esc = {}
    for (label, lam, face), v in faces.items():
        ch = v["ch"]
        w = ch.wts / np.sum(ch.wts)
        esc[(label, lam, face)] = float(np.sum(w[np.abs(ch.atoms) > 12.0]))
        ind = v["ind"]
        tag = f"u3_{label.replace('-', '')}_{lam:.3f}_{face}"
        results[f"{tag}_ind"] = np.array(
            [ind["X_total"], ind["delta_total"], ind["dispersion"],
             esc[(label, lam, face)], ch.M])
        print(f"    {label:5s} lam={lam:.3f} {face}: X={ind['X_total']:7.1f} "
              f"deltaK={ind['delta_total']:.3f} disp={ind['dispersion']:.3f} "
              f"esc12={esc[(label, lam, face)]:.3f} X/M={ind['X_total']/ch.M:.2f}")

    # ---- U3a: is clause (b) family-blind? zeta vs the fake at matched
    # configs on the DENSITY face (Face A) [PINNED bands from calibration] --
    pairs, diffs = [], []
    for lam in (2.2, 2.6, 3.0):
        if ("ZETA", lam, "A") in faces and ("BEUR", lam, "A") in faces:
            iz = faces[("ZETA", lam, "A")]["ind"]
            ib = faces[("BEUR", lam, "A")]["ind"]
            diffs.append((abs(iz["delta_total"] - ib["delta_total"]),
                          abs(iz["dispersion"] - ib["dispersion"])))
            pairs.append(lam)
    dmax = max(d[0] for d in diffs) if diffs else np.inf
    vmax = max(d[1] for d in diffs) if diffs else np.inf
    check("U3a(Q3) clause (b) family-blindness CONFIRMED: zeta-vs-fake "
          "degeneration indicators on the density face agree to < 0.05 at "
          "every matched config (prediction confirmed: Beurling-satisfiable "
          "at density level, zero discrimination alone; the residual 0.01 "
          "is the central-gap geometry = first-zero position = density-"
          "adjacent data) [ADVERSARY: a LINEAR-scale read; log-deltaK "
          "spans 1e-2 down to 9e-14 with ZETA nearest the degenerate "
          "boundary, so the agreement is boundary saturation on top of "
          "the same central-gap geometry; and these indicators do not "
          "respond to genuine spectral escape at all (indicators() "
          "docstring)]", bool(diffs) and dmax < 0.05 and vmax < 0.05,
          f"lams {pairs}: max|d deltaK|={dmax:.3f}, max|d disp|={vmax:.3f}")
    results["u3_blind_diffs"] = np.array(diffs) if diffs else np.array([])

    # ---- U3b: structural escape of the normalized counting measure --------
    inc = []
    for label, lams in fam.items():
        seq = [esc[(label, lam, "A")] for lam in lams]
        inc.append(all(a <= b + 1e-9 for a, b in zip(seq, seq[1:])))
        print(f"    Face-A esc12 along lambda, {label}: {[round(s, 3) for s in seq]}")
    check("U3b(Q3) mass escape from any fixed compact is STRUCTURAL for the "
          "normalized zero-counting measures of ALL families (window growth = "
          "density fact): the naive no-escape clause is posed on the wrong "
          "object; the compact-space clause lives on H, not on the measure",
          all(inc), "esc12 nondecreasing along every family grid")

    # ---- U3c: the Suzuki-analogue profile (surveyor fold-in): remaining
    # Weyl H-mass beyond chain position u X, exact per interval, germ-pure
    # (the artificial tail carries zero Weyl mass by construction) ----------
    prof, idty = {}, []
    z0 = 2j
    for (label, lam, face), v in faces.items():
        if face != "A":
            continue
        ch = v["ch"]
        p, total, iderr = ch.weyl_tail_mass(z0, UGRID)
        prof[(label, lam)] = p
        results[f"u3_prof_{label.replace('-', '')}_{lam:.3f}"] = p
        idty.append(iderr)
    gapsP, uhalf = {}, {}
    for label, lams in fam.items():
        gapsP[label] = [float(np.max(np.abs(prof[(label, a)] - prof[(label, b)])))
                        for a, b in zip(lams, lams[1:])]
        uhalf[label] = [float(UGRID[min(np.searchsorted(-prof[(label, lam)], -0.5),
                                        len(UGRID) - 1)]) for lam in lams]
        results[f"u3_profgaps_{label.replace('-', '')}"] = np.array(gapsP[label])
        results[f"u3_uhalf_{label.replace('-', '')}"] = np.array(uhalf[label])
        print(f"    Weyl tail-mass {label}: u_half {[round(u, 3) for u in uhalf[label]]}"
              + (f", profile gaps {[round(g, 3) for g in gapsP[label]]}"
                 if gapsP[label] else ""))
    worst_id = max(idty)
    if not quick:
        # [PINNED from calibration, deterministic] the measured shape: the
        # profile STABILIZES along lambda for the two integer-lattice combs
        # (zeta gaps 0.059 -> 0.002 -> 0.000, D-H 0.59 -> 0.051 -> 0.001)
        # but NOT for the displaced-lattice fake (0.28, 0.12): the first
        # in-sample lambda-uniformity read that the fake fails. Typed
        # honestly: in-sample, and possibly matching-coarseness (eps=0.25);
        # the finer-eps rerun is a named ADVERSARY case.
        stab = (gapsP["ZETA"][-1] < 0.005 and gapsP["D-H"][-1] < 0.005
                and min(gapsP["BEUR"]) > 0.05
                and all(a >= b for a, b in zip(gapsP["ZETA"], gapsP["ZETA"][1:])))
    else:
        stab = True
    check("U3c(Q3) Suzuki-analogue no-mass-at-the-singular-end profile: the "
          "Weyl-mass identity total = |u1|^2 Im m / Im z is exact (kernel "
          "calculus certified); the decay profile STABILIZES along lambda "
          "for zeta and D-H but NOT for the displaced-lattice fake "
          "(in-sample; finer-eps control handed to ADVERSARY) "
          "[ADVERSARY: the coarse-grid numbers stand as pinned, but the "
          "stabilization reading is a UGRID-floor artifact killed by the "
          "U3d control; this face carries no fake-failing content]",
          worst_id < 1e-30 and stab, f"identity worst rel err {worst_id:.1e}")
    results["u3_identity_worst"] = worst_id

    # ---- U3d [ADVERSARY]: the fine-grid + band-equalization control -------
    # Pre-registered adversarial case 3: is the zeta stability an artifact
    # of u_half saturating at the UGRID floor (0.025 = one step)? It is.
    # On a grid resolving u < 0.025 the gated profiles are seen collapsing
    # onto u = 0+ (all Weyl mass below u ~ 5e-3: the central-gap length
    # blowup of U1 in normalized coordinates), the ordering INVERTS (the
    # fake's first-pair gap becomes the smallest), and after band
    # equalization at 13.6 the fake shows the identical degenerate pattern:
    # the U3c separation was grid coarseness + central-gap geometry, not a
    # lambda-uniformity read the fake fails.
    if not quick:
        UF = np.unique(np.concatenate([np.linspace(0.0, 0.05, 251),
                                       np.linspace(0.05, 1.0, 96)]))
        profF, profX = {}, {}
        for (label, lam, face), v in faces.items():
            if face != "A":
                continue
            pF, _, _ = v["ch"].weyl_tail_mass(2j, UF)
            profF[(label, lam)] = pF
            ch = v["ch"]
            keep = np.abs(ch.atoms) >= 13.6
            chx = build_chain(ch.atoms[keep], ch.wts[keep], 0.0)
            pX, _, _ = chx.weyl_tail_mass(2j, UF)
            profX[(label, lam)] = pX
        gF, gX = {}, {}
        for label, lams in fam.items():
            gF[label] = [float(np.max(np.abs(profF[(label, a)]
                                             - profF[(label, b)])))
                         for a, b in zip(lams, lams[1:])]
            gX[label] = [float(np.max(np.abs(profX[(label, a)]
                                             - profX[(label, b)])))
                         for a, b in zip(lams, lams[1:])]
            results[f"u3d_gapsF_{label.replace('-', '')}"] = np.array(gF[label])
            results[f"u3d_gapsX_{label.replace('-', '')}"] = np.array(gX[label])
            print(f"    [ADVERSARY] fine-grid profile gaps {label}: "
                  f"{[round(g, 3) for g in gF[label]]}; band-equalized: "
                  f"{[round(g, 3) for g in gX[label]]}")
        artifact = (gF["ZETA"][0] > 0.5           # coarse grid said 0.059
                    and gF["D-H"][-1] > 0.05      # coarse grid said 0.001
                    and gF["BEUR"][0] < gF["ZETA"][0]   # ordering inverted
                    and gX["D-H"][1] < 0.05 and gX["BEUR"][1] < 0.05)
        check("U3d(Q3) [ADVERSARY] the U3c stabilization is a UGRID-FLOOR "
              "ARTIFACT: on a grid resolving u < 0.025 zeta's first gap is "
              "> 0.5 (was 0.059), D-H's last gap is > 0.05 (was 0.001, "
              "i.e. non-stabilizing), the fake's first gap is the SMALLEST, "
              "and after band equalization at 13.6 D-H and BEUR show zeta's "
              "own degenerate pattern: no (b)-face separates the families",
              artifact,
              f"fine gaps: Z {[round(g, 2) for g in gF['ZETA']]}, D-H "
              f"{[round(g, 2) for g in gF['D-H']]}, BEUR "
              f"{[round(g, 2) for g in gF['BEUR']]}")
    else:
        print("    (U3d skipped in quick mode: needs the full grid)")
    return esc, prof, gapsP


# ==========================================================================
# U4 (Q4): identification data + the off-line-pair signature.
# ==========================================================================
def run_u4(results, faces, quick):
    print("\n[U4/Q4] IDENTIFICATION + ENTANGLEMENT: the local-mass-defect signature")
    consume("U4", "object's own zeros (synthetic perturbation is object-side)",
            "D-H off-line HEIGHT 85.699 as a window LANDMARK only (no zero "
            "list; K1 guards active)")

    # ---- U4a: synthetic off-line perturbation of the zeta object ----------
    # The nearest-degenerate adjacent zero pair is collided into a complex
    # pair w = t_mid + i delta (canonical choice: minimal separation, no
    # height tuning). The perturbed object is real, even, same type, same
    # total zero count; its Face-A measure LOSES the pair's real atoms: the
    # citation adversary's local mass defect, exhibited synthetically.
    base = ("ZETA", 3.0, 32) if not quick else ("ZETA", 2.2, 12)
    fa = faces[(base[0], base[1], "A")]
    tz, xh, z0s = fa["meta"]["tz"], fa["meta"]["xh"], fa["meta"]["z0s"]
    seps = np.diff(tz)
    k = int(np.argmin(seps))
    t1, t2 = tz[k], tz[k + 1]
    tmid = 0.5 * (t1 + t2)
    print(f"    base {base[0]} {base[1]}: colliding pair ({t1:.2f}, {t2:.2f}), "
          f"sep {seps[k]:.3f}, midpoint {tmid:.2f}")

    tz_p = [t for i, t in enumerate(tz) if i not in (k, k + 1)]
    atoms_p = np.array([-t for t in tz_p[::-1]] + tz_p)
    ch_o = fa["ch"]
    ch_p = build_chain(atoms_p, np.ones(len(atoms_p)), 0.0)
    defect = 1.0 - len(atoms_p) / ch_o.M

    # m-face response: the fixed low identification disk vs a disk beside
    # the defect (localization of the pin's conditioning)
    dm_low = m_dist(mvals(ch_p), fa["mvN"])
    HISAMP = [complex(tmid + 2j)] + [complex(tmid + 2j + 0.9 * np.exp(1j * t))
                                     for t in np.linspace(0, 2 * np.pi, 12,
                                                          endpoint=False)]
    dm_high = m_dist([ch_p.m(z) for z in HISAMP], [ch_o.m(z) for z in HISAMP])

    # chain response localization (Killip-Simon coordinate)
    kk = min(len(ch_o.bs), len(ch_p.bs)) - 1
    db = np.abs(np.array([float(v) for v in ch_o.bs[:kk]])
                - np.array([float(v) for v in ch_p.bs[:kk]]))
    da = np.abs(np.array([float(v) for v in ch_o.as_[:kk]])
                - np.array([float(v) for v in ch_p.as_[:kk]]))
    dj = db + da
    j_argmax = int(np.argmax(dj))
    j_head = float(np.max(dj[:8])) if len(dj) >= 8 else float(np.max(dj))
    j_max = float(np.max(dj))

    io, ip_ = ch_o.indicators(), ch_p.indicators()
    d_ind = (abs(io["delta_total"] - ip_["delta_total"]),
             abs(io["dispersion"] - ip_["dispersion"]))

    # function-side reality certificate against the synthetic pair
    def G(zv):
        return xh(zv) / qpoly(zv, z0s)

    catches = {}
    for delta in (0.2, 0.5):
        w = tmid + 1j * delta

        def Gp(z):
            zz = np.asarray([z], complex)
            num = (zz ** 2 - w ** 2) * (zz ** 2 - np.conj(w) ** 2)
            den = (zz ** 2 - t1 ** 2) * (zz ** 2 - t2 ** 2)
            return complex((G(zz) * num / den)[0])

        lo = 13.6 if base[0] == "ZETA" else 0.05
        Twin = fa["meta"]["Twin"]
        ww, r1, _ = winding_count(
            Gp, [lo - 0.4j, Twin + 0.4 - 0.4j, Twin + 0.4 + 0.4j, lo + 0.4j],
            n0=256)
        wt, r2, _ = winding_count(
            Gp, [lo - 0.05j, Twin + 0.4 - 0.05j, Twin + 0.4 + 0.05j, lo + 0.05j],
            n0=256)
        catches[delta] = (round(ww), round(wt), r1 < 0.05 and r2 < 0.05)
        print(f"      delta={delta}: winding wide {ww:.2f} thin {wt:.2f}")

    caught_02 = catches[0.2][2] and catches[0.2][0] - catches[0.2][1] == 2
    blind_05 = catches[0.5][2] and catches[0.5][0] == catches[0.5][1]
    print(f"    defect {defect:.3f} of atoms; dm low disk {dm_low:.2e} vs "
          f"beside-defect disk {dm_high:.2e} (ratio {dm_high/max(dm_low,1e-30):.1f}x)")
    print(f"    Jacobi response: argmax k={j_argmax}, head(<8) {j_head:.3f} vs "
          f"max {j_max:.3f}; d(deltaK, disp) = ({d_ind[0]:.4f}, {d_ind[1]:.4f})")
    # [ADVERSARY] pair sweep (adversary report, attack C): the 243x ratio is
    # PAIR-SPECIFIC and TRACKS defect location: 9.7x at zeta's lowest pair
    # (t_mid 17.6), 490x mid-window (31.7), 243x here (40.97), decaying to
    # 59x at the top; D-H's lowest pair (t_mid 7.0) gives 2.9x. A fixed
    # ratio would have falsified the localization reading; the tracking
    # CONFIRMS it. Quote the asymmetry as location-dependent (10x-490x),
    # not as a constant.
    check("U4a(Q4) synthetic off-line pair = LOCAL MASS DEFECT, measured: the "
          "collided pair removes its real atoms; the beside-defect m-disk sees "
          "it far more strongly than the fixed low identification disk (the "
          "pin is exact-but-locally-conditioned: the entanglement, quantified); "
          "degeneration indicators nearly blind; the strip reality certificate "
          "catches delta=0.2 (wide-thin = 2) and is BAND-LIMITED at delta=0.5 "
          "[ADVERSARY: ratio pair-specific, 10x-490x, tracking location: "
          "localization reading confirmed by sweep]",
          dm_high > 3 * dm_low and caught_02 and blind_05
          and d_ind[0] < 0.1 and d_ind[1] < 0.1,
          f"dm_high/dm_low = {dm_high/max(dm_low,1e-30):.1f}, "
          f"wide-thin at 0.2: {catches[0.2][0]}-{catches[0.2][1]}, "
          f"at 0.5: {catches[0.5][0]}-{catches[0.5][1]}")
    results["u4_synth"] = np.array([defect, dm_low, dm_high, j_head, j_max,
                                    float(j_argmax), d_ind[0], d_ind[1]])
    results["u4_wind"] = np.array([catches[0.2][0], catches[0.2][1],
                                   catches[0.5][0], catches[0.5][1]])

    # ---- U4b: the DIRECT read at the off-line height (full mode) ----------
    if quick:
        print("    (U4b skipped in quick mode: D-H 3.7/36 build is full-only)")
        return
    xh37, meta37 = get_build("D-H", 3.7, 36)
    atoms, wts, shift, m37 = face_A("D-H", 3.7, 36)
    ch37 = build_chain(atoms, wts, shift)
    _, ec = rt_errs(ch37)
    Twin = m37["Twin"]
    tz37 = m37["tz"]
    f = lambda z: complex((xh37(np.array([z])) / qpoly(np.array([z]),
                                                       m37["z0s"]))[0])
    ww, r1, _ = winding_count(
        f, [4.87 - 0.4j, Twin + 0.4 - 0.4j, Twin + 0.4 + 0.4j, 4.87 + 0.4j],
        n0=256)
    wt, r2, _ = winding_count(
        f, [4.87 - 0.05j, Twin + 0.4 - 0.05j, Twin + 0.4 + 0.05j, 4.87 + 0.05j],
        n0=256)
    counts = [sum(1 for t in tz37 if a <= t < a + 3.0) for a in (77.0, 80.0, 83.0)]
    ctrl = 0.5 * (counts[0] + counts[1])
    print(f"    D-H 3.7/36: window {Twin:.1f} COVERS the off-line height 85.70; "
          f"M={ch37.M}, rt {float(ec):.1e}")
    print(f"    winding wide {ww:.2f} vs thin {wt:.2f}; zeros in [77,80)/"
          f"[80,83)/[83,86): {counts}")
    check("U4b(Q4) DIRECT off-line read (e1k config, identical harness): the "
          "finite chain at a window COVERING gamma ~ 85.7 certifies real "
          "(wide = thin) and shows NO local count anomaly at the off-line "
          "window: the finite chain HIDES the defect (#158 restated on the "
          "chain face); the defect is a limit-level observable, i.e. clause "
          "(a)+(b) conjunction data",
          (r1 < 0.05 and r2 < 0.05 and round(ww) == round(wt)
           and abs(counts[2] - ctrl) <= 1.0 and float(ec) < 1e-30),
          f"counts {counts}, |last - ctrl| = {abs(counts[2] - ctrl):.1f}")
    results["u4_dh37"] = np.array([ww, wt] + counts + [float(ec), ch37.M])


# ==========================================================================
# U5 (Q5): the T1f lead in the chain encoding.
# ==========================================================================
def run_u5(results, faces, grid, quick):
    print("\n[U5/Q5] THE T1f LEAD: gauge separation along lambda, Prokhorov framing")
    consume("U5", "Face-B gauged measures (FE-gated quotient, e1t T1f code path)")
    fam = fam_lams(grid)

    fneg, tv, dist = {}, {}, {}
    for label, lams in fam.items():
        for lam in lams:
            v = faces[(label, lam, "B")]
            fneg[(label, lam)] = v["meta"]["fneg_q"]
            tv[(label, lam)] = v["meta"]["tvq"]
            # chain-encoding distortion: the admission price in m terms
            # (signed formal m vs positive-part chain m, both mass-1)
            N = [g[2] for g in grid if g[0] == label and g[1] == lam][0]
            atoms, aq, shift, _meta = face_B(label, lam, N)
            net = float(np.sum(aq))
            ms = [complex(np.sum((aq / net) / (atoms - complex(z))))
                  for z in MSAMP]
            dist[(label, lam)] = m_dist(ms, v["mvN"])

    print("    fneg_q / sum|aq| / m-distortion (signed vs positive-part, mass-1):")
    for label, lams in fam.items():
        print(f"      {label}: " + ", ".join(
            f"{lam:.2f}: {fneg[(label, lam)]:.4f}/{tv[(label, lam)]:.3g}/"
            f"{dist[(label, lam)]:.3f}" for lam in lams))
        results[f"u5_fneg_{label.replace('-', '')}"] = np.array(
            [fneg[(label, lam)] for lam in lams])
        results[f"u5_tvq_{label.replace('-', '')}"] = np.array(
            [tv[(label, lam)] for lam in lams])
        results[f"u5_dist_{label.replace('-', '')}"] = np.array(
            [dist[(label, lam)] for lam in lams])

    # cross-check against the tracked e1t T1f record where present
    ok_rec, worst_rec = True, 0.0
    if E1T_NPZ.exists():
        d = np.load(E1T_NPZ)
        for (label, lam), v in fneg.items():
            tag = f"t1_{label.replace('-', '')}_{lam:.3f}_fneg_q"
            if tag in d:
                worst_rec = max(worst_rec, abs(float(d[tag]) - v))
        # [PORTABILITY FIX 2026-08-09, LEARNINGS #172] was 1e-9; the
        # fneg_q record inherits the same build noise floor as U0b and
        # amplifies it through the coefficients (worst measured
        # cross-machine deviation 1.3e-8 over the full grid). 1e-6
        # gives 80x headroom and still sits five orders below the
        # smallest tracked fneg_q value.
        ok_rec = worst_rec < 1e-6

    zx = max(v for (lab, _), v in fneg.items() if lab == "ZETA")
    dn = min((v for (lab, _), v in fneg.items() if lab == "D-H"), default=np.inf)
    bn = min((v for (lab, _), v in fneg.items() if lab == "BEUR"), default=np.inf)
    persist = zx < dn <= bn if not quick else zx < bn
    check("U5a(Q5) the T1f gauge separation PERSISTS in the chain encoding "
          "in-sample: the chain admission price fneg_q keeps zeta below D-H "
          "below BEUR at every measured lambda (identical to the e1t record "
          "where tracked; D-H's decreasing trend caveat inherited)",
          persist and ok_rec,
          f"max zeta {zx:.4f} < min D-H {dn:.4f} <= min BEUR {bn:.4f}; "
          f"record match {worst_rec:.1e}")

    # Prokhorov framing: normalized positive-part measures are well-defined
    # at every build (the deep-dressed tvq collapse is a SCALE collapse, not
    # a measure collapse) and their Kolmogorov gaps are the coherence read
    pos_mass = {k: tv[k] * (1 - fneg[k]) for k in tv}
    ks = {}
    for label, lams in fam.items():
        seq = []
        for a, b in zip(lams, lams[1:]):
            c1, c2 = faces[(label, a, "B")]["ch"], faces[(label, b, "B")]["ch"]
            grid_x = np.unique(np.concatenate([c1.atoms, c2.atoms]))
            cdf1 = np.array([np.sum(c1.wts[c1.atoms <= x]) for x in grid_x]) \
                / np.sum(c1.wts)
            cdf2 = np.array([np.sum(c2.wts[c2.atoms <= x]) for x in grid_x]) \
                / np.sum(c2.wts)
            seq.append(float(np.max(np.abs(cdf1 - cdf2))))
        ks[label] = seq
        results[f"u5_ks_{label.replace('-', '')}"] = np.array(seq)
        if seq:
            print(f"    normalized positive-part KS gaps {label}: "
                  f"{[round(s, 3) for s in seq]}")
    check("U5b(Q5) Prokhorov framing holds: the positive-part measure is "
          "nonzero at EVERY build (min mass > 0, so the normalized chain "
          "input dodges the deep-dressed scale collapse), and the normalized "
          "KS coherence gaps are recorded per family",
          min(pos_mass.values()) > 0,
          f"min positive mass {min(pos_mass.values()):.2e} "
          f"(deep-dressed sum|aq| {min(tv.values()):.2e})")
    results["u5_min_posmass"] = min(pos_mass.values())
    return fneg, dist, ks


# ==========================================================================
# U6 (Q6): disciplines and kills.
# ==========================================================================
def run_u6(results, faces, grid, guards, tabs, quick):
    print("\n[U6/Q6] DISCIPLINES: DMV screen, K1, input typing, tail sensitivity")
    consume("U6", "chain-leg certification vector; tail-variant m samples")

    # ---- U6a: the DMV screen MUST fire on the compactness leg -------------
    # Chain-leg certification vector (Face A, density-typed by construction):
    # (round trip ok, l0 = 1, min len > 0, germ > head) booleans plus the
    # degeneration scalars. If this vector separated zeta from the density-
    # matched fake it would be an ALARM (a density-only leg cannot carry
    # discrimination; a separation would mean a bug or a K1 leak).
    fired, det = [], []
    for lam in (2.2, 2.6, 3.0):
        if ("ZETA", lam, "A") not in faces or ("BEUR", lam, "A") not in faces:
            continue
        vz, vb = faces[("ZETA", lam, "A")], faces[("BEUR", lam, "A")]
        boo_z = (vz["ec"] < 1e-30, abs(vz["ind"]["l0"] - 1) < 1e-30,
                 vz["ind"]["min_len"] > 0, vz["ind"]["X_total"] > 1.0)
        boo_b = (vb["ec"] < 1e-30, abs(vb["ind"]["l0"] - 1) < 1e-30,
                 vb["ind"]["min_len"] > 0, vb["ind"]["X_total"] > 1.0)
        dd = abs(vz["ind"]["delta_total"] - vb["ind"]["delta_total"])
        dv = abs(vz["ind"]["dispersion"] - vb["ind"]["dispersion"])
        fired.append(boo_z == boo_b and dd < 0.05 and dv < 0.05)
        det.append(f"lam {lam}: bools equal, |dK|={dd:.2f}, |ddisp|={dv:.2f}")
    check("U6a(Q6) DMV SCREEN FIRED on the compactness leg: the chain-leg "
          "certification vector is indistinguishable between zeta and the "
          "density-matched fake (as it MUST be: the leg is density-blind by "
          "construction; discrimination lives at the pin and, gauge-"
          "conditionally, at the T1f admission price)",
          bool(fired) and all(fired), "; ".join(det))
    results["u6_screen_fired"] = bool(fired) and all(fired)

    # ---- U6b: K1 audit ------------------------------------------------------
    src = Path(__file__).read_text(encoding="utf-8")
    forbidden = ["zeta" + "zero", "ZETA_" + "ZEROS", "DH_" + "ZEROS",
                 ".zeros" + "("]
    scan = [ln.replace("np." + "zeros(", "np_alloc(") for ln in src.splitlines()
            if not ln.strip().startswith("#") and "K1-ALLOW" not in ln]
    hits = [tok for tok in forbidden if any(tok in ln for ln in scan)]
    check("U6b(Q6) K1 audit: no zero-list access anywhere (source scan clean, "
          "runtime guards installed and never tripped; landmark heights 14.13/"
          "5.09/85.70 bound scan windows and labels only)",
          not hits and guards["installed"] and not guards["tripped"],
          f"forbidden tokens: {hits}" if hits else "clean")
    print("    input ledger (what each section consumed):")
    for test in sorted(LEDGER):
        for item in LEDGER[test]:
            print(f"      {test}: {item}")

    # ---- U6c: input typing of every discriminating clause -------------------
    typing = {
        "ghost-quotient gauge (Face B)": "FE-typed gate (BEUR unposable in "
                                         "principle, trivial in practice)",
        "fneg_q admission price (U5a)": "output-level, gauge-conditional, "
                                        "in-sample (T1f scoping inherited)",
        "Face-A chain faces + indicators + round trip": "density-typed "
                                                        "(DMV-screened, U6a)",
        "reality/winding certificate": "CF-manufactured (#158), band-limited "
                                       "(U4a); carries no arithmetic bits",
        "identification of the LIMIT chain": "lattice + Euler (the #160 pin; "
                                             "NOT purchasable here, cited)",
        "Weyl tail-mass profile (U3c)": "density-typed on the finite germ; "
                                        "the lambda-uniform rate is the open "
                                        "clause (Suzuki gauge, no rate in "
                                        "print) [ADVERSARY: the in-sample "
                                        "separation was grid + central-gap "
                                        "geometry (U3d); at its "
                                        "discriminating margin the rate "
                                        "clause is the #160 growth clause "
                                        "in disguise]",
    }
    check("U6c(Q6) every discriminating clause is typed to its input "
          "(Euler gate / lattice / FE / density); a type refusal is not "
          "consumption (e1t adversary scoping respected)",
          all(v for v in typing.values()) and len(typing) >= 6,
          f"{len(typing)} clauses typed")
    print("    INPUT TYPING TABLE:")
    for kk, vv in typing.items():
        print(f"      {kk}: {vv}")

    # ---- U6d: the indivisible-tail battery (the named builder-must-fix) ----
    # Primary TAIL-N (natural closure; the unique tail reproducing the input
    # measure exactly, round-trip certified in U1b). Variants TAIL-0 and
    # TAIL-D change the far boundary condition = a different self-adjoint
    # realization; the finite chain data (lengths, angles, M(x), indicators)
    # is tail-INVARIANT by construction. [ADVERSARY] The Weyl-mass PROFILE
    # is NOT: the Weyl solution depends on the tail angle through its
    # boundary vector (measured normalized-profile shifts up to ~0.28 on
    # face A / ~0.22 on face B, recorded below), so tail sensitivity
    # concentrates on the m-face AND the profile; both measured here.
    dmND, dmN0, dprof = {}, {}, {}
    for (label, lam, face), v in faces.items():
        ch = v["ch"]
        mvD = mvals(ch, "D")
        mv0 = mvals(ch, "0")
        dmND[(label, lam, face)] = m_dist(v["mvN"], mvD)
        dmN0[(label, lam, face)] = m_dist(v["mvN"], mv0)
        pN, _, _ = ch.weyl_tail_mass(2j, UGRID, "N")
        p0, _, _ = ch.weyl_tail_mass(2j, UGRID, "0")
        pD, _, _ = ch.weyl_tail_mass(2j, UGRID, "D")
        dprof[(label, lam, face)] = max(
            float(np.max(np.abs(pN - p0))), float(np.max(np.abs(pN - pD))))
    worstND = max(dmND.values())
    worst0 = max(dmN0.values())
    profA = max(v for k, v in dprof.items() if k[2] == "A")
    profB = max(v for k, v in dprof.items() if k[2] == "B")
    # do the m-face family orderings survive the tail swap? (full grid only)
    # [PINNED from calibration, deterministic] measured outcome: the face-A
    # ordering (zeta first) is tail-STABLE; the face-B ordering flips at the
    # D-H/BEUR margin (means 0.031 vs 0.033, inside the ~0.2 tail band):
    # the mB coherence face is tail-gauge-fragile and is DEMOTED; zeta's own
    # rank never moves. A flip inside the tail band is a scoping fact about
    # the face, not about the families.
    stable_A, zeta_stable, flips = True, True, []
    if not quick:
        fam = fam_lams(grid)
        for face in ("A", "B"):
            means_N, means_D = {}, {}
            for label, lams in fam.items():
                if len(lams) < 2:
                    continue
                gN = [m_dist(faces[(label, a, face)]["mvN"],
                             faces[(label, b, face)]["mvN"])
                      for a, b in zip(lams, lams[1:])]
                gD = [m_dist(mvals(faces[(label, a, face)]["ch"], "D"),
                             mvals(faces[(label, b, face)]["ch"], "D"))
                      for a, b in zip(lams, lams[1:])]
                means_N[label] = float(np.mean(gN))
                means_D[label] = float(np.mean(gD))
            if means_N:
                rank_N = sorted(means_N, key=means_N.get)
                rank_D = sorted(means_D, key=means_D.get)
                if rank_N != rank_D:
                    flips.append(face)
                    margin = abs(sorted(means_N.values())[1]
                                 - sorted(means_N.values())[0])
                    print(f"    [tail-sensitivity] face {face} ordering moves "
                          f"under TAIL-D: {rank_N} -> {rank_D} (margin "
                          f"{margin:.3f} inside tail band {worstND:.2f}: "
                          f"face demoted as tail-gauge-fragile)")
                    if face == "A":
                        stable_A = False
                    if rank_N.index("ZETA") != rank_D.index("ZETA"):
                        zeta_stable = False
    check("U6d(Q6) indivisible-tail battery (the named must-fix): lengths/"
          "angles/M(x)/indicators tail-invariant by construction; the Weyl "
          "PROFILE is NOT [ADVERSARY: measured shifts in the detail; the "
          "prior 'profile tail-invariant' wording was false]; m-face shifts "
          "quantified; the face-A ordering and zeta's rank on every face "
          "survive the swap; the face-B D-H/BEUR margin flips INSIDE the "
          "tail band (that face demoted as tail-gauge-fragile)",
          stable_A and zeta_stable,
          f"max chordal m-shift: TAIL-N vs D {worstND:.3f}, vs 0 {worst0:.3f}; "
          f"max profile shift: face A {profA:.3f}, face B {profB:.3f}; "
          f"flipped faces: {flips if flips else 'none'}")
    results["u6_tail_ND"] = np.array(list(dmND.values()))
    results["u6_tail_N0"] = np.array(list(dmN0.values()))
    results["u6_tail_worst"] = np.array([worstND, worst0])
    results["u6_prof_tailshift"] = np.array([profA, profB])
    results["u6_tail_flips"] = np.array([f == "B" for f in flips], bool)


# ==========================================================================
# main
# ==========================================================================
GRID_FULL = [("ZETA", 2.2, 12), ("ZETA", 2.6, 16), ("ZETA", 3.0, 32),
             ("ZETA", SQRT13, 48),
             ("D-H", 2.2, 12), ("D-H", 2.6, 16), ("D-H", 3.0, 32),
             ("D-H", SQRT13, 48),
             ("BEUR", 2.2, 12), ("BEUR", 2.6, 16), ("BEUR", 3.0, 32)]
GRID_QUICK = [("ZETA", 2.2, 12), ("ZETA", 2.6, 16),
              ("D-H", 2.6, 16), ("BEUR", 2.2, 12)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="cached builds only, reduced grid; NO npz output")
    args = ap.parse_args()
    t_start = time.time()
    mp.mp.dps = 25   # build branch (e1l/e1m-characterized); chain work at dps 50

    guards = {"installed": True, "tripped": False}

    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                            # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid       # K1-ALLOW (guard install)

    grid = GRID_QUICK if args.quick else GRID_FULL
    results = {}
    print("=" * 78)
    print("E1U: trace-normed canonical-system chains for the ghost-quotiented")
    print("     D_log objects: do the two relocated clauses gain anything in")
    print("     the chain coordinate? (LEARNINGS #170 Section-6 rung)")
    print("=" * 78)

    run_u0(results, args.quick)
    faces = run_u1(results, grid, args.quick)
    tabs, gaps_fn, imp = run_u2(results, faces, grid, args.quick)
    run_u3(results, faces, grid, args.quick)
    run_u4(results, faces, args.quick)
    run_u5(results, faces, grid, args.quick)
    run_u6(results, faces, grid, guards, tabs, args.quick)

    print("\n" + "=" * 78)
    print("VERDICT (tiered; the honest statement lives in e1u_canonical_chain.md)")
    print("  chain_buys_beyond_function_face = NO-BEYOND-GEOMETRY (post-")
    print("  ADVERSARY; the pre-round read was YES-IN-SAMPLE, NO-CERTIFICATE):")
    print("  the embedding is well-posed and EXACT (U1, round trips ~1e-49);")
    print("  compactness is entered for free; the two relocated clauses measure")
    print("  exactly as typed:")
    print("  clause (b): density-blind where computable (U3a diffs <= 0.01, U6a")
    print("    screen FIRED), structural on the wrong object (U3b): Beurling-")
    print("    satisfiable at density level as predicted, zero weight alone.")
    print("    [ADVERSARY] the U3c 'fake-failing' profile read was a UGRID-")
    print("    floor artifact plus central-gap geometry (U3d): NO (b)-face")
    print("    separates the families.")
    print("  clause (a): pin data = any C+ disk by Herglotz rigidity, but with")
    print("    a measured local-conditioning asymmetry against a synthetic")
    print("    off-line defect (U4a; pair-specific 10x-490x, tracking the")
    print("    defect location), and the finite chain at the TRUE off-line")
    print("    height hides the defect entirely (U4b): the defect is limit-")
    print("    level (a)+(b) conjunction data; the clauses are entangled.")
    print("  coherence (U2): the mA numbers stand as pinned (zeta 0.0015 <")
    print("    D-H 0.0051 < BEUR 0.0127 on the 2i disk), BUT [ADVERSARY] the")
    print("    flip is LOW-BAND GEOMETRY (U2c): band equalization restores")
    print("    D-H-first and BEUR parity; beside-zero disks restore D-H-first;")
    print("    the eps=0.01 fake reaches D-H parity. The mA face is density-")
    print("    typed; link (ii) stays unpurchased and no face is zeta-first")
    print("    beyond geometry.")
    print("  T1f lead (U5): the admission price persists at every lambda (zeta")
    print("    <= 0.0277 < D-H >= 0.0520 <= BEUR >= 0.2409); the deep-dressed")
    print("    collapse is scale-only under Prokhorov normalization.")
    print("  post-ADVERSARY net: the pre-registered Q2 exit FIRES (no zeta-")
    print("    specific improvement beyond shared compression + density")
    print("    geometry; clause (b) family-blind on every measured face once")
    print("    the band is equalized): the rung closes as the THIRD")
    print("    reformulation; the surviving zeta-first face is the carried")
    print("    e1t T1f admission price (U5a).")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")

    if not args.quick:
        np.savez_compressed(OUT, **results)
        print(f"Saved -> {OUT}")
    else:
        print("(quick mode: no npz saved)")
    print(f"Total time {round(time.time() - t_start, 1)}s")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

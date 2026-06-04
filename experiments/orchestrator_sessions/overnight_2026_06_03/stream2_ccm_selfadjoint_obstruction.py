"""STREAM 2 BUILD (overnight 2026-06-03, STAGED, NOT COMMITTED).

2CCM.1 -- The self-adjointness obstruction of the CCM "zeta spectral triple" determinant.

Turns the survey's "more tractable" route into a concrete, runnable spec. The survey
recommended: compute the regularized determinant of the Connes-Consani-Moscovici
"zeta spectral triple" operator (arXiv:2511.22755, 27 Nov 2025), test "det -> Xi" for
zeta and apply the D-H control. CCM's own headline is: "A rigorous proof of this
convergence would establish the Riemann Hypothesis."

THE NEW COORDINATE (vs LEARNINGS #40-#44). The previous determinant findings were:
  #44 (2PR.1): a regularized det is a CLASS FUNCTION of the eigenvalue MULTISET, hence
               BLIND to the signature -- three unrelated {-n}-spectrum operators give the
               same det. ("blind to the signature.")
  #43 (2DB.1): the de Branges pairing SEES the zeros but with the wrong (strictly-
               stronger-than-RH, pointwise) positivity.
  #40-#42:     the AHK/q-lift mixed-volume form has no slot for the Frobenius trace t.

This experiment SHARPENS #44 with the mechanism #44 did not name: WHY "det -> Xi" is
RH-equivalent rather than RH-reducing. The reason is SELF-ADJOINTNESS, not merely the
class-function property. CCM build H_{N,lambda} SELF-ADJOINT (a rank-one real-symmetric
perturbation of the scaling operator). For a self-adjoint H:
    spectrum(H) is REAL.
If the determinant det_reg(s - H) is to vanish at the zeta zeros s = 1/2 + i*gamma, then
writing H = 1/2 + i*A forces A to be self-adjoint with REAL spectrum {gamma}, so EVERY
zero has Re(s) = 1/2 AUTOMATICALLY. That is the Hilbert-Polya tautology: "det -> Xi for a
self-adjoint H" IS RH, because a self-adjoint operator cannot manufacture an off-line zero.
So CCM's determinant does not REDUCE RH to a convergence; the convergence carries RH because
the operator's self-adjointness has already imposed the signature (the reality = the
polarization). This is the R3.5 "no shortcut" pattern made precise on the 2025 frontier
object, and it is the determinant-side mirror of #43 (de Branges: the pairing that sees the
zeros has the wrong positivity; here: the determinant that sees the zeros has the RH-built-in
positivity, i.e. self-adjointness).

THE D-H CONTROL (clean K2, categorical). An off-line D-H zero at rho = 0.8085 + 85.699i
CANNOT be of the form 1/2 + i*(real). It would require an eigenvalue 85.699 - 0.3085i of A,
which is NOT real: A would have to be NON-self-adjoint. Two independent obstructions stack:
  (K2-a) STRUCTURAL/CATEGORICAL: the CCM construction "only involves the Euler products over
         primes" (their abstract). D-H has NO Euler product, so there is no orbit-length
         spectrum {log p}, so the operator H is UNBUILDABLE for D-H. (Reproduces #41/#20.)
  (K2-b) SPECTRAL: even if one force-fed D-H's coefficients into the template, a self-adjoint
         H provably cannot have an off-line zero in its determinant. To reach D-H's off-line
         zero the generator must be non-self-adjoint (a dissipative/Pollicott-Ruelle resonance,
         NOT a quantum Hamiltonian). So the off-line zero is a SIGNATURE (self-adjointness)
         failure, not a trace failure.

WHAT THIS LOCALIZES THAT #40-#44 DID NOT. The Spec(Z) gap is now phrased as: the missing
Weil cohomology must produce a SELF-ADJOINT (equiv. positively-polarized) global generator
WITHOUT assuming RH. CCM supply a self-adjoint H by numerical fiat (rank-one fit to the low
zeros) and then ask whether its determinant converges to Xi. The non-circular content -- a
PROOF that the natural global generator is self-adjoint -- is exactly the arithmetic Rosati
positivity (08A M4). The signature IS the self-adjointness. This is "all roads to the
signature" (#30) read on the determinant: every realization of zeta as det(s-H) is RH-
equivalent precisely at the point where it asserts H is self-adjoint, and that assertion is
the polarization, never a corollary of the trace.

WHAT IS COMPUTED HERE (all numbers from code in this file, dps as noted):
  PART 1. Finite self-adjoint model. Build random self-adjoint A (n x n), set H = 1/2 + iA.
          Confirm the zeros of det(sI - H) all sit on Re(s) = 1/2 to machine precision, for
          many random draws. (The Hilbert-Polya tautology, made executable.)
  PART 2. The off-line impossibility. Show that to place a zero at 0.8085 + 85.699i the
          required A-eigenvalue is 85.699 - 0.3085i (NOT real); quantify how far a self-
          adjoint A's spectrum must be perturbed (the minimal non-self-adjoint part) to reach
          it. The minimal ||A - A^*|| needed is 2*|Re(rho) - 1/2| = 0.617 per off-line zero.
  PART 3. The CCM truncated-prime determinant (zeta side, reproduces the route's premise).
          Build the partial Euler-product / orbit-length data {log p : p <= x} that CCM use,
          form the resolvent-style sum, and show the prime side oscillates and does NOT
          converge on the critical line (the continuation gap, reproduces #42), so the
          convergence to Xi is genuinely the open content -- and PART 1/2 say that content,
          IF it held for a self-adjoint H, would BE RH.
  PART 4. D-H control. (a) reproduce the off-line zero rho ~ 0.8085 + 85.699i; (b) confirm
          D-H's von Mangoldt coefficients delocalize off prime powers (no Euler product =>
          CCM operator unbuildable); (c) state the categorical K2.

HONEST SCOPE (read before believing anything):
  - PROVED-IN-THIS-FILE: the finite self-adjoint tautology (PART 1, a linear-algebra fact),
    the off-line-eigenvalue arithmetic (PART 2), the prime-side oscillation (PART 3, the
    classical Re(s)>1 convergence fact), the D-H off-line zero + delocalization (PART 4,
    reproduces #20/#41/#43).
  - CITED (NOT verified against the CCM internals beyond the abstract): that CCM's H is
    self-adjoint and that their det -> Xi. The arXiv:2511.22755 abstract states H is a self-
    adjoint rank-one perturbation and that det_reg -> Xi with "a rigorous proof ... would
    establish RH." The self-adjointness claim is the load-bearing import; if the actual CCM
    operator is NOT self-adjoint (e.g. a Pollicott-Ruelle transfer operator), this coordinate
    WEAKENS to #44 and must be re-stated. FLAG FOR VERIFIER: confirm self-adjointness in the
    paper.
  - STRUCTURAL READING (mine): "det -> Xi for self-adjoint H = RH because self-adjoint =>
    real spectrum => on-line zeros" is the Hilbert-Polya tautology; pinning CCM's 2025 claim
    to it is a reading, not a theorem about their paper. It does NOT prove or disprove their
    convergence; it explains why that convergence cannot be a shortcut.
  - This is a NEGATIVE/no-shortcut coordinate. It does NOT construct the Weil cohomology, does
    NOT prove RH, does NOT advance M3/M4. It sharpens #44 (det blind to signature) into
    #44+ (det's self-adjointness IS the signature, so det->Xi is RH not a reduction) and gives
    a categorical-plus-spectral K2 reading of the newest frontier construction.

FALSIFIABLE PREDICTION. If a VERIFIER reads arXiv:2511.22755 and finds H is self-adjoint
(as the abstract says), then: (i) any honest "det -> Xi" proof is necessarily RH-equivalent
(no shortcut), and (ii) the D-H analogue is UNBUILDABLE (no Euler product) AND would be
spectrally forbidden (self-adjoint H cannot have an off-line determinant zero). If instead H
is found to be NON-self-adjoint, the coordinate is FALSIFIED and reduces to #44.

Run:  python -m experiments.orchestrator_sessions.overnight_2026_06_03.stream2_ccm_selfadjoint_obstruction
  (or copy to experiments/arithmetic_geometric/ as e2ccm_selfadjoint.py if promoted.)
"""

from __future__ import annotations

import numpy as np
import numpy.linalg as la
import mpmath as mp

try:
    from experiments._shared.davenport_heilbronn import davenport_heilbronn as DH
    _HAVE_DH = True
except Exception:  # pragma: no cover -- allow standalone run without the package on path
    _HAVE_DH = False

DH_OFFLINE_GUESS = mp.mpc("0.8085", "85.699")


# ----------------------------------------------------------------------------- PART 1
def part1_selfadjoint_tautology(n=8, draws=200, seed=0):
    """Self-adjoint A => H = 1/2 + iA has det(sI-H) vanishing ONLY on Re(s)=1/2.

    This is the Hilbert-Polya tautology as executable linear algebra: the zeros of the
    characteristic polynomial are s = 1/2 + i*lambda_k(A), and lambda_k(A) is real because
    A = A^*. So no random self-adjoint draw EVER produces an off-line zero.
    """
    print("=" * 78)
    print("PART 1. Self-adjoint tautology: H = 1/2 + iA (A=A^*) => all det zeros on Re(s)=1/2")
    print("=" * 78)
    rng = np.random.default_rng(seed)
    worst_offline = 0.0
    max_imag_eig = 0.0
    for _ in range(draws):
        B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        A = (B + B.conj().T) / 2  # self-adjoint
        eig_A = la.eigvals(A)
        max_imag_eig = max(max_imag_eig, float(np.max(np.abs(eig_A.imag))))
        # zeros of det(sI - H): s = 1/2 + i*lambda(A)
        zeros_s = 0.5 + 1j * eig_A
        offline = float(np.max(np.abs(zeros_s.real - 0.5)))
        worst_offline = max(worst_offline, offline)
    print(f"  {draws} random self-adjoint A ({n}x{n}); H = 1/2 + iA:")
    print(f"    max |Im(eig A)|            = {max_imag_eig:.3e}  (A self-adjoint => spectrum real)")
    print(f"    max |Re(zero of det) - 1/2| = {worst_offline:.3e}  (ALL zeros on the critical line)")
    print("  => 'det(s-H) -> Xi for a self-adjoint H' FORCES every zero onto Re(s)=1/2: this IS RH.")
    print("     The convergence cannot be a shortcut; self-adjointness has already imposed RH.\n")
    return dict(max_imag_eig=max_imag_eig, worst_offline=worst_offline)


# ----------------------------------------------------------------------------- PART 2
def part2_offline_impossibility(rho=DH_OFFLINE_GUESS):
    """To place a det-zero at an OFF-line rho, the generator A must be NON-self-adjoint.

    Required eigenvalue of A so that 1/2 + i*lambda = rho is lambda = (rho - 1/2)/i = -i(rho-1/2).
    Its imaginary part is -(Re(rho) - 1/2) != 0 for an off-line zero, so lambda is non-real and
    A cannot be self-adjoint. The minimal non-self-adjoint part ||A - A^*||_op needed to host one
    such eigenvalue is 2|Im(lambda)| = 2|Re(rho) - 1/2|.
    """
    print("=" * 78)
    print("PART 2. Off-line impossibility: an off-line zero forces a NON-self-adjoint generator")
    print("=" * 78)
    re_rho = float(mp.re(rho))
    im_rho = float(mp.im(rho))
    lam = (rho - mp.mpf("0.5")) / 1j  # lambda with 1/2 + i*lambda = rho
    lam_re, lam_im = float(mp.re(lam)), float(mp.im(lam))
    min_nonsa = 2 * abs(re_rho - 0.5)
    print(f"  target off-line zero rho = {re_rho:.4f} + {im_rho:.4f}i  (Re - 1/2 = {re_rho - 0.5:+.4f})")
    print(f"  required A-eigenvalue lambda = -i(rho - 1/2) = {lam_re:.4f} + {lam_im:.4f}i")
    print(f"    Im(lambda) = {lam_im:+.4f} != 0  =>  lambda NON-REAL  =>  A NOT self-adjoint.")
    print(f"  minimal ||A - A^*|| (anti-self-adjoint part) to host this eigenvalue = 2|Re(rho)-1/2| = {min_nonsa:.4f}")
    print("  => the off-line zero is a SIGNATURE (self-adjointness) failure, not a trace failure.")
    print("     A genuine D-H realization needs a dissipative/Pollicott-Ruelle generator, NOT a")
    print("     quantum Hamiltonian. The CCM self-adjoint H cannot host it.\n")
    return dict(lam_re=lam_re, lam_im=lam_im, min_nonsa=min_nonsa)


# ----------------------------------------------------------------------------- PART 3
def _primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def part3_prime_side_oscillation(t=14.134725, cutoffs=(50, 200, 1000, 5000, 20000)):
    """The CCM operator uses ONLY Euler products over p <= x: the orbit-length data {log p}.

    On the critical line the associated prime side (the oscillatory explicit-formula term)
    does NOT converge as x -> infinity (sum_p p^{-1/2} diverges); the zeros live in the
    analytic continuation. So 'det -> Xi' is genuinely the open content (reproduces #42).
    Combined with PART 1/2: that open content, for a self-adjoint H, would BE RH.
    """
    print("=" * 78)
    print("PART 3. CCM prime data {log p : p<=x} oscillates on the critical line (continuation gap)")
    print("=" * 78)
    mp.mp.dps = 30
    vals = []
    for x in cutoffs:
        primes = _primes_up_to(int(x))
        total = mp.mpf(0)
        for p in primes:
            pk, k = p, 1
            while pk <= x:
                total += mp.log(p) * mp.cos(t * mp.log(pk)) / mp.sqrt(pk)
                k += 1
                pk = p ** k
        vals.append(float(total))
    print(f"  oscillatory prime side sum_{{p^k<=x}} (log p) cos(t log p^k)/p^(k/2), t={t}:")
    for x, v in zip(cutoffs, vals):
        print(f"    x={x:>6}:  {v:+.4f}")
    print("  => no limit (oscillates): the zeros are in the continuation, invisible to the local")
    print("     prime data. CCM's det->Xi convergence is the open content; by PART 1/2 it = RH.\n")
    return dict(cutoffs=list(cutoffs), vals=vals)


# ----------------------------------------------------------------------------- PART 4
def part5_krein_signature(n=8, draws=200, seed=1):
    """The punchline: self-adjointness is DEFINITENESS of the metric = the polarization.

    A J-self-adjoint operator (A^* J = J A) for an INDEFINITE metric J can have a COMPLEX
    spectrum. So 'det -> Xi' forces RH only because the CCM metric is POSITIVE-DEFINITE (a
    genuine Hilbert space). Replace J = I (definite) by an indefinite diagonal J = diag(+1,..,-1)
    and the same construction H = 1/2 + iA, A J-self-adjoint, NOW produces OFF-LINE zeros. This
    is the executable form of 'the signature is the polarization' (08A M4): the off-line zeros
    appear exactly when the metric loses definiteness. RH = the metric is definite = self-adjoint
    in a true Hilbert space, NOT J-self-adjoint in a Krein space.
    """
    print("=" * 78)
    print("PART 5. The signature = metric definiteness: J-self-adjoint (indefinite J) => off-line")
    print("=" * 78)
    rng = np.random.default_rng(seed)
    # indefinite metric: half +1, half -1 on the diagonal
    sig = np.array([1.0] * (n // 2) + [-1.0] * (n - n // 2))
    J = np.diag(sig)
    worst_offline_def = 0.0     # definite metric (J=I): control
    worst_offline_indef = 0.0   # indefinite metric: off-line appears
    frac_complex = 0.0
    for _ in range(draws):
        # Build A that is J-self-adjoint: A = J^{-1} S with S Hermitian => J A = S = (J A)^* = A^* J.
        B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        S = (B + B.conj().T) / 2  # Hermitian
        # definite control (J=I): A = S is genuinely self-adjoint -> real spectrum
        eig_def = la.eigvals(S)
        worst_offline_def = max(worst_offline_def, float(np.max(np.abs((0.5 + 1j * eig_def).real - 0.5))))
        # indefinite: A = J^{-1} S = J S (since J^2=I) is J-self-adjoint, generally NON-real spectrum
        A = J @ S
        eig_indef = la.eigvals(A)
        # zeros at 1/2 + i*lambda; off-line iff lambda has nonzero imaginary part
        offln = float(np.max(np.abs((0.5 + 1j * eig_indef).real - 0.5)))
        worst_offline_indef = max(worst_offline_indef, offln)
        frac_complex += float(np.mean(np.abs(eig_indef.imag) > 1e-6)) / draws
    print(f"  {draws} draws, n={n}, indefinite metric J = diag({'+1 '*(n//2)}{'-1 '*(n-n//2)}):")
    print(f"    DEFINITE   metric (J=I): max |Re(zero)-1/2| = {worst_offline_def:.3e}  (on-line, control)")
    print(f"    INDEFINITE metric:       max |Re(zero)-1/2| = {worst_offline_indef:.3e}  (OFF the line)")
    print(f"    fraction of eigenvalues that go complex (indefinite) = {frac_complex:.2%}")
    print("  => off-line zeros appear EXACTLY when the metric loses definiteness. So 'det->Xi for a")
    print("     self-adjoint H' = RH is carried by the DEFINITENESS of the metric = the POLARIZATION")
    print("     (08A M4 / arithmetic Rosati positivity). The signature is the metric, not the trace.")
    print("     This is the determinant-side statement of #30 ('all roads to the signature').\n")
    return dict(worst_offline_def=worst_offline_def,
                worst_offline_indef=worst_offline_indef,
                frac_complex=frac_complex)


def part4_dh_control(refine=True):
    """D-H control: (a) the off-line zero; (b) von Mangoldt delocalization (no Euler product);
    (c) the categorical K2 + the spectral K2."""
    print("=" * 78)
    print("PART 4. D-H control (K2): off-line zero + no Euler product => CCM operator unbuildable")
    print("=" * 78)
    if not _HAVE_DH:
        print("  (D-H package not importable in standalone mode; run via -m from repo root.)\n")
        return dict(available=False)
    mp.mp.dps = 40
    out = dict(available=True)
    if refine:
        rho = mp.findroot(DH.evaluate, DH_OFFLINE_GUESS)
        out["rho"] = (float(mp.re(rho)), float(mp.im(rho)))
        print(f"  (a) D-H off-line zero refined: {mp.nstr(rho, 10)}   |f(rho)| = {mp.nstr(abs(DH.evaluate(rho)),3)}")
        print(f"      Re(rho) - 1/2 = {float(mp.re(rho) - 0.5):+.4f}  (off the critical line; RH FALSE for D-H)")
    # (b) von Mangoldt delocalization
    N = 30
    a = [mp.mpc(0)] * (N + 1)
    for n in range(1, N + 1):
        a[n] = mp.mpc(DH.dirichlet_coefficient(n))
    Lam = [mp.mpc(0)] * (N + 1)
    for n in range(2, N + 1):
        s = a[n] * mp.log(n)
        for d in range(2, n):
            if n % d == 0:
                s -= Lam[d] * a[n // d]
        Lam[n] = s / a[1]

    def is_pp(m):
        for p in _primes_up_to(m):
            k = p
            while k <= m:
                if k == m:
                    return True
                k *= p
        return False

    leaks = [(n, float(abs(Lam[n]))) for n in range(2, N + 1) if not is_pp(n) and float(abs(Lam[n])) > 1e-9]
    out["leaks"] = leaks
    print(f"  (b) D-H von Mangoldt leaks OFF prime powers (first 5): "
          f"{[(n, round(v,3)) for n,v in leaks[:5]]}")
    print("      => NO Euler product => no orbit-length spectrum {log p} => CCM operator UNBUILDABLE.")
    print("  (c) K2 verdict (two stacked obstructions):")
    print("      K2-a CATEGORICAL: D-H has no Euler product, so there is no CCM operator at all.")
    print("      K2-b SPECTRAL:    even force-fed, a self-adjoint H cannot host D-H's off-line zero")
    print("                        (PART 2: needs Im(lambda)=0.3085 != 0). The off-line zero is a")
    print("                        self-adjointness (signature) failure, not a trace failure.\n")
    return out


# ----------------------------------------------------------------------------- driver
def run():
    print("\n2CCM.1 -- the self-adjointness obstruction of the CCM zeta-spectral-triple determinant")
    print("STAGED overnight 2026-06-03; sharpens #44 (det blind to signature) -> det's self-adjointness")
    print("IS the signature, so 'det -> Xi' is RH-equivalent (no shortcut), with a categorical K2.\n")

    p1 = part1_selfadjoint_tautology()
    p2 = part2_offline_impossibility()
    p5 = part5_krein_signature()
    p3 = part3_prime_side_oscillation()
    p4 = part4_dh_control()

    # ---- assertions on the in-file numbers ----
    assert p1["worst_offline"] < 1e-9, "self-adjoint H must give all-on-line zeros"
    assert p1["max_imag_eig"] < 1e-9, "self-adjoint A must have real spectrum"
    assert abs(p2["lam_im"] - (-(0.8085 - 0.5))) < 1e-6, "off-line eigenvalue imaginary part wrong"
    assert abs(p2["min_nonsa"] - 2 * 0.3085) < 1e-3, "minimal non-self-adjoint part wrong"
    assert p5["worst_offline_def"] < 1e-9, "definite-metric control must stay on-line"
    assert p5["worst_offline_indef"] > 1e-3, "indefinite metric must produce off-line zeros"
    # prime side does NOT converge: spread across cutoffs is large relative to the values
    spread = max(p3["vals"]) - min(p3["vals"])
    assert spread > 1.0, "prime side should oscillate (no convergence) on the critical line"
    if p4.get("available"):
        assert abs(p4["rho"][0] - 0.5) > 0.1, "D-H off-line zero must be off the line"
        assert len(p4["leaks"]) >= 3, "D-H von Mangoldt must delocalize off prime powers"
    print("=" * 78)
    print("All in-file assertions PASS. (Numbers above are from THIS code; VERIFIER must re-derive.)")
    print("=" * 78)
    print("\nVERIFIER TARGETS:")
    print("  V1. Read arXiv:2511.22755 and CONFIRM H_{N,lambda} is self-adjoint (load-bearing).")
    print("      If non-self-adjoint, this coordinate FALSIFIES to #44.")
    print("  V2. (Lean) Formalize: A=A^* => spectrum(A) subset R => zeros of det(s-(1/2+iA)) have")
    print("      Re(s)=1/2 (the finite Hilbert-Polya tautology, PART 1).")
    print("  V3. State 'det -> Xi for a self-adjoint H => RH' as the no-shortcut lemma (R3.5 family).")
    print("\nADVERSARY TESTS:")
    print("  A1. Is CCM's rank-one perturbation genuinely self-adjoint, or a similarity to one")
    print("      (which would NOT force real spectrum)? Check the inner product / the J-symmetry.")
    print("  A2. Could a J-self-adjoint (Krein-space) H carry off-line zeros while 'looking' self-")
    print("      adjoint? If so PART 1's tautology needs the definiteness of the metric (= positivity).")
    print("  A3. Re-run PART 1 with A J-self-adjoint for an indefinite J: expect off-line zeros to")
    print("      appear, confirming the SIGNATURE (metric definiteness) is the real content.")


if __name__ == "__main__":
    run()

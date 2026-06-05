# Attack prompt: ChatGPT (paste-ready, self-contained)

> A condensed, copy-paste-ready twin of [`attack_prompt_no_repo.md`](attack_prompt_no_repo.md), tuned for pasting into a fresh ChatGPT (or any chat-box LLM) session. It summarizes the whole program state and frames the solve in one block. All math is plain Unicode so it survives a paste into a chat box; if the target has a code interpreter, the Davenport-Heilbronn control in the disciplines section is runnable from the inlined spec.
>
> Source of truth lives in the repo. If anything here drifts from [`PHASE_STATE.md`](../PHASE_STATE.md), [`docs/03_research/all_roads_to_the_signature.md`](../docs/03_research/all_roads_to_the_signature.md), [`docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../docs/03_research/research_directions/08A_rosati_standard_conjecture.md), [`docs/03_research/soft_detector_wall.md`](../docs/03_research/soft_detector_wall.md), or [`docs/03_research/spec_z_cohomology_landscape.md`](../docs/03_research/spec_z_cohomology_landscape.md), those win. Re-derive this from the longer no-repo prompt when re-syncing.

---

Paste everything below the line into a fresh chat.

---

You are a research collaborator. I am going to summarize the current state of a
multi-year program attacking the Riemann Hypothesis, and then ask you to make a
genuine advance on the one open object it has localized to. Read the whole brief
before responding. Do not brainstorm from a blank page: the cheap and medium
moves are already done, and most "fresh ideas" are restatements of RH that this
brief is built to reject. A negative result that honestly kills a branch is a
real deliverable. A plausible-sounding restatement of RH is not.

== WHAT THE PROGRAM FOUND ==

The program tested four candidate proof architectures for RH:
  1. Spectral (Hilbert-Polya): a self-adjoint operator whose eigenvalues are the
     imaginary parts of the zeta zeros.
  2. Arithmetic-geometric (Deninger / F_1): a cohomology theory for Spec(Z) that
     lifts Weil's proof of RH for curves over F_q.
  3. Direct positivity (Weil / Li): the Weil explicit-formula quadratic form is
     positive, or all Li coefficients lambda_n >= 0.
  4. Analytic (zero-free regions): push Vinogradov-Korobov 2/3 toward 1/2.

Architectures 1, 3, 4 are closed AT THE PROGRAM LEVEL: they bottom out at the
same wall (described below). Architecture 2 survives and has been sharpened to a
single object.

Framing that matters: RH lives at LEVEL 4 (positivity / signature: a
polarization, a Hodge-Riemann positive form, a negative-definite Rosati form),
NOT Level 3 (spectral / statistical: Selberg CLT, GUE / pair-correlation
statistics, log-correlated structure, the Rodgers-Tao Lambda>=0 log-gas flow).
Every Level-3 fact is compatible with a world where some zero has real part 0.51,
so no Level-3 object can close RH. If your proposed object is a statistic or a
spectral realization, it is Level 3 and cannot close RH, however suggestive.

The Spec(Z) cohomology landscape, scored on three rungs:
  (i)   trace: does the object realize zeta as a determinant / trace? Everyone
        passes (zeta or -zeta'/zeta as a regularized determinant).
  (ii)  functional-equation duality: a perfect duality pairing reproducing the
        functional equation? Several pass. This rung is FREE.
  (iii) polarization: does that duality pairing cross into a SIGNED
        (positive / negative-definite) pairing? NO candidate passes. This rung
        IS RH.
Candidates surveyed: Deninger's foliated dynamical system, Connes /
Connes-Consani's scaling site, prismatic cohomology / the Bhatt-Lurie stack
WCart, Hesselholt's THH/TC over the sphere spectrum, Arakelov /
Faltings-Hriljac arithmetic intersection theory, F_1-geometry, and
Adiprasito-Huh-Katz tropical Hodge theory. The universal gap is rung (iii).
Supplying it is RH.

== THE ONE TARGET ==

RH has been reduced to: construct the prismatic Poincare duality over Spec(Z) as
a PERFECT cup product H^1 x H^1 -> H^2 into the Euler-pole fundamental class, on
the infinite-dimensional arithmetic H^1, and prove that cup product is
HODGE-RIEMANN POSITIVE (a polarization) on the primitive part.

Equivalently: RH <=> the FE-duality cup product is a polarization
              <=> (1 - rho) = conj(rho) for every zero
              <=> Re(rho) = 1/2.

Two facts pin down where the work is:
  - Perfectness is FREE. The functional equation gives the duality pairing even
    for Davenport-Heilbronn (residual ~ 6e-30). Constructing the pairing is not
    the hard part.
  - Positivity is the ENTIRE gap. It is the arithmetic Hodge standard conjecture.

So the content splits cleanly into:
  (A) CONSTRUCT the geometric cup product H^1 (x) H^1 -> H^2 over Spec(Z) as a
      perfect pairing into the Euler-pole H^2, on the infinite-dimensional H^1;
  (B) PROVE it is Hodge-Riemann positive on the primitive part (this is RH).

The scalar equivalence (1 - rho) = conj(rho) <=> Re(rho) = 1/2 is a tautology
(true for any complex number). Do NOT "prove" it and call it progress. All
content is in (A) and (B).

This is the standard-conjecture form of Weil's 1948 proof. Over F_q, RH for a
curve is positivity of the Rosati involution on End^0(Jac C) (x) R: the trace
form B(x,y) = Tr(x y^dagger) is positive definite, and applied to Frobenius
(pi^dagger = conj(pi), pi conj(pi) = q) it forces |alpha_i| = sqrt(q). The
arithmetic target asks for the same kind of polarization over Spec(Z), with a
geometric source, not a trace identity.

== HARD CONSTRAINTS (violating one means the output is WRONG, not just weak) ==

D-H DISCIPLINE. The Davenport-Heilbronn function has a functional equation of
Dirichlet-L shape but NO Euler product, and has KNOWN zeros off the critical
line (first off-line zero ~ 0.8085 + 85.699 i, partner 0.1915 + 85.699 i). Any
method in Architectures 1/3/4 that does not distinguish zeta from D-H is
structurally wrong: it would "prove" a false statement. Before claiming any
positivity result, ask whether it would FAIL on D-H. If it passes for D-H, you
built a soft detector, not a proof. Architecture 2 is the exception: no Euler
product => no Frobenius => no algebra to polarize, so the target object is
uninhabited for D-H BY TYPE. Aim for D-H-AWARENESS: the exact defect
D(gamma) = |1 - 2 beta| is 0 for zeta and spikes to 0.617 at D-H's off-line zero.
(D-H spec if you want to build the control in a code sandbox: period-5 Dirichlet
series sum a(n)/n^s, a(1)=1, a(2)=xi, a(3)=-xi, a(4)=-1, a(5)=0, with
xi = (sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1) ~ 0.2841, odd-character-mod-5 gamma
factor. Verify constants against Titchmarsh sec 10.25 before relying on numbers.)

K1 (NON-CIRCULAR). The positivity must come from a polarization (a geometric
source), not be read off the zeros. If your construction needs the zero
locations as input, it is circular and dead.

K2 (D-H exclusion / awareness). The discriminating sign must ride the Euler /
{log p} half that D-H structurally lacks (confirmed: zeroing the prime-power
block makes zeta fail the certificate exactly as D-H does), not the shared
archimedean block.

MARGINAL-POSITIVITY THESIS (why soft methods cannot work). RH is just barely
true, with zero slack. The off-line obstruction for D-H is doubly-exponentially
suppressed: the buffer that is O(q) over F_q collapses to exp(-4 pi x) over Z.
Resolving an off-line zero at height gamma via the non-circular prime side needs
primes up to exp(gamma) (for gamma ~ 85.7, about 1e37). Consequence: no object
built from archimedean data, zero statistics, or a non-circular reconstruction
of the explicit formula can see the obstruction at any reachable resolution
without already knowing the zero location. This is a compass, not a wall: the
proof must engage the exact arithmetic structure (the Euler-product H^2, the
transcendence of {log p}), which is exactly where (A) and (B) live.

== FREEZE LIST (dead on arrival; do not propose, do not re-derive) ==

A proposal that does any of these is a restatement of RH, not a step:
  - prices in soft positivity, fires the same for D-H, or recovers only the SIGN
    (not the analytic margin);
  - re-encodes the polarization as an operator identity, a split lemma, or a
    Lefschetz decomposition;
  - raw or Schur Weil-Gram rescaling in a truncation parameter (sign is set; the
    margin is the exp(-4 pi x) wall);
  - the convex / AHK Hodge signature (wrong polarity, unconditionally (1,n-1),
    arithmetic-blind);
  - any third-L-function min-eigenvalue discriminator (forced positive at any
    reachable truncation by the exp(gamma) cost, independent of RH);
  - truncated FE-pairing Gram nondegeneracy (perfect for any L with an FE,
    including D-H);
  - the de Branges / Conrey-Li pointwise cross-term (strictly stronger than RH;
    fails for zeta);
  - the de Bruijn-Newman / Polya kernel positivity Phi>=0 (orthogonal to RH;
    D-H passes it identically).

A new proposal escapes the freeze only by doing EXACTLY ONE of:
  1. Separating zeta from D-H at reachable truncation (below exp(gamma) primes
     for the off-line zero at gamma ~ 85.7). This would overturn the
     marginal-positivity thesis. If you think you have it, you are probably
     wrong; the float64 "stealth window" is a removable cancellation artifact,
     and the true margin scales like -3.1 eps^2 at the D-H height.
  2. Being a genuine SIGNATURE THEOREM: a polarization / Hodge-Riemann
     positivity / negative-definite Rosati form with a geometric source, not
     another trace, realization, duality, or statistic.

== MILESTONE STATUS ==

  M1 (done): function-field Rosati positivity verified, four equivalent faces,
     exact across genus 1-2 curves.
  M2 (done): arithmetic Frobenius trace form assembled on non-circular data. The
     non-circular Weil form for zeta is positive (min eig ~ +0.035) but does NOT
     separate zeta from D-H (D-H reads spuriously +0.094: its off-line
     obstruction sits below the reconstruction floor). This is the "stealth
     window." Consequence: the next step must be analytic, not a finer truncation.
  M3 (attempted; produced a numerical discriminator, not a proof): deleting the
     composite block separates the controls (zeta +, D-H -, Epstein +) but adds
     no geometric content and is not the analytic domination.
  M4 (THE OPEN STEP = the target above): build the cup-product polarization on
     the infinite-dimensional arithmetic H^1 and prove positivity survives the
     limit. This is the arithmetic Hodge standard conjecture.
  M5 (bookkeeping once M4 lands): derive RH and verify K1/K2.

== WHAT I WANT FROM YOU ==

Pick exactly ONE lane and go deep. Do not spread thin.

  Lane 1 (the real gap): attack (A) or (B) directly. Construct a concrete piece
  of the cup product H^1 x H^1 -> H^2 over Spec(Z), or attack its positivity,
  using a specific cohomology. The most live substrate is prismatic / WCart
  (Bhatt-Lurie): it carries the Frobenius F (finite Euler factors, the von
  Mangoldt trace) and the Sen operator Theta (Hodge-Tate weights, the
  archimedean divisor). The open question is the polarization, not the trace.
  Reason explicitly about whether your construction would fail on D-H, and
  whether that failure is by type or by sign.

  Lane 2 (isolable, valuable regardless of RH): e.g. the Petrov
  non-semisimplicity result (arXiv:2302.11389): the WCart Sen operator is NOT
  semisimple, an obstruction to an eigenspace polarization. Is that obstruction
  fatal or routable? Or: does Deninger's foliated space (arXiv:1807.06400),
  constructed in dim 3 with orbit spectrum {log p}, admit a polarization, or is
  only its trace structure available?

  Lane 3 (assess an external theorem): score a recent paper against the
  (i)-trace / (ii)-FE-duality / (iii)-polarization template. The test is always:
  does it cross into a SIGNED pairing (rung iii), or stop at the trace (rung i)?
  Live watches: Gao-Zhang Beilinson-Bloch + adelic Hodge index
  (arXiv:2407.01304), Connes-Consani Jacobian follow-ups, Tang/Petrov prismatic.

== OUTPUT AND HONESTY ==

Produce a self-contained, paste-ready writeup: the construction or obstruction,
explicit D-H reasoning (would it fail on D-H, by type or by sign), which kill
criteria it passes and which it does not, and where it lands on M1-M5. If you
write code, reconstruct zeta and D-H from the spec above, use >= 30-digit
precision for zeros and L-values, and include the D-H control in the same run.
Report faithfully: state exactly which discipline the result passes and which it
does not. Do not upgrade a discriminator to a theorem, a trace to a signature,
or a sign to a margin. If a branch fails, name what it rules out and where the
proof must then live.

THE ONE-LINE TEST BEFORE YOU SHIP: Did I produce a polarization with a geometric
source that separates zeta from Davenport-Heilbronn, or another trace / statistic
/ restatement dressed as positivity? If the latter, do not ship it as progress.
Record the coordinate (what it ruled out, in which basis) and stop.

# Stream 4 coordinate (dir12-residue): the heat-flow `dH/dt` is the archimedean-suppressed RH-agnostic block of Bombieri W(f)

STAGED, NOT COMMITTED. Overnight 2026-06-03, Stream 4 coordinate factory. One concrete
candidate coordinate for sub-target 12.4 (the residue left open by LEARNINGS #39). Honest
scope below distinguishes PROVED / COMPUTED / CITED / STRUCTURAL-READING. Two small numerical
probes were actually run (commands + outputs reproduced); the main agent should re-derive.

## The residue (what #39 left open)

LEARNINGS #39 closed sub-target 12.4 at the level of the Rodgers-Tao log-gas functional `H(t) = sum_{j!=k} log(1/|x_j-x_k|)` with `dH/dt = -4 E(t)`, `E(t) = sum 1/|x_j-x_k|^2 >= 0`. It found the bridge "RT `Lambda >= 0` = a fragment of Weil/Hodge positivity" is FALSE, because `dH/dt <= 0` holds always (RH-agnostic), the opposite of an easy half of a single positivity. #39 then named ONE non-pre-empted salvageable target (the residue):

> Via the Gaussian-smoothed explicit formula (Balanzario-Cardenas 2023, arXiv:2312.00108), rewrite the heat-flow zero-sum `H_t` as `arch(f_t) + prime(f_t)`, compute `dH/dt` in that representation, and test (D-H discipline) whether it reproduces a DISCRIMINATING sub-block of Bombieri W(f). Prediction (from #38's suppression law): it FAILS.

This coordinate executes that residue as a falsification, with a sharpened structural reason.

## Claim (the candidate coordinate)

CLAIM (predicted-FALSE bridge, a cheap negative coordinate). Write the heat-smoothed
zero-sum via the Gaussian-smoothed explicit formula as

    S_t(f) = sum_rho f_t(gamma_rho) = arch(f_t) + prime(f_t),

where `f_t` is the Gaussian heat weight of width ~ sqrt(t) (Balanzario-Cardenas:
`arch(f_t)` is an integral against `Re psi(1/4 + it/2) = log(xi/2pi)`-type archimedean
density, `prime(f_t)` is a Hermite-weighted von Mangoldt prime sum `sum_n Lambda(n) g_t(log n)`).
Differentiate in the heat time: `d/dt S_t(f) = d/dt arch(f_t) + d/dt prime(f_t)`. The CLAIM is:

   `d/dt S_t` (equivalently the Rodgers-Tao energy `-4E(t)`) does NOT reproduce the
   DISCRIMINATING sub-block of Bombieri's W(f). Specifically:
   (i) `d/dt S_t` carries NO archimedean A_arch block. The flow energy E(t) is a pure
       pair-distance functional of the zero positions; the `arch(f_t)` term differentiates
       to the smooth `log(xi/2pi)` density, which is the COMMON (RH-independent) part, not the
       discriminating place-balance A_arch - P_fin that Bombieri's negative-eigenvalue count
       reads (LEARNINGS #20/#34).
   (ii) E(t) is SIGN-BLIND: an off-line pair at `beta = 1/2 + d` and its mirror `beta = 1/2 - d`
        contribute identically to E (the pair distance is the same), so E cannot detect the side
        of the line. Bombieri's W(f) negative-eigenvalue count is exactly the off-line obstruction;
        a sign-blind functional cannot reproduce that block.
   (iii) Even the magnitude is below the detection floor: a D-H off-line zero at height
        `gamma ~ 85.7` enters the COMPLETED (archimedean-weighted) heat object at level
        `~ exp(-(pi/4) d gamma) ~ 1.5e-29` (the #38 suppression law), far below any detector
        the project has resolved (the raw Weil Gram saw off-line at 2.6%).

NET: `d/dt S_t` is the RH-AGNOSTIC, archimedean-suppressed, sign-blind block of W(f), not the
discriminating one. The bridge is confirmed-false, with a three-part reason (no A_arch block /
sign-blind / sub-floor) sharper than #39's one-line magnitude argument.

## What to compute or obstruct (for VERIFIER / re-derivation)

A single self-contained experiment, suggested path
`experiments/criticality/e_heat_explicit_split.py` (NOT created overnight; this is a spec).

1. Build `S_t(f)` two ways for zeta and for D-H:
   (a) ZERO SIDE: `sum_rho exp(-(gamma_rho - x)^2 / (2 t))` over zeros to `T_max = 200`,
       differentiate numerically in t (or analytically: `d/dt` of a Gaussian).
   (b) PRIME+ARCH SIDE: the Balanzario-Cardenas split `arch(f_t) + prime(f_t)` with
       `prime(f_t) = sum_n Lambda(n) g_t(log n)` (Hermite/Gaussian weight) and `arch(f_t)`
       the `Re psi(1/4 + it/2)` integral. Reuse `experiments/positivity/e3f_weil_prime_side.py`
       machinery (it already assembles prime-sum + gamma-integral + boundary for Bombieri W).
   Verify (a) = (b) to truncation (sanity: the explicit formula is true).
2. Compute `d/dt S_t` in the split and decompose into `d/dt arch` + `d/dt prime`.
3. THE TEST: project `d/dt S_t` onto the Bombieri W(f) test-function basis (the boxcar /
   `phi_b` family already in `e3c_weil_form.py`) and ask whether the resulting Gram block
   reproduces the off-line negative eigenvalue. Predicted NO: the off-line contribution is
   `~ exp(-(pi/4) gamma)`-suppressed and sign-blind.
4. OBSTRUCTION (the durable content if the prediction holds): exhibit that `d/dt arch(f_t)`
   is L-function-independent at leading order (same for zeta and D-H, since the Gamma factor
   is shared) and `d/dt prime(f_t)` is the von Mangoldt sum (delocalised for D-H, #20), so the
   t-derivative inherits the place-balance structure of W but NOT its discriminating sign block.

## D-H control (K2)

The discriminator is built in. Run the experiment on BOTH zeta and Davenport-Heilbronn.
- D-H has a functional equation and the SAME degree-1 Gamma factor as a Dirichlet L, so
  `arch(f_t)` is essentially identical for zeta and D-H (the archimedean place does not see
  the missing Euler product). This is exactly why a heat-flow detector built on the smoothed
  zero-sum is K2-FAILING: it cannot distinguish zeta from D-H.
- D-H's `prime(f_t)` is the von Mangoldt-analogue sum of D-H's coefficients, which DELOCALISES
  off prime powers (LEARNINGS #20/#41, first leak at n=6). If `d/dt S_t` discriminated RH it
  would have to read this delocalisation; the claim is that the heat-time derivative washes it
  out below the `1.5e-29` floor.
- The off-line obstruction (D-H pair at `gamma ~ 85.7`) is the K2 target: a correct RH method
  must fire on it. Predicted: `d/dt S_t` does NOT fire (sub-floor + sign-blind). FAIL = the
  coordinate (the residue is a negative coordinate, as #39 predicted).

## Numerical anchors (PROBES ACTUALLY RUN overnight; main agent re-derive)

Probe 1 (suppression magnitude, the floor any heat detector must beat):
command: `python -c "..."` (completed-Xi for D-H at the off-line height, mp.dps=40)
output (reproduced):
    completed |Xi_DH(85.699)| = 1.50882e-29
    predicted floor exp(-(pi/4)*1*85.699) = 5.86918e-30
    zero density at T=85.7: 0.415866   mean spacing: 2.40462
    D-H off-line real-part offset (beta-1/2): 0.3085
This reproduces LEARNINGS #38's `|Xi_DH(85.7)| ~ 1.5e-29` independently (same order as the
`(pi/4)` prediction). COMPUTED.

Probe 2 (sign-blindness of the log-gas energy + absence of A_arch term, mp.dps=30):
output (reproduced):
    E(+offset) = 2.6268161   E(-offset) = 2.6268161   equal: True
    => log-gas energy is sign-blind to which side of the line: RH-AGNOSTIC by construction.
    A_arch density Re psi(1/4+it/2) at t=10,40,85: 1.609  2.9957  3.7495
    => A_arch grows like log(t); the heat-flow energy E has no such term.
The first two lines are a schematic check that `1/|z - zbar|^2` is even in the offset (PROVED
trivially, the probe just confirms the arithmetic). The A_arch values are the standard
`Re psi(1/4 + it/2)` digamma density (COMPUTED, textbook). Together: the heat energy is
sign-blind and carries no growing archimedean term, while the discriminating Bombieri block does.

## Self-assessment against kill criteria

- K1 (circularity): clean. The coordinate is a FALSIFICATION; it does not assume RH. The
  predicted negative result removes the heat-flow `dH/dt` as a candidate discriminating block.
- K2 (D-H discipline): the coordinate IS a K2 test. Predicted FAIL = the coordinate.
- K3 (Level placement): `dH/dt = -4E` is a Level-3 statistical / dynamical functional (#39);
  the discriminating Bombieri block is Level-4 (signature). The claim is they do not collapse,
  consistent with the four-level commitment.
- K4 (does it engage exact zeta structure?): NO, and that is the finding. The leading
  `arch(f_t)` part is place-independent (zeta = D-H), so the detector cannot engage the Euler
  product. This is the marginal-positivity compass again.

## Honest scope

- STRUCTURAL READING (the load-bearing claim): "`d/dt S_t` is the RH-agnostic / sign-blind /
  sub-floor block of W(f), not the discriminating one." Built on #38's suppression law and
  #39's RT-functional analysis (both already in the project), plus the two probes above. It is
  a PREDICTION about an experiment not yet run, not a theorem. Confidence: high (it is the same
  mechanism #38/#39 already established, now localised to the t-derivative in the explicit-formula
  split), but the project must RUN the e_heat_explicit_split experiment to convert prediction to
  computed coordinate.
- CITED: Balanzario-Cardenas arXiv:2312.00108 (the Gaussian-smoothed explicit formula split,
  STATEMENT-LEVEL, not re-derived overnight); Rodgers-Tao Forum Math Pi 8 (2020) (the flow and
  `dH/dt = -4E`); Bombieri, Weil's quadratic functional (2000) (the W(f) negative-eigenvalue
  count = off-line zeros). These are exactly the references already in #38/#39.
- COMPUTED: Probe 1 (the `1.5e-29` D-H suppression magnitude, reproducing #38) and the A_arch
  digamma densities in Probe 2. PROVED: the sign-blindness of `1/|z - zbar|^2` (trivial parity).
- NOT done overnight: the actual `e_heat_explicit_split.py` experiment (the zero-side =
  prime+arch-side verification, the projection onto the W(f) `phi_b` basis, the D-H off-line
  fire/no-fire verdict). That is the deliverable this coordinate proposes for a depth pass.
- This is a RESIDUE coordinate: it does not change the M3 signature gap, does not prove or
  disprove RH, does not construct anything new in Direction 8. Its value is closing the one
  open salvageable target #39 named, with a sharper (three-part) reason than the one-line
  magnitude argument, and with two reproduced numerical anchors.

## Verification targets (for VERIFIER) and adversarial test cases (for ADVERSARY)

VERIFIER targets (formalizable / re-derivable):
1. The explicit-formula identity `S_t(f) = arch(f_t) + prime(f_t)` matches the zero-side
   Gaussian sum to truncation, for zeta and D-H (numerical, reuse e3f machinery).
2. `d/dt arch(f_t)` for zeta and D-H agree at leading order (the shared Gamma factor): a clean
   place-independence statement.
3. `|Xi_DH(85.699)| < 1e-28` (the suppression floor; Probe 1 reproduces 1.5e-29).

ADVERSARY test cases:
1. Could a DIFFERENT smoothing (not Gaussian) un-suppress the off-line block? Check a heavy-tailed
   weight; the (pi/4) archimedean decay is intrinsic to the Gamma factor, so the prediction is the
   off-line level stays sub-floor for ANY admissible (sub-exponential) weight. If a weight beats it,
   the coordinate is wrong.
2. Could `d/dt prime(f_t)` (the von Mangoldt delocalisation for D-H) survive the t-derivative and
   discriminate? Adversary should compute the D-H `prime(f_t)` delocalisation magnitude at the
   relevant t and compare to the `1.5e-29` arch floor. If the prime delocalisation is LARGER than
   the floor at the t that resolves height 85.7, the prediction (sub-floor) is wrong and this becomes
   a POSITIVE coordinate (a surprise worth depth).
3. Sign-blindness: verify E(+d) = E(-d) is not an artifact of the schematic complex-pair model;
   in the actual Rodgers-Tao real-line flow, confirm the off-line obstruction enters E symmetrically.

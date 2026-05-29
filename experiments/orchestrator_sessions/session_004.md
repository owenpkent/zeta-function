# Session 004 synthesis: from the place-decomposition of the Weil form to a specified Spec(Z) x Spec(Z) intersection target

> Driven by the `docs/03_research/new_mathematics.md` framing ("attack the problem
> from this framing"). One coherent arc: decompose the Weil-form positivity by
> place type (3M), discover it relocates the difficulty to archimedean dominance,
> then make the SIGNATURE mechanism concrete and validated on both sides of the
> function-field / number-field divide (2G, 2H, 2I), and finally specify exactly
> what the missing arithmetic surface must be (2J, 2K).

## The arc

**3M -- input-side place-type decomposition of the Weil form** ([e3m](../positivity/e3m_place_type_balance.md), LEARNINGS #20).
Split the Weil Gram matrix by PLACE TYPE via the explicit formula,
`M = A_arch + P_fin + B_pole`, computable from the Gamma factor + Dirichlet
coefficients with no zeros -- the non-circular, input-side counterpart to the
answer-side on/off split (3J) that finding #19 had shown was a dead end. Validated
the finite/pole blocks against 3F. Clean cancellation-free fingerprint: `Lambda_L`
delocalizes off prime powers iff there is no Euler product (zeta 0, D-H 64). A
decisive Epstein class-number ladder showed composite-support detects NON-EULER,
not RH-failure (reformulation trap, caught). Structural finding: D-H's off-line
obstruction sits at the archimedean-prime cancellation scale, so a soft input-side
reconstruction cannot resolve it -- positivity must engage exact block arithmetic.

**2G -- the Hodge index as a SIGNATURE, function-field template** ([e2g](../arithmetic_geometric/e2g_intersection_signature.md), LEARNINGS #21).
On `C x C`: the primitive intersection form is negative definite, and that
negative-definiteness IS the Hasse-Weil bound `|t| < 2g sqrt(q)` (exact, genus 1-2).
Positivity from a signature, not a trace identity -- the K1 escape route, exhibited.

**2H -- arithmetic Hodge index over Spec(Z)** ([e2h](../arithmetic_geometric/e2h_arithmetic_hodge_index.md), LEARNINGS #22).
The Neron-Tate height pairing on `E(Q)` is positive definite (rank 1,2,3;
regulators match LMFDB). Faltings-Hriljac, validated. The Hodge-index signature is
a genuine THEOREM over Spec(Z) for a single arithmetic surface.

**2I -- the genuine archimedean Neron local height** ([e2i](../arithmetic_geometric/e2i_archimedean_local_height.md), LEARNINGS #23).
Self-derived the Tate telescoping series and validated against `h_hat` to 1e-5
(catching the documented factor-of-2 via the validation gate). Result: integral
generators are 100% archimedean on the diagonal, but the archimedean pairing alone
goes indefinite by rank 3 -- positivity is GLOBAL (archimedean diagonal + finite
off-diagonal glue), the arithmetic-geometry face of 3M's two-clock balance.

**2J / 2K -- the bridge and the specified target** ([2J](../arithmetic_geometric/2J_arakelov_adjunction.md), [2K](../arithmetic_geometric/2K_spec_z_squared_dictionary.md)).
2K maps the explicit-formula data to the would-be intersection NUMBERS on
`S = Spec(Z) x Spec(Z)`: the pole block `B_pole` is the hyperbolic fibre direction,
the prime block `P_fin` is the Frobenius correspondence `Gamma_S . Delta_S` (= the
von Mangoldt / Lefschetz count), the archimedean block (2I's `lambda_inf`) is the
intersection at infinity. 2J covers arithmetic adjunction: `omega-bar^2 = 12 h_Fal`,
the analogue of `Delta^2 = 2-2g`, with the archimedean piece the Petersson norm of
the discriminant.

## The single takeaway

The intersection NUMBERS of the hypothetical arithmetic surface are all computable
today (explicit formula + 2I), and the arithmetic Hodge index is a THEOREM for a
single arithmetic surface (2H). The gap is precisely the **product surface
`Spec(Z) x Spec(Z)` and its Frobenius correspondence** -- and the session converts
"build it" from an aspiration into a SPECIFICATION:

- target intersection form = the Weil-form Gram matrix `A_arch + P_fin + B_pole`;
- hyperbolic `(+1)` direction = the pole of zeta at `s = 1` (`B_pole`);
- the Frobenius correspondence's defining property = `Gamma_S . Delta_S = ` the
  prime side, which exists (prime-power-supported) iff there is an Euler product
  (the K2 discipline made geometric, 3M #20);
- the archimedean fibre's role = 2I's `lambda_inf`, not positive-definite alone,
  so the surface must be global/compactified (no finite-only or archimedean-only
  shortcut, 2I #23).

This is Direction 8 milestones 5.1 (state the index precisely) and 5.6 (K1: the
positivity is a SIGNATURE anchored by the pole, not a trace identity), now grounded
in computed, validated data.

## Methodological note (the discipline that held)

Every transcendental/normalization-sensitive claim was gated on validation against
an independent ground truth, never assumed: the 2I archimedean series was
self-derived and validated against LMFDB `h_hat` (the factor-of-2 was CAUGHT, not
trusted); the 3M place blocks were checked against 3F; the 2G/2H signatures against
Hasse-Weil and LMFDB regulators. The one place a transcribed formula was needed and
could not be reliably obtained (Cohen 7.5.7) was bypassed by derivation-plus-
validation rather than by shipping unvalidated code. The Davenport-Heilbronn / K2
discipline was turned on the project's OWN methods (the composite-support
discriminator was killed by the Epstein ladder).

## Lean status

A VERIFIER pass formalizing the 2G signature condition (primitive form negative
definite <=> Hasse-Weil) and the 2H Faltings-Hriljac positive-definiteness into
`lean/ZetaRH/HodgeIndex.lean` was launched this session; see that file and
`lean/README.md` for the target IDs and build status.

## Commits (session 004)

3M: `b0c6e77`, `18483e2`. 2G: `fbba5dd`. 2H: `20d6987`, `67374d0`. 2I: `03a80bf`.
PHASE_STATE logs: `eb73ee6`, `deda506`, `f12281f`. (2J/2K/synthesis + Lean: this
session's closing commits.)

## Recommended next steps

1. **Numerical:** the 2J follow-up -- period point `tau`, Petersson norm of
   `Delta`, archimedean part of `omega-bar^2 = 12 h_Fal`, validated by SL_2(Z)
   invariance and known Faltings heights (the `omega-bar^2` companion to 2I).
2. **Structural (the real target):** Directions 1-4 (Lambda-blueprints / prismatic)
   now have a SPECIFIED goal from 2K -- construct `S` whose intersection form is the
   Weil-form Gram matrix with `B_pole` as the hyperbolic direction.
3. **Formal:** complete the Lean formalization (real proof of the 2x2 negative-
   definite <=> Hasse-Weil fact; faithful statement of Faltings-Hriljac).

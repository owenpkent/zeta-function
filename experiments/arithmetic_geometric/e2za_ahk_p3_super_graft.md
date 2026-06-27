# e2za: 09A P3 attack via an odd generator + super-tensor (adversary-corrected)

Experiment: [`e2za_ahk_p3_super_graft.py`](e2za_ahk_p3_super_graft.py). LEARNINGS #129.

## What was attempted

The 09A gap is P3: the AHK degree map must carry the Frobenius trace t, but a matroid Chow
ring is purely even/Tate with no H^1 where the modulus-sqrt(q) eigenvalues live (e2yy/#124).
The new idea: over a curve the t-carrying form lives in H^1 (x) H^1 (Kunneth), and Kunneth
of odd pieces is a SUPER (graded) tensor. So maybe P3's missing ingredient is just an ODD
generator, and P1 (the AHK product structure) survives as the super-tensor.

## Verdict (downgraded by an independent ADVERSARY pass): a coordinate, not an advance

The headline claims were over-stated and were retracted:

- "P1 survives" is RETRACTED. The code tests only the SCALAR Lefschetz multiplicativity
  L(C x C) = L(C)^2 = (1-t+q)^2, an identity true for ANY t, q (incl. nonsense). That is NOT
  the AHK ALGEBRA-level local product structure A(star F) = A(L_F) (x) A(L^F) the
  deletion-contraction induction consumes. AHK machinability of a super-algebra is untouched.
- "deg carries t = q+1-t" is the Grothendieck-Lefschetz fixed-point formula restated (a
  tautology), and the odd H^1 + Frobenius is HANDED IN, not sourced (e2yy unchanged). The
  gap is RENAMED, not moved.

What genuinely survives: a correct DIAGNOSIS of e2yy (the missing ingredient is an odd H^1),
K1-cleanliness (Pi from point counts, the fake correctly rejected), and the relabeling of
the gap into two precise open questions: R1 (can a combinatorial object SOURCE a non-Tate
odd H^1 with modulus-sqrt(q) Frobenius?) and R2 (does AHK deletion-contraction RUN on a
super-algebra?). R2 is settled in [`e2zb`](e2zb_super_ahk_recursion.md). P6/M4 untouched.

The adversary's sharpest line, on the marginal-positivity prior: the construction looks
clean precisely where the measured margin is zero, and the clean look is the tell.

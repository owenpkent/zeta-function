# e2zb: R2 (super-AHK machinability) closes into R1; the AHK route to P3 is a dead branch

Experiment: [`e2zb_super_ahk_recursion.py`](e2zb_super_ahk_recursion.py). LEARNINGS #129.
Verified by a literature survey + two adversarial refutation probes (2026-06-27).

## The structural result (the computation)

AHK's only induction is matroid deletion-contraction (chi_M = chi_{M\e} - chi_{M/e}), whose
input is purely combinatorial and t-BLIND: chi depends on (rank, #elements) only. Two
arithmetic decorations of the SAME matroid U(2,3) with the same Tate scale q=25 but different
Frobenius trace -- A (t=2) and B (t=100) -- have IDENTICAL induction input (matroid, minors,
chi, the whole deletion-contraction tree) but different RH-truth (A's moment form is PSD,
B's is indefinite, min eig -1.6e4). So the engine cannot distinguish A from B while RH does.
This elevates e2yy (#124) from "the FORM is t-blind" to "the ENGINE is t-blind": no
deletion-contraction induction over a matroid can carry t. R2 reduces to R1.

## The verified verdict (the corrected reasoning matters)

A SURVEYOR scan + two adversarial probes REFUTED the naive closure reason while confirming
the conclusion:

- "combinatorial => Tate" is FALSE as a theorem (a GAP, not an obstruction): Amini-Piquerez
  prove a genuinely non-Tate combinatorial Kahler package with NO ambient variety
  (off-diagonal tropical h^{p,q}); Belkale-Brosnan + Mnev universality make matroid/Kirchhoff
  schemes arbitrarily non-Tate; Brown-Schnetz give a modular K3 in phi^4.
- The tropical Jacobian polarization is INTRINSIC to the metric graph (Mikhalkin-Zharkov),
  not imported -- so the survey's "imported" reason was also wrong.

What ACTUALLY closes R2 (the corrected, true statement): no known object is at once
(i) bare-combinatorial, (ii) carrying a modulus-sqrt(q) Frobenius on a non-Tate piece, and
(iii) AHK-machinable. The split is on the FROBENIUS clause -- the non-Tate combinatorial
objects (Amini-Piquerez, Babaee-Huh, tropical Jacobians) are FROBENIUS-FREE (over (R,max,+):
no q, no sqrt(q), no Galois), and the sqrt(q)-carriers (Belkale-Brosnan, Brown-Schnetz)
IMPORT the polarization from an ambient variety (= #97). The one live-looking tropical lead
is DOUBLY dead: no arithmetic weight (no t) AND wrong signature (positive-definite, never
flips off-line; the e3r/#97 polarity objection).

## Net + recommendation

R2 is a dead branch: it reduces to R1, and even granting t the AHK polarity is the wrong
(positive-definite) signature for P6/M4. "Combinatorial => Tate => t-blind" is a gap, not a
proven obstruction. Recommendation (from the synthesis): record-and-stop on R2, then pivot
to the ARAKELOV face (09A Section 5/7), the one route that natively carries both a genuine
arithmetic weight (Faltings-Hriljac) and the indefinite Hodge-index signature AHK lacks.
P6/M4 untouched.

# All roads to one signature (P4 survey, first prose pass)

> **Status: DRAFT, gate-free sections only (2026-06-16).** Sections 1, 2, 3, 5, 6 are first-pass prose.
> Section 4 (the Spec($\mathbb{Z}$) scorecard) is a **stub**: its content makes precise
> arithmetic-geometry claims that need an expert reader before they are written down for refereeing.
> Outline + positioning: [`P4_survey_outline.md`](P4_survey_outline.md). Do not circulate.

## Abstract (draft)

Every mature framework for the Riemann Hypothesis succeeds at one task and stops at the same next one.
Spectral (Hilbert-Polya), arithmetic-geometric (Deninger, $\mathbb{F}_1$), direct positivity
(Weil-Li), the analytic zero-free method, and the recent prismatic and topological-Hochschild programs
all *realize* the zeta function as a determinant or a trace of some operator or correspondence. None of
them supplies the one further ingredient that would force the zeros onto the critical line: a
polarization, an RH-equivalent positivity or Hodge-index signature on that realization. We organize the
landscape around this single observation. We grade candidate cohomology theories for
$\mathrm{Spec}(\mathbb{Z})$ against one requirement (does the candidate carry an RH-equivalent
polarization?), we argue that the reason the gap is universal is *marginal positivity* (the relevant
positivity is a near-zero cancellation residue with no slack), and we use the Davenport-Heilbronn
L-function as the operational test that keeps the classification honest. The posture is that this is a
compass, not a verdict: locating the gap as a single, precisely-identified polarization tells the field
where the proof must live.

## 1. Introduction

The Riemann Hypothesis is usually surveyed as a catalog: here is the analytic approach, here is the
spectral approach, here is the arithmetic-geometric approach, each with its partial results and its
obstruction. This survey takes a different cut. We argue that the catalog has a structure, and that the
structure is a convergence. Read at the right altitude, the major approaches are not independent bets on
different mechanisms. They are different constructions of the *same* object, and they fail at the *same*
step.

The object is the zeta function realized as a spectral quantity. Over a function field, Weil's theorem
makes this precise and complete: the zeta function of a curve $C/\mathbb{F}_q$ is a ratio of
characteristic polynomials of Frobenius acting on cohomology, and the Riemann Hypothesis for $C$ is the
statement that a certain intersection form is a polarization (the Hodge index theorem on $C \times C$).
Over $\mathbb{Q}$, every program reaches the first half of this picture (a realization of $\zeta$ as a
determinant or trace) and none reaches the second (the polarization). The gap is not incidental to one
approach. It is the same gap in all of them, and supplying it is itself equivalent to the Riemann
Hypothesis.

This is not the framing of the field's standard references. Bombieri's problem description and Conrey's
*The Riemann Hypothesis* (Notices AMS, 2003) catalog approaches and evidence. Connes' recent survey
(2026) is wide-angle but argues from a single program, the noncommutative-geometry trace formula, toward
RH. None of them organizes the landscape around the convergence claim, none grades the candidate
cohomologies against an explicit polarization requirement, and none uses the Davenport-Heilbronn
function as a systematic discipline. Those three moves are what this survey adds.

A word on posture. We document several methods that provably cannot close RH. We frame each as a
coordinate, not a defeat. A method that fails for a precise structural reason removes a branch and
sharpens where the real proof must live. The marginal-positivity finding in particular reads as a
compass: it says the proof must engage the exact structure of $\zeta$, not as a discouragement but as a
direction.

## 2. Why the problem lives at the level of positivity

It is useful to stratify statements about the zeros by how much they constrain the real parts. At the
statistical level sit the facts about the *distribution* of the zeros: pair correlation and the GUE
law, the Selberg central limit theorem, the moment conjectures, the log-correlated field structure of
$\log|\zeta|$. These are deep and largely established or well-supported. They are also, by themselves,
compatible with a world in which some zero has real part $0.51$. They constrain how the zeros are
spread, not where they sit. We call this the statistical level (Level 3 in the project's four-level
framing; the full stratification is developed elsewhere).

The Riemann Hypothesis is a statement at a strictly higher level: the level of positivity (Level 4).
Weil's criterion expresses RH as the positivity of an explicit quadratic form built from the explicit
formula; Li's criterion expresses it as the nonnegativity of a sequence $\lambda_n$. These are not
statements about the distribution of the zeros. They are exact constraints whose truth is equivalent to
every zero lying on the line. No purely statistical input implies them.

The cleanest way to see the gap between the two levels is the Davenport-Heilbronn function. It satisfies
a functional equation of the Riemann type, it has the analytic continuation, and it shares the
archimedean structure of $\zeta$. It also has zeros off the critical line. So any argument that would
prove RH from functional-equation-plus-continuation data alone must fail, because the same argument
would prove a false statement for Davenport-Heilbronn. The one feature $\zeta$ has and
Davenport-Heilbronn lacks is the Euler product. This is the classical Selberg-class lesson, and we use
it operationally throughout: a proposed method is structurally suspect unless it distinguishes $\zeta$
from Davenport-Heilbronn, and the place where the distinction has to enter is the Euler product.

## 3. The realizations: every road builds the same trace

This section is the positive half of the convergence claim. In each framework, $\zeta$ (or its
completed form) appears as a spectral determinant or a trace.

**Function field (the complete case).** For a curve $C/\mathbb{F}_q$, Hesselholt's formula realizes the
zeta function as a ratio of regularized determinants of the Frobenius-like operator on topological
periodic homology, and Weil's classical proof realizes the same zeta function through Frobenius acting
on $H^1$. Here the full picture exists: the Riemann Hypothesis for $C$ is equivalent to the negative
definiteness of the primitive part of the intersection form on $C \times C$, which is the Hodge index
theorem. The signature *is* the Riemann Hypothesis, and it is a theorem. This is the template the other
roads are trying to lift to $\mathbb{Z}$.

**Spectral.** The Hilbert-Polya program seeks a self-adjoint operator whose eigenvalues are the
imaginary parts of the zeros. Connes' trace formula realizes the explicit formula as a trace on the
adele class space, and the constructive Weil-positivity program produces operators whose spectra
approximate the zeros. In every case the construction delivers the realization; the step that remains is
the positivity, which is RH-equivalent and unproven.

**Arithmetic-geometric.** Deninger's program predicts a cohomology theory for $\mathrm{Spec}(\mathbb{Z})$
with a flow whose regularized determinant is the completed zeta function, and the recent
prismatic and topological-Hochschild programs supply concrete operators (a Frobenius $F$ and a Sen
operator $\Theta$) whose traces recover the Euler factors and the archimedean factor. Again: the
realization is delivered; the polarization is not.

The common shape is unmistakable. Each framework produces $\zeta$ as $\det$ or $\mathrm{Tr}$. The
Riemann Hypothesis is never the realization. It is the signature, the positivity, the polarization on
the realized object, and it is the same object in every framework. That is the irreducible content, and
it is what Section 4 grades the candidates against.

## 4. The Spec(Z) scorecard [STUB, pending expert reader]

> This section is intentionally not drafted. It is the technical core: a table of candidate cohomology
> theories for $\mathrm{Spec}(\mathbb{Z})$ (Deninger foliated, Connes / Connes-Consani, prismatic /
> WCart / Gurney, Hesselholt THH-TC, Arakelov / Faltings-Hriljac, $\mathbb{F}_1$, AHK) graded against
> three columns: (i) realizes $\zeta$ as a trace, (ii) functional-equation duality / perfectness,
> (iii) an RH-equivalent polarization. The claim to be defended is that every candidate has (i), most
> have (ii), and none has (iii); and that (iii) is the conjunction of a small number of
> proven-droppable properties, so that an object with all of them proves RH. These are precise
> arithmetic-geometry assertions about what each theory does and does not supply, and they must be
> vetted by an expert before they are committed to prose. Source: the project's
> `spec_z_cohomology_landscape.md`. The methods subsection (the Davenport-Heilbronn discipline,
> operationalized as a quantitative detector with a counting law) attaches here.

## 5. Marginal positivity: why the gap is universal

If every road reaches the realization and stalls at the polarization, one wants to know why the last
step is uniformly hard. The answer is quantitative, and it is the heart of the compass.

Take the natural truncated form of the Weil quadratic form, built from the archimedean factor and the
primes out to a cutoff. For $\zeta$, its minimal eigenvalue is positive, but only barely: it is a
cancellation residue. In the project's computations the three constituent blocks have norms of order
$55$, $69$, and $123$, yet they sum to a form of norm about $0.33$, a cancellation of roughly $370$ to
one, and the archimedean block on its own is indefinite. The positivity is not a cushion plus a small
perturbation; it is a near-exact cancellation that lands just on the positive side.

Sharper still, the margin collapses doubly exponentially in the cutoff. Through the Slepian
prolate-concentration eigenvalues, the minimal eigenvalue behaves like $\varepsilon(x) \sim e^{-4\pi x}$
as the prime cutoff $x$ grows. It crosses below double-precision by $x \approx 3$ and is around
$10^{-71}$ at the cutoffs the constructive programs need. This is why any finite, structure-blind
computation sees $\zeta$ and Davenport-Heilbronn as indistinguishable: the off-line obstruction sits
below the cancellation floor, in a stealth window.

The discriminating quantity, when one writes it exactly, is the duality-versus-polarization defect
$D(\gamma) = |1 - 2\beta|$, which is identically zero for $\zeta$ and spikes to $0.617$ at
Davenport-Heilbronn's off-line height $\gamma \approx 85.7$. The defect is a clean structural quantity;
what is expensive is evaluating it without assuming the answer, because resolving that height through
the non-circular prime side needs primes out to $e^{\gamma}$, about $10^{37}$. The positivity is exact
and the obstruction is real; only the soft, reachable reconstruction is blind to it.

The reading is directional. Marginal positivity does not say RH is too hard. It says no soft or
structure-blind method has room to work, because there is no slack to absorb an approximation. The proof
must engage the exact arithmetic of $\zeta$, which is precisely the Euler-product structure that
Section 2 isolated and the polarization that Section 4 grades.

## 6. Logical status and stance

The Riemann Hypothesis is a $\Pi^0_1$ sentence: it is equivalent to a universally quantified statement
over a decidable predicate (through Lagarias-type or Robin-type criteria). One consequence is worth
stating because it closes a tempting escape. If RH were proved independent of ZFC, it would thereby be
proved true, since a $\Pi^0_1$ sentence that is independent cannot be false (a false $\Pi^0_1$ sentence
has a finite refuting witness and is therefore provably false). Undecidability is a back door to truth,
not a way out. This also explains a texture of the problem visible from the formalization side: the
effective bounds needed at the arithmetically extreme (highly composite) inputs get sharper without a
uniform soft bound covering all of them, which is the logic-layer shadow of marginal positivity.

We end where we began, on posture. The convergence we document is not a wall. It is a localization. The
field has, across five independent frameworks, narrowed the missing step to a single object: an
RH-equivalent polarization on the arithmetic realization of $\zeta$, equivalently the arithmetic Hodge
standard conjecture, equivalently Rosati positivity in the arithmetic setting. Knowing that the gap is
one precisely-identified positivity, and knowing from marginal positivity that it cannot be supplied
softly, is real progress. It tells us what to build.

## Conclusion (draft)

The Riemann Hypothesis is the signature, not the realization. Every serious framework builds the
realization and stops at the signature, the same signature in each, and that signature is a polarization
equivalent to the arithmetic Hodge standard conjecture. The marginal-positivity phenomenon explains why
no soft method can supply it and points the work toward the exact Euler-product structure of $\zeta$.
The remaining content of the subject, on this reading, is the construction of one object with one
property, and the search has been narrowed to exactly that.

---

### Drafting notes (not for the paper)

- §4 is the gating section; everything else is gate-free and drafted above.
- Numbers in §5 (norms $55/69/123 \to 0.33$, $\sim 370\times$; $\varepsilon \sim e^{-4\pi x}$, crosses
  float64 by $x\approx 3$, $\sim 10^{-71}$ at Connes' $x=13$; $D(\gamma)=|1-2\beta|$, $0.617$ spike at
  $\gamma\approx 85.7$, $e^{\gamma}\approx 10^{37}$) **verified 2026-06-16 against
  `soft_detector_wall.md`** (the frozen consolidation of LEARNINGS #52, #56, #63). A final check against
  the raw `e3v` / `e3y` outputs is still prudent immediately before submission.
- §2 deliberately states only the Level-3-vs-Level-4 cut precisely and defers the full four-level
  definitions to the cited project doc, to avoid overstating a framing not yet written up for referees.
- §3 keeps the realization claims at the level the project has validated (Hesselholt determinant
  formula; Weil/Hodge-index function-field mirror; Deninger/prismatic operators as traces). Do not
  upgrade any "realization" to a "polarization" claim.

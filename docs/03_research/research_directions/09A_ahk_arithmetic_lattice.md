# Direction 9A: The arithmetic AHK lattice (the sharpened BUILDER target)

> **Status: construction target, posted 2026-06-14.** This is the BUILDER spec extracted from the breadth-over-proof-engines sweep ([LEARNINGS #97](../../../experiments/LEARNINGS.md); memory `breadth_proof_engine_sweep`). It refines Direction 9 ([`09_arithmetic_matroid_li.md`](09_arithmetic_matroid_li.md)) and the M4 organ of [`08A_rosati_standard_conjecture.md`](08A_rosati_standard_conjecture.md). It is not an evaluator task. It names a single object to build, the positivity of which is left open on purpose: that open positivity is M4, the arithmetic Hodge standard conjecture.

## 0. Why this is sharper than "build the surface"

Direction 8.A asks for an **arithmetic surface** (a model of $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, a Frobenius correspondence on it, and the Hodge-index signature of its intersection form). That inherits the whole weight of constructing a variety over $\mathbb{F}_1$ before any positivity can be stated.

Adiprasito-Huh-Katz (AHK 2018) proved that the **Hodge-Riemann relations need no variety**: a finite combinatorial object (the Chow ring of a matroid, built from a graded lattice of flats) carries Poincare duality, hard Lefschetz, and a Hodge-Riemann signature, manufactured K1-clean by a strictly submodular Lefschetz element and a deletion-contraction induction. The signature is *sourced* from the combinatorics, never read off any spectrum. That is exactly the K1-noncircular property the program keeps asking for, and AHK is the unique proven witness that it is achievable with no ambient variety (the sweep's one retained positive coordinate, [#97](../../../experiments/LEARNINGS.md)).

So the sharpened target is: **build the combinatorial skeleton, not the variety.** Supply the finite graded lattice plus the one Lefschetz element, and let AHK's machinery (not a curve) carry the Hodge-Riemann relations. The ask shrinks from "a variety and its cohomology" to "a lattice and a submodular function." The positivity of that object's primitive form is RH; we leave it open and make everything else explicit.

## 1. What the original Direction 9 got wrong, and the correction

Direction 9 sought a sequence of matroids $M_n$ on the primes whose **characteristic polynomial converges to $\xi(s)$** ($\chi_{M_n} \to \xi$), reading $\lambda_n \ge 0$ off AHK log-concavity. The cheap falsification ([`e3n_li_signature.py`](../../../experiments/positivity/e3n_li_signature.py), LEARNINGS #27) showed AHK-style log-concavity of the Li / $\xi$-Taylor data is a **non-Euler detector**: it holds with no Euler product and does not separate Davenport-Heilbronn at any reachable order. Degree-1 Hodge-Riemann (log-concavity) is too weak; it lives at the level the marginal-positivity stealth window already closed.

Two structural reasons this happened, both now coordinates ([#40](../../../experiments/LEARNINGS.md), [#97](../../../experiments/LEARNINGS.md)):

1. **The standard Chow-ring form is $t$-blind.** The combinatorial Lefschetz/intersection form does not see the Frobenius trace $t$ that carries RH. The Connes-Consani square's natural mixed-volume (Alexandrov-Fenchel) form gives a Lorentzian signature for free, but it is the characteristic-$1$ shadow: it returns the *same* signature for $t=2$ and $t=100$ (#40). A $t$-blind form cannot be RH, because $\lvert t\rvert \le 2\sqrt q$ is RH.
2. **The standard primitive form is positive-DEFINITE.** AHK's Hodge-Riemann form is definite on each primitive piece (that is what makes the inequalities log-concavity). The signature RH needs is the **indefinite $(1, n-1)$ Hodge index** (Castelnuovo-Severi on $\mathrm{NS}(C \times C)$, e2g); in the AHK world the indefinite piece appears only in a derived $2$-plane (AHK Lemma 9.6), not as the native primitive form.

The correction is to stop converging a characteristic polynomial and instead **decorate** the lattice with arithmetic so that the degree map carries $t$ and the primitive form is born indefinite. The decorated object is no longer a standard matroid; whether it still satisfies Hodge-Riemann is precisely the open kernel.

## 2. The object to build (the BUILDER spec)

Construct a **finite graded lattice** $L$ on the primes $p \le P$ (a poset of "arithmetic flats" with rank function $\mathrm{rk}$ and top rank $r$), together with a graded $\mathbb{Z}$-algebra $A^\bullet(L) = \bigoplus_{k=0}^{r} A^k(L)$ (its Chow / graded-Mobius algebra) and a degree map $\deg: A^r(L) \to \mathbb{Z}$, satisfying all six of the following. Properties (P1)-(P5) are the constructible data; (P6) is left open and is M4.

- **(P1) Local product structure (AHK-machinable).** For every flat $F \in L$, the star $\mathrm{star}(F)$ factors as an AHK product of two smaller arithmetic objects, $A^\bullet(\mathrm{star}(F)) \cong A^\bullet(L_F) \otimes A^\bullet(L^F)$ (restriction and contraction at $F$). This is the local structure AHK's deletion-contraction / semismall induction runs on. Without it there is no machine, only a wish.

- **(P2) Poincare duality.** $A^\bullet(L)$ is a Poincare-duality algebra of socle degree $r$: $\deg: A^r(L) \xrightarrow{\sim} \mathbb{Z}$ and the pairing $A^k \times A^{r-k} \to A^r \xrightarrow{\deg} \mathbb{Z}$ is perfect. (For a genuine matroid this is an AHK theorem; for the arithmetic lattice it is a property to certify.)

- **(P3) The degree map carries the Frobenius trace.** The arithmetic decoration of $\deg$ (the intersection numbers of the prime-atoms) reproduces $q + 1 - t$ over $\mathbb{Z}$: the point-count / Lefschetz-number functional of the lattice equals the arithmetic Frobenius trace, not a combinatorial integer. This is the repair of the $t$-blindness of (#40): $\deg$ must move when $t$ moves. Concretely, on the function-field shadow (P-specialized to a curve $C/\mathbb{F}_q$) the degree of the Frobenius class must be $q + 1 - t = \#C(\mathbb{F}_q)$.

- **(P4) A $t$-carrying strictly submodular Lefschetz element.** There is an element $\ell \in A^1(L)$ from a strictly submodular function $c$ on $L$ (an interior point of the nef/ample cone of the lattice's Bergman-type fan) such that hard Lefschetz holds: $\ell^{r-2k}: A^k \xrightarrow{\sim} A^{r-k}$. Crucially $\ell$ is **$t$-carrying**: the integrals $\deg(\ell^{r-2k} \cdot x \cdot y)$ depend on $t$ (so the Lefschetz form is not the characteristic-$1$ shadow). The submodular function must be **arithmetic** (values from $\log p$ / von Mangoldt / local point-counts), not the rank-only submodular function that produces the $t$-blind form.

- **(P5) The primitive form is INDEFINITE $(1, n-1)$.** On the middle primitive part $P^k = \ker\!\big(\ell^{\,r-2k+1}: A^k \to A^{r-k+1}\big)$ in the degree where RH lives, the Hodge-Riemann bilinear form $Q_\ell(x,y) = (-1)^{k}\deg(\ell^{\,r-2k}\, x\, y)$ has **Lorentzian $(1, n-1)$ signature**, matching $\mathrm{NS}(C\times C)$ (e2g), not the positive-definite AHK primitive form. The indefinite shape must be the native form, not a derived $2$-plane (AHK Lemma 9.6).

- **(P6) [OPEN, = M4] Hodge-Riemann positivity of the decorated object.** With the arithmetic decoration of (P3)-(P5) in place, the Hodge-Riemann relations still hold: $Q_\ell$ is definite (with the prescribed indefinite signature) on the primitive parts. This positivity, specialized through (P3), is exactly $\lvert t\rvert \le 2\sqrt q$ over $\mathbb{Z}$, i.e. RH. **It is left open. Supplying it IS the arithmetic Hodge standard conjecture (M4).**

The whole point of the sharpening: (P1)-(P5) are a finite, checkable, buildable specification. They do not require a variety; they require a lattice and a submodular function. The hard problem is isolated cleanly in (P6), and (P6) is the same M4 every road reaches, now stated as "does an arithmetic AHK lattice satisfy Hodge-Riemann?" rather than "construct the surface and prove its cup-product signature."

## 3. The provenance of each property (which blindness it repairs)

| Property | Repairs | From |
|---|---|---|
| P1 local product | "AHK needs a machine, not a wish" | AHK deletion-contraction; BHMPW semismall |
| P3 $\deg$ carries $t$ | euler-archimedean blindness (atomic degree = integer, not $q+1-t$) | #97 kill of AHK as finished; #40 $t$-loss |
| P4 $\ell$ $t$-carrying | $t$-blindness (same $(1,3)$ for $t=2$ and $t=100$) | #40; #97 indefinite-gate |
| P5 indefinite native form | wrong signature (AHK primitive form is definite) | #97 indefinite-gate; AHK Lemma 9.6; e2g |
| P6 open positivity | the irreducible M4 residual | 08A M4; all_roads thesis |

The sweep's positive coordinate, restated as the design rule for this object: **the $(1,n-1)$ form must be SOURCED from a polarization on a real arithmetic object whose intersection numbers ARE the Frobenius trace $t$**, never PROPAGATED from a combinatorial certificate (the Lorentzian / log-concavity bracket, which is $t$-blind) nor TRANSPORTED through a degeneration (the CKS / limit-MHS route, which imports the polarization $Q$ from a nearby fiber that $\mathrm{Spec}(\mathbb{Z})$ does not have). P3 and P4 are that rule made into requirements.

## 4. Kill-criteria status

- **K1 (signature not trace): clean by design.** Hodge-Riemann is a signature statement; AHK manufactures it from $\ell$, never from the zeros. This object inherits that property (the off-line-flip test should FIRE on $Q_\ell$: moving a zero off the line must flip the primitive-form signature, the way it flips the Weil form in [`offline_flip_test.py`](../../../experiments/positivity/offline_flip_test.py), #96). If $Q_\ell$ does not respond to an off-line zero, the object is $t$-blind again and (P3)/(P4) have failed.
- **K2 (must exclude Davenport-Heilbronn): clean by construction.** No Euler product $\Rightarrow$ no prime-atom independence structure $\Rightarrow$ no lattice $\Rightarrow$ no $A^\bullet$ to take a signature of. D-H cannot even instantiate (P1). This is the combinatorial shadow of "no Euler product $\Leftrightarrow$ no local bidegrees $\Leftrightarrow$ no $\Gamma_S$" (#25/#26).
- **K3 (function-field shadow / fq-specialization): the load-bearing test.** Specializing the prime-lattice to a single curve $C/\mathbb{F}_q$ must recover the AHK/tropical Hodge index already in hand (e2g, 2G): $\deg$ returns $\#C(\mathbb{F}_q) = q+1-t$ (P3), and $Q_\ell$ returns the $(1, 2g)$ Castelnuovo-Severi signature on $\mathrm{NS}(C\times C)$ (P5), with (P6) becoming the Weil bound (a theorem there). If the construction cannot reproduce the function-field case where RH is proven, it is wrong before $\mathbb{Z}$.

## 5. The two faces of the same gap

This is the AHK-side face of M4. The Arakelov-side face is the **Faltings-Hriljac height pairing** plus the archimedean $\Gamma_S$ place (the $\Gamma$-factor as the place at infinity). They are two presentations of one missing object, an arithmetic intersection theory with an indefinite $(1, n-1)$ signature that is $t$-carrying and joins the finite (Euler) and archimedean ($\Gamma$) data:

- **AHK face (this spec):** a finite graded lattice with a $t$-carrying submodular Lefschetz element. Combinatorial, K1-clean, but the arithmetic decoration takes it out of the proven matroid world, so (P6) is open.
- **Arakelov face:** the Faltings-Hriljac pairing is a *proven* Hodge-index-type pairing on an arithmetic surface, but it is positive-**definite** and local to a single surface (transfer-search corpus; #43 region), so it has the wrong signature and no global $\Gamma_S$-joined form.

Each face is missing exactly what the other has: AHK has the indefinite combinatorial signature but not the arithmetic content; Faltings-Hriljac has the arithmetic content but not the indefinite global form. Building the AHK lattice with (P3)-(P5) is an attempt to graft the arithmetic onto the indefinite combinatorial skeleton; the dual attempt grafts the indefinite global form onto Faltings-Hriljac. They meet at (P6).

## 6. Milestones (BUILDER sub-targets)

- **9A.1** Specify the prime-lattice $L$ and the algebra $A^\bullet(L)$ precisely; instantiate (P1) local product structure on the smallest non-trivial case ($P = 2, 3$). (~10 pp.)
- **9A.2** Define the arithmetic submodular function $c$ and the $t$-carrying $\ell$; certify (P2) Poincare duality and (P4) hard Lefschetz on the small case. (~15 pp.)
- **9A.3 (K3, decisive):** function-field specialization. Show $L$ specialized to $C/\mathbb{F}_q$ recovers $\deg = q+1-t$ (P3) and the $(1, 2g)$ Castelnuovo-Severi signature (P5), with (P6) = the Weil bound. A numerical first pass can reuse the e2g intersection form. If this fails, the spec is wrong. (~10 pp.)
- **9A.4** State (P5) over $\mathbb{Z}$ and verify the off-line-flip test fires on $Q_\ell$ (the K1 sanity check, #96). (~5 pp.)
- **9A.5 [OPEN]** (P6): prove Hodge-Riemann for the decorated arithmetic lattice. This is M4. Not scheduled as a finite milestone; it is the open kernel.

## 6A. The 9A.1-9A.3 attempt (2026-06-14): the gap narrows to P3

A first instantiation run ([`../../../experiments/arithmetic_geometric/e2uu_ahk_lattice_attempt.py`](../../../experiments/arithmetic_geometric/e2uu_ahk_lattice_attempt.py), LEARNINGS #105) executed 9A.1-9A.3 on the smallest case, and the result sharpens this spec:

- **9A.3 verified (FF).** On NS($C\times C$), genus 1: the degree map gives $\Gamma\cdot\Delta = \#C(\mathbb{F}_q) = q+1-t$ (P3 holds, carries $t$) and the primitive form is negative-definite iff $|t|<2\sqrt q$ (P6 = the Weil bound). The spec is right where M4 is a theorem.
- **9A.1-9A.2 done (abstract lattice).** The Boolean lattice $B_2$ on $\{2,3\}$ has P1 (the rank-generating polynomial $(1+x)^2$ factors over the atoms) and P2 (Whitney $(1,2,1)$, rank-symmetric). P4 and P5 hold by AHK + #48 -- **but P5 is unconditional, i.e. t-blind**, and the degree map is a combinatorial integer with no $t$-slot: **P3 fails.**
- **The gap is P3.** The bare combinatorial lattice already supplies P1, P2, P4, P5; the single missing property is the **t-carrying degree map** (P3), and P3 is what makes P6 (the primitive polarization) t-dependent and RH-meaningful. **P5 is demoted:** the $(1,n-1)$ signature is free and t-blind (#48), not the discriminator; the earlier P5 wording ("the *primitive* form is indefinite $(1,n-1)$") is corrected -- the $(1,n-1)$ is the *full* form, the *primitive* part is negative-definite and IS the polarization (the carries-$t$-not-definite-vs-indefinite refinement, #101/e2qq).

So the BUILDER target narrows from "build a 6-property object" to **"build a graded prime-lattice whose degree map yields $q+1-t$"**; everything else is combinatorial. P3 (over $\mathbb{Z}$: an arithmetic intersection theory whose Lefschetz numbers are the local Frobenius traces) is the AHK face of the M4 coupling (#104). This is the one place to spend construction effort; do not work P1/P2/P4/P5.

## 6B. The breadth-fingerprint re-derivation, and the genus-1 faithfulness caveat (2026-06-25, #122)

A second pass ([`e2ww_ahk_tslot_flip.py`](../../../experiments/arithmetic_geometric/e2ww_ahk_tslot_flip.py), LEARNINGS #122) ran the Breadth Program's converged M4-polarity **fingerprint** ([`../breadth_program.md`](../breadth_program.md), #120/#121) on the FF/genus-1 primitive form. The form is the **master transfer-candidate** (it passes the corpus `battery()` computationally) and its off-line flip is on the **sign** (passing the #121 selection-not-sign screen Bridgeland failed), so the breadth direction independently **recovers this spec's target object and the same constructible gap, P3**. That convergence is the whole positive content, and it is a connection, **not** an advance.

Two corrections it forces on any future BUILDER work here (adversary-verified):

1. **The arithmetic is the JOINT Gram, not one number.** A first-pass claim that "the arithmetic localizes to the single off-diagonal coupling $s=t$" is **false**: the diagonal $b=2gq$ carries $q$ (the flip threshold $2g\sqrt q$ moves with $q$), and the complex-root / fixed-locus structure requires the functional-equation relation $ab=4g^2q$. P3 is the joint arithmetic Gram $(2g,2gq,t)$, consistent with #104.
2. **The faithfulness caveat (load-bearing).** Genus 1 is the *easiest* Weil case: the $2\times2$ negative-definiteness is just $\det>0$ for a binary quadratic form, which **Hasse proved in 1933** from norm-form positivity, before Weil, with no Hodge index theorem. So in the genus-1 shadow P6 looks automatic the instant P3 is supplied, which is an **artifact**. The genuine M4 difficulty (higher-**rank** Rosati positivity on a $>2$-dimensional primitive part, the archimedean $\Gamma_S$ place, the global $S\to\infty$ assembly) is exactly what the $2\times2$ genus-1 form discards. The breadth fingerprint is therefore a **genus-1-faithful shape**, necessary but silent about where M4 is actually hard; "the fingerprint localizes M4" must not be read as "M4 is elementary once P3 is supplied." The Section-7 compatibility question stays the open kernel.

## 7. Honest scope and probability

The probability that (P6) falls easily is low (single digits), the same order as Direction 8.A: (P6) IS the arithmetic Hodge standard conjecture, and no road has produced it. What this spec changes is the **shape of the remaining work**, and that is real progress in the project's sense (a coordinate that narrows the search):

1. It replaces "build a variety" with "build a finite lattice plus a submodular function," a strictly smaller and fully explicit ask. (P1)-(P5) are checkable on tiny cases by hand or by a short script.
2. It isolates the open part to a single named property (P6) with a clean function-field shadow (K3, 9A.3) that can kill a wrong construction same-day.
3. It encodes the three hard-won kills (#40 $t$-blindness, #97 indefinite-gate, #97 euler-archimedean) as *requirements* (P3, P4, P5), so any object built to this spec cannot repeat them. The earlier Direction 9 failure (a $t$-blind, definite, log-concavity detector) is now structurally excluded by the spec itself.

The risk the spec honestly carries: (P3)-(P5) may be jointly **unsatisfiable by any AHK-machinable lattice**, i.e. the arithmetic decoration that carries $t$ and forces the indefinite native form might be exactly what destroys (P1)'s product structure or (P4)'s submodularity. If so, that is itself a sharp coordinate: it would say the AHK route cannot source the polarization without a variety after all, pushing the program onto the Arakelov face (Section 5) or the still-unspent regime-two frame-audit axis (#97). Either way the search narrows. The object is a target, not a monument.

## 8. References and cross-refs

- Adiprasito, K.; Huh, J.; Katz, E. (2018). *Hodge theory for combinatorial geometries*. Ann. Math. 188(2), 381-452. (P1, P4, P5; Lemma 9.6.)
- Braden, T.; Huh, J.; Matherne, J.; Proudfoot, N.; Wang, B. (2020-22). *Semismall decomposition / singular Hodge theory of matroids*. (The product/semismall structure for P1.)
- Faltings, G.; Hriljac, P. (Arakelov intersection / height pairing). (The Arakelov face, Section 5.)
- Project: [`08A_rosati_standard_conjecture.md`](08A_rosati_standard_conjecture.md) (M4, the M1-M5 ladder), [`09_arithmetic_matroid_li.md`](09_arithmetic_matroid_li.md) (the parent direction this sharpens), [`08_hodge_index_surface.md`](08_hodge_index_surface.md) (the variety route this avoids), [`../all_roads_to_the_signature.md`](../all_roads_to_the_signature.md) (the thesis), [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md) (the scorecard).
- Findings: [LEARNINGS](../../../experiments/LEARNINGS.md) #97 (the sweep that produced this spec), #40 (the $t$-blindness coordinate), #27 (the original Direction 9 kill: log-concavity is a non-Euler detector), #96 (the off-line-flip test, the K1 sanity check), #18-20 (marginal positivity).
- Experiments: [`e3n_li_signature.py`](../../../experiments/positivity/e3n_li_signature.py) (the Direction 9 falsification), [`offline_flip_test.py`](../../../experiments/positivity/offline_flip_test.py) (#96, the K1 flip test), e2g / 2G (the function-field Hodge index, the K3 shadow), [`../../../experiments/lemma_db/transfer_search.py`](../../../experiments/lemma_db/transfer_search.py) (the corpus, which now records the Boucksom-Jonsson kill).

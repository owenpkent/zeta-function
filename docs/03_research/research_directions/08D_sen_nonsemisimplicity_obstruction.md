# Direction 8D: The Sen non-semisimplicity is not the obstruction. A compact-group theorem closes the "polarize the Sen module" branch and relocates M4 to the Frobenius half.

> **Lane 2 deliverable** (isolable, valuable regardless of RH). Audits the load-bearing assumption of [`08B_bhatt_lurie_wcart_signature.md`](08B_bhatt_lurie_wcart_signature.md) against Petrov's non-semisimplicity theorem, and answers the open probe the 2KK ADVERSARY flagged.
> **Companion experiment**: [`experiments/arithmetic_geometric/e2sen_polarization_obstruction.py`](../../../experiments/arithmetic_geometric/e2sen_polarization_obstruction.py).
> **Prior coordinates credited and unified here**: LEARNINGS #66 (2KK, Hodge-star cup is hyperbolic), #67 (2LL, monodromy primitive form as formalism), #68 (2MM, that form is a transport theorem).
> Written 2026-06-05.

## 0. The one-line result

A non-semisimple Sen operator (Petrov, [arXiv:2302.11389](https://arxiv.org/abs/2302.11389)) admits **no positive-definite invariant cup form**, by a one-line compact-group argument. So the polarization RH needs can never be *sourced* from the archimedean Sen structure $\Theta$; it can only be *imported* onto primitive graded pieces (the transport of LEARNINGS #68), and the imported datum is the arithmetic ample class $=$ RH, living on the Euler/Frobenius half that $\Theta$ does not see. This is **routable, not fatal** to 08B, and it is **not progress on (B)**: it prunes the "polarize the Sen module" sub-branch of M4 and redirects the positivity demand to the $F$ side.

## 1. The question (Lane 2)

08B §3-4 asks the Sen operator $\Theta$ on the diffracted Hodge complex to (i) "act on the $n$-th conjugate graded piece by multiplication by $-n$" (a clean weight grading) and (ii) "force the alternating sum of traces to be positive-definite on primitive cohomology" (the polarization, step (4)(b)). Step (ii) presupposes that $\Theta$ is **semisimple**: only a semisimple operator has an eigenspace decomposition on which one can place a Hodge-Riemann form weight-by-weight.

Petrov proves that presupposition false. His theorem: there exist $W_2(k)$-liftable smooth projective varieties of dimension $p+1$ whose Hodge-to-de Rham spectral sequence does not degenerate, and correspondingly **the Sen operator is non-semisimple**. The "$-n$ on the graded piece" is $\mathrm{gr}(\Theta)$, the associated graded; the true operator
$$\Theta = \Theta_{\mathrm{ss}} + \nu, \qquad \nu \ne 0 \text{ nilpotent},$$
carries genuine Jordan blocks whose nilpotent part $\nu$ connects distinct Hodge-Tate weight spaces.

The 2KK ADVERSARY (LEARNINGS #66) reached exactly this crux and left it open:

> "the Petrov non-semisimplicity crux (arXiv:2302.11389, the actual content of the probe) is NOT exercised ... a real [defective Jordan block] DESTROYS the cup form ($B=0$). ... The genuine open question Petrov poses, can an intrinsic positive cup form survive a non-semisimple Sen module, remains untested and is the next honest WCart probe."

This direction answers that question.

## 2. The theorem: $\nu \ne 0 \Rightarrow$ no positive-definite cup form

The Tate-equivariant cup duality (the pairing $H^1 \otimes H^1 \to H^2$ into the weight-$(-w)$ Euler pole; 08B / 2KK use $w = 1$) is
$$\Theta^{\mathsf T} B + B\,\Theta = -w\,B. \tag{$\star$}$$
Rewrite $(\star)$ by shifting $\Theta$ to the Tate center:
$$\bigl(\Theta + \tfrac{w}{2} I\bigr)^{\mathsf T} B + B\bigl(\Theta + \tfrac{w}{2} I\bigr) = 0,$$
which says precisely that $\Theta + \tfrac{w}{2} I \in \mathfrak{so}(B)$, the Lie algebra of the isometry group $O(B)$. Now:

> **Theorem (compact-group obstruction).** If $B$ is positive-definite, then $O(B) \cong O(n)$ is **compact**, so $\mathfrak{so}(B)$ consists of $B$-skew operators, all of which are **semisimple** (diagonalizable over $\mathbb C$, imaginary spectrum). Hence $\Theta + \tfrac{w}{2} I$ is semisimple, so $\Theta$ is semisimple, so $\nu = 0$.
>
> **Contrapositive:** $\nu \ne 0 \;\Rightarrow\;$ there is no positive-definite $B$ solving $(\star)$.

A nonzero nilpotent cannot be an infinitesimal isometry of a definite form. That is the whole proof. The non-semisimplicity of the Sen operator is therefore exactly an obstruction to a *global* positive cup form: it forces you out of "definite form on the whole space" and into the monodromy-weight / primitive-graded (Hodge-Riemann) formulation, where definiteness is asked only of the form on primitive pieces, not of the global cup.

## 3. The existence trichotomy (unifying #66 and #68)

$(\star)$ has a nonzero solution iff the eigenvalues of $\Theta$ resonate, $\mu_i + \mu_j = -w$. Combined with the theorem, a genuine size-$\ge 3$ Jordan block falls into exactly one of three regimes. The companion experiment solves $(\star)$ as a homogeneous Sylvester system and reads the inertia (`numpy`, exact up to float tolerance):

| regime | $\Theta$ (size-3 blocks) | solution dim | inertia | definite? | identity |
|---|---|---|---|---|---|
| semisimple control | $-\tfrac12 I_3$ ($\nu=0$) | 6 | up to $(3,0,0)$ | **YES** $(3,0,0)$ | a definite form exists |
| self-paired | $-\tfrac12 I_3 + N_3$ ($2\mu=-w$) | 2 | $(1,2,0)$ | NO | sign imported = **#68 transport** |
| cross-paired | $0\!\cdot\!I_3{+}N_3 \oplus -I_3{+}N_3$ ($\mu_1{+}\mu_2{=}{-}w$) | 3 | $(3,3,0)$ | NO | hyperbolic, wrong polarity = **#66** |
| non-resonant | $-I_3 + N_3$ | 0 | $B=0$ | NO | the **2KK "$B=0$"** |

Reading. The only configurations that even admit a pairing are self-paired (indefinite; its sign is the free scalar that #68 showed is imported, not intrinsic) and cross-paired (hyperbolic; the wrong-polarity $(k,k)$ split that #66 found at rank 2, here at rank 6). Turning on $\nu$ collapses the 6-dimensional space of forms at $\mu = -\tfrac12$, which **contains the positive-definite identity**, down to a 2-dimensional family with **no definite element**. The "$B=0$" the 2KK adversary hit is simply the non-resonant placement.

**Answer to the 2KK probe: NO.** No intrinsic positive cup form survives a non-semisimple Sen module, in any of the three regimes. The compact-group theorem is the reason #66 and #68 are the only outcomes the project ever found: a definite outcome is forbidden by linear algebra the moment $\nu \ne 0$.

## 4. Is it routable? Yes, and the routing imports the gap

The standard fix for a non-semisimple weight operator in Hodge theory is to stop asking the global form to be definite and instead use the **monodromy-weight filtration** $M(\nu)$ (Jacobson-Morozov: every nilpotent $\nu$ has a unique increasing filtration with $\nu M_k \subseteq M_{k-2}$ and $\nu^\ell : \mathrm{Gr}^M_\ell \xrightarrow{\sim} \mathrm{Gr}^M_{-\ell}$). On the $\nu$-primitive parts $P_\ell = \ker(\nu^{\ell+1} : \mathrm{Gr}_\ell \to \mathrm{Gr}_{-\ell-2})$, the Cattani-Kaplan-Schmid polarization (Schmid 1973; [Cattani-Kaplan, *Invent. math.* 67 (1982) 101-116](https://link.springer.com/article/10.1007/BF01393374); CKS 1986) is
$$Q_\ell(x, y) = Q\bigl(x,\ \nu^\ell\, y\bigr), \qquad \text{positive-definite on } P_\ell \text{ (up to the Weil-operator twist).}$$

So $\nu$ being non-semisimple is **not fatal**: the filtration formulation absorbs the Jordan blocks, and 08B step (4)(b) survives once rephrased on $M(\nu)$ rather than on $\Theta$-eigenspaces.

But the routing imports the very thing that is RH. In $(Q_\ell = Q(\cdot, \nu^\ell\cdot))$, the nilpotent $\nu$ supplies the perfect pairing $\nu^\ell : P_\ell \cong P_{-\ell}^*$ (rung (ii), free), while the **positive form $Q$ is an input**. In geometry $Q$ is the polarization of the nearby smooth fibers of a degenerating variation of Hodge structure; CKS *transport* it through the degeneration. The nilpotent organizes weights; it never manufactures $Q$. This is the same conclusion #68 (2MM) reached for the $N^2=0$ case, now established at the genuine-Jordan level and explained by the compact-group theorem: positivity is structurally external to the Sen module.

Over $\mathrm{Spec}(\mathbb Z)$ there is no ambient polarized VHS to transport from. Supplying $Q$ is supplying the arithmetic polarization, which is RH. Equivalently, in the Lefschetz reading, $\nu$ would have to be cup-with-an-ample-class backed by an arithmetic Hodge index theorem; that ample class is the program's universal gap (rung (iii)). Either reading relocates the demand; neither fills it.

## 5. D-H reasoning: this whole analysis is on the K2-shared half (by type)

$\Theta$ (hence $\nu$) is the **archimedean / Hodge-Tate-weight** operator. By kill criterion K2 the discriminating sign must ride the Euler/Frobenius half $F$ (the $\{\log p\}$ / von Mangoldt trace), not the shared archimedean block. So Petrov's obstruction is on the half that *cannot* separate $\zeta$ from Davenport-Heilbronn. The companion run confirms this directly at $\ge 40$ digits:

- **Rung (ii) is free for both.** Functional-equation residual at $s = 0.3 + 7i$: $|\Lambda(s) - \Lambda(1-s)|_\zeta \approx 1.8\times 10^{-43}$ and $|f(s) - \chi f(1-s)|_{\mathrm{DH}} \approx 1.1\times 10^{-40}$. The FE / archimedean / Sen structure is identical-by-type for $\zeta$ and D-H; it does not separate them. Petrov's $\Theta$-obstruction lives here, so resolving it cannot be the discriminator.
- **Only $F$ separates them.** $\zeta$: the coefficients of $-\zeta'/\zeta$ are von Mangoldt $\Lambda(n)$, supported on $\{2,3,4,5,7,8,9,11,13,\dots\}$ $=$ exactly the prime powers (Euler product / Frobenius $F$ present). D-H: the period-5 coefficients $a(n) = [1,\xi,-\xi,-1,0]$ are **not multiplicative**, e.g. $a(6) = +1$ but $a(2)a(3) = -\xi^2 = -0.0807$. No Euler product $\Rightarrow$ no Frobenius $\Rightarrow$ the polarizable algebra is uninhabited for D-H **by type**.

**D-H verdict: by type.** D-H has the same archimedean $\Gamma$-factor, hence the same Sen/weight structure, hence the same Petrov obstruction. It is not that D-H fails a test $\zeta$ passes; the test is on the shared block and is blind to the difference. This is why the result is recorded as a negative coordinate, not a discriminator.

## 6. Kill criteria and milestone placement

| criterion | status | why |
|---|---|---|
| **K1 (non-circular)** | PASS | The theorem and trichotomy are pure structure on $\Theta$; no zero locations are used as input. |
| **K2 (D-H exclusion rides $F$)** | AFFIRMED | The finding *is* that $\Theta$ is the shared archimedean half and cannot carry the sign. It provides no discriminator and says so. It corroborates K2 rather than violating it. |
| **Marginal-positivity** | CONSISTENT | No soft positivity is claimed. The obstruction relocates to the arithmetic ample class on the $F$ side, where the $\exp(-4\pi x)$ margin lives. |
| **Freeze list** | CLEAR | This is a negative result *about* the operator-identity / Lefschetz re-encoding (it shows that re-encoding imports the polarization), not a proposal that prices in soft positivity, fires for D-H, or recovers only the sign. |

**Milestone: M4, negative coordinate.** 08B is not killed; its load-bearing assumption is corrected. Step (4)(b) must be rephrased on the monodromy-weight filtration $M(\nu)$ of the non-semisimple Sen operator, and its positivity input must come from an arithmetic ample / Lefschetz class riding the Euler-pole $H^2$ (the $F$ half), which Petrov's theorem leaves entirely untouched. The sub-branch this prunes is "obtain the M4 polarization by fixing or decomposing the Sen grading." That branch is closed: by the compact-group theorem there is no global definite Sen-invariant form, and by the transport theorem (#68, generalized here) the primitive-piece form is always imported.

## 7. The one-line test, answered honestly

> Did I produce a polarization with a geometric source that separates $\zeta$ from Davenport-Heilbronn, or another trace / statistic / restatement dressed as positivity?

**Neither.** I produced a structural **negative result**: a compact-group theorem proving the non-semisimple Sen module carries no intrinsic positive cup form (answering the 2KK probe NO and unifying #66 and #68 as its only two non-trivial outcomes), with the D-H control showing the obstruction sits on the shared archimedean half.

**Coordinate recorded.** In the archimedean / Sen ($\Theta$) basis, non-semisimplicity is a transport-and-filtration phenomenon, never a positivity source: a global definite invariant form is forbidden ($\nu \ne 0$), and the primitive-piece form is imported ($=$ RH). The positivity the proof needs must be an arithmetic ample class on the Euler-pole $H^2$, riding the Frobenius $F$ / $\{\log p\}$ half that $\Theta$ does not see. "Polarize the Sen module" is a dead sub-branch of M4. The live front is unchanged and now sharper: construct the ample class on the $F$ side and prove its Hodge index positivity (rung (iii)).

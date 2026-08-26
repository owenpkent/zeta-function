# F2a: the correlation-certificate class $\mathcal{C}$, posed

> **Status: PROPOSED (pre-adversary).** BUILDER deliverable, 2026-08-26, frame session F2a
> of the funding-boundary frame ([`successor_frame_deliberation.md`](successor_frame_deliberation.md)
> Sections 4 and 7; scope rulings in [`funding_boundary_audit_1.md`](funding_boundary_audit_1.md)
> per LEARNINGS #209). This document POSES the certificate class; it attacks nothing and
> proves nothing. Per the frame spec, the posed definition goes to a same-session ADVERSARY
> before any theorem-shape work starts; Section 7 is written for that adversary. The GLSS
> prep block rode inside this session
> ([`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md))
> and the AF Lean repository skim rode as the pattern library
> ([`reading_notes/af_lean_repository_skim.md`](reading_notes/af_lean_repository_skim.md)).
> No em dashes anywhere.

**The question this class formalizes**, verbatim from the frame registration
([`successor_frame_deliberation.md`](successor_frame_deliberation.md) Section 4, Wall 2):

> can ANY sequence of finite-rank certificates whose inputs are prime-correlation data
> (any support, granted freely) certify location-completeness in the limit; and if not, is
> the thing the limit certificate needs beyond correlations exactly the
> uniformity/determinant-class clause (#148), i.e. M4 seen from the counting side?

Nothing in print poses this class (certified unoccupied:
[`reading_notes/proportion_support_landscape.md`](reading_notes/proportion_support_landscape.md)
Section 7, gap 5; the three nearest in-print objects are AF's in-mechanism ceiling, the
GLSS full-funding saturation, and the Lagarias-Rodgers non-decidability certificate, none
of which quantifies over the class). The definitional strategy throughout is the
Alpöge-Furman quarantine style (pattern P2 of the Lean skim): the class is an INTERFACE,
stated as a named bundle of structural clauses plus a named data pool; a certificate is
anything a prover can build over that interface; ingenuity inside the interface is
deliberately unrestricted.

---

## 1. The class, defined

$\mathcal{C}$ is defined by five named clauses: C0-FRAME (the structural interface),
C1-OBJ (the objects), C2-FUND (the funding clause), C3-OUT (the output clause), C4-LIM
(the limit clause). Each clause is a separate attack surface; each definitional choice
carries its stated reason.

### C0-FRAME: the structural interface (what is free, before any data)

A certificate operates on an abstract zero configuration in the AF `ZeroConfig` style
(pattern P1: "they contain no arithmetic"): a multiset $\mathcal{Z}$ of strip points
$\rho = \beta + i\gamma$, $0 \le \beta \le 1$, with multiplicities $m_\rho \ge 1$, closed
under the functional-equation pairing $\rho \mapsto 1 - \bar\rho$ with
$m_{1-\bar\rho} = m_\rho$, finite in every window, and carrying a Riemann-von
Mangoldt-class counting frame: $N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + S$-corrections
with $S \ll \log T$. The frame also carries the archimedean ($\Gamma$-factor) facts of the
completed function. Every structural consequence of C0 is free to the certificate:
reflection symmetry, the four-fold zero classification, the horizontal-multiplicity
combinatorics (an off-line zero forces its partner onto the same horizontal line), inertia
typings of FE-paired blocks, Lebesgue bookkeeping.

*Choices and reasons.* (i) The frame is configuration-abstract because both boundary
engines prove their zero-side steps at exactly this level (AF's `ZeroConfig` with the
zero side "containing no arithmetic"; GLSS's Section 2 classification and Proposition 1
are FE + measure bookkeeping): the class must not be narrower than its own record
holders. (ii) The frame deliberately does NOT contain the Weil explicit formula as an
exact identity. The exact EF against the true primes determines the configuration
outright (the zeros are determined by the primes), so a frame carrying it would collapse
configuration-abstraction and, with it, the entire class question; EF-derived information
enters only through C2's finite, error-carrying reads. This is a load-bearing exclusion,
stated here so the adversary can attack it rather than discover it. (iii) The
Davenport-Heilbronn configuration satisfies C0 verbatim (real coefficients, the
$s \mapsto 1-s$ FE, RvM-class frame: [`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
Section 3(a)); a Beurling system does not (no FE): the frame is where the discipline
bracket's two arms already separate (Section 4).

### C1-OBJ: the objects

A member of $\mathcal{C}$ is a sequence, indexed by $T \to \infty$ (or by windows
$[T, 2T]$; the two indexings are interchangeable for C4 and both are admitted), of
**finite-rank certificates**: at each $T$, a Hermitian form $Q_T$ of finite rank
$d(T) < \infty$ built over C0-FRAME data (vectors indexed by configuration points,
kernels on ordinate gaps, or any other finite-rank device), together with a finite
derivation that combines (a) structural facts from C0, (b) finitely many funded reads
from C2, and (c) arbitrary proven mathematics that touches the configuration ONLY through
(a) and (b), into an output statement of type C3.

*Choices and reasons.* (i) **Rank may grow without restriction.** The AF compression at
$d \asymp N(T, 2T)$ must be in-class, and any no-go that secretly needed bounded rank
would be attacking a strawman. (ii) **Kernel functionals are in-class through their
finite-rank realizations.** The GLSS/Gallagher-Mueller engine reads Fejér-weighted pair
sums $\sum_{\gamma,\gamma'} K((\gamma-\gamma')L)$ with bandlimited $K$; a bandlimited
kernel at height $T$ is realized at finite rank (this is literally what the AF Gabor
compression does to Weil's form), so the second-moment engine sits inside C1. What C1
excludes is only the genuinely infinite-resolution object at fixed $T$: an exact
infinite-rank identity consumed as such, which is the object-side face of the same
exclusion C0(ii) makes on the data side. (iii) The derivation itself is unrestricted
mathematics: no clause anywhere in $\mathcal{C}$ restricts the prover's methods, only the
interface through which the configuration and the primes are seen (this is the too-broad
guard's discipline, Section 3(b)).

### C2-FUND: the funding clause (the admissible data pool $\mathcal{P}$)

Every quantitative input to the certificate's output inequality that is not a C0
structural fact must be a **pool read**. The pool $\mathcal{P}$ has two parametrizations
and one grant syntax.

**$\mathcal{P}_{\mathrm{zero}}$ (zero-side parametrization).** Correlation functionals of
the configuration's **vertical marginal** (the ordinate multiset $\{\gamma\}$, with
multiplicity, of all strip points, wherever $\beta$ sits): weighted $n$-point
gap-counting functionals at the $TL$ normalization ($L = \frac{1}{2\pi}\log T$), with
arbitrary weights and arbitrary gap-scale support, including as special cases Montgomery's
$F(\alpha)$ at any $\alpha$, the pair-count $N(\lambda)$ at any $\lambda$ (fixed or moving
with $T$ per GLSS Remark 1), binned AH densities $P_{k/2}(T)$, the equal-ordinate count
$N^{\circledast}(T)$, and $n$-level analogues for every $n$. Admission is **law-blind**:
PCC in the GUE shape, AH-Pairs plus AH-Weak Density in the quasi-lattice shape, the
$\mathbf{C}$-ladder hypothesis $N^{\circledast} \le (\mathbf{C}+o(1))TL$, or any other
asserted law of the marginal enters on equal syntactic terms. Reason: the boundary
theorems are law-indifferent (GLSS I and II derive the identical conclusion from two
mutually contradictory laws; the mechanism consumes one linear functional of the
correlation measure, not the law's shape:
[`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
Section 4), so a law-typed pool would misdescribe the boundary.

**$\mathcal{P}_{\mathrm{prime}}$ (prime-side parametrization).** Correlation families of
the rational primes at integer shifts: the family $\{B_X(h)\}$,
$B_X(h) = \sum_{n \le X} \Lambda(n)\Lambda(n+h)$, any shift range $h \le H$, any support
$X$ relative to $T$ (in particular past the Fourier-support-1 wall $X \asymp T$), with
Hardy-Littlewood-class asymptotics $B_X(h) = \mathfrak{S}(h)X + o(X)$ (uniformity over
$h \le H(X)$ as stated in the grant), including **full HL\*** and the graded HL\*($k$)
rungs of the AF conditional table; equivalently, short-interval variance functionals of
$\psi$ (the Goldston-Montgomery parametrization of the same currency). The e1af
derivation ([`../../experiments/spectral/e1af_funding_wall.md`](../../experiments/spectral/e1af_funding_wall.md)
Section 2) is the in-repo statement of exactly which such reads the compressed form's
off-diagonal consumes at support $1+\delta$ (shifts $h \le H(\delta) \asymp X/T$ at
weight $\log(H/h)$).

**Both parametrizations are first-class.** The frame question names "prime-correlation
data"; the class widens this to correlation data in either parametrization, for a
measured reason: the actual full-funding boundary theorems (GLSS I/II) are funded
zero-side, and the only in-print bridge between the parametrizations, the
Goldston-Montgomery dictionary (SPC $\iff$ short-interval prime variance), is proven only
under RH; GLSS II avoids the $F(\alpha)$ route explicitly BECAUSE it costs RH. A
prime-only pool would therefore exclude the class's own ceiling inhabitants
([`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
Sections 1.2 and 5, item 1). The GM dictionary is noted inside the class as the
RH-priced bridge; whether an unconditional bridge exists is exactly the Mueller 1983
pointer (Section 6, item 5).

**The grant syntax (G-LAW), and what "granted freely" means.** A pool grant is the TRUTH
of an asymptotic LAW, assumed as an input hypothesis; not its proof, and not a per-$T$
oracle. Precisely: a grant is a statement of the form "$\Phi_T = M(T) + E(T)$ as
$T \to \infty$, with $E$ in the stated error class", for an admissible functional family
$\{\Phi_T\}$ and a stated main term $M$; the certificate may cite the law at any $T$ but
inherits the law's error class wherever it does. Error classes admitted: **o-class only**:
$o(TL)$ at the $TL$ normalization on the zero side (equivalently vanishing relative
error), $o(X)$ per shift on the prime side. Power-saving and square-root error classes
are excluded from the default pool, for a specific reason: the Montgomery-Soundararajan
uniform square-root HL hypothesis has as its $k = 1$ member a statement "equivalent to
the Riemann Hypothesis" (landscape row E5), so a pool admitting square-root grants
admits RH itself as a data item and the class question collapses by smuggling. The
excluded sub-pool is named as an optional labeled extension in Section 6, item 6, with
the collapse-prevention restriction spelled there. Two further syntactic consequences,
both deliberate:

- **No fixed-height reads.** Grants are laws in the running variable; a functional
  pinned at a fixed height, cited inside a growing-$T$ sequence, has no $TL$-normalized
  law and is not grantable. Without this clause a diagonalization leak opens (read a
  fixed integer count with an error floor that shrinks as the ambient $T$ grows, until
  the o-class error drops below $1$ and the read becomes exact); with it, every read
  carries slack at its own scale, always.
- **Granted subsets must be consistent.** PCC and AH contradict each other; a
  certificate selects a consistent grant set $G \subset \mathcal{P}$ and is a theorem
  modulo $G$. The class question quantifies over all consistent $G$ (this is how
  law-blindness and "granted freely, any support" are made precise simultaneously).

**The proven core.** Pool-shaped statements that are proven (Fujii's second moment,
BGSTB's unconditional $F(\alpha)$ on $[0,1]$, the Montgomery-Vaughan-funded diagonal
budgets, Gallagher's $\sum_{h\le y}\mathfrak{S}(h) = y(1+o(1))$) are free: admissibility
is by SHAPE and error class, not by epistemic status. This is what makes AF's Theorem A a
class member that consumes an EMPTY conjectural grant set: all its funding is proven
pool-shaped data at support $\le 1$.

### C3-OUT: the output clause

A certificate's output at height $T$ is a certified inequality on the counting register
of the configuration: lower bounds on good counts (simple-and-on-line $N_0^s$, on-line
$N_0$, distinct $N_d$) and/or upper bounds on defect functionals (the
multiplicity-weighted $N^*$, the equal-ordinate pair count $N^{\circledast}$, the excess
$E(T) := N^{\circledast}(T) - N(T) = \sum_{\text{lines}} h(h-1)$, off-line counts
$N_{\mathrm{off}}$, small-gap counts), each with its own stated error class. Both
record shapes are in-class by inspection: the AF shape
$N_0^s \ge (2 - R(\psi) - o(1))N$ and the GLSS shape $E(T) = o(TL)$ (equivalently
$\#\{\text{simple critical}\} \ge 2N - N^{\circledast} = (1+o(1))N$).

*Choice and reason.* C3 types the STATEMENTS a certificate may certify; it does not
restrict their error class. In particular an absolute-count output ($E(T) < 2$) is
syntactically well-formed C3 output. Whether any member ACHIEVES one is the F2b
question; a definition that excluded absolute-count outputs by fiat would make the no-go
true by construction and worthless.

### C4-LIM: the limit clause ("certify location-completeness in the limit")

The completeness functional is $E(T) = N^{\circledast}(T) - N(T) = \sum_{\text{lines}}
h(h-1)$, where $h(\gamma)$ is the multiplicity mass on the horizontal line $t = \gamma$.
Three register facts, each a finite lemma (VERIFIER targets, Section 8): $E$ is
nondecreasing in $T$; each term $h(h-1)$ is even, so $E(T) < 2 \iff E(T) = 0$; and every
off-line zero and every multiple zero lies on a line with $h \ge 2$, so
$N_{\mathrm{off}}(T) + N_{\mathrm{mult}}(T) \ll E(T)$.

**Definition (C4).** A member of $\mathcal{C}$ *certifies location-completeness in the
limit* if its certified outputs, as theorems over C0 + proven core + its grant set $G$,
imply: there exists $T_0$ such that $E(T) < 2$ for all $T \ge T_0$. By monotonicity and
integrality this is equivalent to $E \equiv 0$: every zero of the configuration is simple
and on the critical line.

Named companion registers, with implications stated:

- **C4-loc** (location proper): eventually $N_{\mathrm{off}}(T) < 1$, i.e.
  $N_{\mathrm{off}} \equiv 0$: RH itself, multiple on-line zeros tolerated. C4 $\Rightarrow$
  C4-loc; not conversely.
- **C4-fin** (cofinite completeness, the weak register): $E(T) = O(1)$: all but finitely
  many zeros simple and on-line. C4 $\Rightarrow$ C4-fin. A no-go at C4-fin is the
  strongest of the three (it rules out even bounded-defect certificates) and is the form
  F2b should attempt first; a no-go at C4 alone is the minimum.

**The register choice, stated prominently.** C4 is posed at the ABSOLUTE-COUNT register,
NOT at density 1, because at the density register the class question is already closed in
print: GLSS I certifies density-1 simple-and-on-line from full-support PCC without RH,
GLSS II certifies the same from the contradictory AH law, and the $\mathbf{C}$-ladder
(GS25) reaches density 1 at its $\mathbf{C} = 1$ endpoint with completeness at NO rung.
A density-register class question would close trivially at the wrong register
([`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
Sections 2 and 5, item 2). The certified quantity and the completeness quantity are the
SAME functional $E(T)$ at two error classes, $o(TL)$ certified versus $< 2$ needed: the
class question is whether any member crosses that error-class gap.

The primary register is $E$ (not $N_{\mathrm{off}}$) because $E$ is the boundary
engines' own certified observable: the mechanism cannot separate off-line pairs from
multiple zeros (both cost one unit of excess $H$ per line, with no $\beta$-localization),
so the register in which the in-print ceiling is stated, and hence in which the gap is
cleanest, is $E$. The cost of this choice (C4 contaminates location with simplicity) is
carried honestly by naming C4-loc and requiring F2b's no-go to cover it (Section 7,
item 1).

### What the class does NOT restrict (deliberate generosity)

Test functions and weights (any); bandwidth and Fourier support (any: the pool grants
correlation data at ALL supports freely); compression geometry (Gabor, wavelet, moment,
anything); rank growth $d(T)$ (any); number of pool reads per $T$ (finite, unbounded);
the granted law (any consistent set); the windowing ($[0,T]$ or $[T,2T]$); and, above
all, the prover's mathematics between interface and output. The no-go, if it lands, must
beat the strongest member, and every generosity removed here would be a soft spot in the
theorem; every restriction $\mathcal{C}$ does impose is on DATA (which functionals, which
normalization, which error class), never on inference.

---

## 2. The boundary inhabitants (calibration: the class is non-empty, and its in-print ceiling is density 1)

| Engine | Grant set $G$ consumed (beyond the proven core) | Object shape | Certified output | Register |
|---|---|---|---|---|
| Montgomery 1973 | RH (a $\beta$-resolved hypothesis: NOT pool-admissible) | Fejér pair bound | $N_s \ge (2/3 - o(1))N$ | out-of-class as stated; content absorbed unconditionally by AF |
| Alpöge-Furman Thm A ([`reading_notes/alpoge_furman_two_thirds.md`](reading_notes/alpoge_furman_two_thirds.md)) | EMPTY (proven pool-shaped funding at support $\le 1$ only) | rank $d \asymp N(T,2T)$ Gabor compression of Weil's form; inertia + rank-trace | $N_0^s \ge (2 - R(\psi) - o(1))N$: $2/3$; $0.6725$ at MT; $5/6$ distinct | density |
| AF HL\*($k$) rungs | $\mathcal{P}_{\mathrm{prime}}$ at growing support | same | $13/18$ at HL\*(4); $100\%$ SIMPLE at full HL\* ("RH itself is out of reach of the mechanism") | density |
| GGOS shadow | the $F$ lower bound $F(\alpha) \ge \tfrac32 - \alpha - \epsilon$ on $[1, \tfrac32)$ granted directly as $\mathcal{P}_{\mathrm{zero}}$ data (in print it is bought with GRH, which is itself not pool-admissible) | window class / SDP | $N_s \ge 0.6845N$ (SDP-improved) | density |
| GLSS I ([`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)) | PCC: full-support pair law of the marginal at $o(TL)$, moving windows | second-moment kernel engine (finite-rank realizable) | $E(T) = o(TL)$, hence $100\%$ simple-and-on-line | density 1 (the ceiling) |
| GLSS II | AH-Pairs + AH-Weak Density (the contradictory law) | same | same conclusion; with (AH1) only: the $50/50$ rung ($\mathbf{C} \le 3/2$) | density 1 |
| $\mathbf{C}$-ladder (GS25) | $N^{\circledast} \le (\mathbf{C}+o(1))TL$, $1 \le \mathbf{C} < 2$ | linear exchange | proportion $\ge 2 - \mathbf{C}$ simple-and-critical | density; completeness at NO rung, including $\mathbf{C}=1$ |
| Lagarias-Rodgers | (not a certificate: the class's no-go PRECEDENT) | explicit AH-spaced point process | everything currently known about correlations cannot rule AH out | a counterexample-configuration at the "currently known" sub-pool |

Calibration readings. (i) $\mathcal{C}$ is non-empty and contains the record holder at
an empty conjectural grant set. (ii) The in-print in-class ceiling is exactly density 1
with an ineffective $o(N(T))$ residual, reached at full funding by two contradictory
laws; NO inhabitant reaches C4, C4-loc, or C4-fin. (iii) The class question is therefore
live at precisely the register C4 names, and the Lagarias-Rodgers row shows the no-go's
natural proof shape (a pool-consistent configuration with the wrong completeness
behavior) already has an in-print ancestor at a smaller pool.

---

## 3. The two failure modes, named and guarded

### (a) TOO NARROW: the no-go re-coats a proven blindness statement

The risk: if $\mathcal{C}$ quietly excludes the engines that DO extract location from
correlation data, the F2b "no-go" collapses to a restatement of #199 (the line-restricted
meter cannot see WHERE off-line zeros are:
[`../../experiments/arithmetic_geometric/e2bd_dh_invisibility.md`](../../experiments/arithmetic_geometric/e2bd_dh_invisibility.md))
or of the primes-thread GUE RH-blindness theorem (ordinate statistics unchanged, bit for
bit, when zeros move off the line), and fails the #201 derivability check on arrival.

The guard, and why it holds as posed: the vertical marginal DOES carry location
information, through the FE-forced ordinate coincidences (an off-line zero and its
partner share a $\gamma$, so off-line-ness is visible to the marginal as equal-ordinate
mass: $N^{\circledast}$ is a pool-shaped functional). The class as defined contains the
two engines that consume exactly that channel (GLSS through $N^{\circledast}$; AF through
inertia bookkeeping funded at support 1), and both PURCHASE location density from it.
So a valid F2b no-go over $\mathcal{C}$ cannot say "correlations see nothing" (false in
the class: they see density) and must say "density is purchasable, the last $o(N(T))$ is
not": its content is pinned to the absolute-count register the Section 2 inhabitants do
NOT reach. Checkable form of the guard: every Section 2 in-class row must satisfy every
clause of Section 1 (verified above by inspection, clause by clause, for AF and GLSS),
and the no-go statement in F2b must quantify over a class containing both engines by
name.

### (b) TOO BROAD: the K1 tautology

The risk: with "certificate" unrestricted, the no-go tautologizes to "whatever proves
completeness must consume M4's clause", which is the K1 circularity shape (define the
needed input as whatever-completes, conclude completeness needs it).

The guard: admissibility in $\mathcal{C}$ is SYNTACTIC everywhere. The funding clause
restricts the DATA the certificate consumes (which functionals of which marginal at
which normalization and error class), never the prover's ingenuity; there is no clause
of the form "the certificate cannot resolve individual zeros", no continuity clause, no
"information" clause; the interface is a hypothesis bundle in the P2 quarantine style,
and anything derivable over it by any mathematics whatever is in-class. If F2b finds
itself able to prove the no-go only for a SEMANTIC subclass ("certificates that cannot
distinguish configurations at resolution ..."), then the definition has failed this
guard and F2a must be re-posed; that failure condition is stated now, in advance, as
part of the definition's own falsifiability.

**The K1 check on the target.** A class no-go neither implies nor consumes RH, and is
compatible with both truth values: in its counterexample-configuration form (Section 5)
it asserts the existence of a C0-configuration matching a grant set with $E$ unbounded,
which is a statement about the interface's resolving power, true or false independently
of where zeta's zeros actually sit. If RH is true, the no-go says pool-funded
certificates cannot prove it; if RH is false, the no-go is still contentful about the
class (and the evading branch is vacuously dead). No direction of implication to RH
exists in either reading.

---

## 4. The discipline scope, inside the definition

**Davenport-Heilbronn** ([`../../experiments/_shared/davenport_heilbronn.py`](../../experiments/_shared/davenport_heilbronn.py)).
The zero-side clauses pose VERBATIM over D-H: its configuration satisfies C0 (FE pairing,
strip, RvM-class frame), every $\mathcal{P}_{\mathrm{zero}}$ functional is well-formed of
its marginal, and the horizontal-multiplicity conversion holds for it exactly as for
zeta. The prime-side parametrization is EMPTY over D-H by the #202(iv) vacuity: $-f'/f$
has poles in $\sigma > 1$ (the convergence-half-plane zeros), no von-Mangoldt-type
Dirichlet series exists there, $B_{DH}(h)$ cannot be posed, and the $R(\psi)$ analogue
diverges. So the class over D-H runs, and its controls are run, on the ZERO-SIDE
parametrization only; at the prime-funding parametrization the class over D-H is empty
by type refusal, which is stated rather than discovered.

Why the bracket bites ONLY at the funding joint at this register: the conclusion-shape
cannot separate. A D-H-class function can SATISFY "asymptotically 100 percent
simple-and-on-line" while violating its own RH (its off-line zeros are a sparse family),
and the in-print instance is Bombieri-Hejhal 1995 via GS25's pointer: linear combinations
of L-functions, conditionally, have almost all zeros simple and on the line [SECONDARY,
per the GLSS note]. So no theorem with the density-1 conclusion distinguishes zeta from
D-H, and the discipline's bite is at C2, never at C3's density register. At C4 the
situation inverts and becomes a test harness: D-H HAS off-line zeros (the certified pair
at $0.8085 + 85.699i$, plus zeros in $\sigma > 1$), so its completeness statement is
FALSE, and any interface-sound limit certificate whose consumed zero-side grants happen
to be TRUE of D-H's marginal would derive a falsehood. Which zero-side laws D-H's
marginal actually satisfies is largely unmeasured; that is exactly what makes D-H an
adversarial test CASE for F2b rather than an automatic refutation.

**Beurling** ([`../../experiments/_shared/beurling.py`](../../experiments/_shared/beurling.py)).
The mirror arm: prime-side parametrization only. A Beurling system loses the zero side at
three named breaks (no FE, so no distinguished line and C3's location predicates are not
well-formed; no four-fold symmetry, so the horizontal-multiplicity conversion evaporates;
no RvM frame or Fujii-class budget in print), while its prime side poses and is exactly
the density-alone comparator. The e1af finding (#208) gives the Beurling arm its precise
duty inside C2: the discriminating content of $\mathcal{P}_{\mathrm{prime}}$ is L1
congruence data (parity, mod-$p$ oscillation of $\{B_X(h)\}$), purchasable from neither
density alone nor total log-space commensurability, so "prime-correlation data" in the
pool is strictly richer than density data, and any F2b argument that would run
identically on a generic Beurling prime side is consuming only the density shadow of the
pool and is wrong about what the pool contains.

**The bracket's role for F2b, in one paragraph.** D-H keeps the zero side and loses the
funding side; Beurling keeps a prime side and loses the zero side; zeta is the
intersection. For F2b this brackets both branches of the attack. On the no-go branch,
any candidate proof must locate its obstruction in something BOTH controls expose: it
cannot rest on "correlations underdetermine location" alone (that is D-H-insensitive and
re-coats #199), and it cannot rest on prime-side density-generic facts alone (the
Beurling arm shows the pool is congruence-rich). On the evading branch, any candidate
limit certificate must name the consumed input that refuses over D-H (a
$\mathcal{P}_{\mathrm{prime}}$ read, per the vacuity) or name the zero-side grant that
D-H's marginal measurably violates; an evading family that cannot say which of these it
does is fare-dodging at the conservation law's joint
([`trojan_horse_m4.md`](trojan_horse_m4.md)) and should be presumed broken.

---

## 5. The target theorem-shape (posed, NOT attacked here)

**The F2b target (no-go form), sharpest honest statement.** For every member of
$\mathcal{C}$ and every consistent grant set $G \subset \mathcal{P}$: if the
certificate's outputs are theorems over C0 + proven core + $G$, uniformly over
C0-configurations, then they do not certify C4-fin (hence neither C4 nor, for the
location half, C4-loc). Equivalently: **the class ceiling is density 1**: the last
$o(N(T))$ is not correlation-purchasable, at any support, under any law, in either
parametrization.

**The heuristic core (from the GLSS anatomy).** The certified quantity and the
completeness quantity are the same functional at two error classes: the engines certify
$E(T) = o(TL)$ and completeness is $E(T) < 2$ ($= 0$ by parity). The gap is an
error-CLASS gap, not a quantity gap: even granting a law exactly, the exchange
identities' own floors ($O(T\sqrt{\log})$ unconditional Fujii; $O(T)$ on RH, which "does
not improve any results", GLSS I Remark 2) sit between every in-class output and the
integer 2, and the pool's G-LAW syntax carries an o-class slack floor on every read by
construction. The no-go's burden is to convert that floor from a property of the two
known engines into a property of the CLASS: to show no finite-rank arrangement of
o-class reads plus C0 structure can amplify slack-carrying inputs into an exact-zero
output. The expected proof shape has the Lagarias-Rodgers ancestor: for every consistent
$G$, construct a C0-configuration matching every grant in $G$ (and the proven core) whose
$E(T)$ is unbounded; configuration-uniform soundness then forbids any in-class
certificate from certifying C4-fin. The known hard part, stated honestly: the
configuration must also match the proven prime-side core through every pool-shaped
consequence of the explicit formula at all supports, which is exactly the funding wall's
content (F1/#208) appearing as a constraint on the counterexample; how much of the EF's
pinning power survives the o-class floor is the mathematical heart of F2b.

**The contrapositive, and the candidate identification of the residue.** If some
certificate does certify C4, it must consume data outside $\mathcal{P}$: either
$\beta$-resolved zero data (location itself: circular), or exact-identity access
(excluded at C0(ii)/C1(ii) as infinite-rank/infinite-precision), or error classes finer
than the pool floor on the same functionals: uniform-in-cutoff control of the slack that
the o-class syntax leaves on every read. That third residue is the candidate
identification: it is #148's uniformity/determinant-class clause ($\xi$ as a regularized
characteristic polynomial with all singularities accounted, budgets computable by
symmetry alone), which is the wall statement M4 seen from the counting side (#201's
re-count: uniform-in-cutoff funding on the vanishing locus;
[`missing_object_interface.md`](missing_object_interface.md);
[`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md)).
Per the frame's Section 5 bar, the #201 derivability check runs on THIS contrapositive
when F2b mints it: the risk that "what completeness must consume" is a restatement of
#148 rather than a theorem about it lives exactly here, and the no-go's value over the
existing ledger is precisely that it would make the identification a THEOREM over a
generous syntactic class rather than a finding.

**The evading branch (what would refute the no-go and move the frontier).** A member of
$\mathcal{C}$ certifying C4-fin: concretely, a finite-rank arrangement whose output error
class beats every read's granted class (an amplifier: integrality exploited to round an
$o$-class bound below 2 at a single scale and propagate by monotonicity, or a
consistency-forcing argument showing every $G$-matching configuration has $E \equiv 0$).
The branch is real (the deliberation's own wording: it "would contradict the compass and
move the frontier"), and the class is built generous precisely so that its discovery, if
possible, is not blocked by the definition.

**Theorem-shape bar (inherited from the frame, restated).** F2b's no-go counts as
progress only at the AF standard: proven modulo NAMED analytic hypotheses, finite
skeleton machine-checked or VERIFIER-drafted with the hypothesis load priced; a bare
well-formed conjecture does not qualify.

**Lean-quarantine sketch (P2 pattern; shape only, NOT a VerifierQueue target yet):**

```lean
/- pseudo-Lean, F2b shape sketch. ZeroConfig as in zeta-23-lean (pattern P1). -/
structure CorrelationPool (Z : ZeroConfig) : Prop where
  vert  : VerticalMarginalLaws Z     -- weighted n-point gap laws, TL norm, o(TL) class
  prime : PrimePairLaws              -- {B_X h} laws, shifts h ≥ 1, o(X) class
  -- deliberately NO field mentions any β, any single ρ, or an exact identity

structure CorrelationCertificate (Z : ZeroConfig) where
  d       : ℝ → ℕ                                    -- rank budget, growth free
  Q       : (T : ℝ) → HermForm (d T)                 -- finite-rank object (C1)
  reads   : FiniteReadsFrom (CorrelationPool Z)      -- funding clause (C2, G-LAW syntax)
  output  : (T : ℝ) → CountingBound Z T              -- C3 statements with error class

def CertifiesLimit (C : CorrelationCertificate Z) : Prop :=
  ∃ T₀, ∀ T ≥ T₀, (C.output T).implies (Edefect Z T < 2)     -- C4

-- F2b target: ∀ Z G C, SoundOver Z G C → ¬ CertifiesLimit C
```

---

## 6. What the definition deliberately leaves out, with reasons

1. **Effectivity distinctions beyond the two named classes.** The pool carries o-class
   grants; the target carries the absolute class; nothing in between is graded. Reason:
   the boundary theorems are ineffective by inheritance (PCC's own error is an
   unquantified $o(TL)$, and every downstream statement inherits it), so a rate ladder
   would fragment the class without moving either end of the gap. If F2b's proof needs a
   rate-quantified pool (for instance to run a quantitative floor argument), the grading
   is added THEN, as a refinement, not now.
2. **Family averaging (the CLLR support-2 evasion).** OUT of the pool. Reason:
   $q$-averaged correlation data over Dirichlet families is not a functional of zeta's
   marginal nor of the rational primes' shift family; the in-print family results (Özlük
   86 percent, CLLR 91 percent at support 2 under GRH) certify FAMILY aggregates and
   cross the support wall by changing the question. A certificate consuming family data
   to conclude about zeta specifically would be a named OUT-OF-CLASS evading candidate:
   F2b's no-go does not constrain it, and the no-go's statement must say so (scope
   honesty), but admitting it into $\mathcal{P}$ would dissolve the class's subject.
3. **The moment-class input family (Levinson/Conrey/PRZZ; BHB's $19/27$ under RH).** OUT
   of the pool. Reason: it is a genuinely different input class in print (mollified
   moments, Kloosterman technology; landscape row A6/B6), not a correlation functional
   of marginal or shifts; the frame question is scoped to correlation funding, and the
   in-print records at this register are correlation-side. Consequence stated plainly:
   the F2b no-go will NOT constrain moment-funded certificates, and the class ceiling
   claim is a claim about the correlation pool only (Section 7, item 6 carries the
   residual risk).
4. **$\beta$-resolved proven facts (zero-density estimates, computational verification,
   zero-free regions).** Out of the interface by design. Reason: the class question is
   what CORRELATION data can fund; a certificate leaning on $\beta$-resolved inputs is
   answering a different question. This costs little: for the limit clause, finite
   verification is void (any off-line zero hides above every verified height; the
   primes-thread bound: below height $3 \times 10^{12}$ nothing surfaces before
   $x \sim 10^{150}$), and classical zero-density bounds are density statements that
   cannot reach an exact-zero register for the same error-class reason the pool cannot.
5. **The Mueller 1983 pointer (arithmetic equivalent of Essential Simplicity), flagged
   follow-up.** If Mueller's Trans. AMS 275 (1983) equivalence delivers an unconditional
   prime-side parametrization of the ES scalar the GLSS engine consumes, the two
   parametrizations of $\mathcal{P}$ partially merge without the RH-priced GM dictionary,
   and the class simplifies. A bounded fetch rides F2b; nothing in the definition depends
   on its outcome (both parametrizations are already first-class).
6. **The power-saving error sub-pool.** Excluded from the default pool (C2's G-LAW
   clause) because its $k = 1$ member is RH (landscape row E5) and its admission
   collapses the question by smuggling. The labeled optional extension, if F2b ever needs
   it: admit power-saving grants at nonzero shifts $h \ge 1$ ONLY (the Bolanz class, row
   E2), with the one-point ($k = 1$) member excluded by syntax. Whether that restricted
   extension is itself collapse-safe is UNKNOWN (no in-print implication from
   square-root-error HL at $k = 2$ to RH is known to this project, and none is claimed);
   it stays out of the default pool precisely because its safety is unpriced. Note the
   AF conditional table's HL\* rungs are carried in-class at the o-class reading; if the
   AF paper's HL\* turns out to be defined with power savings, the extension activates
   for those rows and this is to be checked at source (Section 7, item 4).

---

## 7. Honest limits, and the adversary's checklist

The specific ways this definition could be wrong, listed for the same-session ADVERSARY.
Items 1-4 are the load-bearing ones.

1. **Is the absolute-count register the right completeness surrogate?** C4 is posed at
   $E(T) < 2$, which by parity and monotonicity equals "every zero simple and on-line":
   STRONGER than RH (simplicity contamination), and an all-heights statement rather than
   a limit statement (the "eventually" collapses). The named companions carry the
   alternatives (C4-loc = RH proper; C4-fin = cofinite). Attack surfaces: (a) a
   "location-only" certificate reaching $N_{\mathrm{off}} \equiv 0$ with $E$ unbounded
   would evade a C4-only no-go, so F2b must cover C4-loc explicitly or the frame
   question's word "location" is unearned; (b) conversely, is C4-fin (the strongest no-go
   target) perhaps ALREADY excludable by a soft cardinality argument that would make the
   theorem cheap and its derivability suspect? If a two-line argument kills C4-fin, the
   register must move to C4-loc and the no-go's value re-assessed.
2. **Does syntactic admissibility actually block the tautology?** The interface
   discipline ("the certificate's contact with zeta is exactly C0 + $\mathcal{P}$") is a
   checkable hypothesis-bundle condition for Lean-style certificates, but for informal
   candidate proofs the judgment "is this input pool-shaped?" has edges: e.g. a weighted
   zero sum with weight depending on $\beta$ smuggled through a "gap functional"
   parametrization. The adversary should try to write a $\beta$-sensitive functional
   that passes C2's syntax as written; any success forces a tighter marginal-functional
   definition (the current wording: functionals of the ordinate multiset with
   multiplicity, and of nothing else).
3. **Is law-blind admission too generous (adversarial laws)?** The pool admits ANY
   asserted law of the marginal at o-class. Designed guards: the o-class floor (an exact
   statement like $N^{\circledast} - N = 0$ is not grantable; only its $o(TL)$ shadow
   is, which is HMH, which the GLSS engine already consumes to reach density 1 and no
   further) and the G-LAW syntax (no fixed-height reads: the diagonalization leak named
   at C2 is closed by fiat, and the adversary should try to re-open it through some
   composite functional whose normalization hides a fixed-height read). If either guard
   fails, C2 needs a stronger syntax, not a semantic patch.
4. **Does "granted freely" accidentally admit RH via an equivalence (the GM-dictionary
   risk, named explicitly)?** Pair correlation at all supports is RH-adjacent via
   Montgomery's conjecture, and the prime-side ladder's uniform square-root member IS RH
   (row E5). Present handling: (a) the square-root channel is excluded by the o-class
   cap, with the restricted extension quarantined (Section 6, item 6); (b) full o-class
   pool admission does NOT collapse in print: full PCC yields density 1 (GLSS I), full
   AH yields density 1 (GLSS II), full HL\* yields 100 percent simple and "RH itself is
   out of reach" (AF), and Lagarias-Rodgers certify non-decidability at the
   currently-known sub-pool. Residual risk, stated flatly: no theorem says full o-class
   correlation data does not imply RH; that unproven non-implication is not an
   assumption of the class definition, it is the CONTENT of the class question (if the
   implication were proven tomorrow, the evading branch fires by pure mathematics and
   the frontier moves). The adversary should check the pool for any OTHER member or
   finite conjunction with a known RH-equivalence (the check that matters: nothing in
   $\mathcal{P}$ at o-class is known to imply any zero-free region, any $\beta$-resolved
   statement, or Lindelöf-class control; item E5's $k=1$ is the only known equivalence
   in the surveyed rows and it is out of pool).
5. **Is the proven-core/conjectural split stable in time?** "Proven" grows;
   admissibility is by shape, so growth inside pool shapes is absorbed silently (a proof
   of PCC would move it from grant to core without touching the class). A breakthrough
   of NON-pool shape used by a future engine (a new zero-density species, a moment
   breakthrough) would sit outside $\mathcal{C}$, and the class question would then be
   honestly scoped rather than wrong; but the adversary should confirm the scoping
   sentence in Section 5 (the no-go is about the correlation pool only) is carried into
   any F2b statement, else the theorem over-claims on arrival.
6. **Does excluding the moment class under-scope the no-go?** The wall's external
   interest ("why does the record sit near 2/3 and what must a completeness proof
   consume") presumes the correlation pool is the operative funding channel; the moment
   class is alive (unconditional 2/5 on-line; $19/27$ simple under RH) and un-constrained
   by this class. If the moment class's own input family can be given a pool-shaped
   presentation (its mean values ARE configuration functionals through Hadamard
   factorization), the class boundary drawn at Section 6 item 3 is softer than stated;
   the adversary should probe whether the exclusion is principled or notational.
7. **Frame contamination and convention pedantry.** (a) C0's RvM-class frame must not
   silently carry zeta-specific analytic strength beyond D-H's reach (control: D-H
   satisfies C0; any frame clause D-H fails must be struck or re-typed as pool data).
   (b) Windowing ($[0,T]$ vs $[T,2T]$), $TL$ vs $N(T)$ normalization, the multiset
   conventions ($\gamma > 0$, equal-ordinate exclusion in $N(\lambda)$ vs inclusion in
   $N^{\circledast}$) each admit off-by-convention errors; F2b's formal layer must fix
   them once, in the GLSS papers' conventions (Section 1.1 of the boundary note), and
   the adversary should spot-check the $E(T)$ identities under those conventions.

---

## 8. Hand-off blocks

**Verification targets (VERIFIER; finite, formalizable now, independent of F2b's fate):**

- V-F2a-1: over any C0-configuration, $E(T) = \sum_{\text{lines}} h(h-1)$ is
  nondecreasing in $T$, even-valued, and $E(T) < 2 \iff E(T) = 0$ (the parity lemma).
- V-F2a-2: the conversion inequality $\#\{\text{simple critical, } \gamma \le T\} \ge
  2N(T) - N^{\circledast}(T)$ as a C0-structural theorem (no arithmetic consumed), in the
  AF `ZeroConfig` style.
- V-F2a-3: C4 $\Rightarrow$ C4-loc and C4 $\Rightarrow$ C4-fin; and "C4 holds iff every
  zero is simple and on the line" (the register-collapse lemma).
- V-F2a-4: the off-line/multiplicity domination $N_{\mathrm{off}}(T) +
  N_{\mathrm{mult}}(T) \le E(T)$ (each defective line's $h \le h(h-1)$ for $h \ge 2$).
- (Drafting home: the repo's `lean/ZetaRH/` VerifierQueue, with the `ZeroConfig`
  structure imported in shape from the zeta-23-lean pattern library, not by dependency.)

**Adversarial test cases (ADVERSARY, this session):** the Section 7 checklist, items 1-4
first; plus two concrete probes: (i) attempt a $\beta$-sensitive functional that passes
C2's marginal syntax as written (item 2's edge); (ii) attempt to re-open the fixed-height
diagonalization leak through composite reads (item 3). Grading per the frame's verdict
wiring (#206): the session's grade is the adversary's, not this BUILDER's.

**What F2b inherits if the definition survives:** the class $\mathcal{C}$ with clauses
C0-C4 and pool $\mathcal{P}$; the no-go target at C4-fin (minimum C4, with C4-loc
coverage mandatory); the counterexample-configuration proof shape with its named hard
part (the EF's pinning power under the o-class floor); the evading-branch honesty clause
(any candidate must name its D-H refusal per Section 4); and the Section 5 contrapositive
as the object on which the #201 derivability check runs at mint time.

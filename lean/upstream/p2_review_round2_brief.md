# P2 (#41132) review round 2: brief

Status brief for Mathlib PR [#41132](https://github.com/leanprover-community/mathlib4/pull/41132)
("digamma: reflection, iterated recurrence, and duplication"), staged from
[`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean) (see `README.md`,
`digamma_pr_body.md`). This is a facts-and-options document, not reply text: Mathlib's AI-use
policy requires Owen to write review responses in his own words.

## Summary

- PR is open, head commit `baa4886` (`baa488628509cf06e57b66a207ba735f0329a038`), unchanged since
  the round-1 push on 2026-07-03.
- Round 1 (SnirBroshi, 2026-06-28) was addressed 2026-07-03: `digamma_reflection` golfed from 82
  to 23 lines, `digamma_two_mul` golfed from 63 to 31 lines (Owen's own count, quoted below).
- Round 2 landed 2026-07-17T22:54:27Z to 22:58:50Z: a new reviewer, j-loreaux, left 3 inline
  comments (one review pass, state `COMMENTED`, empty top-level body) and the `awaiting-author`
  label was applied at the same moment.
- All 3 items ask for Lean style / API-surface changes, not corrections to the underlying math.
  CI is green on the current head commit.

## (a) Timeline of activity since 2026-07-03

| Date (UTC) | Author | Type | Content |
|---|---|---|---|
| 2026-07-03T18:09:06Z | github-actions[bot] | PR-summary comment (auto, edited in place) | Declares the 3 new declarations (`digamma_apply_add_nat`, `digamma_reflection`, `digamma_two_mul`) after Owen's round-1 push. Automated bookkeeping, not a review ask. |
| 2026-07-03T19:47:38Z | owenpkent | Issue comment | Misdirected: this comment's content ("Moved the theorem to Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean...", "dropped the s != 1 hypothesis entirely") describes P1 (#41133), not this PR. Superseded two minutes later. |
| 2026-07-03T19:49:10Z | owenpkent | Issue comment | The actual round-1 response: "sorry wrong message! Fair point, those two proofs were too long. I've golfed them: - digamma_reflection: 82 lines down to 23 - digamma_two_mul: 63 lines down to 31 -Owen" |
| 2026-07-17T22:54:27Z | j-loreaux | Inline review comment, `Digamma.lean` line 82 | "if you call this `HasDerivAt.logDeriv_Gamma`, then I think it's totally reasonable to be a `public` lemma." |
| 2026-07-17T22:57:12Z | j-loreaux | Inline review comment, `Digamma.lean` line 112 | "I would turn all this into a `calc` block to improve readability and maintainability." |
| 2026-07-17T22:58:15Z | j-loreaux | Inline review comment, `Digamma.lean` line 147 | "As before, I suggest a `calc` block for this" |
| 2026-07-17T22:58:29Z | j-loreaux | Formal review, state `COMMENTED` | Body is empty; this is the envelope submitted around the 3 comments above (not a fourth, separate item). |
| 2026-07-17T22:58:50Z | j-loreaux | Label event | Applied `awaiting-author`. This is the first status label the PR has had since creation (nothing was applied between the 07-03 fix and this review), so it is tied to this review, not a stale holdover. |

Note on the misdirected 07-03T19:47 comment: it is still visible on the thread and refers to
content that actually belongs to P1's round-1 fix. It is harmless (superseded immediately by the
real reply) but Owen may want to delete it or add a one-line correction if he is replying in this
thread anyway, purely for cleanliness.

## (b) Per-item breakdown: code change or reply only

All three of j-loreaux's comments are attached to code introduced during the round-1 golf, and all
three ask for a code change, not just a clarification.

### 1. Line 82: rename and de-privatize `logDeriv_Gamma_comp`

Current code (`Digamma.lean`, introduced in the round-1 golf; this helper does not exist anywhere
in the pre-golf local source):

```lean
private lemma logDeriv_Gamma_comp {g : ℂ → ℂ} {a s : ℂ} (hg : HasDerivAt g a s)
    (h : ∀ m : ℕ, g s ≠ -(m : ℂ)) :
    logDeriv (fun z ↦ Gamma (g z)) s = a * digamma (g s) := by
  rw [show (fun z ↦ Gamma (g z)) = Gamma ∘ g from rfl,
    logDeriv_comp (differentiableAt_Gamma _ h) hg.differentiableAt, hg.deriv, digamma_def]
  exact mul_comm _ _
```

Requested edit (small and unambiguous; described here, not applied to any file): drop `private`
and rename to `HasDerivAt.logDeriv_Gamma` so it lives in the `HasDerivAt` namespace and is callable
by dot notation. The proof body is unaffected, only the declaration head changes. Three call sites
would need the matching dot-notation rewrite:

- In `digamma_reflection`: `logDeriv_Gamma_comp ((hasDerivAt_id' (x := s)).const_sub 1) hs₁`
  becomes `((hasDerivAt_id' (x := s)).const_sub 1).logDeriv_Gamma hs₁`
- In `digamma_two_mul`: `logDeriv_Gamma_comp ((hasDerivAt_id' (x := s)).add_const (1 / 2)) hsh`
  becomes `((hasDerivAt_id' (x := s)).add_const (1 / 2)).logDeriv_Gamma hsh`
- In `digamma_two_mul`: `logDeriv_Gamma_comp ((hasDerivAt_id' (x := s)).const_mul 2) h2s`
  becomes `((hasDerivAt_id' (x := s)).const_mul 2).logDeriv_Gamma h2s`

These three call sites sit inside the exact blocks items 2 and 3 ask to restructure into `calc`
blocks, so it is cleaner to land this rename together with those rewrites in one commit rather than
as an isolated fixup.

### 2. Line 112: turn `digamma_reflection`'s proof into a `calc` block

Targets the proof of `theorem digamma_reflection`, specifically the
`have key : ... := by rw [...] at key` block (roughly ten chained rewrite lemmas transforming `key`
from `logDeriv (Γ(z)Γ(1-z)) s = logDeriv (π / sin(πz)) s` down to the reflection identity), ending
just before the closing `linear_combination -key`. This is a genuine rewrite, not a mechanical
rename: it requires writing out each intermediate `logDeriv` expression as an explicit `calc` step.
Not attempted here per instructions.

Useful precedent: the project's own earlier, pre-golf source,
[`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean) lines 110-113 and 117-120, already
proves this identity with two `calc` blocks, before the round-1 golf flattened it first into
named `have`s and then into the current `rw [...] at key` chain. That structure (not the
intervening `have`-heavy version, which round 1 explicitly rejected as too long) is the natural
template for satisfying this comment without regressing on round-1's length concern.

### 3. Line 147: turn `digamma_two_mul`'s proof into a `calc` block

Same ask, same shape, applied to `theorem digamma_two_mul`'s analogous
`have key : ... := by rw [...] at key` block (roughly seven chained rewrite lemmas), ending just
before `linear_combination (-1 / 2 : ℂ) * key`. Unlike item 2, there is no local pre-existing
`calc`-block precedent for this proof (the pre-golf source proves it with `have`s throughout, not
`calc`), so this one is more of a fresh write.

## (c) CI and mergeability

- Head commit `baa4886`, unchanged since the round-1 push (2026-07-03, ~18:00-18:08 UTC). No new
  commit has landed in response to round 2 yet.
- Full CI (`ci (fork) / Build`, `Test and lint`, `Lint style`, `Post-Build Step`, `Post-CI job`,
  `Upload to cache`, `Lint and suggest`) all completed with conclusion `success`, last run
  2026-07-03T18:00-18:08Z.
- The check-runs timestamped 2026-07-17T22:58-22:59Z (`set_pr_emoji`, `update-label`,
  `Fix style issues from lint`, `Ping maintainers on Zulip` x4 skipped, `call-splice-bot` x3
  skipped, `Detect bors merge/delegate command` x4 skipped) are bot housekeeping reacting to the
  new review, not a rebuild. They do not indicate any new problem.
- The legacy combined-status endpoint (`/commits/{sha}/status`) reports `pending` /
  `total_count: 0`. This repo only uses the newer Checks API, so that field is not meaningful here
  and can be disregarded.
- `mergeable` / `mergeable_state` read `null` / `"unknown"` on two fetches about two seconds apart.
  GitHub computes this asynchronously rather than on demand via the API; treat it as inconclusive,
  not a conflict signal. Opening the PR page in a browser forces GitHub to compute and display it
  if a definitive read is wanted.
- Labels: `awaiting-author` (applied by j-loreaux at 2026-07-17T22:58:50Z, the same moment as the
  review, and the first status label the PR has had since creation), `t-analysis` and
  `new-contributor` (both auto-applied by the bot at PR creation on 2026-06-28), `LLM-generated`
  (applied by SnirBroshi on 2026-06-28, a human triage action, not a bot).
- j-loreaux's review state is `COMMENTED`, not `CHANGES_REQUESTED`, so GitHub itself is not
  formally blocking the PR. Mathlib's own convention, and the fresh `awaiting-author` label, is
  what signals Owen should act next.

## (d) Talking points for Owen (facts to draw on, not reply text)

- The round-1 golf (2026-07-03) took `digamma_reflection` from 82 to 23 lines and
  `digamma_two_mul` from 63 to 31 lines, in direct response to SnirBroshi's "these are very long
  proofs" comment. That golf is what introduced both the `private lemma logDeriv_Gamma_comp`
  helper and the compressed `rw [...] at key` chains that j-loreaux is now commenting on: neither
  existed in the original, longer submission.
- `logDeriv_Gamma_comp` exists to deduplicate one computation, the log-derivative of `Gamma`
  composed with an affine shift or scale, that both remaining theorems need: once in
  `digamma_reflection` (shift by `1 - s`), twice in `digamma_two_mul` (shift by `s + 1/2`, then
  scale by `2s`). It was marked `private` because at golf time it was treated as internal plumbing,
  not for any correctness reason. j-loreaux's read, that it is generically useful Gamma calculus
  worth exposing under `HasDerivAt`, is a characterization Owen can confirm or push back on
  depending on whether he sees it as a good standalone fact for other Mathlib users.
- The two `calc` requests and the round-1 "too long" complaint are in tension but not
  irreconcilable: a `calc` block does not have to be longer than the equivalent `rw`-chain, since
  it is the same sequence of rewrites written with the intermediate term shown at each step rather
  than folded into one `rw [...] at key`. The framing available to Owen is "restructuring for
  readability while keeping the golfed step count," rather than reverting to the pre-golf
  verbosity.
- The project's own staged source at `lean/ZetaRH/DigammaExtras.lean` still has the pre-golf,
  `calc`-based proof of the reflection identity and does not reflect the golfed code actually in
  the PR (the `logDeriv_Gamma_comp` helper does not exist there at all, and the reflection RHS is
  still the explicit `cos/sin` form rather than `Complex.cot`). If Owen pushes a fix to the Mathlib
  fork for round 2, it would be worth backporting the final accepted structure into this local file
  afterward so it stays an accurate record. That is a housekeeping step for this repo, not
  something to raise with the reviewer.
- Both review rounds, SnirBroshi's and j-loreaux's, have been about Lean style and API surface, not
  the underlying mathematics. The three identities themselves have not been challenged, and CI has
  been green since the round-1 push.

## (e) Cross-reference: P1 status

P1, `riemannZeta_conj` (Mathlib PR #41133), closed 2026-07-07T21:33:36Z with its title rewritten to
`[Merged by Bors] - feat(NumberTheory/Harmonic/ZetaAsymp): conjugation symmetry of riemannZeta`,
confirming a completed Bors merge. The REST API's own `merged` / `merged_at` fields read `false` /
`null` for it, which is a known Mathlib/Bors quirk (Bors performs the merge out of band rather than
through GitHub's native merge button); the rewritten title and the `closed_at` timestamp are the
reliable signals. #41133 is safe to cite as merged precedent if useful in the round-2 reply.

## Outcome (2026-07-18, overnight)

All three requested changes applied and pushed to the PR branch as `1128e854f9` (rename to `HasDerivAt.logDeriv_Gamma` with the namespace-closure fix the rename forced, verified against Mathlib's own `HasDerivAt.cexp`/`const_cpow` precedent; both proofs converted to 3-step calc blocks keeping the golfed lemma set, net +42/-28). Build green before push (2772 jobs, only the edited file recompiled). Owen chose code-only response, no comment text (own-words policy). Review re-request and label flip both permission-blocked for a new contributor (404 / GraphQL denial), so the signals are the push notification + CI re-run; if the `awaiting-author` label sits stale after CI greens, a one-line comment from Owen flips it. Worktree and fork remote cleaned up; pinned checkout pristine.

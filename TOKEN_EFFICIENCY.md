# Token Efficiency with Fable

> Practical guidance for keeping token cost down when running this repo's
> multi-agent proof program on Fable 5. Written 2026-06-09 after a nine-lens
> conjecture run (see [`docs/03_research/first_principles_conjecture_program.md`](docs/03_research/first_principles_conjecture_program.md))
> where a pause/resume exposed a real cost trap. Every tactic here is something
> that bit, or saved, that run. Companion to [`OPERATIONS.md`](OPERATIONS.md).

## 0. The model context that sets the rules

The session model is Fable 5, often the `claude-fable-5[1m]` one-million-token
variant. Two facts drive everything below.

1. **A big context window is not free.** Cost scales with the tokens you actually
   send and generate, not with the window size. A 1M window invites stuffing
   everything in; resist it. The window is headroom for when you genuinely need it,
   not a default.
2. **The prompt cache has a roughly 5-minute TTL.** Re-entering a conversation whose
   context has gone cold pays a full re-read. This is why pacing matters for loops
   and scheduled wake-ups (Section 7).

The single highest-leverage habit: **the cheapest agent is the one you do not
launch.** Multi-agent fan-out is powerful and sometimes correct, but each agent
re-pays the system prompt, the role spec, and whatever context you feed it. Before
fanning out, ask whether one batched agent, or your own main-loop reasoning, does
the job.

## 1. Tier the work across models

Put the expensive model only where creativity or hard reasoning actually lives.
Everything mechanical goes to a cheaper tier.

- **Generation / construction** (BUILDER proposing a conjecture, SYNTHESIZER writing
  the dossier): full model. This is where quality compounds.
- **Judgment against a fixed rubric** (ADVERSARY scoring against the D-H discipline
  and a kill list, VERIFIER checking a stated target): Sonnet, sometimes Haiku. The
  rubric carries the intelligence; the agent applies it.

How to set it:
- Workflow: `agent(prompt, { model: 'sonnet', ... })`, or a per-phase `model` in the
  `meta.phases` entry.
- Agent tool: the `model` parameter (`"sonnet"`, `"haiku"`, `"opus"`, `"fable"`).

In the conjecture run, moving the entire adversarial pass to Sonnet cut the remaining
spend by roughly 80% with no loss of discrimination, because the attack is rubric
application, not invention.

## 2. Batch many small judgments into one agent

One agent reviewing N items beats N agents reviewing one item each whenever the
per-item judgment is small and shares context. N separate agents re-pay the system
prompt and the shared rubric N times; one batched agent pays it once and returns an
array.

- Use a schema with a top-level array (`{ verdicts: [ {name, ...}, ... ] }`) and tell
  the agent to return one entry per item, keyed by an exact-copy identifier.
- This is the right default for scoring, classification, triage, and any pass where
  the items do not need to reason about each other.
- Keep the BARRIER (separate-agent-per-item) only when items genuinely need isolation
  or independent adversarial framing, and even then consider whether 3 batched
  skeptics beat 9 solo ones.

The conjecture run replaced nine separate adversaries with one batched adversary over
all nine conjectures. Same six attacks per item, one system-prompt payment.

## 3. Scope each agent's inputs and outputs

An agent spends tokens on what it reads and what it writes. Bound both.

- **Give data in the prompt; disable file reading when you can.** The batched
  adversary got all nine conjectures and the surveyor brief inline and was told to
  read no repo files. Every avoided `Read` is avoided tokens. Do this whenever the
  agent's job is to reason over data you already hold.
- **Cap output fields.** Tell agents to keep free-text reasoning short (the run capped
  each verdict's reasoning at 120 words). Long "thinking out loud" in a returned field
  is pure cost if you only need the verdict.
- **Ask for structured output, not prose.** A schema forces the agent to return the
  fields you will actually use, and nothing else. You skip a parsing round-trip and the
  agent skips the narration.
- **Point agents at line ranges, not whole files.** When an agent must read, tell it
  the offset/limit or the specific section. Reading a 600-line file to use 30 lines is
  the most common silent waste.

## 4. The workflow cache-resume trap (the one that bit this run)

Workflow resume replays a STRICT PREFIX of the run journal. Completed `agent()` calls
return from cache instantly, but only up to the FIRST call that is new, edited, or did
not finish. Everything after that first gap re-runs live at full price, even agents
that had already completed.

In the conjecture run, the one builder that never finished was early in the journal.
A naive resume therefore re-ran the eight finished builders behind it. The fix that
actually saved the work:

1. **Salvage completed results from disk instead of recomputing.** The journal
   (`.../subagents/workflows/<runId>/journal.jsonl`) and the per-agent files hold every
   finished result. Extract the `type: "result"` entries and write them to a file.
2. **Hand-build a continuation** that reads the salvaged file and only runs the genuinely
   missing pieces, rather than resuming the workflow.

Practical rules to avoid the trap in the first place:
- **Order independent expensive work so the flaky or slow agents come LAST** in the
  journal, so a gap invalidates as little as possible behind it.
- **Prefer `pipeline()` over a `parallel()` barrier** when stages are independent, so a
  single slow item does not hold a barrier and force re-runs of everything in its phase.
- When you do resume, confirm the resume is hitting cache (watch `/workflows` or check
  that finished agents are not restarting) before letting it run.

## 5. Salvage, do not recompute

Any agent output that reached disk is recoverable. Before re-running anything, check:

- `journal.jsonl` in the workflow run directory for `result` entries.
- The per-agent `.jsonl` / `.meta.json` files for individual outputs.

Extracting and reusing these is a few seconds of shell work and saves the full
regeneration cost. This applies to interrupted workflows, killed background agents, and
any run you paused.

## 6. State a budget and let the work self-limit

When you want a hard ceiling, say so in the request with a target like `+200k`. Inside a
workflow this becomes `budget.total`, and you can scale or stop against it:

```js
// scale fan-out to the budget
const FLEET = budget.total ? Math.floor(budget.total / 100_000) : 5
// or loop until nearly spent
while (budget.total && budget.remaining() > 50_000) { ... }
```

Without a target, `budget.remaining()` is `Infinity` and loops run to the agent cap.
A stated budget turns "as much as it takes" into a bounded, predictable spend.

## 7. Keep the cache warm; pace loops deliberately

The roughly 5-minute prompt-cache TTL means idle gaps cost a cold re-read.

- For `/loop` and `ScheduleWakeup`, do not poll harness-tracked background work on a
  short timer. When that work finishes you are re-invoked automatically, so a short
  wake-up just burns a cache miss for nothing. Use a long fallback heartbeat
  (1200s or more) and let the completion notification drive you.
- If you must poll something the harness cannot track (an external run), match the
  interval to how fast that state actually changes, and stay under 300s only when you
  are genuinely watching live external state.
- Do not pick 300s. It pays the cache miss without amortizing it. Either stay under
  ~270s (cache warm) or commit to 1200s+ (one miss buys a long wait).

## 8. Main-loop habits that quietly add up

These are not multi-agent specific but they are where a long session leaks tokens.

- **Use the dedicated tools** (Grep, Glob, Read) over shell `cat` / `grep` / `find`.
  They return cleaner, smaller, link-integrated output.
- **Do not re-read a file you just edited** to "verify" it. Edit and Write error if the
  change failed, and the harness tracks file state. The re-read is pure cost.
- **Make independent tool calls in one message** so they run in parallel. This does not
  cut tokens directly but cuts wall-clock and avoids redundant context restatement
  across turns.
- **Read line ranges, not whole files**, once you know where the content is. Large
  PHASE_STATE.md / TODO.md / LEARNINGS.md reads are the usual offenders; target the
  section.
- **Let summaries do their job.** When context is long the harness summarizes and
  continues; you do not need to pre-emptively dump state into the conversation to
  "save" it.

## 9. Quick checklist before a fan-out

1. Can one batched agent do this instead of N? (Section 2)
2. Can it run on Sonnet/Haiku instead of the full model? (Section 1)
3. Can I hand it the data inline and forbid file reading? (Section 3)
4. Did I cap its output fields and ask for a schema? (Section 3)
5. Are the slow/flaky agents ordered LAST so a resume invalidates little? (Section 4)
6. Did I state a token budget if I want a ceiling? (Section 6)
7. If something already ran, can I salvage it from disk? (Section 5)

The arithmetic of the conjecture run: full price was paid only for one surveyor and
nine builders (the irreducible creative core). The brief restart waste was small, the
entire adversarial pass ran batched on Sonnet, and the final synthesis cost nothing
extra because the main loop did it. That split, expensive model on generation, cheap
batched model on judgment, salvage over recompute, is the whole game.

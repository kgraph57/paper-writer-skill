# The AI-for-Science Operating Model

> The rest of this skill is a *manuscript factory*: it assumes the research
> question and the data already exist, and helps you express, format, and submit
> them. This document is the *research engine* that sits upstream and around it.
> It turns the linear pipeline into a loop and names the two things only a human
> can supply.

---

## 1. Why this document exists

Three frontier systems (2024–2026) defined where "AI for Science" actually is,
and — more usefully — where it isn't:

| System | What the AI did | What stayed human | Lesson |
|--------|-----------------|-------------------|--------|
| **Sakana AI Scientist v2** (2025) | Hypothesis → experiment → analysis → full manuscript, fully autonomous; one paper passed an ICLR *workshop* review (6/7/6) | **Nobody.** No human in the loop | External review found hallucinations, faked results, novelty inflation, and a misattributed citation (LSTM). Authors admitted it would not pass a *conference* bar. **Full autonomy without a human anchor produces confident slop.** |
| **Google AI co-scientist** (Nature, 2026) | Multi-agent *generate → debate → rank → evolve* of hypotheses, grounded in literature + databases | **Wet-lab validation, clinical judgment** | Reproduced an AMR hypothesis in days that took a lab years. But Google states plainly: it "did not achieve autonomous discovery, did not complete clinical trials, did not replace the research team." **The value is the hypothesis engine; truth is decided by the world.** |
| **FutureHouse Robin** (2025) | Hypotheses, experiment design, data analysis, manuscript figures — all AI | **The physical experiments** | Discovered + validated a novel therapeutic candidate; concept-to-submission in 2.5 months. The AI owned the *intellectual scaffold*; humans owned *contact with reality*. |

The pattern is identical across all three. **AI compresses the cost of everything
between idea and reality toward zero. The human's irreducible contribution narrows
to exactly two things: the idea, and the data.** Everything else — search,
synthesis, design drafting, statistics, prose, formatting, compliance, revision —
is execution that AI now does at full power.

This skill is built for a **clinician publishing under their own name**, where a
fabricated finding is not an embarrassment but a patient-safety and
career-integrity event. So we take the frontier's *capability* and bolt on the
*discipline* the frontier systems lacked.

---

## 2. The two human-sovereign inputs

Mark these two gates in every project. They are the only points where the human
is not replaceable — protect them, and automate aggressively everywhere else.

### 💡 IDEA — judgment, meaning, ethics

The human owns:
- **What is worth asking** — clinical relevance, not just statistical tractability.
- **What the finding *means*** — the bridge from a coefficient to a child at a bedside.
- **What is ethical** — consent, equipoise, who is studied, who benefits.
- **Whether to publish at all** — the "is this true and useful enough to put my name on it" call.

AI *proposes* ideas (and should, abundantly — see `templates/research-question.md`).
The human *selects, kills, and reframes* them. An AI-generated hypothesis that no
human chose to pursue is noise, not science.

### 📊 DATA — contact with reality

The human owns:
- **The ground truth** — real patients, real outcomes, the愛育 outpatient clinic. AI cannot generate this; it can only generate *plausible-looking* versions of it, which is the failure mode.
- **The provenance** — IRB approval, de-identification, the chain of custody from chart to CSV.
- **The integrity of measurement** — what was actually measured, with what error.

AI *analyzes, models, and visualizes* data. It must **never originate a data point,
a participant, or a result.** This is the single hardest rule in the skill
(`Section-Specific AI Guidelines` in SKILL.md), and AI-for-Science makes it *more*
load-bearing, not less.

> **The thesis, stated once:** As the marginal cost of execution falls to zero, a
> scientist's job becomes *only* the two things a machine cannot do — supply real
> data and exercise judgment about ideas. Build the workflow so that those two are
> the explicit, protected pivots, and let the machine do the rest at maximum power.

---

## 3. The loop (not the line)

The base skill is a line: `Search → Outline → Draft → Submit`. The research engine
wraps that line in a discovery loop:

```
        💡 IDEA gate (human selects)
                │
   ┌────────────▼─────────────┐
   │  Phase −1: DISCOVERY      │   ← NEW
   │  observation → questions  │   templates/research-question.md
   │  → novelty check          │   references/novelty-check.md
   │  → study design + power   │   templates/study-design.md
   │  → PRE-REGISTRATION lock  │   templates/preregistration.md  ← anti-HARKing gate
   └────────────┬─────────────┘
                │  (plan is now frozen)
        📊 DATA gate (human supplies real data; IRB verified)
                │
   ┌────────────▼─────────────┐
   │  Phases 0–3: EXECUTE      │   existing skill
   │  analysis → draft (IMRAD) │   (now bound to the frozen plan)
   └────────────┬─────────────┘
                │
   ┌────────────▼─────────────┐
   │  Phase 6.5: RED-TEAM      │   ← NEW
   │  try to KILL the claim    │   references/adversarial-review.md
   │  before a reviewer does   │   agent: paper-red-team
   └────────────┬─────────────┘
                │ survives?
        ┌───────┴────────┐
       YES              NO → back to Discovery (the finding was an artifact)
        │
   Phases 4–10: humanize → submit → revise
```

The loop can run more than once. A red-team kill is not a failure — it is the
system working. Sakana v2's papers shipped *because nothing tried to kill them.*

---

## 4. Division of labor across the full loop

| Step | AI does | Human owns | Guardrail |
|------|---------|-----------|-----------|
| Observe | — | **💡 the clinical observation** | — |
| Generate questions | proposes 5–15 candidates, scores FINER | **selects / kills / reframes** | novelty check (§5.2) |
| Design study | drafts design, comparator, power, analysis plan, DAG | **approves; owns ethics & feasibility** | pre-registration (§5.1) |
| Pre-register | drafts the registration record | **submits it; it is now binding** | the lock itself |
| Collect data | — | **📊 supplies real, IRB-approved data** | never AI-originated (§2) |
| Analyze | runs the *pre-registered* analysis, then clearly-labeled exploratory | verifies against raw data | analysis = frozen plan first |
| Draft | writes all IMRAD prose | verifies every number traces to data | base skill Phase 3 |
| Red-team | attacks its own main claim from 4 angles | adjudicates the verdict | adversarial review (§5.3) |
| Submit / revise | drafts everything | signs, decides, corresponds | base skill Phases 7–10 |

Rule of thumb: **if a step can be checked against an external truth (a database, a
raw data file, a statistical assumption), AI may execute it. If a step *defines*
what counts as true or worthwhile (the question, the data, the meaning), a human
must own it.**

---

## 5. The three integrity guardrails

These are what make an AI-accelerated study *more* rigorous than a hand-built one,
instead of less. Each one prevents a documented frontier failure mode.

### 5.1 Pre-registration — prevents HARKing & the garden of forking paths

The danger of a fast loop is that AI can hypothesize-after-results-are-known
(HARKing) and p-hack across a multiverse of analyses at machine speed, dressing
post-hoc noise as an a-priori finding. The only defense is to **freeze the
hypotheses and the primary analysis plan before the data gate** (OSF / UMIN-CTR /
jRCT / PROSPERO). After the lock:
- Pre-registered analyses are reported first, exactly as planned.
- Everything else is labeled **exploratory** and cannot carry a confirmatory claim.
- Deviations from the plan are disclosed, not hidden.

See `templates/preregistration.md`. For systematic reviews this already exists as
the PROSPERO step — this generalizes it to primary studies.

### 5.2 Novelty check — prevents reinvention & novelty inflation

Sakana v2 *overestimated its own novelty*. Before committing to a question, run an
automated "has this already been answered?" sweep against real literature
(PubMed MCP, OpenAlex, Europe PMC, Semantic Scholar) and classify the gap honestly:
genuinely novel / incremental / already-answered / contested. A question that the
literature already settles is killed at near-zero cost — the cheapest experiment
is the one you don't run. See `references/novelty-check.md`.

### 5.3 Adversarial self-review — prevents confident slop

The difference between Robin (credible) and Sakana v2 (slop) was that nothing in
Sakana's loop *tried to make the paper fail.* Before submission, a hostile internal
panel attacks the main claim from four angles — statistical, methodological,
novelty, integrity — and a "steelman the null" pass argues that the finding is
chance, confounding, or bias. If the claim cannot survive its own red team, it does
not go to a journal's red team. See `references/adversarial-review.md` and the
`paper-red-team` agent.

---

## 6. The autonomy dial

How much to automate is a *setting*, not a fixed property. Choose per project, and
state it in the README.

| Mode | AI runs… | Human touches… | Appropriate for |
|------|----------|----------------|-----------------|
| **Manual** | one step at a time, asks before each | everything | learning the method; high-stakes flagship paper |
| **Co-pilot** (default) | a full phase, stops at every gate | both sovereign gates + every gate verdict | most clinical research |
| **Autopilot** | the whole loop between gates, reports after | only the 💡 and 📊 gates + final sign-off | low-stakes, well-trodden designs; never the first time |

**Hard rule for medical / clinical work:** the 💡 IDEA gate, the 📊 DATA gate, and
the pre-registration lock are **never** autopilot. No setting removes the human
from "is this ethical," "is this data real," and "is this what we committed to
test." This is non-negotiable and overrides any "team mode" or stage-gate
automation elsewhere in the skill.

---

## 7. How this maps onto the existing skill

- **New upstream:** Phase −1 (Discovery) runs *before* Phase 0 (Project Init). Its
  output — a frozen, pre-registered, novelty-checked, powered study plan — becomes
  the input the rest of the skill always assumed you already had.
- **Re-enterable:** Phase −1 is not a strict linear chain with one fixed start. An
  advanced study (question or draft protocol already in hand, but pre-data) enters at
  the *first guardrail it hasn't yet passed* — typically novelty, then a design audit,
  prereg, and a design-stage red-team — rather than re-forging a question it already
  has. The loop has no single fixed entry point (see the SKILL.md Phase −1 entry matrix).
- **New self-critique:** Phase 6.5 (Adversarial Review) runs after Quality Review
  (Phase 6) and before Pre-Submission (Phase 7).
- **Upgraded plumbing:** Phase 1 literature search and Phase 5 citation verification
  switch from "WebSearch is unreliable, ask the user" to real literature APIs
  (PubMed MCP et al.).
- **New instrumentation:** `templates/human-loop-ledger.md` records, at every gate,
  whether the decision was 💡 human-judgment, 📊 human-data, or 🤖 AI-execution —
  making the two sovereign inputs auditable.
- **Unchanged:** everything downstream of the data gate. The manuscript factory is
  already excellent; the research engine just feeds it better inputs and stress-tests
  its outputs.

---

## 8. One-paragraph summary for the README

> This skill operates the full scientific loop, not just the writing of it. AI
> generates and ranks research questions, checks their novelty against the live
> literature, designs the study and its power, and — after a human supplies real
> data and locks a pre-registered plan — runs the analysis, drafts the manuscript,
> and red-teams its own main claim before any journal sees it. Two things stay
> human and protected at all times: the **ideas** (what is worth asking, what it
> means, what is ethical) and the **data** (real, IRB-approved, never
> machine-originated). Everything between is executed at full power, under
> pre-registration, novelty, and adversarial-review guardrails that make the science
> more rigorous, not less.

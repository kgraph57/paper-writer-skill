# Research Question Forge

> **Phase −1 — Discovery.** Runs *before* Phase 0 (Project Init).
> Input: a raw clinical observation **or** an existing question/protocol. Output: **one selected, sharpened research question**
> ready to hand to `references/novelty-check.md` and `templates/study-design.md`.
>
> This template implements the Google AI co-scientist pattern (generate → debate →
> rank → evolve) with the human as the irreplaceable final selector.
> See `references/ai-for-science-model.md §2` for why the 💡 IDEA gate is never automated.

---

## 0. Two entry modes

**Decision header:** Did the question come from a clinical spark (→ Mode A) or does a question/protocol already exist (→ Mode B)?

| Mode | Entry condition | Steps to run | Output |
|------|----------------|-------------|--------|
| **A — Forge** | Raw clinical observation; no prior question | §1 → §2 → §3 → §4 → §5 💡 → §6 | Full §6 record |
| **B — Resume/Refine** | A sharpened question or draft protocol already exists; study not yet locked | (a) PECO/PICOTS back-fill → (b) Attack pass → (c) FINER score (N = ?) → (d) §5 💡 re-confirmation → (e) §6 record | Same §6 record |

### Mode B — step-by-step

Run these four sub-steps in order. Skip Steps 1–4 of the forge entirely.

**(a) PECO/PICOTS back-fill.** Fill the §2 framing table for the existing question. Any element left blank is a precision gap — resolve it before continuing.

**(b) Attack pass (single).** The steelman is implicit — the question already survived to protocol stage. Run only the Attack half of §4 Step 2:
- Is the outcome measurable with data you can actually obtain?
- Is there an obvious confounder that would sink the interpretation?
- Would a positive result change anything, or is the effect size too small to matter clinically?
- Is the design implied by the question achievable in your setting?
- Does it risk HARKing — i.e., were you drawn to this question because you already suspect the answer from your data?

Any "yes" to the last point, or a hard "no" on measurability, is a design-change trigger, not a reason to abandon the question.

**(c) FINER scoring.** Score F / I / E / R as in §3. Leave N as `?` — run `references/novelty-check.md` next. A Σ below 15 (counting N = 3) is a signal to revisit the framing, not necessarily to kill the question.

**(d) 💡 Human re-confirmation (§5 sovereign gate).** Explicitly answer: "Is this still the question worth running?" This check is mandatory even for advanced studies — context, feasibility, and clinical relevance can shift between conception and data collection.

> Mode B still produces the identical §6 Output record (P/E/C/O/T/S, FINER scores, rationale, next steps). Downstream files (`references/novelty-check.md`, `templates/study-design.md`) consume §6 and are unaffected by which mode produced it.

---

## 1. Input: the clinical observation

Fill this in before running the forge. The puzzle must come from you — it cannot come from a literature gap AI found on its own. That distinction is the 💡 gate.

```
OBSERVATION RECORD
──────────────────────────────────────────────────────────────
What I saw / heard / measured in the clinic:
  [e.g., "Parents arriving at my outpatient clinic increasingly mention
   they consulted generative-AI tools before coming in. Several had delayed
   presenting a febrile child after the AI told them to 'watch and wait.'"]

Why it surprised or unsettled me:
  [What expectation was violated? What gap does it suggest?]

What I do NOT yet know that would change my practice if I knew it:
  [The clinical knowledge gap — not a literature gap.]

Population I care about:
  [e.g., infants <12 mo with fever, parents in urban tertiary-care setting]

Rough outcome I have in mind:
  [e.g., delayed presentation, inappropriate antibiotic request, diagnostic accuracy]
──────────────────────────────────────────────────────────────
```

> 💡 **Human input required.** AI may prompt or scaffold this form, but cannot
> supply the observation. If the observation originates from an AI-generated
> literature gap rather than a clinical experience, label it clearly — the
> question will need extra novelty justification.

---

## 2. PICO / PECO / PICOTS framing

Choose the frame that matches your likely design before generating candidates.

| Element | Interventional (PICOTS) | Observational (PECO) | Meaning |
|---------|------------------------|----------------------|---------|
| **P** | Population | Population | Who exactly (age, diagnosis, setting) |
| **I** | Intervention | Exposure | What was done or what the patient was exposed to |
| **C** | Comparator | Comparator | The alternative; may be "no exposure" or standard care |
| **O** | Outcome | Outcome | Measurable; specify direction and time horizon |
| **T** | Time / follow-up | — | When outcome is measured |
| **S** | Study design | — | RCT, cohort, cross-sectional, SR… |

**Pediatric example (fills the form above):**

| Element | This example |
|---------|-------------|
| P | Parents/caregivers of febrile children aged 3 mo–5 yr presenting to a general pediatric outpatient clinic |
| E | Pre-visit use of a generative-AI chatbot for symptom assessment |
| C | No pre-visit AI use (sought advice from family, searched a conventional search engine, or no prior advice) |
| O | Time-to-presentation (hours from symptom onset to clinic arrival); secondary: antibiotic request rate at visit |
| — | Cross-sectional survey + chart review |

---

## 3. FINER scoring rubric

Score each candidate question 1–5 on each criterion. Sum → priority rank.
Novelty score is a placeholder (marked `?`) until `references/novelty-check.md` runs.

| Score | Feasible | Interesting | Novel | Ethical | Relevant |
|-------|----------|-------------|-------|---------|----------|
| **5** | Data exist, N achievable in your setting with current resources | Likely to change practice or policy if answered | No prior study found; fills a clear gap | No consent/safety concerns; IRB straightforward | Directly addresses a daily clinical decision |
| **4** | Minor resource gap (one extra funding step or collaboration) | Results would inform guideline update | 1–2 prior studies, conflicting or methodologically weak | Minor procedural requirements (waiver likely) | Addresses a decision you face weekly |
| **3** | Achievable but requires pilot or phased approach | Interesting to subspecialty audience; publication likely | 1–2 prior studies with moderate quality, your angle is incremental | Standard consent required; no special sensitivity | Relevant to your field but not your immediate practice |
| **2** | Requires external data, extended timeline, or significant funding | Primarily fills a textbook gap; limited clinical impact | Prior RCT or SR with consistent results; gap is minor | Sensitive population requires enhanced protections | Relevant to adjacent field; distant from your patients |
| **1** | Not achievable at your institution within a reasonable timeframe | Academic curiosity only; unlikely to change anything | Already definitively answered | Significant ethical barrier; IRB approval unlikely | Addresses a problem that does not exist in your setting |

**Maximum possible score: 25.** Questions below 15 total are usually not worth pursuing unless one criterion (typically Relevance or Feasibility) is a hard blocker that can be addressed.

---

## 4. The forge procedure

### Step 1 — Generate (diverge widely)

Ask AI to generate 5–15 candidate questions from your observation record. Instruct it to vary:
- **Outcome angle**: primary outcome, secondary outcome, process measure, patient-reported
- **Population angle**: narrow (infants only) vs. broad (all pediatric age groups); high-risk subgroup
- **Temporal angle**: acute event vs. long-term behavior change
- **Design angle**: descriptive → etiologic → interventional
- **Comparator angle**: active comparator vs. unexposed vs. historical

> 🤖 AI runs this step. Cast wide; odd angles often reveal the best question.
> Do not prune yet — the goal is breadth.

### Step 2 — Debate (steelman + attack each)

For each candidate, AI runs two passes in sequence:

**Steelman:** Why is this the *best* question in the batch? What would the finding enable?

**Attack:** What makes it weak?
- Is the outcome measurable with data you can actually obtain?
- Is there an obvious confounder that would sink the interpretation?
- Would a positive result actually change anything, or is the effect size too small to matter clinically?
- Is the design implied by the question achievable in your setting?
- Does it risk HARKing — i.e., is there temptation to pick this question because you already suspect the answer from your data?

> 🤖 AI runs steelman + attack. Human reads; begins informal ranking.

### Step 3 — Rank (FINER table)

Fill the FINER table for each surviving candidate. Leave Novelty as `?` — it requires the full `references/novelty-check.md` sweep to score honestly.

| # | Candidate question (one sentence) | F | I | N | E | R | Σ |
|---|----------------------------------|---|---|---|---|---|---|
| 1 | … | | | ? | | | — |
| 2 | … | | | ? | | | — |
| … | | | | | | | |

Sort by Σ (counting N as 3 until confirmed). Flag any question where:
- Any single criterion = 1 → likely a kill
- Feasibility < 3 → defer unless funding is imminent

### Step 4 — Evolve (sharpen top 2–3)

Take the top 2–3 by Σ. For each, apply:

1. **Narrow the population** — remove ambiguity about who is in and who is out.
2. **Operationalize the outcome** — name the instrument, the threshold, the time window.
3. **Name the comparator** explicitly.
4. **State the direction** — are you testing whether exposure *increases*, *decreases*, or *is associated with*?
5. **One-sentence PECO/PICO rewrite**: "Among [P], does [I/E] compared to [C] affect [O] measured at [T]?"

> 🤖 AI drafts evolved versions. Human reviews wording and clinical accuracy.

### 💡 STEP 5 — HUMAN SELECTS (sovereign gate — never automated)

**Stop. The AI does not choose.**

Present the evolved candidates to the research team (or to yourself, if solo). Decide:

| Option | Action |
|--------|--------|
| **Select** | Proceed to novelty check. Record rationale in Output Template (§7). |
| **Kill all** | Return to Step 1 with a revised observation or a different angle. |
| **Reframe** | Combine elements from two candidates; re-enter at Step 4. |
| **Defer** | The observation needs more clinical data before the question is ripe. |

> From `ai-for-science-model.md §2`: "An AI-generated hypothesis that no human chose
> to pursue is noise, not science." A selected question carries the researcher's
> judgment about what is *worth knowing*. Protect that.

---

## 5. Worked pediatric example

**Observation (filled form):**
Pediatric outpatient clinic, 愛育病院. Over several months, parents increasingly mention consulting a generative-AI chatbot before the visit. Three cases this quarter where a febrile infant's presentation was delayed; parents report the AI reassured them. Unsettled because delayed presentation in young infants risks missing serious bacterial infection. Population: infants and young children. Rough outcome: presentation delay.

**Six candidates generated (Step 1):**

| # | Candidate question |
|---|-------------------|
| Q1 | Among parents of febrile children <5 yr, does pre-visit generative-AI use increase time-to-presentation compared to no pre-visit AI use? |
| Q2 | Among parents who used a generative-AI chatbot before a pediatric visit, what proportion received advice inconsistent with published fever guidelines? |
| Q3 | Does pre-visit AI use predict inappropriate antibiotic request at the pediatric visit? |
| Q4 | What factors predict whether a parent uses AI vs. #8000 (Japan's pediatric telephone triage line) as a first contact for pediatric fever? |
| Q5 | Among parents who used generative-AI for fever triage, does the specific platform used (ChatGPT vs. other) affect advice accuracy? |
| Q6 | Can a structured AI chatbot intervention reduce unnecessary nighttime ED visits for non-urgent pediatric fever compared to standard parental education? |

**Steelman / attack highlights (Step 2):**

| # | Steelman | Attack |
|---|----------|--------|
| Q1 | Directly tests patient-safety outcome; time-to-presentation is chart-extractable | Causal interpretation blocked: parents who use AI may differ systematically from those who don't; observational confounding is severe |
| Q2 | Fully AI-auditable; could drive platform accountability | Defining "inconsistent" requires a guideline operationalization; no patient outcome attached |
| Q3 | Antibiotic stewardship angle; outcome is measurable at visit | Antibiotic request is a distal outcome of AI advice; effect size probably small |
| Q4 | Novel behavior-science angle; understanding the choice architecture is upstream of all other questions | Descriptive only; does not answer a clinical question; limited policy traction |
| Q5 | Platform comparison would interest regulators | Requires head-to-head access to multiple platforms at time-of-use; not feasible with chart data |
| Q6 | RCT design, highest evidence level | Requires intervention development, consent infrastructure, and long follow-up — not Phase −1 feasible |

**FINER table (Step 3):**

| # | F | I | N | E | R | Σ (N=3) |
|---|---|---|---|---|---|---------|
| Q1 | 4 | 5 | ? | 4 | 5 | 21 |
| Q2 | 4 | 3 | ? | 5 | 3 | 18 |
| Q3 | 4 | 4 | ? | 5 | 4 | 20 |
| Q4 | 5 | 3 | ? | 5 | 3 | 19 |
| Q5 | 1 | 3 | ? | 4 | 2 | 13 → kill |
| Q6 | 2 | 5 | ? | 3 | 5 | 18 → defer |

*Q5 killed (Feasibility = 1). Q6 deferred (long-horizon RCT). Top 2: Q1 and Q3.*

**Evolved candidates (Step 4):**

> **Q1-evolved:** Among caregivers of febrile children aged 1–60 months presenting
> to a general pediatric outpatient clinic, does self-reported pre-visit use of a
> generative-AI chatbot for symptom assessment — compared to no AI use — associate
> with longer time from symptom onset to clinic arrival (hours), after adjusting
> for fever height, child age, and parental education?
>
> **Q3-evolved:** Among caregivers presenting with a febrile child aged 1–60 months,
> does pre-visit generative-AI use associate with higher odds of explicitly
> requesting antibiotic treatment at first contact, compared to caregivers who
> used no AI or used the #8000 telephone triage line?

**💡 HUMAN SELECTS: Q1-evolved chosen.** Rationale: time-to-presentation is an objective chart-extractable outcome; Q3's antibiotic-request outcome requires visit-level documentation that is less reliable in current workflows. Q1 addresses the safety concern directly.

---

## 6. Output template — Selected Research Question record

Fill this after the human selects. This record is the handoff to novelty check and study design.

```
SELECTED RESEARCH QUESTION
──────────────────────────────────────────────────────────────
Full question (one sentence, PECO/PICO format):
  [Q1-evolved text]

P:  [Caregivers of febrile children aged 1–60 months, general peds outpatient]
E:  [Pre-visit generative-AI chatbot use for symptom assessment]
C:  [No AI use before visit]
O:  [Time from symptom onset to clinic arrival, hours]
T:  [Measured at visit (cross-sectional + chart review)]
S:  [Cross-sectional observational, single-center]

FINER scores (N score confirmed after novelty check):
  F [4]  I [5]  N [?→TBD]  E [4]  R [5]   Σ = 21+N

Why it beat the alternatives:
  [One paragraph: what Q1 can do that Q3/Q4 cannot]

Why I chose this question (clinical judgment, not AI judgment):
  [Your sentence: what this would change in your practice]

Killed / deferred alternatives and reason:
  Q3 — [outcome reliability concern]
  Q5 — [not feasible]
  Q6 — [defer to future funded study]

Next steps:
  □ Novelty check → references/novelty-check.md
  □ Confirm N score; re-rank if literature settles the question
  □ Study design + power → templates/study-design.md
  □ Pre-registration before data access → templates/preregistration.md
──────────────────────────────────────────────────────────────
```

---

## 7. Common mistakes

| Mistake | Why it fails | Fix |
|---------|-------------|-----|
| Question too broad ("What is the role of AI in pediatrics?") | No study design can answer it; no operationalizable outcome | Apply PECO; force a single measurable outcome |
| Outcome not measurable with available data | Data collection will fail or be biased at collection | Name the specific instrument or variable before scoring Feasibility |
| No real gap ("We wanted to confirm X") | Confirmation of known findings is not a research question | Run novelty check first; if question is settled, kill it |
| Design-led question ("We have a dataset so we asked…") | Question was shaped by available data, not clinical need | Return to the observation; redesign the question before touching the dataset |
| HARKing risk: choosing question to match suspected results | Pre-registered analysis becomes a sham; destroys confirmatory value | Pre-register before data access; any post-hoc question is labeled exploratory only. See `templates/preregistration.md` and `ai-for-science-model.md §5.1` |
| AI selects the question autonomously | Violates 💡 IDEA sovereignty; embeds AI's prior biases about what is "interesting" | Hard stop at Step 5; document who selected and why |
| Five-word question with no comparator ("Effect of AI on outcomes") | Uninterpretable; no direction, no comparison group | Apply PECO test: if any element is missing, the question is not ready |

---

## 8. Team-mode note

In a multi-agent setup, Steps 1–2 (generate + debate) map naturally to parallel
generator agents: each agent receives the observation record and independently
produces a candidate list, then a ranker agent synthesizes them into the FINER
table. This reduces anchoring — agents that do not see each other's candidates
produce a more diverse slate.

However: **Step 5 (human selection) is never delegated to an agent, a ranker, or
a consensus vote among models.** From `ai-for-science-model.md §6` (the autonomy
dial): the 💡 IDEA gate has no autopilot setting, regardless of how the rest of
the loop is configured. Document who selected and their explicit reasoning in the
Output Template — this is the audit trail that `templates/human-loop-ledger.md`
will record.

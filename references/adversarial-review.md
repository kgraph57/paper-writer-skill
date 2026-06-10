# Adversarial Review (Phase 6.5)

> **This is not the quality gate.** `paper-quality-gate` checks cross-section
> consistency, word counts, Methods↔Results correspondence, and AI-pattern removal
> — formatting and logical coherence. This document attacks **scientific validity**.
> A paper can pass every quality-gate check and still contain a finding that is
> chance, confounded, or fabricated. Phase 6.5 exists to catch that.

---

## §0 Two Stages This Runs At

This file is usable at **two distinct pipeline positions**. The mechanics
(four reviewers + steelman + YAML verdict) are identical; what the reviewers
read and what a NOT-ANSWERED forces are different.

| | Stage 1 — Design red-team | Stage 2 — Manuscript red-team |
|---|---|---|
| **When** | Pre-data; before the pre-registration lock | Phase 6.5; after the quality gate clears |
| **Trigger** | Before committing to the registry | After quality gate, before submission |
| **Reviewers read** | `templates/study-design.md`, `templates/preregistration.md`, the questionnaire / instruments | The written manuscript |
| **Claim under test** | "The design, as written, will be able to make [claim X]" | The abstract conclusion sentence |
| **Steelman question** | "Can the design, as written, rule out chance / confounding / selection / common-method bias?" | "Is the finding entirely explained by chance / confounding / bias / p-hacking?" |
| **NOT-ANSWERED forces** | A **design change now** (add a variable, fix the registry primary, secure the analyst) — cheap | A MAJOR or KILL verdict — expensive |
| **Evidence demanded from reviewers** | Design docs, not Results (there are none) | Manuscript + data traces |

### Design-stage failure modes (Stage 1 only)

The manuscript version misses these because they are invisible once data exist:

| Failure mode | What to check |
|---|---|
| **Registry-vs-protocol primary mismatch** | The outcome registered in the trial registry ≠ the primary specified in `preregistration.md` or the Methods draft. Fix before locking. |
| **Core hypothesis not operationalizable by the instrument** | The questionnaire or data source cannot actually measure the stated exposure, mediator, or outcome. A "pathway" claim requires temporal ordering a cross-sectional form can never provide. If unresolvable, downgrade the claim and pre-commit the limitation row. |
| **No pre-decision confounder variable (confounding-by-indication)** | The key confounder (e.g., pre-decision perceived severity) is not in the instrument. If sicker children seek both more AI and higher-acuity care, the central association is **unidentifiable, not merely underpowered** — add the variable or downgrade the claim before locking. |
| **Independent analyst is a placeholder** | The COI-free analyst is named but not contracted / committed. For PI-as-builder studies (product under evaluation = PI's own tool), this is a **gating precondition**, not a checkbox — the design is unregisterable without it resolved. |

### How to run in design mode

1. Substitute `templates/study-design.md` + `templates/preregistration.md` +
   instrument draft wherever the reviewer instructions say "the manuscript"
   or "Results."
2. In the YAML report (§5), set `phase: design` and `claim_under_test` to the
   claim the design intends to support.
3. A NOT-ANSWERED in `steelman_result.status` triggers a **mandatory design
   revision** before the pre-registration lock; do not proceed to registration
   until resolved.
4. On completion, re-run as Stage 2 (Phase 6.5) once the manuscript exists.

---

## 1. Why and When

**The Sakana v2 lesson:** Sakana AI Scientist v2 produced papers that passed a
workshop review (scores 6/7/6) while containing hallucinations, faked results,
novelty inflation, and a misattributed citation. The root cause was structural:
nothing in the autonomous loop was *trying to make the paper fail.* Every agent
was optimizing for a better paper, not for a false one's destruction.

Robin and Google co-scientist were credible because human reviewers, wet-lab
results, and real databases acted as external adversaries. This skill operates
for a **clinician whose name goes on the paper** — a fabricated result is not
an embarrassment but a patient-safety and career-integrity event. The internal
red team is the adversary that arrives before the journal's.

**Placement in the pipeline:**

```
Phase 6:  Quality Review (consistency, formatting, AI patterns)
          ↓
Phase 6.5: Adversarial Review ← YOU ARE HERE
          ↓ PASS
Phase 7:  Pre-Submission (journal selection, cover letter, compliance)
          ↓ KILL or MAJOR
          ↑ back to Discovery / Phase 0 (the loop, not a failure)
```

**Trigger:** Run immediately after the quality gate clears, before any submission
preparation. Do not skip on "exploratory" or "preliminary" grounds — those are the
highest-risk papers.

---

## 2. The Four Hostile Reviewers

Each reviewer holds a single lens and actively tries to find a reason the paper
should not be published. They do not balance; they prosecute. Balancing happens
at the synthesis step.

---

### 2.1 Statistical Reviewer

**Central question:** Does the statistical analysis, as reported, actually support
the stated conclusion?

**Must ask:**

- What was the pre-registered primary analysis? Does `templates/preregistration.md`
  exist and match what is reported? If there is no pre-registration, every
  confirmatory claim is flagged immediately.
- P-values: is the threshold pre-specified? If p=0.049 appears, treat it as a
  warning until the protocol confirms the threshold was set before analysis.
- **Garden of forking paths:** count the number of outcome variables, subgroups,
  time-points, covariates, and model specifications. If any one choice among many
  yields the significant result, the finding is provisional.
- **Multiplicity:** are there multiple comparisons? Is a correction applied (FDR,
  Bonferroni) or justified as absent? Is the primary outcome the one reported first,
  or did it migrate after results were seen?
- **Post-hoc subgroups as confirmatory:** any subgroup result presented without
  pre-specification must be labeled exploratory. If it is labeled confirmatory,
  this is a must-fix.
- **Effect size vs. significance:** is a statistically significant result also
  clinically meaningful? A p=0.001 with OR 1.04 in an n=10,000 cohort is
  significant and trivial. The paper must say which it is.
- **Confidence intervals over p-values:** are 95% CIs reported for all primary
  estimates? A CI that includes 1.0 (or 0) contradicts a "significant" claim —
  check for inconsistency.
- **Power and underpowering:** is the sample size justified? An underpowered
  positive finding is more likely to be a false positive than a true one
  (Winner's Curse). An underpowered negative finding cannot be called "no
  difference."
- **Assumption violations:** parametric tests on non-normal data; chi-squared
  with expected cell counts below 5; Pearson correlation on clearly non-linear
  relationships; Cox model without testing the proportional hazards assumption.
- **Regression-to-the-mean:** if the study selected extreme cases at baseline,
  does the follow-up analysis account for regression to the mean, or does it
  misattribute it to treatment?
- **Baseline imbalance:** in non-randomized designs, are baseline differences in
  key confounders reported? Are they adjusted for, or hand-waved?

**Evidence demanded:**

- A direct comparison of the reported analysis against `templates/preregistration.md`.
- For every p-value in the abstract or conclusions, the corresponding CI and
  effect size.
- The full list of analyses run; if only selected ones are reported, an
  explanation.

---

### 2.2 Methodological Reviewer

**Central question:** Is the study design capable of answering the question it
claims to answer?

**Must ask:**

- **Causal language vs. observational design:** does the paper say "X leads to,"
  "X causes," "X reduces" when the design is cross-sectional, retrospective, or
  observational? Label this precisely: "associated with" is not "caused."
- **Confounding:** draw the DAG (or check `templates/study-design.md`). Is every
  common cause of exposure and outcome either controlled for, restricted on, or
  explicitly acknowledged as residual confounding? Unmeasured confounders are not
  automatically harmless.
- **Selection bias:** how were participants selected? Could selection be related
  to both the exposure and outcome? Hospital-based samples, volunteer samples,
  and administrative database samples each have characteristic biases — name them.
- **Information/measurement bias:** how was the exposure measured? How was the
  outcome ascertained? If by self-report, medical record, or administrative code,
  what is the known misclassification rate? Non-differential misclassification
  biases toward the null; differential misclassification can go either direction.
- **Immortal-time bias:** in cohort and pharmacoepidemiological studies, is any
  follow-up time attributed to exposure that occurred before exposure began?
- **Collider bias:** does adjustment for a collider (a variable caused by both
  exposure and outcome, or their causes) open a spurious association?
- **Missing data:** what proportion is missing? Is the missingness mechanism
  documented (MCAR, MAR, MNAR)? Complete-case analysis under MNAR is not
  acceptable for a primary result without sensitivity analysis.
- **Generalizability / external validity:** who does this population represent?
  A single-center pediatric outpatient cohort from a tertiary hospital cannot
  generalize to community pediatrics without explicit qualification. State the
  scope honestly.
- **Design mismatch:** does the design match the question? A cross-sectional
  design cannot establish temporality; a case series cannot estimate incidence;
  a case-control cannot estimate absolute risk.

**Evidence demanded:**

- The DAG from `templates/study-design.md`, if it exists; if not, a verbal
  causal model and its gaps.
- For every causal-sounding claim in the Discussion or Conclusion, the specific
  design element that justifies it.
- The missingness table and the sensitivity analysis (or an explanation of why
  it was omitted).

---

### 2.3 Novelty Reviewer

**Central question:** Is the paper's contribution actually new?

**Must ask:**

- What, precisely, is the claimed contribution? Strip away hedges ("to our
  knowledge," "in this population") and state it as baldly as possible. Then
  ask: has this been shown before?
- Run `references/novelty-check.md` against the stated contribution. Did the
  initial novelty check run before the study, or after results were known?
  Post-hoc novelty framing is suspect.
- **Stronger prior evidence:** has a larger study, a multi-center study, an RCT,
  or a meta-analysis already established this finding? If so, what does this
  study add beyond replication? Replication has value, but the paper must say
  so honestly rather than claiming novelty.
- **Incremental vs. transformative:** is the contribution "same finding, different
  population" (incremental) or "finding that changes practice or understanding"
  (transformative)? The framing in the abstract and Introduction must match the
  actual scope.
- **Novelty inflation:** does the Introduction or Discussion overstate the gap?
  Every citation used to claim a gap must be checked: does it actually fail to
  answer the question, or does it answer it in a way the authors want to
  re-examine?
- **Negative or null results:** if the main finding is null, is it framed as a
  meaningful null (adequate power, pre-specified, eliminates a previously
  plausible hypothesis) or is it dressed up as a positive finding through
  secondary endpoints or subgroups?

**Evidence demanded:**

- The top 5 most similar papers from `references/novelty-check.md`. For each:
  sample size, design, main finding, and how this paper differs or extends.
- A one-sentence statement of the contribution that the authors will stand behind
  if a reviewer asks the same question.

---

### 2.4 Integrity / Clinical Reviewer

**Central question:** Can every claim be traced to real, correctly attributed
data, and is the paper safe for a clinician to read and act on?

**Must ask:**

- **The 📊 gate:** every number in the abstract and results — does it trace
  directly to a raw data file or analysis output? Any number that cannot be
  traced is a fabrication red flag until proven otherwise.
- **Citation authenticity:** cross-reference the key citations against
  `references/citation-verification.md`. Do the cited papers actually say what
  the text claims? Do the PMIDs resolve to real articles? (The Sakana v2 LSTM
  misattribution originated here.)
- **Overclaiming:** does the Conclusion or Discussion make claims that exceed the
  data? Check every statement with a normative or generalizing force
  ("clinicians should," "this supports changing practice," "all patients with X").
  Is that claim earned by the design and sample?
- **Clinical harm potential:** if a clinician reads the conclusion at face value
  and acts on it, what is the worst realistic outcome? A false-positive finding
  in a therapeutic study could lead to adoption of an ineffective or harmful
  treatment. A false-negative could cause abandonment of an effective one.
  The Discussion must address this; if it does not, require it.
- **Ethics and consent:** are IRB approval number and consent procedure reported
  in the Methods? For retrospective studies, is the waiver documented? For
  pediatric data: is assent/parental consent documented? Missing ethics
  disclosure is a submission blocker, not a minor note.
- **Author contributions and conflicts:** are conflicts of interest complete and
  honest? Does the funding source have a financial interest in the outcome?
  Is the statistical analysis independent or conducted by a party with a stake?
- **Retracted or unreliable citations:** are any key citations from journals or
  authors with documented reliability issues? Check against retraction databases
  if a key finding rests on a single cited paper.

**Evidence demanded:**

- A trace path for the top 3 numbers in the abstract: raw data → analysis output
  → reported value.
- Confirmation that all PMIDs in the reference list resolve and match the claimed
  content.
- Explicit ethics statement in Methods, or a must-fix flag.

---

## 3. The "Steelman the Null" Pass

This is a separate, dedicated procedure run after the four reviewers, before the
verdict. It is the hardest test.

**Procedure:**

1. State the main finding in one sentence as affirmatively as possible.
2. Now argue, as forcefully as you can, that this finding is entirely explained
   by: (a) chance, (b) confounding, (c) measurement bias, (d) selection bias,
   or (e) p-hacking / forking paths.
3. Write this argument out. Do not pull punches. Assume a hostile reviewer with
   domain expertise is writing it.
4. Then ask: does the paper, as written, answer this argument? Specifically:
   - Does the statistical section address chance (power, CI, multiplicity)?
   - Does the Methods/Discussion address confounding with a credible response
     (adjustment, restriction, sensitivity analysis, DAG)?
   - Does the Discussion acknowledge and bound the measurement bias?
   - Does the Discussion name and bound the selection bias?
   - Does the pre-registration exclude forking-paths concerns?

**If the steelman argument is more convincing than the paper's defense:**
the Discussion/Limitations section must be strengthened to address it — or the
conclusion must be downgraded from confirmatory to exploratory. If no credible
response exists, this is a KILL.

A paper that cannot steelman itself has not thought hard enough. A paper that
can steelman itself and answer it has done the work.

---

## 4. Verdict Scheme

| Verdict | Definition | Trigger |
|---------|-----------|---------|
| **KILL** | The central claim is not supported by the design, data, or analysis. Confidence in the finding does not survive even one hostile reviewer's core challenge. | Return to Discovery (Phase −1) or Phase 0. The finding may be an artifact. This is the system working. |
| **MAJOR** | The claim survives but one or more must-fix issues would change the interpretation if corrected, or the steelman argument is not answered. | Substantial revision before re-running Phase 6.5. Do not proceed to Phase 7. |
| **MINOR** | The claim survives and the core interpretation holds. Only should-fix issues remain: hedging language, additional sensitivity analysis, labeling of exploratory analyses. | Fix all should-fix items, then proceed to Phase 7. |
| **PASS** | All four reviewers find no major challenges. Steelman argument is answered by existing text. No must-fix issues. | Proceed to Phase 7 (Pre-Submission). |

**KILL is not a failure.** A KILL at Phase 6.5 costs a revision cycle. A KILL
at a journal costs months, public rejection, and reputation. A KILL after
publication costs careers and, in clinical research, patient safety. The earlier
the kill, the cheaper.

---

## 5. Structured Report Template

```yaml
gate: adversarial_review
phase: 6.5
date: YYYY-MM-DD
paper_id: <project-id>
claim_under_test: "<one sentence: the main finding as stated in the abstract conclusion>"

statistical_reviewer:
  must_fix:
    - "<issue 1>"
  should_fix:
    - "<issue 1>"
  verdict: PASS | MINOR | MAJOR | KILL

methodological_reviewer:
  must_fix:
    - "<issue 1>"
  should_fix:
    - "<issue 1>"
  verdict: PASS | MINOR | MAJOR | KILL

novelty_reviewer:
  must_fix:
    - "<issue 1>"
  should_fix:
    - "<issue 1>"
  verdict: PASS | MINOR | MAJOR | KILL

integrity_reviewer:
  must_fix:
    - "<issue 1>"
  should_fix:
    - "<issue 1>"
  verdict: PASS | MINOR | MAJOR | KILL

steelman_result:
  argument: "<the strongest possible case that the finding is chance/confounding/bias>"
  paper_response: "<how the paper currently answers this, or 'NOT ANSWERED'>"
  status: ANSWERED | PARTIAL | NOT_ANSWERED

must_fix_count: <integer>
should_fix_count: <integer>

gate_verdict: PASS | MINOR | MAJOR | KILL
adjudication: 💡 HUMAN  # final verdict is always human-owned
synthesizer_rationale: "<one paragraph>"
```

This YAML header is compatible with the skill's stage-gate loop. A
`gate_verdict: KILL` halts autonomous progression; a `gate_verdict: PASS`
releases Phase 7. The `adjudication: 💡 HUMAN` field is non-negotiable —
the AI panel advises; the human decides whether to kill the project or revise.

---

## 6. Team-Mode Mapping

In multi-agent execution (`paper-red-team` agent):

| Agent | Role | Runs |
|-------|------|------|
| `stats-attacker` | Statistical Reviewer | In parallel with the other three |
| `methods-attacker` | Methodological Reviewer | In parallel |
| `novelty-attacker` | Novelty Reviewer | In parallel |
| `integrity-attacker` | Integrity / Clinical Reviewer | In parallel |
| `synthesizer` | Adjudicates verdict from four reports + steelman | After all four complete |

The four attackers run in **parallel** — they hold different lenses and do not
read each other's output before writing their own. Parallelism prevents anchoring
on the first reviewer's conclusions. The synthesizer runs after all four reports
are complete and runs the steelman pass before issuing the final `gate_verdict`.

🤖 All four reviewers are AI-executed. The `gate_verdict` field in the YAML is
AI-proposed. The 💡 gate — "do I kill this project or fix it" — is **human-owned
and cannot be delegated**, per `ai-for-science-model.md §2` and the hard rules
in §6. The AI panel is a forcing function for human judgment, not a replacement.

---

## 7. Pre-Submission Adversarial Checklist

Run this manually if the agent is not available. One check = one honest answer.
If the honest answer is "I don't know" or "I didn't check," treat it as a flag.

**Statistical integrity**
- [ ] Pre-registration exists and the reported primary analysis matches it
- [ ] All p-values have corresponding CIs and effect sizes reported
- [ ] The primary outcome did not change between registration and reporting
- [ ] Every subgroup result presented in the abstract or conclusion was
      pre-specified (or is explicitly labeled exploratory)
- [ ] Multiple comparisons correction is applied or absence is justified
- [ ] Sample size justification is present and not post-hoc
- [ ] Parametric test assumptions were checked and reported

**Methodological soundness**
- [ ] All causal language ("causes," "leads to," "reduces") is earned by the design
- [ ] The DAG or causal model is documented; major confounders are addressed
- [ ] Selection process is fully described; selection bias named and bounded
- [ ] Measurement validity and potential misclassification are addressed
- [ ] Missing data mechanism is documented; sensitivity analysis exists
- [ ] Generalizability is explicitly bounded in Discussion

**Novelty honesty**
- [ ] The top 5 most similar prior studies are cited and their differences stated
- [ ] The contribution statement survives re-reading after results are known
- [ ] No citation used to claim a gap actually closes the gap

**Integrity and clinical safety**
- [ ] Every number in the abstract traces to a raw data file or analysis output
- [ ] All key citations resolve (PMID checked) and say what the text claims
- [ ] IRB approval number and consent procedure are in the Methods
- [ ] Conflicts of interest and funding are complete and honest
- [ ] The Conclusion does not recommend clinical action beyond what the design supports

**Steelman**
- [ ] The strongest alternative explanation (chance / confounding / bias) is
      named in the Discussion
- [ ] The paper provides a credible response to that alternative explanation,
      or explicitly acknowledges it cannot

**Verdict**
- [ ] The gate_verdict YAML header is filled in and reviewed by the human author
      before Phase 7 begins

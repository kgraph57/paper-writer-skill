# Study Design Template

**Phase −1 | Position:** After novelty-check (`references/novelty-check.md`) → **HERE** → Pre-registration (`templates/preregistration.md`)

**Purpose:** Turn a selected, novelty-checked research question into a complete, powered, analyzable protocol. This document IS the pre-registered plan and WILL become the Methods section. One document; three downstream lives.

**Output contract:** A completed "Study Design Record" (§9). Freeze it before the 📊 DATA gate. Anything decided after seeing data is exploratory — label it or retract it.

---

## 1. Purpose & Placement in the Loop

```
[novelty-check] → [study-design] → [preregistration LOCK] → 📊 DATA gate → [analysis → draft]
                        ↑
                   YOU ARE HERE
```

Phase −1 ends when the Study Design Record is complete and pre-registered. The human's job at this step:
- Approve or reject the design AI drafts
- Own the ethics decision (equipoise, consent, population)
- Confirm the data is obtainable (the 📊 gate check in §7)
- Sign the pre-registration record (irrevocable lock)

🤖 AI executes: design drafting, power calculation, DAG, analysis plan, reporting-guideline mapping.
💡 Human owns: design approval, feasibility reality-check, ethics judgments.

---

## 2. Design Selection Decision Tree

### Step 1: What kind of question is this?

| Question type | Primary goal | Candidate designs |
|---|---|---|
| Frequency / prevalence | Describe burden | Cross-sectional |
| Etiology / risk factor | Does X cause Y? | Cohort, Case-control, RCT |
| Diagnosis / screening | Does test T identify disease D? | Diagnostic accuracy (STARD) |
| Prognosis | What happens to patients with condition C? | Prospective/retrospective cohort |
| Prediction model | Build a score to predict outcome O | Prediction model (TRIPOD+AI) |
| Intervention efficacy | Does treatment T beat control C? | RCT (CONSORT) |
| Intervention effectiveness (real-world) | Same, in routine care | Quasi-experiment, pragmatic RCT |
| Patient experience / meaning | How do patients understand X? | Qualitative (COREQ) |
| Complex causal pathway | Multiple mechanisms | Mixed-methods |

### Step 2: Map to design + reporting guideline

| Design | Guideline | Key reference | Evidence level |
|---|---|---|---|
| RCT | CONSORT 2010 (+extensions) | `references/reporting-guidelines-full.md` | I |
| Systematic review / MA | PRISMA 2020 | ditto | I (synthesis) |
| Prospective cohort | STROBE | ditto | II |
| Retrospective cohort | STROBE | ditto | III |
| Case-control | STROBE | ditto | III |
| Cross-sectional | STROBE | ditto | IV |
| Diagnostic accuracy | STARD 2015 | ditto | varies |
| Prediction model / ML | TRIPOD+AI (2024) | ditto | varies |
| Quasi-experimental | TREND | ditto | III |
| Qualitative | COREQ / SRQR | ditto | qualitative |

**Honesty check for clinicians:** A retrospective chart review or a single-center cross-sectional study is most of what a busy clinician can do. That is fine — incremental evidence at a real local population beats a perfect design that never happens. State the limitations; don't pretend it is something it isn't.

Evidence hierarchy (informal): RCT > prospective cohort > retrospective cohort > case-control > cross-sectional. Diagnostic / prediction models sit outside this hierarchy — they answer different questions.

### Step 3: Feasibility filter (run before committing)

| Constraint | Question to answer | Impact if NO |
|---|---|---|
| Prospective follow-up | Can I track patients ≥ N months? | Drop to retrospective or cross-sectional |
| Randomization | Is equipoise real? Is N achievable? | Drop to observational |
| Existing records | Are the variables captured in the EHR? | Redesign variables or add data collection |
| Event rate | Rare outcome? | Case-control more efficient than cohort |
| IRB timeline | How long is approval? | May gate entire study start |

---

## 3. PICO → Operational Variables

For every PICO element, resolve to a concrete variable before you move on.

### Decomposition table (fill one row per variable)

| PICO element | Concept | Variable name | Type | Instrument / source | Timing | Missing rate expected |
|---|---|---|---|---|---|---|
| P – Population | e.g., febrile infants | `age_days`, `fever_temp_c` | continuous, continuous | EHR vital signs | ED presentation | <5% |
| I – Intervention / Exposure | e.g., ibuprofen use | `ibuprofen_given` | binary (0/1) | EHR medication order | within 4h of arrival | <5% |
| C – Comparator | e.g., acetaminophen only | `comparator_group` | binary | derived | same | — |
| O – Outcome (PRIMARY) | e.g., fever resolution at 4h | `temp_normal_4h` | binary | EHR vital at 4h ± 30 min | 4h post-treatment | ~15% (discharge before 4h) |
| O – Outcome (secondary 1) | ED revisit within 48h | `revisit_48h` | binary | EHR link | 48h | <3% |
| Confounder | age, comorbidity | `age_months`, `comorbidity_score` | continuous, integer | EHR | baseline | <5% |

**Primary outcome rule:** ONE primary outcome. Period. If you list two, the sample size is wrong, the type-I error is inflated, and reviewers will ask which one you really cared about. Secondary outcomes are hypothesis-generating; they do not change the primary N.

If you genuinely have two co-primary outcomes, pre-specify a Bonferroni or Holm correction and power for both — then justify why you need both.

**Exception — descriptive co-primaries (no multiplicity penalty):** Purely descriptive estimands (proportions/means reported with a CI) **may be co-primary without a multiplicity penalty** — they are estimation targets, not tests against a null. There is no type-I error to inflate when nothing is being tested; each estimate stands on its own precision (§5.0 Precision-power). This is the descriptive-primary track: power = CI half-width, not detectable difference. Require a one-line justification in the record and cross-link `templates/preregistration.md` §D, which carries the identical carve-out. The moment any of these estimands is compared against a reference value or against each other, it leaves the descriptive track and the multiplicity rule above re-applies.

---

## 4. Confounding & Bias

### 4.1 DAG thinking (Directed Acyclic Graph)

Before selecting covariates, draw the assumed causal structure. The goal: identify the **minimal sufficient adjustment set** — include confounders, exclude colliders and mediators on the causal path.

**ASCII DAG template:**

```
  Confounder (e.g., age)
       │           │
       ▼           ▼
  Exposure ──────▶ Outcome
       │
       ▼
  Mediator (e.g., fever duration) ──▶ Outcome
                ↑
           [DO NOT adjust for mediators if estimating total effect]

  Collider: Exposure──▶ Collider ◀──Outcome
           [NEVER adjust for a collider — opens a spurious path]
```

**Key rules:**
- Adjust for confounders (common causes of exposure AND outcome).
- Do NOT adjust for mediators (on the causal path) unless you want the direct effect only.
- Do NOT adjust for colliders (common effects). Conditioning on a collider opens a non-causal backdoor. Classic example: adjusting for hospitalization in a study of smoking and disease.
- Use DAGitty (free web tool) or ggdag (R) to verify.

### 4.2 Bias threat register (fill for your design)

| Bias type | Mechanism | Your specific risk | Mitigation |
|---|---|---|---|
| Selection bias | Non-random entry into study | Single-center, referral center population | State explicitly; sensitivity in broader population |
| Information bias | Differential measurement | Outcome assessor knows exposure (retrospective) | Blind outcome extraction; standardize criteria |
| Confounding | Unmeasured common causes | Socioeconomic status not in EHR | Mention as limitation; propensity score if proxy available |
| Immortal-time bias | Person-time before exposure eligibility credited to exposed | Drug exposure defined by first prescription — time before prescription is "immortal" | Time-fixed or time-varying Cox model |
| Attrition bias | Loss to follow-up differs by exposure | Sicker patients drop out of follow-up | Compare lost vs. retained; sensitivity under missing-data assumptions |
| Recall bias | Differential retrospective reporting | Case-control only | Use objective data sources when possible |
| Lead-time bias | Earlier detection advances survival time artificially | Screening studies | Use disease-specific mortality, not overall survival |

---

## 5. Sample Size / Power

**Mantra:** Justify the assumed effect size from the literature found in novelty-check. Using a "clinically meaningful difference" that is 3× larger than any published effect is not justification — it is hope.

### 5.0 Two power regimes (pick BEFORE you calculate)

Power is not one thing. Which regime you are in is decided by the primary estimand, not by taste.

| Regime | Primary estimand | "Power" means | N driven by | Formula source |
|---|---|---|---|---|
| **(a) Difference-power** | A difference / OR / HR tested against a null | Probability of detecting a true effect of size δ | δ, α, 1−β | §5.1–5.3 (existing) |
| **(b) Precision-power** | A descriptive proportion/mean reported with a CI | CI half-width small enough to be useful | p, target half-width E | §5.0 table below |

For a **descriptive primary** (the descriptive-primary track in §3), you do NOT have a δ to power against — there is no null. You power for **precision**: choose the proportion you expect and the CI half-width you are willing to live with, then solve for N. Use the **Wilson** interval (not Wald) for proportions — Wald is anticonservative at small N and near 0/1.

**Wilson CI half-width by N and p (two-sided 95%, worked numbers):**

| Expected p | N = 200 | N = 400 | N = 600 |
|---|---|---|---|
| 0.10 | ±4.3 pp | ±3.0 pp | ±2.5 pp |
| 0.30 | ±6.3 pp | ±4.5 pp | ±3.7 pp |
| 0.50 | ±6.9 pp | ±4.9 pp | ±4.0 pp |

Read it directly: a descriptive primary at **p = 0.30 reaches ±4.5 pp at N = 400** and **±6.3 pp at N = 200** — halving the interval costs roughly 4× the N (precision scales with √N). **Precision is BETTER at low p:** the half-width is widest near p = 0.50 and shrinks as p moves toward 0 or 1, so a rare-ish descriptive primary buys tighter intervals for the same N. State the chosen (p, E, N) triplet in the Study Design Record exactly as you would state δ/α/power for a difference-power study.

```python
# Precision-power for a descriptive proportion (Wilson half-width → N)
from statsmodels.stats.proportion import proportion_confint
def wilson_halfwidth(p, n):
    lo, hi = proportion_confint(round(p*n), n, alpha=0.05, method="wilson")
    return (hi - lo) / 2
for n in (200, 400, 600):
    print(f"p=0.30, N={n}: ±{wilson_halfwidth(0.30, n)*100:.1f} pp")
# p=0.30, N=200: ±6.3 pp / N=400: ±4.5 pp / N=600: ±3.7 pp
```

### 5.1 Required inputs (fill before calculating)

| Input | Symbol | Source | Your value |
|---|---|---|---|
| Effect size / OR / HR / difference | δ | Prior literature (novelty-check) | ___ |
| Type-I error (two-sided) | α | Convention: 0.05 | 0.05 |
| Power | 1-β | Convention: 0.80 (80%) or 0.90 | 0.80 |
| Allocation ratio (RCT) | k = n2/n1 | Design choice | 1:1 |
| Expected event rate (survival/proportion) | p0 | Registry / prior studies | ___ |
| SD of outcome (continuous) | σ | Prior studies | ___ |
| Anticipated loss to follow-up | — | Local estimate | ___ |
| Inflate N by: | N_final = N_calc / (1 − dropout) | — | ___ |

### 5.2 Formulas for common cases

**Two proportions (chi-square / Fisher):**
n per group ≈ 2 × [(z_α/2 + z_β)² × p̄(1−p̄)] / (p1−p2)²
where p̄ = (p1+p2)/2

**Two means (t-test):**
n per group ≈ 2σ²(z_α/2 + z_β)² / δ²

**Survival / log-rank:**
Events required = 4(z_α/2 + z_β)² / [ln(HR)]²
Recruit N = Events / (expected event proportion over follow-up)

**Single proportion precision (cross-sectional):**
n = z_α/2² × p(1−p) / E²
where E = desired margin of error (e.g., 0.05)

**Correlation:**
n ≈ [(z_α/2 + z_β) / atanh(r)]² + 3

### 5.3 Python power calculation (runnable snippets)

**Case 1: Two proportions (most common in clinical research)**
```python
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Example: p_control=0.30, p_treatment=0.45
p0, p1 = 0.30, 0.45
effect = proportion_effectsize(p1, p0)          # Cohen's h
power_analysis = NormalIndPower()
n_per_group = power_analysis.solve_power(
    effect_size=effect,
    alpha=0.05,
    power=0.80,
    ratio=1.0                                    # 1:1 allocation
)
dropout = 0.10                                   # 10% expected dropout
n_required = int(n_per_group / (1 - dropout)) + 1
print(f"N per group (before dropout): {n_per_group:.1f}")
print(f"N per group (after +{int(dropout*100)}% dropout): {n_required}")
print(f"Total N: {n_required * 2}")
```

**Case 2: Two means / continuous outcome**
```python
from statsmodels.stats.power import TTestIndPower

# Example: mean difference=5, SD=12 (from prior literature)
mean_diff, sd = 5, 12
effect_size = mean_diff / sd                     # Cohen's d
power_analysis = TTestIndPower()
n_per_group = power_analysis.solve_power(
    effect_size=effect_size,
    alpha=0.05,
    power=0.80,
    ratio=1.0
)
dropout = 0.10
n_required = int(n_per_group / (1 - dropout)) + 1
print(f"Cohen's d: {effect_size:.3f}")
print(f"N per group (inflated for dropout): {n_required}")
```

### 5.4 Feasibility gate

After you have N_required: Is this achievable?

```
Annual volume at your clinic × study period (years) × eligibility fraction
    ≥ N_required?

  YES → proceed
  NO  → options:
        (a) Extend study period
        (b) Multi-center collaboration
        (c) Reduce power to 0.80 and limit to detectable OR ≥ X
        (d) Switch to a more efficient design (case-control if outcome is rare)
        (e) Accept the underpowered study as exploratory — label it so
```

**Underpowered is not a reason to not publish. It is a reason to not claim confirmatory evidence.**

### 5.5 EPV for the real adjustment set (the "6-covariate" trap)

A descriptive primary needs precision-power (§5.0). But the moment you fit an **adjusted** model for any analytic aim, a second budget binds: **events per variable (EPV)**.

**EPV = events ÷ ESTIMATED PARAMETERS** — and "parameters" is NOT "number of variables." Categorical covariates **expand into dummy columns**: a k-level factor costs k−1 df, a spline costs its basis df, an interaction costs the product. Count df **as collected**, not "1 per variable." The classic failure: a model described as "6 covariates" was really age-band (×4 dummies) + region (×5) + insurance (×3) + season (×3) + sex (×1) + device (×2) ≈ **18 df**. At the EPV ≥ 10 rule of thumb that needs **~180 events**, not 60. Studies that count variables instead of df ship models that are silently 3× overfit.

**Min-N formula (work backward from df, then from the rate):**

```text
events_needed   = 10 × params              # params = EXPANDED df, not variable count
N ≥ (10 × params) / (rate × linkage)
```

where `rate` = outcome proportion and `linkage` = fraction of N that lands in the analyzable set (§5.6). At rate 0.30, an 18-df model needs N ≥ 600 *before* linkage; at 70% linkage, N ≥ 857.

**Rescue rule when EPV is short (the realistic small-N case):**

| Situation | What you may fit | What you may NOT fit |
|---|---|---|
| **Descriptive primary** | Proportions/means + CI (precision-power, §5.0) — **confirmatory** | — |
| **Common outcome, EPV tight** | **ONE parsimonious model: ≤4 estimated parameters, age entered LINEARLY (not banded), Firth-penalized** logistic to tame small-sample/separation bias; report adjusted OR as **exploratory** | A "kitchen-sink" 18-df model; stepwise selection |
| **Rare outcomes (delayed / severe)** | **Counts + exact (Clopper–Pearson) CIs only** | Any adjusted OR — no multivariable model on a handful of events |

Firth penalization (penalized likelihood) is the default for the one parsimonious model: it removes first-order small-sample bias and handles separation, which ordinary `glm` cannot. Entering age **linearly** spends 1 df instead of 3–4 — the single cheapest way to claw back EPV. Anything beyond the one rescue model is exploratory by construction.

### 5.6 Linkage / analyzable-set note (EPV rides on N × linkage)

Headline N is a lie if the analytic set is a **linked subset**. When the model can only run on records where a required field is present (e.g., physician/clinic linked, biomarker drawn, consent re-confirmed), every EPV and precision figure rides on **N × linkage**, not on enrollment N. A study of 1,000 with 60% physician-linkage powers its adjusted models as if N = 600.

Pre-specify, before the lock:

- the **expected linkage rate** (cite the source) and treat it as a power input alongside δ or (p, E);
- a **CONSORT-style valid → linked flow** (enrolled → eligible/valid response → successfully linked → analyzable), with the count and reason for loss at each step, so the analyzable denominator is auditable;
- which estimands run on the **full** valid set (descriptive primary) vs. the **linked subset** (adjusted exploratory aims) — they have different N and must report different denominators.

---

## 6. Pre-specified Analysis Plan

This section is copied verbatim into the pre-registration record. Every deviation after data lock must be disclosed.

### 6.1 Primary analysis

| Element | Specify |
|---|---|
| Primary outcome | [exact variable name from §3] |
| Statistical model | e.g., multivariable logistic regression / Cox PH / linear regression |
| Adjustment set | [list covariates from DAG §4; justify each] |
| Test statistic / estimand | e.g., OR with 95% CI; two-sided Wald test |
| Significance threshold | α = 0.05 (or adjusted if co-primary) |
| Analysis script | `scripts/analysis-template.py --analysis logistic` |

Map to analysis scripts:
- Binary outcome → `scripts/analysis-template.py --analysis logistic`
- Continuous outcome → `scripts/analysis-template.py --analysis linear`
- Survival outcome → `scripts/analysis-template.py --analysis survival`
- Table 1 → `scripts/table1.py`
- Subgroup forest plot → `scripts/forest-plot.py`

### 6.2 Missing data

Pre-specify before seeing the data:

| Expected missing rate | Strategy |
|---|---|
| < 5% on all variables | Complete case analysis; sensitivity with multiple imputation (MI) |
| 5–20% on ≤ 2 key variables | Multiple imputation (m ≥ 20 imputations; `statsmodels` or `miceforest`) |
| > 20% or outcome missing | This is a data quality problem — resolve before analysis, or redesign |
| Outcome missing > 5% | Sensitivity: best-case / worst-case scenario imputation |

Never use mean imputation for a clinical variable — it biases variance.

### 6.3 Multiple comparisons

| Scenario | Pre-specified strategy |
|---|---|
| 1 primary outcome | No correction needed for primary test |
| Co-primary outcomes | Bonferroni (α/k) or Holm-Bonferroni |
| Secondary outcomes | Report uncorrected p-values; label as hypothesis-generating |
| Pre-specified subgroups | Report with interaction p-value; do NOT interpret non-significant interactions as "no effect" |
| Post-hoc subgroups | EXPLORATORY label mandatory; no confirmatory claims |

### 6.4 Pre-specified subgroups (list here, in advance)

| Subgroup variable | Rationale | Interaction test |
|---|---|---|
| e.g., age < 6 months vs. ≥ 6 months | Different physiology / pharmacokinetics | Yes — p_interaction |
| e.g., fever height ≥ 39.5°C | Potential effect modification | Yes |

**Rule:** Post-hoc subgroups added after seeing the data are exploratory. They cannot confirm a hypothesis. They generate the next study's question.

### 6.5 Sensitivity analyses (pre-specified)

| Sensitivity analysis | Purpose |
|---|---|
| Exclude [specific subgroup — pre-specify] | Test robustness to potential selection artifact |
| Per-protocol vs. intention-to-treat | RCT: both must be reported |
| Different confounder adjustment set (e.g., add socioeconomic proxy) | Test DAG assumption sensitivity |
| Complete case vs. MI | Validate missing-data assumption |
| Alternative outcome definition | Test outcome measurement sensitivity |

---

## 7. Feasibility & Ethics Quick-Check

📊 DATA GATE — the human must answer YES to all before proceeding.

| Item | Check |
|---|---|
| IRB pathway | Exempt / expedited / full board? Estimated approval timeline: ___ weeks |
| Consent model | Individual informed consent / waiver of consent (retrospective) / broad consent — which applies? |
| Data availability | Variables in §3 — are ALL of them actually in the EHR / registry you have access to? |
| De-identification | Can you receive a de-identified dataset, or must you work within the hospital system? |
| Timeline | Data collection end → analysis → submission → target journal turnaround = ___ months total |
| Funding / support | Statistical consultation needed? Biostatistician identified? |
| Patient safety | Is equipoise real? Is there a stopping rule for harm (RCT)? |

**If any check is NO:** Stop here. Redesign before the pre-registration lock. A broken feasibility assumption found after data collection is far more expensive than finding it now.

---

## 8. Worked Pediatric Example

**Research question (from novelty-check):** Among febrile infants aged 3–12 months presenting to a single-center pediatric ED, does combination antipyretic therapy (ibuprofen + acetaminophen, alternating 4-hourly) reduce the proportion with fever at 4 hours compared with acetaminophen monotherapy?

### 8.1 Design selection

- Question type: intervention → two treatment arms → RCT is ideal.
- Feasibility check: a single-center ED seeing ~400 eligible febrile infants/year; 80 per year meeting strict inclusion. A 2-year study yields ~160 eligible — likely insufficient for a powered RCT.
- Decision: **Retrospective cohort** using EHR medication orders as natural experiment (some MDs use combination therapy, some do not). Quasi-experimental. Evidence level III. Will report with STROBE.

### 8.2 Variables

| Element | Variable | Type | Source | Timing |
|---|---|---|---|---|
| P | `age_months`, `fever_temp_c_arrival` | continuous | EHR vitals | ED arrival |
| I | `combo_therapy` (1=alternating, 0=single) | binary | EHR medication orders | within 1h of arrival |
| C | `acetaminophen_only` | reference group | derived | — |
| O (primary) | `temp_normal_4h` (< 37.5°C at 4h ± 30 min) | binary | EHR vitals | 4h post-first-dose |
| O (secondary) | `revisit_72h`, `temp_at_2h` | binary, continuous | EHR / telephone follow-up | 72h, 2h |
| Confounders | `age_months`, `initial_temp`, `viral_dx`, `season`, `attending_id` | various | EHR | baseline |

**Primary outcome: one.** `temp_normal_4h`.

### 8.3 DAG

```
age_months ──────────────────────────────▶ temp_normal_4h
     │                                           ▲
     └──▶ combo_therapy ────────────────────────┘
               ▲                  │
     viral_dx ─┘          fever_duration (MEDIATOR — exclude from
     initial_temp ─────▶  combo_therapy   primary adjustment)
     attending_id ──────▶ (prescriber preference = instrument candidate)
```

Adjust for: `age_months`, `initial_temp`, `viral_dx`, `season`. Do NOT adjust for `fever_duration_before_ED` (mediator if on causal path). Consider `attending_id` as a fixed effect or cluster variable.

### 8.4 Sample size

Prior literature: combination therapy increases fever-free rate at 4h from 38% to 55% (illustrative; verify in novelty-check before using).

```python
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

p0, p1 = 0.38, 0.55
effect = proportion_effectsize(p1, p0)
n = NormalIndPower().solve_power(effect_size=effect, alpha=0.05, power=0.80, ratio=1.0)
# → n ≈ 95 per group; inflate 10% for missing 4h vital: n = 106 per group, total N = 212
```

Feasibility: 400 eligible/year × 50% in each arm (if attending practice is ~50/50) × 2 years = 400 total. **N = 212 is achievable.** Proceed.

### 8.5 Analysis plan

- Primary: multivariable logistic regression; `temp_normal_4h` ~ `combo_therapy` + `age_months` + `initial_temp` + `viral_dx` + `season`; report adjusted OR with 95% CI.
- Script: `scripts/analysis-template.py --analysis logistic --outcome temp_normal_4h --predictors combo_therapy age_months initial_temp viral_dx season`
- Table 1: `scripts/table1.py --group combo_therapy`
- Missing data: < 15% expected (early discharge before 4h vital). Pre-specify MI with `miceforest` if > 5%.
- Pre-specified subgroup: age < 6 months vs. ≥ 6 months (pharmacokinetic rationale); report interaction p-value.
- Sensitivity: (a) restrict to attending IDs with ≥ 10 cases; (b) outcome at 3.5–4.5h window rather than 4h ± 30 min.

### 8.6 Feasibility / ethics

- Design = retrospective chart review → IRB: expedited review / waiver of consent likely.
- All variables present in the hospital EHR system.
- Timeline: IRB 8 weeks → data extraction 4 weeks → analysis 4 weeks → draft 6 weeks → submission. ~6 months total.
- No patient safety concern (retrospective observation only).

---

## 9. Study Design Record (Output Template)

Copy this block into `preregistration.md` and into the Methods section draft.

```markdown
## Study Design Record

**Date locked:** YYYY-MM-DD
**Version:** 1.0 (pre-data)

### Question
[Paste FINER-checked question from research-question.md]

### Design
- Type: [RCT / prospective cohort / retrospective cohort / case-control / cross-sectional / diagnostic accuracy / prediction model]
- Setting: [institution, department, study period]
- Reporting guideline: [CONSORT / STROBE / STARD / TRIPOD+AI / other]

### Population
- Inclusion: [list criteria]
- Exclusion: [list criteria]
- Anticipated N: [from §5]

### Exposures / Interventions
[Variable name, type, measurement instrument, timing]

### Primary Outcome (ONE)
[Variable name, type, measurement, timing, definition of event]

### Secondary Outcomes
[List; note these are hypothesis-generating]

### Confounders / Adjustment Set
[List; reference DAG in §4; note what was excluded and why]

### Sample Size Justification
- Effect size assumed: [value + source citation from novelty-check]
- α: 0.05, Power: 0.80
- N per group: [value], Total N: [value]
- Dropout inflation: [%], Final N: [value]

### Primary Analysis
- Model: [logistic / linear / Cox / other]
- Covariates: [list]
- Test statistic: [Wald / LR test / log-rank]
- Script: `scripts/analysis-template.py [flags]`

### Missing Data Strategy
[complete case / MI — method, m= ]

### Pre-specified Subgroups
[list with interaction test plan]

### Sensitivity Analyses
[list]

### IRB / Ethics
- IRB number: [pending / approved: #]
- Consent: [individual / waived]

### Data Gate (📊)
- Human confirmed data obtainability: [YES / NO]
- Human confirmed IRB path: [YES / NO]
```

---

## 10. Common Mistakes

| Mistake | Why it kills the study | Fix |
|---|---|---|
| Underpowered (N set by convenience, not calculation) | True effects will be missed; null results uninterpretable | Calculate N before data collection; label as exploratory if underpowered |
| Multiple primary outcomes | Inflated type-I error; unclear what the paper is about | ONE primary outcome; demote the rest to secondary |
| Adjusting for a collider | Opens a spurious non-causal association; reverses effects | Draw the DAG; never adjust for a common *effect* of exposure and outcome |
| Effect size from hope ("we expect a 50% reduction") | Gross underestimate of N needed; study fails | Extract effect from 2–3 published studies in novelty-check; be conservative |
| Design that cannot answer the question | Cross-sectional study used to infer causality; diagnostic study without index test independence | Match design to question type (§2 decision tree) |
| No missing-data plan | Reviewer rejects or demands re-analysis; conclusions may change | Pre-specify complete-case + MI sensitivity before any analysis |
| Post-hoc subgroups reported as confirmatory | HARKing; inflated false discovery rate | Label ALL post-hoc analyses as exploratory; never p < 0.05 = confirmed in a subgroup |
| Pre-registration after peeking at data | Invalidates the pre-registration entirely | Lock the Study Design Record before the 📊 DATA gate opens |
| Mediator in the adjustment set | Blocks the very pathway you are trying to estimate | Draw DAG; exclude mediators for total-effect estimates |
| Immortal-time bias in cohort | Falsely inflates apparent benefit of exposure | Use time-varying Cox model; start follow-up at exposure time, not cohort entry |

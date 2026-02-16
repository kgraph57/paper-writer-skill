# GRADE Evidence Assessment Template

> The Grading of Recommendations Assessment, Development and Evaluation (GRADE) approach
> rates the certainty of evidence for each outcome across studies.
> Reference: Guyatt et al., BMJ 2008;336:924-926.

---

## Overview

GRADE assesses certainty of evidence on a four-level scale:

| Level | Definition | Symbol |
|-------|-----------|--------|
| **High** | Very confident that the true effect lies close to the estimate | ++++ |
| **Moderate** | Moderately confident; the true effect is likely close but may be substantially different | +++O |
| **Low** | Limited confidence; the true effect may be substantially different | ++OO |
| **Very Low** | Very little confidence; the true effect is likely substantially different | +OOO |

**Starting point:**
- Randomized trials start at HIGH
- Observational studies start at LOW

---

## 1. Downgrade Factors

### 1.1 Risk of Bias (Study Limitations)

**Assessment question:** Are there serious limitations in study design or execution that reduce confidence?

| Severity | Action | Criteria |
|----------|--------|----------|
| No serious | No downgrade | Most studies at low RoB; no study at high RoB contributes >50% of the weight |
| Serious | Downgrade 1 level | Several studies with some concerns; or one influential study at high RoB |
| Very serious | Downgrade 2 levels | Most studies at high RoB; or all studies contributing to the estimate have serious limitations |

**Decision rules:**
- Focus on studies that contribute most weight to the pooled estimate
- Consider whether limitations likely bias toward or away from the intervention effect
- Use individual study RoB assessments (from RoB 2, NOS, etc.) as input

**Rating for this review:**

| Outcome | Key Concerns | Severity | Downgrade |
|---------|-------------|----------|-----------|
| {{OUTCOME_1}} | {{CONCERNS}} | Not serious / Serious / Very serious | 0 / -1 / -2 |
| {{OUTCOME_2}} | {{CONCERNS}} | Not serious / Serious / Very serious | 0 / -1 / -2 |

---

### 1.2 Inconsistency

**Assessment question:** Are results consistent across studies?

| Severity | Action | Criteria |
|----------|--------|----------|
| No serious | No downgrade | I2 < 40% and overlapping CIs; consistent direction of effect |
| Serious | Downgrade 1 level | I2 = 40-75%; some variation in effect size but consistent direction |
| Very serious | Downgrade 2 levels | I2 > 75%; inconsistent direction of effects; unexplained heterogeneity |

**Decision rules:**
- Consider I2 statistic, but do not rely on it alone
- Examine overlap of confidence intervals across studies
- Check for consistent direction of effect
- Consider whether subgroup analyses explain heterogeneity
- If heterogeneity is fully explained by pre-specified subgroups, may not downgrade
- With only 2 studies, I2 is unreliable; focus on effect direction and magnitude

**Additional considerations:**
- Point estimates vary widely across studies: suggests inconsistency
- Prediction interval crosses null or clinically important threshold: suggests inconsistency
- I2 can be misleading with few studies or when all studies are large

**Rating for this review:**

| Outcome | I2 | Prediction Interval | Direction Consistent? | Severity | Downgrade |
|---------|-----|--------------------|-----------------------|----------|-----------|
| {{OUTCOME_1}} | {{I2}}% | {{PI}} | Yes / No | Not serious / Serious / Very serious | 0 / -1 / -2 |
| {{OUTCOME_2}} | {{I2}}% | {{PI}} | Yes / No | Not serious / Serious / Very serious | 0 / -1 / -2 |

---

### 1.3 Indirectness

**Assessment question:** Is the evidence directly applicable to the review question?

| Severity | Action | Criteria |
|----------|--------|----------|
| No serious | No downgrade | PICO elements in studies closely match the review question |
| Serious | Downgrade 1 level | One element of PICO substantially differs; or surrogate outcome used |
| Very serious | Downgrade 2 levels | Multiple elements differ; or the evidence addresses a fundamentally different question |

**Types of indirectness:**

| Type | Example |
|------|---------|
| **Population** | Studies in adults when question is about elderly; different severity |
| **Intervention** | Different dose, formulation, or delivery from the intervention of interest |
| **Comparator** | Active comparator when question asks about placebo comparison |
| **Outcome** | Surrogate outcome (e.g., LDL levels instead of cardiovascular events) |
| **Setting** | Hospital-based when question is about primary care |
| **Indirect comparison** | No head-to-head trials; evidence from network of trials |

**Decision rules:**
- Assess each PICO element separately
- Surrogate outcomes always warrant consideration for downgrade
- Head-to-head comparisons are preferable to indirect comparisons
- Consider whether differences are large enough to meaningfully alter the effect

**Rating for this review:**

| Outcome | Indirectness Type | Details | Severity | Downgrade |
|---------|-------------------|---------|----------|-----------|
| {{OUTCOME_1}} | {{TYPE}} | {{DETAILS}} | Not serious / Serious / Very serious | 0 / -1 / -2 |
| {{OUTCOME_2}} | {{TYPE}} | {{DETAILS}} | Not serious / Serious / Very serious | 0 / -1 / -2 |

---

### 1.4 Imprecision

**Assessment question:** Is the effect estimate precise enough to support a decision?

| Severity | Action | Criteria |
|----------|--------|----------|
| No serious | No downgrade | Narrow CI; adequate sample size; CI does not cross decision thresholds |
| Serious | Downgrade 1 level | Wide CI crossing one decision threshold; or OIS not met |
| Very serious | Downgrade 2 levels | Very wide CI crossing both sides of the decision threshold; very small sample |

**Decision rules:**

For **dichotomous outcomes:**
- Calculate the Optimal Information Size (OIS): the sample size a single adequately powered trial would need
- If total N < OIS, consider downgrading for imprecision
- If 95% CI includes both appreciable benefit (RR < 0.75) and appreciable harm (RR > 1.25), downgrade
- If 95% CI crosses the null (RR = 1.0), consider clinical significance of included range

For **continuous outcomes:**
- If 95% CI includes both clinically important and clinically unimportant effects, downgrade
- Define the minimal clinically important difference (MCID) a priori
- If total N < 400 (rule of thumb), consider downgrading

**Thresholds (customize per outcome):**

| Outcome | MCID or Decision Threshold | OIS |
|---------|---------------------------|-----|
| {{OUTCOME_1}} | {{THRESHOLD}} | {{OIS}} |
| {{OUTCOME_2}} | {{THRESHOLD}} | {{OIS}} |

**Rating for this review:**

| Outcome | Total N | 95% CI | Crosses Threshold? | OIS Met? | Severity | Downgrade |
|---------|---------|--------|-------------------|----------|----------|-----------|
| {{OUTCOME_1}} | {{N}} | {{CI}} | Yes / No | Yes / No | Not serious / Serious / Very serious | 0 / -1 / -2 |
| {{OUTCOME_2}} | {{N}} | {{CI}} | Yes / No | Yes / No | Not serious / Serious / Very serious | 0 / -1 / -2 |

---

### 1.5 Publication Bias

**Assessment question:** Is the body of evidence likely affected by selective publication or reporting?

| Severity | Action | Criteria |
|----------|--------|----------|
| Undetected | No downgrade | Comprehensive search; funnel plot symmetric; no evidence of selective reporting |
| Suspected | Downgrade 1 level | Funnel plot asymmetry; Egger test significant; predominantly small positive studies; industry funding concerns |
| Strongly suspected | Downgrade 2 levels | Clear evidence of missing studies; registered protocols without published results |

**Decision rules:**
- Funnel plots require 10 or more studies to be informative
- Egger test p < 0.10 suggests asymmetry
- Check trial registries for registered but unpublished studies
- Consider whether commercial interest could drive selective reporting
- Small study effects (small studies showing larger effects) suggest publication bias
- If unable to assess (too few studies), note this but do not automatically downgrade

**Rating for this review:**

| Outcome | N Studies | Funnel Plot | Egger p | Registry Check | Severity | Downgrade |
|---------|----------|------------|---------|---------------|----------|-----------|
| {{OUTCOME_1}} | {{N}} | Symmetric / Asymmetric / N/A | {{P}} | {{RESULT}} | Undetected / Suspected | 0 / -1 |
| {{OUTCOME_2}} | {{N}} | Symmetric / Asymmetric / N/A | {{P}} | {{RESULT}} | Undetected / Suspected | 0 / -1 |

---

## 2. Upgrade Factors (Observational Studies Only)

These factors may upgrade certainty of evidence from observational studies. Apply only when no downgrade factors are present (or after accounting for downgrades).

### 2.1 Large Magnitude of Effect

| Magnitude | Action | Criteria |
|-----------|--------|----------|
| Large | Upgrade 1 level | RR > 2 or < 0.5 (consistent evidence from 2+ studies, no plausible confounders) |
| Very large | Upgrade 2 levels | RR > 5 or < 0.2 (direct evidence with no major threats to validity) |

**Decision rules:**
- Effect must be consistent across studies
- No plausible confounding that could fully explain the effect
- Based on unadjusted estimates (adjusted estimates may already account for confounding)

### 2.2 Dose-Response Gradient

| Presence | Action | Criteria |
|----------|--------|----------|
| Present | Upgrade 1 level | Clear dose-response relationship observed across or within studies |

**Decision rules:**
- The gradient should be biologically plausible
- Must be evident in the data, not assumed
- Consider whether a threshold effect might exist

### 2.3 Plausible Confounding Would Reduce Effect

| Situation | Action | Criteria |
|-----------|--------|----------|
| All plausible confounders would reduce the observed effect | Upgrade 1 level | If all residual confounding acts in the opposite direction, the true effect may be even larger |

**Decision rules:**
- List all plausible confounders and their expected direction of bias
- If all bias toward the null, this supports upgrading
- Rarely applied; requires strong understanding of confounding structure

**Rating for this review:**

| Outcome | Large Effect? | Dose-Response? | Confounding Direction? | Total Upgrade |
|---------|--------------|---------------|----------------------|---------------|
| {{OUTCOME_1}} | No / +1 / +2 | No / +1 | No / +1 | {{TOTAL}} |
| {{OUTCOME_2}} | No / +1 / +2 | No / +1 | No / +1 | {{TOTAL}} |

---

## 3. GRADE Evidence Profile Table

Complete one row per outcome.

| Outcome | N Studies (Design) | Risk of Bias | Inconsistency | Indirectness | Imprecision | Pub Bias | Upgrade | Certainty |
|---------|-------------------|-------------|---------------|-------------|------------|----------|---------|-----------|
| {{OUTCOME_1}} | {{N}} ({{DESIGN}}) | 0 / -1 / -2 | 0 / -1 / -2 | 0 / -1 / -2 | 0 / -1 / -2 | 0 / -1 | 0/+1/+2 | HIGH/MOD/LOW/VERY LOW |
| {{OUTCOME_2}} | | | | | | | | |
| {{OUTCOME_3}} | | | | | | | | |

---

## 4. Summary of Findings (SoF) Table

This is the primary output for readers. Present in the manuscript or as a supplementary table.

### Summary of Findings: {{INTERVENTION}} compared to {{COMPARATOR}} for {{CONDITION}}

| Outcome | Timeframe | N Studies (Participants) | Certainty (GRADE) | Relative Effect (95% CI) | Risk with Control | Risk Difference |
|---------|-----------|------------------------|-------------------|-------------------------|-------------------|-----------------|
| {{OUTCOME_1}} | {{TIME}} | {{N_STUDIES}} ({{N_PART}}) | {{GRADE_LEVEL}} | {{RR_OR_HR}} ({{CI}}) | {{BASELINE_RISK}} per 1,000 | {{RISK_DIFF}} per 1,000 ({{CI_DIFF}}) |
| {{OUTCOME_2}} | {{TIME}} | {{N_STUDIES}} ({{N_PART}}) | {{GRADE_LEVEL}} | -- | {{CONTROL_MEAN}} | MD {{MEAN_DIFF}} ({{CI_DIFF}}) |
| {{OUTCOME_3}} | {{TIME}} | {{N_STUDIES}} ({{N_PART}}) | {{GRADE_LEVEL}} | -- | -- | {{NARRATIVE_EFFECT}} |

**Footnotes:**
1. {{FOOTNOTE_EXPLAINING_DOWNGRADE_REASON}}
2. {{FOOTNOTE_EXPLAINING_DOWNGRADE_REASON}}

**Explanations:**
- Baseline risk sourced from: {{SOURCE}}
- GRADE Working Group grades: High = very confident; Moderate = moderately confident; Low = limited confidence; Very low = very little confidence.

---

## 5. GRADE Certainty Calculation Worksheet

Use this worksheet for each outcome to systematically calculate the final certainty rating.

### Outcome: {{OUTCOME_NAME}}

| Step | Item | Value |
|------|------|-------|
| **Starting level** | Study design | RCT = HIGH (4) / Observational = LOW (2) |
| **Downgrade 1** | Risk of bias | 0 / -1 / -2 |
| **Downgrade 2** | Inconsistency | 0 / -1 / -2 |
| **Downgrade 3** | Indirectness | 0 / -1 / -2 |
| **Downgrade 4** | Imprecision | 0 / -1 / -2 |
| **Downgrade 5** | Publication bias | 0 / -1 |
| **Upgrade 1** | Large effect | 0 / +1 / +2 |
| **Upgrade 2** | Dose-response | 0 / +1 |
| **Upgrade 3** | Plausible confounding | 0 / +1 |
| **Final score** | Sum | {{SCORE}} |
| **Final certainty** | 4=High, 3=Moderate, 2=Low, 1 or less=Very low | {{LEVEL}} |

**Justification narrative:**
> {{NARRATIVE_EXPLAINING_ALL_RATING_DECISIONS}}

---

## 6. Common Pitfalls

| Pitfall | Guidance |
|---------|----------|
| Double-counting RoB and inconsistency | If all studies are biased in the same direction, this affects RoB, not inconsistency |
| Downgrading for imprecision when effect is significant | Statistical significance alone does not mean the estimate is precise; check CI width against clinical thresholds |
| Not downgrading observational studies for RoB | Even though they start at LOW, further downgrade is appropriate if studies have serious limitations |
| Upgrading observational studies that have been downgraded | Upgrading is generally only applied when there are no serious downgrades |
| Using GRADE for individual studies | GRADE assesses a body of evidence for each outcome, not individual studies |
| Conflating certainty with recommendation strength | GRADE certainty is about evidence; recommendation strength also considers values, preferences, and resources |

---

## 7. Reporting GRADE in the Manuscript

### In Methods
> The certainty of evidence for each outcome was assessed using the GRADE approach. Evidence was classified as high, moderate, low, or very low based on five domains: risk of bias, inconsistency, indirectness, imprecision, and publication bias. For observational studies, upgrading was considered for large magnitude of effect, dose-response gradient, and plausible confounding reducing the effect. GRADE assessments were performed using [GRADEpro GDT / manual assessment] by two reviewers with disagreements resolved by discussion.

### In Results
> The certainty of evidence was [high/moderate/low/very low] for [outcome] (Table X), downgraded [one level/two levels] due to [specific reasons].

### In Discussion
> The [high/moderate/low/very low] certainty evidence for [outcome] means [interpretation from GRADE definitions]. This [supports/limits] confidence in [specific clinical recommendation or conclusion].

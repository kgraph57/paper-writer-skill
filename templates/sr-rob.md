# Risk of Bias Assessment Templates

> This file contains assessment templates for the four most commonly used RoB tools.
> Select the appropriate tool based on study design.
> All assessments must be performed independently by two reviewers.

---

## Tool Selection Guide

| Study Design | Recommended Tool | Reference |
|-------------|-----------------|-----------|
| Randomized controlled trials | Cochrane RoB 2 | Sterne et al., BMJ 2019;366:l4898 |
| Cohort studies | Newcastle-Ottawa Scale (NOS) | Wells et al. (Ottawa Hospital Research Institute) |
| Case-control studies | Newcastle-Ottawa Scale (NOS) | Wells et al. (Ottawa Hospital Research Institute) |
| Cross-sectional studies | JBI Critical Appraisal Checklist | Moola et al., JBI Manual 2020 |
| Diagnostic accuracy studies | QUADAS-2 | Whiting et al., Ann Intern Med 2011;155:529-536 |

---

## Two-Reviewer Independent Assessment Protocol

### Procedure

1. **Training:** Both reviewers complete tool-specific training before assessment.
2. **Calibration:** Independently assess 2-3 pilot studies and compare results.
3. **Independent assessment:** Each reviewer completes the form without discussion.
4. **Comparison:** After both reviewers finish, compare all judgments.
5. **Resolution:** Discuss disagreements; involve a third reviewer if consensus is not reached.
6. **Documentation:** Record the final judgment, supporting evidence, and resolution method.

### Agreement Reporting

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Percent agreement | (Agreements / Total domains) x 100 | >80% is acceptable |
| Cohen kappa | (Po - Pe) / (1 - Pe) | <0.40 poor; 0.41-0.60 moderate; 0.61-0.80 substantial; >0.80 almost perfect |

---

## 1. Cochrane Risk of Bias 2 (RoB 2) -- For Randomized Controlled Trials

### Study: {{AUTHOR}} ({{YEAR}})

**Assessed for outcome:** {{OUTCOME}}
**Reviewer 1:** {{REVIEWER_1}} | **Reviewer 2:** {{REVIEWER_2}} | **Date:** {{DATE}}

---

### Domain 1: Risk of Bias Arising from the Randomization Process

| # | Signaling Question | Response | Support |
|---|-------------------|----------|---------|
| 1.1 | Was the allocation sequence random? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 1.2 | Was the allocation sequence concealed until participants were enrolled and assigned to interventions? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 1.3 | Did baseline differences between intervention groups suggest a problem with the randomization process? | Y / PY / PN / N / NI | {{SUPPORT}} |

**Domain 1 judgment:** Low / Some concerns / High

**Rationale:** {{RATIONALE}}

---

### Domain 2: Risk of Bias Due to Deviations from the Intended Interventions

**(Effect of assignment to intervention -- intention-to-treat)**

| # | Signaling Question | Response | Support |
|---|-------------------|----------|---------|
| 2.1 | Were participants aware of their assigned intervention during the trial? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 2.2 | Were carers and people delivering the interventions aware of participants' assigned intervention during the trial? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 2.3 | If Y/PY to 2.1 or 2.2: Were there deviations from the intended intervention that arose because of the trial context? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 2.4 | If Y/PY to 2.3: Were these deviations likely to have affected the outcome? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 2.5 | If Y/PY to 2.4: Were these deviations from intended intervention balanced between groups? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 2.6 | Was an appropriate analysis used to estimate the effect of assignment to intervention? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 2.7 | If N/PN to 2.6: Was there potential for a substantial impact (on the result) of the failure to analyze participants in the group to which they were randomized? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |

**Domain 2 judgment:** Low / Some concerns / High

**Rationale:** {{RATIONALE}}

---

### Domain 3: Risk of Bias Due to Missing Outcome Data

| # | Signaling Question | Response | Support |
|---|-------------------|----------|---------|
| 3.1 | Were data for this outcome available for all, or nearly all, participants randomized? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 3.2 | If N/PN to 3.1: Is there evidence that the result was not biased by missing outcome data? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 3.3 | If N/PN to 3.2: Could missingness in the outcome depend on its true value? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 3.4 | If Y/PY to 3.3: Is it likely that missingness in the outcome depended on its true value? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |

**Domain 3 judgment:** Low / Some concerns / High

**Rationale:** {{RATIONALE}}

---

### Domain 4: Risk of Bias in Measurement of the Outcome

| # | Signaling Question | Response | Support |
|---|-------------------|----------|---------|
| 4.1 | Was the method of measuring the outcome inappropriate? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 4.2 | Could measurement or ascertainment of the outcome have differed between intervention groups? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 4.3 | If N/PN to 4.1 and 4.2: Were outcome assessors aware of the intervention received by study participants? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 4.4 | If Y/PY to 4.3: Could assessment of the outcome have been influenced by knowledge of intervention received? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |
| 4.5 | If Y/PY to 4.4: Is it likely that assessment of the outcome was influenced by knowledge of intervention received? | Y / PY / PN / N / NI / NA | {{SUPPORT}} |

**Domain 4 judgment:** Low / Some concerns / High

**Rationale:** {{RATIONALE}}

---

### Domain 5: Risk of Bias in Selection of the Reported Result

| # | Signaling Question | Response | Support |
|---|-------------------|----------|---------|
| 5.1 | Were the data that produced this result analyzed in accordance with a pre-specified analysis plan that was finalized before unblinded outcome data were available for analysis? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 5.2 | Is the numerical result being assessed likely to have been selected, on the basis of the results, from multiple eligible outcome measurements within the outcome domain? | Y / PY / PN / N / NI | {{SUPPORT}} |
| 5.3 | Is the numerical result being assessed likely to have been selected, on the basis of the results, from multiple eligible analyses of the data? | Y / PY / PN / N / NI | {{SUPPORT}} |

**Domain 5 judgment:** Low / Some concerns / High

**Rationale:** {{RATIONALE}}

---

### Overall RoB 2 Judgment

| Domain | Judgment |
|--------|----------|
| 1. Randomization process | Low / Some concerns / High |
| 2. Deviations from intended interventions | Low / Some concerns / High |
| 3. Missing outcome data | Low / Some concerns / High |
| 4. Measurement of the outcome | Low / Some concerns / High |
| 5. Selection of the reported result | Low / Some concerns / High |
| **Overall** | **Low / Some concerns / High** |

**Overall algorithm:**
- **Low risk:** All domains are low risk
- **Some concerns:** Some concerns in at least one domain, but no high risk in any domain
- **High risk:** High risk in at least one domain; OR some concerns in multiple domains in a way that substantially lowers confidence

**Response key:** Y = Yes, PY = Probably yes, PN = Probably no, N = No, NI = No information, NA = Not applicable

---

## 2. Newcastle-Ottawa Scale (NOS) -- For Cohort and Case-Control Studies

### 2A. NOS for Cohort Studies

**Study:** {{AUTHOR}} ({{YEAR}})
**Reviewer:** {{REVIEWER}} | **Date:** {{DATE}}

Maximum score: 9 stars. Thresholds: Good quality >= 7; Fair quality 5-6; Poor quality < 5.

#### Selection (max 4 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 1 | **Representativeness of the exposed cohort** | a) Truly representative of the average in the community [*] | |
| | | b) Somewhat representative of the average in the community [*] | |
| | | c) Selected group of users (e.g., nurses, volunteers) | |
| | | d) No description of the derivation of the cohort | |
| 2 | **Selection of the non-exposed cohort** | a) Drawn from the same community as the exposed cohort [*] | |
| | | b) Drawn from a different source | |
| | | c) No description of the derivation of the non-exposed cohort | |
| 3 | **Ascertainment of exposure** | a) Secure record (e.g., surgical records) [*] | |
| | | b) Structured interview [*] | |
| | | c) Written self-report | |
| | | d) No description | |
| 4 | **Demonstration that outcome of interest was not present at start of study** | a) Yes [*] | |
| | | b) No | |

**Selection stars:** {{N}} / 4

#### Comparability (max 2 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 5 | **Comparability of cohorts on the basis of the design or analysis** | a) Study controls for {{MOST_IMPORTANT_FACTOR}} [*] | |
| | | b) Study controls for any additional factor [*] | |

**Comparability stars:** {{N}} / 2

#### Outcome (max 3 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 6 | **Assessment of outcome** | a) Independent blind assessment [*] | |
| | | b) Record linkage [*] | |
| | | c) Self-report | |
| | | d) No description | |
| 7 | **Was follow-up long enough for outcomes to occur** | a) Yes (adequate follow-up period for outcome of interest) [*] | |
| | | b) No | |
| 8 | **Adequacy of follow-up of cohorts** | a) Complete follow-up (all subjects accounted for) [*] | |
| | | b) Subjects lost to follow-up unlikely to introduce bias (<=20% lost; or description provided of those lost) [*] | |
| | | c) Follow-up rate <80% and no description of those lost | |
| | | d) No statement | |

**Outcome stars:** {{N}} / 3

**Total NOS score:** {{TOTAL}} / 9 -- Quality: Good / Fair / Poor

---

### 2B. NOS for Case-Control Studies

**Study:** {{AUTHOR}} ({{YEAR}})
**Reviewer:** {{REVIEWER}} | **Date:** {{DATE}}

Maximum score: 9 stars. Thresholds: Good quality >= 7; Fair quality 5-6; Poor quality < 5.

#### Selection (max 4 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 1 | **Is the case definition adequate?** | a) Yes, with independent validation [*] | |
| | | b) Yes, e.g., record linkage or based on self-reports | |
| | | c) No description | |
| 2 | **Representativeness of the cases** | a) Consecutive or obviously representative series of cases [*] | |
| | | b) Potential for selection biases or not stated | |
| 3 | **Selection of controls** | a) Community controls [*] | |
| | | b) Hospital controls | |
| | | c) No description | |
| 4 | **Definition of controls** | a) No history of disease (endpoint) [*] | |
| | | b) No description of source | |

#### Comparability (max 2 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 5 | **Comparability of cases and controls on the basis of the design or analysis** | a) Study controls for {{MOST_IMPORTANT_FACTOR}} [*] | |
| | | b) Study controls for any additional factor [*] | |

#### Exposure (max 3 stars)

| # | Item | Options | Stars |
|---|------|---------|-------|
| 6 | **Ascertainment of exposure** | a) Secure record (e.g., surgical records) [*] | |
| | | b) Structured interview where blind to case/control status [*] | |
| | | c) Interview not blinded to case/control status | |
| | | d) Written self-report or medical record only | |
| | | e) No description | |
| 7 | **Same method of ascertainment for cases and controls** | a) Yes [*] | |
| | | b) No | |
| 8 | **Non-response rate** | a) Same rate for both groups [*] | |
| | | b) Non-respondents described | |
| | | c) Rate different and no designation | |

**Total NOS score:** {{TOTAL}} / 9 -- Quality: Good / Fair / Poor

---

## 3. JBI Critical Appraisal Checklist for Analytical Cross-Sectional Studies

**Study:** {{AUTHOR}} ({{YEAR}})
**Reviewer:** {{REVIEWER}} | **Date:** {{DATE}}

| # | Question | Yes | No | Unclear | N/A |
|---|----------|-----|----|---------|-----|
| 1 | Were the criteria for inclusion in the sample clearly defined? | | | | |
| 2 | Were the study subjects and the setting described in detail? | | | | |
| 3 | Was the exposure measured in a valid and reliable way? | | | | |
| 4 | Were objective, standard criteria used for measurement of the condition? | | | | |
| 5 | Were confounding factors identified? | | | | |
| 6 | Were strategies to deal with confounding factors stated? | | | | |
| 7 | Were the outcomes measured in a valid and reliable way? | | | | |
| 8 | Was appropriate statistical analysis used? | | | | |

**Overall appraisal:** Include / Exclude / Seek further info

**Scoring guidance:**
- **Low risk:** 6 or more "Yes" responses with no critical items as "No"
- **Moderate risk:** 4-5 "Yes" responses
- **High risk:** 3 or fewer "Yes" responses or critical items (Q3, Q4, Q7) as "No"

**Rationale:** {{RATIONALE}}

---

## 4. QUADAS-2 -- For Diagnostic Accuracy Studies

**Study:** {{AUTHOR}} ({{YEAR}})
**Index test:** {{INDEX_TEST}}
**Reference standard:** {{REFERENCE_STANDARD}}
**Target condition:** {{TARGET_CONDITION}}
**Reviewer:** {{REVIEWER}} | **Date:** {{DATE}}

---

### Domain 1: Patient Selection

**Signaling questions:**

| # | Question | Response | Support |
|---|----------|----------|---------|
| 1 | Was a consecutive or random sample of patients enrolled? | Y / N / Unclear | {{SUPPORT}} |
| 2 | Was a case-control design avoided? | Y / N / Unclear | {{SUPPORT}} |
| 3 | Did the study avoid inappropriate exclusions? | Y / N / Unclear | {{SUPPORT}} |

**Risk of bias:** Low / High / Unclear
**Concerns regarding applicability:** Low / High / Unclear

---

### Domain 2: Index Test

**Signaling questions:**

| # | Question | Response | Support |
|---|----------|----------|---------|
| 1 | Were the index test results interpreted without knowledge of the results of the reference standard? | Y / N / Unclear | {{SUPPORT}} |
| 2 | If a threshold was used, was it pre-specified? | Y / N / Unclear | {{SUPPORT}} |

**Risk of bias:** Low / High / Unclear
**Concerns regarding applicability:** Low / High / Unclear

---

### Domain 3: Reference Standard

**Signaling questions:**

| # | Question | Response | Support |
|---|----------|----------|---------|
| 1 | Is the reference standard likely to correctly classify the target condition? | Y / N / Unclear | {{SUPPORT}} |
| 2 | Were the reference standard results interpreted without knowledge of the results of the index test? | Y / N / Unclear | {{SUPPORT}} |

**Risk of bias:** Low / High / Unclear
**Concerns regarding applicability:** Low / High / Unclear

---

### Domain 4: Flow and Timing

**Signaling questions:**

| # | Question | Response | Support |
|---|----------|----------|---------|
| 1 | Was there an appropriate interval between index test and reference standard? | Y / N / Unclear | {{SUPPORT}} |
| 2 | Did all patients receive the same reference standard? | Y / N / Unclear | {{SUPPORT}} |
| 3 | Were all patients included in the analysis? | Y / N / Unclear | {{SUPPORT}} |

**Risk of bias:** Low / High / Unclear

---

### QUADAS-2 Summary

| Domain | Risk of Bias | Applicability Concerns |
|--------|-------------|----------------------|
| Patient selection | Low / High / Unclear | Low / High / Unclear |
| Index test | Low / High / Unclear | Low / High / Unclear |
| Reference standard | Low / High / Unclear | Low / High / Unclear |
| Flow and timing | Low / High / Unclear | -- |

---

## 5. Traffic Light Visualization Guide

### Creating Traffic Light Plots

Traffic light plots display per-study, per-domain risk of bias judgments using colored indicators.

**Color coding:**

| Color | RoB 2 / QUADAS-2 | NOS | JBI |
|-------|-------------------|-----|-----|
| Green | Low risk | Good quality (>= 7) | Low risk (>= 6 Yes) |
| Yellow | Some concerns / Unclear | Fair quality (5-6) | Moderate risk (4-5 Yes) |
| Red | High risk | Poor quality (< 5) | High risk (<= 3 Yes) |

### Recommended Software

| Tool | Type | URL |
|------|------|-----|
| robvis | R package | https://github.com/mcguinlu/robvis |
| Risk-of-bias VISualization (robvis) | Web app | https://www.riskofbias.info/welcome/robvis-visualization-tool |
| RevMan | Desktop | Cochrane RevMan |

### robvis R Code Example

```r
# Install
install.packages("robvis")
library(robvis)

# Prepare data (RoB 2 example)
# CSV with columns: Study, D1, D2, D3, D4, D5, Overall
# Values: "Low" / "Some concerns" / "High"

data <- read.csv("rob_data.csv")

# Traffic light plot
rob_traffic_light(data, tool = "ROB2")

# Summary bar plot
rob_summary(data, tool = "ROB2")

# Available tools: "ROB2", "ROBINS-I", "QUADAS-2", "ROB1"
```

### Figure Formatting for Publication

- Use high resolution (>= 300 DPI)
- Include a legend explaining the color coding
- Label all domains clearly
- Order studies alphabetically or by year
- Export as PDF or TIFF for journal submission
- Caption example: "Figure X. Risk of bias assessment of included randomized controlled trials using the Cochrane Risk of Bias 2 tool. Green (+) = low risk; Yellow (?) = some concerns; Red (-) = high risk."

---

## 6. Summary Tables Across All Included Studies

Use these aggregate tables to present RoB results across all included studies in the manuscript.

### For RoB 2 (RCTs)

| Study | D1: Randomization | D2: Deviations | D3: Missing Data | D4: Measurement | D5: Selection | Overall |
|-------|-------------------|----------------|-----------------|----------------|---------------|---------|
| {{STUDY_1}} | L / SC / H | L / SC / H | L / SC / H | L / SC / H | L / SC / H | L / SC / H |
| {{STUDY_2}} | | | | | | |
| {{STUDY_3}} | | | | | | |

L = Low risk, SC = Some concerns, H = High risk

### For NOS (Cohort/Case-Control)

| Study | Selection (/4) | Comparability (/2) | Outcome (/3) | Total (/9) | Quality |
|-------|---------------|-------------------|--------------|-----------|---------|
| {{STUDY_1}} | {{N}} | {{N}} | {{N}} | {{TOTAL}} | Good / Fair / Poor |
| {{STUDY_2}} | | | | | |
| {{STUDY_3}} | | | | | |

### For JBI (Cross-Sectional)

| Study | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Yes Count | Risk |
|-------|----|----|----|----|----|----|----|----|-----------|------|
| {{STUDY_1}} | Y/N/U | Y/N/U | Y/N/U | Y/N/U | Y/N/U | Y/N/U | Y/N/U | Y/N/U | {{N}}/8 | L/M/H |
| {{STUDY_2}} | | | | | | | | | | |

### For QUADAS-2 (Diagnostic Accuracy)

| Study | Patient Selection (RoB / App) | Index Test (RoB / App) | Reference Standard (RoB / App) | Flow and Timing (RoB) |
|-------|------------------------------|----------------------|-------------------------------|----------------------|
| {{STUDY_1}} | L/H/U / L/H/U | L/H/U / L/H/U | L/H/U / L/H/U | L/H/U |
| {{STUDY_2}} | | | | |

L = Low, H = High, U = Unclear, App = Applicability concerns

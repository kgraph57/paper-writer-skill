# Systematic Review Outline Template (PRISMA 2020)

> This template follows the PRISMA 2020 statement (Page et al., BMJ 2021;372:n71).
> Section numbers in brackets [P-XX] map to the PRISMA 2020 27-item checklist.

---

## TITLE [P-1]

<!-- Format: "[Intervention/Exposure] for/and [Outcome] in [Population]: A Systematic Review [and Meta-Analysis]" -->
<!-- Example: "Large Language Models for Patient Education Material Generation: A Systematic Review and Meta-Analysis" -->

{{TITLE}}

---

## ABSTRACT [P-2]

### Background
<!-- 1-2 sentences: Why this review matters -->
{{BACKGROUND_CONTEXT}}

### Objectives
<!-- 1 sentence: PICO/PECO framed question -->
{{REVIEW_QUESTION}}

### Methods
<!-- Data sources, eligibility criteria, study selection, synthesis method -->
We searched {{DATABASES}} from inception to {{SEARCH_DATE}}. We included {{STUDY_DESIGNS}} examining {{INTERVENTION_EXPOSURE}} in {{POPULATION}} reporting {{OUTCOMES}}. Two reviewers independently screened, extracted data, and assessed risk of bias. {{SYNTHESIS_METHOD}} was used for data synthesis.

### Results
<!-- Number screened, included; key findings with effect sizes and CIs -->
Of {{N_IDENTIFIED}} records identified, {{N_INCLUDED}} studies met inclusion criteria (N = {{TOTAL_PARTICIPANTS}}). {{KEY_FINDING_1}}. {{KEY_FINDING_2}}.

### Conclusions
{{MAIN_CONCLUSION}}

### Systematic review registration
{{PROSPERO_ID}}

---

## 1. INTRODUCTION [P-3, P-4]

### 1.1 Rationale [P-3]

<!-- Paragraph 1: Describe the health condition or topic -->
{{CONDITION_BACKGROUND}}

<!-- Paragraph 2: Describe what is known / current evidence -->
{{CURRENT_EVIDENCE}}

<!-- Paragraph 3: Describe the gap / why this review is needed -->
{{EVIDENCE_GAP}}

<!-- Paragraph 4: How this review will address the gap -->
{{HOW_REVIEW_ADDRESSES_GAP}}

### 1.2 Objectives [P-4]

<!-- State the review question using PICO/PECO framework -->

The objective of this systematic review is to {{OBJECTIVE_VERB}} the {{OUTCOME_CONCEPT}} of {{INTERVENTION_EXPOSURE}} {{COMPARED_TO}} in {{POPULATION}}.

Specifically, we aimed to:
1. {{OBJECTIVE_1}}
2. {{OBJECTIVE_2}}
3. {{OBJECTIVE_3}}

---

## 2. METHODS [P-5 through P-17]

### 2.1 Protocol and Registration [P-5, P-24a, P-24b]

This systematic review was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 guidelines. The protocol was registered prospectively with PROSPERO ({{PROSPERO_ID}}) and is available at {{PROTOCOL_URL}}.

<!-- Note any protocol amendments with dates and rationale -->
{{PROTOCOL_AMENDMENTS}}

### 2.2 Eligibility Criteria [P-6]

#### Population
{{POPULATION_CRITERIA}}

#### Intervention / Exposure
{{INTERVENTION_CRITERIA}}

#### Comparator
{{COMPARATOR_CRITERIA}}

#### Outcomes
- **Primary outcome(s):** {{PRIMARY_OUTCOMES}}
- **Secondary outcome(s):** {{SECONDARY_OUTCOMES}}

#### Study Design
{{ELIGIBLE_STUDY_DESIGNS}}

#### Exclusion Criteria
- {{EXCLUSION_1}}
- {{EXCLUSION_2}}
- {{EXCLUSION_3}}

#### Other Limits
- **Language:** {{LANGUAGE_RESTRICTION}}
- **Date range:** {{DATE_RESTRICTION}}
- **Publication type:** {{PUBLICATION_TYPE_RESTRICTION}}

### 2.3 Information Sources [P-7]

We searched the following electronic databases from {{START_DATE}} to {{END_DATE}}:

| Database | Platform | Date Searched |
|----------|----------|---------------|
| MEDLINE | PubMed | {{DATE}} |
| Embase | Elsevier | {{DATE}} |
| Cochrane CENTRAL | Cochrane Library | {{DATE}} |
| {{OTHER_DB}} | {{PLATFORM}} | {{DATE}} |

Additional sources:
- Reference lists of included studies and relevant reviews
- {{GREY_LITERATURE_SOURCES}}
- {{TRIAL_REGISTRIES}}
- Contact with study authors (if applicable)

### 2.4 Search Strategy [P-8]

The search strategy was developed in consultation with a medical librarian. Key concepts were combined using Boolean operators. The full search strategy for all databases is provided in Supplementary Appendix {{X}}.

**Example PubMed strategy:**

```
({{CONCEPT_1_TERMS}}) AND ({{CONCEPT_2_TERMS}}) AND ({{CONCEPT_3_TERMS}})
```

### 2.5 Selection Process [P-9]

Retrieved records were imported into {{REFERENCE_MANAGER}} and deduplicated. Screening was performed using {{SCREENING_TOOL}}.

**Title and abstract screening:** Two reviewers ({{REVIEWER_1}}, {{REVIEWER_2}}) independently screened all titles and abstracts against the eligibility criteria. A calibration exercise was conducted on the first {{N}} records.

**Full-text screening:** The same two reviewers independently assessed full-text articles for eligibility. Reasons for exclusion were documented.

**Conflict resolution:** Disagreements were resolved by discussion or consultation with a third reviewer ({{REVIEWER_3}}).

**Inter-rater reliability:** Agreement was assessed using Cohen's kappa (κ).

### 2.6 Data Collection Process [P-10]

Data were extracted independently by two reviewers using a standardized, pilot-tested data extraction form (Supplementary Appendix {{X}}). Discrepancies were resolved by discussion. Study authors were contacted for missing or unclear data when necessary.

### 2.7 Data Items [P-11]

The following data were extracted from each included study:

- **Study characteristics:** Author, year, country, study design, setting, funding
- **Population:** Sample size, age, sex, clinical characteristics, inclusion/exclusion criteria
- **Intervention/Exposure:** Type, duration, frequency, dose, delivery method
- **Comparator:** Type, details
- **Outcomes:** Definition, measurement tool, time points, effect measures
- **Results:** Point estimates, measures of variability, sample sizes per group

<!-- For time-to-event data: hazard ratios, survival curves -->
<!-- For diagnostic accuracy: 2x2 tables, sensitivity, specificity -->

### 2.8 Study Risk of Bias Assessment [P-12]

Risk of bias was assessed independently by two reviewers using:

| Study Design | Assessment Tool |
|-------------|----------------|
| Randomized controlled trials | Cochrane RoB 2 |
| Non-randomized studies of interventions | ROBINS-I |
| Cohort / case-control studies | Newcastle-Ottawa Scale |
| Cross-sectional studies | JBI Critical Appraisal Checklist |
| Diagnostic accuracy studies | QUADAS-2 |

{{TOOL_JUSTIFICATION}}

### 2.9 Effect Measures [P-13]

<!-- Select and describe the appropriate effect measures -->

| Outcome Type | Effect Measure |
|-------------|---------------|
| Dichotomous | Risk ratio (RR) / Odds ratio (OR) with 95% CI |
| Continuous | Mean difference (MD) / Standardized mean difference (SMD) with 95% CI |
| Time-to-event | Hazard ratio (HR) with 95% CI |
| Diagnostic accuracy | Sensitivity, specificity, AUC |

### 2.10 Synthesis Methods [P-14]

#### 2.10.1 Narrative Synthesis

Studies were grouped by {{GROUPING_VARIABLE}} and findings summarized descriptively, including direction and magnitude of effects.

#### 2.10.2 Meta-Analysis (if applicable)

<!-- Include this section ONLY if quantitative pooling was performed -->

Meta-analysis was performed when ≥{{MINIMUM_STUDIES}} studies reported the same outcome with sufficient clinical and methodological homogeneity.

- **Model:** {{RANDOM_OR_FIXED}}-effects model ({{JUSTIFICATION}})
- **Method:** {{INVERSE_VARIANCE / MANTEL_HAENSZEL / DERSIMONIAN_LAIRD}}
- **Heterogeneity:** Assessed using Cochran's Q test (p < 0.10) and I² statistic
  - Low: I² < 25%
  - Moderate: I² = 25-75%
  - High: I² > 75%
- **Software:** {{SOFTWARE}} (version {{VERSION}})

#### 2.10.3 Subgroup and Sensitivity Analyses [P-15, P-16]

**Pre-specified subgroup analyses:**
1. {{SUBGROUP_1}}
2. {{SUBGROUP_2}}
3. {{SUBGROUP_3}}

**Sensitivity analyses:**
1. Excluding high risk of bias studies
2. {{SENSITIVITY_2}}
3. {{SENSITIVITY_3}}

### 2.11 Reporting Bias Assessment [P-17]

<!-- For meta-analyses with ≥10 studies -->
Publication bias was assessed visually using funnel plots and statistically using {{EGGER_TEST / BEGG_TEST}}.

### 2.12 Certainty of Evidence [P-18]

The certainty of evidence for each outcome was assessed using the Grading of Recommendations Assessment, Development and Evaluation (GRADE) approach. Evidence was rated as high, moderate, low, or very low based on risk of bias, inconsistency, indirectness, imprecision, and publication bias.

---

## 3. RESULTS [P-19 through P-23]

### 3.1 Study Selection [P-19]

<!-- Include PRISMA 2020 flow diagram (Figure 1) -->

The search identified {{N_TOTAL}} records. After removing {{N_DUPLICATES}} duplicates, {{N_SCREENED}} records were screened by title and abstract. Of {{N_FULLTEXT}} full-text articles assessed, {{N_INCLUDED}} studies met all inclusion criteria.

The most common reasons for exclusion at full-text stage were:
1. {{REASON_1}} (n = {{N}})
2. {{REASON_2}} (n = {{N}})
3. {{REASON_3}} (n = {{N}})

**[INSERT PRISMA 2020 FLOW DIAGRAM HERE]**

### 3.2 Study Characteristics [P-20]

<!-- Table 1: Characteristics of Included Studies -->
The {{N_INCLUDED}} included studies were published between {{YEAR_RANGE}}. Studies were conducted in {{COUNTRIES}}. {{N_RCT}} were randomized controlled trials, {{N_COHORT}} were cohort studies, and {{N_OTHER}} were {{OTHER_DESIGNS}}.

Total participants: {{TOTAL_N}} (range: {{MIN_N}} to {{MAX_N}} per study).

| Study | Year | Country | Design | N | Population | Intervention | Comparator | Outcomes | Follow-up |
|-------|------|---------|--------|---|------------|-------------|------------|----------|-----------|
| {{AUTHOR}} | {{YEAR}} | {{COUNTRY}} | {{DESIGN}} | {{N}} | {{POP}} | {{INT}} | {{COMP}} | {{OUT}} | {{FU}} |

### 3.3 Risk of Bias in Studies [P-21]

<!-- Figure 2: Risk of bias summary -->
<!-- Figure 3: Risk of bias graph (traffic light plot) -->

{{ROB_NARRATIVE_SUMMARY}}

Overall, {{N}} studies were rated as low risk, {{N}} as some concerns, and {{N}} as high risk of bias. The most common sources of bias were {{COMMON_BIAS_SOURCES}}.

### 3.4 Results of Individual Studies [P-22]

#### 3.4.1 Primary Outcome: {{PRIMARY_OUTCOME_NAME}}

{{PRIMARY_OUTCOME_NARRATIVE}}

<!-- Forest plot if meta-analysis performed (Figure X) -->

#### 3.4.2 Secondary Outcomes

**{{SECONDARY_OUTCOME_1}}:**
{{SECONDARY_1_NARRATIVE}}

**{{SECONDARY_OUTCOME_2}}:**
{{SECONDARY_2_NARRATIVE}}

### 3.5 Results of Syntheses [P-22]

<!-- If meta-analysis was performed -->

**Pooled effect estimate:** {{EFFECT_MEASURE}} = {{ESTIMATE}} (95% CI: {{LOWER}} to {{UPPER}}; p = {{P_VALUE}})

**Heterogeneity:** I² = {{I2}}%, Q = {{Q}}, p = {{Q_P_VALUE}}

**Prediction interval:** {{LOWER_PI}} to {{UPPER_PI}}

### 3.6 Reporting Biases [P-23a]

{{PUBLICATION_BIAS_RESULTS}}

### 3.7 Certainty of Evidence [P-23b]

<!-- GRADE Summary of Findings Table -->

| Outcome | N Studies (N Participants) | Effect (95% CI) | Certainty | Interpretation |
|---------|--------------------------|------------------|-----------|----------------|
| {{OUTCOME}} | {{N}} ({{PARTICIPANTS}}) | {{EFFECT}} | {{GRADE}} | {{INTERPRETATION}} |

---

## 4. DISCUSSION [P-25, P-26, P-27]

### 4.1 Summary of Evidence [P-25]

<!-- Summarize main findings in context of the review question -->
This systematic review identified {{N}} studies examining {{TOPIC}}. The main findings were:
1. {{FINDING_1}}
2. {{FINDING_2}}
3. {{FINDING_3}}

### 4.2 Comparison with Previous Reviews

{{COMPARISON_WITH_EXISTING_REVIEWS}}

### 4.3 Strengths

- {{STRENGTH_1}}
- {{STRENGTH_2}}
- {{STRENGTH_3}}

### 4.4 Limitations [P-26]

#### Limitations of the Evidence
- {{EVIDENCE_LIMITATION_1}}
- {{EVIDENCE_LIMITATION_2}}

#### Limitations of the Review Process
- {{REVIEW_LIMITATION_1}}
- {{REVIEW_LIMITATION_2}}

### 4.5 Implications [P-27]

#### For Clinical Practice
{{CLINICAL_IMPLICATIONS}}

#### For Research
{{RESEARCH_IMPLICATIONS}}

---

## 5. CONCLUSIONS

<!-- 1-2 paragraphs: General interpretation of results with reference to certainty of evidence -->
{{CONCLUSIONS}}

---

## DECLARATIONS

### Funding
{{FUNDING_SOURCE}}

### Conflicts of Interest
{{COI_STATEMENT}}

### Data Availability
{{DATA_AVAILABILITY}}

### Author Contributions
<!-- Use CRediT taxonomy -->
{{AUTHOR_CONTRIBUTIONS}}

### Acknowledgments
{{ACKNOWLEDGMENTS}}

---

## REFERENCES

<!-- Use reference manager; journal-specific style -->

---

## SUPPLEMENTARY MATERIALS

- **Appendix 1:** Full search strategies for all databases
- **Appendix 2:** List of excluded studies with reasons
- **Appendix 3:** Data extraction form
- **Appendix 4:** Risk of bias detailed assessments
- **Appendix 5:** GRADE evidence profiles
- **Appendix 6:** Funnel plots (if applicable)
- **Appendix 7:** PRISMA 2020 checklist (completed)

---

## PRISMA 2020 Checklist Quick Reference

| # | Item | Section |
|---|------|---------|
| 1 | Title | Title |
| 2 | Abstract | Abstract |
| 3 | Rationale | Introduction 1.1 |
| 4 | Objectives | Introduction 1.2 |
| 5 | Eligibility criteria | Methods 2.2 |
| 6 | Information sources | Methods 2.3 |
| 7 | Search strategy | Methods 2.4 |
| 8 | Selection process | Methods 2.5 |
| 9 | Data collection process | Methods 2.6 |
| 10 | Data items | Methods 2.7 |
| 11 | Study risk of bias assessment | Methods 2.8 |
| 12 | Effect measures | Methods 2.9 |
| 13 | Synthesis methods | Methods 2.10 |
| 14 | Reporting bias assessment | Methods 2.11 |
| 15 | Certainty assessment | Methods 2.12 |
| 16 | Study selection | Results 3.1 |
| 17 | Study characteristics | Results 3.2 |
| 18 | Risk of bias in studies | Results 3.3 |
| 19 | Results of individual studies | Results 3.4 |
| 20 | Results of syntheses | Results 3.5 |
| 21 | Reporting biases | Results 3.6 |
| 22 | Certainty of evidence | Results 3.7 |
| 23 | Discussion - Summary | Discussion 4.1 |
| 24 | Discussion - Limitations | Discussion 4.4 |
| 25 | Discussion - Implications | Discussion 4.5 |
| 26 | Registration and protocol | Methods 2.1 |
| 27 | Support / COI | Declarations |

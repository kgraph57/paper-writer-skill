# Systematic Review Data Extraction Form

> Standardized form for extracting data from included studies.
> Pilot-test on the first 3-5 studies before full extraction.
> Two reviewers extract independently; resolve discrepancies by discussion or third reviewer.

---

## Instructions

1. **Before extraction:** Read the full text of the study carefully.
2. **Complete all fields.** Use "NR" (not reported) if information is unavailable. Use "N/A" if a field does not apply.
3. **Record page numbers** for each extracted data point to facilitate verification.
4. **Contact authors** if critical data are missing (document attempts).
5. **Discrepancies:** After independent extraction, compare forms and resolve disagreements. Document the resolution method.
6. **Save separate forms** for each study (one form = one study).

---

## A. Administrative Information

| Field | Entry |
|-------|-------|
| **Extraction ID** | {{EXTRACTION_ID}} |
| **Reviewer name** | {{REVIEWER_NAME}} |
| **Extraction date** | {{DATE}} |
| **Verification reviewer** | {{VERIFIER_NAME}} |
| **Verification date** | {{VERIFICATION_DATE}} |
| **Discrepancies resolved?** | Yes / No / N/A |
| **Resolution method** | Discussion / Third reviewer / Author contact |

---

## B. Study Identification

| Field | Entry | Page |
|-------|-------|------|
| **First author** | {{AUTHOR}} | — |
| **Publication year** | {{YEAR}} | — |
| **Title** | {{TITLE}} | — |
| **Journal** | {{JOURNAL}} | — |
| **Volume / Issue / Pages** | {{VOL_ISSUE_PAGES}} | — |
| **DOI** | {{DOI}} | — |
| **PMID** | {{PMID}} | — |
| **Country of corresponding author** | {{COUNTRY}} | — |
| **Language** | {{LANGUAGE}} | — |
| **Funding source** | {{FUNDING}} | p. |
| **Conflicts of interest declared** | Yes / No / NR | p. |

---

## C. Study Characteristics

| Field | Entry | Page |
|-------|-------|------|
| **Study design** | RCT / Cohort (prospective/retrospective) / Case-control / Cross-sectional / Before-after / Other: ___ | p. |
| **If RCT: randomization method** | {{RANDOMIZATION}} | p. |
| **If RCT: allocation concealment** | Adequate / Inadequate / Unclear / NR | p. |
| **If RCT: blinding** | Participants / Outcome assessors / Both / None / NR | p. |
| **Single-center or multi-center** | Single / Multi (n = ___) | p. |
| **Country/countries of study conduct** | {{COUNTRIES}} | p. |
| **Setting** | Hospital / Primary care / Community / Online / Other: ___ | p. |
| **Study period** | {{START}} to {{END}} | p. |
| **Recruitment period** | {{RECRUITMENT_PERIOD}} | p. |
| **Follow-up duration** | {{FOLLOW_UP}} | p. |
| **Registration number** | {{TRIAL_REG}} | p. |
| **Protocol published** | Yes (ref: ___) / No / NR | p. |

---

## D. Participant Characteristics

| Field | Entry | Page |
|-------|-------|------|
| **Inclusion criteria** | {{INCLUSION}} | p. |
| **Exclusion criteria** | {{EXCLUSION}} | p. |
| **Total enrolled** | n = {{N_ENROLLED}} | p. |
| **Total analyzed** | n = {{N_ANALYZED}} | p. |
| **Attrition / loss to follow-up** | n = {{N_LOST}} ({{PERCENT}}%) | p. |
| **Age (mean ± SD or median [IQR])** | {{AGE}} | p. |
| **Sex (% female)** | {{SEX}} | p. |
| **Race/Ethnicity** | {{RACE_ETHNICITY}} | p. |
| **Disease/condition** | {{CONDITION}} | p. |
| **Severity/stage** | {{SEVERITY}} | p. |
| **Comorbidities** | {{COMORBIDITIES}} | p. |
| **Baseline characteristics balanced?** | Yes / No / Unclear | p. |

### Group-Level Detail

| Characteristic | Intervention Group (n = ) | Control Group (n = ) | p-value |
|---------------|--------------------------|---------------------|---------|
| Age | | | |
| Sex (% female) | | | |
| {{CHARACTERISTIC_1}} | | | |
| {{CHARACTERISTIC_2}} | | | |
| {{CHARACTERISTIC_3}} | | | |

---

## E. Intervention / Exposure

| Field | Entry | Page |
|-------|-------|------|
| **Intervention name** | {{INTERVENTION}} | p. |
| **Intervention description** | {{DESCRIPTION}} | p. |
| **Dose / intensity** | {{DOSE}} | p. |
| **Frequency** | {{FREQUENCY}} | p. |
| **Duration** | {{DURATION}} | p. |
| **Mode of delivery** | {{DELIVERY_MODE}} | p. |
| **Provider / administrator** | {{PROVIDER}} | p. |
| **Fidelity assessment** | Yes / No / NR | p. |
| **Co-interventions** | {{CO_INTERVENTIONS}} | p. |

---

## F. Comparator / Control

| Field | Entry | Page |
|-------|-------|------|
| **Comparator type** | Placebo / Active control / Standard care / No intervention / Other: ___ | p. |
| **Comparator description** | {{COMPARATOR_DESC}} | p. |
| **Dose / intensity** | {{COMP_DOSE}} | p. |
| **Duration** | {{COMP_DURATION}} | p. |

---

## G. Outcome Measures

### G1. Primary Outcome

| Field | Entry | Page |
|-------|-------|------|
| **Outcome name** | {{PRIMARY_OUTCOME}} | p. |
| **Definition** | {{DEFINITION}} | p. |
| **Measurement tool/method** | {{TOOL}} | p. |
| **Tool validity reported** | Yes / No | p. |
| **Unit of measurement** | {{UNIT}} | p. |
| **Time point(s)** | {{TIME_POINTS}} | p. |
| **Outcome assessor** | Self-report / Clinician / Blinded assessor / Other: ___ | p. |

### G2. Secondary Outcomes

| # | Outcome Name | Measurement Tool | Time Point | Page |
|---|-------------|-----------------|------------|------|
| 1 | {{OUTCOME_1}} | {{TOOL_1}} | {{TIME_1}} | p. |
| 2 | {{OUTCOME_2}} | {{TOOL_2}} | {{TIME_2}} | p. |
| 3 | {{OUTCOME_3}} | {{TOOL_3}} | {{TIME_3}} | p. |
| 4 | {{OUTCOME_4}} | {{TOOL_4}} | {{TIME_4}} | p. |

### G3. Adverse Events / Harms

| Field | Entry | Page |
|-------|-------|------|
| **Adverse events reported** | Yes / No | p. |
| **Serious adverse events** | {{SAE}} | p. |
| **Withdrawals due to AE** | n = {{N_AE_WITHDRAWAL}} | p. |
| **Details** | {{AE_DETAILS}} | p. |

---

## H. Results

### H1. Dichotomous Outcomes

| Outcome | Intervention (events/total) | Control (events/total) | Effect Measure | Estimate (95% CI) | p-value | Page |
|---------|---------------------------|----------------------|----------------|-------------------|---------|------|
| {{OUTCOME}} | {{E1}}/{{N1}} | {{E2}}/{{N2}} | RR / OR / HR | {{ESTIMATE}} ({{CI}}) | {{P}} | p. |

### H2. Continuous Outcomes

| Outcome | Intervention (mean ± SD, n) | Control (mean ± SD, n) | Effect Measure | Estimate (95% CI) | p-value | Page |
|---------|---------------------------|----------------------|----------------|-------------------|---------|------|
| {{OUTCOME}} | {{MEAN1}} ± {{SD1}}, n={{N1}} | {{MEAN2}} ± {{SD2}}, n={{N2}} | MD / SMD | {{ESTIMATE}} ({{CI}}) | {{P}} | p. |

### H3. Time-to-Event Outcomes

| Outcome | Intervention (median, events/total) | Control (median, events/total) | HR (95% CI) | p-value | Page |
|---------|-----------------------------------|-------------------------------|-------------|---------|------|
| {{OUTCOME}} | {{MED1}}, {{E1}}/{{N1}} | {{MED2}}, {{E2}}/{{N2}} | {{HR}} ({{CI}}) | {{P}} | p. |

### H4. Subgroup/Sensitivity Analyses Reported by Authors

| Analysis | Subgroup | Effect (95% CI) | Interaction p-value | Page |
|----------|----------|-----------------|---------------------|------|
| {{ANALYSIS}} | {{SUBGROUP}} | {{EFFECT}} | {{P_INTERACTION}} | p. |

### H5. Adjusted vs. Unadjusted Estimates

| Outcome | Unadjusted Estimate (95% CI) | Adjusted Estimate (95% CI) | Variables Adjusted | Page |
|---------|------------------------------|---------------------------|-------------------|------|
| {{OUTCOME}} | {{UNADJ}} | {{ADJ}} | {{VARIABLES}} | p. |

---

## I. Risk of Bias Rating

| Domain | Rating | Support for Judgment | Page |
|--------|--------|---------------------|------|
| {{DOMAIN_1}} | Low / Some concerns / High | {{JUSTIFICATION}} | p. |
| {{DOMAIN_2}} | Low / Some concerns / High | {{JUSTIFICATION}} | p. |
| {{DOMAIN_3}} | Low / Some concerns / High | {{JUSTIFICATION}} | p. |
| {{DOMAIN_4}} | Low / Some concerns / High | {{JUSTIFICATION}} | p. |
| {{DOMAIN_5}} | Low / Some concerns / High | {{JUSTIFICATION}} | p. |
| **Overall** | Low / Some concerns / High | {{OVERALL_JUSTIFICATION}} | — |

> Refer to sr-rob.md for tool-specific domains and signaling questions.

---

## J. Notes

| Item | Notes |
|------|-------|
| **Data conversion needed** | {{CONVERSION_NOTES}} |
| **Author contact required** | {{CONTACT_NOTES}} |
| **Multiple publications** | {{LINKED_REFS}} |
| **Potential overlap with other included studies** | {{OVERLAP_NOTES}} |
| **Other notes** | {{OTHER_NOTES}} |

---

## Data Conversion Reference

Use these formulas when raw data need transformation:

| Situation | Formula |
|-----------|---------|
| SE to SD | SD = SE x sqrt(n) |
| 95% CI to SE | SE = (upper - lower) / 3.92 |
| Median + IQR to mean + SD | Mean ≈ (Q1 + median + Q3) / 3; SD ≈ (Q3 - Q1) / 1.35 |
| Median + range to mean + SD | Mean ≈ (low + 2×median + high) / 4; SD ≈ range / 4 |
| OR to RR | RR = OR / (1 - P0 + P0 × OR), where P0 = baseline risk |
| % to proportion | p = % / 100 |
| Change score SD (unknown) | SD_change = sqrt(SD_pre² + SD_post² - 2×r×SD_pre×SD_post), assume r = 0.5 |

---

## Checklist Before Finalizing

- [ ] All fields completed or marked NR/N/A
- [ ] Page numbers recorded for all extracted data
- [ ] Effect sizes and CIs correctly transcribed
- [ ] Numerators and denominators double-checked
- [ ] Risk of bias domains all rated with justifications
- [ ] Second reviewer has independently completed their form
- [ ] Discrepancies identified and resolved
- [ ] Data conversions documented with formulas used

# Statistical Reporting Guide (Extended SAMPL)

> Based on SAMPL (Statistical Analyses and Methods in the Published Literature) guidelines. Covers reporting requirements for common statistical methods in medical research.

---

## General Principles

### Every Statistical Result Must Include

1. **The test used** (name of statistical test)
2. **Sample size** (N for each group)
3. **Effect size** (difference, ratio, correlation coefficient)
4. **Measure of precision** (95% CI preferred over P value alone)
5. **Exact P value** (P = 0.032, not P < 0.05; exception: P < 0.001)

### Reporting Numbers

| Type | Format | Example |
|------|--------|---------|
| Percentages | 1 decimal place | 45.3% |
| Means | Appropriate to measurement precision | 5.7 kg |
| Standard deviation | Same decimal places as mean | 5.7 ± 2.3 kg |
| P values | 2-3 significant figures | P = 0.034 |
| P values < 0.001 | State as P < 0.001 | P < 0.001 |
| Confidence intervals | Same precision as estimate | 95% CI, 1.2 to 3.4 |
| Odds/hazard ratios | 2 decimal places | OR 2.34 (95% CI, 1.15 to 4.76) |

---

## By Study Design

### Randomized Controlled Trials

**Required in Methods:**
- Primary and secondary outcomes defined a priori
- Sample size calculation (alpha, power, expected effect, method)
- Randomization method (block, stratified, computer-generated)
- Allocation concealment method
- Blinding details
- ITT vs per-protocol analysis plan
- Handling of missing data
- Interim analyses and stopping rules (if any)
- Statistical software and version

**Required in Results:**
- CONSORT flow diagram (screened → randomized → analyzed)
- Baseline characteristics table (Table 1) — NO P values for baseline
- Primary outcome with effect size and 95% CI
- Number needed to treat (NNT) for binary outcomes
- Both ITT and per-protocol results (if different)
- Subgroup analyses labeled as exploratory

**Example:**
```
The primary outcome (30-day mortality) occurred in 45 of 200 patients (22.5%)
in the intervention group and 68 of 198 patients (34.3%) in the control group
(absolute risk reduction, 11.8 percentage points; 95% CI, 3.2 to 20.4;
P = 0.007; NNT = 9).
```

### Observational Studies (Cohort, Case-Control, Cross-Sectional)

**Required in Methods:**
- Exposure and outcome definitions
- Confounders identified and adjustment method
- Missing data handling
- Sensitivity analyses planned

**Required in Results:**
- Unadjusted AND adjusted estimates
- Confounders adjusted for (list them)
- For cohort: incidence rates, hazard ratios, relative risks
- For case-control: odds ratios
- For cross-sectional: prevalence ratios or odds ratios

**Example (Cohort):**
```
After adjustment for age, sex, BMI, and smoking status, patients with
diabetes had a higher risk of cardiovascular events (adjusted HR, 1.85;
95% CI, 1.32 to 2.59; P < 0.001) compared with non-diabetic patients.
```

### Diagnostic Accuracy Studies

**Required:**
- Sensitivity with 95% CI
- Specificity with 95% CI
- Positive and negative predictive values
- Positive and negative likelihood ratios
- AUC (area under ROC curve) with 95% CI
- 2×2 table (TP, FP, FN, TN)

**Example:**
```
The biomarker had a sensitivity of 85.2% (95% CI, 78.1% to 90.6%) and
specificity of 72.4% (95% CI, 64.8% to 79.2%) for detecting the disease.
The AUC was 0.86 (95% CI, 0.81 to 0.91).
```

---

## Common Statistical Methods — How to Report

### t-Test
```
Mean systolic BP was higher in the treatment group than in the control group
(142.3 ± 18.5 mm Hg vs 135.7 ± 16.2 mm Hg; mean difference, 6.6 mm Hg;
95% CI, 2.1 to 11.1; P = 0.004, unpaired t-test).
```

### Chi-Square Test
```
The proportion of adverse events was higher in group A than group B
(35/100 [35.0%] vs 20/100 [20.0%]; χ² = 5.7; P = 0.017).
```

### Mann-Whitney U Test
```
Median length of stay was shorter in the intervention group
(5 days [IQR, 3-8] vs 7 days [IQR, 4-12]; P = 0.003, Mann-Whitney U test).
```

### Logistic Regression
```
In multivariable logistic regression adjusted for age, sex, and BMI,
hypertension was independently associated with the outcome
(adjusted OR, 2.14; 95% CI, 1.32 to 3.47; P = 0.002).
```

### Cox Proportional Hazards
```
In multivariable Cox regression, the intervention was associated with
lower mortality (adjusted HR, 0.65; 95% CI, 0.48 to 0.88; P = 0.005).
The proportional hazards assumption was verified using Schoenfeld residuals.
```

### Kaplan-Meier
```
The 5-year overall survival rate was 72.3% (95% CI, 65.1% to 78.5%) in the
intervention group and 58.1% (95% CI, 50.4% to 65.0%) in the control group
(log-rank P = 0.003).
```

### Linear Mixed Models
```
Using a linear mixed model with random intercepts for patients, the
intervention group showed a greater decrease in HbA1c over 12 months
(between-group difference, -0.5%; 95% CI, -0.8% to -0.2%; P = 0.001).
```

### Meta-Analysis
```
The pooled risk ratio was 0.75 (95% CI, 0.62 to 0.91; P = 0.003;
I² = 42%; 8 studies, N = 3,245). A random-effects model (DerSimonian-Laird)
was used due to moderate heterogeneity.
```

---

## Sample Size Calculation

### How to Report

```
METHODS — Sample Size

A sample size of 200 per group was calculated to detect a 10 percentage-point
difference in the primary outcome (50% vs 40%) with 80% power at a two-sided
significance level of 0.05 (chi-square test). Allowing for 15% dropout,
the target enrollment was 236 per group.
```

### Required Elements
1. Expected effect size (and basis for the estimate)
2. Alpha level (usually 0.05)
3. Power (usually 80% or 90%)
4. Statistical test assumed
5. Dropout allowance
6. Software used for calculation (optional but good practice)

---

## Missing Data

### How to Report

```
METHODS — Missing Data

Missing data were present for BMI (5.2%), smoking status (3.1%), and
income (12.4%). We used multiple imputation (m = 20 datasets) assuming
data were missing at random (MAR). Results from complete-case analysis
were similar (Supplementary Table S3).
```

### Methods to Report

| Method | When to Use | How to Report |
|--------|------------|---------------|
| Complete-case analysis | <5% missing, MCAR | "Complete-case analysis was used (N missing = X)" |
| Multiple imputation | 5-40% missing, MAR | "Multiple imputation (m=20) under MAR assumption" |
| Last observation carried forward | Avoid — outdated | Not recommended by current guidelines |
| Sensitivity analysis | Always | "Sensitivity analyses assuming MNAR were performed" |

---

## Multiple Comparisons

### When to Adjust
- Pre-specified secondary outcomes: adjustment recommended
- Post-hoc/exploratory analyses: label as exploratory, interpret with caution
- Subgroup analyses: usually no formal adjustment, but state as hypothesis-generating

### Common Methods

| Method | Use Case |
|--------|----------|
| Bonferroni | Conservative; few comparisons |
| Holm | Less conservative than Bonferroni |
| Benjamini-Hochberg (FDR) | Many comparisons (genomics, proteomics) |
| Tukey HSD | ANOVA post-hoc pairwise |
| No adjustment | If analyses are pre-specified and limited |

### How to Report
```
To account for multiple comparisons across 3 secondary outcomes,
a Bonferroni-corrected significance threshold of P < 0.017 was used.
```

---

## Table 1: Baseline Characteristics

### Format Rules

1. **Continuous, normal**: Mean ± SD
2. **Continuous, skewed**: Median (IQR or range)
3. **Categorical**: N (%)
4. **RCTs**: Do NOT include P values in Table 1 (randomization should balance)
5. **Observational**: P values acceptable (comparing exposed vs unexposed)
6. **Missing data**: Report N for each variable if different from group total

---

## Statistical Software Reporting

```
All statistical analyses were performed using R version 4.3.2
(R Foundation for Statistical Computing, Vienna, Austria) with the
'survival' package (version 3.5-7). Two-sided P values < 0.05 were
considered statistically significant.
```

Common alternatives:
- Stata version X (StataCorp LLC, College Station, TX)
- SAS version X (SAS Institute, Cary, NC)
- SPSS version X (IBM Corp, Armonk, NY)
- Python version X with scipy, statsmodels, lifelines packages
- JMP version X (SAS Institute)
- EZR version X (Saitama Medical Center, Jichi Medical University)

---

## 日本語

### 統計報告の要点

- 検定名、サンプルサイズ、効果量、95%信頼区間、P値を必ず記載
- P値は正確な値を報告（P = 0.034、P < 0.001）
- 「有意差なし」ではなく「統計学的に有意な差を認めなかった」
- Table 1のRCTではP値不要（ランダム化で均衡が保たれているため）
- 欠測データの処理方法を明記
- 多重比較の補正方法を記載
- 統計ソフトとバージョンを明記
- EZR（自治医科大学）は日本で広く使用されている

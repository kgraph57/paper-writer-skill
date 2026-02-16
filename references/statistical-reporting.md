# Statistical Reporting Guide for Medical Papers

## Overview

This guide covers statistical reporting standards for medical and health sciences research. Following these conventions ensures clarity, reproducibility, and compliance with journal requirements. Based on the SAMPL (Statistical Analyses and Methods in the Published Literature) guidelines and ICMJE recommendations.

Reference: Lang TA, Altman DG. Basic statistical reporting for articles published in Biomedical Journals: The "Statistical Analyses and Methods in the Published Literature" guidelines. Int J Nurs Stud. 2015;52(1):5-9.

---

## 1. Reporting p-Values

### Rules

- **Always report exact p-values** to 2-3 decimal places
- Use "p < 0.001" only when the exact value is below 0.001
- **Never write "p < 0.05"** or "p = NS" (non-significant)
- Do not use "p = 0.000" (use "p < 0.001")
- Always report p-values alongside effect sizes and confidence intervals

### Correct Examples

```
The mean difference was 2.3 kg (95% CI: 1.1 to 3.5; p = 0.002).
There was no significant difference between groups (mean difference: 0.4 kg, 95% CI: -0.8 to 1.6; p = 0.48).
The association was significant (OR = 2.15, 95% CI: 1.23 to 3.76; p = 0.007).
The hazard ratio was 0.72 (95% CI: 0.58 to 0.89; p < 0.001).
```

### Incorrect Examples (Avoid)

```
WRONG: The result was significant (p < 0.05).
WRONG: The result was not significant (p = NS).
WRONG: p = 0.000
WRONG: p = .03  (always include leading zero)
WRONG: The p-value was 0.04, which was significant.  (report effect size!)
```

### Formatting Conventions

- Lowercase italic "p" in most journals: *p* = 0.003
- No hyphen: "p value" or "p-value" (check journal style)
- Space around equals sign: *p* = 0.03 (not p=0.03)
- Leading zero: *p* = 0.03 (not *p* = .03)

---

## 2. Confidence Intervals

### Rules

- **Always report 95% CIs** with effect sizes (this is often more informative than p-values)
- Specify the confidence level if not 95%
- Use "to" or a comma to separate bounds (not a hyphen, which can be confused with a minus sign)
- Report CIs to the same decimal places as the point estimate

### Formatting

```
# Preferred formats (check journal style):
95% CI: 1.23 to 3.45
95% CI [1.23, 3.45]
95% CI (1.23-3.45)    # acceptable but "to" is clearer

# With effect size:
OR = 2.15 (95% CI: 1.23 to 3.76)
HR = 0.72; 95% CI, 0.58 to 0.89
Mean difference: 3.2 (95% CI: 1.1 to 5.3)
```

### Interpretation Tips

- If 95% CI for a ratio (OR, RR, HR) crosses 1.0, the result is not statistically significant
- If 95% CI for a difference crosses 0, the result is not statistically significant
- Width of CI indicates precision of the estimate
- Narrow CI = precise estimate; Wide CI = imprecise estimate

---

## 3. Descriptive Statistics

### When to Use Mean +/- SD vs. Median (IQR)

| Data Distribution | Measure of Center | Measure of Spread | Format |
|-------------------|-------------------|-------------------|--------|
| Normal (symmetric) | Mean | Standard Deviation (SD) | 45.2 +/- 12.3 |
| Skewed (non-normal) | Median | Interquartile Range (IQR) | 38.0 (IQR: 25.0-52.0) |
| Ordinal data | Median | IQR or range | Median: 3 (IQR: 2-4) |
| Counts/proportions | Count | Percentage | 45 (67.2%) |

### How to Assess Normality

- **Visual**: Histogram, Q-Q plot
- **Statistical tests**: Shapiro-Wilk (n < 50), Kolmogorov-Smirnov (n >= 50)
- **Rule of thumb**: Skewness between -1 and +1 suggests approximate normality
- **Practical**: If n > 30, means are often robust due to CLT, but still report median for skewed data

### Reporting Formats

```
# Continuous, normally distributed:
Age was 45.2 +/- 12.3 years (mean +/- SD).

# Continuous, skewed:
Length of stay was 5 days (IQR: 3-9).
Hospital costs were $12,450 (IQR: $7,200-$24,800).

# Categorical:
Female sex: 128 (64.0%)
Diabetes: 45/200 (22.5%)

# Table 1 format:
Age, years, mean +/- SD               45.2 +/- 12.3
BMI, kg/m2, median (IQR)              27.3 (24.1-31.5)
Female sex, n (%)                      128 (64.0)
Smoking status, n (%)
  Never                                95 (47.5)
  Former                               62 (31.0)
  Current                              43 (21.5)
```

### Common Mistakes

- Reporting mean +/- SEM (standard error of the mean) instead of SD for descriptive purposes
  - SD describes the data distribution
  - SEM describes the precision of the mean estimate
  - For Table 1 (baseline characteristics): always use SD
- Using +/- for skewed data (report median and IQR instead)
- Not specifying whether you are reporting SD or SEM
- Reporting percentages without the actual counts

---

## 4. Common Statistical Tests and When to Use Them

### Decision Tree

```
What type of outcome?
|
+-- Continuous outcome
|   |
|   +-- 2 groups
|   |   +-- Independent samples
|   |   |   +-- Normal: Independent t-test
|   |   |   +-- Non-normal: Mann-Whitney U test
|   |   +-- Paired/matched
|   |       +-- Normal: Paired t-test
|   |       +-- Non-normal: Wilcoxon signed-rank test
|   |
|   +-- 3+ groups
|       +-- Independent samples
|       |   +-- Normal: One-way ANOVA
|       |   +-- Non-normal: Kruskal-Wallis test
|       +-- Repeated measures
|           +-- Normal: Repeated-measures ANOVA
|           +-- Non-normal: Friedman test
|
+-- Categorical outcome
|   |
|   +-- 2x2 table
|   |   +-- Expected cell counts >= 5: Chi-square test
|   |   +-- Expected cell counts < 5: Fisher exact test
|   |
|   +-- RxC table
|   |   +-- Expected cell counts >= 5: Chi-square test
|   |   +-- Small expected counts: Fisher-Freeman-Halton test
|   |
|   +-- Paired/matched
|       +-- McNemar test
|
+-- Time-to-event outcome
    +-- 2 groups: Log-rank test
    +-- 2+ groups with covariates: Cox proportional hazards
    +-- Survival probability at time t: Kaplan-Meier
```

### Reporting Each Test

#### Independent t-test
```
Mean systolic BP was higher in the intervention group (132.4 +/- 15.2 mmHg)
than the control group (126.1 +/- 14.8 mmHg), with a mean difference of
6.3 mmHg (95% CI: 2.1 to 10.5; t(198) = 2.96, p = 0.003).
```

#### Mann-Whitney U test
```
Median length of stay was shorter in the intervention group (4 days,
IQR: 2-7) compared to the control group (6 days, IQR: 3-11;
U = 3842, p = 0.012).
```

#### Chi-square test
```
The proportion of patients achieving the primary endpoint was higher
in the treatment group (68/150, 45.3%) than the control group
(42/148, 28.4%; chi-square = 9.67, df = 1, p = 0.002).
```

#### Fisher exact test
```
There was no significant association between genotype and adverse events
(3/25 [12.0%] vs. 1/23 [4.3%]; Fisher exact test, p = 0.61).
```

#### One-way ANOVA
```
Mean HbA1c differed significantly across the three treatment groups
(F(2, 147) = 8.42, p < 0.001). Post hoc Tukey HSD tests revealed
that Group A (7.2 +/- 0.8%) was significantly lower than Group C
(8.1 +/- 1.1%, p < 0.001), but not Group B (7.6 +/- 0.9%, p = 0.12).
```

#### Kruskal-Wallis test
```
Median pain scores differed significantly among the three groups
(H(2) = 12.34, p = 0.002). Pairwise comparisons with Bonferroni
correction showed Group A (median: 3, IQR: 2-5) was significantly
lower than Group C (median: 6, IQR: 4-8; p = 0.001).
```

---

## 5. Regression Reporting

### Logistic Regression (Odds Ratios)

```
In multivariable logistic regression, diabetes was independently
associated with 30-day mortality (adjusted OR = 2.34, 95% CI: 1.45 to
3.78; p < 0.001), after adjusting for age, sex, BMI, and smoking status.
```

Table format:
```
| Variable         | Unadjusted OR (95% CI)  | p     | Adjusted OR (95% CI)    | p     |
|-----------------|-------------------------|-------|-------------------------|-------|
| Diabetes        | 2.89 (1.87-4.47)       | <0.001| 2.34 (1.45-3.78)        | <0.001|
| Age (per year)  | 1.03 (1.01-1.05)       | 0.002 | 1.02 (1.00-1.04)       | 0.04  |
| Male sex        | 1.56 (1.02-2.39)       | 0.04  | 1.41 (0.89-2.23)       | 0.14  |
| BMI (per kg/m2) | 1.05 (1.01-1.09)       | 0.01  | 1.03 (0.99-1.07)       | 0.18  |
| Current smoker  | 1.78 (1.12-2.83)       | 0.015 | 1.65 (1.01-2.69)       | 0.046 |
```

### Cox Proportional Hazards (Hazard Ratios)

```
In multivariable Cox regression, the intervention was associated with
reduced risk of disease progression (adjusted HR = 0.68, 95% CI: 0.52
to 0.89; p = 0.005), after adjusting for age, stage, and performance
status. The proportional hazards assumption was met (Schoenfeld residuals
global test, p = 0.34).
```

### Linear Regression (Beta Coefficients)

```
In multivariable linear regression, each additional hour of weekly
exercise was associated with a 0.15% decrease in HbA1c
(beta = -0.15, 95% CI: -0.23 to -0.07; p < 0.001), adjusting for
age, sex, baseline HbA1c, and medication use. The model explained
34% of the variance in HbA1c change (adjusted R-squared = 0.34).
```

### Poisson/Negative Binomial Regression (Incidence Rate Ratios)

```
The intervention group had a significantly lower rate of hospital
readmissions (adjusted IRR = 0.72, 95% CI: 0.58 to 0.89; p = 0.003).
```

### Key Reporting Elements for Any Regression

- [ ] Specify the regression model type
- [ ] Report both unadjusted and adjusted estimates
- [ ] List all covariates in the adjusted model
- [ ] Report how covariates were selected (a priori, stepwise, etc.)
- [ ] Check and report model assumptions
- [ ] Report model fit statistics (R-squared, AIC, C-statistic, Hosmer-Lemeshow)
- [ ] Report the number of events per variable (EPV) for logistic/Cox models (aim for >= 10)

---

## 6. Sample Size Justification

### Template for Sample Size Reporting

```
Sample size was calculated a priori using [software name, version].
Assuming a [effect size description] of [value], with a two-sided
significance level of 0.05 and 80% power, [N] participants per group
were required. Accounting for an estimated [X]% dropout rate, we
planned to enroll [N_total] participants ([N_per_group] per group).
```

### Examples by Study Design

#### RCT (Continuous Outcome)
```
Based on previous literature, we assumed a mean HbA1c reduction of
0.5% (SD = 1.0%) in the intervention group compared to control.
With alpha = 0.05 (two-sided) and 80% power, 64 participants per
group were needed (independent t-test). Allowing for 15% attrition,
we aimed to recruit 75 per group (150 total).
```

#### RCT (Binary Outcome)
```
We estimated the control group event rate at 30% and a clinically
meaningful absolute risk reduction of 15% (to 15%). With alpha = 0.05
and 80% power, 121 participants per group were required (chi-square
test). With 10% loss to follow-up, we targeted 134 per group (268 total).
```

#### Cohort Study
```
With an expected exposure prevalence of 25%, outcome rate of 10%
in unexposed and a hazard ratio of 2.0 to detect, 85% power, and
alpha = 0.05, we required 450 participants (Schoenfeld method for
Cox regression with 3 covariates).
```

### For Pilot/Feasibility Studies
```
As a pilot study, formal sample size calculation was not performed.
We aimed to recruit 30 participants per group based on recommendations
for pilot studies (Lancaster et al., 2004) to estimate key parameters
for a future definitive trial.
```

---

## 7. Multiple Comparisons Correction

### When to Apply

- **Always** when testing multiple hypotheses simultaneously
- **Always** for post-hoc pairwise comparisons after ANOVA
- **Consider** for multiple secondary outcomes

### Common Methods

| Method | Description | When to Use |
|--------|-------------|-------------|
| Bonferroni | alpha/n | Conservative; few comparisons |
| Holm-Bonferroni | Step-down Bonferroni | Less conservative than Bonferroni |
| Tukey HSD | Pairwise after ANOVA | All pairwise comparisons |
| Dunnett | Compare to single control | Multiple treatments vs. one control |
| Benjamini-Hochberg | Controls FDR | Many comparisons (e.g., genomics) |
| No correction | Pre-specified primary | Single primary outcome, pre-specified |

### Reporting Example

```
Post hoc pairwise comparisons were performed using Tukey's HSD to
control for multiple comparisons. The Benjamini-Hochberg procedure
was applied to secondary outcome analyses to control the false
discovery rate at 5%.
```

### When NOT to Correct

- Pre-specified single primary outcome (no correction needed)
- Exploratory analyses (clearly label as exploratory)
- Subgroup analyses (report as hypothesis-generating, not confirmatory)

---

## 8. Missing Data Handling and Reporting

### Reporting Requirements

1. **Describe the extent**: N and % missing for each variable
2. **Assess the mechanism**: MCAR, MAR, or MNAR
3. **Describe the approach**: How missing data were handled
4. **Sensitivity analysis**: Show results are robust to assumptions

### Missing Data Mechanisms

| Mechanism | Definition | Example | Test |
|-----------|-----------|---------|------|
| MCAR | Missing completely at random | Lab error | Little's MCAR test |
| MAR | Missing at random (conditional) | Older patients miss visits | Compare observed vs. missing |
| MNAR | Missing not at random | Sicker patients drop out | Cannot test; assume and do sensitivity analysis |

### Common Approaches

```
# Complete case analysis (list-wise deletion)
"Analysis was restricted to participants with complete data on all
variables (n = [N], [X]% of the total sample)."

# Multiple imputation
"Missing data ([X]% overall, ranging from [X]% to [X]% across variables)
were handled using multiple imputation by chained equations (MICE) with
[M] imputed datasets. The imputation model included all analysis
variables plus auxiliary variables associated with missingness."

# Last observation carried forward (less preferred)
"Missing values were imputed using last observation carried forward
(LOCF). Sensitivity analyses using complete cases and multiple
imputation yielded similar results."

# Maximum likelihood
"Full information maximum likelihood (FIML) estimation was used
to handle missing data under the MAR assumption."
```

### Reporting Table for Missing Data

```
| Variable            | N (%) Missing | Mechanism Assessment |
|--------------------|---------------|---------------------|
| Primary outcome    | 12 (6.0%)    | MAR (associated with age) |
| Secondary outcome  | 8 (4.0%)     | MCAR (Little's test p = 0.42) |
| Covariate: BMI     | 15 (7.5%)    | MAR |
| Covariate: Smoking | 3 (1.5%)     | MCAR |
```

---

## 9. Survival Analysis Reporting

### Kaplan-Meier

```
Median overall survival was 18.3 months (95% CI: 14.2 to 22.4) in
the intervention group and 12.7 months (95% CI: 9.8 to 15.6) in
the control group. The 1-year survival rate was 72.3% (95% CI: 64.1%
to 79.2%) in the intervention group and 54.8% (95% CI: 46.1% to 62.7%)
in the control group.
```

### Log-rank Test

```
Kaplan-Meier curves showed significantly better progression-free
survival in the intervention group (log-rank test: chi-square = 8.42,
df = 1, p = 0.004).
```

### Cox Proportional Hazards

```
In multivariable Cox regression adjusted for age, sex, and tumor stage,
the intervention was associated with reduced mortality risk
(adjusted HR = 0.65, 95% CI: 0.48 to 0.88; p = 0.005).

The proportional hazards assumption was evaluated using Schoenfeld
residuals. No significant violations were detected for any covariate
(global test p = 0.28). Linearity of continuous covariates was assessed
using Martingale residuals.
```

### Key Elements to Report

- [ ] Number at risk at key time points (for KM curves)
- [ ] Median follow-up time (reverse KM method preferred)
- [ ] Number of events and censored observations
- [ ] Proportional hazards assumption test results
- [ ] Handling of tied event times (Efron or Breslow method)
- [ ] Time unit (months, years)

---

## 10. Meta-Analysis Specific Reporting

### Heterogeneity

```
# I-squared (I2)
Substantial heterogeneity was observed across studies (I2 = 72%,
95% CI: 48% to 85%; Q = 28.6, df = 8, p < 0.001).

# Interpretation of I2:
#   0-25%:   Low heterogeneity
#   25-50%:  Moderate heterogeneity
#   50-75%:  Substantial heterogeneity
#   75-100%: Considerable heterogeneity

# Tau-squared (between-study variance)
The between-study variance was tau2 = 0.15 (95% CI: 0.04 to 0.52).
```

### Pooled Effect Estimates

```
# Random-effects model (DerSimonian-Laird)
The pooled odds ratio was 1.85 (95% CI: 1.23 to 2.78; p = 0.003)
using a random-effects model (DerSimonian-Laird method).

# Fixed-effects model (Mantel-Haenszel)
The pooled risk ratio was 0.72 (95% CI: 0.61 to 0.85; p < 0.001)
using a fixed-effects model (Mantel-Haenszel method).

# When to use which:
# - Random-effects: Expected clinical/methodological heterogeneity (most common)
# - Fixed-effects: Studies are functionally identical (rare)
# - Report both if results differ meaningfully
```

### Forest Plot Interpretation

A forest plot should display:
- Each study with its point estimate and 95% CI (horizontal line)
- Study weight (box size proportional to weight)
- Pooled estimate (diamond at bottom)
- Line of no effect (OR=1 or MD=0)
- Overall heterogeneity statistics

```
# Reporting forest plot results
Figure [N] presents the forest plot for [outcome]. Individual study
estimates ranged from [lowest] to [highest]. The pooled estimate
favored [intervention/control] (OR = 1.85, 95% CI: 1.23 to 2.78).
Smith et al. (2020) contributed the largest weight (18.3%) to the
pooled estimate.
```

### Publication Bias Assessment

```
# Funnel plot
Visual inspection of the funnel plot (Figure [N]) suggested
[symmetry/asymmetry], indicating [no evidence of/potential]
publication bias.

# Egger's test
Egger's regression test showed [no significant/significant] evidence
of small-study effects (intercept = 1.23, 95% CI: -0.45 to 2.91;
p = 0.14).

# Begg's test (rank correlation)
Begg's test was not significant (Kendall's tau = 0.12, p = 0.38).

# Trim and fill
Trim-and-fill analysis imputed [N] missing studies. The adjusted
pooled estimate was OR = 1.62 (95% CI: 1.05 to 2.50), compared
to the original OR = 1.85 (95% CI: 1.23 to 2.78).
```

**Note**: Publication bias tests have low power with fewer than 10 studies. State this limitation if applicable.

### Subgroup and Sensitivity Analyses

```
# Subgroup analysis
Subgroup analysis by study design showed a pooled OR of 2.12
(95% CI: 1.34 to 3.35; I2 = 45%) for RCTs and 1.56 (95% CI: 0.89
to 2.73; I2 = 68%) for observational studies. The test for subgroup
differences was not significant (chi-square = 1.23, df = 1, p = 0.27).

# Leave-one-out sensitivity analysis
Leave-one-out sensitivity analysis showed that removal of any
single study did not substantially change the pooled estimate
(range: 1.68 to 2.01), suggesting robustness of the findings.

# Sensitivity by risk of bias
Restricting to studies with low risk of bias (n = 5) yielded
a pooled OR of 1.72 (95% CI: 1.15 to 2.57), consistent with
the overall estimate.
```

### GRADE Certainty Assessment

```
The certainty of evidence was assessed using the GRADE approach.
Evidence was rated as [high/moderate/low/very low] due to
[risk of bias/inconsistency/indirectness/imprecision/publication bias].

| Outcome | Studies | Participants | Certainty | Effect (95% CI) |
|---------|---------|-------------|-----------|-----------------|
| Mortality | 8 RCTs | 2,456 | Moderate (downgraded for imprecision) | RR 0.78 (0.60-1.01) |
| Hospital stay | 6 RCTs | 1,834 | Low (downgraded for risk of bias and inconsistency) | MD -1.5 days (-2.8 to -0.2) |
```

---

## 11. Common Mistakes to Avoid

### Top 15 Statistical Reporting Errors

1. **Reporting p < 0.05 instead of exact values** -- Always give exact p-values
2. **No confidence intervals** -- Every effect size needs a CI
3. **Mean +/- SD for skewed data** -- Use median (IQR) for non-normal distributions
4. **SEM instead of SD in descriptive tables** -- SD describes the data; SEM describes precision of the mean
5. **Not specifying the statistical test** -- Always name the test used
6. **No sample size justification** -- Even retrospective studies should discuss power
7. **Ignoring multiple comparisons** -- Apply appropriate correction or justify not doing so
8. **Not reporting missing data** -- State N and % missing, method of handling
9. **"Trending toward significance" (p = 0.06)** -- Either significant or not; discuss clinical relevance instead
10. **Using parametric tests on ordinal data** -- Likert scales are ordinal; use non-parametric tests
11. **Not checking regression assumptions** -- Report assumption checks (linearity, normality of residuals, etc.)
12. **Confusing association with causation** -- Use appropriate language for observational studies
13. **Reporting only "significant" results** -- Report all pre-specified analyses regardless of p-value
14. **Inappropriate rounding** -- Report effect sizes to 2 decimal places; p-values to 2-3
15. **No denominator for percentages** -- Always report n/N (%) format

### Language Guidelines

```
# CORRECT: Precise statistical language
"There was a statistically significant difference in mean HbA1c
between groups (mean difference: 0.5%, 95% CI: 0.2% to 0.8%; p = 0.002)."

# INCORRECT: Vague language
"HbA1c was significantly better in the treatment group (p < 0.05)."

# CORRECT: For non-significant results
"The difference in readmission rates was not statistically significant
(12.3% vs. 10.8%, absolute difference: 1.5%, 95% CI: -3.2% to 6.2%;
p = 0.53), though the CI does not exclude a clinically meaningful difference."

# INCORRECT: For non-significant results
"There was no difference between groups (p = 0.53)."
(This conflates "no significant difference" with "no difference")

# For observational studies, use:
"associated with" NOT "caused by"
"risk factor for" NOT "leads to"
"higher odds of" NOT "increased the risk of"
```

---

## 12. Quick Reference: Which Numbers to Report

### By Study Design

| Design | Primary Analysis | Report |
|--------|-----------------|--------|
| RCT | Between-group comparison | Effect size, 95% CI, p-value, NNT |
| Cohort | Association | OR/RR/HR, 95% CI, p-value |
| Case-control | Association | OR, 95% CI, p-value |
| Cross-sectional | Prevalence/association | Prevalence (95% CI), OR |
| Diagnostic | Test accuracy | Sensitivity, specificity, PPV, NPV, AUC (95% CI) |
| Meta-analysis | Pooled effect | Pooled estimate, 95% CI, I2, Q, p-value |
| Qualitative | Themes | N/A (no statistical tests) |

### Checklist Before Submission

- [ ] All p-values are exact (or < 0.001)
- [ ] All effect sizes have 95% CIs
- [ ] Descriptive stats match data distribution (mean+/-SD or median(IQR))
- [ ] Statistical tests are named and appropriate
- [ ] Sample size justification is included
- [ ] Missing data are described and addressed
- [ ] Multiple comparisons are addressed
- [ ] Model assumptions are checked and reported
- [ ] Figures have appropriate labels and legends
- [ ] Numbers in text match numbers in tables
- [ ] Denominators are clear for all percentages
- [ ] Software and version are specified

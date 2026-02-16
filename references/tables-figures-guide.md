# Tables and Figures Guide

## Overview

Tables and figures are the backbone of a paper. Many reviewers look at the abstract, then the tables and figures, before reading the text. Design them to tell the story independently.

---

## General Principles

1. Each table/figure should convey one clear message without requiring the reader to consult the text
2. Do not duplicate data between tables and text, or between tables and figures
3. All tables and figures must be cited in the text in numerical order
4. Captions must be self-explanatory -- include enough context to understand the figure without reading the main text
5. Consistent formatting across all tables/figures in the manuscript

---

## When to Use Tables vs. Figures

| Use a Table when... | Use a Figure when... |
|---------------------|---------------------|
| Presenting exact numerical values | Showing trends, patterns, or distributions |
| Comparing multiple variables across groups | Demonstrating spatial or temporal relationships |
| Reporting baseline characteristics | Presenting survival curves, forest plots |
| Showing regression results | Illustrating a process, pathway, or algorithm |
| Data precision matters | Visual impression matters |

---

## Tables

### Table 1: Baseline Characteristics (Standard Format)

```
Table 1. Baseline characteristics of the study population

| Characteristic | Total (N=XXX) | Group A (n=XXX) | Group B (n=XXX) | p-value |
|----------------|---------------|-----------------|-----------------|---------|
| Age, years, mean +/- SD | | | | |
| Female sex, n (%) | | | | |
| BMI, kg/m2, median (IQR) | | | | |
| Comorbidities, n (%) | | | | |
|   Hypertension | | | | |
|   Diabetes | | | | |
|   Heart failure | | | | |
| Laboratory values | | | | |
|   HbA1c, %, mean +/- SD | | | | |
|   eGFR, mL/min/1.73m2 | | | | |

Data are presented as mean +/- SD, median (IQR), or n (%).
p-values from [t-test / Mann-Whitney U / chi-square / Fisher exact] as appropriate.
Abbreviations: BMI, body mass index; eGFR, estimated glomerular filtration rate;
HbA1c, glycated hemoglobin; IQR, interquartile range; SD, standard deviation.
```

Rules for Table 1:
- Use mean +/- SD for normal data, median (IQR) for skewed data
- Always report both n and % for categorical variables
- State the statistical test used in the footnote
- Define all abbreviations in the footnote
- For RCTs: do NOT include p-values in Table 1 (CONSORT recommendation)

### Regression Results Table

```
Table X. Multivariable [logistic/Cox/linear] regression analysis for [outcome]

| Variable | Unadjusted OR (95% CI) | p | Adjusted OR (95% CI) | p |
|----------|------------------------|---|----------------------|---|
| [Var 1] | | | | |
| [Var 2] | | | | |
| [Var 3] (ref: [category]) | | | | |
|   [Category A] | | | | |
|   [Category B] | | | | |

aOR, adjusted odds ratio; CI, confidence interval; OR, odds ratio.
Adjusted for [list all covariates].
```

### Table Formatting Rules

- [ ] Title above the table (not below)
- [ ] No vertical lines (horizontal lines only: top, header separator, bottom)
- [ ] Column headers clearly labeled with units
- [ ] Consistent decimal places within each column
- [ ] Footnotes for abbreviations, statistical tests, special symbols
- [ ] Use superscript letters (a, b, c) for footnotes, not symbols
- [ ] Total sample size in the header row

---

## Figures

### Common Figure Types in Medical Papers

| Figure Type | When to Use | Tool |
|-------------|-------------|------|
| Flow diagram (CONSORT/PRISMA) | Patient selection, study flow | draw.io, Lucidchart |
| Kaplan-Meier curve | Survival/time-to-event data | R, Python, SPSS, Stata |
| Forest plot | Meta-analysis, subgroup effects | R (metafor), Python, RevMan |
| Bar chart / Box plot | Group comparisons | R (ggplot2), Python (matplotlib) |
| Scatter plot | Correlations, regression | R, Python |
| ROC curve | Diagnostic accuracy | R (pROC), Python (sklearn) |
| Timeline | Case reports, clinical course | draw.io, PowerPoint |
| Heatmap | Correlation matrix, gene expression | R (pheatmap), Python (seaborn) |
| Graphical abstract | Visual summary for TOC | BioRender, Illustrator, Canva |

### Figure Resolution Requirements

| Purpose | Resolution | Format |
|---------|-----------|--------|
| Print publication | 300 DPI minimum | TIFF, EPS, PDF |
| Online only | 150 DPI minimum | PNG, JPEG, SVG |
| Line art (graphs, diagrams) | 600-1200 DPI | TIFF, EPS, SVG |
| Photographs / medical images | 300 DPI | TIFF, JPEG |

Most journals require TIFF or EPS at 300+ DPI for final submission.

### Figure Size Guidelines

| Type | Width | Notes |
|------|-------|-------|
| Single column | 8.5 cm (3.3 in) | Most figures |
| 1.5 column | 11.4 cm (4.5 in) | Wider figures |
| Double column | 17.4 cm (6.85 in) | Full-width figures |

Design at final print size. Text within figures should be 8-12 pt after scaling.

### Caption Writing Rules

```
Figure [N]. [Descriptive title in sentence case].
[Detailed explanation of what is shown, including statistics].
[Explanation of symbols, colors, or abbreviations].
[Sample sizes if not in the figure itself].
Abbreviations: [list all].
```

Example:
```
Figure 2. Kaplan-Meier estimates of progression-free survival
by treatment group. The intervention group (solid line) showed
longer progression-free survival compared with the control group
(dashed line) (median: 18.3 vs. 12.7 months; log-rank p = 0.004).
Shaded areas represent 95% confidence intervals. Numbers at risk
are shown below the x-axis. HR, hazard ratio; CI, confidence interval.
```

### Caption Checklist

- [ ] Starts with "Figure [N]." (period after number)
- [ ] Descriptive title (not just "Results")
- [ ] Key statistical values included
- [ ] All symbols/colors/line styles explained
- [ ] Abbreviations defined
- [ ] Self-explanatory without reading main text

---

## CONSORT Flow Diagram Template

```
Assessed for eligibility (n= )
          |
     Excluded (n= )
     - Not meeting criteria (n= )
     - Declined to participate (n= )
     - Other reasons (n= )
          |
     Randomized (n= )
      /              \
Allocated to         Allocated to
intervention (n= )   control (n= )
     |                    |
Lost to follow-up   Lost to follow-up
(n= , reasons)      (n= , reasons)
     |                    |
Analyzed (n= )       Analyzed (n= )
Excluded from        Excluded from
analysis (n= ,      analysis (n= ,
reasons)             reasons)
```

---

## Color Usage Guidelines

- Use colorblind-friendly palettes (avoid red-green combinations)
- Recommended palettes: Okabe-Ito, viridis, ColorBrewer
- Ensure figures are readable in grayscale (for print)
- Use different line styles (solid, dashed, dotted) in addition to colors
- Maintain consistent color assignments across all figures

---

## Common Mistakes

1. Too many panels in one figure -- split into multiple figures if > 6 panels
2. Axis labels too small -- must be readable at final print size (8+ pt)
3. 3D graphs -- almost never appropriate for scientific figures; use 2D
4. Pie charts -- avoid; use bar charts instead (easier to compare)
5. Dual y-axes -- misleading; use separate panels instead
6. Missing error bars -- always show variability (SD, SEM, or 95% CI)
7. Inconsistent scales -- when comparing panels, use the same axis range
8. Low resolution -- always export at 300+ DPI for submission
9. Copyright violation -- get permission for any reproduced figures
10. Missing patient consent -- clinical photos require written consent

---

## File Organization in Project

```
figures/
  fig1_consort-flow.{svg,tiff}
  fig1_caption.md
  fig2_kaplan-meier.{svg,tiff}
  fig2_caption.md
  graphical-abstract.{svg,tiff}

tables/
  table1_baseline.md
  table2_regression.md
  table3_outcomes.md
```

Each figure file should have a companion caption file for easy editing.

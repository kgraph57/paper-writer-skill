# Data Analysis Workflow

## Overview

Data analysis follows the data directory flow:

```
data/raw/ → data/processed/ → data/analysis/ → tables/ + figures/
```

Claude Code executes Python scripts directly. All analysis output goes to `data/analysis/`.

## Available Scripts

| Script | Purpose | Key Output |
|--------|---------|------------|
| `scripts/table1.py` | Table 1 (baseline characteristics) | Markdown table with N, %, mean±SD, P values |
| `scripts/analysis-template.py` | Statistical analyses | Descriptive stats, t-test, logistic regression, survival |
| `scripts/forest-plot.py` | Forest plot (meta-analysis) | PNG + SVG |

## Analysis Workflow Steps

### Step 1: Data Inspection

```python
import pandas as pd
df = pd.read_csv("data/processed/cohort_final.csv")
print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
```

### Step 2: Table 1 — Baseline Characteristics

```bash
python scripts/table1.py \
  --input data/processed/cohort_final.csv \
  --group treatment_group \
  --exclude patient_id \
  --output tables/table1.md
```

Auto-detects:
- Continuous → mean ± SD (normal) or median [IQR] (non-normal)
- Binary → n (%)
- Categorical → n (%) per level
- P values: t-test/Mann-Whitney for continuous, chi-square/Fisher's for categorical

### Step 3: Primary Analysis

Choose based on study design:

**Cross-sectional / Case-control → Logistic Regression:**

```bash
python scripts/analysis-template.py \
  --input data/processed/cohort_final.csv \
  --analysis logistic \
  --outcome outcome \
  --predictors age sex bmi exposure \
  --output-dir data/analysis/
```

Output: Univariate + multivariate OR with 95% CI

**Cohort with time-to-event → Survival Analysis:**

```bash
python scripts/analysis-template.py \
  --input data/processed/cohort_final.csv \
  --analysis survival \
  --time follow_up_months \
  --event event_occurred \
  --group exposure_group \
  --output-dir data/analysis/
```

Output: Kaplan-Meier curves, median survival, log-rank P

**Continuous outcome → Linear Regression:**

```bash
python scripts/analysis-template.py \
  --input data/processed/cohort_final.csv \
  --analysis linear \
  --outcome score \
  --predictors age sex treatment \
  --output-dir data/analysis/
```

**Group comparison → t-test / Mann-Whitney:**

```bash
python scripts/analysis-template.py \
  --input data/processed/cohort_final.csv \
  --analysis ttest \
  --outcome measurement \
  --group treatment_group \
  --output-dir data/analysis/
```

### Step 4: Subgroup & Sensitivity Analyses

Common subgroup analyses to consider:
- By sex (male/female)
- By age group (< 65 / ≥ 65)
- By disease severity
- Excluding outliers
- Complete case analysis vs. imputed data

### Step 5: Figures

**Common figure types for medical papers:**

| Figure Type | When to Use | Python Library |
|-------------|------------|----------------|
| Box plot | Group comparison | matplotlib |
| Kaplan-Meier curve | Survival analysis | lifelines + matplotlib |
| Forest plot | Meta-analysis / subgroup analysis | `scripts/forest-plot.py` |
| ROC curve | Diagnostic / prediction model | sklearn + matplotlib |
| Flow diagram | Patient selection (CONSORT/PRISMA) | manual or mermaid |
| Scatter plot | Correlation | matplotlib |
| Bar chart | Categorical comparison | matplotlib |

**Figure specifications for journals:**
- Resolution: 300 DPI minimum (600 DPI for line art)
- Format: TIFF or EPS preferred; PNG/SVG acceptable
- Width: single column (8.5 cm) or double column (17.5 cm)
- Font: Arial or Helvetica, 8-12 pt
- Color: use colorblind-safe palettes

### Step 6: Link to Manuscript

After analysis is complete, link results to manuscript sections:

| Analysis Output | Maps to |
|----------------|---------|
| `tables/table1.md` | Results: "Baseline characteristics..." |
| `data/analysis/logistic_*.md` | Results: "In multivariate analysis..." |
| `data/analysis/km_curve.png` | Figure 1 |
| `data/analysis/descriptive_stats.md` | Results: first paragraph |

## Common Python Packages

```
# Core (usually pre-installed)
numpy
pandas

# Statistics
scipy          # t-test, chi-square, Mann-Whitney, Shapiro-Wilk
statsmodels    # Logistic regression, linear regression, GLM

# Survival
lifelines      # Kaplan-Meier, Cox regression, log-rank test

# Visualization
matplotlib     # All figure types
seaborn        # Statistical visualization

# Machine learning (if needed)
scikit-learn   # ROC, AUC, prediction models
```

Install all at once:

```bash
pip install numpy pandas scipy statsmodels lifelines matplotlib seaborn scikit-learn
```

## Statistical Reporting Checklist

Before writing Results, confirm:

- [ ] Effect sizes reported with 95% confidence intervals
- [ ] P values reported to 3 decimal places (P < 0.001 for very small)
- [ ] Statistical tests named (e.g., "Mann-Whitney U test")
- [ ] Software and version documented (e.g., "Python 3.12, scipy 1.14")
- [ ] Two-sided tests used (unless justified)
- [ ] Multiple comparison correction applied (if >1 primary outcome)
- [ ] Missing data handling described
- [ ] Sample size justification provided (if applicable)

See `references/statistical-reporting-full.md` for detailed SAMPL guidelines.

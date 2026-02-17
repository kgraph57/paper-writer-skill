# Data Management Template

## Data Directory Structure

```
data/
├── raw/                    # Original data (NEVER modify)
│   ├── README.md           # Data source, extraction date, IRB info
│   └── (raw data files)
├── processed/              # Cleaned, de-identified data
│   ├── README.md           # Processing steps applied
│   └── (processed files)
├── analysis/               # Statistical output, model results
│   ├── README.md           # Analysis software, scripts used
│   └── (analysis output)
└── data-dictionary.md      # Variable definitions
```

## data/raw/README.md Template

```markdown
# Raw Data

## Source
- **Database**: [e.g., hospital EMR, REDCap, research database]
- **Extraction date**: YYYY-MM-DD
- **Extracted by**: [name]
- **Query/method**: [how data was extracted]

## Ethics
- **IRB approval**: [approval number]
- **IRB institution**: [institution name]
- **Approval date**: YYYY-MM-DD
- **Data use agreement**: [Yes/No, reference number if applicable]

## Files

| File | Description | Records | Variables | Format |
|------|-------------|---------|-----------|--------|
| | | | | |

## Important
- DO NOT modify files in this directory
- All cleaning/transformation goes in processed/
- Keep a backup outside this project directory
```

## data/processed/README.md Template

```markdown
# Processed Data

## Processing Log

| Step | Date | Description | Script/Method | Input | Output |
|------|------|-------------|---------------|-------|--------|
| 1 | YYYY-MM-DD | De-identification | [manual/script] | raw/file.csv | processed/file_deidentified.csv |
| 2 | YYYY-MM-DD | Exclude criteria applied | [manual/script] | | |
| 3 | YYYY-MM-DD | Missing data handled | [method] | | |
| 4 | YYYY-MM-DD | Variable recoding | [details] | | |

## De-identification Checklist

- [ ] Patient names removed
- [ ] Medical record numbers removed
- [ ] Dates shifted or generalized (age only, year only)
- [ ] Geographic data generalized (prefecture level or broader)
- [ ] Rare conditions/combinations checked for re-identification risk
- [ ] Free-text fields reviewed and scrubbed
- [ ] File metadata (Excel author, etc.) cleaned

## Inclusion/Exclusion

- **Total records extracted**: N
- **Excluded**: N (reasons below)
  - Reason 1: n
  - Reason 2: n
  - ...
- **Final sample**: N

## Files

| File | Description | Records | Variables | Format |
|------|-------------|---------|-----------|--------|
| | | | | |
```

## data/analysis/README.md Template

```markdown
# Analysis Output

## Software
- **Statistical software**: [R / Stata / SPSS / Python / SAS]
- **Version**: [version number]
- **Key packages**: [e.g., tidyverse, survival, lme4]

## Analysis Scripts

| Script | Description | Input | Output |
|--------|-------------|-------|--------|
| | | | |

## Output Files

| File | Description | Corresponds to |
|------|-------------|----------------|
| | | Table 1 |
| | | Figure 1 |
| | | Supplementary Table S1 |

## Reproducibility
- [ ] Scripts run without manual intervention
- [ ] Random seed set (if applicable)
- [ ] Software version documented
- [ ] All file paths are relative (no hardcoded absolute paths)
```

## data/data-dictionary.md Template

```markdown
# Data Dictionary

## Overview
- **Dataset**: [name]
- **Source**: [reference to raw/README.md]
- **Last updated**: YYYY-MM-DD
- **Total variables**: N
- **Total records**: N

## Variables

| Variable | Label | Type | Values/Range | Unit | Missing | Notes |
|----------|-------|------|-------------|------|---------|-------|
| pt_id | Patient ID | string | unique identifier | — | 0 | De-identified |
| age | Age at enrollment | integer | 0-120 | years | | |
| sex | Sex | categorical | 0=Female, 1=Male | — | | |
| bmi | Body Mass Index | continuous | 10.0-60.0 | kg/m² | | |
| | | | | | | |

### Type definitions
- **categorical**: finite set of values (list all levels)
- **continuous**: numeric with decimal
- **integer**: whole number
- **string**: text
- **date**: YYYY-MM-DD format
- **binary**: 0/1 or Yes/No

### Missing data codes
- `NA`: not available (data exists but was not recorded)
- `NP`: not applicable (variable does not apply to this patient)
- (blank): truly missing
```

---

## Quick Setup Guide

When starting a new paper project, create the data directory:

1. Create `data/raw/`, `data/processed/`, `data/analysis/`
2. Copy raw data into `data/raw/` — these files are READ-ONLY from this point
3. Fill in `data/raw/README.md` (source, ethics, file inventory)
4. Create `data/data-dictionary.md` for all variables
5. Process data in `data/processed/`, logging each step
6. Run analyses, save output to `data/analysis/`
7. Link analysis output to specific Tables/Figures in the manuscript

## File Naming Convention

```
[type]_[description]_[version].[ext]

Examples:
  raw_patient_demographics_v1.csv
  processed_cohort_final.csv
  analysis_table1_descriptive.xlsx
  analysis_figure2_survival_curve.png
```

Rules:
- Lowercase, underscores (no spaces, no Japanese characters in filenames)
- Version suffix for files that may be updated (`_v1`, `_v2`)
- Date suffix for snapshots (`_20260217`)
- Keep extensions consistent (`.csv` for tabular data, `.xlsx` only when formulas needed)

## Data Security Reminders

- **NEVER commit patient-identifiable data to git**
- Add `data/raw/` to `.gitignore` if the repository is shared
- Store raw data backups in a separate secure location
- Follow your institution's data handling policy
- Encrypt sensitive files if stored on cloud services

### Recommended .gitignore additions

```
# Raw patient data (never commit)
data/raw/*.csv
data/raw/*.xlsx
data/raw/*.sav
data/raw/*.dta

# Large analysis output
data/analysis/*.pdf
data/analysis/*.png
data/analysis/*.tiff
```

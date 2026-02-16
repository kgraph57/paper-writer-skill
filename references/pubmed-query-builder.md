# PubMed Search Query Construction Guide

## Overview

This guide provides a systematic approach to building effective PubMed search queries for systematic reviews, scoping reviews, and comprehensive literature searches. Following this process ensures reproducibility and completeness.

---

## 1. MeSH Term Lookup Process

Medical Subject Headings (MeSH) are the NLM controlled vocabulary used to index articles in PubMed.

### Step-by-Step MeSH Lookup

1. **Open MeSH Browser**: https://meshb.nlm.nih.gov/search
2. **Search your concept** (e.g., "artificial intelligence")
3. **Review the MeSH tree** to find the most appropriate term
4. **Check "Entry Terms"** (synonyms that map to the MeSH heading)
5. **Note the tree number** for understanding hierarchy
6. **Decide on explosion**: By default, PubMed "explodes" MeSH terms to include all narrower terms

### Example: Finding MeSH for "Machine Learning"

```
Search: machine learning
Result: Artificial Intelligence [MeSH]
  └── Machine Learning [MeSH]
       ├── Deep Learning [MeSH]
       ├── Supervised Machine Learning [MeSH]
       └── Unsupervised Machine Learning [MeSH]

Entry Terms: neural networks, random forest, support vector machine...
```

**Key Decision**: Searching `"Machine Learning"[MeSH]` automatically includes Deep Learning, Supervised ML, etc. Use `"Machine Learning"[MeSH:NoExp]` to exclude narrower terms.

### Common MeSH Pitfalls

- New concepts may not have MeSH terms yet (e.g., "ChatGPT" - no MeSH as of 2025)
- MeSH terms are updated annually; check the year introduced
- Some MeSH terms are surprisingly broad or narrow
- Articles published recently may not yet have MeSH terms assigned

---

## 2. Boolean Operators

### AND — Narrows results (intersection)

```
"Diabetes Mellitus"[MeSH] AND "Artificial Intelligence"[MeSH]
→ Articles about BOTH diabetes AND AI
```

### OR — Broadens results (union)

```
"Machine Learning"[MeSH] OR "Deep Learning"[MeSH] OR "neural network*"[tiab]
→ Articles about ANY of these concepts
```

### NOT — Excludes results (use with caution)

```
"Diabetes Mellitus"[MeSH] NOT "Diabetes Mellitus, Type 1"[MeSH]
→ Diabetes articles excluding Type 1
```

**Warning**: NOT can inadvertently exclude relevant articles. An article about both Type 1 and Type 2 diabetes would be excluded. Use sparingly and document your rationale.

### Operator Precedence and Grouping

PubMed processes operators left to right. **Always use parentheses** to control logic:

```
("Diabetes Mellitus, Type 2"[MeSH] OR "type 2 diabetes"[tiab])
AND
("Artificial Intelligence"[MeSH] OR "machine learning"[tiab] OR "deep learning"[tiab])
AND
("Diagnosis"[MeSH] OR "diagnosis"[tiab] OR "detection"[tiab])
```

---

## 3. Field Tags

### Most Commonly Used

| Tag | Field | Description | Example |
|-----|-------|-------------|---------|
| `[MeSH]` | MeSH Terms | Controlled vocabulary (exploded) | `"Neoplasms"[MeSH]` |
| `[MeSH:NoExp]` | MeSH (no explosion) | Exact MeSH heading only | `"Neoplasms"[MeSH:NoExp]` |
| `[Majr]` | MeSH Major Topic | MeSH term is a major focus | `"Neoplasms"[Majr]` |
| `[tiab]` | Title/Abstract | Words in title or abstract | `"machine learning"[tiab]` |
| `[ti]` | Title only | Words in title only | `"systematic review"[ti]` |
| `[au]` | Author | Author name | `"Smith JA"[au]` |
| `[pt]` | Publication Type | Type of publication | `"Randomized Controlled Trial"[pt]` |
| `[dp]` | Date of Publication | Publication date | `"2020/01/01"[dp] : "2025/12/31"[dp]` |
| `[la]` | Language | Language of article | `English[la]` |
| `[sb]` | Subset | Database subset | `medline[sb]` |
| `[tw]` | Text Word | All text fields | `"patient education"[tw]` |

### Advanced Field Tags

| Tag | Field | Example |
|-----|-------|---------|
| `[ad]` | Affiliation | `"Harvard"[ad]` |
| `[jn]` | Journal Name | `"JAMA"[jn]` |
| `[pmid]` | PubMed ID | `"12345678"[pmid]` |
| `[doi]` | DOI | `"10.1001/jama.2020.1234"[doi]` |

### Truncation and Wildcards

- **Asterisk (*)**: Truncation — `"therap*"` finds therapy, therapies, therapeutic, etc.
- Truncation works with `[tiab]` and `[tw]`, NOT with `[MeSH]`
- Place `*` at the end of a word stem (minimum 4 characters recommended)
- **Phrase searching**: Use quotes for exact phrases — `"patient education"[tiab]`

---

## 4. Filters

### Common Filters (Applied via URL or Advanced Search)

```
# Humans only (exclude animal-only studies)
Humans[MeSH]

# English language
English[la]

# Date range
("2020/01/01"[dp] : "2025/12/31"[dp])

# Publication types
"Randomized Controlled Trial"[pt]
"Systematic Review"[pt]
"Meta-Analysis"[pt]
"Review"[pt]
"Clinical Trial"[pt]
"Observational Study"[pt]

# Age groups
"Adult"[MeSH]          # 19+ years
"Child"[MeSH]          # 0-18 years
"Aged"[MeSH]           # 65+ years
"Infant"[MeSH]         # 1-23 months

# Sex
"Female"[MeSH]
"Male"[MeSH]
```

### Study Design Filters (Validated)

PubMed provides validated filters. For systematic reviews, use the **Cochrane Highly Sensitive Search Strategy** for RCTs:

```
# Cochrane RCT filter (sensitivity-maximizing version)
randomized controlled trial[pt]
OR controlled clinical trial[pt]
OR randomized[tiab]
OR placebo[tiab]
OR drug therapy[sh]
OR randomly[tiab]
OR trial[tiab]
OR groups[tiab]
NOT (animals[MeSH] NOT humans[MeSH])
```

---

## 5. Building a Systematic Search: Concept Table Method

### Step 1: Define Your PICO/PEO Question

| Element | Description | Example |
|---------|-------------|---------|
| P (Population) | Who? | Adults with Type 2 diabetes |
| I (Intervention/Exposure) | What? | AI-based clinical decision support |
| C (Comparison) | Compared to? | Standard care |
| O (Outcome) | Result? | Glycemic control (HbA1c) |

### Step 2: Build the Concept Table

| Concept 1 (Population) | Concept 2 (Intervention) | Concept 3 (Outcome) |
|------------------------|--------------------------|---------------------|
| "Diabetes Mellitus, Type 2"[MeSH] | "Artificial Intelligence"[MeSH] | "Glycated Hemoglobin A"[MeSH] |
| "type 2 diabetes"[tiab] | "Machine Learning"[MeSH] | "HbA1c"[tiab] |
| "T2DM"[tiab] | "Deep Learning"[MeSH] | "glycemic control"[tiab] |
| "NIDDM"[tiab] | "artificial intelligence"[tiab] | "blood glucose"[tiab] |
| "non-insulin dependent"[tiab] | "machine learning"[tiab] | "Glycemic Control"[MeSH] |
| | "deep learning"[tiab] | "Blood Glucose"[MeSH] |
| | "neural network*"[tiab] | |
| | "clinical decision support"[tiab] | |

### Step 3: Combine with Boolean Logic

```
# Within each concept: combine with OR
# Between concepts: combine with AND

(
  "Diabetes Mellitus, Type 2"[MeSH]
  OR "type 2 diabetes"[tiab]
  OR "T2DM"[tiab]
  OR "NIDDM"[tiab]
  OR "non-insulin dependent"[tiab]
)
AND
(
  "Artificial Intelligence"[MeSH]
  OR "Machine Learning"[MeSH]
  OR "Deep Learning"[MeSH]
  OR "artificial intelligence"[tiab]
  OR "machine learning"[tiab]
  OR "deep learning"[tiab]
  OR "neural network*"[tiab]
  OR "clinical decision support"[tiab]
)
AND
(
  "Glycated Hemoglobin A"[MeSH]
  OR "Glycemic Control"[MeSH]
  OR "Blood Glucose"[MeSH]
  OR "HbA1c"[tiab]
  OR "glycemic control"[tiab]
  OR "blood glucose"[tiab]
)
```

### Step 4: Add Limits (if appropriate)

```
AND Humans[MeSH]
AND English[la]
AND ("2015/01/01"[dp] : "2025/12/31"[dp])
```

---

## 6. Example Queries for Common Systematic Review Topics

### Example A: LLMs for Patient Education

```
(
  "Artificial Intelligence"[MeSH]
  OR "Natural Language Processing"[MeSH]
  OR "large language model*"[tiab]
  OR "LLM"[tiab]
  OR "ChatGPT"[tiab]
  OR "GPT-4"[tiab]
  OR "generative AI"[tiab]
  OR "generative artificial intelligence"[tiab]
  OR "chatbot*"[tiab]
)
AND
(
  "Patient Education as Topic"[MeSH]
  OR "Health Literacy"[MeSH]
  OR "Health Communication"[MeSH]
  OR "patient education"[tiab]
  OR "health information"[tiab]
  OR "health literacy"[tiab]
  OR "patient information"[tiab]
  OR "consumer health"[tiab]
)
```

### Example B: AI in Medical Imaging Diagnostics

```
(
  "Artificial Intelligence"[MeSH]
  OR "Deep Learning"[MeSH]
  OR "artificial intelligence"[tiab]
  OR "deep learning"[tiab]
  OR "convolutional neural network*"[tiab]
  OR "computer-aided detect*"[tiab]
  OR "computer-aided diagnos*"[tiab]
)
AND
(
  "Diagnostic Imaging"[MeSH]
  OR "Radiology"[MeSH]
  OR "radiograph*"[tiab]
  OR "CT scan*"[tiab]
  OR "MRI"[tiab]
  OR "X-ray*"[tiab]
  OR "medical imag*"[tiab]
  OR "pathology"[tiab]
)
AND
(
  "Sensitivity and Specificity"[MeSH]
  OR "ROC Curve"[MeSH]
  OR "accuracy"[tiab]
  OR "sensitivity"[tiab]
  OR "specificity"[tiab]
  OR "AUC"[tiab]
  OR "diagnostic performance"[tiab]
)
```

### Example C: Telemedicine for Mental Health

```
(
  "Telemedicine"[MeSH]
  OR "Telehealth"[MeSH]
  OR "Remote Consultation"[MeSH]
  OR "telemedicine"[tiab]
  OR "telehealth"[tiab]
  OR "telepsychiatry"[tiab]
  OR "teletherapy"[tiab]
  OR "video consult*"[tiab]
)
AND
(
  "Mental Disorders"[MeSH]
  OR "Depression"[MeSH]
  OR "Anxiety Disorders"[MeSH]
  OR "mental health"[tiab]
  OR "depression"[tiab]
  OR "anxiety"[tiab]
  OR "psychiatric"[tiab]
)
AND
(
  "Treatment Outcome"[MeSH]
  OR "treatment outcome*"[tiab]
  OR "effectiveness"[tiab]
  OR "efficacy"[tiab]
  OR "patient satisfaction"[tiab]
)
```

---

## 7. Sensitivity vs. Precision Trade-offs

### High Sensitivity (Recall) — For Systematic Reviews

**Goal**: Find ALL relevant articles, accept many irrelevant ones.

Strategies:
- Use both MeSH terms AND free-text synonyms
- Include spelling variants (e.g., "randomised" and "randomized")
- Use truncation liberally (`therap*`, `diagnos*`)
- Minimize NOT operators
- Use fewer concepts (omit outcome concept if broad)
- Explode MeSH terms (default)
- Include [tw] text word searches

```
# HIGH SENSITIVITY: broader, more results
("diabetes"[tiab] OR "diabetic"[tiab] OR "Diabetes Mellitus"[MeSH])
```

### High Precision (Specificity) — For Focused Searches

**Goal**: Find mostly relevant articles, miss some edge cases.

Strategies:
- Use [Majr] (Major MeSH topic) instead of [MeSH]
- Search [ti] (title only) instead of [tiab]
- Use more specific MeSH terms with [MeSH:NoExp]
- Add more concept lines (stricter AND combinations)
- Use publication type filters

```
# HIGH PRECISION: narrower, fewer results
("Diabetes Mellitus, Type 2"[Majr] AND "type 2 diabetes"[ti])
```

### Practical Recommendation

For systematic reviews: **maximize sensitivity first**, then screen results. The cost of missing a relevant study outweighs the cost of screening extra irrelevant ones.

| Search Type | Sensitivity Target | Precision Expectation |
|-------------|-------------------|----------------------|
| Systematic review | >95% | 5-20% |
| Scoping review | >90% | 10-30% |
| Rapid review | >80% | 20-50% |
| Clinical question | 60-80% | 40-70% |

---

## 8. Saving and Documenting Searches

### PubMed My NCBI

1. Create a free NCBI account at https://www.ncbi.nlm.nih.gov/myncbi/
2. Run your search in PubMed
3. Click "Save" under the search bar
4. Name your search and save to My NCBI
5. Set up email alerts for new results (useful during review period)

### Documentation Requirements (PRISMA-S)

For systematic reviews, document ALL of the following:

```markdown
## Search Documentation Template

**Database**: PubMed/MEDLINE via PubMed.gov
**Date of Search**: YYYY-MM-DD
**Date Range Searched**: YYYY-MM-DD to YYYY-MM-DD
**Searcher**: [Name, credentials]
**Peer Reviewer**: [Name, credentials]

### Search Strategy

Line 1: "Concept A MeSH"[MeSH] OR "concept a"[tiab]
Line 2: "Concept B MeSH"[MeSH] OR "concept b"[tiab]
Line 3: #1 AND #2
Line 4: #3 AND Humans[MeSH] AND English[la]

### Results

Total records retrieved: [N]
After deduplication: [N]
```

### Version Control

- Save each iteration of your search strategy
- Note the date, number of results, and changes made
- Use a spreadsheet or version-controlled document
- Record why changes were made between iterations

---

## 9. Other Database Search Syntax Differences

### Scopus

```
# Field codes differ from PubMed
TITLE-ABS-KEY("machine learning")          # equivalent to [tiab]
TITLE("machine learning")                   # equivalent to [ti]
AUTH("Smith J")                              # author
PUBYEAR > 2019                              # date filter
DOCTYPE(ar)                                  # article type
LANGUAGE(english)                            # language

# Example query
TITLE-ABS-KEY("artificial intelligence" OR "machine learning")
AND TITLE-ABS-KEY("diabetes")
AND PUBYEAR > 2019
AND DOCTYPE(ar)
AND LANGUAGE(english)
```

### CINAHL (via EBSCOhost)

```
# Uses CINAHL Headings (similar to MeSH but different)
(MH "Artificial Intelligence+")             # + means explode
(MH "Diabetes Mellitus, Type 2")
TI "machine learning" OR AB "machine learning"  # title/abstract
PT "Journal Article"                         # publication type

# Limiters available via interface:
# Published Date, Language, Age Groups, Human
```

### Cochrane Library (CENTRAL)

```
# Uses MeSH terms similar to PubMed
#1 MeSH descriptor: [Artificial Intelligence] explode all trees
#2 "machine learning":ti,ab,kw
#3 "deep learning":ti,ab,kw
#4 #1 OR #2 OR #3
#5 MeSH descriptor: [Diabetes Mellitus, Type 2] explode all trees
#6 "type 2 diabetes":ti,ab,kw
#7 #5 OR #6
#8 #4 AND #7
```

### Web of Science

```
# Field tags
TS=("machine learning")     # Topic (title, abstract, keywords)
TI=("machine learning")     # Title only
AU=("Smith J")              # Author
PY=(2020-2025)              # Publication year
DT=(Article)                # Document type
LA=(English)                # Language

# Example
TS=("artificial intelligence" OR "machine learning")
AND TS=("diabetes mellitus")
AND PY=(2020-2025)
AND LA=(English)
```

### Embase (via Ovid)

```
# Uses Emtree terms (similar to but different from MeSH)
exp artificial intelligence/        # exploded Emtree term
"machine learning".ti,ab.          # title/abstract
limit to (english language and yr="2020-2025")

# Embase includes conference abstracts by default
# Consider excluding if needed:
NOT conference abstract.pt.
```

### Translation Table

| Concept | PubMed | Scopus | CINAHL | Cochrane |
|---------|--------|--------|--------|----------|
| Controlled vocabulary | [MeSH] | N/A (use keywords) | (MH "Term+") | MeSH descriptor |
| Title/Abstract | [tiab] | TITLE-ABS-KEY() | TI/AB | :ti,ab,kw |
| Truncation | * | * | * | * |
| Proximity | N/A | W/n, PRE/n | Nn | NEAR/n |
| Explode | Default | N/A | + after term | explode all trees |

---

## 10. PRESS Checklist for Peer Review of Search Strategies

The **Peer Review of Electronic Search Strategies (PRESS)** checklist ensures search quality.

### PRESS 2015 Checklist Items

1. **Translation of the research question**
   - Does the search strategy match the research question?
   - Are all PICO/PEO elements represented?
   - Is the logic (AND/OR/NOT) correct?

2. **Boolean and proximity operators**
   - Are Boolean operators used correctly?
   - Is grouping with parentheses correct?
   - Are proximity operators appropriate for the database?

3. **Subject headings (MeSH/Emtree)**
   - Are subject headings relevant and appropriate?
   - Is explosion/non-explosion justified?
   - Are Major Topic restrictions appropriate?
   - Are subheadings (qualifiers) used correctly?

4. **Text word searching (free text)**
   - Are all relevant synonyms included?
   - Are spelling variants covered (British/American)?
   - Is truncation used appropriately?
   - Are phrase searches used where needed?

5. **Spelling, syntax, and line numbers**
   - Is the syntax correct for the database?
   - Are line numbers referenced correctly?
   - Are there any typos?

6. **Limits and filters**
   - Are limits (language, date, species) justified?
   - Could limits exclude relevant studies?
   - Are validated search filters used where available?

### Peer Review Process

1. Send your complete search strategy to a librarian or information specialist
2. Include your research question and inclusion/exclusion criteria
3. Allow 1-2 weeks for review
4. Document the reviewer, date, and changes made
5. Re-run the search after incorporating feedback

### PRESS Evidence-Based Checklist Reference

McGowan J, Sampson M, Salzwedel DM, et al. PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. J Clin Epidemiol. 2016;75:40-46.

---

## Quick Reference: Search Building Workflow

```
1. Define research question (PICO/PEO)
         ↓
2. Identify key concepts (2-4 concepts)
         ↓
3. Find MeSH terms for each concept
         ↓
4. List free-text synonyms for each concept
         ↓
5. Build concept table (MeSH + free text per concept)
         ↓
6. Combine within concepts with OR
         ↓
7. Combine between concepts with AND
         ↓
8. Add appropriate filters/limits
         ↓
9. Run search, review first 50-100 results
         ↓
10. Iterate: add missing terms, adjust specificity
         ↓
11. Peer review (PRESS checklist)
         ↓
12. Translate to other databases
         ↓
13. Document everything (PRISMA-S compliant)
```

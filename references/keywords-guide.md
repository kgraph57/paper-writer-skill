# Keywords Selection Guide

## Overview

Keywords determine discoverability. Poorly chosen keywords mean fewer readers find your paper. This guide covers selection strategy, MeSH terms, and journal-specific requirements.

---

## General Rules

1. Typically 3-10 keywords (check journal requirements)
2. Do not repeat words already in the title
3. Include both specific and broader terms
4. Use established terminology (MeSH, EMTREE)
5. Include methodological terms if relevant (e.g., "systematic review", "machine learning")
6. Consider what readers would search to find your paper

---

## Keyword Selection Strategy

### Step 1: Extract Core Concepts

From your research question, identify:
- Disease/condition
- Population
- Intervention/exposure
- Outcome
- Method/study design

Example: "Does AI-assisted screening improve early detection of diabetic retinopathy in primary care?"
- Disease: diabetic retinopathy
- Population: primary care patients
- Intervention: artificial intelligence, screening
- Outcome: early detection, diagnostic accuracy
- Method: deep learning

### Step 2: Map to MeSH Terms

Search the MeSH database for each concept:

```
URL: https://meshb.nlm.nih.gov/search
```

For each concept, find:
- The preferred MeSH term (use this)
- Entry terms (synonyms indexed under the MeSH term)
- Tree number (hierarchical position -- helps identify broader/narrower terms)

Example mapping:
| Concept | MeSH Term | Tree Number |
|---------|-----------|-------------|
| diabetic retinopathy | Diabetic Retinopathy | C11.768.590.200 |
| artificial intelligence | Artificial Intelligence | L01.224.050 |
| screening | Mass Screening | N06.850.520.450 |
| deep learning | Deep Learning | L01.224.050.375.210 |
| primary care | Primary Health Care | N04.590.233.727 |

### Step 3: Select Final Keywords

Choose 5-8 keywords that:
- Cover all major concepts in the paper
- Mix specific and broader terms
- Include at least 2-3 MeSH terms
- Add 1-2 free-text terms not covered by MeSH (e.g., emerging technology names)

Example final keywords:
```
diabetic retinopathy; artificial intelligence; deep learning;
mass screening; primary health care; diagnostic accuracy;
convolutional neural network
```

---

## MeSH vs. Free-Text Keywords

| Type | When to Use | Example |
|------|-------------|---------|
| MeSH terms | Always include when available | "Diabetic Retinopathy" |
| Free-text | For concepts not yet in MeSH | "large language model" |
| Subheadings | When specificity needed | "Diabetic Retinopathy/diagnosis" |
| Combination | For compound concepts | "artificial intelligence" + "diagnosis" |

Note: MeSH terms are updated annually. Newer concepts (e.g., specific AI architectures, new drugs) may not have MeSH terms yet. Use free-text for these.

---

## Journal-Specific Requirements

| Journal Type | Typical Requirement |
|-------------|-------------------|
| PubMed-indexed | MeSH terms preferred |
| Elsevier journals | "Use MeSH terms where possible" |
| BMJ family | 3-10 keywords |
| JAMA Network | Uses MeSH-based subject headings |
| Nature portfolio | Up to 6 keywords |
| Springer journals | 4-6 keywords |
| JMIR | 5-10 keywords, MeSH preferred |
| Japanese journals | Japanese + English keywords (both) |

---

## Japanese Keywords

For Japanese journals requiring bilingual keywords:

```
Keywords: diabetic retinopathy, artificial intelligence, screening
キーワード：糖尿病網膜症、人工知能、スクリーニング
```

Rules:
- Direct MeSH-to-Japanese mapping exists in the MeSH Japanese translation
- URL: https://meshb.nlm.nih.gov/ (select Japanese display)
- Keep the same number and order in both languages
- Use established Japanese medical terminology

---

## Common Mistakes

1. Using words that already appear in the title (redundant)
2. Using overly broad terms only ("medicine", "treatment")
3. Using overly specific terms only (too narrow for discovery)
4. Using abbreviations as keywords (spell out: "artificial intelligence" not "AI")
5. Including brand names unless the paper is specifically about that product
6. Too few keywords (missing discoverability)
7. Not checking if MeSH terms exist for your concepts

---

## Keywords Checklist

- [ ] 3-10 keywords selected (check journal limit)
- [ ] No duplication with title words
- [ ] MeSH terms used where available
- [ ] Mix of specific and broader terms
- [ ] Methodological keyword included if relevant
- [ ] Disease/condition keyword included
- [ ] Population keyword included
- [ ] All keywords are terms a reader would actually search
- [ ] Japanese keywords match English keywords (if bilingual)
- [ ] No abbreviations used as keywords

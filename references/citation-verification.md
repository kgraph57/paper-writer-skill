# Citation Verification Workflow

## Overview

AI language models frequently fabricate ("hallucinate") citations. Every AI-generated reference must be verified before inclusion in a manuscript. This guide provides a systematic workflow for verification.

**Rule: Never trust an AI-generated citation without independent verification.**

---

## Common AI Citation Fabrication Patterns

Be alert to these red flags:

| Pattern | Example | Detection |
|---------|---------|-----------|
| **Plausible but nonexistent paper** | Real author + real journal + fabricated title | Search PubMed by title |
| **Wrong author combination** | Author A's topic + Author B's name | Verify author list matches |
| **Incorrect year** | Correct paper but wrong publication year | Cross-check with DOI |
| **Fabricated DOI** | DOI format is correct but resolves to nothing | Check doi.org resolution |
| **Journal mismatch** | Real paper published in different journal | Verify journal name |
| **Volume/page errors** | Correct paper but wrong bibliographic details | Check against database record |
| **Merged citations** | Elements from 2+ real papers combined into one | Search each element separately |
| **Retracted papers cited as valid** | Paper exists but was retracted | Check Retraction Watch |
| **Preprint cited as published** | Paper is on arXiv/medRxiv but not peer-reviewed | Verify publication status |
| **Outdated version cited** | Guideline or meta-analysis has been updated | Check for latest version |

---

## Step-by-Step Verification Process

### Step 1: Title Search (Primary Check)

Search the exact title in multiple databases:

#### PubMed
```
URL: https://pubmed.ncbi.nlm.nih.gov/
Search: "[exact paper title]"
Use quotes for exact match
```

#### Google Scholar
```
URL: https://scholar.google.com/
Search: allintitle: [key words from title]
Or use quotes: "[exact title]"
```

#### Semantic Scholar
```
URL: https://www.semanticscholar.org/
Search: "[exact paper title]"
Good for CS/AI papers not in PubMed
```

**If title not found**: The paper likely does not exist. Do NOT proceed to use it.

### Step 2: DOI Verification

If a DOI is provided:

```
# Direct resolution
https://doi.org/[DOI]

# CrossRef API lookup
https://api.crossref.org/works/[DOI]

# Example:
https://doi.org/10.1001/jama.2023.12345
https://api.crossref.org/works/10.1001/jama.2023.12345
```

**Check**: Does the resolved page match the claimed title, authors, and journal?

### Step 3: PMID Verification

If a PMID is provided:

```
# Direct PubMed link
https://pubmed.ncbi.nlm.nih.gov/[PMID]/

# PubMed E-utilities API
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=[PMID]&retmode=json

# Example:
https://pubmed.ncbi.nlm.nih.gov/37654321/
```

**Check**: Does the PMID correspond to the claimed paper?

### Step 4: Author Verification

Cross-reference the author list:

```
# PubMed author search
[LastName FirstInitial][au]
Example: Smith JA[au] AND machine learning[tiab]

# ORCID lookup (if available)
https://orcid.org/[ORCID-ID]

# Google Scholar author profile
Search author name → check their publication list
```

**Check**: Has this author actually published in this topic area?

### Step 5: Journal Verification

Confirm the journal is real and the paper appeared there:

```
# NLM Catalog (for journal existence)
https://www.ncbi.nlm.nih.gov/nlmcatalog/

# Journal website table of contents
Check the specific volume/issue for the paper
```

### Step 6: Content Verification

Even if the paper exists, verify that:
- [ ] The claims attributed to the paper are actually in the paper
- [ ] The data/statistics cited match what the paper reports
- [ ] The conclusions drawn are consistent with the paper's actual findings
- [ ] The paper is not being cited out of context

---

## Batch Verification Approach

For manuscripts with many references (20+), use this efficient workflow:

### Phase 1: Rapid Triage (2-3 min per reference)

```
For each reference:
1. Copy exact title
2. Paste into PubMed search (with quotes)
3. Mark as: ✅ Found | ❌ Not found | ⚠️ Partial match
```

### Phase 2: Detail Check (Found references)

```
For each ✅ Found reference:
1. Compare: authors, year, journal, volume, pages
2. Verify DOI resolves correctly
3. Mark as: ✅ Verified | ⚠️ Details wrong
```

### Phase 3: Resolution (Problem references)

```
For each ❌ or ⚠️ reference:
- ❌ Not found → Find replacement or remove
- ⚠️ Partial match → Correct bibliographic details
- ⚠️ Details wrong → Update with correct information
```

### Batch Verification Using CrossRef API

For programmatic batch checking:

```bash
#!/bin/bash
# Verify a list of DOIs against CrossRef

while IFS= read -r doi; do
  response=$(curl -s "https://api.crossref.org/works/${doi}" 2>/dev/null)
  status=$(echo "$response" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    title = data['message']['title'][0] if data['message']['title'] else 'NO TITLE'
    print(f'OK: {title}')
except:
    print('FAILED: DOI not found')
" 2>/dev/null)
  echo "${doi} -> ${status}"
done < doi_list.txt
```

### PubMed E-utilities Batch Search

```bash
# Search PubMed for a title
TITLE="machine learning diagnosis cancer"
ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${TITLE}'))")
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${ENCODED}[Title]&retmode=json"
```

---

## Handling Specific Scenarios

### Scenario 1: Paper Exists but Details Are Wrong

**Symptoms**: Title matches, but author order, year, journal, or volume/pages differ.

**Resolution**:
1. Use the PubMed/CrossRef record as the authoritative source
2. Update all bibliographic fields to match the database record
3. Double-check that the paper's content still supports the citation context

### Scenario 2: Paper Does Not Exist

**Symptoms**: No results for title search in any database.

**Resolution**:
1. Search for the topic described in the fabricated title
2. Find a real paper that makes the same point
3. Read the real paper to confirm it supports the claim
4. Replace the fabricated citation with the verified one
5. Update the in-text citation context if needed

### Scenario 3: Paper Is Retracted

**Symptoms**: Paper found but marked as retracted.

**Resolution**:
1. Check Retraction Watch database: https://retractionwatch.com/retracted-coronavirus-covid-19-papers/
2. Check PubMed for retraction notice (will show "Retracted" label)
3. Read the retraction notice to understand why
4. **Do NOT cite retracted papers** unless discussing the retraction itself
5. Find alternative supporting evidence
6. If citing to discuss the retraction: cite both the original paper AND the retraction notice

### Scenario 4: Preprint Not Yet Published

**Symptoms**: Found on bioRxiv/medRxiv/arXiv but not in a peer-reviewed journal.

**Resolution**:
1. Check if a published version now exists (search title in PubMed)
2. If published: cite the published version, not the preprint
3. If still preprint only: cite as preprint with clear labeling
   - Format: "Author et al. Title. medRxiv. Year. doi: [preprint DOI]. Preprint."
4. Consider whether the journal accepts preprint citations
5. Note: Some journals restrict or prohibit preprint citations

### Scenario 5: Multiple Versions Exist

**Symptoms**: Paper has been updated, corrected, or republished.

**Resolution**:
1. Always cite the most recent/final version
2. For Cochrane reviews: cite the latest update
3. For clinical guidelines: cite the current version
4. Note the version/edition if relevant

---

## Retraction Watch Database Usage

### Online Database
```
URL: http://retractiondatabase.org/
Search by: author, title, DOI, PubMed ID, or journal
```

### What to Check
- Is the paper retracted?
- Is the paper under investigation (expression of concern)?
- What was the reason for retraction?
  - Data fabrication/falsification
  - Plagiarism
  - Duplicate publication
  - Authorship disputes
  - Honest errors

### PubMed Retraction Labels
PubMed marks retracted articles with:
- "Retracted Publication" on the article record
- Linked retraction notice
- Search filter: `retracted publication[pt]`

---

## Verification Checklist Template

Use this for each reference in your manuscript:

```markdown
## Reference #[N]

- [ ] **Title verified**: Found in PubMed / Google Scholar / Scopus
- [ ] **Authors verified**: Author list matches database record
- [ ] **Year verified**: Publication year is correct
- [ ] **Journal verified**: Published in the stated journal
- [ ] **Volume/Issue/Pages verified**: Bibliographic details correct
- [ ] **DOI verified**: DOI resolves to the correct paper
- [ ] **Not retracted**: Checked Retraction Watch / PubMed
- [ ] **Content verified**: Paper actually supports the claim made
- [ ] **Citation context accurate**: Not cited out of context

Status: ✅ Verified / ⚠️ Needs correction / ❌ Replace
Notes: [any discrepancies found]
```

---

## Tools Summary

| Tool | URL | Best For |
|------|-----|----------|
| PubMed | https://pubmed.ncbi.nlm.nih.gov/ | Biomedical literature (primary) |
| CrossRef API | https://api.crossref.org/works/ | DOI verification, metadata |
| Google Scholar | https://scholar.google.com/ | Broad search, citation counts |
| Semantic Scholar | https://www.semanticscholar.org/ | AI/CS papers, API access |
| Retraction Watch | http://retractiondatabase.org/ | Retraction checking |
| ORCID | https://orcid.org/ | Author identity verification |
| PubMed E-utilities | https://eutils.ncbi.nlm.nih.gov/ | Programmatic PubMed access |
| Scopus | https://www.scopus.com/ | Citation metrics, author profiles |
| Web of Science | https://www.webofscience.com/ | Citation tracking, h-index |
| doi.org | https://doi.org/ | DOI resolution |
| NLM Catalog | https://www.ncbi.nlm.nih.gov/nlmcatalog/ | Journal verification |

---

## Quick Decision Tree

```
AI generated a citation
├── Search title in PubMed (exact match)
│   ├── FOUND → Verify all details (author, year, journal, DOI)
│   │   ├── All correct → ✅ Use citation (check content too)
│   │   ├── Minor errors → ⚠️ Correct details from database
│   │   └── Major discrepancies → ⚠️ Re-read paper, may be wrong citation
│   └── NOT FOUND → Search Google Scholar
│       ├── FOUND → Paper may be non-biomedical; verify details
│       └── NOT FOUND → ❌ Citation is fabricated
│           └── Find real paper on the same topic → Replace
└── DOI provided?
    └── Resolve at doi.org
        ├── Resolves → Check if it matches claimed paper
        └── Does not resolve → ❌ DOI is fabricated
```

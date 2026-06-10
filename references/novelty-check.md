# Novelty Check — Phase −1 Guardrail

> **Placement:** Run once per surviving candidate question, after `templates/research-question.md`
> generates and scores candidates and **before** `templates/study-design.md` is opened.
> Output is the Novelty Assessment record (template at the end of this file).
>
> **Purpose:** The cheapest experiment is the one you don't run. Classify each gap
> honestly against the live literature. This is the direct implementation of the
> §5.2 guardrail in `references/ai-for-science-model.md`.

---

## 🤖 The Sakana v2 Anti-Pattern (Read This First)

Sakana AI Scientist v2 rated its own output "novel" when independent review found
the same territory already mapped. The failure was structural: the system searched
only what it already knew, accepted its own framing of the gap, and had no
adversarial step that could contradict it.

**The corrective is not asking AI to try harder. It is running a live query against
real literature databases the AI cannot hallucinate, then classifying the verdict
honestly — including the verdict "already answered, kill this."**

A human must read the top 5–10 closest papers and make the final call (💡 IDEA gate).
AI executes the sweep; the human owns the verdict.

---

## The Four Novelty Verdicts

| Verdict | Meaning | Decision |
|---------|---------|----------|
| **GENUINELY NOVEL** | No published answer exists; no ongoing trial/SR covers it | Proceed to study design |
| **INCREMENTAL** | Answered in a narrower population, older dataset, or lower-evidence design; your study adds meaningful precision | Proceed — but the differentiator must be explicit in the Introduction and pre-registration |
| **ALREADY ANSWERED** | A well-powered RCT, SR, or current clinical guideline settles the question | Kill or reframe. State *why* the existing evidence does not answer your specific version |
| **CONTESTED** | Conflicting high-quality evidence exists; the field has no consensus | Strong warrant to study — design to adjudicate, not to add a vote |

---

## Sweep Procedure

### Step 0 — Build the Query

Convert the candidate question from PICO elements (see `references/pubmed-query-builder.md`):

```
Population:    [MeSH term] OR [free text synonym]
Intervention:  [MeSH term] OR [free text synonym]
Comparison:    (if applicable)
Outcome:       [primary outcome term]

Combine: (P) AND (I) AND (O)
Add date filter: 2015[PDAT] : 3000[PDAT]  ← last ~10 years as default
Add study-type filter if desired: systematic[sb] OR meta-analysis[pt]
```

Run the full combined query AND a loose version (drop the Outcome term) to
catch adjacent work. Write down the exact query string — it goes into the
Novelty Assessment record.

---

### Step 1 — PubMed MCP (Primary Biomedical Sweep)

PubMed is the primary database for clinical and biomedical questions.
Use the MCP tools directly:

**Initial search:**
```
mcp__claude_ai_PubMed__search_articles
  query: "<your PICO query>"
  max_results: 20
```

**Check each result's metadata:**
```
mcp__claude_ai_PubMed__get_article_metadata
  pmid: "<PMID>"
```

**Expand from the closest paper (seed expansion):**
```
mcp__claude_ai_PubMed__find_related_articles
  pmid: "<PMID of closest paper>"
  max_results: 15
```
Seed expansion catches papers that share citation network topology but may not
share your exact terminology. Run it on the top 2–3 closest papers.

**Retrieve full text if key paper needs close reading:**
```
mcp__claude_ai_PubMed__get_full_text_article
  pmid: "<PMID>"
```

**Convert IDs if you have a DOI but need a PMID:**
```
mcp__claude_ai_PubMed__convert_article_ids
  ids: ["10.1001/..."]
  id_type: "doi"
```

**Look up a specific citation by journal/year/author when suspected duplicate:**
```
mcp__claude_ai_PubMed__lookup_article_by_citation
  journal: "Pediatrics"
  year: 2022
  first_author: "Smith"
```

Record: total hits, top 5–10 papers (PMID + title + year), and whether any
directly answer the question.

---

### Step 2 — Systematic Review & Protocol Registries

These catch work that would make your study redundant *before* it even publishes.

**Cochrane Library** — complete SRs:
```
https://www.cochranelibrary.com/search?q=<your+terms>
```
Fetch via WebFetch or `mcp__firecrawl__firecrawl_scrape`.

**PROSPERO** — registered SR protocols (including in-progress):
```
https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=...
https://www.crd.york.ac.uk/PROSPERO/search/SearchSummary.php?SuppliedID=<query>
```
If a PROSPERO record covers your exact question and is active, your independent
SR would be a duplicate — **kill or contact the team**.

**Epistemonikos** (SR synthesis across Cochrane + 50 databases):
```
https://www.epistemonikos.org/en/search?q=<query>
```

---

### Step 3 — Trial Registries (Ongoing Primary Research)

If an ongoing RCT or prospective study will answer the question in 2–3 years,
a new observational study may be pre-empted.

| Registry | URL | Scope |
|----------|-----|-------|
| ClinicalTrials.gov | `https://clinicaltrials.gov/search?term=<query>` | US + international |
| UMIN-CTR | `https://upload.umin.ac.jp/cgi-bin/ctr/ctr_view_j.cgi` | Japan |
| jRCT | `https://jrct.niph.go.jp/en-latest-detail/<id>` | Japan (new) |
| ISRCTN | `https://www.isrctn.com/search?q=<query>` | UK + global |

Filter for: Status = Recruiting OR Active, Not Recruiting. If a large RCT
has 3 years of follow-up left, plan to submit yours as a pilot/exploratory
framing, not a definitive trial.

---

### Step 4 — Broad Literature (OpenAlex, Europe PMC, Semantic Scholar)

For coverage beyond PubMed (non-indexed journals, preprints, citation graph):

**OpenAlex** (no API key required):
```
https://api.openalex.org/works?search=<url-encoded-query>&filter=publication_year:2015-&sort=cited_by_count:desc&per_page=20
```
Fetch via WebFetch. Sort by `cited_by_count:desc` to surface the most
influential work. A highly-cited paper directly answering your question is a
near-certain "ALREADY ANSWERED" signal.

**Europe PMC** (preprints + full-text search):
```
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<query>&format=json&resultType=core&pageSize=20
```
Catches medRxiv/bioRxiv preprints before PubMed indexes them.

**Semantic Scholar** (citation graph, influential-citation count):
```
https://api.semanticscholar.org/graph/v1/paper/search?query=<query>&fields=title,authors,year,citationCount,influentialCitationCount&limit=20
```
`influentialCitationCount` flags papers that methodologically shaped the field —
if one of these directly answers your question, that is a strong ALREADY ANSWERED.

**NotebookLM (optional — corpus grounding):**
If you have collected PDFs of relevant papers, use NotebookLM MCP
(`mcp__notebooklm-mcp__notebook_query`) to query across the local corpus.
Best for deep reading across 10–30 pre-loaded papers.

---

### Step 5 — Non-English & Adjacent Field Check

The honest-novelty checklist below governs this step. Minimum:
- Search with at least one non-English term if the question is clinically
  active in Japan (e.g., UMIN-CTR search in Japanese characters).
- Run one adjacent-field query (e.g., if your question is pediatric,
  run the adult version to see if the adult answer translates).

---

## Tools Summary

| Tool | Endpoint / MCP | Best For |
|------|---------------|---------|
| PubMed MCP | `mcp__claude_ai_PubMed__search_articles` | Primary biomedical sweep |
| PubMed related papers | `mcp__claude_ai_PubMed__find_related_articles` | Citation-network expansion |
| PubMed full text | `mcp__claude_ai_PubMed__get_full_text_article` | Close reading of key papers |
| PubMed metadata | `mcp__claude_ai_PubMed__get_article_metadata` | Confirm study type, date, journal |
| PubMed ID convert | `mcp__claude_ai_PubMed__convert_article_ids` | DOI ↔ PMID reconciliation |
| PubMed citation lookup | `mcp__claude_ai_PubMed__lookup_article_by_citation` | Check suspected duplicate |
| OpenAlex API | `https://api.openalex.org/works?search=…` | Broad coverage, citation count sort |
| Europe PMC API | `https://www.ebi.ac.uk/europepmc/…` | Preprints + full-text search |
| Semantic Scholar API | `https://api.semanticscholar.org/graph/v1/paper/search?…` | Citation graph, influential papers |
| Cochrane Library | `https://www.cochranelibrary.com/search?q=…` | Completed systematic reviews |
| PROSPERO | `https://www.crd.york.ac.uk/PROSPERO/…` | In-progress SR registrations |
| Epistemonikos | `https://www.epistemonikos.org/en/search?q=…` | SR synthesis across 50 databases |
| ClinicalTrials.gov | `https://clinicaltrials.gov/search?term=…` | Ongoing trials (US + international) |
| UMIN-CTR | `https://upload.umin.ac.jp/cgi-bin/ctr/…` | Ongoing trials (Japan) |
| jRCT | `https://jrct.niph.go.jp/…` | Ongoing trials (Japan, new system) |
| NotebookLM MCP | `mcp__notebooklm-mcp__notebook_query` | Local PDF corpus grounding |

Fetch non-MCP endpoints via WebFetch, `mcp__firecrawl__firecrawl_scrape`, or
`mcp__tavily__tavily_search` as available.

---

## Honest-Novelty Checklist

Before assigning a GENUINELY NOVEL verdict, confirm you can check every box:

- [ ] Searched with ≥2 synonym/alternative term sets (not just your preferred phrasing)
- [ ] Searched non-English sources if clinically active in Japan (UMIN-CTR; J-STAGE via WebFetch)
- [ ] Searched preprint servers (Europe PMC catches medRxiv/bioRxiv)
- [ ] Ran seed expansion (`find_related_articles`) on the top 2–3 closest papers
- [ ] Checked for an ongoing trial that will answer the same question (ClinicalTrials.gov, UMIN, jRCT)
- [ ] Checked PROSPERO for a registered SR in progress
- [ ] Ran the adjacent-field version of the query (e.g., adult analogue of a pediatric question)
- [ ] Sorted OpenAlex by `cited_by_count:desc` — no high-citation paper directly answers this
- [ ] The "gap" is a genuine absence of evidence, not an unsearched corner of the literature
- [ ] A clinician-expert reviewed the top papers and agrees the question is unanswered

If any box is unchecked, the verdict cannot be GENUINELY NOVEL.

---

## Decision Tree

```
Candidate research question
         │
         ▼
Run PubMed MCP sweep (Steps 1–2)
         │
         ├── Cochrane SR / PROSPERO active review already covers this?
         │        YES ──► ALREADY ANSWERED → Kill or contact SR team
         │        NO  ──► continue
         │
         ▼
Top 5–10 papers found. Does any directly answer your primary endpoint
in your target population at adequate power?
         │
         ├── YES, one or more well-powered RCT/SR/guideline
         │        ──► ALREADY ANSWERED → Kill
         │            OR reframe: "why doesn't the existing answer
         │            apply to our population/setting/time?" — if
         │            compelling, relabel INCREMENTAL and proceed
         │
         ├── YES, but lower-quality evidence only (observational,
         │   small N, older dataset, different subgroup)
         │        ──► INCREMENTAL → Proceed, explicit differentiator required
         │
         ├── YES, and conflicting results across studies
         │        ──► CONTESTED → Proceed, design to adjudicate
         │
         └── NO papers close to the question
                  │
                  ▼
         Honest-novelty checklist — all 10 boxes checked?
                  │
                  ├── NO ──► Complete missing steps, re-run sweep
                  └── YES ──► GENUINELY NOVEL → Proceed to study design
```

---

## Novelty Assessment Record (Output Template)

Fill one record per candidate question that passes initial FINER scoring.

```markdown
## Novelty Assessment

**Date:** YYYY-MM-DD
**Question:** [Exact PICO-formatted question from research-question.md]
**Assessed by:** [Name] (human) + AI sweep

### Query Used
- PubMed string: `[exact query]`
- OpenAlex string: `[exact query]`
- Date bounds: [YYYY]–present
- Synonyms tested: [list]

### Registry Check
- PROSPERO: [active protocol? Y/N — title if Y]
- ClinicalTrials.gov: [ongoing trial? Y/N — NCT if Y]
- UMIN/jRCT: [ongoing trial? Y/N — ID if Y]

### Top Existing Papers (5–10 closest)

| # | PMID / DOI | Title (short) | Year | Design | N | Verdict relevance |
|---|-----------|---------------|------|--------|---|------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| … | | | | | | |

### What They Leave Open
[2–4 sentences: what the existing literature does NOT answer that this question does]

### Honest-Novelty Checklist
- [ ] ≥2 synonym sets searched
- [ ] Non-English / J-STAGE searched (if applicable)
- [ ] Preprints checked (Europe PMC)
- [ ] Seed expansion run on top 2–3 papers
- [ ] Ongoing trials checked
- [ ] PROSPERO checked
- [ ] Adjacent-field query run
- [ ] OpenAlex sorted by citation count — no high-citation direct answer
- [ ] "Gap" confirmed as genuine, not just unsearched
- [ ] Clinician-expert sign-off

### Verdict
**[ ] GENUINELY NOVEL / [ ] INCREMENTAL / [ ] ALREADY ANSWERED / [ ] CONTESTED**

### Differentiator Statement
"Our study differs from the existing literature because…"
[1–2 sentences. This language goes directly into the Introduction.]

### Decision
**[ ] Proceed to study-design.md**
**[ ] Reframe — revised question:** [new question]
**[ ] Kill — reason:** [reason]

**Approved by (💡 IDEA gate):** ___________  Date: ___________
```

---

## Cross-References

- `references/ai-for-science-model.md` §5.2 — the guardrail this file implements
- `templates/research-question.md` — upstream: generates candidate questions
- `references/pubmed-query-builder.md` — how to build the PICO query in Step 0
- `templates/study-design.md` — downstream: opens only after NOVEL/INCREMENTAL/CONTESTED verdict
- `templates/preregistration.md` — the downstream lock that freezes the plan
- `references/adversarial-review.md` — the downstream red-team that stress-tests the claim

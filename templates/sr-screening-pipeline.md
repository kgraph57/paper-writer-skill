# Systematic Review Screening Pipeline (Execution)

> The connective tissue between the **protocol** (`sr-prospero.md`) and the
> **extraction form** (`sr-data-extraction.md`). This template covers the part
> the other SR templates assume is already done: actually *running* study
> selection and producing the numbers that fill the PRISMA flow diagram
> (`sr-prisma-flow.md`).
>
> **Scope:** identification → de-duplication → title/abstract screening →
> full-text screening → data extraction hand-off. Risk of bias (`sr-rob.md`),
> GRADE (`sr-grade.md`), and synthesis are downstream of this pipeline.
>
> **Hard rule:** an LLM is a *first-pass screener and one arm of a dual review*,
> never the sole arbiter. Every include/exclude decision is made by **two
> independent passes**, conflicts are reconciled, and the final call on
> disagreements belongs to the human reviewer. This is what Cochrane and PRISMA
> 2020 require, and it is what keeps the review defensible.

---

## 0. Prerequisites

Before running the pipeline, confirm these exist:

1. **A registered protocol** with eligibility criteria — see `sr-prospero.md`.
   The inclusion/exclusion criteria live in a single source of truth:
   `00_literature/protocol.md` (or the PROSPERO entry). The screeners read this
   file; they never invent criteria.
2. **A documented search** — see the parent skill's Phase 1
   (`00_literature/search-strategy.md`): databases, full query strings, search
   date, and per-database hit counts.
3. **Raw exports** from each database (RIS, NBIB/PubMed, BibTeX, or CSV) saved
   into `00_literature/screening/00_imported/`, one file per database so the
   identification counts are auditable.

If any of these are missing, stop and complete them first. Screening without a
registered protocol is not a systematic review.

---

## 1. Directory layout

This pipeline owns the `00_literature/screening/` subtree:

```
00_literature/
├── protocol.md                        # Eligibility criteria (single source of truth)
├── search-strategy.md                 # Databases, queries, date, per-DB counts
└── screening/
    ├── 00_imported/                    # Raw DB exports (READ-ONLY)
    │   ├── pubmed.nbib
    │   ├── scopus.ris
    │   ├── cochrane.ris
    │   └── ...
    ├── 01_deduplicated.csv             # ← scripts/sr-dedup.py
    ├── 02_title_abstract_screen.csv    # ← dual TA screening
    ├── 03_fulltext_screen.csv          # ← dual FT screening
    ├── 04_extraction_table.csv         # ← data extraction (overview row per study)
    ├── full-texts/                     # Retrieved PDFs (renamed by sr-pdf-link.py)
    ├── extraction/                     # One sr-data-extraction.md per included study
    └── counts/
        ├── identification.json         # ← scripts/sr-dedup.py
        └── prisma-summary.md           # ← scripts/sr-prisma-count.py
```

**Never modify `00_imported/`.** Every stage reads its input and writes a *new*
file. This makes the whole pipeline re-runnable and auditable.

---

## 2. Stage 1 — Import & De-duplicate (deterministic)

De-duplication is not a judgment call, so it runs as a script, not an agent.

```bash
python scripts/sr-dedup.py \
  --input 00_literature/screening/00_imported \
  --output 00_literature/screening/01_deduplicated.csv \
  --counts 00_literature/screening/counts/identification.json
```

**What it does:**
- Parses every `.ris`, `.nbib`, `.bib`, `.csv`, `.txt` in the input folder.
- Normalizes DOI and title; removes duplicates by **exact DOI**, then **exact
  normalized title**, then **fuzzy title match** (ratio ≥ 0.92, same year).
- Keeps the record with the most complete metadata; logs which record each
  duplicate collapsed into (`dup_of` column).
- Writes per-database counts + total identified + duplicates removed +
  records-after-dedup to `identification.json`.

**`01_deduplicated.csv` columns:**

| Column | Meaning |
|--------|---------|
| `record_id` | Stable ID assigned at import (e.g., `R0001`) |
| `doi` | Normalized DOI (lowercase, no URL prefix) |
| `pmid` | PubMed ID if present |
| `title`, `authors`, `year`, `journal` | Bibliographic fields |
| `abstract` | Abstract text (drives TA screening) |
| `source_db` | Originating database export |
| `dup_of` | Blank if kept; `record_id` it merged into if removed |

**Verify before proceeding:** open the CSV, spot-check 10 rows, and confirm the
duplicate count in `identification.json` is plausible (typically 20–40% overlap
across biomedical databases). If dedup over-merged distinct studies, loosen the
fuzzy threshold (`--fuzzy 0.95`) and re-run.

---

## 3. Stage 2 — Title/Abstract screening (DUAL, independent)

This is the first judgment stage. Run **two independent screening passes** that
cannot see each other's decisions, then reconcile.

### 3.1 Independent passes

Spawn two screeners (Agent tool, or team mode). Each receives **only**:
- `protocol.md` (eligibility criteria)
- `01_deduplicated.csv` (the `title` + `abstract` columns only)

and is instructed:

> You are an independent title/abstract screener for a systematic review.
> For every record, decide **include / exclude / unclear** against the
> eligibility criteria in protocol.md and nothing else.
> - "Include" = the abstract gives no reason to exclude (be permissive at TA
>   stage — when in doubt, keep it; the full-text stage will catch it).
> - "Exclude" = the abstract clearly violates at least one criterion. Name the
>   criterion.
> - "Unclear" = not enough information in the abstract → treat as include for
>   retrieval.
> Output one row per record: record_id, decision, one-line reason. Never read
> the other reviewer's output. Never guess beyond the abstract.

Pass A writes `reviewer1_*`, Pass B writes `reviewer2_*`. **They must not be
given each other's results** — that is what makes the agreement statistic
meaningful.

### 3.2 Reconcile

Merge both passes into `02_title_abstract_screen.csv`:

| Column | Meaning |
|--------|---------|
| `record_id`, `title`, `abstract` | Carried from Stage 1 |
| `reviewer1_decision`, `reviewer1_reason` | Pass A |
| `reviewer2_decision`, `reviewer2_reason` | Pass B |
| `conflict` | `Y` if the two decisions disagree (include vs exclude) |
| `consensus_decision` | Final include/exclude (see rule below) |
| `resolution_method` | `agreement` / `unclear→include` / `human` |

**Reconciliation rule (conservative, PRISMA-aligned):**
- Both **include** (or either "unclear") → `consensus = include`.
- Both **exclude** → `consensus = exclude`.
- **Conflict** (one include, one exclude) → `consensus = include` *provisionally*
  and flag `conflict = Y`. **The human reviewer resolves every conflict before
  Stage 3.** Do not let the model silently break ties on a hard exclude.

Compute Cohen's κ on reviewer1 vs reviewer2 (collapse "unclear" into "include").
Report it; κ < 0.6 means the criteria are ambiguous — revise `protocol.md` and
re-screen rather than pushing forward.

**Human gate:** present the conflict rows to the user. Only after they sign off
do the provisional consensus values become final.

---

## 4. Stage 3 — Full-text screening (DUAL, independent)

### 4.1 Retrieve and link PDFs

Place retrieved PDFs in `full-texts/`, then link them to records by DOI:

```bash
python scripts/sr-pdf-link.py \
  --pdfs 00_literature/screening/full-texts \
  --records 00_literature/screening/02_title_abstract_screen.csv \
  --include-only \
  --rename
```

This extracts the DOI from each PDF, joins it to the records, renames matched
PDFs to `{firstauthor}_{year}_{pmid-or-doislug}.pdf` (copies into
`full-texts/renamed/`, originals untouched), and reports:
- records marked include at TA with **no PDF found** → "reports not retrieved"
- PDFs that matched no record → flag for manual check.

Record the "reports not retrieved" count; it feeds the PRISMA diagram.

### 4.2 Independent passes

Run two independent full-text passes over the TA-included records that have a
PDF. Each screener receives `protocol.md` + the assigned PDFs and decides
**include / exclude**. At full text, every exclude **must** carry one PRISMA
exclusion-reason category:

`Wrong population` · `Wrong intervention/exposure` · `Wrong comparator` ·
`Wrong outcome` · `Wrong study design` · `Wrong setting` · `Language` ·
`Full text unavailable` · `Conference abstract only` · `Protocol/registry only`
· `Not original research` · `Duplicate`

(These match `sr-prisma-flow.md` so the figure's exclusion box fills cleanly.)

### 4.3 Reconcile

Write `03_fulltext_screen.csv`:

| Column | Meaning |
|--------|---------|
| `record_id`, `title`, `pdf_file` | Identity + linked PDF |
| `pdf_retrieved` | `Y`/`N` |
| `reviewer1_decision`, `reviewer1_reason` | Pass A (+ category if exclude) |
| `reviewer2_decision`, `reviewer2_reason` | Pass B (+ category if exclude) |
| `conflict` | `Y` if disagree |
| `consensus_decision` | include / exclude |
| `exclusion_reason_category` | PRISMA category (excludes only) |
| `resolution_method` | `agreement` / `human` |

**At full text, conflicts are NOT auto-resolved.** Every `conflict = Y` goes to
the human reviewer (or a third reviewer). Compute κ again and report it.

---

## 5. Stage 4 — Data extraction (hand-off)

For every record with `consensus_decision = include` at full text:

1. Create one `extraction/{record_id}.md` from `sr-data-extraction.md`.
2. Two reviewers extract independently (or one extracts + one verifies);
   resolve discrepancies per that form's instructions.
3. **No guessing.** Missing field → `NR` (not reported); inapplicable → `N/A`.
   Record page numbers for every extracted value.
4. Maintain `04_extraction_table.csv` as a one-row-per-study overview (study_id,
   design, country, n, population, intervention, comparator, primary outcome,
   effect estimate, RoB overall) for the characteristics-of-studies table.

Extraction then flows into RoB (`sr-rob.md`), GRADE (`sr-grade.md`), and
synthesis, all handled by the parent SR writing workflow (SKILL.md Phase 3-D).

---

## 6. Produce PRISMA numbers (deterministic)

Once the three stage CSVs exist, generate every number the flow diagram needs:

```bash
python scripts/sr-prisma-count.py \
  --identification 00_literature/screening/counts/identification.json \
  --ta 00_literature/screening/02_title_abstract_screen.csv \
  --ft 00_literature/screening/03_fulltext_screen.csv \
  --output 00_literature/screening/counts/prisma-summary.md
```

This emits `prisma-summary.md` with:
- All PRISMA 2020 flow counts (identified, duplicates, screened, TA-excluded,
  sought, not retrieved, assessed, FT-excluded by reason, included).
- Cohen's κ for TA and FT screening (inter-rater reliability for the Methods).
- The 8 internal-consistency checks from `sr-prisma-flow.md` (each PASS/FAIL).

Copy these numbers into the chosen `sr-prisma-flow.md` template, and the κ
values into the Methods "selection process" paragraph.

---

## 7. What goes where (no duplication)

| Need | Template / script |
|------|-------------------|
| Eligibility criteria, registration | `sr-prospero.md` |
| **Running screening, dual review, counts** | **this file + sr-dedup / sr-pdf-link / sr-prisma-count** |
| Per-study extraction form | `sr-data-extraction.md` |
| Risk of bias | `sr-rob.md` |
| Certainty of evidence | `sr-grade.md` |
| Flow figure | `sr-prisma-flow.md` |
| Methods/Results prose | SKILL.md Phase 3-D + `sr-outline.md` |

---

## 8. What not to do

- **Do not** let a single LLM pass be the final screening decision. Dual,
  independent, reconciled — always.
- **Do not** hide conflicts. Every disagreement is surfaced to the human.
- **Do not** auto-resolve full-text conflicts toward exclude. A wrongly excluded
  study is invisible; bias toward retrieval and let the human decide.
- **Do not** give a screener the other reviewer's output — it destroys the
  agreement statistic and reintroduces the context-clutter problem dual review
  exists to avoid.
- **Do not** extract data the paper does not report. `NR`, never a guess.
- **Do not** modify `00_imported/`. Every stage is additive and re-runnable.
- **Do not** run the pipeline before the protocol is registered.
```

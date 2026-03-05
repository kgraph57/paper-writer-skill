# Paper Writer Skill

A Claude Code skill for medical/scientific paper writing. Covers the entire manuscript lifecycle from literature search to submission, peer review response, and rejection handling.

> **日本語版はこちら → [README.ja.md](README.ja.md)**

## Overview

A **10-phase** pipeline that generates and manages IMRAD-format project directories with structured Markdown files, a literature matrix, and quality checklists.

```mermaid
graph LR
    P1[1. Literature Search] --> P2[2. Outline]
    P2 --> P25[2.5 Tables/Figures]
    P25 --> P3[3. Draft]
    P3 --> P4[4. Humanize]
    P4 --> P5[5. References]
    P5 --> P6[6. Quality Review]
    P6 --> P7[7. Pre-Submission]
    P7 --> P8["8. Revision ①"]
    P8 --> P9["9. Post-Acceptance"]
    P7 -.-> P10["10. Rejection → Resubmit"]
    P10 -.-> P1
```

## Architecture: Autonomous Stage-Gate System (v3.1)

Every phase is guarded by a quality gate. If the gate returns **FAIL**, the system automatically generates structured feedback, dispatches a fixer agent in `revision_mode`, and re-checks — up to 3 iterations before escalating to the user. No phase proceeds until its gate returns **PASS**.

```mermaid
flowchart TD
    subgraph "Per-Phase Loop (max 3 iterations)"
        A["Phase N Complete"] --> B{"Quality Gate"}
        B -->|PASS| C["→ Phase N+1"]
        B -->|FAIL iter < 3| D["Generate feedback.md"]
        D --> E["Fixer Agent\n(revision_mode)"]
        E --> B
        B -->|FAIL iter ≥ 3| F["⚠ Escalate to User"]
    end

    style B fill:#f9a825,stroke:#f57f17,color:#000
    style C fill:#66bb6a,stroke:#388e3c,color:#fff
    style F fill:#ef5350,stroke:#c62828,color:#fff
```

### 8 Quality Gates

```mermaid
flowchart LR
    subgraph "Phase 1"
        G1["📚 Literature\n≥10 papers\nAll DOIs valid"]
    end
    subgraph "Phase 2"
        G2["📋 Outline\nAll IMRAD sections\n≥2 citations mapped"]
    end
    subgraph "Phase 2.5"
        G25["📊 Tables/Figures\nAll designs complete\nJournal limits OK"]
    end
    subgraph "Phase 3"
        G3["✍️ Section Draft\nScore ≥80%\nMust Fix = 0"]
    end
    subgraph "Phase 4"
        G4["🔍 Humanize\nHigh-priority\nAI patterns = 0"]
    end
    subgraph "Phase 5"
        G5["📖 References\nFabrication = 0\nOrphan cites = 0"]
    end
    subgraph "Phase 6"
        G6["🔗 Cross-Section\nPASS or\nCONDITIONAL_PASS"]
    end
    subgraph "Phase 7"
        G7["📦 Submission\nAll docs ready\nWord count OK"]
    end

    G1 --> G2 --> G25 --> G3 --> G4 --> G5 --> G6 --> G7
```

### Team Mode: 7 Parallel Agents (v3.0)

Phases are parallelized with specialized agents running concurrently:

```mermaid
flowchart TB
    subgraph P1["Phase 1 — Literature Search (3 parallel)"]
        L1[PubMed Searcher]
        L2[Google Scholar Searcher]
        L3[Domain DB Searcher]
    end

    subgraph P3["Phase 3 — Drafting (grouped parallel)"]
        direction LR
        D1[Methods] --> D3[Intro]
        D2[Results] --> D4[Conclusion]
    end

    subgraph P4["Phase 4 — Humanize (up to 6 parallel)"]
        H1[Humanizer × N sections]
    end

    subgraph P6["Phase 6 — Quality Review"]
        R1[Section Reviewer ×N]
        R2[Quality Gate — opus]
    end

    L1 & L2 & L3 --> MERGE["Merge Matrix"]
    MERGE --> D1 & D2
    D3 & D4 --> H1
    H1 --> R1
    R1 --> R2
```

| Agent | Role | Model |
|-------|------|-------|
| `paper-lit-searcher` | Database-specific literature search | sonnet |
| `paper-table-figure-planner` | Table and figure design | sonnet |
| `paper-section-drafter` | Section drafting (parameterized) | sonnet |
| `paper-humanizer` | AI writing pattern removal | haiku |
| `paper-ref-builder` | Citation collection and verification | sonnet |
| `paper-section-reviewer` | Per-section quality check | sonnet |
| `paper-quality-gate` | Cross-section consistency + final verdict | opus |

## Supported Paper Types

| Type | Structure | Reporting Guideline |
|------|-----------|---------------------|
| **Original Article** | Full IMRAD | STROBE / CONSORT |
| **Case Report** | Intro / Case / Discussion | CARE |
| **Review Article** | Thematic sections | — |
| **Systematic Review** | PRISMA-compliant | PRISMA 2020 |
| **Letter / Short Communication** | Condensed IMRAD | Same as original |
| **Study Protocol** | SPIRIT-compliant | SPIRIT 2025 |

## Usage

### Invoke from Claude Code

```
/paper-writer
```

Or use natural language triggers:
- `write paper` / `start manuscript` / `research paper`
- `論文を書く` / `論文執筆` / `原稿作成`

### Project Setup

The skill prompts you for:

1. **Working title**
2. **Paper type** (one of the 6 types above)
3. **Target journal** (optional, recommended)
4. **Language** (English / Japanese / Both)
5. **Research question** (one sentence)
6. **Available data** (existing tables/figures)

When a target journal is specified, the skill automatically looks up word limits, citation style, abstract format, and other requirements.

## File Structure

```
paper-writer/
├── SKILL.md                           # Main workflow definition
├── CHANGELOG.md                       # Version history
├── README.md                          # This file
├── README.ja.md                       # Japanese documentation
│
├── templates/                         # 31 files — Section templates
│   ├── project-init.md                # Project initialization (Original Article)
│   ├── project-init-case.md           # Project initialization (Case Report)
│   ├── literature-matrix.md           # Literature comparison matrix
│   ├── methods.md                     # Methods writing guide
│   ├── results.md                     # Results writing guide
│   ├── introduction.md                # Introduction writing guide
│   ├── discussion.md                  # Discussion writing guide
│   ├── conclusion.md                  # Conclusion writing guide
│   ├── abstract.md                    # Abstract writing guide (Original Article)
│   ├── cover-letter.md                # Cover letter template
│   ├── submission-ready.md            # Pre-submission checklist
│   ├── case-report.md                 # Case presentation (CARE-compliant)
│   ├── case-introduction.md           # Case report introduction
│   ├── case-abstract.md               # Case report abstract (CARE format)
│   ├── review-article.md              # Review article structure guide
│   ├── sr-outline.md                  # Systematic review outline
│   ├── sr-data-extraction.md          # SR data extraction template
│   ├── sr-prisma-flow.md              # PRISMA flow diagram
│   ├── sr-grade.md                    # GRADE evidence assessment
│   ├── sr-rob.md                      # Risk of bias assessment
│   ├── sr-prospero.md                 # PROSPERO registration template
│   ├── response-to-reviewers.md       # Response to reviewers template
│   ├── revision-cover-letter.md       # Revision cover letter
│   ├── declarations.md                # Declarations (ethics, COI, funding, AI disclosure)
│   ├── graphical-abstract.md          # Graphical abstract guide
│   ├── title-page.md                  # Title page template
│   ├── highlights.md                  # Key points / highlights (JAMA, BMJ, etc.)
│   ├── limitations-guide.md           # Limitations section guide
│   ├── acknowledgments.md             # Acknowledgments template
│   ├── proof-correction.md            # Post-acceptance proof correction guide
│   ├── data-management.md             # Data management (raw/processed/analysis)
│   └── analysis-workflow.md           # Data analysis workflow guide
│
├── references/                        # 27 files — Reference materials
│   ├── imrad-guide.md                 # IMRAD structure and writing principles
│   ├── section-checklist.md           # Per-section quality checklist
│   ├── citation-guide.md              # Citation formatting and management
│   ├── citation-verification.md       # Citation verification guide
│   ├── reporting-guidelines.md        # Reporting guidelines summary
│   ├── reporting-guidelines-full.md   # 20+ reporting guidelines with checklists
│   ├── humanizer-academic.md          # AI writing detection (EN 18 + JP 13 patterns)
│   ├── statistical-reporting.md       # Statistical reporting guide
│   ├── statistical-reporting-full.md  # Extended SAMPL guide
│   ├── journal-selection.md           # Journal selection strategy
│   ├── pubmed-query-builder.md        # PubMed search query builder
│   ├── multilingual-guide.md          # Multilingual support guide
│   ├── coauthor-review.md             # Co-author review process
│   ├── ai-disclosure.md               # ICMJE 2023 AI disclosure guide
│   ├── tables-figures-guide.md        # Tables and figures creation guide
│   ├── keywords-guide.md              # Keywords and MeSH selection strategy
│   ├── supplementary-materials.md     # Supplementary materials strategy
│   ├── hook-compatibility.md          # Claude Code hook compatibility
│   ├── submission-portals.md          # Submission portal guide
│   ├── open-access-guide.md           # OA models, APCs, CC licenses
│   ├── clinical-trial-registration.md # Clinical trial registration guide
│   ├── abstract-formats.md            # Journal-specific abstract formats
│   ├── word-count-limits.md           # Word count limits by journal
│   ├── coi-detailed.md               # COI categories, CRediT taxonomy, ORCID
│   ├── desk-rejection-prevention.md   # Desk rejection prevention
│   ├── journal-reformatting.md        # Journal reformatting and cascading strategy
│   └── master-reference-list.md       # Master URL list (100+ links, 13 categories)
│
└── scripts/                           # 5 files — Utilities & Analysis
    ├── compile-manuscript.sh           # Compile sections into single manuscript
    ├── word-count.sh                  # Word count utility
    ├── forest-plot.py                 # Forest plot generator
    ├── table1.py                      # Table 1 generator (baseline characteristics)
    └── analysis-template.py           # Statistical analysis template (t-test, logistic, survival)
```

**Total: 66 files** (31 templates + 27 references + 5 scripts + SKILL.md + CHANGELOG.md + README.md)

## Workflow (10 Phases)

| Phase | Description | Key Operations |
|-------|-------------|----------------|
| **0** | Project Initialization | Journal requirements lookup, reporting guideline selection, directory generation, data management & analysis |
| **1** | Literature Search | PubMed/Google Scholar search, literature matrix creation |
| **2** | Outline | Paper skeleton design (user approval required) |
| **2.5** | Tables & Figures | Design tables/figures before writing prose |
| **3** | Drafting | Methods → Results → Intro P3 + Conclusion → Discussion → Intro P1-2 → Abstract → Title |
| **4** | Humanize | AI writing pattern removal (EN 18 + JP 13 patterns) |
| **5** | References | Citation formatting, deduplication, existence verification |
| **6** | Quality Review | Cross-section verification, reporting guideline compliance |
| **7** | Pre-Submission | Cover letter, title page, declarations, final checklist |
| **8** | Revision | Reviewer comment organization, response letter, revision implementation |
| **9** | Post-Acceptance | Proof review (24-72 hr), correction submission, post-publication tasks |
| **10** | Rejection & Resubmission | Assessment, quick reformat, cascading submission strategy |

## Reporting Guidelines (20+)

CONSORT 2025, STROBE, PRISMA 2020, CARE, STARD 2015, SQUIRE 2.0, SPIRIT 2025, TRIPOD+AI 2024, ARRIVE 2.0, CHEERS 2022, MOOSE, TREND, SRQR, COREQ, AGREE II, RECORD, STREGA, ENTREQ, PRISMA-ScR, GRADE

## Language Support

| Language | Coverage |
|----------|----------|
| **English** | All templates and guides, 18 AI writing detection patterns |
| **Japanese** | All templates bilingual (EN/JP), 13 AI writing detection patterns, である-style |

## AI Writing Detection (Humanizer)

A dedicated phase (Phase 4) to remove AI-generated writing patterns from academic manuscripts.

- **English**: 18 patterns (significance inflation, AI vocabulary, filler phrases, etc.)
- **Japanese**: 13 patterns (symbol overuse, rhythm monotony, academic-specific issues)
- Section-specific priority patterns
- Before/after examples included

## Master Reference List

`references/master-reference-list.md` contains 100+ URLs organized in 13 categories:

1. Author Guidelines (ICMJE, EQUATOR, etc.)
2. Reporting Guidelines (CONSORT, STROBE, etc.)
3. Ethics & Registration (ClinicalTrials.gov, UMIN, etc.)
4. Statistics (SAMPL, Cochrane, etc.)
5. Literature Databases (PubMed, Google Scholar, etc.)
6. Reference Managers (Zotero, Mendeley, etc.)
7. Submission Portals (ScholarOne, etc.)
8. AI Disclosure (ICMJE, Nature policies, etc.)
9. Open Access (DOAJ, Sherpa Romeo, etc.)
10. Writing Support (editing services, etc.)
11. Figure/Table Tools (BioRender, GraphPad, etc.)
12. Journal Author Instructions (major journals)
13. Japanese Resources (Ichushi, CiNii, etc.)

## Installation

Clone this repository into the Claude Code skills directory:

```bash
git clone https://github.com/kgraph57/paper-writer-skill.git ~/.claude/skills/paper-writer
```

Register the skill in Claude Code settings:

```json
// Add to "skills" in ~/.claude/settings.json
{
  "skills": {
    "paper-writer": {
      "path": "~/.claude/skills/paper-writer"
    }
  }
}
```

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- WebSearch / WebFetch (used for literature search)
- Python 3 + numpy, pandas, scipy, statsmodels, lifelines, matplotlib (for data analysis scripts)

## License

Private repository.

## Versions

- **v3.1.0** (2026-03-05) — Autonomous Stage-Gate System: 8 quality gates with auto-fix loops
- **v3.0.0** (2026-03-05) — Team Mode: 7 parallel agents for concurrent execution
- **v2.1.0** (2026-02-17) — Data management & analysis integration, 4 new files
- **v2.0.0** (2026-02-17) — Full lifecycle coverage, 16 new files, 10 phases
- **v1.0.0** (2026-02-17) — Structural improvements, 6 new files, 5 paper types

See [CHANGELOG.md](CHANGELOG.md) for details.

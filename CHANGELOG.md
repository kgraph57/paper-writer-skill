# Changelog

## [3.1.0] - 2026-03-05

### Autonomous Stage-Gate System

Added autonomous quality loop: each phase has a gate that blocks progress until PASS. FAIL triggers automatic feedback → fix → re-check (max 3 iterations, then escalate to user).

### 8 Gates

| Phase | Gate | PASS Condition | Gate Agent | Fixer Agent |
|-------|------|---------------|------------|-------------|
| 1 | Literature quality | ≥10 papers, all DOIs valid | section-reviewer | lit-searcher |
| 2 | Outline | All IMRAD sections, ≥2 citation mappings | section-reviewer | User escalation |
| 2.5 | Tables/Figures | All design files complete | section-reviewer | table-figure-planner |
| 3 | Section draft | Score ≥80%, Must Fix = 0 | section-reviewer | section-drafter |
| 4 | Humanize | High-priority AI patterns = 0 | section-reviewer | humanizer |
| 5 | References | Fabrication = 0, orphan citations = 0 | ref-builder (verifier) | ref-builder (builder) |
| 6 | Cross-section | PASS or CONDITIONAL_PASS | quality-gate (opus) | section-drafter |
| 7 | Submission prep | All required documents, word count OK | section-reviewer | section-drafter |

### Agent Modifications (6 files)

| Agent | Change |
|-------|--------|
| `paper-section-drafter` | Added `revision_mode` + `feedback_file` inputs; Step 0 for targeted fixes |
| `paper-humanizer` | Added `revision_mode` + `feedback_file` inputs; Step 0 for pattern-specific fixes |
| `paper-section-reviewer` | Added YAML verdict header (`gate_verdict`, `must_fix_count`, `score_percent`) |
| `paper-quality-gate` | Added `affected_sections` to YAML header for targeted repair |
| `paper-lit-searcher` | Added `revision_mode` for targeted re-search of gaps |
| `paper-table-figure-planner` | Added `revision_mode` for targeted design fixes |

### SKILL.md Updates

- Added ~100 lines "Autonomous Stage-Gate System" subsection inside Team Mode
- Gate flow diagram, feedback file format, revision_mode invocation template
- Escalation protocol, YAML verdict format, parallel gate execution rules

## [3.0.0] - 2026-03-05

### Team Mode: Parallel Agent Execution

Added 7-agent team architecture for parallel execution across all phases. Invoke with "チームで" / "team mode" / "並列で".

### New Agents (7)

| Agent | Role | Model |
|-------|------|-------|
| `paper-lit-searcher` | Database-specific literature search (PubMed, Scholar, CiNii, etc.) | sonnet |
| `paper-table-figure-planner` | Table and figure design from outline and data | sonnet |
| `paper-section-drafter` | Generic section drafting (parameterized per section) | sonnet |
| `paper-humanizer` | AI writing pattern detection and removal | haiku |
| `paper-ref-builder` | Citation collection (builder mode) and verification (verifier mode) | sonnet |
| `paper-section-reviewer` | Per-section quality check against section-checklist | sonnet |
| `paper-quality-gate` | Cross-section consistency verification and final PASS/FAIL gate | opus |

### SKILL.md Updates

| Update | Description |
|--------|-------------|
| **Team Mode section** | Full team workflow documentation added before Reference Files section (+117 lines) |
| **Phase 1 team** | 3 parallel literature searchers (PubMed, Scholar, domain DB) |
| **Phase 2.5 team** | 2 parallel planners (tables + figures) |
| **Phase 3 team** | Grouped parallel drafting by dependency (Methods+Results pair, Intro+Conclusion pair, etc.) |
| **Phase 4 team** | Up to 6 parallel humanizers (one per section, haiku model) |
| **Phase 6 team** | Parallel section reviewers + opus-level cross-section quality gate |
| **Phase 7 team** | 4 parallel submission document assemblers |
| **Phase 8 team** | 3 parallel revision handlers (Must Fix, Should Fix, Rebuttal) |

### Summary

- **7 agent definitions** installed to `~/.claude/agents/paper-*.md`
- **Backup** at `Project/skills/agents/paper-team/`
- **Model strategy**: haiku for pattern-matching (humanizer), sonnet for most work, opus for critical review (quality gate)
- **Paper-type specific parallelization**: Original Article, Case Report, and Systematic Review each have optimized parallel drafting rounds

---

## [2.1.0] - 2026-02-17

### Data Management & Analysis Integration

Added research data management and statistical analysis capabilities to the paper-writer skill.

### New Files (4)

| File | Description |
|------|-------------|
| `templates/data-management.md` | Data directory structure, README templates, de-identification checklist, file naming conventions |
| `templates/analysis-workflow.md` | 6-step analysis workflow (data inspection → Table 1 → primary analysis → subgroup → figures → manuscript linking) |
| `scripts/table1.py` | Table 1 generator — auto-detects variable types, Shapiro-Wilk normality test, group comparison with P values |
| `scripts/analysis-template.py` | Statistical analysis template — descriptive stats, t-test/Mann-Whitney, logistic regression (uni+multi), Kaplan-Meier survival |

### SKILL.md Updates

| Update | Description |
|--------|-------------|
| **Step 0.4: Organize Research Data** | Data directory setup, data dictionary, de-identification workflow |
| **Step 0.5: Data Analysis** | Python-based analysis workflow with scripts for Table 1, regression, survival analysis |
| **Project directory structures** | Added `data/` directory (raw/processed/analysis) to both Original Article and Case Report templates |
| **Reference Files list** | Added 4 new entries (data-management, analysis-workflow, table1.py, analysis-template.py) |

### Summary

- **66 files** total (31 templates, 27 references, 5 scripts, + SKILL.md, CHANGELOG.md, README.md, README.ja.md)
- **Data pipeline**: raw/ → processed/ → analysis/ → tables/ + figures/
- **Analysis types**: Table 1, descriptive stats, t-test, logistic regression, survival analysis, forest plot
- **Python packages**: numpy, pandas, scipy, statsmodels, lifelines, matplotlib, seaborn

---

## [2.0.0] - 2026-02-17

### Comprehensive Gap Analysis & Expansion

Exhaustive testing across all paper types and journal requirements identified 30+ gaps. This release adds 16 new files and major SKILL.md updates to cover the complete medical paper lifecycle.

### New Files (16)

**Templates (5):**

| File | Description |
|------|-------------|
| `templates/title-page.md` | Title page template with running head, ORCID, affiliations, word counts, clinical trial registration (EN/JP) |
| `templates/highlights.md` | Key Points (JAMA), "What is known" (BMJ), Highlights (Elsevier), Lay Summary, PNAS Significance (EN/JP) |
| `templates/limitations-guide.md` | Limitations section guide with 4 categories, direction-of-bias templates, SR two-part format (EN/JP) |
| `templates/acknowledgments.md` | Acknowledgments template (AI tools, medical writing, patient acknowledgment, EN/JP) |
| `templates/proof-correction.md` | Post-acceptance proof correction guide (24-72hr timeline, checklists, proofing systems) |

**References (11):**

| File | Description |
|------|-------------|
| `references/submission-portals.md` | Submission portal guide (ScholarOne, Editorial Manager, eJournalPress, OJS, common errors) |
| `references/open-access-guide.md` | OA models, APCs by journal, CC licenses, preprint servers, funder mandates (EN/JP) |
| `references/clinical-trial-registration.md` | Registration guide (ClinicalTrials.gov, UMIN-CTR, jRCT, WHO dataset, timing rules) |
| `references/abstract-formats.md` | Journal-specific abstract formats (JAMA, NEJM, Lancet, BMJ, Annals, Nature Med, PLOS Med) |
| `references/word-count-limits.md` | Word count limits by journal (general, specialty, case reports, SRs, letters, JP journals) |
| `references/coi-detailed.md` | Detailed COI categories (financial/personal/institutional), CRediT taxonomy, ORCID guide |
| `references/desk-rejection-prevention.md` | 8 common desk rejection reasons, self-check, journal selection strategy |
| `references/journal-reformatting.md` | Quick reformatting checklist, reference style comparison, cascading submission strategy |
| `references/statistical-reporting-full.md` | Extended SAMPL guide (by study design, common tests, sample size, missing data, multiple comparisons) |
| `references/reporting-guidelines-full.md` | 20+ reporting guidelines with checklists (CONSORT 2025, STROBE, PRISMA, CARE, STARD, SPIRIT, TRIPOD+AI, GRADE) |
| `references/master-reference-list.md` | Master reference list with URLs — 13 categories, 100+ resources for medical paper writing |

### SKILL.md Major Updates

| Update | Description |
|--------|-------------|
| **Study Protocol paper type** | Added to Supported Paper Types table |
| **Reporting guidelines expanded** | CONSORT 2025, SPIRIT 2025, TRIPOD+AI 2024, ARRIVE 2.0, CHEERS 2022, STARD 2015 added |
| **Discussion: Limitations** | Explicit reference to limitations-guide.md, mandatory subsection noted |
| **Case Report: Patient Perspective** | CARE item 10 added to Case Presentation structure |
| **Phase 7: Pre-Submission** | Added title page, highlights/key points, acknowledgments, declarations to checklist |
| **Phase 9: Post-Acceptance** | New phase: proof review, correction submission, post-publication tasks |
| **Phase 10: Rejection & Resubmission** | New phase: rejection assessment, quick reformat, cascading submission strategy |
| **Workflow overview** | Updated to include Post-Acceptance and Rejection phases |
| **Reference Files list** | Expanded with all 16 new file entries |

### Summary

- **62 files** total in the skill (27 references, 32 templates, 3 scripts)
- **6 paper types** with workflows (Original Article, Case Report, Review, Systematic Review, Letter, Study Protocol)
- **10 phases** in the full pipeline (was 8): +Post-Acceptance, +Rejection & Resubmission
- **20+ reporting guidelines** referenced (was 6)
- **100+ URLs** in master reference list
- **Complete lifecycle coverage**: from literature search through publication and rejection handling

---

## [1.0.0] - 2026-02-17

### Major Skill Improvement

Full review and structural enhancement of the paper-writer skill based on experienced researcher feedback.

### New Files (6)

| File | Description |
|------|-------------|
| `references/ai-disclosure.md` | ICMJE 2023 AI tool disclosure guide with journal-specific policies and EN/JP templates |
| `references/tables-figures-guide.md` | Comprehensive tables/figures creation guide (Table 1 format, figure types, resolution, captions) |
| `references/keywords-guide.md` | Keywords and MeSH term selection strategy with journal-specific requirements |
| `references/supplementary-materials.md` | Supplementary materials strategy (main text vs. supplement decision framework) |
| `templates/declarations.md` | Declaration templates: Ethics, Informed Consent, COI, Funding, Data Availability, AI Disclosure, CRediT (EN/JP) |
| `templates/graphical-abstract.md` | Graphical abstract design guide (layouts, specs, tools) |

### SKILL.md Structural Additions

| Addition | Description |
|----------|-------------|
| Phase 0.1 expansion | Added AI disclosure, keywords, and graphical abstract to journal requirements capture |
| Phase 1.1 improvement | Added practical literature search caveats (user-provided papers first, citation verification) |
| **Phase 2.5: Tables & Figures** | New phase between Outline and Drafting — design tables/figures before writing prose |
| **Phase 3-C: Review Article** | Complete workflow for review articles (thematic sections, introduction, conclusion) |
| **Phase 3-D: Systematic Review** | Complete PRISMA 2020-compliant workflow (Methods, Results, Discussion, with checklist items) |
| **Phase 3-E: Letter/Short Communication** | Condensed IMRAD workflow with word limit focus |
| **Phase 8: Revision** | Post-peer-review workflow (organize comments, response letter, implement revisions, verify) |
| Paper-type status trackers | 5 separate status tables for Original Article, Case Report, Review, SR, and Letter |
| Updated Reference Files | Added all 11 new reference entries to the list |

### Template Updates

| File | Changes |
|------|---------|
| `templates/project-init.md` | Added Reporting Guideline to Paper Info; Full Journal Requirements table; Tables & Figures and Declarations phases; Title → Title & Keywords; Declarations Status section |
| `templates/project-init-case.md` | Same improvements + "Informed Consent for Publication" (required for case reports) |
| `references/humanizer-academic.md` | Added C-7 non-academic writing pattern (JP pattern count: 12 → 13) |

### Workflow Overview Update

```
Before: Literature Search → Organization → Outline → Draft → Humanize → References → Quality Review → Submit
After:  Literature Search → Outline → Tables/Figures → Draft → Humanize → References → Quality Review → Pre-Submission → [Revision]
```

### Summary

- **46 files** total in the skill (16 references, 27 templates, 3 scripts)
- **5 paper types** now have complete workflows (Original Article, Case Report, Review, Systematic Review, Letter)
- **ICMJE 2023 compliance** for AI disclosure
- **13 Japanese patterns** (was 12) for AI writing detection
- **18 English patterns** for AI writing detection

# Review Article Templates

## Overview

This template covers two types of review articles commonly written in medical/scientific fields:
1. **Narrative Review** - Qualitative synthesis organized by themes
2. **Scoping Review** - Systematic mapping of evidence using established frameworks

Both differ fundamentally from systematic reviews (which use PRISMA, meta-analysis, and strict inclusion/exclusion criteria).

---

## How Narrative Reviews Differ from Systematic Reviews

| Aspect | Narrative Review | Systematic Review |
|--------|-----------------|-------------------|
| **Research question** | Broad, exploratory | Focused, specific (PICO) |
| **Search strategy** | Selective, not exhaustive | Comprehensive, reproducible |
| **Study selection** | Author discretion | Predefined inclusion/exclusion criteria |
| **Quality assessment** | Optional, informal | Mandatory, standardized tools |
| **Synthesis** | Qualitative, thematic | Quantitative (meta-analysis) or qualitative |
| **Bias risk** | Higher (selection bias) | Lower (systematic approach) |
| **Registration** | Not required | PROSPERO registration recommended |
| **Reporting guideline** | No formal standard (SANRA exists) | PRISMA 2020 |
| **Best for** | Broad topic overviews, educational purposes | Answering specific clinical questions |

---

## Part 1: Narrative Review Structure

### Common Organizational Strategies

Choose the structure that best fits your topic:

#### 1. Thematic Organization (Most Common)
Group literature by themes or subtopics. Best when the topic has clearly distinct aspects.

```
Theme 1: [Mechanism / Pathophysiology]
Theme 2: [Clinical Presentation]
Theme 3: [Diagnostic Approaches]
Theme 4: [Treatment Options]
Theme 5: [Future Directions]
```

#### 2. Chronological Organization
Trace the evolution of understanding over time. Best for topics with clear historical development.

```
Era 1: Early observations (before 2000)
Era 2: Molecular era (2000-2010)
Era 3: Precision medicine era (2010-2020)
Era 4: AI-assisted approaches (2020-present)
```

#### 3. Methodological Organization
Group by research methodology. Best for fields with diverse research approaches.

```
Group 1: In vitro studies
Group 2: Animal models
Group 3: Observational clinical studies
Group 4: Randomized controlled trials
Group 5: Real-world evidence
```

#### 4. Conceptual/Model-Based Organization
Build around a theoretical framework or model.

```
Component 1: Input factors
Component 2: Process mechanisms
Component 3: Output/outcome measures
Component 4: Moderating factors
```

### Narrative Review Outline Template

```markdown
# [Title]: A Narrative Review

## Abstract
- Background (2-3 sentences): Why this review is needed
- Purpose (1 sentence): What this review aims to accomplish
- Methods (1-2 sentences): How literature was identified and selected
- Results (3-5 sentences): Key findings organized by theme
- Conclusions (1-2 sentences): Main takeaways and implications
- Keywords: [keyword1], [keyword2], [keyword3], [keyword4], [keyword5]

## 1. Introduction
- 1.1 Background and context
  - Define the topic and its clinical/scientific significance
  - State the current state of knowledge
  - Identify gaps or controversies
- 1.2 Rationale for this review
  - Why a narrative review (vs. systematic review)?
  - What has changed since prior reviews?
- 1.3 Objectives
  - Clearly state what this review covers and does not cover
  - Define scope boundaries

## 2. Search Strategy (Brief Methods)
- Databases searched (PubMed, Scopus, Web of Science, etc.)
- Key search terms used
- Time period covered
- Language restrictions
- Note: This section can be brief for narrative reviews but adds credibility

## 3. [Theme 1 Title]
- 3.1 [Subtopic A]
- 3.2 [Subtopic B]
- 3.3 Summary of Theme 1

## 4. [Theme 2 Title]
- 4.1 [Subtopic A]
- 4.2 [Subtopic B]
- 4.3 Summary of Theme 2

## 5. [Theme 3 Title]
- 5.1 [Subtopic A]
- 5.2 [Subtopic B]
- 5.3 Summary of Theme 3

## 6. [Theme 4 Title] (as needed)

## 7. Discussion / Synthesis
- Integration across themes
- Clinical or practical implications
- Comparison with previous reviews
- Limitations of the current evidence
- Limitations of this review

## 8. Future Directions
- Gaps identified in the literature
- Recommended research priorities
- Emerging methodologies or technologies

## 9. Conclusions
- 3-5 key takeaways
- Clinical bottom line (if applicable)

## References

## Tables and Figures
- Table 1: Summary of key studies reviewed
- Table 2: [Theme-specific comparison table]
- Figure 1: [Conceptual framework or timeline]
```

### Tips for Organizing Themes

1. **Start with a literature matrix**: Before writing, create a spreadsheet with columns for citation, year, study design, population, key findings, and your assigned theme tag.

2. **Use the "3-pass" approach**:
   - Pass 1: Read titles/abstracts, assign preliminary themes
   - Pass 2: Read full texts of included papers, refine themes
   - Pass 3: Identify connections between themes

3. **Each theme section should**:
   - Open with a topic sentence defining the theme
   - Present evidence from multiple sources (not just one study)
   - Compare and contrast findings across studies
   - End with a brief synthesis statement

4. **Transition between themes**: Use explicit transition paragraphs that link one theme to the next. Avoid isolated "silos" of information.

5. **Balance coverage**: Ensure each theme has roughly comparable depth. If one theme dominates, consider splitting it.

6. **Address contradictions**: When studies disagree, explicitly discuss why (different populations, methods, definitions).

---

## Part 2: Scoping Review Structure

### Framework: JBI / Arksey & O'Malley (2005) with Levac et al. (2010) Enhancements

Scoping reviews follow a 6-stage framework:

| Stage | Description |
|-------|-------------|
| 1 | Identifying the research question |
| 2 | Identifying relevant studies |
| 3 | Study selection |
| 4 | Charting the data |
| 5 | Collating, summarizing, and reporting results |
| 6 | Consultation (optional but recommended) |

### Scoping Review Outline Template

```markdown
# [Title]: A Scoping Review

## Abstract (Structured)
- Background:
- Objectives:
- Inclusion criteria:
- Sources of evidence:
- Charting methods:
- Results:
- Conclusions:
- Keywords:

## 1. Introduction
- 1.1 Background / Rationale
  - Context and significance of the topic
  - Why a scoping review (not systematic review)?
    - Broad topic, diverse evidence base
    - Emerging field with heterogeneous studies
    - Mapping evidence rather than answering specific question
- 1.2 Review question(s)
  - Use PCC framework (Population, Concept, Context)
  - Example: "What is the extent of [concept] in [population] within [context]?"
- 1.3 Objectives
  - Map the existing evidence
  - Identify key concepts and definitions
  - Identify gaps in the literature
  - Inform future systematic reviews

## 2. Methods
- 2.1 Protocol and registration
  - JBI methodology followed
  - Protocol registered at [OSF/other] (if applicable)
  - Reported per PRISMA-ScR (PRISMA Extension for Scoping Reviews)
- 2.2 Eligibility criteria
  - Population:
  - Concept:
  - Context:
  - Types of evidence sources: (primary research, reviews, grey literature, etc.)
  - Exclusion criteria:
- 2.3 Information sources
  - Databases: PubMed, CINAHL, Scopus, Web of Science, etc.
  - Grey literature: Google Scholar, organizational websites, conference proceedings
  - Reference list scanning
  - Date range:
  - Language:
- 2.4 Search strategy
  - Full search strategy for at least one database (usually in appendix)
  - Developed with librarian/information specialist (recommended)
- 2.5 Selection of sources of evidence
  - Two-stage screening: title/abstract → full text
  - Independent screening by ≥2 reviewers (recommended)
  - Conflict resolution process
  - PRISMA-ScR flow diagram
- 2.6 Data charting
  - Data charting form (pilot tested)
  - Variables extracted:
    - Author(s), year, country
    - Study design / methodology
    - Population characteristics
    - Concept details
    - Context
    - Key findings relevant to review question(s)
  - Charting performed by [number] reviewers
- 2.7 Critical appraisal (optional for scoping reviews)
  - If performed, state tool used and rationale

## 3. Results
- 3.1 Search results
  - PRISMA-ScR flow diagram (identification, screening, eligibility, inclusion)
  - Number at each stage
- 3.2 Characteristics of included sources
  - Table: Summary of all included studies
  - Publication year distribution
  - Geographic distribution
  - Study design distribution
- 3.3 Results of individual sources
  - Organized by review question or theme
  - Descriptive mapping (not quality assessment)
- 3.4 [Findings organized by theme/category]
  - Category 1: [Description and mapping]
  - Category 2: [Description and mapping]
  - Category 3: [Description and mapping]

## 4. Discussion
- 4.1 Summary of evidence
  - What is known about this topic
  - How the evidence landscape is shaped
- 4.2 Implications for practice
- 4.3 Implications for research
  - Gaps identified → recommendations for future studies
  - Areas suitable for systematic review
- 4.4 Limitations
  - Of the scoping review process
  - Of the included evidence

## 5. Conclusions

## References

## Appendices
- Appendix A: Full search strategies for all databases
- Appendix B: Data charting form
- Appendix C: List of excluded studies with reasons (if applicable)

## Tables and Figures
- Table 1: Characteristics of included sources of evidence
- Table 2: Data charting results by [category]
- Figure 1: PRISMA-ScR flow diagram
- Figure 2: [Distribution map, timeline, or conceptual map]
```

---

## Quality Criteria for Narrative Reviews

### SANRA (Scale for the Assessment of Narrative Review Articles)

Use this 6-item scale to self-assess your narrative review quality:

| Item | Criterion | Score (0-2) |
|------|-----------|-------------|
| 1 | **Justification of the article's importance** | 0=none, 1=partial, 2=clear |
| 2 | **Statement of concrete aims or formulation of questions** | 0=none, 1=vague, 2=specific |
| 3 | **Description of the literature search** | 0=none, 1=partial, 2=detailed |
| 4 | **Referencing** (appropriate citation density) | 0=poor, 1=adequate, 2=thorough |
| 5 | **Scientific reasoning** (logical argumentation) | 0=poor, 1=adequate, 2=strong |
| 6 | **Appropriate presentation of data** | 0=poor, 1=adequate, 2=excellent |

**Target: Score ≥ 9/12 for publication-quality narrative reviews.**

### Additional Quality Indicators

- [ ] Clear scope boundaries defined
- [ ] Search strategy described (even if not exhaustive)
- [ ] Balanced representation of evidence (not cherry-picked)
- [ ] Contradictory evidence acknowledged
- [ ] Tables summarizing key evidence provided
- [ ] Clinical or practical implications stated
- [ ] Limitations honestly disclosed
- [ ] Recent literature included (within last 2-3 years)
- [ ] Seminal/foundational papers cited
- [ ] Writing is accessible to the target audience

---

## Choosing Between Review Types

```
Is your question specific and answerable with PICO?
├── YES → Consider Systematic Review (PRISMA)
└── NO → Is the field well-established with defined terminology?
    ├── YES → Narrative Review
    └── NO → Scoping Review (JBI/Arksey & O'Malley)
```

## Reporting Guidelines Quick Reference

| Review Type | Reporting Guideline | Registration |
|-------------|-------------------|--------------|
| Narrative Review | SANRA (quality), no formal reporting guideline | Not required |
| Scoping Review | PRISMA-ScR | OSF or JBI (recommended) |
| Systematic Review | PRISMA 2020 | PROSPERO (required) |
| Systematic Review with Meta-analysis | PRISMA 2020 + MOOSE | PROSPERO (required) |

---
name: paper-writer
description: "Medical/scientific paper writing workflow skill. Manages the full pipeline from literature search to submission-ready manuscript. Creates and manages a project directory with IMRAD-format section files, literature matrix, reference management, and quality checklists. Supports both English and Japanese papers. Triggers: 'write paper', 'paper-write', 'start manuscript', '論文を書く', '論文執筆', '論文プロジェクト', 'manuscript', 'research paper', '原稿作成'."
---

# Paper Writer Skill

Full-pipeline academic paper writing assistant. From literature search to submission-ready manuscript.

## Overview

This skill manages the entire paper writing workflow:

```
Literature Search → Outline → Tables/Figures → Draft → Humanize → References → Quality Review → Pre-Submission → [Revision]
```

Each paper is a **project directory** containing structured Markdown files for every section, a literature matrix, and quality checklists.

### Supported Paper Types

| Type | Structure | Reporting Guideline | Notes |
|------|-----------|-------------------|-------|
| **Original Article** | Full IMRAD | STROBE / CONSORT | Default |
| **Case Report** | Intro / Case / Discussion | CARE | Separate templates |
| **Review Article** | Thematic sections | - | Flexible structure |
| **Letter / Short Communication** | Condensed IMRAD | Same as original | Word limit focus |
| **Systematic Review** | PRISMA-compliant | PRISMA 2020 | With PRISMA checklist |

## Workflow

### Phase 0: Project Initialization

When the user invokes this skill, ask for:

1. **Working title** (can change later)
2. **Paper type** (Original Article / Case Report / Review / Letter / Systematic Review)
3. **Target journal** (optional but recommended)
4. **Language** (English / Japanese / Both)
5. **Research question** in one sentence
6. **Key data** available (what Tables/Figures already exist?)

#### Step 0.1: Capture Journal Requirements

If a target journal is specified, look up and document:
- **Word limits**: total manuscript, abstract, each section (if specified)
- **Citation style**: Vancouver, APA, NLM, or other
- **Required sections**: some journals require separate Conclusion, others don't
- **Abstract format**: structured or unstructured, word limit
- **Figure/Table limits**: maximum number allowed
- **Reporting guideline**: which checklist the journal requires
- **Special requirements**: cover page format, line numbering, etc.
- **AI disclosure**: whether the journal requires AI usage disclosure, and where (Methods, Acknowledgments, or dedicated section). See `references/ai-disclosure.md`.
- **Keywords**: number required, MeSH preferred or free-text. See `references/keywords-guide.md`.
- **Graphical abstract**: required or optional. See `templates/graphical-abstract.md`.

Use `WebSearch` to look up the journal's "Instructions for Authors" page.

Record all requirements in the README.md under a "Journal Requirements" section.

#### Step 0.2: Select Reporting Guideline

Based on paper type and study design, select the appropriate reporting guideline:

| Study Type | Guideline | Reference |
|-----------|-----------|-----------|
| Randomized Controlled Trial | CONSORT 2010 | `references/reporting-guidelines.md` |
| Observational study (cohort, case-control, cross-sectional) | STROBE | `references/reporting-guidelines.md` |
| Systematic review / meta-analysis | PRISMA 2020 | `references/reporting-guidelines.md` |
| Case report | CARE | `references/reporting-guidelines.md` |
| Diagnostic accuracy study | STARD | EQUATOR Network |
| Quality improvement study | SQUIRE | EQUATOR Network |

Read `~/.claude/skills/paper-writer/references/reporting-guidelines.md` and note the key checklist items for the selected guideline. These items will be checked throughout the writing process.

#### Step 0.3: Create Project Directory

**For Original Article / Review / Letter / Systematic Review:**

```
{project-dir}/
├── README.md                    # Project overview, status tracker
├── 00_literature/
│   ├── search-strategy.md       # Search terms, databases, dates
│   ├── literature-matrix.md     # Structured comparison table
│   └── key-papers/              # Notes on important papers
├── 01_outline.md                # Paper outline / structure plan
├── 02_methods.md                # Methods section
├── 03_results.md                # Results section
├── 04_introduction.md           # Introduction section
├── 05_discussion.md             # Discussion section
├── 06_conclusion.md             # Conclusion section
├── 07_abstract.md               # Abstract
├── 08_title.md                  # Title candidates and final title
├── 09_references.md             # Reference list
├── 10_cover-letter.md           # Cover letter to editor
├── figures/                     # Figure files and captions
├── tables/                      # Table files
└── checklists/
    ├── section-quality.md       # Per-section quality checklist
    └── submission-ready.md      # Pre-submission checklist
```

**For Case Report:**

```
{project-dir}/
├── README.md                    # Project overview, status tracker
├── 00_literature/
│   ├── search-strategy.md
│   ├── literature-matrix.md
│   └── key-papers/
├── 01_outline.md
├── 02_case.md                   # Case presentation (CARE structure)
├── 03_introduction.md           # Introduction (why reportable)
├── 04_discussion.md             # Discussion
├── 05_abstract.md               # Abstract (CARE format)
├── 06_title.md                  # Title (must contain "case report")
├── 07_references.md
├── 08_cover-letter.md
├── figures/
├── tables/
└── checklists/
    ├── section-quality.md
    └── submission-ready.md
```

Read `~/.claude/skills/paper-writer/templates/project-init.md` with the `Read` tool and use it to generate `README.md`. For Case Reports, use `project-init-case.md` instead.

**File numbering follows the recommended writing order**, not the reading order. This is intentional.
### Phase 1: Literature Search & Organization

#### Step 1.1: Define Search Strategy

Create `00_literature/search-strategy.md` with:

- **Databases**: PubMed, Google Scholar (always available); Scopus, CiNii (if user has institutional access)
- **Search terms**: MeSH terms + free-text keywords
- **Inclusion/exclusion criteria** for papers
- **Date range**

**How to search:**

Use `WebSearch` with targeted queries:
- For PubMed: search `"search terms" pediatric asthma pubmed`
- For Google Scholar: search `"search terms" site:scholar.google.com`
- For general: search the research question directly

If WebSearch results are limited, use `WebFetch` on specific PubMed URLs:
```
https://pubmed.ncbi.nlm.nih.gov/?term=search+terms&sort=date
```

**Important**: WebSearch may not reliably return PubMed results with `site:` filtering. If results are poor, try broader searches and filter manually, or ask the user to provide key papers they already know.

**Practical reality**: AI-based literature search has significant limitations. The most reliable workflow is:
1. Ask the user to provide their 3-5 key papers (they usually know them already)
2. Use WebSearch to supplement with additional relevant papers
3. Use `references/pubmed-query-builder.md` to construct proper PubMed queries
4. Have the user validate the final literature list for completeness
5. Verify every AI-found citation exists (see `references/citation-verification.md`)

#### Step 1.2: Build Literature Matrix

Read `~/.claude/skills/paper-writer/templates/literature-matrix.md` with the `Read` tool.

For each relevant paper found, extract and organize:

| Author (Year) | Design | N | Population | Key Finding | Limitation | Relevance |
|----------------|--------|---|------------|-------------|------------|-----------|

Aim for **15-30 papers** for an original article, **8-15** for a case report, **30-50** for a systematic review.

#### Step 1.3: Identify Key Papers

For the 3-5 most important papers, create individual notes in `00_literature/key-papers/` with:

- Full citation
- Study design and quality assessment
- Key results with exact numbers
- How it relates to the current paper
- What gap it leaves (that our paper addresses)

### Phase 2: Outline

Create `01_outline.md` with the paper skeleton.

Read `~/.claude/skills/paper-writer/references/imrad-guide.md` with the `Read` tool for the detailed IMRAD structure. For Case Reports, this guide does not apply directly — use the CARE structure instead.

The outline should specify:

- Each section's key points (bullet list)
- Which papers support which points
- Which Tables/Figures go where
- The **story arc**: Background Problem → Gap → Our Approach → Findings → Implications
- For Case Reports: Background → Why Reportable → Case Details → Clinical Lesson

**Get user approval on outline before proceeding to drafting.**

### Phase 2.5: Tables & Figures

Read `~/.claude/skills/paper-writer/references/tables-figures-guide.md` with the `Read` tool.

Tables and figures are the backbone of a paper — many reviewers look at the abstract, then the tables/figures, before reading the text. **Design them before writing prose** so the text can reference them naturally.

#### Step 2.5.1: Plan Tables & Figures

Based on the outline, determine:
- Which data belongs in a table vs. a figure vs. the text
- Table 1 is almost always "Baseline Characteristics" (use the template in `references/tables-figures-guide.md`)
- How many tables/figures are allowed by the journal (check Phase 0 requirements)

#### Step 2.5.2: Create Tables

Create table files in `tables/` directory:
- `table1_baseline.md` — Baseline characteristics (standard format)
- `table2_*.md` — Additional tables as needed (regression results, outcomes, etc.)

**Rules:**
- Title above the table
- No vertical lines (horizontal lines only)
- Consistent decimal places within each column
- Footnotes for abbreviations and statistical tests
- Total sample size in the header row

#### Step 2.5.3: Plan Figures

Create caption files in `figures/` directory:
- `fig1_caption.md` — Often a flow diagram (CONSORT/PRISMA) or study design
- `fig2_caption.md` — Key result visualization

**Rules:**
- Captions must be self-explanatory without reading the main text
- Include key statistics in captions
- Specify resolution requirements (300+ DPI for print, 600+ for line art)
- Use colorblind-friendly palettes

#### Step 2.5.4: Graphical Abstract (if required)

If the journal requires or encourages a graphical abstract, read `~/.claude/skills/paper-writer/templates/graphical-abstract.md` and plan the visual summary.

**Get user review on table/figure plan before proceeding to drafting.**

### Phase 3: Drafting

**The writing order is intentional and produces better papers.** Follow it strictly.

---

#### 3-A: Original Article Workflow

##### Step 3.1: Methods & Results (Write as a pair)

Read `~/.claude/skills/paper-writer/templates/methods.md` and `~/.claude/skills/paper-writer/templates/results.md` with the `Read` tool.

**Methods rules:**
- Reproducibility is everything
- Include: study design, patients/subjects, data collection, statistical analysis, ethics
- Every method must have a corresponding result

**Results rules:**
- Facts only, no interpretation
- No references to other studies
- Every Table/Figure must be mentioned in text
- Methods ↔ Results must correspond 1:1

Write `02_methods.md` and `03_results.md` together, ensuring perfect correspondence. Cross-check: every subsection in Methods must map to a corresponding subsection in Results, and vice versa.

**Workflow**: Write Methods subsection 1 → Results subsection 1 → Methods subsection 2 → Results subsection 2 → ... This interleaving ensures 1:1 correspondence.

##### Step 3.2: Introduction (Paragraph 3) & Conclusion (Write as a pair)

Read `~/.claude/skills/paper-writer/templates/introduction.md` and `~/.claude/skills/paper-writer/templates/conclusion.md` with the `Read` tool.

**Why write Paragraph 3 first?** The study objective (Introduction P3) and the conclusion must mirror each other. Writing them together guarantees alignment. Paragraphs 1-2 provide background that funnels toward the objective — they are easier to write once the objective is locked.

**Introduction structure (3 paragraphs):**
1. General background (everyone agrees with this)
2. Clinical question / knowledge gap (but we don't know X)
3. Study objective (therefore, we investigated...)

**Conclusion rules:**
- Must directly answer the objective stated in Introduction paragraph 3
- One core message
- Brief and direct

Write the final paragraph of `04_introduction.md` and `06_conclusion.md` together to ensure they mirror each other.

##### Step 3.3: Discussion

Read `~/.claude/skills/paper-writer/templates/discussion.md` with the `Read` tool.

**Discussion structure:**
1. Summary of main findings
2-N. Comparison with prior literature (use `00_literature/literature-matrix.md`)
N+1. Limitations (be honest)
N+2. Clinical implications / future directions

**Discussion rules:**
- No new results
- No excessive speculation
- Support every claim with a reference
- Keep it focused

##### Step 3.4: Introduction (Paragraphs 1-2)

Now write paragraphs 1-2 of `04_introduction.md`. The background should funnel toward the research question already written in paragraph 3.

##### Step 3.5: Abstract

Read `~/.claude/skills/paper-writer/templates/abstract.md` with the `Read` tool.

Write `07_abstract.md` as a structured abstract:
- Background/Objective (1-2 sentences)
- Methods (2-3 sentences)
- Results (3-4 sentences)
- Conclusions (1-2 sentences)

Check the journal-specific word limit captured in Phase 0. The Abstract must be consistent with the full text. Cross-check all numbers.

##### Step 3.6: Title

Write `08_title.md` with 3-5 title candidates. Evaluate each against:
- Specific (what was studied?)
- Concise (< 15 words ideal)
- Contains keywords (searchable)
- No conclusion spoilers

**Get user approval on final title.**

---

#### 3-B: Case Report Workflow

##### Step 3.1-CR: Case Presentation

Read `~/.claude/skills/paper-writer/templates/case-report.md` with the `Read` tool.

Write `02_case.md` following the CARE structure:
1. Patient information (demographics, history)
2. Clinical findings
3. Timeline (consider a timeline figure)
4. Diagnostic assessment
5. Therapeutic intervention
6. Follow-up and outcomes

**Rules:**
- Chronological order
- Only clinically relevant details
- Document informed consent for publication
- Report both positive AND negative findings

##### Step 3.2-CR: Discussion

Read `~/.claude/skills/paper-writer/templates/discussion.md` with the `Read` tool.

Write `04_discussion.md`:
1. Why this case is significant (clinical lesson)
2. Comparison with published literature
3. Limitations of the case
4. Clinical implications

Keep it focused and shorter than in an Original Article.

##### Step 3.3-CR: Introduction

Read `~/.claude/skills/paper-writer/templates/case-introduction.md` with the `Read` tool.

Write `03_introduction.md`:
1. Brief background on the condition
2. Why this case is reportable (rarity, novelty, instructive value)
3. Optional: "We report a case of... to highlight..."

Write the Introduction AFTER the Case section — you need to know the full case to justify its reporting.

##### Step 3.4-CR: Abstract

Read `~/.claude/skills/paper-writer/templates/case-abstract.md` with the `Read` tool.

Write `05_abstract.md` using the CARE abstract structure:
- Background (1-2 sentences: why this case is worth reporting)
- Case Presentation (3-5 sentences: demographics, findings, diagnosis, treatment, outcome)
- Conclusions (1-2 sentences: clinical lesson)

Do NOT use Methods/Results structure for Case Report abstracts.

##### Step 3.5-CR: Title

Write `06_title.md` with 3-5 title candidates. For case reports:
- Title MUST contain "case report" (CARE requirement)
- Include the diagnosis or key finding
- Example: "Successful treatment of severe pediatric asthma with dupilumab: a case report"

**Get user approval on final title.**

---

#### 3-C: Review Article Workflow

Review articles synthesize existing literature on a topic. The structure is thematic rather than IMRAD.

##### Step 3.1-RA: Thematic Sections

Read `~/.claude/skills/paper-writer/templates/discussion.md` for general writing guidance.

Organize the body into thematic sections based on the outline. Common structures:
1. **Chronological**: Evolution of understanding over time
2. **Thematic**: Grouped by subtopic (most common)
3. **Methodological**: Grouped by study approach

Each section should:
- Synthesize findings across studies (not just summarize one at a time)
- Identify areas of consensus and controversy
- Highlight gaps in the literature
- Use the literature matrix to ensure comprehensive coverage

##### Step 3.2-RA: Introduction

Write the introduction:
1. Scope and importance of the topic
2. Why a review is needed now (new evidence, controversy, emerging field)
3. Objectives and scope of this review

##### Step 3.3-RA: Conclusion & Future Directions

Write the conclusion:
1. Synthesize the key themes identified
2. Current state of knowledge
3. Gaps and future research directions
4. Clinical implications (if applicable)

##### Step 3.4-RA: Abstract

Write an unstructured abstract (unless journal requires structured format):
- Purpose of the review
- Methods (databases searched, date range, selection criteria)
- Key findings synthesized across themes
- Conclusions

##### Step 3.5-RA: Title

Write title candidates. For review articles:
- Include "review", "narrative review", or "scoping review" in the title
- Clearly state the topic
- Example: "Artificial intelligence in diagnostic radiology: a narrative review"

**Get user approval on final title.**

---

#### 3-D: Systematic Review Workflow

Read `~/.claude/skills/paper-writer/templates/sr-outline.md` with the `Read` tool for the complete PRISMA 2020-compliant template.

Systematic reviews follow a strict, pre-registered protocol. The template provides the full structure with PRISMA 2020 checklist item numbers.

##### Step 3.1-SR: Methods

The Methods section is the most critical part. Write it following PRISMA items P-5 through P-18:
1. Protocol and registration (PROSPERO ID)
2. Eligibility criteria (PICO/PECO)
3. Information sources (databases, dates)
4. Search strategy (full strategy in supplementary)
5. Selection process (screening, inter-rater reliability)
6. Data collection process
7. Data items
8. Risk of bias assessment (tool selection)
9. Effect measures
10. Synthesis methods (narrative and/or meta-analysis)
11. Subgroup and sensitivity analyses
12. Reporting bias assessment
13. Certainty of evidence (GRADE)

##### Step 3.2-SR: Results

Write Results following PRISMA items P-19 through P-23:
1. PRISMA flow diagram (Figure 1 — mandatory)
2. Study characteristics table
3. Risk of bias summary
4. Results of individual studies
5. Results of syntheses (forest plots if meta-analysis)
6. Reporting biases (funnel plots if ≥10 studies)
7. Certainty of evidence (GRADE Summary of Findings table)

##### Step 3.3-SR: Discussion

Write Discussion following PRISMA items P-25 through P-27:
1. Summary of evidence with certainty levels
2. Comparison with previous reviews
3. Strengths and limitations (both evidence and review process)
4. Implications for practice and research

##### Step 3.4-SR: Introduction, Abstract, Title

Follow the same principles as Original Article but with SR-specific framing:
- Introduction: justify why this SR is needed (no existing SR, outdated SR, new evidence)
- Abstract: must include number of studies, total participants, key pooled estimates
- Title: must include "systematic review" (and "meta-analysis" if applicable)

**Get user approval on final title.**

---

#### 3-E: Letter / Short Communication Workflow

Letters and short communications follow a condensed IMRAD format. The key constraint is the **word limit** (typically 600-1500 words).

##### Step 3.1-LT: Condensed Draft

Write a single file covering all sections:
1. **Introduction** (1-2 sentences): State the purpose directly. No lengthy background.
2. **Methods** (1 paragraph): Essential details only. Reference a fuller description elsewhere if needed.
3. **Results** (1-2 paragraphs): Key findings only. Usually 1 table OR 1 figure (not both).
4. **Discussion** (1-2 paragraphs): Main interpretation, 1-2 comparisons with literature, key limitation.

**Rules:**
- Every word counts — eliminate all filler
- Typically limited to 1 table + 1 figure, or 2 of one type
- References usually limited to 10-15
- No separate Conclusion section (fold into last Discussion paragraph)

##### Step 3.2-LT: Abstract

Write a brief abstract (often 100-150 words, unstructured).

##### Step 3.3-LT: Title

Short, direct titles work best. No need for elaborate structure.

**Get user approval on final title.**

### Phase 4: Humanize

Read `~/.claude/skills/paper-writer/references/humanizer-academic.md` with the `Read` tool.

After drafting, run a humanization pass on every section to remove AI-generated writing patterns.

#### Step 4.1: Scan for AI Patterns

Read each section file and identify:

**English papers** — check for these 18 patterns:
1. Significance inflation ("pivotal", "evolving landscape", "underscores")
2. Notability claims ("landmark", "renowned", "groundbreaking")
3. Superficial -ing analyses ("highlighting", "underscoring", "showcasing")
4. Promotional language ("profound impact", "remarkable", "dramatic")
5. Vague attributions ("Studies have shown", "Experts argue")
6. Formulaic challenges ("Despite challenges... future outlook")
7. AI vocabulary ("Additionally", "crucial", "delve", "landscape", "pivotal")
8. Copula avoidance ("serves as" instead of "is")
9. Negative parallelisms ("Not only... but also")
10. Rule of three overuse (forcing ideas into groups of three)
11. Synonym cycling ("Patients... Participants... Subjects")
12. False ranges ("from X to Y" on unrelated scales)
13. Em dash overuse
14. Title Case in headings
15. Curly quotation marks
16. Filler phrases ("In order to", "It is important to note", "comprehensive investigation")
17. Excessive hedging ("may suggest... have the potential to")
18. Generic positive conclusions ("The future looks bright")

**Japanese papers (日本語)** — 13パターン（A〜C）+ AIボキャブラリー一覧（D）をチェック:

A. 記号と表記（3パターン）:
- emダッシュ、カギ括弧多用、丸括弧補足しすぎ

B. 文のリズム（3パターン）:
- 同じ語尾の連続（である。である。である。）
- 接続詞過多（さらに、また、加えて）
- 段落の終わりが毎回きれいに閉じる

C. 学術文特有の問題（7パターン）:
- C-1 保険が多い（逃げ道の常設）
- C-2 根拠なき評価語（非常に有効、大きなメリット）
- C-3 抽象語だけで押し切る
- C-4 AIボキャブラリー（包括的、革新的、シームレス、示唆に富む）
- C-5 同義語の言い換え連打
- C-6 受動態の過剰使用（検討が行われた → 検討した）
- C-7 非学術的な文体の混入（「参考になれば幸いである」「ポイントは以下の通り」→ 削除）

D. AIボキャブラリー一覧: `references/humanizer-academic.md` の日本語セクションDを参照。C-4のパターン判定に使う語彙リスト。

#### Step 4.2: Rewrite

Consult `references/humanizer-academic.md` for specific before/after examples. For each identified pattern:
1. Replace with precise, specific academic language
2. Preserve all data, statistics, and citations exactly
3. Use simple constructions ("is" over "serves as")
4. Remove filler and reduce hedging to match evidence strength
5. Ensure consistent terminology throughout
6. If 3+ AI patterns appear in one sentence, rewrite the entire sentence rather than fixing patterns individually

#### Step 4.3: Section-Specific Focus

**English:**

| Section | Priority Patterns |
|---------|------------------|
| Introduction | #1 Significance inflation, #5 Vague attributions, #7 AI vocabulary, #3 -ing analyses |
| Methods | #16 Filler phrases, #8 Copula avoidance |
| Results | #3 -ing analyses, #4 Promotional language |
| Discussion | #17 Excessive hedging, #6 Formulaic challenges |
| Conclusion | #18 Generic conclusions, #1 Significance inflation |
| Abstract | ALL patterns (most visible section) |

**日本語:**

| セクション | 重点パターン |
|-----------|-------------|
| 緒言 | C-2 根拠なき評価語, B-2 接続詞過多 |
| 方法 | C-6 受動態の過剰使用, C-3 抽象語 |
| 結果 | B-1 同じ語尾, A-3 丸括弧多用 |
| 考察 | C-1 保険が多い, C-4 AIボキャブラリー |
| 結論 | C-2 根拠なき評価語, C-7 非学術的文体 |
| 抄録 | 全パターン |

#### Step 4.4: Verify

After humanization:

**English:**
- [ ] Scientific content unchanged (no data or citations lost)
- [ ] No "Additionally" / "Furthermore" at sentence start (max 1 per section)
- [ ] No "pivotal" / "crucial" / "landscape" / "delve"
- [ ] No "-ing" phrases tacked on for fake depth
- [ ] No "serves as" / "stands as" (use "is")
- [ ] Em dashes used sparingly (< 2 per page)
- [ ] Consistent terminology (no synonym cycling)
- [ ] Sentence rhythm varies (short and long sentences mixed)
- [ ] No generic conclusions remaining
- [ ] Hedging proportionate to evidence strength

**日本語:**
- [ ] 「さらに」「また」「加えて」の連発がない（各セクション最大1回）
- [ ] 同じ語尾が3回以上続いていない
- [ ] 根拠なき「非常に」「大きな」がない
- [ ] 受動態の過剰使用がない（能動態に直す）
- [ ] 定型的な締めの句がない（「参考になれば幸いである」等）
- [ ] 抽象語だけで押し切っていない
- [ ] カギ括弧を多用していない

### Phase 5: References

Read `~/.claude/skills/paper-writer/references/citation-guide.md` with the `Read` tool.

Build `09_references.md` (or `07_references.md` for Case Reports):

1. Collect all cited papers from all sections
2. Format according to target journal style captured in Phase 0 (Vancouver, APA, etc.)
3. Number sequentially as cited
4. Verify completeness: every reference is cited in text, every citation has a reference entry
5. **Verify authenticity**: For EVERY AI-suggested reference, confirm the paper exists via `WebSearch` with the exact title. AI frequently fabricates plausible-sounding citations.

### Phase 6: Quality Review

Read `~/.claude/skills/paper-writer/references/section-checklist.md` with the `Read` tool. For Case Reports, also check the CARE-specific items in `templates/case-report.md`.

Run the quality checklist against each section. Update `checklists/section-quality.md` with results.

**Verification checklist:**
- [ ] Methods ↔ Results correspondence (Original Article only)
- [ ] Introduction objective ↔ Conclusion answer
- [ ] All Tables/Figures mentioned in text
- [ ] No interpretation in Results (Original Article only)
- [ ] No new results in Discussion
- [ ] Abstract numbers match full text
- [ ] All references cited and formatted
- [ ] Word count within target journal limits (check Phase 0 requirements)
- [ ] Reporting guideline followed (check Phase 0 selected guideline)
- [ ] AI writing patterns removed (Phase 4 verification passed)
- [ ] Consistent terminology throughout all sections
- [ ] Ethics approval and informed consent documented

### Phase 7: Pre-Submission

Read `~/.claude/skills/paper-writer/templates/cover-letter.md` and `~/.claude/skills/paper-writer/templates/submission-ready.md` with the `Read` tool.

Create:
1. Cover letter using the template
2. `checklists/submission-ready.md` using the template — fill in journal-specific limits from Phase 0
3. Compile all sections into a single reading-order Markdown file for the user to review

**Final compilation order (reading order):**

For Original Article:
```
Title → Abstract → Introduction → Methods → Results → Discussion → Conclusion → References
```

For Case Report:
```
Title → Abstract → Introduction → Case Presentation → Discussion → References
```

The compiled file should include all section content in sequence. Tables and Figures should be referenced but kept in their separate folders.

### Phase 8: Revision (Post-Review)

When the user receives reviewer comments (peer review, editorial decision letter):

#### Step 8.1: Organize Reviewer Comments

Create `revision/reviewer-comments.md`:

1. Parse the decision letter and reviewer comments
2. Number each comment sequentially (R1-1, R1-2, R2-1, R2-2, etc.)
3. Categorize each comment:
   - **Must fix**: Factual errors, missing data, methodological concerns
   - **Should fix**: Reasonable suggestions that improve the paper
   - **Consider**: Optional suggestions, stylistic preferences
   - **Rebut**: Comments based on misunderstanding (requires polite explanation)

#### Step 8.2: Create Response Letter

Create `revision/response-letter.md`:

For each comment, use this format:

```
**Comment R1-1:** [Quote the reviewer's comment]

**Response:** [Your response]

**Changes made:** [Specific changes with page/line numbers, or explanation if no change]
```

**Rules for response letters:**
- Thank the reviewer for constructive feedback (once at the beginning, not per comment)
- Be specific about what was changed and where
- For rebuttals, acknowledge the reviewer's perspective, then explain with evidence
- Never be defensive or dismissive
- If a change was not made, explain why with references or data

#### Step 8.3: Implement Revisions

1. Track which sections need modification based on reviewer comments
2. Make changes in the relevant section files
3. Mark changed text (many journals require highlighted changes or a diff)
4. Roll back affected phases: re-run Humanize (Phase 4) and Quality Review (Phase 6) on modified sections
5. Update word counts and verify journal limits are still met

#### Step 8.4: Verify Revision Completeness

- [ ] Every reviewer comment has a response
- [ ] Every "Must fix" and "Should fix" item has been addressed
- [ ] Rebuttals are supported by evidence
- [ ] Changed text is marked/highlighted
- [ ] References updated if new citations added
- [ ] Abstract updated if results or conclusions changed
- [ ] Cover letter for resubmission drafted

## Section-Specific AI Guidelines

### What AI Should Do

| Section | AI Role |
|---------|---------|
| Literature search | Search, organize, summarize — user validates relevance |
| Methods | Draft based on user's data description — user verifies accuracy |
| Results | Structure and format — user provides the actual data |
| Case (Case Report) | Structure chronologically — user provides clinical details |
| Introduction | Draft background from literature — user refines narrative |
| Discussion | Suggest comparisons with literature — user controls interpretation |
| Abstract | Generate from full text — user ensures accuracy |
| References | Format and organize — user verifies completeness and authenticity |

### What AI Should NOT Do

- Fabricate data or statistics
- Invent citations (always verify with `WebSearch`)
- Write Results without user-provided data
- Write Case Presentation without user-provided clinical details
- Make clinical recommendations beyond the data
- Skip the user approval step at outline and title phases

## Status Tracking

Update `README.md` status after each phase. Use these status values:
- **Not Started**: Phase not begun
- **In Progress**: Phase actively being worked on (add details in Notes)
- **Draft Complete**: First draft finished, pending review
- **Done**: Phase completed and reviewed

Use the appropriate status tracker based on paper type:

**Original Article:**

| Phase | Status | Last Updated |
|-------|--------|-------------|
| Literature Search | Not Started | - |
| Outline | Not Started | - |
| Tables & Figures | Not Started | - |
| Methods & Results | Not Started | - |
| Introduction & Conclusion | Not Started | - |
| Discussion | Not Started | - |
| Abstract | Not Started | - |
| Title & Keywords | Not Started | - |
| Humanize | Not Started | - |
| References | Not Started | - |
| Declarations | Not Started | - |
| Quality Review | Not Started | - |
| Pre-Submission | Not Started | - |

**Case Report:**

| Phase | Status | Last Updated |
|-------|--------|-------------|
| Literature Search | Not Started | - |
| Outline | Not Started | - |
| Tables & Figures | Not Started | - |
| Case Presentation | Not Started | - |
| Discussion | Not Started | - |
| Introduction | Not Started | - |
| Abstract | Not Started | - |
| Title & Keywords | Not Started | - |
| Humanize | Not Started | - |
| References | Not Started | - |
| Declarations | Not Started | - |
| Quality Review | Not Started | - |
| Pre-Submission | Not Started | - |

**Review Article:**

| Phase | Status | Last Updated |
|-------|--------|-------------|
| Literature Search | Not Started | - |
| Outline | Not Started | - |
| Tables & Figures | Not Started | - |
| Thematic Sections | Not Started | - |
| Introduction | Not Started | - |
| Conclusion & Future Directions | Not Started | - |
| Abstract | Not Started | - |
| Title & Keywords | Not Started | - |
| Humanize | Not Started | - |
| References | Not Started | - |
| Declarations | Not Started | - |
| Quality Review | Not Started | - |
| Pre-Submission | Not Started | - |

**Systematic Review:**

| Phase | Status | Last Updated |
|-------|--------|-------------|
| Literature Search | Not Started | - |
| Outline | Not Started | - |
| Tables & Figures | Not Started | - |
| Methods (PRISMA) | Not Started | - |
| Results (PRISMA) | Not Started | - |
| Discussion | Not Started | - |
| Introduction | Not Started | - |
| Abstract | Not Started | - |
| Title & Keywords | Not Started | - |
| Humanize | Not Started | - |
| References | Not Started | - |
| Declarations | Not Started | - |
| Quality Review | Not Started | - |
| Pre-Submission | Not Started | - |

**Letter / Short Communication:**

| Phase | Status | Last Updated |
|-------|--------|-------------|
| Literature Search | Not Started | - |
| Outline | Not Started | - |
| Tables & Figures | Not Started | - |
| Condensed Draft | Not Started | - |
| Abstract | Not Started | - |
| Title & Keywords | Not Started | - |
| Humanize | Not Started | - |
| References | Not Started | - |
| Quality Review | Not Started | - |
| Pre-Submission | Not Started | - |

## Resuming a Project

When the user invokes this skill on an existing project directory:

1. **Read `README.md`** to understand current status, paper type, target journal, and research question
2. **Scan section files** to assess actual content state:
   - Read each section file that shows "In Progress" or "Draft Complete"
   - Check word count and completeness (empty sections, TODO markers, partial drafts)
   - Compare actual file state with the status tracker — the files are the source of truth
3. **Present a summary to the user**: "Here is where we left off: [status]. The next step is [phase]. Shall I continue?"
4. **Check for workflow updates**: Compare the README status table against the canonical phase list above. If phases are missing (e.g., old project created before "Humanize" was added), add them with "Not Started" status and inform the user
5. **Resume from the next incomplete phase**
6. **Update status tracker**

### Handling Mid-Project Changes

**Changing target journal**: If the user wants to change the target journal:
1. Update README.md Paper Info and Journal Requirements
2. Re-check: citation style, word limits, abstract format, reporting guideline
3. Reformat references if citation style changed
4. Check word counts against new limits
5. Update cover letter

**Adding data or revisions**: If the user has new data or reviewer feedback:
1. Identify which sections are affected
2. Roll back affected phases to "In Progress"
3. Re-run from that phase forward (including Humanize and Quality Review)

## Language Support

### English Papers
- Use standard academic English
- Follow target journal's style guide
- Flag awkward phrasing for user review

### Japanese Papers
- IMRAD形式は英語論文と同じ（Case Reportは例外: CARE形式）
- 「です・ます」ではなく「である」調
- 専門用語は原則として日本語（初出時に英語併記）
- 症例報告では「症例提示」「臨床経過」等の標準的な見出しを使用
- 論文の書き方ガイドが別途ある場合は参照のこと

## Reference Files

- `references/imrad-guide.md` - IMRAD structure and writing principles
- `references/section-checklist.md` - per-section quality checklist (Original Article + Case Report)
- `references/citation-guide.md` - citation formatting and management
- `references/reporting-guidelines.md` - CONSORT, STROBE, PRISMA, CARE summaries
- `references/humanizer-academic.md` - AI writing pattern detection (EN 18 + JP 13 patterns)
- `templates/project-init.md` - project README template (Original Article)
- `templates/project-init-case.md` - project README template (Case Report)
- `templates/literature-matrix.md` - literature comparison matrix
- `templates/methods.md` - Methods section writing guide (Original Article)
- `templates/results.md` - Results section writing guide (Original Article)
- `templates/case-report.md` - Case presentation writing guide (Case Report, CARE-compliant)
- `templates/case-introduction.md` - Case Report introduction guide
- `templates/case-abstract.md` - Case Report abstract guide (CARE format)
- `templates/introduction.md` - Introduction section writing guide (Original Article)
- `templates/discussion.md` - Discussion section writing guide
- `templates/conclusion.md` - Conclusion writing guide
- `templates/abstract.md` - Abstract writing guide (Original Article)
- `templates/cover-letter.md` - Cover letter template
- `templates/submission-ready.md` - Pre-submission checklist template
- `templates/sr-outline.md` - Systematic review outline (PRISMA 2020)
- `templates/declarations.md` - Declarations templates (Ethics, COI, Funding, AI, CRediT)
- `templates/graphical-abstract.md` - Graphical abstract design guide
- `references/ai-disclosure.md` - AI tool disclosure guide (ICMJE 2023)
- `references/tables-figures-guide.md` - Tables and figures creation guide
- `references/keywords-guide.md` - Keywords and MeSH term selection guide
- `references/supplementary-materials.md` - Supplementary materials strategy guide
- `references/citation-verification.md` - Citation authenticity verification guide
- `references/pubmed-query-builder.md` - PubMed search query construction guide

## External References

- ICMJE Recommendations (Uniform Requirements for Manuscripts)
- EQUATOR Network (reporting guidelines)
- CONSORT 2010 (RCTs)
- STROBE (observational studies)
- PRISMA 2020 (systematic reviews)
- CARE (case reports)
- STARD (diagnostic accuracy studies)
- matsuikentaro1/humanizer_academic (English academic AI pattern detection)
- humanizer-ja (Japanese AI writing pattern detection)
- Wikipedia: Signs of AI writing

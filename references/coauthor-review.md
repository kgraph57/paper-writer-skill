# Co-Author Review Workflow

## Overview

This guide provides a structured workflow for managing co-author contributions, review cycles, and final approval before manuscript submission. It covers the CRediT taxonomy for contribution tracking, communication templates, and conflict resolution.

---

## ICMJE Authorship Criteria

Before listing co-authors, verify that each person meets ALL FOUR ICMJE criteria:

1. **Substantial contributions** to the conception or design of the work; or the acquisition, analysis, or interpretation of data for the work; AND
2. **Drafting the work** or revising it critically for important intellectual content; AND
3. **Final approval** of the version to be published; AND
4. **Agreement to be accountable** for all aspects of the work in ensuring that questions related to the accuracy or integrity of any part of the work are appropriately investigated and resolved.

All four criteria must be met. Contributors who do not meet all four should be listed in the Acknowledgments section.

### Common Pitfalls
- **Gift authorship**: Adding someone who did not contribute substantially (e.g., department chair who only provided lab space)
- **Ghost authorship**: Omitting someone who contributed substantially (e.g., a medical writer)
- **Coercion authorship**: Being pressured to add someone for political reasons

---

## CRediT (Contributor Roles Taxonomy)

Use the CRediT taxonomy to transparently document each author's contributions:

| Role | Definition | Degree |
|------|-----------|--------|
| Conceptualization | Ideas; formulation of research goals and aims | Lead / Supporting / Equal |
| Data curation | Management activities for research data | Lead / Supporting / Equal |
| Formal analysis | Statistical, mathematical, computational analysis | Lead / Supporting / Equal |
| Funding acquisition | Financial support for the project | Lead / Supporting / Equal |
| Investigation | Conducting research and investigation process | Lead / Supporting / Equal |
| Methodology | Development or design of methodology | Lead / Supporting / Equal |
| Project administration | Management and coordination responsibility | Lead / Supporting / Equal |
| Resources | Provision of study materials, computing resources | Lead / Supporting / Equal |
| Software | Programming, software development | Lead / Supporting / Equal |
| Supervision | Oversight and leadership responsibility | Lead / Supporting / Equal |
| Validation | Verification of results/experiments | Lead / Supporting / Equal |
| Visualization | Preparation of figures and data presentation | Lead / Supporting / Equal |
| Writing - original draft | Preparation of the initial draft | Lead / Supporting / Equal |
| Writing - review & editing | Critical review, commentary, revision | Lead / Supporting / Equal |

### CRediT Tracking Template

```markdown
| Author | Conceptualization | Methodology | Investigation | Analysis | Writing-OD | Writing-RE | Supervision |
|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| [Author 1] | Lead | Lead | Supporting | Lead | Lead | Lead | - |
| [Author 2] | Supporting | Lead | Lead | Supporting | Supporting | Equal | - |
| [Author 3] | - | Supporting | Lead | Lead | - | Supporting | - |
| [Author 4] | Supporting | - | - | - | - | Supporting | Lead |
```

---

## Review Request Communication

### English Email Template

```
Subject: Manuscript Review Request - [Short Title] - Response by [Date]

Dear [Co-author Name],

I hope this message finds you well. I am writing to request your review
of our manuscript titled:

"[Full Manuscript Title]"

Target journal: [Journal Name]
Submission deadline: [Date]

I have attached the current draft (version [X.X], dated [Date]).
Please find the manuscript and supplementary materials in the attached files.

I would appreciate your feedback on the following:
1. Scientific accuracy and completeness of your contributed sections
2. Overall flow and logical structure
3. Any factual errors or missing references
4. Figures and tables relevant to your expertise
5. Your approval of the author list and contribution statement

Could you please return your comments by [Date]?

If you have any questions or need additional time, please let me know.

Thank you for your contribution to this work.

Best regards,
[Corresponding Author Name]

Attachments:
- [Manuscript_v[X.X]_[Date].docx]
- [Supplementary_materials.docx]
- [Author_contribution_form.xlsx]
```

### Japanese Email Template

```
件名：論文原稿のご確認依頼 - [略題] - [日付]までにご返信ください

[共著者名] 先生

いつもお世話になっております。[所属]の[氏名]です。

下記の論文原稿がまとまりましたので、ご確認をお願いいたします。

論文タイトル：「[論文タイトル]」
投稿予定雑誌：[雑誌名]
投稿予定日：[日付]

添付ファイルに原稿（バージョン[X.X]、[日付]付）を
お送りいたします。

以下の点についてご確認いただけますと幸いです：
1. ご担当部分の科学的正確性と完全性
2. 全体的な論理構成と流れ
3. 事実関係の誤りや参考文献の不足
4. ご専門に関連する図表の適切性
5. 著者リストおよび著者貢献の記載内容

[日付]までにコメントをいただけますと助かります。

ご質問やお時間が必要な場合は、ご遠慮なくお知らせください。

何卒よろしくお願い申し上げます。

[責任著者名]
[所属]
[連絡先]

添付資料：
- [Manuscript_v[X.X]_[Date].docx]
- [Supplementary_materials.docx]
- [著者貢献記録表.xlsx]
```

---

## Feedback Integration Process

### Step 1: Collect Feedback

```
For each co-author:
- [ ] Received comments by deadline
- [ ] If no response: send reminder at 3 days, 7 days, 14 days
- [ ] Track which version they reviewed
- [ ] Note whether they used track changes or inline comments
```

### Step 2: Categorize Feedback

Organize all co-author comments into categories:

| Category | Priority | Action |
|----------|----------|--------|
| Factual errors | Critical | Fix immediately |
| Missing references | High | Add references |
| Structural suggestions | Medium | Evaluate and decide |
| Writing style preferences | Low | Consider if consistent |
| Contradictory feedback | Requires discussion | Schedule call/meeting |

### Step 3: Integrate Changes

```
1. Create a new version (e.g., v2.0) for integrated changes
2. Address all Critical and High priority items
3. For Medium/Low items, use judgment (corresponding author decides)
4. For contradictory feedback, discuss with involved co-authors
5. Document all changes in a change log
```

### Step 4: Circulate Updated Version

```
Send updated manuscript to all co-authors with:
- Change log summarizing what was modified
- Response to each co-author's comments
- Request for final approval (not another full review)
- Deadline for final sign-off
```

---

## Version Control for Manuscript Drafts

### File Naming Convention

```
[ProjectName]_v[Major].[Minor]_[Date]_[Status].docx

Examples:
AI-Diagnosis_v0.1_20260101_initial-draft.docx
AI-Diagnosis_v0.2_20260115_methods-added.docx
AI-Diagnosis_v1.0_20260201_first-complete-draft.docx
AI-Diagnosis_v1.1_20260210_after-coauthor-review.docx
AI-Diagnosis_v2.0_20260301_revision-round1.docx
AI-Diagnosis_v2.0_20260301_SUBMITTED.docx
```

### Version Numbering Guide

| Version | Meaning |
|---------|---------|
| v0.x | Drafting phase (incomplete sections) |
| v1.0 | First complete draft |
| v1.x | Revisions based on co-author feedback |
| v2.0 | Submission-ready version |
| v2.x | Post-review revisions |
| v3.0 | Resubmission after peer review |

### Change Log Template

```markdown
## Change Log

### v1.1 (2026-02-15) - Co-author Review Integration

Changes from Author 2 feedback:
- Updated Table 2 with corrected values (Methods section)
- Added 3 references to Discussion
- Revised paragraph 2 of Introduction for clarity

Changes from Author 3 feedback:
- Corrected statistical method description (Methods section)
- Added subgroup analysis results (Results section)

Changes from Author 4 feedback:
- No changes requested (approved as-is)

Unresolved:
- Author 2 and Author 3 disagree on interpretation of Figure 3
  -> Scheduled discussion for 2026-02-18
```

---

## Timeline Management

### Recommended Timeline (Working Backwards from Submission)

| Week | Task | Responsible |
|------|------|-------------|
| W-8 | Complete first draft (v1.0) | Lead author |
| W-7 | Internal review by lead author | Lead author |
| W-6 | Send to co-authors for review | Corresponding author |
| W-4 | Deadline for co-author feedback | All co-authors |
| W-3 | Integrate feedback, create v1.1 | Lead author |
| W-2 | Circulate v1.1 for final approval | Corresponding author |
| W-1 | Collect final approvals | Corresponding author |
| W-0.5 | Format for journal, prepare cover letter | Lead author |
| W-0 | Submit | Corresponding author |

### Reminder Schedule

```
Day 0:  Send manuscript for review
Day 3:  Check if all co-authors acknowledged receipt
Day 7:  First reminder to non-responders
Day 14: Second reminder (escalate: call or message)
Day 21: Final reminder with firm deadline
Day 28: Deadline (as originally communicated)
```

### When a Co-Author Is Unresponsive

1. Send reminders at increasing frequency (see above)
2. Try alternative communication channels (phone, in-person)
3. If no response after 4 weeks:
   - Document all contact attempts
   - Consult with other co-authors
   - Consider whether the person meets ICMJE criteria
   - If they do not meet criteria: move to Acknowledgments
   - If they do meet criteria: make final attempt, then escalate to department/institution

---

## Handling Disagreements Between Co-Authors

### Common Disagreement Types

1. **Data interpretation**: Co-authors disagree on what the results mean
2. **Methodology**: Disagreement about analytical approach
3. **Authorship order**: Disputes about who contributed more
4. **Inclusion/exclusion of data**: Whether certain results should be reported
5. **Tone/framing**: How strongly to state conclusions

### Resolution Process

```
Step 1: Identify the specific point of disagreement
Step 2: Gather evidence supporting each position
Step 3: Discuss (meeting preferred over email for complex issues)
Step 4: Corresponding author proposes resolution
Step 5: If unresolved -> seek input from a neutral expert
Step 6: If still unresolved -> follow institution's research integrity policy
Step 7: Document the final decision and rationale
```

### Guidelines for Resolution

- **Data interpretation**: Present both interpretations in the Discussion; let the reader decide
- **Methodology**: Defer to the expert in that method; consider sensitivity analyses
- **Authorship order**: Use CRediT to objectively assess contributions; refer to ICMJE
- **Data inclusion**: Err on the side of transparency; report all pre-specified outcomes
- **Tone**: Be conservative; let the data speak

---

## Final Approval Workflow Before Submission

### Pre-Submission Checklist

```markdown
## Final Approval Checklist

### Content
- [ ] All co-authors have reviewed the final version
- [ ] All co-authors have provided written approval (email is sufficient)
- [ ] Author list is correct (names, order, affiliations)
- [ ] CRediT contributions are documented and agreed upon
- [ ] Corresponding author is designated and confirmed
- [ ] All co-authors agree with the target journal

### Compliance
- [ ] ICMJE forms completed by all authors (if required by journal)
- [ ] Conflict of interest disclosures collected from all authors
- [ ] Funding statements reviewed and approved by all authors
- [ ] Data availability statement agreed upon
- [ ] Ethics approval documented

### Final Sign-Off
- [ ] Author 1: [Name] - Approved on [Date] via [email/meeting]
- [ ] Author 2: [Name] - Approved on [Date] via [email/meeting]
- [ ] Author 3: [Name] - Approved on [Date] via [email/meeting]
- [ ] Author 4: [Name] - Approved on [Date] via [email/meeting]
```

### Final Approval Email Template (English)

```
Subject: FINAL APPROVAL REQUEST - [Short Title] - Please respond by [Date]

Dear Co-authors,

The manuscript is now ready for submission. Please find the final version
(v[X.X]) attached.

Target journal: [Journal Name]
Planned submission date: [Date]

Please confirm the following by replying to this email:

1. I have reviewed the final manuscript and approve its submission.
2. I confirm that my contributions are accurately described.
3. I confirm that I meet the ICMJE authorship criteria.
4. I have disclosed all potential conflicts of interest.
5. I agree with the author order as listed.

A simple "I approve" reply is sufficient if you agree with all points above.

If you have any remaining concerns, please contact me immediately.

Thank you for your contributions to this work.

Best regards,
[Corresponding Author]
```

### Final Approval Email Template (Japanese)

```
件名：【最終承認依頼】[略題] - [日付]までにご返信ください

共著者の皆様

論文の最終版が完成いたしました。
添付の最終原稿（v[X.X]）をご確認ください。

投稿先雑誌：[雑誌名]
投稿予定日：[日付]

以下の点をご確認の上、本メールにご返信ください：

1. 最終原稿を確認し、投稿を承認します。
2. 著者貢献の記載内容が正確であることを確認します。
3. ICMJE著者資格基準を満たしていることを確認します。
4. 利益相反について適切に開示しました。
5. 記載されている著者順に同意します。

上記すべてにご同意いただける場合、「承認します」とのご返信で結構です。

ご懸念がございましたら、至急ご連絡ください。

何卒よろしくお願い申し上げます。

[責任著者名]
[所属]
[連絡先]
```

---

## Tracking Spreadsheet Template

Create a shared spreadsheet with these columns:

```
| Author | Email | ORCID | Affiliation | CRediT Roles | v1.0 Sent | v1.0 Feedback | v1.1 Sent | Final Approval | ICMJE Form | COI Form |
|--------|-------|-------|-------------|--------------|-----------|---------------|-----------|----------------|------------|----------|
| | | | | | [Date] | [Date/Pending] | [Date] | [Yes/No/Date] | [Done/Pending] | [Done/Pending] |
```

This provides a single-view dashboard for managing the entire co-author workflow.

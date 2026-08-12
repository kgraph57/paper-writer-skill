# Case Study: Discovery → Draft → Humanize → Adversarial Catch

A two-minute read of one illustrative pass through the skill's pipeline. The clinical spark is **PHI-free and fictional** — built to show the product shape, not a real patient. Every template and checklist named below already exists in this repository.

> **The loop:** Input → Discovery → Weak path → Gated path → Humanize → Adversarial → Proof

## 1. Input — the spark a clinician actually has

Illustrative, de-identified notes (entire input; no cleanup):

```text
Want a CARE case report.
Non-diabetic adult started a GLP-1 agonist for weight management.
Within 3 weeks: recurrent symptomatic hypoglycemia, workup otherwise unrevealing.
Stopped the drug; events resolved.
Have labs timeline + meds list (de-identified). IRB waiver for single case on file.
Target journal leaning BMJ Case Reports. Language: English.
```

## 2. Discovery — forge questions, then lock the IDEA

Phase −1 does not open a blank Methods section. It forges FINER-scored candidates, runs a novelty skim against live literature, and stops at the human gates:

| Candidate | FINER sketch | Novelty skim (illustrative) |
| --- | --- | --- |
| Q1. Mechanism review of GLP-1 and glucose in non-diabetics | Broad; weak "case" fit | Crowded review space |
| **Q2. CARE report: temporal association + negative workup + dechallenge** | Feasible with on-hand data | Room for a well-documented single case |
| Q3. Series protocol for prospective capture | Needs resources not available | Wrong product for this spark |

**Human locks Q2** (💡 IDEA). **Human confirms** the lab/meds extract is real and de-identified (📊 DATA). The skill does not invent glucose values or a patient.

Artifacts used: `templates/research-question.md`, `templates/project-init-case.md`, `references/novelty-check.md`, `references/ai-for-science-model.md`.

## 3. Weak path — "just write the paper"

If you skip gates and ask a generic model for an abstract, you often get significance inflation and promotional language (patterns the repo's humanizer is built to kill):

```text
This landmark case underscores a pivotal challenge in the evolving
therapeutic landscape of GLP-1 agonists, highlighting the crucial need
for heightened clinical vigilance in non-diabetic populations.
```

Accurate vibe, useless science writing. No timeline. No CARE structure. No limits stated.

## 4. Gated path — outline, exhibits, then prose

With gates on:

1. **Literature matrix** (≥10 sources, DOIs checked) before outline approval.
2. **Outline** mapped to CARE sections; human approval required.
3. **Tables/figures before prose** — e.g. Table 1 timeline of glucose / meds; Figure 1 clinical course.
4. **Draft in writing order** (Case presentation → Discussion → … → Abstract → Title).
5. Stage-gates refuse to proceed on FAIL (feedback → fixer → re-check, max 3).

Relevant templates: `templates/case-report.md`, `templates/case-abstract.md`, `templates/literature-matrix.md`, `references/reporting-guidelines.md` (CARE).

## 5. Humanize — two real pattern fixes

From `references/humanizer-academic.md`:

| Pattern | Before | After |
| --- | --- | --- |
| Significance inflation | "represents a pivotal challenge in the evolving landscape" | "is uncommon but clinically important when hypoglycemia appears after GLP-1 initiation in a non-diabetic adult" |
| Superficial -ing analysis | "glucose normalized after cessation, highlighting the drug's role" | "glucose normalized after cessation (dechallenge); rechallenge was not performed." |

Phase 4's gate requires high-priority AI patterns = 0 before references/quality review.

## 6. Adversarial review — catch the overclaim

`references/adversarial-review.md` red-teams the central claim. Illustrative finding:

> **Overclaim:** Abstract implies causality ("GLP-1 caused hypoglycemia") from a single uncontrolled case.
> **Fix:** Frame as temporal association + dechallenge; state that causality cannot be proven; list alternative explanations considered and why they were less likely.
> **Verdict:** Revise (not KILL) — the IDEA is intact; the wording overreached.

A true **KILL** (fatal design/ethics/data problem) would return to Phase −1 instead of polishing a bad paper.

## 7. Proof — what already ships in-repo

You do not need to trust a staged "accepted paper." Reproduce the workflow pieces that exist today:

| Piece | Where |
| --- | --- |
| Operating model (IDEA/DATA sovereignty) | `references/ai-for-science-model.md` |
| Novelty + adversarial guides | `references/novelty-check.md`, `references/adversarial-review.md` |
| CARE / case templates | `templates/case-report.md`, `templates/case-abstract.md`, `templates/case-introduction.md` |
| Humanizer patterns | `references/humanizer-academic.md` |
| Data rules (raw gitignored, no PHI in chat) | `templates/data-management.md`, `SECURITY.md` |
| Compile / word-count utilities | `scripts/compile-manuscript.sh`, `scripts/word-count.sh` |

```bash
# after install / clone
npx skills add kgraph57/paper-writer-skill
# then in Claude Code / your agent:
# "Start a CARE case report from these de-identified notes…"
```

## What this case study deliberately does *not* claim

- No journal acceptance, impact factor, or "N doctors use this."
- No real patient identifiers or real lab dumps.
- No promise that the skill replaces IRB review or auto-submits to journals.

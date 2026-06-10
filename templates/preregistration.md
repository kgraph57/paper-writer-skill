# Pre-Registration Template
## Phase −1 Integrity Gate — Freeze Before the 📊 Data Gate

---

## 1. Why Pre-Register

An AI-accelerated research loop is a HARKing machine unless you lock it. The
garden-of-forking-paths problem — where hundreds of plausible analysis choices
produce whatever p-value you need — already existed in human-speed science.
Add a co-scientist running model selection, covariate permutations, and outcome
re-operationalizations at machine speed (§5.1 of `references/ai-for-science-model.md`)
and the multiverse expands by orders of magnitude. The only discipline that closes
the gate is to **freeze the hypotheses and the exact primary analysis plan before
any outcome data are examined** — in a timestamped, immutable, public record.
After that lock, pre-registered analyses are confirmatory; everything else is
exploratory and must be labeled as such. Without this gate, a fast loop produces
confident slop, indistinguishable from Sakana AI Scientist v2's output.

---

## 2. Placement in the Research Loop

```
Phase −1: DISCOVERY
  ├── research question          (templates/research-question.md)
  ├── novelty check              (references/novelty-check.md)
  ├── study design + power       (templates/study-design.md)  ← input to this file
  └── 🔒 PRE-REGISTRATION LOCK   ← YOU ARE HERE
          │  (plan is now frozen; timestamp obtained)
          │
  📊 DATA GATE  ← data collection begins here (or, for retrospective data,
                   outcome data examination begins here — see §9)
          │
  Phases 0–3: analysis (bound to the frozen plan) → draft (IMRAD)
```

**Stop rule:** Data are not analyzed for outcomes until the registration record is
submitted and the timestamp is obtained. The timestamp is the evidence of the lock.

---

## 3. Which Registry

| Study type | Registry | Mandatory vs. recommended | Timing |
|---|---|---|---|
| Interventional clinical trial (Japan) | **jRCT** (jrct.niph.go.jp) | **Mandatory** under 臨床研究法 (Clinical Trials Act, 2018) for specified / non-specified clinical studies using unapproved drugs/devices or off-label use. See `references/clinical-trial-registration.md`. | Before first enrollment |
| Interventional clinical trial (Japan, UMIN legacy) | **UMIN-CTR** (umin.ac.jp/ctr/) | Recommended; widely accepted by ICMJE journals. Being superseded by jRCT for new trials. | Before first enrollment |
| Interventional clinical trial (international) | **ClinicalTrials.gov** | Mandatory for ICMJE submission; required by US law for applicable trials | Before first enrollment |
| Systematic review / meta-analysis | **PROSPERO** (crd.york.ac.uk/prospero/) | Strongly recommended; see `templates/sr-prospero.md` for the full template — do not duplicate here | Before screening begins |
| Observational / cross-sectional / cohort / case-control | **OSF Registries** (osf.io/registries) | Recommended | Before data collection; if retrospective, before outcome examination |
| Prediction model / secondary data analysis | **OSF** or **AsPredicted** (aspredicted.org) | Recommended | Before outcome examination |
| Purely exploratory / hypothesis-generating | No registry required | — | N/A |
| Animal / preclinical | **preclinicaltrials.eu** | Recommended | Before experiment |

> Japan-specific note: 臨床研究法 requires jRCT registration for 特定臨床研究
> (specified clinical research). Observational studies and retrospective chart
> reviews are typically outside its scope, but confirm with your IRB.

---

## 4. The Pre-Registration Record Template

Copy this block into your OSF / AsPredicted / UMIN-CTR / jRCT form.
Complete every field before submitting. Fields marked **(required)** have no
acceptable blank.

---

```markdown
## Pre-Registration Record

### A. Administrative

- **Title** (identical to the manuscript working title): {{PREREG_TITLE}}
- **Registry**: {{REGISTRY_NAME}}
- **Registration number** (assigned after submission): {{REG_NUMBER}}
- **Registration timestamp** (UTC): {{TIMESTAMP}}
- **Corresponding PI**: {{PI_NAME}} <{{PI_EMAIL}}>
- **Co-investigators**: {{COINVESTIGATORS}}
- **Study design input document**: templates/study-design.md, version {{VERSION}},
  dated {{DESIGN_DATE}}

---

### B. Hypotheses  **(required)**

State directionally. Vague hypotheses cannot be confirmed or disconfirmed.

- **H0 (null)**: {{H0 — e.g., "There is no difference in 30-day readmission
  rate between Group A and Group B."}}
- **H1 (alternative, directional if possible)**: {{H1 — e.g., "Group A has a
  lower 30-day readmission rate than Group B."}}
- **Direction of expected effect**: [ ] one-sided  [ ] two-sided  Reason: {{REASON}}

For secondary hypotheses, list separately as H2, H3, etc., each with own H0/H1.

**Estimand variant — descriptive / estimation primaries.** Not every primary aim is a test. For a descriptive/estimation primary (a proportion or mean you are *measuring*, not comparing against a null), do NOT force a directional H0/H1 — the estimate IS the result. Instead state:

- **Estimand**: {{the quantity being estimated — e.g., "proportion of caregivers who consulted a generative-AI tool before the visit, in the full valid-response set"}}
- **Precision target**: {{the CI half-width you are powering for — e.g., "95% Wilson CI half-width ≤ ±4.5 pp at an expected p ≈ 0.30, N = 400" (see study-design.md §5.0)}}
- **H0**: *Not applicable — estimation, not testing.*

A study may register **two descriptive co-primaries this way** without a multiplicity penalty (see §D carve-out); each is justified by its own precision target, not by a shared α.

---

### C. Study Design  **(required)**

- **Design**: {{RCT / prospective cohort / retrospective cohort / cross-sectional
  / case-control / other}}
- **Setting**: {{SETTING}}
- **Planned sample size**: N = {{N}}  (see power calculation in §F)
- **Data-collection start date** (must be AFTER lock): {{START_DATE}}
- **Data-collection end date**: {{END_DATE}}
- **Inclusion criteria**: {{INCLUSION}}
- **Exclusion criteria**: {{EXCLUSION}}

---

### D. Primary Outcome  **(required — ONE only, unless the descriptive carve-out applies)**

> Rule: if you have more than one primary outcome, you are running more than one
> study. Pick one. Pre-register the others as secondary.
>
> **Carve-out — descriptive co-primaries (no multiplicity penalty).** Purely
> descriptive co-primaries (proportions/means reported with a CI) are allowed
> **without** a multiplicity penalty **when neither is tested against a null** —
> they are estimation targets, not tests, so there is no shared type-I error to
> split (mirrors `templates/study-design.md` §3 and §5.0; use the §B estimand
> variant for each). This holds only while every co-primary stays descriptive: if
> any is compared against a reference value or against the other, it becomes a test
> and the ONE-only rule plus §H multiplicity correction re-apply.
> **Require an explicit one-line justification here**, e.g.: "Two descriptive
> co-primaries (AI-consultation prevalence; pre-visit information-source mix); each
> is an estimand with its own precision target (§B); neither is tested against a
> null, so no multiplicity penalty is taken."

- **Outcome name**: {{OUTCOME_NAME}}
- **Operationalization** (exactly what is measured, how, by whom, at what time
  point; precise enough that a stranger could reproduce it):
  {{OPERATIONALIZATION — e.g., "30-day all-cause readmission to any hospital,
  ascertained by electronic medical record review at day 30 ± 2 days post-discharge,
  confirmed by a blinded research assistant using ICD-10 codes. Counted as binary
  event (yes/no)."}}
- **Source / instrument**: {{SOURCE}}
- **Timing**: {{TIMING}}

---

### E. Secondary Outcomes

List each with the same precision as the primary. These will be reported with
multiplicity correction (§H).

| # | Outcome | Operationalization | Timing |
|---|---|---|---|
| S1 | {{NAME}} | {{OPERATIONALIZATION}} | {{TIMING}} |
| S2 | {{NAME}} | {{OPERATIONALIZATION}} | {{TIMING}} |

---

### F. Sample Size and Stopping Rule  **(required)**

- **Effect size assumed**: {{EFFECT_SIZE}} (source: {{CITE OR RATIONALE}})
- **Power**: {{POWER — e.g., 80%}}
- **Alpha**: {{ALPHA — e.g., 0.05, two-sided}}
- **Calculated N**: {{N_PER_ARM}} per arm / {{N_TOTAL}} total
- **Attrition assumed**: {{ATTRITION%}}; inflated N: {{N_INFLATED}}
- **Stopping rule** (for RCTs or sequential designs): {{STOPPING_RULE or "Not
  applicable — fixed sample design."}}
- **Software / function used**: {{e.g., R pwr::pwr.t.test(); G*Power 3.1}}

---

### G. Primary Analysis Plan  **(required — fully specified)**

> This is the single most important field. A stranger with access to the dataset
> must be able to run this analysis from this description alone.

- **Statistical model**: {{e.g., "Logistic regression"}}
- **Outcome variable**: {{VARIABLE_NAME_IN_DATASET}}
- **Primary predictor / treatment variable**: {{VARIABLE_NAME}}
- **Adjustment set / covariates** (list each, with justification):
  1. {{COVARIATE_1}} — {{REASON}}
  2. {{COVARIATE_2}} — {{REASON}}
- **Test / estimand**: {{e.g., "Wald test on the treatment coefficient; odds ratio
  with 95% CI"}}
- **Significance threshold**: α = {{ALPHA}}, {{one-sided / two-sided}}
- **Software and package version**: {{e.g., R 4.4.0, glm(); Stata 18, logistic}}
- **Handling of the analysis**: {{e.g., "intention-to-treat primary; per-protocol
  sensitivity"}}

---

### H. Multiplicity Correction  **(required if >1 outcome)**

- **Method**: {{e.g., Bonferroni, Benjamini-Hochberg FDR, hierarchical testing}}
- **Applied to**: {{primary only / all pre-specified outcomes / subgroup tests}}
- **Adjusted threshold for secondary outcomes**: α' = {{ALPHA_ADJUSTED}}

**Regime — "Exploratory analytic surface, no correction."** For a pilot whose
adjusted/association analyses are all EPV-limited and exploratory (study-design.md
§5.5), the honest move is **no multiplicity correction — because nothing here is
confirmatory**. To use this regime without it becoming a fishing licence:

- **Pre-specify a CLOSED list** of which exploratory tests may even appear in the
  abstract or conclusion. Anything not on this list cannot surface there.

| # | Exploratory test (closed list) | May appear in abstract/conclusion? |
|---|---|---|
| X1 | {{e.g., AI-use × caregiver age, adjusted Firth OR}} | Yes — as hypothesis-generating only |
| X2 | {{e.g., delayed-care count by source}} | No — supplementary table only |

- **None is a "finding."** State in the record: *"No exploratory result is reported
  as a finding; all are hypothesis-generating and require prospective replication."*
- **Estimate + CI only; suppress p.** Prefer reporting the estimate with its CI and
  **omit the p-value** for exploratory tests, so no reader (or co-scientist) can
  back-door a significance claim out of an uncorrected surface.

This regime pairs with the §D descriptive carve-out: the descriptive co-primaries
are confirmatory-by-precision, and *everything else* lives on this uncorrected
exploratory surface. The split is enforced by the Firewall table (§5).

---

### I. Missing-Data Plan  **(required)**

- **Expected missingness**: {{RATE%}} in {{VARIABLE}}
- **Mechanism assumption**: {{MCAR / MAR / MNAR; rationale}}
- **Primary missing-data approach**: {{e.g., "Multiple imputation by chained
  equations (MICE), m = 20 imputations, R mice package"}}
- **Sensitivity analysis**: {{e.g., "Complete-case analysis as sensitivity; pattern
  mixture model for MNAR sensitivity"}}

---

### J. Pre-Specified Subgroup Analyses

> Only subgroups with a plausible biological/clinical rationale should be
> pre-specified. Fishing is what the EXPLORATORY section is for.

| Subgroup | Variable | Cut-point | Rationale | Test for interaction? |
|---|---|---|---|---|
| {{SUBGROUP_1}} | {{VARIABLE}} | {{CUT}} | {{RATIONALE}} | Yes / No |
| {{SUBGROUP_2}} | {{VARIABLE}} | {{CUT}} | {{RATIONALE}} | Yes / No |

Subgroup analyses that do not appear in this table are **exploratory**.

---

### K. Exploratory Analyses (declared in advance)

List analyses that will be conducted but are explicitly labeled hypothesis-generating.
These cannot yield confirmatory claims regardless of their p-values.

- {{EXPLORATORY_1 — e.g., "Association between X and Y in the full cohort,
  unadjusted; for hypothesis generation only."}}
- {{EXPLORATORY_2}}

**Confirmatory / Exploratory Firewall (drop-in — fill one column per analysis class).**
This anti-HARKing table binds each analysis to what it is *allowed to claim* before
any data are seen. Columns = the descriptive co-primary (§D carve-out) vs. the
uncorrected exploratory surface (§H regime). Fill it as part of the frozen record:

| Row | Descriptive co-primary | Exploratory analytic surface |
|---|---|---|
| **What it is** | Estimand (proportion/mean + CI); estimation, not testing | Adjusted/association model on an EPV-limited set |
| **Inference allowed** | Point estimate with precision; "we estimate p = X (95% CI …)" | "Pattern consistent with …; hypothesis-generating only" |
| **p-value use** | None — no null is tested | **Suppressed** — estimate + CI only |
| **CI use** | Primary inferential output (Wilson) | Reported, but not as evidence of an effect |
| **Primary finding in abstract?** | Yes | No — only the closed-list items (§H), labeled hypothesis-generating |
| **Causal claim?** | No (descriptive) | No — association only |
| **Requires replication?** | No (precision pre-met) | Yes — always, prospectively |

> This is the per-analysis-class twin of the project-level table in §5; keep the two
> consistent. Any analysis that cannot be placed in one of these columns before the
> lock is, by definition, exploratory.

---

### L. Data-Collection Confirmation  **(required)**

- [ ] Data collection has NOT yet begun (prospective)
- [ ] Data exist but outcome variables have NOT yet been examined (retrospective —
  see §9 caveat)
- Date of this declaration: {{DATE}}
- Declared by: {{NAME, ROLE}}
```

---

## 5. The Confirmatory / Exploratory Firewall

| Dimension | Pre-registered (confirmatory) | Not pre-registered (exploratory) |
|---|---|---|
| **What it is** | Analysis specified in the frozen record before data examination | Anything added after the lock, regardless of reason |
| **Inference allowed** | "We reject H0 (p = X). This supports [directional claim]." | "This is a hypothesis-generating observation. Replication required." |
| **CI / p-value use** | Standard frequentist or Bayesian inference | Report descriptively; no claims of significance |
| **Manuscript placement** | Results §, primary table | Results §, secondary table, clearly labeled "Exploratory" |
| **Can it be a primary finding?** | Yes | No |
| **Requires replication?** | No (confirmatory if plan was well-powered) | Yes, always |
| **Journal disclosure** | Cite registration number | Disclose as post-hoc / exploratory |

**Hard rule:** Any analysis not in the frozen plan is exploratory, full stop. This
includes: (a) post-hoc covariate additions; (b) outcome redefinition; (c) subgroups
not in §J; (d) sensitivity analyses not pre-specified; (e) models suggested by
patterns in the data. None of these are forbidden — they are scientifically
valuable. They just cannot carry a confirmatory claim.

---

## 6. Deviation Handling

Deviations from the registered plan are expected; hiding them is the problem.

**Rule:** Every deviation is disclosed in the Methods section. The registered plan
and the actual analysis are compared side-by-side. Undisclosed deviations are
misconduct.

### Deviations Log Template

Keep this file alongside your analysis code (e.g., `deviations-log.md` in the
project repo):

```markdown
## Deviations from Pre-Registered Plan

| # | Date | Section deviated from | Planned | Actual | Reason | Impact on inference |
|---|---|---|---|---|---|---|
| D1 | {{DATE}} | §G Primary analysis | {{PLANNED}} | {{ACTUAL}} | {{REASON}} | {{e.g., "Conservative; increases Type II error"}} |
| D2 | {{DATE}} | §D Primary outcome | {{PLANNED}} | {{ACTUAL}} | {{REASON}} | {{e.g., "Outcome now composite; increases power, changes estimand"}} |
```

**Methods section disclosure template:**

```
The pre-registered analysis plan ({{REGISTRY}}, {{REG_NUMBER}}) was followed with
the following deviations: [1] {{DEVIATION_1 — what changed, why, direction of
potential bias}}. [2] {{DEVIATION_2}}. The original pre-registered analyses are
reported in Supplementary Table S{{N}} for comparison.
```

---

## 7. Registered Reports

A Registered Report (RR) is the strongest form of pre-registration: the journal
reviews and accepts the Introduction + Methods in principle **before data
collection**, guaranteeing publication regardless of the result. This structurally
eliminates publication bias. Pursue an RR when:

- The study is powered for a null result that would be scientifically important
- The research question is contentious and you anticipate publication resistance
- The team is willing to pre-commit publicly to a design that may not yet be fully
  optimized

List of journals offering RRs: cos.io/rr. For clinical journals in Japan, BMJ Open
and PLOS ONE are accessible options with RR tracks.

---

## 8. Verification Checklist (Before the 📊 Data Gate)

Complete this before any outcome data are examined or analyzed.

- [ ] Registration submitted to the correct registry (§3 decision table)
- [ ] Timestamp obtained and recorded in the project README
- [ ] Registration number inserted into the manuscript shell (Methods)
- [ ] Primary outcome: exactly ONE, fully operationalized (§D)
- [ ] Primary analysis: a stranger could run it from §G alone
- [ ] Adjustment set listed with rationale (§G)
- [ ] Sample size calculation documented with assumptions and software (§F)
- [ ] Multiplicity correction specified if >1 outcome (§H)
- [ ] Missing-data plan documented (§I)
- [ ] Pre-specified subgroups listed with interaction tests declared (§J)
- [ ] Exploratory analyses declared as such in §K
- [ ] Data collection has not started, OR retrospective-data caveat applies (§9)
- [ ] Deviations log file created and committed to project repo (initially empty)
- [ ] Human-loop ledger updated: pre-registration step logged
  (`templates/human-loop-ledger.md`)

---

## 9. Retrospective-Data Caveat

Clinicians frequently use already-collected chart data. Be honest about what
pre-registration can and cannot do here.

| Condition | What to do | What to disclose |
|---|---|---|
| Data exist; outcome variables **not yet examined** | Register before opening outcome columns. This is the strongest feasible version for retrospective data. | "Data were collected prior to registration. Outcome variables were not examined until after registration ({{REG_NUMBER}}, {{TIMESTAMP}})." |
| Data exist; some descriptive / non-outcome exploration done | Register before any outcome analysis. | "Exploratory descriptive analysis was performed prior to registration; no outcome associations were examined." |
| Data exist; outcome data already partially examined | Registration is still better than none, but is weaker. All pre-examination work is exploratory. | "This is a post-hoc analysis. The analysis plan was registered after initial data inspection ({{REG_NUMBER}}). All findings should be considered hypothesis-generating and require prospective replication." |
| Prospective data; collection not started | Gold standard. Register before enrollment. | Cite registration number; state data collection start date post-timestamp. |

**Do not claim a retrospective registration is equivalent to prospective
pre-registration.** Reviewers and readers will check the timestamp against the
data-collection end date. Honesty here is non-negotiable for a clinician publishing
under their own name.

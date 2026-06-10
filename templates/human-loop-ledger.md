# Human-Loop Ledger

**File lives at:** `log/human-loop-ledger.md` in every paper project.  
**Update:** continuously, at every decision gate, from Phase −1 through submission.  
**Feeds:** `references/ai-disclosure.md` (AI-use statement) and `references/coi-detailed.md` (CRediT mapping) at submission.

---

## 1. Purpose

As AI execution cost falls toward zero, the audit trail of human judgment and human data IS the evidence of scientific integrity. A reader, an editor, or a future self needs to be able to answer: "Who decided this? Was the data real? Was this the question the authors committed to test?" This ledger makes those answers explicit and traceable — it operationalizes the two sovereign gates (💡 IDEA, 📊 DATA) defined in `references/ai-for-science-model.md §2` and the autonomy dial in `§6`.

Without a ledger, AI assistance is invisible and unaccountable. With one, every contribution is attributable and the AI-disclosure statement writes itself.

---

## 2. Decision Types

| Type | Meaning | Examples | May be 🤖? |
|------|---------|---------|-----------|
| 💡 **Human-judgment** | Idea, meaning, ethics, go/no-go | Question selection, novelty verdict, design approval, pre-registration sign-off, interpretation of a finding, whether to submit | **Never** for sovereign gates (see §4) |
| 📊 **Human-data** | Ground truth, provenance, IRB chain of custody | Data collection, IRB approval, de-identification confirmation, primary analysis adherence check, raw-data verification | **Never** for data origin |
| 🤖 **AI-execution** | Anything checked against an external truth | Literature search, draft prose, statistical code, table formatting, citation verification, red-team pass, revision tracking | Yes — automate aggressively |

**Hard rule for clinical work:** the 💡 IDEA gate, the 📊 DATA gate, and the pre-registration lock are **never** 🤖 autopilot. This is non-negotiable and overrides any autonomy mode setting.

---

## 3. Autonomy Mode Declaration

Fill at project start. Cannot be changed retroactively.

```
Project: _______________________________________________
Date declared: _________________________________________
Declared by: ___________________________________________

Autonomy mode (circle one):

  Manual     Co-pilot [default]     Autopilot

Manual:    AI runs one step at a time; human touches everything.
Co-pilot:  AI runs a full phase, stops at every gate; human decides all 💡/📊 verdicts.
Autopilot: AI runs the whole loop between gates; human owns only the sovereign gates + final sign-off.
           — NEVER use Autopilot for your first paper with this workflow —
           — NEVER use Autopilot for the 💡 IDEA gate, 📊 DATA gate, or pre-registration lock —

Sovereign gates are NEVER autopilot regardless of mode selected above.
```

---

## 4. The Ledger Table

Copy this table into `log/human-loop-ledger.md`. Add rows as needed. Delete none.

| Date | Phase | Decision point | Type | Decided by | AI proposal (if any) | Human action | Notes |
|------|-------|---------------|------|-----------|---------------------|--------------|-------|
| | −1 | **Clinical observation identified** | 💡 | [name] | — | Originate | The spark. No AI proposal here. |
| | −1 | **Research question selected** from AI-generated shortlist | 💡 | [name] | [list candidates proposed] | Accept / Modify / Reject | See `templates/research-question.md` |
| | −1 | **Novelty verdict** (novel / incremental / answered / contested) | 💡 | [name] | AI sweep output | Accept / Override | See `references/novelty-check.md` |
| | −1 | **Study design approved** (design, comparator, power, DAG) | 💡 | [name] | AI draft | Accept / Modify | Design is frozen from this point |
| | −1 | **Pre-registration submitted** (OSF / UMIN / jRCT / PROSPERO) | 💡 | [name] | AI drafted record | Human submits (binding) | Registration ID: ___ |
| | 0 | **IRB approval confirmed** | 📊 | [name] | — | Originate | Approval #: ___, Date: ___ |
| | 0 | **Data provenance verified** (de-id, chain of custody) | 📊 | [name] | — | Originate | Source: ___, N=___ |
| | 1–2 | Literature search executed | 🤖 | AI (PubMed MCP) | — | — | n=___ hits; human reviewed titles |
| | 3 | **Primary analysis adherence check** (pre-reg vs. actual) | 📊 | [name] | AI diff report | Accept / Flag deviations | Deviations disclosed: yes / no |
| | 3 | Statistical analysis run | 🤖 | AI | Code + output | Human verified against raw data | |
| | 4–5 | Draft prose (IMRAD) | 🤖 | AI | Full draft | Human edited | |
| | 5 | Every number traces to source data | 📊 | [name] | AI spot-check | Human confirmed | |
| | 6.5 | **Red-team adjudication** (statistical / methodological / novelty / integrity) | 💡 | [name] | AI red-team output | Accept verdict / Override | See `references/adversarial-review.md` |
| | 7 | Journal selected and fit assessed | 💡 | [name] | AI recommendation | Accept / Override | Target: ___ |
| | 7 | **Final submission sign-off** | 💡 | [name] | AI compliance check | Human submits | Submission ID: ___ |
| | 7 | **Title and abstract approved** | 💡 | [name] | AI draft | Accept / Modify | Final title: ___ |
| | 8–10 | Reviewer response drafts | 🤖 | AI | Draft replies | Human revised + signed | |
| | 10 | **Accept / revise / withdraw decision** | 💡 | [name] | AI recommendation | Human decides | |

---

## 5. Rolling Up the Ledger at Submission

### 5a. AI Disclosure Statement

From the ledger, extract all 🤖 rows and group by task. Template (adapt from `templates/declarations.md`):

```
During the preparation of this manuscript, the authors used Claude (Anthropic)
for the following purposes: literature search and summarization (Phases 1–2);
statistical analysis scripting (Phase 3); draft prose generation (Phases 4–5);
citation verification (Phase 5); and adversarial self-review (Phase 6.5).
All AI-assisted output was reviewed, edited, and verified by the authors.
The authors take full responsibility for the content of this publication.
No AI tool generated, imputed, or modified any data point.
```

**Worked example** (from a filled ledger with entries dated 2026-03-01 through 2026-05-15):

> "Phases 1–2: literature search via PubMed MCP (n=847 abstracts screened by AI; 62 full texts reviewed by KO). Phase 3: R analysis scripts drafted by Claude; verified by KO against de-identified dataset (IRB #2026-014). Phase 4–5: IMRAD first draft by Claude; substantially revised by KO. Phase 6.5: red-team pass by Claude; verdict adjudicated by KO. All 💡 and 📊 decision points in the project ledger (log/human-loop-ledger.md) carry KO's name and date."

### 5b. CRediT Author Contribution Mapping

Walk the ledger; map each decision type to CRediT roles:

| CRediT role | Maps to ledger type | Assigned to |
|-------------|--------------------|----|
| Conceptualization | 💡 question selection, novelty verdict | [human name] |
| Methodology | 💡 design approval, pre-registration | [human name] |
| Investigation | 📊 data collection, IRB, provenance | [human name] |
| Formal analysis | 🤖 statistical analysis (human-verified) | [human name] + AI |
| Data curation | 📊 primary analysis adherence, number check | [human name] |
| Writing – original draft | 🤖 prose (human-edited) | [human name] + AI |
| Writing – review & editing | 💡 all 💡 revision decisions | [human name] |
| Supervision | 💡 autonomy mode declaration, sign-off | [human name] |

**Note:** AI is not an author. Contributions where AI executed and human verified go under the human's name with AI use disclosed in the statement above.

**Worked example CRediT block:**

```
KO: Conceptualization, Methodology, Investigation, Data curation,
Formal analysis, Writing – original draft, Writing – review & editing.
AI tools (Claude): assisted with literature retrieval, analysis scripting,
draft prose, and adversarial review; see AI Disclosure statement.
```

---

## 6. Why This Matters

When AI execution cost approaches zero, a manuscript can be produced without a single genuine human decision — the Sakana AI Scientist failure in plain language. The ledger is the defense: it forces every gate to surface a named human, a date, and an explicit accept/modify/reject action. An editor can request it. A co-author can audit it. A retracting institution can trace it. And when a finding turns out to be wrong, the ledger shows whether the failure was in the AI execution (acceptable, fixable) or in the human judgment gates (the author's responsibility). The distinction matters clinically, legally, and for the future of AI-assisted research. A study without this trail is not more efficient — it is unaccountable.

---

## 7. Submission Verification Checklist

Before clicking Submit, confirm all of the following:

- [ ] Every 💡 row has a named human decider and a date
- [ ] Every 📊 row traces to an IRB approval number or a raw data file identifier
- [ ] No sovereign gate row (question selection, pre-registration, data provenance, final sign-off) is marked 🤖
- [ ] Pre-registration ID is recorded and the registered analysis matches what was run
- [ ] Any deviation from the pre-registered plan is disclosed in the manuscript
- [ ] The AI disclosure statement lists every 🤖 task type present in the ledger
- [ ] The CRediT block is consistent with the ledger (no AI listed as author)
- [ ] Ledger is saved to `log/human-loop-ledger.md` and committed to the project repo
- [ ] Ledger is cross-referenced in `references/ai-disclosure.md` and `references/coi-detailed.md`

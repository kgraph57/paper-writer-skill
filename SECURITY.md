# Security Policy

## Normal Skill Behavior

This package is a documentation-first Agent Skill for medical/scientific
manuscript writing. Unlike zero-network skills, it **intentionally uses network
access** for literature work: WebSearch/WebFetch and literature APIs (PubMed,
OpenAlex, Europe PMC, Semantic Scholar) during Phase −1 novelty checks, Phase 1
literature search, and Phase 5 citation verification. No credentials are
required for any of these.

The utility scripts under `scripts/` are optional. They read local files, write
local Markdown/plot outputs, and make no network calls. Analysis and PDF
utilities use the Python packages listed in `requirements.txt`.

## Clinical Data Handling — the hard rules

This skill is built for clinicians working with real patient data. The data
rules below mirror `templates/data-management.md` and the AI-for-Science model
(`references/ai-for-science-model.md`):

- **Raw clinical data stays local. Always.** Generated project directories keep
  original data under `data/raw/`, which is treated as read-only and is
  **gitignored** — it must never be committed or pushed anywhere.
- **Never commit PHI.** Only de-identified, processed data belongs in
  `data/processed/`. De-identification happens before anything leaves the raw
  folder.
- **Never paste identifiable patient information into any AI chat**, including
  the agent running this skill. Work from de-identified extracts.
- **AI never originates data.** The skill must never fabricate a data point,
  participant, or result (📊 DATA sovereignty). Any output that appears to
  contain invented data is a bug — report it.

## Permissions

| Capability | Used | Notes |
| --- | --- | --- |
| Network access | Yes | Literature APIs and web search only; no telemetry |
| Filesystem write | Yes | Manuscript project directories and script outputs |
| External tools | Optional | Python packages from `requirements.txt`; pandoc for docx/pdf compile |
| Credentials | No | No API keys required |
| Background execution | No | |

## Safety Rules

- Do not add hidden scripts or install-time automation.
- Do not add new network destinations without documenting them here.
- Do not embed real patient data — even "harmless" fragments — in examples,
  tests, or case studies. All repo examples are illustrative and PHI-free.
- Do not weaken the 💡 IDEA / 📊 DATA human-sovereignty gates in SKILL.md.

## Reporting

Open a GitHub issue for suspected vulnerabilities, unsafe instructions, or
hidden behavior. Do not include patient data or other confidential material in
public reports.

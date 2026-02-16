# PRISMA 2020 Flow Diagram Templates

## Overview

The PRISMA 2020 flow diagram documents the flow of information through different phases of a systematic review: identification, screening, and inclusion. This file provides copy-paste ready templates in three formats.

Reference: Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71.

---

## 1. Mermaid.js Version (Recommended)

Copy this code into any Mermaid-compatible renderer (GitHub, Notion, Obsidian, Mermaid Live Editor at https://mermaid.live).

```mermaid
flowchart TD
    %% ============================================================
    %% PRISMA 2020 Flow Diagram
    %% Systematic Review: [YOUR REVIEW TITLE]
    %% Date: [YYYY-MM-DD]
    %% ============================================================

    %% --- IDENTIFICATION ---
    subgraph id["<b>Identification</b>"]
        direction TB
        db1["Records identified from databases<br/>(n = [N])<br/><br/>PubMed (n = [N])<br/>Scopus (n = [N])<br/>CINAHL (n = [N])<br/>Cochrane (n = [N])"]
        other1["Records identified from other sources<br/>(n = [N])<br/><br/>Citation searching (n = [N])<br/>Grey literature (n = [N])<br/>Expert consultation (n = [N])"]
        dup["Records removed before screening:<br/>Duplicate records (n = [N])<br/>Records marked as ineligible<br/>by automation tools (n = [N])<br/>Records removed for<br/>other reasons (n = [N])"]
    end

    %% --- SCREENING ---
    subgraph sc["<b>Screening</b>"]
        direction TB
        screen1["Records screened<br/>(n = [N])"]
        excl1["Records excluded<br/>(n = [N])"]
        sought1["Reports sought<br/>for retrieval<br/>(n = [N])"]
        notret1["Reports not<br/>retrieved<br/>(n = [N])"]
        assessed1["Reports assessed<br/>for eligibility<br/>(n = [N])"]
        excl2["Reports excluded (n = [N]):<br/>Wrong population (n = [N])<br/>Wrong intervention (n = [N])<br/>Wrong comparator (n = [N])<br/>Wrong outcome (n = [N])<br/>Wrong study design (n = [N])<br/>Wrong setting (n = [N])<br/>Not in English (n = [N])<br/>Conference abstract only (n = [N])<br/>Other (n = [N])"]
    end

    %% --- INCLUDED ---
    subgraph inc["<b>Included</b>"]
        direction TB
        final["Studies included in review<br/>(n = [N])<br/>Reports included<br/>(n = [N])"]
        quant["Studies included in<br/>quantitative synthesis<br/>(meta-analysis)<br/>(n = [N])"]
    end

    %% --- FLOW CONNECTIONS ---
    db1 --> dup
    other1 --> dup
    dup --> screen1
    screen1 --> excl1
    screen1 --> sought1
    sought1 --> notret1
    sought1 --> assessed1
    assessed1 --> excl2
    assessed1 --> final
    final --> quant

    %% --- STYLING ---
    style id fill:#e8f4f8,stroke:#2196F3,stroke-width:2px
    style sc fill:#fff3e0,stroke:#FF9800,stroke-width:2px
    style inc fill:#e8f5e9,stroke:#4CAF50,stroke-width:2px
```

### Simplified Version (No Meta-Analysis)

If your systematic review does not include a meta-analysis, use this version:

```mermaid
flowchart TD
    subgraph id["<b>Identification</b>"]
        db1["Records identified from databases<br/>(n = [N])<br/><br/>PubMed (n = [N])<br/>Scopus (n = [N])<br/>Web of Science (n = [N])"]
        other1["Records from other sources<br/>(n = [N])"]
        dup["Duplicates removed (n = [N])<br/>Records removed for other reasons (n = [N])"]
    end

    subgraph sc["<b>Screening</b>"]
        screen1["Records screened<br/>(n = [N])"]
        excl1["Records excluded<br/>(n = [N])"]
        sought1["Reports sought for retrieval<br/>(n = [N])"]
        notret1["Reports not retrieved<br/>(n = [N])"]
        assessed1["Reports assessed for eligibility<br/>(n = [N])"]
        excl2["Reports excluded (n = [N]):<br/>Reason 1 (n = [N])<br/>Reason 2 (n = [N])<br/>Reason 3 (n = [N])"]
    end

    subgraph inc["<b>Included</b>"]
        final["Studies included in review<br/>(n = [N])"]
    end

    db1 --> dup
    other1 --> dup
    dup --> screen1
    screen1 --> excl1
    screen1 --> sought1
    sought1 --> notret1
    sought1 --> assessed1
    assessed1 --> excl2
    assessed1 --> final

    style id fill:#e8f4f8,stroke:#2196F3,stroke-width:2px
    style sc fill:#fff3e0,stroke:#FF9800,stroke-width:2px
    style inc fill:#e8f5e9,stroke:#4CAF50,stroke-width:2px
```

---

## 2. PlantUML Version

Save as `.puml` file or paste into PlantUML renderer (https://www.plantuml.com/plantuml/uml).

```plantuml
@startuml PRISMA_2020_Flow_Diagram
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 11
skinparam RectangleBorderColor #333333
skinparam RectangleBackgroundColor #FFFFFF

title PRISMA 2020 Flow Diagram\n[YOUR REVIEW TITLE]

' ====== IDENTIFICATION ======
rectangle "**Identification**" #e8f4f8 {
    rectangle "Records identified from\ndatabases (n = [N])\n\nPubMed (n = [N])\nScopus (n = [N])\nCINAHL (n = [N])\nCochrane (n = [N])" as db
    rectangle "Records identified from\nother sources (n = [N])\n\nCitation searching (n = [N])\nGrey literature (n = [N])\nExpert consultation (n = [N])" as other
    rectangle "Records removed before screening:\nDuplicate records (n = [N])\nRecords marked ineligible by\nautomation tools (n = [N])\nRecords removed for\nother reasons (n = [N])" as dup
}

' ====== SCREENING ======
rectangle "**Screening**" #fff3e0 {
    rectangle "Records screened\n(n = [N])" as screen
    rectangle "Records excluded\n(n = [N])" as excl1
    rectangle "Reports sought for\nretrieval (n = [N])" as sought
    rectangle "Reports not\nretrieved (n = [N])" as notret
    rectangle "Reports assessed for\neligibility (n = [N])" as assess
    rectangle "Reports excluded (n = [N]):\nWrong population (n = [N])\nWrong intervention (n = [N])\nWrong comparator (n = [N])\nWrong outcome (n = [N])\nWrong study design (n = [N])\nOther (n = [N])" as excl2
}

' ====== INCLUDED ======
rectangle "**Included**" #e8f5e9 {
    rectangle "Studies included in review\n(n = [N])\nReports included\n(n = [N])" as included
    rectangle "Studies included in\nquantitative synthesis\n(meta-analysis)\n(n = [N])" as meta
}

' ====== CONNECTIONS ======
db -down-> dup
other -down-> dup
dup -down-> screen
screen -right-> excl1
screen -down-> sought
sought -right-> notret
sought -down-> assess
assess -right-> excl2
assess -down-> included
included -down-> meta

@enduml
```

---

## 3. ASCII Art Version (Plain Text)

For use in plain text documents, emails, or protocols where graphical rendering is unavailable.

```
=============================================================================
                      PRISMA 2020 FLOW DIAGRAM
                      [YOUR REVIEW TITLE]
=============================================================================

 IDENTIFICATION
+----------------------------------------------+
|                                              |
|  Records identified from     Records from    |
|  databases (n = [N])         other sources   |
|                              (n = [N])       |
|    PubMed      (n = [N])                     |
|    Scopus      (n = [N])     Citation        |
|    CINAHL      (n = [N])     searching       |
|    Cochrane    (n = [N])     (n = [N])       |
|                              Grey lit         |
|                              (n = [N])       |
+----------------------------------------------+
                      |
                      v
+----------------------------------------------+
|  Records removed before screening:           |
|    Duplicate records removed  (n = [N])      |
|    Ineligible by automation   (n = [N])      |
|    Other reasons              (n = [N])      |
+----------------------------------------------+
                      |
                      v
 SCREENING
+----------------------------------------------+
|  Records screened  ------>  Records excluded |
|  (n = [N])                  (n = [N])        |
+----------------------------------------------+
                      |
                      v
+----------------------------------------------+
|  Reports sought    ------>  Reports not      |
|  for retrieval              retrieved         |
|  (n = [N])                  (n = [N])        |
+----------------------------------------------+
                      |
                      v
+----------------------------------------------+
|  Reports assessed  ------>  Reports excluded |
|  for eligibility            (n = [N]):       |
|  (n = [N])                                   |
|                       Wrong population  [N]  |
|                       Wrong intervention[N]  |
|                       Wrong comparator  [N]  |
|                       Wrong outcome     [N]  |
|                       Wrong design      [N]  |
|                       Not in English    [N]  |
|                       Other             [N]  |
+----------------------------------------------+
                      |
                      v
 INCLUDED
+----------------------------------------------+
|  Studies included in review (n = [N])        |
|  Reports included           (n = [N])        |
+----------------------------------------------+
                      |
                      v
+----------------------------------------------+
|  Studies included in quantitative synthesis  |
|  (meta-analysis) (n = [N])                   |
+----------------------------------------------+
```

---

## 4. Customization Instructions

### Step-by-Step

1. **Replace `[N]` placeholders** with your actual numbers
2. **Replace `[YOUR REVIEW TITLE]`** with your systematic review title
3. **Adjust database names** in the Identification box to match your actual search
4. **Customize exclusion reasons** in the eligibility assessment box to match your criteria
5. **Remove the meta-analysis box** if your review is qualitative only
6. **Add or remove "other sources"** categories as needed

### Common Modifications

#### No Other Sources (Databases Only)

Remove the `other1` box and merge all records into the database path.

#### Multiple Database Paths

If you searched very different types of databases (e.g., clinical databases vs. trial registries), you can split the Identification section:

```mermaid
flowchart TD
    subgraph id["Identification"]
        db_biomed["Biomedical databases<br/>(n = [N])<br/>PubMed, Scopus, CINAHL"]
        db_trial["Trial registries<br/>(n = [N])<br/>ClinicalTrials.gov, WHO ICTRP"]
        db_grey["Grey literature<br/>(n = [N])<br/>Google Scholar, ProQuest"]
    end
```

#### Scoping Review (No Critical Appraisal Box)

Scoping reviews typically do not include quality assessment. Simply remove any quality/risk-of-bias boxes.

#### Updated Systematic Review

If updating a previous review, add a box for "Studies included in previous version (n = [N])" feeding into the Included section.

### Exclusion Reason Categories

Choose from these common exclusion categories (customize to your review):

| Category | Description |
|----------|-------------|
| Wrong population | Does not meet population criteria |
| Wrong intervention/exposure | Intervention does not match |
| Wrong comparator | No appropriate comparison group |
| Wrong outcome | Primary outcome not measured |
| Wrong study design | Not the target study design (e.g., not RCT) |
| Wrong setting | Study conducted in excluded setting |
| Language | Not in included language(s) |
| Duplicate | Same study reported elsewhere |
| Full text unavailable | Could not obtain full text after attempts |
| Conference abstract only | No full peer-reviewed publication |
| Protocol/registry only | Only a study protocol, no results |
| Not original research | Editorial, letter, commentary |

### Number Verification Checklist

Before finalizing your PRISMA diagram, verify:

- [ ] Total identified = sum of all database records + other sources
- [ ] Records after deduplication = Total identified - duplicates removed
- [ ] Records screened = Records after deduplication
- [ ] Records excluded (title/abstract) + reports sought = records screened
- [ ] Reports not retrieved + reports assessed = reports sought
- [ ] Reports excluded (full text) + studies included = reports assessed
- [ ] Sum of exclusion reasons = total reports excluded at full text
- [ ] Studies in meta-analysis <= studies included in review

---

## 5. Tools for Rendering

| Tool | Format | URL |
|------|--------|-----|
| Mermaid Live Editor | Mermaid | https://mermaid.live |
| PlantUML Server | PlantUML | https://www.plantuml.com/plantuml/uml |
| GitHub | Mermaid (native) | Any .md file in a repo |
| Obsidian | Mermaid (native) | Use mermaid code block |
| draw.io / diagrams.net | Manual | https://app.diagrams.net |
| PRISMA Flow Diagram Generator | Web form | http://www.prisma-statement.org/PRISMAStatement/FlowDiagram |
| Lucidchart | Manual | https://lucid.app |

### Export Tips

- **For journals**: Export as SVG or high-resolution PNG (300+ DPI)
- **Mermaid Live Editor**: Click "Actions" > "PNG" or "SVG"
- **PlantUML**: Append `/svg/` or `/png/` to the URL
- **Most journals accept**: TIFF, EPS, PDF, or high-res PNG
- **Typical figure size**: Width 170mm (full page) or 85mm (single column)

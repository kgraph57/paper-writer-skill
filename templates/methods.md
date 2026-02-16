# Methods Section Writing Guide

## Structure

Write Methods in this order:

### 1. Study Design
- State the study design explicitly (e.g., "This was a retrospective cohort study")
- Include registration number if applicable (clinical trials)

### 2. Setting & Participants
- **When**: study period (e.g., "January 2020 to December 2024")
- **Where**: institution, department
- **Who**: inclusion criteria, exclusion criteria
- **How identified**: consecutive patients, random sample, etc.

### 3. Data Collection
- What variables were collected
- How they were measured (instruments, definitions)
- Who collected the data
- Data sources (medical records, surveys, etc.)

### 4. Outcomes
- Primary outcome: clearly defined
- Secondary outcomes: listed
- How outcomes were measured

### 5. Statistical Analysis
- Descriptive statistics approach
- Comparative statistics (which tests, why)
- Multivariate analysis if applicable
- Missing data handling
- Software and version (e.g., "R version 4.3.1")
- Significance threshold (e.g., "p < 0.05 was considered significant")

### 6. Ethical Considerations
- IRB/Ethics committee approval (name, approval number)
- Informed consent (obtained or waived, with reason)
- Data handling and privacy

## Rules

- Be specific enough for another researcher to replicate the study
- Every method described here MUST have a corresponding result in `03_results.md`
- Write Methods and Results as a pair: after drafting each Methods subsection, immediately draft the corresponding Results subsection
- Use past tense
- Do not include results in this section
- Reference established methods (e.g., "as described by Author et al. [ref]")
- Use consistent terminology throughout (e.g., if you say "patients" here, say "patients" in all sections)

## Common Mistakes

- Missing study period dates
- Vague inclusion/exclusion criteria
- Not specifying statistical software
- Forgetting ethics approval statement
- Not defining how variables were measured

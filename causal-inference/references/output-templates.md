# Output templates

Adapt these templates to the task. Keep the verdict near the top.

## Template A: research idea / design mode

### 1. Causal question and estimand

- Question:
- Treatment:
- Outcome:
- Unit:
- Target estimand:

### 2. Where identification could come from

For each plausible source of variation:

- identifying variation;
- comparison group;
- assumptions;
- what institutional facts would make the assumption plausible or implausible;
- data requirements.

### 3. Candidate designs ranked

Rank only genuinely plausible designs.

For each:

- why it fits;
- main advantage;
- main identification threat;
- recommended estimator family only after the design is justified.

### 4. Minimum evidence needed

List the specific institutional evidence, plots, diagnostics, or falsification exercises needed before estimation.

### 5. Recommended next specification

If enough information exists, give a concrete estimating equation or Stata skeleton and explain what each term does.

### 6. Verdict

Use one standard credibility label.

## Template B: identification audit

### 1. Identification verdict

One short paragraph: state whether the design identifies the claimed causal parameter and the single biggest reason for the verdict.

### 2. What is actually identifying the estimate

- intended estimand;
- actual estimator/estimand;
- identifying variation;
- comparison group;
- most important assumption.

### 3. Threats ranked by severity

Use a table when useful:

| Severity | Threat | Why it matters | Can current design fix it? | Evidence/action needed |
|---|---|---|---|---|

Do not list cosmetic issues above identification failures.

### 4. Method-use audit

State whether the chosen method is appropriate for the actual treatment path and data structure.

For DID/event study, explicitly address timing and heterogeneity.
For RDD, explicitly address cutoff assignment, manipulation, bandwidth/inference, and locality.
For IV, explicitly address relevance, exclusion, independence, weak identification, and estimand interpretation.
For synthetic control, explicitly address donor pool, pre-fit, contamination, and inference.

### 5. What would change the verdict

Give concrete changes: different comparison group, different estimator, additional pre-periods, alternative treatment coding, sensitivity analysis, new data, design change, or narrower estimand.

### 6. Method references

List only verified sources used in the diagnosis and say why each matters.

## Template C: Stata code audit

### Identification verdict

State the econometric verdict before code details.

### Code-to-estimator map

For each important block:

- code/command;
- what it estimates;
- assumption/default that matters;
- issue if any.

### Problems

Separate into:

1. **Identification**
2. **Estimator choice**
3. **Inference**
4. **Implementation/code**
5. **Interpretation/reporting**

### Corrected implementation

Provide corrected Stata code only for issues that are truly coding or estimator-choice problems. Do not present new code as if it solves a fundamentally invalid identification design.

### Verification checklist

Tell the user exactly what output to return if further audit is needed: sample counts, treatment cohorts, first stage, event-time support, bandwidth output, cluster counts, pre-fit metrics, etc.

## Template D: method choice comparison

Use when the user asks which causal method to use.

| Method | Identifying variation | Core assumption | Fits this setting? | Main failure mode | Estimand |
|---|---|---|---|---|---|

Then rank the methods and explain why. Do not recommend a method merely because the required variable names can be constructed.

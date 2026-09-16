# Result Interpretation and External-Facing Report Protocol

Use this reference whenever interpreting figures or tables, assembling a results story, or producing an HTML/PDF/Word-style results report from empirical outputs.

## Numbering is mandatory

- Number figures and tables separately and sequentially: `Figure 1`, `Figure 2`, ... and `Table 1`, `Table 2`, ... .
- Give every displayed figure and table a concise substantive title.
- Do not mix ad hoc labels such as `Diagnostic A`, `D1`, or unnumbered mechanism tables into the main sequence unless the user explicitly asks for appendix-style labels.
- If an item belongs in an appendix, use an appendix convention consistently, such as `Figure A1` or `Table A1`.

## Every figure and table gets the same interpretation structure

For each displayed item, provide all five components below. Do not omit a component merely because it seems obvious.

### 1. What the figure/table shows

Describe the visible or tabulated empirical pattern first. Report the economically relevant direction, magnitude, timing, group comparison, and uncertainty when available. Keep this section descriptive before moving to broader interpretation.

### 2. Importance and role in the paper

State why the item matters for the research question and classify its role using one of these labels:

- **Core**: central evidence without which the main story would materially weaken.
- **Supporting**: strengthens a central result, mechanism, or interpretation but is not itself the headline evidence.
- **Diagnostic**: primarily evaluates identification, measurement, sample support, timing, or data quality.
- **Appendix**: useful verification or robustness evidence that should normally stay out of the main narrative.

Also state the likely placement when useful: main text, results section, mechanism section, identification section, or appendix. Do not equate statistical significance with importance.

### 3. What the pattern can and cannot establish

State the warranted inferential content. Distinguish descriptive association, first-stage evidence, raw DID/DDD variation, adjusted regression evidence, event-study diagnostics, and causal interpretation. Do not turn a visual pattern or a non-rejected pre-trend test into proof of identification.

### 4. Connection to identification, sample support, or mechanism

Explain how the item contributes to the research design. Connect it to the relevant counterfactual comparison, support across design cells, treatment/exposure variation, timing, baseline-risk heterogeneity, dynamic mechanism, or other substantive channel. If the item does not materially inform identification or mechanism, say what narrower role it serves.

### 5. Interpretation notes

Use this final block to state the minimum contextual qualification needed to read the result correctly. Tailor the heading and tone to the audience as described below.

## Internal versus external-facing reporting

Distinguish working diagnostics from material intended to be shown to supervisors, seminar audiences, coauthors, referees, or other readers.

### Internal working memo

For private/internal analysis, be explicit. The fifth block may be titled **Concerns and next steps**, **Potential issue**, or **Follow-up**. State suspicious discontinuities, composition changes, weak cells, measurement concerns, nonparallel movements, unresolved robustness questions, or additional checks directly.

### External-facing HTML/report

For material intended to be shown to others, do not use headings such as **Problems**, **Weaknesses**, **Concerns**, or **Next steps** by default. Use neutral headings such as:

- **Interpretation notes**
- **Scope and context**
- **Reading this result**
- **Additional context**

Keep this section concise and proportionate. Do not expose an internal to-do list or speculative concern merely because it appeared during exploratory analysis. Separate private workflow tasks from reader-facing interpretation.

At the same time, do not conceal a limitation that would materially change the meaning, credibility, or scope of the result. If omitting a caveat would make the claim misleading, include it in neutral factual language and calibrate the substantive claim accordingly. External-facing presentation should be polished, not deceptive.

Examples:

- Internal: `Concern: the control group moves before treatment; test alternative windows.`
- External: `Interpretation notes: pre-policy movements are not perfectly flat, so the figure is treated as a diagnostic rather than proof of parallel trends.`

- Internal: `Next step: investigate small Black subgroup cells.`
- External: `Scope and context: subgroup estimates are less precise where cell sizes are small.`

## HTML/report layout

When producing an HTML interpretation report, use a consistent card or section for each item:

`Figure N. Title` or `Table N. Title`

1. **What it shows**
2. **Importance: Core / Supporting / Diagnostic / Appendix**
3. **What it can and cannot establish**
4. **Connection to identification, support, or mechanism**
5. **Interpretation notes** for external-facing output, or **Concerns and next steps** for an explicitly internal working memo

After the item-by-item interpretation, add a separate synthesis section that builds the overall economic story. Do not let the synthesis replace the required interpretation of individual figures and tables.

## Story construction

Build the story only after interpreting every relevant item. Organize the synthesis around economic logic rather than significance hunting:

1. motivating empirical pattern;
2. treatment/exposure or first stage;
3. main outcome result;
4. heterogeneity central to the research question;
5. mechanism evidence;
6. identification evidence and scope;
7. robustness/supporting evidence.

Distinguish headline evidence from diagnostics. A result can be statistically insignificant yet economically important as a bound, falsification check, first-stage diagnostic, or source of scope information.

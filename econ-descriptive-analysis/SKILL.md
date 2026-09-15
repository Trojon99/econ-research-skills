# Empirical Descriptive Analysis

## Core rule

Treat descriptive analysis as a design-diagnostic stage, not a catalog of summary statistics.

Prefer figures whenever a figure can communicate the empirical pattern clearly. Do not create tables by default simply because descriptive statistics are requested. Retain tables only when exact values, sample counts, variable definitions, baseline balance, or compact coefficient summaries materially help interpretation or reproducibility.

## Workflow

1. Identify the research design before selecting outputs.
   - Determine the outcome, treatment/exposure, comparison group, timing, baseline variables, subgroup dimensions, and unit of observation.
   - Distinguish cross-sectional, panel, event-time, repeated cross-section, DID, DDD, RDD, and other designs.
   - Do not interpret descriptive differences as causal effects.

2. Audit the analysis sample first.
   - Check observations and unique persons/units.
   - Check missingness and support in the cells needed for the design.
   - Check whether weights are cross-sectional, longitudinal, replicate, or otherwise design-specific.
   - Flag small cells and attrition before emphasizing subgroup patterns.

3. Build a small descriptive summary layer from the analysis master.
   - Aggregate once where possible, then draw multiple figures from the summary data.
   - For large person-month panels, prefer `collapse`, `contract`, `egen`, or equivalent grouped operations over deeply nested loops that repeatedly scan the full master.
   - Keep summary `.dta`/`.csv` outputs when useful for auditing, but treat them as supporting files rather than the main deliverable.
   - Reuse an existing working/analysis master unless upstream construction has changed.

4. Produce figures in research-priority order.
   - Main outcome trends by treatment/comparison group.
   - First-stage or exposure trends when relevant.
   - Baseline-risk or health-group heterogeneity central to the design.
   - Transition, persistence, entry, exit, or dropout diagnostics for dynamic outcomes.
   - Seasonality when transitions may reflect school calendars, survey timing, or other recurring cycles.
   - Raw DID/DDD cell patterns or health gaps before regression adjustment.
   - Selected demographic heterogeneity only when it helps assess support, external validity, or a substantive mechanism.
   - Attrition, missingness, or follow-up plots when panel retention matters.

5. Add tables only for information that is awkward or misleading as a figure.
   - Baseline characteristics with exact values.
   - Sample-support and small-cell counts.
   - Variable-definition or timing audits.
   - Compact regression/robustness summaries when the user explicitly wants exact coefficients.
   - Do not duplicate a figure with a large table unless exact numbers are needed.

6. Interpret the figures economically.
   - State what pattern is visible.
   - State what the pattern can and cannot establish.
   - Connect the pattern to identification, sample support, or mechanism.
   - Flag suspicious discontinuities, seasonality, composition changes, or nonparallel movements for follow-up.

## Figure selection rules

Use `references/figure-design.md` when choosing figure types or organizing a figure set. For DID/event-study parallel-trends figures, pre-trend diagnostics, or dynamic-effect plots, also read `references/parallel-trends-figures.md`.

Prioritize the following:

- Two-group trend plots for treatment versus comparison groups.
- Four-line or faceted plots for treatment/comparison crossed with a binary baseline-risk group.
- Facets for race, sex, or other multi-category heterogeneity when putting every category on one axis would be unreadable.
- Relative event-time plots for parallel-trend diagnostics. If the figure is labeled or described as a parallel-trends figure, its x-axis must be relative to treatment/policy timing (for example, -4, -3, -2, -1, 0, +1, +2), not absolute calendar time.
- Seasonal month-of-year plots for entry/exit/dropout transitions.
- Gap plots for DID/DDD descriptives when the research question is about changes in disparities.
- Bar or dot plots for one-time baseline composition or topical-module prevalence.

Avoid:

- Pie charts for empirical-economics research outputs.
- Dense spaghetti plots with too many groups.
- Large table dumps as the primary descriptive deliverable.
- Plotting every available variable mechanically.
- Smoothing away economically meaningful timing or policy discontinuities without justification.

## Stata conventions

When generating Stata code:

- Preserve the project's existing code style and naming conventions.
- Prefer explicit, auditable blocks for the most important figures.
- Use small loops for genuinely repetitive graph exports, but do not use nested loops that repeatedly rescan a large master when one grouped collapse can do the work.
- Build figure-ready datasets first, then graph from those datasets.
- Save figures into clearly named subfolders by purpose, such as `core_trends`, `health_heterogeneity`, `dropout`, `raw_ddd`, and `design_audit`.
- Export publication-friendly formats such as PDF, while preserving graph-ready data separately.
- Keep labels economically interpretable rather than exposing cryptic variable names in final figures when practical.
- Show the relevant time unit explicitly: month, quarter, wave, or event time. For parallel-trends figures, recode the x-axis to relative event time even when the underlying data are stored in calendar months/quarters/waves.
- Use weights only when their interpretation is appropriate; do not silently treat a cross-sectional weight as a panel weight.

## DID and DDD descriptives

Before formal regression, visualize the identifying variation.

For DID:
- Treat **relative event time** as mandatory for any figure called a parallel-trends figure. Construct event time as period relative to the policy/treatment date and use labels such as `-4, -3, -2, -1, 0, +1, +2` (or clearly ordered `Pre 4 ... Post 2` labels if needed). Do not use absolute calendar dates on the x-axis of the parallel-trends figure.
- Default to two complementary relative-time diagnostics when data permit: (1) raw treated/comparison outcome trends in levels aligned to event time, and (2) an event-study coefficient plot from the design-appropriate estimator.
- Show more than two pre-treatment event-time points when data permit and retain enough history to reveal differential dynamics.
- Mark the treatment boundary at event time 0 and any substantively important announcement/transition window in relative-time units.
- An absolute calendar-time outcome plot may be created separately to diagnose seasonality, composition, or calendar shocks, but label it as a calendar-time/raw-trend diagnostic rather than a parallel-trends figure and never substitute it for the relative-time parallel-trends figure.
- State the event-study normalization/reference period and show uncertainty.
- Do not call similar-looking raw trends, individually insignificant pre-coefficients, or a failed-to-reject joint pretrend test proof of parallel trends.
- If treatment timing is staggered or treatment effects may be heterogeneous across cohorts, do not default to a conventional TWFE lead-lag event study; route estimator choice through the causal-inference workflow.
- When parallel trends is a central threat, consider sensitivity analysis to bounded violations rather than relying only on pretesting.

For DDD:
- Plot the four underlying group paths when readable, or plot the within-group gap over time.
- Show how the relevant disparity changes for eligible versus comparison units.
- Report raw cells only as descriptive evidence; do not present the raw DDD as a causal estimate without the full identification argument.

For policy transitions:
- Mark or clearly describe enactment, implementation, and excluded transition windows when relevant.
- Avoid coding ambiguous transition months into pre or post merely to simplify a graph.

## Dynamic education outcomes

When studying enrollment, persistence, exit, or dropout:

- Distinguish raw exits from confirmed dropout, temporary breaks, completion, and unresolved follow-up when the data permit.
- Examine calendar-month seasonality before interpreting exit spikes as dropout.
- Plot risk-set denominators or flag weak support when transition rates are based on small numbers.
- Prefer a persistence/dropout definition based on observed future status over a hard-coded assumption that particular months are school breaks, unless the data or institutional rules justify the hard coding.

## Health and subgroup descriptives

When health is a baseline moderator or risk measure:

- Separate baseline health from contemporaneous or post-treatment health.
- Do not relabel a broad general-health measure as purely physical or mental health.
- When multiple health measures exist at different waves, show timing and comparability before combining them.
- Plot the main baseline health split prominently if it defines the empirical estimand.

For race/ethnicity, sex, and other subgroup plots:
- Preserve the project's agreed category construction.
- Prefer faceting or a small number of targeted subgroup figures over one overcrowded figure.
- Flag small subgroup cells rather than overinterpreting noisy lines.

## Default deliverable

Unless the user requests otherwise, provide:

1. A short figure plan tied to the research question.
2. Code or analysis that creates the figure-ready summary data.
3. The figures themselves or graph-export code.
4. Only the minimum supporting tables needed for exact values and auditability.
5. A brief interpretation of what each major figure contributes to the research design.

If the user explicitly says to prefer figures over tables, make figures the dominant output and keep tables in the background for verification only.

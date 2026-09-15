# Parallel-Trends and Event-Study Figure Protocol

Use this reference for DID/event-study requests involving parallel trends, pre-trends, dynamic effects, treatment timing, or graphical diagnostics.

## Core rule: parallel-trends figures use relative time

Any figure labeled, described, or delivered as a **parallel-trends figure** must put **relative/event time** on the x-axis. Recenter the underlying calendar month, quarter, year, or wave so that the treatment/policy boundary is event time 0 and pre/post periods are shown as negative/positive relative periods (for example, `-4, -3, -2, -1, 0, +1, +2`). Do not use absolute calendar dates on the x-axis of the parallel-trends figure.

Do not treat one graph as doing every job. Prefer two complementary relative-time figures when data permit:

1. **Raw outcome trends in levels aligned to event time** by treated and comparison group. This shows the empirical group paths before and after treatment on the same relative-time scale.
2. **Event-study coefficient plot** showing relative-time estimates from the estimator that matches the design. This shows dynamic adjusted differences relative to an explicit normalization/reference period and should include uncertainty.

A separate absolute calendar-time outcome plot can still be useful for diagnosing seasonality, calendar shocks, composition changes, or implementation details. Treat that as a **calendar-time/raw-trend diagnostic**, not as the parallel-trends figure. Neither descriptive raw trends nor an event-study coefficient plot proves the counterfactual parallel-trends assumption.

## Before plotting

Establish all of the following before generating the figure:

- outcome and unit of observation;
- treated/exposed group and comparison group;
- whether group membership is fixed or changes over time;
- treatment/policy date and any enactment, announcement, implementation, or transition dates that differ;
- underlying calendar-time unit and the event-time mapping used for the parallel-trends figure;
- analysis sample and weighting scheme;
- panel versus repeated cross-section structure;
- clustering/assignment level for inference;
- whether treatment timing is common or staggered;
- whether anticipation is plausible;
- whether treatment reverses or switches off.

If treatment timing is staggered, heterogeneous, reversible, or continuous, do not automatically use a conventional TWFE lead-lag event study. Route the estimator choice through the causal-inference workflow first.

## Figure A: raw trends in levels aligned to relative event time

### Construction

- Plot the same outcome used in the main design, in its natural level or a substantively justified transformation.
- Put relative/event time on the x-axis and the outcome mean/rate on the y-axis. Construct event time from the underlying calendar period and treatment/policy date; do not leave absolute dates on the parallel-trends x-axis.
- Plot treated and comparison groups separately on the same axes when readable.
- Use the weighting scheme that matches the main descriptive estimand. If weights are important or controversial, keep an unweighted diagnostic as a robustness/support check rather than silently mixing conventions.
- Mark the treatment boundary at event time 0 (or between -1 and 0 for discrete periods when clearer). If enactment, announcement, implementation, and effective dates differ, express the relevant boundaries or excluded transition window in relative-time units.
- Show enough pre-treatment event-time periods to evaluate differential dynamics. Do not truncate the pre-period merely because a shorter window looks more parallel. If seasonality or calendar-specific shocks are a concern, inspect them in a separate calendar-time diagnostic.
- Avoid smoothing lines by default. Smoothing can conceal policy discontinuities, seasonal breaks, or differential pre-trends.
- Keep the outcome scale common across groups/panels that are being visually compared.
- When support changes materially over time, report or retain period-specific observation/person counts.

### Interpretation

Use raw levels to inspect:

- whether treated and control outcomes have similar pre-treatment slopes/shapes;
- whether baseline level differences are large enough to require substantive explanation;
- whether one group has a pre-policy break, seasonal pattern, or composition shift;
- whether the apparent post-policy divergence starts before implementation, suggesting anticipation or another shock.

Do not say that close-looking lines 'verify' or 'prove' parallel trends. Parallel pre-trends are at most indirect evidence about the unobserved counterfactual trend after treatment.

## Figure B: event-study coefficients

### Construction

- Use event time on the x-axis and estimated treatment-group relative differences/effects on the y-axis.
- State the normalization/reference period in the note. A common default is the last pre-treatment period, but a broader pre-treatment reference window can be reasonable when justified.
- If a single reference period is used, plot or clearly indicate the normalized zero coefficient so readers understand the baseline.
- If a broader pre-treatment reference window is used, interpret pre-treatment coefficients as deviations around that normalization and evaluate the overall path/slope rather than mechanically asking whether each coefficient differs from zero.
- Plot point estimates and 95% pointwise confidence intervals by default.
- For a central event-study figure, consider simultaneous/uniform confidence bands (for example, sup-t bands) in addition to pointwise intervals when the software/estimator supports them.
- Add a horizontal zero line and a vertical treatment boundary. For discrete periods, placing the vertical line between the last untreated and first treated period is often clearer than placing it through a point.
- Label endpoint bins explicitly, e.g. `<= -6` and `>= 6`, when distant periods are pooled. Do not draw a pooled endpoint as if it represented one exact event time.
- Avoid connecting coefficients with a line when the line implies unsupported interpolation; connected points are acceptable when used only to emphasize the ordered event-time path.
- Keep pre- and post-treatment estimates visually distinguishable but do not use significance-driven colors.

### Pre-treatment diagnostics

Treat pre-event coefficients as placebo-style diagnostics, not direct proof of the identifying assumption.

- Report a joint Wald test of the relevant pre-treatment coefficients when useful.
- Do not interpret `p > 0.05` as evidence that parallel trends holds. Conventional pre-trend tests can have low power.
- Do not decide whether to report the main estimate only after seeing whether a pre-trend test 'passes'; conditioning on a pretest can distort estimation and inference.
- Look at economically meaningful magnitudes and trends, not only statistical significance.
- When the identifying assumption is central and the data are informative enough, supplement the graph with sensitivity analysis allowing bounded violations of parallel trends, such as Rambachan-Roth / HonestDiD.
- Economic/institutional arguments for the comparison group remain necessary even when the pre-period looks flat.

## Common-date DID versus staggered adoption

### Common treatment date / canonical 2xT DID

For one treated group and one comparison group around a common policy date, a useful event-study regression interacts treatment-group status with period indicators. The omitted/reference period defines the normalization. Use the same sample, weights, controls, fixed effects, and clustering logic as the main specification unless the graph is intentionally raw/descriptive and clearly labeled as such.

The most informative default pair is:

1. raw treated/control outcome means by **relative event period**;
2. treatment-group x event-time interaction coefficients with uncertainty.

A separate calendar-time raw-outcome plot is optional for calendar-shock or seasonality diagnostics, but do not call it the parallel-trends figure.

### Staggered treatment timing

Do not default to a conventional TWFE lead-lag plot when treatment effects may differ across cohorts or event time. Such coefficients can be contaminated by effects from other periods/cohorts. Use an estimator appropriate to the treatment path and estimand (for example, group-time ATT, interaction-weighted, imputation, or another design-appropriate method), then plot its event-time aggregation.

Also inspect event-time support and cohort composition. Long leads/lags may be identified by a shrinking and changing set of cohorts.

## Stata implementation patterns

### A. Raw trend data and figure

Prefer one grouped collapse rather than repeated `summarize` loops over periods and groups.

```stata
* Raw weighted outcome trends for the parallel-trends figure.
* POLICY_PERIOD is the numeric period in which treatment/policy begins.
* Recenter calendar time so the x-axis is relative event time.
preserve
    keep if sample_main == 1
    keep if !missing(outcome, treated, period, analysis_weight)

    gen int event_time = period - POLICY_PERIOD
    gen byte n_outcome = !missing(outcome)

    collapse (mean) outcome_mean=outcome ///
             (rawsum) n_outcome=n_outcome [aw=analysis_weight], ///
             by(event_time treated)

    save "${WorkFolder}/parallel_trends_raw_outcome.dta", replace

    twoway ///
        (connected outcome_mean event_time if treated == 0, sort) ///
        (connected outcome_mean event_time if treated == 1, sort), ///
        xline(-0.5, lpattern(dash)) ///
        xtitle("Periods relative to treatment") ///
        ytitle("Mean outcome") ///
        legend(order(1 "Comparison" 2 "Treated"))

    graph export "${OutputFolder}/figures/parallel_trends_raw_outcome.png", replace
restore
```

Replace `POLICY_PERIOD` with the numeric Stata month/quarter/wave used in the project. If treatment starts at the beginning of event time 0, `xline(-0.5)` visually separates the last untreated period (-1) from the first treated period (0). If the unit-period data are not unique, compute the intended unit-level/period-level mean and support count explicitly before collapsing. For staggered timing, do not construct a naive common `POLICY_PERIOD`; use treatment-specific event time and verify support/composition or use the design-appropriate event-study estimator.

### B. Event-study plotting from estimator output

Keep estimation and graphing conceptually separate. After the design-appropriate estimator produces an auditable dataset with one row per event time and variables such as `event_time`, `b`, and `se`, plot it directly:

```stata
* Event-study coefficient figure from stored estimator output.
gen ci_lo = b - invnormal(.975) * se
gen ci_hi = b + invnormal(.975) * se

sort event_time

twoway ///
    (rcap ci_hi ci_lo event_time) ///
    (connected b event_time, sort), ///
    yline(0, lpattern(dash)) ///
    xline(-0.5, lpattern(dash)) ///
    xtitle("Event time") ///
    ytitle("Estimate relative to reference period") ///
    legend(off)

graph export "${OutputFolder}/figures/event_study_outcome.png", replace
```

Use the estimator's own simultaneous confidence-band or plotting routine when uniform inference is required. Do not reconstruct standard errors incorrectly from rounded tables.

### C. Official Stata DID diagnostics

For designs that genuinely match `didregress`/`xtdidregress`, `estat trendplots` provides mean-outcome trend diagnostics and `estat ptrends` provides a formal linear parallel-trends test. Treat these as diagnostics only. A nonrejection from `estat ptrends` does not establish parallel trends, and the command is not a substitute for an event-study/sensitivity analysis when those are substantively needed.

### D. `xtevent`

For linear panel event-study designs that match its identifying setup, `xtevent`/`xteventplot` can provide standardized event-study visualization. Current functionality includes normalization at the period before treatment by default, pointwise intervals, uniform sup-t confidence bands, pretrend Wald-test p-values, endpoint handling, and trend overlays. Use it only when its model/estimand matches the design; software convenience does not validate identification.

### E. HonestDiD

When sensitivity to violations of parallel trends is a core concern, the Stata `honestdid` package implements Rambachan-Roth sensitivity analysis and can graph robust confidence sets over allowed deviations. Verify the current package documentation before coding because coefficient indexing depends on the preceding event-study estimator.

## Reporting checklist

A publication/review-ready parallel-trends figure note should make clear:

- outcome and sample;
- treated and comparison groups;
- event-time unit and how it is constructed from the underlying calendar period;
- treatment/implementation date and transition exclusions;
- weighting;
- fixed effects and controls for model-based figures;
- clustering/inference level;
- reference period or normalization;
- whether endpoint periods are binned;
- whether intervals are pointwise or simultaneous;
- estimator used, especially under staggered timing;
- that pre-trend diagnostics are not proof of counterfactual parallel trends.

## Sources and methodological basis

Use these as the main methodological references and verify current software documentation when exact syntax matters:

- Baker, Andrew, Brantly Callaway, Scott Cunningham, Andrew Goodman-Bacon, and Pedro H. C. Sant'Anna. 2026. "Difference-in-Differences Designs: A Practitioner's Guide." *Journal of Economic Literature* 64(2): 498-557. DOI: 10.1257/jel.20251650.
- Ghanem, Dalia, Pedro H. C. Sant'Anna, and Kaspar Wuthrich. 2026. "When Should Pre-trends Be Parallel?" *AEA Papers and Proceedings* 116: 64-69. DOI: 10.1257/pandp.20261109.
- Roth, Jonathan. 2022. "Pretest with Caution: Event-Study Estimates after Testing for Parallel Trends." *American Economic Review: Insights* 4(3): 305-322. DOI: 10.1257/aeri.20210236.
- Rambachan, Ashesh, and Jonathan Roth. 2023. "A More Credible Approach to Parallel Trends." *Review of Economic Studies* 90(5): 2555-2591. DOI: 10.1093/restud/rdad018.
- Miller, Douglas L. 2023. "An Introductory Guide to Event Study Models." *Journal of Economic Perspectives* 37(2): 203-230. DOI: 10.1257/jep.37.2.203.
- Freyaldenhoven, Simon, Christian B. Hansen, Jorge Perez Perez, Jesse M. Shapiro, and Constantino Carreto. 2025. "xtevent: Estimation and visualization in the linear panel event-study design." *Stata Journal* 25(1): 97-135. DOI: 10.1177/1536867X251322964.
- Sun, Liyang, and Sarah Abraham. 2021. "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics* 225(2): 175-199. DOI: 10.1016/j.jeconom.2020.09.006.
- Callaway, Brantly, and Pedro H. C. Sant'Anna. 2021. "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics* 225(2): 200-230. DOI: 10.1016/j.jeconom.2020.12.001.

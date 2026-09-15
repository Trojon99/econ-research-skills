# Stata causal-identification audit

Use this file when reviewing or proposing Stata code. The goal is to determine what the code estimates and whether it matches the causal design.

## First pass: reconstruct the code

Extract:

1. dependent variable;
2. treatment/exposure/instrument/running variable;
3. unit and time identifiers;
4. treatment cohort or event-time variable;
5. controls;
6. fixed effects;
7. sample restrictions;
8. analytic/frequency/probability weights;
9. clustering or other VCE choices;
10. estimator/package and important options;
11. post-estimation aggregation or plotting code.

Then state the implied estimand as precisely as possible.

## Generic regression and fixed-effects commands

For commands such as `regress`, `areg`, `xtreg`, or `reghdfe`:

- identify the coefficient that the user interprets causally;
- state the variation left after absorbed fixed effects;
- inspect whether treatment is collinear or nearly absorbed;
- inspect interactions and omitted categories;
- flag post-treatment controls;
- check whether group-by-time or unit-specific trends change the estimand or remove identifying variation;
- check whether clustering matches assignment and serial dependence;
- do not call a TWFE coefficient a valid DID estimate solely because unit and time FE are present.

## DID and event-study code

Possible commands include official Stata DID commands and community packages such as `csdid`, `eventstudyinteract`, `did_imputation`, `did_multiplegt_dyn`, `honestdid`, and related packages.

Because syntax and package versions can change, verify current documentation or the authors' repositories before giving exact syntax.

Audit these concepts regardless of command:

- cohort/first-treatment variable is correct;
- never-treated values are coded as the command expects;
- not-yet-treated observations are handled as intended;
- treatment is absorbing if the estimator assumes it;
- event time is defined relative to first treatment and not accidentally reset;
- omitted reference period is intentional;
- anticipation periods are handled explicitly;
- event-time support is adequate at each horizon;
- aggregation weights match the desired ATT/event-study estimand;
- standard errors are clustered at an appropriate level;
- code does not use already-treated units as controls when the estimator is intended to avoid that;
- post-estimation plots are not mixing coefficients from incompatible estimators or normalizations.

For conventional TWFE event-study code such as interactions of leads/lags plus unit/time FE, explicitly assess contamination from heterogeneous treatment effects under staggered adoption.

## RDD code

For `rdrobust`, `rdbwselect`, `rdplot`, `rddensity`, or related commands:

- verify the running variable and cutoff;
- confirm whether the running variable is centered or the cutoff option is used correctly;
- identify sharp versus fuzzy treatment assignment;
- check bandwidth selection and whether manual bandwidths were chosen ex ante or after inspecting results;
- check polynomial order and avoid defaulting to high-order global polynomials;
- distinguish conventional versus robust bias-corrected estimates/inference;
- check covariate use and whether covariates are predetermined;
- inspect mass points/discreteness and manipulation concerns;
- confirm clustering or sampling assumptions;
- ensure plots and formal estimators are not being interpreted as identical procedures.

## IV code

For `ivregress`, `ivreg2`, `ivreghdfe`, or related commands:

- identify endogenous regressors and excluded instruments;
- ensure included exogenous controls are treated consistently in first and second stages;
- inspect first-stage output and weak-identification diagnostics;
- inspect overidentification tests only as limited diagnostics, not proof of exclusion;
- verify robust/clustered inference choices;
- assess many-instrument concerns;
- check whether fixed effects remove most instrument variation;
- check whether standard first-stage rules are appropriate for the number of endogenous variables, instruments, heteroskedasticity, and clustering;
- use weak-ID-robust inference when needed and verify the implementation against current documentation.

## Shift-share code

If the instrument is constructed as a sum of shares times shocks:

- inspect the base period for shares;
- inspect whether shocks mechanically include the observation's own outcome/exposure and whether leave-one-out construction is needed;
- inspect concentration of shares/shocks and effective number of shocks;
- determine whether identification is shock-based or share-based;
- check inference at the correct level for that identification story.

Do not audit only the final `ivreg2` line; audit construction of the instrument upstream.

## Synthetic control code

Possible implementations include `synth`, `sdid`, or other community packages. Verify package provenance and current syntax.

Audit:

- treated unit and treatment period;
- donor-pool exclusions;
- predictor/pre-treatment windows;
- pre-fit metrics;
- placebo loops and their comparison set;
- whether donor units are contaminated or treated later;
- whether inference is valid for the number of treated units and design;
- whether a staggered setting requires a method designed for staggered adoption rather than repeated ad hoc SCM runs.

## Common code traps

Flag these when present:

- generating event time after dropping observations in a way that changes treatment cohorts;
- replacing missing treatment dates with arbitrary large/small numeric values without checking command semantics;
- using `post` indicators that switch on before actual treatment because of date coding;
- using calendar year instead of exact policy timing when treatment starts mid-period;
- coding treatment at the individual level when assignment occurs at a cluster level;
- clustering below the assignment level;
- absorbing a treatment-by-group interaction that is supposed to identify the effect;
- including outcomes or mediators measured after treatment as controls;
- selecting bandwidths/specifications by statistical significance;
- reporting only preferred horizons after looking at all event-time coefficients;
- interpreting an omitted base coefficient as estimated zero rather than a normalization;
- using `preserve`/`restore`, merges, duplicates, or collapse operations that silently change the estimation sample.

## How to report a code audit

Use three separate labels:

- **Implementation**: Does the code run the intended estimator?
- **Identification**: Would that estimator identify the stated causal parameter in this setting?
- **Inference**: Are the reported standard errors/confidence intervals/tests appropriate?

A code fix cannot repair a failed identification assumption. State this explicitly when relevant.

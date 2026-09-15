# Method map for causal identification

Use this file as a diagnostic map, not as a substitute for reading the relevant methodological literature. New variants and edge cases require a current literature search.

## Universal checks

For every design, establish:

- estimand and target population;
- assignment mechanism or source of identifying variation;
- comparison group/counterfactual;
- timing and treatment dynamics;
- interference/spillovers;
- selection into sample and attrition;
- post-treatment conditioning and bad controls;
- functional-form dependence;
- measurement error;
- level of statistical dependence and appropriate inference.

A regression coefficient is not automatically the desired causal estimand even when the regression contains unit and time fixed effects.

## Randomized and encouragement designs

Check randomization unit, treatment assignment probability, compliance, attrition, interference, stratification/blocking, cluster randomization, and whether analysis follows assignment or treatment received.

For encouragement designs, distinguish ITT from IV/LATE. Do not interpret treatment-on-treated effects without the assumptions needed for IV identification.

## Selection on observables / matching / weighting / doubly robust estimation

Core identification requires an unconfoundedness/conditional independence assumption plus overlap/positivity for the target estimand.

Audit:

- whether covariates are genuinely pre-treatment;
- whether important confounders are observed;
- overlap and extreme weights;
- estimand changed by trimming;
- specification sensitivity;
- whether matching or weighting creates balance on relevant covariates;
- outcome-model and propensity-model dependence;
- whether doubly robust language is used correctly.

Do not claim that propensity-score matching "solves endogeneity". It addresses selection on observed covariates under strong assumptions.

## Panel fixed effects

Ask what within-unit variation identifies the coefficient after all absorbed effects.

Audit:

- whether treatment changes within units;
- treatment timing and persistence;
- time-varying confounding;
- bad controls and simultaneous policies;
- dynamic responses and lag structure;
- serial correlation and clustering;
- heterogeneous treatment effects and implicit weighting;
- whether the FE regression is being misdescribed as DID when the required comparison structure is absent.

Unit FE remove time-invariant unit heterogeneity; they do not remove time-varying omitted variables.

## Canonical 2x2 DID

Target a clearly defined ATT/ATET.

Core assumptions commonly include:

- parallel trends for untreated potential outcomes over the relevant period;
- no anticipation before treatment;
- stable treatment definition and sample composition;
- no interference/spillovers that contaminate controls;
- no other differential shock coincident with treatment unless separately addressed.

Check level versus log scale and whether the parallel-trends claim is scale-sensitive.

Pre-treatment coefficients can reveal some violations but non-rejection does not establish parallel trends.

## Staggered-adoption DID and event studies

First determine whether treatment is absorbing. If not, route to switching/reversal methods rather than applying absorbing-treatment estimators mechanically.

Audit:

- cohort definition and first-treatment date;
- never-treated versus not-yet-treated controls;
- whether already-treated units serve as controls;
- treatment-effect heterogeneity across cohorts and event time;
- event-time support and composition across horizons;
- anticipation windows;
- weighting/aggregation used to construct a headline ATT or event-study path;
- pre-trend testing and sensitivity to deviations;
- inference with the actual treatment-assignment clusters.

Conventional TWFE event-study coefficients can mix cohort-time effects under heterogeneous treatment effects. Modern alternatives include group-time ATT approaches, interaction-weighted approaches, imputation estimators, and estimators designed for switching or nonbinary treatments. Choose based on the treatment path and target estimand, not popularity.

Seed literature to verify/update before use:

- Callaway and Sant'Anna (2021), "Difference-in-Differences with Multiple Time Periods," Journal of Econometrics.
- Sun and Abraham (2021), "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects," Journal of Econometrics.
- Goodman-Bacon (2021), "Difference-in-Differences with Variation in Treatment Timing," Journal of Econometrics.
- Borusyak, Jaravel, and Spiess (2024), "Revisiting Event-Study Designs: Robust and Efficient Estimation," Review of Economic Studies, DOI 10.1093/restud/rdae007.
- Roth, Sant'Anna, Bilinski, and Poe (2023), "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature," Journal of Econometrics.
- Rambachan and Roth (2023), "A More Credible Approach to Parallel Trends," Review of Economic Studies, DOI 10.1093/restud/rdad018.
- de Chaisemartin and D'Haultfoeuille (2024), "Difference-in-Differences Estimators of Intertemporal Treatment Effects," Review of Economics and Statistics.

For current applications, also search for post-2024 work on aggregation, continuous treatment, treatment reversals, few treated clusters, and alternative event-study estimators.

## Continuous or multivalued treatment in DID/panel settings

Do not assume a continuous treatment coefficient is a causal dose response under the same assumptions as binary DID.

Clarify:

- level versus change in treatment;
- existence of stayers or near-stayers;
- whether dose can rise and fall;
- whether the target is an average slope, dose-response contrast, or effect of a discrete treatment change;
- heterogeneity in marginal effects;
- support/overlap across treatment changes;
- whether linearity is substantive or merely convenient.

Search current methods before recommending an estimator because this literature is developing quickly.

## Triple differences (DDD)

DDD does not automatically repair a failed DID. State the additional comparison dimension and the identifying restriction it introduces.

Audit:

- which lower-order differences are differenced out;
- whether the third dimension has its own differential trends;
- whether treatment varies at the level needed to separate the triple interaction;
- whether fixed effects/interactions absorb the identifying variation;
- clustering at the treatment-assignment level;
- interpretation under heterogeneous effects.

## Regression discontinuity design (RDD)

Distinguish sharp, fuzzy, geographic/spatial, and local-randomization interpretations.

For continuity-based sharp/fuzzy RD, audit:

- exact assignment rule and cutoff;
- running-variable definition and measurement;
- ability to manipulate/sort around the cutoff;
- continuity of potential outcomes and other determinants at the cutoff;
- local polynomial order;
- bandwidth selection;
- robust bias-corrected inference where appropriate;
- predetermined covariate continuity/balance as diagnostics;
- density/manipulation diagnostics;
- mass points/heaping/discrete running variables;
- treatment compliance for fuzzy RD;
- local nature of the estimand and external-validity claims;
- multiple cutoffs or multiple running variables.

Avoid high-order global polynomials as a default. Do not choose bandwidth by significance hunting.

Seed literature to verify/update:

- Calonico, Cattaneo, and Titiunik (2014), "Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs," Econometrica.
- Calonico, Cattaneo, Farrell, and Titiunik (2017), "rdrobust: Software for Regression-Discontinuity Designs," Stata Journal.
- Calonico, Cattaneo, and Farrell (2020), "Optimal Bandwidth Choice for Robust Bias-Corrected Inference in Regression Discontinuity Designs," The Econometrics Journal, DOI 10.1093/ectj/utz022.
- Cattaneo, Jansson, and Ma (2018), manipulation/density testing work associated with `rddensity`.

Search current literature for discrete running variables, geographic RD, multiple cutoffs/scores, fuzzy RD power, local randomization, and newer inference refinements.

## Regression kink design (RKD)

Audit continuity/smoothness assumptions around the kink, the policy rule generating the slope change, manipulation of the running variable, functional form, bandwidth/local-polynomial choices, and whether the first-stage kink is strong enough for a fuzzy RKD interpretation.

Do not conflate a visible kink in an outcome graph with a valid RKD design.

## Instrumental variables (IV)

State the IV estimand and causal chain explicitly.

Audit:

- relevance/first stage;
- exclusion restriction;
- independence/exogeneity of the instrument;
- monotonicity or other assumptions needed for LATE interpretation;
- treatment take-up and compliers;
- weak identification;
- many instruments;
- heterogeneous effects and external validity;
- clustering and assignment level;
- direct channels, general-equilibrium effects, spillovers, or defiers that undermine interpretation.

Do not treat a large first-stage F statistic as evidence for exclusion. Do not interpret 2SLS as the population ATE unless additional assumptions justify that claim.

For weak instruments, use current weak-identification diagnostics and robust inference appropriate to heteroskedasticity/clustering/many instruments rather than relying mechanically on one historical cutoff.

Seed literature to verify/update:

- Angrist and Imbens (1994), LATE framework.
- Andrews, Stock, and Sun (2019), "Weak Instruments in Instrumental Variables Regression: Theory and Practice," Annual Review of Economics.
- Search current literature for weak identification with many instruments and clustered dependence before recommending an inferential procedure.

## Shift-share / Bartik instruments

State whether identification is justified by quasi-random shocks, quasi-random exposure shares, or another structure. These are not interchangeable stories.

Audit:

- construction of shares and shocks;
- whether shares are measured pre-treatment;
- concentration of identifying weight across shocks or sectors;
- correlation among shocks;
- endogenous exposure shares;
- leave-one-out or mechanical-correlation issues when relevant;
- appropriate shock-level or exposure-level inference;
- interpretation of the 2SLS estimand under heterogeneous effects.

Seed literature to verify/update:

- Goldsmith-Pinkham, Sorkin, and Swift (2020), "Bartik Instruments: What, When, Why, and How," American Economic Review.
- Borusyak, Hull, and Jaravel (2022), "Quasi-Experimental Shift-Share Research Designs," Review of Economic Studies, DOI 10.1093/restud/rdab030.

## Synthetic control and related panel counterfactual methods

Audit:

- treated unit(s) and treatment date(s);
- donor pool and contamination;
- pre-treatment fit;
- predictor/outcome weighting choices;
- length and informativeness of the pre-treatment period;
- interpolation versus extrapolation;
- spillovers into donor units;
- placebo/permutation or other inference and whether it matches the design;
- treatment-effect heterogeneity and staggered adoption;
- covariates and low-rank/interactive-factor structure when using extensions.

Poor pre-treatment fit is a design warning, not a cosmetic problem.

Relevant families include classical SCM, augmented SCM, synthetic DID, matrix completion/interactive fixed effects, and newer staggered or multiple-outcome extensions. Search current literature before choosing among them.

Seed literature to verify/update:

- Abadie, Diamond, and Hainmueller (2010), classical synthetic control.
- Abadie (2021), "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects," Journal of Economic Literature.
- Arkhangelsky, Athey, Hirshberg, Imbens, and Wager (2021), "Synthetic Difference-in-Differences," American Economic Review.
- Ben-Michael, Feller, and Rothstein (2021), augmented synthetic control.
- Athey, Bayati, Doudchenko, Imbens, and Khosravi (2021), matrix completion for causal panel data.

## Time-series shocks, local projections, and macro identification

Do not call a time-series regression causal without an explicit shock-identification argument. Determine whether identification comes from timing restrictions, external instruments, narrative shocks, high-frequency surprises, sign restrictions, or another design.

Audit shock exogeneity, anticipation, information effects, serial correlation, horizon overlap, state dependence, instrument strength, and whether the estimated impulse response corresponds to the intended structural shock.

Search specialized current literature when this family is invoked.

## Spatial and network exposure designs

Check interference and exposure mapping explicitly. Standard SUTVA is often implausible.

Audit direct versus spillover effects, geographic sorting, spatially correlated shocks, exposure definitions, partial interference assumptions, and spatial inference.

If the user's design relies on a specialized network/spatial causal estimator, search the current literature rather than extrapolating from ordinary DID or IV.

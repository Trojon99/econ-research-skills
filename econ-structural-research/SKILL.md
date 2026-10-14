---
name: econ-structural-research
description: Use for structural and quantitative economics research.
version: 0.1.0
author: Panfeng Hu (Trojon99), Hermes Agent
metadata:
  hermes:
    tags: [economics, structural, quantitative, estimation, welfare]
---

# Structural and Quantitative Economics Research

Develop, audit, estimate, and validate structural or quantitative economic models. Choose modeling complexity to answer the economic question, not to demonstrate a technique. This workflow complements reduced-form research and does not replace model-specific literature.

## When to Use

- Structural identification, calibration, estimation, simulation, or computational economics.
- Dynamic choice, household or firm decisions, industrial organization, quantitative macroeconomics, equilibrium models, or transition dynamics.
- Model-based policy counterfactuals, welfare analysis, or audits of numerical model results.
- Do not force descriptive, causal reduced-form, measurement, or theory projects into an estimated structural model. Explain why primitives, an unsupported counterfactual, or equilibrium feedback require modeling when proposing one.

## Prerequisites

Use the user's current materials and project instructions first. Read relevant files with `read_file` and `search_files`; verify necessary institutional facts, citations, external parameter values, and software behavior with reliable sources. Never invent access, moments, estimates, convergence, or results. Use Chinese for discussion and academic English for formal research writing. If a key choice is missing and changes the analysis, ask rather than silently assuming it; exploratory assumptions must be explicit.

Tool names here refer to Hermes capabilities. On another assistant platform, use its equivalent permitted file-reading, source-retrieval, and code-execution tools; do not invent unavailable tool APIs.

## Procedure

### 1. Specify the economic object

State the question, population and period, baseline, policy experiment, and estimand or economic object. Distinguish causal treatment effects, preference or technology parameters, mechanisms, predictive objects, equilibrium outcomes, and welfare. Explain what evidence or model restriction could discriminate the favored mechanism from credible rivals. A structural parameter and a reduced-form coefficient are not interchangeable.

### 2. Make the model explicit

List agents, states, actions, timing, information, expectations, constraints, and initial conditions. Define preferences, technologies, endowments, shock distributions, transition laws, and institutional rules. Label each object as measured, estimated, externally fixed, or maintained. Specify the solution or equilibrium concept and market clearing where relevant. Address existence, multiplicity, and equilibrium selection rather than assuming a numerical solution is unique. For macro models, define units, stocks versus flows, aggregation, identities, shock processes, and whether the object is a steady state or a transition.

### 3. Map observations to model objects

Document exact variable definitions, sample restrictions, units, aggregation, observation frequency, and time alignment. Address measurement error, latent states, proxy variables, missingness, censoring, attrition, and selection. Identify where a model variable differs from an observed variable. Preserve raw data and use auditable derived files; do not silently modify the user's existing specification or data workflow.

### 4. Audit identification before optimizing

For each parameter, identify the moments, variation, exclusions, normalization, or functional-form restrictions that inform it. Explain why the parameter is not observationally equivalent to another parameter or mechanism. Distinguish identification from precise estimation and numerical optimizer success. Inspect moment sensitivities, objective profiles, rank diagnostics where applicable, and alternative parameter sets; local rank does not establish global identification. Document weak identification and scale/location normalizations. Justify external values for the relevant population and period, and sensitivity-test them. A good in-sample fit is not identification.

### 5. Define estimation or calibration

Specify likelihood or moments, weighting, sample construction, estimation targets, parameter transformations and bounds, simulation size, seeds, and stopping criteria. For simulated criteria, justify simulation design and use common random numbers where appropriate; test simulation noise rather than hiding it. Explain whether reported values are externally fixed, calibrated, or statistically estimated. Describe sampling uncertainty and the resampling unit or dependence structure; include first-stage uncertainty when relevant. Do not apply regular asymptotic intervals automatically to weakly identified, boundary, or nonregular objects.

### 6. Build and exercise a reproducible solver

Separate primitives, solver, measurement/moment mapping, estimation, validation, and counterfactual code. Use `terminal` or `execute_code` for calculations and real execution, not mental arithmetic or fabricated outputs. Record source code version, sample, configuration, software versions, grid, tolerances, optimizer settings, and seeds. Preserve existing entrypoints unless an authorized change is necessary.

Validate feasibility and budgets, Bellman or first-order conditions as appropriate, probability and distribution normalization, equilibrium and accounting residuals, and boundary behavior. Treat corner solutions with the appropriate conditions rather than demanding interior equalities. Test grid refinement, interpolation, tolerances, initial values, simulation size, and economically meaningful limiting cases or simpler benchmarks. Independent residual checks must test the computed solution, not merely repeat the solver's stop flag. Save failed convergence and optimizer diagnostics; never label an unconverged or infeasible run as an estimate. For stochastic approximations, report the applicable error criterion rather than imposing irrelevant exact residual tests.

### 7. Validate economic implications

Label estimation-target fit as in-sample. Use untargeted moments, held-out evidence, institutional predictions, or independent reduced-form evidence when feasible. Explain what failure would challenge the model rather than narrating every result as support. Do not count the same empirical evidence once as an estimation target and again as independent validation. Check parameter plausibility, heterogeneity, alternative specifications, and sensitivity to target selection and weighting. Keep numerical error, simulation error, sampling uncertainty, identification uncertainty, and specification uncertainty separate.

### 8. Close the counterfactual

State what policy or primitive changes, what stays fixed, which agents respond, and whether prices, participation, composition, market clearing, financing, expectations, and transition paths adjust. Explain partial versus general equilibrium and any equilibrium-selection rule. Re-solve the relevant decision and equilibrium problems rather than changing a fitted outcome mechanically. State when preference, technology, or institutional invariance is an assumption. Qualify extrapolation outside supported variation and distinguish comparative steady states from realized transition paths.

### 9. Make welfare claims auditable

Specify whose welfare, the metric, discounting, baseline, aggregation and distributional weights, price changes, transition costs, policy financing, and transfers. Avoid treating transfers as net resource losses without accounting for recipients and financing. Explain what is omitted and whether reported willingness-to-pay, compensating variation, equivalent variation, or utility changes require extra assumptions. Distinguish estimated mechanisms from maintained normative and model assumptions. Report sensitivity, distributional consequences, and uncertainty rather than only an aggregate point estimate.

### 10. Deliver the requested result

Keep conversational design advice proportional to the current question. Do not produce a full proposal or select a narrative on the user's behalf unless requested. For requested computation, deliver exercised code and actual outputs, with convergence, residuals, fit versus validation, uncertainty, and run provenance. Clearly state any blocked or incomplete acceptance criterion and the cheapest informative repair.

## Optional frontier reference

Load `references/nber-frontier.md` when approximate latent-variable estimation or capacity-policy counterfactuals are relevant. These full-text-grounded working-paper lessons are provisional and do not replace the workflow or local project overlays.

## Pitfalls

- Complexity does not fix absent identifying variation or poorly measured objects.
- An optimizer's success status does not establish a correct equilibrium, unique optimum, or identified parameter.
- Calibration targets and reduced-form evidence are not independent validation when reused.
- A steady-state difference is not a transition welfare calculation.
- Stated preferences do not automatically identify revealed choices or policy welfare.
- Do not change raw data, remote/SSH settings, credentials, unrelated profiles, or access iCloud files. Profile management and research execution may occur on different machines; preserve that separation.

## Verification

Before claiming completion, check that the research question and model objects are explicit; every reported parameter has an identification or external-value justification; all calculations come from actual runs; solver and equilibrium diagnostics pass or failures are disclosed; targets and independent validation are distinguished; counterfactual closure and welfare assumptions are stated; and provenance and uncertainty are documented. Cite only sources actually verified and never invent empirical results or citations.

## Optional applied reference

Load `references/evidence-to-equilibrium.md` on demand for reduced-form evidence, structural identification and equilibrium closure. This reference distinguishes tutorial reading, primary-source checks and unexecuted software; it does not establish numerical validation.

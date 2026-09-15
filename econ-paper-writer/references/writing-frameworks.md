# Writing Frameworks

## Contents

1. General standard
2. Reduced-form empirical papers
3. Quantitative structural papers
4. Hybrid empirical-structural papers
5. Abstract architecture
6. Introduction architecture
7. Literature reviews
8. Results and quantitative claims
9. Choosing an empirical architecture
10. Capatina reference patterns

## General standard

Treat a paper as a sequence of economic functions, not a collection of elegant sentences. Make the question, evidence, mechanism, and implication easy to recover. Use technical detail only when it advances identification, measurement, model interpretation, or replication.

Prefer:

- concrete subjects and active verbs;
- explicit comparison groups and counterfactuals;
- calibrated verbs such as "is consistent with," "suggests," "implies in the model," and "we estimate";
- numbers that identify the estimand, unit, group, and benchmark;
- transitions that explain why the next section or exercise is necessary.

Avoid:

- generic claims that a topic is "important" without economic content;
- inflated novelty language;
- causal verbs unsupported by the stated design;
- long lists of papers without synthesis;
- vague references such as "this result" when several results precede it.

## Reduced-form empirical papers

Use this default sequence:

1. State the economic question and why the setting can answer it.
2. Explain the institutional variation or source of identification.
3. Define the data, sample, treatment, comparison, and outcomes.
4. State the estimating design and identifying assumption at the appropriate level.
5. Report the main estimate with magnitude and benchmark.
6. Present validation, dynamics, heterogeneity, or mechanisms in the order needed for interpretation.
7. Delimit what the estimate identifies and avoid broader structural or welfare claims unless supplied.

In empirical-strategy prose, distinguish:

- the source of variation;
- the estimand;
- the maintained identifying assumption;
- threats and the supplied checks that address them.

Write the economic comparison before treating the estimator as self-explanatory. Describe data as measurement rather than storage: connect variables and sample construction to the concepts they represent. In results prose, separate the estimate from its scale and interpretation when combining them would obscure either object. Present robustness checks as evidence about named threats. Treat subgroup or auxiliary-outcome patterns as mechanism evidence only when the supplied logic connects them to the proposed channel.

For a major rewrite, classify the empirical paper as causal reduced-form, descriptive or measurement-focused, event-study, policy evaluation, or mixed empirical-model. Use that classification to keep the central object visible: a treatment effect, a measurement contribution, a dynamic pattern, a policy exposure, or empirical evidence that disciplines a model.

Apply these section-level checks when the supplied material supports them:

- **Introduction:** state the setting, data, and identifying variation before an extended literature discussion; preserve the main result, its magnitude, and any strategically important mechanism or secondary contribution.
- **Data:** identify the dataset, sample period, unit of observation, coverage, sample construction and restrictions, final sample size, key variables, units, transformations, missingness, measurement limits, and selection concerns that affect interpretation.
- **Results:** begin with the main estimate or plotted pattern rather than warm-up specifications. Separate coefficient interpretation, statistical precision, specification stability, economic magnitude, and causal interpretation.
- **Null or imprecise results:** state what the supplied confidence interval can or cannot rule out. If a power calculation is needed but absent, mark it as a missing input rather than inferring adequate or inadequate power.
- **Robustness:** name the threat each check addresses and report whether the evidence changes the interpretation; do not present an unexplained inventory of specifications.
- **Heterogeneity:** give the economic reason for each group comparison, report the relevant estimates and benchmarks, and delimit claims when subgroup precision is weak.
- **Mechanisms:** separate the proposed channel, the observed pattern, the evidence bearing on the channel, and the remaining caveat. Do not treat a suggestive subgroup pattern as direct identification of a mechanism.

## Quantitative structural papers

Use this default sequence:

1. Pose the economic question in terms of decisions, dynamics, mechanisms, or policy counterfactuals. Explain, using the author's supplied material, which object descriptive or reduced-form evidence cannot recover and why a model is needed.
2. Establish the data facts the model must explain.
3. Define the economic environment: agents, timing, states, choices, payoffs, constraints, information, and equilibrium concept.
4. Separate model primitives, endogenous objects, estimated parameters, calibrated parameters, and external inputs.
5. Introduce only the model ingredients needed to map the data facts into the mechanisms or policy objects of interest.
6. Connect each estimated or calibrated parameter to the data variation, moments, external evidence, or maintained assumptions that discipline it.
7. Describe estimation and computation transparently enough for the reader to understand the objective, moments or likelihood, numerical procedure, and source of uncertainty when supplied.
8. Demonstrate model fit on outcomes relevant to the intended exercises, separating targeted from untargeted moments and fit from identification.
9. Define each counterfactual before reporting its results: the baseline, policy or primitive changed, objects held fixed, equilibrium adjustment, and aggregation rule.
10. Report behavioral responses, distributional incidence, fiscal effects, and welfare separately before combining them into an overall interpretation.
11. State which findings are model implications rather than direct empirical estimates and keep their dependence on maintained assumptions visible.

For theory and structural exposition, establish the agents, choices, timing, information, and central friction in prose before dense notation when the supplied material allows it. Explain the economic role of a maintained assumption when that role matters for the result. After a proposition, comparative static, or counterfactual result, state the incentive, constraint, or equilibrium force behind it rather than leaving the reader with only a formal sign or numerical change. Keep that intuition within the author's supplied model; do not invent a mechanism to make the prose smoother.

Do not describe a model as credible merely because it is detailed. Ground model relevance in its mapping to data, targeted and untargeted fit, and the economic purpose of each exercise.

Use calibrated structural language. Write that a model is designed to capture an object, that estimates are informative about a parameter, that a counterfactual illustrates an implication, or that a welfare calculation follows under maintained assumptions when stronger language is not warranted.

Adapt emphasis to the structural family named in the supplied material:

- for IO demand and market-power papers, keep consumer choice, pricing, markups, merger or policy changes, and market definition distinct;
- for dynamic discrete-choice papers, make states, timing, continuation values, switching costs, expectations, and solution or approximation methods recoverable;
- for search and matching papers, distinguish search effort, offers or applications, matching, bargaining, durations, and equilibrium tightness;
- for quantitative macro and heterogeneous-agent papers, separate calibration or estimation, cross-sectional and transition dynamics, aggregation, equilibrium, and policy experiments;
- for trade and spatial papers, distinguish bilateral or local variation, mobility or commuting, market access, equilibrium adjustments, and welfare aggregation;
- for auctions and market-design papers, define information, strategies, allocation and payment rules, equilibrium, identification, and the policy or mechanism counterfactual.

Before finalizing structural prose, verify that it states why the model is needed, which assumptions matter, what disciplines the key parameters, whether the reported fit bears on the counterfactual, how the counterfactual is defined, and what the welfare measure represents. If a missing or inconsistent element materially affects interpretation, use the main skill's pause protocol. Surface the issue without proposing new assumptions, sensitivity exercises, or a redesigned model on the author's behalf.

## Hybrid empirical-structural papers

Build a bridge rather than two disconnected papers:

1. Use reduced-form or descriptive evidence to establish motivating facts.
2. Explain which policy question or mechanism remains unidentified from those facts alone.
3. Introduce the model as the device that supplies the missing mapping.
4. Show how empirical variation disciplines key model objects.
5. Return to the motivating evidence when interpreting mechanisms and counterfactuals.

Use explicit bridge sentences that state what the empirical analysis establishes and what additional object the model is needed to recover.

## Abstract architecture

A compact abstract should make the paper's core objects recoverable without forcing a fixed number of sentences or a universal word count. When supported by the supplied material, include:

1. the question, economic object, or puzzle;
2. the setting, data, design, measurement contribution, or model used to answer it;
3. the main result with direction and an interpretable magnitude when available;
4. a mechanism, counterfactual, or strategically important secondary contribution when it is part of the paper's claim;
5. the warranted interpretation or contribution.

Prefer reader order over author workflow. Do not spend the opening on broad importance while postponing the result. Do not name a method without making the economic comparison or model role intelligible. Do not delete a central mechanism or secondary contribution solely to satisfy a default length convention.

## Introduction architecture

A strong introduction often performs these functions:

1. Ask a concrete economic question.
2. State the paper's approach and central mechanism.
3. Explain the data and empirical or model framework.
4. Summarize main quantitative results with interpretable magnitudes.
5. Explain mechanism decomposition, heterogeneity, or policy experiments.
6. Position contributions relative to verified literature.
7. Give a short roadmap when useful.

The order may vary. Preserve the paper's logic rather than forcing a fixed paragraph count.

## Literature reviews

Organize sources by their role in the paper:

- what is known about the outcome;
- what identifies the relevant causal relationship;
- what mechanisms prior models include or omit;
- what institutional or population setting differs;
- what object the current paper measures or quantifies.

For each cluster:

1. state the shared question or approach;
2. synthesize the relevant findings at the evidence level available;
3. identify the precise relationship to the current paper using only the author's supplied positioning.

Avoid asserting a gap solely because a search returned no item. Say that the current Zotero corpus does not cover the category.

## Results and quantitative claims

Report a result in this order when applicable:

1. direction;
2. magnitude and unit;
3. reference group or baseline;
4. statistical uncertainty for estimates;
5. economic interpretation;
6. heterogeneity or mechanism;
7. limitation of the claim.

For counterfactuals, distinguish accounting changes, behavioral responses, equilibrium responses, government-budget effects, and welfare effects.

## Choosing an empirical architecture

Use one coherent empirical backbone. Add complementary designs only when each answers a distinct inferential question.

### Policy exposure across cohorts and places

Introduce:

1. the policy rule and implementation timing;
2. why exposure varies across cohorts and places;
3. the treatment and comparison dimensions;
4. direct evidence that the policy changed the intended first-stage object;
5. event-study or placebo patterns that map onto predicted exposure;
6. outcome estimates, mechanisms, and any fiscal accounting.

Make the identifying comparison concrete before giving the regression equation.

### Admission cutoffs and multiple education choices

State the economically relevant alternative, not merely the treatment label. When choices are unordered, explain why the next-best option differs across people and how the data reveal it. Interpret estimates locally for applicants whose choices are shifted by the cutoff.

### A main design with complementary evidence

When a paper uses difference-in-differences plus regression discontinuity, value-added measures, or mechanism data:

- identify the main design;
- state the principal threat;
- explain exactly which auxiliary design addresses which question;
- keep estimates from different designs conceptually separate;
- synthesize them only after their estimands and populations are clear.

### Experiment plus structural model

Explain the division of labor:

- the experiment supplies credible exogenous variation and validates selected responses;
- the model interprets mechanisms, handles dynamics or equilibrium effects, and evaluates policies outside the experimental treatment.

State what the experimental contrast identifies by itself and which additional assumptions the structural analysis requires.

## Capatina reference patterns

The initial reference corpus includes:

- Elena Capatina, "Life-cycle effects of health risk," *Journal of Monetary Economics* (2015).
- Elena Capatina and Michael Keane, "Health Shocks, Health Insurance, Human Capital, and the Dynamics of Earnings and Health," *Journal of Political Economy* (2026).

Use these papers as structural-writing references, not as universal templates.

### 2015 pattern

The paper moves from a sharply delimited question about health risk to a unified life-cycle framework, data and calibration, model performance, and controlled quantitative experiments. Its introduction identifies multiple channels, explains why they must be studied jointly, describes the model and calibration, previews the experiments, and reports economically interpretable magnitudes. The quantitative section separates removal of health effects from removal of risk around conditional averages, which keeps the counterfactual objects distinct.

Transferable writing lessons:

- enumerate mechanisms early when later exercises separately quantify them;
- justify a unified framework through interactions among mechanisms;
- connect calibration fit to the legitimacy of the subsequent quantitative exercises;
- describe each experiment by the object changed and the object held fixed;
- report heterogeneity using concrete group comparisons.

### 2026 pattern

The paper opens with linked questions about health shocks, life-cycle outcomes, inequality, and insurance. It develops the mechanism before technical detail: immediate lost work, future health and productivity, reduced experience accumulation, and behavioral responses. It then connects a rich life-cycle model to several datasets, measurement corrections, model fit, mechanism decompositions, insurance counterfactuals, fiscal effects, welfare, and demographic heterogeneity.

Transferable writing lessons:

- state dynamic amplification clearly before presenting the model;
- explain how the model unifies previously separate conceptual approaches;
- distinguish treatment access, treatment choice, insurance, and payment mechanisms;
- name the data contribution and measurement problem alongside the model;
- preview decompositions using mutually intelligible channels;
- separate direct earnings effects, human-capital effects, health-productivity effects, and behavioral effects;
- present policy results as a balanced accounting of utilization, labor supply, transfers, revenue, longevity-linked costs, net cost, and welfare;
- place the formal literature review after the introduction when the contribution spans several literatures and needs more space.

Do not copy sentence-level phrasing from either paper. Apply their functional architecture only when it matches the user's task.

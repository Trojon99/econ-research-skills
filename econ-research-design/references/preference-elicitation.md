# Preference Elicitation in Economics and Health Economics

Use this reference when designing, reviewing, interpreting, or explaining a preference-elicitation study. Treat preference elicitation as a family of measurement strategies, not as a single estimator.

## 1. Start from the preference object

Before choosing a method, identify:

1. **Whose preferences?** Patients, caregivers, clinicians, consumers, citizens, payers, or another decision maker.
2. **Preferences over what?** Treatments, services, product attributes, health states, risks, time, money, policy features, or complete alternatives.
3. **For which decision?** Treatment design, benefit-risk assessment, reimbursement, service design, priority setting, welfare analysis, or QALY valuation.
4. **Which output is needed?** Ordinal ranking, marginal utility weights, marginal rates of substitution, WTP/WTA, maximum acceptable risk, choice probabilities, latent classes, or health-state utility values.
5. **What behavioral environment matters?** A hypothetical stated-choice environment or observed revealed behavior.

Do not select DCE, BWS, TTO, SG, or contingent valuation before these are clear.

## 2. Method map

### Discrete choice experiment (DCE) / choice-based conjoint
Use when the object is a multi-attribute alternative and the target is trade-offs among attributes. Respondents repeatedly choose among alternatives whose attribute levels vary experimentally.

Typical outputs: preference coefficients, MRS, WTP, maximum acceptable risk, predicted choice probabilities, preference heterogeneity.

### Best-worst scaling (BWS)
Use when repeated best/worst judgments are substantively defensible. Distinguish:
- object case: choose best/worst items;
- profile case: choose best/worst attribute levels within one profile;
- multiprofile case / best-worst DCE: choose best/worst alternatives.

Do not assume BWS is automatically superior to a single-best DCE. Evidence shows methods can produce different preference estimates, and worst choices can be noisier in some settings.

### Contingent valuation / direct WTP-WTA
Use when the monetary valuation itself is the main object and a defensible hypothetical market/scenario can be constructed. Audit anchoring, starting-point effects, protest responses, strategic responses, and hypothetical bias.

### Time trade-off (TTO) and Standard Gamble (SG)
Use primarily for health-state valuation when the object is utility anchored to health/death states rather than preferences over treatment attributes. TTO trades longevity against health quality; SG trades health outcomes against risk. Do not treat either as interchangeable with a treatment DCE.

### Rating/ranking/VAS and simple importance scores
Useful for descriptive elicitation or task development, but they do not generally recover the same trade-off information as choice-based methods. Avoid interpreting a 1-5 importance score as an economic marginal rate of substitution.

### Revealed preference
Infer preferences from observed choices in real markets or behavior. This may improve behavioral realism but requires a model of constraints, prices, information, choice sets, and selection. Observed behavior is not a pure readout of preferences.

## 3. DCE economic foundation

Start from random utility:

`U_njt = V_njt + epsilon_njt = beta' X_njt + epsilon_njt`

The deterministic utility component must match the attribute coding and hypotheses. Choice probabilities depend on assumptions about the error distribution and substitution pattern.

Conditional logit is a useful benchmark but imposes restrictive homogeneity and IIA-type structure. Consider mixed logit/random-parameter logit when preference heterogeneity and repeated choices matter; latent class models when discrete preference types are substantively meaningful. Do not choose a more complicated estimator merely because it fits better.

Repeated tasks from the same respondent create panel structure. Estimation and uncertainty should respect within-person dependence.

## 4. Attribute and level development

Treat attribute development as substantive measurement, not questionnaire decoration.

Build attributes from the decision context using literature, qualitative interviews/focus groups, expert input, policy documents, and/or prior data as appropriate. Attributes should be:
- salient to the decision;
- conceptually distinct enough to permit interpretation;
- actionable or decision-relevant where possible;
- understandable to respondents;
- capable of realistic and sufficiently varying levels;
- comprehensive enough to avoid obvious omitted features without producing excessive task burden.

Audit whether one attribute is a label/bundle for several others. If a study includes both a certification label and the practices that certification bundles, ask whether the label has utility beyond its component practices and whether collinearity or interpretation becomes problematic.

Levels should be plausible, span policy-relevant ranges, and permit identification of the desired trade-offs. Range matters for apparent attribute importance.

## 5. Choice-task construction

Specify:
- number of alternatives;
- labeled versus unlabeled alternatives;
- opt-out, neither, or status-quo alternative;
- forced choice versus voluntary choice;
- number of tasks per respondent;
- ordering/randomization;
- blocking;
- dominance or plausibility constraints;
- visual presentation and comprehension aids.

An outside option is not cosmetic. It changes the decision being modeled and may be necessary when real-world consumers can decline all offered alternatives.

Avoid implausible combinations simply to maximize statistical efficiency. Statistical efficiency cannot repair a choice task that respondents do not regard as meaningful.

## 6. Experimental design

The design must identify the parameters in the intended model. Track:
- full/fractional factorial structure;
- orthogonality/balance versus efficiency-based design;
- D-, A-, or other efficiency criteria when used;
- zero versus informative Bayesian priors;
- pilot-derived priors;
- blocking and allocation of tasks;
- level overlap and constraints;
- interactions/nonlinear effects that must be separately identified.

Follow the principle emphasized in ISPOR experimental-design guidance: choose the design conditional on study objectives and the statistical model, not by software default.

## 7. Coding and interpretation

State the coding explicitly.
- dummy coding gives coefficients relative to an omitted reference level;
- effects coding changes coefficient interpretation and reference reconstruction;
- continuous coding imposes functional form across levels.

Never rank attributes by raw coefficient magnitude when attributes use different coding or level ranges.

For a monetary attribute with coefficient `beta_cost`, a marginal WTP for a change can often be represented as:

`WTP = - DeltaV_attribute / beta_cost`

For a single linear coefficient this reduces to a coefficient ratio. Report uncertainty around ratios, not only numerator/denominator standard errors. Confirm sign and functional-form assumptions for cost.

Maximum acceptable risk and time trade-offs use analogous marginal-rate-of-substitution logic only when the utility specification supports that interpretation.

## 8. Preference heterogeneity versus scale heterogeneity

This distinction is mandatory when comparing people or groups.

Observed coefficient differences can arise because:
- tastes differ; or
- error variance/choice consistency differs, changing the scale of utility coefficients.

Because random-utility coefficients are identified relative to error scale, raw coefficient comparisons across samples, survey modes, countries, or subgroups can confound preference and scale heterogeneity.

Use models or normalizations appropriate to the substantive comparison, and phrase claims cautiously when scale is not separately identified.

## 9. Decision heuristics and attribute non-attendance

Respondents may simplify tasks by ignoring attributes, using lexicographic rules, always choosing the cheapest option, or focusing on one salient feature. These behaviors may reflect true preferences, cognitive burden, or task artifacts.

Do not mechanically delete respondents who fail an internal test. Diagnose whether the behavior invalidates the target interpretation. Attribute-non-attendance models, stated attendance questions, response-time evidence, and sensitivity analyses can be informative but each has its own measurement assumptions.

## 10. Validity and quality audit

Separate:

### Content validity
Do attributes, levels, wording, and tasks represent the intended decision and population?

### Comprehension and response process
Use cognitive interviews, think-aloud work, piloting, comprehension checks, and debrief questions where appropriate.

### Internal validity
Possible diagnostics include dominance/rationality tasks, repeated choices, transitivity-related checks, monotonicity, response time, and stability. Do not equate passing one test with proof of valid preferences.

### Reliability
Assess repeated-task or test-retest stability when relevant.

### External validity
Ask whether hypothetical choices predict or correspond to consequential choices in the target setting. Stated-preference estimates do not automatically equal real-world behavior.

### Representativeness
Audit sampling frame, response/nonresponse, exclusions, weighting, and whether the intended decision population is actually represented.

## 11. Sample size

Do not rely mechanically on a single rule of thumb. Sample requirements depend on the number of alternatives, tasks, levels, parameterization, desired subgroup/heterogeneity analysis, priors, design efficiency, and estimator.

Rules such as the Johnson-Orme heuristic can be rough planning devices for simple main-effects designs, not a substitute for design-specific simulation or precision/power analysis. Prefer simulation when the final design and target estimands are known.

## 12. DCE versus causal inference

A DCE experimentally varies attributes inside a survey task, which supports interpretation of how those task attributes change stated choices under the experimental choice environment. It does not by itself identify the causal effect of adopting the corresponding real-world policy, treatment, or service on health, education, employment, or other outcomes.

If a paper combines a preference experiment with a policy-effect claim, separate the two identification problems and invoke the causal-inference framework for the latter.

## 13. Health-state valuation is a distinct branch

For QALY/health-state valuation, first ask whether the target is a utility scale anchored at full health and death, a latent health-state value, or a preference ordering. TTO, SG, DCE-based valuation, VAS, and hybrid models impose different assumptions and anchoring strategies.

Do not import WTP interpretation into TTO/SG mechanically. When valuing instruments such as EQ-5D, verify the protocol and current value-set methodology relevant to the jurisdiction before recommending an estimator or elicitation format.

## 14. Minimum audit template

When reviewing a preference study, answer:

1. What exact preference object is being estimated?
2. Why is this elicitation method appropriate relative to alternatives?
3. How were attributes/items and levels developed?
4. What is the choice task and outside option?
5. How was the experimental design generated and piloted?
6. What population and sample are represented?
7. What utility/choice model is estimated and how are variables coded?
8. How are repeated tasks and heterogeneity handled?
9. Could scale differences be mistaken for preference differences?
10. How are WTP/MRS/risk trade-offs computed and uncertainty quantified?
11. What validity, reliability, and response-quality evidence is shown?
12. What can the estimates legitimately imply for actual decisions, welfare, or policy?

## 15. Core sources and current guidance

When current guidance matters, verify the latest version online. Anchor searches in primary or authoritative sources.

- Johnson FR, Lancsar E, Marshall D, et al. *Constructing Experimental Designs for Discrete-Choice Experiments: Report of the ISPOR Conjoint Analysis Experimental Design Good Research Practices Task Force.* Value in Health 2013;16(1):3-13.
- Hauber AB, González JM, Groothuis-Oudshoorn CGM, et al. *Statistical Methods for the Analysis of Discrete Choice Experiments: A Report of the ISPOR Conjoint Analysis Good Research Practices Task Force.* Value in Health 2016;19(4):300-315.
- Mühlbacher AC, Kaczynski A, Zweifel P, Johnson FR. *Experimental measurement of preferences in health and healthcare using best-worst scaling: an overview.* Health Economics Review 2016;6:2.
- Whitty JA, Oliveira Gonçalves AS. *A Systematic Review Comparing the Acceptability, Validity and Concordance of Discrete Choice Experiments and Best-Worst Scaling for Eliciting Preferences in Healthcare.* Patient 2018;11:301-317.
- Krucien N, Sicsic J, Ryan M. *For better or worse? Investigating the validity of best-worst discrete choice experiments in health.* Health Economics 2019;28:572-586.
- FDA. *Incorporating Voluntary Patient Preference Information over the Total Product Life Cycle.* Final Guidance, March 2026. Use it when the decision context involves regulatory patient-preference information.

Treat these as anchors, not a frozen canon. For new studies, regulatory submissions, software-specific advice, sample-size simulation, or claims about current best practice, search and verify newer guidance and methodological evidence before answering.

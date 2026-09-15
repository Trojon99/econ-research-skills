# Benchmark Corpus

## Contents

1. How to use the corpus
2. Reduced-form benchmarks
3. Structural and hybrid benchmarks
4. Task-to-benchmark routing

## How to use the corpus

Use these papers as references for functional architecture, paragraph roles, sequencing, and calibrated reporting. Do not treat their substantive findings as facts available for a new draft unless the paper is also verified in the user's current Zotero corpus or supplied materials. Do not copy distinctive wording.

Choose the smallest relevant subset. A literature review may need several benchmarks for organization, but a paragraph rewrite rarely needs more than one.

When full text is available, learn at four levels without imitating surface language:

- **paper architecture:** the order in which the question, design or model, evidence, limitations, and implications appear;
- **paragraph role:** the single job performed by each paragraph, such as defining an estimand, explaining identifying variation, motivating a state variable, reporting a result, or delimiting a claim;
- **sentence function:** the sequence within a paragraph, typically claim -> reason or comparison -> evidence -> interpretation or caveat;
- **claim discipline:** how the paper distinguishes estimates from model implications, local effects from broader relevance, and measured outcomes from welfare or policy conclusions.

Before using a benchmark, write a short role map for the target passage. Match functions and ordering, not sentence templates, signature phrases, paragraph counts, or the benchmark's substantive claims. A benchmark may guide only the portions for which the user has supplied the necessary evidence.

## Reduced-form benchmarks

### Duflo (2001), "Schooling and Labor Market Consequences of School Construction in Indonesia"

**Architecture:** economic questions and endogeneity problem -> large policy intervention -> two-dimensional exposure by cohort and region -> linked survey and program data -> schooling effect -> wage effect -> instrumental-variables return to schooling -> tentative cost-benefit analysis.

**Transferable moves:**

- open with the substantive questions and immediately identify why existing correlations are insufficient;
- explain treatment exposure in plain language before formal specification;
- preview the first stage, reduced form, IV estimate, and cost-benefit calculation as separate objects;
- explain the identifying comparison with simple cohort-by-exposure means before introducing the regression;
- place the identifying assumption next to the first estimate and say plainly when it cannot be taken for granted;
- describe placebo cohorts or alternative comparisons as control experiments tied to a named threat;
- report ranges when results vary across justified specifications;
- acknowledge imprecision at the point where the affected estimate is interpreted;
- keep the introduction compact when one policy experiment carries the paper.

Use for classic policy-exposure designs, concise introductions, IV chains, and education-policy papers.

### Goodman-Bacon (2021), "The Long-Run Effects of Childhood Insurance Coverage"

**Architecture:** long-run policy question -> institutional introduction of Medicaid -> expected life-course mechanisms -> data organized by race, state of birth, and cohort -> cohort-by-state difference-in-differences -> event-study validation -> health, labor-market, education, and transfer outcomes -> fiscal externalities, costs, and QALYs -> discussion and conclusion.

**Transferable moves:**

- explain predicted long-run channels before presenting estimates;
- map each cohort's age at implementation into expected exposure;
- state the event-study shape predicted for ineligible, partially exposed, and fully exposed cohorts, then assess the design against that shape rather than offering a generic pretrend statement;
- distinguish what event-time patterns reveal about amount of exposure from what they cannot separately reveal about age at exposure;
- report heterogeneous outcomes before aggregating fiscal consequences;
- distinguish individual income effects from government savings and social benefits;
- define each fiscal component before aggregation, including transfer savings, tax revenue, and longevity-related costs;
- compare discounted fiscal savings with historical program costs using a common benchmark year and keep direct costs, fiscal externalities, and health benefits separate.

Use for health-policy exposure, long-run outcomes, event studies, life-course mechanisms, and fiscal accounting.

### Bleemer (2022), "Affirmative Action, Mismatch, and Economic Mobility after California's Proposition 209"

**Architecture:** contested policy debate -> three explicit questions -> novel linked administrative data -> difference-in-differences backbone -> enrollment cascade -> education and wage outcomes -> sample-selection threat -> complementary regression discontinuity evidence -> mechanism tests using transcript data -> distributional and allocative-efficiency discussion -> three contributions.

**Transferable moves:**

- turn a polarized debate into answerable empirical questions;
- state the main design and data linkage before previewing the result sequence;
- organize the introduction, result preview, and empirical sections in the same order as the opening questions;
- confront the strongest selection threat immediately after the main estimates;
- assign distinct inferential roles to the main design, complementary design, and mechanism data instead of presenting them as generic robustness;
- separate intention-to-treat averages, effects on directly affected students when supported, and aggregate implications;
- explain which mechanism prediction the mechanism evidence tests and report a null mechanism result without treating it as a failed paper result;
- state limitations and local interpretation before broader policy implications.

Use for multi-design reduced-form papers, higher-education policy, mechanisms, and distributional comparisons.

### Kirkeboen, Leuven, and Mogstad (2016), "Field of Study, Earnings, and Self-Selection"

**Architecture:** economically important choice -> identification problem with multiple unordered alternatives -> need for instruments plus next-best alternatives -> centralized admissions setting -> administrative rankings and cutoff instruments -> three broad findings -> local interpretation and limitations -> contributions to field-of-study, college-quality, and selection literatures.

**Transferable moves:**

- make the identification obstacle itself part of the motivation;
- define the causal comparison as one education type relative to a particular next-best alternative;
- explain why conventional binary-treatment language is inadequate;
- connect institutional assignment rules to both instruments and preference information;
- use a concrete preferred-versus-next-best example before presenting the general estimand;
- summarize results as a small number of broad conclusions;
- distinguish ex post payoffs from ex ante returns and state the local population clearly;
- place the main extrapolation limits immediately after the headline findings, including the complier margin and setting dependence.

Use for multidimensional education choices, admission cutoffs, comparative advantage, and identification-focused introductions.

## Structural and hybrid benchmarks

### Keane and Wolpin (1997), "The Career Decisions of Young Men"

**Architecture:** structural objective -> benefits of theory-consistent parameters and decision rules -> evolution of the human-capital and selection literature -> dynamic schooling, work, and occupational-choice model -> NLSY implementation -> basic-model fit and diagnosed failures -> extended model -> within- and out-of-sample fit -> heterogeneity decomposition -> tuition-subsidy experiment.

**Transferable moves:**

- explain what the structural approach recovers that descriptive relationships cannot;
- separate those gains into interpretable parameters, decision rules for policy changes, linked responses across choices, and welfare or distributional objects;
- motivate joint modelling through interdependence among schooling, experience, and occupation;
- connect each state variable to future rewards and choices;
- let model failure motivate a transparent extension rather than hiding it;
- introduce the decision problem in the order choices -> current rewards -> state transitions -> continuation values;
- distinguish targeted fit, broader data patterns, out-of-sample forecasts, behavioral implications, and welfare analysis.

Use for dynamic discrete choice, foundational structural exposition, model development, and fit diagnostics.

### Attanasio, Meghir, and Santiago (2012), "Education Choices in Mexico"

**Architecture:** randomized policy and data -> limits of the experimental treatment effect -> structural model estimated with experimental variation -> explicit comparison with an alternative ex ante model -> grant-income nonpooling and identification -> village-level general-equilibrium wage effects -> policy redesign simulations.

**Transferable moves:**

- state clearly what the randomized experiment answers and what it cannot extrapolate to;
- present experiment and model as complements rather than rivals;
- show which parameter or behavioral distinction the experimental variation identifies;
- compare modelling approaches through assumptions and identified objects, not labels;
- use a concrete economic contrast, such as whether two income sources enter behavior equivalently, to make an identifying restriction intelligible;
- state why each extra model margin is needed before describing its implementation;
- explain why the level of randomization permits equilibrium-effect estimation;
- define how equilibrium responses may attenuate or amplify the experimental effect;
- end with revenue-neutral policy redesigns that reveal the model's practical value without confusing extrapolation with experimental evidence.

Use for experiment-structural integration, conditional cash transfers, education choice, and program redesign.

### Blundell, Costa Dias, Meghir, and Shaw (2016), "Female Labor Supply, Human Capital, and Welfare Reform"

**Architecture:** incentives and insurance problem -> short-run quasi-experimental evidence -> dynamic life-cycle model of education, labor supply, wages, and savings -> policy reforms as identification and validation -> estimated elasticities and experience returns -> long-run tax-credit counterfactuals -> insurance, incentives, and welfare.

**Transferable moves:**

- explain why short-run labor-supply estimates do not answer long-run career and welfare questions;
- use reduced-form reform evidence before the model to establish credible responses;
- state how reforms interact with age and observed heterogeneity to identify the model;
- connect full-time, part-time, and nonwork choices to different human-capital paths;
- justify savings as the endogenous self-insurance margin required for welfare analysis;
- pair each model-fit comparison with the behavior or counterfactual for which that fit matters;
- replicate the short-run quasi-experimental response in simulated model data before relying on long-run exercises when the supplied analysis does so;
- report behavioral, human-capital, savings, fiscal, and welfare effects separately, and state when an effect ends with policy eligibility.

Use for reduced-form-to-structural bridges, policy reforms, labor supply, human capital, savings, and welfare.

### Abbott, Gallipoli, Meghir, and Violante (2019), "Education Policy and Intergenerational Transfers in Equilibrium"

**Architecture:** education-finance problem -> overlapping-generations model with skills, parental transfers, student work, grants, loans, risk, and general equilibrium -> staged estimation from multiple datasets -> untargeted fit and external validation -> removal of existing aid -> grant and loan expansions -> targeting comparisons -> equilibrium, crowd-out, intergenerational, productivity, and welfare decompositions.

**Transferable moves:**

- motivate model richness by naming the financing and equilibrium margins needed for the policy question;
- introduce private crowd-out before policy results because it governs interpretation;
- give a chronological life-cycle overview before formal notation so the reader can recover agents, transfers, education, work, saving, family formation, and equilibrium feedbacks;
- describe staged estimation by linking parameter blocks to datasets and moments;
- validate with untargeted life-cycle profiles, mobility statistics, borrowing, and simulated quasi-experimental responses;
- define immediate partial responses and long-run general-equilibrium responses before comparing them, including prices, distributions, private transfers, and the fiscal adjustment used to balance the budget;
- decompose welfare gains into productivity, initial inequality, and consumption uncertainty;
- compare universal, need-tested, and ability-tested policies on a common resource basis;
- return in the discussion to the market failures and crowd-out mechanisms that explain the welfare ranking, rather than merely restating the ranking.

Use for education finance, intergenerational models, equilibrium policy analysis, external validation, and welfare decomposition.

### Capatina (2015), "Life-Cycle Effects of Health Risk"

**Architecture:** health-risk question -> four channels -> unified life-cycle model -> data and calibration -> model performance -> experiments removing health effects and experiments removing risk around conditional means -> education heterogeneity and welfare.

**Transferable moves:**

- enumerate the mechanisms early and provide one concrete empirical fact for each when the supplied material supports it;
- motivate a unified model through interactions among channels, not through model breadth alone;
- connect the reported fit to the outcomes used in the quantitative exercises;
- define two counterfactual families separately: replacing bad-health states with good-health values changes both levels and risk, while replacing realizations with age-group conditional means isolates variation around those means;
- state whether channels are removed individually, jointly, or over selected life stages before reporting results;
- report education-group heterogeneity with comparable levels, percentages, and welfare units, and do not add channel effects mechanically when interactions matter.

Use for channel decomposition, health risk, calibrated life-cycle models, and controlled quantitative experiments.

### Capatina and Keane (2026), "Health Shocks, Health Insurance, Human Capital, and the Dynamics of Earnings and Health"

**Architecture:** linked dynamic questions -> model unifying treatment choice and health investment -> multiple insurance roles -> measurement correction and several datasets -> calibration and fit -> earnings-channel decomposition -> insurance counterfactual -> fiscal and welfare accounting -> racial and ethnic heterogeneity.

**Transferable moves:**

- open with a small set of linked questions and answer them through one explicit mechanism chain before technical detail;
- explain how the model unifies conceptual approaches by identifying the choice or constraint that connects them;
- distinguish insurance as price protection, consumption smoothing, access to treatment, and an influence on labor-supply incentives;
- introduce measurement error or underreporting beside the data contribution, then show why correcting it matters for calibration and policy incidence;
- evaluate untargeted fit on the selection and transition margins most relevant to the counterfactual;
- define mutually intelligible decomposition terms before reporting their magnitudes, such as contemporaneous labor supply, accumulated experience, health-related productivity, and behavioral responses to risk;
- present the insurance experiment as a ledger of utilization, labor supply, transfers, taxes, longevity-linked costs, net cost, and welfare, followed by transparent subgroup heterogeneity.

Use for health-human-capital dynamics, treatment and insurance, measurement problems, mechanism decomposition, and balanced-budget counterfactuals.

## Task-to-benchmark routing

| Writing task | Primary benchmarks |
|---|---|
| Concise reduced-form introduction | Duflo (2001) |
| Modern policy-exposure event study | Goodman-Bacon (2021) |
| Multiple empirical designs in one paper | Bleemer (2022) |
| Multiple unordered education choices | Kirkeboen, Leuven, and Mogstad (2016) |
| Foundational dynamic discrete-choice model | Keane and Wolpin (1997) |
| Randomized experiment plus structural model | Attanasio, Meghir, and Santiago (2012) |
| Quasi-experimental evidence plus life-cycle model | Blundell et al. (2016) |
| General-equilibrium education policy | Abbott et al. (2019) |
| Calibrated health-risk channel decomposition | Capatina (2015) |
| Health, insurance, human capital, and policy counterfactuals | Capatina and Keane (2026) |

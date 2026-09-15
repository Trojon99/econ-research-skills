# Curated causal-identification method literature

Snapshot verified: 2026-08-11.

Use this file as a high-priority reading map, not a frozen canon. Re-run the verification workflow in `literature-verification.md` whenever the user asks for the latest method, a paper's current publication status, or an edge case not covered here.

## How to use this library

For a user-facing diagnosis:

1. Identify the design and the exact complication first.
2. Read only the relevant section below.
3. Prefer published papers over working-paper versions.
4. Use a paper only if its result changes the identification, estimator, inference, or interpretation advice.
5. Do not infer that a newer paper dominates older work merely because it is newer.
6. Treat machine learning, regularization, and flexible nuisance estimation as estimation tools unless the paper explicitly changes identification assumptions.

Publication labels below reflect the status verified on the snapshot date.

## Difference-in-differences and event studies

High priority because modern DiD practice changes materially with staggered timing, heterogeneous effects, continuous doses, composition changes, interference, and sensitivity to parallel-trends violations.

### Core and synthesis

- Baker, Andrew, Brantly Callaway, Scott Cunningham, Andrew Goodman-Bacon, and Pedro H. C. Sant'Anna. 2026. "Difference-in-Differences Designs: A Practitioner's Guide." *Journal of Economic Literature* 64(2): 498-557. DOI: 10.1257/jel.20251650. **Published.** Use as the first synthesis for mapping estimands, 2x2 building blocks, covariates, weights, multiple periods, and staggered treatment.
- Callaway, Brantly, and Pedro H. C. Sant'Anna. 2021. "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics* 225(2). **Published.** Use for group-time ATT identification and aggregation with multiple periods/staggered adoption.
- Sun, Liyang, and Sarah Abraham. 2021. "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics* 225(2). **Published.** Use when conventional lead/lag TWFE event studies may mix cohort-specific effects.
- Goodman-Bacon, Andrew. 2021. "Difference-in-Differences with Variation in Treatment Timing." *Journal of Econometrics*. **Published.** Use to understand decomposition and weighting in staggered-adoption TWFE.
- Roth, Jonathan, Pedro H. C. Sant'Anna, Alyssa Bilinski, and John Poe. 2023. "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature." *Journal of Econometrics* 235(2). **Published.** Use as a compact map of the modern DiD literature.
- Borusyak, Kirill, Xavier Jaravel, and Jann Spiess. 2024. "Revisiting Event-Study Designs: Robust and Efficient Estimation." *Review of Economic Studies* 91(6): 3253-3285. DOI: 10.1093/restud/rdae007. **Published.** Use for imputation-based estimation under staggered adoption and heterogeneous effects; the framework also covers DDD and some nonbinary treatments.

### Parallel trends, pre-trends, and sensitivity

- Rambachan, Ashesh, and Jonathan Roth. 2023. "A More Credible Approach to Parallel Trends." *Review of Economic Studies* 90(5). DOI: 10.1093/restud/rdad018. **Published.** Use for sensitivity analysis when exact parallel trends is doubtful.
- Ghanem, Dalia, Pedro H. C. Sant'Anna, and Kaspar Wüthrich. 2026. "When Should Pre-trends Be Parallel?" *AEA Papers and Proceedings* 116: 64-69. DOI: 10.1257/pandp.20261109. **Published.** Use to avoid treating pre-trends mechanically as a direct test of the identifying parallel-trends restriction.

### Continuous, nonlinear, composition, and interference extensions

- Callaway, Brantly, Andrew Goodman-Bacon, and Pedro H. C. Sant'Anna. "Difference-in-Differences with a Continuous Treatment." **Conditionally accepted at the American Economic Review; Dec. 2025 version verified via author pages; NBER Working Paper 32117 (2024), DOI: 10.3386/w32117.** Re-check publication status before citing. Use when treatment intensity is continuous; ordinary binary-DiD intuition is insufficient for causal dose-response interpretation.
- Callaway, Brantly, Andrew Goodman-Bacon, and Pedro H. C. Sant'Anna. 2024. "Event Studies with a Continuous Treatment." *AEA Papers and Proceedings* 114: 601-605. **Published.** Use for event-time/dose aggregation issues under continuous treatment.
- Zhang, Lucas Zheng. 2026. "Continuous Difference-in-Differences with Double/Debiased Machine Learning." *The Econometrics Journal* 29(2): 256-276. DOI: 10.1093/ectj/utaf024. **Published.** Use for conditional parallel trends with continuous treatment and high-dimensional/flexible nuisance estimation.
- Xu, Ruonan. 2026. "Dynamic Difference-in-Differences with Interference." *AEA Papers and Proceedings* 116: 58-63. DOI: 10.1257/pandp.20261108. **Published.** Use when spillovers contaminate standard no-interference DiD comparisons.
- Botosaru, Irene, and Laura Liu. 2026. "Event Studies with Feedback." *AEA Papers and Proceedings* 116: 70-74. DOI: 10.1257/pandp.20261110. **Published.** Use when treatment affects time-varying covariates that feed back into later outcomes or treatment dynamics.
- Wooldridge, Jeffrey M. 2026. "Nonlinear Difference-in-Differences with Repeated Cross Sections." *AEA Papers and Proceedings* 116: 75-80. DOI: 10.1257/pandp.20261111. **Published.** Use for nonlinear outcome models/repeated cross-sections rather than imposing linear TWFE mechanically.

### Few treated clusters / inference

- Hagemann, Andreas. 2025. "Inference with a Single Treated Cluster." *Review of Economic Studies* 92(6): 3968-3994. DOI: 10.1093/restud/rdaf002. **Published.** Use when there is one treated cluster or very few treated clusters; conventional cluster asymptotics can be unreliable.

## Triple differences (DDD)

DDD is not merely "DID plus another interaction." Audit the precise higher-order counterfactual restriction and the comparisons carrying weight.

- Olden, Andreas, and Jarle Møen. 2022. "The Triple Difference Estimator." *The Econometrics Journal* 25(3): 531-553. DOI: 10.1093/ectj/utac010. **Published.** Core reference. Shows that DDD can have a causal interpretation when the bias in the two constituent DiDs is the same; it does not mechanically require two separate parallel-trends assumptions.
- Borusyak, Kirill, Xavier Jaravel, and Jann Spiess. 2024. "Revisiting Event-Study Designs: Robust and Efficient Estimation." *Review of Economic Studies* 91(6): 3253-3285. DOI: 10.1093/restud/rdae007. **Published.** Relevant because the imputation framework explicitly covers triple-difference designs.
- Ortiz-Villavicencio, Marcelo, and Pedro H. C. Sant'Anna. 2025. "Better Understanding Triple Differences Estimators." **Working paper, May 2025 version verified via Sant'Anna's author page.** Use as a frontier reference for covariate-adjusted and staggered DDD, including regression adjustment, IPW, and doubly robust approaches. Re-check publication status before citing.
- Strezhnev, Anton. 2023. "Decomposing Triple-Differences Regression under Staggered Adoption." **Working paper/preprint.** Use as a warning about forbidden/contaminated comparisons and homogeneity restrictions in conventional staggered triple-interaction regressions. Re-check current version/status before citing.

Do not treat very recent stacked/higher-order DDD preprints as default recommendations until their current version, assumptions, and publication status have been freshly verified.

## Regression discontinuity designs

### Canonical continuity-based RD

- Calonico, Sebastian, Matias D. Cattaneo, and Rocio Titiunik. 2014. "Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs." *Econometrica* 82(6): 2295-2326. DOI: 10.3982/ECTA11757. **Published.** Core robust bias-corrected inference reference.
- Calonico, Sebastian, Matias D. Cattaneo, Max H. Farrell, and Rocio Titiunik. 2017. "rdrobust: Software for Regression-Discontinuity Designs." *Stata Journal* 17(2). **Published.** Use for implementation lineage; verify current package documentation separately.
- Calonico, Sebastian, Matias D. Cattaneo, and Max H. Farrell. 2020. "Optimal Bandwidth Choice for Robust Bias-Corrected Inference in Regression Discontinuity Designs." *The Econometrics Journal* 23(2): 192-210. DOI: 10.1093/ectj/utz022. **Published.** Use for bandwidth selection tied to robust bias-corrected inference.
- Cattaneo, Matias D., Michael Jansson, and Xinwei Ma. 2020. "Simple Local Polynomial Density Estimators." *Journal of the American Statistical Association* 115(531): 1449-1455. DOI: 10.1080/01621459.2019.1635480. **Published.** Use for modern density/manipulation diagnostics; current `rddensity` documentation should be checked for implementation.
- Calonico, Sebastian, Matias D. Cattaneo, Max H. Farrell, and Rocio Titiunik. 2019. "Regression Discontinuity Designs Using Covariates." *Review of Economics and Statistics* 101(3): 442-451. DOI: 10.1162/rest_a_00760. **Published.** Use when covariates are included for precision; covariate adjustment does not repair invalid continuity/manipulation assumptions.

### High-dimensional, noise-based, and boundary/geographic RD

- Kreiss, Alexander, and Christoph Rothe. 2023. "Inference in Regression Discontinuity Designs with High-Dimensional Covariates." *The Econometrics Journal* 26(2): 105-123. DOI: 10.1093/ectj/utac029. **Published.** Use when many predetermined covariates are available and regularized/local selection is considered.
- Eckles, Dean, Nikolaos Ignatiadis, Stefan Wager, and Han Wu. 2025. "Noise-Induced Randomization in Regression Discontinuity Designs." *Biometrika* 112(2): asaf003. DOI: 10.1093/biomet/asaf003. **Published.** Use only when exogenous noise/measurement structure in the running variable is substantively defensible; it is a distinct identification strategy, not a generic RD replacement.
- Cattaneo, Matias D., Rocio Titiunik, and Ruiqi Rae Yu. 2026. "Estimation and Inference in Boundary Discontinuity Designs: Distance-Based Methods." *Journal of Econometrics* 256(A): 106266. DOI: 10.1016/j.jeconom.2026.106266. **Published.** Use for geographic/boundary assignment with multidimensional scores and distance-based local polynomial methods; do not collapse geography to distance without checking what effect is identified.

For local-randomization RD, discrete/mass-point running variables, multiple cutoffs, fuzzy RD, or power calculations, run a fresh search in the Cattaneo/Titiunik `rdpackages` ecosystem and primary papers before making a recommendation.

## Regression kink designs

- Card, David, David S. Lee, Zhuan Pei, and Andrea Weber. 2015. "Inference on Causal Effects in a Generalized Regression Kink Design." *Econometrica* 83(6): 2453-2483. **Published.** Use for identification/inference when the treatment rule changes slope rather than level. Verify DOI/current implementation if citing exact bibliographic details.

## Instrumental variables, weak identification, and judge/examiner designs

### Core IV / LATE and weak identification

- Angrist, Joshua D., and Guido W. Imbens. 1994. "Identification and Estimation of Local Average Treatment Effects." *Econometrica* 62(2): 467-475. **Published.** Core LATE interpretation under IV assumptions.
- Andrews, Isaiah, James H. Stock, and Liyang Sun. 2019. "Weak Instruments in Instrumental Variables Regression: Theory and Practice." *Annual Review of Economics* 11. **Published.** Use as a broad weak-IV practice review.
- Mikusheva, Anna, and Liyang Sun. 2024. "Weak Identification with Many Instruments." *The Econometrics Journal* 27(2): C1-C28. DOI: 10.1093/ectj/utae007. **Published.** Use when many instruments and weak identification interact; emphasizes weak-ID-robust testing rather than conventional many-IV 2SLS heuristics.
- Cao, Jianfei. 2026. "Robust IV Inference with Clustering Dependence." *The Econometrics Journal* 29(1): 125-142. DOI: 10.1093/ectj/utaf021. **Published.** Use when weak/robust IV inference must accommodate clustering; verify that the paper's dependence structure matches the application.

### Judge / examiner IV

- Chyn, Eric, Brigham Frandsen, and Emily Leslie. 2025. "Examiner and Judge Designs in Economics: A Practitioner's Guide." *Journal of Economic Literature* 63(2): 401-439. DOI: 10.1257/jel.20241719. **Published.** First-stop guide for examiner-leniency instruments, identifying assumptions, tests, leave-out construction, estimation choices, and interpretation.
- Frandsen, Brigham, Lars Lefgren, and Emily Leslie. 2023. "Judging Judge Fixed Effects." *American Economic Review* 113(1): 253-277. DOI: 10.1257/aer.20201860. **Published.** Use for diagnostics/tests of core judge-design assumptions rather than treating estimated judge leniency as automatically valid.
- Sigstad, Henrik. 2026. "Monotonicity among Judges: Evidence from Judicial Panels and Consequences for Judge IV Designs." *American Economic Review* 116(1): 189-208. DOI: 10.1257/aer.20231104. **Published.** Use when monotonicity is a substantive concern; conventional diagnostics can miss monotonicity violations.

## Shift-share, Bartik, formula instruments, and constructed exposure

- Goldsmith-Pinkham, Paul, Isaac Sorkin, and Henry Swift. 2020. "Bartik Instruments: What, When, Why, and How." *American Economic Review* 110(8): 2586-2624. DOI: 10.1257/aer.20181047. **Published.** Use when identification is argued through exposure shares and Rotemberg-weight logic.
- Borusyak, Kirill, Peter Hull, and Xavier Jaravel. 2022. "Quasi-Experimental Shift-Share Research Designs." *Review of Economic Studies* 89(1): 181-213. DOI: 10.1093/restud/rdab030. **Published.** Use when identification is argued through quasi-random shocks and shock-level orthogonality.
- Borusyak, Kirill, and Peter Hull. 2023. "Nonrandom Exposure to Exogenous Shocks." *Econometrica* 91(6): 2155-2185. DOI: 10.3982/ECTA19367. **Published.** Use for formula treatments/instruments and recentering when exposure to otherwise exogenous shocks is nonrandom.
- Borusyak, Kirill, Peter Hull, and Xavier Jaravel. 2025. "Design-Based Identification with Formula Instruments: A Review." *The Econometrics Journal* 28(1): 83-108. DOI: 10.1093/ectj/utae003. **Published.** Use as a synthesis of design-based identification for shift-share, simulated, network/spatial, and other formula instruments.

Always state whether the exogeneity claim is about shocks, shares/exposures, or a recentered formula. Do not mix these identification stories.

## Synthetic control, synthetic DiD, and causal panel counterfactuals

### Core families

- Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2010. "Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program." *Journal of the American Statistical Association* 105(490): 493-505. **Published.** Core SCM reference.
- Abadie, Alberto. 2021. "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." *Journal of Economic Literature* 59(2): 391-425. DOI: 10.1257/jel.20191450. **Published.** Use as the main design/practice synthesis.
- Arkhangelsky, Dmitry, Susan Athey, David A. Hirshberg, Guido W. Imbens, and Stefan Wager. 2021. "Synthetic Difference-in-Differences." *American Economic Review* 111(12): 4088-4118. DOI: 10.1257/aer.20190159. **Published.** Use for the hybrid unit/time weighting approach that links SCM and DiD.
- Ben-Michael, Eli, Avi Feller, and Jesse Rothstein. 2021. "The Augmented Synthetic Control Method." *Journal of the American Statistical Association* 116(536): 1789-1803. DOI: 10.1080/01621459.2021.1929245. **Published.** Use when imperfect pre-treatment fit motivates outcome-model augmentation.
- Athey, Susan, Mohsen Bayati, Nikolay Doudchenko, Guido Imbens, and Khashayar Khosravi. 2021. "Matrix Completion Methods for Causal Panel Data Models." *Journal of the American Statistical Association* 116(536): 1716-1730. DOI: 10.1080/01621459.2021.1891924. **Published.** Use for low-rank panel counterfactual models rather than literal synthetic-unit weighting.
- Ben-Michael, Eli, Avi Feller, and Jesse Rothstein. 2022. "Synthetic Controls with Staggered Adoption." *Journal of the Royal Statistical Society: Series B* 84(2): 351-381. DOI: 10.1111/rssb.12448. **Published.** Use for staggered adoption with synthetic-control-style balancing.

### 2026 frontier extensions

- Cao, Jianfei, Shirley Lu, and Hang Wu. 2026. "Synthetic Control Inference for Staggered Adoption." *The Econometrics Journal*, corrected proof, utag015. DOI: 10.1093/ectj/utag015. **Published online 29 May 2026.** Use when staggered-adoption SCM inference is central; compare assumptions with Ben-Michael, Feller, and Rothstein (2022) and DiD alternatives.
- Tian, Wei, Seojeong Lee, and Valentyn Panchenko. 2026. "Synthetic Controls with Multiple Outcomes." *The Econometrics Journal*, corrected proof, utag005. DOI: 10.1093/ectj/utag005. **Published online 20 March 2026.** Use when related pre-treatment outcomes add an extra dimension for constructing synthetic weights, especially with short pre-periods.
- Sakaguchi, Shosei, and Hayato Tagawa. 2026. "Identification and Bayesian Inference for Synthetic Control Methods with Spillover Effects." *The Econometrics Journal*, corrected proof, utag006. DOI: 10.1093/ectj/utag006. **Published online 4 May 2026.** Use when donor contamination/spillovers violate standard SCM no-interference assumptions.

Do not select SCM merely because there is one treated unit. Pre-treatment fit, donor support, interpolation, treatment timing, and contamination remain design requirements.

## Unconfoundedness, doubly robust estimation, and double machine learning

### Identification versus nuisance estimation

These methods do not create quasi-experimental identification. Unless the design supplies another source of identification, causal interpretation still requires unconfoundedness/conditional exchangeability plus overlap for the target estimand.

- Rosenbaum, Paul R., and Donald B. Rubin. 1983. "The Central Role of the Propensity Score in Observational Studies for Causal Effects." *Biometrika* 70(1): 41-55. DOI: 10.1093/biomet/70.1.41. **Published.** Foundational propensity-score reference.
- Chernozhukov, Victor, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, and James Robins. 2018. "Double/Debiased Machine Learning for Treatment and Structural Parameters." *The Econometrics Journal* 21(1): C1-C68. DOI: 10.1111/ectj.12097. **Published.** Core DML reference: orthogonal scores plus cross-fitting for high-dimensional/flexible nuisance functions.
- Chang, Neng-Chieh. 2020. "Double/Debiased Machine Learning for Difference-in-Differences Models." *The Econometrics Journal* 23(2): 177-191. DOI: 10.1093/ectj/utaa001. **Published.** Use when DiD identification is conditional on high-dimensional covariates; DML handles nuisance estimation, not the parallel-trends assumption itself.
- Knaus, Michael C. 2022. "Double Machine Learning-Based Programme Evaluation under Unconfoundedness." *The Econometrics Journal* 25(3): 602-627. DOI: 10.1093/ectj/utac015. **Published.** Use for practical DML-based ATE/heterogeneity/policy evaluation under selection on observables.
- Clarke, Paul S., and Annalivia Polselli. 2026. "Double Machine Learning for Static Panel Models with Fixed Effects." *The Econometrics Journal* 29(1): 69-86. DOI: 10.1093/ectj/utaf011. **Published.** Use when high-dimensional nonlinear confounding is combined with static panel fixed-effects structure.
- Zhang, Lucas Zheng. 2026. "Continuous Difference-in-Differences with Double/Debiased Machine Learning." *The Econometrics Journal* 29(2): 256-276. DOI: 10.1093/ectj/utaf024. **Published.** Use for continuous-treatment DiD with flexible nuisance functions and conditional parallel trends.

Never recommend DML as a generic cure for omitted variables, endogenous treatment, invalid instruments, failed parallel trends, manipulation in RD, or spillovers.

## Local projections and dynamic causal responses

Local projections are primarily an impulse-response estimation device; the causal content comes from the shock/instrument/design, not from the LP regression itself.

- Jordà, Òscar. 2005. "Estimation and Inference of Impulse Responses by Local Projections." *American Economic Review* 95(1): 161-182. **Published.** Foundational LP reference.
- Jordà, Òscar, and Alan M. Taylor. 2025. "Local Projections." *Journal of Economic Literature* 63(1): 59-110. DOI: 10.1257/jel.20241521. **Published.** Use as a current synthesis for LP specification and inference.
- Dube, Arindrajit, Davide Girardi, Òscar Jordà, and Alan M. Taylor. 2023. "A Local Projections Approach to Difference-in-Differences Event Studies." Federal Reserve Bank of San Francisco Working Paper 2023-12. DOI: 10.24148/wp2023-12. **Working paper.** Use when combining clean-control DiD logic with horizon-specific local projections; re-check publication status before citing.

## What to search freshly instead of relying on this snapshot

Always refresh the literature for:

- treatment reversals/switching and nonabsorbing DiD;
- continuous or multivalued treatment with staggered adoption;
- DDD with staggered adoption, covariates, or stacked estimators;
- interference/network spillovers in DiD or SCM;
- few treated clusters and randomization/design-based inference;
- weak IV with many instruments, clustering, or judge/examiner instruments;
- geographic/boundary RD, multiple scores/cutoffs, discrete running variables, or fuzzy RD edge cases;
- high-dimensional covariates or machine learning layered onto a causal design;
- formula instruments, simulated instruments, market access, or network exposure;
- any paper published/updated after the snapshot date.

# Literature verification and current-method refresh

Use this protocol to keep causal-method advice current and bibliographically reliable.

## Source hierarchy

Prefer, in order:

1. official journal/publisher article pages and DOI records;
2. NBER working-paper pages for NBER papers and revision information;
3. official working-paper repositories of recognized institutions;
4. authors' university pages for current drafts and replication materials;
5. package authors' official repositories/documentation for software behavior;
6. RePEc/IDEAS or similar indexes only as cross-checks when primary pages are unavailable;
7. arXiv/SSRN only when the work is genuinely still a preprint/working paper, and label it accordingly.

Do not use blogs, forum posts, AI-generated bibliographies, or secondary summaries as evidence that a method paper exists.

## Verification checklist for every cited method paper

Confirm at least:

- exact title;
- authors;
- publication year or working-paper date;
- journal/outlet or working-paper series;
- DOI or official source page when available;
- publication status: published, forthcoming/advance article, working paper, or preprint;
- whether a newer published version supersedes the working paper.

If any detail remains uncertain, omit the uncertain detail or mark it as needing verification. Never fabricate bibliographic metadata.

## Current-method search workflow

When a design raises a modern complication, search the most recent relevant literature before giving a strong recommendation.

1. Search by design + complication, not only by command name.
   - examples: `staggered difference in differences heterogeneous treatment effects`
   - `continuous treatment difference in differences`
   - `regression discontinuity discrete running variable inference`
   - `weak instruments clustered inference`
   - `synthetic control staggered adoption`
2. Search official journal domains and NBER first.
3. Identify survey/synthesis papers to map the literature, then verify the primary papers behind the recommendation.
4. Check publication date and revision date. A working paper may have changed materially.
5. Search for the estimator's current implementation and documentation separately from the theory paper.
6. Explain why the paper is relevant to the user's exact design. Do not dump an unfiltered bibliography.

## Recency rule

For canonical identification facts, use established references.

For estimator choice, finite-sample inference, continuous treatments, staggered adoption, few clusters, weak instruments, high-dimensional adjustments, synthetic-control extensions, or software syntax, actively look for work from roughly the last five years and especially the last two years.

Treat "latest" as a search problem, not a memory question.

## Verified baseline references and current seeds

The following were verified against authoritative sources when this skill was created. Re-check status when recency matters.

### DID / event studies

- Callaway, Brantly, and Pedro H. C. Sant'Anna. 2021. "Difference-in-Differences with Multiple Time Periods." Journal of Econometrics 225(2).
- Sun, Liyang, and Sarah Abraham. 2021. "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." Journal of Econometrics 225(2).
- Goodman-Bacon, Andrew. 2021. "Difference-in-Differences with Variation in Treatment Timing." Journal of Econometrics.
- Roth, Jonathan, Pedro H. C. Sant'Anna, Alyssa Bilinski, and John Poe. 2023. "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature." Journal of Econometrics 235(2).
- Rambachan, Ashesh, and Jonathan Roth. 2023. "A More Credible Approach to Parallel Trends." Review of Economic Studies 90(5). DOI: 10.1093/restud/rdad018.
- Borusyak, Kirill, Xavier Jaravel, and Jann Spiess. 2024. "Revisiting Event-Study Designs: Robust and Efficient Estimation." Review of Economic Studies 91(6). DOI: 10.1093/restud/rdae007.
- de Chaisemartin, Clement, and Xavier D'Haultfoeuille. 2024. "Difference-in-Differences Estimators of Intertemporal Treatment Effects." Review of Economics and Statistics.
- Abadie, Alberto, Joshua Angrist, Brigham Frandsen, and Jorn-Steffen Pischke. 2025. "Harvesting Differences-in-Differences and Event-Study Evidence." NBER Working Paper 34550. Treat as a working paper unless a published version is found.

### RDD

- Calonico, Sebastian, Matias D. Cattaneo, and Rocio Titiunik. 2014. "Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs." Econometrica 82(6).
- Calonico, Sebastian, Matias D. Cattaneo, Max H. Farrell, and Rocio Titiunik. 2017. "rdrobust: Software for Regression-Discontinuity Designs." Stata Journal 17(2).
- Calonico, Sebastian, Matias D. Cattaneo, and Max H. Farrell. 2020. "Optimal Bandwidth Choice for Robust Bias-Corrected Inference in Regression Discontinuity Designs." The Econometrics Journal 23(2). DOI: 10.1093/ectj/utz022.
- Cattaneo, Matias D., Michael Jansson, and Xinwei Ma. 2018. Work underlying `rddensity` manipulation testing; verify the exact journal/software citation needed for the user's application.
- For new questions about fuzzy RD, discrete running variables, noise-induced randomization, local randomization, or power, perform a fresh search rather than relying only on this baseline.

### IV and weak identification

- Angrist, Joshua D., and Guido W. Imbens. 1994. Foundational LATE framework.
- Andrews, Isaiah, James H. Stock, and Liyang Sun. 2019. "Weak Instruments in Instrumental Variables Regression: Theory and Practice." Annual Review of Economics 11.
- "Weak Identification with Many Instruments," The Econometrics Journal 27(2), 2024. Verify authors and exact recommendations from the official article before citing in user-facing output.
- "Robust IV Inference with Clustering Dependence," The Econometrics Journal 29(1), 2026, DOI 10.1093/ectj/utaf021. Verify applicability before recommending it; do not treat one recent paper as universal best practice.

### Shift-share / Bartik

- Goldsmith-Pinkham, Paul, Isaac Sorkin, and Henry Swift. 2020. "Bartik Instruments: What, When, Why, and How." American Economic Review.
- Borusyak, Kirill, Peter Hull, and Xavier Jaravel. 2022. "Quasi-Experimental Shift-Share Research Designs." Review of Economic Studies 89(1). DOI: 10.1093/restud/rdab030.

### Synthetic control / panel counterfactuals

- Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2010. Classical synthetic-control paper.
- Abadie, Alberto. 2021. "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." Journal of Economic Literature.
- Arkhangelsky, Dmitry, Susan Athey, David A. Hirshberg, Guido W. Imbens, and Stefan Wager. 2021. "Synthetic Difference-in-Differences." American Economic Review.
- Ben-Michael, Eli, Avi Feller, and Jesse Rothstein. 2021. Augmented synthetic-control method. Verify exact publication details before user-facing citation if needed.
- Athey, Susan, Mohsen Bayati, Nikolay Doudchenko, Guido Imbens, and Khashayar Khosravi. 2021. Matrix completion methods for causal panel data. Verify exact outlet details before user-facing citation if needed.
- "Synthetic Control Inference for Staggered Adoption," The Econometrics Journal, advance/publication record available in 2025-2026. Verify exact bibliographic status before citing.
- "Synthetic Controls with Multiple Outcomes," The Econometrics Journal, advance/publication record available in 2025-2026. Verify exact bibliographic status before citing.

## Software verification

For exact Stata syntax, search current documentation at the time of use.

Examples of authoritative implementation sources:

- official Stata documentation/pages for built-in DID/IV/panel commands;
- `rdpackages` documentation for `rdrobust`/`rddensity` family;
- authors' repositories for `did_imputation` and similar research packages;
- package help files distributed with the command;
- peer-reviewed Stata Journal software articles when available.

Do not assume a package's defaults, variable coding, or option names from memory.

## Citation behavior in the diagnosis

Only cite papers that actually affect the diagnosis or estimator recommendation. For each, state the relevant methodological point in one sentence.

If the user asks for a comprehensive literature review, expand the search. Otherwise, prefer a small verified set over a long unverified bibliography.

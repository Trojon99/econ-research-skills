# Frontier evidence: approximate estimation and policy closure

These are bounded lessons from verified working-paper text, not new defaults, validated software, or settled findings. Physical PDF page numbers are used throughout. Preserve local project overlays and require actual replication before calling an estimator numerically validated.

## Variational approximations as auxiliary estimators

**Practice:** In latent dynamic models, distinguish likelihood identification, information retained by an approximate auxiliary estimator, and numerical convergence. Do not equate a larger ELBO with recovery of the data-generating parameter.

**Source and version:** Balke, Bonhomme and Lamadon, NBER **w35877**, *Indirect Variational Inference: Applications to Earnings Dynamics*, official citation-publication metadata **2026-10-12**, October 2026 PDF. [Paper](https://www.nber.org/papers/w35877); [PDF](https://www.nber.org/system/files/working_papers/w35877/w35877.pdf). Reading: complete 62-page PDF text, including §§1–9 and appendices; no replication, line-by-line proof audit, or full visual figure audit. HTML dcterms.date/citation_publication_date, not a web extractor's creation date, defines the release field.

**Paper's claim:** VI may converge to a pseudo-true parameter when the posterior family is restrictive. IVI uses VI as an auxiliary estimator and matches its observed-data target to its target on simulated data. A one-to-one binding function is the key identification assumption (§4, PDF pp.14–19, especially p.17). Fixed-point convergence requires a separate contraction condition (p.18). The asymptotic variance incorporates simulation and the inverse binding-function Jacobian; Appendix A explicitly omits ELBO noise (pp.49–51).

**Assistant's bounded inference:** Audit three distinct failures: model observational equivalence; a weak/non-injective binding map; and incomplete inner/outer optimization. Simulation bias correction does not repair model misspecification. A successful optimizer or a fixed iteration count does not establish any of these identification conditions.

**Threat → diagnostic → remaining limitation:**
- Posterior-family distortion → benchmark against a linear Gaussian model with exact likelihood/posterior and compare correlated versus mean-field families (§5, pp.23–27) → success in a simple benchmark does not establish correctness in a nonlinear model.
- Weak binding information → inspect parameter slices, local Jacobian conditioning, alternative roots and starting values → local rank cannot establish global injectivity.
- Stochastic outer objective → use common simulator draws, ELBO draws and initialization within a run; check independent seeds across runs → fixing draws smooths the objective but does not eliminate simulation error (Appendix F, p.58).
- Truncated computation → report matching residuals, inner-fit diagnostics, damping and tolerance sensitivity → the paper's fixed outer-loop counts are implementation choices, not a general stopping rule. Its PSID point estimate uses 50 outer iterations while bootstrap fits use 20; validate that difference before copying the inference procedure (pp.58–59).

**Applicability assumptions:** A credible generative model and simulator; an informative auxiliary estimator; the required uniqueness, smoothness and rank conditions; controlled optimization/ELBO errors; resampling at the relevant dependence unit. Paper evidence concerns earnings-process modules, not a full estimated consumption/labor-supply model.

**Remaining limitations:** No general proof of global identification for every extended earnings model or systematic coverage validation for large neural posterior families. Speed comparisons do not establish equal statistical accuracy or include all IVI outer-loop costs. Risk-premium exercises use maintained preferences and income-as-consumption proxies, not policy welfare with insurance, financing and equilibrium responses.

## Local allocation returns versus full capacity-policy effects

**Practice:** For capacity-constrained allocation policies, distinguish cutoff compliers, all reassigned agents, and aggregate policy effects. Track outside options, declined offers and knock-on reallocations; fixed total seats do not imply equal counts of benefiting and losing agents.

**Source and version:** Barahona, Dobbin and Otero, NBER **w35893**, *Affirmative Action in Centralized College Admissions Systems*, official release **2026-10-12**, October 2026 PDF. [Paper](https://www.nber.org/papers/w35893); [PDF](https://www.nber.org/system/files/working_papers/w35893/w35893.pdf). Reading: all 80 PDF pages, including complete main text and appendices A–K; no replication or full visual figure audit.

**Paper's claim:** The framework separates marginal returns from average switcher effects and group-specific switcher counts (§4.2, pp.17–19). Admissions cutoffs provide local comparisons; structural potential outcomes also rely on distance as an excluded choice shifter and specified control functions (§6.3, pp.30–32). Counterfactuals re-solve offers, take-up and waitlists while holding capacity and the applicant pool fixed (§7.1, pp.35–36). Knock-on changes mean a one-for-one extrapolation of marginal returns misses some losses (§7.4, pp.38–39).

**Assistant's bounded inference:** Use reduced-form evidence to anchor local returns, not as independent validation if already used to identify model objects. Report both per-switcher changes and switcher counts. Separate allocation-rank changes from skills, wages, resource costs, distributional values and welfare.

**Threat → diagnostic → remaining limitation:**
- Ignored fallback/take-up → link application, offers, acceptance, waitlist and outside-platform outcomes → unobserved outside options may still require model restrictions.
- Distance exclusion → map direct commuting, relocation and family-support channels and test supported implications → observed controls cannot prove distance has no direct effect on completion.
- Counterfactual non-invariance → state fixed preferences, scores, eligibility, capacity and applicant pool; consider alternative peer/behavior/outside-market responses → modeled reallocation is not a full long-run general equilibrium.
- Misinterpreted quality proxy → report the program ranking definition and completion separately → admissions-score rank is not teaching value added or monetary welfare.

**Applicability assumptions:** Credible local cutoff design and compliance interpretation; stable matching/preference and take-up restrictions; valid excluded shifters and outcome functions; explicit mechanism mapping. The paper's simulation uses an unrestricted-report DA counterfactual, whereas observed initial applications are limited to two options (p.35 footnote 35); equivalence is a maintained modeling bridge, not automatic.

**Remaining limitations:** Functional-form and selection-correction assumptions extend beyond the RD support. Peer effects, altered preparation/application behavior and the outside higher-education market are not fully re-equilibrated. Simulation replications are not parameter-uncertainty draws. Graduation rank alone cannot establish net welfare.

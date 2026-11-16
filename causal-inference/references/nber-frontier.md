# Frontier evidence: measurement and the causal outcome

This is a bounded research-design reference, not a replacement for the core identification workflow. Working-paper evidence is provisional; preserve disagreements and do not promote an individual result to consensus.

## Randomize reporting protocols when the policy may change disclosure

**Practice:** Separate the effect on reported outcomes from the effect on the latent behavior. Where feasible, randomize measurement protocols within the policy-evaluation sample and test treatment-by-protocol interactions using common support and a direct difference test; do not compare two significance labels.

**Source and version:** Agüero, Aldana, Field, Frisancho, Rodriguez Hurtado and Romero, NBER **w35891**, *Measurement Error in Self-Reported Data on Stigmatized Behavior: Experimental Evidence on Intimate Partner Violence*, official release **2026-10-12**, October 2026 PDF. [Official paper](https://www.nber.org/papers/w35891); [PDF](https://www.nber.org/system/files/working_papers/w35891/w35891.pdf). Actual reading: all 22 PDF pages, including complete main text and tables; independent online appendix also read by delegated reviewer; no replication or full visual figure audit. Support below uses the main PDF's physical page numbers, verified in the extracted text.

**Paper's claim:** In a within-village randomized survey experiment in Peru, the private ballot protocol increases reported IPV relative to audible questions. Table 1 (PDF p.11) reports any-IPV rates of 0.393 and 0.459. The authors interpret higher reporting as reduced underreporting, and use natural experiments to show that the survey protocol can change estimates of IPV determinants (§§3–4, PDF pp.10–17).

**Assistant's bounded inference:** Randomization identifies a protocol effect on reports; absent a truth benchmark it does not establish that every added report is true, that residual underreporting disappears, or that privacy alone caused the difference. The ballot also changes response format and comprehension assistance. Distinguish protocol randomization from the identification of the policy exposure itself. The education estimates in Table 2 (PDF p.17) use different bandwidths across protocols; a common-bandwidth interaction analysis is an additional diagnostic proposed by the assistant, not an already verified author result.

**Threat → diagnostic → remaining limitation:**
- Differential disclosure → randomized protocol arms plus direct policy-by-protocol comparisons → the true outcome remains latent without validation data or additional restrictions.
- Miscomprehension → contemporaneous non-sensitive validation items and independently varied visual/reading assistance → later validation among selected recontacted respondents cannot prove comprehension in the original sample.
- Short-run dynamics measured by an ever/lifetime question → collect dated events or explicitly short reference periods → a cyclical lifetime report can reflect recency or disclosure, not only a changing event hazard (§4, PDF p.14).

**Applicability assumptions:** Protocol assignment is implemented as randomized, attrition and interference are audited, outcome definitions and reference periods are identical, and changing privacy does not expose respondents to harm. Complier-characteristic interpretations additionally require the stated reporting monotonicity and false-report restrictions; randomization alone does not provide them (§3.2, PDF p.12).

**Remaining limitations:** Rural/peri-urban cohabiting mothers are not all women; list-experiment estimates are noisier and do not identify individual joint histories. The policy natural experiments require their own exclusion/continuity or timing assumptions. This reference is not a blanket recommendation to replace existing instruments, and does not establish a universal ranking of survey methods.

## Keep auxiliary coverage and utilization samples distinct

**Practice:** When the outcome linkage observes one insurance program but not all coverage or service use, construct a sample-and-clock crosswalk before using auxiliary datasets to interpret the first stage or mechanism. Separate the policy-induced change in the outcome population from a coverage contrast in a proxy population and a utilization level among selected covered people.

**Source and scope:** Campain, Miller, Persson, Rossin-Slater, Wherry and King, [NBER w36033](https://www.nber.org/papers/w36033), *Preconception Medicaid and Maternal and Infant Health: Evidence from Linked Administrative Data*, released 2026-11-16, November 2026 PDF. Main narrative read at physical PDF pp.4–25; Tables 1–2 at pp.44–45 and Appendix A plus selected claims-construction material at pp.46–48 checked. Remaining appendix tables/figures and full visual audit not completed; no replication. Working-paper evidence, not consensus.

**Author evidence:** The linked birth/tax/enrollment sample measures preconception Medicaid enrollment, not all insurance or claims. A reweighted ACS sample assesses overall coverage; a separate post-expansion claims sample describes use among women continuously enrolled before a first-pregnancy claim. The authors acknowledge that this last analysis does not observe counterfactual utilization (PDF pp.11–16, 21, 25, 47). Their actual DID compares income below 150% FPL with 200–300% FPL, excluding the intermediate band; it is not a local RD at the statutory 138% threshold (pp.14, 17–18).

**Assistant inference and diagnostics:**
- Program take-up versus net coverage → tabulate all-source coverage in an appropriately matched auxiliary population → transportability remains an assumption when future pregnancy and the same preconception window are unobserved. Demographic reweighting does not establish it.
- High utilization among covered people versus induced utilization → state enrollment, pregnancy-claim and observation requirements and seek a policy counterfactual → a high post-treatment use level alone cannot identify a utilization response or mediation effect.
- Annual tax income versus monthly eligibility → document tax-unit construction, non-filers, the missing-income rule and calendar weights; compare source-specific enrollment and restricted-source estimates → these diagnostics do not certify monthly eligibility or remove policy-induced income selection. Appendix A explicitly notes the annual/monthly mismatch.
- A strong program-enrollment first stage with null health effects → report outcome-specific uncertainty and the exact policy contrast → do not divide an outcome effect by a first stage from a different population or clock to manufacture a per-year insurance effect.

**Boundary:** Auxiliary data can make a mechanism more or less plausible without identifying it. Neither the selected-claims description nor the proxy-population coverage analysis repairs the main DID's parallel-trends, live-birth selection or concurrent-policy assumptions.

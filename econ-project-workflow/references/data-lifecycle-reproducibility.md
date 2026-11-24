# Data Lifecycle and Reproducibility

## Contents
1. Data classes
2. Safe reduction and caching
3. Validation
4. Reproducible execution
5. Cross-language handoffs

## 1. Data classes

### `data/original/`
Treat source data as immutable. Never clean in place or overwrite provider files.

### `data/work/`
Use for meaningful products expected to be reused: cleaned data, merged masters, analysis-ready datasets, model inputs, figure/table source data, and expensive stable caches.

### `data/temp/`
Use for disposable intermediates that are safe to delete and regenerate. Do not use it as a catch-all for important downstream inputs.

### `data/output/`
Use for final human-facing figures, tables, reports, and presentation-ready outputs. Machine-readable support files normally belong in `data/work/`.

## 2. Safe reduction and caching

Reduce data early when it is statistically and structurally safe:

- load only required columns/variables when practical;
- drop no-longer-needed variables after construction;
- restrict observations after confirming excluded records are not needed for lags, leads, baselines, transitions, future outcomes, joins, risk sets, or model state construction;
- reuse cached stable products when upstream inputs/code have not changed.

Do not optimize by silently changing samples, denominators, weighting, missing-value rules, treatment timing, or model definitions.

## 3. Validation

Validate structural assumptions close to the transformation that depends on them:

- file/object existence;
- variable/column existence;
- key uniqueness;
- allowed category/range values;
- date/index ordering;
- expected join states;
- observation/entity counts;
- transition/risk-set logic;
- valid dimensions/support for model inputs.

Unexpected duplicates, unmatched records, failed assertions, or malformed objects should be treated as errors unless the research design explicitly permits them.

## 4. Reproducible execution

Prefer deterministic outputs given the same intended inputs and code.

- Set fixed seeds for random sampling, simulation, bootstrap setup, randomized tie-breaking, or other stochastic operations.
- Put machine-specific absolute paths in configuration/entrypoint code, not throughout substantive modules.
- Log major stages and failures.
- Do not rely on undocumented working-directory state, object state from a previous interactive session, or implicit sort/index order.
- Make order-sensitive panel/sequence operations explicitly sort/index data before using lags/leads or analogous operations.
- Keep coarse progress messages for long jobs so failures can be localized.

## 5. Cross-language handoffs

For a file produced in one language and consumed in another, document:

- producer and consumer stage;
- file path and format;
- unit of observation/model object;
- key/index variables;
- missing-value conventions;
- date/time encoding;
- category/value-label semantics;
- weights and units when relevant.

Prefer portable formats only when they preserve the required semantics. Do not sacrifice labels, precision, or type information without documenting the conversion.

### Reconciling a panel estimate across programs

Before replacing a working implementation, retain one small reproducible specification from the original program. For each implementation export the sorted **keys of the rows actually estimated**, the outcome and treatment coding, weights and their meaning, fixed-effect dimensions, omitted levels, cluster IDs/counts, coefficient labels, estimates, SEs, and interval degrees of freedom. Matching row counts do not prove that the keys match. A panel index is not a uniqueness check; if two records share an entity and date, resolve their economic unit before fitting either model.

If estimates differ, reconcile the keys first (including missing controls, zero weights, and singleton removals), then compare the variation left in the treatment after the same controls and fixed effects. In a linear FE specification a regressor lying in the span of the absorbed indicators (for example, a state-year exposure with state-by-year fixed effects) cannot identify its coefficient. Do not retain it by quietly changing the fixed effects. If slopes match but intervals differ, compare covariance estimators, clusters, small-sample multipliers, treatment of absorbed parameters and reference distribution **before** changing the research specification. For example, `fixest` separates covariance choice from small-sample corrections. Record an intentional difference if the two procedures target different objects; agreement across programs is not evidence for parallel trends or instrument validity.

### Licensed financial panels: join as of the relevant date

A firm, security, trade, filing and fiscal report are different rows. Declare the intended unit and population before selecting vendor tables or copying a set of filters. Preserve release/schema and observation dates separately; when the analysis requires information available at a past decision date, fiscal period end is not proof a value was public then. Save the as-of cutoff and the release/amendment policy. On an identifier crosswalk with effective dates, count **zero, one and multiple active matches per source row** on the relevant date. Inspect overlapping links and share classes before aggregating: retaining the first match or averaging across securities silently creates a different portfolio. Tabulate excluded units and value totals where appropriate. Do not hardcode a current table name or treat a domestic-common-share or consolidated-industrial filter as universally required. Preserve the query and filter ledger separately from licensed data; never assume access or redistribution rights.

Reading entry points: [Barrios Skills, econometrics collection at reviewed revision](https://github.com/Barrios88/barrios-skills/tree/680c98370381593141bf1d39da4353354958e2f0/skills/econometrics), especially PyFixest’s checklist, Python panel indexing, and WRDS’s query filters and link dates. For estimator settings see the maintainers’ [fixest standard-errors vignette](https://lrberge.github.io/fixest/articles/standard_errors.html) and [reghdfe help](https://scorreia.com/help/reghdfe.html). These are reconciliation checks, not a benchmark of the packages or validation of a vendor-specific filter.

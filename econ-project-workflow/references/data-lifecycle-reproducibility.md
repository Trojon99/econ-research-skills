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

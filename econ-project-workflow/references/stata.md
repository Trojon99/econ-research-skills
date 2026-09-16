# Stata Backend Conventions

Apply these rules when the economics project uses Stata. They supplement the generic `econ-project-workflow` contract.

## Contents
1. Project entrypoint and modular do-files
2. Paths and file headers
3. Performance: bulk operations and loops
4. Safe data reduction and I/O
5. `preserve` / `restore` and temporary storage
6. Figures and tables
7. Fail-fast validation and merges
8. Weighted-statistics semantics
9. Reproducible execution
10. Regression code
11. Code-review checklist

## 1. Project entrypoint and modular do-files

Use `00_master.do` as the normal entrypoint for a Stata project unless the project has an established alternative.

A typical sequence is:

```text
code/
├── 00_master.do
├── 01_clean_core.do
├── 02_build_core_master.do
├── 03_merge_topical_modules.do
├── 04_construct_analysis_variables.do
├── 05_descriptives.do
├── 05_figures.do
├── 06_regression_analysis.do
├── 07_robustness.do
└── 08_mechanisms.do
```

Keep substantive stages separate when they have distinct responsibilities. `00_master.do` should set paths/globals, create required folders, define coarse rebuild/run switches, open the workflow/logging, and call stage files in order.

Subordinate do-files should use project globals established by the master. Avoid repeated `cd` calls and duplicated machine-specific path definitions.

## 2. Paths and file headers

Use the generic project folders:

```stata
global BaseFolder     "/path/to/project"
global CodeFolder     "${BaseFolder}/code"
global OriginalFolder "${BaseFolder}/data/original"
global WorkFolder     "${BaseFolder}/data/work"
global TempFolder     "${BaseFolder}/data/temp"
global OutputFolder   "${BaseFolder}/data/output"
global DocFolder      "${BaseFolder}/doc"
global LogFolder      "${BaseFolder}/log"
```

Start every substantive `.do` file with a concise header stating purpose, main inputs, main outputs, unit of observation, and key/panel order when relevant.

Example:

```stata
*===============================================================================
* File:    04_construct_analysis_variables.do
* Purpose: Construct the analysis sample and downstream variables.
*
* Inputs:
*   ${WorkFolder}/core_master.dta
*
* Outputs:
*   ${WorkFolder}/analysis_master.dta
*
* Unit of observation:
*   Person-month
*
* Key / panel order:
*   person_id ym
*===============================================================================
```

Add short comments before substantial blocks explaining statistical intent and data flow, not every trivial command.

## 3. Performance: bulk operations and loops

Prefer operations that process many observations/groups in one pass:

- `collapse`
- `contract`
- `egen`
- `bysort`
- `reshape`
- `merge`
- `append`
- direct `generate` / `replace`

For grouped descriptives, prefer one grouped operation to nested loops that repeatedly scan the full dataset.

Avoid using `foreach` or `forvalues` merely to make code shorter. Especially avoid nested loops whose bodies repeatedly call expensive commands such as `summarize`, `count`, `preserve`, `use`, `save`, `merge`, or `append` on a large master.

A repeated explicit block is acceptable when it is faster and easier to audit.

Retain a loop when it is technically necessary, materially safer for a systematic specification grid, or cheap enough that performance is irrelevant. Explain non-obvious retained loops briefly.

## 4. Safe data reduction and I/O

Load only needed variables from wide datasets when practical:

```stata
use person_id wave age_group outcome analysis_weight ///
    using "${WorkFolder}/analysis_master.dta", clear
```

Reduce observations early only after confirming the dropped records are not needed to construct lags, leads, baselines, transitions, future outcomes, or person-level variables.

Avoid repeatedly reading, saving, merging, or appending a large master. Prefer to prepare small extracts first, combine small files before a large merge when appropriate, and reuse stable work datasets when upstream construction has not changed.

## 5. `preserve` / `restore` and temporary storage

A small number of clear `preserve` / `restore` iblocks is fine. Do not place repeated large-data `preserve` / `restore` inside high-iteration loops.

Use storage according to lifetime:

- Stata `tempfile`: only within the current do-file/session;
- `data/temp/`: disposable intermediates that may need to survive across do-files or debugging;
- `data/work/`: stable cleaned/merged/analysis/supporting datasets used downstream;
- `data/output/`: final human-facing figures/tables only.

If a collapsed/intermediate dataset is reused later or underlies a final output, save it in `data/work/`, not `data/temp/`.

## 6. Figures and tables

Use `.png` by default for exploratory/review figures because they are easy to browse. Change format at publication stage only when required.

Use Word-readable tables by default, preferably `.docx` with `putdocx` when appropriate. Use legacy `.doc` only when specifically required.

Save final figures/tables under `data/output/`; save their machine-readable source datasets under `data/work/`.

For HTML figure-review reports, follow the generic `references/figure-review-html-benchmark.md` and `assets/figure-review-template.html` from `econ-project-workflow`.

## 7. Fail-fast validation and merges

Before important transformations, use checks such as:

```stata
confirm file "${OriginalFolder}/source.dta"
confirm variable person_id wave analysis_weight
isid person_id wave
assert inlist(binary_var, 0, 1, .)
```

For merges:

- verify intended keys with `isid` when appropriate;
- inspect `_merge` immediately;
- assert or explicitly check allowed merge states before dropping `_merge`;
- treat unexpected using-only rows, duplicate keys, or update conflicts as errors unless the design permits them.

Do not use:

```stata
merge ...
drop _merge
```

without validating the merge first.

Use `capture` only when an error is genuinely expected and handled. Do not blanket-wrap important construction in `capture` to keep the pipeline running.

## 8. Weighted-statistics semantics

Do not trade statistical correctness for speed.

If a table needs weighted means but unweighted nonmissing counts, construct explicit indicators and preserve the intended denominator, for example:

```stata
gen byte n_y = !missing(y)
collapse (mean) mean_y=y (rawsum) n_y [aw=analysis_weight], ///
    by(group1 group2)
```

Check that optimizations do not alter sample eligibility, treatment timing, health/education definitions, risk sets, missingness, weighting, denominators, transitions, or event timing.

## 9. Reproducible execution

Default practices:

- start substantive do-files with the intended Stata `version` and `set more off`;
- keep absolute machine paths in the master/configuration layer;
- set and document a fixed seed before stochastic operations;
- write logs to `log/` with stable names;
- explicitly sort on full key/order variables before order-sensitive panel operations;
- do not rely on state left by a previously run do-file;
- keep work datasets deterministic given the same inputs/code/settings/seeds.

## 10. Regression code

Do not replace substantively distinct regression specifications with `collapse` or other data-reduction shortcuts.

Keep regression-specific controls, fixed effects, clustering variables, and common samples inside the regression do-file rather than in `00_master.do`.

Example:

```stata
local controls_main   "female married parent_coreside"
local fixed_effects   "i.calendar_year i.calendar_month"
local cluster_var     "person_id"
```

Use locals only for genuinely shared ingredients. Keep substantively different robustness specifications explicit rather than hiding meaningful differences behind overly generic macros/programs.

For systematic repeated regressions, suppress unnecessary output rendering where appropriate and provide coarse progress messages. A loop is acceptable when it materially improves correctness or consistency of a specification grid.

## 11. Code-review checklist

Actively look for:

- nested loops containing expensive data operations;
- repeated scans of the same large panel;
- repeated large-master I/O;
- abstractions that cause many small passes over data;
- opportunities for grouped `collapse`/bulk operations;
- data products saved to `data/output/` that belong in `data/work/`;
- wide files loaded with many unused variables;
- restrictions applied too late when they could safely be earlier;
- `preserve`/`restore` inside expensive loops;
- merges whose `_merge` is not validated;
- `capture` hiding unexpected errors;
- panel code relying on implicit sort order.

Do not mechanically remove every loop or abstraction. Prioritize changes with a clear correctness, performance, reproducibility, or auditability benefit.

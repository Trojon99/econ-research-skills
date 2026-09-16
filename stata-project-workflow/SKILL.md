---
name: stata-project-workflow
description: Use when ChatGPT creates, edits, reviews, debugs, optimizes, refactors, or organizes Stata projects, including .do/.ado files, master pipelines, data folders, merges, validation, logs, intermediate datasets, tables, figures, regressions, reproducible research outputs, and HTML result-review reports. Apply the user's explicit, performance-oriented Stata workflow: modular numbered do-files run from one master file, minimal expensive loops, bulk operations, fail-fast validation, early data reduction, reproducible execution, and the standard project layout code, data/original, data/output, data/temp, data/work, doc, and log.
---

# Stata Project Workflow

Apply these conventions by default to all Stata code unless the user explicitly asks for a different style.

## Core priority

Use this priority order:

1. Preserve the correct statistical definition, sample, denominator, weighting, missing-value treatment, and research design.
2. Minimize runtime and repeated passes over large datasets.
3. Make the code explicit and easy to audit line by line.
4. Only then optimize for brevity or elegance.

Code repetition is acceptable. Compact looping is not a goal by itself.

## Standard project folder layout

Use this directory structure by default for the user's Stata projects unless the user explicitly specifies a different layout:

```text
project_root/
├── code/
├── data/
│   ├── original/
│   ├── output/
│   ├── temp/
│   └── work/
├── doc/
└── log/
```

Treat each folder as follows:

- `code/`: store Stata code files such as `.do` and `.ado` files.
- `data/original/`: store raw/original source data. Treat these files as read-only inputs; do not overwrite them during cleaning or analysis.
- `data/work/`: store datasets created from the original data and used for analysis. This includes cleaned files, merged masters, analysis-ready datasets, and the machine-readable datasets that underlie figures and tables.
- `data/temp/`: store temporary/scratch datasets that are intermediate, disposable, and safe to recreate.
- `data/output/`: store final human-facing figures and tables. Do not store the supporting `.dta`, `.csv`, or other data files used to generate those figures or tables here; keep those supporting datasets in `data/work/`.
- `doc/`: store project documentation such as data manuals, codebooks, questionnaires, technical notes, and other reference documents.
- `log/`: store Stata log files and other execution logs.

When useful, create subfolders under `data/output/` for final figures and tables, but keep the underlying analysis/output datasets in `data/work/`.

Prefer path globals that reflect this layout, for example:

```stata
global BaseFolder     "/path/to/project"
global CodeFolder     "${BaseFolder}/code"
global OriginalFolder "${BaseFolder}/data/original"
global OutputFolder   "${BaseFolder}/data/output"
global TempFolder     "${BaseFolder}/data/temp"
global WorkFolder     "${BaseFolder}/data/work"
global DocFolder      "${BaseFolder}/doc"
global LogFolder      "${BaseFolder}/log"
```

Do not create alternative top-level folders such as `results/`, `figures/`, `tables/`, or `processed/` unless the user explicitly asks for a different structure. Put final figures/tables under `data/output/`, and put processed/analysis/supporting datasets under `data/work/`.

## Master-driven modular workflow

Use one master do-file as the normal entry point for the project. Keep each substantive stage in a separate numbered do-file and let the master call them in execution order.

A typical structure is:

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

The exact names may vary by project, but keep the following principles:

- `00_master.do` sets paths/globals, creates required folders, defines rebuild/run switches, opens the main workflow, and calls the stage files.
- Keep cleaning, merging, variable construction, descriptives, figures, regressions, robustness, and mechanisms in separate files when they are substantively distinct.
- Use ordered numeric prefixes when execution order matters.
- Run the full project from the master rather than manually executing many files in an ad hoc order.
- Subordinate do-files should use the project globals established by the master and should not change the working directory with repeated `cd` commands.
- Do not duplicate path definitions across every do-file unless a small fallback is intentionally included for standalone debugging.
- Use rebuild switches or cached work datasets when upstream construction has not changed, so downstream analysis can be rerun without rebuilding raw-data stages.

## Do-file purpose, inputs, outputs, and code comments

Start every substantive `.do` file with a concise header that makes the file understandable without reading the entire script. State at least:

- what the do-file does and why it exists;
- the main input dataset(s) or file(s);
- the main output dataset(s), table(s), or figure(s);
- the unit of observation of the principal input/output data when relevant;
- the key or panel structure when relevant.

Use a header pattern such as:

```stata
*===============================================================================
* File:    04_construct_analysis_variables.do
* Purpose: Construct the analysis sample and the health, insurance, education,
*          treatment, transition, and outcome variables used downstream.
*
* Inputs:
*   ${WorkFolder}/sipp2008_core_topical_master.dta
*
* Outputs:
*   ${WorkFolder}/sipp2008_analysis_master.dta
*
* Unit of observation:
*   Person-month
*
* Key / panel order:
*   lgtkey ym
*===============================================================================
```

Keep the description factual and update it when the file's responsibilities change. Do not leave stale headers.

Within the do-file, add short comments before substantial blocks so a reader can quickly see what each section is doing. Explain the statistical or data-flow purpose, the relevant sample or grouping when material, and why a non-obvious implementation is used. Comment generously enough that the code can be audited section by section, but do not comment every trivial line or merely restate Stata syntax.

In `00_master.do`, add a short purpose comment near each `do` call. When useful, also note the principal input and output so the master provides a high-level map of the pipeline.

## Prefer bulk operations

Prefer Stata commands that process many observations or groups in one pass, including:

- `collapse`
- `egen`
- `bysort`
- `reshape`
- `merge`
- `append`
- direct `generate` / `replace`

For grouped descriptive statistics, prefer one explicit `collapse ..., by(...)` block over nested loops that repeatedly call `summarize`, `count`, `mean`, or similar commands on the full dataset.

When several subgroup outputs are needed, write separate explicit blocks when useful. For example, write separate blocks for overall, sex, race, health, and age-group summaries rather than wrapping them in one generic `foreach` if the explicit version is at least as fast and easier to audit.

## Avoid loops by default

Do not use `foreach` or `forvalues` merely to make code shorter.

Avoid patterns such as:

```stata
foreach y of local outcomes {
    foreach w of local waves {
        foreach a in 1 2 {
            foreach g of local groups {
                quietly summarize `y' [aw=weight] if ...
            }
        }
    }
}
```

This pattern repeatedly rescans the same large dataset and should normally be replaced by a grouped bulk operation such as:

```stata
collapse (mean) mean_y1=y1 mean_y2=y2 [aw=weight], ///
    by(swave age_group group)
```

It is acceptable to repeat similar `collapse` blocks for different samples or grouping variables.

Retain a loop only when at least one of these is true:

- the loop is technically necessary for a dynamic operation;
- explicit repetition would materially increase the chance of a correctness error;
- the loop only performs cheap metadata/validation work and does not repeatedly scan a large dataset;
- the number of iterations is small and the runtime cost is negligible.

When a non-obvious loop remains, add a short comment explaining why it is retained.

## Reduce data early

Shrink large datasets as early as is statistically safe.

Prefer selective loading when the raw or work dataset is wide:

```stata
use lgtkey swave age_group college_enroll analysis_weight ///
    using "${WorkFolder}/analysis_master.dta", clear
```

rather than loading hundreds of unused variables and carrying them through the full do-file.

Also reduce observations early with `keep if` when the restriction is part of the intended analysis sample and no excluded observations are still needed to construct lags, leads, baselines, transitions, or person-level variables.

Rules:

- Load only required variables from wide raw files when practical.
- Drop unused variables after construction steps that need them are complete.
- Restrict to the analysis sample early only after confirming the restriction cannot alter person-level or longitudinal construction.
- For panel transitions, baselines, lags, leads, or future outcomes, construct the longitudinal variable before dropping observations that are needed to define it.

## Minimize large-data I/O

Avoid repeatedly loading, saving, merging, or appending a large master dataset.

Prefer to:

- prepare small extracts first;
- append small extracts before merging them into a large master;
- perform one large merge instead of several sequential large-master merges;
- append several files in one operation rather than repeatedly growing a large in-memory dataset;
- reuse cached analysis files when upstream construction has not changed.

Respect the folder semantics when doing this:

- read source files from `data/original/`;
- write cleaned/merged/analysis datasets to `data/work/`;
- use `data/temp/` only for disposable intermediates;
- write final figures/tables to `data/output/`;
- write logs to `log/`.

## Avoid expensive preserve/restore patterns

`preserve`/`restore` is acceptable for a small number of clear transformation blocks, but do not put repeated large-data `preserve`/`restore` operations inside nested or high-iteration loops.

Prefer explicit blocks such as:

```stata
* Sample A
preserve
    keep if sample_a == 1
    collapse ..., by(...)
    save "${WorkFolder}/sample_a_summary.dta", replace
restore

* Sample B
preserve
    keep if sample_b == 1
    collapse ..., by(...)
    save "${WorkFolder}/sample_b_summary.dta", replace
restore
```

rather than looping over samples and repeatedly preserving, filtering, summarizing, and restoring the full master.

If an intermediate collapsed dataset is reused across stages, save it once in `data/work/` or, if truly disposable, `data/temp/`, instead of reconstructing it repeatedly.

## Distinguish tempfile, data/temp, and data/work

Use storage according to lifetime and reuse:

- Stata `tempfile`: use for intermediates needed only within the current do-file/session. These should disappear automatically and do not need to be inspected later.
- `data/temp/`: use for disposable intermediate files that may need to survive across do-files, survive an interrupted run, or be inspected during debugging. They must be safe to delete and regenerate.
- `data/work/`: use for meaningful cleaned, merged, analysis-ready, cached, or supporting datasets that are expected to be reused or that underlie final figures/tables.
- `data/output/`: use only for final human-facing figures and tables, not their machine-readable source data.

Do not use `data/temp/` as a catch-all replacement for `data/work/`. If downstream analysis depends on the file as a stable input, it belongs in `data/work/`.

## Default figure and table outputs

Use output formats that are convenient for the user's current research workflow.

- Generate preliminary and review figures as `.png` by default. PNG is preferred at the exploratory stage because figures can be browsed and scrolled through quickly. Do not switch preliminary figures to PDF/EPS merely because those formats are common for publication.
- Generate tables in a Word-readable format by default, preferably `.docx`. Use Stata's Word-output facilities such as `putdocx` when appropriate. Use legacy `.doc` only when the user specifically needs it or when an existing workflow requires it.
- Save final human-facing figure files under `data/output/` (for example `data/output/figures/figure_1.png`).
- Save final human-facing table files under `data/output/` (for example `data/output/tables/table_1.docx`).
- Save the machine-readable data that underlie figures and tables in `data/work/`, not in `data/output/`.
- If a figure or table later moves to publication stage, change the export format only when the publication workflow requires it or the user asks for it.

Do not treat `.csv` or `.dta` files as the final human-facing table merely because they are easy to export; they are supporting data products and belong in `data/work/` unless the user explicitly requests otherwise.

## HTML result-review reports

When the user asks for an HTML review or interpretation of Stata figures/results, produce a research-oriented report rather than a simple image gallery.

**Benchmark requirement:** treat the project's designated reference figure-review HTML as the canonical interaction and layout benchmark. For these reports, read `references/figure-review-html-benchmark.md` and use `assets/figure-review-template.html` as the default structural template. Preserve its section navigation, sticky search/filter toolbar, visible-count indicator, score threshold filter, expand/collapse controls, native `<details>` figure cards collapsed by default, hash-target auto-open behavior, duplicate cross-links, and project-relative source paths unless the user explicitly asks for a different format.

- Generate two self-contained HTML files by default for this project: a Chinese version for the user and an English version suitable for collaborators or supervisors. Keep the figure order, numeric results, ratings, and substantive conclusions aligned across the two versions.
- Begin with a concise synthesis of the overall empirical story, including results that support the proposed mechanism and results that weaken, contradict, or qualify it. Do not cherry-pick favorable figures.
- For **every figure**, show all of the following visibly next to the figure:
  1. **Importance rating (1-5)**, where 5 is central paper evidence and 1 is normally safe to omit.
  2. **Figure meaning**: what is plotted, including the outcome, sample/grouping, time unit, and denominator when relevant.
  3. **Facts in the figure**: the main observed levels, trends, gaps, reversals, or support counts. Use exact values from tables/source data when available; label visual readings as approximate.
  4. **Role in the paper story**: whether the figure establishes motivation, first stage, main education result, health heterogeneity, mechanism, robustness, measurement validity, sample support, or background.
  5. **Interpretation boundary**: what the figure does **not** establish, including causal limits, small-cell support, weighting/denominator issues, recall windows, seasonality, attrition/aging-out, measurement definitions, or duplication with another figure.
- If a figure is a duplicate or near-duplicate of another output, say so explicitly and do not count it as independent evidence.
- Keep descriptive figures distinct from regression evidence. Do not describe a raw trend or raw Pre/Post comparison as a causal effect.
- When sample support is thin, report the relevant unique-person/event counts alongside the figure rather than hiding the point with an arbitrary minimum-N rule.
- Prefer embedded images so each HTML file can be opened as a standalone document without external file paths.
- Number every figure review item sequentially with a stable three-digit identifier (`001`, `002`, `003`, ...). Use the same figure number in the Chinese and English reports. Unless the user specifies another order, number figures in report display order, preserving the project folder order and then filename order within each folder.
- In each figure header, display the items in this order: **importance score**, **three-digit figure number**, **filename**, then the short role/priority caption. Example: `4/5   093   hh_unmet_care_by_age_wave.png`.
- At the very bottom of every figure card, show the figure's exact project-relative location in monospace. Use the compact path form used by the project review pages, for example `figures/06_topical/hh_unmet_care_by_age_wave.png`. Do not replace this with an absolute machine path. Do not invent a path when the source location is unknown.
- Keep the per-figure layout consistent with the established review format, in this exact vertical order: **(1)** header with importance score, three-digit number, filename, and short role/priority caption; **(2)** the four explanatory fields — Figure meaning, Facts in the figure, Role in the paper story, Interpretation boundary — placed **above the image**; **(3)** the figure image; **(4)** the project-relative source path at the very bottom. Do not place the explanatory fields below the image unless the user explicitly asks for a different layout.

## Fail fast and validate structural assumptions

Prefer explicit checks that stop the pipeline near the source of an error rather than allowing silent corruption to propagate downstream.

Before or after important transformations, use appropriate checks such as:

```stata
confirm file "${OriginalFolder}/source.dta"
confirm variable lgtkey swave analysis_weight
isid lgtkey swave
assert inlist(binary_var, 0, 1, .)
```

For merges:

- verify the intended key structure with `isid` on the using dataset when appropriate;
- inspect `_merge` immediately after the merge;
- `assert` or explicitly check which merge statuses are allowed before dropping `_merge`;
- treat unexpected using-only rows, duplicate keys, or update conflicts as errors unless the research design explicitly permits them.

Do not write:

```stata
merge ...
drop _merge
```

without first validating that the merge behaved as intended.

For constructed variables, validate important invariants such as:

- binary/range restrictions;
- mutually exclusive categories;
- date/wave ordering;
- person-wave or person-month uniqueness;
- expected observation/person counts when known;
- transition logic and risk-set restrictions.

Use `capture` only when an error is genuinely expected and handled. Do not blanket-wrap important data construction in `capture` merely to keep the do-file running. When `capture` is used, inspect `_rc` and fail with an informative message if the condition is not the expected one.

## Preserve weighted-statistics semantics

Do not trade statistical correctness for speed.

When a table needs weighted means but unweighted nonmissing observation counts, construct explicit nonmissing indicators and use a bulk pattern such as:

```stata
gen byte n_y = !missing(y)
collapse (mean) mean_y=y (rawsum) n_y [aw=analysis_weight], ///
    by(group1 group2)
```

Check that an optimization does not silently change:

- the analysis sample;
- eligibility or treatment timing;
- health or education definitions;
- risk-set definitions;
- missing-value handling;
- weighting;
- observation/person denominators;
- transition or event timing.

## Reproducible execution

Write do-files so the project can be rerun later on another machine with the same intended inputs.

Default practices:

- Start substantive do-files with the intended Stata `version` and `set more off`.
- Keep machine-specific absolute paths confined to the master/configuration layer; use project globals elsewhere.
- Set and document a fixed seed before any random sampling, simulation, bootstrap setup, random tie-breaking, or other stochastic operation that depends on a seed.
- Open logs in `log/` with stable, descriptive names. Use named logs when multiple logs may coexist.
- For order-sensitive panel construction, explicitly sort on the full required key/order variables before using lag/lead logic and assert uniqueness when the design requires it.
- Avoid relying on undocumented current sort order, working directory, or state left by a previously run do-file.
- Keep generated work datasets deterministic given the same source data, code, settings, and seeds.

## Comment explicit blocks

Add comments before substantial transformations. Comments should state what the block computes, which sample it uses, what it groups by, where the result is saved, and why the implementation is structured that way when performance matters.

Prefer comments about statistical intent and data flow over comments that merely paraphrase Stata syntax.

Example:

```stata
* Sex-specific weighted wave trends.
* One collapse computes every requested outcome by wave x age group x sex,
* avoiding repeated full-data summarize calls. The collapsed dataset is saved
* in data/work because it is the data source for a final table/figure.
preserve
    keep if sample_core == 1 & !missing(female, analysis_weight)
    collapse ... [aw=analysis_weight], by(swave age_group female)
    save "${WorkFolder}/sex_wave_trends.dta", replace
restore
```

## Review existing code for performance and reliability

When reviewing Stata code, actively look for:

- nested loops containing `summarize`, `count`, `regress`, `preserve`, `use`, `save`, `merge`, or `append`;
- repeated scans over the same large person-month dataset;
- repeated large-master I/O;
- generic helper programs whose abstraction causes many small data passes;
- code that can be replaced by one or a few grouped `collapse` operations;
- datasets being written to `data/output/` when they should be in `data/work/`;
- large files loaded with many unused variables;
- analysis restrictions applied too late when they could safely be applied earlier;
- `preserve`/`restore` inside expensive loops;
- merges whose `_merge` results are not validated;
- important `capture` statements that hide unexpected errors;
- longitudinal code that depends on an implicit or unstable sort order.

Do not mechanically remove every loop. Focus first on loops whose bodies perform expensive data operations. If a loop is harmless, say so rather than rewriting it only for appearance.

## Regression code

Do not replace substantively distinct regression specifications with `collapse`; estimation commands must preserve the intended model.

Keep regression-specific specification definitions inside the regression do-file rather than in `00_master.do`. At the beginning of `06_regression_analysis.do`, define shared control sets, fixed-effect sets, clustering variables, common estimation samples, or other repeated regression ingredients in clearly named local macros when doing so improves consistency. For example:

```stata
* Common regression specifications used in this file only.
local controls_main     "female married parent_coreside"
local controls_income   "family_income_month poverty_ratio"
local fixed_effects     "i.calendar_year i.calendar_month"
local cluster_var       "lgtkey"
```

Use these locals only for ingredients that are genuinely common across specifications. Keep substantively different robustness specifications explicit rather than hiding meaningful differences behind overly generic macros or programs. Do not move these regression-specific definitions into the master file merely to avoid repetition.

If robustness or mechanism files need their own common specification sets, define them locally in those files rather than turning the master into a repository of regression details.

For many repeated regressions, avoid unnecessary output rendering when results are posted or stored programmatically. Use quiet execution where appropriate and add coarse progress messages so the user can see that Stata is still running.

If repeated regression specifications can be written explicitly without making correctness worse, prefer explicit blocks. If a loop is materially safer for a systematic specification grid, retain it and explain why.

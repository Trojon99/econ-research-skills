# Project Structure and Orchestration

## Contents
1. Stable folder layout
2. Single entrypoint
3. Module boundaries
4. Multi-language projects
5. Documentation and outputs

## 1. Stable folder layout

Use this structure by default:

```text
project_root/
├── code/
├── data/
│   ├── original/
│   ├── work/
│   ├── temp/
│   └── output/
├── doc/
└── log/
```

The folder meanings are a project contract, not language-specific conventions.

- `code/`: executable research logic.
- `data/original/`: immutable source data.
- `data/work/`: reproducible research data products and reusable caches.
- `data/temp/`: disposable scratch files.
- `data/output/`: final human-facing artifacts.
- `doc/`: manuals, codebooks, questionnaires, research notes, technical documentation.
- `log/`: run logs and diagnostics.

Do not overwrite `data/original/`. Do not place final human-facing outputs in `data/work/`. Do not place machine-readable analysis datasets in `data/output/` merely because they are generated late in the pipeline.

## 2. Single entrypoint

A project should have one normal entrypoint that makes the intended execution order obvious.

Examples:

- Stata: `00_master.do`
- Python: `run_pipeline.py`
- R: `run_pipeline.R`
- Julia: `run_pipeline.jl`

The entrypoint should remain thin. Typical responsibilities:

- configure project-relative paths;
- define coarse run/rebuild switches;
- create missing required directories;
- initialize logging;
- call substantive stages in dependency order;
- report completion/failure clearly.

Do not put detailed regression grids, model equations, or extensive transformation logic into the entrypoint.

## 3. Module boundaries

Split code when a stage has distinct inputs/outputs or a distinct research responsibility. A useful default sequence is:

```text
00 entrypoint/config
01 source cleaning
02 core master/model input construction
03 auxiliary merges/modules
04 analysis variables/sample/model objects
05 descriptives/figures
06 main estimation/model solution
07 robustness/validation
08 mechanisms/heterogeneity/counterfactuals
```

The exact names should follow the project. Do not create empty ceremonial stages.

Each substantive module should expose enough metadata to audit:

- purpose;
- principal input(s);
- principal output(s);
- observation/model unit;
- key/index structure;
- important dependencies.

## 4. Multi-language projects

Keep the top-level folder contract stable. If several languages are genuinely used, organize `code/` only as much as needed, for example:

```text
code/
├── stata/
├── python/
└── julia/
```

or keep ordered cross-language modules in one `code/` directory if that is easier to follow.

Choose orchestration according to actual complexity. Do not add Make/Snakemake/containers solely because the project is multi-language. Add a workflow manager only when explicit dependency tracking, incremental rebuilding, or cross-language execution is difficult to maintain with a simple driver.

Cross-language handoffs should use stable files or clearly documented interfaces. Record the producing stage, consuming stage, file format, keys/index, and semantic meaning.

## 5. Documentation and outputs

Keep documentation that explains external data or project conventions in `doc/`. Keep code comments near the implementation when they explain a local non-obvious choice.

Final figures/tables/reports belong under `data/output/`. Their machine-readable source datasets belong under `data/work/` when retaining them materially improves reproducibility or auditability.

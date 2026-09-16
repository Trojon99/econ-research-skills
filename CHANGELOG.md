# Changelog

This repository is actively maintained. Significant changes to skill behavior, routing, methodology coverage, or repository structure are recorded here.

The project follows a lightweight Semantic Versioning convention:

- **MAJOR**: breaking changes to skill names, interfaces, or core workflow assumptions.
- **MINOR**: new skills, substantial new methodological modules, or meaningful capability expansions.
- **PATCH**: bug fixes, documentation corrections, routing refinements, and non-breaking maintenance.

## [0.2.1] - 2026-09-16

Maintenance and synchronization patch.

### Fixed
- Fixed invalid YAML frontmatter in `stata-project-workflow` by quoting the long trigger description so the skill passes the official validator.
- Kept the public Stata workflow generic by referring to the project-designated review benchmark and to collaborators/supervisors rather than project-specific filenames or people.

### Synchronized
- Confirmed `econ-research-design`, `causal-inference`, `econ-descriptive-analysis`, and `econ-paper-writer` are aligned between GitHub and the current ChatGPT skill set.
- Confirmed the GitHub `seminar-companion` includes method routing to causal inference, preference elicitation, descriptive analysis, Stata workflow, and paper writing; the matching validated package is used for ChatGPT-side update.
- GitHub `main` remains the source of truth.

## [0.2.0] - 2026-09-16

First formally versioned release.

### Added
- Added a comprehensive preference-elicitation reference to `econ-research-design`, covering DCE/conjoint analysis, BWS, WTP/WTA, TTO, standard gamble, health-state valuation, preference/scale heterogeneity, validity, and interpretation boundaries.
- Added explicit preference-elicitation routing to `econ-research-design`.
- Added repository-level version and maintenance metadata.

### Changed
- Clarified the intended division of labor across research design, causal inference, descriptive analysis, Stata workflow, paper writing, and seminar support.
- Began standardizing skill metadata and trigger descriptions under the current ChatGPT Skills format.

### Maintenance
- GitHub `main` is the source of truth for the maintained skill library.
- Methodological references are treated as updateable snapshots rather than a frozen canon; current guidance should be re-verified when recency matters.

## Pre-versioning

Before `v0.2.0`, the repository was developed iteratively without formal release numbers. Earlier commits remain available in Git history, but no retrospective semantic-version labels are assigned to them.

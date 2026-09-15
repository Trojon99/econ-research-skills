# Overleaf Conventions

Use these conventions for a complete economics paper, research proposal, or Overleaf project. For a short prose fragment, preserve the surrounding source instead.

## Template precedence

- Treat the user's uploaded `main.tex` or other designated LaTeX template as authoritative. Rewrite inside it while preserving its document class, preamble, package order, page geometry, spacing, title and author construction, custom commands, bibliography system, and other project conventions.
- Do not substitute another template, bibliography system, or package set merely from preference. Add a package only when the requested content requires it and the existing project does not already supply the capability.
- Treat a paper identified as reference-only as evidence or a rhetorical model. Do not modify it, copy its author list into the target, or infer target authorship from it.
- Preserve the author's chosen title, authorship, affiliation, acknowledgements, and draft notice unless the user requests a change.

## Default house format

When the user requests the established Overleaf format but no template is available in the current turn, use this baseline:

```latex
\documentclass[12pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{setspace}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}
\usepackage{natbib}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}
\usepackage{authblk}
\usepackage{indentfirst}

\onehalfspacing
```

Use the user's supplied title and author block. Do not add coauthors from reference papers.

## Source layout

- Put each natural-language paragraph on one physical source line and separate paragraphs with one blank line. Do not hard-wrap prose for visual width.
- Split preamble settings, displayed equations, alignments, tables, lists, bibliography entries, and other syntax-sensitive environments across lines as needed for valid and readable LaTeX.
- Do not place the research question in a `quote` environment unless the user explicitly asks for it.
- Keep an economics-paper Introduction as continuous prose without internal subsection headings when that is the user's established convention.
- Do not add `\label` commands to subsections unless the user explicitly asks for subsection cross-references. Section, equation, figure, and table labels remain permissible when required.

## Compatibility and validation

- Use standard Overleaf-compatible packages and compile the complete project before delivery.
- Preserve one bibliography workflow consistently. Never mix manual `thebibliography`, BibTeX, and `biblatex` without an explicit migration request.
- Check for unresolved citations and references, overfull boxes, malformed metadata, missing assets, and package-specific compilation failures.
- Render the compiled PDF and visually inspect every page before delivery when layout matters.
